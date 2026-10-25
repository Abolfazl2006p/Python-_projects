# Python Web Vulnerability Scanner

A custom, modular web vulnerability scanner built from scratch in Python. This tool is designed to crawl web applications, discover forms/links, and test for common vulnerabilities like SQL Injection.

## 🚀 Features
- **Requester (requester.py)**: Handles HTTP requests with custom user-agents, sessions, and timeout management.
- **Crawler (crawler.py)**: Crawls the target website to extract all links and HTML forms.
- **SQLi Checker (sqli_checker.py)**: Automatically injects payloads into forms and analyzes server responses for database errors to detect SQL Injection.

## 🛠️ How to Use
1. Install the required dependencies:
   `bash
   pip install requests beautifulsoup4