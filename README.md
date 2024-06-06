# memory-master
An open-source spaced-repetition software application written in Python.

## Description
I wanted to create an open source spaced-repition software that combines the beauty of Mochi and the extensability an and accessibility of Anki.

Here's a detailed plan to develop your desktop-based spaced repetition software using Python and PyQt5, focusing on each step from design to implementation:

### 1. Define Your Requirements
**Features:**
- Flashcard creation and management
- Spaced repetition algorithm (Leitner system or SuperMemo)
- User interface and user experience (UI/UX)
- Data storage
- Optional features: image support, audio playback, tagging, progress tracking

### 2. Choose a Programming Language and Framework
**Programming Language:** Python
**Framework:** PyQt5 for GUI

### 3. Design the Database
Using SQLite

### 4. Implement the Spaced Repetition Algorithm
**Leitner System:**
- Cards are moved between different boxes based on user performance.
- Each box represents a different interval for review.

### 5. Create the User Interface
**Using PyQt5:**

1. **Install PyQt5:**

2. **Main Window:**
   - Create main window with navigation options for creating and reviewing flashcards.

3. **Flashcard Creation:**
   - Form to input front and back text, upload images/audio, and add tags.

4. **Flashcard Review:**
   - Display flashcard front.
   - Provide options to reveal the back and mark performance.
   - Update the next review date based on the algorithm.

### 6. Implement Data Storage and Synchronization
**Local Storage with SQLite:**
- Use SQLite for storing flashcards locally.
- Functions to add, edit, delete, and fetch flashcards.

### Putting It All Together
1. **Set Up Project:**
   - Create a project directory.
   - Set up a virtual environment and install required libraries (`PyQt5`, `sqlite3`).

2. **Database Initialization:**
   - Run the `init_db` function to set up the database schema.

3. **GUI Design:**
   - Use Qt Designer to design the UI and save it as `main_window.ui`.
   - Implement PyQt5 code to load the UI and connect buttons to functionality.

4. **Algorithm Integration:**
   - Implement the spaced repetition algorithm and integrate it with the review process.

5. **Data Management:**
   - Implement functions to manage flashcard data in SQLite.

By following these steps, you'll have a functional desktop-based spaced repetition software built with Python and PyQt5.

Here is the project structure:
```markdown
memory-master/
├── main.py
├── database/
│   ├── __init__.py
│   ├── db_manager.py
├── models/
│   ├── __init__.py
│   ├── flashcard.py
│   ├── user.py
├── ui/
│   ├── __init__.py
│   ├── main_window.py
│   ├── create_flashcard_dialog.py
│   ├── review_flashcard_widget.py
├── algorithms/
│   ├── __init__.py
│   ├── leitner.py
│   ├── supermemo.py
├── resources/
│   ├── images/
│   ├── styles/
│       └── main.qss
└── utils/
    ├── __init__.py
    ├── helpers.py
```