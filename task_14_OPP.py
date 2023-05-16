## Homework Practice

# 1. Create add method to add two countries together. This method should create another country object 
#    with the name of the two countries combined and population of the two countries added together.

class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population
    
    def add(self, other_country):
        new_name = self.name + ' ' + other_country.name
        new_population = self.population + other_country.population
        new_country = Country(new_name, new_population)
        return new_country

bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)
bosnia_herzegovina = bosnia.add(herzegovina)

print(bosnia_herzegovina.name, bosnia_herzegovina.population)


# 2. Implement previous method with magic method

class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population
    
    def __add__(self, other_country):
        new_name = self.name + ' ' + other_country.name
        new_population = self.population + other_country.population
        new_country = Country(new_name, new_population)
        return new_country
    
bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina  

print(bosnia_herzegovina.name, bosnia_herzegovina.population)


#3.Create a Car class with the following attributes: brand, model, year, and speed. 
#  The Car class should have the following methods: accelerate and brake. 
#  The accelerate method should increase the speed by 5, and the brake method should decrease the speed by 5.

class Car:
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed
        
    def accelerate(self):
        self.speed += 5
    
    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0
            
my_car = Car('Toyota', 'Camry', 2022)

print(my_car.speed)

my_car.accelerate()
print(my_car.speed)

my_car.brake()
print(my_car.speed)


#4. Create a Robot class with the following attributes: orientation, position_x, position_y. 
# The Robot class should have the following methods: move, turn, and display_position. 
# The move method should take a number of steps and move the robot in the direction it is currently facing. 
# The turn method should take a direction (left or right) and turn the robot in that direction. 
# The display_position method should print the current position of the robot.

class Robot:
    def __init__(self, orientation, position_x=0, position_y=0):
        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y
        
    def move(self, steps):
        match self.orientation:
            case 'up':
                self.position_y += steps
            case 'down':
                self.position_y -= steps
            case 'left':
                self.position_x -= steps
            case 'right':
                self.position_x += steps
        
    def turn(self, direction):
        match direction:
            case 'left':
                match self.orientation:
                    case 'up':
                        self.orientation = 'left'
                    case 'down':
                        self.orientation = 'right'
                    case 'left':
                        self.orientation = 'down'
                    case 'right':
                        self.orientation = 'up'
            case 'right':
                match self.orientation:
                    case 'up':
                        self.orientation = 'right'
                    case 'down':
                        self.orientation = 'left'
                    case 'left':
                        self.orientation = 'up'
                    case 'right':
                        self.orientation = 'down'  
        
    def display_position(self):
        print(f'Position: ({self.position_x}, {self.position_y}), Orientation: {self.orientation}')
 
 
my_robot = Robot('up')

my_robot.display_position()  

my_robot.move(3)
my_robot.display_position()  

my_robot.turn('right')
my_robot.move(2)
my_robot.display_position()  

my_robot.turn('left')
my_robot.move(4)
my_robot.display_position()  
