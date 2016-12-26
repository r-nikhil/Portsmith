import os, sys

class Log:
	def __init__(self, file):
		self.file = file

	def tail(self):
		fd = open(self.file)
		fd.seek(0, os.SEEK_END)

		while True:
			where = fd.tell()
			line = fd.readline()

			if not line:
				time.sleep(.25)
				fd.seek(where)
			else:
				yield line