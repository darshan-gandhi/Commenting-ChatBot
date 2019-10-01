import sqlite3
import  json
from datetime import datetime

timeframe= '2015-01'

sql_transaction= []

connection = sqlite3.connect('{}.db'.format(timeframe))
c = connection.cursor()

def creat_table() : 
	c.excecute ("CREATE TABLE IF NOT EXITSTS parent_reply (parent_id TEXT PRIMARY KEY, comment_id TEXT UNIQUE ,comment TEXT, subreddit TEXT, unix INT, score INT)" )

def format_data():
	data=data.replace("\n " ," newlinechar ").replace("\r", " newlinechar ").replace(' " ', " ' ")
	return data


def find_parent(pid):
	try:
		sql= "SELCT comment FROM parent_reply WHERE comment_id= '{}' LIMIT 1".format(pid)
		c.excecute(sql)
		result=c.fetchone()
		if result!= None:
			return result[0]
		else: 
			return False

	except Exception as e:
		print("Error is there")
		return False

if  _name_ == "_main_" :
	create_table()
	row_counter=0 
	paired_rows=0 

	with open("Downloads:/RC_{}".format(timeframe.split('-')[],timeframe), buffering=1000) as f:
		for row in f:
			row_counter+=1
			row=json.loads(row)
			parent_id=row['parent_id']
			body=format_data(row['body'])
			created_utc=row['created_utc']
			score=row['score']
			subreddit=row['subreddit']

			parent_data=find_parent(parent_id)
