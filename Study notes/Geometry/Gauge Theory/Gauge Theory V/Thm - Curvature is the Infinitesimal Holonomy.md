---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - The Path-Ordered Exponential Solves the Linear Parallel-Transport Equation"
  - "Def - Holonomy Group of a Connection"
  - "Def - Parallel Transport in a Principal Bundle"
  - "Thm - Structure Equation for the Curvature"
  - "Def - Local Connection Form and Gauge Potential"
  - "Def - Lie-Algebra-Valued Differential Forms and Their Bracket"
  - "Thm - Stokes' Theorem on Manifolds"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $G \subset GL(n; \mathbb{K})$ is a matrix Lie group ($\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$), with Lie algebra $\mathfrak{g} = T_eG \subset \operatorname{Mat}(n \times n; \mathbb{K})$; the bracket on $\mathfrak{g}$ is the matrix commutator $[X, Y] = XY - YX$. We write $\pi : P \to B$ for a $G$-principal bundle over a smooth manifold $B$ and $\omega \in \Omega^1(P; \mathfrak{g})$ for a connection $1$-form on it. The group acts on $P$ on the **right**, $R_g(p) = p \cdot g$, in the standing convention of the series.

Fix a base point $b_0 \in B$ and a trivialising open set $U_\alpha \ni b_0$ with a smooth local section $s_\alpha : U_\alpha \to P|_{U_\alpha}$. The **local connection form** (gauge potential) is $A := s_\alpha^* \omega \in \Omega^1(U_\alpha; \mathfrak{g})$, restated from [[Def - Local Connection Form and Gauge Potential|its definition]]: it is the pullback of the connection along $s_\alpha$, an $\mathfrak{g}$-valued $1$-form on the base. In coordinates $x = (x^1, \dots, x^m)$ on $U_\alpha$ centred at $b_0$ (so $b_0$ has coordinates $(0, \dots, 0)$), we write
$$A = \sum_{j=1}^m A_j \, dx^j, \qquad A_j \in C^\infty(U_\alpha; \mathfrak{g}),$$
and abbreviate $A = A_j \, dx^j$ with the summation over the repeated index $j$ understood. The **local curvature** $2$-form is
$$F := dA + A \wedge A \in \Omega^2(U_\alpha; \mathfrak{g}),$$
where for a matrix group the wedge of the matrix-valued form with itself is $A \wedge A = \sum_{j<k} [A_j, A_k] \, dx^j \wedge dx^k$; this is the local form $s_\alpha^* \Omega$ of the principal curvature $\Omega = d\omega + \tfrac{1}{2}[\omega \wedge \omega]$, restated in the Statement below.

For a $\mathfrak{g}$-valued or matrix-valued form $\eta = \sum_I \eta_I \, dx^I$ with entries $\eta_I \in C^0$, the sup-norm is $\lVert \eta \rVert_{C^0} := \sup_{x} \max_I \lVert \eta_I(x) \rVert$ over the closed ball named below, with $\lVert \cdot \rVert$ a fixed submultiplicative matrix norm on $\operatorname{Mat}(n \times n; \mathbb{K})$ (so $\lVert XY \rVert \le \lVert X \rVert \, \lVert Y \rVert$); the $C^1$-norm $\lVert A \rVert_{C^1}$ adds the sup-norms of the first coordinate derivatives $\partial_i A_j$.

A curve $c : [0, 1] \to B$ is **piecewise smooth**; $\dot c$ is its velocity and $c$ is a **loop at $b_0$** when $c(0) = c(1) = b_0$. Integration $\int_c \eta$ of a $\mathfrak{g}$-valued $1$-form is $\int_0^1 \eta_{c(\tau)}(\dot c(\tau)) \, d\tau$, and $\int_S \eta$ of a $\mathfrak{g}$-valued form over an oriented surface is the entrywise integral of the scalar components. We use $\operatorname{Pexp}$ for the [[Def - Path-Ordered Exponential|path-ordered exponential]] and $\operatorname{hol}(c) \in G$ for the [[Def - Holonomy Group of a Connection|holonomy]] of a loop, both recalled in the proof. The symbol $O(L^k)$ denotes a $\operatorname{Mat}(n \times n; \mathbb{K})$-valued quantity of norm at most $KL^k$ for a constant $K$ and all $L \in (0, L_0)$.

> [!warning] Convention: curvature sign and the $\tfrac{1}{2}$
> This series writes the principal curvature as $\Omega = d\omega + \tfrac{1}{2}[\omega \wedge \omega]$ (structure equation), whose local form is $F = dA + \tfrac{1}{2}[A \wedge A]$. For a **matrix group** the bracket-of-forms convention $[\alpha \wedge \beta](X, Y) = [\alpha(X), \beta(Y)] - [\alpha(Y), \beta(X)]$ gives $\tfrac{1}{2}[A \wedge A] = A \wedge A$ (ordinary matrix wedge product), so $F = dA + A \wedge A$; both forms appear below and are identical here. The source (Bär–Wernli §2.6) writes the same expansion; where its transcription carries an index slip it is corrected on this page and the correction is flagged at the point of use.

---

# Statement

> **Theorem (curvature is the infinitesimal holonomy).** Let $G \subset GL(n; \mathbb{K})$ be a matrix group and $\pi : P \to B$ a $G$-principal bundle with connection $1$-form $\omega$. Fix $b_0 \in B$, a trivialising set $U_\alpha \ni b_0$ with section $s_\alpha$, coordinates centred at $b_0$, and set $A = s_\alpha^* \omega = A_j \, dx^j$ with local curvature $F = dA + A \wedge A$. Let $C > 0$ and $L_0 > 0$ be constants, and for each $L \in (0, L_0)$ let
> $$c_L : [0, 1] \to B$$
> be a piecewise smooth loop at $b_0$ that is parametrised **proportionally to arc length** (so $\lVert \dot c_L(\tau) \rVert$ is constant in $\tau$), has length at most $CL$, lies in the closed coordinate ball $\overline{B}(b_0, CL) = \{x : \lVert x \rVert \le CL\}$, and bounds a compact oriented surface $S_L \subset U_\alpha$ with $\partial S_L = c_L$ and area at most $CL^2$. Then, as $L \searrow 0$,
> $$\operatorname{hol}(c_L) = 1_n - \int_{S_L} F + O(L^3),$$
> where the constant hidden in $O(L^3)$ depends only on $C$, on $n$, and on the $C^1$-norm $\lVert A \rVert_{C^1}$ of $A$ on the ball $\overline{B}(b_0, CL_0)$. Here $\operatorname{hol}(c_L) \in G \subset \operatorname{Mat}(n \times n; \mathbb{K})$ is the holonomy of $c_L$ in the trivialisation $s_\alpha$, acting on the model fibre $\mathbb{K}^n$ in the defining representation.

The companion form recorded during the proof, which exhibits the two pieces of the curvature separately, is:

