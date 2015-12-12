from simple_salesforce import Salesforce
import csv
import sys,datetime,time
import string

import mysql.connector
from mysql.connector.constants import ClientFlag
from sfdc_config import SFUSER,SFPW,SF_TOKEN,DBUSER,DBPW,DBHOST,DBNAME,opportunity_directory,OPPORTUNITY_FIELD_TYPE_MAP,OPPORTUNITY_FIELD_DICT,OPPORTUNITY_ORDERED_FIELDS
FIELD_TYPE_MAP=OPPORTUNITY_FIELD_TYPE_MAP
FIELD_DICT = OPPORTUNITY_FIELD_DICT
ORDERED_FIELDS = OPPORTUNITY_ORDERED_FIELDS
directory = opportunity_directory

#make CSVs for main table and split values
the_date = time.strftime("%d-%m-%Y")

file_out = directory+'opportunity%s.csv' % (the_date)
csv_out = open(file_out, 'wb')

csv_handler = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

sf = Salesforce(password=SFPW, username=SFUSER, security_token=SF_TOKEN)

#connect to DB
#note that the client_flag allows the mysql module to access files on the computer
cnx = mysql.connector.connect(user=DBUSER, password=DBPW,
                              host=DBHOST,
                              database=DBNAME, client_flags=[ClientFlag.LOCAL_FILES])
cursor = cnx.cursor()

sosl = "SELECT %s FROM Opportunity" % ','.join(FIELD_DICT.values()) 

p = sf.query_all(sosl)
#for all records in the returned sql
index = 1
for record in p['records']:	
	row = []
	for a in ORDERED_FIELDS:
		code = FIELD_DICT[a]
		path = code.split(".")
		#print a
		element = record
		for p in path:
			#print element,p
			try:
				element = element[p]
			except:
				element = ""
				pass
		
		#Set empty values to null. This does not include "None"!
		if not record[code]:
			row.append("NULL")
		elif (FIELD_TYPE_MAP[a] == "datetime"):
			if (str(record[code]) == "None"):
				row.append("NULL")
			else:
				row.append(str(record[code])[0:10])
		elif (FIELD_TYPE_MAP[a] != "string"): #some records are boolean or float
			row.append(str(record[code]))
		else:
			row.append(record[code].encode('utf-8')) #some names are not unicode
	csv_handler.writerow(row)
	index = index+1

#must close the file before reading it with the MySQL load
csv_out.close()
error_flag = "False"

#WRITE TO DB
try:
	#each pull is a full export, meaning we can truncate daily
	#turn off foreign key constraint and on to preserve foreign key reference while still able to truncate. Need to clean data in the future!!
	sql = """SET FOREIGN_KEY_CHECKS=0;"""
	cursor.execute(sql)
	
	sql = """TRUNCATE sf_opportunity;"""
	cursor.execute(sql)
	
	sql = """
		LOAD DATA LOCAL INFILE '{}'
		REPLACE INTO TABLE sf_opportunity
		FIELDS TERMINATED BY ',' 
		OPTIONALLY ENCLOSED BY '"'
		LINES TERMINATED BY "\r\n";
		"""
	cursor.execute(sql.format(file_out))
	
except mysql.connector.Error as err:
	print("Something went wrong: {}".format(err))
	error_flag = "True";
#only execute code if no error
if error_flag != "True":
	cnx.commit()
