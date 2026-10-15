# **NumPy Fundamentals

**A beginner-friendly repository that demonstrates core NumPy concepts, examples, and exercises.**

---

## **Table of Contents**

- [About](#about)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Core Topics Covered](#core-topics-covered)
- [Examples](#examples)
- [How to Run](#how-to-run)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## **About**

This repository contains clear, concise examples and exercises to help learners understand the fundamentals of NumPy — the fundamental package for numerical computing in Python. It is suitable for beginners and as a quick reference for experienced users.

## **Installation**

- Make sure you have Python 3.8+ installed.
- Recommended: create and use a virtual environment.

Install NumPy via pip:

```bash
pip install numpy
```

Or with conda:

```bash
conda install numpy
```

## **Quick Start**

```python
import numpy as np

# Create an array
arr = np.array([1, 2, 3, 4])
print(arr)

# Basic operations
print(arr + 2)
print(arr * 3)

# Array shape
print(arr.shape)
```

## **Core Topics Covered**

- **Arrays and data types** — creating arrays, dtype, type conversions
- **Array indexing & slicing** — basic, boolean, and fancy indexing
- **Shape manipulation** — reshape, ravel, transpose
- **Arithmetic and broadcasting** — elementwise ops and broadcasting rules
- **Aggregations & statistics** — sum, mean, std, min, max, argmin/argmax
- **Linear algebra basics** — dot, matmul, determinant (via numpy.linalg)
- **Random generation** — random module usage
- **Performance tips** — vectorization vs Python loops
- **I/O** — saving and loading arrays (np.save, np.load, np.savetxt)

## **Examples**

- Basic array creation and operations (examples/basic_arrays.ipynb)
- Indexing and slicing examples (examples/indexing_slicing.ipynb)
- Broadcasting and vectorized computations (examples/broadcasting.ipynb)
- Linear algebra examples (examples/linear_algebra.ipynb)
- Small exercises with solutions (exercises/README.md)

## **How to Run**

- Jupyter notebooks: install Jupyter (`pip install jupyter`) and run `jupyter notebook` to open the examples.
- Python scripts: run the .py files with `python path/to/script.py`.

## **Contributing**

- Contributions are welcome. Please open an issue for new feature ideas or bugs, and submit a pull request with clear descriptions.
- Follow the existing file/folder structure: place notebooks in `examples/` and exercises in `exercises/`.

## **License**

This project is open source — add a LICENSE file if you want a specific license. Suggested: MIT.

## **Contact**

If you have questions or suggestions, open an issue or reach out to the repository owner.