> **Theorem (assembled form).** Under the same hypotheses,
> $$\operatorname{hol}(c_L) = 1_n - \underbrace{\int_{S_L} dA}_{\text{first order, } O(L^2)} - \underbrace{\int_{S_L} A \wedge A}_{\text{ordering, } O(L^2)} + O(L^3),$$
> the first integral coming from the first-order (linear) term of the holonomy and the second from the non-commutativity of the ordered product of the connection along the loop.

The two blockquotes state the same result: $\int_{S_L} F = \int_{S_L}(dA + A \wedge A)$, so the assembled form collapses to the principal form. The point of separating them is that $\int_{S_L} dA$ would be the whole answer for an **abelian** structure group (there the ordering term $\int_{S_L} A \wedge A$ vanishes, since $[A_j, A_k] = 0$), recovering the exact identity $\operatorname{hol}(c) = \exp(-\int_S dA)$ of [[Thm - Holonomy of an Abelian Connection is the Exponential of the Curvature Integral|the abelian holonomy theorem]] to first order; the commutator term $\int_{S_L} A \wedge A$ is precisely the non-abelian correction.

---

# Motivation

Curvature was defined twice in this series, and neither definition looks like holonomy. On a vector bundle it is the failure of second covariant derivatives to commute, $F_\nabla(X, Y) = \nabla_X \nabla_Y - \nabla_Y \nabla_X - \nabla_{[X, Y]}$; on a principal bundle it is the structure-equation $2$-form $\Omega = d\omega + \tfrac{1}{2}[\omega \wedge \omega]$, measuring the non-integrability of the horizontal distribution. Holonomy, by contrast, is a global and finite object: transport a frame around a closed loop and record the group element $\operatorname{hol}(c) \in G$ by which it comes back rotated. The question this theorem answers is the one every student of connections asks first and every physicist answers by drawing a small square: *how are these two things the same?* We already know they are related in one direction — a flat connection ($F = 0$) has trivial holonomy on contractible loops — but that is a qualitative statement. The theorem makes it quantitative and local: the holonomy of a small loop, to the order at which anything nontrivial happens, **is** the flux of the curvature through the loop.

The importance is that it converts a differential invariant into a measurable transport. The curvature is an infinitesimal object, a $2$-form; you cannot "see" a $2$-form directly. What you can see is the discrepancy after carrying a vector around a small closed path, and this theorem says that discrepancy is $-\int_S F$ to leading order. This is the exact sense in which $F_{\mu\nu}$ in physics is "the field": the electromagnetic and Yang–Mills field strengths are the infinitesimal holonomies of the gauge connection, and a Wilson loop $\operatorname{tr} \operatorname{hol}(c)$ around a small loop probes $\operatorname{tr} F$ through it. The theorem is also the local heart of the [[Def - Holonomy Group of a Connection|Ambrose–Singer]] circle of ideas, which reconstructs the whole holonomy group from the curvature: if curvature is the derivative of holonomy at a point, then integrating curvature over all loops rebuilds holonomy, and the Lie algebra of the holonomy group is spanned by the curvature values. This page proves only the pointwise, second-order statement — the derivative — but that is the statement from which the rest follows.

There is one more reason the result matters here. The abelian case was exact and easy: for $G$ abelian the ordered product is an ordinary product, the path-ordered exponential collapses to $\exp(-\int_c A)$, and Stokes gives $\operatorname{hol}(c) = \exp(-\int_S F)$ with no error term at all. The non-abelian case has no such closed form — there is a genuine ordering ambiguity in the product of the connection values along the loop, and the exact holonomy is an infinite Dyson series. The theorem says that this ordering ambiguity is exactly what promotes $dA$ to the full curvature $dA + A \wedge A$: the commutator term $A \wedge A$ is the second-order residue of non-commutativity, invisible in the abelian case and dominant in the non-abelian one.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypotheses are a matrix structure group and a shrinking family of small loops of controlled length, diameter, and area. The interesting sources are the situations that *manufacture* such a family without announcing it.

The first disguised source is **a single fixed loop rescaled toward a point**. Given any smooth loop $\gamma : [0, 1] \to B$ based at $b_0$, contained in one coordinate chart, its rescalings $c_L(\tau) := L \cdot \gamma(\tau)$ in coordinates (or, chart-free, the loops obtained by flowing $\gamma$ under a contracting vector field) form exactly a family satisfying the hypotheses: length scales like $L$, diameter like $L$, and the bounded area like $L^2$. The non-obvious bridge is that a *single* loop already contains the infinitesimal-holonomy data once one is willing to look at its shrunk copies; one does not need a pre-arranged family. *Example problem:* compute the curvature of a connection at a point by transporting a frame around a shrinking coordinate square and reading off the $O(L^2)$ coefficient — this is Ambrose–Singer in one point and the basis of [[Ex - Second-Order Holonomy Expansion for a Small Square in the Plane|the small-square exercise]].

The second disguised source is **a Riemannian geodesic parallelogram or geodesic triangle**. On a Riemannian manifold the loop built from four geodesic segments of length $L$ (a "geodesic quadrilateral") automatically has length $O(L)$, sits in a ball of radius $O(L)$, and bounds a geodesic surface of area $O(L^2)$; the Levi-Civita connection is a matrix connection in an orthonormal frame. The non-obvious step is that the metric geometry supplies the length, diameter, and area bounds for free, so the theorem applies verbatim and computes the Riemann curvature as the leading rotation of a parallel-transported vector. *Example problem:* recover that the holonomy of transport around a small geodesic triangle on the sphere is rotation by the enclosed area (the [[Ex - Parallel Transport around a Geodesic Triangle on the Sphere|spherical-triangle]] fact) as the $-\int_S F$ term with $F$ the Gaussian curvature.

The third disguised source is **a lattice or plaquette in a discretised gauge theory**. In lattice gauge theory the fundamental variable is a group element $U_\ell \in G$ on each edge, and the product $U_\square$ around an elementary plaquette of spacing $L$ is, in the continuum limit, the holonomy of a small square loop. The non-obvious bridge is that the plaquette variable is literally $\operatorname{hol}(c_L)$ for the square $c_L$ of side $L$, so the theorem is the statement that the continuum action $\operatorname{Re} \operatorname{tr}(1 - U_\square) \sim \tfrac{1}{2}\lVert F \rVert^2 L^4$ reproduces the Yang–Mills Lagrangian. *Example problem:* derive the Wilson action's continuum limit by expanding $1 - \operatorname{hol}(c_L) = \int_{S_L} F + O(L^3)$ and squaring.

**Targets (Output Amplification).** The bare conclusion is a second-order expansion of one holonomy. Combined with other ingredients it does much more.

