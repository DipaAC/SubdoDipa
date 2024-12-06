import requests
import json
import sys
from colorama import Fore, Style

def print_ascii_art():
    ascii_art = r"""
 SSS  U   U  BBBB   DDDD   OOO   DDDD   III  PPPP   AAAAA
S     U   U  B   B  D   D O   O  D   D   I   P   P  A   A
 SSS  U   U  BBBB   D   D O   O  D   D   I   PPPP   AAAAA
    S U   U  B   B  D   D O   O  D   D   I   P      A   A
SSSS   UUU   BBBB   DDDD   OOO   DDDD   III  P     A   A
                                                 
    """
    print(ascii_art)
    print(f"{Fore.YELLOW}[ INF ] Tools sedang berjalan mohon menunggu beberapa saat (Terima kasih telah menggunakan DIPA TOOLS).")
    print()

def get_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        subdomains = set()
        for entry in data:
            subdomain = entry['name_value']
            subdomains.add(subdomain)

        return subdomains

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}[ ERR ] Error fetching data")
        return set()

def print_subdomains(subdomains, domain):
    if subdomains:
        print(f"{Fore.GREEN}Subdomains and original domains for {domain}:")
        print()
        for index, subdomain in enumerate(sorted(subdomains), start=1):
            print(f"{Fore.WHITE}[ {index} ] {subdomain}")
        print(f"{Fore.WHITE}[ {len(subdomains) + 1} ] {domain}")
        print()
        print(f"{Fore.GREEN}Thank you for using SubdoList Tools")
    else:
        print(f"{Fore.WHITE}[ ERR ] No subdomains found for {domain}.")

if _name_ == "_main_":
    if len(sys.argv) != 3 or sys.argv[1] != '-s':
        print("Use : subdolist -s domain.name")
        sys.exit(1)

    domain = sys.argv[2]
    print_ascii_art()
    subdomains = get_subdomains(domain)
    print_subdomains(subdomains, domain)
