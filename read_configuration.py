import ConfigParser


class BaseConfiguration:
	"""
	Permet de lire la section [Base] du fichier de configuration
	"""
	def __init__(self, file_configuration, printing):
		"""
		Creer une instance de ConfigParser et charge toutes les informations de la section [Base]
		"""
		self.config = ConfigParser.ConfigParser()
		self.config.readfp(open(file_configuration))
		self.read_title()
		self.read_description()
		self.read_version()
		self.read_author()
		self.read_date()
		self.read_type()
		if(printing == True):
			self.print_base_configuration()

	def read_title(self):
		"""
		Recupere le titre
		"""
		self.title = self.config.get('Base', 'title')
		return self.title

	def read_description(self):
		"""
		Recupere la description
		"""
		self.description = self.config.get('Base', 'description')
		return self.description

	def read_version(self):
		"""
		Recupere la version
		"""
		self.version = self.config.get('Base', 'version')
		return self.version

	def read_author(self):
		"""
		Recupere l'auteur
		"""
		self.author = self.config.get('Base', 'author')
		return self.author

	def read_date(self):
		"""
		Recupere la date
		"""
		self.date = self.config.get('Base', 'date')
		return self.date

	def read_type(self):
		"""
		Recupere le type d'exploit
		"""
		self.type = self.config.get('Base', 'type')
		return self.type

	def print_base_configuration(self):
		print '\nExploit Configuration:'
		print "	Title:", self.title
		print "	Description:", self.description
		print "	Version:", self.version
		print "	Author:", self.author
		print "	Date:", self.date
		print "	Exploit type:", self.type



class ExploitationConfiguration:
	def __init__(self, file_configuration):
		self.config = ConfigParser.ConfigParser()
		self.config.readfp(open(file_configuration))
		self.read_method()
		self.read_url()
		self.read_parameters()

	def read_method(self):
		self.method = self.config.get('Exploitation', 'method')
		return self.method

	def read_url(self):
		self.url = self.config.get('Exploitation', 'url')
		return self.url

	def read_parameters(self):
		self.tab = {}
		self.parameters = self.config.options('Parameters')
		for i in range(len(self.parameters)):
			self.tab[self.parameters[i]] = self.config.get('Parameters', self.parameters[i])
		return self.tab



class PayloadConfiguration:
	"""
	Charge le payload
	"""
	def __init__(self, file_payload, printing):
		"""
		Creer une instance de ConfigParser et charge toutes les informations de la section [Payload]
		"""
		self.config = ConfigParser.ConfigParser()
		self.config.readfp(open(file_payload))
		self.read_title()
		self.read_description()
		self.read_payload()
		if(printing == True):
			self.print_payload_configuration()

	def read_title(self):
		"""
		Recupere le titre
		"""
		self.title = self.config.get('Payload', 'title')
		return self.title

	def read_description(self):
		"""
		Recupere la description
		"""
		self.description = self.config.get('Payload', 'description')
		return self.description

	def read_payload(self):
		"""
		Recupere le payload
		"""
		self.payload = self.config.get('Payload', 'payload')
		return self.payload

	def print_payload_configuration(self):
		print '\nPayload:'
		print '	Title:', self.title
		print '	Description:', self.description