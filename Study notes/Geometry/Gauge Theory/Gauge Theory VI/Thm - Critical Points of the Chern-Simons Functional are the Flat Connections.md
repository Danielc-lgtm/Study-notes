---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Chern-Simons Functional"
  - "Def - Flat Connection"
  - "Thm - Stokes' Theorem on Manifolds"
  - "Thm - Curvature of a Shifted Connection"
  - "Thm - The Space of Connections is an Affine Space"
  - "Thm - Gauge Transformations Act on Connections and Curvature"
  - "Thm - Gauge Variation of the Chern-Simons Functional"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ is a **closed** — that is, compact and without boundary — oriented smooth three-manifold, and $P \to M$ is a principal $SU(2)$-bundle. Chapter III shows that every principal $SU(2)$-bundle over a manifold of dimension at most three is trivial, so we fix once and for all a global trivialisation of $P$. Under it a connection on $P$ is recorded by its local connection form, a single $\mathfrak{su}(2)$-valued one-form
$$A \in \Omega^1(M; \mathfrak{su}(2)) = \Gamma\big(T^*M \otimes \mathfrak{su}(2)\big),$$
and the affine space of all connections $\mathcal{A}(P)$ is thereby identified with the vector space $\Omega^1(M; \mathfrak{su}(2))$ (a choice of base connection — here the trivial connection $A = 0$ — turns the affine space into a vector space; that $\mathcal{A}(P)$ is affine over $\Omega^1(M; \operatorname{ad}P) \cong \Omega^1(M;\mathfrak{su}(2))$ is [[Thm - The Space of Connections is an Affine Space|the affine-space theorem]]).

Here $\mathfrak{su}(2)$ is the Lie algebra of $SU(2)$, the real vector space of **traceless skew-Hermitian** complex $2 \times 2$ matrices,
$$\mathfrak{su}(2) = \{\xi \in \mathfrak{gl}_2(\mathbb{C}) : \xi^* = -\xi,\ \operatorname{tr}\xi = 0\},$$
where $\xi^* = \overline{\xi}^{\,\mathsf T}$ is the conjugate transpose; it is three-dimensional over $\mathbb{R}$, with basis the anti-Hermitian Pauli matrices $-i\sigma_1, -i\sigma_2, -i\sigma_3$. The symbol $\operatorname{tr}$ always denotes the ordinary matrix trace in the defining (two-dimensional) representation.

A **$\mathfrak{su}(2)$-valued $p$-form** on $M$ is an element of $\Omega^p(M; \mathfrak{su}(2)) = \Gamma(\Lambda^p T^*M \otimes \mathfrak{su}(2))$; in a chart it is written $\alpha = \sum_I \alpha_I\, dx^I$ with each coefficient $\alpha_I$ a smooth $\mathfrak{su}(2)$-valued function. For $\alpha \in \Omega^p(M;\mathfrak{su}(2))$ and $\beta \in \Omega^q(M;\mathfrak{su}(2))$, the **wedge product with matrix multiplication** $\alpha \wedge \beta \in \Omega^{p+q}(M; \mathfrak{gl}_2(\mathbb{C}))$ is defined in a chart by $\alpha \wedge \beta = \sum_{I,J} (\alpha_I \beta_J)\, dx^I \wedge dx^J$, where $\alpha_I \beta_J$ is the matrix product; this is the meaning of every juxtaposition of matrix-valued forms below. The **trace** $\operatorname{tr}(\alpha) \in \Omega^p(M)$ is the ordinary scalar form obtained by applying $\operatorname{tr}$ to each coefficient matrix. The exterior derivative $d$ acts entrywise on matrix-valued forms; since $\operatorname{tr}$ is a fixed linear map with constant coefficients, $d\operatorname{tr}(\alpha) = \operatorname{tr}(d\alpha)$.

The **curvature** of $A$ in the fixed trivialisation is
$$F_A = dA + A \wedge A \in \Omega^2(M; \mathfrak{su}(2)),$$
the local curvature form of the connection $\nabla = d + A$; the identity $F_A = dA + A \wedge A$ is the specialisation of [[Thm - Curvature of a Shifted Connection|the shifted-connection theorem]] to the trivial base connection, recalled at the point of use. For a matrix group the bracket term of the general structure equation collapses, $\tfrac12[A \wedge A] = A \wedge A$, so no factor of $\tfrac12$ appears; this is the standing series convention.

The **Chern–Simons form** and **Chern–Simons functional** are
$$\operatorname{cs}(A) := \operatorname{tr}\!\Big(A \wedge dA + \tfrac23\, A \wedge A \wedge A\Big) \in \Omega^3(M), \qquad \vartheta(A) := \frac{1}{8\pi^2} \int_M \operatorname{cs}(A) \in \mathbb{R}/\mathbb{Z},$$
as defined on [[Def - Chern-Simons Functional|the Chern–Simons functional page]]. The reduction modulo $\mathbb{Z}$ is forced: changing the trivialisation of $P$ changes the real number $\tfrac{1}{8\pi^2}\int_M \operatorname{cs}(A)$ by an integer, so only its residue class is trivialisation-independent. We write $\widetilde\vartheta(A) := \tfrac{1}{8\pi^2}\int_M \operatorname{cs}(A) \in \mathbb{R}$ for the genuine real number computed in the fixed trivialisation, so that $\vartheta = \widetilde\vartheta \bmod \mathbb{Z}$.

The **gauge group** is $\mathcal{G}(P) \cong \operatorname{Map}(M, SU(2))$ (a gauge transformation, read through the trivialisation, is a smooth map $g\colon M \to SU(2)$), acting on connections on the right by $A \cdot g = g^{-1} A g + g^{-1} dg$. A connection is **flat** when $F_A = 0$ ([[Def - Flat Connection|the flat-connection definition]]).

> [!warning] Convention: the trace pairing and its sign
> The bilinear form used throughout is $\langle \xi, \eta \rangle := -\operatorname{tr}(\xi \eta)$ on $\mathfrak{su}(2)$; the minus sign makes it positive definite (Lemma 4), because $\operatorname{tr}(\xi^2) \le 0$ for anti-Hermitian $\xi$. Haydys writes the functional exactly as $\vartheta(A) = \tfrac1{8\pi^2}\int_M \operatorname{tr}(A \wedge dA + \tfrac23 A\wedge A\wedge A)$ (his §3.2, equation following (95)); we follow this normalisation verbatim. The first-variation computation on this page reproduces Haydys's displayed identity $d\vartheta_A(a) = \tfrac1{4\pi^2}\int_M \operatorname{tr}(F_A \wedge a)$ (his p. 31), filling the two steps he leaves implicit — the integration by parts and the non-degeneracy of the pairing. No source typo affects the items covered here (Haydys's Appendix-B correction, the missing $\tfrac1{8\pi^2}$ in Exercise 96(a), concerns a different display and is handled on [[Thm - The Four-Dimensional Formula for the Chern-Simons Functional|the four-dimensional-formula page]]).

---

# Statement

