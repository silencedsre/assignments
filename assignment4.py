#IMPLEMENTING ROCK PAPER SISSIORS

import random
dict_rps={
    0:"ROCK",
    1:"PAPER",
    2:"SISSIORS"
}

list_win=[[0,2],[2,1],[1,0]]
list_compare=[]

while True:
    com_input = random.randint(0, 2)
    user_input= int(input("ENTER 0 FOR ROCK, 1 for PAPER, 2 for SISSIORS: "))

    if(user_input>2):
        print("ENTER VALID NUMBER(0-2)")
        exit()
    # how to goto while?

    print("USER HITS: "+str(dict_rps[user_input]))
    print("COMPUTER HITS: "+str(dict_rps[com_input]))

    if user_input==com_input:
        print("DRAW!")
        exit()
    #how to goto while?

    list_compare.append(user_input)
    list_compare.append(com_input)

    for items in list_win:
        if list_compare==items:
            print("USER WINS")

        elif list_compare==items[::-1]:
            print("COMPUTER WINS")
