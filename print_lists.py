from exploit_configuration import *
from read_configuration import *
from plugins_loader import *
from os import *

class PrintLists:
	def PrintListExploits(self):
		exploits = listdir('./exploits/')
		for exploit in exploits:
			BaseConfiguration('./exploits/'+exploit, True)
			print "	Filename: %s" %exploit

	def PrintListPayloads(self):
		payloads = listdir('./payloads/')
		for payload in payloads:
			PayloadConfiguration('./payloads/'+payload, True, '')
			print "	Filename: %s" %payload

	def PrintListPlugins(self):
		plugins = listdir('./plugins/')
		PluginLoader(plugins, True)