def greet():
    print("Hello World")

hello = greet
hello()

operations = {
    "average": lambda seq: sum(seq) / len(seq),
    "total": sum,
    "top": max
}

students = [
    {"name":'Aishu',"grades":[80,90,70,90,100]},
    {"name":'Mohan',"grades":[80,90,70,90,100]},
    {"name":'vikram',"grades":[80,90,70,90,100]},
]

for student in students:
    name = student["name"]
    grades = student["grades"]
    print(f" student: {name}")
    operation = input("Enter opertion like average or total or top: ")
    operation_function = operations[operation]
    print(operation_function(grades))
        





    
    
          
    
    
    
