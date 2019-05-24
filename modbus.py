#!/usr/bin/env python
# scripts/examples/simple_tcp_client.py
import socket
import time

from umodbus import conf
from umodbus.client import tcp
from datetime import datetime

# Enable values to be signed (default is False).
conf.SIGNED_VALUES = True

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('10.10.53.10', 502))

# Returns a message or Application Data Unit (ADU) specific for doing
# Modbus TCP/IP.
starttime=time.time()
while True:
    message = tcp.read_holding_registers(slave_id=2, starting_address=3205, quantity=1)
    response = tcp.send_message(message, sock)
    print(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f): "), response)
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))

# Response depends on Modbus function code. This particular returns the
# amount of coils written, in this case it is.

sock.close()
