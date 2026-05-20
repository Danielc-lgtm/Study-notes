---
type: definition
subject: complex-analysis
prereqs:
  - "Def - Power Series and Radius of Convergence"
  - "Def - Holomorphic Function"
tags: [analysis, complex-analysis]
---

# Notation

$\exp(z) = e^z$ — the complex exponential of $z \in \mathbb{C}$. $\sin z, \cos z$ — the complex sine and cosine. We use $\exp$ and $e^{(\cdot)}$ interchangeably. For real $y$, the **principal argument** $\operatorname{Arg}(z) \in (-\pi, \pi]$. Full registry on [[Complex Analysis I — Basic Notions]].

---

# Axiom Motivation

The real exponential $e^x$ is uniquely characterized by the differential equation $f' = f$ with initial condition $f(0) = 1$, and equivalently by its Taylor series $\sum x^n/n!$ which has radius of convergence $\infty$. To extend to the complex plane, the cleanest move is to *take the same series* and check that it converges for every complex $z$ — which it does, since $\limsup |1/n!|^{1/n} = 0$, giving radius $\infty$.

Defining $\exp(z)$ this way has three advantages. First, the function is automatically holomorphic on $\mathbb{C}$ (by the [[Thm - Power Series is Holomorphic with Termwise Derivative|termwise differentiation theorem]] for power series). Second, $\exp'(z) = \exp(z)$ by termwise differentiation. Third, on the real line it agrees with the familiar $e^x$, so it is genuinely an extension.

The deep payoff is **Euler's formula**: separating $\exp(iy) = \sum (iy)^n/n!$ into real and imaginary parts (the powers of $i$ cycle through $1, i, -1, -i$), one gets $\exp(iy) = \cos y + i \sin y$. This is *not* a separate axiom — it is forced by the series definition. The functions $\cos y$ and $\sin y$ that appear are exactly the real $\cos$ and $\sin$, identifiable from their Taylor series. So the complex exponential *unifies* the real exponential with the real trigonometric functions, and the seemingly separate identities $e^{x+y} = e^x e^y$ and $\cos(x + y) = \cos x \cos y - \sin x \sin y$ become *one identity*: $\exp(z + w) = \exp(z) \exp(w)$.

