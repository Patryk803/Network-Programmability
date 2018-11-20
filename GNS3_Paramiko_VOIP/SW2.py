import time
import paramiko

ip_address = "192.168.100.1"
username = "Dominika"
password = "cisco"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print "Successful connection", ip_address

remote_connection = ssh_client.invoke_shell()

remote_connection.send("configure terminal\n")
remote_connection.send("ip dhcp snooping\n")
remote_connection.send("ip dhcp snooping vlan 6\n")
remote_connection.send("interface gigabitEthernet 0/0\n")
remote_connection.send("no negotiation auto\n")
remote_connection.send("speed 1000\n")
remote_connection.send("duplex full\n")
remote_connection.send("switchport trunk encapsulation dot1q\n")
time.sleep(1)
remote_connection.send("switchport mode trunk\n")
remote_connection.send("switchport trunk allowed vlan 6,100\n")
remote_connection.send("switchport trunk native vlan 666\n")
remote_connection.send("ip dhcp snooping trust\n")
remote_connection.send("exit\n")



remote_connection.send("interface gigabitEthernet 0/2\n")
time.sleep(1)
remote_connection.send("switchport mode access\n")
remote_connection.send("switchport access vlan 6\n")
remote_connection.send("switchport port-security\n")
remote_connection.send("switchport port-security maximum 2\n")
remote_connection.send("switchport port-security mac-address sticky\n")
remote_connection.send("ip dhcp snooping trust\n")
time.sleep(1)
remote_connection.send("exit\n")


time.sleep(1)
remote_connection.send("interface range gigabitEthernet 0/3, gigabitEthernet 1/0-3, gigabitEthernet 2/0-3, gigabitEthernet 3/0-3\n")
remote_connection.send("switchport mode access\n")
time.sleep(1)
remote_connection.send("switchport access vlan 999\n")
remote_connection.send("switchport port-security\n")
remote_connection.send("switchport port-security mac-address sticky\n")
remote_connection.send("shutdown\n")
time.sleep(1)
remote_connection.send("exit\n")
time.sleep(1)
 

remote_connection.send("interface range gigabitEthernet 0/1-2\n")
remote_connection.send("spanning-tree portfast edge\n")
remote_connection.send("spanning-tree bpduguard enable\n")



remote_connection.send("end\n")

time.sleep(1)
output = remote_connection.recv(65535)
print output
