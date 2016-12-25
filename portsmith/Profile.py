import os, string
import ConfigParse

from CryptoMethd import CryptoMethd

class Profile:

	def __init__(self, directory, knockPort=None, cipherKey):
		self.directory = directory
		self.name = directory.rstrip('/').split('/')[-1]
		self.knockPort = knockPort
		# instance of the crypto methods
		self.CryptoMethd = CryptoMethd(self, self.cipherKey)



	def getName(self):
		return self.name

	def getKnockPort(self):
		return self.knockPort



	def storeKey(self, key, path):
		file = open(path, 'w')
		file.write(binascii.b2a_base64(key))
		file.close()


	def encrypt(self, plaintext):
		return self.CryptoMethd.encrypt(plaintext)

	def decrypt(self, ciphertext):
		return self.CryptoMethd.decrypt(ciphertext)