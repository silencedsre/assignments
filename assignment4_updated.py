import random
dict_rps={
    0:"ROCK",
    1:"PAPER",
    2:"SISSIORS"
}

list_win=[[0,2],[2,1],[1,0]]
list_compare=[]
count_user=0
count_computer=0

while True:
    user_input= int(input("\n\nENTER 0 FOR ROCK, 1 for PAPER, 2 for SISSIORS: "))
    com_input = random.randint(0, 2)

    if(user_input>3):
        print("ENTER VALID HIT BETWEEN NUMBER(0-2) OR NUMBER 3 TO EXIT")

    else:
            if user_input==3:
                print("\nUSER " + str(count_user) + " COMPUTER " + str(count_computer))
                break
                
            print("USER HITS: "+str(dict_rps[user_input]))
            print("COMPUTER HITS: "+str(dict_rps[com_input]))

            if user_input == com_input:
                print("DRAW!")
            else:

                list_compare.append(user_input)
                list_compare.append(com_input)

                if list_compare in list_win:
                    print("USER WINS")
                    count_user+=1
                    print("\nUSER " + str(count_user) + " COMPUTER " + str(count_computer))

                else:
                    print("COMPUTER WINS")
                    count_computer+=1
                    print("\nUSER " + str(count_user) + " COMPUTER " + str(count_computer))

                list_compare = []
