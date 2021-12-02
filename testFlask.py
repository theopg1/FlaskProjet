from flask import Flask, request, jsonify, json

app = Flask(__name__)
app.config["DEBUG"] = True

books = json.load(open("books.json"))

@app.route('/')
def index():
 return "<h1>hello my app</h1>"

@app.route('/about')
def about():
    return 'The about page'

@app.route('/api/books',  methods=['GET'])
def list1():
    return jsonify(books)

@app.route('/api/V1/book/isbn/<isbn>',  methods=['GET'])
def list2(isbn):
    for book in books:
        if book['isbn'] == isbn:
            return jsonify(book), 200
    return "Livre introuvable" 

@app.route('/api/V2/book/isbn',  methods=['GET'])
def list3():
    if 'isbn' in request.args:
        isbn = str(request.args['isbn'])
    else:
        return "Veuillez renseigner un isbn !", 404
    
    results = []

    for book in books:
        if book['isbn'] == isbn:
            results.append(book)

    return jsonify(results) 

@app.route('/api/V1/book/title/<title>',  methods=['GET'])
def list4(title):
    for book in books:
        if book['title'] == title:
            return jsonify(book), 200
    return "Livre introuvable" 

@app.route('/api/V2/book/title',  methods=['GET'])
def list5():
    if 'title' in request.args:
        title = str(request.args['title'])
    else:
        return "Veuillez renseigner un title !", 404
    
    results = []

    for book in books:
        if book['title'] == title:
            return jsonify(results)

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)