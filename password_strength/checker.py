"""Password strength checks based on simple, explainable heuristics."""

from dataclasses import dataclass
import string

COMMON_PASSWORDS = frozenset(
    {
        "123456",
        "123456789",
        "12345678",
        "password",
        "password1",
        "qwerty",
        "qwerty123",
        "letmein",
        "welcome",
        "admin",
        " iloveyou".strip(),
    }
)


@dataclass(frozen=True)
class StrengthResult:
    """The score and guidance produced for a password."""

    score: int
    maximum_score: int
    tips: tuple[str, ...]
    is_common: bool

    @property
    def label(self) -> str:
        """Return a human-readable label for the score."""
        if self.score <= 1:
            return "Very weak"
        if self.score == 2:
            return "Weak"
        if self.score == 3:
            return "Fair"
        if self.score == 4:
            return "Good"
        return "Strong"


def check_password(password: str) -> StrengthResult:
    """Check password length, character variety, and common-password usage."""
    tips: list[str] = []
    score = 0

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        tips.append("Use at least 12 characters.")
    else:
        tips.append("Use at least 8 characters, ideally 12 or more.")

    categories = (
        any(character.islower() for character in password),
        any(character.isupper() for character in password),
        any(character.isdigit() for character in password),
        any(character in string.punctuation for character in password),
    )
    variety = sum(categories)
    if variety >= 3:
        score += 2
    elif variety == 2:
        score += 1
        tips.append("Mix at least three character types: lowercase, uppercase, numbers, and symbols.")
    else:
        tips.append("Add a mix of lowercase, uppercase, numbers, and symbols.")

    normalized = password.casefold()
    is_common = normalized in COMMON_PASSWORDS
    if is_common:
        tips.insert(0, "Avoid common passwords and predictable variations.")
    else:
        score += 1

    if not tips and score < 5:
        tips.append("Use a longer, unique passphrase for an even stronger password.")

    return StrengthResult(score, 5, tuple(tips), is_common)
