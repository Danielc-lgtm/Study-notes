---
type: definition
subject: geometric-mechanics
prereqs:
  - "Def - Symplectic Manifold"
  - "Def - Hamiltonian Vector Field"
  - "Def - The Smooth Functions Ring"
tags: [physics, geometric-mechanics, symplectic-geometry, lie-algebra]
---

# Notation

$(M, \omega)$ is a symplectic manifold. For $f \in C^\infty(M)$, $X_f$ is its [[Def - Hamiltonian Vector Field|Hamiltonian vector field]] defined by $\iota_{X_f}\omega = df$. The **Poisson bracket** is the bilinear operation $\{\cdot, \cdot\} : C^\infty(M) \times C^\infty(M) \to C^\infty(M)$ defined below. In canonical coordinates $(q^i, p_i)$, we use $\partial_{q^i}f := \partial f/\partial q^i$ and $\partial_{p_i}f := \partial f/\partial p_i$.

---

# Axiom Motivation

We have a symplectic manifold with its assignment $H \mapsto X_H$ converting energy functions into vector fields. We have Hamiltonian flows preserving the symplectic form. We have the central computation $df/dt = X_H(f)$ giving the time-derivative of an observable $f$ along the flow of $H$. The question is: **is there an intrinsic algebraic structure on the space of observables $C^\infty(M)$ that encodes Hamiltonian dynamics?**

Begin with the time-evolution computation. For a function $f$ on phase space, evolving under the Hamiltonian flow of $H$, the time derivative is

$$\frac{df}{dt} = X_H(f) = \omega(X_H, X_f) \cdot \text{(some sign convention)}.$$

The right-hand side $\omega(X_H, X_f)$ is **antisymmetric in $H$ and $f$**. So define $\{f, H\} := \omega(X_f, X_H) = X_f(H) = -X_H(f)$ (with our sign convention; conventions vary). Then $df/dt = -\{H, f\} = \{f, H\}$. The Poisson bracket is born from the structure of time evolution: **the derivative of $f$ along the flow of $H$ is $\{f, H\}$**.

Now ask: what axiomatic properties should $\{\cdot, \cdot\}$ have? Three are forced.

**Bilinearity:** time evolution is linear in the energy, so $\{f, H_1 + H_2\} = \{f, H_1\} + \{f, H_2\}$, and the derivative of $f$ is linear in $f$, so $\{f_1 + f_2, H\} = \{f_1, H\} + \{f_2, H\}$. Both linearities are evident from $\{f, g\} = \omega(X_f, X_g)$ and the linearity of $f \mapsto X_f$ and of $\omega$.

**Antisymmetry:** $\omega$ is antisymmetric, so $\{f, g\} = \omega(X_f, X_g) = -\omega(X_g, X_f) = -\{g, f\}$. This is automatic from the definition.

**Leibniz rule** (also called the **derivation property**): $\{f, gh\} = \{f, g\}h + g\{f, h\}$. This says the Poisson bracket "differentiates" its second argument like a derivation. The reason is that $\{f, gh\} = X_f(gh) = X_f(g)h + g X_f(h) = \{f, g\}h + g\{f, h\}$ — it's just the Leibniz rule for the vector field $X_f$ acting on the product $gh$. Combined with antisymmetry, this means **the Poisson bracket is a derivation in both arguments**: it makes $C^\infty(M)$ into something stronger than just a Lie algebra — a **Poisson algebra** (a commutative algebra with a Lie-algebra structure compatible with the product via Leibniz).

**Jacobi identity:** $\{f, \{g, h\}\} + \{g, \{h, f\}\} + \{h, \{f, g\}\} = 0$. This is *not* automatic from the previous axioms; it is a consequence of $d\omega = 0$. In fact, **the Jacobi identity for $\{\cdot, \cdot\}$ is equivalent to the closedness of $\omega$** — a remarkable algebraic-to-geometric translation. Without Jacobi, $(C^\infty(M), \{\cdot, \cdot\})$ would fail to be a Lie algebra, and the Poisson-bracket calculus would break down. With Jacobi, we have a full **Poisson algebra** structure on $C^\infty(M)$, and quantization (the operator algebra of quantum mechanics) becomes the deformation of this Poisson algebra.

