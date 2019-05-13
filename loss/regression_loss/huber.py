import numpy as np


def huber(predictions, targets, delta):
    """
        Huber Loss, Smooth Mean Absolute Error

        Algo:

            MAE when 𝛿 ~ 0 and MSE when 𝛿 ~ ∞ (large numbers.)

            Case 1: |y-f(x)| <= 𝛿 calculate ((y-f(x))**2)/2
            Case 2: Otherwise 𝛿 |y - f(x)| - (𝛿**2)/2

    :param predictions:
    :param targets:
    :param delta:
    :return:
    """
    loss = np.where(np.abs(targets-predictions) < delta, 0.5*((targets-predictions)**2), delta*np.abs(targets - predictions) - 0.5*(delta**2))
    return np.sum(loss)
