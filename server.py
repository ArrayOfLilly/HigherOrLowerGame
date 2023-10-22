from flask import Flask, url_for
from random import randint

app = Flask(__name__)
print(__name__)
num: int


@app.route("/")
def show_page():
	main_image = url_for('static', filename='img/main.gif')
	global num
	num = randint(0, 9)
	print(f'Number to guess is: {num}')
	return (f'<h1 style="text-align: center; font-family: American TypeWriter; padding: 20px">Guess a number between 0 '
			f'and 9</h1><div style="text-align: center;"><img src="{main_image}" style="width: 50%"/></div>')


@app.route("/<int:number>")
def guess(number):
	print(f'Guess is: {number}')
	if num == number:
		hit_image = url_for('static', filename='img/hit.png')
		return (f'<h1 style="text-align: center; font-family: American TypeWriter; padding: 20px">You found '
				f'me!</h1><div style="text-align: center"><img src="{hit_image}" style="width: 50%"/></div>')
	elif num > number:
		low_image = url_for('static', filename='img/low.png')
		return (f'<h1 style="text-align: center; font-family: American TypeWriter; padding: 20px">Too low!</h1><div '
				f'style="text-align: center"><img src="{low_image}" style="width: 50%"/></div>')
	else:
		high_image = url_for('static', filename='img/high.png')
		return (f'<h1 style="text-align: center; font-family: American TypeWriter; padding: 20px">Too high!</h1><div '
				f'style="text-align: center"><img src="{high_image}" style="width: 50%"/></div>')


if __name__ == "__main__":
	app.run(debug=True)

