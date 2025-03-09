import re
import spacy

# Load NLP Model
nlp = spacy.load("en_core_web_sm")

def analyze_logs(log_file):
    """Reads logs and summarizes issues using AI."""
    with open(log_file, "r") as file:
        logs = file.read()

    # Extract Errors & Warnings
    error_lines = re.findall(r"ERROR: (.+)", logs)
    warning_lines = re.findall(r"WARNING: (.+)", logs)

    # AI-Based Summary
    doc = nlp(" ".join(error_lines + warning_lines))
    summary = " ".join([sent.text for sent in list(doc.sents)[:5]])  # ✅ Fix applied

    return f"Deployment Log Summary:\nErrors: {len(error_lines)}\nWarnings: {len(warning_lines)}\nAI Summary: {summary}"

# Run AI Analysis
print(analyze_logs("deployment_logs.txt"))
