from flask import Flask, render_template
app = Flask(__name__)
app = Flask(__name__, template_folder='template',static_folder='static') 
@app.route('/')
def demo():
    return render_template('demo.html')

@app.route('/chance')
def chance():
    return render_template('chance.html')

@app.route('/noChance')
def noChance():
    return render_template('noChance.html')


if __name__ == "__main__":
    app.run()
