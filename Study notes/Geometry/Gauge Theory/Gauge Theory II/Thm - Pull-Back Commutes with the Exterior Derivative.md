---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Pullback of a Differential Form on a Manifold"
  - "Def - Exterior Derivative on a Manifold"
  - "Thm - Coordinate Expression for the Exterior Derivative"
  - "Thm - Pullback Commutes with d for 1-Forms"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ and $N$ are smooth manifolds — smooth, Hausdorff, second countable, and $C^\infty$, as everywhere in this series — of dimensions $m = \dim M$ and $n = \dim N$, and $F : M \to N$ is a smooth map. We write $\Omega^k(N) = \Gamma(\Lambda^k T^*N)$ for the space of smooth $k$-forms on $N$, and likewise $\Omega^k(M)$; a $0$-form is a smooth function, $\Omega^0(N) = C^\infty(N)$. The [[Def - Exterior Derivative on a Manifold|exterior derivative]] is the operator $d : \Omega^k \to \Omega^{k+1}$; the [[Def - Pullback of a Differential Form on a Manifold|pullback]] along $F$ is the operator $F^* : \Omega^k(N) \to \Omega^k(M)$ defined pointwise by
$$(F^*\omega)_p(v_1, \dots, v_k) = \omega_{F(p)}\big(dF_p(v_1), \dots, dF_p(v_k)\big), \qquad p \in M,\ v_1, \dots, v_k \in T_pM,$$
where $dF_p : T_pM \to T_{F(p)}N$ is the differential of $F$ at $p$. On functions the pullback is precomposition, $F^*g = g \circ F$ for $g \in C^\infty(N)$. The wedge product of forms is $\wedge$, and $\Lambda^k V^*$ is the space of alternating $k$-covectors on a vector space $V$ ([[Def - Alternating Tensor and Lambda k V Dual|alternating tensors]]).

For a chart $(V, y^j)$ on $N$ we use increasing multi-indices $J = (j_1 < \cdots < j_k)$, write $dy^J = dy^{j_1} \wedge \cdots \wedge dy^{j_k}$, and abbreviate the primed sum over increasing multi-indices of length $k$ by $\sum'_J$. For a smooth map into such a chart we write $F^j = y^j \circ F \in C^\infty(F^{-1}(V))$ for the $j$-th component function of $F$. The symbol $\operatorname{supp}$ denotes the support of a function, and $\chi$ denotes a bump function. The full symbol registry for the chapter is on the topic page [[Gauge Theory II — Vector Bundles, Covariant Derivatives, and Curvature]].

> [!warning] Convention: this page re-proves a flagged prerequisite
> The differential-geometry chapter records the higher-degree naturality statement $F^*(d\omega) = d(F^*\omega)$ on a page whose proof is incomplete. That page is **flagged** in this series and is never cited as an authority. The present page carries the complete proof and is the page every gauge-theory result links to when it needs naturality of $d$. We invoke only fully proved inputs: the degree-zero case [[Thm - Pullback Commutes with d for 1-Forms]], the [[Thm - Coordinate Expression for the Exterior Derivative|coordinate formula for the exterior derivative]], the [[Thm - Wedge Product Properties|properties of the wedge product]], the nilpotence [[Thm - d-Squared-is-Zero]], and the existence of [[Thm - Existence of Smooth Bump Functions|smooth bump functions]].

---

# Statement

> **Theorem (Naturality of the exterior derivative).** Let $F : M \to N$ be a smooth map between smooth manifolds. Then the pullback $F^* : \Omega^\bullet(N) \to \Omega^\bullet(M)$ is an $\mathbb{R}$-linear homomorphism of graded algebras that commutes with the exterior derivative. Explicitly, for all $\omega \in \Omega^k(N)$ and $\eta \in \Omega^\ell(N)$:
> $$\textbf{(i)}\quad F^*(\omega \wedge \eta) = F^*\omega \wedge F^*\eta, \qquad\qquad \textbf{(ii)}\quad F^*(d\omega) = d(F^*\omega).$$

> **Theorem (vector-valued version).** Let $V$ be a fixed finite-dimensional real vector space. For a $V$-valued form $\omega \in \Omega^k(N; V) = \Omega^k(N) \otimes V$, define $F^*\omega$ and $d\omega$ componentwise in any basis of $V$. Then, for every scalar form $\eta \in \Omega^\ell(N)$,
> $$F^*(\eta \wedge \omega) = F^*\eta \wedge F^*\omega \qquad\text{and}\qquad F^*(d\omega) = d(F^*\omega),$$
> and both identities are independent of the chosen basis of $V$.

The scalar statement is Lee, *Introduction to Smooth Manifolds*, 2nd ed., Proposition 14.26 (with the wedge-homomorphism half being Proposition 14.23); the vector-valued statement is its componentwise consequence, and it is the form in which naturality is used throughout gauge theory, where the coefficient space is a Lie algebra $\mathfrak{g}$.

---

# Motivation

The exterior derivative $d$ and the pullback $F^*$ are the two operations that make differential forms into a usable global calculus, and this theorem is the single identity that says they are compatible. Read as a diagram, it asserts that

$$\begin{array}{ccc}
\Omega^k(N) & \xrightarrow{\ d\ } & \Omega^{k+1}(N) \\
\big\downarrow{\scriptstyle F^*} & & \big\downarrow{\scriptstyle F^*} \\
\Omega^k(M) & \xrightarrow{\ d\ } & \Omega^{k+1}(M)
\end{array}$$

commutes for every smooth $F$. Its role is not computational novelty but structural: it is exactly what upgrades the de Rham complex from a chart-bound bookkeeping device into a functor on the category of smooth manifolds. Once $F^* d = d F^*$ holds, a closed form pulls back to a closed form and an exact form to an exact form, so $F$ induces a well-defined map on de Rham cohomology, and cohomology becomes a smooth invariant rather than an accident of coordinates.

For gauge theory the theorem is a load-bearing lemma rather than a headline. Almost every local object in the subject is produced by pulling a globally defined form back along a section or a transition map. A [[Def - Local Connection Form and Gauge Potential|local connection form]] is $A_s = s^*\omega$, the pullback of the principal connection $\omega$ along a local section $s$; the local curvature is $s^*\Omega$; the transformation laws that relate two local descriptions of the same connection are pullback identities along the transition map. Whenever we differentiate one of these pulled-back forms — to write a structure equation, to check a Bianchi identity, or to compute a Chern–Weil form — we silently commute $d$ past a pullback. Making that commutation legitimate, once and completely, is the purpose of this page.

