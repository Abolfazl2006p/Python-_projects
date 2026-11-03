from requester import Requester
from dir_fuzzer import DirFuzzer

scanner = Requester()
fuzzer = DirFuzzer(scanner)

target = "http://127.0.0.1:5000"
print(f"[*] Starting scan on {target}...")

found = fuzzer.fuzz(target)

print(f"\n[+] Total paths found: {len(found)}")
for item in found:
    print(f"  - {item['url']} -> Status: {item['status']}")
    