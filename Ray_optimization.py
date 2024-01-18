import os
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from ray import tune
import ray
from tune_sklearn import TuneSearchCV
from Opening_Dataset import X, y

os.environ["RAY_AIR_NEW_OUTPUT"] = "0"

# Load example dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Ray
ray.init()

# Define the search space
search_space = {
    "hidden_layer_sizes": tune.choice([(30, 128, 5), (30, 256, 5), (30, 68, 5)]),
    "activation": tune.choice(['tanh']),
    "alpha": tune.choice([0.0001]),
    "learning_rate_init": tune.choice([0.0001]),
    "random_state": tune.choice([42]),
    "max_iter": tune.choice([200]),  # You can adjust this value
    "early_stopping": tune.choice([True]),  # Enable early stopping
    "n_iter_no_change": tune.choice([10]),  # Number of iterations with no improvement to wait before stopping
    "verbose": tune.choice([True]),  # Set to True for more training information
    # "activation": tune.choice(['relu', 'tanh']),
    # "alpha": tune.loguniform(1e-6, 1e-2),
    # "learning_rate_init": tune.loguniform(1e-5, 1e-2),
}

# Perform hyperparameter tuning with Ray Tune and TuneSearchCV
clf = MLPClassifier()
tune_search = TuneSearchCV(
    clf,
    search_space,
    search_optimization="bayesian",
    n_trials=6,
    n_jobs=6,
    early_stopping=True,
    max_iters=20,
    scoring="accuracy"
    # local_dir="./ray_results"  # Set a directory to store the results
)
#tune_search.fit(X_train, y_train)
tune_search.fit(X_train, y_train)
#y_pred = tune_search.predict(X_test)

# Print the best hyperparameters
print("Best Parameters:", tune_search.best_params_)
