# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Nadya"
my_age = 23
my_bio = " dkks "
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)

def options():
    while True:
        print("------------------------")
        print("Would you like to:")
        print("1) Creat a new club .\n or:")
        print("2) Browse and join_clubs .\n or:")
        print("3) View existing clubs .\n or:")
        print("4) Display members of a club .\n or:")
        print("-1) Close application .")
        choose = input()
        if choose == "1":
            create_club()
        elif choose == "2":
            join_clubs()
        elif choose == "3":
            view_clubs()
        elif choose == "4":
            view_club_members()
        elif choose =="-1":
            break
        else :
            print(" Wrong number try agein")    
        

    

def create_club():
    # your code goes here!
    club_name = input("Pick a name for your awesome new club :")
    club_des = input("What id your club about?")
    new_club = Club(club_name,club_des)
    print("Enter the numbers of the people you would like to recruit to your new club (-1 to stop)")
    for index , member in enumerate (population) :
        print ("[%d] %s" %( index+1 , member.name ))
    club_member = int(input())
    new_club.recruit_member(myself)
    new_club.assign_president(myself)
    stop = True
    while stop :
        if len(population) >= club_member and club_member > 0:
            new_club.recruit_member(population[club_member -1])
            club_member = int(input())  
        else :
            stop = False     
    clubs.append(new_club)
   
    print ("Here\'s your club %s\n%s\n"%(new_club.name,new_club.description))
    new_club.print_member_list()
            



def view_clubs():
    for club_d in clubs :
        p = len(club_d.members)
        print ("\t\t\t NAME: %s\n\t\t\tDESCRIPTION: %s\n\t\t\t MEMBERS: %s \n" %(club_d.name,club_d.description, str(p)))
    

def view_club_members():
    view_clubs()
    print("Enter the name of the club whose members you'd like to see : ")
    club_cho = input()
    for club_f in clubs :
        if club_f.name.lower() == club_cho.lower():
            club_f.print_member_list()
    
def join_clubs():
    view_clubs()
    club_n = input("Enter the name of the club you'd like to join : ")
    for club_f in clubs :
        if club_f.name.lower() == club_n.lower():
            club_f.recruit_member(myself)
            print("%s just joined %s" %(myself.name,club_n))
            break

def application():
    introduction()
    options()
    
