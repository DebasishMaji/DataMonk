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