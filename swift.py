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
no="1234567890"

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
		#print name,college,mobile,receipt		
		if(college=="" or name=="" or receipt=="" or mobile==""):		
			a.append('Fill all details')
			flag = 1
		for i in range(len(name)):
			if(str(name[i]) not in alp):
				a.append('Enter valid name')
				flag = 1
		for i in range(len(college)):
			if(str(college[i]) not in alp):
				a.append('Enter valid college name')
				flag = 1
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
			#print "done"			
			self.begin()
		else:
			QMessageBox.about(self,'error','%s\n%s\n%s\n%s\n%s\n%s' %(a[0],a[1],a[2],a[3],a[4],a[5]))
		

	def begin(self):
		self.Form.hide()
		self.setupUi(self)
		self.showFullScreen()		
		self.para=	{
			0 : "The fish are just 120 microns long and 30 microns thick, much smaller than a human hair. Researchers can 3D print hundreds of the fish in seconds. The fish are printed with tiny particles of platinum in the tail which react with hydrogen peroxide. When the microfish are placed in peroxide, the tails move, propelling the fish along. The scientists can also add other particles to the materials used to print the fish, including chemicals that can detect and absorb toxins like bee venom. In the study, they showed that the microfish could detoxify a liquid contaminated with a toxin. As the fish work, they glow red, and the swimming motion helps make sure they don't miss a drop of the contaminant.\n\nThese fish are just a proof of concept. They won't be used outside of a lab for a long time yet, but their creators have very high hopes for the fish.",
			1 : "Whether or not you believe in God, you must believe this: when we as a species abandon our trust in a power greater than us, we abandon our sense of accountability. Faiths, all faiths... are admonitions that there is something we cannot understand, something to which we are accountable. With faith we are accountable to each other, to ourselves, and to a higher truth. Religion is flawed, but only because man is flawed. The church consists of a brotherhood of imperfect, simple souls wanting only to be a voice of compassion in a world spinning out of control.\n\nThe first major grouping of Shakespeare plays begins with his histories and comedies of the 1590s. Shakespeare's earliest plays tended to be adaptations of other playwright's works and employed blank verse and little variation in rhythm.",
			2 : "PICT IEEE Student Branch (PISB), one of the most active student Branches of IEEE, is the proud host of the annual technical event Credenz. It is one of the most innovative and scientific events held in August every year. It is organised exclusively by students of PISB. It has grown manifold since its inception in 2004, and has made a name for itself as a Technical Renaissance showcasing the young emerging minds of technocrats and administrators. Through its deluge of competitions, lectures, exhibitions and workshops, Credenz endeavors to enkindle the minds of thousands of students visiting annually. Over the years, it has attracted the connoisseurs of Engineering and Technology.Credenz represents zenith of science and engineering in a landscape of future visionaries and scientists. From thrilling robotic competitions to the enriching workshops, every bit promises to be a fulfilling experience. ",
			3 : "The ability to understand natural language queries is a big deal. You can ask, for example: I'm going to be in Boston. I like basketball. What do you suggest, Watson?\" You might get several answers: Celtics tickets, Boston College tickets, Harvard tickets. Or in the offseason, Watson may suggest you drive to the Basketball Hall of Fame in Springfield (MA). Companies are already using Watson this way. Fluid, Inc.'s Watson-based retail solutions deliver granular results to queries such as \"I am taking my wife and three children camping in upstate New York in October and I need a tent.\"\n\nConsider this : Watson has been taught to pass the medical boards. Would you trust it to diagnose you and prescribe medication? What if you claim to be in pain and Watson doesn't believe your subjective input?",
			4 : "Apple's secretive project aimed at testing self-driving cars seems worlds apart from the tech giant's usual business of smartphones and tablets. But the idea of a robotic \"iCar\" raises an intriguing possibility: What if self-driving cars were represented by virtual assistants similar to Apple\'s Siri for the iPhone and iPad?\n\nA version of Siri for self-driving cars might even adopt a familiar virtual face on a display screen to win the trust of potential human owners. Getting people to trust in a future world filled with self-driving cars could go a long way toward making commutes both safer and faster.\n\nThe promise of robot cars has driven both traditional automakers and tech giants such as Google and China's Baidu to develop their own versions of the technology.",
			5 : "Bob acted as virtual driver while study participants sat in a driving simulator. Half of the participants got to ride along with a Bob who resembled them, whereas the other half of the participants got a Bob with a dissimilar face. The familiar Bob also behaved in two additional ways calculated to help increase trust. First, he mimicked the head movements of participants, with a four-second delay to avoid any creepiness.\n\nSecond, Bob displayed the same driving goals as the study participant on a computer screen. Participants were asked to rank their goals in terms of comfort, energy efficiency and speed. In the end, participants rated the familiar Bob as more trustworthy than the dissimilar Bob during driving scenarios leading up to road obstacles such as shallow or sharp turns, a traffic jam, a red traffic light or a fallen tree on the road.",
			6 : "One limitation of the study came from the fact that the driving scenarios all stopped just before the critical moment of dealing with the road obstacle.It's possible that dissimilar Bob could have won an equivalent level of trust as familiar Bob if he had shown participants that he could successfully navigate such obstacles. But in this case, Verberne and his colleagues intentionally chose to stop short so that they could focus on measuring levels of trust in the midst of uncertainty.\n\nThe three types of similarity in the familiar Bob-face, head movement and shared driving goals-did not seem to add up to more overall trust compared with previous studies that tested just one type of similarity. But having a virtual driving assistant with as many similarities as possible might appeal to different self driving car owners who subconsciously value one type of similarity over the other.",
			7 : "Such research represents just a first step toward understanding how a virtual driver might make self-driving cars appear more friendly. For example, the study did not directly test whether having a self-driving car represented by a virtual assistant increases human trust compared with a silent, faceless robot car. It's also possible that just having a faceless virtual driver with a likeable voice and winning personality might also do the trick.\n\nA virtual driving assistant with both a friendly face and voice might seem like the obvious end goal. But researchers may still have to tread carefully in finding the right combination. In a past study, Verberne discovered that combining an artificial-sounding voice with a face similar to the human owner could actually creep people out.",
			8 : "Apple's upcoming media event has been expected to take place on September 9 for quite some time. It's exactly the same date that Apple held their fall event in 2014 as well, when the iPhone 6 and Apple Watch was announced. Many experts believe that Force Touch-a new feature that allows touchpads and touchscreens to determine how much pressure is applied to their surface-will be added to the iPhone 6s.\n\nForce Touch is already available in the Apple Watch, and it was added to the newest Macbook earlier this year at WWDC. In addition to new hardware, many expect iOS 9 to be rolled out to existing iPhone 6 handsets and any new ones that are announced. Other changes that are expected include a better camera, faster processor, and thicker design to prevent bending.",
			9 : "The internet is flooded with photos-of your brunch, of your cat, of your estranged elementary school friend's cousin's wedding. 1.8 billion photos are uploaded daily, and most of them are objectively pretty terrible. Now a team of computer scientists from Princeton University and software company Adobe have created a program to make those photos just a little better, by identifying and eliminating distracting elements, according to a paper presented recently at this year's Computer Vision and Pattern Recognition Conference in Boston.\n\nThere are lots of elements of a \"casual\" photo that can make it terrible-bad lighting, off-angles. But one that's often ignored is the inclusion of distracting elements, objects in the photo that distract the viewer's attention from the image's main focus.",
			10 : "Instagram now supports portrait and landscape photos in its app, meaning you'll start seeing more rectangular photos in your feed. Taking photos within the app will continue to default to square-shaped pictures, but photos imported from other apps will preserve their look. Instead of the letterbox view, the Instagram photo feed will adjust in size accordingly.\n\n\"It turns out that nearly one in five photos or videos people post aren't in the square format,\" said Instagram in a statement. \"Now, when choosing a photo or video, you can tap the format icon to adjust the orientation to portrait or landscape instead of square.\"",
				}
		self.r=randrange(11)
		#print self.r
		print self.para[self.r]
		
		global new,new1

		self.cur=self.output_para.textCursor()		
		self.cur.movePosition(QTextCursor.Start)
		format=self.cur.charFormat()
		format.setForeground(QtCore.Qt.yellow)
		self.cur.setCharFormat(format)
		self.cur.insertText(self.para[self.r])
		#self.output_para.insertPlainText(" ")
		self.cell1=(self.output_para.toPlainText())
		self.timer = QTimer(self)
		self.start_time = 90
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
		self.thing=0
		self.wrong_words=0
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
			"""print self.cell1
			print len(self.cell1)"""	
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
				#print "inside if red"			
			else:
				self.cur.insertText(self.cell1[self.count2+1])
				#print "inside else red"
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
		self.words=float(self.all_char1/5.0)		
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
		self.start_time = 90
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
			a=90-self.start_time
			elapsed = str(a)+".0"						
			self.wrong_words=float(self.wrong_char1/5.0)
			#print self.wrong_words
			self.gross_wpm=float(self.words)*60.0/float(elapsed)
			self.thing=float(self.wrong_words)*60.0/float(elapsed)
			self.lcd_accuracy.display(self.acc)
			self.net_wpm=float(self.gross_wpm-self.thing)
			self.lcd_wpm.display(self.net_wpm)
			
		else:
			self.timer.stop()
			self.net_wpm=self.gross_wpm-(self.wrong_char1/5.0)
			QMessageBox.about(self,'TIME"S UP!!!','Time\'s up. Press OK to see your final SCORE!!!')
			QMessageBox.about(self,'SCORE','Accuracy	:	%d\n\nWPM	:	%d' %(self.acc,self.net_wpm))
			#print "message printed"
			conn.execute("INSERT INTO result values(?,?)",(str(receipt),str(self.net_wpm)))
			conn.commit()
			self.hide()
					
	#conn.execute("INSERT OR IGNORE INTO swift values(?,?,?,?,?)",(0,str(name),str(receipt),str(college),str(mobile)))
app = QtGui.QApplication(sys.argv)
#app.setStyleSheet("QTextEdit {color:red}")
myWindow = MyWindowClass()
#myWindow.show()
app.exec_()
