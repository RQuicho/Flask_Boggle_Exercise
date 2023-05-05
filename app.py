from boggle import Boggle
from flask import Flask, render_template, request, session, jsonify
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-secret-key'
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/')
def home_page():
	"""Creates a new board."""
	board = boggle_game.make_board()
	session['board'] = board

	return render_template('make_board.html', board=board)

@app.route('/check-word', methods=['POST'])
def check_word():
	"""Checks if the submitted word is in the dictionary and on board."""
	board = session['board']
	word = request.form['guess']
	response = boggle_game.check_valid_word(board, word)

	return response

	# guessed_words = session.get('guessed_words', set())
	# score = session.get('score', 0)
	
	# if response == 'ok' and word not in guessed_words:
	# 	guessed_words.add(word)
	# 	session['guessed_words'] = guessed_words

	# 	score += len(word)
	# 	session['score'] = score

	# guessed_words_list = list(guessed_words)

	# return jsonify(result=response, guessed_words=guessed_words_list, score=score)
	# return jsonify(result=response, guessed_words=list(guessed_words), score=score)
	# return render_template('make_board.html', board=board, score=score, guessed_words=guessed_words)


# @app.route('/score', methods=['POST'])
# def show_score():
# 	"""Shows current score."""