Combine the conclusion with **a covering of a large loop by a mesh of small ones**. A loop $c$ bounding a surface $S$ can be written as a concatenation of small plaquette loops $c_{L}^{(i)}$ whose boundaries cancel on shared edges; multiplying the plaquette holonomies (ordered) and passing to the limit gives the non-abelian Stokes theorem, $\operatorname{hol}(c) = \operatorname{Pexp}\!\big(-\int_S F\big)$ in the surface-ordered sense. The extra ingredient is the group multiplicativity $\operatorname{hol}(c_2 * c_1) = \operatorname{hol}(c_2)\operatorname{hol}(c_1)$ from [[Thm - Properties of Parallel Transport|the properties of parallel transport]]; the payoff is that the local statement globalises to a surface integral.

Combine the conclusion with **the Ad-equivariance of curvature**. Under a change of frame $s_\alpha' = s_\alpha \cdot g$ one has $A' = g^{-1} A g + g^{-1} dg$ and $F' = g^{-1} F g$ ([[Thm - Transformation of Local Connection and Curvature Forms|the transformation law]]), while $\operatorname{hol}'(c_L) = g(b_0)^{-1}\operatorname{hol}(c_L) g(b_0)$. The extra ingredient is the conjugation-covariance of both sides; the payoff is that "$\operatorname{hol}(c_L) - 1 \approx -\int_{S_L} F$" is a frame-independent statement — a conjugation-covariant identity between two conjugation-covariant objects — so the curvature it recovers is the honest, gauge-covariant field.

Combine the conclusion with **a trace and an invariant polynomial**. Taking $\operatorname{tr}$ (or any Ad-invariant polynomial) of both sides kills the frame ambiguity entirely and yields $\operatorname{tr}(1_n - \operatorname{hol}(c_L)) = \int_{S_L}\operatorname{tr} F + O(L^3)$, a genuinely gauge-invariant scalar. The extra ingredient is Ad-invariance of the trace; the payoff is the Wilson-loop observable and, integrated against itself, the Chern–Weil forms of [[Def - Chern-Weil Form of an Invariant Polynomial|the next chapter]] — characteristic numbers read off from holonomy.

---

# Why Is It True

Strip away the bookkeeping and the mechanism is a single competition of orders of magnitude. Parallel transport around a loop is governed by the linear equation $\dot v = -A(c(\tau))(\dot c(\tau)) \, v$, and its solution operator — the holonomy — is the ordered exponential $\operatorname{Pexp}(-\int_c A)$, an infinite series whose $j$-th term is a $j$-fold ordered integral of the connection along the loop. Because the loop has length $O(L)$, each factor of the connection contributes a factor $O(L)$, so the $j$-th term is naively $O(L^j)$. If that were the whole story only the linear term would survive at leading order, and the answer would be $1 - \int_c A$. But the loop is *closed*, and around a closed loop the linear term is not $O(L)$ but $O(L^2)$: by Stokes, $\int_c A = \int_S dA$, and a $2$-form integrated over an area-$O(L^2)$ surface is $O(L^2)$. The leading $O(L)$ contributions cancel because the loop returns to where it started. This is the crucial gain: closure demotes the linear term by one power of $L$.

Once the linear term is $O(L^2)$, the *quadratic* term of the ordered exponential competes with it, and this is where non-commutativity enters. Split the quadratic term into its symmetric and antisymmetric parts under exchange of the two ordered factors. The symmetric part is exactly half the square of the linear integral, $\tfrac{1}{2}(\int_c A)^2$, hence $O(L^4)$ — negligible. The antisymmetric part is the commutator of the two factors, and *it does not vanish for a non-abelian group*. Freezing the connection at the base point (an $O(L)$ error) and applying Stokes once more turns this commutator integral into exactly $-\int_S A \wedge A$, the missing piece of the curvature. So the two surviving contributions at order $L^2$ are $-\int_S dA$ from the closed linear term and $-\int_S A \wedge A$ from the antisymmetric quadratic term, and together they are $-\int_S(dA + A \wedge A) = -\int_S F$.

> **The mechanism in one sentence:** to second order the holonomy of a small loop is $1$ minus the flux of the curvature through the loop, the $dA$ piece coming from the (closed) linear transport and the $A \wedge A$ piece coming from the non-commutativity of the ordered product of the connection along the loop.

The abelian case is the sanity check that makes the mechanism vivid. When $G$ is abelian every commutator vanishes, the antisymmetric part is zero, and the ordered exponential is an ordinary exponential; the identity is then exact, $\operatorname{hol}(c) = \exp(-\int_S dA)$, with no series and no error. The commutator term $A \wedge A$ is, quite literally, the price of ordering — the amount by which "transport out and back" fails to commute when the group does not.

---

# What Makes This Hard

The single non-obvious step is recognising that the linear term of the holonomy, though built from a length-$O(L)$ integral, is actually $O(L^2)$ because the loop is closed — everything downstream depends on this demotion, and a reader who leaves the linear term at $O(L)$ concludes, wrongly, that curvature never enters. The second trap is the error bookkeeping: one must show that *freezing* the connection coefficients at the base point and *replacing* the antisymmetric double integral by a line integral each cost only $O(L^3)$, which requires the $C^1$-control of $A$ (through $\lVert A_j(x) - A_j(0)\rVert \le \lVert A \rVert_{C^1}\lVert x\rVert$) and the area bound on $S$ — hypotheses that are easy to state and easy to forget to use. The common error is to declare "$\int_c A = \int_S dA$ so the linear term is $\int_S F$" and stop, which double-counts (it silently attributes the whole curvature to the linear term) and skips the genuinely non-abelian commutator computation that supplies $A \wedge A$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Write the holonomy as the ordered exponential of $-\int_c A$ and expand it to second order with an explicit $O(L^3)$ remainder. Show the first-order term equals $-\int_S dA$ by Stokes (hence $O(L^2)$), the symmetric half of the second-order term is $O(L^4)$, and the antisymmetric half equals $-\int_S A \wedge A + O(L^3)$ by freezing the coefficients and applying Stokes a second time. Add the two surviving $O(L^2)$ pieces to get $-\int_S(dA + A \wedge A) = -\int_S F$.

**Subgoal decomposition:**

1. **Identify the holonomy with the ordered exponential and expand to second order.**
   - *Hint:* Parallel transport solves $\dot v = -A(\dot c) v$; its solution operator is $\operatorname{Pexp}(-\int_c A)$, and the tail of the Dyson series past the quadratic term is bounded by $\tfrac{1}{6}e^{a} a^3$ with $a = \int_0^1 \lVert A(\dot c)\rVert \, d\tau = O(L)$.
   - *Why needed:* It reduces the whole problem to two universal integrals — one linear, one quadratic — plus a controlled remainder.

2. **Evaluate the first-order term by Stokes.**
   - *Hint:* $\int_0^1 A_{c}(\dot c) \, d\tau = \int_c A = \int_S dA$, and $\lVert\int_S dA\rVert \le \lVert dA \rVert_{C^0}\operatorname{area}(S) = O(L^2)$.
   - *Why needed:* It supplies the $-\int_S dA$ piece and shows the linear term is $O(L^2)$, so the quadratic term is not negligible against it.

