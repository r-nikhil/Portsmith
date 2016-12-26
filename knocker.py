import os, sys
import subprocess
from struct import *
from cryptography.fernet import Fernet

homedir = os.path.expanduser('~')

if not os.path.isdir(homedir + '/.portsmith/'):
	print "create .portsmith directory and get enc.key and port.txt"
	sys.exit()

keyFile = open(homedir + '/.portsmith/enc.key', 'rb+')
key = keyFile.readline()
keyFile.close()

portFile = open(homedir + '/.portsmith/port.txt', 'r')
knockPort = int(portFile.readline())
portFile.close()

cipher_suite = Fernet(key)

def main(argv):
	portToOpen = argv[1]
	host = argv[2]


	portToOpen = pack('!H', int(portToOpen))
	packetData = cipher_suite.encrypt(portToOpen)

	(idField, seqField, ackField, winField) = unpack('!HIIH', packetData)
	knock = ["hping3", "-S", "-c", "1",
			"-p", str(knockPort),
			"-N", str(idField),
			"-w", str(winField),
			"-M", str(seqField),
			"-L", str(ackField),
			host]

	try:
		subprocess.call(knock, shell = False)
		print("knocked")

	except OSError:
		print("is hping3 installed ?")
		sys.exit()


if __name__ = '__main__':
	main(sys.argv)