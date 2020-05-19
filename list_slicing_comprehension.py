my_friends = ['Ram','Kumar','Suresh','Deepak','Aishu']
print(my_friends[2:4])
my_list = [0,1,2,3,4]
double_list = []

#traditional methods
for number in my_list:
    double_list.append(number * 2)
print(double_list)

# list comprehension
double_list = [number * 2 for number in my_list]
print(double_list)

my_friends_lower = [friend.lower() for friend in my_friends]
print(my_friends_lower)

friend_name = input("Enter your friend name: ")

if friend_name.lower() in my_friends_lower:
    
    print(f" Your {friend_name.title()} is in the my_friends")
    
    
    
          



