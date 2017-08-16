import socket
import sys
import logging
import time
import datetime
from logging.handlers import TimedRotatingFileHandler
import os



print('START')
os.chdir("/home/delkov/Documents/MOSCOW/ECO_COMPLETE/sbs_store")
log_file = "sbs"
logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler(log_file, when="s", interval=1, backupCount=0)
logger.addHandler(handler)
buffer_size=1024# sleep_time=0

# big_log_file="big_log.txt"

while True:
	time.sleep(1) # avoid flood
	try:
# Create a TCP/IP socket
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
		server_address = ('localhost', 1489)
		sock.connect(server_address)
		print('after break')
		while 1:
			data = sock.recv(buffer_size)
			if not data:
				break
			print(data)



			# with open(big_log_file, 'a+') as f1:
				# f1.write(data)


			# f.write(data)
			logger.info(data.rstrip().decode('UTF-8'))

	except Exception as e:
		print(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + '\n' +str(e))
		# sleep_time=0.1


	finally:
		print('PROGAM FINISHED')
		sock.close()
    # print >>sys.stderr, 'closing socket'
    # sock.close()
