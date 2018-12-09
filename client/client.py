import socket
import time

CONST_KEY = b"YOUR_32_BYTE_KEY" 
CONST_REMOTE_IP = "ESP8266_IP_ADDRESS"
CONST_REMOTE_PORT = 8001
addr = socket.getaddrinfo(CONST_REMOTE_IP, CONST_REMOTE_PORT)[0][-1]

def send_reset(key, trigger_id):
	s = socket.socket()
	s.settimeout(1)
	try:
		s.connect(addr)
		sdat = s.send(bytearray(CONST_KEY)+bytearray(trigger_id.to_bytes(1, byteorder="little")))
		s.close()
		return "  DATA SEND OK  "
	except:
		return " DATA SEND FAIL "
print(send_reset(CONST_KEY,0))
