# Active Directory Threat Simulation & Log Analyzer (Purple Team Framework)

A comprehensive cybersecurity framework built on **Kali Linux** for Active Directory security assessment, incorporating both offensive attack simulation (Red Team) and defensive log analysis (Blue Team) mapped to the **MITRE ATT&CK Framework**.

## Project Components

### 1. Red Team Attack Simulator (`ad_attack_sim.py`)
Simulates credential access and brute-force attacks against Active Directory Domain Services.
* **Attack Vector:** Credential Access / Password Spraying
* **MITRE ATT&CK Tactic:** Credential Access (TA0006)
* **MITRE ATT&CK Technique:** Brute Force (T1110)

### 2. Blue Team Threat Detection Engine (`detect.py`)
Parses Windows Event Logs (`.evtx`) to identify threat activity and generates dynamic forensic reports.
* **Brute Force Detection (Event ID 4625):** Identifies repeated authentication failures.
* **Log Clearing Detection (Event ID 1102):** Detects defense evasion attempts where event logs are wiped (TA0005 / T1070).
* **Automated Reporting:** Outputs results directly to `report.txt`.

## Prerequisites & Installation
Ensure you have Python 3 and the required EVTX parsing library installed on Kali Linux:
```bash
pip install python-evtx --break-system-packages
