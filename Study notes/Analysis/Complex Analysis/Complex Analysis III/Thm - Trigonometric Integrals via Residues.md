---
type: theorem
subject: complex-analysis
prereqs:
  - "Thm - Residue Theorem"
  - "Thm - Computing Residues"
tags: [analysis, complex-analysis]
---

# Notation

$R(\cos\theta, \sin\theta)$ is a rational function of $\cos\theta$ and $\sin\theta$ (i.e., a quotient of polynomial expressions in these two variables). The substitution $z = e^{i\theta}$, so $dz = iz\,d\theta$, $\cos\theta = (z + 1/z)/2$, $\sin\theta = (z - 1/z)/(2i)$. Full registry on [[Complex Analysis III — Winding, Laurent, Residues]].

---

# Statement

> **Theorem (Trigonometric Integrals via Residues).** Let $R(x, y)$ be a rational function of two variables, and suppose $R(\cos\theta, \sin\theta)$ has no singularities for $\theta \in \mathbb{R}$ (equivalently, the associated rational function $\tilde R$ below has no poles on $|z| = 1$). Then
> $$\int_0^{2\pi} R(\cos\theta, \sin\theta)\,d\theta = 2\pi i \sum_{|w| < 1}\operatorname{Res}_w \tilde R(z), \qquad \tilde R(z) := \frac{1}{iz}\, R\!\left(\frac{z + z^{-1}}{2},\, \frac{z - z^{-1}}{2i}\right),$$
> the sum being over all poles of $\tilde R$ inside the open unit disc.

---

# Motivation

Trigonometric integrals $\int_0^{2\pi} R(\cos\theta, \sin\theta)\,d\theta$ — over a full period — have a natural complex-analytic reformulation. The unit circle $z = e^{i\theta}$ parametrizes $[0, 2\pi)$, and on it, $\cos\theta$ and $\sin\theta$ become rational functions of $z$. The integral $\int_0^{2\pi}\ldots d\theta$ becomes a contour integral $\oint_{|z|=1}\ldots dz$, and the residue theorem evaluates it in terms of the poles inside the unit disc.

This technique handles a broad class of integrals — anything of the form $\int_0^{2\pi} R(\cos\theta, \sin\theta)\,d\theta$ with $R$ rational and having no poles on the unit circle. Classical examples include $\int_0^{2\pi} d\theta/(a + b\cos\theta)$, $\int_0^{2\pi}\cos(n\theta) d\theta/(a + b\cos\theta)$, and various weighted trigonometric averages.

The conceptual point: the unit circle is the natural domain for periodic functions, and the residue calculus on the unit disc is the natural tool for integrals over it. This is one of the cleanest applications of the residue theorem, with no "side integral to bound" — the contour is just the unit circle, traversed once.

---

# Sources and Targets

**Sources (Input Broadening)**

**$\int_0^{2\pi} R(\cos\theta, \sin\theta)\,d\theta$ with $R$ rational, no poles on $|z| = 1$.** Direct application.

**Integrals with $\cos(n\theta), \sin(n\theta)$.** Write $\cos(n\theta) = (z^n + z^{-n})/2$, $\sin(n\theta) = (z^n - z^{-n})/(2i)$ after substitution. Resulting integrand is still rational in $z$.

**Integrals with absolute values.** $|\cos\theta|, |\sin\theta|$ are not analytic, so direct substitution fails. However, integrals like $\int_0^{2\pi}|\cos\theta|^p\,d\theta$ can sometimes be reduced via symmetries.

**Targets (Output Amplification)**

The integral evaluates as $2\pi i \sum_{|w| < 1}\operatorname{Res}_w\tilde R(z)$ where $\tilde R(z)$ is the converted integrand.

Combine with **Cauchy's integral formula.** Property $D$: if $\tilde R$ can be written as $g(z)/z$ for a $g$ holomorphic on $\overline{\mathbb{D}}$, then by CIF $\oint \tilde R = 2\pi i g(0)$.

Combine with **partial fraction decomposition.** For $R$ a rational function of $\cos\theta$, the substitution often yields $\tilde R(z) = P(z)/(Q(z)\cdot z)$ — partial fractions then separate the contribution of each pole.

---

# Why Is It True

The substitution $z = e^{i\theta}$ is a parametrization of the unit circle: as $\theta$ ranges from $0$ to $2\pi$, $z$ traces the unit circle once counterclockwise. We have $dz/d\theta = ie^{i\theta} = iz$, so $d\theta = dz/(iz)$. The trigonometric functions become rational in $z$ on the unit circle: $\cos\theta = \operatorname{Re}(e^{i\theta}) = (z + \bar z)/2 = (z + 1/z)/2$ (using $|z| = 1 \Rightarrow \bar z = 1/z$), and similarly $\sin\theta = (z - 1/z)/(2i)$.

Substituting:
$$\int_0^{2\pi} R(\cos\theta, \sin\theta)\,d\theta = \oint_{|z|=1} R\left(\frac{z + z^{-1}}{2}, \frac{z - z^{-1}}{2i}\right)\cdot\frac{dz}{iz}.$$
The integrand is rational in $z$, and its poles are the roots of the denominator (after clearing the $1/z$ factors). The poles inside the unit disc contribute residues; poles on the unit circle would invalidate the substitution, hence the hypothesis "$R$ has no poles on $|z| = 1$".

