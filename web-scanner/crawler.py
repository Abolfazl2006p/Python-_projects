from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

class Crawler:
    def __init__(self, requester):
        self.requester = requester
        self.visited_urls = set()
        self.links = set()
        self.forms = []

    def extract_links(self, url, html_content):
        soup = BeautifulSoup(html_content, "html.parser")
        for a_tag in soup.find_all("a", href=True):
            href = a_tag.get("href")
            full_url = urljoin(url, href)
            if urlparse(full_url).netloc == urlparse(url).netloc:
                self.links.add(full_url)

    def extract_forms(self, url, html_content):
        soup = BeautifulSoup(html_content, "html.parser")
        for form in soup.find_all("form"):
            action = form.get("action")
            method = form.get("method", "get").lower()
            inputs = []
            for input_tag in form.find_all("input"):
                input_name = input_tag.get("name")
                if input_name:
                    inputs.append(input_name)
            
            form_details = {
                "action": urljoin(url, action) if action else url,
                "method": method,
                "inputs": inputs
            }
            self.forms.append(form_details)

    def crawl(self, start_url):
        print(f"[*] Crawling: {start_url}")
        response = self.requester.get(start_url)
        if response and response.status_code == 200:
            self.visited_urls.add(start_url)
            self.extract_links(start_url, response.text)
            self.extract_forms(start_url, response.text)
        return self.links, self.forms
    