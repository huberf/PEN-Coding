def main():
	import turtle
	import random

	random.seed()

	speed = 6
	highspeed = 100000

	fred = turtle.Turtle()
	fred.shape('turtle')

	wn = turtle.Screen()

	step = 10
	steps = step

	enemies = None

	fred.speed(speed)
	fred.up()
	fred.goto(100, 0)
	fred.dot()
	fred.goto(-100, 0)
	enemies = [[None, 0, random.randrange(-90/step, 90/step) * step, False],
			[None, 20, random.randrange(-90/step, 90/step) * step, True],
			[None, 30, random.randrange(-90/step, 90/step) * step, False],
			[None, 40, random.randrange(-90/step, 90/step) * step, True],
			[None, 50, random.randrange(-90/step, 90/step) * step, False],
			[None, 60, random.randrange(-90/step, 90/step) * step, True]]

	for i in enemies:
		i[0] = turtle.Turtle()
		i[0].up()
		i[0].goto(i[1], i[2])

	def enemy():
		for i in enemies:
			if i[3] == False:
				i[2]-=step
				if i[2] <= -100:
					i[3] = True
			else:
				i[2]+=step
				if i[2] >= 100:
					i[3] = False
			i[0].goto(i[1], i[2])
		if collisions(fred.xcor(), fred.ycor()):
			print "You died!"
			wn.bye()
			main()

	def collisions(x, y):
		collided = False
		for i in enemies:
			if x == i[1] and y == i[2]:
				collided = True
		if x == 100 and y == 0:
			while True:
				print "Success!"
				wn.bye()
				main()

		return collided

	def up():
		fred.speed(highspeed)
		fred.setheading(90)
		fred.speed(speed)
		fred.forward(steps)
		fred.speed(highspeed)
		fred.setheading(0)
		fred.speed(speed)
		if collisions(fred.xcor(), fred.ycor()):
			print "You died!"
			wn.bye()
			main()

	def down():
		fred.speed(highspeed)
		fred.setheading(270)
		fred.speed(speed)
		fred.forward(steps)
		fred.speed(highspeed)
		fred.setheading(0)
		fred.speed(speed)
		if collisions(fred.xcor(), fred.ycor()):
			print "You died!"
			wn.bye()
			main()

	def left():
		fred.backward(steps)
		if collisions(fred.xcor(), fred.ycor()):
			print "You died!"
			wn.bye()
			main()

	def right():
		fred.forward(steps)
		if collisions(fred.xcor(), fred.ycor()):
			print "You died!"
			wn.bye()
			main()

	# These lines "wire up" keypresses to the handlers we've defined.
	wn.onkey(up, "Up")
	wn.onkey(down, "Down")
	wn.onkey(left, "Left")
	wn.onkey(right, "Right")
	wn.onkey(quit, "q")

	# Now we need to tell the window to start listening for events,
	# If any of the keys that we're monitoring is pressed, its
	# handler will be called.
	wn.listen()

	from time import sleep
	while True:
		enemy()
		sleep(0.5)


#Begin game
main()