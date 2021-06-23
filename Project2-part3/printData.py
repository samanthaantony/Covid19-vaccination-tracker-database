import pymysql
import pandas


# Connection to the Omega server
connector = pymysql.connect(host='acadmysqldb001p.uta.edu', user='sxj7440', 
	password='abcd@2019', db='sxj7440')

cursor = connector.cursor()


# Showing the existing tables in the database
cursor.execute("SHOW TABLES");
connector.commit()
results = cursor.fetchall()
print(results)


# For Qn2 query:

# Printing FEDERAL table data
print("\n*****************FEDERAL BODY DATA:*****************")
fedGetStr = "SELECT * FROM FEDERAL"
cursor.execute(fedGetStr)
fedResults = cursor.fetchall()
for line in fedResults:
	print("Federal Body Name: ",line[0])


# Printing VACCINE table data
print("\n*****************VACCINE DATA:*****************")
vacGetStr = "SELECT * FROM VACCINE"
cursor.execute(vacGetStr)
vacResults = cursor.fetchall()
for line in vacResults:
	print("Manufacturer Name: ",line[0])
	print("Vaccine type: ",line[1])
	print("Count of doses procured: ",line[2])
	print("Number of doses shipped to the Federal Body: ",line[3])
	print("Name of the Federal Body doses were shipped to: ",line[4])
	print("Date of shipment: ",line[5])
	print("\n")


# Printing STATES table data
print("\n*****************STATE TABLE DATA:*****************")
stateGetStr = "SELECT * FROM STATES"
cursor.execute(stateGetStr)
stateResults = cursor.fetchall()
for line in stateResults:
	print("State Name: ",line[0])
	print("Population of the State: ",line[1])
	print("Number of doses shipped to the State: ",line[2])
	print("Name of the Federal Body that shipped the vaccines: ",line[3])
	print("\n")


# Printing LOCAL_BODIES table data
print("\n*****************LOCAL BODIES TABLE DATA:*****************")
localGetStr = "SELECT * FROM LOCAL_BODIES"
cursor.execute(localGetStr)
localResults = cursor.fetchall()
for line in localResults:
	print("County Name: ",line[0])
	print("Population of the County: ",line[1])
	print("Name of the State where the County belongs to: ",line[2])
	print("Zipcode of the local body: ",line[3])
	print("\n")


# Printing PATIENT table data
print("\n*****************PATIENT TABLE DATA:*****************")
patientGetStr = "SELECT * FROM PATIENT"
cursor.execute(patientGetStr)
patientResults = cursor.fetchall()
for line in patientResults:
	print("Name of the Patient: ",line[1])
	print("Patient's Age: ",line[2])
	print("Patient's Phone: ",line[3])
	print("Patient's Address: ",line[5])
	print("Patient's unique ID: ",line[6])
	print("Patient was administered on: ",line[7])
	print("Patient's occupation/status: ",line[11])
	print("Check if Patient had any adverse effects after administration: ",line[12])
	print("Type of Vaccine that was administered: ",line[0])
	print("Date the doses were shipped : ",line[8])
	print("Type of the dose administered(1 or 2): ",line[10])
	print("Manufacturer Name of the Vaccine: ",line[9])
	print("County where the Patient was administered: ",line[14])
	print("Zipcode where the Patient was administered: ",line[13])
	print("Phase in which the Patient was administered: ",line[4])
	print("\n")		



# Printing ALLERGIES table data
print("\n*****************ALLERGIES TABLE DATA:*****************")
allergiesGetStr = "SELECT * FROM ALLERGIES"
cursor.execute(allergiesGetStr)
allergiesResults = cursor.fetchall()
for line in allergiesResults:
	print("Allergy Name: ",line[0])
	print("ID of the Patient: ",line[1])
	print("Type of Dose the Patient was administered: ",line[2])
	print("\n")



