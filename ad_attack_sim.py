import sys
import time
from datetime import datetime

def print_banner():
    print("=" * 60)
    print("      ACTIVE DIRECTORY RED TEAM ATTACK SIMULATION TOOL     ")
    print("  Framework: Ethical Hacking & Security Assessment (Kali)  ")
    print("=" * 60 + "\n")

def simulate_brute_force(target_ip, user_list, password_list):
    print(f"[+] Launching Credential Access Attack (MITRE T1110) on Target: {target_ip}")
    print("[+] Testing authentication mechanisms against AD Domain Services...\n")
    
    attempts = 0
    for user in user_list:
        for pwd in password_list:
            attempts += 1
            print(f"[*] [{datetime.now().strftime('%H:%M:%S')}] Attempt {attempts}: Testing User='{user}' | Password='{pwd}'")
            time.sleep(0.5)
            
    print(f"\n[!] Attack Simulation Complete: {attempts} authentication requests sent.")
    print("[!] Target Security Logs should reflect Event ID 4625 (Failed Logon).\n")

def generate_attack_report(target_ip):
    report_file = "attack_report.txt"
    with open(report_file, "w") as f:
        f.write("============================================================\n")
        f.write("        ACTIVE DIRECTORY RED TEAM EXECUTION REPORT          \n")
        f.write(f" Executed on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f" Target IP  : {target_ip}\n")
        f.write(" Platform   : Kali Linux Attack Vector\n")
        f.write("============================================================\n\n")
        f.write("[EXECUTION SUMMARY]\n")
        f.write(" -> Attack Vector: Credential Access / Password Spraying\n")
        f.write(" -> MITRE ATT&CK Tactic  : Credential Access (TA0006)\n")
        f.write(" -> MITRE ATT&CK Technique: Brute Force (T1110)\n")
        f.write(" -> Expected Forensic Footprint: Event ID 4625 in Windows Security Log\n")
        f.write("-" * 60 + "\n")
    print(f"[+] Attack Execution Log successfully generated: {report_file}")

if __name__ == "__main__":
    print_banner()
    target = input("Enter Target Domain / IP Address: ") if len(sys.argv) < 2 else sys.argv[1]
    users = ["Administrator", "krbtgt", "guest"]
    passwords = ["123456", "Password123!", "Admin2026!"]
    
    simulate_brute_force(target, users, passwords)
    generate_attack_report(target)
  
