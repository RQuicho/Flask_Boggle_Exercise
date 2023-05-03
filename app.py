from boggle import Boggle
from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-secret-key'

boggle_game = Boggle()

@app.route('/')
def home_page():
	"""Creates a new board."""
	board = boggle_game.make_board()
	session['board'] = board

	return render_template('make_board.html', board=board)

@app.route('/', methods=["POST"])
def check_word_in_dict():
	"""Checks if the submitted word is in the dictionary provided."""
	




