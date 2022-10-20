#!/usr/bin/python3

# Here we import modules, pyfiglet ,socket and time....!!
import pyfiglet
import socket
import time 


#banner 
print("__-----___----_____----____"*3)
banner = pyfiglet.figlet_format("PORT SCANNER")
print(banner)

author = "                              <..!!by ANKUSHGuPt@ AKA mrrobot_h4ck3r !!!..!!> "
print(author) 
print("__-----___----_____----____"*3)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# here we asking for the target website or a host..!!

target = input('Enter the IP Address or Website:-')

# next line gives us the ip address of the target if it is a website
target_ip = socket.gethostbyname(target)
print('Starting scan on host:', target_ip)

# function programm for scanning ports


def port_scan(port):
	try:
		s.connect((target_ip, port))
		return True
	except:
		return False
	

start = time.time()

# here we are scanning port 1 to 100
for port in range(1,100):
	if port_scan(port):
		print(f'port {port} is open')
	else:
		print(f'port {port} is closed')

end = time.time()
print(f'Time taken {end-start:.2f} seconds')