> **Theorem (critical points of the Chern–Simons functional).** Let $M$ be a closed oriented smooth three-manifold and $P \to M$ a principal $SU(2)$-bundle, trivialised, so that a connection is a form $A \in \Omega^1(M; \mathfrak{su}(2))$ and
> $$\vartheta(A) = \frac{1}{8\pi^2}\int_M \operatorname{tr}\!\Big(A \wedge dA + \tfrac23\, A \wedge A \wedge A\Big) \in \mathbb{R}/\mathbb{Z}, \qquad F_A = dA + A \wedge A.$$
>
> **(i) First variation.** For all $A, a \in \Omega^1(M; \mathfrak{su}(2))$,
> $$\frac{d}{ds}\Big|_{s=0} \vartheta(A + sa) = \frac{1}{4\pi^2} \int_M \operatorname{tr}(F_A \wedge a).$$
>
> **(ii) Critical points are flat.** The connection $A$ is a critical point of $\vartheta$ — that is, the linear functional $d\vartheta_A\colon a \mapsto \tfrac{d}{ds}\big|_0 \vartheta(A+sa)$ on $\Omega^1(M;\mathfrak{su}(2))$ vanishes identically — if and only if $A$ is flat, $F_A = 0$.
>
> **(iii) Descent to the orbit space.** The functional $\vartheta$ is gauge invariant and descends to a map $\mathcal{A}(P)/\mathcal{G}(P) \to \mathbb{R}/\mathbb{Z}$, and flatness is a gauge-invariant condition; hence the critical set of $\vartheta$ on $\mathcal{A}(P)/\mathcal{G}(P)$ is exactly the set of gauge-equivalence classes of flat connections.

---

# Motivation

The Chern–Simons functional is the three-dimensional shadow of the second Chern class. On a four-manifold the four-form $\operatorname{tr}(F_A \wedge F_A)$ measures the instanton number; the [[Thm - Transgression Formula and the Chern-Simons Form|transgression formula]] shows that this four-form is exact whenever the bundle is trivial, with primitive precisely the Chern–Simons three-form: $d\operatorname{cs}(A) = \operatorname{tr}(F_A \wedge F_A)$. Integrating the primitive over a closed three-manifold produces a number — up to the integer ambiguity that records which four-manifold one imagines bounding $M$. So $\vartheta$ is a canonical real-valued (modulo $\mathbb{Z}$) function on the infinite-dimensional space of connections, and it is natural to ask the question one asks of any function: where are its critical points, and what do they mean?

The answer is as clean as it could be. The critical points are exactly the flat connections. This is the geometric content of the slogan that **the Chern–Simons functional is the antiderivative of the curvature**: its first variation at $A$, in the direction $a$, is the pairing of the curvature $F_A$ against $a$. A function whose derivative is (a pairing with) the curvature has its stationary points precisely where the curvature vanishes, exactly as an ordinary primitive $F(x) = \int^x f$ has its stationary points where $f$ vanishes. The Chern–Simons functional is the honest infinite-dimensional realisation of that picture.

This matters because flat connections are the objects of central interest in three-dimensional gauge theory, and this theorem is the bridge that makes them accessible by variational methods. Flat connections are the "vacua" — the ground states — of Chern–Simons gauge theory; by [[Thm - Flat Connections and Monodromy Representations of the Fundamental Group|the monodromy theorem]] they correspond, up to gauge, to conjugacy classes of representations $\pi_1(M) \to SU(2)$, so the critical set of $\vartheta$ is the $SU(2)$-representation variety of $\pi_1(M)$. Regarding $\vartheta$ as a Morse function on the orbit space $\mathcal{A}/\mathcal{G}$, whose critical points are the flat connections and whose gradient flow lines are anti-self-dual instantons on $M \times \mathbb{R}$, is the starting point of instanton Floer homology. All of that programme rests on the single computation carried out here: that the first variation of $\vartheta$ is a pairing with the curvature, and that this pairing is non-degenerate.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypotheses of the theorem — a closed oriented three-manifold and an $SU(2)$-bundle — are mild, so the useful "source" question is: in which disguised situations does one get to invoke the first-variation formula and read off flatness?

The first disguised source is **a variational problem on connections whose action can be written in Chern–Simons form**. Whenever a functional $S$ on the space of connections of a trivialised $SU(2)$-bundle over a closed three-manifold has the shape $S(A) = c\int_M \operatorname{tr}(A \wedge dA + \tfrac23 A^{\wedge 3})$ for a constant $c$, this theorem hands you its Euler–Lagrange equation for free: the equation of motion is $F_A = 0$. The non-obvious bridge is recognising a given physical action as a multiple of $\operatorname{cs}$; once recognised, no further variation is needed. *Example problem:* in the physics literature the level-$k$ Chern–Simons action is $S_k(A) = \tfrac{k}{4\pi}\int_M \operatorname{tr}(A \wedge dA + \tfrac23 A^{\wedge 3})$; deduce that its classical solutions are the flat connections regardless of the level $k$, because scaling the action by a nonzero constant does not move its critical points.

The second disguised source is **a one-parameter family of connections whose energy you wish to differentiate**. Any smooth path $s \mapsto A_s$ in $\mathcal{A}$ with $A_0 = A$ and $\tfrac{d}{ds}\big|_0 A_s = a$ has $\tfrac{d}{ds}\big|_0 \vartheta(A_s) = \tfrac1{4\pi^2}\int_M \operatorname{tr}(F_A \wedge a)$, by the chain rule and part (i), because $\vartheta$ is a polynomial functional and only the initial velocity $a$ enters the first derivative. The bridge is that the affine structure of $\mathcal{A}$ lets one replace an arbitrary path by the straight line $A + sa$ with the same initial velocity ([[Thm - The Space of Connections is an Affine Space|the affine-space theorem]]). *Example problem:* along a gradient-flow line of $\vartheta$, identify $\tfrac{d}{ds}\vartheta(A_s)$ with the $L^2$-norm-squared of the curvature, so that the flow decreases $\vartheta$ until it reaches a flat connection.

The third disguised source is **a closed three-manifold together with a homomorphism $\rho\colon \pi_1(M) \to SU(2)$**. Such a $\rho$ builds a flat connection (its associated flat bundle carries a canonical flat connection), and this theorem then certifies that this connection is a critical point of $\vartheta$. The bridge runs through [[Thm - Flat Connections and Monodromy Representations of the Fundamental Group|the monodromy theorem]], which converts the algebraic datum $\rho$ into the geometric datum $A$ with $F_A = 0$. *Example problem:* for $M$ the three-torus $T^3$, every triple of commuting elements of $SU(2)$ gives a flat connection and hence a critical point of $\vartheta$, and one computes the critical value.

**Targets (Output Amplification).** The bare conclusion — critical set equals flat connections — combines with further ingredients into much more.

Combine the conclusion with **the monodromy theorem for flat connections** (chapter V/VI). Flat connections modulo gauge are in bijection with conjugacy classes of representations $\pi_1(M) \to SU(2)$, so the critical set of $\vartheta$ on $\mathcal{A}/\mathcal{G}$ *is* the representation variety $\operatorname{Hom}(\pi_1(M), SU(2))/\text{conjugation}$. The extra ingredient is the correspondence between flatness and monodromy; the payoff is that a differential-geometric variational problem is identified with an algebraic moduli space, opening it to both differential-topological and representation-theoretic tools.

