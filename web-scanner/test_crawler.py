from requester import Requester
from crawler import Crawler

scanner = Requester()
crawler = Crawler(scanner)

target = "http://127.0.0.1:5000"
print(f"Starting crawler on {target}...")

links, forms = crawler.crawl(target)

print(f"\n[+] Found {len(links)} links:")
for link in links:
    print(f"  - {link}")

print(f"\n[+] Found {len(forms)} forms:")
for form in forms:
    print(f"  - Action: {form['action']} | Method: {form['method']} | Inputs: {form['inputs']}")
    