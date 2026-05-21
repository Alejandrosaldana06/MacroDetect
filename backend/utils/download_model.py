import os
import requests
from tqdm import tqdm

MODEL_ID = "1SdH4zte5QoSmw6d7CQXLnj9r8BD6TtZF"
MODEL_PATH = "backend/model/unet_resnet101.pth"
BASE_URL = "https://docs.google.com/uc?export=download"

def download_file_from_google_drive(id, destination):
    session = requests.Session()

    response = session.get(BASE_URL, params={'id': id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(BASE_URL, params=params, stream=True)

    save_response_content(response, destination)

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

def save_response_content(response, destination, chunk_size=32768):
    total = int(response.headers.get('content-length', 0))
    with open(destination, "wb") as f, tqdm(
        total=total,
        unit='B',
        unit_scale=True,
        desc="📦 Downloading model"
    ) as pbar:
        for chunk in response.iter_content(chunk_size):
            if chunk:
                f.write(chunk)
                pbar.update(len(chunk))

def download_model():
    if os.path.exists(MODEL_PATH):
        print("✅ Model already downloaded.")
        return

    print("⬇️ Downloading model from Google Drive...")
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    download_file_from_google_drive(MODEL_ID, MODEL_PATH)
    print("✅ Model downloaded successfully.")

if __name__ == "__main__":
    download_model()
