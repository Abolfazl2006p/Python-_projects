class XSSChecker:
    def __init__(self, requester):
        self.requester = requester
        self.payloads = ["<script>alert('XSS')</script>", "\"><script>alert(1)</script>", "javascript:alert(1)"]

    def scan_form(self, form):
        is_vulnerable = False
        for payload in self.payloads:
            data = {input_name: payload for input_name in form['inputs']}
            
            if form['method'] == 'post':
                response = self.requester.post(form['action'], data=data)
            else:
                response = self.requester.get(form['action'], params=data)

            if response is not None:
                if payload in response.text:
                    print(f"[!] XSS Found!")
                    print(f"    URL: {form['action']}")
                    print(f"    Payload: {payload}")
                    is_vulnerable = True
                    break
        return is_vulnerable