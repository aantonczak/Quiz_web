from flask import Flask
from flask import render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config.update(dict(SECRET_KEY = "haslo"))



PYTANIA = [
    {
        'pytanie': u'Stolica Hiszpani, to:',  # pytanie
        'odpowiedzi': [u'Madryt', u'Warszawa', u'Barcelona'],  # możliwe odpowiedzi
        'odpok': u'Madryt',  # poprawna odpowiedź
    },
    {
        'pytanie': u'Objętość sześcianu o boku 6 cm, wynosi:',
        'odpowiedzi': [u'36', u'216', u'18'],
        'odpok': u'216',
    },
    {
        'pytanie': u'Symbol pierwiastka Helu, to:',
        'odpowiedzi': [u'Fe', u'H', u'He'],
        'odpok': u'He',
    }
]



@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
        punktacja = 0
        odpowiedzi = request.form
        for k, i in odpowiedzi.items():
            if i == PYTANIA[int(k)]["odpok"]:
                punktacja+=1

        flash(u"Uzyskałeś {0} na 5 możliwych punktów.".format(punktacja))

        return redirect(url_for("index"))

    return render_template('index.html', pytania = PYTANIA)


if __name__ == '__main__':
    app.run(debug=True)