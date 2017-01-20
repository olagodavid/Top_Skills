def progress():
    #The total number of skills in the curriculum
    general_list = [1,2,4,3]
    #The total number of skills studied so far
    studied_list = [2,4]
    a = general_list
    b = studied_list
    b =  int((len(b)/len(a))*100)
    return ("your progress is "+str(b)+"%")
#The function call
print(progress())
