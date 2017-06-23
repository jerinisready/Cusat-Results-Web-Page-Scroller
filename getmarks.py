# AUTHER : JERINISREADY
# DATE   : 22nd JUNE 2017
# PROJECT: exam.cusat.ac.in WebScroller

from lib import csvSupport,webSupport


mRollNo = range(12141000,12141062)     	# mRollNo is the list of roll numbersof which we have to take the marks of.

mCsv = csvSupport.csv()			# Creates a csv file and features to read/ write the contents of file.
mWeb = webSupport.webData()		# Class which Scrolls into the web url and 
					#
for i in mRollNo:			
	mWeb.getData(i)			# webData.getData(regn,url='<S8 Regular Exam Url>') Gets the data over Internet
	eachData = mWeb.parse()		# webData.parse() parse the html page using specific Regular Expression and returns
					# the comma seperated lines.
	print eachData			# prints the value into terminal // comment it out to hide on terminal
	try:
		mCsv.addLine(eachData)	# adds a new line to the file
	except Exception:
		mCsv.close()		# Saves The file and exit
