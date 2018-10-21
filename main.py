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
	
def createRide(conn, rno, price, rdate, seats, lugDesc, src, dst, driver, cno):
	cur = conn.cursor()
	cur.execute("insert into rides values(:rno, :price, :rdate, :seats, :lugDesc, :src, :dst, :driver, :cno)", {"rno":rno, "price":price, "rdate":rdate, "seats":seats, "lugDesc":lugDesc, "src":src, "dst":dst, "driver":driver, "cno":cno})

def offerRide(rdate, numSeats, pricePerSeat, lugDesc, src, dst):
	pass
	
def varifyPwd(psd):
	# encrypt, decrypt, varify the pwd stored under the members email with the one entered
	pass

def getUnseenMessages():
	# On login, display all messages that are marked as unseen 
	pass

def exitProgram():
	# Available at all times, ends program.
	pass
	
def searchForRide(src, dst, enroute):
	#get all (top 5 if to many) rides that match src, dst
	pass
	
def cancelBooking():
	# Show all bookings the member has offered
	pass
	
	

def main():
	database = "/home/ben/Desktop/CMPUT291/P1/P1.db"
	conn = createConnection(database)

	with conn:
		print("1. Query memebers by email: ")
		selectMemByEmail(conn, "ben@g.com")
		selectAllMem(conn)
		
if __name__ == '__main__':
	main()
		

			



