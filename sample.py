print("    /")
print("   /|")
print("  / |")

####################################################################################################################
character_name = "Vipul" #String
character_age =" 23"
is_Male = True #Boolean
print("Hey this is "  +  character_name  +" Yae" + character_age)
print("I am 23 year old")

character_name = "Chetan" #changing it in the middle
print("I like my name "+ character_name)
print("I like being 23")

#We can store String, for number character_name= 50 without a ""
####################################################################################################################
#Strings
#we need "" for String
#\n for new line or \" for Quotation Mark or just \\
phrase = "Giraffe Acadaemy"
print(phrase.lower() + " Is cool")# without "" and  +"To concatinate" and .lower to change all to lower
print(phrase.islower())# provides Boolean  Value
print(phrase.upper().isupper()) #First Connverted it to upper then to Check wheather it was done.
print(phrase.__len__())
print(len(phrase))
print(phrase[2])
print(phrase.count("f"))
print(phrase.replace("Gir","AND"))#Case Sensitive

####################################################################################################################
#Working with numbers
from math import *
######From Math Function
print(floor(7.5))
print(ceil(3.4))
print(sqrt(36))
######End of Math Function
my_number = -5
print(6+7)
print(10 % 3) #Modulus
print(str(my_number)+"My fav Number")#This is now just String
#print(my_number+"Hello") Error
print(abs(my_number))
print(pow(3 , 2)) #Power 3 raised to 2
print(max(4,5)) #Also Min
print(round(6.7))
print(round(6.4))
##################################################################################################################
#Getting Input from USer

name = input("Enter your Name ")
age = input("Age is")
print("Helllo" + name + "You are" + age)
##################################################################################################################
#Calculator
num1 = input("Enter First Number")
num2 = input("Enter Second Number")

result = num1+num2 #Stings so concatination
add_result = int(num1) + int(num2) #No decimal is allowed
add_result2 = float(num1) + float(num2) #for decimal values
print(add_result2)
print(result)
print(add_result)
##################################################################################################################
#MadLibs

#print("Roses are Red")
#print("Voilets are Blue")
#print("I love me")
color = input("Enter a color")
plural_noun = input("Enter the noun")
celeb = input("Name a celeb")

print("Roses are " + color)
print(plural_noun + " are Blue")
print("I love " + celeb)
##################################################################################################################
#List
#To store a list of data
#List is []
#Strings, Int and Boolean all are allowed
friends = ["Vipul", "Bob", "Chetan"]
#           0       1       2
#           -3      -2      -1
friends[1] = "Haha" # tO CHANGE values
print(friends[0])
print(friends[2])
print(friends[-2])
print(friends[1:])# After one postion to the last element
print(friends[1:3])
################################################################################################################
#List Functions

lucky_numbers = [4,222.5,22,34,73]
friends = ["Chetan", "Bob", "Sinn", "LOlita"]
friends.extend(lucky_numbers)# Append a list
friends.append("Tiping")#Append element
friends.insert(1,"Yogesh",)
friends.remove("Chetan")
#friends.clear()
friends.pop()
#friends.index("Kevin")
print(friends.count("Bob"))#Counting
lucky_numbers.sort()
friends.index("Bob")
print(friends)
print(lucky_numbers)
friends2 = friends.copy()#Copying a list
print(friends2)
##############################################################################################################
#Tupples
#They are Immutable (Cannot be modified)
# () Are Tupples

coordinates = [(5, 7),(6,8)]

print(coordinates[1]) #Same as List
#################################################################################################################
#Function

def say_hi(name, age):
    print("Say hii"+ name + " You are " + str(age))

#print("Top")
say_hi(" Vipul", 23)#Function call to line 124
say_hi(" Chetan", 23)
#print("Low")

################################################################################################################
#Return Statement
#Anything Raised to the Power Anything
def cube(num,power):
    return pow(int(num),int(power))
    #Code after this doesnt work

print(cube(3,2))
print(cube(57, 34))
result = cube(22, 33)
print(result)
