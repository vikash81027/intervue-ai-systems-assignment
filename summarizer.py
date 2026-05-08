import os
import sys
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def get_client():
    key=os.getenv("API_KEY")
    if not key:
        raise ValueError("API_KEY not found in .env")
    return Groq(api_key=key)

def read_file(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    with open(path,"r",encoding="utf-8") as f:
        return f.read()

def build_prompt(transcript):
    return f"""
You are an expert technical interviewer evaluating a candidate.

Analyze the interview transcript and produce a concise, structured evaluation.

Return output EXACTLY in this format:

1. Topics Covered:
- List ONLY 4 to 6 key topics (merge similar ideas, avoid redundancy)

2. Candidate Profile:
- Role: (be specific, e.g., "Senior Frontend Engineer (Angular/React + Ionic)")
- Justification: 2 to 3 concise lines based on experience, depth, and skills

3. Candidate Summary:
Write a single paragraph of 3 to 5 sentences that includes:
- experience level
- key strengths
- any gaps or concerns
- overall evaluation

End the paragraph with:
Hiring Signal: Strong Hire / Hire / No Hire

Strict Rules:
- Do NOT use markdown formatting (no **bold**, no headings styling)
- Keep output clean, plain text, and easy to read
- Do NOT exceed topic limit
- Avoid repetition
- Do NOT explain everything from transcript, summarize intelligently
- Be decisive and sound like a real interviewer (not descriptive, but evaluative)
- Prefer precise and specific role naming (avoid generic titles)

If the transcript is unclear or incomplete, make reasonable assumptions.

Transcript:
{transcript}
"""

def summarize(transcript):
    if os.path.exists("last_output.txt"):
        print("Using cached output...")
        with open("last_output.txt","r",encoding="utf-8") as f:
            return f.read()

    client=get_client()
    prompt=build_prompt(transcript)

    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}]
    )

    result=response.choices[0].message.content

    with open("last_output.txt","w",encoding="utf-8") as f:
        f.write(result)

    return result

if __name__=="__main__":
    if len(sys.argv)<2:
        print("Usage: python summarizer.py <file>")
        sys.exit(1)

    path=sys.argv[1]
    transcript=read_file(path)
    result=summarize(transcript)

    print("\n=== SUMMARY ===\n")
    print(result)