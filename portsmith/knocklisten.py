import syslog
from portsmith.LogEntry import LogEntry
from portsmith.Profile import Profile

class knockListener:

	def __init__(self, logFile, profiles):
		self.logFile = logFile


	def listenAndOpen(self):
		for line in self.logFile.tail():
			try:
				logEntry = LogEntry(line)




			except:
				syslog.syslog("cant read log")