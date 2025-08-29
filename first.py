from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title='Portfolio')

if __name__ == '__main__':
    app.run(debug=True)  # debug=True helps while coding
