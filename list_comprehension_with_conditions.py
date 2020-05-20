numbers = [1,2,3,4,5,6]
odds = [age for age in numbers if age % 2 == 1]
print(odds)

friends = ['Ram','Kumar','Dinesh','Suresh','Deepak']
guests = ['Aishu','Vikram','Surya','dinesh','kumar']

guests_lower = [guest.lower() for guest in guests]
print(guests_lower)

present_friends = [name.title() for name in friends if name.lower() in guests_lower]
print(present_friends)

# traditional methods using set intersection

friends_lower1 = set([name.lower() for name in friends])
guests_lower1 = set([guests.lower() for guests in guests])

print(friends_lower1.intersection(guests_lower1))
