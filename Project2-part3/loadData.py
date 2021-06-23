import pymysql
import pandas

# For connection to Omega server
connector = pymysql.connect(host='acadmysqldb001p.uta.edu', user='sxj7440', 
	password='abcd@2019', db='sxj7440')

cursor = connector.cursor()

# Showing the existing tables in database
cursor.execute("SHOW TABLES");
connector.commit()
results = cursor.fetchall()
print(results)


# For Qn1 query:

# For adding records into the FEDERAL table
# The data is read from the file FEDERAL.csv
fFederal = pandas.read_csv('FEDERAL.csv')
rows = len(fFederal)
# print(rows)

for i in range(0,rows):
	line = fFederal.iloc[i,:]
	# print(line)

	Fname = str(line['Fname'])
	print(Fname)

	try:
		str1 = "INSERT INTO FEDERAL VALUES (%s)"
		data = (Fname)

		cursor.execute(str1,data)
		connector.commit()
		results = cursor.fetchall()			

	except Exception as e:
		print(e)
		pass


# For adding records into the VACCINE table
# The data is read from the VACCINE.csv
fVaccine = pandas.read_csv('VACCINE.csv')
rows = len(fVaccine)
# print(rows)

for i in range(0,rows):
	line = fVaccine.iloc[i,:]
	# print(line)

	Mname = str(line['Mname'])
	# print(Mname)
	Vac_Type = str(line['Vac_Type'])
	Proc_count = str(line['Proc_count'])
	NumDoses_shipped = str(line['NumDoses_shipped'])
	Fname = str(line['Fname'])
	Date = str(line['Date_shipped'])
	# print(Date)

	m = Date.find('/')
	Month = Date[0:m]
	Date = Date [m+1:]
	# print("M",Month)

	d = Date.find('/')
	Day = Date[0:d]
	Date = Date[d+1:]
	# print("D",Day)

	Year = Date
	# print("Y",Year)
	Date = str(Year)+"-"+str(Month)+"-"+str(Day)	

	# print(Date)

	try:
		str1 = "INSERT INTO VACCINE VALUES (%s,%s,%s,%s,%s,%s)"
		data = (Mname,Vac_Type,Proc_count,NumDoses_shipped,Fname,Date)

		cursor.execute(str1,data)
		connector.commit()
		results = cursor.fetchall()			

	except Exception as e:
		print(e)
		pass


# For adding records into the STATES table
# The data is read from the STATES.csv
fStates = pandas.read_csv('STATES.csv')
rows = len(fStates)
# print(rows)

for i in range(0,rows):
	line = fStates.iloc[i,:]
	# print(line)

	Sname = str(line['Sname'])
	# print(Mname)
	Spopulation = str(line['Spopulation'])
	No_of_dose = str(line['No_of_dose'])
	Fname = str(line['Fname'])


	try:
		str1 = "INSERT INTO STATES VALUES (%s,%s,%s,%s)"
		data = (Sname,Spopulation,No_of_dose,Fname)

		cursor.execute(str1,data)
		connector.commit()
		results = cursor.fetchall()			

	except Exception as e:
		print(e)
		pass


# For adding records into the LOCAL_BODIES table
# The data is read from the LOCAL_BODIES.csv
fLocal_bodies = pandas.read_csv('LOCAL_BODIES.csv')
rows = len(fLocal_bodies)
# print(rows)

for i in range(0,rows):
	line = fLocal_bodies.iloc[i,:]
	# print(line)

	County = str(line['County'])
	# print(Mname)
	Lpopulation = str(line['Lpopulation'])
	Sname = str(line['Sname'])
	Zipcode = str(line['Zipcode'])


	try:
		str1 = "INSERT INTO LOCAL_BODIES VALUES (%s,%s,%s,%s)"
		data = (County,Lpopulation,Sname,Zipcode)

		cursor.execute(str1,data)
		connector.commit()
		results = cursor.fetchall()			

	except Exception as e:
		print(e)
		pass



# For adding records into the VACCINATION_CAMPS table
# The data is read from the VACCINATION_CAMPS.csv
fVaccination_camps = pandas.read_csv('VACCINATION_CAMPS.csv')
rows = len(fVaccination_camps)
# print(rows)

for i in range(0,rows):
	line = fVaccination_camps.iloc[i,:]
	# print(line)

	Location = str(line['Location'])
	# print(Mname)
	County = str(line['County'])
	Zipcode = str(line['Zipcode'])


	try:
		str1 = "INSERT INTO VACCINATION_CAMPS VALUES (%s,%s,%s)"
		data = (Location,County,Zipcode)

		cursor.execute(str1,data)
		connector.commit()
		results = cursor.fetchall()			

	except Exception as e:
		print(e)
		pass


# For adding records into the HEALTH_CARE_CENTERS table
# The data is read from the HEALTH_CARE_CENTERS.csv
fHealth_care_centers = pandas.read_csv('HEALTH_CARE_CENTERS.csv')
rows = len(fHealth_care_centers)
# print(rows)

for i in range(0,rows):
	line = fHealth_care_centers.iloc[i,:]
	# print(line)

	Name = str(line['Name'])
	Type = str(line['Type'])
	# print(Mname)
	County = str(line['County'])
	Zipcode = str(line['Zipcode'])


	try:
		str1 = "INSERT INTO HEALTH_CARE_CENTERS VALUES (%s,%s,%s,%s)"
		data = (Name,Type,County,Zipcode)

		cursor.execute(str1,data)
		connector.commit()
		results = cursor.fetchall()			

	except Exception as e:
		print(e)
		pass


# For adding records into the LABS_AND_PHARMACIES table
# The data is read from the LABS_AND_PHARMACIES.csv
fLabs_and_pharmacies = pandas.read_csv('LABS_AND_PHARMACIES.csv')
rows = len(fLabs_and_pharmacies)
# print(rows)

