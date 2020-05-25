import requests
import time
from tqdm import tqdm

requests.packages.urllib3.disable_warnings()


def main():
    base_url = 'http://127.0.0.1:5000/'

    for _ in range(15):
        print(f"Attempt #{_}")
        response = requests.get(f"{base_url}")
        if response.status_code == 200:
            print(response.text)
        elif response.status_code == 429:
            print(f"Pause for {response.headers['Retry-After']} seconds...")
            for i in tqdm(range(int(response.headers['Retry-After']))):
                time.sleep(1)
            response = requests.get(f"{base_url}")
            print(response.text)


if __name__ == "__main__":
    main()