The combination of these four axioms — bilinearity, antisymmetry, Leibniz, Jacobi — defines what is called a **Poisson algebra** structure on the algebra of observables, abstracting the symplectic origin.

Why do we want the Lie algebra structure? Several reasons. First, conservation laws: $f$ is conserved by the flow of $H$ iff $\{f, H\} = 0$, and the Jacobi identity lets us derive new conservation laws from old ones ($\{f, H\} = \{g, H\} = 0$ implies $\{\{f, g\}, H\} = 0$). Second, the Lie algebra structure on $C^\infty(M)$ is the **classical limit** of the operator algebra structure on quantum observables ($[\hat A, \hat B]/i\hbar \to \{A, B\}$ in the $\hbar \to 0$ limit) — this is the foundational link between classical and quantum mechanics. Third, the map $f \mapsto X_f$ becomes a Lie algebra homomorphism into $\Gamma(TM)$ (with Lie bracket of vector fields), embedding the algebra of observables inside the algebra of symmetries.

What if we *drop* the Jacobi identity, keeping only antisymmetry and Leibniz? We get a **near-Poisson** structure, also known as a **Loday bracket** or **Leibniz algebra**. These exist and are interesting, but they fail to support the standard machinery of conservation laws and quantization. Jacobi is what makes the structure "physical".

What if we *strengthen* by demanding $\{f, g\}$ depends only on the algebraic structure of the ring $C^\infty(M)$, not on the symplectic form? Then we're asking for a **biderivation** of the commutative algebra $C^\infty(M)$, and there are many such derivations — every Poisson bracket is one, parametrized by a Poisson bivector $\pi \in \Gamma(\Lambda^2 TM)$. Symplectic Poisson brackets are exactly the **nondegenerate** ones; **Poisson manifolds** (with possibly degenerate $\pi$) generalize the symplectic case and arise naturally in symmetry reduction (the dual of a Lie algebra, $\mathfrak{g}^*$, has a canonical degenerate Poisson structure).

In summary: bilinearity, antisymmetry, and Leibniz follow algebraically from $\{f, g\} = \omega(X_f, X_g)$ and the basic properties of $\omega$. Jacobi follows from the closedness $d\omega = 0$. The full four-axiom package makes $C^\infty(M)$ a Poisson algebra, which is the right algebraic structure for classical mechanics and the bridge to quantum mechanics.

---

# The Definition

Let $(M, \omega)$ be a symplectic manifold. The **Poisson bracket** is the bilinear operation $\{\cdot, \cdot\} : C^\infty(M) \times C^\infty(M) \to C^\infty(M)$ defined by

$$\{f, g\} := \omega(X_f, X_g) = X_f(g) = -X_g(f),$$

where $X_f$ is the [[Def - Hamiltonian Vector Field|Hamiltonian vector field]] of $f$, satisfying $\iota_{X_f}\omega = df$.

The three equivalent expressions are reconciled as follows:
$\omega(X_f, X_g) = (\iota_{X_f}\omega)(X_g) = df(X_g) = X_g(f) = -X_f(g) \cdot (-1) = X_f(g) \cdot (-1) \cdot (-1)$ — depending on sign convention; with the convention used here (Frankel/Marsden), $\{f, g\} = X_f(g)$.

In canonical (Darboux) coordinates $(q^i, p_i)$ on $T^*Q$ in which $\omega = \sum_i dp_i \wedge dq^i$:

$$\{f, g\} = \sum_i \left( \frac{\partial f}{\partial q^i}\frac{\partial g}{\partial p_i} - \frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q^i}\right).$$

**Fundamental brackets:** $\{q^i, q^j\} = 0$, $\{p_i, p_j\} = 0$, $\{q^i, p_j\} = \delta^i_j$ (Kronecker delta). These are the classical analogues of the quantum canonical commutation relations $[\hat q^i, \hat p_j] = i\hbar\delta^i_j$.

**Properties** (proved in [[Thm - Poisson Bracket is a Lie Algebra Structure on Smooth Functions]]):
1. **Bilinearity:** $\{af + bg, h\} = a\{f, h\} + b\{g, h\}$ for $a, b \in \mathbb{R}$.
2. **Antisymmetry:** $\{f, g\} = -\{g, f\}$.
3. **Leibniz rule:** $\{f, gh\} = \{f, g\}h + g\{f, h\}$.
4. **Jacobi identity:** $\{f, \{g, h\}\} + \{g, \{h, f\}\} + \{h, \{f, g\}\} = 0$.

