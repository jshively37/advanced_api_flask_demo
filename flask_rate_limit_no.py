import requests

requests.packages.urllib3.disable_warnings()


def main():
    base_url = 'http://127.0.0.1:5000/'

    for _ in range(15):
        print(f"Attempt #{_}")
        response = requests.get(f"{base_url}")
        print(response.status_code)


if __name__ == "__main__":
    main()
