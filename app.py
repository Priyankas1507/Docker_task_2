from flask import Flask

app = Flask(__name__)

@app.route('/')
def details():
    return '''
    <h1>Priyanka S</h1>
    <p>Profession: Student</p>
    <p>Location: CHennai</p>
    <p>Hobbies: Reading books</p>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

