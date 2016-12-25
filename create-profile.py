import os, sys
from portsmith.Profile import Profile


DAEMON_DIR = '/etc/portsmith.d'
PROFILES_DIR= DAEMON_DIR + 'profiles/'

def createDirectory(profileName):
	if not os.path.isdir(DAEMON_DIR):
		os.mkdir(DAEMON_DIR)

	if not os.path.isdir(PROFILES_DIR):
		os.mkdir(PROFILES_DIR)

	if not os.path.isdir(PROFILES_DIR + profileName):
		os.mkdir(PROFILES_DIR + profileName)


def main(argv):
	profileName = argv[0]
	knockPort = argv[1]

	createDirectory(profileName)
	profile = Profile(PROFILES_DIR + profileName, knockPort)
	profile.store()

	print("Profile generated at" + PROFILES_DIR + profileName)

if __name__ == '__main__':
	main(sys.argv[1:])

