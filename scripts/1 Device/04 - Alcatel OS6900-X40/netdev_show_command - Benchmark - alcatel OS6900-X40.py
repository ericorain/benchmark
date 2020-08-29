#!/usr/bin/env python3

# Import Python library
import asyncio, netdev
import time

# Coroutine used for the tasks
async def task(param):

    # Beginning of the counter
    start_time = time.time()

    # Create an object for the devices and open SSH connections
    async with netdev.create(**param) as device:

        # Connection time
        print("--- Connection --- %s second(s) ---" % (time.time() - start_time))

        # Testing sending simple command
        
        # Command to send
        cmd = "show configuration snapshot"

        # Sending command
        output = await device.send_command(cmd)

        # Display the output
        print(output)

        # End of command
        print("--- END --- %s second(s) ---" % (time.time() - start_time))

# Main coroutine
async def main():

    # Parameters of the network device
    my_device = {
        'username' : 'LOGIN',
        'password' : 'PASSWORD',
        'host': 'IP_ADDRESS',
        'device_type': 'alcatel_aos',
    }

    # List of devices
    devices = [my_device]
    
    # List of tasks
    my_tasks = [task(dev) for dev in devices]
    
    # Starting the coroutine of the tasks
    await asyncio.wait(my_tasks)


# Main function call
if __name__ == '__main__':

    # Run the main coroutine
    asyncio.run(main())

    '''
    Result:
    ********************************************************************************
    --- Connection --- 1.0350358486175537 second(s) ---
    --- END --- 1.894153118133545 second(s) ---
    ********************************************************************************

    '''