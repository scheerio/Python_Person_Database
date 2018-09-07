#EXAMPLE USING SQLITE WITH PYTHON: DATABASE OF PEOPLE
#Created by Ben Scheer, 9/1/18

#tools to import
import sqlite3
import time

#this handles displaying info to the user
def handleInfo():
#will repeat if input is wrong
    continueThis = True
    while continueThis == True:
        activity = raw_input('Type in 1 to view the youngest age. Type in 2 to view the oldest age. Type in 3 to view average age. Type in 4 to view all entries between two dates: ')
        ageArray = []
        #try printing all the info needed
        try:
            conn = sqlite3.connect('people.db')
            cursor = conn.execute("SELECT NAME, AGE, DATE from PEOPLE")
            #runs through data
            for row in cursor:
                print "NAME = ", row[0]
                print "AGE = ", row[1]
                print "DATE = ", row[2], "\n"
                ageArray.append(row[1])
            conn.commit()
            conn.close()
            #choice logic
            if activity == "1":
                print("\nThe youngest age is:")
                print(min(ageArray))
                continueThis = False
            if activity == "2":
                print("\nThe oldest age is:")
                print(max(ageArray))
                continueThis = False
            if activity == "3":
                print("\nThe average age is:")
                print(sum(ageArray) / float(len(ageArray)))
                continueThis = False
            if activity == "4":
                date1 = raw_input('Enter the first date to start at (in the format of 2018-09-04): ')
                date2 = raw_input('Enter the second date to end at (in the format of 2018-09-05): ')
                conn = sqlite3.connect('people.db')
                print(date1)
                print(date2)
                cursor = conn.execute("SELECT * FROM PEOPLE WHERE DATE BETWEEN '" + date1 + "' AND '" +  date2 + "'")
                print ("\nHere are all the entries in the database for your dates.")
                for row in cursor:
                    print "NAME = ", row[0]
                    print "AGE = ", row[1]
                    print "DATE = ", row[2], "\n"
                print("\nOperation done successfully.\n")
                conn.commit()
                conn.close()
                continueThis = False
            else:
                continueThis = True
        except:
            print("Data not here!")

def setUpDatabase():
    #do stuff here
    conn = sqlite3.connect('people.db')
    print "\nOpened database successfully";
    conn.execute('''CREATE TABLE IF NOT EXISTS PEOPLE
        (NAME TEXT PRIMARY KEY,
        AGE INTEGER NOT NULL,
        DATE TEXT NOT NULL);''')
    print "Table created successfully\n";
    conn.close()

#this functions handles entered data
def enterNew():
    age = 0
    quit = False
    array = []
    tryAgain = True
    while quit == False:
        tryAgain = True
        name = raw_input('Enter the name of the person: ')
        age = raw_input('Enter the age of the person: ')
        currentTime = time.strftime('%Y-%m-%d %H:%M:%S')
        print("\nThis will be stored in the database now.")
        #store here
        conn = sqlite3.connect('people.db')
        conn.execute("INSERT INTO PEOPLE (NAME, AGE, DATE) VALUES (?, ?, ?)",
                    (name, age, currentTime))
        print("Success.")
        conn.commit()
        print "Records created successfully";
        conn.close()
        #see if user wants to try again
        while tryAgain == True:
            goAgain = raw_input("Do you wish to enter another person? y/n: ")
            if goAgain == "n":
                quit = True
                tryAgain = False
            elif goAgain == "y":
                tryAgain = False
            else:
                tryAgain = True
    print("Program done.")

#see whether user wants to get data, or put in new data
noMistakes = True
setUpDatabase()
#will repeat if input is wrong
while noMistakes == True:
    #see what user wants to do
    activity = raw_input('Type in 1 to see info from the database. Type in 2 to enter a new person. Type in 3 to reset all data on the database: ')
    #go to entering new data
    if activity == "2":
        noMistakes = False
        enterNew()
    #delete all data
    if activity == "3":
        conn = sqlite3.connect('people.db')
        print "Opened database successfully";
        conn.execute("DROP TABLE PEOPLE;")
        conn.commit()
        conn.close()
    #list info
    if activity == "1":
        noMistakes = False
        handleInfo()
    else:
        print("You need to say '1' or '2' or '3'. Try again.")















