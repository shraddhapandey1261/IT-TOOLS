# Class composition allows explicit relations between objects.
# In this example,people live in cities that belong to counties.
# Composition allows people to acces the number of all people living in their country:
class Country(object):
     
     # Initializing the function
     def __init__(self):
          self.cities=[]

     def addCity(self,city):
          self.cities.append(city)

# Class created 
class City(object):
     def __init__(self,numPeople):
          self.people=[]
          self.numPeople=numPeople

     def addPerson(self,person):
          self.people.append(person)

     def join_country(self,country):
          self.country=country
          country.addCity(self)

          for i in range(self.numPeople):
               Person(i).join_city(self)

# Class created                
class Person(object):
     def __init__(self,ID):
          self.ID=ID

     def join_city(self,city):
          self.city=city
          city.addPerson(self)

     def people_in_my_country(self):
          x=sum([len(c.people)for c in self.city.country.cities])
          return x

US=Country()  # Creating instance
NYC=City(10).join_country(US)
SF=City(5).join_country(US)

print(US.cities[0].people[0].people_in_my_country())
