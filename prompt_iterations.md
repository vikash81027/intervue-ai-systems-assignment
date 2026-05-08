# Prompt Iterations

## Iteration 1

### Prompt
Create a summary of the interview transcript and identify the candidate profile.

### Input
A raw interview transcript containing technical discussion, project experience, and problem-solving questions.

### Output
The model generated a general summary with mixed formatting. Important technical points were sometimes skipped, and the role identification was too generic.

### What Worked
- Basic summarization worked correctly
- Main interview flow was understood by the model

### What Didn’t Work
- Output structure was inconsistent
- Important details were missed
- Candidate profile was too broad and not role-specific

### Changes Made for Next Iteration
I introduced separate sections for topics, profile evaluation, and candidate summary to improve clarity and consistency.

---

## Iteration 2

### Prompt
Analyze the interview transcript and return output in three sections:
1. Topics Covered
2. Candidate Profile
3. Candidate Summary

Keep the response concise and professional.

### Input
Transcript containing frontend development, Ionic framework, Angular, performance optimization, and AI-assisted development discussions.

### Output
The response became more structured and easier to read. The model identified technical skills more accurately, but some outputs were still repetitive and overly descriptive.

### What Worked
- Better formatting and readability
- Improved role identification
- More relevant technical summaries

### What Didn’t Work
- Some repetition in summaries
- Inconsistent detail level across transcripts
- Outputs occasionally became too long

### Changes Made for Next Iteration
I added stricter formatting rules, topic limits, sentence limits, and instructions to avoid repetition and generic explanations.

---

## Iteration 3 (Final)

### Prompt
Analyze the interview transcript and generate a structured evaluation with:
- Topics Covered
- Candidate Profile
- Candidate Summary

Rules:
- Keep output concise and evaluation-focused
- Avoid repetition
- Use precise role naming
- Limit topics to key discussion points only
- Add a hiring signal
- Make reasonable assumptions if transcript is incomplete

### Input
Different interview transcript styles including technical discussions, architecture design, frontend development, AI-assisted workflows, and communication-based evaluation.

### Output
The final version produced clean, structured, and more consistent outputs across different transcript types. The summaries became more professional, concise, and closer to real interviewer evaluations.

### What Worked
- Consistent formatting
- Better role matching
- Reduced repetition
- More readable and practical summaries

### Final Observation
The final prompt performed much better because the instructions were more specific and constrained. Adding clear formatting rules and evaluation-focused guidance improved both consistency and overall output quality.
