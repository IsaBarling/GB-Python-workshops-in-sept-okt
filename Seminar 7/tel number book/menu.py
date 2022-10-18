import record as re
import csv
import jfather as j
#import xml
        
def menu0():
    print("What do you want to do?")
    print("1. Create new data")
    print("2. Open data")
    print("3. Save current values into file")
    print("4. Show current values")
    return input()

def menu1():
    records = []
    while True:
        
        uInput = input("Enter the record(LName,FName,Tel,Des):")
        try:
            arr = uInput.split(",")
            r = re.record(arr[0],arr[1], arr[2], arr[3])            
            records.append(r)
            print("Record was successfully read")
            choice = input("Do you want to add more records? (Y/N)")
            if(choice == "N"):
                break;
        except Exception as E:
            print(e)
    path = input("Specify path to save data:")
    try:
        arr = path.split(".")
        ext = arr[len(arr)-1]
        if( ext == "csv"):
            csv.Save(records, path)
        elif(ext == "json"):
            j.Save(records, path)
        elif(ext == "xml"):
            j.Save(records, path)
        else:
            print("Extension is unknown!")
    except Exception as e:
        print(e)
        
def menu2(records):
    path = input("Specify path to load data:")
    arr = path.split(".")
    uInput = input("Do you want to append data to the current? Y/N")
    try:
        records2 = []
        ext = arr[len(arr)-1]
        if(ext =="csv"):
            records2 = csv.Open(path)
        elif(ext == "json"):
            records2 = j.Open(path)
        elif(ext == "xml"):
            records2 = j.Open(path)
        else:
            print("Extension is unknown!")
            return records
        print(records2)
        if(uInput == "Y"):               
            records += records2
        else:
            records = records2
    except Exception as e:
        print(e)
    
    return records

def menu3(records):
    path = input("Specify path to save data:")
    arr = path.split(".")
    ext = arr[len(arr)-1]
    if( ext == "csv"):
        csv.Save(records, path)
    elif(ext == "json"):
        j.Save(records, path)
    elif(ext == "xml"):
        j.Save(records, path)#xml is depricated
    else:
        print("Extension is unknown!")