By the residue theorem,
$$\int_0^{2\pi} R(\cos\theta, \sin\theta)\,d\theta = 2\pi i \sum_{|w| < 1}\operatorname{Res}_w\tilde R(z), \quad\text{where } \tilde R(z) = \frac{1}{iz} R\left(\frac{z + z^{-1}}{2}, \frac{z - z^{-1}}{2i}\right).$$

The conceptual point: *periodic integrals are unit-circle integrals*. The complex unit circle is the natural complexification of the real interval $[0, 2\pi]$ with periodic boundary, and the residue theorem evaluates contour integrals on it.

---

# What Makes This Hard

The non-obvious step is **the substitution $z = e^{i\theta}$ and the careful conversion of $\cos\theta, \sin\theta, d\theta$**. The substitution is mechanical but the resulting expression often needs to be simplified — clearing the $1/z$ factors, identifying poles inside the disc, and computing residues. A common error is to mishandle the $1/z$ from $d\theta = dz/(iz)$ — this introduces an automatic simple pole at $z = 0$ which must be included in the residue sum.

---

# Rederivation Scaffold

**High-level strategy:**
Substitute $z = e^{i\theta}$, converting the trigonometric integral to a contour integral on the unit circle. The integrand becomes rational in $z$. Identify poles inside the unit disc and apply the residue theorem.

**Subgoal decomposition:**

1. **Substitute.** $z = e^{i\theta}$, $d\theta = dz/(iz)$, $\cos\theta = (z + z^{-1})/2$, $\sin\theta = (z - z^{-1})/(2i)$.

2. **Simplify.** Combine into $\tilde R(z) = (1/(iz)) R((z + z^{-1})/2, (z - z^{-1})/(2i))$. Clear the $z^{-1}$ factors to get a rational function in $z$ (with $z$ in the denominator from the $1/z$).

3. **Identify poles inside $|z| = 1$.** Solve the equation "denominator of $\tilde R = 0$" with $|w| < 1$.

4. **Compute residues at each pole.** Use the standard formulas.

5. **Apply the residue theorem.** $\int_0^{2\pi} R\,d\theta = 2\pi i \sum \operatorname{Res}$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $R(\cos\theta, \sin\theta)$ be a rational function with no poles on $|z| = 1$. Substitute $z = e^{i\theta}$:
> - $\cos\theta = (z + 1/z)/2$
> - $\sin\theta = (z - 1/z)/(2i)$
> - $d\theta = dz/(iz)$
>
> The integrand transforms:
> $$\int_0^{2\pi} R(\cos\theta, \sin\theta)\,d\theta = \oint_{|z|=1} R\left(\frac{z + z^{-1}}{2}, \frac{z - z^{-1}}{2i}\right)\cdot\frac{dz}{iz}.$$
>
> Denote $\tilde R(z) := \frac{1}{iz} R\left(\frac{z + z^{-1}}{2}, \frac{z - z^{-1}}{2i}\right)$. After clearing denominators, $\tilde R$ is a rational function of $z$ (typically with poles at $z = 0$ from the $1/z$, plus any other poles from $R$).
>
> The unit circle is a closed contour, traversed counterclockwise, so by the [[Thm - Residue Theorem|residue theorem]],
> $$\oint_{|z|=1}\tilde R(z)\,dz = 2\pi i \sum_{|w| < 1}\operatorname{Res}_w \tilde R.$$
>
> Therefore,
> $$\int_0^{2\pi} R(\cos\theta, \sin\theta)\,d\theta = 2\pi i \sum_{|w| < 1}\operatorname{Res}_w \tilde R. \quad\blacksquare$$

---

# Cross-Field Exercise Suggestions

**$\int_0^{2\pi} d\theta/(a + b\cos\theta) = 2\pi/\sqrt{a^2 - b^2}$ for $a > |b| > 0$.** Apply with $R = 1/(a + b\cos\theta)$. Substituting: $a + b\cos\theta = a + b(z + 1/z)/2 = (2az + b z^2 + b)/(2z)$. So $\tilde R(z) = (1/(iz)) \cdot (2z/(bz^2 + 2az + b)) = 2/(i(bz^2 + 2az + b))$. Poles: $z = (-a \pm \sqrt{a^2 - b^2})/b$, one inside the disc (the larger root, $z = (-a + \sqrt{a^2 - b^2})/b$). Residue: $2/(i \cdot 2b z_0 + 2a) = 1/(i\sqrt{a^2 - b^2})$. Integral $= 2\pi i \cdot 1/(i\sqrt{a^2 - b^2}) = 2\pi/\sqrt{a^2 - b^2}$.

**$\int_0^{2\pi} \cos(n\theta)\,d\theta/(a + b\cos\theta)$.** Variant where $\cos(n\theta) = (z^n + z^{-n})/2$ appears in the integrand. Splitting and applying the same technique.

**Generating functions of orthogonal polynomials.** The Chebyshev, Legendre, and Hermite polynomials' generating functions yield contour-integral representations via this technique, leading to many classical orthogonality and recursion relations.

---

# Bridges

- **[[Thm - Residue Theorem]]** — the engine.

- **[[Thm - Computing Residues]]** — used to compute residues at interior poles.

- **[[Thm - Real Rational Integrals via Residues]]** — a variant where the contour is real-axis-plus-semicircle, not the unit circle.

---

# Unlocked by This

> [!tip] Generating Functions and Contour Integrals *(from Combinatorics)*
> Many combinatorial identities have generating function proofs that reduce to contour integration on the unit circle, via the same substitution.
