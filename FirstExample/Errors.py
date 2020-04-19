# Index error            : Index does not exist
# Key Error              : Key does not exist or used incorrectly
# Name Error             : Variable is not defined
# Attribute Error        : Attribute not available for a specific object
# Not Implemented Error  : Custom string that states that a method not implemented
# Runtime Error          : Error ran from program (general)
# Syntax Error           : Illegal syntax
# Indentation Error      : Ensure that indentation used in the correct place
# Tab Error              : Different tab space
# Type Error             : '+' adding two types such as int and str
# Value Error            : Invalid literal: int() usually cause error
# Import Error           : Reference error: circular import
# Deprecation Warning    : Method or action no longer most up to date


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}'


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f'Tried to add `{car.__class__.__name__}` to the garage but only can add `Car` objects.')
        self.cars.append(car)


ford = Garage()
this_car = Car('Chevy', 'S10')
ford.add_car(this_car)
print(len(ford))
try:
    ford.add_car('Fiesta')
except TypeError:
    print("car was not a Car")


class CustomError(ValueError):
    """Exception raised when a specific error code is needed."""

    def __init__(self, message, code):
        super().__init__(f'Error Code {code}: {message}')
        self.code = code


err = CustomError("DOC Message", 200)
print(err.__doc__)
# raise CustomError("Wow that went wrong", 500)
