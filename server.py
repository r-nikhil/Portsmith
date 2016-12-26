import os, sys
from portsmith.log import Log
from portsmith.knocklsiten import knockListener

def checkConditions():
	if(not os.geteuid() == 0):
		print("run the server code as root")
		sys.exit()

	if(not os.path.isdir('/etc/portsmith.d/profiles/')):
		print("generate profiles first ")
		sys.exit()


def main(argv):
	logFile = Log('/var/log/kern.log')
	knockListener = KnockListener(logFile)
	 
	checkConditions()





if __name__ == '__main__':
	main(sys.argv)