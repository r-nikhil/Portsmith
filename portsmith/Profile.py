import os, string

from portsmith.crypto import CryptoMethd

class Profile:

	def __init__(self, directory, knockPort):
		self.directory = directory
		self.knockPort = knockPort
		self.cryptoMethd = CryptoMethd()



	def getKnockPort(self):
		return self.knockPort

	def loadKey(self, keyFile):
		file = open(keyFile, 'rb+')
		key = file.readline()
		file.close
		return key

	def storeKey(self):
		file = open(self.directory + "/enc.key", 'wb')
		file.write(self.cryptoMethd.key)
		file.close()

	def storePort(self):
		file = open(self.directory + "/port.txt", 'w')
		file.write(str(self.knockPort))
		file.close


	def encrypt(self, plaintext):
		return self.CryptoMethd.encrypt(plaintext)

	def decrypt(self, ciphertext):
		return self.CryptoMethd.decrypt(ciphertext)


