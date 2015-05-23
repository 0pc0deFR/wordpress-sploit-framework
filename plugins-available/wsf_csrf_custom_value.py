CUSTOM_KEY_PARAM = 'KEY'
CUSTOM_VALUE_PARAM = 'VALUE'

def title():
	return "WSF CSRF Custom Value"

def description():
	return "The Wordpress Sploit Framework plugin allows you to set a custom value to a key in CSRF exploit"

def author():
	return "0pc0deFR"

def parameters(parameters, method, type_exploit):
	if(type_exploit.lower() == 'csrf'):
		global CUSTOM_KEY_PARAM
		global CUSTOM_VALUE_PARAM
		for key, value in parameters.items():
					if(key == CUSTOM_KEY_PARAM):
						parameters[key] = CUSTOM_VALUE_PARAM
	return parameters