Combine the conclusion with **the second-variation (Hessian) of $\vartheta$ at a flat connection**. The Hessian of $\vartheta$ at a critical point $A$ is the operator $a \mapsto \tfrac1{4\pi^2}\, d^A a$ (obtained by differentiating $F_A = dA + A\wedge A$), whose kernel modulo the gauge directions is the twisted cohomology $H^1(M; \operatorname{ad}A)$. The extra ingredient is elliptic Hodge theory for the twisted de Rham complex (chapter IX); the payoff is a description of the local structure of the critical set — smoothness, dimension, and obstruction — in cohomological terms, which is exactly the deformation theory a Morse-theoretic count needs.

Combine the conclusion with **the anti-self-duality equation on $M \times \mathbb{R}$** (chapter VII). The downward gradient trajectories of $\vartheta$, in the natural $L^2$ metric on $\mathcal{A}$, are precisely the anti-self-dual connections on the cylinder $M \times \mathbb{R}$ that are asymptotic to flat connections at the two ends. The extra ingredient is the Yang–Mills / instanton machinery; the payoff is **instanton Floer homology**, the homology of a chain complex generated by the flat connections (the critical points) with differential counting instantons (the gradient lines) — the deepest downstream consequence of this theorem.

---

# Why Is It True

Set aside the formal bookkeeping and think of $\vartheta$ as a function on the vector space $V = \Omega^1(M; \mathfrak{su}(2))$. In coordinates on this space the functional is a **cubic polynomial**: a quadratic piece $\tfrac1{8\pi^2}\int_M \operatorname{tr}(A \wedge dA)$ coming from the $A \wedge dA$ term, and a cubic piece $\tfrac1{12\pi^2}\int_M \operatorname{tr}(A^{\wedge 3})$ coming from the $\tfrac23 A^{\wedge 3}$ term. To find the derivative of a cubic polynomial one perturbs $A \rightsquigarrow A + sa$ and collects the coefficient of $s^1$; that is all the first variation is.

When one does this, the quadratic term $\operatorname{tr}(A \wedge dA)$ produces two pieces, $\operatorname{tr}(a \wedge dA)$ and $\operatorname{tr}(A \wedge da)$, that look different but become equal after **integration by parts** — the boundary term vanishes because $M$ is closed, and this is the only place compactness-without-boundary is used. The cubic term produces three pieces, $\operatorname{tr}(a \wedge A \wedge A)$ in its three cyclic positions, which become equal after using the **graded cyclicity of the trace**. Adding everything up, the linear-in-$a$ part reorganises exactly into $\operatorname{tr}(a \wedge (dA + A\wedge A)) = \operatorname{tr}(a \wedge F_A)$. The whole computation is the observation that the differential of a cubic reassembles the curvature $dA + A\wedge A$ out of the derivative term $dA$ (from the quadratic) and the quadratic term $A \wedge A$ (from the cubic).

> **The mechanism in one sentence: the first variation of $\vartheta$ pairs the perturbation $a$ against the curvature $F_A = dA + A\wedge A$, because integration by parts turns the derivative term of $\operatorname{cs}$ into $dA$ and cyclicity turns its cubic term into $A\wedge A$, and these are precisely the two summands of the curvature.**

Once the first variation is $\tfrac1{4\pi^2}\int_M \operatorname{tr}(F_A \wedge a)$, half the theorem is immediate: if $F_A = 0$ then every directional derivative is zero, so $A$ is critical. The other half needs one more fact — that this pairing is not accidentally zero. If $F_A \ne 0$ somewhere, we must exhibit a direction $a$ in which $\vartheta$ actually changes. Here the sign convention on $\mathfrak{su}(2)$ does the work: $-\operatorname{tr}$ is a genuine inner product, so $\operatorname{tr}(F_A \wedge a)$ can be made pointwise equal to $|F_A|^2$ times the volume element by choosing $a$ to be the appropriate "dual" of $F_A$, and then the integral is strictly positive. In other words, the pairing $(F, a) \mapsto \int_M \operatorname{tr}(F \wedge a)$ is non-degenerate, so a curvature that survives the pairing against every $a$ must have been zero to begin with.

---

# What Makes This Hard

Two steps are routinely skipped and each hides a real point. The first is the **integration by parts**: one must know that $\operatorname{tr}(A \wedge da)$ and $\operatorname{tr}(dA \wedge a)$ differ by an exact form $d\operatorname{tr}(A \wedge a)$ whose integral over the closed manifold vanishes — the sign in the graded Leibniz rule ($d(A \wedge a) = dA \wedge a - A \wedge da$, since $A$ has odd degree one) and the hypothesis "$M$ closed" both enter, and dropping either breaks the identity. The second is the **non-degeneracy**, which is where the "only if" direction genuinely lives: the formula $d\vartheta_A(a) = \tfrac1{4\pi^2}\int_M \operatorname{tr}(F_A \wedge a)$ shows critical $\Leftarrow$ flat trivially, but critical $\Rightarrow$ flat requires that the pairing separate curvatures, and this rests on the positive-definiteness of $-\operatorname{tr}$ on $\mathfrak{su}(2)$ together with the freedom to choose $a$ locally. A common error is to invoke the Hodge star and set $a = \star F_A$ before the Hodge star has been developed (it enters only in chapter VII); we avoid this by constructing the test form $a$ explicitly in a single chart, which needs nothing beyond a bump function.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Expand $\vartheta(A + sa)$ as a cubic polynomial in $s$ and read off the coefficient of $s$. Simplify that coefficient using two algebraic facts — the graded cyclicity of the trace (to merge the three cubic terms) and integration by parts on the closed manifold (to merge the two quadratic terms) — until it becomes $\tfrac1{4\pi^2}\int_M \operatorname{tr}(F_A \wedge a)$. Deduce "flat $\Rightarrow$ critical" instantly, and "critical $\Rightarrow$ flat" by constructing, from a hypothetical nonzero $F_A$, a test form $a$ against which the pairing is strictly positive.

**Subgoal decomposition:**

1. **Graded cyclicity of the trace.** Show $\operatorname{tr}(\alpha \wedge \beta) = (-1)^{pq}\operatorname{tr}(\beta \wedge \alpha)$ for matrix-valued forms of degrees $p, q$.
   - *Hint:* Combine the scalar cyclicity $\operatorname{tr}(\alpha_I \beta_J) = \operatorname{tr}(\beta_J \alpha_I)$ with the sign in $dx^I \wedge dx^J = (-1)^{pq} dx^J \wedge dx^I$.
   - *Why needed:* It merges the three cubic terms and identifies $\operatorname{tr}(a \wedge F_A) = \operatorname{tr}(F_A \wedge a)$.

2. **First variation of the integrand.** Show $\tfrac{d}{ds}\big|_0 \operatorname{cs}(A+sa) = \operatorname{tr}(a \wedge dA + A \wedge da + 2\, a \wedge A \wedge A)$.
   - *Hint:* Expand $(A+sa)\wedge d(A+sa)$ and $(A+sa)^{\wedge 3}$, keep the $s^1$ coefficient, then use subgoal 1 to see the three cubic terms are equal, so $\tfrac23 \cdot 3 = 2$.
   - *Why needed:* It is the raw derivative before simplification.

3. **Integration by parts.** Show $\int_M \operatorname{tr}(A \wedge da) = \int_M \operatorname{tr}(a \wedge dA)$.
   - *Hint:* $d\operatorname{tr}(A \wedge a) = \operatorname{tr}(dA \wedge a) - \operatorname{tr}(A \wedge da)$; integrate and use Stokes with $\partial M = \varnothing$; then $\operatorname{tr}(dA\wedge a) = \operatorname{tr}(a \wedge dA)$ by subgoal 1.
   - *Why needed:* It merges the two quadratic terms so the curvature can appear.

