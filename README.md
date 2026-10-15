```markdown
# NumPy Fundamentals Practice

A beginner-friendly collection of Python examples for learning and practicing the fundamentals of **NumPy**[cite: 7]. This repository documents a structured learning journey through small, focused programs covering arrays, dimensions, arithmetic, vectorized operations, slicing, filtering, broadcasting, aggregations, and random number generation.

---

## 📚 Topics Covered

* **NumPy Basics**: Creating arrays, converting Python lists to arrays, comparing lists versus NumPy arrays, and checking data types[cite: 7, 9].
* **Array Dimensions and Shape**: Working with 1D, 2D, 3D, and 4D arrays, understanding `ndim`, `shape`, and multi-dimensional indexing[cite: 5].
* **Arithmetic Operations**: Performing scalar arithmetic, element-wise operations, and boolean comparisons[cite: 2].
* **Vectorized Operations**: Applying calculations across array elements without writing explicit Python loops[cite: 2].
* **Mathematical Functions**: Using square roots, rounding, floor functions, exponential values, and $\pi$ (pi)[cite: 2].
* **Array Slicing**: Selecting rows and columns, slicing specific ranges, and manipulating array slices[cite: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
* **Boolean Filtering**: Selecting values based on conditions using Boolean indexing and `np.where()`[cite: 4].
* **Broadcasting**: Performing arithmetic operations on arrays with compatible shapes by virtually expanding dimensions[cite: 3].
* **Aggregation Functions**: Summarizing data using sum, mean, standard deviation, variance, min, max, index positions (`argmin`, `argmax`), and the `axis` parameter[cite: 1].
* **Random Number Generation**: Generating random integers and floats using `default_rng()`, setting seeds, creating uniform distributions, shuffling arrays, and choosing random elements[cite: 10].
* **Performance Timing**: Comparing standard Python lists with NumPy operations using `%timeit`[cite: 8].

---

## 🗂️ Repository Contents

| File | Concepts Practiced |
| :--- | :--- |
| `numpy1.py` | Comparing a NumPy array with a Python list and checking their types[cite: 7] |
| `numpy2.py` | Timing Python lists and NumPy operations with `%timeit`[cite: 8] |
| `numpy3.py` | Creating arrays from lists and capturing user input into NumPy arrays[cite: 9] |
| `num4.py` | Basic array operations and scalar multiplication[cite: 6] |
| `Arithmatic.py` | Scalar arithmetic, vectorized math functions, element-wise operations, and comparisons[cite: 2] |
| `multidimensional.py` | 1D, 2D, 3D, and 4D arrays; dimensions, shape, and multi-dimensional indexing[cite: 5] |
| `slicing.py` | Selecting rows and columns from a 2D array[cite: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| `filtering.py` | Boolean filtering, conditional statements, and `np.where()`[cite: 4] |
| `broadcasting.py` | Broadcasting with scalars and arrays of different shapes[cite: 3] |
| `Aggregate.py` | Aggregation functions and the `axis` parameter (`axis=0` and `axis=1`)[cite: 1] |
| `randomNUM.py` | Random integers and floats, uniform distributions, array shuffling, and random selections[cite: 10] |

> **Note:** For a cleaner and more consistent naming convention, it is recommended to rename `Arithmatic.py` to `arithmetic.py` and `Aggregate.py` to `aggregation.py`.

---

## ⚙️ Requirements

* **Python 3**
* **NumPy**

Most scripts can be executed directly from the terminal. Note that performance timing examples utilizing `%timeit` require an IPython or Jupyter notebook environment[cite: 8].

---

## 🚀 Setup & Installation

### 1. Clone the Repository
Replace `<your-github-username>` with your actual GitHub username:
```bash
git clone [https://github.com/](https://github.com/)<your-github-username>/numpy-fundamentals-practice.git
cd numpy-fundamentals-practice

```

### 2. Create a Virtual Environment (Recommended)

* **On Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate

```


* **On macOS or Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate

```



### 3. Install Dependencies

```bash
python -m pip install numpy

```

---

## ▶️ Running Examples

Execute any script directly from the repository folder using Python:

```bash
python multidimensional.py

```

You can replace `multidimensional.py` with any of the practice scripts, such as:

```bash
python filtering.py
python broadcasting.py
python Aggregate.py
python randomNUM.py

```

---

## 🎯 Learning Goals

Through these programs, the focus is on mastering:

* Creating, inspecting, and transforming NumPy arrays.


* Navigating multi-dimensional shapes, dimensions, and indexing techniques.


* Executing high-performance vectorized calculations and element-wise arithmetic.


* Applying condition-based filtering and custom transformations with `np.where()`.


* Leveraging broadcasting rules for arrays of varying shapes.


* Summarizing datasets efficiently via aggregation functions across specified axes.


* Simulating and sampling data using robust random number generators.



---

## 📈 Project Status

**Learning in progress.** New examples and explanations will continue to be added as advanced NumPy concepts are explored.

---

## 💡 Acknowledgment

Created as a personal Python learning repository to explore and master NumPy fundamentals through practical code examples.

```

```
