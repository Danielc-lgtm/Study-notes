---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Complex Exponential and Trigonometric Functions"
  - "Thm - Power Series is Holomorphic with Termwise Derivative"
  - "Thm - Constant on a Domain if Derivative is Zero"
tags: [analysis, complex-analysis]
---

# Notation

$\exp(z) = \sum_{n=0}^\infty z^n/n!$ — the complex exponential. We write $e^z$ for $\exp(z)$. $\mathbb{C}^\times = \mathbb{C} \setminus \{0\}$. Full registry on [[Complex Analysis I — Basic Notions]].

---

# Statement

> **Theorem (properties of the complex exponential).** Let $\exp(z) = \sum_{n=0}^\infty z^n/n!$, defined by its power series (which has radius of convergence $\infty$). Then:
>
> 1. **(Holomorphicity and derivative.)** $\exp$ is entire and $\exp'(z) = \exp(z)$ for all $z \in \mathbb{C}$.
> 2. **(Addition formula.)** $\exp(z + w) = \exp(z) \exp(w)$ for all $z, w \in \mathbb{C}$.
> 3. **(Non-vanishing.)** $\exp(z) \neq 0$ for every $z \in \mathbb{C}$, and $\exp(z) \exp(-z) = 1$.
> 4. **(Periodicity.)** $\exp(z + 2\pi i) = \exp(z)$ for all $z \in \mathbb{C}$, and $\exp(z) = 1$ if and only if $z \in 2\pi i \mathbb{Z}$.
> 5. **(Surjectivity onto $\mathbb{C}^\times$.)** For every $w \in \mathbb{C}^\times = \mathbb{C} \setminus \{0\}$, there exists $z \in \mathbb{C}$ with $\exp(z) = w$; the set of such pre-images is $\{z_0 + 2\pi i k : k \in \mathbb{Z}\}$ for any single pre-image $z_0$.

---

# Motivation

The complex exponential, defined by its power series $\sum z^n/n!$, is the single most important entire function. The "properties" theorem packages the algebraic and analytic identities of $\exp$ — addition formula, derivative formula, non-vanishing, periodicity, surjectivity onto $\mathbb{C}^\times$ — into a single statement. From these, *everything* about complex exponentials, trigonometric identities, the logarithm and its branches, and the complex powers $z^\alpha$ follows.

The motivation for proving these via complex methods (rather than from Euler's formula plus real-variable identities) is twofold. First, the proofs are cleaner and more general — the addition formula $\exp(z + w) = \exp(z) \exp(w)$ holds for all complex $z, w$, not just real. Second, the methodology generalizes: the use of [[Thm - Constant on a Domain if Derivative is Zero]] to upgrade identities from one point to the whole plane is a model technique for many complex-analytic identities.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's hypothesis is just "the definition $\exp(z) = \sum z^n/n!$".

The first disguised source is **the power series with radius $\infty$**: any function defined by such a series is entire and the theorem's techniques apply. Used to derive properties of $\sin, \cos$ analogously.

The second disguised source is **the differential equation $f' = f$ with $f(0) = 1$**: uniquely characterizes $\exp$ (by the constancy-from-zero-derivative argument). So any function satisfying this DE *is* $\exp$.

**Targets (Output Amplification)**

The conclusions are: (i) $\exp$ is entire with $\exp' = \exp$; (ii) addition formula; (iii) non-vanishing; (iv) periodicity $2\pi i$; (v) surjectivity onto $\mathbb{C}^\times$.

Combine **addition formula with Euler's formula.** Property $D$: $\exp(iy) = \cos y + i \sin y$. The amplified result: the addition formulas for $\sin, \cos$ as the real and imaginary parts of $\exp(i(\theta + \phi)) = \exp(i\theta)\exp(i\phi)$. See [[Ex - Euler's formula and trigonometric identities]].

Combine **non-vanishing with the existence of branches of $\log$.** Property $D$: $\exp(z) \neq 0$ for all $z$. The amplified result: $\exp$ is a covering map $\mathbb{C} \to \mathbb{C}^\times$, hence has local inverses (branches of $\log$) on every simply connected subdomain of $\mathbb{C}^\times$.

Combine **periodicity with the structure of pre-images.** Property $D$: $\exp(z) = w \neq 0$. The amplified result: the full set of pre-images is $\{z + 2\pi i k : k \in \mathbb{Z}\}$ — a uniformly spaced lattice. This periodic structure is what makes $\log$ multivalued.

---

# Why Is It True

**(i) Entire with $\exp' = \exp$.** Direct from termwise differentiation: $\exp'(z) = \sum n z^{n-1}/n! = \sum z^{n-1}/(n-1)! = \exp(z)$. The series has radius $\infty$, so this is valid everywhere.

