import requests
import dns.resolver
from urllib.parse import urlparse 

def find_subdomains(domain):
    subdomains = []
    try:
        answers = dns.resolver.query(domain, 'CNAME')
        for rdata in answers:
            subdomain = str(rdata.target)[:-1]
            subdomains.append(subdomain)
    except dns.resolver.NXDOMAIN:
        pass
    return subdomains 

def check_takeover(subdomain):
    response = requests.get(f"http://{subdomain}")
    if response.status_code == 404:
        print(f"[+] Subdomain '{subdomain}' is available for takeover!") 

def main():
    website = input("Enter the website URL: ")
    parsed_url = urlparse(website)
    domain = parsed_url.netloc
    subdomains = find_subdomains(domain)
    for subdomain in subdomains:
        check_takeover(subdomain) 

# Kullanım örneği:
main()
