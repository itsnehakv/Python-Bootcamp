import turtle as t
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT=10

class CarManager():
    def __init__(self):
        self.OUR_CARS = []
        self.car_speed=STARTING_MOVE_DISTANCE


    def creation(self):
        random_chance=random.randint(1,6)
        if random_chance==1:  #to generate cars in less frequency
            newcar=t.Turtle()
            newcar.penup()
            newcar.shape("square")
            newcar.shapesize(stretch_wid=1.2, stretch_len=2)
            random_y = random.randint(-250, 280)
            newcar.goto(x=400, y=random_y)
            newcar.color(random.choice(COLORS))
            self.OUR_CARS.append(newcar)

    def movement(self):
        for car in self.OUR_CARS:
            car.setheading(180)
            car.forward(self.car_speed)    #or -->car.backward()

    def increasing(self):
        self.car_speed+=MOVE_INCREMENT
