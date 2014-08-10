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
	def __init__(self, list_plugin):
		self.list_plugin = list_plugin

	def load_func_payload(self, payload, method, type_exploit):
		self.payload = payload
		self.method = method
		self.type_exploit = type_exploit
		for plugin in self.list_plugin:
			if plugin.find('.pyc') == -1:
				self.import_plugin = imp.load_source(plugin[len(plugin)-3], './plugins/%s' % plugin)
				try:
					self.payload = self.import_plugin.payload(self.payload, self.method, self.type_exploit)
				except:
					self.except_error = ''
		return self.payload