from flask import Flask

app = Flask(__name__)

@app.route('/')
def home ():
    raise Exception("This app is broken. Please fix it before running the tests.")

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=5000)