The most concrete way to feel the content is to watch it fail to be trivial. The pullback of a form is defined by a genuinely non-trivial pointwise recipe involving the differential $dF_p$, while $d$ is a differentiation of coefficient functions. There is no reason on the surface that differentiating-then-transporting should equal transporting-then-differentiating; that they agree is precisely the chain rule, promoted from functions to forms of every degree.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis is minimal — any smooth map $F : M \to N$ and any smooth form on $N$ — so the useful question is when a problem hands you a pullback of a form without announcing it, since those are exactly the situations in which the theorem earns its keep.

The first disguised source is **a form written in coordinates as a pullback of standard coordinate forms**. Whenever a form on a manifold is expressed through functions $F^j$ and their differentials $dF^j$ — a graph, a parametrised surface $\Phi : U \to N$, a change of variables — it is really a pullback: $\Phi^*(dy^{j_1} \wedge \cdots \wedge dy^{j_k}) = dF^{j_1} \wedge \cdots \wedge dF^{j_k}$. Recognising this lets one differentiate the expression by differentiating on the source instead, which is usually far cheaper. *Example problem:* to compute the exterior derivative of the area form pulled back to a parametrised surface, differentiate the pulled-back one-forms $dF^j$ directly, using that each is closed, rather than expanding the determinant.

The second disguised source is **a section of a bundle used to trivialise a global form**. A local section $s : U \to P$ of a principal bundle produces $A_s = s^*\omega$; a local frame $e$ of a vector bundle produces the connection matrix. These are pullbacks of one universally defined form along many different local sections, and the naturality theorem is what guarantees that $d(s^*\omega) = s^*(d\omega)$, which is the first step in deriving the local structure equation. The non-obvious bridge is that "local connection form" is not an independent gadget but a pullback, so its exterior derivative is controlled by the exterior derivative upstairs.

The third disguised source is **a homotopy or a smooth family of maps**. A smooth homotopy $H : M \times [0,1] \to N$ is a single smooth map, and the forms $H^*\omega$ on the product carry all the information of the family $t \mapsto (H_t)^*\omega$. Naturality of $d$ on $H$ is the engine behind the homotopy invariance of de Rham cohomology and behind the transgression formulas of Chern–Weil theory, where one integrates $H^*$ of a characteristic form over the interval factor. The non-obvious step is that a family of pullbacks is a single pullback on a larger manifold, to which the theorem applies verbatim.

**Targets (Output Amplification)**

