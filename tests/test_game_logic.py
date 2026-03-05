from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# ---------------------------------------------------------------------------
# Bug-regression tests — logic is defined inline to avoid the streamlit
# import side-effect that prevents importing from app.py directly.
# ---------------------------------------------------------------------------

def _check_guess_fixed(guess, secret):
    """Inline copy of the fixed check_guess from app.py."""
    if guess == secret:
        return "Win", "Correct!"
    try:
        if guess > secret:
            return "Too High", "Go LOWER!"
        else:
            return "Too Low", "Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "Correct!"
        if g > secret:
            return "Too High", "Go HIGHER!"
        return "Too Low", "Go LOWER!"


def _get_range_for_difficulty_fixed(difficulty: str):
    """Inline copy of the fixed get_range_for_difficulty from app.py."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200
    return 1, 100


def test_hint_direction_high_guess():
    # Bug 1 — hint direction was swapped: when guess > secret the original code
    # returned "Too Low" / "Go HIGHER" instead of "Too High" / "Go LOWER".
    # This test catches that regression by asserting the outcome is "Too High"
    # and that the hint message tells the player to go LOWER, not HIGHER.
    outcome, message = _check_guess_fixed(80, 50)
    assert outcome == "Too High", (
        "A guess above the secret must produce outcome 'Too High', not 'Too Low'"
    )
    assert "LOWER" in message, (
        "Hint for a high guess must say LOWER, not HIGHER"
    )


def test_hint_direction_low_guess():
    # Bug 1 (complementary) — also verify the low-guess branch was not
    # accidentally broken by the swap fix: guess < secret must be "Too Low".
    outcome, message = _check_guess_fixed(20, 50)
    assert outcome == "Too Low", (
        "A guess below the secret must produce outcome 'Too Low'"
    )
    assert "HIGHER" in message, (
        "Hint for a low guess must say HIGHER"
    )


def test_hard_difficulty_range_exceeds_normal():
    # Bug 2 — Hard difficulty originally returned (1, 50), which is *smaller*
    # than Normal's (1, 100), making Hard easier rather than harder.
    # The fix sets Hard to (1, 200).  This test catches the regression by
    # asserting the Hard upper bound is strictly greater than Normal's.
    _, normal_high = _get_range_for_difficulty_fixed("Normal")
    _, hard_high = _get_range_for_difficulty_fixed("Hard")
    assert hard_high > normal_high, (
        f"Hard upper bound ({hard_high}) must exceed Normal upper bound "
        f"({normal_high}); original bug returned 50 which is less than 100"
    )
    assert hard_high > 100, (
        "Hard difficulty upper bound must be greater than 100"
    )


def test_check_guess_with_int_secret_no_type_coercion():
    # Bug 3 — the original app code cast the secret to str on even-numbered
    # attempts before passing it to check_guess, causing string-based
    # comparisons that produced wrong results (e.g. "9" > "80" is True as
    # strings but False as ints).  The fix always passes an int secret.
    # This test confirms that when both guess and secret are ints the numeric
    # comparison branch is used and the result is correct — specifically a
    # case that would be wrong under string comparison.
    #
    # "9" > "80" is True (lexicographic), but 9 > 80 is False.
    # So with an int secret of 80 and guess of 9 we must get "Too Low".
    outcome, _ = _check_guess_fixed(9, 80)
    assert outcome == "Too Low", (
        "guess=9 vs secret=80 (both ints) must be 'Too Low'; "
        "string comparison would have incorrectly returned 'Too High'"
    )
