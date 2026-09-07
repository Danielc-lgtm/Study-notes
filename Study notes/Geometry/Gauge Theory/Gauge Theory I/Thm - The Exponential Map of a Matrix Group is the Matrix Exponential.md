---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - One-Parameter Subgroups are the Integral Curves of Left-Invariant Vector Fields"
  - "Thm - The Closed Subgroup Theorem"
  - "Def - Classical Matrix Groups"
tags: [geometry, gauge-theory, lie-groups]
---

# Notation

Throughout, $\mathbb{K}$ denotes either $\mathbb{R}$ or $\mathbb{C}$, and $\operatorname{Mat}(n \times n; \mathbb{K})$ is the associative algebra of $n \times n$ matrices over $\mathbb{K}$, with identity $1_n$. We write $GL(n; \mathbb{K}) = \{g \in \operatorname{Mat}(n \times n; \mathbb{K}) : \det g \neq 0\}$ for the [[Def - Classical Matrix Groups|general linear group]], which is an open subset of $\operatorname{Mat}(n \times n; \mathbb{K}) \cong \mathbb{K}^{n^2}$ and therefore a Lie group of the same dimension. A **matrix group** (or matrix Lie group) means a subgroup $G \subseteq GL(n; \mathbb{K})$ that is closed as a subset in the manifold topology; by the [[Thm - The Closed Subgroup Theorem|closed subgroup theorem]] such a $G$ is an embedded Lie subgroup of $GL(n; \mathbb{K})$.

We equip $\operatorname{Mat}(n \times n; \mathbb{K})$ with the **operator norm**
$$\lVert X \rVert := \sup_{v \in \mathbb{K}^n,\ |v| = 1} |Xv|,$$
where $|\cdot|$ is the standard Hermitian norm on $\mathbb{K}^n$. This norm is **submultiplicative**, $\lVert XY \rVert \le \lVert X \rVert \lVert Y \rVert$, and satisfies $\lVert 1_n \rVert = 1$; because $\operatorname{Mat}(n \times n; \mathbb{K})$ is finite-dimensional it is a Banach space (a complete normed space) under any norm, and a Banach algebra under this one.

For a Lie group $G$ we write $\mathfrak{g} = T_e G$ for its Lie algebra, the tangent space at the identity $e$; following the series convention, the bracket on $\mathfrak{g}$ is the bracket of left-invariant vector fields, which for a matrix group is the commutator $[X, Y] = XY - YX$. When $G \subseteq GL(n; \mathbb{K})$ is a matrix group, the inclusion identifies $\mathfrak{g} = T_e G$ with a linear subspace $\mathfrak{g} \subseteq \operatorname{Mat}(n \times n; \mathbb{K}) = T_e\, GL(n; \mathbb{K}) = \mathfrak{gl}(n; \mathbb{K})$. We write $\exp_G : \mathfrak{g} \to G$ for the [[Def - Exponential Map of a Lie Group|abstract Lie-theoretic exponential map]], defined by $\exp_G(X) = \gamma_X(1)$ where $\gamma_X : \mathbb{R} \to G$ is the unique one-parameter subgroup with $\dot\gamma_X(0) = X$, and we reserve the notation $e^X$ (no subscript) for the matrix exponential defined below. The full symbol registry is on the topic page [[Gauge Theory I — Lie Groups, Representations, and Group Actions]].

> [!warning] Convention: the source omits a step
> This page follows Bär's lecture notes (§1.4). Bär's Theorem 1.4.11 establishes $\exp_G(X) = e^X$ for a matrix group $G$ but does not verify that $e^{tX}$ actually lies in the subgroup $G$ (as opposed to merely in the ambient $GL(n; \mathbb{K})$) when $X \in \mathfrak{g}$. That verification is the geometric content of the [[Thm - The Closed Subgroup Theorem|closed subgroup theorem]] and is supplied in full in **Step A** of the formal proof below. Where we cite Bär we have filled this gap.

---

# Statement

> **Theorem (the exponential map of a matrix group is the matrix exponential).** Fix $\mathbb{K} \in \{\mathbb{R}, \mathbb{C}\}$.
>
> **Part I — the matrix exponential.** For every $X \in \operatorname{Mat}(n \times n; \mathbb{K})$ the series
> $$e^X := \sum_{k=0}^{\infty} \frac{X^k}{k!} = 1_n + X + \frac{X^2}{2!} + \frac{X^3}{3!} + \cdots$$
> converges absolutely in $\operatorname{Mat}(n \times n; \mathbb{K})$. It satisfies $e^{0} = 1_n$; the functional equation
> $$e^{(s+t)X} = e^{sX}\, e^{tX} \qquad \text{for all } s, t \in \mathbb{R};$$
> and, as a curve in $\operatorname{Mat}(n \times n; \mathbb{K})$,
> $$\frac{d}{dt}\, e^{tX} = X\, e^{tX} = e^{tX}\, X, \qquad \text{so in particular } \left.\frac{d}{dt}\right|_{t=0} e^{tX} = X.$$
> Consequently $e^{tX} \in GL(n; \mathbb{K})$ with $(e^{tX})^{-1} = e^{-tX}$, and $t \mapsto e^{tX}$ is a smooth one-parameter subgroup of $GL(n; \mathbb{K})$ with initial velocity $X$; hence $\exp_{GL(n;\mathbb{K})}(X) = e^X$.
>
> **Part II — identification on a closed subgroup.** Let $G \subseteq GL(n; \mathbb{K})$ be a matrix group with Lie algebra $\mathfrak{g} \subseteq \operatorname{Mat}(n \times n; \mathbb{K})$. Then for every $X \in \mathfrak{g}$ we have $e^{tX} \in G$ for all $t \in \mathbb{R}$, and
> $$\exp_G(X) = e^X.$$
> Moreover the Lie algebra is recovered as $\mathfrak{g} = \{X \in \operatorname{Mat}(n \times n; \mathbb{K}) : e^{tX} \in G \text{ for all } t \in \mathbb{R}\}$.

> **Corollary (worked instance, $SO(2)$).** With $\mathfrak{so}(2) = \left\{ A_\theta = \begin{pmatrix} 0 & -\theta \\ \theta & 0 \end{pmatrix} : \theta \in \mathbb{R} \right\}$, one has $e^{A_\theta} = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$, the rotation by angle $\theta$. Hence $\exp : \mathfrak{so}(2) \to SO(2)$ is surjective but not injective.

---

# Motivation

