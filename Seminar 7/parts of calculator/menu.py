
print("Calculator welcomes you!", sep="\n")
print()
print()
print("Working with:", sep="\n")
print("1 - rational", "2 - complex", "0 - exit", sep="\n")

ent_num = input()

if ent_num == "1":
    print("Choose the operation: ")
    print("1 - summary", "2 - subtraction", "3 - multiplication", "4 - division", "5 - power", "6 - square root", "0 - previous menu", sep="\n")

if ent_num == "2":
    print("Choose the operation: ")
    print("1 - summary", "2 - subtraction", "3 - multiplication", "4 - division", "5 - power", "6 - square root", "0 - previous menu", sep="\n")

if ent_num == "0":
    print("Oops, see you later!")