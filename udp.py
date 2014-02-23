import output
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

class Print(output.Output):
	requiredData = []
	optionalData = []
	def __init__(self,data):
		pass
	def outputData(self,dataPoints):
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Internet/UDP
		for i in dataPoints:
			print i["name"] + ": " + str(i["value"]) + " " + i["symbol"]
                        val = "%.1f" % (i["value"])
                        sock.sendto(i["name"]+":"+val, (UDP_IP, UDP_PORT))
		return True
