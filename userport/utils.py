"""
Helper methods for the application.
"""
import requests
import hashlib
import secrets


def get_domain_from_email(email: str):
    """
    Parse domain from given string.
    Raises error if string doesn't contain @ string.
    """
    if '@' not in email:
        raise ValueError(f'Invalid email string: f{email}')
    _, domain = email.split('@')
    return domain


def fetch_html_page(url: str) -> str:
    """
    Fetch HTML page for gien URL.
    """
    response = requests.get(url)
    content_type: str = response.headers['content-type']
    if "text/html" not in content_type:
        raise ValueError(
            f'Invalid Content Type; expected text/html, got {content_type}')
    return response.text


def generate_hash(key: str) -> str:
    """
    Helper to hash an existing key. Returns hex string of length 16.
    """
    h = hashlib.shake_256(key.encode('utf-8'))
    return h.hexdigest(16)
