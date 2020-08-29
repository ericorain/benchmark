#!/usr/bin/env python3

# Import Python library
from netmiko import ConnectHandler
import time

my_device = {
    'device_type': 'cisco_s300',
    'ip':   'IP_ADDRESS',
    'username': 'LOGIN',
    'password': 'PASSWORD',
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

    # Sending command
    output = net_connect.send_command("show run", expect_string="#")

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
    --- Connection --- 3.469167947769165 second(s) ---
    --- END --- 5.102663278579712 second(s) ---
    """