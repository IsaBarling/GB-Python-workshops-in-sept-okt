def CheckForWinner(nums):
    check = False
    winningPos = [[1, 2, 3] , [4, 5, 6], [7, 8, 9], [1,4,7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3,5,7]]
    for pos in winningPos:
        n = 0
        for num in pos:
            if len(nums)> 0 and num in nums:
                n += 1
        if n == 3:
            check = True
    return check

def GetLine():
    val = ""
    for i in range(20):
        val += "-"
    return val

def GetEmptyField():
    line = ""
    line += GetLine() + "\r\n"
    for i in range(1, 4):
        line += str(i) + "\t"
    line +=  "\r\n" + GetLine() + "\r\n"
    for i in range(4, 7):
        line += str(i) + "\t"
    line +=  "\r\n"+ GetLine() + "\r\n"
    for i in range(7, 10):
        line += str(i) + "\t"
    return line

    
field = GetEmptyField()
print(field)
currentField = field
moves = 9
finish = False
nums = []
numsP1 = []
numsP2 = []

while(moves >= 0 and not finish):
    if(moves%2 == 1):
        print("Player 1")
    else:
        print("Player 2")
    player = moves%2
    ch = ''
    if(player == 0):
        ch = "❌"
    else:
        ch = "⭕"
    num = -1
    while(True):
        try:
            num = int(input("Pos:"))
            if(num > 9 or num < 0):
                print("Wrong input1")
            if(num in nums):
                print("Already filled")
            else:
                print(num)
                nums.append(num)
                print(nums)
                if(player==0):
                    numsP1.append(num)
                else:
                    numsP2.append(num)
               
                currentField = currentField.replace(str(num), ch)
                break;                   
        except Exception as e:
            print(e)
            print("Wrong input")
      
    print(currentField)
    
    numsP2.sort()
    print(numsP1)
    if(player == 0):
        finish = CheckForWinner(numsP1)
    else:
        finish = CheckForWinner(numsP2)
    if(finish):
        print("Player " + str(player+1) + " won!")
    moves -= 1