from flask import Blueprint, jsonify
from models.book import Book, Category, BookCategory
from extensions import db

homepage_bp = Blueprint('homepage', __name__)

@homepage_bp.route('/homepage', methods=['GET'])
def get_homepage():
    categories = Category.query.all()
    homepage_data = []

    for category in categories:
        books_in_category = db.session.query(Book).join(BookCategory).filter(BookCategory.category_id == category.id).all()
        category_data = {
            "id": category.id,
            "name": category.name,
            "books": [book.to_dict() for book in books_in_category]
        }
        homepage_data.append(category_data)

    return jsonify({"categories": homepage_data})
