---
type: definition
subject: complex-analysis
prereqs:
  - "Def - Branch of the Logarithm"
  - "Def - Complex Exponential and Trigonometric Functions"
tags: [analysis, complex-analysis]
---

# Notation

$z \in \mathbb{C}^\times$, $\alpha \in \mathbb{C}$ — the base and exponent. $z^\alpha$ — the complex power. $\operatorname{Log}$ — the principal branch of the logarithm, defined on the slit plane $\mathbb{C} \setminus (-\infty, 0]$. Full registry on [[Complex Analysis I — Basic Notions]].

---

# Axiom Motivation

For positive real $x$ and real $\alpha$, the power $x^\alpha$ has a clean definition: $x^\alpha = e^{\alpha \log x}$, where $\log$ is the real logarithm. The exponent rule $x^{\alpha + \beta} = x^\alpha x^\beta$ follows from the exponent rule for $e$. This definition is canonical because $\log x$ is single-valued for $x > 0$.

In the complex setting, the same formula $z^\alpha = \exp(\alpha \log z)$ is the natural extension — but now $\log z$ is *multivalued*, and so $z^\alpha$ inherits the multivaluedness. Different branches of $\log$ produce different values of $z^\alpha$, differing by factors of $\exp(\alpha \cdot 2\pi i k) = e^{2\pi i \alpha k}$ for $k \in \mathbb{Z}$.

The cases divide into three:

(1) **$\alpha$ an integer.** Then $e^{2\pi i \alpha k} = 1$ for every $k$, so all branches give the *same* value: $z^\alpha$ is single-valued. This recovers the standard integer power: $z^2$, $z^{-1}$, etc.

(2) **$\alpha$ rational, $\alpha = p/q$ in lowest terms.** Then $e^{2\pi i \alpha k} = e^{2\pi i p k/q}$ takes exactly $q$ distinct values as $k$ varies, so $z^{p/q}$ has exactly $q$ values. For $\alpha = 1/n$, these are the $n$ $n$-th roots of $z$ — exactly the multivaluedness we expect from "the $n$-th root function".

(3) **$\alpha$ irrational or non-real.** Then $e^{2\pi i \alpha k}$ takes infinitely many distinct values as $k \in \mathbb{Z}$, so $z^\alpha$ is *infinitely* multivalued. This is the maximally complicated case.

The choice of *principal branch* — defining $z^\alpha := \exp(\alpha \operatorname{Log} z)$ on the slit plane — singles out one value, the most natural one when the base is positive real (and where the principal branch agrees with the real $\log$). This makes $z^\alpha$ a single-valued holomorphic function on the slit plane, with the price that it does *not* satisfy $(zw)^\alpha = z^\alpha w^\alpha$ in general — the latter identity fails by a phase factor depending on the arguments.

