import datetime

class Pet:
    def __init__(self,species,breed,name,color,gender,owner,address,birthdate):
         self.species=species
         self.breed=breed
         self.name=name
         self.color=color
         self.gender=gender
         self.owner=owner
         self.address=address
         self.birthdate=birthdate


# class Pet:
#     def __init__(self,name):
#         self.name=name
#     def pet_species(self,species):
#         self.species=species
#     def pet_breed(self,breed):
#         self.breed=breed
#     def pet_color(self,color):
#         self.color=color
#     def pet_gender(self,gender):
#         self.gender=gender
#     def pet_owner(self,owner):
#         self.owner=owner
#     def pet_address(self,address):
#         self.address=address
#     def pet_birthdate(self,birthdate):
#         self.birthdate=datetime.datetime(birthdate)



    def getAge(self):
        d1 = datetime.date.today()
        d2 = self.birthdate
        return int(abs((d2 - d1).days/365.2425))

    def __str__(self):
        return f'{self.name} is {self.getAge()} years old and belongs to {self.species} species and of color {self.color}'


class Dog(Pet):

    def __init__(self,breed,name,color,gender):
        self.species = 'canis familiaris'
        self.gender = gender
        self.color = color
        self.breed = breed
        self.name = name

class Puppy(Dog):
    def __init__(self,species,breed,name,color,gender,owner,address,birthdate):
        Pet.__init__(self,species,breed,name,color,gender,owner,address,birthdate)
    def getAge(self):
        d2 = self.birthdate
        return int(abs((d2 - datetime.date.today()).days/31))
    def __str__(self):
        return f'{self.name} is {self.getAge()}months old and belongs to {self.species} and of color {self.color}'
    def play(self):
        return "(___()'`;\\n      /,    /`\\n      \\\\\"--\\\\"


x=Pet('Dog','labador','Tommy','Black','1','Aswini','1234,village ln,95123',datetime.date(2019, 5, 17))
print(f'{x.getAge()} years')
print(x)

y=Dog('labador','Tommy','Black','1')
z=Puppy('Dog','labador','Tommy','Black','1','Aswini','1234,village ln,95123',datetime.date(2019, 5, 17))
print(f'{z.getAge()} months')
print(z)
print(z.play())




