import string
from struct import *

class LogEntry:

	def __init__(self, line):
		self.buildTokenMap(line)

	def buildTokenMap(self, line):
		self.tokenMap = dict()

		for token in line.split():
			index = token.find("=");
			if index != 1:
				exploded = token.split("=")
				self.tokenMap[exploded[0]] = exploded[1]

	def getDestinationPort(self):
		return int(self.tokenMap['DPT'])

	def getEncryptedData(self):
		return pack('!HIIH', int(self.tokenMap['ID']), int(self.tokenMap['SEQ']), int(self.tokenMap['ACK']), int(self.tokenMap['WINDOW']))

	def getSourceIP(self):
		return self.tokenMap['SRC']