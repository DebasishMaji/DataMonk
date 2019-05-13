import numpy as np


def logcosh(predictions, targets):
    """
        Log-Cosh Loss

            Algo:

                1. Calculate differences between predictions and targets
                2. calculate cosh of differences
                3. calculate log of subsequent result

    :param predictions:
    :param targets:
    :return:
    """
    loss = np.log(np.cosh(predictions - targets))
    return np.sum(loss)
