"""Training and evaluation of the Linear Regression model."""
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


def train_model(X, y, test_size=0.2, random_state=42):
    """Split the data, train Linear Regression and evaluate it."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    return model, X_train, X_test, y_test, y_pred, mae, r2


def predict_marks(model, study_hours, attendance, previous_marks):
    """Predict final marks (limited to the range 0 - 100)."""
    features = [[study_hours, attendance, previous_marks]]
    marks = model.predict(features)[0]
    return float(min(max(marks, 0.0), 100.0))
