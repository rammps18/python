cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "suzuki", "model": "Maruti", "mileage": 21000, "fuel_consumed": 430},
    {"make": "Tata", "model": "indica", "mileage": 19000, "fuel_consumed": 410},
    {"make": "Hundai", "model": "verna", "mileage": 17000, "fuel_consumed": 390}

    ]

cars_dict = {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460}

def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    name = f"{car['make']} {car['model']}"
    print(f"{name} does {mpg} miles per gallon")

calculate_mpg(cars_dict)

for car in cars:
    calculate_mpg(car)
    
    