3. **Discard the symmetric part of the second-order term.**
   - *Hint:* Symmetrising the ordered double integral over the full square gives $\tfrac{1}{2}(\int_c A)^2$, and $(\int_S dA)^2 = O(L^4)$.
   - *Why needed:* It removes half of the quadratic term at no cost, leaving only the commutator (antisymmetric) half.

4. **Evaluate the antisymmetric part: freeze, integrate, Stokes, bracket.**
   - *Hint:* Freeze $A_j$ at $b_0$ ($O(L)$ error over an $O(L^2)$ double integral $= O(L^3)$); do the inner $\tau_1$-integral to get $\int_c(x^k dx^j - x^j dx^k)$; Stokes gives $-2\int_S dx^j \wedge dx^k$; antisymmetrising the frozen coefficients turns $A_j(0)A_k(0)$ into $[A_j(0), A_k(0)]$.
   - *Why needed:* It produces $-\int_S A \wedge A$, the non-abelian half of the curvature.

5. **Assemble.**
   - *Hint:* First order $-\int_S dA$, symmetric $O(L^4)$, antisymmetric $-\int_S A\wedge A + O(L^3)$; sum and use $F = dA + A \wedge A$.
   - *Why needed:* It combines the surviving $O(L^2)$ contributions into the flux of the curvature.

---

# Lemma Decomposition

> [!note]- Lemma 1: Second-order Dyson expansion of the holonomy with an $O(L^3)$ remainder
> **Statement:** In the trivialisation $s_\alpha$ the holonomy of the loop $c = c_L$ is the path-ordered exponential $\operatorname{hol}(c) = \operatorname{Pexp}(-\int_c A)$, and, writing $a := \int_0^1 \lVert A_{c(\tau)}(\dot c(\tau))\rVert \, d\tau$,
> $$\operatorname{hol}(c) = 1_n - \int_0^1 A_{c(\tau)}(\dot c(\tau)) \, d\tau + \int_0^1 \! d\tau_2 \int_0^{\tau_2}\! d\tau_1 \, A_{c(\tau_2)}(\dot c(\tau_2)) \, A_{c(\tau_1)}(\dot c(\tau_1)) + R, \qquad \lVert R \rVert \le \tfrac{1}{6} e^{a} a^3.$$
> Since $a \le \lVert A \rVert_{C^0} \cdot \operatorname{length}(c) \le \lVert A \rVert_{C^0} CL$, one has $R = O(L^3)$.
>
> **Hint:** Use the Dyson series and its term bounds from the path-ordered-exponential theorem; bound the tail $\sum_{j \ge 3}$ by comparison with $e^a$.
>
> **Why needed:** It turns the holonomy into the two universal integrals the rest of the proof evaluates, with the error controlled from the start.
>
> > [!note]- Full proof
> > **Identify the holonomy with the ordered exponential.** By [[Def - Parallel Transport in a Principal Bundle|parallel transport]] and [[Def - Holonomy Group of a Connection|the definition of holonomy]], the holonomy $\operatorname{hol}(c) \in G$ of a loop $c$ at $b_0$ is the group element by which the horizontal lift fails to close, $\Gamma(c)(p) = p \cdot \operatorname{hol}(c)$ for the horizontal lift starting at $p = s_\alpha(b_0)$; equivalently, acting on the model fibre $\mathbb{K}^n$ in the defining representation, it is the solution operator at time $1$ of the linear parallel-transport equation
> > $$\dot v(\tau) = -A_{c(\tau)}(\dot c(\tau)) \, v(\tau), \qquad v(0) = v_0,$$
> > where $A_{c(\tau)}(\dot c(\tau)) = A_j(c(\tau)) \dot c^j(\tau) \in \mathfrak{g}$. This is the matrix-group form of the horizontal-lift ODE; the identification $\operatorname{hol}(c) = \operatorname{Pexp}(-\int_c A)$ is exactly the content of [[Def - Path-Ordered Exponential|the path-ordered exponential]] as the solution operator.
> >
> > **Restate the ordered-exponential theorem.** By [[Thm - The Path-Ordered Exponential Solves the Linear Parallel-Transport Equation|the path-ordered exponential theorem]] — *for continuous $A : [0, 1] \to \operatorname{Mat}(n \times n; \mathbb{K})$ the unique solution of $\dot v = -A v$, $v(0) = v_0$, is $v(1) = \sum_{j \ge 0} T_j v_0$ with*
> > $$T_j = (-1)^j \int_0^1 \! d\tau_j \int_0^{\tau_j}\! d\tau_{j-1} \cdots \int_0^{\tau_2}\! d\tau_1 \, A(\tau_j) \cdots A(\tau_1), \qquad \lVert T_j \rVert \le \frac{1}{j!}\left(\int_0^1 \lVert A(\tau)\rVert \, d\tau\right)^{\!j},$$
> > *the series converging absolutely and uniformly* — applied with $A(\tau) := A_{c(\tau)}(\dot c(\tau))$, we have $\operatorname{hol}(c) = \sum_{j \ge 0} T_j$. Setting $a := \int_0^1 \lVert A_{c(\tau)}(\dot c(\tau))\rVert \, d\tau$, the bound reads $\lVert T_j \rVert \le a^j / j!$.
> >
> > **Isolate the first three terms.** By construction $T_0 = 1_n$, $T_1 = -\int_0^1 A_{c(\tau)}(\dot c(\tau)) \, d\tau$, and $T_2 = \int_0^1 d\tau_2 \int_0^{\tau_2} d\tau_1 \, A_{c(\tau_2)}(\dot c(\tau_2)) A_{c(\tau_1)}(\dot c(\tau_1))$. Set $R := \sum_{j \ge 3} T_j$, so that $\operatorname{hol}(c) = 1_n + T_1 + T_2 + R$, which is the displayed expansion.
> >
> > **Bound the remainder.** For $j \ge 3$ we have $j!/(j-3)! = j(j-1)(j-2) \ge 6$, hence $a^j/j! = (a^3/6)\cdot 6 a^{j-3}/j! \le (a^3/6) \cdot a^{j-3}/(j-3)!$. Summing,
> > $$\lVert R \rVert \le \sum_{j \ge 3} \frac{a^j}{j!} \le \frac{a^3}{6}\sum_{j \ge 3}\frac{a^{j-3}}{(j-3)!} = \frac{a^3}{6}\sum_{m \ge 0}\frac{a^m}{m!} = \frac{a^3}{6}\,e^{a} \qquad \text{(re-index } m = j-3\text{, then the series for } e^a\text{)}.$$
> >
> > **Control $a$ by the length of the loop.** Since $\lVert A_{c(\tau)}(\dot c(\tau))\rVert = \lVert A_j(c(\tau))\dot c^j(\tau)\rVert \le \lVert A \rVert_{C^0}\lVert \dot c(\tau)\rVert$ (submultiplicativity and the definition of $\lVert A \rVert_{C^0}$ on the ball, which contains $c$), integrating gives $a \le \lVert A \rVert_{C^0}\int_0^1 \lVert \dot c \rVert \, d\tau = \lVert A \rVert_{C^0}\operatorname{length}(c) \le \lVert A \rVert_{C^0}CL$. For $L < L_0$ small enough that $\lVert A \rVert_{C^0}CL_0 \le 1$ we have $a \le 1$, so $e^a \le e$ and $\lVert R \rVert \le \tfrac{e}{6}(\lVert A \rVert_{C^0}CL)^3 = O(L^3)$, with the constant depending only on $C$ and $\lVert A \rVert_{C^0}$. This proves the claim. $\blacksquare$

