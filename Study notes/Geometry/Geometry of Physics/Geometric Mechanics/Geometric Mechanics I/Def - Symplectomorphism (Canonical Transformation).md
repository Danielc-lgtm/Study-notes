---
type: definition
subject: geometric-mechanics
prereqs:
  - "Def - Symplectic Manifold"
  - "Def - Diffeomorphism"
  - "Def - Pullback of a Differential Form on a Manifold"
tags: [physics, geometric-mechanics, symplectic-geometry]
---

# Notation

$(M_1, \omega_1)$ and $(M_2, \omega_2)$ are symplectic manifolds (same dimension $2n$). $\varphi : M_1 \to M_2$ is a smooth map; $\varphi^*$ denotes [[Def - Pullback of a Differential Form on a Manifold|pullback of differential forms]]. $\mathrm{Symp}(M, \omega)$ denotes the group of symplectomorphisms of $(M, \omega)$ to itself; $\mathrm{Ham}(M, \omega)$ denotes the subgroup of **Hamiltonian symplectomorphisms** — those arising as the time-$1$ map of a (time-dependent) Hamiltonian flow.

In classical-mechanics literature, symplectomorphisms are called **canonical transformations**; the two terms denote the same object.

---

# Axiom Motivation

We have symplectic manifolds. We have the geometric setup of Hamiltonian dynamics. We need the right notion of **structure-preserving map** between symplectic manifolds — the morphisms in the category of symplectic geometry. The motivating question is: **which diffeomorphisms preserve all the structure that makes Hamiltonian mechanics work?**

The answer is straightforward: we want maps that preserve the symplectic form $\omega$. A diffeomorphism $\varphi : M_1 \to M_2$ preserves the symplectic form if $\varphi^*\omega_2 = \omega_1$ — pulling back $\omega_2$ to $M_1$ via $\varphi$ recovers $\omega_1$. This single condition packages all the structure preservation we want.

Why is this the right condition? Because **everything we care about in symplectic mechanics is built from $\omega$**:

- The **Hamiltonian vector field** $X_H$ is defined by $\iota_{X_H}\omega = dH$. If $\varphi^*\omega_2 = \omega_1$, then the pushforward $\varphi_*X_H$ on $M_2$ satisfies $\iota_{\varphi_* X_H}\omega_2 = d(H \circ \varphi^{-1})$, so $X_H$ on $M_1$ and $X_{H\circ\varphi^{-1}}$ on $M_2$ are intertwined by $\varphi$. **Symplectomorphisms map Hamiltonian dynamics to Hamiltonian dynamics**.

- The **Poisson bracket** $\{f, g\} = \omega(X_f, X_g)$ is defined using $\omega$. If $\varphi^*\omega_2 = \omega_1$, then $\{f, g\}_1 \circ \varphi^{-1} = \{f \circ \varphi^{-1}, g \circ \varphi^{-1}\}_2$ — **symplectomorphisms intertwine the Poisson brackets**. They are Poisson algebra isomorphisms in the right sense.

