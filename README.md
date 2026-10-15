# NumPy Fundamentals Practice

A beginner-friendly collection of Python examples for learning and practicing the fundamentals of **NumPy**. This repository documents my learning journey through small, focused programs covering arrays, dimensions, arithmetic operations, vectorization, slicing, filtering, broadcasting, aggregation, and random number generation.

## 📚 Topics Covered

- **NumPy Basics:** Creating arrays, converting Python lists to NumPy arrays, comparing Python lists with NumPy arrays, and checking data types.
- **Array Dimensions and Shape:** Working with 1D, 2D, 3D, and 4D arrays and understanding `ndim`, `shape`, and multidimensional indexing.
- **Arithmetic Operations:** Performing scalar arithmetic, element-wise operations, and Boolean comparisons.
- **Vectorized Operations:** Applying calculations to array elements without explicit Python loops.
- **Mathematical Functions:** Using square roots, rounding, floor functions, exponential functions, and π.
- **Array Slicing:** Selecting rows and columns, extracting specific ranges, and working with array slices.
- **Boolean Filtering:** Selecting elements based on conditions using Boolean indexing and `np.where()`.
- **Broadcasting:** Performing operations on arrays with compatible shapes.
- **Aggregation Functions:** Calculating sum, mean, standard deviation, variance, minimum, maximum, `argmin()`, and `argmax()`, including the use of the `axis` parameter.
- **Random Number Generation:** Generating random integers and floating-point numbers using `default_rng()`, setting seeds, creating uniform distributions, shuffling arrays, and selecting random elements.
- **Performance Timing:** Comparing Python list operations with NumPy operations using `%timeit`.

## 🗂️ Repository Contents

| File | Concepts Practiced |
|---|---|
| `numpy1.py` | Comparing NumPy arrays with Python lists and checking data types |
| `numpy2.py` | Timing Python list and NumPy operations using `%timeit` |
| `numpy3.py` | Creating arrays from lists and capturing user input into NumPy arrays |
| `num4.py` | Basic array operations and scalar multiplication |
| `Arithmatic.py` | Scalar arithmetic, mathematical functions, element-wise operations, and comparisons |
| `multidimensional.py` | 1D, 2D, 3D, and 4D arrays, dimensions, shape, and multidimensional indexing |
| `slicing.py` | Selecting rows and columns and extracting array slices |
| `filtering.py` | Boolean filtering, conditional statements, and `np.where()` |
| `broadcasting.py` | Broadcasting with scalars and arrays of different shapes |
| `Aggregate.py` | Aggregation functions and the `axis` parameter (`axis=0` and `axis=1`) |
| `randomNUM.py` | Random integers and floats, uniform distributions, shuffling, and random selections |

**Note:** Consider renaming `Arithmatic.py` to `arithmetic.py` and `Aggregate.py` to `aggregation.py` for consistent file naming. Update the table if you rename these files.

## ⚙️ Requirements

- Python 3
- NumPy

Install NumPy using pip:

```bash
python -m pip install numpy
```

Most scripts can be run directly from the terminal. The `numpy2.py` example uses `%timeit`, which requires an IPython or Jupyter environment.

## 🚀 Setup and Installation

### 1. Clone the Repository

Replace `akankshavishwasrao3000` with your GitHub username if you use a different account.

```bash
git clone https://github.com/akankshavishwasrao3000/numpy-fundamentals-practice.git
cd numpy-fundamentals-practice
```

### 2. Install Dependencies

```bash
python -m pip install numpy
```

### 3. Run an Example

For example:

```bash
python numpy1.py
```

For the `%timeit` example, open `numpy2.py` in an IPython or Jupyter environment and run its timing commands there.

## 🎯 Learning Goal

The goal of this repository is to strengthen my understanding of NumPy through practical examples and hands-on coding, building a foundation for numerical computing and data analysis in Python.
