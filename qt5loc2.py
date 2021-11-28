import sys 
import time
import io
import os
import re
import pickle
import tempfile
import subprocess
from subprocess import check_output
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit
from PyQt5 import QtCore
from PyQt5.Qt import Qt

o = ""
cmd = ""

class Example(QMainWindow):
	
	def __init__(self):
		super().__init__()
		self.o = None
		self.path = None
		self.a = None
		self.lineEntry = QLineEdit(self)
		self.lineEntry.returnPressed.connect(self.bar)
		self.lineEntry.returnPressed.connect(self.run)

		self.lineEntry.move(16,16)
		self.lineEntry.resize(200,40)

		self.qlabel = QLabel(self)
		self.qlabel.move(16,64)

		self.lineEntry.textChanged.connect(self.onChanged)
		
		self.setGeometry(50,50,320,200)
		self.setWindowTitle("QLineEdit Example")
		self.show()

	def onChanged(self, text):
		self.qlabel.adjustSize()		
		cmd = f"cd /usr/share/applications && ls -1 | grep {text}"
		path = subprocess.check_output(cmd, shell=True).decode('ascii').strip()
		appname = f"cat /usr/share/applications/{path}"
		name = subprocess.check_output(appname, shell=True).decode('ascii', 'ignore')
		print(name)
		#print(f"{name} !!!!!!")
		#self.name = name
		#path = os.path.join('/tmp', 'ls.txt')
		#print(self.name)
		#file = open(path, "w")
		#file.write(self.name)
		#self.qlabel.setText(name)
		#barw = "sh ~/code/appLauncher/barupdate.sh"
		#subprocess.run(barw, shell=True)


#tmp = tempfile.NamedTemporaryFile()
#		with open(tmp.name, 'w') as f:
#			f.write(name)
#		#use readline for a grep like function
#		with open(tmp.name) as f:
#			for line in f.readlines():
#				if 'Exec=' in line:
#					f = io.StringIO()
#					print(line, file=f)
#		
		

	def bar(self):
		pid = """cd /tmp && ls | grep "polybar" | sed 's/[^0-9]//g'"""
		pidc = subprocess.check_output(pid, shell=True).decode('ascii')
		print(pidc)
		path = os.path.join('/tmp', 'ls.txt')
		print(path)
		print(f"{self.name} tessssst")
		file = open(path, "w")
		file.write(self.name)
		barr = "echo hook:module/demo1 >>/tmp/polybar_mqueue.*"
		barw = f"echo hook:module/demo2 >>/tmp/polybar_mqueue.*"
		subprocess.run(barr, shell=True)
		subprocess.run(barw, shell=True)
		#print(a).decode('ascii')

	def run(self):
		a = f"""cd /usr/share/applications && cat {self.path}""" 
		a.self = a
		#cm2 = (a2 + b2)
		#i dont think these errors in this ascii decode should be ignored but oh well
		o2 = subprocess.check_output(a, shell=True).decode('ascii', 'ignore')
		#create a temp file so that i can...
		tmp = tempfile.NamedTemporaryFile()
		with open(tmp.name, 'w') as f:
			f.write(o2)
		#use readline for a grep like function
		with open(tmp.name) as f:
			for line in f.readlines():
				if 'Exec=' in line:
					f = io.StringIO()
					print(line, file=f)
		a = f.getvalue()
		exec = a.replace("Exec=", "")
		run = subprocess.run(f'{exec} & disown', shell=True)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
