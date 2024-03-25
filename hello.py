frends = [('rahul',19),
          ('hari',21),
          ('raman',15),
          ('ram',13),
          ('sita',19)]

age = lambda data:data[1] >=18

drinking_buddies = list(filter(age, frends))

for i in drinking_buddies:
    print(i)