from ipaddress import ip_network
net = ip_network("192.168.10.77/26", strict=False)
print(net.network_address)
print(net.netmask)
print(net.num_addresses)
print(sum(bin(int(ip)).count("1") % 2 == 0 for ip in net))
