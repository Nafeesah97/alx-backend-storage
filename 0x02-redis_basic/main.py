#!/usr/bin/env python3
"""
Main file
"""
import time


get_page = __import__('web').get_page
urls = ["http://slowwly.robertomurray.co.uk/delay/10000/url/https://example.com",
            "http://slowwly.robertomurray.co.uk/delay/10000/url/https://www.google.com"]

for url in urls:
    start_time = time.time()
    content = get_page(url)
    print(f"URL: {url}, Content Length: {len(content)}, Time Taken: {time.time() - start_time} seconds")
