from cryptography.fernet import Fernet
key = Fernet.generate_key()

file = open('test.key' , 'wb')
file.write(key)
file.close


file = open('test.key', 'rb+')
key1 = file.readline()
file.close

if key == key1:
	print("at last this is over")