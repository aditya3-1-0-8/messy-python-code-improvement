"""Student grade report (improved version of messy_script.py)."""

STUDENTS = [("Aditya", 92), ("Riya", 85), ("Kabir", 58), ("Neha", 71)]


def calculate_average(students):
    """Return the average marks of a list of (name, marks) pairs."""
    return sum(marks for _, marks in students) / len(students)


def get_grade(marks):
    """Convert marks to a letter grade."""
    if marks >= 90:
        return "A"
    if marks >= 75:
        return "B"
    if marks >= 60:
        return "C"
    return "F"


def main():
    print(f"Class average: {calculate_average(STUDENTS):.2f}")
    for name, marks in STUDENTS:
        print(f"{name}: {marks} marks, grade {get_grade(marks)}")


if __name__ == "__main__":
    main()
