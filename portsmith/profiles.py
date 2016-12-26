import os
from Profile import Profile

class Profiles:

	def __init__(self, directory):
		self.profiles = list()

		for item in os.listdir(directory):
			if os.path.isdir(os.path.join(directory, item)):
				self.profiles.append(Profile(os.path.join(directory, item)))

	def getProfileForPort(self, port):
		for profile in self.profiles:
			# open all port.txt and find out the actual port ?
			#figure out better way to do this


		return