The abstract exponential map $\exp_G : \mathfrak{g} \to G$ is defined by an existence-and-uniqueness theorem for ordinary differential equations: $\exp_G(X)$ is the value at time $1$ of the integral curve, starting at the identity, of the left-invariant vector field determined by $X$. This definition is conceptually clean — it is what makes $\exp_G$ natural, a local diffeomorphism, and the source of one-parameter subgroups — but it is computationally opaque. Handed a specific matrix $X$, the definition tells us to solve a differential equation on the manifold $G$, and it does not, on its own, produce a number.

The matrix exponential $e^X = \sum_{k \ge 0} X^k / k!$ is the opposite. It is completely explicit: one raises $X$ to powers, divides by factorials, and adds. It can be evaluated by hand on a $2 \times 2$ matrix, diagonalised, estimated numerically, and differentiated term by term. What it is *not*, a priori, is a map into any particular Lie group, nor is it obviously the same object as $\exp_G$.

This theorem is the bridge. It says that for the groups we actually compute with — the [[Def - Classical Matrix Groups|classical matrix groups]] $O(n)$, $SO(n)$, $U(n)$, $SU(n)$, $SL(n; \mathbb{K})$, and $GL(n; \mathbb{K})$ itself — the abstract construction and the concrete power series are one and the same map. Every structural fact about $\exp_G$ proved by differential-geometric means (that it is a local diffeomorphism, that Lie group homomorphisms intertwine it, that its differential at the origin is the identity) may therefore be executed by manipulating a convergent series of matrices; and conversely, every calculation with the series inherits the geometric meaning of the abstract map. This is the identity that turns the theory of the exponential map into a computation, and almost everything later in the series that requires an explicit connection form, holonomy, or curvature in a matrix group passes through it. The guiding question of §1.4 — *how does one actually compute the exponential map of a group given as matrices?* — is answered here in one word: with the power series.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis that feeds Part II is *$X$ lies in the Lie algebra $\mathfrak{g}$ of the closed matrix group $G$*. Recognising this hypothesis in disguise is the recurring skill.

The first disguised source is **a matrix satisfying the linearised defining equation of $G$**. Property $B$ is "$X$ satisfies the equation obtained by differentiating the constraints that cut out $G$ at the identity" — for instance $X^t + X = 0$ for $G = O(n)$, or $\operatorname{tr} X = 0$ for $G = SL(n; \mathbb{K})$, or $X^* + X = 0$ for $G = U(n)$. The bridge is the last clause of this theorem: $\mathfrak{g} = \{X : e^{tX} \in G \text{ for all } t\}$, and one checks that $X$ satisfying the linearised equation forces $e^{tX}$ to satisfy the finite equation. For example, if $X^t = -X$ then $(e^{tX})^t e^{tX} = e^{tX^t} e^{tX} = e^{-tX} e^{tX} = 1_n$, so $e^{tX} \in O(n)$, whence $X \in \mathfrak{o}(n)$. *Example problem:* prove that the antisymmetric matrices form the Lie algebra of $O(n)$ by exponentiating, rather than by the regular value theorem.

The second disguised source is **the velocity of a smooth curve of group elements through the identity**. Property $B$ is "$X = \dot c(0)$ for a smooth curve $c : (-\varepsilon, \varepsilon) \to G$ with $c(0) = e$". The bridge is that $T_e G = \mathfrak{g}$ *is by definition* the set of such velocities, so any infinitesimal deformation of the identity inside $G$ is a legitimate input, and $e^{tX}$ is then the canonical one-parameter subgroup tangent to $c$ at $t = 0$. This is how a symmetry known only infinitesimally — the generator of a family of transformations — is integrated to a genuine one-parameter group of symmetries. *Example problem:* given a one-parameter family of rotations of $\mathbb{R}^3$ specified only by its angular velocity at $t = 0$, recover the rotations themselves as $e^{tX}$.

The third disguised source is **the anti-self-adjoint generator of a physical continuous symmetry**. Property $B$ is "$X$ is a skew-Hermitian matrix, $X^* = -X$" (or skew-Hermitian and traceless). The bridge is that skew-Hermitian matrices are exactly $\mathfrak{u}(n)$ (traceless: $\mathfrak{su}(n)$), so $e^{tX}$ is a one-parameter group of unitary operators; in quantum mechanics, with $X = -iH/\hbar$ for a Hermitian Hamiltonian $H$, the theorem says the time-evolution operator $U(t) = e^{-itH/\hbar}$ is literally the matrix exponential of the generator, and it is automatically unitary. *Example problem:* show that the Schrödinger evolution generated by a Hermitian Hamiltonian on a finite-dimensional state space is a one-parameter group in $U(n)$.

**Targets (Output Amplification)**

The conclusion is the identification $\exp_G = e^{(\cdot)}$ on a matrix group. Combined with other results it amplifies.

Combine this theorem with **the [[Thm - Naturality of the Exponential Map|naturality of the exponential map]]** — that a Lie group homomorphism $\varphi : G \to H$ satisfies $\varphi \circ \exp_G = \exp_H \circ\, d_e\varphi$. For a matrix representation $\varrho : G \to GL(V)$, both sides become matrix exponentials, and the extra ingredient $D$ (naturality) yields $E$: $\varrho(e^X) = e^{d_e\varrho(X)}$. The payoff is that one computes the image of a whole one-parameter subgroup under any representation by exponentiating the differential of the representation — the workhorse identity of representation theory in coordinates.

Combine this theorem with **the [[Thm - The Exponential Map is a Local Diffeomorphism at the Origin|local diffeomorphism theorem]]** — that $d_0 \exp_G = \operatorname{id}_{\mathfrak{g}}$, so $\exp_G$ restricts to a diffeomorphism of a neighbourhood of $0 \in \mathfrak{g}$ onto a neighbourhood of $e \in G$. The extra ingredient $D$ (local invertibility) combined with our identification $E$ gives explicit canonical coordinates of the first kind: near $e$, points of the matrix group are named by the matrix $X$ with $g = e^X$, and this chart is computed with the series. The payoff is a concrete coordinate system adapted to the group structure, in which one-parameter subgroups are straight lines through the origin.

Combine this theorem with **the [[Thm - The Closed Subgroup Theorem|closed subgroup theorem]]'s characterisation** $\mathfrak{g} = \{X : e^{tX} \in G \text{ for all } t\}$. The extra ingredient $D$ is a set of finite equations defining $G$; the payoff $E$ is a mechanical recipe for the Lie algebra: substitute $g = e^{tX}$ into the defining equations, differentiate at $t = 0$, and read off the linear conditions on $X$. This is exactly how every classical Lie algebra is computed in §1.2, and it turns the identification of $\mathfrak{g}$ from a manifold-theoretic question into a one-line differentiation.

