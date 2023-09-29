import subprocess
import argparse
import re
import random

# Function to generate a random MAC address
def generate_random_mac():
    # Generate a random MAC address with a valid format
    mac = [random.randint(0x00, 0xff) for _ in range(6)]
    mac[0] &= 0xFE  # Ensure the first octet is even to comply with MAC address rules
    return ':'.join(map(lambda x: f'{x:02x}', mac))

# Function to change the MAC address of a network interface
def change_mac(interface, new_mac):
    try:
        # Check if the user wants to generate a random MAC address
        if new_mac == "random":
            new_mac = generate_random_mac()
            print(f"[+] Generated random MAC: {new_mac}")

        # Check if the provided MAC address is in a valid format
        if not re.match(r'^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$', new_mac):
            raise ValueError("Invalid MAC address format")

        # Disable the network interface
        subprocess.call(["ifconfig", interface, "down"])

        # Change the MAC address
        subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])

        # Enable the network interface
        subprocess.call(["ifconfig", interface, "up"])

        print(f"[+] Successfully changed MAC of {interface} to {new_mac}")
    except Exception as e:
        print(f"[-] An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", required=True, help="Interface to change MAC")
    parser.add_argument("-m", "--mac", dest="new_mac", required=True, help="New MAC address or 'random' for a random MAC")

    args = parser.parse_args()

    # Call the function to change the MAC address
    change_mac(args.interface, args.new_mac)

if __name__ == "__main__":
    main()
