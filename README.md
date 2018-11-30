# Convex Hull solver written in Python

Dependencies:
- [NumPy](http://www.numpy.org/)

   NumPy provides functions to simplify linear algebraic equations, such as cross product, dot product, etc.
- [Matplotlib](https://matplotlib.org/)

   Matplotlib is used to create a visualization of the running algorithms. Additionally, Matplotlib saves an image for each finished dataset by every algorithm that ran visually to the `images/` folder.
- [SciPy](https://www.scipy.org/)

   SciPy is solely used after each algorithm has run to assert that the results of the algorithm are equal to the results of SciPy's `ConvexHull` function.

 Running the program:
- To run the program in 'benchmarking mode', which runs each algorithm 25 times, run main.py with `python3 main.py`.
- To run the program in 'visual mode', which displays the running algorithms, run main.py with `python3 main.py -v`.
