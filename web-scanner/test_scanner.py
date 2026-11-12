from requester import Requester
from crawler import Crawler
from sqli_checker import SQLiChecker
from xss_checker import XSSChecker
from csrf_checker import CSRFChecker

scanner = Requester()
crawler = Crawler(scanner)
sqli_checker = SQLiChecker(scanner)
xss_checker = XSSChecker(scanner)
csrf_checker = CSRFChecker()

target = "http://127.0.0.1:5001"
print(f"[*] Starting comprehensive scan on {target}...")

links, forms = crawler.crawl(target)

print(f"\n[*] Testing {len(forms)} forms for vulnerabilities...")
for form in forms:
    print(f"\n  -> Scanning form at: {form['action']}")
    
    if not sqli_checker.scan_form(form):
        print(f"     [-] No SQLi found.")
        
    if not xss_checker.scan_form(form):
        print(f"     [-] No XSS found.")
        
    if not csrf_checker.scan_form(form):
        print(f"     [-] No CSRF found (Token exists).")