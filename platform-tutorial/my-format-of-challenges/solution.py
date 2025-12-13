class Challenge:
    """
    Represents a coding challenge in the platform.
    """

    VALID_STATUSES = {"draft", "published"}
    VALID_DIFFICULTIES = {"Easy", "Medium", "Hard"}

    # Solution 1
    def __init__(self, title, description, status="draft", difficulty=None):
        # Basic fields
        self.title = title
        self.description = description
        self.status = status
        self.difficulty = difficulty

        # Metadata dictionary storing arbitrary info
        self.metadata = {
            "version": 1,
            "created_by": "system",
            "word_count": self._calculate_word_count(description),
        }

        # Validation
        self._validate_title(title)
        self._validate_description(description)
        self._validate_status(status)
        self._validate_difficulty(difficulty)

    # ------------------------------------------------------------
    # Validation methods
    # ------------------------------------------------------------

    def _validate_title(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if len(title.strip()) == 0:
            raise ValueError("Title cannot be empty.")

    def _validate_description(self, description):
        if not isinstance(description, str):
            raise TypeError("Description must be a string.")
        if len(description) < 5:
            raise ValueError("Description must be at least 5 characters long.")

    def _validate_status(self, status):
        if status not in self.VALID_STATUSES:
            raise ValueError(
                f"Invalid status '{status}'. Allowed: {list(self.VALID_STATUSES)}"
            )

    # Solution 2
    def _validate_difficulty(self, difficulty):
        if difficulty not in self.VALID_DIFFICULTIES:
            raise ValueError(
                f"Invalid difficulty '{difficulty}'. "
                f"Allowed: {list(self.VALID_DIFFICULTIES)}"
            )

    # ------------------------------------------------------------
    # Utility and helper methods
    # ------------------------------------------------------------

    def _calculate_word_count(self, text):
        return len(text.split())

    def publish(self):
        self.status = "published"

    def unpublish(self):
        self.status = "draft"

  # Solution 3
    def get_difficulty(self):
        return self.difficulty

    def get_summary(self):
        """
        Required format:
        [title]: [description]
        Difficulty: [difficulty]
        """
        return (
          # Solution 4
            f"{self.title}: {self.description}\n"
            f"Difficulty: {self.difficulty}"
        )

    def get_metadata(self):
        return dict(self.metadata)

    def rename(self, new_title):
        self._validate_title(new_title)
        self.title = new_title

    # ------------------------------------------------------------
    # Original placeholder method
    # ------------------------------------------------------------

    def increase_version(self):
        self.metadata["version"] += 1

class ChallengeManager:
    """
    Handles creation, retrieval, and searching of challenges.
    """

    def __init__(self):
        self._challenges = []

    def add_challenge(self, challenge):
        if not isinstance(challenge, Challenge):
            raise TypeError("Must add a Challenge object.")
        self._challenges.append(challenge)

    def get_challenge(self, index):
        return self._challenges[index]

    def list_challenges(self):
        return list(self._challenges)

    def find_by_title(self, title):
        matches = []
        for c in self._challenges:
            if c.title.lower() == title.lower():
                matches.append(c)
        return matches

    def publish_all(self):
        for c in self._challenges:
            c.publish()

    def remove_challenge(self, index):
        if index < 0 or index >= len(self._challenges):
            raise IndexError("Invalid challenge index.")
        del self._challenges[index]
