import sqlite3
from sqlite3 import Error

def createConnection(P1):
	try:
		conn = sqlite3.connect(P1)
		return conn
	
	except Error as e:
		print(e)
		
	return None
	
def selectAllMem(conn):
	
	cur = conn.cursor()
	cur.execute("SELECT * FROM members")
	
	rows = cur.fetchall()
	
	for row in rows:
		print(row)
		
def selectMemByEmail(conn, email):
	
	cur = conn.cursor()
	cur.execute("select * from members where email=?", (email,))
	
	rows = cur.fetchall()
	
	for row in rows:
		print(row)
		
def createMem(conn, email, name, phone, pwd):
	cur = conn.cursor()
	cur.execute("insert into members values(:email, :name, :phone, :pwd)", {"email": email, "name": name, "phone": phone, "pwd": pwd})
		
def createCar(conn, cno, make, model, year, seats, owner):
	cur = conn.cursor()
	cur.execute("insert into cars values(:cno, :make, :model, :year, :seats, :owner)", {"cno" : cno, "make" : make, "model" : model, "year" : year, "seats" : seats, "owner" : owner})
	
def main():
	database = "/home/ben/Desktop/CMPUT291/P1/P1.db"
	
	conn = createConnection(database)

	
	with conn:
		print("1. Query memebers by email: ")
		selectMemByEmail(conn, "ben@g.com")
		
		selectAllMem(conn)
		
if __name__ == '__main__':
	main()
		

			


