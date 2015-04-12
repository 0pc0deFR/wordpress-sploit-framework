from exploit_configuration import *
from print_lists import *
from sys import *

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
		elif(arg == "-P"):
			self.PrintListPlugins()
			#List plugins
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
		print "-P: List plugins"
		print "-h: Print this help"

	def PrintListPayloads(self):
		print_list_payloads =  PrintLists()
		print_list_payloads.PrintListPayloads()

	def PrintListExploits(self):
		print_list_exploits =  PrintLists()
		print_list_exploits.PrintListExploits()

	def PrintListPlugins(self):
		print_list_plugins = PrintLists()
		print_list_plugins.PrintListPlugins()

Loader(argv)