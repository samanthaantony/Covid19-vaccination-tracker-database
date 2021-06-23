import pymysql
import pandas

# Connecting to Omega account
connector = pymysql.connect(host='acadmysqldb001p.uta.edu', user='sxj7440', 
	password='abcd@2019', db='sxj7440')

cursor = connector.cursor()

# Displaying the tables in the database
cursor.execute("SHOW TABLES");
connector.commit()
results = cursor.fetchall()
print(results)


# For Qn 4 queries: 4.1 - 4.5
# User Menu for options
print("Select an option from the following to enter data: ")
print("1. Procure a certain number of one type of vaccine.")
print("2. To distribute certain amount to a state.")
print("3. To distribute certain amount to a local body.")
print("4. To administer vaccine on a new patient.")
print("5. To see if there is any adverse reaction for a patient.")

choice = input("\nPlease select option (1-5): ")
print(choice)

# For Qn4.1 query
# Adding a new record in the Vaccine table to procure certain number of vaccines
# of a certain manufacturer:
if choice.strip() == "1":
	Mname = input("\nEnter the vaccine manufacturer name: ")
	Vac_Type = input("\nEnter the vaccine type: ")
	Proc_count = input("\nEnter the number of doses procured: ")
	NumDoses_shipped = input("\nEnter the number of doses shipped to the Federal body: ")

	# To avoid foreign key errors, a drop down menu for already listed 
	# federal bodies are shown so that the user can choose from one of them
	print("\nEnter any one of the following Federal bodies: ")
	str1 = "SELECT Fname from FEDERAL"
	cursor.execute(str1)
	connector.commit()
	results = cursor.fetchall()
	for line in results:
		print(line[0])

	Fname = input()
	Date = input("\nEnter the date the doses were shipped(mm/dd/yyyy): ")

	m = Date.find('/')
	Month = Date[0:m]
	Date = Date [m+1:]
	d = Date.find('/')
	Day = Date[0:d]
	Date = Date[d+1:]
	Year = Date	
	Date_Shipped = str(Year)+"-"+str(Month)+"-"+str(Day)

	# Insert command and its execution:
	str1 = "INSERT INTO VACCINE VALUES (%s,%s,%s,%s,%s,%s)"
	data = (Mname,Vac_Type,Proc_count,NumDoses_shipped,Fname,Date_Shipped)

	cursor.execute(str1,data)
	connector.commit()
	results = cursor.fetchall()


# For Qn4.2 query:
# Distributing a certain number to a state:
elif choice.strip() == "2":
	Sname = input("\nEnter state name to which doses should be shipped: ")
	Spopulation = input("\nEnter population of the State: ")
	No_of_dose = input("\nEnter the number of doses shipped to the State: ")

	# List of already listed Federal bodies for the user to choose from to avoid
	# foreign key errors
	print("\nEnter any one of the following Federal bodies which shipped the doses: ")
	str1 = "SELECT Fname from FEDERAL"
	cursor.execute(str1)
	connector.commit()
	results = cursor.fetchall()
	for line in results:
		print(line[0])

	Fname = input()

	# Insert command and its execution
	str1 = "INSERT INTO STATES VALUES (%s,%s,%s,%s)"
	data = (Sname,Spopulation,No_of_dose,Fname)

	cursor.execute(str1,data)
	connector.commit()
	results = cursor.fetchall()


# Fro Qn 4.3 query:
# Distributing to a certain local body:
elif choice.strip() == "3":
	County = input("\nEnter County name to which doses should be shipped: ")
	Lpopulation = input("\nEnter population of the County: ")

	# To avoid foreign key errors when inputting state name:
	print("\nEnter State name of the local body from the list: ")
	str1 = "SELECT Sname from STATES"
	cursor.execute(str1)
	connector.commit()
	results = cursor.fetchall()
	for line in results:
		print(line[0])
	Sname = input()

	Zipcode = input("\nEnter the zipcode of the local body: ")

	No_of_dose = input("\nEnter the number of doses shipped to the local body: ")
	Date = input("\nEnter the date doses were received(mm/dd/yyyy): ")
	m = Date.find('/')
	Month = Date[0:m]
	Date = Date [m+1:]
	d = Date.find('/')
	Day = Date[0:d]
	Date = Date[d+1:]
	Year = Date	
	Date_received = str(Year)+"-"+str(Month)+"-"+str(Day)

	print("\nEnter the vaccine type, date shipped and vaccine manufacturer name from the list: ")
	str1 = "SELECT Vac_Type,Date_shipped,Mname from VACCINE"
	cursor.execute(str1)
	connector.commit()
	results = cursor.fetchall()
	for line in results:
		print(line)


	Vac_Type = input("\nEnter the vaccine type shipped: ")
	Date = input("\nEnter the date doses were shipped to the Federal body(mm/dd/yyyy): ")
	m = Date.find('/')
	Month = Date[0:m]
	Date = Date [m+1:]
	d = Date.find('/')
	Day = Date[0:d]
	Date = Date[d+1:]
	Year = Date	
	Date_Shipped = str(Year)+"-"+str(Month)+"-"+str(Day)

	Mname = input("\nEnter the vaccine manufacturer name: ")

	# Insert command into local bodies to have a record of the county and zipcode
	str1 = "INSERT INTO LOCAL_BODIES VALUES (%s,%s,%s,%s)"
	data = (County,Lpopulation,Sname,Zipcode)

	cursor.execute(str1,data)
	connector.commit()
	results = cursor.fetchall()

	# Insert command into the Have table to have a record for the same county and 
	# zipcode to keep track of doses it has
	str1 = "INSERT INTO HAVE VALUES (%s,%s,%s,%s,%s,%s,%s)"
	data = (No_of_dose,Date_received,Vac_Type,Date_Shipped,Mname,County,Zipcode)

	cursor.execute(str1,data)
	connector.commit()
	results = cursor.fetchall()