This naturally leads to *defining* $\sin z$ and $\cos z$ in terms of $\exp$: $\sin z = (\exp(iz) - \exp(-iz))/(2i)$ and $\cos z = (\exp(iz) + \exp(-iz))/2$. These reduce to the real $\sin, \cos$ on the real axis (by Euler's formula). They extend the trigonometric functions to the complex plane with the same algebraic identities — and reveal new behaviour: $\cos(iy) = \cosh y$ grows exponentially, so $\cos$ is *unbounded* on $\mathbb{C}$, unlike its real restriction.

Why is this the right way to define $\sin$ and $\cos$, rather than via a power series? Because the exponential definition makes the addition formulas trivial corollaries of $\exp(z+w) = \exp(z)\exp(w)$, the derivative formulas trivial corollaries of $\exp' = \exp$, and the periodicity automatic from the periodicity of $\exp(iy)$ in $y$. Anything you could prove from the power series is faster from the exponential definition. The power series for $\sin, \cos$ then drops out as a *consequence*, by expanding the exponentials.

The choice to define complex $\sin, \cos$ to *agree* with their real counterparts on $\mathbb{R}$ is the only natural one — any other definition would break the desired property that complex functions extend real ones.

---

# The Definition

**Complex exponential.** The **complex exponential** is the function $\exp : \mathbb{C} \to \mathbb{C}$ defined by the power series
$$\exp(z) := \sum_{n=0}^\infty \frac{z^n}{n!}, \qquad z \in \mathbb{C}.$$
This series has radius of convergence $\infty$, so $\exp$ is entire. We also write $e^z$ for $\exp(z)$.

**Complex sine and cosine.** Define
$$\sin z := \frac{\exp(iz) - \exp(-iz)}{2i}, \qquad \cos z := \frac{\exp(iz) + \exp(-iz)}{2}.$$
Equivalently, as power series:
$$\sin z = \sum_{n=0}^\infty (-1)^n \frac{z^{2n+1}}{(2n+1)!}, \qquad \cos z = \sum_{n=0}^\infty (-1)^n \frac{z^{2n}}{(2n)!}.$$
Both are entire.

**Euler's formula.** For all $y \in \mathbb{R}$:
$$\exp(iy) = \cos y + i \sin y.$$
This holds also for complex $z$: $\exp(iz) = \cos z + i \sin z$, by direct computation from the definitions.

**Hyperbolic functions.** $\sinh z := (\exp(z) - \exp(-z))/2$ and $\cosh z := (\exp(z) + \exp(-z))/2$. The identities $\cos(iz) = \cosh z, \sin(iz) = i \sinh z$ follow directly.

---

# Relate to Other Fields / Compression

In **Lie theory**, the complex exponential is the prototype of the **exponential map** of a Lie group. For the additive group $(\mathbb{C}, +)$, the exponential is the map $\mathbb{C} \to \mathbb{C}^\times$ given by $z \mapsto e^z$, with the addition-to-multiplication property $e^{z + w} = e^z e^w$. For matrix Lie groups, the matrix exponential $e^X = \sum X^n/n!$ plays the analogous role — it is *literally* the same series, now applied to matrices.

In **harmonic analysis**, $\exp(iy)$ for real $y$ is the **character** of the group $\mathbb{R}$ (a continuous homomorphism $\mathbb{R} \to \mathbb{T}$, the unit circle). The Fourier transform $\hat f(\xi) = \int f(x) e^{-2\pi i x \xi}\,dx$ uses these characters as a basis. Euler's formula is the bridge: it identifies trigonometric oscillations with the imaginary part of $e^{iy}$.

In **quantum mechanics**, $e^{-iHt/\hbar}$ is the time-evolution operator generated by the Hamiltonian $H$. The complex exponential is the foundation of unitary evolution, and its series definition is the foundation of perturbation theory.

In **probability**, the **characteristic function** $\varphi(t) = E[e^{itX}]$ uses the complex exponential to package the moment information of a real random variable into a complex-analytic function.

---

# Examples / Corollaries

**Is an instance — $\exp(1) = e$.** The classical $e \approx 2.718$ — by definition the value of the series at $z = 1$.

**Is an instance — $\exp(i\pi) = -1$.** Euler's identity. By the formula: $\exp(i\pi) = \cos\pi + i\sin\pi = -1 + 0 = -1$.

**Is an instance — periodicity.** $\exp(z + 2\pi i) = \exp(z) \exp(2\pi i) = \exp(z) \cdot 1 = \exp(z)$. So $\exp$ is periodic with period $2\pi i$ — a feature of the *complex* exponential entirely absent from the real one.

**Is NOT an instance of a bounded function — $\cos z$ is unbounded on $\mathbb{C}$.** Compute $\cos(iy) = (e^{-y} + e^y)/2 = \cosh y$, which grows exponentially as $y \to \infty$. So $\cos$ takes arbitrarily large values along the imaginary axis. This is the most striking feature distinguishing complex from real trigonometric functions.

**Is NOT an instance of a surjection $\mathbb{C} \to \mathbb{C}$ — $\exp$ is surjective $\mathbb{C} \to \mathbb{C}^\times$ but never hits $0$.** Since $\exp(z) \exp(-z) = 1$, $\exp(z) \neq 0$ for any $z$. The image is $\mathbb{C}^\times = \mathbb{C} \setminus \{0\}$, and surjectivity onto that follows from $\exp(\log r + i\theta) = re^{i\theta}$ hitting every nonzero point.

**Corollary — addition formulas for trig from $\exp$.** $\cos(z + w) + i \sin(z + w) = \exp(i(z+w)) = \exp(iz)\exp(iw) = (\cos z + i \sin z)(\cos w + i \sin w)$. Expanding and equating real and imaginary parts gives the classical addition formulas. See [[Ex - Euler's formula and trigonometric identities]].

**Corollary — $|\exp(iy)| = 1$ for real $y$.** From Euler, $|\exp(iy)|^2 = \cos^2 y + \sin^2 y = 1$. So the imaginary axis maps to the unit circle.

**Calibration check.** Compute $\exp(2\pi i) = 1$, $\exp(\pi i/2) = i$, $\exp(\ln 2) = 2$. Verify the de Moivre identity $(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$ as a special case of $\exp(in\theta) = (\exp(i\theta))^n$.

---

# Unlocked by This

> [!tip] Logarithm and Powers *(from this topic)*
> The exponential is the bridge to [[Def - Branch of the Logarithm|branches of $\log$]] and [[Def - Complex Power|complex powers]] $z^\alpha = \exp(\alpha \log z)$. The multivalued character of $\log$ (and of $z^\alpha$ for non-integer $\alpha$) reflects the periodicity of $\exp$.

> [!tip] Möbius Transformations and Conformal Maps *(from CA IV)*
> The conformal maps of standard regions are built from compositions of $\exp$, $\log$, $z^\alpha$, and Möbius transformations. The exponential maps strips to sectors, and the logarithm undoes this.

> [!tip] Fourier Series *(from Harmonic Analysis)*
> The functions $\{e^{inx}\}_{n \in \mathbb{Z}}$ form an orthonormal basis of $L^2([0, 2\pi])$, and Fourier series express functions as linear combinations. The complex exponential is the basis of the entire theory.
