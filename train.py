from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import numpy as np

# Read in data
X_train = np.genfromtxt("data/train_features.csv")
y_train = np.genfromtxt("data/train_labels.csv")
X_test = np.genfromtxt("data/test_features.csv")
y_test = np.genfromtxt("data/test_labels.csv")

# Fit a model
depth = 5
clf = RandomForestClassifier(max_depth=depth)
clf.fit(X_train, y_train)

acc = clf.score(X_test, y_test)
print(acc)

y_pred = clf.predict(X_test)

metrics = """
Accuracy: {:10.4f}

![Confusion Matrix](plot.png)
""".format(acc)
with open("metrics.txt", "w") as outfile:
    outfile.write(metrics)

# Plot it
disp = ConfusionMatrixDisplay.from_predictions(y_test, y_pred, normalize="true", cmap=plt.cm.Blues)
plt.savefig("plot.png")
