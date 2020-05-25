from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException


def main():
    switches = {
        "good_router": {
            "host": "10.246.32.203",
            "port": "1222",
            "device_type": "cisco_ios"
        },
        "bad_creds_router": {
            "host": "10.246.32.203",
            "port": "3222",
            "device_type": "cisco_ios"
        },
        "timeout_router": {
            "host": "10.246.32.224",
            "port": "1222",
            "device_type": "cisco_ios"
        },
    }

    username = input('Enter your username: ')
    password = getpass('Enter your password: ')

    for router, value in switches.items():
        device = {'device_type': value['device_type'],
                  'host': value['host'],
                  'port': value['port'],
                  'username': username,
                  'password': password,
                  }
        print(f"Logging into {router}")
        print('-' * 20)
        try:
            with ConnectHandler(**device, auth_timeout=10):
                print(f"{router} successfully connected")
        except (NetMikoTimeoutException):
            print(f"{router} is unreachable")
        except (NetMikoAuthenticationException):
            print(f"{router} authentication failure")
        except Exception as e:
            print(f"{router}:  {repr(e)}")
        print('\n')


if __name__ == "__main__":
    main()
