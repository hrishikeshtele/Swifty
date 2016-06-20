import time
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from random import *
import login_pg
import sqlite3

conn = sqlite3.connect('swifty.db')
receipt=0
try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

form_class = uic.loadUiType("main_final.ui")[0]
alp="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTXVWXYZ _"
no="1234567890_"

class MyWindowClass(QtGui.QMainWindow, form_class):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.Form = QtGui.QMainWindow()
		self.log = login_pg.Ui_MainWindow()
		self.log.setupUi(self.Form)
		self.Form.showFullScreen()
		print "init" 
		self.log.login.clicked.connect(self.done_login)
	def done_login(self):
		global receipt		
		name=self.log.nam.text()
		college=self.log.col.text()
		receipt=self.log.rec.text()
		mobile=self.log.mob.text()
		a=[]
		flag = 0
		print name,college,mobile,receipt		
		if(college=="" or name=="" or receipt=="" or mobile==""):		
			a.append('Fill all details')
			flag = 1
		for i in range(len(name)):
			if(str(name[i]) not in alp):
				a.append('Enter valid name')
				flag = 1
				break
		for i in range(len(college)):
			if(str(college[i]) not in alp):
				a.append('Enter valid college name')
				flag = 1
				break
		if(len(mobile)!=10):
			a.append('Phone no should be 10 digits long')
			flag = 1
		for i in range(len(mobile)):
			if(str(mobile[i]) not in no):
				a.append('mobile: Enter only numbers')
				flag = 1
				break
		for i in range(len(receipt)):
			if(str(receipt[i]) not in no):
				a.append('Receipt: Enter only numbers')
				flag = 1
				break
		for i in range(6-len(a)):
			a.append("")
		if flag == 0:
			#sqlstr1=
			conn.execute("INSERT OR IGNORE INTO swift values(?,?,?,?)",(str(name),str(receipt),str(college),str(mobile)))
			conn.commit()
			print "done"			
			self.begin()
		else:
			QMessageBox.about(self,'error','%s\n%s\n%s\n%s\n%s\n%s' %(a[0],a[1],a[2],a[3],a[4],a[5]))
		

	def begin(self):
		self.Form.hide()
		self.setupUi(self)
		self.showFullScreen()		
		self.para=	{
			0 : "The first major grouping of Shakespeare plays begins with his histories and comedies of the 1590s. Shakespeare's earliest plays tended to be adaptations of other playwright's works and employed blank verse and little variation in rhythm.",
			1 : "Whether or not you believe in God, you must believe this: when we as a species abandon our trust in a power greater than us, we abandon our sense of accountability. Faiths... all faiths... are admonitions that there is something we cannot understand, something to which we are accountable. With faith we are accountable to each other, to ourselves, and to a higher truth. Religion is flawed, but only because man is flawed. The church consists of a brotherhood of imperfect, simple souls wanting only to be a voice of compassion in a world spinning out of control.",
			2 : "Whether or not you believe in God, you must believe this: when we as a species abandon our trust in a power greater than us, we abandon our sense of accountability. Faiths... all faiths... are admonitions that there is something we cannot understand, something to which we are accountable. With faith we are accountable to each other, to ourselves, and to a higher truth. Religion is flawed, but only because man is flawed. The church consists of a brotherhood of imperfect, simple souls wanting only to be a voice of compassion in a world spinning out of control.",
			3 : "Whether or not you believe in God, you must believe this: when we as a species abandon our trust in a power greater than us, we abandon our sense of accountability. Faiths... all faiths... are admonitions that there is something we cannot understand, something to which we are accountable. With faith we are accountable to each other, to ourselves, and to a higher truth. Religion is flawed, but only because man is flawed. The church consists of a brotherhood of imperfect, simple souls wanting only to be a voice of compassion in a world spinning out of control.",
			4 : "Whether or not you believe in God, you must believe this: when we as a species abandon our trust in a power greater than us, we abandon our sense of accountability. Faiths... all faiths... are admonitions that there is something we cannot understand, something to which we are accountable. With faith we are accountable to each other, to ourselves, and to a higher truth. Religion is flawed, but only because man is flawed. The church consists of a brotherhood of imperfect, simple souls wanting only to be a voice of compassion in a world spinning out of control.",
			5 : "Whether or not you believe in God, you must believe this: when we as a species abandon our trust in a power greater than us, we abandon our sense of accountability. Faiths... all faiths... are admonitions that there is something we cannot understand, something to which we are accountable. With faith we are accountable to each other, to ourselves, and to a higher truth. Religion is flawed, but only because man is flawed. The church consists of a brotherhood of imperfect, simple souls wanting only to be a voice of compassion in a world spinning out of control.",
			6 : "Whether or not you believe in God, you must believe this: when we as a species abandon our trust in a power greater than us, we abandon our sense of accountability. Faiths... all faiths... are admonitions that there is something we cannot understand, something to which we are accountable. With faith we are accountable to each other, to ourselves, and to a higher truth. Religion is flawed, but only because man is flawed. The church consists of a brotherhood of imperfect, simple souls wanting only to be a voice of compassion in a world spinning out of control.",
			7 : "Whether or not you believe in God, you must believe this: when we as a species abandon our trust in a power greater than us, we abandon our sense of accountability. Faiths... all faiths... are admonitions that there is something we cannot understand, something to which we are accountable. With faith we are accountable to each other, to ourselves, and to a higher truth. Religion is flawed, but only because man is flawed. The church consists of a brotherhood of imperfect, simple souls wanting only to be a voice of compassion in a world spinning out of control.",
			8 : "Whether or not you believe in God, you must believe this: when we as a species abandon our trust in a power greater than us, we abandon our sense of accountability. Faiths... all faiths... are admonitions that there is something we cannot understand, something to which we are accountable. With faith we are accountable to each other, to ourselves, and to a higher truth. Religion is flawed, but only because man is flawed. The church consists of a brotherhood of imperfect, simple souls wanting only to be a voice of compassion in a world spinning out of control.",
			9 : "Whether or not you believe in God, you must believe this: when we as a species abandon our trust in a power greater than us, we abandon our sense of accountability. Faiths... all faiths... are admonitions that there is something we cannot understand, something to which we are accountable. With faith we are accountable to each other, to ourselves, and to a higher truth. Religion is flawed, but only because man is flawed. The church consists of a brotherhood of imperfect, simple souls wanting only to be a voice of compassion in a world spinning out of control.",
			10 : "Whether or not you believe in God, you must believe this: when we as a species abandon our trust in a power greater than us, we abandon our sense of accountability. Faiths... all faiths... are admonitions that there is something we cannot understand, something to which we are accountable. With faith we are accountable to each other, to ourselves, and to a higher truth. Religion is flawed, but only because man is flawed. The church consists of a brotherhood of imperfect, simple souls wanting only to be a voice of compassion in a world spinning out of control.",
			11 : "Whether or not you believe in God, you must believe this: when we as a species abandon our trust in a power greater than us, we abandon our sense of accountability. Faiths... all faiths... are admonitions that there is something we cannot understand, something to which we are accountable. With faith we are accountable to each other, to ourselves, and to a higher truth. Religion is flawed, but only because man is flawed. The church consists of a brotherhood of imperfect, simple souls wanting only to be a voice of compassion in a world spinning out of control.",
				}
		self.r=randrange(12)
		#print self.r
		#print self.para[self.r]
		
		global new,new1

		self.cur=self.output_para.textCursor()		
		self.cur.movePosition(QTextCursor.Start)
		format=self.cur.charFormat()
		format.setForeground(QtCore.Qt.yellow)
		self.cur.setCharFormat(format)
		self.cur.insertText(self.para[1])
		#self.output_para.insertPlainText(" ")
		self.cell1=(self.output_para.toPlainText())
		self.timer = QTimer(self)
		self.start_time = 150
		self.lcd_time.display("%02d:%02d" % (self.start_time/60,self.start_time % 60))
		self.restartTimer()
		self.timer.timeout.connect(self.updateLCD)
		self.count1=0
		self.count2=0
		self.setWindowState(QtCore.Qt.WindowMaximized)
		self.input_para.textChanged[str].connect(self.done_typing_clicked)		
		self.cur.movePosition(QTextCursor.Start)		
		self.words=0
		self.acc=0			
		self.correct_char=0
		self.wrong_char=0		
		self.all_char=0
		self.net_wpm=0
		self.counter=0
		self.compensate=0			
		self.correct_char1=0
		self.wrong_char1=0		
		self.all_char1=0
		self.counter1=0
		self.compensate1=0
		self.count11=0
		self.count21=0	
		self.cur.deleteChar()		
		fmt=self.cur.charFormat()		
		fmt.setFontUnderline(True)		
		self.cur.setCharFormat(fmt)
		self.cur.insertText(self.cell1[self.count2])
		self.cur.movePosition(QTextCursor.Start)		
		
	"""def calc_wpm(self):
		self.gross_wpm=int((self.all_char1/5)/((150-start_time)/60))
		net_wpm=gross_wpm-int((wrong_char/((150-start_time)/60))"""

	def new_function(self):
			self.output_para.clear()
			self.cur.movePosition(QTextCursor.Start)
			format=self.cur.charFormat()
			format.setForeground(QtCore.Qt.yellow)
			self.cur.setCharFormat(format)
			self.r=randrange(12)
			self.cur.insertText(self.para[self.r])		
			self.cell1=(self.output_para.toPlainText())	
			self.cur.movePosition(QTextCursor.Start)			
			self.words=0
			self.acc=0			
			self.correct_char=0
			self.wrong_char=0		
			self.all_char=0
			self.counter=0
			self.compensate=0
			self.count1=0
			self.count2=0		
			"""self.cur.deleteChar()		
			fmt=self.cur.charFormat()		
			fmt.setFontUnderline(True)		
			self.cur.setCharFormat(fmt)
			self.cur.insertText(self.cell1[self.count2])
			self.cur.movePosition(QTextCursor.Start)	
			#QMessageBox.about(self,'Swift Typer','Press OK when you are ready.')
			#print self.count1
			#print self.count2"""

	def done_typing_clicked(self,text):
		new=text
		new1=text[-1]	
		#print new
		#print new1		
		if((len(new)-01)<self.count1):
			self.count1-=1
			self.count11-=1
			self.compensate+=1
			self.compensate1+=1
			return			
		elif(new1==self.cell1[self.count2]):
			self.correct_char+=1
			self.correct_char1+=1
			
			"""			
			self.cur.deleteChar()	
			format=self.cur.charFormat()
			format.setForeground(QtCore.Qt.green)
			self.cur.setCharFormat(format)
			self.cur.insertText(self.cell1[self.count2])
			#self.last=new[self.count1]
			"""
			
			#
			self.cur.deleteChar()			
			format=self.cur.charFormat()
			format.setFontUnderline(True)			
			format.setForeground(QtCore.Qt.green)
			self.cur.setCharFormat(format)
			self.cur.insertText(self.cell1[self.count2])
			#
			self.cur.movePosition(QTextCursor.Left)			
			self.cur.deleteChar()			
			format=self.cur.charFormat()
			format.setFontUnderline(False)			
			format.setForeground(QtCore.Qt.green)
			self.cur.setCharFormat(format)
			self.cur.insertText(self.cell1[self.count2])
			#
			self.cur.deleteChar()			
			format=self.cur.charFormat()
			format.setFontUnderline(True)			
			format.setForeground(QtCore.Qt.white)
			self.cur.setCharFormat(format)
			if(self.all_char>=(len(self.cell1))-1):
				self.cur.insertText(self.cell1[self.count2])
				#print "inside if green"	
			else:
				self.cur.insertText(self.cell1[self.count2+1])
				#print "inside else green"				
			self.cur.movePosition(QTextCursor.Left)
			#
			self.count1+=1
			self.count11+=1
			self.count21+=1
			self.count2+=1
		elif(new1!=self.cell1[self.count2]):
			self.wrong_char+=1
			self.wrong_char1+=1			

			"""
			self.cur.deleteChar()
			format=self.cur.charFormat()
			format.setForeground(QtCore.Qt.red)
			self.cur.setCharFormat(format)
			self.cur.insertText(self.cell1[self.count2])
			"""

			#
			self.cur.deleteChar()			
			format=self.cur.charFormat()
			format.setFontUnderline(True)			
			format.setForeground(QtCore.Qt.red)
			self.cur.setCharFormat(format)
			self.cur.insertText(self.cell1[self.count2])
			#
			self.cur.movePosition(QTextCursor.Left)			
			self.cur.deleteChar()			
			format=self.cur.charFormat()
			format.setFontUnderline(False)			
			format.setForeground(QtCore.Qt.red)
			self.cur.setCharFormat(format)
			self.cur.insertText(self.cell1[self.count2])
			#
			self.cur.deleteChar()			
			format=self.cur.charFormat()
			format.setFontUnderline(True)			
			format.setForeground(QtCore.Qt.white)
			self.cur.setCharFormat(format)
			#self.cur.insertText(self.cell1[self.count2])

			if(self.all_char>=(len(self.cell1))-1):
				self.cur.insertText(self.cell1[self.count2])			
			else:
				self.cur.insertText(self.cell1[self.count2+1])
			self.cur.movePosition(QTextCursor.Left)
			#	"""		

			self.count1+=1
			self.count11+=1
			self.count2+=1
			self.count21+=1
		self.all_char+=1 			
		self.all_char1+=1				
		tot=len(text)+self.compensate
		tot=len(text)+self.compensate1
		self.acc=float(self.correct_char1)/tot*100	
		self.words=self.all_char1/5.0		
		#print "count1 is %d" %self.count1
		#print "count2 is %d" %self.count2
		#print "count11 is %d" %self.count11
		#print "count21 is %d" %self.count21
		#print "len of cell1 is %d" %len(self.cell1)
		#print ""
		#print "all_char = %d" %self.all_char
		#print "correct_char = %d" %self.correct_char
		#print "wrong_char = %d" %self.wrong_char
		#print "words = %d" %self.words
		#print "accuracy = %f" %self.acc		
		#print "correct_char1 is %d" %self.correct_char1
		#print "all_char1 is %d" %self.all_char1
		
		if(self.all_char>=(len(self.cell1))):
			self.new_function()
		

	def restartTimer(self):
		self.timer.stop()
		self.start_time = 150
		self.lcd_time.display("%d:%02d" % (self.start_time/60,self.start_time % 60))
		# Restart the timer
		self.timer.start(1000)
		

	def updateLCD(self):
		global receipt,username
		# Update the lcd
		if self.counter1==0:
			self.counter1+=1
			QMessageBox.about(self,'Swift Typer','Press OK when you are ready.')
		self.start_time -= 1
		if self.start_time >= 0:
			self.lcd_time.display("%d:%02d" % (self.start_time/60,self.start_time % 60))
			a=150-self.start_time
			elapsed = str(a)+".0"
			self.gross_wpm=float(self.words)*60.0/float(elapsed)
			self.lcd_accuracy.display(self.acc)
			self.net_wpm=float(self.gross_wpm-(self.wrong_char1/5.0)*60.0/(float(elapsed)))
			self.lcd_wpm.display(self.net_wpm)
		else:
			self.timer.stop()
			self.net_wpm=self.gross_wpm-(self.wrong_char1/5)
			QMessageBox.about(self,'TIME"S UP!!!','Time\'s up. Press OK to see your final SCORE!!!')
			QMessageBox.about(self,'SCORE','Accuracy	:	%d\n\nWPM	:	%d' %(self.acc,self.net_wpm))
			print "message printed"
			conn.execute("INSERT INTO result values(?,?)",(str(receipt),str(self.net_wpm)))
			conn.commit()

					
	#conn.execute("INSERT OR IGNORE INTO swift values(?,?,?,?,?)",(0,str(name),str(receipt),str(college),str(mobile)))
app = QtGui.QApplication(sys.argv)
#app.setStyleSheet("QTextEdit {color:red}")
myWindow = MyWindowClass()
#myWindow.show()
app.exec_()
