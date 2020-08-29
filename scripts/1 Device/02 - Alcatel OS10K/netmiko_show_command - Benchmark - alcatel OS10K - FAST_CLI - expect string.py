#!/usr/bin/env python3

# Import Python library
from netmiko import ConnectHandler
import time

my_device = {
    'username': 'LOGIN',
    'password': 'PASSWORD',
    'ip':   'IP_ADDRESS',
    'device_type': 'alcatel_aos',
    'fast_cli': True,
}

# Main function
def my_netmiko_command():

    # Beginning of the counter
    start_time = time.time()

    # Connexion to the device
    net_connect = ConnectHandler(**my_device)

    # Connection time
    print("--- Connection --- %s second(s) ---" % (time.time() - start_time))

    # Command to send
    cmd = "show configuration snapshot"

    # Sending command
    output = net_connect.send_command(cmd, expect_string=">")

    # Display the output
    print(output)

    # End of command
    print("--- END --- %s second(s) ---" % (time.time() - start_time))

# Main function call
if __name__ == '__main__':

    # Run the function
    my_netmiko_command()

    """
    Results:
    --- Connection --- 0.9288327693939209 second(s) ---
    --- END --- 1.5000059604644775 second(s) ---
    """