import sys
notstudied_list = []
studied_list = []
def add_skill():
    
    print ("Enter Skill Starting with 'Studied' for skills you have studied or 'Unstudied' for skills not studied ")
    print ("Example: studied HTML")
    skill = input ("add skill: ")
    #split string into list 
    temp_list = skill.split()
    if temp_list[0] == "studied" and temp_list[1] not in studied_list:
        
        studied_list.append (temp_list[1])
        print ("Data Saved to Studied List")
    elif temp_list[0] == "studied" and temp_list[1] in studied_list:
        print ("Skill already in database")
    elif temp_list[0] == "unstudied" and temp_list[1] not in notstudied_list:
        notstudied_list.append(temp_list[1])
        print ("Data Saved to Not Studied List")
    elif temp_list[0] == "unstudied" and temp_list[1] in notstudied_list:
        notstudied_list.append(temp_list[1])
        print ("Skill already in Not studied list")
    else:
        print ("Invalid input")
        return skill
    
    all = studied_list.extend(notstudied_list)
    return all
if __name__ == '__main__':
    add_skill()
