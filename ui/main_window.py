# Defines the main application window.

from PyQt5.QtWidgets import QMainWindow, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QLabel, QWidget, QToolBar, QAction
from database.db_manager import init_db, get_due_flashcards, update_flashcard_review

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spaced Repetition Software")
        self.setGeometry(100, 100, 800, 600)
        self.current_flashcard = None

        self.init_ui()
        init_db()
        self.show_next_flashcard()

    def init_ui(self):
        self.central_widget = QWidget()
        self.layout = QVBoxLayout()

        self.flashcard_label = QLabel("Flashcard")
        self.layout.addWidget(self.flashcard_label)

        self.remember_button = QPushButton("Remembered")
        self.remember_button.clicked.connect(self.mark_remembered)
        self.layout.addWidget(self.remember_button)

        self.forget_button = QPushButton("Forgotten")
        self.forget_button.clicked.connect(self.mark_forgotten)
        self.layout.addWidget(self.forget_button)

        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def show_next_flashcard(self):
        flashcards = get_due_flashcards()
        if flashcards:
            self.current_flashcard = flashcards[0]
            self.flashcard_label.setText(self.current_flashcard[1])  # Display the front text
        else:
            self.flashcard_label.setText("No flashcards due today!")

    def mark_remembered(self):
        if self.current_flashcard:
            update_flashcard_review(self.current_flashcard[0], True)
            self.show_next_flashcard()

    def mark_forgotten(self):
        if self.current_flashcard:
            update_flashcard_review(self.current_flashcard[0], False)
            self.show_next_flashcard()
