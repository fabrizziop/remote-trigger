import gc
import webrepl
import network
import time
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
	sta_if.active(True)
	sta_if.connect('YOUR_WIFI_SSID','YOUR_WIFI_PSK')
	while not sta_if.isconnected():
		pass
sta_if.ifconfig(('IP', 'NETMASK', 'GATEWAY', 'DNS'))
webrepl.start()
gc.collect()
