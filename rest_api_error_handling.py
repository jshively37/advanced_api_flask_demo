import requests

requests.packages.urllib3.disable_warnings()


def get_token(base_url, username, password, headers):
    url = f"{base_url}system/api/v1/auth/token"
    token = requests.post(
        url,
        headers=headers,
        auth=(username, password),
        verify=False).json()
    return token["Token"]


def main():

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # Get request with no token - Raise 401
    base_url = 'https://sandboxdnac.cisco.com/dna/'
    username = 'devnetuser'
    password = 'Cisco123!'
    site_info = requests.get(
        f"{base_url}intent/api/v1/site",
        headers=headers,
        verify=False
    )
    if site_info.status_code == 401:
        print(f'{site_info.status_code}: Unauthorized. Please check that token exists')

    # 400 Bad payload
    base_url = 'https://dna-3-dnac.campus.wwtatc.local/dna/'
    username = "wwt"
    password = "WWTwwt1!"
    token = get_token(base_url, username, password, headers)
    headers['x-auth-token'] = token
    cli_response = requests.post(
        url=f"{base_url}intent/api/v1/network-device-poller/cli/read-request",
        headers=headers,
        verify=False)
    if cli_response.status_code == 400:
        print(f'{cli_response.status_code}: Malformed payload/bad request')

    # Meraki 404
    url = 'https://api.meraki.com/api/v0/organizations'
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-Cisco-Meraki-API-Key": '111'
    }
    response = requests.get(
        url,
        headers=headers
    )
    if response.status_code == 404:
        print(f'{response.status_code}: Meraki check API key and try again')

if __name__ == "__main__":
    main()