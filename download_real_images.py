import os
import requests
from PIL import Image
from io import BytesIO

# Create directory if it doesn't exist
os.makedirs('sample_images/real', exist_ok=True)

# URLs of real plant disease images (placeholder license-free images)
image_urls = {
    "tomato_late_blight": "https://plantvillage.psu.edu/assets/diseases/a94e5eeae9501c75e98dfa7d1059d5f05b84b31bc9bc42f8dcc19f3fea077fbb.jpg",
    "tomato_leaf_mold": "https://plantvillage.psu.edu/assets/diseases/e9fd0dad312fdffb51ece1ede1c163a0839bc7aa4e55bc3bf77c0de1236115d6.jpg",
    "tomato_healthy": "https://plantvillage.psu.edu/assets/diseases/c9a414bb9fe8aebc5b95f10b33f13e6aabf28a1ecad6d164f2c076b76e56a1fe.jpg",
    "potato_early_blight": "https://plantvillage.psu.edu/assets/diseases/cd90b92e45c57fbe1eade80842190ec736aadeac7c9de6a00a1d24c5ab0e8ddd.jpg"
}

downloaded_files = []

# Download and save images
for label, url in image_urls.items():
    try:
        # Attempt to download the image
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            
            # Resize to manageable dimensions
            img = img.resize((400, 400))
            
            # Save image
            file_path = f'sample_images/real/{label}.jpg'
            img.save(file_path)
            downloaded_files.append(file_path)
            print(f"Downloaded and saved: {file_path}")
        else:
            print(f"Failed to download {label} image: HTTP {response.status_code}")
    except Exception as e:
        print(f"Error downloading {label} image: {e}")

print(f"Downloaded {len(downloaded_files)} real plant disease images")