The four together make $(C^\infty(M), \{\cdot, \cdot\}, \cdot)$ a **Poisson algebra**: a commutative associative algebra equipped with a Lie bracket compatible with the product via Leibniz. In particular, $(C^\infty(M), \{\cdot, \cdot\})$ is an (infinite-dimensional, real) Lie algebra.

A function $C \in C^\infty(M)$ is a **Casimir** if $\{C, f\} = 0$ for every $f \in C^\infty(M)$; on a symplectic manifold (with nondegenerate $\omega$), the only Casimirs are the locally constant functions, but on more general Poisson manifolds nontrivial Casimirs exist.

---

# Categorical / Structural Definition

The Poisson bracket on $C^\infty(M)$ is the algebraic structure of a **Poisson algebra**: an associative, commutative $\mathbb{R}$-algebra $A$ equipped with a Lie bracket $\{\cdot, \cdot\} : A \times A \to A$ such that $\{f, \cdot\}$ is a derivation of the algebra structure for every $f \in A$ (the Leibniz rule). This is the structure that abstracts the algebraic content of classical mechanics, separating from the geometric content (which is the symplectic manifold).

**Universal property:** the Poisson algebra of a symplectic manifold is the **algebra of observables**, and any "reasonable" assignment of an algebra of observables to a phase space is a Poisson algebra. The reverse construction — going from an abstract Poisson algebra to a geometric "symplectic" object — is the program of **Poisson geometry**: every Poisson algebra arises as the algebra of functions on a **Poisson manifold** (a smooth manifold with a Poisson bivector $\pi \in \Gamma(\Lambda^2 TM)$ satisfying $[\pi, \pi]_{SN} = 0$ in the Schouten bracket, the Jacobi-identity condition).

In categorical terms: the assignment $(M, \omega) \rightsquigarrow (C^\infty(M), \cdot, \{\cdot, \cdot\})$ is a contravariant functor from the category of symplectic manifolds (with symplectomorphisms) to the category of Poisson algebras (with Poisson algebra homomorphisms). The image is contained in the subcategory of **symplectic Poisson algebras** — those whose underlying Poisson bivector is nondegenerate.

The **deformation quantization program** (Bayen–Flato–Fronsdal–Lichnerowicz–Sternheimer, completed by Kontsevich) shows that every Poisson algebra admits a formal deformation $(A[[\hbar]], *_\hbar)$ — the **star product** — whose leading-order term in $\hbar$ is the commutative product and whose first $\hbar$-correction is $\{\cdot, \cdot\}/2$. This is the structural reason quantum mechanics is "the deformation of classical mechanics": the Poisson algebra is the classical limit of the operator algebra.

---

# Relate to Other Fields / Compression

The Poisson bracket is the **classical limit of the quantum commutator**. In quantum mechanics, observables are operators on a Hilbert space, and the algebraic structure of observables is the **commutator** $[\hat A, \hat B] = \hat A \hat B - \hat B \hat A$. The dynamics is governed by Heisenberg's equation $d\hat A/dt = [\hat A, \hat H]/i\hbar$. In the classical limit $\hbar \to 0$, the commutator (divided by $i\hbar$) converges to the Poisson bracket: $[\hat A, \hat B]/i\hbar \to \{A, B\}$. So Heisenberg's equation classicalizes to $df/dt = \{f, H\}$ — the Hamiltonian time-evolution equation. The fundamental brackets $\{q^i, p_j\} = \delta^i_j$ are the classicalization of the canonical commutation relations $[\hat q^i, \hat p_j] = i\hbar\delta^i_j$.

From the Lie algebra perspective, the Poisson bracket makes $C^\infty(M)$ into a (very large) Lie algebra, and many finite-dimensional Lie algebras embed inside as Poisson subalgebras. For example, on $T^*\mathbb{R}^3$ the angular momentum components $L^i = \epsilon^{ijk}q^j p_k$ satisfy $\{L^i, L^j\} = \epsilon^{ijk}L^k$ — the Lie algebra $\mathfrak{so}(3)$. This is the classical-mechanical realization of $\mathfrak{so}(3)$, which becomes (after quantization) the quantum angular momentum algebra of $\mathfrak{su}(2)$ representations.

