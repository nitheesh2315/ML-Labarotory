"""Helper functions: validated input and performance category."""


def get_number(prompt, low, high):
    """Keep asking until a number between low and high is entered."""
    while True:
        text = input(prompt).strip()
        try:
            value = float(text)
        except ValueError:
            print("  Invalid input. Please enter a number.")
            continue
        if low <= value <= high:
            return value
        print(f"  Value must be between {low} and {high}. Try again.")


def get_category(marks):
    """Convert predicted marks into a performance category."""
    if marks >= 85:
        return "Excellent"
    if marks >= 70:
        return "Good"
    if marks >= 50:
        return "Average"
    return "Needs Improvement"
