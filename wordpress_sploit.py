from exploit_configuration import *
from urllib import *
from argparse import *

"""
class version(Action):
	def __call__(self, parser, namespace, values, option_string=None):
		print 'ok'

class uri(Action):
	def __call__(self, parser, namespace, values, option_string=None):
		print 'serveur'

parser = ArgumentParser()
parser.add_argument('S', action=uri, nargs=1, help='Definir le serveur cible')
parser.add_argument('-P', action=version, nargs=1, help='Load your plugin')
args = parser.parse_args()
"""
ExploitConfiguration('C:/Users/0pc0deFR/Desktop/Wordpress Sploit/exploits/WordPress_bib2html_0_9_3_Cross_Site_Scripting', 'C:/Users/0pc0deFR/Desktop/Wordpress Sploit/payloads/alert', 'http://serveur/')