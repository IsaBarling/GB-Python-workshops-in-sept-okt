import json as JZ
import record as rec

def Save(records, path):
    print(records)
    records2 = []
    for r in records:
        records2.append(f'{ "Firstname" : "{r.Firstname}", "Lastname" : "{r.Lastname}" , "Telephone" : "{r.Telephone}" , "Description" : "{r.Description}" }')
    with open(path, "w", encoding='utf-8') as duck:
        duck.write("[" + ",".join(records2) + "]")
    return
    try:
        records2 =[]
        for rec in records:
            print(rec.toJSON())
            records2.append((rec.__dict__))
            print(records2)
        print(records2)
        with open(path, "w", encoding='utf-8') as duck:
            for rec in records:
                #duck.write(str(records2))
                JZ.dump(records2, duck)
        
        with open(path, "r+", encoding='utf-8') as duck:
            text = duck.read()
            text = text.replace("][", "")
            
            duck.write(text)
            #for r in records:
                #duck.write(r.Surname + ";" + r.Firstname + ";" + r.Telephone + ";" + r.Description + ";" + "\n")
    except Exception as e:
        print(e)
        
def Open(path):
    records = []
    try:
        with open(path, "r", encoding='utf-8') as duck:
            data = duck.read()
            data = data.split("}")
            for i in range(len(data)):
                el = data[i].split(",")
                fn = ""
                ln = ""
                tel = ""
                ds = ""
                for val in el:
                    if ":" not in val:
                        continue
                    pair = val.strip().split(":")
                    p0 = pair[0].strip()
                    p1 = pair[1].strip()
                    key = p0.split("\"")[1]
                    value = p1.strip()[1:len(p1)-1]
                    if("Firstname" in key):
                        fn = value
                    elif("Lastname" in key):
                        ln = value
                    elif("Telephone" in key):
                        tel = value
                    elif("Description" in key):
                        ds = value
                
                if(ln != "" and fn != "" and tel != ""):
                    r = rec.record(ln, fn, tel, ds)
                    records.append(r)
                
    #        data = JZ.load(duck)
     #       print(data)
      #      for line in data:
       #         r = rec.record(line["Lastname"],line["Firstname"], line["Telephone"], line["Description"])
        #        print(r)
         #       records.append(r)                
                
    except Exception as e:
        print(e)
    print(records)
    return records

