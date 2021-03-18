import datetime
from dataclasses import dataclass

@dataclass
class Pet:
    breed: str
    name: str
    color: str
    gender: bytes
    owner: str
    address: str
    birthdate: datetime
    species: str





    def getAge(self):
        d1 = datetime.date.today()
        d2 = self.birthdate

        # Data Validation
        assert type(self.birthdate) == datetime.date
        # Data Validation
        assert d2<d1
        return int(abs((d2 - d1).days/365.2425))



    def __str__(self):
        return f'{self.name} is {self.getAge()} years old and belongs to {self.species} species and of color {self.color}'

@dataclass
class Dog(Pet):
    species: str = 'canis familiaris'


class Puppy(Dog):
    # Polimorphism
    def getAge(self):
        d2 = self.birthdate
        return int(abs((d2 - datetime.date.today()).days/31))
    def __str__(self):
        return f'{self.name} is {self.getAge()}months old and belongs to {self.species} and of color {self.color}'
    def play(self):
        return "(___()'`;\\n      /,    /`\\n      \\\\\"--\\\\"


x=Pet('labador','Tommy','Black','1','Aswini','1234,village ln,95123',datetime.date(2019, 5, 17),'Dog')
print(f'{x.getAge()} years')
print(x)

y=Dog('labador','Tommy','Black','1','Aswini','1234,village ln,95123',datetime.date(2019, 5, 17),'Dog')
z=Puppy('labador','Tommy','Black','1','Aswini','1234,village ln,95123',datetime.date(2019, 5, 17),'Dog')
print(f'{z.getAge()} months')
print(z)
print(z.play())