Combine the conclusion with **the definition of a local connection form** to obtain the local structure equation. If $A_s = s^*\omega$ and $\Omega = d\omega + \tfrac12[\omega \wedge \omega]$, then applying $s^*$ and using $s^*(d\omega) = d(s^*\omega) = dA_s$ together with the fact that $s^*$ preserves wedges gives $s^*\Omega = dA_s + \tfrac12[A_s \wedge A_s]$. The extra ingredient is the naturality of the Lie-bracket wedge under $s^*$, itself a consequence of clause (i); the payoff is that the local curvature is computed entirely downstairs on $U$, and the two local forms $A_s$, $A_{s'}$ obey the gauge transformation law. See [[Thm - Transformation of Local Connection and Curvature Forms]].

Combine the conclusion with **an invariant polynomial and a connection** to obtain the naturality of Chern–Weil forms. If $f$ is an $\operatorname{Ad}$-invariant polynomial and $F_A$ a curvature form, then for a smooth map $g : M' \to M$ the pullback bundle carries the pulled-back connection and $g^*(f(F_A)) = f(g^* F_A)$ as forms, so $g^*$ commutes with the closed Chern–Weil representative. The extra ingredient is that $f(F_A)$ is built from wedges of the components of $F_A$, on which $g^*$ acts as an algebra homomorphism by clause (i), and $g^*$ commutes with the $d$ used to prove closedness by clause (ii). The payoff is that [[Def - Chern-Weil Form of an Invariant Polynomial|characteristic forms]] are natural, hence descend to characteristic classes that are functorial under bundle maps.

Combine the conclusion with **Stokes' theorem** to obtain the change-of-variables invariance of integration. For an orientation-preserving diffeomorphism $F$ and a top form $\omega$, naturality of $d$ makes the pullback a chain map, so $\int_M F^*\omega = \int_N \omega$ is compatible with $\int_M d(F^*\alpha) = \int_{\partial M} F^*\alpha = \int_{\partial N}\alpha$. The extra ingredient is Stokes' theorem on both manifolds; the payoff is that all of de Rham integration theory is coordinate-free, because the boundary operator and $d$ intertwine through $F^*$.

---

# Why Is It True

Strip away the degrees and look at what each side does to a single coordinate monomial $\omega_J\,dy^J$. The pullback replaces the coefficient $\omega_J$ by the composite $\omega_J \circ F$ and replaces each basic one-form $dy^j$ by the differential $dF^j$ of the corresponding component function of $F$ — this is the chain rule, and it is the only thing pullback does to a monomial. The exterior derivative, on the other hand, differentiates the coefficient and wedges on the new differential, leaving the $dy^J$ factors alone because $d$ annihilates them. The two operations touch different halves of the monomial: pullback rewrites the letters, $d$ differentiates the coefficient. Since differentiating the coefficient of a monomial and rewriting its letters are independent bookkeeping steps, the order cannot matter.

The one place the two halves could have interfered is the coefficient, and there the degree-zero case settles it: pulling back the differential of a function is the same as differentiating the pulled-back function, $F^*(dg) = d(g \circ F)$, which is the chain rule for functions. Everything of positive degree is then carried by two purely algebraic facts — that pullback is a wedge homomorphism, so it distributes over the monomial, and that each pulled-back coordinate differential $dF^j$ is closed, so the differentials contribute nothing when $d$ passes over them. The induction on degree is only the observation that a monomial of degree $k$ is a coefficient times a wedge of $k$ closed one-forms, and both $F^*$ and $d$ respect that decomposition.

**The whole theorem is the chain rule $F^*(dg) = d(g\circ F)$ for functions, made to propagate to every degree by the two facts that pullback preserves wedges and that $dF^j$ is closed.**

---

# What Makes This Hard

The single subtle point is that neither side is defined by a formula that visibly commutes: the pullback's pointwise recipe involves $dF_p$ and hides the chain rule, while $d$ is characterised abstractly by the graded Leibniz rule and nilpotence rather than by a manifestly natural expression. The common error is to prove the identity on functions and coordinate one-forms and then declare it "clearly extends by linearity", which skips the two genuine steps — that pullback is a wedge homomorphism in every degree (so it distributes over a monomial), and that the wedge of pulled-back differentials $dF^{j_1} \wedge \cdots \wedge dF^{j_k}$ is closed (so the graded Leibniz rule leaves no leftover terms when $d$ crosses it). A second, quieter error is to forget that the coordinate expression $\omega = \sum'_J \omega_J\,dy^J$ is only local, so that the argument must be assembled from a chart cover through the locality of both $d$ and $F^*$, not run once on a global expression that does not exist.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Both $d$ and $F^*$ are local, so it suffices to prove the identity on $U = F^{-1}(V)$ for a chart $(V, y^j)$ on $N$, where $\omega$ has a coordinate expression $\sum'_J \omega_J\,dy^J$. On such a monomial, pull the pullback through the wedge (it is a wedge homomorphism), turn each $F^*(dy^j)$ into $dF^j$ (degree-zero naturality), and compute both $F^*(d\omega)$ and $d(F^*\omega)$ down to the same expression $\sum'_J d(\omega_J \circ F) \wedge dF^{j_1} \wedge \cdots \wedge dF^{j_k}$, using that each $dF^j$ is closed.

**Subgoal decomposition:**

1. **Locality.** Show that both sides may be computed on $F^{-1}(V)$ chart by chart.
   - *Hint:* $d$ is local by a bump-function argument; $F^*$ is local because its value at $p$ depends only on $F$ near $p$ and $\omega$ near $F(p)$.
   - *Why needed:* The coordinate expression of $\omega$ exists only on a chart, so the whole computation is local; without locality there is no monomial to work with.

2. **Pullback is a wedge homomorphism.** Show $F^*(\omega \wedge \eta) = F^*\omega \wedge F^*\eta$ in every degree.
   - *Hint:* At each point this is a statement about a linear map $L = dF_p$; check it on decomposable forms using the determinant identity for the wedge.
   - *Why needed:* It lets $F^*$ distribute over a coordinate monomial $\omega_J\,dy^{j_1} \wedge \cdots \wedge dy^{j_k}$, which is the only way to reduce to the degree-zero case.

3. **Degree-zero naturality on coefficients and coordinates.** Use $F^*(dg) = d(g \circ F)$ to get $F^*(dy^j) = dF^j$ and $F^*(d\omega_J) = d(\omega_J \circ F)$.
   - *Hint:* Apply the already-proved one-form theorem to the coordinate functions $y^j$ and to the coefficients $\omega_J$.
   - *Why needed:* This is the chain rule; it is the only genuinely analytic input, and everything else is algebra.

4. **Pulled-back differentials are closed.** Show $d(dF^{j_1} \wedge \cdots \wedge dF^{j_k}) = 0$.
   - *Hint:* Each $dF^j = d(\text{function})$ is closed by $d^2 = 0$; propagate by the graded Leibniz rule and induction.
   - *Why needed:* When $d$ crosses the wedge of coordinate differentials in $d(F^*\omega)$, the graded Leibniz rule produces a leftover term $\pm(\omega_J \circ F)\,d(dF^{j_1} \wedge \cdots)$; this subgoal kills it.

5. **Assemble.** Compute $F^*(d\omega)$ and $d(F^*\omega)$ on a monomial and observe they are equal term by term; conclude by linearity and locality.
   - *Hint:* Both reduce to $\sum'_J d(\omega_J \circ F) \wedge dF^{j_1} \wedge \cdots \wedge dF^{j_k}$.
   - *Why needed:* This is the identity itself.

---

# Lemma Decomposition

> [!note]- Lemma 1: The exterior derivative is a local operator
> **Statement:** Let $\alpha \in \Omega^k(M)$ and let $U \subseteq M$ be open. If $\alpha$ vanishes on $U$, then $d\alpha$ vanishes on $U$. Consequently $(d\alpha)|_U = d(\alpha|_U)$: the exterior derivative of the restriction equals the restriction of the exterior derivative.
>
> **Hint:** For $p \in U$ take a bump function equal to $1$ near $p$ and supported in $U$, and multiply.
>
> **Why needed:** The coordinate expression of a form exists only on a chart. Locality is what lets the proof compute $d\alpha$ on the open set $F^{-1}(V)$, where a coordinate expression is available, and then reassemble the global identity from a chart cover.
>
> > [!note]- Full proof
> > **What is assumed and what is shown.** Assume $\alpha \in \Omega^k(M)$ vanishes identically on the open set $U$. We show $(d\alpha)_p = 0$ for every $p \in U$.
> >
> > **Construct a bump function.** Fix $p \in U$. By the [[Thm - Existence of Smooth Bump Functions|existence of smooth bump functions]] — for any point $p$ of a smooth manifold and any neighbourhood $U$ of $p$ there is a function $\chi \in C^\infty(M)$ with $0 \le \chi \le 1$, $\chi \equiv 1$ on a neighbourhood $W$ of $p$ with $W \subseteq U$, and $\operatorname{supp}\chi \subseteq U$ compact — choose such a $\chi$ with $\chi \equiv 1$ on a neighbourhood $W \ni p$ and $\operatorname{supp}\chi \subseteq U$.
> >
> > **The product $\chi\alpha$ vanishes globally.** At a point $q \in U$ we have $\alpha_q = 0$ (hypothesis: $\alpha$ vanishes on $U$), so $(\chi\alpha)_q = \chi(q)\,\alpha_q = 0$. At a point $q \notin U$ we have $\chi(q) = 0$ (since $\operatorname{supp}\chi \subseteq U$), so $(\chi\alpha)_q = 0$. Hence $\chi\alpha = 0$ on all of $M$, and therefore $d(\chi\alpha) = 0$ on all of $M$ (the exterior derivative of the zero form is zero, by $\mathbb{R}$-linearity of $d$).
> >
> > **Expand by the graded Leibniz rule.** Regarding $\chi \in \Omega^0(M)$ and $\alpha \in \Omega^k(M)$, the [[Def - Exterior Derivative on a Manifold|graded Leibniz rule]] gives
> > $$0 = d(\chi\alpha) = d\chi \wedge \alpha + \chi\,d\alpha \qquad \text{(graded Leibniz rule, degree of }\chi\text{ is }0\text{, so the sign is }(-1)^0 = +1).$$
> >
> > **Evaluate near $p$.** On the neighbourhood $W$ of $p$ we have $\chi \equiv 1$, hence $d\chi \equiv 0$ on $W$ (the differential of a locally constant function vanishes). Substituting $\chi = 1$ and $d\chi = 0$ into the displayed identity, on $W$
> > $$0 = 0 \wedge \alpha + 1 \cdot d\alpha = d\alpha \qquad \text{(}d\chi = 0\text{ and }\chi = 1\text{ on }W\text{).}$$
> > In particular $(d\alpha)_p = 0$.
> >
> > **Conclusion.** Since $p \in U$ was arbitrary, $d\alpha$ vanishes on $U$. Applying this to $\alpha = \beta - \beta'$ for two forms agreeing on $U$ shows $d\beta = d\beta'$ on $U$; taking $\beta' $ any smooth extension of $\beta|_U$ and reading the statement on the manifold $U$ itself gives $(d\alpha)|_U = d(\alpha|_U)$. Therefore the exterior derivative is local. $\blacksquare$

> [!note]- Lemma 2: The pullback is a local operator
> **Statement:** Let $F : M \to N$ be smooth, $\omega \in \Omega^k(N)$, and $U \subseteq M$ open. Then $(F^*\omega)|_U = (F|_U)^*(\omega)$; more precisely, the value $(F^*\omega)_p$ depends only on the germ of $F$ at $p$ and the germ of $\omega$ at $F(p)$. In particular, if $\omega$ vanishes on an open set $V \subseteq N$, then $F^*\omega$ vanishes on $F^{-1}(V)$.
>
> **Hint:** Read off the defining pointwise formula for $F^*\omega$.
>
> **Why needed:** Together with Lemma 1 it lets the identity be checked on $F^{-1}(V)$ for one chart $V$ at a time and then reassembled over a chart cover of $N$.
>
> > [!note]- Full proof
> > **What is assumed and what is shown.** Let $p \in M$. We show that $(F^*\omega)_p$ is determined by $F$ and $\omega$ arbitrarily near $p$ and $F(p)$, and deduce the restriction and vanishing statements.
> >
> > **The defining formula is pointwise.** By definition of the [[Def - Pullback of a Differential Form on a Manifold|pullback]], for $v_1, \dots, v_k \in T_pM$,
> > $$(F^*\omega)_p(v_1, \dots, v_k) = \omega_{F(p)}\big(dF_p(v_1), \dots, dF_p(v_k)\big) \qquad \text{(definition of }F^*\text{).}$$
> > The right-hand side uses only three pieces of data: the point $F(p)$, the linear map $dF_p : T_pM \to T_{F(p)}N$, and the single covector $\omega_{F(p)} \in \Lambda^k T^*_{F(p)}N$.
> >
> > **Each datum is local.** The differential $dF_p$ is computed from $F$ on any neighbourhood of $p$ (it is the derivative of $F$ at $p$ and depends only on the germ of $F$ at $p$). The covector $\omega_{F(p)}$ is the value of $\omega$ at the single point $F(p)$ and depends only on the germ of $\omega$ at $F(p)$. Hence $(F^*\omega)_p$ is unchanged if $F$ is replaced by any smooth map agreeing with it near $p$ and $\omega$ by any form agreeing with it near $F(p)$.
> >
> > **Restriction.** For $p \in U$, the map $F|_U$ agrees with $F$ near $p$, so $(F^*\omega)_p = ((F|_U)^*\omega)_p$; as $p$ ranges over $U$ this reads $(F^*\omega)|_U = (F|_U)^*\omega$.
> >
> > **Vanishing.** Suppose $\omega \equiv 0$ on an open $V \subseteq N$ and let $p \in F^{-1}(V)$, so $F(p) \in V$ and $\omega_{F(p)} = 0$. Then the displayed formula gives $(F^*\omega)_p(v_1, \dots, v_k) = 0_{F(p)}(\cdots) = 0$ for all $v_i$, so $(F^*\omega)_p = 0$. Therefore $F^*\omega$ vanishes on $F^{-1}(V)$. $\blacksquare$

> [!note]- Lemma 3: Pullback is an $\mathbb{R}$-linear homomorphism of the wedge algebra
> **Statement:** Let $F : M \to N$ be smooth. Then $F^* : \Omega^\bullet(N) \to \Omega^\bullet(M)$ is $\mathbb{R}$-linear and satisfies $F^*(\omega \wedge \eta) = F^*\omega \wedge F^*\eta$ for all $\omega \in \Omega^k(N)$, $\eta \in \Omega^\ell(N)$. This is clause (i) of the theorem.
>
> **Hint:** Fix $p$ and set $L = dF_p$; the claim is the pointwise fact that the algebraic pullback $L^* : \Lambda^\bullet T^*_{F(p)}N \to \Lambda^\bullet T^*_pM$ is a wedge homomorphism, which is checked on wedges of one-covectors via the determinant identity.
>
> **Why needed:** It lets $F^*$ distribute over a coordinate monomial $\omega_J\,dy^{j_1} \wedge \cdots \wedge dy^{j_k}$, reducing every degree to the degree-zero (function) case.
>
> > [!note]- Full proof
> > **What is assumed and what is shown.** Fix $p \in M$ and write $L = dF_p : T_pM \to T_{F(p)}N$, a linear map, and $q = F(p)$. For a covector $\alpha \in \Lambda^r T^*_q N$ define its algebraic pullback $L^*\alpha \in \Lambda^r T^*_p M$ by $(L^*\alpha)(v_1, \dots, v_r) = \alpha(Lv_1, \dots, Lv_r)$; then $(F^*\omega)_p = L^*(\omega_q)$ by definition of the pullback. We show $L^*$ is $\mathbb{R}$-linear and $L^*(\alpha \wedge \beta) = L^*\alpha \wedge L^*\beta$; evaluating at every $p$ then gives the statement for forms.
> >
> > **Linearity.** For $\alpha, \alpha' \in \Lambda^r T^*_q N$ and $c \in \mathbb{R}$,
> > $$L^*(\alpha + c\alpha')(v_1, \dots, v_r) = (\alpha + c\alpha')(Lv_1, \dots, Lv_r) = \alpha(Lv_1, \dots) + c\,\alpha'(Lv_1, \dots) = (L^*\alpha + cL^*\alpha')(v_1, \dots, v_r),$$
> > using the linearity of $\alpha \mapsto \alpha(Lv_1, \dots, Lv_r)$ in $\alpha$. Hence $L^*$ is $\mathbb{R}$-linear, and so is $F^*$ pointwise, hence as a map of forms.
> >
> > **Reduction to decomposables.** By the [[Thm - Wedge Product Properties|basis identity for the wedge product]] — for a basis $(\varepsilon^i)$ of $T^*_q N$ the products $\varepsilon^{i_1} \wedge \cdots \wedge \varepsilon^{i_r}$ with $i_1 < \cdots < i_r$ form a basis of $\Lambda^r T^*_q N$ — every element of $\Lambda^\bullet T^*_q N$ is an $\mathbb{R}$-linear combination of wedges of one-covectors. Since both sides of $L^*(\alpha \wedge \beta) = L^*\alpha \wedge L^*\beta$ are $\mathbb{R}$-bilinear in $(\alpha, \beta)$ (by the linearity just shown and the bilinearity of $\wedge$), it suffices to verify the identity when $\alpha = \alpha^1 \wedge \cdots \wedge \alpha^k$ and $\beta = \beta^1 \wedge \cdots \wedge \beta^\ell$ are wedges of one-covectors $\alpha^i, \beta^j \in T^*_q N$.
> >
> > **Pullback of a wedge of one-covectors.** For one-covectors $\gamma^1, \dots, \gamma^r \in T^*_q N$ and vectors $v_1, \dots, v_r \in T_pM$, the [[Thm - Wedge Product Properties|determinant identity]] $(\gamma^1 \wedge \cdots \wedge \gamma^r)(w_1, \dots, w_r) = \det(\gamma^i(w_j))$ gives
> > $$L^*(\gamma^1 \wedge \cdots \wedge \gamma^r)(v_1, \dots, v_r) = (\gamma^1 \wedge \cdots \wedge \gamma^r)(Lv_1, \dots, Lv_r) = \det\!\big(\gamma^i(Lv_j)\big) \qquad \text{(definition of }L^*\text{; determinant identity).}$$
> > Each entry $\gamma^i(Lv_j) = (L^*\gamma^i)(v_j)$ by definition of $L^*$ on the one-covector $\gamma^i$, so
> > $$\det\!\big(\gamma^i(Lv_j)\big) = \det\!\big((L^*\gamma^i)(v_j)\big) = (L^*\gamma^1 \wedge \cdots \wedge L^*\gamma^r)(v_1, \dots, v_r) \qquad \text{(determinant identity, read backwards).}$$
> > Since this holds for all $v_1, \dots, v_r$, we conclude $L^*(\gamma^1 \wedge \cdots \wedge \gamma^r) = L^*\gamma^1 \wedge \cdots \wedge L^*\gamma^r$ for any one-covectors.
> >
> > **Homomorphism on decomposables.** Apply the previous display to the concatenated list $\alpha^1, \dots, \alpha^k, \beta^1, \dots, \beta^\ell$:
> > $$L^*(\alpha \wedge \beta) = L^*(\alpha^1 \wedge \cdots \wedge \alpha^k \wedge \beta^1 \wedge \cdots \wedge \beta^\ell) = L^*\alpha^1 \wedge \cdots \wedge L^*\alpha^k \wedge L^*\beta^1 \wedge \cdots \wedge L^*\beta^\ell,$$
> > where the first equality uses associativity of $\wedge$ ([[Thm - Wedge Product Properties|associativity]]). Regrouping the same associativity,
> > $$L^*\alpha^1 \wedge \cdots \wedge L^*\beta^\ell = (L^*\alpha^1 \wedge \cdots \wedge L^*\alpha^k) \wedge (L^*\beta^1 \wedge \cdots \wedge L^*\beta^\ell) = L^*\alpha \wedge L^*\beta,$$
> > using the previous display once for each of $\alpha$ and $\beta$. This proves the identity on decomposables, hence in general.
> >
> > **Conclusion.** Evaluating at every point $p$, $F^*(\omega \wedge \eta) = F^*\omega \wedge F^*\eta$, and $F^*$ is $\mathbb{R}$-linear. $\blacksquare$

