#!/usr/bin/env python3
""" Test Web file """

from web import get_page, redis_conn

url = "http://slowwly.robertomurray.co.uk/delay/1000/url/http://www.google.com"
page_content = get_page(url)
print(page_content)

access_count_key = f"count:{url}"
access_count = redis_conn.get(access_count_key)
print(f"Access count for {url}: {access_count.decode('utf-8')}")
