import sqlite3
from sqlite3 import Error
from random import randint

currentUser = None

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
		
def createMem(conn):
	email = input("Please enter your email: ")
	name = input("Please enter your name: ")
	phone = input("Please enter your phone: ")
	pwd = input("Please enter your pwd: ")
	cur = conn.cursor()
	cur.execute("insert into members values(:email, :name, :phone, :pwd)", {"email": email, "name": name, "phone": phone, "pwd": pwd})
		
def createCar(conn, cno, make, model, year, seats, owner):
	cur = conn.cursor()
	cur.execute("insert into cars values(:cno, :make, :model, :year, :seats, :owner)", {"cno" : cno, "make" : make, "model" : model, "year" : year, "seats" : seats, "owner" : owner})
	
def createRide(conn, rno, price, rdate, seats, lugDesc, src, dst, driver, cno):
	cur = conn.cursor()
	cur.execute("insert into rides values(:rno, :price, :rdate, :seats, :lugDesc, :src, :dst, :driver, :cno)", {"rno":rno, "price":price, "rdate":rdate, "seats":seats, "lugDesc":lugDesc, "src":src, "dst":dst, "driver":driver, "cno":cno})

def offerRide(conn):
	rdate = input("Please enter the ride date: ")
	numSeats = input("Number of available seats: ")
	pricePerSeat = input("Price per seat: ")
	#TODO: Fill in options
	lugDesc = input("Bried luggage description (options)") 
	src = input("locations of departure: ")
	dst = input("Locations of Arrival: ")
	
	cur = conn.cursor()
	cur.execute("select rno from rides")
	rno = randint(1, 100000)
	while rno in cur.fetchall():
		rno = randint(1, 100000)
		
	cur.execute("insert into rides values(:rno, :pricePerSeat, :rdate, :numSeats, :lugDesc, :src, :dst)", {"rno":rno, "pricePerSeat":pricePerSeat, "rdate":rdate, "numSeats":numSeats, "lugDesc":lugDesc, "src":src, "dst":dst})
	
def displayOptions(conn):
	choice = input("What would you like to do next?\nUse the following keys:\nPost a ride (1)\nFind a Ride (2)\nShow My Bookings (3)\nExit (4)\n")
	return int(choice)

def login(conn):
	# encrypt, decrypt, varify the pwd stored under the members email with the one entered
	email = input("please enter your email: ")
	pwdTry = input("please enter your password: ")
	cur = conn.cursor()
	cur.execute("select pwd from members where (email=:email)", {"email":email})
	realPwd = cur.fetchone()
	if (realPwd[0] == pwdTry):
		print("Welcome")
		global currentUser
		currentUser = email
		return True
	else:
		print("Incorrect Password")
		return False

def displayMessages(conn):
	email = currentUser
	cur = conn.cursor()
	
	cur.execute("select * from inbox where (email=:email and seen = 0)", {"email":email})
	emails = cur.fetchall()
	
	for email in emails:
		print(email)
	
	

def main():
	database = "/home/ben/Desktop/CMPUT291/rideShare/P1.db"
	conn = createConnection(database)
	while True:
	
		SorL = input("Enter S to signup or L to login")
		if SorL == "l":
			if not login(conn):
				continue
			
		elif SorL == "s":
			createMem(conn)
			varifyPwd(conn)
		
		displayMessages(conn)
		choice = displayOptions(conn)
		switch (choice)
		
	
		
		
	with conn:
		print(varifyPwd(conn, "pwd48", "mem48@g.com"))
		
if __name__ == '__main__':
	main()
		

			



