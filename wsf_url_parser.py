from sys import *
import os.path
from urlparse import *

def PrintHelp():
    print "This tool help for extract all parms informations in URL!\n"
    print "Example: %s URL\n" %argv[0]

def WriteOutput(write_output):
    if(os.path.isfile('exploit') == False):
        output = file('exploit', 'w')
        output.write('[Base]\n')
        output.write('title=\n')
        output.write('description:\n')
        output.write('version=\n')
        output.write('author=\n')
        output.write('date=\n')
        output.write('type=\n\n')
        output.write('[Identifiers]\n')
        output.write('EDB=\n')
        output.write('CVE=\n\n')
        output.write('[Exploitation]\n')
        output.write('method=\n')
        output.write('url=\n\n')
        output.write('[Parameters]\n')
        output.close()
    output = file('exploit', 'a')
    output.write(write_output + '\n')
    output.close()

print "WordPress Sploit Framework - URL Parser - V1.0\n"
if(len(argv) < 2):
	PrintHelp()
else:
	parse = urlparse(argv[1])
	params = parse_qs(parse[4])
	for key in params:
		WriteOutput(key + '=' + params[key][0])