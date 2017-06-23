# AUTHER : JERINISREADY
# DATE   : 22nd JUNE 2017
# PROJECT: exam.cusat.ac.in WebScrolle

import urllib2,urllib
import re
import datetime

class webData:
	"SCROLLS OVER SERVER TO SET REQUEST,  GET DATA AND PARSE TO RETURN A ',' Seperated String"

	def __init__(self):
		self.__body = ""
		self.__month = "April"
		self.__year = "2017"
		self.__sem = '8'
		self.__res_type = 'Regular'
		self.__time = datetime.datetime.strftime(datetime.datetime.now(),"%Y/%m/%d+%H:%M:%S.000+GMT+0530")


	def getData(self,regn,url='http://exam.cusat.ac.in/erp5/cusat/CUSAT-RESULT/Result_Declaration/display_sup_result'):
		"GET DATA FROM URL"

		data = urllib.urlencode({		# SET OF POST VALUES THAT HAVE TO BE TRANSFERED TO SERVER.
		'regno'		:regn,
		'date_time'	:self.__time,
		'ipadress'	:"",
		'month'		:self.__month,
		'year'		:self.__year,
		'semester'	:self.__sem,
		'result_type'	:self.__res_type,
		'deg_name'	:'B.Tech',
		'statuscheck'	:'failed'})

		websrc = urllib2.urlopen(url,data)
		self.__body = websrc.read()

	def setMonth(self,m) : self.__month=m		# set Month of Exam [ eg : webData.setMonth('April')]
	def setYear(self,m) : self.__year=m		# Set Year of Exam [ eg : webData.setMonth('2017')]
	def setSem(self,m) : self.__sem=m		# Set Semester of Exam [eg : webData.setMonth('8')]
	def setResultType(self,m) : self.__res_type=m	# Set Resutl type Regular / Improvement / Supplimentary
							# 			[ eg: webData.setResultType('Regular') ]


	def parse(self):				# RETURNS A ',' SEPERATED FILES
		"PARSE DATA FROM GETDATA METHOD AND RETURNS A ',' SEPERATED FILES"
		text = self.__body					
		if re.search("Invalid Registration number",text): 
			return "RollNumber Not Found"
		par = re.compile(r'<tr>|</tr>|<td>|</td>|<th>|</th>|<b>|</b>|<td style="text-align:center;">|<br>|<td style="text-align:center;" id="state.">|&nbsp;:&nbsp;')
		mBody = par.split(text)
		mBody = filter(None, mBody)
		del mBody[0]
		del mBody[-3:]
		mBody = [i.replace('\n','') for i in mBody]
		mBody = [i.replace('  ','') for i in mBody]
		mBody = filter(	lambda v: (len(v)>0  and v.strip(' \t\n\r')!= '' for v in mBody),mBody)
		#for i,v in enumerate(mBody):
		#	 print "{}  : {} ".format(i,v)
		ind = (2,5,28,34,40,46,52,58,61,62,65,68)
		indx = []
		strv = ""
		try:
			indx = [mBody[i] for i in ind[0:-4]]
			indx.append(mBody[ind[-4]].split(':')[1])
			indx.append(mBody[ind[-3]].split(':')[1])		
			indx.append(mBody[ind[-2]])
			indx.append(mBody[ind[-1]])		
		except Exception: pass
		strv = ", ".join(indx)
		strv.replace("  ","" )
		return strv.replace("\n","")

if( __name__ == '__main__' ):
	a = webData()
	a.getData(12141024)
	list_ =  a.parse()
	print list_