> [!note]- Lemma 4: A wedge of exact one-forms is closed
> **Statement:** Let $h^1, \dots, h^k \in C^\infty(P)$ be smooth functions on a manifold $P$. Then $d(dh^1 \wedge \cdots \wedge dh^k) = 0$.
>
> **Hint:** Each $dh^i$ is closed because $d^2 = 0$; propagate through the wedge by the graded Leibniz rule and induction on $k$.
>
> **Why needed:** In computing $d(F^*\omega)$, the exterior derivative must cross the wedge $dF^{j_1} \wedge \cdots \wedge dF^{j_k}$ of pulled-back coordinate differentials; the graded Leibniz rule leaves a term proportional to $d$ of that wedge, and this lemma shows it vanishes.
>
> > [!note]- Full proof
> > **What is assumed and what is shown.** Let $h^1, \dots, h^k \in C^\infty(P)$. We show $d(dh^1 \wedge \cdots \wedge dh^k) = 0$ by induction on $k$.
> >
> > **Base case $k = 1$.** $d(dh^1) = 0$ by nilpotence of the exterior derivative, [[Thm - d-Squared-is-Zero]] — for every form $\alpha$, $d(d\alpha) = 0$, applied to the $0$-form $\alpha = h^1$.
> >
> > **Inductive step.** Suppose $d(dh^2 \wedge \cdots \wedge dh^k) = 0$; write $\beta = dh^2 \wedge \cdots \wedge dh^k \in \Omega^{k-1}(P)$, a form of degree $k-1$. Then $dh^1 \wedge \cdots \wedge dh^k = dh^1 \wedge \beta$, and by the [[Def - Exterior Derivative on a Manifold|graded Leibniz rule]] applied to the degree-$1$ form $dh^1$,
> > $$d(dh^1 \wedge \beta) = d(dh^1) \wedge \beta + (-1)^1\,dh^1 \wedge d\beta \qquad \text{(graded Leibniz rule, }\deg dh^1 = 1\text{).}$$
> > The first term vanishes because $d(dh^1) = 0$ (nilpotence, [[Thm - d-Squared-is-Zero]]); the second vanishes because $d\beta = 0$ (inductive hypothesis). Hence $d(dh^1 \wedge \cdots \wedge dh^k) = 0$.
> >
> > **Conclusion.** By induction the claim holds for every $k \ge 1$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $F : M \to N$ be smooth. Clause (i), $F^*(\omega \wedge \eta) = F^*\omega \wedge F^*\eta$, together with the $\mathbb{R}$-linearity of $F^*$, is exactly **Lemma 3**, proved above; we use it freely below. It remains to prove clause (ii), $F^*(d\omega) = d(F^*\omega)$ for $\omega \in \Omega^k(N)$.
>
> **Step 0 — reduction to a chart on $N$.** Both $F^*(d\omega)$ and $d(F^*\omega)$ are smooth $(k+1)$-forms on $M$. Two forms on $M$ are equal if and only if they agree on each set of an open cover of $M$. Cover $N$ by charts $(V_\alpha, y^j)$ and set $U_\alpha = F^{-1}(V_\alpha)$, an open cover of $M$ because $F$ is continuous. We claim it suffices to prove
> $$F^*(d\omega)\big|_{U_\alpha} = d(F^*\omega)\big|_{U_\alpha} \qquad\text{for each }\alpha.$$
> Indeed, by the locality of the pullback (**Lemma 2**), $\big(F^*(d\omega)\big)\big|_{U_\alpha} = (F|_{U_\alpha})^*\big((d\omega)|_{V_\alpha}\big)$ and $\big(F^*\omega\big)\big|_{U_\alpha} = (F|_{U_\alpha})^*\big(\omega|_{V_\alpha}\big)$; by the locality of the exterior derivative (**Lemma 1**), $\big(d(F^*\omega)\big)\big|_{U_\alpha} = d\big((F^*\omega)|_{U_\alpha}\big)$ and $(d\omega)|_{V_\alpha} = d(\omega|_{V_\alpha})$. Thus each side, restricted to $U_\alpha$, is computed entirely from $F|_{U_\alpha} : U_\alpha \to V_\alpha$ and the form $\omega|_{V_\alpha}$ on the chart $V_\alpha$. Fix one such $\alpha$ and write $F$, $\omega$, $U$, $V$ for the restricted data; on $V$ the coordinates $y^j$ are available and $F$ has component functions $F^j = y^j \circ F \in C^\infty(U)$.
>
> **Step 1 — coordinate expression of $\omega$.** On the chart $V$ the form $\omega$ has a unique expansion
> $$\omega = \sum'_J \omega_J\,dy^J = \sum'_J \omega_J\,dy^{j_1} \wedge \cdots \wedge dy^{j_k}, \qquad \omega_J \in C^\infty(V),$$
> the sum over increasing multi-indices $J = (j_1 < \cdots < j_k)$ (existence and uniqueness of the coordinate expansion of a $k$-form, [[Def - Differential k-Form on a Manifold|definition of a differential form in coordinates]]).
>
> **Step 2 — the pullback $F^*\omega$ in terms of the $F^j$.** Applying $F^*$, using its $\mathbb{R}$-linearity and the wedge-homomorphism property (**Lemma 3**),
> $$F^*\omega = \sum'_J F^*(\omega_J)\;(F^*dy^{j_1}) \wedge \cdots \wedge (F^*dy^{j_k}) \qquad \text{(Lemma 3, applied to the monomial }\omega_J\,dy^{j_1} \wedge \cdots \wedge dy^{j_k}\text{).}$$
> Here $F^*(\omega_J) = \omega_J \circ F$ is the pullback of the function $\omega_J$ (pullback on $0$-forms). For each coordinate one-form, the degree-zero naturality — this is [[Thm - Pullback Commutes with d for 1-Forms]]: *for a smooth map $F : M \to N$ and $g \in C^\infty(N)$, one has $F^*(dg) = d(g \circ F)$ as one-forms on $M$* — applied to the coordinate function $g = y^j$ gives
> $$F^*(dy^j) = d(y^j \circ F) = dF^j \qquad \text{(Thm ``Pullback Commutes with }d\text{ for 1-Forms'', with }g = y^j\text{).}$$
> Substituting,
> $$F^*\omega = \sum'_J (\omega_J \circ F)\;dF^{j_1} \wedge \cdots \wedge dF^{j_k}. \tag{$\ast$}$$
>
> **Step 3 — compute $d(F^*\omega)$.** Apply $d$ to $(\ast)$, using $\mathbb{R}$-linearity of $d$ and the [[Def - Exterior Derivative on a Manifold|graded Leibniz rule]] on each monomial, viewing $(\omega_J \circ F)$ as a $0$-form and $dF^{j_1} \wedge \cdots \wedge dF^{j_k}$ as a $k$-form:
> $$d(F^*\omega) = \sum'_J \Big[ d(\omega_J \circ F) \wedge \big(dF^{j_1} \wedge \cdots \wedge dF^{j_k}\big) + (-1)^0\,(\omega_J \circ F)\, d\big(dF^{j_1} \wedge \cdots \wedge dF^{j_k}\big) \Big] \qquad \text{(graded Leibniz, }\deg(\omega_J \circ F) = 0\text{).}$$
> By **Lemma 4** the wedge $dF^{j_1} \wedge \cdots \wedge dF^{j_k}$ of the exact one-forms $dF^{j_i}$ is closed, so $d(dF^{j_1} \wedge \cdots \wedge dF^{j_k}) = 0$ and the second summand vanishes. Hence
> $$d(F^*\omega) = \sum'_J d(\omega_J \circ F) \wedge dF^{j_1} \wedge \cdots \wedge dF^{j_k}. \tag{$\ast\ast$}$$
>
> **Step 4 — compute $F^*(d\omega)$.** On the chart $V$ the [[Thm - Coordinate Expression for the Exterior Derivative|coordinate formula for the exterior derivative]] — *for $\omega = \sum'_J \omega_J\,dy^J$ one has $d\omega = \sum'_J d\omega_J \wedge dy^J$* — gives
> $$d\omega = \sum'_J d\omega_J \wedge dy^{j_1} \wedge \cdots \wedge dy^{j_k} \qquad \text{(coordinate formula for }d\text{).}$$
> Apply $F^*$, again by its $\mathbb{R}$-linearity and the wedge-homomorphism property (**Lemma 3**):
> $$F^*(d\omega) = \sum'_J (F^* d\omega_J) \wedge (F^*dy^{j_1}) \wedge \cdots \wedge (F^*dy^{j_k}) \qquad \text{(Lemma 3).}$$
> Now $d\omega_J$ is the differential of the function $\omega_J \in C^\infty(V)$, so the same degree-zero naturality [[Thm - Pullback Commutes with d for 1-Forms|used in Step 2]] — the identity $F^*(dg) = d(g \circ F)$ — applied with $g = \omega_J$, gives $F^*(d\omega_J) = d(\omega_J \circ F)$; and $F^*(dy^{j_i}) = dF^{j_i}$ as in Step 2. Substituting,
> $$F^*(d\omega) = \sum'_J d(\omega_J \circ F) \wedge dF^{j_1} \wedge \cdots \wedge dF^{j_k}. \tag{$\ast\ast\ast$}$$
>
> **Step 5 — compare and globalise.** The right-hand sides of $(\ast\ast)$ and $(\ast\ast\ast)$ are identical term by term, so
> $$d(F^*\omega) = F^*(d\omega) \qquad\text{on } U = U_\alpha.$$
> Since $\{U_\alpha\}$ covers $M$ and the identity holds on each $U_\alpha$ (Step 0), it holds on all of $M$.
>
> **Conclusion.** For every smooth $F : M \to N$ and every $\omega \in \Omega^k(N)$, $F^*(\omega \wedge \eta) = F^*\omega \wedge F^*\eta$ (Lemma 3) and $F^*(d\omega) = d(F^*\omega)$. Therefore the pullback is an $\mathbb{R}$-linear homomorphism of graded algebras that commutes with the exterior derivative. $\blacksquare$

