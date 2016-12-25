
## will write setup script when the project is good enough to be distriuted :P

import sys, os , shutil



setup ( name = 'portsmith',
		version = '0.1',
		description = 'Secure Port Knocking Implementation',
		author = 'Nikhil. R',
		author_email = 'rnikhil96@outlook.com',
		url = 'https://github.com/rnikhil275/Portsmith',
		license = 'GPL',
		packages=["portsmith", "portsmith.proxy"],
		)