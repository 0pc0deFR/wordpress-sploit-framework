from exploit_configuration import *
from print_lists import *
from sys import *
from os import *

class Loader:
	def __init__(self, argv):
		self.exploit = self.payload = self.target = None
		self.LoadArgs(argv)
		if(self.exploit != None and self.payload != None and self.target != None):
			ExploitConfiguration(self.exploit, self.payload, self.target)
		elif(len(argv) < 2):
			self.PrintHelp()

	def LoadArgs(self, args):
		len_args = len(args)
		i = 1 #Ignore le nom du fichier en cours d'execution
		while(i < len_args):
			if(self.LoadArg(args[i])==0):
				if(i == 1):
					self.exploit = './exploits/' + args[i]
				elif(i == 2):
					self.payload = './payloads/' + args[i]
				elif(i == 3):
					self.target = args[i]
			i=i+1

	def LoadArg(self, arg):
		if(arg == "-p"):
			#List payloads
			self.PrintListPayloads()
		elif(arg == "-e"):
			self.PrintListExploits()
			#List exploits
		elif(arg == "-Pe"):
			self.PrintListPluginsEnabled()
			#List plugins enabled
		elif(arg == "-Pa"):
			self.PrintListPluginsAvailable()
			#List plugins available
		elif(arg == '-Pen'):
			self.PluginEnable(argv[2])
		elif(arg == '-Pdis'):
			self.PluginDisable(argv[2])
		elif(arg == "-h"):
			self.PrintHelp()
		else:
			return 0

	def PrintHelp(self):
		print "WordPress Sploit Framework\n"
		print "Example: %s [Exploit] [Payload] [Target]\n" %argv[0]
		print "Help:"
		print "-p: List payloads"
		print "-e: List exploits"
		print "-Pe: List plugins enabled"
		print "-Pa: List plugins available"
		print "-Pen [PLUGIN]: Enable the plugin"
		print "-Pdis [PLUGIN]: Disable the plugin"
		print "-h: Print this help"

	def PrintListPayloads(self):
		print_list_payloads =  PrintLists()
		print_list_payloads.PrintListPayloads()

	def PrintListExploits(self):
		print_list_exploits =  PrintLists()
		print_list_exploits.PrintListExploits()

	def PrintListPluginsEnabled(self):
		print_list_plugins = PrintLists()
		print_list_plugins.PrintListPluginsEnabled()

	def PrintListPluginsAvailable(self):
		print_list_plugins = PrintLists()
		print_list_plugins.PrintListPluginsAvailable()

	def PluginEnable(self, plugin):
		if(path.isfile('./plugins-available/' + plugin)):
			system('ln -s ../plugins-available/' + plugin + ' ./plugins-enabled/' + plugin)
		else:
			print('No file exist!')

	def PluginDisable(self, plugin):
		if(path.isfile('./plugins-enabled/' + plugin)):
			system('rm -r ./plugins-enabled/' + plugin)
		else:
			print('No file exist!')

Loader(argv)