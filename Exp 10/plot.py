"""Graphs for the Student Performance Prediction experiment."""
import matplotlib
matplotlib.use("Agg")           # save the graph as an image file
import matplotlib.pyplot as plt


def save_graph(X, y, y_test, y_pred, mae, r2, filename):
    """Save (a) actual vs predicted marks and (b) study hours vs marks."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

    # (a) Actual vs predicted marks (test students)
    ax1.scatter(y_test, y_pred, color="tab:blue", s=70,
                label="Test student")
    ax1.plot([20, 100], [20, 100], "r--", label="Perfect prediction")
    ax1.set_xlabel("Actual marks")
    ax1.set_ylabel("Predicted marks")
    ax1.set_title(f"Actual vs Predicted (MAE={mae:.2f}, R2={r2:.4f})")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # (b) Study hours vs final marks of all students in the dataset
    ax2.scatter(X[:, 0], y, color="tab:green", s=50)
    ax2.set_xlabel("Study hours per day")
    ax2.set_ylabel("Final marks")
    ax2.set_title("Study Hours vs Final Marks (dataset)")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()
