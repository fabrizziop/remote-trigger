# remote-trigger
Remotely trigger something, using an ESP8266 with a relay near it.

The circuit should be very simple. Use as many relays as you want, I did a small 3.3V to 12V logic converter for the ESP, then triggered a MOSFET with it.

This is useful for restarting computers, turning on/off remote lights/LED strips. It is really barebones/proof of concept.

The key is merely for identifying and being sure the client will only trigger the right equipment. TLS should be use in hostile network enviroments!. I probably will implement it when I do something really useful with this.