---

# The Vector-Valued Version

The gauge-theoretic uses of naturality are almost always for forms whose coefficients lie in a Lie algebra $\mathfrak{g}$, so we record the extension to a fixed coefficient space and prove that it reduces cleanly to the scalar theorem.

> **Theorem (naturality for $V$-valued forms).** Let $V$ be a fixed finite-dimensional real vector space with basis $(e_a)_{a=1}^r$. A $V$-valued $k$-form on $N$ is $\omega = \sum_{a=1}^r \omega^a \otimes e_a$ with scalar components $\omega^a \in \Omega^k(N)$. Define the pullback and exterior derivative componentwise,
> $$F^*\omega := \sum_{a=1}^r (F^*\omega^a) \otimes e_a, \qquad d\omega := \sum_{a=1}^r (d\omega^a) \otimes e_a,$$
> and for a scalar form $\eta \in \Omega^\ell(N)$ set $\eta \wedge \omega := \sum_a (\eta \wedge \omega^a) \otimes e_a$. Then
> $$F^*(\eta \wedge \omega) = F^*\eta \wedge F^*\omega \qquad\text{and}\qquad F^*(d\omega) = d(F^*\omega),$$
> and neither the operators nor these identities depend on the chosen basis of $V$.

> [!note]- Complete formal proof
> **What is assumed and what is shown.** Fix a basis $(e_a)$ of $V$ and let $\omega = \sum_a \omega^a \otimes e_a$ with $\omega^a \in \Omega^k(N)$, and $\eta \in \Omega^\ell(N)$ scalar. We prove the two identities and then their basis-independence.
>
> **Naturality of $d$.** Using the componentwise definitions and the scalar theorem on each component,
> $$F^*(d\omega) = F^*\!\Big(\sum_a (d\omega^a) \otimes e_a\Big) = \sum_a F^*(d\omega^a) \otimes e_a = \sum_a d(F^*\omega^a) \otimes e_a = d\Big(\sum_a (F^*\omega^a) \otimes e_a\Big) = d(F^*\omega),$$
> where the first and last equalities are the componentwise definitions, the second is the definition of $F^*$ on a $V$-valued form (with the constant basis vectors $e_a$ untouched), the third applies clause (ii) of the scalar theorem to each scalar component $\omega^a$, and the fourth is again the componentwise definition of $d$.
>
> **Compatibility with the scalar wedge.** By the same componentwise reduction,
> $$F^*(\eta \wedge \omega) = F^*\!\Big(\sum_a (\eta \wedge \omega^a) \otimes e_a\Big) = \sum_a F^*(\eta \wedge \omega^a) \otimes e_a = \sum_a (F^*\eta \wedge F^*\omega^a) \otimes e_a = F^*\eta \wedge F^*\omega,$$
> the third equality being clause (i) of the scalar theorem applied to the pair $(\eta, \omega^a)$.
>
> **Basis-independence.** Let $(\tilde e_b)$ be another basis, related by $e_a = \sum_b c^b{}_a\,\tilde e_b$ with a constant invertible matrix $(c^b{}_a) \in \mathbb{R}^{r \times r}$. Then $\omega = \sum_a \omega^a \otimes e_a = \sum_b \big(\sum_a c^b{}_a\,\omega^a\big) \otimes \tilde e_b$, so the new components are $\tilde\omega^b = \sum_a c^b{}_a\,\omega^a$. Because $F^*$ and $d$ are $\mathbb{R}$-linear and the $c^b{}_a$ are constants,
> $$\sum_b (F^*\tilde\omega^b) \otimes \tilde e_b = \sum_{b}\Big(\sum_a c^b{}_a\,F^*\omega^a\Big) \otimes \tilde e_b = \sum_a (F^*\omega^a) \otimes \Big(\sum_b c^b{}_a \tilde e_b\Big) = \sum_a (F^*\omega^a) \otimes e_a,$$
> so the componentwise definition of $F^*\omega$ is the same in both bases, and likewise for $d\omega$. The two identities, being basis-free statements about these operators, therefore hold independently of the basis.
>
> **Conclusion.** The $V$-valued pullback commutes with the exterior derivative and with the scalar wedge, and does so basis-independently. $\blacksquare$

