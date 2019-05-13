import numpy as np


def mse(predictions, targets):
    """
        Mean Square Error or Quadratic Loss or L2 Loss

        Algo:
            Pre-calculation:
                Find the regression line.
                Insert your X values into the linear regression equation to find the new Y values (Y').

            1. Subtract the new Y value from the original to get the error.
            2. Square the errors.
            3. Add up the errors.
            4. Find the mean.

    :return: mean square error for a given prediction data set and corresponding truth value
    """
    differences = predictions - targets
    differences_squared = differences**2
    differences_squared_mean = differences_squared.mean()
    mse_val = np.sqrt(differences_squared_mean)
    return mse_val
