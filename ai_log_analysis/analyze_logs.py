import re
import os


def analyze_logs(log_file):
    """Reads logs and summarizes issues using regex patterns."""
    try:
        # Handle different encodings
        try:
            with open(log_file, "r", encoding="utf-8") as file:
                logs = file.read()
        except UnicodeDecodeError:
            with open(log_file, "r", encoding="latin-1") as file:
                logs = file.read()

        # Extract Errors & Warnings
        error_lines = re.findall(r"ERROR: (.+)", logs)
        warning_lines = re.findall(r"WARNING: (.+)", logs)

        # Create summary
        error_summary = ". ".join(error_lines[:3]) if error_lines else "No errors found"
        warning_summary = ". ".join(warning_lines[:3]) if warning_lines else "No warnings found"

        return f"Deployment Log Summary:\nErrors: {len(error_lines)}\nWarnings: {len(warning_lines)}\nSummary: {error_summary}. {warning_summary}"

    except Exception as e:
        return f"❌ Error analyzing logs: {str(e)}"


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_file = os.path.join(script_dir, "deployment_logs.txt")

    # Create a sample log file if it doesn't exist
    if not os.path.exists(log_file):
        with open(log_file, "w", encoding="utf-8") as f:
            f.write("INFO: Application started\nWARNING: High memory usage\nERROR: Failed to connect to database\n")

    # Run analysis
    print(analyze_logs(log_file))