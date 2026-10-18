## Task 3: Router Hardening (TP-Link TD-W9960)
- Logged into the router admin panel using default credentials (admin/admin).
- Vulnerability identified: WPS was enabled.
- Vulnerability identified: Admin password was the default (admin).
- Mitigation: Disabled WPS. Network SSID is hidden.
- Note: Left the default admin password as is for now (decision made by user).
## TryHackMe Completion
- completed "Linux Fundamentals Part 1" room.
- Tasks completed: 5
- Point earned: 64
##Wireshark & Network Analysis
- Captured DNS queries to resolve IP addresses (e.g., varzesh3.com).
- Captured HTTP GET request on `neverssl.com`.
- Extracted real user-Agent. Noticed that Windows 11 is spoofed as "Windows NT 10.0" for web compatibility. 
