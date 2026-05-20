---
type: exercise
subject: complex-analysis
difficulty: "⭐"
prereqs:
  - "Def - Branch of the Logarithm"
  - "Def - Complex Exponential and Trigonometric Functions"
tags: [analysis, complex-analysis]
---

# Problem Statement

(a) Show that the **principal branch** of the logarithm $\operatorname{Log}$ (defined on the slit plane $\mathbb{C} \setminus (-\infty, 0]$) is *not* defined at $z = -1$. Find a branch on which $\log(-1)$ *is* defined, and compute its value.

(b) Compute $\operatorname{Log}(i)$ and $\operatorname{Log}(-i)$ using the principal branch.

(c) List the full set of values of $\log(-1)$, $\log(i)$, $\log(-i)$ across all branches.

**Recall:**

The [[Def - Branch of the Logarithm|principal branch]] $\operatorname{Log}$ is defined on $\mathbb{C} \setminus (-\infty, 0]$ by $\operatorname{Log}(z) = \log|z| + i\operatorname{Arg}(z)$, where $\operatorname{Arg}(z) \in (-\pi, \pi)$ is the principal argument. Different branches differ by integer multiples of $2\pi i$.

---

# Convergent Strategy

**Problem class:** Direct computation using the formula $\operatorname{Log}(z) = \log|z| + i\operatorname{Arg}(z)$.

**Assumption pattern:** Specific complex numbers $-1, i, -i$ on or off the principal branch's domain.

**Theorem routing:** Compute modulus and argument; apply the formula. For points on the slit (boundary), choose an alternative branch.

**Key decision point:** The principal branch's domain excludes the negative real axis, so $\operatorname{Log}(-1)$ is *not defined* there. Switching to a branch with a different slit (e.g., along the positive imaginary axis) makes $\log(-1)$ defined.

---

# Legal Operations Used

1. **Compute modulus and argument** of $z$.
2. **Apply the principal branch formula** $\operatorname{Log}(z) = \log|z| + i\operatorname{Arg}(z)$.
3. **Switch to an alternative branch** when the principal branch fails at the input.
4. **Enumerate values across branches** using $\log z + 2\pi i k$ for $k \in \mathbb{Z}$.

---

# Hints

> [!note]- Hint 1
> For $i$: $|i| = 1$, $\operatorname{Arg}(i) = \pi/2$ (it's on the upper imaginary axis, in $(-\pi, \pi)$). So $\operatorname{Log}(i) = \log 1 + i\pi/2 = i\pi/2$.

> [!note]- Hint 2
> $-1$ is on the slit (negative real axis), so principal branch undefined. Use a branch with $\operatorname{Arg} \in (0, 2\pi)$ (slit along positive real axis instead). Then $\operatorname{Arg}(-1) = \pi$, giving $\log(-1) = i\pi$.

---

# Solution

**(a) $\log(-1)$.**

The principal branch $\operatorname{Log}$ is defined on $\mathbb{C} \setminus (-\infty, 0]$. The point $z = -1$ is in the *removed* set $(-\infty, 0]$, so $\operatorname{Log}(-1)$ is *undefined* on the principal branch.

To define $\log(-1)$, switch to a branch with a different slit. For instance, slit along the positive imaginary axis: the domain $\mathbb{C} \setminus \{it : t \geq 0\}$ is simply connected and avoids $0$, so by [[Thm - Existence of a Logarithm on Simply Connected Domains]], a branch exists. With argument in $(\pi/2 - 2\pi, \pi/2)$ (say), the argument of $-1$ is $-\pi$, giving $\log(-1) = \log 1 + i(-\pi) = -i\pi$ on this branch.

Alternatively, slit along positive real axis: $\mathbb{C} \setminus [0, \infty)$, argument in $(0, 2\pi)$. Then $\operatorname{Arg}(-1) = \pi$, so $\log(-1) = i\pi$ on this branch.

**(b) $\operatorname{Log}(i)$ and $\operatorname{Log}(-i)$.**

$|i| = 1$, $\operatorname{Arg}(i) = \pi/2$ (upper imaginary axis, in $(-\pi, \pi)$). So
$$\operatorname{Log}(i) = \log 1 + i\pi/2 = i\pi/2.$$

$|-i| = 1$, $\operatorname{Arg}(-i) = -\pi/2$ (lower imaginary axis, in $(-\pi, \pi)$). So
$$\operatorname{Log}(-i) = \log 1 + i(-\pi/2) = -i\pi/2.$$

**(c) Full sets across branches.**

For any $w \in \mathbb{C}^\times$, the set of all logarithms is $\{\log w_0 + 2\pi i k : k \in \mathbb{Z}\}$ where $\log w_0$ is any one fixed value.

$$\log(-1) \in \{i\pi + 2\pi i k : k \in \mathbb{Z}\} = \{\ldots, -3i\pi, -i\pi, i\pi, 3i\pi, 5i\pi, \ldots\}.$$
$$\log(i) \in \{i\pi/2 + 2\pi i k\} = \{\ldots, -3i\pi/2, i\pi/2, 5i\pi/2, \ldots\}.$$
$$\log(-i) \in \{-i\pi/2 + 2\pi i k\} = \{\ldots, -5i\pi/2, -i\pi/2, 3i\pi/2, \ldots\}.$$

> [!note]- Complete formal solution
> **(a)** $-1 \in (-\infty, 0]$, the cut of the principal branch, so $\operatorname{Log}(-1)$ is undefined. On a branch defined by slitting along $[0, \infty)$ with argument in $(0, 2\pi)$, $\operatorname{Arg}(-1) = \pi$ and $\log(-1) = i\pi$.
>
> **(b)** $\operatorname{Log}(i) = i\pi/2$, $\operatorname{Log}(-i) = -i\pi/2$.
>
> **(c)** The full sets are obtained by adding $2\pi i k, k \in \mathbb{Z}$ to any one value of the logarithm. $\blacksquare$

---

# Key Takeaways

**The principal branch is undefined exactly on its cut.**

When evaluating $\log z$ for $z$ on the negative real axis, the principal branch fails — and this is by design. The cut is a discontinuity locus: $\operatorname{Log}$ has values approaching $+i\pi$ from above and $-i\pi$ from below at points on the negative real axis. The jump $2\pi i$ is the periodicity of $\exp$ made visible. To define $\log$ at a point on the cut, one must use a *different* branch with a different cut.

**Multivaluedness is parameterized by integers.**

The set of logarithms of any fixed $w \neq 0$ is $\log w_0 + 2\pi i \mathbb{Z}$ — countably infinite, with integer parameter. Each branch picks out one value; tracing around a loop around $0$ shifts the value by $2\pi i$. The integer parameter is the *winding number* of the loop, and this is the entry point to the topological theory of branched covers.

**Choose the right branch for the problem.**

In computations, the freedom to choose any branch is a feature: pick the branch whose cut avoids the relevant contour. For a contour integral that goes around $0$, no single branch can be defined on the whole contour — branch cuts are unavoidable, and the *jump* of $\log$ across the cut becomes part of the answer (the "keyhole contour" technique in [[Complex Analysis III — Winding, Laurent, Residues|CA III]]).
