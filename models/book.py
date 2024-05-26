from datetime import datetime
from extensions import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    cover_image_url = db.Column(db.String(255))
    summary = db.Column(db.Text)
    reading_time = db.Column(db.String(50))  # e.g., "11 min"
    insights = db.Column(db.Integer)
    key_points = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'cover_image_url': self.cover_image_url,
            'summary': self.summary,
            'reading_metrics': {
                'key_points': self.key_points,
                'reading_time': self.reading_time,
                'insights': self.insights
            },
            'description': self.description
        }

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

class BookCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

class Chapter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    text_summary = db.Column(db.Text, nullable=False)
    audio_summary_url = db.Column(db.String(255))
    order = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'text_summary': self.text_summary,
            'audio_summary_url': self.audio_summary_url,
            'order': self.order
        }
