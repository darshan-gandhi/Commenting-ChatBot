import sqlite3
import  json
from datetime import datetime

timeframe= '2015-01'

sql_transaction= []

connection = sqlite3.connect('{}.db'.format(timeframe))
c = connection.cursor()

def creat_table() : 
	c.excecute ("CREATE TABLE IF NOT EXITSTS parent_reply (parent_id TEXT PRIMARY KEY, comment_id TEXT UNIQUE ,comment TEXT, subreddit TEXT, unix INT, score INT)" )

	if  _name_ == "_main_" :
		create_table()

	