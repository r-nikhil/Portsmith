from cryptography.fernet import Fernet 







Class CrytoMethd:
	
	def __init__(self, profile):
		self.profile = profile
		self.key = Fernet.generate_key()
		self.f = Fernet(self.key)
		

	def encrypt(self, plaintext):

		encrypted = self.f.encrypt(plaintext)
		return encrypted

		
		return encrypted

	def decrypt(self, ciphertext):
		decrypted = self.f.decrypt(ciphertext)
		return decrypted