# For Qn 4.4 query:
# To add a new patient information:
elif choice.strip() == "4":
	Name = input("\nEnter patient name: ")
	Age = input("\nEnter patient's age: ")
	Contact = input("\nEnter Phone contact of the patient: ")
	Vac_Phase = input("\nEnter the phase in which the patient got administered: ")
	Address = input("\nEnter address of patient: ")
	Date = input("\nEnter date of vaccine administeration(mm/dd/yyyy): ")
	m = Date.find('/')
	Month = Date[0:m]
	Date = Date [m+1:]
	d = Date.find('/')
	Day = Date[0:d]
	Date = Date[d+1:]
	Year = Date	
	Date_administered = str(Year)+"-"+str(Month)+"-"+str(Day)

	# To avoid foreign key errors when choosing the VACCINE data:
	print("\nEnter the vaccine type, date shipped and manufacturer of the vaccine from the list: ")
	str1 = "SELECT Vac_Type,Date_shipped,Mname from VACCINE"
	cursor.execute(str1)
	connector.commit()
	results = cursor.fetchall()
	for line in results:
		print(line)

	Vac_Type = input("\nEnter the vaccine type shipped: ")
	Date = input("\nEnter the date doses were shipped to the Federal body: ")
	m = Date.find('/')
	Month = Date[0:m]
	Date = Date [m+1:]
	d = Date.find('/')
	Day = Date[0:d]
	Date = Date[d+1:]
	Year = Date	
	Date_Shipped = str(Year)+"-"+str(Month)+"-"+str(Day)

	Mname = input("\nEnter the vaccine manufacturer name: ")

	Adv_Effects = input("\nEnter if the patient showed any adverse effects(1-yes,0-no): ")
	Id_num = input("\nEnter the unique ID of the patient: ")
	Occupation = input("\nEnter the patient's occupation: ")
	Type_Of_Dose = input("\nEnter the type of dose administered(1 or 2): ")

	# To avoid foreign key error when choosing the place of administeration:
	print("\nEnter the zipcode and County from the list: ")
	str1 = "SELECT Zipcode,County from LOCAL_BODIES"
	cursor.execute(str1)
	connector.commit()
	results = cursor.fetchall()
	for line in results:
		print(line)

	Zipcode = input("\nEnter the zipcode: ")
	County = input("\nEnter the county name: ")

	# Insert command and its execution:
	str1 = "INSERT INTO PATIENT VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	data = (Vac_Type,Name,Age,Contact,Vac_Phase,Address,Id_num,Date_administered,Date_Shipped,Mname,Type_Of_Dose,Occupation,Adv_Effects,Zipcode,County)

	cursor.execute(str1,data)
	connector.commit()
	results = cursor.fetchall()


# For Qn 4.5 query:
# To check if there is any adverse effect for a patient given patient details:
elif choice.strip() == "5":
	Name = input("\nEnter patient name: ")
	Id_num = input("\nEnter patient's ID: ")
	Type_Of_Dose = input("\nEnter the type of dose administered: ")

	# Based on the ID_num, Name and Type of dose administered the result is chosen:
	# If any of the 3 columns do not match with any record in the database,
	# it would return saying there is no such patient
	str1 = "SELECT Adv_Effects from PATIENT where Name = %s and Id_num = %s and Type_of_Dose = %s"
	data = (Name,Id_num,Type_Of_Dose)

	cursor.execute(str1,data)
	connector.commit()
	results = cursor.fetchall()
	if(results == ()):
		print("No such patient")
	for line in results:
		if(line[0] == 1):
			print("The patient has adverse effects")
		else:
			print("The patient has no adverse effects")

# For any wrong option:
else:
	print("Wrong option")