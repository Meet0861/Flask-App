import os
"""
JWT_SECRET_KEY is set as environ. 
It is set by docker to the current environ 
"""
class LocalConfig():
	DEBUG = False
	TESTING = False
	LOG_LEVEL = 'DEBUG'
	JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 1)