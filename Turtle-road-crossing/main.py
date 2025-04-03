import turtle as t
import time
import car_manager as cm
import scoreboard as sb
import player as p

screen = t.Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
player=p.Player()
screen.listen()
screen.onkeypress(fun=player.move_up, key="Up")
score=sb.Scoreboard()
car = cm.CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.creation_right()
    car.creation_left()
    car.movement_left()
    car.movement_right()

    for cars in car.OUR_CARS_right:
        if player.distance(cars)<23:
            score.when_game_over()
            game_is_on=False

    for cars in car.OUR_CARS_left:
        if player.distance(cars)<23:
            score.when_game_over()
            game_is_on=False

    if player.ycor()>290:
        score.level_up()
        player.at_finish_line()
        car.increasing()


screen.exitonclick()
