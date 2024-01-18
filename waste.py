# Define the training function
def train_mlp(config):
    clf = MLPClassifier(
        hidden_layer_sizes=config["hidden_layer_sizes"],
        # activation=config["activation"],
        # alpha=config["alpha"],
        # learning_rate_init=config["learning_rate_init"],
        activation='tanh',
        alpha=0.0001,
        learning_rate_init=0.0001,
        random_state=42,
        max_iter=200,  # You can adjust this value
        early_stopping=True,  # Enable early stopping
        n_iter_no_change=10,  # Number of iterations with no improvement to wait before stopping
        verbose=True  # Set to True for more training information
    )
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return 1 - accuracy  # minimize 1 - accuracy

