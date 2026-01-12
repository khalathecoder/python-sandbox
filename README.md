# Pentest Python Basics

This repository contains small Python scripts created to practice basic syntax and automation concepts relevant to penetration testing exams (e.g., PenTest+).

The focus is on understanding how scripts perform reconnaissance, handle input, and automate repetitive tasks—not on advanced exploitation.

---

## Scripts

### recon_basics.py
A simple HTTP reconnaissance script that:
- Accepts a URL as a command-line argument
- Sends an HTTP GET request
- Prints the HTTP status code
- Handles errors gracefully

Example usage:
```bash
python recon_basics.py http://example.com
