import sys
notstudied_list = []
studied_list = []

def add_skill():
    
    print ("Enter Skill Starting with 'studied' for skills you have studied or 'notstudied' for skills not studied ")
    print ("Example: studied HTML")
    skill = input ("add skill: ")
    #split string into list 
    temp_list = skill.split()
    if temp_list[0] == "studied" and temp_list[1] not in studied_list:
        
        studied_list.append (temp_list[1])
        print ("Data Saved to Studied List")
    elif temp_list[0] == "studied" and temp_list[1] in studied_list:
        print ("Skill already in database")
    elif temp_list[0] == "notstudied" and temp_list[1] not in notstudied_list:
        notstudied_list.append(temp_list[1])
        print ("Data Saved to Not Studied List")
    elif temp_list[0] == "notstudied" and temp_list[1] in notstudied_list:
        notstudied_list.append(temp_list[1])
        print ("Skill already in Not studied list")
    else:
        print ("Invalid input")
        return skill
    all = studied_list.extend(notstudied_list)
    return all

def show_notstudied_list():
	count = 1
	print("To Study")
	for d in notstudied_list:
		print("{0} - {1}".format(count, d))
		count += 1

def show_studied_list():
	count = 1
	print("Studied")
	for d in studied_list:
		print("{0} - {1}".format(count, d))
		count += 1

def progress():
    #The total number of skills in the curriculum
    general_list = studied_list + notstudied_list
    #The total number of skills studied so far
    a = general_list
    b = studied_list
    b =  int((len(b)/len(a))*100)
    print("your progress is "+str(b)+"%")


def shel():
	while True:
		print("Skills Map App")
		print("1. Add skill")
		print("2. Show studied skills")
		print("3. Show not studied skills")
		print("4. View learning progress")
		print("0. Quit")
		x = input("Please select an option: ")
		x = int(x)
		if x == 0:
			#exit
			break
			pass
		elif x == 1:
			add_skill()
			pass
		elif x == 2:
			#show studied
			show_studied_list()
			pass
		elif x == 3:
			#show not studied
			show_notstudied_list()
			pass
		elif x == 4:
			#view progress
			#The function call
			progress()
		else:
			print("Invalid input")

if __name__ == "__main__":
	shel()