for i in range(0,rows):
	line = fLabs_and_pharmacies.iloc[i,:]
	# print(line)

	Name = str(line['Name'])
	Type = str(line['Type'])
	# print(Mname)
	County = str(line['County'])
	Zipcode = str(line['Zipcode'])


	try:
		str1 = "INSERT INTO LABS_AND_PHARMACIES VALUES (%s,%s,%s,%s)"
		data = (Name,Type,County,Zipcode)

		cursor.execute(str1,data)
		connector.commit()
		results = cursor.fetchall()			

	except Exception as e:
		print(e)
		pass



# For adding records into the PATIENT table
# The data is read from the PATIENT_1.csv
fPatient = pandas.read_csv('PATIENT_1.csv')
rows = len(fPatient)
# print(rows)

for i in range(0,rows):
	line = fPatient.iloc[i,:]
	# print(line)

	Name = str(line['Name'])
	Age = str(int(line['Age']))
	# print(Age)
	Contact = str(line['Contact'])
	Vac_Phase = str(line['Vac_Phase'])
	Address = str(line['Address'])
	Date = str(line['Date_Administered'])
	m = Date.find('/')
	Month = Date[0:m]
	Date = Date [m+1:]
	d = Date.find('/')
	Day = Date[0:d]
	Date = Date[d+1:]
	Year = Date
	Date_Administered = str(Year)+"-"+str(Month)+"-"+str(Day)

	Vac_Type = str(line['Vac_Type'])

	Date = str(line['Date_Shipped'])
	m = Date.find('/')
	Month = Date[0:m]
	Date = Date [m+1:]
	d = Date.find('/')
	Day = Date[0:d]
	Date = Date[d+1:]
	Year = Date
	Date_Shipped = str(Year)+"-"+str(Month)+"-"+str(Day)	

	Adv_Effects = str(line['Adv_Effects'])
	Id_Num = str(line['Id_Num'])
	Occupation = str(line['Occupation'])
	Type_Of_Dose = str(line['Type_Of_Dose'])
	Zipcode = str(line['ZipCode'])
	County = str(line['County'])
	Mname = str(line['Mname'])


	# print(Date)

	try:
		str1 = "INSERT INTO PATIENT VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		data = (Vac_Type,Name,Age,Contact,Vac_Phase,Address,Id_Num,Date_Administered,Date_Shipped,Mname,Type_Of_Dose,Occupation,Adv_Effects,Zipcode,County)

		cursor.execute(str1,data)
		connector.commit()
		results = cursor.fetchall()			

	except Exception as e:
		print(e)
		pass


# For adding records into the ALLERGIES table
# The data is read from the ALLERGY.csv
fAllergy = pandas.read_csv('ALLERGY.csv')
rows = len(fAllergy)
# print(rows)

for i in range(0,rows):
	line = fAllergy.iloc[i,:]
	# print(line)

	Allergy = str(line['Allergy'])
	Id_Num = str(int(line['Id_Num']))
	# print(Age)
	Type_Of_Dose = str(line['Type_Of_Dose'])

	# print(Date)

	try:
		str1 = "INSERT INTO ALLERGIES VALUES (%s,%s,%s)"
		data = (Allergy,Id_Num,Type_Of_Dose)

		cursor.execute(str1,data)
		connector.commit()
		results = cursor.fetchall()			

	except Exception as e:
		print(e)
		pass



# For adding records into the MED_Condition table
# The data is read from the MED_Condition.csv
fMED_condition = pandas.read_csv('MED_Condition.csv')
rows = len(fMED_condition)
# print(rows)

for i in range(0,rows):
	line = fMED_condition.iloc[i,:]
	# print(line)

	cond = str(line['Condition'])
	Id_Num = str(int(line['Id_num']))
	# print(Age)
	Type_Of_Dose = str(line['Type_Of_Dose'])

	# print(Date)

	try:
		str1 = "INSERT INTO MED_Condition VALUES (%s,%s,%s)"
		data = (cond,Id_Num,Type_Of_Dose)

		cursor.execute(str1,data)
		connector.commit()
		results = cursor.fetchall()			

	except Exception as e:
		print(e)
		pass



# For adding records into the HAVE table
# The data is read from the HAVE.csv
fHAVE = pandas.read_csv('HAVE.csv')
rows = len(fHAVE)
# print(rows)

for i in range(0,rows):
	line = fHAVE.iloc[i,:]
	# print(line)

	No_Of_Doses = str(line['No_Of_Doses'])
	Date = str(line['Date_Received'])
	m = Date.find('/')
	Month = Date[0:m]
	Date = Date [m+1:]
	d = Date.find('/')
	Day = Date[0:d]
	Date = Date[d+1:]
	Year = Date
	Date_received = str(Year)+"-"+str(Month)+"-"+str(Day)
	Vac_Type = str(line['Vac_Type'])
	Date = str(line['Date_Shipped'])
	m = Date.find('/')
	Month = Date[0:m]
	Date = Date [m+1:]
	d = Date.find('/')
	Day = Date[0:d]
	Date = Date[d+1:]
	Year = Date	
	Date_Shipped = str(Year)+"-"+str(Month)+"-"+str(Day)
	Mname = str(line['Mname'])
	County = str(line['County'])
	ZipCode = str(line['ZipCode'])

	# print(Date)

	try:
		str1 = "INSERT INTO HAVE VALUES (%s,%s,%s,%s,%s,%s,%s)"
		data = (No_Of_Doses,Date_received,Vac_Type,Date_Shipped,Mname,County,ZipCode)

		cursor.execute(str1,data)
		connector.commit()
		results = cursor.fetchall()			

	except Exception as e:
		print(e)
		pass
