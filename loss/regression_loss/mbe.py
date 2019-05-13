
def mbe(predictions, targets):
    """
        Mean Bias Error

        Algo:

            1. Calculate the differences between predictions and targets.
            2. Add them all up.
            3. Divide by the number of errors.

    :param predictions:
    :param targets:
    :return:
    """
    differnces = predictions - targets
    mbe_val = differnces.mean()
    return mbe_val
