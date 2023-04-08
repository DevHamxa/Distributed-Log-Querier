import subprocess
# import socket
import os
import netifaces 
import paramiko

"""hostname=socket.gethostname()
IpAddr=socket.gethostbyname (hostname) 
print("comp name: "+hostname) 
print("comp ip address"+IpAddr)"""

for link in netifaces.ifaddresses('enp0s3')[netifaces.AF_INET]:
	cnodeaddr = link['addr']
	print(link['addr'])
if cnodeaddr == "192.168.1.10":       # Use ipaddress that you have manually set for the system to communicate over the cluster
	cnode = 0
elif cnodeaddr == "192.168.1.11":     # Use ipaddress that you have manually set for the system to communicate over the cluster
	cnode = 1
elif cnodeaddr == "192.168.1.12":     # Use ipaddress that you have manually set for the system to communicate over the cluster
	cnode = 2

while True:
	try: 
		node = int(input("Select the Server Node you want to Query: \n0. Master Node \n1. Node-1 \n2. Node-2 \nSelect Your Choice: "))
		break
	except ValueError:
		print("Please Enter a Number.")

if cnode == node:
	print("You are Quering the current Machine......")
	Query = input("Enter the Reguler Expression / Query: \n 1. -c -- This prints only a count of the lines that match a pattern. \n 2. -h -- Display the matched lines, but do not display the filenames. \n 3. -i -- Ignores, case for matching .\n 4. -l -- Displays the list of filenames only. \n 5. -v -- This prints out all the lines that do not match the pattern. \n 6. -e exp -- Specifies expression with this option can be used multiple times. \n 7. -f file -- Takes pattern from file, one per line. \n 8. -E -- Treats pattern as an extended reguler expression. \n 9. -w -- Match whole word. \n 10. -0 -- Print every matched line on seperate line. \n 11. -A n -- Prints only searched line and n lines after the result. \n 12. -B n -- Prints searched line and n lines before the result. \n 13. -C n -- Prints n lines before and after the result. \n 14. -n -- Display the matched lines and there line numbers. \n Your Selected Character is: ")
	smnode = os.system("grep " + Query)
	print("The exit code was: %d" % smnode)

else:
	if node == 0:
		print("Ready Query Master Node..........")
		Query = input("Enter the Reguler Expression / Query: \n 1. -c -- This prints only a count of the lines that match a pattern. \n 2. -h -- Display the matched lines, but do not display the filenames. \n 3. -i -- Ignores, case for matching .\n 4. -l -- Displays the list of filenames only. \n 5. -v -- This prints out all the lines that do not match the pattern. \n 6. -e exp -- Specifies expression with this option can be used multiple times. \n 7. -f file -- Takes pattern from file, one per line. \n 8. -E -- Treats pattern as an extended reguler expression. \n 9. -w -- Match whole word. \n 10. -0 -- Print every matched line on seperate line. \n 11. -A n -- Prints only searched line and n lines after the result. \n 12. -B n -- Prints searched line and n lines before the result. \n 13. -C n -- Prints n lines before and after the result. \n 14. -n -- Display the matched lines and there line numbers. \n Your Selected Character is: ")
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect('192.168.1.10', username='UserName', password='password')   # change the ipaddress, username, password according to the machine your querieng
		# stdin, stdout, stderr = client.exec_command('cat /proc/meminfo')
		stdin, stdout, stderr = client.exec_command('grep ' + Query)
		for line in stdout:
			print(line.strip('\n'))
		client.close()
	
	elif node == 1:
		print("Ready Query Node-1..........")
		Query = input("Enter the Reguler Expression / Query: \n 1. -c -- This prints only a count of the lines that match a pattern. \n 2. -h -- Display the matched lines, but do not display the filenames. \n 3. -i -- Ignores, case for matching .\n 4. -l -- Displays the list of filenames only. \n 5. -v -- This prints out all the lines that do not match the pattern. \n 6. -e exp -- Specifies expression with this option can be used multiple times. \n 7. -f file -- Takes pattern from file, one per line. \n 8. -E -- Treats pattern as an extended reguler expression. \n 9. -w -- Match whole word. \n 10. -0 -- Print every matched line on seperate line. \n 11. -A n -- Prints only searched line and n lines after the result. \n 12. -B n -- Prints searched line and n lines before the result. \n 13. -C n -- Prints n lines before and after the result. \n 14. -n -- Display the matched lines and there line numbers. \n Your Selected Character is: ")
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect('192.168.1.11', username='UserName', password='password')   # change the ipaddress, username, password according to the machine your querien
		# stdin, stdout, stderr= client.exec_command('cat /proc/meminfo')
		stdin, stdout, stderr = client.exec_command('grep ' + Query)
		for line in stdout: 
			print(line.strip('\n'))
		client.close()
	
	elif node == 2:
		print("Ready Query Node-2..........")
		Query = input("Enter the Reguler Expression / Query: \n 1. -c -- This prints only a count of the lines that match a pattern. \n 2. -h -- Display the matched lines, but do not display the filenames. \n 3. -i -- Ignores, case for matching .\n 4. -l -- Displays the list of filenames only. \n 5. -v -- This prints out all the lines that do not match the pattern. \n 6. -e exp -- Specifies expression with this option can be used multiple times. \n 7. -f file -- Takes pattern from file, one per line. \n 8. -E -- Treats pattern as an extended reguler expression. \n 9. -w -- Match whole word. \n 10. -0 -- Print every matched line on seperate line. \n 11. -A n -- Prints only searched line and n lines after the result. \n 12. -B n -- Prints searched line and n lines before the result. \n 13. -C n -- Prints n lines before and after the result. \n 14. -n -- Display the matched lines and there line numbers. \n Your Selected Character is: ")
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect('192.168.1.12', username='UserName', password='password')   # change the ipaddress, username, password according to the machine your querien
		# stdin, stdout, stderr = client.exec_command('cat /proc/meminfo')
		stdin, stdout, stderr = client.exec_command('grep ' + Query)
		for line in stdout:
			print(line.strip('\n'))
		client.close()

	elif node < 0 or node > 2:
		print("No such Server Node Exists!")
