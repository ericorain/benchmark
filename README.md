# Performances of network libraries and other technologies


# 1 - Performance for 1 device

Library tested:
- napalm==2.5.0
- netmiko==3.1.1
- netdev==0.9.3 (modified)

Time used is in seconds.

## 1 - 1 Cisco SG350-10

| Library / Technology             | Netmiko          | Netmiko FAST CLI + expect_string | Netdev           | Napalm           |
|----------------------------------|------------------|----------------------------------|------------------|------------------|
| Device                           | Cisco SG350-10   | Cisco SG350-10                   | Cisco SG350-10   | Cisco SG350-10   |
| Operating system version         | 2.5.5.47         | 2.5.5.47                         | 2.5.5.47         | 2.5.5.47         |
| Command used                     | show run         | show run                         | show run         | show run         |
| Time to be in connection status  | 7.26763558387756 | 3.46916794776916                 | 5.68317532539368 | 7.58145022392273 |
| Time of execution of the command | 9.92956066131592 | 5.10266327857971                 | 7.34068417549133 | N/A              |


On a SG350-10 Cisco switch, the slowest library is Napalm with 7.58 seconds of connection and a failure for running the "show run" command (the device is not correctly supported and the prompt is not found). Netmiko supports that device but the performance are not outstanding (almost 10 seconds to get the result on a SG350-10). Netdev is 2 seconds faster than Netmiko with a custom support of the SG350-10 (not supported before the test). Netmiko with optimisation is 2 seconds faster than Netdev but FAST_CLI option can make a program less reliable.


## 1 - 2 Alcatel OS10K

| Library / Technology             | Netmiko                     | Netmiko FAST CLI + expect_string | Netdev                      |
|----------------------------------|-----------------------------|----------------------------------|-----------------------------|
| Device                           | OS10K                       | OS10K                            | OS10K                       |
| Command used                     | show configuration snapshot | show configuration snapshot      | show configuration snapshot |
| Time to be in connection status  | 4.359698057174683           | 0.9288327693939209               | 0.674893856048584           |
| Time of execution of the command | 5.749777793884277           | 1.5000059604644775               | 1.011824369430542           |

## 1 - 3 Alcatel OS6860E-48

| Library / Technology             | Netmiko                     | Netmiko FAST CLI + expect_string | Netdev                      |
|----------------------------------|-----------------------------|----------------------------------|-----------------------------|
| Device                           | OS6860E-48                  | OS6860E-48                       | OS6860E-48                  |
| Command used                     | show configuration snapshot | show configuration snapshot      | show configuration snapshot |
| Time to be in connection status  | 4.517857789993286           | 1.1811323165893555               | 0.9079082012176514          |
| Time of execution of the command | 6.065119743347168           | 1.9323439598083496               | 1.6970608234405518          |

## 1 - 4 Alcatel OS6900-X40

| Library / Technology             | Netmiko                     | Netmiko FAST CLI + expect_string | Netdev                      |
|----------------------------------|-----------------------------|----------------------------------|-----------------------------|
| Device                           | OS6900-X40                  | OS6900-X40                       | OS6900-X40                  |
| Command used                     | show configuration snapshot | show configuration snapshot      | show configuration snapshot |
| Time to be in connection status  | 4.4587788581848145          | 1.1811323165893555               | 1.0350358486175537          |
| Time of execution of the command | 5.999888896942139           | 1.6560468673706055               | 1.894153118133545           |

## 1 - 5 Alcatel OS6850E-48X

| Library / Technology             | Netmiko                     | Netmiko FAST CLI + expect_string | Netdev                      |
|----------------------------------|-----------------------------|----------------------------------|-----------------------------|
| Device                           | OS6850E-48X                 | OS6850E-48X                      | OS6850E-48X                 |
| Operating system version         | 6.4.6.125.R01               | 6.4.6.125.R01                    | 6.4.6.125.R01               |
| Command used                     | show configuration snapshot | show configuration snapshot      | show configuration snapshot |
| Time to be in connection status  | 5.630496263504028 *         | 2.041717767715454 *              | 2.234604597091675 *         |
| Time of execution of the command | 7.264156818389893 *         | 2.7667365074157715 *             | 3.0749030113220215 *        |

(*) The operating system used for the tests is quite old. The results are random since a software crash happens for Netmiko and Netdev after 3~4 attempts. Netdev says: "asyncssh.misc.ConnectionLost: Connection lost" and Netmiko'error is "paramiko.ssh_exception.SSHException: Error reading SSH protocol banner". A gracefull disconnect has been added at the end of Netdev script without improvement.