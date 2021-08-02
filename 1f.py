import socket

host = socket.gethostname()
host_ipAddress = socket.gethostbyname(host)
remote_host = 'www.naver.com'
ipAddress = socket.gethostbyname(remote_host)
packedIp = socket.inet_aton(ipAddress)
unpackedIp = socket.inet_ntoa(packedIp)
 
print(f"네이버 IP: {ipAddress}")
print(f"Packed IP : {packedIp}")
print(f"Unpacked IP : {unpackedIp}")
print(f"Host : {host}")
print(f"Host ip : {host_ipAddress}")

