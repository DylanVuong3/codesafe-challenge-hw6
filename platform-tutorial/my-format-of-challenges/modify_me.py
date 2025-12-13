# modify_me.py
#
# This is the main file you will modify to complete the challenge.
# The code below represents a simplified challenge management system.
# It is intentionally incomplete: there is currently NO difficulty system.
# Your task will be to add a secure difficulty implementation without breaking existing functionality.

class Challenge:
    """
    Represents a coding challenge in the platform.
    """

    def __init__(self, title, description, status="draft"):
        # Basic fields
        self.title = title
        self.description = description
        self.status = status  # "draft" or "published"

        # Metadata dictionary storing arbitrary info
        self.metadata = {
            "version": 1,
            "created_by": "system",
            "word_count": self._calculate_word_count(description),
        }

        # NOTE:
        # --------------------------------------------------------
        # There is NO difficulty label in this starter code.
        # You must securely add:
        #   - a difficulty attribute
        #   - validation for allowed difficulty values
        #   - get_difficulty()
        #   - modify get_summary() to include difficulty
        # --------------------------------------------------------

        # Validate fields
        self._validate_title(title)
        self._validate_description(description)
        self._validate_status(status)

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
        allowed = ["draft", "published"]
        if status not in allowed:
            raise ValueError(f"Invalid status '{status}'. Allowed: {allowed}")

    # ------------------------------------------------------------
    # Utility and helper methods
    # ------------------------------------------------------------

    def _calculate_word_count(self, text):
        return len(text.split())

    def publish(self):
        self.status = "published"

    def unpublish(self):
        self.status = "draft"

    def get_summary(self):
        """
        Original functionality users must not break.
        After implementing difficulty, summary should include difficulty.
        """
        return f"{self.title}: {self.description}"

    def get_metadata(self):
        return dict(self.metadata)

    def rename(self, new_title):
        self._validate_title(new_title)
        self.title = new_title

    # ------------------------------------------------------------
    # Placeholder methods (no difficulty here!)
    # ------------------------------------------------------------

    def increase_version(self):
        self.metadata["version"] += 1


# -------------------------------------------------------------------
# ChallengeManager - manages a list of Challenge objects
# -------------------------------------------------------------------

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


# End of file (~130 lines)
