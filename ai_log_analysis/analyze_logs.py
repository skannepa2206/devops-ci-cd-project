import re
import os


def analyze_logs(log_file):
    """Reads logs and summarizes issues using regex patterns instead of NLP."""
    try:
        with open(log_file, "r") as file:
            logs = file.read()

        # Extract Errors & Warnings
        error_lines = re.findall(r"ERROR: (.+)", logs)
        warning_lines = re.findall(r"WARNING: (.+)", logs)

        # Simple summary without using spaCy
        error_summary = ". ".join(error_lines[:3])  # First 3 errors
        warning_summary = ". ".join(warning_lines[:3])  # First 3 warnings

        summary = f"Found issues: {error_summary}. {warning_summary}"
        if len(error_summary) + len(warning_summary) == 0:
            summary = "No significant issues found."

        return f"Deployment Log Summary:\nErrors: {len(error_lines)}\nWarnings: {len(warning_lines)}\nSummary: {summary}"

    except Exception as e:
        return f"❌ Error analyzing logs: {str(e)}"


if __name__ == "__main__":
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_file = os.path.join(script_dir, "deployment_logs.txt")

    # Ensure the log file exists
    if not os.path.exists(log_file):
        with open(log_file, "w") as f:
            f.write("INFO: Application started\nWARNING: High memory usage\nERROR: Failed to connect to database\n")

    # Run log analysis
    print(analyze_logs(log_file))