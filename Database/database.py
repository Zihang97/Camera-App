import pymysql

password = "*******"

def createtable(password):
	db = pymysql.connect(host = "localhost", user = "root", password = password, database = "camera_app")
	 
	cursor = db.cursor()
	
	cursor.execute('drop table if exists images')

	sql = "CREATE TABLE images (author VARCHAR(40), create_time VARCHAR(40), img text)"
	 
	cursor.execute(sql)
	 
	db.close()


def POST(password, imgaddr):
	
	db = pymysql.connect(host = "localhost", user = "root", password = password, database = "camera_app")
	 
	cursor = db.cursor()
	
	auth = info_dict['author']
	create_time = info_dict['create_time']

	sql = "insert into images (author, create_time, img) values(%s, %s, %s)"
	cursor.execute(sql, (auth, create_time, imgaddr))

	db.commit()
	
	db.close()


def GET(password, creator):
	db = pymysql.connect(host = "localhost", user = "root", password = password, database = "camera_app")
	 
	cursor = db.cursor()

	sql = "select * from images where author=%s"
	cursor.execute(sql, (creator))
	result = cursor.fetchone()
	
	creator = result[0]
	content = result[3]
	 
	db.close()

	return [creator, content]


def DELETE(password, creator):
	db = pymysql.connect(host = "localhost", user = "root", password = password, database = "camera_app")
	 
	cursor = db.cursor()

	sql = "delete from images where author=%s"
	cursor.execute(sql, (creator))

	db.commit()
	 
	db.close()
