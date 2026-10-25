class SQLiChecker:
    def __init__(self, requester):
        self.requester = requester
        self.payloads = ["'", "\"", "1' OR '1'='1", "1' OR 1=1--"]
        self.errors = ["sql syntax", "mysql_fetch", "sqlite3", "syntax error", "unclosed quotation mark"]

    def scan_form(self, form):
        is_vulnerable = False
        for payload in self.payloads:
            data = {input_name: payload for input_name in form['inputs']}
            
            if form['method'] == 'post':
                response = self.requester.post(form['action'], data=data)
            else:
                response = self.requester.get(form['action'], params=data)

            if response is not None:
                for error in self.errors:
                    if error.lower() in response.text.lower():
                        print(f"[!] SQLi Found!")
                        print(f"    URL: {form['action']}")
                        print(f"    Payload: {payload}")
                        print(f"    Error: {error}")
                        is_vulnerable = True
                        break
            if is_vulnerable:
                break
        return is_vulnerable