4. **Positive-definiteness of the trace form.** Show $\langle \xi, \eta\rangle = -\operatorname{tr}(\xi\eta)$ is a positive-definite inner product on $\mathfrak{su}(2)$.
   - *Hint:* For anti-Hermitian $\xi$, $-\operatorname{tr}(\xi^2) = \operatorname{tr}(\xi \xi^*) = \sum_{i,j}|\xi_{ij}|^2$.
   - *Why needed:* It powers the non-degeneracy in subgoal 5.

5. **Non-degeneracy of the pairing.** Show that if $F \in \Omega^2(M;\mathfrak{su}(2))$ satisfies $\int_M \operatorname{tr}(F \wedge a) = 0$ for all $a \in \Omega^1(M;\mathfrak{su}(2))$, then $F = 0$.
   - *Hint:* If $F(p_0) \ne 0$, write $F = \sum_{i<j} F_{ij}\, dx^i \wedge dx^j$ in an oriented chart, take $a = \chi(b_1 dx^1 + b_2 dx^2 + b_3 dx^3)$ with $b_1 = -F_{23}, b_2 = F_{13}, b_3 = -F_{12}$ and a bump $\chi \ge 0$; then $\operatorname{tr}(F \wedge a) = \chi\,|F|^2\, dx^1\wedge dx^2\wedge dx^3 > 0$ near $p_0$.
   - *Why needed:* It gives "critical $\Rightarrow$ flat".

6. **Assemble.** Combine 2 and 3 to get part (i); read off part (ii) using 5; deduce part (iii) from gauge-invariance of curvature and of $\vartheta$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Graded cyclicity of the trace of matrix-valued forms
> **Statement:** Let $\alpha \in \Omega^p(M; \mathfrak{gl}_2(\mathbb{C}))$ and $\beta \in \Omega^q(M; \mathfrak{gl}_2(\mathbb{C}))$. Then
> $$\operatorname{tr}(\alpha \wedge \beta) = (-1)^{pq}\, \operatorname{tr}(\beta \wedge \alpha) \in \Omega^{p+q}(M).$$
> In particular $\operatorname{tr}(F_A \wedge a) = \operatorname{tr}(a \wedge F_A)$ (degrees $2$ and $1$, sign $(-1)^{2} = +1$), and for three one-forms $\operatorname{tr}(a \wedge A \wedge A) = \operatorname{tr}(A \wedge a \wedge A) = \operatorname{tr}(A \wedge A \wedge a)$.
>
> **Hint:** Work in a chart, use the scalar cyclicity of the matrix trace on each coefficient and the transposition sign for scalar wedge products.
>
> **Why needed:** It is the algebraic identity that merges the three cubic terms in the first variation and that lets $\operatorname{tr}(a \wedge F_A)$ be rewritten as $\operatorname{tr}(F_A \wedge a)$ to match the statement.
>
> > [!note]- Full proof
> > **Reduce to a single monomial.** Both sides are $\mathbb{R}$-bilinear in $(\alpha, \beta)$ and are defined chartwise, so it suffices to prove the identity for $\alpha = \xi\, dx^I$ and $\beta = \eta\, dx^J$, where $\xi, \eta \in \mathfrak{gl}_2(\mathbb{C})$ are constant matrices, $I$ is an increasing multi-index of length $p$, and $J$ is one of length $q$.
> >
> > **Compute both sides.** By the definition of the wedge product with matrix multiplication,
> > $$\operatorname{tr}(\alpha \wedge \beta) = \operatorname{tr}(\xi \eta)\, dx^I \wedge dx^J \qquad \text{(definition of } \alpha \wedge \beta \text{ and of } \operatorname{tr} \text{ on forms).}$$
> > On the other hand,
> > $$\operatorname{tr}(\beta \wedge \alpha) = \operatorname{tr}(\eta \xi)\, dx^J \wedge dx^I \qquad \text{(same definitions).}$$
> >
> > **Apply scalar cyclicity and the transposition sign.** The scalar matrix trace is cyclic, $\operatorname{tr}(\eta\xi) = \operatorname{tr}(\xi\eta)$, and swapping a $p$-form past a $q$-form costs the Koszul sign, $dx^J \wedge dx^I = (-1)^{pq}\, dx^I \wedge dx^J$ (each of the $p$ one-form factors of $dx^I$ is moved past each of the $q$ one-form factors of $dx^J$). Therefore
> > $$\operatorname{tr}(\beta \wedge \alpha) = \operatorname{tr}(\xi\eta)\,(-1)^{pq}\, dx^I \wedge dx^J = (-1)^{pq}\, \operatorname{tr}(\alpha \wedge \beta) \qquad \text{(cyclicity of } \operatorname{tr} \text{; Koszul sign).}$$
> > Rearranging gives $\operatorname{tr}(\alpha \wedge \beta) = (-1)^{pq}\operatorname{tr}(\beta \wedge \alpha)$.
> >
> > **The two special cases.** For $F_A$ (degree $2$) and $a$ (degree $1$): $pq = 2$, so $\operatorname{tr}(a \wedge F_A) = (-1)^{2}\operatorname{tr}(F_A \wedge a) = \operatorname{tr}(F_A \wedge a)$. For three one-forms, apply the identity with $\alpha = a$ (degree $1$) and $\beta = A \wedge A$ (degree $2$): $\operatorname{tr}(a \wedge A \wedge A) = (-1)^{1\cdot 2}\operatorname{tr}(A \wedge A \wedge a) = \operatorname{tr}(A \wedge A \wedge a)$; and with $\alpha = A$ (degree $1$), $\beta = a \wedge A$ (degree $2$): $\operatorname{tr}(A \wedge a \wedge A) = (-1)^{1\cdot 2}\operatorname{tr}(a \wedge A \wedge A) = \operatorname{tr}(a \wedge A \wedge A)$. Hence all three cyclic arrangements of $\operatorname{tr}(a \wedge A \wedge A)$ are equal. $\blacksquare$

