from requester import Requester
from crawler import Crawler
from sqli_checker import SQLiChecker

scanner = Requester()
crawler = Crawler(scanner)
sqli_checker = SQLiChecker(scanner)

target = "http://127.0.0.1:5000"
print(f"[*] Starting scan on {target}...")

links, forms = crawler.crawl(target)

print(f"\n[*] Testing {len(forms)} forms for SQL Injection...")
for form in forms:
    is_vuln = sqli_checker.scan_form(form)
    if not is_vuln:
        print(f"[-] Form at {form['action']} seems safe.")