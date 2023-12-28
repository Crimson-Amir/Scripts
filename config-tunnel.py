import socket
import subprocess


def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}")
        exit(1)


# Get IP_KHAREJ and IP_IRAN from user input
try:
    IP_IRAN = socket.gethostbyname(socket.gethostname())
    IP_KHAREJ = input("Enter IP_KHAREJ: ")
except KeyboardInterrupt:
    print("\nUser interrupted the input.")
    exit(1)
except socket.gaierror as e:
    print(f"Failed to retrieve the IP address: {e}")
    exit(1)

# Execute the commands on the server
commands = [
    "sysctl net.ipv4.ip_forward=1",
    f"iptables -t nat -A PREROUTING -p tcp --dport 22 -j DNAT --to-destination {IP_IRAN}",
    f"iptables -t nat -A PREROUTING -j DNAT --to-destination {IP_KHAREJ}",
    "iptables -t nat -A POSTROUTING -j MASQUERADE"
]

for command in commands:
    run_command(command)

# Create and write the contents to /etc/rc.local
rc_local_contents = """\
#!/bin/bash
sysctl net.ipv4.ip_forward=1
iptables -t nat -A PREROUTING -p tcp --dport 22 -j DNAT --to-destination {IP_IRAN}
iptables -t nat -A PREROUTING -j DNAT --to-destination {IP_KHAREJ}
iptables -t nat -A POSTROUTING -j MASQUERADE
"""

# Replace IP_IRAN and IP_KHAREJ in the rc_local_contents
rc_local_contents = rc_local_contents.replace("{IP_IRAN}", IP_IRAN)
rc_local_contents = rc_local_contents.replace("{IP_KHAREJ}", IP_KHAREJ)

try:
    with open('/etc/rc.local', 'w') as file:
        file.write(rc_local_contents)
except IOError as e:
    print(f"Error writing to /etc/rc.local: {e}")
    exit(1)

# Give root access to /etc/rc.local
run_command("sudo chmod +x /etc/rc.local")

# Execute the command to update /etc/resolv.conf
update_resolvconf_command = 'echo -e "nameserver 8.8.8.8\nnameserver 4.2.2.4" | sudo tee /etc/resolv.conf'
run_command(update_resolvconf_command)

# Create and write the contents to /etc/systemd/system/update-resolvconf.service
update_resolvconf_contents = """\
[Unit]
Description=Update resolv.conf on startup
After=network.target

[Service]
ExecStart=/bin/bash -c 'echo -e "nameserver 8.8.8.8\nnameserver 4.2.2.4" > /etc/resolv.conf'

[Install]
WantedBy=multi-user.target
"""

try:
    with open('/etc/systemd/system/update-resolvconf.service', 'w') as file:
        file.write(update_resolvconf_contents)
except IOError as e:
    print(f"Error writing to /etc/systemd/system/update-resolvconf.service: {e}")
    exit(1)

# Enable the update-resolvconf.service
run_command('sudo systemctl enable update-resolvconf.service')

# Download the file via URL using wget
wget_command = "wget -N --no-check-certificate https://github.com/teddysun/across/raw/master/bbr.sh"
run_command(wget_command)

# Give executable permissions to the downloaded file
chmod_command = "chmod +x bbr.sh"
run_command(chmod_command)

# Execute the installation script
bash_command = "bash bbr.sh"
run_command(bash_command)

print("Installation completed successfully!")
print("Server settings updated successfully!")
print("Additional server settings updated successfully!")
print("BBR installation completed successfully!")