When $V = \mathfrak{g}$ is a Lie algebra there is in addition the bracket-wedge $[\cdot \wedge \cdot]$ of $\mathfrak{g}$-valued forms. Its naturality, $F^*[\alpha \wedge \beta] = [F^*\alpha \wedge F^*\beta]$, follows by the same componentwise argument together with clause (i): in a basis $[\alpha \wedge \beta] = \sum_{a,b} (\alpha^a \wedge \beta^b) \otimes [e_a, e_b]$, and $F^*$ acts as a wedge homomorphism on each scalar factor while leaving the constant brackets $[e_a, e_b]$ fixed. This is the form of naturality that carries $s^*\Omega = dA_s + \tfrac12[A_s \wedge A_s]$ downstairs in the derivation of the local structure equation.

---

# Cross-Field Exercise Suggestions

**Maurer–Cartan pullback on a Lie group.** Let $G$ be a matrix Lie group with left Maurer–Cartan form $\theta = g^{-1}\,dg \in \Omega^1(G; \mathfrak{g})$, and let $F : M \to G$ be a smooth map, so $F^*\theta = F^{-1}\,dF$ is the logarithmic derivative of $F$. The structure equation $d\theta + \tfrac12[\theta \wedge \theta] = 0$ pulls back, by naturality of $d$ and of the bracket-wedge, to $d(F^*\theta) + \tfrac12[F^*\theta \wedge F^*\theta] = 0$. This is non-obvious as an application because the pulled-back form $F^{-1}dF$ is a concrete matrix of one-forms with no visible group left in it, yet it satisfies the same quadratic identity; the theorem is what transports the identity from $G$ to $M$ without recomputation. This is the mechanism behind the gauge transformation law for local connection forms.