**(ii) Addition formula.** The slick proof uses constancy. Fix $w \in \mathbb{C}$ and define $F(z) := \exp(z + w) \exp(-z)$. By the product rule and chain rule:
$$F'(z) = \exp(z + w)\exp(-z) + \exp(z + w)(-\exp(-z)) = 0.$$
So $F$ is constant by [[Thm - Constant on a Domain if Derivative is Zero]] on the connected $\mathbb{C}$. Evaluating at $z = 0$: $F(0) = \exp(w) \cdot 1 = \exp(w)$. So $F(z) = \exp(w)$ for all $z$, i.e., $\exp(z + w) \exp(-z) = \exp(w)$. Equivalently, $\exp(z + w) = \exp(z) \exp(w)$ (multiplying both sides by $\exp(z)$, which is *nonzero* — see below — but this can be arranged by computing $\exp(z) \exp(-z) = \exp(0) = 1$ first).

**(iii) Non-vanishing.** From (ii) with $w = -z$: $\exp(z)\exp(-z) = \exp(0) = 1$. So $\exp(z) \neq 0$ (else the product is $0$).

**(iv) Periodicity.** By (ii), $\exp(z + 2\pi i) = \exp(z) \exp(2\pi i)$. Compute $\exp(2\pi i) = \cos(2\pi) + i\sin(2\pi) = 1$ (using Euler's formula, which follows from the series definition by separating real and imaginary parts of $\exp(iy)$). So $\exp(z + 2\pi i) = \exp(z)$. Furthermore, the set $\{z : \exp(z) = 1\}$ equals $2\pi i \mathbb{Z}$: $\exp(z) = 1$ means $e^x(\cos y + i \sin y) = 1$, which forces $e^x = 1$ (so $x = 0$) and $\cos y = 1, \sin y = 0$ (so $y \in 2\pi\mathbb{Z}$). Combined: $z \in 2\pi i \mathbb{Z}$.

**(v) Surjective onto $\mathbb{C}^\times$.** For $w = re^{i\theta} \in \mathbb{C}^\times$ with $r > 0$ and $\theta \in \mathbb{R}$, take $z = \log r + i\theta$ (real $\log$). Then $\exp(z) = e^{\log r}(\cos\theta + i\sin\theta) = r e^{i\theta} = w$.

The deep observation: (ii) is the *key* identity, from which (iii), (iv) all follow algebraically; and the proof of (ii) via the constancy argument is the model use of [[Thm - Constant on a Domain if Derivative is Zero]] to lift a single-point identity to a global one.

---

# What Makes This Hard

The non-obvious step is the *constancy proof* of the addition formula. The naive approach — multiply two power series and verify coefficients — works but is tedious. The slick proof defines an auxiliary function $F(z) = \exp(z + w)\exp(-z)$ whose derivative is zero, deducing constancy from the connectedness of $\mathbb{C}$. This trick — "differentiate an algebraic expression, show the derivative vanishes, evaluate at a convenient point" — is the model for many functional-identity proofs.

---

# Rederivation Scaffold

**High-level strategy:**
$\exp' = \exp$ from termwise differentiation. Addition formula from the constancy argument with $F(z) = \exp(z + w)\exp(-z)$. Non-vanishing from $\exp(z)\exp(-z) = 1$. Periodicity from Euler's formula and the addition formula. Surjectivity from the polar decomposition.

**Subgoal decomposition:**

1. **$\exp' = \exp$.** Termwise differentiation of the power series.

2. **Addition formula.** Define $F(z) = \exp(z + w)\exp(-z)$, show $F'(z) = 0$, conclude $F$ constant, evaluate at $z = 0$.

3. **Non-vanishing.** $\exp(z)\exp(-z) = \exp(0) = 1 \neq 0$.

4. **Periodicity.** Use the addition formula with $w = 2\pi i$ and $\exp(2\pi i) = 1$ (Euler).

5. **Surjectivity onto $\mathbb{C}^\times$.** For $w = re^{i\theta}$ with $r > 0$, take $z = \log r + i\theta$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Derivative formula
> **Statement:** $\exp'(z) = \exp(z)$ for all $z \in \mathbb{C}$.
>
> **Hint:** Termwise differentiation of $\sum z^n/n!$.
>
> > [!note]- Full proof
> > $\exp'(z) = \sum_{n=1}^\infty n z^{n-1}/n! = \sum_{n=1}^\infty z^{n-1}/(n-1)! = \sum_{k=0}^\infty z^k/k! = \exp(z)$ (set $k = n - 1$). Termwise differentiation legitimate inside the disc of convergence, which is all of $\mathbb{C}$. $\blacksquare$

> [!note]- Lemma 2: Addition formula
> **Statement:** $\exp(z + w) = \exp(z)\exp(w)$ for all $z, w \in \mathbb{C}$.
>
> **Hint:** Show $F(z) := \exp(z + w)\exp(-z)$ has $F' \equiv 0$; conclude $F$ constant.
>
> > [!note]- Full proof
> > Fix $w \in \mathbb{C}$. Define $F : \mathbb{C} \to \mathbb{C}$ by $F(z) = \exp(z + w)\exp(-z)$. By product rule and Lemma 1:
> > $$F'(z) = \exp(z + w)\exp(-z) + \exp(z + w)\cdot(-\exp(-z)) = 0.$$
> > By [[Thm - Constant on a Domain if Derivative is Zero]] on the connected domain $\mathbb{C}$, $F$ is constant. Evaluating at $z = 0$: $F(0) = \exp(w) \cdot \exp(0) = \exp(w) \cdot 1 = \exp(w)$. So $F(z) = \exp(w)$ for all $z$, i.e.,
> > $$\exp(z + w) \exp(-z) = \exp(w). \quad (*)$$
> > Apply (*) with $w$ replaced by $-z$: $\exp(0)\exp(-z) = \exp(-z)$, so $\exp(z)\exp(-z) = \exp(0)\cdot 1 = 1$. Multiply (*) by $\exp(z)$: $\exp(z + w) \cdot 1 = \exp(z) \exp(w)$. $\blacksquare$

> [!note]- Lemma 3: Non-vanishing and periodicity
> **Statement:** $\exp(z) \neq 0$ for all $z$, and $\exp(z + 2\pi i) = \exp(z)$. Moreover $\exp(z) = 1 \Leftrightarrow z \in 2\pi i\mathbb{Z}$.
>
> > [!note]- Full proof
> > Non-vanishing: from Lemma 2, $\exp(z)\exp(-z) = \exp(0) = 1$. If $\exp(z) = 0$, the product is $0$, not $1$ — contradiction.
> >
> > Periodicity: by Lemma 2, $\exp(z + 2\pi i) = \exp(z)\exp(2\pi i)$. By **Euler's formula** (separating real and imaginary parts of $\exp(iy)$ in the series): $\exp(2\pi i) = \cos(2\pi) + i\sin(2\pi) = 1 + 0 = 1$. So $\exp(z + 2\pi i) = \exp(z)$.
> >
> > Characterization of $\exp^{-1}(1)$: write $z = x + iy$. Then $\exp(z) = e^x(\cos y + i\sin y)$. Set equal to $1$: separate real and imaginary parts give $e^x\cos y = 1, e^x\sin y = 0$. The second forces $\sin y = 0$, i.e., $y = k\pi$, $k \in \mathbb{Z}$. Then $\cos y = \pm 1$, so $e^x = \pm 1$. Since $e^x > 0$, must have $\cos y = 1$, so $y = 2k\pi$, and $e^x = 1$, so $x = 0$. Hence $z = 2k\pi i$. $\blacksquare$

> [!note]- Lemma 4: Surjectivity onto $\mathbb{C}^\times$
> **Statement:** For every $w \in \mathbb{C}^\times$, there exists $z \in \mathbb{C}$ with $\exp(z) = w$.
>
> > [!note]- Full proof
> > Write $w$ in polar form: $w = re^{i\theta}$ with $r = |w| > 0$ and $\theta \in \mathbb{R}$. Define $z = \log r + i\theta$ (real natural logarithm of $r$ exists since $r > 0$). Then by Lemma 2 and Euler:
> > $$\exp(z) = \exp(\log r)\exp(i\theta) = r(\cos\theta + i\sin\theta) = re^{i\theta} = w. \quad \blacksquare$$

---

# Formal Proof

> [!note]- Complete formal proof
> Combine Lemmas 1, 2, 3, 4 in order. Each is proved by direct computation or by the constancy argument. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Matrix exponential.** Define $\exp(A) = \sum A^n/n!$ for a square matrix $A$. The same series argument gives $\exp(0) = I$ and the derivative formula $(d/dt)\exp(tA) = A\exp(tA)$. The addition formula $\exp(A + B) = \exp(A)\exp(B)$ holds *only if $A, B$ commute* (the non-commutativity breaks the naive proof). This is the foundation of the Lie group exponential.

**Cumulants from logarithm of MGF.** In probability, the moment generating function $M(t) = E[e^{tX}]$ is related to cumulants via $\log M(t) = \sum k_n t^n/n!$. The addition formula $\exp(z + w) = \exp(z)\exp(w)$ underlies the additivity of cumulants under independent sums.

**Stone–von Neumann.** In quantum mechanics, the canonical commutation relation $[\hat x, \hat p] = i\hbar$ exponentiates to the Weyl form $e^{i\alpha\hat x}e^{i\beta\hat p} = e^{i\alpha\beta\hbar}e^{i\beta\hat p}e^{i\alpha\hat x}$ — a *projective* version of the addition formula. Stone–von Neumann uniquely classifies the irreducible unitary representations.

---

# Bridges

- **[[Def - Complex Exponential and Trigonometric Functions]]** — the source definition.

- **[[Thm - Constant on a Domain if Derivative is Zero]]** — the key tool in proving the addition formula.

- **[[Def - Branch of the Logarithm]]** — the surjectivity and non-vanishing of $\exp$ are what make logarithms well-defined (up to branch choice) on $\mathbb{C}^\times$.

- **[[Thm - Existence of a Logarithm on Simply Connected Domains]]** — uses the periodicity to characterize where branches of $\log$ exist.
