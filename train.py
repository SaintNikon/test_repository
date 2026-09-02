"""
Обучение классификатора на датасете Iris.
Используется для практики работы с Git.
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def main():
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    model = RandomForestClassifier(max_depth=8, random_state=42)
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)
    # comments
    print(f"Accuracy на тесте: {score:.2%}")


if __name__ == "__main__":
    main()