**Homotopy invariance of de Rham cohomology.** Given a smooth homotopy $H : M \times [0,1] \to N$ between $F_0$ and $F_1$ and a closed form $\omega \in \Omega^k(N)$, one wants $F_0^*\omega$ and $F_1^*\omega$ to differ by an exact form. The construction integrates $H^*\omega$ over the interval factor and uses $H^*(d\omega) = d(H^*\omega) = 0$ to run Stokes on the product; naturality of $d$ on the single map $H$ is exactly what makes the chain-homotopy formula close. The application is non-obvious because the family $t \mapsto F_t^*\omega$ looks like it needs a $t$-dependent version of the theorem, whereas the trick is to see the family as one pullback along $H$ and apply the theorem once.

**Pulling back the volume form under a change of variables.** For an orientation-preserving diffeomorphism $F : M \to N$ of oriented $n$-manifolds and the volume form $\omega$ on $N$, naturality of $d$ makes $F^*$ a chain map, so it commutes with the boundary in Stokes' theorem and yields $\int_M F^*\omega = \int_N \omega$. The application is non-obvious because the identity is usually stated as a Jacobian computation with no forms in sight; recognising the change-of-variables formula as the top-degree instance of $F^*d = dF^*$ paired with Stokes is the transferable move.

---

# Bridges

