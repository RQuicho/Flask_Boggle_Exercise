from boggle import Boggle
from flask import Flask, render_template, request, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-secret-key'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/')
def home_page():
	"""Creates a new board."""
	board = boggle_game.make_board()
	session['board'] = board

	return render_template('make_board.html', board=board)

@app.route('/', methods=["POST"])
def check_word():
	"""Checks if the submitted word is in the dictionary and on board."""
	board = session["board"]
	word = request.form["guess"]
	response = boggle_game.check_valid_word(board, word)

	return response





