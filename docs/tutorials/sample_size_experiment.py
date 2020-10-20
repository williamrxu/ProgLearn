from sklearn.ensemble import RandomForestClassifier
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Dropout
from tensorflow.keras.optimizers import SGD, Adam

__all__ = [
    "random_forest_classifier_model",
    "binary_deep_neural_network",
    "parametric_convolutional_neural_network",
    "multiclass_deep_neural_network",
]


def random_forest_classifier_model(X_train, y_train, num_trees, max_depth, verbose):
    """
    Returns a random forest classifier model trained on data X_train and labels y_train

    Args:
        X_train : ndarray
            A numpy array of input data with shape [num_examples, num_features]
        y_train : ndarray
            A numpy array of data labels with shape [num_examples,]
        num_trees : int
            An int to identify number of trees to train the classifier with
        max_depth : int
            An int to identify the max depth of each tree in the classifier

    Returns:
        rf_model : object
            A random forest classifier model for predicting new data
    """

    rf_model = RandomForestClassifier(
        n_estimators=num_trees, max_depth=max_depth, verbose=verbose
    )
    rf_model.fit(X_train, y_train)

    return rf_model


def binary_deep_neural_network(
    X_train, y_train, epochs, batch_size, learning_rate, validation_split, verbose
):
    """
    Returns a binary neural network model trained on data X_train and labels y_train

    Args:
        X_train : ndarray
            A numpy array of input data with shape [num_examples, num_features]
        y_train : ndarray
            A numpy array of data labels with shape [num_examples,]
        epochs : int
            An int to identify the total number of epochs the models is trained with
        batch_size : int
            An int to identify the batch size for training the model
        learning_rate : float
            A float to identify the learning rate of the Adam optimizer
        validation_split : float
            A float between 0 and 1 to represent the amount of training data to be used for validation
        verbose : int
            An int to represent the level of output while training the model

    Returns:
        dnn_model : object
            A trained binary neural network
    """

    dnn_model = Sequential()

    dnn_model.add(Dense(X_train.shape[1], activation="relu"))
    dnn_model.add(Dense(8, activation="relu"))
    dnn_model.add(Dense(units=1, activation="sigmoid"))

    adam_optimizer = Adam(learning_rate=learning_rate)
    dnn_model.compile(
        optimizer=adam_optimizer, loss="binary_crossentropy", metrics=["accuracy"]
    )

    dnn_model.fit(
        x=X_train,
        y=y_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_split=validation_split,
        verbose=verbose,
    )

    return dnn_model


def multiclass_deep_neural_network(
    X_train,
    y_train,
    output_nodes,
    epochs,
    batch_size,
    learning_rate,
    validation_split,
    verbose,
):
    """
    Returns a multiclass neural network model trained on data X_train and labels y_train

    Args:
        X_train : ndarray
            A numpy array of input data with shape [num_examples, num_features]
        y_train : ndarray
            A numpy array of data labels with shape [num_examples,]
        output_nodes : int
            An int corresponding to the number of classes in the dataset if greater than 2
        epochs : int
            An int to identify the total number of epochs the models is trained with
        batch_size : int
            An int to identify the batch size for training the model
        learning_rate : float
            A float to identify the learning rate of the Adam optimizer
        validation_split : float
            A float between 0 and 1 to represent the amount of training data to be used for validation
        verbose : int
            An int to represent the level of output while training the model

    Returns:
        dnn_model_mc : object
            A trained multiclass neural network
    """

    dnn_model_mc = Sequential()

    dnn_model_mc.add(Dense(8, activation="relu"))
    dnn_model_mc.add(Dense(8, activation="relu"))
    dnn_model_mc.add(Dense(units=output_nodes, activation="softmax"))

    adam_optimizer = Adam(learning_rate=learning_rate)
    dnn_model_mc.compile(
        optimizer=adam_optimizer, loss="categorical_crossentropy", metrics=["accuracy"]
    )

    dnn_model_mc.fit(
        x=X_train,
        y=y_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_split=validation_split,
        verbose=verbose,
    )

    return dnn_model_mc


def parametric_convolutional_neural_network(
    X_train,
    y_train,
    complexity,
    epochs,
    batch_size,
    learning_rate,
    validation_split,
    verbose,
):
    """
    Returns a convolutional neural network model trained on data X_train and labels y_train

    Args:
        X_train : ndarray
            A numpy array of input data
        y_train : ndarray
            A numpy array of data labels with shape [num_examples,]
        complexity : int
            An int to represent an arbitrary complexity value where each additional int over
            2 adds another convolutional layer to the model
        epochs : int
            An int to identify the total number of epochs the models is trained with
        batch_size : int
            An int to identify the batch size for training the model
        learning_rate : float
            A float to identify the learning rate of the Adam optimizer
        validation_split : float
            A float between 0 and 1 to represent the amount of training data to be used for validation
        verbose : int
            An int to represent the level of output while training the model

    Returns:
        cnn_model : object
            A trained convolutional neural network
    """

    cnn_model = Sequential()

    cnn_model.add(Conv2D(32, (3, 3), activation="relu", input_shape=(32, 32, 3)))
    cnn_model.add(Conv2D(64, (3, 3), activation="relu"))
    cnn_model.add(MaxPooling2D((2, 2)))

    if complexity > 2:
        for _ in range(1, complexity - 1):
            cnn_model.add(Conv2D(64, (3, 3), activation="relu"))

        cnn_model.add(MaxPooling2D((2, 2)))

    cnn_model.add(Flatten())
    cnn_model.add(Dense(64, activation="relu"))
    cnn_model.add(Dense(1, activation="sigmoid"))

    adam_optimizer = Adam(learning_rate=learning_rate)
    #     sgd = SGD(learning_rate=learning_rate)
    cnn_model.compile(
        optimizer=adam_optimizer, loss="binary_crossentropy", metrics=["accuracy"]
    )

    cnn_model.fit(
        x=X_train,
        y=y_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_split=validation_split,
        verbose=verbose,
    )

    return cnn_model
