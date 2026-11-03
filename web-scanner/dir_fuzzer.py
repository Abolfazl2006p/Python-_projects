import concurrent.futures

class DirFuzzer:
    def __init__(self, requester):
        self.requester = requester
        self.wordlist = [
            "admin", "login", "api", "backup", "config", "test",
            "dashboard", "user", "setting", "robots.txt", ".git", "db"
        ]

    def fuzz(self, base_url):
        print(f"[*] Starting Directory Fuzzing on {base_url}")
        found_paths = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executore:
            future_to_url = {executore.submit(self._check_path, base_url, path): path for path in self.wordlist}
            for future in concurrent.futures.as_completed(future_to_url):
                result = future.result()
                if result:
                    found_paths.append(result)

        return found_paths

    def _check_path(self,base_url, path):
        url = f"{base_url.rstrip('/')}/{path}"
        response = self.requester.get(url)
        if response and response.status_code in [200, 301, 302, 403]:
            print(f"[+] Found: {url} (Status: {response.status_code})")
            return {"url": url, "status": response.status_code}
        return None
                            