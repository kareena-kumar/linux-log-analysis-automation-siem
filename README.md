\# Linux Log Analysis, Automation \& SIEM Visualisation

> A cybersecurity project demonstrating SOC analyst workflows through manual Linux log investigation, Python automation, and Splunk SIEM analysis.


\## Overview


This project demonstrates how a Security Operations Centre (SOC) analyst can investigate Linux authentication logs using three complementary approaches:


\- Manual log investigation

\- Python automation

\- Splunk SIEM visualisation


Using a real-world Linux authentication dataset from LogHub, I identified repeated SSH brute-force attempts, extracted indicators of compromise (IoCs), automated detection with Python, and visualised attack patterns in Splunk Enterprise.


\---


\## Skills Demonstrated


\- Linux log analysis

\- SSH authentication investigation

\- Python automation

\- Splunk Enterprise

\- SIEM monitoring

\- Threat detection

\- IOC identification

\- Incident reporting


\---


\## Project Structure


```text

linux-log-analysis-automation-siem/

├── src/

│   └── log\_analysis.py

├── reports/

│   ├── project\_report.pdf

│   └── suspicious\_log\_entries.csv

├── screenshots/

├── sample-data/

│   └── README.md

├── .gitignore

├── README.md

└── requirements.txt

```


\---


\## Stage 1 – Manual Log Analysis


Reviewed raw Linux authentication logs to identify suspicious login activity.


\### Key Findings


\- High-volume automated SSH brute-force attack detected.

\- Repeated failed login attempts targeted both `root` and unknown usernames.

\- Primary Indicators of Compromise (IoCs):

&#x20; - `218.188.2.4`

&#x20; - `220-135-151-1.hinet-ip.hinet.net`


\### Recommended Actions


\- Block malicious IP addresses.

\- Enable automated rate limiting.

\- Deploy intrusion prevention tools such as Fail2Ban.


\---


\## Stage 2 – Python Automation


The Python script automatically scans Linux log files for suspicious authentication activity.


\### Features


\- Detects:

&#x20; - Failed passwords

&#x20; - Authentication failures

&#x20; - Invalid users

\- Processes large log files automatically.

\- Exports suspicious events to CSV.


\### Result


\- \*\*607 suspicious events detected\*\*


\---


\## Stage 3 – Splunk SIEM Analysis


Logs were ingested into Splunk Enterprise to simulate a Security Operations Centre workflow.


\### Example SPL Query


```spl

index="linux\_logs" source="Linux\_2k.log"

("Failed password" OR "authentication failure" OR "invalid user" OR "user unknown")

| stats count by rhost user

| sort -count

```


\### Key Findings


\- 608 authentication-related events identified.

\- 80 attempts against the `root` account from `150.183.249.110`.

\- 23 attempts from `207.243.167.114`.

\- Short bursts of repeated login attempts indicate automated brute-force behaviour.


\---


\## Splunk Screenshots


> Screenshots can be added later if Splunk is reinstalled.


\- Search results

\- Statistics view

\- Dashboard visualisation


\---


\## Key Outcomes


| Method | Outcome |

|--------|---------|

| Manual Analysis | Identified SSH brute-force attack |

| Python Automation | 607 suspicious events detected |

| Splunk SIEM | 608 correlated security events |


Together these approaches demonstrate how manual investigation, scripting, and SIEM tools complement each other during security monitoring.


\---


\## Dataset


This project uses the publicly available \*\*Linux\_2k.log\*\* dataset from LogHub.


The dataset is \*\*not included\*\* in this repository.


Download instructions are available in `sample-data/README.md`.


\---


\## Future Improvements


\- MITRE ATT\&CK mapping

\- GeoIP enrichment

\- Fail2Ban integration

\- AI-assisted alert summarisation

\- Interactive Splunk dashboards

