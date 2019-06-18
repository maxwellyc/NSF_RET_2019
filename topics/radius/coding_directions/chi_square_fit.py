# Instead of using an average coeficient, we could do a Chi^2 fit

# To begin, we select a suitable range and step size. In the case of R vs A, the range is probably 0.92~1.0, a good step size might be 0.001 or less. Step size meaning the incremental step you take, for eg, if step_size = 0.001, range = 0.92 ~ 1.0, the points you've chosen for the fit would be: 0.921, 0.922, 0.923 .... 0.999, 1.0.

# The step size is determined by how accurate you want your coeficients to be, increasing it would increase your computational cost, although in our little experiment it probably won't matter.

# The initial range is more or less an educated guess, if you really have no clue which range to choose (say in other problems), then you have no choice but to start with a large range and pay the corresponding computational cost. Read "Maxima and minima" wikipedia page about local and global minima.

# To set a range, try numpy.arange(), read the documentations and see to use this in your case

# The basic idea is to test all the values in this range, and find the one that minimizes (generates the smallest) chi^2.

# It might be useful to define a Python function for chi^2, check out how to define a function

# Once you have the chi^2 and coeficient correspondence, how would you identify the coeficient that gave you the smallest chi^2? What data structure can you use?
