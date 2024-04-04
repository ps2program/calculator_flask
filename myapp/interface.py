from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
books = [
    {"id": 1, "title": "Python Programming", "author": "John Doe"},
    {"id": 2, "title": "Data Science Essentials", "author": "Jane Smith"},
    {"id": 3, "title": "Machine Learning Basics", "author": "Alice Johnson"}
]

# Endpoint to get all books
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Endpoint to get a specific book by ID
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