Why this is worth the trouble: complex powers are essential to evaluate real integrals like $\int_0^\infty x^{\alpha-1}/(1 + x)\,dx$ via contour integration — the contour goes around a branch cut for $z^{\alpha-1}$, and the *jump* of $z^{\alpha-1}$ across the cut produces the answer. Without complex powers, this family of integrals (which includes the gamma function's Mellin transform representations) is much harder.

A subtlety: when $\alpha$ is a positive integer, the definition via $\exp(\alpha \operatorname{Log} z)$ agrees with the standard $z \cdot z \cdots z$ ($\alpha$ times), but the latter is defined for all $z \in \mathbb{C}$ including $z = 0$, while the former requires $z \neq 0$. We extend $z^\alpha$ to $z = 0$ by continuity when possible: $0^\alpha = 0$ for $\operatorname{Re}(\alpha) > 0$, undefined for $\operatorname{Re}(\alpha) \leq 0$.

---

# The Definition

**Complex power.** For $z \in \mathbb{C}^\times$ and $\alpha \in \mathbb{C}$, using the principal branch $\operatorname{Log}$ on the slit plane $\mathbb{C} \setminus (-\infty, 0]$:
$$z^\alpha := \exp(\alpha \operatorname{Log} z), \qquad z \in \mathbb{C} \setminus (-\infty, 0].$$

This defines a single-valued, holomorphic function $z \mapsto z^\alpha$ on the slit plane.

**On a general branch.** For a general branch $\lambda$ of $\log$ defined on an open $U \subseteq \mathbb{C}^\times$, define
$$z^\alpha := \exp(\alpha \lambda(z)), \qquad z \in U.$$
Different branches give values differing by factors $e^{2\pi i \alpha k}$, $k \in \mathbb{Z}$. We say $z^\alpha$ is **multivalued**: the set of all possible values is $\{\exp(\alpha(\operatorname{Log} z + 2\pi i k)) : k \in \mathbb{Z}\}$.

**Derivative.** On any branch where $z^\alpha$ is defined: $(d/dz) z^\alpha = \alpha z^{\alpha-1}$ — same as the real formula, computed via the chain rule.

**Special cases.**
- For $\alpha = n \in \mathbb{Z}$: $z^n$ is single-valued on all of $\mathbb{C}^\times$ (extends to $\mathbb{C}$ for $n \geq 0$, to $\mathbb{C}^\times$ for $n < 0$), and agrees with the standard integer power.
- For $\alpha = 1/n$ with $n \in \mathbb{Z}_{> 0}$: $z^{1/n}$ takes $n$ values (the $n$ $n$-th roots of $z$), and the principal branch picks one of them.
- For general $\alpha$: multivalued with values differing by factors of $e^{2\pi i \alpha}$.

---

# Relate to Other Fields / Compression

In **algebraic geometry**, the multivaluedness of $z^{1/n}$ corresponds to the *covering* $\mathbb{C}^\times \to \mathbb{C}^\times$ given by $w \mapsto w^n$, which is an $n$-sheeted covering branched over $0$. The Riemann surface of $z^{1/n}$ has $n$ sheets glued along the branch cut.

In **probability**, the **gamma function** $\Gamma(\alpha) = \int_0^\infty x^{\alpha - 1} e^{-x}\,dx$ uses real powers of positive reals — single-valued. Its complex extension via contour integration uses complex powers and branch cuts. The same machinery underlies the beta function and the Mellin transform.

In **number theory**, the Riemann zeta function $\zeta(s) = \sum n^{-s}$ uses complex powers $n^{-s} = \exp(-s \log n)$. Since $n > 0$ is a positive real, $\log n$ is single-valued, so $n^{-s}$ is unambiguous — but on the complex plane $s \in \mathbb{C}$, the function inherits the complex-analytic structure.

---

# Examples / Corollaries

**Is an instance — $i^i$.** Using the principal branch: $\operatorname{Log}(i) = i\pi/2$, so $i^i = \exp(i \cdot i\pi/2) = \exp(-\pi/2) \approx 0.208$. A real number! On other branches, $i^i = \exp(i \cdot (i\pi/2 + 2\pi i k)) = \exp(-\pi/2 - 2\pi k)$, giving infinitely many real values.

**Is an instance — $\sqrt z$ on the slit plane.** $z^{1/2} = \exp(\operatorname{Log}(z)/2) = \sqrt{|z|} \exp(i\operatorname{Arg}(z)/2)$. So $\sqrt 4 = 2$ (positive), $\sqrt{-4}$ undefined on the slit plane (boundary of domain), $\sqrt i = \exp(i\pi/4) = (1 + i)/\sqrt 2$.

**Is an instance — $z^2 = z \cdot z$.** For $\alpha = 2$, $z^2 = \exp(2\operatorname{Log} z) = \exp(\operatorname{Log}(z^2)) = z^2$ (the standard square). Multivaluedness vanishes for integer exponents.

**Is NOT an instance — the exponent rule $(zw)^\alpha = z^\alpha w^\alpha$ in general.** Take $z = w = -1$ on the *boundary* of the principal branch's domain (both are not in the slit plane, so the principal value is not defined; but using a branch slit along the positive real axis with $\operatorname{Arg} \in (0, 2\pi)$): $\operatorname{Log}(-1) = i\pi$, so $(-1)^{1/2} = \exp(i\pi/2) = i$. Then $((-1)(-1))^{1/2} = 1^{1/2} = 1$ (principal), but $(-1)^{1/2} \cdot (-1)^{1/2} = i \cdot i = -1$. The identity fails by a factor of $-1$. The general rule: $(zw)^\alpha = z^\alpha w^\alpha \cdot e^{2\pi i \alpha k}$ for some $k \in \mathbb{Z}$ depending on arguments.

**Is NOT an instance — $z^\alpha$ at $z = 0$ for $\operatorname{Re}(\alpha) \leq 0$.** $0^0$ is conventionally $1$ in some contexts but is genuinely indeterminate; $0^{-1}$ is undefined (division by zero); $0^i$ would be $\exp(i \cdot (-\infty)) = \exp$ of an undefined quantity. The origin is excluded from the natural domain.

**Corollary — for positive real $x > 0$, $x^\alpha$ on the principal branch agrees with the real power.** Since $\operatorname{Log}(x) = \log x$ for $x > 0$, $x^\alpha = \exp(\alpha \log x)$, which is the standard real definition.

**Corollary — periodicity in the exponent.** $z^{\alpha + 2\pi i / \operatorname{Log}(z)} = z^\alpha$ on each branch — though the formula is awkward because the period depends on $z$.

**Calibration check.** Compute $(-1)^{1/3}$ on the principal branch: $\operatorname{Log}(-1)$ is undefined on the slit plane (boundary), so we must use a different branch. On a branch with $\operatorname{Arg}(-1) = \pi$ (slit along positive real axis): $(-1)^{1/3} = \exp(i\pi/3) = (1 + i\sqrt 3)/2$, the principal cube root. The other cube roots are $-1$ and $\exp(-i\pi/3)$, obtained from other branches.

---

# Unlocked by This

> [!tip] Contour Integration with Branch Cuts *(from CA III/IV)*
> Real integrals like $\int_0^\infty x^{\alpha-1}/(1 + x)\,dx = \pi/\sin(\pi\alpha)$ are evaluated by integrating $z^{\alpha-1}/(1 + z)$ around a **keyhole contour** that wraps around the positive real axis branch cut. The jump of $z^{\alpha-1}$ across the cut is the key.

> [!tip] Riemann Surfaces of $z^{1/n}$ *(from Complex Geometry)*
> The function $z^{1/n}$ has $n$ values for each $z \neq 0$. Its **Riemann surface** is $n$ copies of the slit plane glued together along the cut — the multivaluedness becomes single-valued on the surface.

> [!tip] Mellin Transform *(from Harmonic Analysis)*
> The Mellin transform $\tilde f(s) = \int_0^\infty x^{s - 1} f(x)\,dx$ uses complex powers of positive reals; it is the multiplicative analogue of the Fourier transform.