---

# Why Is It True

The abstract exponential map is defined so that $t \mapsto \exp_G(tX)$ is *the* one-parameter subgroup of $G$ with velocity $X$ at the identity — it is the unique smooth homomorphism $\mathbb{R} \to G$ pointing in the direction $X$ at time zero. The whole theorem is the observation that the matrix series $t \mapsto e^{tX}$ is visibly such a homomorphism, so it can be nothing else.

**The matrix series $t \mapsto e^{tX}$ is manifestly a smooth homomorphism $\mathbb{R} \to GL(n; \mathbb{K})$ with velocity $X$ at the identity, and the abstract exponential is by definition the only such homomorphism, so the two coincide.**

To see the mechanism, look at the differential equation. On $GL(n; \mathbb{K})$, which is open in $\operatorname{Mat}(n \times n; \mathbb{K})$, the left-invariant vector field determined by $X \in \mathfrak{gl}(n; \mathbb{K})$ has value $gX$ at the point $g$, because left translation $L_g(h) = gh$ is a linear map with differential $h \mapsto gh$. The integral curve through the identity is therefore the solution of the matrix differential equation $\dot\gamma = \gamma X$, $\gamma(0) = 1_n$. Term-by-term differentiation of the series shows $\tfrac{d}{dt} e^{tX} = e^{tX} X$, and $e^{0} = 1_n$, so the series solves exactly this equation. Uniqueness of solutions of ordinary differential equations then forces $e^{tX} = \exp_{GL}(tX)$, and evaluating at $t = 1$ gives $e^X = \exp_{GL}(X)$.

For a closed subgroup $G$ the only additional content is geometric rather than analytic: one must know that the curve $e^{tX}$, built inside the ambient $GL(n; \mathbb{K})$, never leaves the subgroup $G$ when $X$ is tangent to $G$ at the identity. This is precisely what the closed subgroup theorem guarantees, by describing the Lie algebra of a closed subgroup as the set of directions whose one-parameter subgroups stay inside. Once the curve is known to live in $G$, the same uniqueness argument, now run inside $G$, identifies $e^{tX}$ with $\exp_G(tX)$.

---

# What Makes This Hard

The genuinely non-obvious step is the one Bär's text passes over: that $e^{tX} \in G$, and not merely in the ambient $GL(n; \mathbb{K})$, whenever $X \in \mathfrak{g}$. Producing a curve inside the subgroup from a tangent direction is exactly the difficulty the closed subgroup theorem exists to resolve, and it cannot be seen from the power series alone. The most common error is a different one: assuming $e^{A + B} = e^A e^B$ for arbitrary matrices — this is false unless $A$ and $B$ commute, and the functional equation of Part I survives only because $sX$ and $tX$ do commute. A third pitfall is manipulating the series (rearranging it into a Cauchy product, differentiating it term by term) before establishing that it converges and that the rearrangement and differentiation are licensed; each such interchange must be justified by absolute or uniform convergence, not taken for granted.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** First establish the matrix exponential as an analytic object on the Banach algebra $\operatorname{Mat}(n \times n; \mathbb{K})$ — convergence, the functional equation, the derivative — using only submultiplicativity of the operator norm and standard theorems on absolutely and uniformly convergent series. This makes $t \mapsto e^{tX}$ a smooth one-parameter subgroup of $GL(n; \mathbb{K})$ with velocity $X$, so uniqueness of one-parameter subgroups identifies it with $\exp_{GL}$. Then, for a closed subgroup $G$, invoke the closed subgroup theorem to keep the curve inside $G$, and run the uniqueness argument again inside $G$.

**Subgoal decomposition:**

1. **Convergence.** Show $\sum_k X^k / k!$ converges absolutely in $\operatorname{Mat}(n \times n; \mathbb{K})$.
   - *Hint:* Submultiplicativity gives $\lVert X^k \rVert \le \lVert X \rVert^k$; compare with the scalar series for $e^{\lVert X \rVert}$; absolute convergence in a Banach space implies convergence.
   - *Why needed:* Nothing may be manipulated until the object exists.

2. **Functional equation.** Show $e^{(s+t)X} = e^{sX} e^{tX}$.
   - *Hint:* Multiply the two absolutely convergent series as a Cauchy product; because $sX$ and $tX$ commute, the inner sum is $\tfrac{1}{k!}\sum_l \binom{k}{l} s^l t^{k-l} X^k = \tfrac{(s+t)^k}{k!} X^k$ by the binomial theorem.
   - *Why needed:* It gives the homomorphism property and, at $s = t$, invertibility.

3. **Derivative.** Show $\tfrac{d}{dt} e^{tX} = X e^{tX} = e^{tX} X$.
   - *Hint:* Differentiate term by term; justify with the Weierstrass M-test that the differentiated series converges uniformly on compact $t$-intervals.
   - *Why needed:* It supplies the initial velocity $X$ and the differential equation $\dot\gamma = \gamma X$.

4. **One-parameter subgroup and $\exp_{GL}$.** Assemble subgoals 1–3 into: $t \mapsto e^{tX}$ is a smooth homomorphism $\mathbb{R} \to GL(n; \mathbb{K})$ with $\dot\gamma(0) = X$; conclude $e^{tX} = \exp_{GL}(tX)$.
   - *Hint:* The left-invariant field on $GL$ is $g \mapsto gX$; the one-parameter subgroup theorem says a smooth homomorphism from $\mathbb{R}$ is the integral curve $\gamma_X$ of that field, and $\gamma_X(t) = \exp(tX)$; uniqueness of one-parameter subgroups with given velocity closes it.
   - *Why needed:* This is Part I's identification, and the template for Part II.

5. **Staying in $G$.** For a closed subgroup $G$ and $X \in \mathfrak{g}$, show $e^{tX} \in G$ for all $t$.
   - *Hint:* The closed subgroup theorem identifies $\mathfrak{g}$ with $\{X : \exp_{GL}(tX) \in G \text{ for all } t\}$; use subgoal 4 to replace $\exp_{GL}(tX)$ by $e^{tX}$.
   - *Why needed:* Without it the curve is not a curve in $G$ and $\exp_G$ is not even reachable.

6. **Identification on $G$.** Conclude $\exp_G(X) = e^X$.
   - *Hint:* $t \mapsto e^{tX}$ is now a smooth homomorphism $\mathbb{R} \to G$ (smoothness into $G$ because $G$ is embedded) with velocity $X \in T_e G$; run subgoal 4's uniqueness argument inside $G$; evaluate at $t = 1$.
   - *Why needed:* This is the theorem.

