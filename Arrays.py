#You have a list of your favourite marvel super heros

heroes = ['Spider man','Thor','Hulk','Iron man','Captain America' ]

#Length of the list

print(len(heroes))

#Add 'black panther' at the end of this list

heroes.append('Black panther')
print(heroes)

#You realize that you need to add 'black panther' after 'hulk',
#so remove it from the list first and then add it after 'hulk'

heroes.remove('Black panther')
heroes.insert(3,'Black panther')
print(heroes)

#Remove thor and hulk from list and replace them with doctor strang in one line of code

heroes[1:3]=['Doctor strange']
print(heroes)

#Sort the list in alphabetical order

heroes.sort()
print(heroes)
