# AUTHER : JERINISREADY
# DATE   : 22nd JUNE 2017
# PROJECT: exam.cusat.ac.in WebScrolle

import time
import random
import re
import os

class csv:
	__filelock__ = False;

	def __init__(self,name="cusat_S8_Result_"+str(time.time())):
		# +str(random.randrange(1000))
		self.filename = name
		__filelock__ = True
		try: 
			os.mkdir('datas')		# Saves Data in a folder 'datas'
		except Exception: pass
		os.chdir('datas')
		f = open(name+".csv","w")
		s = "Registration Number, NAME, CS 1801 AAPP , CS 1802 OOMD , CS 1803 DC , CS 1804 E3 DC/MC , CS 18L1 PROJECT, CS 18L2 COURCE VIVA, Sem Total, GPA, CGPA, GRADE\n"
		f.write(s)
		self.f = f

	def write(self):				# Open again in write mode once the file is closed.!
		if not __filelock__ : 
			__filelock__ = True
			os.chdir('datas')
			self.f = open(name+".csv","w")
		else :  
			print " [ x ] File is Already opened, " 
			print "  [ x ] Try Close file and retry csv.close() ( RECOMMENTED ) or " 
 			print ()
			print "  Error : Try Opening a Locked Item."

	def addLine(self,s):				# Writes the content as a new Line
		self.f.write(s)
		self.f.write('\n')

	def fname(self):				# Returns the filename
		return self.filename		

	def read(self, force=False):			# Reads the content of File 
		if force :  self.close()
		if self.__filelock__ : 
			print " [ x ] File is Already in write mode, "
			print " [ x ] Try Close file and retry ( RECOMMENTED ) or  "
			print " [ x ] Try opening Forcefully csv.read(force=true)) ( NOT RECOMMENTED )" 
			print()
			print " Error : Try Opening a Locked Item."
		else : 
			m = open(self.filename+".csv","r")
			x = m.read()
			m.close()
			return x
 
	def close(self):				# Saves the content and Close
		if not self.f.closed:
			self.f.close()
			__filelock__ = False


	def __del__(self):				# Saves and Close file on auto Termination such as Exceptions.
		self.f.close()


if( __name__ == '__main__' ):
	a = csv()
	#print f.filename()
	a.fname()
	print a.read(force=True)


		
		