---

# Lemma Decomposition

> [!note]- Lemma 1: The matrix exponential converges absolutely
> **Statement:** For every $X \in \operatorname{Mat}(n \times n; \mathbb{K})$ the series $\sum_{k=0}^{\infty} X^k / k!$ converges absolutely in $\big(\operatorname{Mat}(n \times n; \mathbb{K}), \lVert \cdot \rVert\big)$, and its sum $e^X$ satisfies $\lVert e^X \rVert \le e^{\lVert X \rVert}$.
>
> **Hint:** Submultiplicativity gives $\lVert X^k \rVert \le \lVert X \rVert^k$; dominate by the scalar exponential series; invoke completeness.
>
> **Why needed:** It makes $e^X$ a well-defined element of the algebra, so that every later manipulation of the series has an object to act on, and it provides the norm bound used in the M-tests below.
>
> > [!note]- Full proof
> > **Submultiplicativity of the operator norm.** For $X, Y \in \operatorname{Mat}(n \times n; \mathbb{K})$ and any unit vector $v \in \mathbb{K}^n$, $|XYv| \le \lVert X \rVert\, |Yv| \le \lVert X \rVert \lVert Y \rVert\, |v| = \lVert X \rVert \lVert Y \rVert$ (by the definition of the operator norm applied first to $X$ acting on $Yv$, then to $Y$ acting on $v$); taking the supremum over unit $v$ gives $\lVert XY \rVert \le \lVert X \rVert \lVert Y \rVert$. By induction, $\lVert X^k \rVert \le \lVert X \rVert^k$ for every $k \ge 0$ (with $\lVert X^0 \rVert = \lVert 1_n \rVert = 1 = \lVert X \rVert^0$).
> >
> > **Domination by a convergent scalar series.** The series of norms of the terms is bounded term by term:
> > $$\sum_{k=0}^{\infty} \left\lVert \frac{X^k}{k!} \right\rVert = \sum_{k=0}^{\infty} \frac{\lVert X^k \rVert}{k!} \le \sum_{k=0}^{\infty} \frac{\lVert X \rVert^k}{k!} = e^{\lVert X \rVert} < \infty \qquad (\text{by } \lVert X^k \rVert \le \lVert X \rVert^k \text{ and the convergence of the real exponential series}).$$
> > Thus $\sum_k X^k / k!$ is **absolutely convergent**: the series of norms converges.
> >
> > **Completeness closes it.** The space $\operatorname{Mat}(n \times n; \mathbb{K}) \cong \mathbb{K}^{n^2}$ is finite-dimensional, hence complete in the operator norm (all norms on a finite-dimensional space are equivalent, and $\mathbb{K}^{n^2}$ is complete). In a complete normed space every absolutely convergent series converges (the partial sums form a Cauchy sequence, since $\big\lVert \sum_{k=m}^{p} X^k/k! \big\rVert \le \sum_{k=m}^{p} \lVert X^k\rVert / k! \to 0$ as $m, p \to \infty$). Therefore $e^X = \sum_k X^k / k!$ exists in $\operatorname{Mat}(n \times n; \mathbb{K})$, and passing to the limit in the partial-sum bound gives $\lVert e^X \rVert \le \sum_k \lVert X^k \rVert / k! \le e^{\lVert X \rVert}$. Therefore the matrix exponential is a well-defined matrix with the stated norm bound. $\blacksquare$

> [!note]- Lemma 2: The functional equation for commuting exponents
> **Statement:** For every $X \in \operatorname{Mat}(n \times n; \mathbb{K})$ and all $s, t \in \mathbb{R}$, $e^{(s+t)X} = e^{sX}\, e^{tX}$. In particular $e^{0} = 1_n$ and $e^{tX}$ is invertible with $(e^{tX})^{-1} = e^{-tX}$.
>
> **Hint:** Form the Cauchy product of the two absolutely convergent series; use that $sX$ and $tX$ commute so that $(sX)^l (tX)^m = s^l t^m X^{l+m}$; collect by the binomial theorem.
>
> **Why needed:** It is the group-homomorphism property of $t \mapsto e^{tX}$ and, evaluated at $t = -s$, the invertibility that places the curve in $GL(n; \mathbb{K})$.
>
> > [!note]- Full proof
> > **The value at zero.** Every term of $\sum_k (0 \cdot X)^k / k!$ vanishes except $k = 0$, which is $1_n$; hence $e^{0} = 1_n$.
> >
> > **Absolute convergence licenses the Cauchy product.** By Lemma 1 the series $\sum_l (sX)^l / l!$ and $\sum_m (tX)^m / m!$ both converge absolutely in the Banach algebra $\operatorname{Mat}(n \times n; \mathbb{K})$. For two absolutely convergent series $\sum_l a_l$ and $\sum_m b_m$ in a Banach algebra, the product of the sums equals the sum of the Cauchy product, $\big(\sum_l a_l\big)\big(\sum_m b_m\big) = \sum_{k=0}^{\infty} c_k$ with $c_k = \sum_{l=0}^{k} a_l\, b_{k-l}$, and the product series converges absolutely (this is the Cauchy-product theorem, valid in any Banach algebra because the rearrangement is justified by absolute convergence). Apply it with $a_l = (sX)^l / l!$ and $b_m = (tX)^m / m!$:
> > $$e^{sX}\, e^{tX} = \sum_{k=0}^{\infty} c_k, \qquad c_k = \sum_{l=0}^{k} \frac{(sX)^l}{l!}\, \frac{(tX)^{k-l}}{(k-l)!} \qquad (\text{Cauchy product}).$$
> >
> > **Commutativity and the binomial theorem.** Since $sX$ and $tX$ are scalar multiples of the single matrix $X$, they commute, and $(sX)^l (tX)^{k-l} = s^l t^{k-l} X^l X^{k-l} = s^l t^{k-l} X^k$. Therefore
> > $$c_k = \sum_{l=0}^{k} \frac{s^l t^{k-l}}{l!\,(k-l)!}\, X^k = \frac{X^k}{k!} \sum_{l=0}^{k} \binom{k}{l} s^l t^{k-l} = \frac{X^k}{k!}\,(s+t)^k \qquad \left(\text{since } \tfrac{1}{l!(k-l)!} = \tfrac{1}{k!}\binom{k}{l} \text{ and by the binomial theorem}\right).$$
> >
> > **Resummation.** Summing over $k$,
> > $$e^{sX}\, e^{tX} = \sum_{k=0}^{\infty} \frac{(s+t)^k X^k}{k!} = e^{(s+t)X} \qquad (\text{by the definition of } e^{(s+t)X}).$$
> >
> > **Invertibility.** Taking $t = -s$ gives $e^{sX}\, e^{-sX} = e^{(s - s)X} = e^{0} = 1_n$, and symmetrically $e^{-sX}\, e^{sX} = 1_n$; hence $e^{sX}$ is invertible with inverse $e^{-sX}$. Therefore the functional equation holds and $e^{tX} \in GL(n; \mathbb{K})$ for every $t$. $\blacksquare$

