import ipaddress

IPv4addresses = [('192.168.45.5',24),\
                 ('194.15.10.10',20),\
                 ('128.45.78.1',16),\
                 ('120.11.10.9',32),\
                 ('95.255.255.4',8),\
                 ('41.45.11.5',2),\
                 ('48.45.10.8',10),\
                 ('45.74.74.74',30),\
                 ('12.12.4.5',26),\
                 ('10.78.1.9',4)]
                 
for address in IPv4addresses:
    IPv6prefix = address[1]+16*6
    
    IPv6_4 = ("::FFFF:{}/{}".format(address[0],IPv6prefix))
    
    IPv6 = ipaddress.IPv6Interface(IPv6_4)
    print("%s/%i gets converted to %s" % (address[0],address[1],IPv6))