- **Local connection and curvature forms.** A [[Def - Local Connection Form and Gauge Potential|local connection form]] is the pullback $A_s = s^*\omega$ of a principal connection along a local section $s$, and the local curvature is $s^*\Omega$. Applying $s^*$ to the structure equation $\Omega = d\omega + \tfrac12[\omega \wedge \omega]$ and using $s^*(d\omega) = d(s^*\omega) = dA_s$ (this theorem) together with $s^*[\omega \wedge \omega] = [A_s \wedge A_s]$ (the bracket-wedge naturality above) gives the local structure equation $s^*\Omega = dA_s + \tfrac12[A_s \wedge A_s]$. This is the construction that turns a global connection into computable matrices of forms on coordinate patches; see [[Thm - Transformation of Local Connection and Curvature Forms]].

- **Naturality of Chern–Weil forms.** For an $\operatorname{Ad}$-invariant polynomial $f$ and a bundle map covering $g : M' \to M$, the pullback connection has curvature $g^* F_A$, and $g^*(f(F_A)) = f(g^* F_A)$ because $f(F_A)$ is assembled from wedges of the matrix entries of $F_A$, on which $g^*$ is an algebra homomorphism (clause (i)), while the closedness $d\,f(F_A) = 0$ that makes it a characteristic representative is preserved because $g^*$ commutes with $d$ (clause (ii)). This is why the [[Def - Chern-Weil Form of an Invariant Polynomial|Chern–Weil form]] defines a natural cohomology class, and it is the naturality that gives characteristic classes their functoriality.

- **The exterior covariant derivative and pulled-back bundles.** When a connection is pulled back along $g : M' \to M$, the induced exterior covariant derivative on bundle-valued forms is compatible with $g^*$: the local formula $d^\nabla(e\sigma) = e(d\sigma + A \wedge \sigma)$ pulls back by combining this theorem on the scalar part $d\sigma$ with the pullback of $A \wedge \sigma$. Naturality of the plain $d$ is the scalar backbone of the naturality of $d^\nabla$; see [[Def - Exterior Covariant Derivative on a Vector Bundle]].

---

# Unlocked by This

> [!tip] Functoriality of de Rham cohomology *(from Algebraic Topology)*
> Because $F^* d = d F^*$, a smooth map $F : M \to N$ sends closed forms to closed forms and exact forms to exact forms, so it induces a well-defined linear map $F^* : H^k_{dR}(N) \to H^k_{dR}(M)$ on de Rham cohomology, contravariantly and compatibly with composition. This is what makes de Rham cohomology a smooth invariant. See **de Rham cohomology as a contravariant functor**.

> [!tip] The pullback is a cochain map of the de Rham complex *(from Homological Algebra)*
> Clauses (i) and (ii) together say that $F^* : (\Omega^\bullet(N), d) \to (\Omega^\bullet(M), d)$ is a morphism of commutative differential graded algebras: it respects the product and the differential. Every algebraic consequence of being a cochain map — long exact sequences, spectral sequences, cup-product structures on cohomology — is then available for smooth maps of manifolds.
