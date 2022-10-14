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
    for i in range(1, 10):
        if(i == 4 or i == 7):
            line += "\r\n" + GetLine() + "\r\n"
        line += str(i) + "\t"
        
    line += "\r\n" + GetLine() + "\r\n"
    return line

    
currentField = GetEmptyField()
print(currentField)
moves = 9
finish = False
nums = [[],[]]
draw = True
ch = ''

while(moves >= 0 and not finish):
    if(moves%2 == 1):
        print("Player 1")
    else:
        print("Player 2")
    player = moves%2

    if(player == 0):
        ch = "❌"
    else:
        ch = "⭕"
    num = -1

    while(moves > 0):
        try:
            num = int(input("Pos:"))
            if(num > 9 or num < 0):
                print("Wrong input1")
            if(num in nums):
                print("Already filled")
            else:
                print(num)
                nums.append(num)  # type: ignore
                print(nums)
                if(player==0):
                    nums[0].append(num)
                else:
                    nums[1].append(num)
               
                currentField = currentField.replace(str(num), ch)
                break;                   
        except Exception as e:
            print(e)
            print("Wrong input")
      
    print(currentField)
    
    if(player == 0):
        finish = CheckForWinner(nums[0])
    else:
        finish = CheckForWinner(nums[1])
    if(finish):
        if(player == 1):
            print("Player 1 won!")
        else:
            print("Player 2 won!")
        draw = False
    moves -= 1
if(draw):
    print("Draw")