import requests
import time
from tqdm import tqdm

requests.packages.urllib3.disable_warnings()


def main():
    base_url = 'http://127.0.0.1:5000/'
    backoff_factor = 1

    for _ in range(15):
        print(f"Attempt #{_}")
        response = requests.get(base_url)
        while response.status_code == 429:
            print('429 Found')
            backoff_factor *= 2
            print(f"Sleeping for {backoff_factor} seconds")
            for i in tqdm(range(backoff_factor)):
                time.sleep(1)
            response = requests.get(base_url)
        print(response.text)


if __name__ == "__main__":
    main()