> [!note]- Lemma 3: Term-by-term differentiation of the matrix exponential
> **Statement:** The map $t \mapsto e^{tX}$ from $\mathbb{R}$ to $\operatorname{Mat}(n \times n; \mathbb{K})$ is differentiable, with $\dfrac{d}{dt}\, e^{tX} = X\, e^{tX} = e^{tX}\, X$; in particular $\left.\tfrac{d}{dt}\right|_{0} e^{tX} = X$. Iterating, $t \mapsto e^{tX}$ is smooth (indeed real-analytic), with $\tfrac{d^j}{dt^j} e^{tX} = X^j e^{tX}$.
>
> **Hint:** The series $\sum_k t^k X^k / k!$ has derivative series $\sum_{k \ge 1} t^{k-1} X^k / (k-1)!$; bound it on $|t| \le R$ by $\lVert X \rVert\, e^{R \lVert X \rVert}$ and apply the Weierstrass M-test, then the uniform-convergence differentiation theorem.
>
> **Why needed:** It gives the initial velocity $X$ (subgoal 4) and the differential equation $\dot\gamma = \gamma X$ that identifies $e^{tX}$ with an integral curve.
>
> > [!note]- Full proof
> > **The differentiated series.** Write $F(t) = \sum_{k=0}^{\infty} f_k(t)$ with $f_k(t) = \dfrac{t^k X^k}{k!}$, a series of smooth $\operatorname{Mat}(n \times n; \mathbb{K})$-valued functions of $t \in \mathbb{R}$. Each term is differentiable with
> > $$f_k'(t) = \frac{k\, t^{k-1}}{k!}\, X^k = \frac{t^{k-1}}{(k-1)!}\, X^k \quad (k \ge 1), \qquad f_0'(t) = 0.$$
> >
> > **Uniform convergence of the differentiated series (Weierstrass M-test).** Fix $R > 0$. For $|t| \le R$ and $k \ge 1$,
> > $$\lVert f_k'(t) \rVert = \frac{|t|^{k-1}}{(k-1)!}\, \lVert X^k \rVert \le \frac{R^{k-1} \lVert X \rVert^{k}}{(k-1)!} =: M_k \qquad (\text{by } |t| \le R \text{ and } \lVert X^k \rVert \le \lVert X \rVert^k),$$
> > and $\sum_{k \ge 1} M_k = \lVert X \rVert \sum_{k \ge 1} \dfrac{(R \lVert X \rVert)^{k-1}}{(k-1)!} = \lVert X \rVert\, e^{R \lVert X \rVert} < \infty$. By the Weierstrass M-test the series $\sum_k f_k'$ converges uniformly on $[-R, R]$. The series $\sum_k f_k$ itself converges pointwise (Lemma 1, applied to $tX$).
> >
> > **The differentiation theorem.** For $\operatorname{Mat}(n \times n; \mathbb{K})$-valued (equivalently, coordinatewise real- or complex-valued) functions on an interval, if $\sum_k f_k$ converges at one point and $\sum_k f_k'$ converges uniformly on the interval, then $\sum_k f_k$ is differentiable and may be differentiated term by term. Applying it on each $[-R, R]$ (and $R$ was arbitrary),
> > $$F'(t) = \sum_{k=1}^{\infty} \frac{t^{k-1}}{(k-1)!}\, X^k = \sum_{j=0}^{\infty} \frac{t^{j}}{j!}\, X^{j+1} \qquad (\text{term-by-term differentiation; reindex } j = k-1).$$
> >
> > **Factoring out $X$.** In the reindexed series each term is $\frac{t^j}{j!} X^{j+1} = X \cdot \frac{t^j X^j}{j!} = \frac{t^j X^j}{j!} \cdot X$ (the matrix $X$ commutes with every power of itself), so
> > $$F'(t) = X \sum_{j=0}^{\infty} \frac{t^j X^j}{j!} = X\, e^{tX}, \qquad F'(t) = \left(\sum_{j=0}^{\infty} \frac{t^j X^j}{j!}\right) X = e^{tX}\, X.$$
> > Setting $t = 0$ leaves only the $j = 0$ term, giving $\left.\tfrac{d}{dt}\right|_0 e^{tX} = X\, e^{0} = X$.
> >
> > **Smoothness.** The same argument applied to $t \mapsto X^j e^{tX}$ shows it is differentiable with derivative $X^{j+1} e^{tX}$; by induction every derivative $\tfrac{d^j}{dt^j} e^{tX} = X^j e^{tX}$ exists and is continuous, so $t \mapsto e^{tX}$ is of class $C^\infty$. Therefore the matrix exponential is a smooth curve with the stated derivative. $\blacksquare$

