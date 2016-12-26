import syslog
from portsmith.LogEntry import LogEntry
from portsmith.Profile import Profile


class knockListener:

	def __init__(self, logFile, profiles):
		self.logFile = logFile
		self.profiles = profiles


	def listenAndOpen(self):
		for line in self.logFile.tail():
			try:
				logEntry = LogEntry(line)
				#getProfileforPOrt searches through all port.txt files and finds the correct encryption key
				profile = self.profiles.getProfileforPort(logEntry.getDestinationPort())

				if (profile != None):

					ciphertext = logEntry.getEncryptedData()
					port = profile.decrypt(ciphertext)
					sourceIP = logEntry.getSourceIP()

					self.portOpener.open(sourceIP, port)
					syslog.syslog("opening port for " + sourceIP + "at " + str(port))





			except:
				syslog.syslog("cant read log")