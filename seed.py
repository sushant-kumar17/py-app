from app import create_app
from extensions import db
from models.user import User
from models.book import Book, Category, BookCategory, Chapter
from datetime import datetime

app = create_app()

with app.app_context():
    # Create some sample books
    book1 = Book(title="Same as Ever", author="Morgan Housel", description="A guide to what never changes.", cover_image_url="http://example.com/same_as_ever.jpg", summary="Overcome procrastination, improve productivity, and achieve more meaningful things.", reading_time="11 min", insights=6, key_points=7)
    book2 = Book(title="The Automatic Millionaire", author="David Bach", description="A powerful one-step plan to live and finish rich.", cover_image_url="http://example.com/automatic_millionaire.jpg", summary="Achieve financial freedom.", reading_time="15 min", insights=5, key_points=8)
    book3 = Book(title="Do It Today", author="Darius Foroux", description="Overcome procrastination, improve productivity, and achieve more meaningful things.", cover_image_url="http://example.com/do_it_today.jpg", summary="Find out why procrastination is a problem today and how to fight it.", reading_time="11 min", insights=6, key_points=7)
    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book3)
    db.session.commit()

    # Link books to categories
    db.session.add(BookCategory(book_id=book1.id, category_id=category1.id))
    db.session.add(BookCategory(book_id=book2.id, category_id=category1.id))
    db.session.add(BookCategory(book_id=book3.id, category_id=category2.id))
    db.session.commit()

    # Create sample chapters for "Do It Today"
    chapter1 = Chapter(book_id=book3.id, title="Say goodbye to procrastination", text_summary="Summary of chapter 1", audio_summary_url="http://example.com/do_it_today_chapter1.mp3", order=1)
    chapter2 = Chapter(book_id=book3.id, title="Own your life", text_summary="Summary of chapter 2", audio_summary_url="http://example.com/do_it_today_chapter2.mp3", order=2)
    chapter3 = Chapter(book_id=book3.id, title="Fight procrastination with productivity streaks", text_summary="Summary of chapter 3", audio_summary_url="http://example.com/do_it_today_chapter3.mp3", order=3)
    db.session.add(chapter1)
    db.session.add(chapter2)
    db.session.add(chapter3)
    db.session.commit()

    print("Database seeded successfully!")
