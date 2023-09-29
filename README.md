# Mac_changer
Linux based Mac Changer

```markdown
# MAC Address Changer

This Python script allows you to change the MAC (Media Access Control) address of a network interface on a Linux system. You can specify a new MAC address or generate a random one.

## Prerequisites

- Python 3.x
- Linux-based operating system

## Usage

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/your-username/mac-address-changer.git
   ```

2. Navigate to the project directory:

   ```shell
   cd mac-address-changer
   ```

3. Run the script with the following command:

   ```shell
   python mac_changer.py -i <INTERFACE> -m <NEW_MAC>
   ```

   - `<INTERFACE>`: Specify the network interface for which you want to change the MAC address.
   - `<NEW_MAC>`: Provide the new MAC address you want to set, or use "random" to generate a random MAC address.

   Example:

   ```shell
   python mac_changer.py -i eth0 -m 00:11:22:33:44:55
   ```

   or

   ```shell
   python mac_changer.py -i eth0 -m random
   ```

4. The script will attempt to change the MAC address of the specified interface. If successful, it will display a success message along with the new MAC address.

## Important Notes

- Ensure that you have the necessary permissions to change the MAC address on your system.
- The first octet of a MAC address must be an even number. The script automatically enforces this rule.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This script is inspired by various online tutorials and community contributions.

Feel free to fork, contribute, and make improvements to this script. If you encounter any issues or have suggestions for enhancements, please create an issue or a pull request.
```
