import record as rec

import menu as m

records = []

text = ""
print("Welcome, roockie, to exit the program press q")
    
while(True):
    text = m.menu0()
    if(text=="q"):
        break;
    choice = ""
    try:
        choice = int(text)
        if choice == 1:
            m.menu1()
        elif choice == 2:
            records = m.menu2(records)
        elif choice == 4:            
            for record in records:
                try:
                    record.Show()
                except Exception as e:
                    print(e)
    except:
        print("Wrong input, asshole!")
    