from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Challenge 2 coming right up!'

if __name__ == "__main__":
    app.run()
