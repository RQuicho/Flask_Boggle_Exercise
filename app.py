from boggle import Boggle
from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-secret-key'

boggle_game = Boggle()

@app.route('/')
def home_page():
	"""Creates a new board."""
	board = boggle_game.make_board()

	return render_template('make_board.html', board=board)





