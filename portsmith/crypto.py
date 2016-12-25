from cryptography.fernet import Fernet

class CryptoMethd:
	
	def __init__(self):
		self.key = Fernet.generate_key()
		self.cipher_suite = Fernet(self.key)
		

	def encrypt(self, plaintext):

		encrypted = self.cipher_suite.encrypt(plaintext)
		return encrypted
	
		
	def decrypt(self, ciphertext):
		decrypted = self.cipher_suite.decrypt(ciphertext)
		return decrypted