**True name:** the true name of the Poisson bracket is **"infinitesimal canonical transformation generated by $f$, evaluated on $g$"** — operationally, $\{f, g\}$ is the rate of change of $g$ under the Hamiltonian flow of $f$. Symmetrically, it is also the rate of change of $-f$ under the flow of $g$. The definition $\{f, g\} = \omega(X_f, X_g)$ makes this manifest: it is the symplectic-form pairing of the two vector fields generated by $f$ and $g$.

---

# Examples / Corollaries

**Fundamental brackets on $T^*\mathbb{R}^n$.** With $\omega = \sum_i dp_i \wedge dq^i$:
- $\{q^i, q^j\} = 0$ (positions Poisson-commute)
- $\{p_i, p_j\} = 0$ (momenta Poisson-commute)
- $\{q^i, p_j\} = \delta^i_j$ (canonical conjugate pair)

These three formulas, by Leibniz and bilinearity, determine the Poisson bracket of any polynomial functions on phase space.

**Time evolution.** For any $f \in C^\infty(M)$ and Hamiltonian $H$, the time derivative of $f$ along the Hamiltonian flow of $H$ is
$$\frac{df}{dt} = X_H(f) = \{f, H\}.$$
**Energy conservation** is the special case $f = H$: $dH/dt = \{H, H\} = -\{H, H\} = 0$ by antisymmetry.

**Conservation laws.** $f$ is a constant of motion (conserved along the flow of $H$) iff $\{f, H\} = 0$. So conservation laws are exactly the functions that Poisson-commute with the Hamiltonian.

**Angular momentum on $T^*\mathbb{R}^3$.** Define $L^i = \epsilon^{ijk}q^j p_k$ for $i = 1, 2, 3$. Then:
- $\{L^i, L^j\} = \epsilon^{ijk}L^k$ — the angular momentum components form $\mathfrak{so}(3)$.
- $\{L^2, L^i\} = 0$ where $L^2 = \sum_i (L^i)^2$ — $L^2$ is a Casimir of the angular-momentum subalgebra.

This is computed in [[Ex - Poisson Bracket of Angular Momentum Components]].

**Harmonic oscillator constants.** For $H = \tfrac{1}{2}(p^2 + q^2)$ on $T^*\mathbb{R}$, the only conserved quantities (functions $f$ with $\{f, H\} = 0$) on the level sets of $H$ are functions of $H$ itself. So the harmonic oscillator has *one* independent constant of motion (the energy), and is integrable with action $I = \tfrac{1}{2}(q^2 + p^2)$ and angle $\theta = \arctan(p/q)$.

**Is NOT an instance: a bracket that fails Leibniz.** Consider the bilinear, antisymmetric "bracket" $\{f, g\}_? := f - g$ on $C^\infty(M)$. This satisfies bilinearity and antisymmetry but fails Leibniz: $\{f, gh\}_? = f - gh$ versus $\{f, g\}_?h + g\{f, h\}_? = (f-g)h + g(f-h) = fh + gf - 2gh$ — not equal in general. So this is *not* a Poisson bracket.

**Is NOT an instance: a bracket on a manifold without symplectic structure that doesn't satisfy Jacobi.** Take $M = \mathbb{R}^3$ and try $\{f, g\}_? := (\partial_x f)(\partial_y g) - (\partial_y f)(\partial_x g)$ (only using $x, y$, not $z$). This is bilinear, antisymmetric, Leibniz — but the Jacobi identity needs to be checked. It actually does hold here (this is the Poisson bracket coming from the *degenerate* $2$-form $dx \wedge dy$ on $\mathbb{R}^3$, with $z$ as a Casimir), so this is a Poisson structure but not a symplectic one. The Jacobi identity is the subtle one — antisymmetric Leibniz operations that fail Jacobi are common in the wild.

**Corollary (Jacobi for conservation laws).** If $\{f, H\} = 0$ and $\{g, H\} = 0$, then by Jacobi $\{\{f, g\}, H\} + \{\{g, H\}, f\} + \{\{H, f\}, g\} = 0$, and the last two terms vanish, so $\{\{f, g\}, H\} = 0$. **The Poisson bracket of two conserved quantities is conserved.** This is the cheapest way to discover new conservation laws from old ones, and it is why the conserved quantities of a system form a Lie subalgebra of $C^\infty(M)$.