> [!note]- Lemma 2: The first-order term is $-\int_S dA$, and it is $O(L^2)$
> **Statement:** With $c = c_L$ and $S = S_L$, the first-order term satisfies $T_1 = -\int_0^1 A_{c(\tau)}(\dot c(\tau))\,d\tau = -\int_c A = -\int_S dA$, and $\lVert \int_S dA \rVert \le \lVert dA \rVert_{C^0}\operatorname{area}(S) \le \lVert dA \rVert_{C^0}CL^2 = O(L^2)$.
>
> **Hint:** Apply Stokes' theorem entrywise to the matrix-valued $1$-form $A$, then bound a $2$-form integrated over an $O(L^2)$ surface.
>
> **Why needed:** It supplies the $dA$ half of the curvature and demotes the linear term from the naive $O(L)$ to $O(L^2)$, which is what lets the quadratic term contribute at the same order.
>
> > [!note]- Full proof
> > **Rewrite the term as a line integral.** By the definition of the integral of a $\mathfrak{g}$-valued $1$-form along a curve, $\int_0^1 A_{c(\tau)}(\dot c(\tau)) \, d\tau = \int_c A$; this holds entry by entry of the matrix $A$, as each scalar component $A^{(pq)}$ is an ordinary $1$-form and $\int_c A^{(pq)} = \int_0^1 A^{(pq)}_{c(\tau)}(\dot c(\tau))\,d\tau$.
> >
> > **Apply Stokes entrywise.** By [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] — *for a compact oriented surface $S$ with boundary $\partial S = c$ (compatibly oriented) and a smooth $1$-form $\eta$, $\int_{\partial S}\eta = \int_S d\eta$* — applied to each scalar component $A^{(pq)}$ (smooth on $U_\alpha \supset S$ by hypothesis), we get $\int_c A^{(pq)} = \int_S dA^{(pq)}$. Collecting the $n^2$ entries into the matrix, $\int_c A = \int_S dA$. Hence $T_1 = -\int_c A = -\int_S dA$.
> >
> > **Bound the size.** The $2$-form $dA$ has entries $dA^{(pq)} = \partial_i A^{(pq)}_j \, dx^i \wedge dx^j$, whose coefficient functions are bounded by $\lVert A \rVert_{C^1}$; integrating over $S$ and using that $S$ has area at most $CL^2$,
> > $$\Big\lVert \int_S dA \Big\rVert \le \lVert dA \rVert_{C^0}\operatorname{area}(S) \le \lVert dA \rVert_{C^0}\, CL^2 = O(L^2) \qquad \text{(triangle inequality for the entrywise integral; area bound on } S\text{)},$$
> > where $\lVert dA \rVert_{C^0}$ is controlled by $\lVert A \rVert_{C^1}$. Therefore $T_1 = -\int_S dA$ is of size $O(L^2)$. $\blacksquare$

> [!note]- Lemma 3: The symmetric part of the second-order term is $O(L^4)$
> **Statement:** Write the second-order term as $T_2 = I_s + I_a$ with
> $$I_{s/a} := \tfrac{1}{2}\int_0^1\! d\tau_2 \int_0^{\tau_2}\! d\tau_1 \big(A_{c(\tau_2)}(\dot c(\tau_2))\,A_{c(\tau_1)}(\dot c(\tau_1)) \mp A_{c(\tau_1)}(\dot c(\tau_1))\,A_{c(\tau_2)}(\dot c(\tau_2))\big).$$
> Then $2 I_s = \big(\int_0^1 A_{c(\tau)}(\dot c(\tau))\,d\tau\big)^2 = \big(\int_S dA\big)^2 = O(L^4)$, so $I_s = O(L^4)$ is absorbed into the $O(L^3)$ remainder.
>
> **Hint:** Extend the ordered domain $\{\tau_1 \le \tau_2\}$ to the full square by symmetry; recognise the result as the square of the first-order integral, then use Lemma 2.
>
> **Why needed:** It disposes of half the quadratic term without computation, leaving only the antisymmetric (commutator) half to evaluate.
>
> > [!note]- Full proof
> > **Symmetrise over the square.** Write $B(\tau) := A_{c(\tau)}(\dot c(\tau)) \in \mathfrak{g}$. By definition $2 I_s = \int_0^1 d\tau_2 \int_0^{\tau_2} d\tau_1 \big(B(\tau_2)B(\tau_1) + B(\tau_1)B(\tau_2)\big)$. Relabelling the dummy variables $(\tau_1, \tau_2) \leftrightarrow (\tau_2, \tau_1)$ in the second summand turns its domain $\{\tau_1 \le \tau_2\}$ into $\{\tau_2 \le \tau_1\}$ while leaving the integrand $B(\tau_2)B(\tau_1)$ (now with the swapped names) equal to $B(\tau_1)B(\tau_2)$; concretely,
> > $$\int_0^1\! d\tau_2\!\int_0^{\tau_2}\! d\tau_1\, B(\tau_1)B(\tau_2) = \iint_{\tau_2 \le \tau_1} B(\tau_2)B(\tau_1)\, d\tau_2\, d\tau_1 \qquad \text{(rename } \tau_1 \leftrightarrow \tau_2\text{)}.$$
> > Adding the two triangles, whose overlap is the measure-zero diagonal, recovers the full unit square:
> > $$2 I_s = \iint_{[0,1]^2} B(\tau_2)B(\tau_1)\, d\tau_2\, d\tau_1 = \Big(\int_0^1 B(\tau_2)\, d\tau_2\Big)\Big(\int_0^1 B(\tau_1)\, d\tau_1\Big) = \Big(\int_0^1 B(\tau)\, d\tau\Big)^2 \qquad \text{(Fubini; the double integral factorises)}.$$
> >
> > **Insert Lemma 2 and bound.** By Lemma 2, $\int_0^1 B(\tau)\, d\tau = \int_c A = \int_S dA$, so $2 I_s = (\int_S dA)^2$. Taking norms and using $\lVert \int_S dA \rVert = O(L^2)$ from Lemma 2 together with submultiplicativity,
> > $$\lVert I_s \rVert = \tfrac{1}{2}\big\lVert (\textstyle\int_S dA)^2\big\rVert \le \tfrac{1}{2}\big\lVert \textstyle\int_S dA\big\rVert^2 \le \tfrac{1}{2}(\lVert dA \rVert_{C^0}CL^2)^2 = O(L^4).$$
> > Hence $I_s = O(L^4)$, which is of smaller order than the $O(L^3)$ remainder and is absorbed into it. $\blacksquare$

