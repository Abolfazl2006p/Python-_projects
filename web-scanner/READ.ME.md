# Web Vulnerability Scanner

A custom, modular web vulnerability scanner built from scratch in Python. This tool is designed to crawl web applications, discover hidden directories, and test for common vulnerabilities including SQL Injection, XSS, and CSRF.

## 🚀 Features
- **Requester (requester.py)**: Handles HTTP requests with custom user-agents, sessions, and timeout management.
- **Crawler (crawler.py)**: Crawls the target website to extract all links and HTML forms.
- **SQLi Checker (sqli_checker.py)**: Automatically injects payloads into forms and analyzes server responses for database errors to detect SQL Injection.
- **XSS Checker (xss_checker.py)**: Injects JavaScript payloads into forms to detect Cross-Site Scripting vulnerabilities.
- **CSRF Checker (csrf_checker.py)**: Analyzes HTML forms to detect missing anti-CSRF tokens, indicating potential Cross-Site Request ForgeryDirectory Fuzzer (dir_fuzzer.py)er (dir_fuzzer.py)**: Discovers hidden directories and sensitive endpoints using a wordlist.

## 🛠️ How to Use
1. Install the required dependencies:
   `bash
   pip install requests beautifulsoup4