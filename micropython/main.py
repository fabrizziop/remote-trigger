import time
import usocket
from machine import Pin, ADC
from utime import sleep, ticks_ms

CONST_KEY = b"YOUR_32_BYTE_KEY" 

#ADD HERE ADDITIONAL PIN/RELAY COMBOS
CONST_PIN = {
0: Pin(5, Pin.OUT, value=0),
}

s = usocket.socket()
addr = usocket.getaddrinfo('0.0.0.0', 8001)[0][-1]
s.bind(addr)
s.listen(100)



def simple_data(ba):
	valid = True
	key = ba[0:32]
	trigger_id = int(ba[32])
	for i in range(0,32):
		if CONST_KEY[i] != key[i]:
			valid = False
	return [valid, trigger_id]

def get_data():
	conn, addr = s.accept()
	sdat = conn.recv(33)
	conn.close()
	return simple_data(sdat)

def cycle_pin(trigger_id):
	try:
		CONST_PIN[trigger_id].value(0)
		time.sleep(1)
		CONST_PIN[trigger_id].value(1)
		time.sleep(0.5)
		CONST_PIN[trigger_id].value(0)
		time.sleep(1)
	except:
		print("Cycle Pin Error")

def main_loop():
	while True:
		cur_data = get_data()
		print(cur_data)
		if cur_data[0] == True:
			cycle_pin(cur_data[1])
		time.sleep(1)

main_loop()
