# Interview Transcript Summarizer

This project was built as part of the AI Systems Intern take-home assignment for intervue.io.
The application takes an interview transcript as input and generates a structured summary containing:
- Topics Covered
- Candidate Profile
- Candidate Summary

The main focus of this assignment was prompt design, structured output generation, and handling different interview styles effectively.

---

# Tech Stack

- Python
- Groq API
- Llama 3.1 8B Instant
- python-dotenv

---

# Project Files

- `summarizer.py` → Main script used for transcript summarization
- `prompt_iterations.md` → Prompt testing and improvement process
- `README.md` → Project documentation
- `kk.txt` → Sample interview transcript file

---

# Setup Instructions

## Install Dependencies

```bash
pip install groq python-dotenv
```

---

## Add API Key

Create a `.env` file in the project directory and add:

```env
API_KEY=your_api_key_here
```

---

## Run the Project

```bash
python summarizer.py kk.txt
```

---

# Output

The script generates:
- Key discussion topics from the interview
- Suitable candidate profile/role
- Short professional candidate evaluation with hiring signal

---

# Model Used

- Provider: Groq
- Model: llama-3.1-8b-instant


# Reflection

While working on this assignment, I found that prompt structure played a much bigger role than the model itself. The earlier versions of the prompt produced outputs that were either too generic or inconsistent across different transcripts.

To improve the results, I refined the instructions to make the summaries more structured, concise, and evaluation-focused. I also added stricter formatting guidance to reduce repetition and improve clarity.

Testing the prompt on different transcript styles helped improve consistency and made the final output more reliable. With more time, I would further improve the evaluation logic by adding scoring, better role matching, and support for multiple transcript formats.