> [!note]- Lemma 2: First variation of the Chern–Simons integrand
> **Statement:** For all $A, a \in \Omega^1(M; \mathfrak{su}(2))$,
> $$\frac{d}{ds}\Big|_{s=0} \operatorname{cs}(A + sa) = \operatorname{tr}\big(a \wedge dA + A \wedge da + 2\, a \wedge A \wedge A\big),$$
> where $\operatorname{cs}(B) = \operatorname{tr}(B \wedge dB + \tfrac23 B \wedge B \wedge B)$.
>
> **Hint:** Substitute $B = A + sa$, expand $B \wedge dB$ and $B^{\wedge 3}$ as polynomials in $s$, and keep the coefficient of $s^1$; then collapse the three cubic terms with Lemma 1.
>
> **Why needed:** It is the raw first derivative of the integrand, before integration by parts turns it into a pairing with the curvature.
>
> > [!note]- Full proof
> > **Expand the quadratic term.** With $B = A + sa$, we have $dB = dA + s\, da$ (the exterior derivative is $\mathbb{R}$-linear), so
> > $$B \wedge dB = (A + sa) \wedge (dA + s\, da) = A \wedge dA + s\,(a \wedge dA + A \wedge da) + s^2\, a \wedge da \qquad \text{(bilinearity of } \wedge \text{).}$$
> > Its $s^1$-coefficient is $a \wedge dA + A \wedge da$.
> >
> > **Expand the cubic term.** Multiplying out $B^{\wedge 3} = (A + sa)\wedge(A+sa)\wedge(A+sa)$ and collecting the terms with exactly one factor of $a$,
> > $$B \wedge B \wedge B = A^{\wedge 3} + s\,(a \wedge A \wedge A + A \wedge a \wedge A + A \wedge A \wedge a) + O(s^2) \qquad \text{(trilinearity of } \wedge \text{).}$$
> > Its $s^1$-coefficient is $a \wedge A \wedge A + A \wedge a \wedge A + A \wedge A \wedge a$.
> >
> > **Apply the trace and Lemma 1 to the cubic terms.** Taking $\operatorname{tr}$ of the $s^1$-coefficient of $\tfrac23 B^{\wedge 3}$ and using that the three cyclic arrangements are equal (Lemma 1),
> > $$\tfrac23\,\operatorname{tr}(a \wedge A \wedge A + A \wedge a \wedge A + A \wedge A \wedge a) = \tfrac23 \cdot 3\,\operatorname{tr}(a \wedge A \wedge A) = 2\,\operatorname{tr}(a \wedge A \wedge A) \qquad \text{(Lemma 1: the three terms coincide).}$$
> >
> > **Assemble.** Because $s \mapsto \operatorname{cs}(A + sa)$ is a polynomial in $s$ with coefficients that are fixed smooth three-forms, its derivative at $s = 0$ is the coefficient of $s^1$ (a polynomial is differentiated term by term). Combining the two expansions,
> > $$\frac{d}{ds}\Big|_{s=0} \operatorname{cs}(A + sa) = \operatorname{tr}(a \wedge dA + A \wedge da) + 2\,\operatorname{tr}(a \wedge A \wedge A) = \operatorname{tr}\big(a \wedge dA + A \wedge da + 2\, a \wedge A \wedge A\big).$$
> > This is the claimed identity. $\blacksquare$

> [!note]- Lemma 3: Integration by parts on a closed manifold
> **Statement:** Let $M$ be a closed oriented manifold and $A, a \in \Omega^1(M; \mathfrak{su}(2))$. Then
> $$\int_M \operatorname{tr}(A \wedge da) = \int_M \operatorname{tr}(a \wedge dA).$$
>
> **Hint:** Show the two integrands differ by the exact form $d\operatorname{tr}(A \wedge a)$, apply Stokes with empty boundary, then use Lemma 1 to turn $\operatorname{tr}(dA \wedge a)$ into $\operatorname{tr}(a \wedge dA)$.
>
> **Why needed:** It merges the two quadratic terms $\operatorname{tr}(a \wedge dA)$ and $\operatorname{tr}(A \wedge da)$ of Lemma 2 into a single $2\operatorname{tr}(a\wedge dA)$, so that the curvature $dA + A \wedge A$ can be reassembled.
>
> > [!note]- Full proof
> > **Differentiate the trace form $\operatorname{tr}(A \wedge a)$.** The scalar two-form $\operatorname{tr}(A \wedge a) \in \Omega^2(M)$ satisfies $d\operatorname{tr}(A \wedge a) = \operatorname{tr}\big(d(A \wedge a)\big)$, because $\operatorname{tr}$ is a constant-coefficient linear map and therefore commutes with $d$. By the graded Leibniz rule — valid for matrix-valued forms since $d$ acts entrywise and matrix multiplication is bilinear — and since $A$ has odd degree one,
> > $$d(A \wedge a) = dA \wedge a + (-1)^{1}\, A \wedge da = dA \wedge a - A \wedge da \qquad \text{(graded Leibniz rule, } \deg A = 1 \text{).}$$
> > Applying $\operatorname{tr}$,
> > $$d\operatorname{tr}(A \wedge a) = \operatorname{tr}(dA \wedge a) - \operatorname{tr}(A \wedge da) \qquad \text{(} \operatorname{tr} \text{ is linear).}$$
> >
> > **Integrate and apply Stokes.** Integrate over $M$ and invoke [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] — for a smooth $(n-1)$-form $\omega$ on a compact oriented $n$-manifold $M$ with boundary, $\int_M d\omega = \int_{\partial M} \omega$. Here $M$ is closed, so $\partial M = \varnothing$ and the right-hand side is zero:
> > $$0 = \int_{\partial M} \operatorname{tr}(A \wedge a) = \int_M d\operatorname{tr}(A \wedge a) = \int_M \operatorname{tr}(dA \wedge a) - \int_M \operatorname{tr}(A \wedge da) \qquad \text{(Stokes, } \partial M = \varnothing \text{).}$$
> > Hence $\int_M \operatorname{tr}(A \wedge da) = \int_M \operatorname{tr}(dA \wedge a)$.
> >
> > **Rewrite with Lemma 1.** By Lemma 1 with degrees $2$ (for $dA$) and $1$ (for $a$), $\operatorname{tr}(dA \wedge a) = (-1)^{2\cdot 1}\operatorname{tr}(a \wedge dA) = \operatorname{tr}(a \wedge dA)$. Therefore
> > $$\int_M \operatorname{tr}(A \wedge da) = \int_M \operatorname{tr}(a \wedge dA). \qquad \blacksquare$$

> [!note]- Lemma 4: The trace form is a positive-definite inner product on $\mathfrak{su}(2)$
> **Statement:** The bilinear form $\langle \xi, \eta \rangle := -\operatorname{tr}(\xi\eta)$ on $\mathfrak{su}(2)$ is real-valued, symmetric, and positive definite: $\langle \xi, \xi \rangle \ge 0$ with equality if and only if $\xi = 0$.
>
> **Hint:** For anti-Hermitian $\xi$, $\xi^* = -\xi$, so $-\operatorname{tr}(\xi^2) = \operatorname{tr}(\xi\xi^*)$, which is the sum of the squared moduli of the entries.
>
> **Why needed:** It is the pointwise positivity that makes the curvature-pairing non-degenerate (Lemma 5): it guarantees that the locally constructed test form yields a strictly positive integrand wherever the curvature is nonzero.
>
> > [!note]- Full proof
> > **Reality.** For $\xi, \eta \in \mathfrak{su}(2)$ we have $\xi^* = -\xi$ and $\eta^* = -\eta$, hence entrywise conjugates $\overline{\xi} = -\xi^{\mathsf T}$ and $\overline{\eta} = -\eta^{\mathsf T}$. Then
> > $$\overline{\operatorname{tr}(\xi\eta)} = \operatorname{tr}(\overline{\xi}\,\overline{\eta}) = \operatorname{tr}(\xi^{\mathsf T}\eta^{\mathsf T}) = \operatorname{tr}\big((\eta\xi)^{\mathsf T}\big) = \operatorname{tr}(\eta\xi) = \operatorname{tr}(\xi\eta) \qquad \text{(} \overline{\xi} = -\xi^{\mathsf T} \text{; } (\eta\xi)^{\mathsf T} = \xi^{\mathsf T}\eta^{\mathsf T} \text{; } \operatorname{tr} A^{\mathsf T} = \operatorname{tr} A \text{; cyclicity).}$$
> > So $\operatorname{tr}(\xi\eta) \in \mathbb{R}$, and $\langle \xi, \eta\rangle = -\operatorname{tr}(\xi\eta)$ is real.
> >
> > **Symmetry.** By cyclicity of the trace, $\operatorname{tr}(\xi\eta) = \operatorname{tr}(\eta\xi)$, so $\langle \xi, \eta\rangle = \langle \eta, \xi\rangle$.
> >
> > **Positive definiteness.** Fix $\xi \in \mathfrak{su}(2)$. Since $\xi^* = -\xi$,
> > $$\langle \xi, \xi\rangle = -\operatorname{tr}(\xi^2) = -\operatorname{tr}(\xi \cdot (-\xi^*)) = \operatorname{tr}(\xi\xi^*) = \sum_{i,j} \xi_{ij}\,\overline{\xi_{ij}} = \sum_{i,j} |\xi_{ij}|^2 \ge 0 \qquad \text{(} \xi = -\xi^* \text{; } (\xi\xi^*)_{ii} = \sum_j \xi_{ij}\overline{\xi_{ij}} \text{).}$$
> > The final sum is zero if and only if every entry $\xi_{ij}$ vanishes, that is, if and only if $\xi = 0$. Hence $\langle\cdot,\cdot\rangle$ is positive definite.
> >
> > **Concrete check.** On the basis $-i\sigma_1, -i\sigma_2, -i\sigma_3$ of $\mathfrak{su}(2)$, where $\sigma_a$ are the Pauli matrices with $\sigma_a^2 = I$, we get $\langle -i\sigma_a, -i\sigma_a\rangle = -\operatorname{tr}\big((-i\sigma_a)^2\big) = -\operatorname{tr}(-\sigma_a^2) = \operatorname{tr}(I) = 2 > 0$, so these basis vectors are orthogonal (a short computation gives $\operatorname{tr}(\sigma_a\sigma_b) = 2\delta_{ab}$) with squared length $2$. $\blacksquare$

