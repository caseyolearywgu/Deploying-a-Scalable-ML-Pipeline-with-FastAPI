import pytest
# TODO: add necessary import
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model, compute_model_metrics, inference

# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    # Adding a test to confirm that a Random Forest Classifier model is returned.
    """
    # Your code here
    X_train = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
    y_train = [0,1,0,1]
    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier)

# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    # Adding a test to pass in true labels and predictions, then assert that the precision,
    # recall, and F1 scores match the expected result.
    """
    # Your code here
    y = [0,0,1,0,1,1,0,1]
    preds = [1,0,1,0,0,1,1,1]
    actual_precision, actual_recall, actual_f1 = compute_model_metrics(y, preds)
    assert np.isclose(actual_precision, 0.6)
    assert np.isclose(actual_recall, 0.75) 
    assert np.isclose(actual_f1, 0.666666)

# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # Adding a test to determine that the inference() method returns the expected shape.
    """
    # Your code here
    X_train = [[1,2,3], [4,5,6]]
    y_train = [0,1]
    X_test = [[1,2,3], [4,5,6]]
    model = train_model(X_train, y_train)
    preds = inference(model, X_test)
    assert len(preds) == len(X_test)
