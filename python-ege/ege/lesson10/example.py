from ipaddress import ip_network
net = ip_network("172.16.47.130/255.255.248.0", strict=False)
address = str(net.network_address)
print(address)
print(sum(map(int, address.split("."))))