> [!note]- Lemma 5: Non-degeneracy of the curvature pairing
> **Statement:** Let $M$ be a closed oriented three-manifold and $F \in \Omega^2(M; \mathfrak{su}(2))$. If
> $$\int_M \operatorname{tr}(F \wedge a) = 0 \quad \text{for every } a \in \Omega^1(M; \mathfrak{su}(2)),$$
> then $F = 0$.
>
> **Hint:** Argue by contraposition. If $F(p_0) \ne 0$, write $F$ in an oriented chart and choose $a$ supported near $p_0$ so that $\operatorname{tr}(F \wedge a)$ is a nonnegative multiple of the volume form, strictly positive at $p_0$.
>
> **Why needed:** It converts the vanishing of the first variation $d\vartheta_A = \tfrac1{4\pi^2}\int_M \operatorname{tr}(F_A \wedge \cdot)$ into the vanishing of $F_A$, giving the "only if" direction of the theorem. The construction uses only a bump function, so the Hodge star of chapter VII is not needed.
>
> > [!note]- Full proof
> > **Set up the contrapositive.** Suppose $F \ne 0$; we produce an $a$ with $\int_M \operatorname{tr}(F \wedge a) \ne 0$. Since $F \ne 0$ there is a point $p_0 \in M$ with $F(p_0) \ne 0$. Choose a positively oriented chart $(U; x^1, x^2, x^3)$ about $p_0$, so that $dx^1 \wedge dx^2 \wedge dx^3$ is a positive multiple of the orientation form on $U$, and write
> > $$F|_U = \sum_{1 \le i < j \le 3} F_{ij}\, dx^i \wedge dx^j, \qquad F_{ij} \in C^\infty(U; \mathfrak{su}(2)),$$
> > with $F_{12}, F_{13}, F_{23}$ smooth $\mathfrak{su}(2)$-valued functions; at least one of them is nonzero at $p_0$ because $F(p_0) \ne 0$.
> >
> > **Construct the local test form.** Define smooth $\mathfrak{su}(2)$-valued functions on $U$ by
> > $$b_1 := -F_{23}, \qquad b_2 := F_{13}, \qquad b_3 := -F_{12},$$
> > and the local one-form $\eta := b_1\, dx^1 + b_2\, dx^2 + b_3\, dx^3 \in \Omega^1(U; \mathfrak{su}(2))$.
> >
> > **Compute the wedge.** Only the terms with $\{i, j, k\} = \{1, 2, 3\}$ contribute to the top-degree form $F|_U \wedge \eta = \sum_{i<j,\,k} F_{ij} b_k\, dx^i \wedge dx^j \wedge dx^k$. Using $dx^1\wedge dx^3\wedge dx^2 = -dx^1\wedge dx^2\wedge dx^3$ and $dx^2\wedge dx^3\wedge dx^1 = +dx^1\wedge dx^2\wedge dx^3$,
> > $$F|_U \wedge \eta = \big(F_{12} b_3 - F_{13} b_2 + F_{23} b_1\big)\, dx^1 \wedge dx^2 \wedge dx^3 \qquad \text{(collecting the three orderings of } \{1,2,3\} \text{).}$$
> > Substituting the definitions of the $b_k$,
> > $$F|_U \wedge \eta = \big(-F_{12}^2 - F_{13}^2 - F_{23}^2\big)\, dx^1 \wedge dx^2 \wedge dx^3 \qquad \text{(} b_3 = -F_{12},\, b_2 = F_{13},\, b_1 = -F_{23} \text{).}$$
> >
> > **Take the trace and apply Lemma 4.** Writing $\langle\cdot,\cdot\rangle = -\operatorname{tr}(\cdot\,\cdot)$ and $|F|^2 := \sum_{i<j}\langle F_{ij}, F_{ij}\rangle = -\operatorname{tr}(F_{12}^2 + F_{13}^2 + F_{23}^2)$,
> > $$\operatorname{tr}(F|_U \wedge \eta) = -\operatorname{tr}(F_{12}^2 + F_{13}^2 + F_{23}^2)\, dx^1 \wedge dx^2 \wedge dx^3 = |F|^2\, dx^1 \wedge dx^2 \wedge dx^3.$$
> > By Lemma 4 the function $|F|^2 = \sum_{i<j}\langle F_{ij}, F_{ij}\rangle$ is nonnegative on $U$, and it is strictly positive exactly where some $F_{ij}$ is nonzero — in particular $|F|^2(p_0) > 0$. By continuity there is an open neighbourhood $V$ of $p_0$ with $\overline{V} \subset U$ on which $|F|^2 > 0$.
> >
> > **Globalise with a bump function.** Choose $\chi \in C^\infty(M)$ with $\chi \ge 0$, $\operatorname{supp}\chi \subset V$, and $\chi(p_0) = 1$ (such a bump function exists on any manifold). Define
> > $$a := \chi\, \eta \in \Omega^1(M; \mathfrak{su}(2)),$$
> > extended by zero outside $V$; this is smooth and globally defined because $\chi$ is supported in $V \subset U$. Since $\chi$ is a scalar function (a zero-form), it factors through the wedge and the trace: $\operatorname{tr}(F \wedge a) = \chi\, \operatorname{tr}(F|_U \wedge \eta) = \chi\, |F|^2\, dx^1 \wedge dx^2 \wedge dx^3$ on $V$, and $\operatorname{tr}(F \wedge a) = 0$ off $\operatorname{supp}\chi$.
> >
> > **Conclude strict positivity of the integral.** Integrating over the positively oriented $V$,
> > $$\int_M \operatorname{tr}(F \wedge a) = \int_V \chi\, |F|^2\, dx^1\, dx^2\, dx^3 > 0,$$
> > because the integrand $\chi\,|F|^2$ is nonnegative and strictly positive on a neighbourhood of $p_0$ (where $\chi(p_0) = 1$ and $|F|^2(p_0) > 0$). Thus the pairing does not vanish against this $a$, contradicting the hypothesis. By contraposition, if the pairing vanishes against every $a$ then $F = 0$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $M$ be a closed oriented three-manifold, $P \to M$ a trivialised principal $SU(2)$-bundle, and $A, a \in \Omega^1(M; \mathfrak{su}(2))$. We prove (i), (ii), (iii) in turn.
>
> **Step 0 — the derivative is well-posed.** In the fixed trivialisation the tangent space to $\mathcal{A}(P)$ at $A$ is $\Omega^1(M; \mathfrak{su}(2))$, since $\mathcal{A}(P)$ is affine over $\Omega^1(M; \operatorname{ad}P) \cong \Omega^1(M; \mathfrak{su}(2))$ by [[Thm - The Space of Connections is an Affine Space|the affine-space theorem]] — for two connections the difference is a $\operatorname{ad}$-valued one-form, and adding any such form to a connection gives a connection. The straight line $s \mapsto A + sa$ is therefore a path in $\mathcal{A}(P)$ with velocity $a$. The real number $\widetilde\vartheta(A + sa) = \tfrac1{8\pi^2}\int_M \operatorname{cs}(A + sa)$ is a genuine cubic polynomial in $s$ (its integrand is a polynomial in $s$ with coefficients fixed smooth three-forms on the compact $M$), and $\vartheta = \widetilde\vartheta \bmod \mathbb{Z}$ with the same fixed trivialisation held throughout the path, so $\tfrac{d}{ds}\big|_0 \vartheta(A + sa) = \tfrac{d}{ds}\big|_0 \widetilde\vartheta(A + sa)$ is unambiguous. This defines the linear functional $d\vartheta_A(a) := \tfrac{d}{ds}\big|_0 \vartheta(A + sa)$ on $\Omega^1(M;\mathfrak{su}(2))$.
>
> **Step 1 — differentiate the integrand (part (i), first half).** By Lemma 2,
> $$\frac{d}{ds}\Big|_{s=0} \operatorname{cs}(A + sa) = \operatorname{tr}\big(a \wedge dA + A \wedge da + 2\, a \wedge A \wedge A\big) \qquad \text{(Lemma 2).}$$
> Since $\widetilde\vartheta(A+sa)$ is a polynomial in $s$ whose $s$-coefficient is $\tfrac1{8\pi^2}\int_M \big(\text{the above integrand}\big)$,
> $$d\vartheta_A(a) = \frac{1}{8\pi^2}\int_M \operatorname{tr}\big(a \wedge dA + A \wedge da + 2\, a \wedge A \wedge A\big) \qquad \text{(differentiate the polynomial term by term).}$$
>
> **Step 2 — integrate by parts (part (i), second half).** By Lemma 3, $\int_M \operatorname{tr}(A \wedge da) = \int_M \operatorname{tr}(a \wedge dA)$ (this is where "$M$ closed" is used, through Stokes' theorem with empty boundary). Substituting,
> $$d\vartheta_A(a) = \frac{1}{8\pi^2}\int_M \operatorname{tr}\big(2\, a \wedge dA + 2\, a \wedge A \wedge A\big) = \frac{1}{4\pi^2}\int_M \operatorname{tr}\big(a \wedge (dA + A \wedge A)\big) \qquad \text{(Lemma 3; factor } 2 \text{ and linearity of } \operatorname{tr} \text{).}$$
> Now recall $F_A = dA + A \wedge A$: this is [[Thm - Curvature of a Shifted Connection|the shifted-connection theorem]] applied to the trivial base connection $\nabla = d$, for which $F_\nabla = 0$ and $d^\nabla a = da$, giving $F_{d + A} = 0 + dA + A \wedge A$. Hence $dA + A \wedge A = F_A$, and by Lemma 1 ($\operatorname{tr}(a \wedge F_A) = \operatorname{tr}(F_A \wedge a)$),
> $$d\vartheta_A(a) = \frac{1}{4\pi^2}\int_M \operatorname{tr}(a \wedge F_A) = \frac{1}{4\pi^2}\int_M \operatorname{tr}(F_A \wedge a) \qquad \text{(} F_A = dA + A\wedge A \text{; Lemma 1).}$$
> This is part (i).
>
> **Step 3 — flat implies critical (part (ii), $\Leftarrow$).** Suppose $F_A = 0$. Then for every $a$, $d\vartheta_A(a) = \tfrac1{4\pi^2}\int_M \operatorname{tr}(0 \wedge a) = 0$. So the functional $d\vartheta_A$ vanishes identically and $A$ is a critical point.
>
> **Step 4 — critical implies flat (part (ii), $\Rightarrow$).** Suppose $A$ is critical, so $d\vartheta_A(a) = 0$ for every $a \in \Omega^1(M; \mathfrak{su}(2))$. By part (i), this says $\int_M \operatorname{tr}(F_A \wedge a) = 0$ for every $a$. By the non-degeneracy of the curvature pairing (Lemma 5, applied with $F = F_A$), it follows that $F_A = 0$, that is, $A$ is flat. Combining Steps 3 and 4, $A$ is critical if and only if $F_A = 0$, which is part (ii).
>
> **Step 5 — descent to the orbit space (part (iii)).** First, flatness is gauge invariant. By [[Thm - Gauge Transformations Act on Connections and Curvature|the gauge-action theorem]], under a gauge transformation $g$ the curvature transforms by conjugation, $F_{A \cdot g} = \operatorname{Ad}_{g^{-1}} F_A = g^{-1} F_A g$ in the matrix trivialisation; since $g^{-1} F_A g = 0 \iff F_A = 0$, the connection $A \cdot g$ is flat if and only if $A$ is flat, so the set of flat connections is a union of gauge orbits.
>
> Second, $\vartheta$ descends. By [[Thm - Gauge Variation of the Chern-Simons Functional|the gauge-variation theorem]], for a gauge transformation $g\colon M \to SU(2)$ one has $\widetilde\vartheta(A \cdot g) = \widetilde\vartheta(A) + \deg g$ with $\deg g \in \mathbb{Z}$; reducing modulo $\mathbb{Z}$, $\vartheta(A \cdot g) = \vartheta(A)$, so $\vartheta$ is constant on gauge orbits and descends to a well-defined map $\overline{\vartheta}\colon \mathcal{A}(P)/\mathcal{G}(P) \to \mathbb{R}/\mathbb{Z}$. Its differential is therefore a well-defined object on the orbit space, and a class $[A]$ is critical for $\overline{\vartheta}$ precisely when $A$ is critical for $\vartheta$ on $\mathcal{A}(P)$ (the extra directions along the gauge orbit contribute nothing, as $\vartheta$ is constant along them). By part (ii) these are exactly the flat connections, and by the first paragraph of this step their gauge-equivalence classes are well-defined points of $\mathcal{A}(P)/\mathcal{G}(P)$. Therefore the critical set of $\overline{\vartheta}$ is exactly the set of gauge-equivalence classes of flat connections.
>
> **Conclusion.** The first variation of $\vartheta$ is the pairing $\tfrac1{4\pi^2}\int_M \operatorname{tr}(F_A \wedge \cdot)$ with the curvature (part (i)); this pairing vanishes identically if and only if the curvature vanishes (part (ii)); and both the functional and the flatness condition are gauge invariant, so the critical set on the orbit space is exactly the moduli space of flat connections (part (iii)). $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The abelian toy model — variational calculus on a line bundle.** Restrict $A$ to take values in a fixed line $\mathbb{R}\cdot\xi_0 \subset \mathfrak{su}(2)$, so $A = \alpha\,\xi_0$ with $\alpha$ an ordinary real one-form. Then $A \wedge A = (\alpha \wedge \alpha)\,\xi_0^2 = 0$ (a one-form wedged with itself vanishes), so $F_A = dA = d\alpha\,\xi_0$ and $\vartheta$ reduces to the quadratic $\tfrac{c}{8\pi^2}\int_M \alpha \wedge d\alpha$ with $c = -\operatorname{tr}(\xi_0^2)$. The theorem specialises to: the critical points of $\int_M \alpha \wedge d\alpha$ over closed one-forms modulo exact ones are the *closed* one-forms $d\alpha = 0$. This is a warm-up worth doing by hand because it isolates the integration-by-parts step from the cyclicity step (the cubic term is absent) and makes visible that the first variation of the abelian Chern–Simons form is the pairing with $d\alpha$. It also shows that the theorem is genuinely three-dimensional and $SU(2)$-flavoured only through the cubic term; the mechanism "derivative equals pairing with curvature" is already present for line bundles.

**Morse theory on an infinite-dimensional manifold.** Regard $\vartheta$ as a smooth real-valued (modulo $\mathbb{Z}$) function on the Banach or Fréchet manifold $\mathcal{A}/\mathcal{G}$ and ask for its gradient with respect to the $L^2$ metric $\langle a, b\rangle_{L^2} = -\int_M \operatorname{tr}(a \wedge \star b)$ (which requires a Riemannian metric on $M$ and the Hodge star of chapter VII). The theorem identifies the gradient of $\vartheta$ as a multiple of $\star F_A$, so the critical points are the zeros of the gradient, namely the flat connections, and the gradient flow $\dot A = -\star F_A$ is the equation whose trajectories are anti-self-dual connections on $M \times \mathbb{R}$. The point of the exercise is to see that the abstract critical-point statement proved here becomes, once a metric is chosen, the concrete Floer gradient-flow equation, so that instanton Floer homology is Morse homology for $\vartheta$.

**Representation varieties from a purely algebraic starting point.** Take a finitely presented group $\Gamma = \langle x_1, \dots, x_n \mid r_1, \dots, r_m\rangle$ that arises as the fundamental group of a closed oriented three-manifold $M$ (for instance a surface-bundle group, or the discrete Heisenberg group for a certain circle bundle over the torus). The theorem, together with the monodromy correspondence, says that the critical set of $\vartheta$ on $\mathcal{A}/\mathcal{G}$ is the character variety $\operatorname{Hom}(\Gamma, SU(2))/\text{conjugation}$, a real algebraic set cut out by the relations $r_i$. The exercise is to compute this variety for a specific $\Gamma$ — say, for the torus $\Gamma = \mathbb{Z}^3$ one gets triples of commuting elements of $SU(2)$, hence a quotient of $(S^1)^3$ — and to observe that the differential-geometric critical-point problem and the algebraic representation problem have literally the same solution set. The connection is non-obvious because nothing in the definition of $\vartheta$ mentions $\pi_1(M)$.

---

# Bridges

- **[[Thm - Transgression Formula and the Chern-Simons Form|Transgression formula]]** — the four-dimensional origin of $\operatorname{cs}$. The transgression formula proves $d\operatorname{cs}(A) = \operatorname{tr}(F_A \wedge F_A)$, exhibiting the Chern–Simons three-form as a primitive of the second-Chern-class integrand. This is what makes $\vartheta$ "the antiderivative of the curvature" at the level of forms; the present theorem is the corresponding statement at the level of the functional and its critical points. The two together say that $\operatorname{cs}$ transgresses $\operatorname{tr}(F \wedge F)$ and that the functional it defines is stationary exactly at flat connections.

- **[[Def - Chern-Simons Functional|The Chern–Simons functional]]** — the object being differentiated. The definition page establishes that $\vartheta$ is well defined in $\mathbb{R}/\mathbb{Z}$, independent of the trivialisation and of the bounding four-manifold; this theorem computes its first variation and reads off the critical set. The well-definedness (the $\mathbb{R}/\mathbb{Z}$ ambiguity) is exactly why "critical point" must be phrased through the differential $d\vartheta_A$, which is genuinely real-valued even though $\vartheta$ is only circle-valued.

- **[[Thm - Gauge Variation of the Chern-Simons Functional|Gauge variation of $\vartheta$]]** — the reason the critical-point statement descends to the orbit space. Under a gauge transformation $g$, $\vartheta$ changes by the integer $\deg g$, so $\vartheta$ is $\mathbb{R}/\mathbb{Z}$-valued and gauge invariant; combined with the gauge-invariance of flatness, this is what lets the critical set be a subset of $\mathcal{A}/\mathcal{G}$ rather than of $\mathcal{A}$.

- **[[Thm - Flat Connections and Monodromy Representations of the Fundamental Group|Flat connections and monodromy]]** — the identification of the critical set. This theorem says the critical points are the flat connections; the monodromy theorem says the flat connections modulo gauge are the conjugacy classes of representations $\pi_1(M) \to SU(2)$. Composing the two identifies the critical set of $\vartheta$ with the $SU(2)$-representation variety of $\pi_1(M)$, the bridge from gauge theory to representation theory.

- **[[Thm - Curvature of a Shifted Connection|Curvature of a shifted connection]]** — the algebraic backbone of the computation. Its specialisation to the trivial base connection gives $F_A = dA + A \wedge A$, the identity used in Step 2 to recognise the reassembled curvature; more broadly it shows that curvature is a quadratic map on the affine space of connections, which is why $\vartheta$ is cubic and its differential is a pairing with the (quadratic) curvature.

---

# Unlocked by This

> [!tip] Instanton Floer homology *(from Low-Dimensional Topology)*
> Viewing $\vartheta$ as a Morse function on $\mathcal{A}/\mathcal{G}$ whose critical points are the flat connections and whose gradient trajectories are instantons on $M \times \mathbb{R}$ produces **instanton Floer homology**, an invariant of three-manifolds whose Euler characteristic recovers (twice) the Casson invariant. See the outlook on the Series Map; this is developed with the Yang–Mills machinery of chapter VII and the Fredholm and transversality theory of chapter X.

> [!tip] Chern–Simons quantum field theory *(from Mathematical Physics)*
> The functional $\vartheta$ is the classical action of a topological quantum field theory; its critical points, the flat connections, are the classical solutions, and the path integral $\int e^{2\pi i k\, \vartheta(A)}\,\mathcal{D}A$ (with integer level $k$, well defined because $\vartheta$ is $\mathbb{R}/\mathbb{Z}$-valued) produces invariants of knots and three-manifolds. The fact proved here — that the classical equations of motion are $F_A = 0$ — is the statement that this field theory has no local degrees of freedom.
