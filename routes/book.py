from flask import Blueprint, jsonify
from models.book import Book, Chapter, Category, BookCategory
from extensions import db

book_bp = Blueprint('book', __name__)

@book_bp.route('/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    chapters = Chapter.query.filter_by(book_id=book.id).order_by(Chapter.order).all()
    categories = db.session.query(Category).join(BookCategory).filter(BookCategory.book_id == book.id).all()

    book_details = book.to_dict()
    book_details['chapters'] = [chapter.to_dict() for chapter in chapters]
    book_details['categories'] = [category.to_dict() for category in categories]
    book_details['author_info'] = {
        "name": book.author,
        "bio": f"{book.author} struggled with unproductivity, slow career growth, and job dissatisfaction until an epiphany led him to study productivity."
    }
    book_details['actions'] = {
        "read": "http://example.com/read",
        "listen": "http://example.com/listen"
    }

    return jsonify(book_details)