- The **Liouville volume** $\omega^n$ is the $n$-fold wedge of $\omega$, so $\varphi^*\omega_2^n = (\varphi^*\omega_2)^n = \omega_1^n$. **Symplectomorphisms preserve phase-space volume**. (In particular, every symplectomorphism is volume-preserving — but the converse is dramatically false in dimensions $\geq 4$, by Gromov's non-squeezing theorem.)

- The **Lagrangian submanifolds** are defined by $\omega|_L = 0$ and $\dim L = n$. A symplectomorphism carries Lagrangians to Lagrangians.

So preserving $\omega$ preserves all the structure. The single equation $\varphi^*\omega_2 = \omega_1$ is the right axiom.

Why call it a "canonical transformation" in classical-mechanics language? Because in the early days of mechanics, before the symplectic framework was made manifest, the natural question was: **what coordinate changes on phase space preserve the form of Hamilton's equations?** A coordinate change $(q, p) \to (Q, P)$ is called "canonical" if Hamilton's equations in the new coordinates still read $\dot Q^i = \partial H'/\partial P_i$, $\dot P_i = -\partial H'/\partial Q^i$ for some new Hamiltonian $H'$. The structural answer — which took a generation to crystallize — is: **a coordinate change preserves the form of Hamilton's equations if and only if it preserves the symplectic 2-form** $\omega = dp_i \wedge dq^i$, i.e., it is a symplectomorphism.

The classical condition for canonicity (in pre-symplectic language) is the preservation of the **Poisson brackets**: $\{Q^i, Q^j\}_{(q,p)} = 0$, $\{P_i, P_j\}_{(q,p)} = 0$, $\{Q^i, P_j\}_{(q,p)} = \delta^i_j$ — that the new coordinates have the same fundamental brackets as the old ones. This is precisely $\varphi^*\omega = \omega$, written out in components. The transition from "canonical transformation" to "symplectomorphism" is the transition from coordinate-based mechanics to coordinate-free geometric mechanics.

What if we *weaken* the condition to $\varphi^*\omega_2 = c\,\omega_1$ for some nonzero constant $c$ (or for $c \in C^\infty(M_1)$)? The first weakening — $c$ a nonzero constant — gives **conformal symplectomorphisms**, which preserve symplectic structure up to rescaling and are important in some contexts (e.g., contact geometry). The second weakening — $c$ a function — destroys most of the dynamical content: the Hamiltonian vector field $X_H$ would not transform correctly. Neither variant is what classical mechanics needs; the rigid condition $\varphi^*\omega_2 = \omega_1$ is what makes everything work.

What if we *strengthen* the condition by also requiring $\varphi$ to be the time-$1$ map of a Hamiltonian flow? This gives the smaller class of **Hamiltonian symplectomorphisms** $\mathrm{Ham}(M, \omega) \leq \mathrm{Symp}(M, \omega)$. The two coincide on simply connected manifolds (or more generally when $H^1_{dR}(M; \mathbb{R}) = 0$); on a torus or any manifold with nontrivial first cohomology, $\mathrm{Symp}/\mathrm{Ham} \cong H^1_{dR}(M; \mathbb{R})$ measures the cohomological obstruction. The distinction matters: Hamiltonian symplectomorphisms are those arising from a "Newton's-equation" dynamics, while general symplectomorphisms include topologically nontrivial transformations like "translation by a closed but non-exact $1$-form".

---

# The Definition

Let $(M_1, \omega_1)$ and $(M_2, \omega_2)$ be symplectic manifolds. A **symplectomorphism** (also called a **canonical transformation** in classical mechanics) is a diffeomorphism $\varphi : M_1 \to M_2$ satisfying

$$\varphi^*\omega_2 = \omega_1.$$

The set of symplectomorphisms of $(M, \omega)$ to itself, denoted $\mathrm{Symp}(M, \omega)$, forms an (infinite-dimensional) Lie group under composition, with Lie algebra the **symplectic vector fields** — vector fields $X$ with $\mathcal{L}_X\omega = 0$ (equivalently, $\iota_X\omega$ closed).

A symplectomorphism $\varphi : M \to M$ is called **Hamiltonian** if there exists a time-dependent Hamiltonian $H_t : M \times [0, 1] \to \mathbb{R}$ such that $\varphi = \phi^H_1$, the time-$1$ map of the flow of the time-dependent vector field $X_{H_t}$. The Hamiltonian symplectomorphisms form a normal subgroup $\mathrm{Ham}(M, \omega) \trianglelefteq \mathrm{Symp}(M, \omega)$, with quotient $\mathrm{Symp}/\mathrm{Ham}$ controlled by $H^1_{dR}(M; \mathbb{R})$ (Calabi homomorphism).

**In canonical coordinates** $(q^i, p_i)$ in which $\omega = \sum dp_i \wedge dq^i$, a smooth map $\varphi(q, p) = (Q(q, p), P(q, p))$ is a symplectomorphism if and only if the Jacobian matrix $J = \partial(Q, P)/\partial(q, p)$ satisfies $J^T \Omega J = \Omega$, where $\Omega = \begin{pmatrix}0 & I_n \\ -I_n & 0\end{pmatrix}$ — i.e., $J$ is a symplectic matrix at every point. Equivalently, the **fundamental Poisson brackets** must be preserved:

$$\{Q^i, Q^j\} = 0, \qquad \{P_i, P_j\} = 0, \qquad \{Q^i, P_j\} = \delta^i_j.$$

---

# Categorical / Structural Definition

The symplectomorphisms are the **morphisms in the category of symplectic manifolds**. With objects symplectic manifolds and morphisms symplectomorphisms (which, by the rank theorem and nondegeneracy of $\omega$, must be local diffeomorphisms — so they are diffeomorphisms onto their image), this category is the natural setting for symplectic geometry. The isomorphism classes in this category are the symplectic structures up to global symplectic-equivalence.

The group $\mathrm{Symp}(M, \omega)$ is an **infinite-dimensional Fréchet Lie group**, with Lie algebra the symplectic vector fields $\mathfrak{symp}(M, \omega) = \{X \in \Gamma(TM) : \mathcal{L}_X\omega = 0\}$. The exponential map $\exp : \mathfrak{symp} \to \mathrm{Symp}$ sends $X$ to the time-$1$ map of its flow (when $X$ is complete). The Lie subalgebra $\mathfrak{ham}(M, \omega) \leq \mathfrak{symp}(M, \omega)$ of **Hamiltonian vector fields** integrates to the Hamiltonian symplectomorphism group $\mathrm{Ham}(M, \omega)$.

The short exact sequence of Lie algebras
$$0 \to \mathbb{R} \to C^\infty(M) \xrightarrow{H \mapsto X_H} \mathfrak{ham}(M, \omega) \to 0$$
(with kernel the locally constant functions, on a connected $M$ just the constants) is the algebraic content of "the Hamiltonian vector fields are the image of the function-to-flow map". Integrating gives a similar exact sequence at the level of groups.

The cohomological obstruction $\mathfrak{symp}/\mathfrak{ham} \cong H^1_{dR}(M; \mathbb{R})$: a symplectic vector field $X$ corresponds to a closed $1$-form $\iota_X\omega$, and it is Hamiltonian iff this $1$-form is exact, with the class $[\iota_X\omega] \in H^1_{dR}(M; \mathbb{R})$ as the obstruction.

In categorical language: $\mathrm{Symp}$ is a sheaf of Lie groups on $M$, with $\mathrm{Ham}$ an infinite-dimensional subgroup, and the quotient is governed by sheaf cohomology of $\underline{\mathbb{R}}$. The **Calabi invariant** $\mathrm{Symp}/\mathrm{Ham} \to H^1_{dR}(M; \mathbb{R})$ is the canonical surjection from this quotient.

---

# Relate to Other Fields / Compression

A symplectomorphism is the **symplectic analogue of an isometry** of a Riemannian manifold. An isometry $\varphi : (M_1, g_1) \to (M_2, g_2)$ is a diffeomorphism with $\varphi^*g_2 = g_1$; a symplectomorphism is a diffeomorphism with $\varphi^*\omega_2 = \omega_1$. The contrast is structural: isometries form a *finite-dimensional* Lie group (because Riemannian geometry has so many local invariants — curvature — that an isometry is determined by its 1-jet at a point), while symplectomorphisms form an *infinite-dimensional* Lie group (because Darboux's theorem rules out local invariants, so the structure is "infinitely flexible" locally). The local rigidity of Riemannian geometry produces small symmetry groups; the local flexibility of symplectic geometry produces enormous ones.

From the dynamical systems perspective, a symplectomorphism is the time-$t$ map of a Hamiltonian flow (if Hamiltonian) or, more generally, the time-$t$ map of a symplectic flow. The study of symplectomorphisms of a fixed symplectic manifold — their fixed points, periodic points, conjugacy classes, generating functions — is a major topic in dynamical systems, with deep connections to **billiard dynamics**, **the Arnold conjecture**, and **Floer homology**.

In quantum mechanics, the analogue of a symplectomorphism is a **unitary operator** on the Hilbert space. Both groups (symplectomorphisms and unitaries) are the structure-preserving automorphisms of the relevant arena, and **quantization** is a (program for a) functor from the symplectic to the unitary category, mapping $\varphi \in \mathrm{Symp}(M)$ to $U(\varphi) \in U(\mathcal{H})$ in a way that respects composition. The success of this functor is the success of quantization; the obstructions are anomalies.

**True name:** the true name of a symplectomorphism is **"a change of coordinates on phase space that preserves the form of Hamilton's equations"** — the original classical-mechanics meaning. The pullback condition $\varphi^*\omega_2 = \omega_1$ is the coordinate-free abstraction of this dynamical preservation.

---

# Examples / Corollaries

**Is an instance: any Hamiltonian flow $\phi^H_t$.** By [[Thm - Hamiltonian Flows are Symplectomorphisms]], $(\phi^H_t)^*\omega = \omega$ for all $t$. So Hamiltonian flows are symplectomorphisms for every $t$ — and in fact they are *Hamiltonian* symplectomorphisms (members of $\mathrm{Ham}$, not just $\mathrm{Symp}$).

**Is an instance: linear symplectic maps on $\mathbb{R}^{2n}$.** A linear map $\varphi : \mathbb{R}^{2n} \to \mathbb{R}^{2n}$ with matrix $A \in \mathrm{Sp}(2n, \mathbb{R})$ (i.e., $A^T J A = J$ where $J$ is the standard symplectic matrix) is a symplectomorphism of $(\mathbb{R}^{2n}, \omega_0)$. The symplectic group $\mathrm{Sp}(2n, \mathbb{R})$ has dimension $n(2n+1)$ and includes: the identity; the time-$t$ map of any harmonic oscillator; the canonical "exchange of $q$ and $p$" given by $\varphi(q, p) = (p, -q)$; the rescaling $(q, p) \mapsto (\lambda q, \lambda^{-1}p)$.

**Is an instance: cotangent lift of a diffeomorphism.** For a diffeomorphism $f : Q \to Q'$, the cotangent lift $T^*f : T^*Q' \to T^*Q$ defined by $(T^*f)(\alpha_q)(v) = \alpha_{f(q)}(df_q(v))$ is a symplectomorphism (in fact its inverse $(T^*f)^{-1} : T^*Q \to T^*Q'$ is the symplectomorphism in the forward direction). These are the **point transformations** of classical mechanics — symplectomorphisms induced by configuration-space transformations. They form a subgroup of all symplectomorphisms; generic symplectomorphisms mix $q$ and $p$ in ways that no point transformation can.

**Is an instance: the time-$t$ flow of the harmonic oscillator.** On $\mathbb{R}^2$ with $\omega = dp \wedge dq$, the harmonic oscillator $H = \tfrac{1}{2}(p^2 + q^2)$ generates the flow $\phi_t(q, p) = (q\cos t + p\sin t, -q\sin t + p\cos t)$. This is rigid rotation in the $(q, p)$-plane, and it preserves area, hence preserves $\omega$. The rotation angle is the time $t$, so $\phi_{2\pi} = \mathrm{id}$ — the oscillator is periodic.

**Is an instance: translations of $\mathbb{R}^{2n}$.** $\varphi(q, p) = (q + a, p + b)$ for constants $(a, b) \in \mathbb{R}^{2n}$ is a symplectomorphism: $\varphi^*\omega_0 = \omega_0$ since the symplectic form is translation-invariant. These are *not* Hamiltonian (on $\mathbb{R}^{2n}$ they are, since $\mathbb{R}^{2n}$ is contractible) on more general manifolds — for instance, on the torus $T^{2n}$, translations are symplectomorphisms but not Hamiltonian for generic directions of translation.

**Is NOT an instance: $\varphi(q, p) = (q, 2p)$ on $\mathbb{R}^2$.** Then $\varphi^*(dp \wedge dq) = d(2p) \wedge dq = 2\,dp\wedge dq \neq dp \wedge dq$. So this is *not* a symplectomorphism; it is a **conformal symplectomorphism** that rescales $\omega$ by $2$. This is consistent — area scales by $2$ in this map — but it is not a canonical transformation in the classical sense.

**Is NOT an instance: $\varphi(q, p) = (q, p^3)$ on $\mathbb{R}^2$.** $\varphi^*(dp \wedge dq) = 3p^2\, dp \wedge dq \neq dp \wedge dq$. So this is not a symplectomorphism even though it is a smooth diffeomorphism. (As a side remark, $\varphi$ is not even close to symplectic: it scales area by $3p^2$, which is large for large $p$ and vanishes at $p = 0$.)

**Is NOT an instance: a non-bijective $\varphi$.** Even if $\varphi^*\omega_2 = \omega_1$, we require $\varphi$ to be a diffeomorphism, i.e., bijective with smooth inverse. The "exchange" $\varphi(q, p) = (p, q)$ is a diffeomorphism; the constant map $\varphi(q, p) = (0, 0)$ is not.

**Corollary (preservation of Liouville volume).** $\varphi^*\omega_2^n = (\varphi^*\omega_2)^n = \omega_1^n$. So every symplectomorphism preserves the symplectic volume form. (But the converse is dramatically false in dimensions $\geq 4$, by Gromov's non-squeezing theorem.)

**Corollary (preservation of Poisson brackets).** $\{f \circ \varphi^{-1}, g \circ \varphi^{-1}\}_2 = \{f, g\}_1 \circ \varphi^{-1}$, i.e., a symplectomorphism intertwines the Poisson algebras $C^\infty(M_1)$ and $C^\infty(M_2)$. So conservation laws transform consistently.

**Corollary (preservation of Lagrangian submanifolds).** If $L \subset M_1$ is Lagrangian and $\varphi : M_1 \to M_2$ is a symplectomorphism, then $\varphi(L) \subset M_2$ is Lagrangian. This is the structural reason **Lagrangian submanifolds are the natural objects of study** in symplectic topology — they are the canonically distinguished submanifolds that survive the action of the (huge) symplectomorphism group.

**Corollary (group structure of $\mathrm{Symp}(M, \omega)$).** Closure under composition: $(\varphi_1 \circ \varphi_2)^*\omega = \varphi_2^*\varphi_1^*\omega = \varphi_2^*\omega = \omega$. Inverses are symplectomorphisms: $(\varphi^{-1})^*\omega = ((\varphi^*)^{-1})\omega = \omega$. The identity is clearly a symplectomorphism. So $\mathrm{Symp}(M, \omega)$ is a group; it inherits the smooth structure from $\mathrm{Diff}(M)$.

**Calibration check.** If you can do these three things, you have understood the definition. First, verify by direct computation that the harmonic-oscillator flow $\phi_t(q, p) = (q\cos t + p\sin t, -q\sin t + p\cos t)$ preserves $\omega = dp \wedge dq$ — compute $\phi_t^*\omega$ and check it equals $\omega$. Second, compute the pullback of $\omega = dp_1 \wedge dq^1 + dp_2 \wedge dq^2$ under the map $\varphi(q, p) = (q_1 + q_2, q_1 - q_2, (p_1 + p_2)/2, (p_1 - p_2)/2)$ and check whether $\varphi$ is a symplectomorphism. Third, show that the cotangent lift $T^*f$ of a smooth diffeomorphism $f : Q \to Q'$ satisfies $(T^*f)^*\theta_{Q} = \theta_{Q'}$ (preservation of the tautological 1-form), hence $(T^*f)^*\omega_Q = \omega_{Q'}$.

---

# Unlocked by This

> [!tip] Generating Functions and Hamilton–Jacobi Theory *(from Classical Mechanics)*
> Every symplectomorphism $\varphi : T^*Q_1 \to T^*Q_2$ can locally be encoded by a **generating function**: a smooth function $S(q_1, q_2)$ (or one of several Legendre-related variants, $S(q_1, p_2)$ etc.) such that the relations $p^{(1)}_i = \partial S/\partial q^i_{(1)}$, $p^{(2)}_i = -\partial S/\partial q^i_{(2)}$ implicitly define $\varphi$. For the time-$t$ Hamiltonian flow itself, the generating function $S(q_1, q_2, t)$ satisfies the **Hamilton–Jacobi equation** $\partial S/\partial t + H(q_2, \partial S/\partial q_2, t) = 0$. Solving this equation for a complete integral $S(q, \alpha, t)$ depending on $n$ parameters integrates Hamilton's equations by quadratures — the most powerful classical solution method, and the bridge to WKB quantum mechanics.

> [!tip] Floer Homology and the Arnold Conjecture *(from Symplectic Topology)*
> **Arnold's conjecture** asserts that the number of fixed points of a Hamiltonian symplectomorphism $\varphi \in \mathrm{Ham}(M, \omega)$ of a closed symplectic manifold is at least $\sum_i \dim H^i(M; \mathbb{R})$ — the sum of Betti numbers. **Floer homology** $HF^*(\varphi, \omega)$ is a graded vector space invariant of the Hamiltonian symplectomorphism, computed from a Morse-theory-like chain complex generated by fixed points of $\varphi$, with differential given by counts of holomorphic strips connecting them. Floer proved his eponymous theorem that $HF^*(\varphi, \omega) \cong H^*(M; \mathbb{R})$, establishing Arnold's conjecture for the manifolds where the construction applies — a deep global rigidity result that compensates for Darboux's local flexibility.

> [!tip] Hofer's Geometry on $\mathrm{Ham}(M, \omega)$ *(from Symplectic Topology)*
> Hofer (1990) discovered a **bi-invariant Finsler metric** on $\mathrm{Ham}(M, \omega)$: the **Hofer norm** of a Hamiltonian symplectomorphism $\varphi$ is the infimum over all Hamiltonians $H_t$ generating a path from $\mathrm{id}$ to $\varphi$ of $\int_0^1 (\max H_t - \min H_t)\,dt$. This is the only known non-trivial bi-invariant metric on a group of diffeomorphisms; in stark contrast, the group $\mathrm{Diff}(M)$ admits no bi-invariant metric (one can always "shrink" diffeomorphisms by composition with appropriate conjugations). The diameter of $(\mathrm{Ham}(M), d_H)$ is infinite for many symplectic manifolds, and Hofer's metric is a deep symplectic invariant tied to symplectic capacities and Floer-theoretic invariants.
