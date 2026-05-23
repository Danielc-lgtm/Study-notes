---
type: theorem
subject: thermodynamics
prereqs:
  - "Def - Covector Field and Differential 1-Form"
  - "Def - Integrable Distribution"
  - "Thm - The Frobenius Theorem"
  - "Thm - Frobenius Theorem in Forms Language"
tags: [physics, thermodynamics, differential-geometry]
---

# Notation

$M^{n+1}$ is a smooth manifold, $\theta$ a smooth nowhere-vanishing 1-form on $M$. An **integrating factor** for $\theta$ on an open set $V$ is a smooth function $\lambda : V \to \mathbb{R}\setminus\{0\}$ such that $\theta/\lambda$ is exact on $V$, i.e., $\theta = \lambda\, df$ for some smooth $f : V \to \mathbb{R}$. See [[Thermodynamics I — Caratheodory's Approach to the Second Law]] for the full registry.

---

# Statement

> **Theorem (existence of integrating factor for a single Pfaffian).** Let $M^{n+1}$ be a smooth manifold and $\theta$ a smooth nowhere-vanishing 1-form on $M$. The following are equivalent:
>
> 1. $\theta$ satisfies the Frobenius integrability condition: $\theta \wedge d\theta = 0$ at every point of $M$.
> 2. The codimension-one distribution $\ker \theta$ is involutive.
> 3. $\ker \theta$ is integrable: $M$ is locally foliated by codimension-one submanifolds tangent to $\ker \theta$.
> 4. Locally on each sufficiently small open $V \subset M$, there exist smooth functions $\lambda : V \to \mathbb{R}\setminus\{0\}$ and $f : V \to \mathbb{R}$ with $\theta|_V = \lambda\, df$ — an integrating factor and its integral.

> **Corollary.** Under any of the equivalent conditions, the level sets of $f$ on each Frobenius chart are the local integral submanifolds of $\ker \theta$, and the integrating factor $\lambda = \theta/df$ is uniquely determined on each chart up to the substitution $(\lambda, f) \mapsto (\lambda/g'(f), g(f))$ for any smooth strictly monotone function $g$.

---

# Motivation

This is the standard reformulation of the [[Thm - The Frobenius Theorem|Frobenius theorem]] for the special case of a *single* Pfaffian equation $\theta = 0$ (rather than a system of $r$ Pfaffians). It is the most-used form of Frobenius in physics — every appearance of "integrating factor" in classical thermodynamics, mechanics, optics, and partial differential equations is an instance of this theorem.

The motivation for isolating this case is twofold. First, the codimension-one case has a particularly clean algebraic characterisation: the Frobenius obstruction reduces from a system of conditions to a single 3-form equation $\theta \wedge d\theta = 0$. This makes it computationally tractable — checking integrability is just computing a wedge product. Second, the corresponding integrating factor is a single scalar function (rather than a matrix of factors as in the general system case), making it physically interpretable as a single physical quantity (in thermodynamics: the absolute temperature; in mechanics: a conserved scalar).

The theorem is the converse-and-extension of the elementary calculus fact "$df$ is closed, so if $\omega$ is exact then $d\omega = 0$". The converse "$d\omega = 0 \Rightarrow \omega$ exact" is false in general (it holds on contractible domains by the Poincaré lemma) but the *weaker* statement "$\omega$ admits an integrating factor (i.e., $\omega/\lambda$ is exact for some $\lambda$)" is governed by the Frobenius condition. Specifically: a nowhere-vanishing 1-form $\theta$ on a manifold may not be exact, may not even be closed, but it admits a local integrating factor iff $\theta \wedge d\theta = 0$. This is a substantial weakening of exactness and a substantial strengthening of "no condition" — it is the precise integrability condition for $\theta$.

The role of this theorem in thermodynamics is to convert the Frobenius integrability of $\ker \delta Q$ (the *geometric* output of Caratheodory's principle) into the existence of *state functions* $T$ and $S$ with $\delta Q = T\, dS$ (the *algebraic* form used in computations). It is the bridge from "the adiabatic foliation exists" to "absolute temperature and entropy exist".

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "the 1-form $\theta$ satisfies $\theta \wedge d\theta = 0$ (or equivalently any of the four equivalent conditions)". Recognising when this is present is the principal skill.

The most common source is **a direct computation $\theta \wedge d\theta = 0$ in coordinates**. Given $\theta$ in local coordinates, compute $d\theta$ (the exterior derivative), wedge with $\theta$, and check if the resulting 3-form vanishes identically. For a 2-dimensional manifold this is automatic ($\theta \wedge d\theta$ is a 3-form on a 2-manifold, hence trivially zero); for higher dimensions it is a genuine algebraic condition on the coefficients of $\theta$. The bridge from a coordinate expression to the integrability conclusion is just the wedge computation.

A second source is **a physical hypothesis of "inaccessibility"** (Caratheodory's principle). This is the input to [[Thm - The Heat 1-Form is Integrable|the heat-1-form-is-integrable theorem]] and converts to $\delta Q \wedge d(\delta Q) = 0$ via the [[Thm - Caratheodory's Theorem on the Second Law|Caratheodory–Frobenius theorem]]. So Caratheodory's principle is a source for the present theorem via an intermediate step.

A third source is **the local existence of a state function with the right derivative**. If you can exhibit, on any open subset, a smooth function $f$ with $df$ proportional to $\theta$, then $\theta \wedge d\theta = (\lambda\, df) \wedge (d\lambda \wedge df) = 0$ on that subset, and by smoothness the conclusion extends globally. The bridge: any local construction of an integrating factor implies the integrability condition.

A fourth source is **the codimension-one structure with a known foliation**. If the manifold $M$ comes with a known foliation by codimension-one submanifolds and $\theta$ is a 1-form annihilating the tangent spaces of the leaves (e.g., $\theta = h \cdot dF$ where $F$ is the leaf-labelling function and $h$ is any smooth nowhere-zero function), then $\ker \theta$ coincides with the tangent distribution of the foliation, is integrable, and the integrability condition holds. The bridge converts a geometric (foliation) input to the algebraic conclusion.

**Targets (Output Amplification)**

The theorem's conclusion is "$\theta = \lambda\, df$ locally". Combining with further inputs gives stronger results.

The principal target combination is **local integrability plus a global transversal $\Rightarrow$ globally defined integrating factor and integral**. The theorem gives $\lambda, f$ locally on each Frobenius chart, but these need not agree on overlaps in a way that produces global functions. If the foliation has a global transversal $\gamma_0$ that meets every leaf exactly once, the construction "label each leaf by its parameter on $\gamma_0$" produces a globally defined $f$, and $\lambda := \theta/df$ then extends globally. The combination is nonobvious because the local theorem says nothing about global topology; the global transversal hypothesis is what makes the local-to-global passage work.

A second target combination is **local integrability plus a uniqueness convention $\Rightarrow$ canonical integrating factor**. The integrating factor $\lambda$ is non-unique: $(\lambda, f)$ and $(\lambda/g'(f), g(f))$ give the same $\theta$ for any monotone $g$. Adding a convention that pins down the freedom — for instance, "$\lambda$ must agree with the empirical temperature on a reference state" or "$f$ must equal a specified function on a reference state" — selects a unique pair. In thermodynamics this is the universality requirement that picks out the absolute temperature. The combination is nonobvious because the integrability condition gives only the *existence* of $\lambda$, not its identification with any specific physical quantity.

A third target combination is **integrability plus a second 1-form $\omega$ with $\theta \wedge \omega$ closed $\Rightarrow$ a "second integrating factor" relating $\theta$ and $\omega$**. This is the structure exploited in the construction of *higher* thermodynamic potentials: $\theta = T\, dS$ and $\omega = -p\, dV$ give $\theta + \omega = dU - $ (corrections), and the simultaneous integrability of both 1-forms enables the Legendre-transform structure of $H, F, G$. The combination is nonobvious because each integrating-factor existence is local, but combining them produces global algebraic relations among the resulting state functions.

---

# Why Is It True

The intuition is geometric: **a 1-form $\theta$ with $\theta \wedge d\theta = 0$ defines a codimension-one distribution that is locally tangent to a foliation; the leaf-labelling function is the integral $f$, and the proportionality factor between $\theta$ and $df$ is the integrating factor $\lambda$.** The bolded one-liner: **integrability of $\theta$ means $\ker \theta$ has leaves, and an integrating factor is a leaf-labelling function multiplied by a normalisation.**

In a Frobenius chart for $\ker \theta$ — local coordinates $(x^1, \ldots, x^n, y)$ in which the leaves of $\ker \theta$ are coordinate slices $y = \text{const}$ — the 1-form $\theta$ must be a scalar multiple of $dy$ (the unique 1-form, up to scaling, annihilating the $\partial_{x^i}$ directions that span $\ker \theta$). Writing $\theta = \lambda(x, y)\, dy$, we read off $f = y$ as the integral and $\lambda$ as the integrating factor. The nowhere-vanishing assumption on $\theta$ gives $\lambda \neq 0$ everywhere.

The reverse direction — that $\theta = \lambda\, df$ implies $\theta \wedge d\theta = 0$ — is an algebraic identity: $d\theta = d\lambda \wedge df + \lambda\, d^2 f = d\lambda \wedge df$ (since $d^2 = 0$), so $\theta \wedge d\theta = (\lambda\, df) \wedge (d\lambda \wedge df) = \lambda\, d\lambda \wedge df \wedge df = 0$ (since $df \wedge df = 0$). This is a one-line algebraic computation showing that integrating factors automatically satisfy the integrability condition.

The non-trivial direction is the converse — that integrability gives an integrating factor. This is the content of Frobenius's theorem, which constructs the Frobenius chart from involutivity (or equivalently $\theta \wedge d\theta = 0$). The construction is iterative: choose a transversal direction, flow vector fields tangent to $\ker \theta$ to fill out a leaf, repeat. The Frobenius coordinates emerge from this construction, and $\lambda, f$ are then read off as above.

---

# What Makes This Hard

The hardest conceptual step is the *non-uniqueness* of the integrating factor. Students often expect that $\theta = \lambda\, df$ uniquely determines $\lambda$ and $f$; in fact only the pair *up to a transformation* $(\lambda, f) \mapsto (\lambda/g'(f), g(f))$ is determined. So if you find one integrating factor, you have found infinitely many — and choosing the "right" one (in thermodynamics, the absolute temperature) requires extra physical input beyond Frobenius.

A subsidiary difficulty is the local-vs-global distinction. Frobenius gives the integrating factor and integral on each chart, but they may not patch together to global functions if the foliation has nontrivial topology (e.g., dense leaves on a torus). The theorem is honestly stated as a *local* existence result; globality requires additional hypotheses.

Mathematically the proof is direct from Frobenius, so this theorem is "easy" given Frobenius — but the work of Frobenius itself (involutivity = integrability) is the substantive part. The present theorem is its physically-interpretable shadow.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the proof from [[Thm - The Frobenius Theorem]].**

**High-level strategy:** Identify the four equivalent conditions, then prove the implications in a cycle. The non-trivial step is "involutivity ⇒ integrating-factor representation", which uses Frobenius coordinates and reads off $\theta = \lambda\, dy$.

**Subgoal decomposition:**

1. **Show condition 1 ($\theta \wedge d\theta = 0$) is equivalent to condition 2 (involutivity of $\ker \theta$).** This is the forms-language Frobenius criterion: $\theta \wedge d\theta(X, Y, Z) = 0$ unwound algebraically, using $d\theta(X, Y) = X[\theta(Y)] - Y[\theta(X)] - \theta([X, Y])$ on $X, Y \in \ker \theta$, gives $\theta([X, Y]) = 0$, i.e., $[X, Y] \in \ker \theta$.
   - *Hint:* expand $\theta \wedge d\theta(X, Y, Z)$ for $X, Y \in \ker \theta$ and $Z$ transverse; the only nonzero term is $\theta(Z)\, d\theta(X, Y)$, and vanishing forces $d\theta(X, Y) = 0$ on $\ker \theta$, equivalent by Cartan to $\theta([X, Y]) = 0$.
   - *Why needed:* converts the algebraic condition (1) to the geometric condition (2).

2. **Show condition 2 (involutivity) is equivalent to condition 3 (integrability).** This is [[Thm - The Frobenius Theorem|Frobenius's theorem]] proper: involutivity is necessary and sufficient for the existence of integral submanifolds.
   - *Hint:* Necessity (3 ⇒ 2) is the easy direction: vector fields tangent to integral submanifolds have brackets tangent to the same submanifolds. Sufficiency (2 ⇒ 3) is Frobenius's theorem, proved via the commutator-flow construction.
   - *Why needed:* this is the geometric heart of the theorem.

3. **Show condition 3 (integrability) implies condition 4 (integrating factor).** Use the Frobenius chart from condition 3: in coordinates $(x^1, \ldots, x^n, y)$ where the leaves are slices $y = \text{const}$, the form $\theta$ annihilates $\partial_{x^i}$ and hence equals $\lambda\, dy$ for some smooth $\lambda$.
   - *Hint:* expand $\theta$ in the coordinate cobasis $dx^1, \ldots, dx^n, dy$ and use the orthogonality conditions $\theta(\partial_{x^i}) = 0$ to set the $dx^i$ coefficients to zero.
   - *Why needed:* this delivers the integrating-factor representation.

4. **Show condition 4 implies condition 1.** Direct computation: if $\theta = \lambda\, df$, then $\theta \wedge d\theta = (\lambda\, df) \wedge (d\lambda \wedge df) = 0$ since $df \wedge df = 0$.
   - *Hint:* the algebraic identity $df \wedge df = 0$ kills the wedge product.
   - *Why needed:* closes the equivalence cycle.

---

# Lemma Decomposition

> [!note]- Lemma 1: $\theta \wedge d\theta = 0 \Leftrightarrow \ker \theta$ involutive
> **Statement:** Let $\theta$ be a smooth nowhere-vanishing 1-form on $M^{n+1}$. Then $\theta \wedge d\theta = 0$ at every point iff for every $X, Y \in \ker \theta$ defined locally, $[X, Y] \in \ker \theta$.
>
> **Hint:** Use the algebraic expansion $\theta \wedge d\theta(X, Y, Z) = \theta(X)\, d\theta(Y, Z) - \theta(Y)\, d\theta(X, Z) + \theta(Z)\, d\theta(X, Y)$, restricted to $X, Y \in \ker \theta$ and $Z$ a transverse complementary vector. The first two terms vanish on $\ker \theta$; the third gives $\theta(Z)\, d\theta(X, Y)$, which must be zero, forcing $d\theta(X, Y) = 0$ (since $\theta(Z) \neq 0$). Then by Cartan's invariant formula, $d\theta(X, Y) = -\theta([X, Y])$ on $\ker \theta$, giving $\theta([X, Y]) = 0$, i.e., $[X, Y] \in \ker \theta$.
>
> **Why needed:** This is the forms-language version of the Frobenius involutivity criterion for a single Pfaffian.
>
> > [!note]- Full proof
> > Let $x_0 \in M$. Choose a basis $X_1, \ldots, X_n, Z$ of $T_{x_0}M$ with $X_1, \ldots, X_n \in \ker \theta|_{x_0}$ and $\theta(Z)|_{x_0} \neq 0$. Extend to smooth local vector fields with the same property.
> >
> > Compute $\theta \wedge d\theta(X_i, X_j, Z)$ for $i \neq j$, using the formula for the wedge of forms:
> > $$\theta \wedge d\theta(X_i, X_j, Z) = \theta(X_i)\,d\theta(X_j, Z) - \theta(X_j)\,d\theta(X_i, Z) + \theta(Z)\,d\theta(X_i, X_j).$$
> > The first two terms vanish since $\theta(X_i) = \theta(X_j) = 0$, leaving $\theta(Z)\, d\theta(X_i, X_j)$.
> >
> > Now use the invariant formula $d\theta(X_i, X_j) = X_i[\theta(X_j)] - X_j[\theta(X_i)] - \theta([X_i, X_j])$ (see [[Differential Geometry VIII — Differential Forms]]). Since $\theta(X_i) = \theta(X_j) = 0$ identically, the first two terms vanish, leaving $d\theta(X_i, X_j) = -\theta([X_i, X_j])$.
> >
> > So $\theta \wedge d\theta(X_i, X_j, Z) = -\theta(Z) \cdot \theta([X_i, X_j])$. Since $\theta(Z) \neq 0$, this vanishes iff $\theta([X_i, X_j]) = 0$, iff $[X_i, X_j] \in \ker \theta$.
> >
> > For other choices of three vectors (all in $\ker \theta$, or with two transverse), the formula reduces by similar manipulations to conditions already covered or to triviality. So $\theta \wedge d\theta = 0$ at every point iff $\ker \theta$ is involutive at every point.

> [!note]- Lemma 2: Integrability $\Rightarrow$ integrating-factor representation
> **Statement:** Suppose $\ker \theta$ is integrable on an open set $V$, so there are Frobenius coordinates $(x^1, \ldots, x^n, y)$ on $V$ with leaves $y = \text{const}$. Then $\theta = \lambda(x, y)\, dy$ for some smooth nowhere-zero $\lambda$.
>
> **Hint:** Expand $\theta = a_1\, dx^1 + \cdots + a_n\, dx^n + b\, dy$ in the coordinate cobasis. The conditions $\theta(\partial_{x^i}) = 0$ (since $\partial_{x^i}$ spans $\ker \theta$) give $a_i = 0$. So $\theta = b(x, y)\, dy$, with $b \neq 0$ from nowhere-vanishing of $\theta$.
>
> **Why needed:** This is the explicit construction of the integrating factor from Frobenius coordinates.
>
> > [!note]- Full proof
> > In Frobenius coordinates, the vectors $\partial_{x^1}, \ldots, \partial_{x^n}$ span the leaves of $\ker \theta$ at every point. So $\theta(\partial_{x^i}) = 0$ for $i = 1, \ldots, n$. Writing $\theta = a_1\, dx^1 + \cdots + a_n\, dx^n + b\, dy$ and evaluating on $\partial_{x^j}$:
> > $$0 = \theta(\partial_{x^j}) = a_1\, dx^1(\partial_{x^j}) + \cdots + a_n\, dx^n(\partial_{x^j}) + b\, dy(\partial_{x^j}) = a_j.$$
> > So $a_j = 0$ for all $j = 1, \ldots, n$, and $\theta = b(x, y)\, dy$. Set $\lambda := b$ and $f := y$. Since $\theta \neq 0$ everywhere, $\lambda \neq 0$.

> [!note]- Lemma 3: Integrating-factor representation $\Rightarrow$ integrability condition
> **Statement:** If $\theta = \lambda\, df$ on an open set $V$ with $\lambda$ smooth and nowhere zero, then $\theta \wedge d\theta = 0$ on $V$.
>
> **Hint:** Direct computation: $d\theta = d(\lambda\, df) = d\lambda \wedge df + \lambda\, d^2 f = d\lambda \wedge df$, and $\theta \wedge d\theta = (\lambda\, df) \wedge (d\lambda \wedge df) = \lambda\, df \wedge d\lambda \wedge df = -\lambda\, d\lambda \wedge df \wedge df = 0$.
>
> **Why needed:** This closes the equivalence — if an integrating factor exists, the Frobenius obstruction vanishes.
>
> > [!note]- Full proof
> > Compute step by step: $d\theta = d(\lambda)\wedge df + \lambda \cdot d(df) = d\lambda \wedge df + 0 = d\lambda \wedge df$. Then
> > $$\theta \wedge d\theta = (\lambda\, df) \wedge (d\lambda \wedge df) = \lambda \, (df \wedge d\lambda) \wedge df = -\lambda\, (d\lambda \wedge df) \wedge df = -\lambda\, d\lambda \wedge (df \wedge df).$$
> > The wedge of a 1-form with itself, $df \wedge df$, is zero by the antisymmetry of the wedge product on 1-forms. So $\theta \wedge d\theta = 0$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — well-posedness.** $M$ is a smooth $(n+1)$-manifold, $\theta$ a smooth nowhere-vanishing 1-form. All four conditions are smooth-geometric properties, well-defined on any smooth manifold.
>
> **(1 ⇒ 2)** By Lemma 1, $\theta \wedge d\theta = 0$ implies $\ker \theta$ is involutive.
>
> **(2 ⇒ 3)** This is [[Thm - The Frobenius Theorem|Frobenius's theorem]]: an involutive distribution is integrable. The proof constructs the integral submanifolds as images of small discs under composite flows of vector fields tangent to $\ker \theta$, with integrability following from involutivity via the closure of brackets.
>
> **(3 ⇒ 4)** By Lemma 2, integrability provides Frobenius coordinates, and in these coordinates $\theta = \lambda\, dy$ with $\lambda$ nowhere zero. Set $f := y$.
>
> **(4 ⇒ 1)** By Lemma 3, the existence of an integrating factor implies $\theta \wedge d\theta = 0$ by direct computation.
>
> The cycle 1 ⇒ 2 ⇒ 3 ⇒ 4 ⇒ 1 shows all four conditions equivalent. The corollary on non-uniqueness of the integrating factor follows from the observation that $(\lambda, f) \mapsto (\lambda/g'(f), g(f))$ satisfies $(\lambda/g'(f)) \cdot d(g(f)) = (\lambda/g'(f)) \cdot g'(f)\, df = \lambda\, df = \theta$ for any smooth strictly monotone $g$, giving another valid integrating-factor representation.

---

# Cross-Field Exercise Suggestions

**The optical eikonal equation.** In geometrical optics in an inhomogeneous medium, the wavefronts are level surfaces of a function $\psi$ (the *eikonal*) satisfying $|\nabla \psi|^2 = n(x)^2$ (the eikonal equation, where $n$ is the refractive index). The light rays are integral curves of $\nabla \psi$. The connection to this theorem: the 1-form $\theta$ representing infinitesimal phase change is $\theta = n(x)\, ds$ along a ray, and the wavefronts are integral surfaces of $\ker \theta$. The integrating factor is $n(x)$, and the integral $f = \psi$ is the eikonal. The existence of wavefronts as level sets of a global function depends on the integrability of $\theta$ — which is automatic for static media but fails for general dispersive or time-varying media.

**Conservation laws in dynamical systems.** A vector field $X$ on a manifold $M$ admits a *conserved quantity* $f$ (a function with $X[f] = 0$) iff the 1-form $\iota_X g$ (where $g$ is some background metric) has a kernel containing $X$ that is integrable. For Hamiltonian systems this is automatic ($f = H$, the Hamiltonian); for general dynamical systems it is a non-trivial integrability question. This is the geometric reformulation of "does this ODE admit a first integral?" and lies at the foundation of the theory of completely integrable systems.

**Exact differential equations in elementary ODEs.** A first-order ODE $M(x, y)\, dx + N(x, y)\, dy = 0$ is **exact** iff $\partial M/\partial y = \partial N/\partial x$. If not, one seeks an integrating factor $\lambda(x, y)$ such that $\lambda M\, dx + \lambda N\, dy$ is exact. The existence of $\lambda$ for an arbitrary $M, N$ is governed by the integrability condition for the 1-form $\theta = M\, dx + N\, dy$ on $\mathbb{R}^2$ — which is *automatic* on a 2-manifold (every 1-form on $\mathbb{R}^2$ is integrable). For 1-forms on $\mathbb{R}^3$ the condition is non-trivial; this is why integrating factors for ODEs in 2 variables always exist but partial differential equations in 3+ variables may not admit them.

---

# Bridges

- **[[Thm - The Frobenius Theorem]]** is the general theorem on involutive distributions of any codimension. This theorem is its specialisation to codimension one (single Pfaffian), with the involutivity condition algebraically translated to $\theta \wedge d\theta = 0$ and the integrability conclusion translated to the integrating-factor representation $\theta = \lambda\, df$. The higher-codimension Frobenius theorem requires a system of Pfaffians $\theta_1, \ldots, \theta_r$ with the simultaneous integrability condition $d\theta_\alpha \wedge \theta_1 \wedge \cdots \wedge \theta_r = 0$ for each $\alpha$.

- **[[Thm - Caratheodory's Theorem on the Second Law]]** uses this theorem to extract the integrating factor and entropy from the Frobenius integrability of $\delta Q$. The chain runs: Caratheodory's principle (physical axiom) → integrability of $\ker \delta Q$ (Caratheodory–Frobenius theorem) → integrating factor and state function $\delta Q = T\, dS$ (present theorem). The present theorem is the final link, converting integrability into the algebraic form physicists use.

- **[[Thm - The Heat 1-Form is Integrable]]** is the physical application of this theorem to the heat 1-form: combining Caratheodory's theorem with the present theorem gives the integrating-factor representation of $\delta Q$, identified as absolute temperature times the differential of entropy.

- **The Poincaré lemma** ($d\omega = 0 \Rightarrow \omega = df$ locally on contractible domains). This is the *closed-form* analogue of the integrating-factor theorem. A closed 1-form $\omega$ (satisfying $d\omega = 0$) is locally exact (equal to $df$); this is the integrating-factor theorem with $\lambda = 1$. The present theorem extends the Poincaré lemma to the case where $\omega$ is not closed but $\omega \wedge d\omega = 0$ — i.e., not exact but admits an integrating factor. The Poincaré lemma is the trivial case, the present theorem is the non-trivial one. Both are theorems about converting a local cohomological obstruction (closedness, or the Frobenius obstruction) into a local exactness statement (existence of $f$, or of $\lambda$ and $f$).

---

# Unlocked by This

> [!tip] Absolute Temperature and Entropy *(from this topic)*
> The integrating-factor representation $\delta Q = T\, dS$ identifies $T$ (the integrating factor) as the absolute temperature and $S$ (the integral) as the entropy. The full discussion — including the uniqueness of $T$ up to a multiplicative constant via the zeroth law, and the orientation of $S$ via the irreversibility of stirring — is in [[Def - Absolute Temperature and Entropy]].

> [!tip] Cartan's Theory of Pfaffian Systems *(from Exterior Differential Systems)*
> The integrability of a single Pfaffian is the simplest case of **Cartan's theory of exterior differential systems**, which classifies systems of Pfaffian equations $\theta_1 = \cdots = \theta_r = 0$ by their integrability properties. Non-integrable systems may still have integral submanifolds of various dimensions ("Cartan-Kähler theorem"), and the theory connects to control theory, geometric PDE, and the geometry of jet bundles. See Bryant, Chern, Gardner, Goldschmidt, Griffiths, *Exterior Differential Systems* (1991) for the systematic theory.

> [!tip] Integrability in Hamiltonian Mechanics *(from Geometric Mechanics)*
> An autonomous Hamiltonian system on a symplectic manifold is **completely integrable** if it admits $n = \dim M / 2$ independent conserved quantities in involution (Poisson-commuting). This is the symplectic-geometric analogue of the Frobenius integrability condition, with the Poisson bracket playing the role of the Lie bracket. The Liouville-Arnold theorem then gives action-angle coordinates and explicit solutions in terms of $n$-tori. See [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics]] for the symplectic setup; complete integrability is a much stronger condition than the single-Pfaffian integrability of the present theorem.
