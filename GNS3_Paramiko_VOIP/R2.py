import time
import paramiko

ip_address = "192.168.100.2"
username = "Dominika"
password = "cisco"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print "Successful connection", ip_address

remote_connection = ssh_client.invoke_shell()

remote_connection.send("configure terminal\n")
remote_connection.send("ip access-list extended VOIP\n")
remote_connection.send("permit ip host 192.168.6.6 host 192.168.5.5\n")
remote_connection.send("exit\n")
remote_connection.send("username R1 password cisco\n")
remote_connection.send("ip route 0.0.0.0 0.0.0.0 132.0.0.1\n")
remote_connection.send("interface serial 1/0\n")
remote_connection.send("encapsulation ppp\n")
remote_connection.send("ppp authentication chap\n")
remote_connection.send("ppp chap hostname R2\n")
remote_connection.send("ip address 132.0.0.2 255.255.255.0\n")
remote_connection.send("no shutdown\n")
remote_connection.send("exit\n")
print "Interface Serial 1/0 has been configured"
remote_connection.send("ip dhcp excluded-address 192.168.6.1\n")
remote_connection.send("ip dhcp pool Vlan6\n")
remote_connection.send("network 192.168.6.0 255.255.255.0\n")
remote_connection.send("domain-name Dominika.com\n")
remote_connection.send("default-router 192.168.6.1\n")
remote_connection.send("lease infinite\n")
print "DHCP has been configured"
remote_connection.send("dial-peer voice 1 voip\n")
time.sleep(1)
remote_connection.send("destination-pattern 555.\n")
remote_connection.send("session target ipv4:132.0.0.1\n")
remote_connection.send("exit\n")
remote_connection.send("telephony-service\n")
remote_connection.send("max-ephones 1\n")
remote_connection.send("max-dn 1\n")
remote_connection.send("ip source-address 192.168.6.1 port 2000\n")
remote_connection.send("auto assign 1 to 1\n")
remote_connection.send("transfer-system full-consult\n")
remote_connection.send("exit\n")
remote_connection.send("ephone-dn  1\n")
time.sleep(2)
remote_connection.send("number 6666\n")
remote_connection.send("description Dominika_VLAN6\n")
remote_connection.send("name Dominika_Vlan6\n")
remote_connection.send("label Dominika_Vlan6\n")
remote_connection.send("exit\n")
remote_connection.send("ephone 1\n")
remote_connection.send("keepalive 10\n")
remote_connection.send("exit\n")
print "VOIP has been configured"
remote_connection.send("end\n")

time.sleep(1)
output = remote_connection.recv(65535)
print output
