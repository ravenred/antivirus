#import libraries
import hashlib
import glob
import os
#Database Libraries
import mysql.connector

#Database Connection
db = mysql.connector.connect(host='localhost', user='root', password='root', database='known_hash')
cursor = db.cursor()

sql_statement = "SELECT * FROM HASHES"

cursor.execute(sql_statement)

find_hash = cursor.fetchall()

def findhashes():
    dirs = glob.glob("C:/Users/Ian/Documents/testav/*")  #Reads all files in a directory

    for file in dirs: #Loops through files
        with open(file, 'rb') as getmd5:    #Opens files in a read only mode puts files in a variable
            filehash = getmd5.read()  #variable is read then stored again
            gethash = hashlib.md5(filehash).hexdigest()    #data is then hashed and put into hex
            print("Filename: "+file+"  MD5: " + gethash)

            hashed = []

            for hashed in find_hash:
                knownhash = hashed[0]

                #print ("MD5 = ", knownhash)

            if knownhash == gethash:  #Compares a knownhash to each hash
                print("Known File Found!!! \n"+knownhash+"Filename: "+file)

                deleteoption = input("Do You Want To Delete This File? (Y/N): ")  #User can select to delete file

                if deleteoption == "y":   #If user inputs "y"
                    print("File is Deleted!")    #Notifies user
                    os.remove(file)    #Uses os library to delete file

                else:    #If user selects "n"
                    print("Known File Not Deleted")

            else:    #If no known files found
                print("No Known File Found")
findhashes()
