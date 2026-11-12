class CSRFChecker:
    def init(self):
        pass

    def scan_form(self, form):
        has_token = False
        for input_name in form['inputs']:
            if 'csrf' in input_name.lower() or 'token' in input_name.lower():
                has_token = True
                break

        if not has_token:
            print(f"[!] Potential CSRF Vulnerability found!")
            print(f"    Form Action: {form['action']}")
            print(f"    Reason: No CSRF token detected in form inputs.")
            return True
        
        return False