import os
import urllib

SQLMAP_URI = '/usr/bin/sqlmap'

def title():
	return "WSF SQLMap Plugin"

def description():
	return "The plugin is a interface for SQLMap"

def author():
	return "0pc0deFR"

def payload(payload, method, type_exploit):
	if(type_exploit.lower() == 'sql'):
		payload = "[SQLMAP]"
	return payload

def exploit(url, parameters, method, type_exploit):
	global SQLMAP_URI
	if(type_exploit.lower() == 'sql' and os.path.isfile(SQLMAP_URI)):
		for key, value in parameters.items():
			if value == "[SQLMAP]":
				vulnerable_key = key
		try:
			dbms = input("You can define DBMS parameter for SQLMap:")
		except:
			dbms = None
		try:
			sql_query = input('You can define SQL Query parameter for SQLMap:')
		except:
			sql_query = None
		try:
			cookie = input('You can define Cookie parameter for SQLMap:')
		except:
			cookie = None
		parameters = urllib.urlencode(parameters)
		command = SQLMAP_URI
		if method.lower() == "get":
			command += " -u " + url+"?%s" % parameters
		elif method.lower() == "post":
			command += " -u " + url + " --data=" + parameters
		command += " -p '" + vulnerable_key + "'"
		if dbms != None:
			command += " --dbms=" + dbms
		if sql_query != None:
			command += " --sql_query=" + sql_query
		if cookie != None:
			command += " --cookie=" + cookie
 		os.system(command)
		return False
	else:
		return True