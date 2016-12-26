import subprocess, os, syslog, sys

class PortOpener:

	def __init__(self, stream):
		self.stream = stream


	def waitForKnocks(self):
		while True:
			sourceIP = self.stream.readline().rstrip("\n")
			port = self.stream.readline().rstrip("\n")

			iprule = 'iptables -I INPUT -m limit --limit 1/minute --limit-burst 1 -m state --state NEW -p tcp -s' + sourceIP + '--dport' + str(port) + '-j ACCEPT'
			command = iprule.split()

			subprocess.call(command, shell = False)


	def open(self, sourceIP, port):

		self.stream.write(sourceIP)
		self.stream.write(str(port))
		self.stream.flush