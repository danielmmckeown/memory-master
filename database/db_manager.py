# Handles database connections, schema initialization, and CRUD operations.

import sqlite3
from datetime import datetime

DATABASE_NAME = 'flashcards.db'

def init_db():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS flashcards
                 (id INTEGER PRIMARY KEY, front_text TEXT, back_text TEXT, image_path TEXT, audio_path TEXT, tags TEXT, next_review_date TEXT, box INTEGER, last_reviewed TEXT)''')
    conn.commit()
    conn.close()

def add_flashcard(front_text, back_text, image_path, audio_path, tags, next_review_date, box, last_reviewed):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute('''INSERT INTO flashcards (front_text, back_text, image_path, audio_path, tags, next_review_date, box, last_reviewed)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (front_text, back_text, image_path, audio_path, tags, next_review_date, box, last_reviewed))
    conn.commit()
    conn.close()

# Add more CRUD functions as needed