# Printing MED_Condition table data
print("\n*****************MED Conditions TABLE DATA:*****************")
medGetStr = "SELECT * FROM MED_Condition"
cursor.execute(medGetStr)
medResults = cursor.fetchall()
for line in medResults:
	print("Condition Name: ",line[0])
	print("ID of the Patient: ",line[1])
	print("Type of Dose the Patient was administered: ",line[2])
	print("\n")



# Printing VACCINATION_CAMPS table data
print("\n*****************VACCINATION CAMPS TABLE DATA:*****************")
vacCampGetStr = "SELECT * FROM VACCINATION_CAMPS"
cursor.execute(vacCampGetStr)
vacCampResults = cursor.fetchall()
for line in vacCampResults:
	print("Location of the camp: ",line[0])
	print("Zipcode of the camp: ",line[2])
	print("County Name: ",line[1])
	print("\n")



# Printing HEALTH_CARE_CENTERS table data
print("\n*****************HEALTH CARE CENTERS TABLE DATA:*****************")
healthCampGetStr = "SELECT * FROM HEALTH_CARE_CENTERS"
cursor.execute(healthCampGetStr)
healthCampResults = cursor.fetchall()
for line in healthCampResults:
	print("Name of the center: ",line[0])
	print("Type of the center: ",line[1])
	print("Zipcode of the camp: ",line[3])
	print("County Name: ",line[2])
	print("\n")



# Printing LABS_AND_PHARMACIES table data
print("\n*****************LABS AND PHARMACIES TABLE DATA:*****************")
labCampGetStr = "SELECT * FROM LABS_AND_PHARMACIES"
cursor.execute(labCampGetStr)
labCampResults = cursor.fetchall()
for line in labCampResults:
	print("Name of the outlet: ",line[0])
	print("Type of the outlet: ",line[1])
	print("Zipcode of the camp: ",line[3])
	print("County Name: ",line[2])
	print("\n")



# For Qn3 query:

# Displaying datewise progress by the County
# select Date_administered,County,count(Date_administered) from PATIENT group by County,Date_administered order by Date_administered;
print("\n***************** Date wise progress by County *****************")
DateProgressByCounty = "select Date_administered,County,count(Date_administered) from PATIENT group by County,Date_administered order by Date_administered"
cursor.execute(DateProgressByCounty)
DateProgressByCountyResults = cursor.fetchall()
# print(DateProgressByCountyResults)
for line in DateProgressByCountyResults:
	print(line)


# Displaying datewise progress by the State
# select Date_administered,Sname,count(Date_administered) from PATIENT,LOCAL_BODIES where PATIENT.County = LOCAL_BODIES.County group by Sname,Date_administered order by Date_administered;
print("\n***************** Date wise progress by State *****************")
DateProgressByState = "select Date_administered,Sname,count(Date_administered) from PATIENT,LOCAL_BODIES where PATIENT.County = LOCAL_BODIES.County group by Sname,Date_administered order by Date_administered"
cursor.execute(DateProgressByState)
DateProgressByStateResults = cursor.fetchall()
# print(DateProgressByCountyResults)
for line in DateProgressByStateResults:
	print(line)

# For Qn3 query:
#Displaying Monthwise progress by the County
print("\n***************** Monthwise progress by County *****************")
MonthProgressByCounty= "select month(Date_administered) Month , County, count(County) cumulative_progress from PATIENT group by County,month(Date_administered)"
cursor.execute(MonthProgressByCounty)
MonthProgressByCountyResults = cursor.fetchall()
# print(DateProgressByCountyResults)
for line in MonthProgressByCountyResults:
	print(line)

# Displaying Monthwise progress by the State
print("\n***************** Monthwise progress by State *****************")       
MonthProgressByState="select month(Date_administered) Month , Sname, count(Sname) cumulative_progress from PATIENT,LOCAL_BODIES where PATIENT.County = LOCAL_BODIES.County  group by Sname,month(Date_administered)"
cursor.execute(MonthProgressByState)
MonthProgressByStateResults = cursor.fetchall()
# print(DateProgressByStateResults)
for line in MonthProgressByStateResults:
	print(line)