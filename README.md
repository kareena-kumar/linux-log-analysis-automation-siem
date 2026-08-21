# Linux Log Analysis, Automation & SIEM Visualisation

> A cybersecurity project demonstrating **SOC analyst workflows** through manual Linux log investigation, Python automation, and Splunk SIEM analysis.

---

## Overview

This project demonstrates how a **Security Operations Centre (SOC) analyst** can investigate Linux authentication logs using three complementary approaches:

1. **Manual log investigation**
2. **Python automation**
3. **Splunk SIEM analysis and visualisation**

Using a publicly available Linux authentication dataset from **LogHub**, the project identifies repeated SSH brute-force attempts, extracts **Indicators of Compromise (IoCs)**, automates suspicious-event detection using Python, and visualises attack patterns using **Splunk Enterprise**.

---

## Technologies Used

| Technology                          | Purpose                                                                  |
| ----------------------------------- | ------------------------------------------------------------------------ |
| **Python**                          | Automated Linux log analysis and exported suspicious events to CSV       |
| **Splunk Enterprise**               | SIEM analysis, event correlation, and authentication log investigation   |
| **Linux Authentication Logs**       | Investigated SSH authentication failures and brute-force activity        |
| **Git & GitHub**                    | Version control, documentation, and project management                   |
| **CSV**                             | Structured export of suspicious authentication events for reporting      |

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
├── screenshots/
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

The first stage involved manually reviewing raw Linux authentication logs to identify suspicious authentication activity and potential indicators of compromise.

## Key Findings

* Identified a **high-volume, automated SSH brute-force attack**.
* Repeated failed login attempts targeted both the `root` account and unknown usernames.
* Multiple authentication attempts originated from external IP addresses.

### Primary Indicators of Compromise

* **IP Address:** `218.188.2.4`
* **Hostname:** `220-135-151-1.hinet-ip.hinet.net`

## Recommended Actions

Based on the observed activity, the following security controls were recommended:

* Block identified malicious IP addresses.
* Implement automated authentication rate limiting.
* Deploy intrusion prevention tools such as **Fail2Ban**.
* Monitor authentication logs for repeated failed-login patterns.

---

# Stage 2 – Python Automation

The second stage automated the manual investigation process using Python.

The script scans Linux authentication logs for patterns associated with suspicious authentication activity and extracts relevant events for further investigation.

## Detection Features

The script identifies:

* **Failed password attempts**
* **Authentication failures**
* **Invalid users**
* Suspicious authentication events from large log files

The detected events are exported to a **CSV file** for further analysis and reporting.

## Result

> **607 suspicious authentication events detected**

This demonstrates how scripting can reduce the time required to manually identify suspicious activity within large log files.

---

# Stage 3 – Splunk SIEM Analysis

The third stage involved ingesting the Linux authentication logs into **Splunk Enterprise** to simulate a Security Operations Centre monitoring workflow.

Splunk was used to:

* Search and filter authentication events
* Aggregate security events
* Identify repeated authentication attempts
* Correlate activity by source IP and username
* Visualise suspicious authentication patterns

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
| **Manual Analysis**   | Identified an SSH brute-force attack and extracted IoCs       |
| **Python Automation** | Automatically detected **607 suspicious events**              |
| **Splunk SIEM**       | Aggregated and analysed **607 authentication-related events** |

Together, these approaches demonstrate how **manual investigation, scripting, and SIEM technologies complement one another in a SOC environment**.

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

---

# Future Improvements

Potential extensions to this project include:

* **MITRE ATT&CK technique mapping**
* **GeoIP enrichment**
* **Fail2Ban integration**
* **AI-assisted security alert summarisation**
* **Automated threat-intelligence enrichment**
* **Interactive Splunk dashboards**
* **Automated incident reports**
* **Real-time log monitoring**

---

## Project Takeaways

This project provided practical experience across the security monitoring lifecycle, from **raw log investigation and threat identification through to automated detection and SIEM-based visualisation**.

It demonstrates the ability to:

* Investigate security events using Linux logs
* Identify suspicious authentication behaviour
* Extract and document IoCs
* Automate repetitive security-analysis tasks with Python
* Query and analyse security events using Splunk
* Communicate technical findings through structured reporting

The project therefore provides a practical demonstration of **SOC monitoring, threat detection, log analysis, security automation, and incident investigation skills**.
