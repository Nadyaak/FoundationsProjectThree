# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        # your code goes here!
        self.name = name
        self.bio = bio
        self.age = age


class Club():
    def __init__(self, name, description):
        # your code goes here!
        self.name = name
        self.description = description
        self.president = None
        self.members = []


    def assign_president(self, person):
        # your code goes here!
        self.president = person

    def recruit_member(self, person):
        # your code goes here!
        self.members.append(person)


    def print_member_list(self):
        # your code goes here!
        print ("Members: ")
        total = 0.0
        averg = 0.0
        for member in self.members:
            taxt = "- " + member.name + " (" + str(member.age) + " yeears old " 
            taxt += ", president) " if member == self.president else ") "
            taxt +=  member.bio
            print(taxt)
            total = total+ member.age    
        lent = float(len(self.members)) 
        averg = total /(lent)
        print ("Average age in this club: "+ str(averg) +" yr") 
        
        """
            total += member.age 
        lent = len(self.members)+1 """ 