> [!note]- Lemma 4: The curve $t \mapsto e^{tX}$ is the one-parameter subgroup $\exp_{GL}(tX)$
> **Statement:** For every $X \in \mathfrak{gl}(n; \mathbb{K}) = \operatorname{Mat}(n \times n; \mathbb{K})$, the curve $t \mapsto e^{tX}$ is a smooth group homomorphism $\mathbb{R} \to GL(n; \mathbb{K})$ with $\left.\tfrac{d}{dt}\right|_0 e^{tX} = X$, and it equals the abstract one-parameter subgroup: $e^{tX} = \exp_{GL(n;\mathbb{K})}(tX)$ for all $t$; in particular $\exp_{GL}(X) = e^X$.
>
> **Hint:** On the open subset $GL \subseteq \operatorname{Mat}$ the left-invariant field of $X$ is $g \mapsto gX$; the differential equation $\dot\gamma = \gamma X$, $\gamma(0) = 1_n$ is solved by $e^{tX}$ (Lemma 3); the one-parameter subgroup theorem identifies its solution with $\exp_{GL}(tX)$.
>
> **Why needed:** It is Part I's identification and the exact template that Part II re-runs inside a closed subgroup.
>
> > [!note]- Full proof
> > **The curve lands in $GL$ and is a homomorphism.** By Lemma 2, $e^{(s+t)X} = e^{sX} e^{tX}$ and $e^{0} = 1_n$, and each $e^{tX}$ is invertible; hence $t \mapsto e^{tX}$ is a group homomorphism from $(\mathbb{R}, +)$ into $GL(n; \mathbb{K})$. By Lemma 3 it is smooth, with $\left.\tfrac{d}{dt}\right|_0 e^{tX} = X$.
> >
> > **The left-invariant vector field on $GL$.** Since $GL(n; \mathbb{K})$ is an open subset of the vector space $\operatorname{Mat}(n \times n; \mathbb{K})$, its tangent space at every point $g$ is canonically $\operatorname{Mat}(n \times n; \mathbb{K})$, and left translation $L_g : h \mapsto gh$ is the restriction of a linear map, so its differential at any point is $L_g$ itself: $d_h L_g(Y) = gY$. Hence the left-invariant vector field $X^L$ determined by $X = X^L(e) \in T_e\, GL = \operatorname{Mat}$ has value
> > $$X^L(g) = d_e L_g(X) = gX \qquad (\text{differential of the linear map } L_g).$$
> >
> > **The curve is the integral curve of $X^L$.** By Lemma 3, $\tfrac{d}{dt} e^{tX} = e^{tX} X = X^L(e^{tX})$, and $e^{0} = 1_n = e$; so $t \mapsto e^{tX}$ is an integral curve of the left-invariant field $X^L$ through the identity.
> >
> > **Identification with the abstract exponential.** By the [[Thm - One-Parameter Subgroups are the Integral Curves of Left-Invariant Vector Fields|one-parameter subgroup theorem]] — a smooth curve $\gamma : \mathbb{R} \to G'$ with $\gamma(0) = e$ is a group homomorphism if and only if it is the integral curve through $e$ of the left-invariant vector field $X^L$ with $X = \dot\gamma(0)$, this integral curve is complete and equals $t \mapsto \exp_{G'}(tX)$, and it is the unique one-parameter subgroup with initial velocity $X$ — applied to $G' = GL(n; \mathbb{K})$ and this $X$, the integral curve of $X^L$ through the identity is exactly $t \mapsto \exp_{GL}(tX)$. Since $t \mapsto e^{tX}$ is also that integral curve, uniqueness of integral curves gives
> > $$e^{tX} = \exp_{GL(n;\mathbb{K})}(tX) \qquad \text{for all } t \in \mathbb{R};$$
> > evaluating at $t = 1$, $e^X = \exp_{GL}(X)$. Therefore on the full general linear group the matrix exponential is the Lie-theoretic exponential map. $\blacksquare$
> >
> > (For $\mathbb{K} = \mathbb{R}$ this is the computation carried out in [[Ex - The Exponential Map of GL(n,R) is the Matrix Exponential]]; the argument above is identical over $\mathbb{K} = \mathbb{C}$, since $GL(n; \mathbb{C})$ is likewise open in $\operatorname{Mat}(n \times n; \mathbb{C})$ and left translation is again linear.)

---

# Formal Proof

> [!note]- Complete formal proof
> Fix $\mathbb{K} \in \{\mathbb{R}, \mathbb{C}\}$ and $n \ge 1$.
>
> **Step 0 — the objects are well-posed.** By **Lemma 1**, for every $X \in \operatorname{Mat}(n \times n; \mathbb{K})$ the series $e^X = \sum_{k \ge 0} X^k / k!$ converges absolutely, so $e^X$ is a well-defined matrix; this is the only precondition needed before manipulating the series.
>
> **Part I — the matrix exponential and $\exp_{GL}$.**
>
> **Convergence, functional equation, derivative.** Absolute convergence is **Lemma 1**. The functional equation $e^{(s+t)X} = e^{sX} e^{tX}$, with $e^{0} = 1_n$ and $(e^{tX})^{-1} = e^{-tX}$, is **Lemma 2**. The derivative identity $\tfrac{d}{dt} e^{tX} = X e^{tX} = e^{tX} X$, hence $\left.\tfrac{d}{dt}\right|_0 e^{tX} = X$, is **Lemma 3**. Together these are exactly the three displayed assertions of Part I.
>
> **One-parameter subgroup and identification.** By **Lemma 4**, $t \mapsto e^{tX}$ is a smooth group homomorphism $\mathbb{R} \to GL(n; \mathbb{K})$ with initial velocity $X$, and $\exp_{GL(n;\mathbb{K})}(tX) = e^{tX}$; at $t = 1$, $\exp_{GL}(X) = e^X$. This proves Part I.
>
> **Part II — a closed subgroup $G \subseteq GL(n; \mathbb{K})$ with Lie algebra $\mathfrak{g}$.**
>
> **Step A — the curve stays in $G$.** We must show $e^{tX} \in G$ for all $t \in \mathbb{R}$ whenever $X \in \mathfrak{g}$. Because $G$ is a closed subgroup of the Lie group $GL(n; \mathbb{K})$, the [[Thm - The Closed Subgroup Theorem|closed subgroup theorem]] — *a topologically closed subgroup $H$ of a Lie group $G'$ is an embedded Lie subgroup, and its Lie algebra, regarded as a subspace of $\mathfrak{g}'$, is $\mathfrak{h} = \{Y \in \mathfrak{g}' : \exp_{G'}(tY) \in H \text{ for all } t \in \mathbb{R}\}$* — applies with $G' = GL(n; \mathbb{K})$, $\mathfrak{g}' = \mathfrak{gl}(n; \mathbb{K}) = \operatorname{Mat}(n \times n; \mathbb{K})$, and $H = G$. It identifies the Lie algebra of $G$ (as an embedded Lie subgroup, i.e. $\mathfrak{g} = T_e G \subseteq \operatorname{Mat}$) with
> $$\mathfrak{g} = \{X \in \operatorname{Mat}(n \times n; \mathbb{K}) : \exp_{GL}(tX) \in G \text{ for all } t \in \mathbb{R}\} \qquad (\text{closed subgroup theorem, Lie algebra characterisation}).$$
> By Part I, $\exp_{GL}(tX) = e^{tX}$, so this reads
> $$\mathfrak{g} = \{X \in \operatorname{Mat}(n \times n; \mathbb{K}) : e^{tX} \in G \text{ for all } t \in \mathbb{R}\} \qquad (\text{substituting } \exp_{GL} = e^{(\cdot)}).$$
> In particular, if $X \in \mathfrak{g}$ then $e^{tX} \in G$ for every $t$. This is the step Bär's text omits, and it also proves the last assertion of Part II (the displayed recovery of $\mathfrak{g}$).
>
> **Step B — smoothness of the curve into $G$.** The closed subgroup theorem gives that $G$ is an *embedded* submanifold of $GL(n; \mathbb{K})$. A smooth map into an ambient manifold whose image lies in an embedded submanifold is smooth as a map into the submanifold (in a slice chart adapted to $G$, the transverse coordinates of the map vanish identically and the remaining coordinates are smooth). Since $t \mapsto e^{tX}$ is smooth into $GL(n; \mathbb{K})$ (Lemma 3) and, by Step A, takes values in $G$, it is a smooth curve $\mathbb{R} \to G$.
>
> **Step C — identification on $G$.** By Step B and Lemma 2, $t \mapsto e^{tX}$ is a smooth group homomorphism $\mathbb{R} \to G$ (its values multiply by the functional equation, inherited from the ambient group), and by Lemma 3 its initial velocity is $\left.\tfrac{d}{dt}\right|_0 e^{tX} = X$, which lies in $T_e G = \mathfrak{g}$ by hypothesis. Applying the [[Thm - One-Parameter Subgroups are the Integral Curves of Left-Invariant Vector Fields|one-parameter subgroup theorem]] now to $G$ itself — the unique one-parameter subgroup of $G$ with initial velocity $X$ is $t \mapsto \exp_G(tX)$ — and noting that $t \mapsto e^{tX}$ is such a one-parameter subgroup, uniqueness gives
> $$e^{tX} = \exp_G(tX) \qquad \text{for all } t \in \mathbb{R} \qquad (\text{uniqueness of one-parameter subgroups with velocity } X).$$
> Evaluating at $t = 1$,
> $$\exp_G(X) = e^X.$$
>
> **Conclusion.** Part I establishes the matrix exponential as a convergent series with the functional equation and derivative, identifying it with $\exp_{GL}$; Part II carries the identification to every closed subgroup, with the curve remaining in $G$ by the closed subgroup theorem. Therefore, for a matrix group $G \subseteq GL(n; \mathbb{K})$ and $X \in \mathfrak{g}$, the abstract exponential map coincides with the matrix exponential, $\exp_G(X) = e^X$, and $\mathfrak{g} = \{X : e^{tX} \in G \text{ for all } t\}$. $\blacksquare$

