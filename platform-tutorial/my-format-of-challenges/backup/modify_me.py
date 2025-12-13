# backups/modify_me.py
#
# Immutable backup of the original challenge source code.
# This file represents the baseline implementation and does NOT
# include difficulty labels.

class Challenge:
    """
    Current data strucutre of the class Challenge
    """

    def __init__(self, title, description, status="draft"):
        self.title = title
        self.description = description
        self.status = status

        self.metadata = {
            "version": 1,
            "created_by": "system",
            "word_count": self._calculate_word_count(description),
        }

        self._validate_title(title)
        self._validate_description(description)
        self._validate_status(status)

    # ---------------- Validation ----------------

    def _validate_title(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if not title.strip():
            raise ValueError("Title cannot be empty.")

    def _validate_description(self, description):
        if not isinstance(description, str):
            raise TypeError("Description must be a string.")
        if len(description) < 5:
            raise ValueError("Description must be at least 5 characters.")

    def _validate_status(self, status):
        if status not in ["draft", "published"]:
            raise ValueError("Invalid status.")

    # ---------------- Utilities ----------------

    def _calculate_word_count(self, text):
        return len(text.split())
        
    def publish(self):
        self.status = "published"

    def unpublish(self):
        self.status = "draft"

    def get_summary(self):
        return f"{self.title}: {self.description}"

    def get_metadata(self):
        return dict(self.metadata)

    def rename(self, new_title):
        self._validate_title(new_title)
        self.title = new_title


class ChallengeManager:
    """
    Manages Challenge objects.
    """

    def __init__(self):
        self._challenges = []

    def add_challenge(self, challenge):
        if not isinstance(challenge, Challenge):
            raise TypeError("Expected Challenge instance.")
        self._challenges.append(challenge)

    def get_challenge(self, index):
        return self._challenges[index]

    def list_challenges(self):
        return list(self._challenges)

    def find_by_title(self, title):
        return [c for c in self._challenges if c.title.lower() == title.lower()]

    def filter_by_tag(self, tag):
        return [c for c in self._challenges if tag in c.tags]

    def publish_all(self):
        for c in self._challenges:
            c.publish()

    def remove_challenge(self, index):
        if index < 0 or index >= len(self._challenges):
            raise IndexError("Invalid index.")
        del self._challenges[index]
