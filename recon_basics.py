import requests
import sys


if len(sys.argv) < 2:
    print("Usage: python recon_basics.py <url>")
    sys.exit(1)

url = sys.argv[1]


try:
    response = requests.get(url, timeout=5)
    print(url, response.status_code)
except requests.exceptions.RequestException:
    print(url, "request failed")
