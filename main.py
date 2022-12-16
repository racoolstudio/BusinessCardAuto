import random

from flask import Flask, render_template
from datetime import date

app = Flask(__name__)


#  to edit a website like wordpress
# document.body.contentEditable = true
@app.route('/')
def businessCard():
    currentYear = date.today().year
    return render_template('card.html', year=currentYear)


if __name__ == '__main__':
    app.run(debug=True)
