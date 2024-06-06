# Defines the flashcard model(s).

class Flashcard:
    def __init__(self, id, front_text, back_text, image_path, audio_path, tags, next_review_date, box, last_reviewed):
        self.id = id
        self.front_text = front_text
        self.back_text = back_text
        self.image_path = image_path
        self.audio_path = audio_path
        self.tags = tags
        self.next_review_date = next_review_date
        self.box = box
        self.last_reviewed = last_reviewed

    def update_review_date(self, new_date):
        self.next_review_date = new_date

    def move_to_next_box(self):
        self.box = min(self.box + 1, 5)

    def reset_box(self):
        self.box = 1
