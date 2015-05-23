import os
import imp

class PluginsLoader:
	"""
	Permet de charger les plugins
	"""
	def __init__(self, plugins_dir):
		if(os.path.isdir(plugins_dir)):
			self.dir = plugins_dir
			self.tab_plugins = []

	def load_plugins(self, plugin_name):
		return os.listdir(self.dir)

class PluginLoader:
	def __init__(self, list_plugin, type_dir, Printing = False):
		self.list_plugin = list_plugin
		if Printing == True:
			if type_dir == "available":
				self.print_plugin_configuration_available()
			elif type_dir == "enabled":
				self.print_plugin_configuration_enabled()

	def load_func_payload(self, payload, method, type_exploit):
		self.payload = payload
		self.method = method
		self.type_exploit = type_exploit
		for plugin in self.list_plugin:
			if plugin.find('.pyc') == -1:
				self.import_plugin = imp.load_source(plugin[:len(plugin)-3], './plugins-enabled/%s' % plugin)
				try:
					self.payload = self.import_plugin.payload(self.payload, self.method, self.type_exploit)
				except:
					self.except_error = ''
		return self.payload

	def load_func_parameters(self, parameters, method, type_exploit):
		self.parameters = parameters
		self.method = method
		self.type_exploit = type_exploit
		for plugin in self.list_plugin:
			if plugin.find('.pyc') == -1:
				self.import_plugin = imp.load_source(plugin[:len(plugin)-3], './plugins-enabled/%s' % plugin)
				try:
					self.parameters = self.import_plugin.parameters(self.parameters, self.method, self.type_exploit)
				except:
					self.except_error = ''
		return self.parameters

	def load_func_exploit(self, url, parameters, method, type_exploit):
		self.url = url
		self.parameters = parameters
		self.method = method
		self.type_exploit = type_exploit
		self.exploit = True
		for plugin in self.list_plugin:
			if plugin.find('.pyc') == -1:
				self.import_plugin = imp.load_source(plugin[:len(plugin)-3], './plugins-enabled/%s' % plugin)
				try:
					self.exploit = self.import_plugin.exploit(self.url, self.parameters, self.method, self.type_exploit)
				except:
					self.except_error = ''
		return self.exploit

	def print_plugin_configuration_available(self):
		for plugin in self.list_plugin:
			if plugin.find('.pyc') == -1:
				self.import_plugin = imp.load_source(plugin[:len(plugin)-3], './plugins-available/%s' % plugin)
				try:
					print '\nPlugin:'
					print '	Title:', self.import_plugin.title()
					print '	Description:', self.import_plugin.description()
					print '	Author:', self.import_plugin.author()
					print '	Filename: ', plugin
				except:
					self.except_error = ''

	def print_plugin_configuration_enabled(self):
		for plugin in self.list_plugin:
			if plugin.find('.pyc') == -1:
				self.import_plugin = imp.load_source(plugin[:len(plugin)-3], './plugins-enabled/%s' % plugin)
				try:
					print '\nPlugin:'
					print '	Title:', self.import_plugin.title()
					print '	Description:', self.import_plugin.description()
					print '	Author:', self.import_plugin.author()
					print '	Filename: ', plugin
				except:
					self.except_error = ''