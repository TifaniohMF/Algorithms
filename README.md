# 🎯️ ALGORITHM

![License](https://img.shields.io/badge/license-MIT-green)
![Last Commit](https://img.shields.io/github/last-commit/TifaniohMF/Algorithms)

In this repository, you can see different algorithm based in mathematics.


---

## 📁️ Projects structure
```text
Algorithms/
├── LICENSE
├── README.md
├── fibonacci
│   ├── README.md
│   ├── docs
│   │   ├── docs.aux
│   │   ├── docs.log
│   │   ├── docs.pdf
│   │   └── docs.tex
│   ├── src
│   │   ├── __init__.py
│   │   └── fibonacci.py
│   └── test_fibonacci.py
├── math_lib
│   ├── README.md
│   ├── src
│   │   ├── __init__.py
│   │   ├── abs.py
│   │   ├── power.py
│   │   └── sqrt.py
│   └── tests
│       ├── __init__.py
│       ├── test_abs.py
│       ├── test_power.py
│       └── test_sqrt.py
├── pyproject.toml
├── requirement.txt
├── sort-algo
│   ├── README.md
│   ├── docs
│   │   ├── algorithms.pdf
│   │   └── algorithms.tex
│   ├── src
│   │   ├── __init__.py
│   │   ├── sorting_by_bubbles.py
│   │   ├── sorting_by_replacement.py
│   │   └── sorting_by_select.py
│   └── test_sort_algo.py
└── stats
    ├── src
    │   ├── __init__.py
    │   └── stats.py
    └── tests
        ├── __init__.py
        └── test_stats.py
```
---

## 💻️ Use and installation

Make you sure have python 3.x install into your pc.

1. Clone repository
```bash
git clone https://github.com/TifaniohMF/Algorithms.git
cd Algorithms
```

2. Execute
This is just an example, if you want to know the fibonacci number.
You can import package Fibonacci as follows.
```python
from fibonacci.fibonacci import *

def main():
     fibonacci(5) # If you know the five fibonacci number 
     fibonacci(50)
     
if __name__ == '__main__':
     main()
```

---

### 🤝 Contributions

1. Fork the project.
2. Create a branch dedicated :  

```bash
git checkout -b feature/nouvelle-fonctionnalite
```

3. Commit your changes :  

```bash
git commit -m "feat : add a feature"
```

4. Push to the branch :  

```bash
git push origin feature/new-feature
```

5. Open a **Pull Request**

---
