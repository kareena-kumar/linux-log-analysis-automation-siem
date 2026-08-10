# log_analysis.py

from pathlib import Path

# Step 1: Open and read log file
log_file = Path(__file__).parent / "Linux_2k.log"

with open(log_file, "r", encoding="utf-8") as file:
    logs = file.readlines()

# Step 2: Focus on lines 50–500
subset_logs = logs[49:500] # Python is 0-based index

# Step 3: Search for suspicious patterns
suspicious_entries = []
for line in subset_logs:
    if "Failed password" in line:
        suspicious_entries.append(("Failed Login", line.strip()))
    elif "authentication failure" in line:
        suspicious_entries.append(("Auth Failure", line.strip()))
    elif "user unknown" in line or "invalid user" in line:
        suspicious_entries.append(("Unknown User", line.strip()))

# Step 4: Print Results
print("=== Suspicious Log Entries (Lines 50–500) ===")
for entry_type, entry in suspicious_entries:
    print(f"[{entry_type}] {entry}")

print(f"\nTotal suspicious entries found:{len(suspicious_entries)}")