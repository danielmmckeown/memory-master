# Implements the Leitner system.

from datetime import datetime, timedelta

def get_review_date(box):
    intervals = {1: 1, 2: 3, 3: 7, 4: 14, 5: 30}
    return datetime.now() + timedelta(days=intervals[box])

def update_flashcard_review(card_id, remembered):
    conn = sqlite3.connect('flashcards.db')
    c = conn.cursor()
    
    # Fetch current box
    c.execute('SELECT box FROM flashcards WHERE id=?', (card_id,))
    box = c.fetchone()[0]

    # Update box and next review date
    if remembered:
        new_box = min(box + 1, 5)
    else:
        new_box = 1

    next_review_date = get_review_date(new_box).strftime('%Y-%m-%d')
    last_reviewed = datetime.now().strftime('%Y-%m-%d')

    c.execute('''UPDATE flashcards
                 SET box=?, next_review_date=?, last_reviewed=?
                 WHERE id=?''', (new_box, next_review_date, last_reviewed, card_id))
    
    conn.commit()
    conn.close()
