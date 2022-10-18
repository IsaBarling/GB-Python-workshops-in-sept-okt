import record as rec
def Save(records, path):
    try:
        with open(path, "w", encoding='utf-8') as duck:
            for r in records:
                if r.Lastname is not None:
                    duck.write(r.Lastname + ";" + r.Firstname + ";" + r.Telephone + ";" + r.Description + ";" + "\n")
    except Exception as e:
        print(e)
        
def Open(path):
    records = []
    try:
        with open(path, "r", encoding='utf-8') as duck:
            lines = duck.readlines()
            for l in lines:
                arr = l.split(";")
                r = rec.record(arr[0],arr[1], arr[2], arr[3])
                records.append(r)
                
    except Exception as e:
        print(e)
    return records