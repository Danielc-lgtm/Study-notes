---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Simply Connected Domain in Complex Analysis"
  - "Def - Conformal Map"
  - "Thm - Conformal Automorphisms of the Unit Disc"
tags: [analysis, complex-analysis]
---

# Notation

$U \subseteq \mathbb{C}$ is a nonempty, simply connected, proper open subset (proper means $U \neq \mathbb{C}$). $\mathbb{D} = \{z : |z| < 1\}$. A **biholomorphism** $U \to \mathbb{D}$ is a holomorphic bijection with holomorphic inverse. Full registry on [[Complex Analysis IV — Mapping Theory and Applications]].

---

# Motivation

The **Riemann mapping theorem** is one of the deepest classical theorems in complex analysis. It says: every simply connected, proper open subset of $\mathbb{C}$ is biholomorphically equivalent to the unit disc. So all such domains — circles, ellipses, polygons, even fractal-boundary shapes — are *the same* from the point of view of complex analysis.

This is a complete *classification* of planar simply connected domains up to biholomorphism. There is only one such domain (modulo biholomorphism), and it can be chosen to be $\mathbb{D}$. The exceptional case $\mathbb{C}$ itself is excluded (a biholomorphism $\mathbb{C} \to \mathbb{D}$ would be a bounded entire function, hence constant by Liouville).

The theorem unifies an enormous amount of geometry. Solving a problem on a complicated domain can be done by conformally mapping to $\mathbb{D}$, solving there, and pulling back. This works for Dirichlet problems, Neumann problems, certain spectral problems, and many others.

This topic states the theorem *without proof*. The full proof is involved, requiring normal families (Montel's theorem), an extremization argument (maximizing $|f'(z_0)|$ over injective holomorphic $f : U \to \mathbb{D}$), and Hurwitz's theorem to ensure the extremizer is injective. The proof is presented in detail in graduate complex analysis (e.g., Stein's book).

---

# Sources and Targets

**Sources (Input Broadening)**

**Simply connected, proper open subset of $\mathbb{C}$.** The standard hypothesis. Common examples:
- Discs and ellipses (convex domains).
- Polygons (simply connected by visual inspection).
- Slit planes $\mathbb{C}\setminus L$ for $L$ a ray.
- Wedges (sectors) of $\mathbb{C}$.

**A domain visibly homeomorphic to a disc.** Bridge: homeomorphic-to-a-disc and topologically simply connected are equivalent for open planar domains; Riemann mapping gives biholomorphism.

**Targets (Output Amplification)**

Combine with **the Poisson integral formula.** Property $D$: have a biholomorphism $\phi : U \to \mathbb{D}$. Amplified result $E$: solve the Dirichlet problem on $U$ by pulling back the Poisson solution on $\mathbb{D}$ via $\phi$.

Combine with **uniqueness.** Property $D$: two biholomorphisms $\phi_1, \phi_2 : U \to \mathbb{D}$. Amplified result $E$: they differ by an element of $\operatorname{Aut}(\mathbb{D})$ (a 3-parameter family). Specifically, $\phi_2 = T \circ \phi_1$ for some $T \in \operatorname{Aut}(\mathbb{D})$.

Combine with **boundary behaviour (Carathéodory).** Property $D$: $U$ has a Jordan curve boundary. Amplified result $E$: the biholomorphism extends continuously (in fact homeomorphically) to the closed sets — **Carathéodory's extension theorem**.

---

# Why Is It True

The intuition: simply connected proper open subsets of $\mathbb{C}$ all "look the same" topologically (homeomorphic to a disc, with $\pi_1 = 0$), and holomorphic structure is supposed to be "fine enough" to distinguish only the simply-connected-or-not (and excluded $\mathbb{C}$ case) at the planar level.

More concretely: the *Schwarz lemma*-style extremization argument. Among all injective holomorphic $f : U \to \mathbb{D}$ with $f(z_0) = 0$ (for a fixed $z_0 \in U$), choose the one maximizing $|f'(z_0)|$ (a real number bounded above by the universal Schwarz bound). Show this extremal $f$ is surjective: if it missed any $w_0 \in \mathbb{D}$, one could construct an $\tilde f$ with $|\tilde f'(z_0)| > |f'(z_0)|$, contradicting extremality. The construction of $\tilde f$ uses square roots and Blaschke factors — exactly the operations that simple-connectedness of $U$ allows (square root exists when $U$ is simply connected and avoids $0$).

The whole proof can be summarized: *simply connected* + *proper* are exactly the conditions needed to construct the extremal map and to verify its surjectivity. Without simple-connectedness, square roots wouldn't exist globally; without properness, the extremization would be vacuous.

---

# What Makes This Hard

The non-obvious step is the **construction of the extremal map and the proof of its surjectivity via the "missing-value" argument**. The whole proof rests on (a) Montel's theorem for compactness of the family, (b) Hurwitz's theorem for injectivity preservation, (c) the square-root construction for the missing-value step. Each is a separate substantial result.

The reason the proof is omitted in IB: it requires Montel's theorem and the extensive theory of normal families, which is a substantial chapter in itself.

---

# Rederivation Scaffold

**High-level strategy:**
Among injective holomorphic $f : U \to \mathbb{D}$ with $f(z_0) = 0$, maximize $|f'(z_0)|$ using normal families (Montel). Show the maximizer is surjective by the missing-value argument: if it missed $w_0$, construct $\tilde f$ with larger $|\tilde f'(z_0)|$, contradicting extremality.

**Subgoal decomposition:**

1. **The family $\mathcal{F} = \{f : U \to \mathbb{D} \text{ injective holomorphic}, f(z_0) = 0\}$ is nonempty.** Construct one explicit member, using square roots on a simply connected $U$ that avoids some point.

