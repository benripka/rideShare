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

def matchLocations(conn, keyword):
	cur = conn.cursor()
	cur.execute("select * from locations where city like :keyword or prov like :keyword or lcode like :keyword or address like :keyword",{"substr": "%" + srcTry + "%"} )
	guess = cur.fetchall()
		

	

def offerRide(conn):
	rdate = input("Please enter the ride date: ")
	numSeats = input("Number of available seats: ")
	pricePerSeat = input("Price per seat: ")
	#TODO: Fill in options
	lugDesc = input("Bried luggage description (options)") 
	srcTry = input("locations of departure: ")
	dstTry = input("Locations of Arrival: ")
			
	
	rno = randint(1, 100000)
	global currentUser
	driver = currentUser
	prin
	while rno in cur.fetchall():
		rno = randint(1, 100000)
	
	cur.execute("insert into rides values(:rno, :pricePerSeat, :rdate, :numSeats, :lugDesc, :src, :dst, :driver, :cno)", {"rno":rno, "pricePerSeat":pricePerSeat, "rdate":rdate, "numSeats":numSeats, "lugDesc":lugDesc, "src":src, "dst":dst, "driver":driver, "cno":cno})
	conn.commit()
def displayOptions(conn):
	choice = input("What would you like to do next?\nUse the following keys:\nPost a ride (1)\nFind a Ride (2)\nShow My Bookings (3)\nExit (4)\n")
	return choice

def login(conn):
	# encrypt, decrypt, varify the pwd stored under the members email with the one entered
	print("Login: \n")
	email = input("please enter your email: ")
	pwdTry = input("please enter your password: ")
	cur = conn.cursor()
	cur.execute("select pwd from members where (email=:email)", {"email":email})
	realPwd = cur.fetchone()
	if realPwd is None:
		return False
	if (realPwd[0] == pwdTry):
		print("Welcome")
		global currentUser
		currentUser = email
		return True
	else:
		print("Incorrect Password")
		return False
		
def printDivider():
	print("\n\n-------------------------------------------------------\n\n")

def displayMessages(conn):
	#TODO: make the messages change to seen in the database after displaying

	global currentUser
	email = currentUser
	cur = conn.cursor()
	seen = "n"
	cur.execute("select * from inbox where (email=:email and seen = :seen)", {"email":email, "seen":seen})
	emails = cur.fetchall()
	if len(emails) > 0:
		print("You've got "+ str(len(emails)) + " new messages!")
	
	for email in emails:
		print("From " + email[2] + ": " + email[3])
		print("Sent on: " + email[1])
		
def findRide(conn):
	print("finding ride")
	pass
	
def showBookings(conn):
	print("showing booking")
	pass
	
def nextStep(choice, conn):
	return {
		'1' : lambda: offerRide(conn),
		'2'	: lambda: findRide(conn),
		'3'	: lambda: showBookings(conn),
		'4' : lambda: exit(conn)
	}[choice]()

def homeScreen(conn):
	while True:	
			printDivider()
			displayMessages(conn)
			print("\n")
			choice = displayOptions(conn)
			
			#If exit is selected!
			if choice == '4':
				break
			printDivider()
			nextStep(choice, conn)
	return
			
def loginScreen(conn):
	while True:
		
		# This block is the login/signup screen, it loops until a user logs in.
		printDivider()
		SorL = input("Enter S to signup or L to login ")
		if SorL == "l":
			printDivider()
			if not login(conn):
				print("invalid unsername or password, try again:")
				continue
			else:
				homeScreen(conn)
			
		elif SorL == "s":
			printDivider()
			createMem(conn)
			printDivider()
			if not login(conn):
				print("invalid unsername or password, try again:")
				continue
			else:
				homeScreen(conn)
		else:
			print("Invalid Choice! \n")
			continue
	

def main():
	database = "/home/ben/Desktop/CMPUT291/P1/P1.db"
	conn = createConnection(database)
	
	loginScreen(conn)
	homeScreen(conn)
	

		
if __name__ == '__main__':
	main()
		

			



