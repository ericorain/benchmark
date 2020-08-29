#!/usr/bin/env python3

# Import Python library
from napalm import get_network_driver
import time

# Main function
def main():

    # Beginning of the counter
    start_time = time.time()

    # Definition of the equipment type
    driver = get_network_driver('ios')

    # Connection information
    device = driver(
        hostname="IP_ADDRESS",
        username="LOGIN",
        password="PASSWORD",
    )

    # Connection to the device
    device.open()

    # Connection time
    print("--- Connection --- %s second(s) ---" % (time.time() - start_time))

    # Command to send
    cmd = ["show run"]

    # Sending command
    output = device.cli(cmd)

    # Display the output
    print(output)

    # End of command
    print("--- END --- %s second(s) ---" % (time.time() - start_time))


# Main function call
if __name__ == '__main__':

    # Run the function
    main()


    """
    Results:
    --- Connection --- 7.5814502239227295 second(s) ---
    Search pattern never detected in send_command_expect: [Kswitch3b96df\#
    """