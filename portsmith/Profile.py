import os, string
import ConfigParse

from crytography.fernet import Fernet
class Profile:

	def __init__(self, directory, knockPort):
		self.directory = directory
		self.knockPort = knockPort
		


	def getKnockPort(self):
		return self.knockPort

	def loadKey(self, keyFile):
		file = open(keyFile, 'rb+')
		key = file.readline()
		file.close
		return key

	def storeKey(self, key, path):
		file = open(self.directory + "/enc.key", 'w')
		file.write(key)
		file.close()

	def storePort(self):
		file = open(self.directory + "port.txt", 'w')
		file.write(str(knockPort))
		file.close

	def store():
		self.storeKey()
		self.storePort()


	def encrypt(self, plaintext):
		return self.CryptoMethd.encrypt(plaintext)

	def decrypt(self, ciphertext):
		return self.CryptoMethd.decrypt(ciphertext)