**Corollary (involution).** Two functions $f, g$ are **in involution** if $\{f, g\} = 0$. By Leibniz, the involutive subalgebra (functions Poisson-commuting with a fixed $H$, for instance) is closed under products and under Poisson brackets with each other (by Jacobi). For an integrable system, the maximal involutive subalgebras have dimension $n$ (= half the dimension of phase space), and a maximal involutive family $\{f_1 = H, f_2, \dots, f_n\}$ gives action-angle coordinates by [[Thm - Liouville's Theorem on Phase Space Volume|Arnold–Liouville]].

**Corollary (Hamiltonian vector field commutator).** $[X_f, X_g] = -X_{\{f, g\}}$ (with our sign convention). The map $f \mapsto X_f$ is a Lie algebra anti-homomorphism (or homomorphism, with opposite convention) from $(C^\infty(M), \{\cdot,\cdot\})$ to $(\Gamma(TM), [\cdot, \cdot])$.

**Calibration check.** If you can do these three things, you have understood the definition. First, compute $\{q^1 + p_2, q^2 - p_1\}$ on $T^*\mathbb{R}^2$ from the coordinate formula and the fundamental brackets. Second, verify directly (without using Jacobi as a black box) that $\{q^1, \{q^2, p_2\}\} + \{q^2, \{p_2, q^1\}\} + \{p_2, \{q^1, q^2\}\} = 0$ on $T^*\mathbb{R}^2$. Third, show that for $H = \tfrac{1}{2}(p^2 + q^2)$ on $T^*\mathbb{R}$, the function $q^2 + p^2$ is conserved (compute $\{q^2 + p^2, H\}$).

---

# Unlocked by This

> [!tip] Deformation Quantization and Star Products *(from Mathematical Physics)*
> **Deformation quantization** (Bayen–Flato–Fronsdal–Lichnerowicz–Sternheimer, 1978; Kontsevich, 1997) constructs an associative product $*_\hbar$ on the formal power series $C^\infty(M)[[\hbar]]$ such that $f *_\hbar g = fg + (i\hbar/2)\{f, g\} + O(\hbar^2)$, deforming the commutative pointwise product into a noncommutative one whose commutator recovers (up to $i\hbar$) the Poisson bracket. **Kontsevich's formality theorem** says such star products exist on any Poisson manifold and are unique up to equivalence. This is the mathematical realization of "quantization as deformation of the classical algebra of observables", an alternative to the more direct geometric quantization that always produces a Hilbert space.

> [!tip] Casimirs and Symplectic Leaves *(from Poisson Geometry)*
> On a general (degenerate) **Poisson manifold**, the **Casimir functions** $C$ — those with $\{C, f\} = 0$ for all $f$ — generate the radical of the Poisson structure. The level sets of all Casimirs together foliate the manifold into **symplectic leaves**: lower-dimensional submanifolds on which the Poisson structure restricts to a (nondegenerate) symplectic structure. The Poisson manifold $\mathfrak{g}^*$ (dual of a Lie algebra, with the Kirillov–Kostant–Souriau Poisson structure) has symplectic leaves the **coadjoint orbits**, which carry canonical $G$-invariant symplectic structures and play a central role in the orbit method of representation theory.

> [!tip] Noether's Theorem in Symplectic Form *(from Hamiltonian Group Actions)*
> When a Lie group $G$ acts on $(M, \omega)$ preserving $\omega$ and a $G$-invariant Hamiltonian $H$, the **moment map** $\mu : M \to \mathfrak{g}^*$ produces $\dim G$ conserved quantities: for each $\xi \in \mathfrak{g}$, the function $\mu^\xi := \langle \mu, \xi\rangle$ satisfies $\{\mu^\xi, H\} = 0$. Moreover, the assignment $\xi \mapsto \mu^\xi$ is a Lie algebra homomorphism $\mathfrak{g} \to (C^\infty(M), \{\cdot,\cdot\})$. This is the precise symplectic-geometric statement of **Noether's theorem**: continuous symmetries produce conserved quantities, and the conserved quantities themselves form a Lie algebra realizing $\mathfrak{g}$ inside the Poisson algebra of observables.
