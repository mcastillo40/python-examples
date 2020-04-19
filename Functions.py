def MPG(car):
    return car["mileage"] / car["fuel_consumed"]


Name = lambda car: f"{car['make']} {car['model']}"


Divide = lambda x, y: x/y


operation_methods = {
    "name": Name,
    "mpg": MPG,
    "divide": Divide
}


def Calculate(new_car):
    mpg = operation_methods['mpg']
    name = operation_methods['name']
    print(f"{name(new_car)} does {mpg(new_car)}.")

def Main():
    cars = [
        {"make": "Chevy1", "model": "Colorado", "mileage": 23000, "fuel_consumed": 460},
        {"make": "Chevy2", "model": "Colorado", "mileage": 23000, "fuel_consumed": 460},
        {"make": "Chevy3", "model": "Colorado", "mileage": 23000, "fuel_consumed": 460},
    ]

    for car in cars:
        Calculate(car)

    print(Divide(10,2))

Main()