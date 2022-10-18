import record as rec
#import xml.etree.ElementTree as ET

def Save(records, path):
    try:        
        with open(path, "w", encoding='utf-8') as duck:
            duck.write("<Phonebook>")
            for r in records:
                duck.write("<Record>")
                duck.write("<Lastname>" + r.Lastname + "</Lastname>")
                duck.write("<Firstname>" + r.Firstname + "</Firstname>")                
                duck.write("<Telephone>" + r.Telephone + "</Telephone>")
                duck.write("<Description>" + r.Description + "</Description>")                
                duck.write("</Record>")
            duck.write("</Phonebook>")
    except Exception as e:
        print(e)
        
def Open(path):
    records = []
    try:
        tree = ET.parse(path)
        root = tree.getroot()
        for r in root.findall("Record"):
                fn = r.find('Firstname').text
                ln = r.find('Lastname').text
                tel = r.find('Telephone').text
                ds = r.find('Description').text
                records.append(rec.record(ln, fn, tel, ds))
        return records
    except Exception as e:
        print(e)
    return records