# animations.py

import requests
from streamlit_lottie import st_lottie


def load_lottieurl(url: str):
    """Loads a Lottie animation from a URL."""
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# URLs for the animations
LOTTIE_URLS = {
    "welcome": "https://lottie.host/648b22a6-193c-49aa-97f2-1a2c38d3886f/xKZWkYjNo2.json",
    "healthy": "https://lottie.host/179929f9-2150-4033-8c3b-4892c57f2231/rP9s3V4z3i.json",
    "sick": "https://lottie.host/97262a98-31e9-43f1-b125-a12b3f11904a/wG50whaWwO.json"
}


def show_animation(name: str, height: int = 200):
    """Loads and displays a specific Lottie animation."""
    url = LOTTIE_URLS.get(name)
    if url:
        lottie_json = load_lottieurl(url)
        if lottie_json:
            st_lottie(lottie_json, height=height)
