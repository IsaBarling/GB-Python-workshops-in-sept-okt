import json as JZ
import record as rec

def Save(records, path):
    print(records)
    records2 = []
    for r in records:
        records2.append(f'{ "Firstname" : "{r.Firstname}", "Lastname" : "{r.Lastname}" , "Telephone" : "{r.Telephone}" , "Description" : "{r.Description}" }')
    with open(path, "w", encoding='utf-8') as duck:
        duck.write("[" + ",".join(records2) + "]")
        
        
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
    except Exception as e:
        print(e)
    print(records)
    return records