> [!note]- Lemma 4: The antisymmetric part is $-\int_S A \wedge A + O(L^3)$
> **Statement:** With $I_a$ as in Lemma 3 and $A = A_j \, dx^j$ in coordinates centred at $b_0$,
> $$I_a = -\int_S A \wedge A + O(L^3) = -\sum_{j < k}[A_j(0), A_k(0)]\int_S dx^j \wedge dx^k + O(L^3),$$
> and the two expressions agree because $A \wedge A = \sum_{j<k}[A_j, A_k]\,dx^j \wedge dx^k$.
>
> **Hint:** Freeze the coefficients $A_j$ at $b_0$ (error $O(L^3)$), perform the inner $\tau_1$-integral to reach $\int_c(x^k dx^j - x^j dx^k)$, apply Stokes to get $-2\int_S dx^j \wedge dx^k$, and antisymmetrise the frozen coefficients into a commutator.
>
> **Why needed:** It produces the $A \wedge A$ half of the curvature — the entire non-abelian content of the theorem.
>
> > [!note]- Full proof
> > **Set up coordinates and expand.** Write $B(\tau) = A_{c(\tau)}(\dot c(\tau)) = A_j(c(\tau))\dot c^j(\tau)$ with the sum over $j = 1, \dots, m$. By definition,
> > $$2 I_a = \int_0^1\! d\tau_2 \int_0^{\tau_2}\! d\tau_1\big(B(\tau_2)B(\tau_1) - B(\tau_1)B(\tau_2)\big) = \int_0^1\! d\tau_2 \int_0^{\tau_2}\! d\tau_1\, A_j(c(\tau_2))A_k(c(\tau_1))\big(\dot c^j(\tau_2)\dot c^k(\tau_1) - \dot c^j(\tau_1)\dot c^k(\tau_2)\big),$$
> > where the second equality relabels the summation index in the second product ($B(\tau_1)B(\tau_2) = A_j(c(\tau_1))A_k(c(\tau_2))\dot c^j(\tau_1)\dot c^k(\tau_2)$, then swap the names $j \leftrightarrow k$ in that term so that the matrix product reads $A_j A_k$ throughout) and collects.
> >
> > **Freeze the coefficients at the base point.** Replace each $A_j(c(\tau))$ by its value $A_j(0)$ at $b_0$ (which has coordinates $0$). The replacement error in $A_j(c(\tau))$ is $A_j(c(\tau)) - A_j(0)$, and by the mean value inequality applied to each entry, using that $c(\tau)$ lies in the ball of radius $CL$,
> > $$\lVert A_j(c(\tau)) - A_j(0)\rVert \le \lVert A \rVert_{C^1}\,\lVert c(\tau)\rVert \le \lVert A \rVert_{C^1}\, CL = O(L) \qquad \text{(} C^1\text{-bound on } A\text{; } c(\tau) \in \overline{B}(b_0, CL)\text{)}.$$
> > The double integral of the remaining factors is bounded by
> > $$\int_0^1\! d\tau_2 \int_0^{\tau_2}\! d\tau_1\, \lVert \dot c(\tau_2)\rVert\,\lVert \dot c(\tau_1)\rVert \le \tfrac{1}{2}\Big(\int_0^1 \lVert \dot c\rVert\, d\tau\Big)^2 = \tfrac{1}{2}\operatorname{length}(c)^2 \le \tfrac{1}{2}(CL)^2 = O(L^2),$$
> > so each freezing replacement changes $2 I_a$ by at most $O(L) \cdot O(L^2) = O(L^3)$ (there are finitely many index pairs $(j, k)$, at most $m^2$, absorbed into the constant). Hence
> > $$2 I_a = A_j(0)A_k(0)\int_0^1\! d\tau_2 \int_0^{\tau_2}\! d\tau_1\big(\dot c^j(\tau_2)\dot c^k(\tau_1) - \dot c^j(\tau_1)\dot c^k(\tau_2)\big) + O(L^3).$$
> >
> > **Perform the inner integral.** Because $c(0) = b_0$ has coordinates $0$, the fundamental theorem of calculus gives $\int_0^{\tau_2}\dot c^k(\tau_1)\, d\tau_1 = c^k(\tau_2) - c^k(0) = c^k(\tau_2)$, and likewise $\int_0^{\tau_2}\dot c^j(\tau_1)\, d\tau_1 = c^j(\tau_2)$. Therefore, treating $\tau_2$ as the outer variable,
> > $$\int_0^1\! d\tau_2 \int_0^{\tau_2}\! d\tau_1\big(\dot c^j(\tau_2)\dot c^k(\tau_1) - \dot c^j(\tau_1)\dot c^k(\tau_2)\big) = \int_0^1\big(\dot c^j(\tau_2)\,c^k(\tau_2) - c^j(\tau_2)\,\dot c^k(\tau_2)\big)\, d\tau_2 = \int_c\big(x^k\, dx^j - x^j\, dx^k\big),$$
> > the last equality being the definition of the line integral of the $1$-form $x^k\, dx^j - x^j\, dx^k$ along $c$. (The source's transcription writes $\dot c^k(\tau_1)$ for the second factor here; the corrected index is $\tau_2$, as forced by the completed inner integration, and is used above.)
> >
> > **Apply Stokes a second time.** By [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] with $\partial S = c$, and computing $d(x^k\, dx^j - x^j\, dx^k) = dx^k \wedge dx^j - dx^j \wedge dx^k = -2\, dx^j \wedge dx^k$ (since $dx^k \wedge dx^j = -dx^j \wedge dx^k$),
> > $$\int_c\big(x^k\, dx^j - x^j\, dx^k\big) = \int_S d\big(x^k\, dx^j - x^j\, dx^k\big) = -2\int_S dx^j \wedge dx^k.$$
> > Substituting,
> > $$2 I_a = A_j(0)A_k(0)\cdot\big(-2\textstyle\int_S dx^j \wedge dx^k\big) + O(L^3), \qquad\text{so}\qquad I_a = -A_j(0)A_k(0)\int_S dx^j \wedge dx^k + O(L^3),$$
> > with the sum over all ordered pairs $(j, k)$.
> >
> > **Antisymmetrise into a commutator.** The $2$-form coefficient $\int_S dx^j \wedge dx^k$ is antisymmetric in $(j, k)$, so only the antisymmetric part of the matrix coefficient $A_j(0)A_k(0)$ survives the sum: pairing $(j, k)$ with $(k, j)$,
> > $$A_j(0)A_k(0)\int_S dx^j \wedge dx^k = \sum_{j<k}\big(A_j(0)A_k(0) - A_k(0)A_j(0)\big)\int_S dx^j \wedge dx^k = \sum_{j<k}[A_j(0), A_k(0)]\int_S dx^j \wedge dx^k.$$
> > Hence $I_a = -\sum_{j<k}[A_j(0), A_k(0)]\int_S dx^j \wedge dx^k + O(L^3)$.
> >
> > **Unfreeze the bracket to recover $\int_S A \wedge A$.** By [[Def - Lie-Algebra-Valued Differential Forms and Their Bracket|the wedge of matrix-valued forms]], $A \wedge A = A_j A_k\, dx^j \wedge dx^k = \sum_{j<k}[A_j, A_k]\, dx^j \wedge dx^k$, so $\int_S A \wedge A = \sum_{j<k}\big(\int_S [A_j, A_k]\, dx^j \wedge dx^k\big)$ with *variable* coefficients. The difference between the frozen and variable versions is bounded by the same freezing estimate: for each $j < k$,
> > $$\Big\lVert \int_S\big([A_j, A_k] - [A_j(0), A_k(0)]\big)\, dx^j \wedge dx^k\Big\rVert \le \sup_S\lVert [A_j, A_k] - [A_j(0), A_k(0)]\rVert \cdot \operatorname{area}(S) \le O(L)\cdot O(L^2) = O(L^3),$$
> > where the sup is $O(L)$ because $[A_j, A_k](x) - [A_j, A_k](0)$ is $C^1$ in $x$ with $\lVert x \rVert \le CL$ and $\lVert [A_j, A_k]\rVert$ is controlled by $\lVert A \rVert_{C^0}\lVert A \rVert_{C^1}$. Therefore
> > $$I_a = -\sum_{j<k}[A_j(0), A_k(0)]\int_S dx^j \wedge dx^k + O(L^3) = -\int_S A \wedge A + O(L^3). \qquad \blacksquare$$

---

# Formal Proof

> [!note]- Complete formal proof
> We must show that, under the stated hypotheses, $\operatorname{hol}(c_L) = 1_n - \int_{S_L} F + O(L^3)$ as $L \searrow 0$, with $F = dA + A \wedge A$ and the $O(L^3)$ constant depending only on $C$, $n$, and $\lVert A \rVert_{C^1}$ on the ball $\overline{B}(b_0, CL_0)$. Fix $L \in (0, L_0)$ and abbreviate $c := c_L$, $S := S_L$.
>
> **Step 0 — the objects are well posed.** For $L < L_0$ small enough, $S \subset U_\alpha$ (given), so $A = s_\alpha^*\omega$ and $F = s_\alpha^*\Omega$ are defined and smooth on a neighbourhood of $S$; the coordinates centred at $b_0$ cover $S$; and $c$ is a piecewise smooth loop at $b_0$ parametrised proportionally to arc length, so $\lVert \dot c(\tau)\rVert = \operatorname{length}(c) \le CL$ is constant in $\tau$. The holonomy $\operatorname{hol}(c) \in G$ is defined by [[Def - Holonomy Group of a Connection|the holonomy of a loop]], and in the trivialisation $s_\alpha$ it acts on the model fibre $\mathbb{K}^n$ as the time-$1$ solution operator of the parallel-transport equation. All quantities below are entrywise integrals of continuous matrix-valued functions and hence exist.
>
> **Step 1 — expand the holonomy to second order (Lemma 1).** By Lemma 1,
> $$\operatorname{hol}(c) = 1_n + T_1 + T_2 + R, \qquad T_1 = -\int_0^1 A_{c(\tau)}(\dot c(\tau))\, d\tau, \quad T_2 = \int_0^1\! d\tau_2\!\int_0^{\tau_2}\! d\tau_1\, A_{c(\tau_2)}(\dot c(\tau_2))A_{c(\tau_1)}(\dot c(\tau_1)),$$
> with $\lVert R \rVert \le \tfrac{1}{6}e^a a^3 = O(L^3)$, where $a = \int_0^1\lVert A_{c(\tau)}(\dot c(\tau))\rVert\, d\tau \le \lVert A \rVert_{C^0}CL$. This uses the identification $\operatorname{hol}(c) = \operatorname{Pexp}(-\int_c A)$ and the term bounds of [[Thm - The Path-Ordered Exponential Solves the Linear Parallel-Transport Equation|the path-ordered exponential theorem]].
>
> **Step 2 — evaluate the first-order term (Lemma 2).** By Lemma 2, $T_1 = -\int_c A = -\int_S dA$ (Stokes, applied entrywise), and $\lVert \int_S dA \rVert \le \lVert dA \rVert_{C^0}CL^2 = O(L^2)$. Thus the linear term contributes exactly $-\int_S dA$, of size $O(L^2)$.
>
> **Step 3 — split the second-order term and discard its symmetric half (Lemma 3).** Write $T_2 = I_s + I_a$ as in Lemma 3. By Lemma 3, $2 I_s = (\int_S dA)^2$, so $I_s = O(L^4)$ and is absorbed into the $O(L^3)$ error.
>
> **Step 4 — evaluate the antisymmetric half (Lemma 4).** By Lemma 4, $I_a = -\int_S A \wedge A + O(L^3)$, obtained by freezing the connection coefficients at $b_0$ (error $O(L^3)$, by the $C^1$-bound on $A$ and the area bound on $S$), integrating the inner variable to reach $\int_c(x^k\, dx^j - x^j\, dx^k)$, applying Stokes to get $-2\int_S dx^j \wedge dx^k$, and antisymmetrising $A_j(0)A_k(0)$ into $[A_j(0), A_k(0)]$; the identity $A \wedge A = \sum_{j<k}[A_j, A_k]\, dx^j \wedge dx^k$ restores the variable coefficients.
>
> **Step 5 — assemble.** Combining Steps 1–4,
> $$\operatorname{hol}(c) = 1_n + T_1 + (I_s + I_a) + R = 1_n - \int_S dA + O(L^4) + \Big(-\int_S A \wedge A + O(L^3)\Big) + O(L^3),$$
> where the two named $O(L^3)$ terms are the remainder $R$ (Step 1) and the freezing errors (Step 4), and $O(L^4)$ is $I_s$ (Step 3). All error terms combine into a single $O(L^3)$ with constant depending only on $C$, $n$, and $\lVert A \rVert_{C^1}$ (each contributing constant was of this form: $\tfrac{e}{6}(\lVert A \rVert_{C^0}C)^3$ from $R$; $\lVert dA \rVert_{C^0}^2 C^2 /2$ from $I_s$; and $O(L)\cdot O(L^2)$ freezing constants built from $\lVert A \rVert_{C^1}$, $C$, and $m \le$ (a bound depending on $n$) from Step 4). Therefore
> $$\operatorname{hol}(c) = 1_n - \int_S dA - \int_S A \wedge A + O(L^3) = 1_n - \int_S\big(dA + A \wedge A\big) + O(L^3) = 1_n - \int_S F + O(L^3),$$
> using the linearity of the integral and, in the last step, the identification $F = dA + A \wedge A = dA + \tfrac{1}{2}[A \wedge A]$ from [[Thm - Structure Equation for the Curvature|the structure equation]] — *the principal curvature is $\Omega = d\omega + \tfrac{1}{2}[\omega \wedge \omega]$, with local form $F = s_\alpha^*\Omega = dA + \tfrac{1}{2}[A \wedge A]$, equal to $dA + A \wedge A$ for a matrix group*.
>
> **Conclusion.** To second order in $L$, the holonomy of the small loop $c_L$ differs from the identity by exactly the flux of the curvature through the bounded surface: $\operatorname{hol}(c_L) = 1_n - \int_{S_L} F + O(L^3)$. The $-\int_{S_L} dA$ piece is the (closed) linear transport and the $-\int_{S_L} A \wedge A$ piece is the second-order residue of the non-commutativity of the ordered product; together they are the full curvature. Therefore curvature is the infinitesimal holonomy. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Riemannian geometry: the Gauss map and the angle defect.** Apply the theorem to the Levi-Civita connection on the tangent bundle of a surface, written as an $SO(2)$-connection in a local orthonormal frame. The holonomy around a small geodesic triangle is a rotation, and the theorem identifies its angle with $-\int_S F$, where $F$ is the curvature $2$-form; since $SO(2)$ is abelian the ordering term drops out and one recovers the Gauss–Bonnet angle defect $\int_S K\, dA$ exactly. This applies because a geodesic triangle of side $L$ is a loop satisfying every hypothesis, and it is non-obvious because the "rotation of a parallel-transported vector" is usually presented as a global integral rather than as the leading term of a holonomy expansion; the exercise is to see the two as the same fact, and to notice that the theorem's error term is *absent* here precisely because of abelianness.

**Lattice gauge theory: the continuum limit of the Wilson action.** Take a hypercubic lattice with spacing $L$ and $G$-valued link variables, and let $U_\square = \operatorname{hol}(c_L)$ be the plaquette product around an elementary square of side $L$. The theorem gives $1_n - U_\square = \int_{S_L} F + O(L^3) = F_{\mu\nu}L^2 + O(L^3)$ for the coordinate plane $\mu\nu$, so the Wilson action density $\operatorname{Re}\operatorname{tr}(1_n - U_\square)$ expands as $\tfrac{1}{2}\lVert F_{\mu\nu}\rVert^2 L^4 + \dots$, reproducing the Yang–Mills Lagrangian. This applies because plaquettes are the square loops of the theorem, and it is non-obvious because the discrete link product carries no manifest curvature; the exercise extracts the field strength as the imaginary/anti-Hermitian part of the plaquette at second order.

**Quantum mechanics: the Berry phase and the Berry curvature.** For a family of Hamiltonians $H(x)$ with a non-degenerate ground state, adiabatic transport defines a $U(1)$-connection (Berry connection) whose holonomy around a small loop in parameter space is the Berry phase. The theorem gives the phase as $-\int_S F$ with $F$ the Berry curvature, and for degenerate levels the non-abelian ($U(k)$) version keeps the $A \wedge A$ term as the non-abelian Berry curvature. This applies because parameter-space loops of size $L$ satisfy the hypotheses, and it is non-obvious because the Berry phase is defined by an adiabatic limit rather than a transport ODE; the exercise is to identify the adiabatic holonomy with $\operatorname{Pexp}(-\int_c A)$ and read off the curvature.

---

# Bridges

- **The non-abelian Stokes theorem.** Tiling a surface $S$ by small plaquettes $c_L^{(i)}$ and multiplying their holonomies in order — the shared edges cancel by $\operatorname{hol}(c^{-1}) = \operatorname{hol}(c)^{-1}$ from [[Thm - Properties of Parallel Transport|the properties of parallel transport]] — turns the pointwise expansion of this page into the surface-ordered exponential $\operatorname{hol}(\partial S) = \operatorname{Pexp}_S(-\int_S F)$. Each plaquette contributes $1 - \int_{S^{(i)}} F + O(L^3)$; the product of these across the mesh, as $L \to 0$, is the surface-ordered integral, and the leading correction is the honest surface integral of the curvature. This page is the single-plaquette input; the bridge is the passage to the whole surface.

- **The Ambrose–Singer theorem.** This page proves that curvature is the *derivative* of holonomy at a point: $\tfrac{d}{d(\text{area})}\operatorname{hol} = -F$. The Ambrose–Singer theorem is the integrated converse — the Lie algebra of the holonomy group is spanned by the curvature values $\operatorname{hol}(\gamma)^{-1}F(X, Y)\operatorname{hol}(\gamma)$ transported to the base point over all loops $\gamma$ and all $X, Y$. The construction is to differentiate the holonomy of the "lasso" loops (a path out, a small loop, the path back) using exactly the expansion proved here, and to check that the resulting Lie subalgebra is closed under bracket. This page supplies the infinitesimal generator; Ambrose–Singer assembles the generators into the holonomy Lie algebra.

- **The field strength of gauge theory.** In physics the Yang–Mills field strength $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu + [A_\mu, A_\nu]$ is *defined* by the small-loop holonomy: $\operatorname{hol}(\square_{\mu\nu}) = 1 - F_{\mu\nu}L^2 + O(L^3)$ for the coordinate square in the $\mu\nu$-plane. This is precisely the theorem, read in coordinates: expanding $\int_S F$ over the square of side $L$ gives $F_{\mu\nu}L^2$, and the commutator piece $[A_\mu, A_\nu]$ is the coordinate form of $A \wedge A$. The bridge is that the operational, measurement-based definition of the field (parallel transport around a plaquette) coincides with the differential-geometric curvature — the content that makes $F_{\mu\nu}$ gauge-covariant and observable through Wilson loops.

---

# Unlocked by This

> [!tip] Wilson loops and confinement *(from Yang–Mills theory)*
> The trace $W(c) = \operatorname{tr}\operatorname{hol}(c)$ of the holonomy is the gauge-invariant Wilson loop; this page's small-loop expansion, $W(c_L) = n - \int_{S_L}\operatorname{tr} F + O(L^3)$, is its short-distance behaviour, and the large-loop behaviour (area versus perimeter law) is the order parameter for confinement. See **Yang–Mills Theory (VII)**.

> [!tip] The Ambrose–Singer holonomy theorem *(from the holonomy of connections)*
> The reconstruction of the holonomy Lie algebra from the curvature values over all loops, whose infinitesimal input is exactly this page's expansion. See **Ambrose–Singer Theorem**.
