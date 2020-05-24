import requests
import time
from tqdm import tqdm

requests.packages.urllib3.disable_warnings()


def main():
    base_url = 'http://127.0.0.1:5000/'
    requests_per_period = 10
    pause_period = 10

    for _ in range(15):
        print(f"Attempt #{_}")
        response = requests.get(base_url)
        print(response.text)
        if (_ + 1) % requests_per_period == 0:
            print(f"Pausing for {pause_period} seconds to avoid 429")
            for _ in tqdm(range(pause_period)):
                time.sleep(1)


if __name__ == "__main__":
    main()
