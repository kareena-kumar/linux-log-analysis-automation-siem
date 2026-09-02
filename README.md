# Linux Log Analysis, Automation & SIEM Visualisation
![Status: Completed](https://img.shields.io/badge/Status-Completed-brightgreen)
![Difficulty: ★★☆☆☆](https://img.shields.io/badge/Difficulty-%E2%98%85%E2%98%85%E2%98%86%E2%98%86%E2%98%86-yellow)
[![Time Spent: 16h](https://img.shields.io/badge/Time%20Spent-16h-orange)]()

> A cybersecurity project demonstrating **SOC analyst workflows** through manual Linux log investigation, Python automation, and Splunk SIEM analysis.

---

## Overview

This repository documents my end-to-end cybersecurity project demonstrating core SOC analyst workflows. In this project, I investigated Linux authentication logs using three complementary approaches:  

1. **Manual log analysis**
2. **Python script automation** and
3. **Splunk SIEM visualisation**

Using a publicly available Linux authentication dataset from **LogHub**, I identified repeated SSH brute-force attempts, extracted Indicators of Compromise (IoCs), automated suspicious event detection using Python, and built visual attack dashboards in Splunk Enterprise.

---

## Technologies Used

| Technology | Purpose |
| --------- | ----------- |
| **Python**  | Automated Linux log analysis and exported suspicious events to CSV  |
| **Splunk Enterprise**  | SIEM analysis, event correlation, and authentication log investigation  |
| **Linux Authentication Logs**   | Investigated SSH authentication failures and brute-force activity  |
| **Git & GitHub**   | Version control, documentation, and project management   |
| **CSV**  | Structured export of suspicious authentication events for reporting  |

---

## Skills Demonstrated

* **Linux log analysis**
* **SSH authentication investigation**
* **Python automation**
* **Splunk Enterprise**
* **SIEM monitoring**
* **Threat detection**
* **Indicator of Compromise (IoC) identification**
* **Incident investigation and reporting**

---

## Project Structure

```text
linux-log-analysis-automation-siem/
│
├── src/
│   └── log_analysis.py
│
├── reports/
│   ├── project_report.pdf
│   └── suspicious_log_entries.csv
│
├── sample-data/
│   └── README.md
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# Stage 1 – Manual Log Analysis

In the first phase of this project, I manually reviewed raw Linux authentication logs to uncover suspicious activity and identify potential security threats.

## Key Findings

* **Brute-Force Detection:** I uncovered a high-volume, automated SSH brute-force attack.
* **Target Accounts:** I observed repeated failed login attempts targeting both the `root` administrative account and various non-existent usernames.
* **Origin:** I verified that multiple malicious authentication attempts originated from external IP addresses.

### Primary Indicators of Compromise

* **IP Address:** `218.188.2.4`
* **Hostname:** `220-135-151-1.hinet-ip.hinet.net`

## Recommended Actions

Based on my findings during the manual investigation, I recommended the following controls:
1. Block identified malicious IP addresses at the firewall level.
2. Implement automated authentication rate limiting.
3. Deploy host-based intrusion prevention tools such as **Fail2Ban** - monitors system logs for repeated failed login attempts and temporarily blocks the offending IP addresses using firewall rules. 
5. Set up persistent log monitoring for repeated failed login patterns.

---

# Stage 2 – Python Automation

To streamline the investigation process, I wrote a custom Python script (`src/log_analysis.py`) to automate pattern detection across large log files.

## Detection Features

The script identifies:

* Failed password attempts
* General authentication failures
* Invalid user login attempts

Once parsed, the script automatically exports all detected events into a structured CSV file (`reports/suspicious_log_entries.csv`).

## Result

> **607 suspicious authentication events detected**

This demonstrates how scripting can reduce the time required to manually identify suspicious activity within large log files.

---

# Stage 3 – Splunk SIEM Analysis

In the final stage, I ingested the Linux authentication dataset into **Splunk Enterprise** to simulate a real-world Security Operations Centre (SOC) monitoring workflow.

Using Splunk, I:
* Created targeted Search Processing Language (SPL) queries to filter authentication events.
* Aggregated security events by source IP and targeted usernames.
* Correlated short bursts of failed logins to confirm automated brute-force behaviour.

## Example SPL Query

```spl
index="linux_logs" source="Linux_2k.log"
("Failed password" OR "authentication failure" OR "invalid user" OR "user unknown")
| stats count by rhost user
| sort -count
```

## Key Findings

* **607 authentication-related events** were identified.
* **80 attempts** against the `root` account originated from `150.183.249.110`.
* **23 attempts** originated from `207.243.167.114`.
* Short bursts of repeated authentication attempts indicated **automated brute-force behaviour**.


---

# Key Outcomes

| Method                | Outcome                                                       |
| --------------------- | ------------------------------------------------------------- |
| **Manual Analysis**   | I manually identified the SSH brute-force attack vectors and extracted core IoCs.  |
| **Python Automation** | I automated log parsing to instantly catch 607 suspicious entries. |
| **Splunk SIEM**       | I aggregated all 607 events into structured visual dashboards and IP frequency counts. |

---

## Project Reflections & Takeaways

This project provided practical experience across the security monitoring lifecycle, from **raw log investigation and threat identification through to automated detection and SIEM-based visualisation**.

Key takeaways from this project include: 
* Hands-on experience investigating Linux authentication events.
* Translating manual detection steps into efficient Python scripts.
* Writing SPL queries in Splunk to aggregate and correlate threats.
* Documenting IoCs and technical findings for clear incident reporting.

---

## Project Scorecard

![Architecture: 3/5](https://img.shields.io/badge/Architecture-3/5-blue)
![Technical Depth: 4/5](https://img.shields.io/badge/Technical%20Depth-4/5-lightblue)
![Problem Solving: 4/5](https://img.shields.io/badge/Problem%20Solving-4/5-green)
![Documentation: 5/5](https://img.shields.io/badge/Documentation-5/5-brightgreen)
![Practical Relevance: 5/5](https://img.shields.io/badge/Relevance-5/5-purple)
![Difficulty: ★★☆☆☆](https://img.shields.io/badge/Difficulty-%E2%98%85%E2%98%85%E2%98%86%E2%98%86%E2%98%86-yellow)

### **Overall Score**
![Overall: 21/25](https://img.shields.io/badge/Overall-21/25-success)

---

# Dataset

This project uses the publicly available **Linux_2k.log** dataset from **LogHub**.

The original dataset can be found here:

**[LogHub – Linux Log Dataset](https://github.com/logpai/loghub/tree/master/Linux)**

The dataset is **not included in this repository**.

For instructions on obtaining and using the dataset, see:

```text
sample-data/README.md
```

> **Dataset attribution:** The Linux log dataset is provided by LogHub. This repository uses the dataset for educational and cybersecurity analysis purposes.
