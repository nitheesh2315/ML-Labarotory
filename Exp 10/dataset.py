"""Sample dataset for Student Performance Prediction."""
import numpy as np

FEATURE_NAMES = ["Study hours per day", "Attendance (%)",
                 "Previous marks"]

# Each row: (study_hours, attendance_percent, previous_marks, final_marks)
STUDENT_DATA = [
    (5.4, 85, 89, 70), (2.6, 57, 53, 42), (1.0, 77, 85, 53),
    (4.3, 91, 53, 59), (2.8, 99, 62, 58), (4.9, 77, 95, 68),
    (5.4, 70, 95, 64), (2.1, 93, 72, 58), (1.2, 61, 66, 38),
    (7.4, 92, 73, 75), (4.5, 72, 50, 54), (2.3, 98, 77, 64),
    (3.6, 77, 35, 50), (2.1, 79, 51, 48), (4.6, 97, 86, 71),
    (6.2, 76, 40, 60), (4.6, 82, 88, 74), (5.2, 59, 38, 50),
    (3.3, 65, 44, 48), (3.7, 80, 94, 70), (5.2, 75, 73, 62),
    (2.1, 80, 61, 49), (3.8, 92, 40, 56), (2.5, 55, 75, 53),
    (7.1, 59, 75, 66), (6.9, 76, 92, 74), (5.0, 67, 43, 57),
    (7.5, 66, 68, 68), (7.2, 98, 74, 72), (3.6, 99, 60, 63),
]


def load_dataset():
    """Return the feature matrix X and target vector y (NumPy arrays)."""
    data = np.array(STUDENT_DATA, dtype=float)
    X = data[:, :3]     # study hours, attendance, previous marks
    y = data[:, 3]      # final marks out of 100
    return X, y
