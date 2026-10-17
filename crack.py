import hashlib

target_hash = "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"
wordlist = ["admin", "123456", "qwerty", "password123", "root"]

print("Starting dictionary attack...")

for password in wordlist:
    guess_hash = hashlib.sha256(password.encode()).hexdigest()
    
    if guess_hash == target_hash:
        print(f"[+] Password found: {password}")
        break
    else:
        print(f"[-] Tried {password} -> Failed")