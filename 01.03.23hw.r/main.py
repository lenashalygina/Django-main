import concurrent.futures
import requests

def download_image(url):
    response = requests.get(url)
    filename = url.split("/")[-1]
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"Downloaded {filename}")

urls = [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg",
    "https://example.com/image3.jpg",
    "https://example.com/image4.jpg",
    "https://example.com/image5.jpg",
    "https://example.com/image6.jpg",
    "https://example.com/image7.jpg",
    "https://example.com/image8.jpg",
    "https://example.com/image9.jpg",
    "https://example.com/image10.jpg",
]

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(download_image, urls)
