#import libraries
import hashlib
import glob
import os

def findhashes():
    dirs = glob.glob("C:/Users/shane/Downloads/Malware_Files/Malware/*")  #Reads all files in a directory

    for file in dirs: #Loops through files
        with open(file, 'rb') as getmd5:    #Opens files in a read only mode puts files in a variable
            filehash = getmd5.read()  #variable is read then stored again
            gethash = hashlib.md5(filehash).hexdigest()    #data is then hashed and put into hex
            print("Filename: "+file+"  MD5: " + gethash)

            knownhash="2a480f28394b06373b88aad510a3ed2d"

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
