import os, sys
from portsmith.log import Log
from portsmith.profiles import Profiles
from portsmith.knocklsiten import knockListener
from portsmith.PortOpener import PortOpener
def checkConditions():
	if(not os.geteuid() == 0):
		print("run the server code as root")
		sys.exit()

	if(not os.path.isdir('/etc/portsmith.d/profiles/')):
		print("generate profiles first ")
		sys.exit()

def handleFirewall(input, config):
	portOpener = PortOpener(input)
	portOpener.waitForKnocks()

def knockHandler(output, profiles):
	portOpener = PortOpener(output)
	knockListener = KnockListener(logFile, profiles, portOpener)

def main(argv):
	logFile = Log('/var/log/kern.log') 
	checkConditions()

	knockHandler(os.fdopen(output, "w"), profiles)




if __name__ == '__main__':
	main(sys.argv)