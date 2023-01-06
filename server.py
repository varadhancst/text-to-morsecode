from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class TaskForm(FlaskForm):
    text_string = StringField(u'Original string:', validators=[DataRequired()])
    submit = SubmitField(u'Submit')


MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TaskForm()
    string = None
    converted_text = None

    if form.validate_on_submit() and request.method == "POST":
        string = form.text_string.data
        word = string
        result = []
        for i in word.upper():
            if i == " ":
                result.append(" ")
            else:
                result.append(MORSE_CODE_DICT[i])
        converted_text = ''.join(map(str, result))

    return render_template('index.html', string=string, converted_text=converted_text, form=form)


if __name__ == "__main__":
#     app.run(host='0.0.0.0:$PORT', port=5000)
    app.run(host='0.0.0.0', port=5000)
