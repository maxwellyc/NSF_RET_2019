import numpy as np
import matplotlib.pyplot as plt

# 1. After transforming data into readable format like .txt or .csv, how would you convert it into convenient data structure that you could use?

# 2. Understand how to use the built-in function open() in python
file = open("","r") # Input data file

# 3. Understand how to use the built-in function readlines() in python
lines = file.readlines()

# 4. What is the structure of "lines"? You can either read the documentation of readlines(), or you could simply print it out using function print (), you can also try function type().

# 5. Read about build-in function split(), can it be of any use here? Can you use it on each element of lines?

# 6. Recall how you did the fitting of coefficients by hand, can you use <for loops> to automate this process? Also think about how you would store the results?

# 7. When you have all the individual coefficients, which one should you use? Or would you use other methods to obtain the best coefficient?

# 8. Is there any pattern in the different coefficients that you could exploit, to make the fit better? What's the easiest way to discover a pattern or trend, in our radii vs mass number A example?

# 9. Look at the data pdf file again, what radius is this? Is this the radius of the nucleus, or is it something slightly different? Besides finding a relationship between R(radius) and A(mass #), can you think of other basic nuclear variable(s) that could potentially be related to R?

# 10. Once you've completed the above, recall the chi^2 fit we talked about, relating to step 7, how would you use chi^2 fit to present a better coeficient. W


# We'll do chi^2 fitting on the next code project.