2. **$\mathcal{F}$ is a normal family (Montel).** Uniformly bounded by $1$ ⟹ normal.

3. **Maximize $|f'(z_0)|$.** Take a sequence with $|f_n'(z_0)| \to \sup$; extract a locally uniformly convergent subsequence; limit is in $\mathcal{F}$ (using Hurwitz for injectivity preservation).

4. **The maximizer $f$ is surjective.** Suppose not, $f(U) \subsetneq \mathbb{D}$ with $w_0 \in \mathbb{D}\setminus f(U)$. Construct $\tilde f$ with $|\tilde f'(z_0)| > |f'(z_0)|$ using square root of a Blaschke composition.

5. **Conclusion.** $f$ is a biholomorphism $U \to \mathbb{D}$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The family is nonempty
> **Statement:** For simply connected proper $U \subset \mathbb{C}$ and $z_0 \in U$, there exists an injective holomorphic $f : U \to \mathbb{D}$ with $f(z_0) = 0$.
>
> **Hint:** Pick a point $w_0 \notin U$. On simply connected $U$ avoiding $w_0$, $\log(z - w_0)$ has a branch. Use this to construct a square-root-based injection into a half-plane, then into $\mathbb{D}$.
>
> *Proof: see Stein's Complex Analysis Ch. 8 or any graduate text.*

> [!note]- Lemma 2: Montel's theorem
> **Statement:** A uniformly bounded family of holomorphic functions on a domain is a normal family — every sequence has a locally uniformly convergent subsequence.
>
> *Standard; proved by Arzelà–Ascoli applied to the uniformly bounded holomorphic functions (which are uniformly equicontinuous on compact subsets by the Cauchy integral formula).*

> [!note]- Lemma 3: Missing-value construction
> **Statement:** If $f : U \to \mathbb{D}$ is injective holomorphic with $f(z_0) = 0$ and $f(U) \subsetneq \mathbb{D}$, then there exists $\tilde f : U \to \mathbb{D}$ injective holomorphic with $\tilde f(z_0) = 0$ and $|\tilde f'(z_0)| > |f'(z_0)|$.
>
> **Hint:** Pick $w_0 \in \mathbb{D}\setminus f(U)$. Compose with Blaschke to move $w_0$ to $0$; take square root (possible because the composition is nonvanishing on simply connected $U$); compose with another Blaschke. Compute the derivative at $z_0$.

---

# Formal Proof

> [!note]- Statement only (proof omitted)
> 
> **Theorem (Riemann Mapping).** Let $U \subseteq \mathbb{C}$ be a nonempty, simply connected, proper open subset. Then there exists a biholomorphism $\phi : U \to \mathbb{D}$.
>
> **Uniqueness.** Two biholomorphisms $U \to \mathbb{D}$ differ by an element of $\operatorname{Aut}(\mathbb{D})$: $\phi_2 = T \circ \phi_1$ for some $T \in \operatorname{Aut}(\mathbb{D})$. Fixing the value at one point $z_0 \in U$ (say $\phi(z_0) = 0$) and the direction of $\phi'(z_0)$ (say $\phi'(z_0) > 0$, real and positive) uniquely determines $\phi$.
>
> *The proof uses normal families (Montel's theorem), Hurwitz's theorem, and the missing-value construction described above. See Stein's Complex Analysis Chapter 8 for a complete proof.*

---

# Cross-Field Exercise Suggestions

**Construct an explicit map.** For specific domains (half-planes, wedges, strips, slit planes), construct the Riemann map explicitly using compositions of standard maps:
- Upper half-plane to disc: $z \mapsto (z - i)/(z + i)$.
- Wedge $\{0 < \arg z < \alpha\}$ to upper half-plane: $z \mapsto z^{\pi/\alpha}$ (using a branch).
- Strip to disc: composition $z \mapsto e^z$ then $z \mapsto (z - i)/(z + i)$.

**Dirichlet problem on a polygon.** Apply Riemann mapping (here, the Schwarz–Christoffel formula gives the explicit map) to transfer the Dirichlet problem from the polygon to the upper half-plane, solve there, pull back.

**Modulus of an annulus.** Annuli are *not* simply connected, so the Riemann mapping doesn't apply. Instead, two annuli are biholomorphic iff they have the same **modulus** (ratio of radii). This is the simplest example of a *conformal modulus* — a moduli space invariant.

---

# Bridges

- **[[Def - Simply Connected Domain in Complex Analysis]]** — the hypothesis.

- **[[Def - Conformal Map]]** — the kind of map being constructed.

- **[[Thm - Conformal Automorphisms of the Unit Disc]]** — describes the uniqueness up to automorphism.

- **[[Thm - Hurwitz's Theorem]]** — used in the proof to preserve injectivity under limits.

- **[[Thm - Schwarz Lemma]]** — provides the extremization framework.

---

# Unlocked by This

> [!tip] Uniformization Theorem *(from Riemann Surfaces)*
> The **uniformization theorem** generalizes Riemann mapping: every simply connected Riemann surface is biholomorphic to $\hat{\mathbb{C}}$, $\mathbb{C}$, or $\mathbb{D}$. This trichotomy is the foundation of Riemann surface theory.

> [!tip] Schwarz–Christoffel Mapping *(from Applied Math)*
> The [[Ex - Schwarz–Christoffel for a polygon|Schwarz–Christoffel formula]] gives explicit Riemann maps from the upper half-plane to polygons, with applications to potential theory, fluid flow, and electrostatics.

> [!tip] Solving PDEs by Conformal Pullback *(from Applied Math)*
> Riemann mapping reduces boundary value problems on complicated domains to ones on $\mathbb{D}$. See [[Ex - Solving Dirichlet on a half-plane via conformal mapping]].
