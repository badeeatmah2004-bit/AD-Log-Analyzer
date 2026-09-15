# Active Directory Threat Detection & Event Log Analyzer

A Python-based security tool built on **Kali Linux** to parse Windows Event Logs (`.evtx`) and detect cyber threats targeting Active Directory environments.

## Features & Detection Rules
* **Brute Force Detection (Event ID 4625):** Identifies repeated failed login attempts.
  * **MITRE ATT&CK Tactic:** Credential Access (TA0006)
  * **MITRE ATT&CK Technique:** Brute Force (T1110)
* **Log Clearing Detection (Event ID 1102):** Detects defense evasion techniques where audit logs are wiped.
  * **MITRE ATT&CK Tactic:** Defense Evasion (TA0005)
  * **MITRE ATT&CK Technique:** Indicator Removal (T1070)
* **Automated Reporting:** Generates a real-time summary report saved to `report.txt`.

## Prerequisites & Installation
Ensure you have Python 3 and the `python-evtx` library installed on Kali Linux:
```bash
pip install python-evtx
