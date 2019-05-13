# Loss Function

 Loss function or cost function is a function that maps an event or values of one or more variables onto a real number intuitively representing some "cost" associated with the event.
   
   * Mean Square Error or Quadratic Loss or L2 Loss

         Algo:
            Pre-calculation:
                Find the regression line.
                Insert your X values into the linear regression equation to find the new Y values (Y').

            1. Subtract the new Y value from the original to get the error.
            2. Square the errors.
            3. Add up the errors.
            4. Find the mean.
     
   * Mean Absolute Error
   
         Algo:
            1. Find all of your absolute errors, xi – x.
            2. Add them all up.
            3. Divide by the number of errors.
    
   * Mean Bias Error
   
          Algo:

            1. Calculate the differences between predictions and targets.
            2. Add them all up.
            3. Divide by the number of errors.
   
   * Huber Loss, Smooth Mean Absolute Error

          Algo:

            MAE when 𝛿 ~ 0 and MSE when 𝛿 ~ ∞ (large numbers.)

            Case 1: |y-f(x)| <= 𝛿 calculate ((y-f(x))**2)/2
            Case 2: Otherwise 𝛿 |y - f(x)| - (𝛿**2)/2
   
   * Log-Cosh Loss

          Algo:
            
            1. Calculate differences between predictions and targets
            2. calculate cosh of differences
            3. calculate log of subsequent result