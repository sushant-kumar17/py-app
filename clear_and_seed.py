import json
from app import create_app
from extensions import db
from models.book import Book, Category, BookCategory, Chapter

app = create_app()

with app.app_context():
    # Clear existing data
    db.session.query(BookCategory).delete()
    db.session.query(Chapter).delete()
    db.session.query(Book).delete()
    db.session.query(Category).delete()
    db.session.commit()

    # Load data from JSON file
    with open('book-data.json') as f:
        data = json.load(f)
    
    # Seed new data
    for category_data in data['record']['categories']:
        category = Category(name=category_data['name'])
        db.session.add(category)
        db.session.commit()
        
        for book_data in category_data['books']:
            book = Book(
                title=book_data['book_name'],
                author=book_data['author'],
                description=book_data['description'],
                cover_image_url=book_data['cover_image'],
                summary=book_data['description'],
                reading_time=book_data['reading_time'],
                insights=len(book_data['chapters']),
                key_points=book_data['number_of_chapters']
            )
            db.session.add(book)
            db.session.commit()
            
            # Link book to category
            book_category = BookCategory(book_id=book.id, category_id=category.id)
            db.session.add(book_category)
            
            # Add chapters
            for chapter_data in book_data['chapters']:
                chapter = Chapter(
                    book_id=book.id,
                    title=chapter_data['chapter_title'],
                    text_summary=chapter_data['chapter_description'],
                    audio_summary_url=chapter_data['audio_file'],
                    order=chapter_data['chapter_title'].split(":")[0].split(" ")[1]
                )
                db.session.add(chapter)
            
            db.session.commit()

    print("Database seeded successfully!")
