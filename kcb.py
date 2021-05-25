question_list = [
    "How many continents are there?",              # pehla question
    "What is the capital of India?",            # doosra question
    "NG mei kaun se course padhaya jaata hai?"    # teesra question
]

options_list = [
    #pehle question ke liye options
    ["Four", "Nine", "Seven", "Eight"],
    #second question ke liye options
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    #third question ke liye options
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]

# har ek question ke liye, uski solution key (yeh index nahi hai)
solution_list = [3, 4, 1]
ans=["seven","Delhi","software Engineering"]
i=0
count=0
while i<len(question_list):
    m=question_list[i]
    print(m)
    j=0
    k=i
    while j<len(options_list[i]):
        d=options_list[k][j]
        print(j+1,d)
        j=j+1
    userinput1=input("do you usnig lifeline")
    if userinput1=="yes":
        print("50-50")
        if count==0:
            print(options_list[i][i])
            print(ans[i])
            userinput2=int(input("only now time using lifeline"))
            if userinput2==2:
                print("your answer is correct ")
                count=count+1
            else:
                print("your answer is wrong")
                break
        else:
            print("you can't use more lifeline")
            userinput3=int(input("choose the answer"))
            if userinput3==solution_list[i]:
                print("your ans is correct")
            else:
                print("your answer is wrong")
                break
    else:
        userinput4=int(input("choose the answer"))
        if userinput4==solution_list[i]:
            print("your answer is coreect")
        else:
            print("your answer is wrong")
    i=i+1


        






