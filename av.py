#import Libraries
import hashlib
import glob
import os
#GUI Libraries
import tkinter
from tkinter import *
import tkinter.messagebox
#Database Libraries
import mysql.connector

mainframe = tkinter.Tk()
mainframe.wm_title("Anti Malware")

frame = Frame(mainframe, height=150, width=750)
frame.pack()

#Database Connection
db = mysql.connector.connect(host='localhost', user='root', password='root', database='known_hash')
cursor = db.cursor()

sql_statement = "SELECT * FROM HASHES"

cursor.execute(sql_statement)

find_hash = cursor.fetchall()

#Dialog Box
mainframe.text = Text(mainframe, width=100)

def findhashes():
    dirs = glob.glob("C:/Users/Ian/Documents/antivirus-master/testav/*")  #Reads all files in a directory

    totalfiles=0
    knownfiles=0

    for file in dirs: #Loops through files
        with open(file, 'rb') as getmd5:    #Opens files in a read only mode puts files in a variable
            filehash = getmd5.read()  #variable is read then stored again
            gethash = hashlib.md5(filehash).hexdigest()    #data is then hashed and put into hex
            print("Filename: "+file+"  MD5: " + gethash)
            mainframe.text.insert(END, "Filename: "+file+"  MD5: " + gethash+"\n")

            hashed = []

            for hashed in find_hash:
                knownhash = hashed[0]

                print ("MD5 = ", knownhash)
                        

            if knownhash == gethash:  #Compares a knownhash to each hash
                print("Known File Found!!! \n"+knownhash+"Filename: "+file)
                mainframe.text.tag_add("known", 1.0)
                mainframe.text.tag_config("known", background="red")    #known files are displayed green
                mainframe.text.insert(END, "Known File Found!!! \n"+knownhash+"Filename: "+file+"\n", "known")
                totalfiles+=1
                knownfiles += 1

                #deleteoption = raw_input("Do You Want To Delete This File? (Y/N): ")  #User can select to delete file
                deleteoption = tkinter.messagebox.askyesno("File Found", "Would You Like To Delete?\n"+file)

                if deleteoption == True:   #If user inputs "yes"
                    print("File is Deleted!")    #Notifies user
                    mainframe.text.tag_add("delete", 1.0)
                    mainframe.text.tag_config("delete", background="orange")    #delete files are displayed green
                    mainframe.text.insert(END, "File is Deleted!"+"\n", "delete")

                    getmd5.close()
                    os.remove(file)    #Uses os library to delete file

                else:    #If user selects "no"
                    print("Known File Not Deleted")
                    mainframe.text.insert(END, "Known File Not Deleted"+"\n", "known") #File is displayed in red

            else:    #If no known files found
                print("No Known File Found")
                mainframe.text.tag_add("unknown", 1.0)    #unknown files are displayed green
                mainframe.text.tag_config("unknown", background="green")
                mainframe.text.insert(END, "No Known File Found"+"\n", "unknown")
                totalfiles += 1

    print("Total Files Scanned: ", totalfiles)
    # Counter Label
    mainframe.total = Label(mainframe, text="Total Files Scanned: %d" % totalfiles)
    mainframe.total.pack(side=TOP)

    #Known Files
    mainframe.known = Label(mainframe, text="Total Files Known Files: %d" % knownfiles)
    mainframe.known.pack(side=TOP)

#Scan Button
scan = Button(mainframe, text="Scan", command=findhashes)
scan.pack(side=TOP)

mainframe.text.pack(side=BOTTOM)

mainframe.mainloop()
