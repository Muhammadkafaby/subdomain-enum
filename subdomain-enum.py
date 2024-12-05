import requests
import argparse
import os
from colorama import Fore, Style, init
import logging

# Initialize colorama
init(autoreset=True)

# Configure logging
logging.basicConfig(filename='subdomain_enum.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def main(domain):
    if not os.path.exists("subdomains.txt"):
        print(Fore.RED + "Error: 'subdomains.txt' file not found!")
        return

    with open("subdomains.txt") as file:
        subdoms = file.read().splitlines()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    for sub in subdoms:
        sub_domain = f"http://{sub}.{domain}"

        try:
            response = requests.get(sub_domain, headers=headers, timeout=5)
            if response.status_code == 200:
                print(Fore.GREEN + "Valid domain: " + sub_domain)
                logging.info("Valid domain: %s", sub_domain)
            else:
                print(Fore.YELLOW + "Invalid domain: " + sub_domain)
        except requests.ConnectionError:
            print(Fore.RED + "Connection error: " + sub_domain)
        except requests.Timeout:
            print(Fore.RED + "Timeout error: " + sub_domain)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Subdomain Enumeration Tool")
    parser.add_argument("-d", "--domain", help="The domain to enumerate subdomains for")
    args = parser.parse_args()

    if args.domain:
        main(args.domain)
    else:
        domain = input("Please enter the domain to enumerate subdomains for: ")
        main(domain)