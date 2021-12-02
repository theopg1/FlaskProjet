from flask import Flask

app = Flask(__name__)

database = { 'PierreDurand':
            [
                {
                  "from": "Paris",
                  "to": "Berlin",
                  "date": "25/02/2019 10h39"
                }
            ]
           }

@app.route('/list/<user>', methods=['GET'])
def list(user):
    if user in database:
        return str(database[user]), 200
    else:
        return "L'utilisateur est introuvable !", 404


if __name__ == '__main__':
    app.run(debug=True)