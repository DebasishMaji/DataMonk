import numpy as np


def mae(predictions, targets):
    """
        Mean Absolute Error

        Algo:
            1. Calculate the differences between predictions and targets.
            2. Add them all up.
            3. Divide by the number of errors.
    :param predictions:
    :param targets:
    :return:
    """
    differences = predictions - targets
    absolute_differences = np.absolute(differences)
    mea_val = absolute_differences.mean()
    return mea_val
