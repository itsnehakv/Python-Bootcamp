import turtle as t
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT=5

class CarManager():
    def __init__(self):
        self.OUR_CARS_right= []
        self.OUR_CARS_left = []
        self.car_speed=STARTING_MOVE_DISTANCE



    def creation_right(self):
        random_chance=random.randint(1,10)
        if random_chance==1:  #to generate cars in less frequency
            newcar=t.Turtle()
            newcar.penup()
            newcar.shape("square")
            newcar.shapesize(stretch_wid=1.2, stretch_len=2)
            random_y = random.randint(-250, 0)
            newcar.goto(x=400, y=random_y)
            newcar.color(random.choice(COLORS))
            self.OUR_CARS_right.append(newcar)

    def creation_left(self):
        random_chance = random.randint(1, 10)
        if random_chance == 1:  # to generate cars in less frequency
            newcar = t.Turtle()
            newcar.penup()
            newcar.shape("square")
            newcar.shapesize(stretch_wid=1.2, stretch_len=2)
            random_y = random.randint(0, 250)
            newcar.goto(x=-400, y=random_y)
            newcar.color(random.choice(COLORS))
            self.OUR_CARS_left.append(newcar)

    def movement_right(self):
        for car in self.OUR_CARS_right:
            car.setheading(180)
            car.forward(self.car_speed)    #or -->car.backward()

    def movement_left(self):
        for car in self.OUR_CARS_left:
            car.setheading(0)
            car.forward(self.car_speed)

    def increasing(self):
        self.car_speed+=MOVE_INCREMENT
