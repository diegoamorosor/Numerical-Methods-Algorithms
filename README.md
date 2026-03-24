
<p align="center"> 
  <img src="https://i.imgur.com/PNaPIab.png" alt="Image-Numerical-Methods" /> 
</p>

<h1 style="text-align: center">Numerical Methods Algorithms 🧮</h1>

**Numerical Methods Algorithms** are mathematical tools designed to solve complex computational problems through approximations and iterative processes. Unlike analytical methods, which provide exact formulas, numerical methods keep running step-by-step until they find an approximate solution within a mathematically acceptable margin of error.

---

## 🤔 How Do They Work?

Numerical algorithms translate high-level calculus and algebra into programmable computer logic. Based on your provided scripts, these algorithms are divided into three main mathematical categories.

### 1️⃣ Systems of Linear Equations (Iterative Solvers)
These methods find the vector $x$ that satisfies the matrix equation $Ax=b$ by starting with an initial guess and continuously refining it.

* **Jacobi Method (`jacob.py`):** * **Math:** Isolates each variable and uses the values from the *previous* iteration to calculate the new ones. The iterative formula is $$x^{(k+1)}=D^{-1}(b-Rx^{(k)})$$
    * **Code Analysis:** Your script features excellent vectorization using `numpy` (`diag`, `diagflat`, `dot`) to perform matrix operations all at once, avoiding nested `for` loops. However, the iterations are hardcoded (`N=25`) instead of stopping dynamically based on an error threshold.
* **Gauss-Seidel Method (`Método de Gauss-Seidel.py` & `metodoGS.py`):** * **Math:** An improvement over Jacobi. Instead of waiting for the next round, it uses the newly calculated values of $x$ *immediately* within the same iteration.
    * **Code Analysis (Static):** Uses clean Python slicing (`A[i,:i]` and `A[i,i+1:]`) to separate the sums. It implements a highly efficient stopping criterion using `np.allclose` to compare entire vectors with a relative tolerance.
    * **Code Analysis (Interactive):** Calculates the relative percentage error for each variable individually. It smartly includes a protection clause (`if(x[k]!=0):`) to prevent "division by zero" errors if the true root is exactly $0$.

### 2️⃣ Root Finding (Non-Linear Equations)
These scripts search for the specific value of $x$ that makes a function equal to zero: $f(x)=0$.

* **Bisection Method (`metodoBisec.py`):**
    * 
    * **Math:** A "closed" method. It requires an interval $[a,b]$ where the function changes sign (guaranteeing a root exists via Bolzano's Theorem). It then repeatedly cuts the interval in half: $$x_r=\frac{x_l+x_u}{2}$$
    * **Code Analysis:** Uses the `sympy` library for dynamic text-based function inputs. Your script includes a robust "smart scan": it divides the total range into sub-intervals and scans sequentially for sign changes (`valorYV*valorYA<0`) before launching the core bisection logic.
* **Fixed-Point Open Method (`Método de Punto Fijo Abierto.py`):** * **Math:** An "open" method that transforms $f(x)=0$ into $x=g(x)$. Your code cleverly automates this by defining the iterative function as $F(x)=f(x)+x$.
    * **Code Analysis:** Allows for a single initial guess $x_0$ or an interval scan. **Risk:** Open methods do not guarantee convergence. If the derivative of $g(x)$ is greater than $1$ near the root, the iterations will diverge to infinity.

### 3️⃣ Numerical Integration
These algorithms approximate the area under a curve defined by a definite integral $\int_{a}^{b}f(x)dx$ by dividing it into smaller, manageable geometric shapes.

* **Trapezoidal Rule (`trapecio.py`):** * 
    * **Math:** Approximates the area by connecting points with straight lines to form trapezoids: $$I\approx\frac{h}{2}\left[f(x_0)+2\sum f(x_i)+f(x_n)\right]$$ where $h=\frac{b-a}{n}$.
    * **Code Analysis:** A textbook implementation that correctly applies the weight of $2$ to all intermediate points using a `while i < n` loop. It is universal and works with any integer number of segments $n$.
* **Simpson's 1/3 Rule (`simpsom13.py`):** * 
    * **Math:** Improves accuracy by connecting triplets of points with parabolas (degree-2 polynomials). It multiplies odd-indexed points by $4$ and even-indexed points by $2$.
    * **Code Analysis:** **Critical detail:** Mathematically, this method *strictly requires an even number of segments* ($n$). The script currently lacks a validation check to block the user from entering an odd number.
* **Simpson's 3/8 Rule (`simpson38.py`):** * **Math:** Connects four points using cubic polynomials (degree-3). Multiples of 3 get a weight of $2$, while others get a weight of $3$.
    * **Code Analysis:** Highly memory efficient as it sums values on the fly within the loop instead of storing them in lists. **Critical detail:** This method requires $n$ to be a multiple of $3$, which also lacks an input validation check in the code.

---

## 🚀 Advantages

* **Computability:** Allows computers to solve advanced calculus and massive matrices using basic arithmetic loops.
* **Controllable Precision:** You can explicitly dictate the exact accuracy needed by tightening the error tolerance or increasing the number of integration segments ($n$).
* **Flexibility:** Can handle highly irregular mathematical functions that have no analytical anti-derivative or direct algebraic solution.

## ⚠️ Disadvantages

* **Truncation and Round-off:** Results are rarely 100% exact; they are subject to floating-point limitations and approximation errors.
* **Divergence Risks:** Open root methods (Fixed-Point) and iterative matrix solvers (Jacobi) can spiral into infinite loops if specific mathematical conditions (like diagonal dominance) are not met.
* **Performance Bottlenecks:** Evaluating symbolic math expressions repeatedly inside a loop is computationally expensive and slows down execution time.

---

## 📊 Comparison of the Implemented Methods

| Method | Category | Mathematical Approach | Key Constraint / Requirement |
| :--- | :--- | :--- | :--- |
| **Jacobi** | Linear Systems | Simultaneous update | Slower convergence; needs diagonal dominance. |
| **Gauss-Seidel** | Linear Systems | Sequential update | Faster than Jacobi; needs diagonal dominance. |
| **Bisection** | Root Finding | Bracketing (Closed) | Guaranteed to converge; strictly requires a sign change. |
| **Fixed-Point** | Root Finding | Open Formula | Fast, but high risk of divergence. |
| **Trapezoidal** | Integration | Linear Segments | Lower accuracy; works with any integer $n$. |
| **Simpson's 1/3** | Integration | Quadratic Segments | High accuracy; strictly requires $n$ to be an **even** number. |
| **Simpson's 3/8** | Integration | Cubic Segments | High accuracy; strictly requires $n$ to be a **multiple of 3**. |

---

## 🧩 Applications of Numerical Methods

* **Engineering Simulation:** Finite Element Analysis (FEA) uses iterative solvers to process massive structural stress and heat transfer matrices.
* **Computer Graphics:** Simulating fluid dynamics or calculating lighting rendering equations where analytical math is too slow.
* **Data Science & Machine Learning:** Finding the roots of loss function derivatives to optimize algorithms.

---

## 📝 Additional Notes

* **Code Optimization Tip:** In your interactive scripts, instead of evaluating the string function repeatedly with `sympy.sympify().subs()` inside your loops, use `sympy.lambdify` *once* before the loop starts. This compiles the text into a native Python function, drastically speeding up your algorithms!
* **Fun Fact** 🤓 Simpson's rules are named after English mathematician Thomas Simpson, but the astronomer Johannes Kepler used incredibly similar geometric techniques over 100 years earlier to calculate the volume of wine barrels!
