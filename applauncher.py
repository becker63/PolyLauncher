import sys 
import subprocess
import os
import configparser
import re
import glob
from PyQt5.QtWidgets import QApplication, QGraphicsOpacityEffect, QDialog, QLabel, QLineEdit
from PyQt5 import QtCore
from PyQt5.Qt import Qt

o = ""
cmd = ""

class Example(QDialog):
	
	def __init__(self):
		super().__init__()
		self.setWindowOpacity(0)
		self.rpath = None
		self.path = None
		self.appname = None
		self.lineEntry = QLineEdit(self)
		self.lineEntry.returnPressed.connect(self.run)

		self.lineEntry.move(16,16)
		self.lineEntry.resize(200,40)

		self.qlabel = QLabel(self)
		self.qlabel.move(16,64)

		self.lineEntry.textChanged.connect(self.onChanged)
		
		self.setGeometry(50,50,320,200)
		self.setWindowTitle("QLineEdit Example")
		self.show()
		self.paths()
		
	
	def paths(self):
		self.qlabel.adjustSize()		
		config = configparser.RawConfigParser()
		print(config.sections())
		#saves all .desktop files to an array
		path = glob.glob(f'/usr/share/applications/*.desktop')
		names = []
		for e in path:
			config.read(e)
			name = (config['Desktop Entry']['Name'])
			a = f'{name }={e}'
			names.append(a)
		snames = '\n'.join(names)
		print(snames)
		self.paths = snames
		

	def onChanged(self, text):
		rpath=""
		appname = ""
		print(self.paths)
		snames = self.paths
		
		cinput = text.capitalize()
		for line in snames.split('\n'):
			if cinput in line:
				t = re.sub(r'^.*?=', '=', line)
				rpath = t.replace("=", "") 
				print(rpath)
				break
		for line in snames.split('\n'):
			if cinput in line:
				sline = ''.join(line)
				format = sline.split("=", 1)
				appname = format[0] 
				print(appname)
				break
		self.rpath = rpath
		self.appname = appname
		
		path = os.path.join('/tmp', 'ls.txt')
		file = open(path, "w")
		file.write(self.appname)
		os.system('sh ~/code/appLauncher/barupdate.sh ')

	def bar(self):
		path = os.path.join('/tmp', 'ls.txt')
		file = open(path, "w")
		file.write(self.appname)
		os.system('echo hook:module/demo2 >>/tmp/polybar_mqueue.*')

	def run(self):
		config = configparser.RawConfigParser()
		print(self.rpath)
		config.read(self.rpath)
		exec = (config['Desktop Entry']['Exec'])
		print(exec)
		subprocess.run(f'{exec} & disown', shell=True)
		exit()
		

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())