> [!note]- Worked corollary: $\exp$ on $\mathfrak{so}(2)$ is the rotation, surjective but not injective (Bär, Example 1.4.12)
> We compute $\exp : \mathfrak{so}(2) \to SO(2)$ explicitly and read off its surjectivity and non-injectivity. Recall $SO(2) \subseteq GL(2; \mathbb{R})$ is a closed subgroup, so Part II applies, and its Lie algebra is
> $$\mathfrak{so}(2) = \left\{ A_\theta := \begin{pmatrix} 0 & -\theta \\ \theta & 0 \end{pmatrix} : \theta \in \mathbb{R} \right\},$$
> the antisymmetric $2 \times 2$ real matrices.
>
> **Powers of $A_\theta$.** Write $J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, so $A_\theta = \theta J$ and $J^2 = -1_2$. Then
> $$A_\theta^{2k} = \theta^{2k} (J^2)^k = \theta^{2k}(-1_2)^k = (-1)^k \theta^{2k}\, 1_2, \qquad A_\theta^{2k+1} = A_\theta^{2k}\, A_\theta = (-1)^k \theta^{2k}\,(\theta J) = (-1)^k \theta^{2k+1} J,$$
> for every $k \ge 0$ (by $J^2 = -1_2$ and $A_\theta = \theta J$).
>
> **Summing the series.** The matrix exponential converges absolutely (Lemma 1), so its terms may be split into the even and odd sub-series and each summed separately:
> $$e^{A_\theta} = \sum_{k=0}^{\infty} \frac{A_\theta^{2k}}{(2k)!} + \sum_{k=0}^{\infty} \frac{A_\theta^{2k+1}}{(2k+1)!} = \left(\sum_{k=0}^{\infty} \frac{(-1)^k \theta^{2k}}{(2k)!}\right) 1_2 + \left(\sum_{k=0}^{\infty} \frac{(-1)^k \theta^{2k+1}}{(2k+1)!}\right) J \qquad (\text{even/odd split, absolute convergence}).$$
> The two scalar series are the Taylor series of $\cos\theta$ and $\sin\theta$, so
> $$e^{A_\theta} = \cos\theta \cdot 1_2 + \sin\theta \cdot J = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} \qquad (\text{by } \textstyle\sum_k \frac{(-1)^k\theta^{2k}}{(2k)!} = \cos\theta,\ \sum_k \frac{(-1)^k\theta^{2k+1}}{(2k+1)!} = \sin\theta).$$
> By Part II, $\exp_{SO(2)}(A_\theta) = e^{A_\theta}$, the rotation matrix $R_\theta$ of angle $\theta$.
>
> **Surjectivity.** Every element of $SO(2)$ is a rotation $R_\theta = \big(\begin{smallmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{smallmatrix}\big)$ for some $\theta \in \mathbb{R}$ (the defining conditions $g^t g = 1_2$, $\det g = 1$ force the columns to be an oriented orthonormal frame, hence of this form). Since $R_\theta = \exp_{SO(2)}(A_\theta)$, the map $\exp : \mathfrak{so}(2) \to SO(2)$ hits every element; it is **surjective**.
>
> **Non-injectivity.** The angles $\theta$ and $\theta + 2\pi$ give the same rotation, $R_\theta = R_{\theta + 2\pi}$, so $\exp(A_\theta) = \exp(A_{\theta + 2\pi})$ while $A_\theta \neq A_{\theta + 2\pi}$; concretely $\exp(A_\theta) = 1_2 \iff \cos\theta = 1$ and $\sin\theta = 0 \iff \theta \in 2\pi\mathbb{Z}$, so the preimage of the identity is $\{A_{2\pi k} : k \in \mathbb{Z}\}$, an infinite set. Hence $\exp$ is **not injective**.
>
> **Conclusion.** The exponential of a matrix in $\mathfrak{so}(2)$ is the corresponding planar rotation, and $\exp : \mathfrak{so}(2) \to SO(2)$ is surjective but not injective. $\blacksquare$

This worked instance is drilled further, with the kernel $2\pi\mathbb{Z}$ computed in full, in [[Ex - The Exponential Map of so(2) is Surjective but Not Injective]].

---

# Cross-Field Exercise Suggestions

**Quantum time evolution.** On a finite-dimensional Hilbert space $\mathbb{C}^n$ with a Hermitian Hamiltonian $H = H^*$, the Schrödinger equation $i\hbar\, \dot\psi = H\psi$ has solution $\psi(t) = U(t)\psi(0)$ with $U(t) = e^{-itH/\hbar}$. The theorem applies because $X = -iH/\hbar$ is skew-Hermitian, so $X \in \mathfrak{u}(n)$ and $U(t) = e^{tX}$ is a one-parameter subgroup of $U(n)$; it is non-obvious that time evolution is *automatically* unitary, but this is forced by $X^* = -X$ giving $U(t)^* U(t) = e^{tX^*} e^{tX} = e^{-tX} e^{tX} = 1_n$. The exercise is to prove unitarity of the evolution and to identify the conserved probability $|\psi(t)|^2$ with the invariance of the Hermitian form under $U(n)$.

**Linear autonomous dynamical systems.** The system $\dot x = A x$ on $\mathbb{R}^n$ with constant coefficient matrix $A$ has solution $x(t) = e^{tA} x(0)$; the theorem certifies that this matrix exponential is exactly the flow of the (linear) left-invariant field on $GL(n; \mathbb{R})$ generated by $A$. It is non-obvious how the qualitative behaviour (growth, decay, oscillation) is encoded, and the exercise is to relate the eigenvalues of $A$ to the long-time behaviour of $e^{tA}$ — real parts controlling exponential growth or decay, imaginary parts controlling rotation — which is the spectral reading of the same series computed above for $\mathfrak{so}(2)$.

**Structure-preserving numerical integration.** A numerical scheme for a differential equation evolving on a matrix group $G$ (a rigid body on $SO(3)$, a Hamiltonian flow on $Sp(2n)$) will generically drift off the group when advanced by an ordinary Runge–Kutta step in the ambient matrix space. Lie group integrators instead advance by $g_{k+1} = g_k\, e^{h X_k}$ with $X_k \in \mathfrak{g}$, and the theorem is what guarantees the update stays exactly on $G$ (Step A). The exercise is to show that such an exponential update preserves the group constraint to machine precision, whereas an additive update does not, and to estimate the local error of one step.

**Screw motions in robotics.** A rigid motion of $\mathbb{R}^3$ is an element of $SE(3)$, and the exponential of a *twist* — an element of $\mathfrak{se}(3)$ pairing an angular and a linear velocity — is the finite screw motion (a rotation about, and translation along, a fixed axis). The theorem identifies the abstract exponential of the twist with the matrix exponential of its $4 \times 4$ representation, which the exercise asks the reader to compute in closed form using the nilpotency structure of $\mathfrak{se}(3)$, generalising the $\mathfrak{so}(2)$ computation above to the semidirect product $SE(3) = SO(3) \ltimes \mathbb{R}^3$.

---

# Bridges

- **Naturality and representations.** The [[Thm - Naturality of the Exponential Map|naturality of the exponential map]] states $\varphi \circ \exp_G = \exp_H \circ\, d_e\varphi$ for a Lie group homomorphism $\varphi : G \to H$. When $G$ and $H$ are matrix groups and $\varphi = \varrho$ is a representation, this theorem turns both exponentials into series, giving $\varrho(e^X) = e^{d_e\varrho(X)}$. The construction is: differentiate the representation at the identity to obtain the Lie algebra representation $d_e\varrho$, exponentiate on the algebra side, and the identity says the group-level image is the exponential of the differential. This is the mechanism by which the standard, adjoint, and tensor-power representations of $SU(2)$ and $U(1)$ are computed on one-parameter subgroups later in the chapter.

- **Computing Lie algebras from defining equations.** The closed subgroup theorem's characterisation $\mathfrak{g} = \{X : e^{tX} \in G \text{ for all } t\}$, combined with Part I, gives a mechanical construction of $\mathfrak{g}$: write the finite equations defining $G \subseteq GL(n; \mathbb{K})$ (for $O(n)$: $g^t g = 1_n$; for $SL$: $\det g = 1$; for $U(n)$: $g^* g = 1_n$), substitute $g = e^{tX}$, differentiate at $t = 0$ using $\tfrac{d}{dt}|_0 e^{tX} = X$ and the product rule, and read off the linear conditions ($X^t + X = 0$; $\operatorname{tr} X = 0$; $X^* + X = 0$). This construction is executed group by group in [[Def - Classical Matrix Groups|the classical groups]] and their Lie algebras.

- **The two exponential maps.** The name "exponential map" is shared with the [[Def - The Riemannian Exponential Map|Riemannian exponential map]] of a metric, which sends a tangent vector to the endpoint of the geodesic it generates. On a compact Lie group carrying a bi-invariant metric, the two constructions coincide: the geodesics through the identity are exactly the one-parameter subgroups $t \mapsto e^{tX}$, so the Riemannian exponential of the bi-invariant metric equals the group exponential computed here. This coincidence is the engine of the surjectivity result [[Thm - The Exponential Map of a Compact Connected Lie Group is Surjective|for compact connected groups]], where a minimizing geodesic from the identity to any point exhibits that point as an exponential.

- **Failure of surjectivity off the compact case.** The corollary shows $\exp$ is onto for $SO(2)$, which is compact; the construction breaks for non-compact groups. Substituting $g = e^X$ into the traceless condition and analysing eigenvalues shows, for instance, that $\operatorname{diag}(-2, -\tfrac12) \in SL(2; \mathbb{R})$ is not an exponential of any element of $\mathfrak{sl}(2; \mathbb{R})$, because a real traceless $2 \times 2$ matrix exponentiates to a matrix whose eigenvalues are $e^{\pm\lambda}$ with $\lambda$ real or purely imaginary, never a pair of distinct negative reals. The bridge between the two behaviours is compactness, and the contrast is worked out in the exercises to this section.

---

# Unlocked by This

> [!tip] One-parameter subgroups are matrix exponentials *(from Lie theory)*
> Every continuous, hence smooth, homomorphism $\mathbb{R} \to G$ into a matrix group is of the form $t \mapsto e^{tX}$ for a unique $X \in \mathfrak{g}$. This reduces the classification of one-parameter subgroups to a choice of tangent vector and makes the group's local structure fully explicit through the series.

> [!tip] Canonical coordinates of the first kind *(from differential geometry)*
> Because $\exp_G = e^{(\cdot)}$ is a local diffeomorphism at the origin, the assignment $X \mapsto e^X$ is a chart of $G$ near the identity in which one-parameter subgroups are straight lines through $0$; every local computation on the group near $e$ may be transported to a computation on the vector space $\mathfrak{g}$ with the concrete series.
