import sys 
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit
from PyQt5 import QtCore
from PyQt5.Qt import Qt

o = ""
cmd = ""

class Example(QMainWindow):
	
	def __init__(self):
		super().__init__()
		self.o = None
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

	def onChanged(self, text):
		self.qlabel.setText(text)
		self.qlabel.adjustSize()
		cmd = f"cd /usr/share/applications && ls | sed -e 's/\.desktop$//' | sed -e 's/\org.gnome.//' | grep {text} | head -1"
		o = os.popen(cmd)
		self.o = o.read()
		print(self.o)

	def run(self):
		a = f'''cd /usr/share/applications && cat $fn | grep "^Exec*" | awk '{gsub("Exec=", "");print}''''
		


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
