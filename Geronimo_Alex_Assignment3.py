'''
Assignment 3
By: Alex Geronimo
Last Modified: 7/3/17
'''

class Pet:

    #Create two variables kind and color; assign values
    color = "black"
    kind = "pet...(vague)"

    def __init__(self, name): #In the constructor, initialize the pets name
        self.name = name

    def __str__(self):
        return "{0} is a {1}".format(self.name, self.kind) #Print the name and description of dog

    def do_tricks(self):

        print("{0} is doing tricks!".format(self.name)) #Print the name of the pet and that it is doing tricks
        self.speak() #Call the speak method
        self.jump()#Call the jump method

    def speak(self):
        pass

    def jump(self):
        pass


class Jumper(): #This is a mixin class for jump

    def jump(self):
        print("{0} is jumping!".format(self.name)) #Create jump method that prints that a Pet is jumping and the pets name


class Dog (Jumper, Pet):  #You will need to inherit for this to work

    kind = "canine" #Change kind to canine

    def __str__(self):
        return "{0} is a {1}".format(self.name, self.kind) #Print the name and description of dog

    def __call__(self, action):
        self.action = action

    #Rollover action prints the name of the dog and that it is rolling over
        if action == 'rollover':
            return '{0} is rolling over!'.format(self.name)

    #Owner action returns the name of the owner
        elif action == "owner" or "Owner":
            owner = "Alex"
            return owner

        else:
            print("Please use action 'rollover' or 'owner'. ")

class BigDog (Dog):  #You will need to inherit for this to work

    color = "tan" # Change the color to tan

    def __str__(self):
        return "{0} is a {1} big dog!".format(self.name, self.color) #Print the name and description of BigDog

    def speak(self):
        # Print dogs name and what it says
        print("I guess {0} is a special talking dog...\n{0} says: I am a talking dog, get over it!".format(self.name))


class SmallDog (Dog):  #You will need to inherit for this to work

    color = "brindle" # Change the color to brindle

    def __str__(self):
        return "{0} is a {1} small dog!".format(self.name, self.color) #Print the name and description of SmallDog

    def speak(self):

    # Print dogs name and what it says
        print("I guess {0} is a special talking dog.\n{0} says: whhooofff... but I can also talk ...whhoooff".format(self.name))


class Cat (Jumper, Pet):  #You will need to inherit for this to work

    kind = "feline" #Change the kind to feline

    def __str__(self):
        return "{0} is a {1}".format(self.name, self.kind) #Print the name and description of cat


    def speak(self):

    # Print cats name and what it says
       print("I guess {0} is a special talking cat.\n{0} says: meeoow...shut up ...meeoow".format(self.name))


    def climb(self):

    #Prints the name of the cat and that it is climbing
        print("{0} is climbing! ".format(self.name))


class HouseCat (Cat):  #You will need to inherit for this to work

    color = "white" #Change the color to white

    def __str__(self):
    #Print the name and description of cat
        return "{0} is a {1} cat".format(self.name, self.color)


    def speak(self):

    # Print cats name and what it says
        print("I guess {0} is a special talking house cat.\n{0} says: meeoow...get the @#$% away from me ...meeoow".format(self.name))


# END CLASSES ###########################################

#EXERCISE YOUR CODE

#    1. Instantiate each class(except jumper)

pet = Pet('Fluffy')
dog = Dog('Ralph')
bigdog = BigDog('Dawson')
smalldog = SmallDog('Pinot')
cat = Cat('Valentino')
housecat = HouseCat('Julie')

#    2. Create a list of the instantiated objects

pet_list = [pet,dog,bigdog,smalldog,cat,housecat]

#    3. Loop through the objects

for object in pet_list:

#    4. Print __str__
     print(object.__str__())

#    5. print the kind of pet
     print("Kind: " + object.kind)

#    6. Print the Color of the pet
     print("Color: " + object.color)

#    7. Have the pet do tricks
     object.do_tricks()

#    8. if applicable, print rollover action and the owners name
     if isinstance (object,Dog):
         print(object.__call__('rollover'))
         print("Owner: " + object.__call__('owner'))

#    9. If applicable, have the pet climb
     if isinstance (object, Cat):
         object.climb()

#       10. To separate each pet print underscores
     print("___________________")

print("Pets are cool!")
