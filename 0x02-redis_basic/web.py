import requests
import redis


def get_page(url: str) -> str:
    """Function to obtain the HTML content of a URL and cache the result."""
    # Connect to Redis
    r = redis.Redis()

    # Increment access count for the URL
    count_key = f"count:{url}"
    r.incr(count_key)

    # Check if the content is already cached
    cached_content = r.get(url)
    if cached_content:
        return cached_content.decode('utf-8')

    # Retrieve the HTML content from the URL
    response = requests.get(url)
    html_content = response.text

    # Cache the content with an expiration time of 10 seconds
    r.setex(url, 10, html_content)

    return html_content
