import pickle
from sklearn.datasets import fetch_openml
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X, Y = fetch_openml(name = 'mnist_784', version = 1, return_X_y = True)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

model = RandomForestClassifier(n_jobs = -1)


model.fit(X_train, y_train)

print(model.score(X_test, y_test))

with open('mnist_model.pkl', 'wb') as f:
    pickle.dump(model, f)