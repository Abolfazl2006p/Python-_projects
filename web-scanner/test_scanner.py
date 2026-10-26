from requester import Requester
from crawler import Crawler
from sqli_checker import SQLiChecker
from xss_checker import XSSChecker

scanner = Requester()
crawler = Crawler(scanner)
sqli_checker = SQLiChecker(scanner)
xss_checker = XSSChecker(scanner)

target = "http://127.0.0.1:5000"
print(f"[*] Starting comprehensive scan on {target}...")

links, forms = crawler.crawl(target)

print(f"\n[*] Testing {len(forms)} forms for vulnerabilities...")
for form in forms:
    print(f"  -> Scanning form at: {form['action']}")
    
    if not sqli_checker.scan_form(form):
        print(f"     [-] No SQLi found.")
        
    if not xss_checker.scan_form(form):
        print(f"     [-] No XSS found.")