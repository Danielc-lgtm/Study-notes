---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - Kuranishi Model for a Fredholm Map"
  - "Thm - Inverse Function Theorem on Banach Spaces"
  - "Def - Regular Value and Transversality for Fredholm Maps"
  - "Def - Fredholm Map and Its Index"
  - "Def - Smooth Manifold with Boundary"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $X$ and $Y$ are **Banach manifolds** — Hausdorff, second countable topological spaces with an atlas of charts into open subsets of separable Banach spaces and smooth transition maps ([[Def - Banach Manifold and Smooth Maps between Banach Spaces|Banach manifold]]). For a point $x\in X$ the tangent space is the Banach space $T_xX$, and a smooth map $F\colon X\to Y$ has at each $x$ a bounded linear differential $d_xF\colon T_xX\to T_{F(x)}Y$. We write $\ker d_xF\subseteq T_xX$ for its kernel, $\operatorname{Im}d_xF\subseteq T_{F(x)}Y$ for its image, and $\operatorname{coker}d_xF := T_{F(x)}Y/\operatorname{Im}d_xF$ for its cokernel.

A bounded linear operator $A\colon E\to G$ between Banach spaces is a **Fredholm operator** if $\dim\ker A<\infty$, its range $\operatorname{Im}A$ is closed, and $\dim\operatorname{coker}A<\infty$; its **index** is the integer $\operatorname{index}A := \dim\ker A - \dim\operatorname{coker}A$ ([[Def - Fredholm Operator and Index|Fredholm operator and index]]). A smooth map $F\colon X\to Y$ is a [[Def - Fredholm Map and Its Index|Fredholm map]] if $d_xF$ is a Fredholm operator for every $x\in X$; the index $\operatorname{index}d_xF$ is then locally constant in $x$ and hence constant on each connected component of $X$, and this common value on a component is written $\operatorname{index}F$.

A point $y\in Y$ is a **regular value** of $F$ if $d_xF$ is surjective for every $x\in F^{-1}(y)$ (vacuously so if $F^{-1}(y)=\varnothing$); the set of $x$ where $d_xF$ fails to be surjective is $\operatorname{Crit}(F)$, the critical points. For a finite-dimensional embedded submanifold $Z\subseteq Y$ with tangent space $T_zZ\subseteq T_zY$ at $z\in Z$, the map $F$ is **transverse to $Z$**, written $F\pitchfork Z$, if
$$\operatorname{Im}d_xF + T_zZ = T_zY\qquad\text{for every }z\in Z\text{ and every }x\in F^{-1}(z);$$
the case $Z=\{z\}$ recovers "$z$ is a regular value" ([[Def - Regular Value and Transversality for Fredholm Maps|regular value and transversality]]).

An **embedded submanifold** of a Banach manifold is a subset that is, in a chart around each of its points, the intersection of the chart domain with a closed subspace admitting a closed complement; a finite-dimensional subspace of a Banach space is always closed and always complemented, so a finite-dimensional embedded submanifold has this local model automatically. A **Banach manifold with boundary** is modelled on **half-spaces**: each chart maps into an open subset of a half-space $\mathbb{H}_\lambda := \{u\in E : \lambda(u)\ge 0\}$ of a Banach model space $E$, where $\lambda\colon E\to\mathbb{R}$ is a fixed nonzero bounded linear functional (equivalently $E = E'\times[0,\infty)$ with $E' = \ker\lambda$); its boundary $\partial X$ is the closed submanifold corresponding to $\{\lambda=0\}$, and the tangent space $T_xX$ at a boundary point is the **full** model space $E$, not the half-space ([[Def - Smooth Manifold with Boundary|smooth manifold with boundary]]). We write $\bigsqcup$ for a disjoint union.

> [!warning] Convention:
> Haydys states the finite-dimensional index of a smooth map between finite-dimensional manifolds as $\operatorname{index}F = \dim X - \dim Y$ (Haydys p. 48 prints "$\dim Y-\dim X$", a sign typo corrected in the source's typo appendix, item 11); we use $\operatorname{index}A = \dim\ker A - \dim\operatorname{coker}A$ throughout, which agrees: for $A\colon\mathbb{R}^m\to\mathbb{R}^n$ one has $\dim\ker A - \dim\operatorname{coker}A = (m-\operatorname{rank}A)-(n-\operatorname{rank}A) = m-n$. The three results below are Haydys's Corollary 163 (part (i)), Theorem 165 (part (ii)), and the boundary version he uses implicitly in the degree theory of §6.2; Haydys proves only part (i) (a two-line corollary of the Kuranishi model) and dismisses part (ii) with "just as in the finite-dimensional case [GP10]", so parts (ii) and (iii) are written out in full here.

---

# Statement

> **Theorem (regular value and transversality for Fredholm maps).** Let $F\colon X\to Y$ be a smooth Fredholm map between Banach manifolds.
>
> **(i) (Regular value theorem.)** If $y\in Y$ is a regular value of $F$, then $F^{-1}(y)$ is a smooth embedded submanifold of $X$; on each connected component of $X$ that it meets, its dimension is the finite number $\operatorname{index}F$ (in particular $F^{-1}(y)=\varnothing$ on any component where $\operatorname{index}F<0$), and its tangent space is
> $$T_xF^{-1}(y) = \ker d_xF\qquad\text{for every }x\in F^{-1}(y).$$
>
> **(ii) (Transversality theorem.)** If $Z\subseteq Y$ is a finite-dimensional embedded submanifold and $F\pitchfork Z$, then $F^{-1}(Z)$ is a smooth embedded submanifold of $X$; on each component of $X$ that it meets its dimension is $\operatorname{index}F + \dim Z$, and its tangent space is
> $$T_xF^{-1}(Z) = (d_xF)^{-1}(T_{F(x)}Z)\qquad\text{for every }x\in F^{-1}(Z).$$
>
> **(iii) (Boundary version.)** Suppose $X$ is a Banach manifold with boundary $\partial X$, and $y\in Y$ is a regular value of both $F$ and the restriction $F|_{\partial X}\colon\partial X\to Y$. Then $F^{-1}(y)$ is a smooth manifold with boundary, with
> $$\partial\big(F^{-1}(y)\big) = F^{-1}(y)\cap\partial X = (F|_{\partial X})^{-1}(y),$$
> and $\dim F^{-1}(y) = \operatorname{index}F$ on each component (where $F$ has constant index).

> **Corollary (the cobordism of a homotopy).** Let $F_0,F_1\colon X\to Y$ be smooth Fredholm maps between Banach manifolds ($X$ without boundary), and let $H\colon X\times[0,1]\to Y$ be a smooth homotopy with $H(\cdot,0)=F_0$ and $H(\cdot,1)=F_1$, such that $H$ is a Fredholm map. If $y\in Y$ is a regular value of $H$, of $F_0$, and of $F_1$, then $H^{-1}(y)$ is a smooth manifold with boundary
> $$\partial\big(H^{-1}(y)\big) = \big(F_0^{-1}(y)\times\{0\}\big)\;\bigsqcup\;\big(F_1^{-1}(y)\times\{1\}\big),$$
> of dimension $\operatorname{index}F + 1$ on each component, where $\operatorname{index}F$ is the common index of $F_0$ and $F_1$.

The three parts are tied together by a single mechanism, developed in the proof: **wherever $y$ is a regular value, the Kuranishi model of $F$ has zero cokernel and so is literally a submanifold chart**, and each of (ii) and (iii) reduces to (i) by converting its extra hypothesis (transversality to $Z$; regularity on the boundary) into the ordinary regularity of an auxiliary map.

---

# Motivation

The single most useful thing one can do with a map is to slice it: fix a value $y$ in the target and look at the set $F^{-1}(y)$ of solutions of the equation $F(x)=y$. In finite dimensions the [[Thm - Regular Value Theorem on Manifolds|regular value theorem]] says that when $y$ is a regular value the solution set is a smooth manifold of dimension $\dim X - \dim Y$, and this is the workhorse that produces spheres as level sets of quadratic forms, Lie groups as level sets of matrix equations, and configuration spaces of mechanics as constraint sets. The whole of gauge theory rests on the infinite-dimensional analogue: the objects one cares about — the space of anti-self-dual connections modulo gauge, the Seiberg–Witten moduli space — are cut out inside an infinite-dimensional space of fields by a nonlinear differential equation, and one wants to know that the solution set is a *finite-dimensional* smooth manifold whose dimension one can compute.

The obstruction to copying the finite-dimensional statement verbatim is that "$\dim X - \dim Y$" is the difference of two infinities. The Fredholm condition is exactly what repairs this. A Fredholm map is one whose linearisation, at every point, has finite-dimensional kernel and finite-dimensional cokernel; the difference of these two finite numbers, the index, is the substitute for $\dim X - \dim Y$. Part (i) is the statement that this substitution works: at a regular value, the solution set is a smooth manifold of dimension exactly the index. Because the index is a *stable* quantity — invariant under compact perturbation and continuous in the operator — it can be computed by deformation and, for elliptic operators, by the Atiyah–Singer index theorem, so the dimension of a moduli space becomes a topological number.

Part (ii) generalises the target from a point to a finite-dimensional submanifold $Z$, replacing "regular value" by "transverse to $Z$". This is the form one needs when the value cannot be moved — for instance when it must be a fixed point of a symmetry — and one instead intersects with a submanifold of allowed values, or when one wants the dimension formula $\operatorname{index}F+\dim Z$ that interpolates between a level set ($\dim Z=0$) and an open set ($Z=Y$, in finite dimensions). Part (iii) is what makes the *degree* well defined: to compare the count of solutions at two regular values one connects them and studies a one-parameter family, whose universal solution set is a manifold *with boundary* the two fibres, so a boundary version of the regular value theorem is not a technical afterthought but the very device that turns "count of solutions" into a deformation invariant.

This page assumes the reader has met the finite-dimensional regular value theorem, the notion of a Fredholm operator and its index, and the local normal form of a Fredholm map — the Kuranishi model. It does not assume any prior infinite-dimensional differential topology; every step is reduced either to the Kuranishi model or to a finite-dimensional fact proved on the page.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypothesis of part (i) is "$F$ Fredholm and $y$ regular", but in practice one almost never verifies surjectivity of $d_xF$ at each solution directly. The skill is recognising the disguised inputs that deliver it.

The first disguised source is **a semilinear elliptic equation on a closed manifold**. A map of the form $F(u)=Lu+N(u)$, where $L$ is an elliptic differential operator between Sobolev completions and $N$ is a nonlinearity of strictly lower order, is Fredholm because $d_uF = L + d_uN$ is $L$ plus an operator that factors through a compact Sobolev embedding, hence a compact perturbation of the Fredholm operator $L$ ([[Thm - Stability of the Fredholm Property under Small and Compact Perturbations|stability of the Fredholm property under compact perturbations]]); its index equals $\operatorname{index}L$, which elliptic theory computes. The bridge $B\Rightarrow A$ is "elliptic principal symbol $+$ lower-order nonlinearity $\Rightarrow$ Fredholm map of computable index", and it is non-obvious because ellipticity is a condition on the top-order symbol while the Fredholm property is a global analytic fact that only holds after completing in the right Sobolev norms. *Example problem:* show that $u\mapsto\Delta u+u^3$ on a closed surface is a smooth Fredholm map of index $0$, and deduce that for a residual set of right-hand sides its solution set is a smooth $0$-manifold.

The second disguised source is **any smooth map between finite-dimensional manifolds**. Such a map is trivially Fredholm, with $\operatorname{index}=\dim X-\dim Y$ at every point, because every linear map between finite-dimensional spaces has closed range and finite-dimensional kernel and cokernel. The bridge is that the finite-dimensional [[Thm - Regular Value Theorem on Manifolds|regular value theorem]] is the special case of part (i) with the index made explicit; recognising a finite-dimensional problem as a Fredholm problem lets one apply the parametric and degree machinery of this chapter uniformly. *Example problem:* recover that $S^{n-1}=f^{-1}(1)$ for $f(x)=|x|^2$ on $\mathbb{R}^n$ is a manifold of dimension $n-1=\operatorname{index}f$, since $d_xf$ has rank $1$ at each nonzero $x$.

The third disguised source is **a map whose nonzero degree or index computation has already been done**. If one knows $\operatorname{index}F=0$ and that some regular value has an odd number of preimages, the [[Def - Mod-2 Degree of a Proper Fredholm Map|mod-2 degree]] is nonzero, and part (i) applied at *every* regular value then guarantees a nonempty finite solution set there; conversely, if $\operatorname{index}F<0$, part (i) shows every regular value has empty preimage, so the interesting values are all critical. The bridge is "index and a single count $\Rightarrow$ structure of the solution set at all regular values". *Example problem:* show that a Fredholm map of index $-1$ misses a residual set of values entirely.

**Targets (Output Amplification).** The bare conclusion is "the solution set is a manifold"; combined with further ingredients it becomes the central constructions of gauge theory.

Combine part (i) with **the Sard–Smale theorem**. Part (i) tells you the solution set is a manifold *at a regular value*; the [[Thm - Sard-Smale Theorem|Sard–Smale theorem]] tells you that regular values are residual, hence dense. Together they yield: after an arbitrarily small perturbation of the value (or, parametrically, of the equation), the solution set is a smooth manifold of dimension the index. This is the standard existence-of-a-good-representative argument for moduli spaces, and the extra ingredient is genericity.

Combine part (ii) with **an equivariant structure**. When a group acts and the value $y$ is forced to be fixed, one cannot perturb $y$; instead one intersects with a finite-dimensional submanifold $Z$ of admissible values and uses $F\pitchfork Z$. The payoff $E$ is a moduli space of dimension $\operatorname{index}F+\dim Z$, the form in which the dimension of the framed or parametrised Seiberg–Witten moduli space appears. The extra ingredient is the geometry of the admissible set $Z$.

Combine part (iii) with **compactness of the one-parameter family**. Part (iii) makes the universal solution set of a homotopy a $1$-manifold with boundary the two fibres; if the family is additionally proper, the $1$-manifold is compact, and [[Thm - Compact One-Manifolds have an Even Number of Boundary Points|a compact one-manifold has an even number of boundary points]]. The payoff is that the two fibre counts have the same parity — the well-definedness and homotopy invariance of the mod-2 degree. The extra ingredient is properness, which supplies compactness.

---

# Why Is It True

The engine is a normal form. Near any solution point $p\in F^{-1}(y)$, the [[Thm - Kuranishi Model for a Fredholm Map|Kuranishi model]] rewrites $F$, after a diffeomorphism $\phi$ of the source, as the *sum of an isomorphism and a finite-dimensional correction*: in the splittings $X=X_0\oplus X_1$, $Y=Y_0\oplus Y_1$ with $X_0=\ker d_pF$ and $Y_0=\operatorname{Im}d_pF$, one has $F(\phi(x_0,x_1))=Tx_1+f(x_0,x_1)$, where $T\colon X_1\to Y_0$ is a linear isomorphism and $f$ takes values in the finite-dimensional cokernel direction $Y_1$. Solving $F=y$ (that is, $=0$ after translating) splits into two pieces: the $Y_0$-component $Tx_1=0$ forces $x_1=0$ because $T$ is invertible, and the $Y_1$-component becomes a finite-dimensional equation $f_0(x_0)=0$ on the kernel $X_0$.

Regularity is exactly the statement that the finite-dimensional piece is vacuous. If $y$ is a regular value then $d_pF$ is surjective, so the cokernel direction $Y_1$ is $\{0\}$, the map $f$ is identically zero, and the equation $F(\phi(x_0,x_1))=0$ reduces to $x_1=0$ alone. What is left, $\{(x_0,0)\}$, is an open piece of the finite-dimensional space $X_0=\ker d_pF$, carried by the diffeomorphism $\phi$ onto a neighbourhood of $p$ in $F^{-1}(y)$. So near a regular solution the solution set *is* a copy of the kernel, and its dimension is $\dim\ker d_pF$, which equals the index precisely because the cokernel is zero.

> **The mechanism in one sentence: at a regular value the Kuranishi model of a Fredholm map has zero cokernel, so it is nothing but a submanifold chart, and the solution set is locally a copy of the (finite-dimensional) kernel — a manifold of dimension the index.**

Parts (ii) and (iii) do not need a new idea; they manufacture regularity. For (ii), a finite-dimensional submanifold $Z$ is locally the zero set of a submersion $\rho$ onto a Banach space; the composite $\rho\circ F$ is again Fredholm, and transversality of $F$ to $Z$ is exactly the condition that makes $0$ a regular value of $\rho\circ F$, so (i) applies to $\rho\circ F$ and the index bookkeeping produces the dimension $\operatorname{index}F+\dim Z$. For (iii), the solution set near a boundary point sits inside the (finite-dimensional) solution set of an *extended* map obtained by forgetting the boundary; the boundary-defining function, restricted to that finite-dimensional manifold, has $0$ as a regular value precisely because $y$ is regular for $F|_{\partial X}$ as well as for $F$, and a smooth function with a regular value at $0$ cuts its domain into a manifold with boundary. In every case the infinite dimensions are inert: they are the isomorphism $T$, which contributes nothing to the solution set, and all of the geometry happens in the finite-dimensional kernel.

---

# What Makes This Hard

The one genuinely infinite-dimensional subtlety is that "dimension counting" is illegal in $Y$: one cannot write $\dim F^{-1}(y)=\dim X-\dim Y$ or subtract $\dim\operatorname{Im}d_xF$ from $\dim Y$, because both are infinite. The correct replacements — the index and the finite cokernel — are what the Fredholm hypothesis buys, and every dimension statement must be routed through the *finite-dimensional* kernel and cokernel rather than through the ambient spaces. In part (ii) this shows up as the need to prove that the composite $\rho\circ F$ is Fredholm on a whole neighbourhood (not merely surjective at the one point), which requires knowing that composing a Fredholm operator with a surjective Fredholm operator keeps the range closed — a fact that is automatic once the cokernel is finite-dimensional but is false for general bounded operators. In part (iii) the trap is to assume that "regular value of $F$" alone gives a manifold with boundary; it does not, and one must separately require $y$ regular for $F|_{\partial X}$, the omission of which produces corners rather than a smooth boundary.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove (i) by invoking the Kuranishi model at a solution point and observing that regularity kills the cokernel direction, leaving a copy of the finite-dimensional kernel. Reduce (ii) to (i) by writing the submanifold $Z$ locally as the zero set of a submersion $\rho$ and applying (i) to $\rho\circ F$, with the transversality hypothesis converted into regularity and a linear-algebra dimension count. Reduce (iii) to (i) by extending $F$ across the boundary, applying (i) to get a finite-dimensional solution manifold $S$, and slicing $S$ by the boundary-defining function, whose regularity at $0$ follows from regularity of $F|_{\partial X}$.

**Subgoal decomposition:**

1. **Kernel of a surjective Fredholm operator is finite-dimensional of dimension the index; finite-dimensional subspaces split.**
   - *Hint:* If $A$ is surjective then $\operatorname{coker}A=0$, so $\operatorname{index}A=\dim\ker A$; a finite-dimensional subspace is closed, and a Hahn–Banach / basis argument produces a closed complement.
   - *Why needed:* It is what makes $F^{-1}(y)$ finite-dimensional in (i) and identifies its dimension with the index.

2. **A finite-dimensional embedded submanifold is locally the zero set of a submersion onto a Banach space, and that submersion is a Fredholm map of index $\dim Z$.**
   - *Hint:* Use the submanifold chart: split the model space of $Y$ as $T_zZ\oplus W$ with $W$ a closed complement, and take $\rho=$ projection onto $W$ in the chart.
   - *Why needed:* It is the device that turns "preimage of $Z$" into "level set of $\rho\circ F$", reducing (ii) to (i).

3. **Composition with a surjective Fredholm operator is Fredholm; a transversal linear-algebra dimension count.**
   - *Hint:* For $\rho\circ F$ near a solution, bound $\dim\ker$ and $\dim\operatorname{coker}$ by those of the factors and use that finite cokernel forces closed range; then compute $\dim(d_xF)^{-1}(T_zZ)=\operatorname{index}F+\dim Z$ by a quotient count.
   - *Why needed:* It supplies the Fredholm property of $\rho\circ F$ on a neighbourhood (so (i) applies) and the dimension in (ii).

4. **A smooth real function with a regular value at $0$ cuts a finite-dimensional manifold into a manifold with boundary.**
   - *Hint:* Near a zero the submersion normal form makes the function a coordinate; the superlevel set is then a coordinate half-space.
   - *Why needed:* It is the finite-dimensional slicing step that produces the boundary in (iii).

5. **Assemble (iii): extend $F$ across the boundary, apply (i), and slice by the boundary functional; the slice is regular because $F|_{\partial X}$ is regular.**
   - *Hint:* The extended map's fibre $S$ is a finite-dimensional manifold; $F^{-1}(y)$ near a boundary point is $\{s\in S:\lambda(s)\ge0\}$; show $\lambda|_S$ has $0$ as a regular value by comparing the kernels of $d_xF$ and $d_xF|_{\ker\lambda}$.
   - *Why needed:* It is the boundary version, and its homotopy specialisation is the cobordism corollary.

---

# Lemma Decomposition

> [!note]- Lemma 1: The kernel of a surjective Fredholm operator has dimension the index; finite-dimensional subspaces are closed and complemented
> **Statement:** Let $A\colon E\to G$ be a Fredholm operator between Banach spaces. (a) Every finite-dimensional subspace $V\subseteq E$ is closed and admits a closed complement. (b) If $A$ is surjective, then $\ker A$ is a finite-dimensional (hence closed and complemented) subspace of dimension $\dim\ker A=\operatorname{index}A$; in particular $\operatorname{index}A\ge 0$.
>
> **Hint:** For (a) pick a basis and dual functionals via Hahn–Banach. For (b), surjective means $\operatorname{coker}A=0$, so $\operatorname{index}A=\dim\ker A-0$.
>
> **Why needed:** It is the fact that makes $F^{-1}(y)$ finite-dimensional in part (i), gives its dimension as $\operatorname{index}F$, and supplies the splitting that the definition of an embedded submanifold requires.
>
> > [!note]- Full proof
> > **(a) Finite-dimensional subspaces are closed.** Let $V\subseteq E$ have basis $v_1,\dots,v_m$. A finite-dimensional normed space is complete (it is linearly homeomorphic to $\mathbb{R}^m$, and $\mathbb{R}^m$ is complete), and a complete subspace of a metric space is closed; hence $V$ is closed in $E$.
> >
> > **(a) Finite-dimensional subspaces are complemented.** For each $j$ let $\ell_j\colon V\to\mathbb{R}$ be the $j$-th coordinate functional relative to the basis, so $\ell_j(v_i)=\delta_{ij}$. Each $\ell_j$ is bounded on the finite-dimensional space $V$, so by the Hahn–Banach theorem it extends to a bounded functional $\tilde\ell_j\colon E\to\mathbb{R}$ (Hahn–Banach: a bounded functional on a subspace extends to the whole space with the same norm). Set $W:=\bigcap_{j=1}^m\ker\tilde\ell_j$, a closed subspace (an intersection of kernels of bounded functionals). Then $V\cap W=\{0\}$ (if $v=\sum a_iv_i\in W$ then $a_j=\tilde\ell_j(v)=0$ for all $j$), and every $x\in E$ decomposes as $x=\sum_j\tilde\ell_j(x)\,v_j + \big(x-\sum_j\tilde\ell_j(x)\,v_j\big)$ with the first summand in $V$ and, applying each $\tilde\ell_k$, the second in $W$. Hence $E=V\oplus W$ with $W$ closed, so $V$ is complemented.
> >
> > **(b) Dimension of the kernel.** Suppose $A$ is surjective, so $\operatorname{Im}A=G$ and $\operatorname{coker}A=G/\operatorname{Im}A=\{0\}$, whence $\dim\operatorname{coker}A=0$. By the definition of the index,
> > $$\operatorname{index}A=\dim\ker A-\dim\operatorname{coker}A=\dim\ker A-0=\dim\ker A,$$
> > which is finite because $A$ is Fredholm. Being finite-dimensional, $\ker A$ is closed and complemented by part (a). Since $\dim\ker A\ge 0$, also $\operatorname{index}A\ge 0$. $\qquad\blacksquare$

> [!note]- Lemma 2: A finite-dimensional embedded submanifold is locally the zero set of a Fredholm submersion of index $\dim Z$
> **Statement:** Let $Z\subseteq Y$ be a $d$-dimensional embedded submanifold of a Banach manifold $Y$ and $z\in Z$. Then there is an open neighbourhood $U$ of $z$ in $Y$, a Banach space $W$, and a smooth map $\rho\colon U\to W$ with $\rho(z)=0$, $Z\cap U=\rho^{-1}(0)$, such that at every $y'\in U$ the differential $d_{y'}\rho$ is surjective with $\ker d_{y'}\rho$ of dimension $d$; hence $\rho$ is a Fredholm map with $\operatorname{index}d_{y'}\rho=d$, and $\ker d_z\rho=T_zZ$.
>
> **Hint:** Take a submanifold chart $\psi\colon U\to E_Y$ sending $Z\cap U$ into a $d$-dimensional subspace $V_0$; write $E_Y=V_0\oplus W$ with $W$ closed and let $\rho=\operatorname{pr}_W\circ\psi$.
>
> **Why needed:** It converts "preimage of $Z$" into "level set of the single map $\rho\circ F$", the reduction on which part (ii) turns.
>
> > [!note]- Full proof
> > **Set up the submanifold chart.** By the definition of an embedded submanifold, there is a chart $\psi\colon U\to E_Y$ (a diffeomorphism onto an open subset of the model Banach space $E_Y$ of $Y$) with $\psi(z)=0$ such that $\psi(Z\cap U)=\psi(U)\cap V_0$, where $V_0\subseteq E_Y$ is a closed subspace admitting a closed complement. Because $Z$ has dimension $d$, the subspace $V_0$ is $d$-dimensional; being finite-dimensional it is closed and, by Lemma 1(a), complemented: fix a closed complement $W$, so $E_Y=V_0\oplus W$.
> >
> > **Define the submersion.** Let $\operatorname{pr}_W\colon E_Y\to W$ be the bounded linear projection onto $W$ along $V_0$ (bounded because the decomposition $E_Y=V_0\oplus W$ into closed subspaces makes the projections bounded, by the closed graph theorem). Set $\rho:=\operatorname{pr}_W\circ\psi\colon U\to W$. Then $\rho(z)=\operatorname{pr}_W(0)=0$, and for $y'\in U$,
> > $$\rho(y')=0\iff\operatorname{pr}_W(\psi(y'))=0\iff\psi(y')\in V_0\iff y'\in Z\cap U,$$
> > so $Z\cap U=\rho^{-1}(0)$ (using $\psi(y')\in\psi(U)\cap V_0\iff\psi(y')\in V_0$ since $\psi(y')\in\psi(U)$ always).
> >
> > **Differential.** By the chain rule $d_{y'}\rho=\operatorname{pr}_W\circ d_{y'}\psi$. Since $\psi$ is a diffeomorphism, $d_{y'}\psi\colon T_{y'}Y\to E_Y$ is a bounded linear isomorphism, and $\operatorname{pr}_W\colon E_Y\to W$ is bounded and surjective with kernel $V_0$. Therefore $d_{y'}\rho$ is surjective (composition of surjections), and
> > $$\ker d_{y'}\rho=(d_{y'}\psi)^{-1}(\ker\operatorname{pr}_W)=(d_{y'}\psi)^{-1}(V_0),$$
> > which is the image of the $d$-dimensional space $V_0$ under the isomorphism $(d_{y'}\psi)^{-1}$, hence $d$-dimensional. A surjective operator with $d$-dimensional kernel has closed range (its range is all of $W$) and zero cokernel, so it is Fredholm of index $d-0=d$. In particular at $y'=z$ we have $\ker d_z\rho=(d_z\psi)^{-1}(V_0)=T_zZ$, since $d_z\psi$ carries $T_zZ$ isomorphically onto $V_0$ (the tangent space of the submanifold maps to the tangent space of its image $V_0$ in the chart). Thus $\rho$ is a Fredholm map with the stated kernel dimensions. $\qquad\blacksquare$

> [!note]- Lemma 3: Composition with a surjective Fredholm operator is Fredholm; the transversal dimension count
> **Statement:** Let $A\colon E\to G$ and $B\colon G\to H$ be bounded operators between Banach spaces with $A$ Fredholm and $B$ Fredholm and surjective. Then: (a) $BA$ is Fredholm, with $\ker BA=A^{-1}(\ker B)$ and $\dim\operatorname{coker}BA\le\dim\operatorname{coker}A$. (b) If moreover $V\subseteq G$ is a finite-dimensional subspace with $\operatorname{Im}A+V=G$, then $A^{-1}(V)$ is finite-dimensional with $\dim A^{-1}(V)=\operatorname{index}A+\dim V$.
>
> **Hint:** For (a), bound $\dim\ker BA$ by $\dim\ker A+\dim\ker B$ and use that a finite-dimensional cokernel forces closed range. For (b), factor $A$ through $A^{-1}(V)$ and count via the quotient $G/\operatorname{Im}A$.
>
> **Why needed:** Part (a) makes $\rho\circ F$ a Fredholm map on a whole neighbourhood, so part (i) applies to it in (ii); part (b) is the transversal dimension formula.
>
> > [!note]- Full proof
> > **(a) $BA$ is Fredholm.** First, $\ker BA=\{x\in E:BAx=0\}=\{x:Ax\in\ker B\}=A^{-1}(\ker B)$. The restriction $A|\colon A^{-1}(\ker B)\to\ker B$ has kernel $\ker A$ and image contained in the finite-dimensional space $\ker B$, so by the rank–nullity relation for the linear map $A|$,
> > $$\dim A^{-1}(\ker B)\le\dim\ker A+\dim\ker B<\infty,$$
> > and $\ker BA$ is finite-dimensional. Next, $\operatorname{Im}BA=B(\operatorname{Im}A)$. Because $B$ is surjective, the induced linear map $\bar B\colon G/\operatorname{Im}A\to H/B(\operatorname{Im}A)$, $\bar B(g+\operatorname{Im}A):=B g + B(\operatorname{Im}A)$, is well defined and surjective, so
> > $$\dim\operatorname{coker}BA=\dim\big(H/B(\operatorname{Im}A)\big)\le\dim\big(G/\operatorname{Im}A\big)=\dim\operatorname{coker}A<\infty.$$
> > Thus $BA$ has finite-dimensional cokernel; by [[Thm - Closed Range is Automatic for Finite-Dimensional Cokernel|the theorem that a bounded operator with finite-dimensional cokernel has closed range]] — *if $S\colon E\to H$ is bounded and $H/\operatorname{Im}S$ is finite-dimensional, then $\operatorname{Im}S$ is closed* — the range of $BA$ is closed. Finite-dimensional kernel, closed range, and finite-dimensional cokernel are exactly the Fredholm conditions, so $BA$ is Fredholm.
> >
> > **(b) The dimension count.** Assume $V\subseteq G$ finite-dimensional with $\operatorname{Im}A+V=G$. The restriction $A|\colon A^{-1}(V)\to V\cap\operatorname{Im}A$ is surjective (given $w\in V\cap\operatorname{Im}A$, write $w=Ax$; then $x\in A^{-1}(V)$) with kernel $\ker A$, so by rank–nullity for $A|$,
> > $$\dim A^{-1}(V)=\dim\ker A+\dim\big(V\cap\operatorname{Im}A\big).\tag{3.1}$$
> > Let $q\colon G\to G/\operatorname{Im}A$ be the quotient map; $\dim(G/\operatorname{Im}A)=\dim\operatorname{coker}A=:c<\infty$. The hypothesis $\operatorname{Im}A+V=G$ says $q(V)=G/\operatorname{Im}A$, i.e. $q|_V$ is surjective; its kernel is $V\cap\operatorname{Im}A$, so by rank–nullity for $q|_V$,
> > $$\dim V=\dim\big(V\cap\operatorname{Im}A\big)+c,\quad\text{hence}\quad\dim\big(V\cap\operatorname{Im}A\big)=\dim V-c.\tag{3.2}$$
> > Substituting (3.2) into (3.1),
> > $$\dim A^{-1}(V)=\dim\ker A+\dim V-c=\big(\dim\ker A-c\big)+\dim V=\operatorname{index}A+\dim V,$$
> > using $\operatorname{index}A=\dim\ker A-\dim\operatorname{coker}A=\dim\ker A-c$. Both $\dim\ker A$ and $\dim V$ are finite, so $A^{-1}(V)$ is finite-dimensional. $\qquad\blacksquare$

> [!note]- Lemma 4: A regular value of a smooth real function cuts a finite-dimensional manifold into a manifold with boundary
> **Statement:** Let $S$ be a smooth finite-dimensional manifold (without boundary) of dimension $k\ge 1$, and $\pi\colon S\to\mathbb{R}$ a smooth function with $0$ a regular value (that is, $d_s\pi\ne 0$ for every $s\in\pi^{-1}(0)$). Then $S_{\ge 0}:=\{s\in S:\pi(s)\ge 0\}$ is a smooth $k$-manifold with boundary, and $\partial S_{\ge 0}=\pi^{-1}(0)$.
>
> **Hint:** Interior points ($\pi>0$) are already interior manifold points. At a boundary point, the submersion normal form makes $\pi$ a coordinate, and $S_{\ge0}$ becomes a coordinate half-space.
>
> **Why needed:** It is the finite-dimensional slicing step that produces the boundary in part (iii).
>
> > [!note]- Full proof
> > **Interior points.** The set $\{s:\pi(s)>0\}$ is open in $S$ (preimage of the open ray $(0,\infty)$ under continuous $\pi$), so each such point has a neighbourhood diffeomorphic to an open subset of $\mathbb{R}^k$; these are ordinary interior manifold charts, and they cover $S_{\ge0}\setminus\pi^{-1}(0)$.
> >
> > **Boundary points.** Let $s_0\in\pi^{-1}(0)$. Since $0$ is a regular value, $d_{s_0}\pi\colon T_{s_0}S\to\mathbb{R}$ is surjective, i.e. $\pi$ is a submersion at $s_0$. By the finite-dimensional [[Thm - The Implicit Function Theorem|implicit function theorem]] in its submersion form — *a smooth map that is a submersion at a point admits, in suitable coordinates centred there, the coordinate-projection normal form* — there is a chart $\theta\colon O\to\mathbb{R}^k$ on an open neighbourhood $O$ of $s_0$ in $S$, with $\theta(s_0)=0$, in which $\pi$ becomes the last coordinate:
> > $$\pi\circ\theta^{-1}(u_1,\dots,u_k)=u_k\qquad\text{for }(u_1,\dots,u_k)\in\theta(O).$$
> > In these coordinates,
> > $$\theta\big(S_{\ge0}\cap O\big)=\{(u_1,\dots,u_k)\in\theta(O):u_k\ge 0\}=\theta(O)\cap\mathbb{H}^k,$$
> > where $\mathbb{H}^k=\{u\in\mathbb{R}^k:u_k\ge 0\}$ is the standard half-space, and
> > $$\theta\big(\pi^{-1}(0)\cap O\big)=\{u\in\theta(O):u_k=0\}=\theta(O)\cap\partial\mathbb{H}^k.$$
> > Thus $\theta$ is a boundary chart for $S_{\ge0}$ near $s_0$ ([[Def - Smooth Manifold with Boundary|manifold-with-boundary chart]]), identifying $S_{\ge0}\cap O$ with a relatively open subset of $\mathbb{H}^k$ and $\pi^{-1}(0)\cap O$ with its boundary face. Transition maps between two such charts are smooth (they are transition maps of $S$ restricted to half-spaces, and preserve $\{u_k\ge0\}$ because they preserve the sign of $\pi$).
> >
> > **Conclusion.** The interior charts and the boundary charts together form a smooth atlas with boundary on $S_{\ge0}$; a point is a boundary point exactly when its $u_k$-coordinate is $0$, i.e. exactly when $\pi=0$. Hence $S_{\ge0}$ is a smooth $k$-manifold with boundary and $\partial S_{\ge0}=\pi^{-1}(0)$. $\qquad\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $F\colon X\to Y$ be a smooth Fredholm map between Banach manifolds. We prove the three parts in turn; parts (ii) and (iii) reduce to (i). All three statements are local on $X$, so it suffices to work in a chart around a chosen point of the relevant preimage and produce there a submanifold (or manifold-with-boundary) chart; the local charts assemble into a global smooth structure because on overlaps they are restrictions of charts of $X$.
>
> ---
> **Part (i): the regular value theorem.**
>
> **Step 0 — reduce to Banach spaces and to the value $0$.** Fix $x\in F^{-1}(y)$. Choose charts carrying a neighbourhood of $x$ to an open set in a Banach space $X$ (we reuse the letter) and a neighbourhood of $y$ to an open set in a Banach space $Y$, with $x\mapsto 0$ and $y\mapsto 0$. In these charts $F$ is a smooth Fredholm map with $F(0)=0$, and $0$ is a regular value (regularity is a statement about the differential, invariant under charts). It remains to show $F^{-1}(0)$ is, near $0$, a copy of $\ker d_0F$ of dimension $\operatorname{index}F$ with tangent space $\ker d_0F$.
>
> **Step 1 — invoke the Kuranishi model.** Apply the [[Thm - Kuranishi Model for a Fredholm Map|Kuranishi model]] to $F$ at $p=0$. Restated: *with $L:=d_0F$, $X_0:=\ker L$, $Y_0:=\operatorname{Im}L$, and closed complements $X=X_0\oplus X_1$, $Y=Y_0\oplus Y_1$ (with $\dim X_0<\infty$, $\dim Y_1<\infty$), the restriction $T:=L|_{X_1}\colon X_1\to Y_0$ is a bounded linear isomorphism, and there is a diffeomorphism $\phi$ from a neighbourhood $V$ of $0$ in $X$ onto a neighbourhood of $0$ with $\phi(0)=0$, together with a smooth $f\colon V\to Y_1$ with $f(0)=0$ and $d_0f=0$, such that $F(\phi(x_0,x_1))=Tx_1+f(x_0,x_1)$ for $(x_0,x_1)\in V$.* Such closed complements exist: $X_0=\ker L$ is finite-dimensional, hence complemented by Lemma 1(a), and $Y_1$ may be taken as a complement of the closed finite-codimension subspace $Y_0=\operatorname{Im}L$.
>
> **Step 2 — regularity kills the cokernel direction.** Because $0$ is a regular value, $L=d_0F$ is surjective, so $Y_0=\operatorname{Im}L=Y$ and therefore $Y_1=\{0\}$. Then $f\colon V\to Y_1=\{0\}$ is the zero map, and the Kuranishi identity becomes
> $$F\big(\phi(x_0,x_1)\big)=Tx_1\qquad\text{for }(x_0,x_1)\in V.\tag{$\ast$}$$
> Since $T\colon X_1\to Y_0=Y$ is an isomorphism, $Tx_1=0$ if and only if $x_1=0$. Hence, for $(x_0,x_1)\in V$,
> $$\phi(x_0,x_1)\in F^{-1}(0)\iff F(\phi(x_0,x_1))=0\iff Tx_1=0\iff x_1=0.$$
> Therefore $\phi$ carries $\big(X_0\times\{0\}\big)\cap V$ bijectively onto $F^{-1}(0)\cap\phi(V)$ (by $(\ast)$ and the displayed equivalence), and since $\phi$ is a diffeomorphism this exhibits $F^{-1}(0)$ near $0$ as the image, under the diffeomorphism $\phi$, of a relatively open subset of the closed subspace $X_0\times\{0\}$.
>
> **Step 3 — this is a submanifold chart.** The subspace $X_0=\ker d_0F$ is finite-dimensional (Lemma 1(b)), hence closed and complemented in $X$ (complement $X_1$). Thus $\phi^{-1}$ is a chart of $X$ near $x$ in which $F^{-1}(0)$ is exactly the intersection with the closed complemented subspace $X_0\times\{0\}$. By the definition of an embedded submanifold, $F^{-1}(0)$ is a smooth embedded submanifold near $x$, modelled on $X_0$, of dimension $\dim X_0=\dim\ker d_0F$. By Lemma 1(b), $\dim\ker d_0F=\operatorname{index}d_0F$; since the index is constant on the connected component of $x$, this equals $\operatorname{index}F$ on that component. If $\operatorname{index}F<0$ on some component, then no $x$ there can have $d_xF$ surjective (that would force $\dim\ker d_xF=\operatorname{index}F<0$, impossible), so $F^{-1}(y)$ is empty on that component, vacuously a manifold.
>
> **Step 4 — the tangent space.** Differentiate $(\ast)$ at $0$: writing $d_0\phi\colon X\to T_xX$ for the (invertible) differential of the chart map,
> $$d_0F\circ d_0\phi\,(v_0,v_1)=T v_1\qquad(v_0,v_1)\in X_0\oplus X_1,$$
> by the chain rule applied to $F\circ\phi=(x_0,x_1)\mapsto Tx_1$. Restricting to $v_1=0$ gives $d_0F\big(d_0\phi(v_0,0)\big)=0$, so $d_0\phi(X_0\times\{0\})\subseteq\ker d_0F$. As $d_0\phi$ is an isomorphism, $\dim d_0\phi(X_0\times\{0\})=\dim X_0=\dim\ker d_0F$, and a subspace of $\ker d_0F$ of the same finite dimension equals it: $d_0\phi(X_0\times\{0\})=\ker d_0F$. Finally $T_xF^{-1}(0)=d_0\phi\big(T_0(X_0\times\{0\})\big)=d_0\phi(X_0\times\{0\})=\ker d_0F$, since the tangent space of the flat submanifold $X_0\times\{0\}$ at $0$ is $X_0\times\{0\}$ and $\phi$ is a diffeomorphism carrying it to $F^{-1}(0)$. Translating back, $T_xF^{-1}(y)=\ker d_xF$. This proves (i).
>
> *(Alternatively, part (i) is the special case of [[Thm - Inverse Function Theorem on Banach Spaces|the regular-value part of the Banach inverse function theorem]] — $y$ regular and $\ker d_xF$ complemented, which holds automatically since $\ker d_xF$ is finite-dimensional — with the dimension read off from Lemma 1(b). We have given the Kuranishi argument to keep the mechanism visible.)*
>
> ---
> **Part (ii): the transversality theorem.**
>
> Fix $x\in F^{-1}(Z)$ and put $z:=F(x)\in Z$; write $d:=\dim Z$. The claim is local near $x$.
>
> **Step 0 — a local defining submersion for $Z$.** By Lemma 2 there are an open neighbourhood $U$ of $z$ in $Y$, a Banach space $W$, and a smooth map $\rho\colon U\to W$ with $\rho(z)=0$, $Z\cap U=\rho^{-1}(0)$, such that $d_{y'}\rho$ is surjective with $d$-dimensional kernel for every $y'\in U$, and $\ker d_z\rho=T_zZ$. Set $g:=\rho\circ F\colon F^{-1}(U)\to W$; then, on $F^{-1}(U)$,
> $$g^{-1}(0)=\{x'\in F^{-1}(U):\rho(F(x'))=0\}=\{x'\in F^{-1}(U):F(x')\in Z\}=F^{-1}(Z)\cap F^{-1}(U).$$
> So near $x$, $F^{-1}(Z)$ is the zero set of the single map $g$.
>
> **Step 1 — $g$ is a Fredholm map near $x$.** For $x'\in F^{-1}(U)$, the chain rule gives $d_{x'}g=d_{F(x')}\rho\circ d_{x'}F$. Here $d_{x'}F$ is Fredholm (as $F$ is a Fredholm map) and $d_{F(x')}\rho$ is a surjective Fredholm operator (Lemma 2). By Lemma 3(a), the composite $d_{x'}g$ is a Fredholm operator. Hence $g$ is a Fredholm map on the open set $F^{-1}(U)$.
>
> **Step 2 — transversality makes $0$ a regular value of $g$.** We show $d_{x}g$ is surjective at every $x\in g^{-1}(0)=F^{-1}(Z)\cap F^{-1}(U)$; fix such an $x$ and $z=F(x)$. The transversality hypothesis $F\pitchfork Z$ reads $\operatorname{Im}d_xF+T_zZ=T_zY$. Apply the surjective operator $d_z\rho$ to this identity of subspaces of $T_zY=T_{F(x)}Y\subseteq$ (chart of) $U$:
> $$d_z\rho\big(\operatorname{Im}d_xF\big)+d_z\rho\big(T_zZ\big)=d_z\rho\big(T_zY\big)=W,$$
> using that $d_z\rho$ is onto $W$. But $d_z\rho(T_zZ)=d_z\rho(\ker d_z\rho)=\{0\}$ (Lemma 2 gives $\ker d_z\rho=T_zZ$). Therefore $d_z\rho(\operatorname{Im}d_xF)=W$, i.e.
> $$\operatorname{Im}(d_xg)=\operatorname{Im}(d_z\rho\circ d_xF)=d_z\rho(\operatorname{Im}d_xF)=W,$$
> so $d_xg$ is surjective. Hence $0$ is a regular value of $g$.
>
> **Step 3 — apply part (i) to $g$.** By part (i), $g^{-1}(0)=F^{-1}(Z)\cap F^{-1}(U)$ is a smooth embedded submanifold with, at each $x$,
> $$T_xF^{-1}(Z)=\ker d_xg=\ker\big(d_z\rho\circ d_xF\big)=(d_xF)^{-1}\big(\ker d_z\rho\big)=(d_xF)^{-1}\big(T_zZ\big),$$
> the third equality because $d_xg\,v=0\iff d_z\rho(d_xF v)=0\iff d_xF v\in\ker d_z\rho$. This is the asserted tangent space.
>
> **Step 4 — the dimension.** Its dimension is $\operatorname{index}g$ (part (i)); we compute it directly with Lemma 3(b), taking $A=d_xF$ (Fredholm, index $\operatorname{index}F$) and $V=T_zZ$ (finite-dimensional, $\dim V=d$). The transversality identity $\operatorname{Im}d_xF+T_zZ=T_zY$ is exactly the hypothesis $\operatorname{Im}A+V=G$ of Lemma 3(b) (with $G=T_zY$), so
> $$\dim T_xF^{-1}(Z)=\dim(d_xF)^{-1}(T_zZ)=\operatorname{index}d_xF+\dim Z=\operatorname{index}F+\dim Z$$
> on the component of $x$. This proves (ii).
>
> ---
> **Part (iii): the boundary version.**
>
> Now $X$ is a Banach manifold with boundary and $y$ is a regular value of $F$ and of $F|_{\partial X}$. Fix $x\in F^{-1}(y)$; the claim is local near $x$.
>
> **Case A — $x$ is an interior point.** A neighbourhood of $x$ in $X$ is an ordinary Banach manifold (no boundary), so part (i) applies verbatim: $F^{-1}(y)$ is, near $x$, a smooth embedded submanifold of dimension $\operatorname{index}F$, with no boundary points there. These charts cover $F^{-1}(y)\setminus\partial X$.
>
> **Case B — $x$ is a boundary point.** Work in a boundary chart carrying a neighbourhood of $x$ to an open subset $\Omega$ of a half-space $\mathbb{H}_\lambda=\{u\in E:\lambda(u)\ge 0\}$ of the Banach model space $E$, with $x\mapsto 0$ and $\lambda\colon E\to\mathbb{R}$ a nonzero bounded functional, so that $\partial X$ corresponds to $\{\lambda=0\}=\ker\lambda$; also carry a neighbourhood of $y$ to an open set in a Banach space $Y$ with $y\mapsto 0$. Recall that the tangent space $T_xX$ at the boundary point is the full space $E$, and $T_x\partial X=\ker\lambda$.
>
> **Step 0 — extend $F$ across the boundary.** By definition of a smooth map on a manifold with boundary, $F$ extends to a smooth map $\tilde F$ on an open neighbourhood $O$ of $0$ in the full space $E$ (with $\tilde F=F$ on $O\cap\mathbb{H}_\lambda$). Since $d_0\tilde F=d_0F\colon E\to Y$ is the same bounded operator, $\tilde F$ is Fredholm near $0$ (the Fredholm property is open: [[Thm - Stability of the Fredholm Property under Small and Compact Perturbations|small perturbations of a Fredholm operator are Fredholm]], and $x'\mapsto d_{x'}\tilde F$ is continuous), and $d_0\tilde F=d_0F$ is surjective because $y$ is a regular value of $F$. Shrinking $O$, $0$ is a regular value of $\tilde F$ there.
>
> **Step 1 — the extended fibre is a finite-dimensional manifold.** By part (i) applied to $\tilde F$ on the boundaryless open set $O$, the set $S:=\tilde F^{-1}(0)$ is, near $0$, a smooth embedded submanifold of $O$ of dimension $\operatorname{index}d_0F=\operatorname{index}F$, with $T_0 S=\ker d_0F$; in particular $S$ is a *finite-dimensional* manifold (Lemma 1(b): $\dim\ker d_0F=\operatorname{index}F<\infty$). Near $x=0$,
> $$F^{-1}(y)=\tilde F^{-1}(0)\cap\mathbb{H}_\lambda=\{s\in S:\lambda(s)\ge 0\},$$
> because on $\mathbb{H}_\lambda$ the maps $F$ and $\tilde F$ agree.
>
> **Step 2 — the boundary functional restricts to a submersion on $S$.** Let $\pi:=\lambda|_S\colon S\to\mathbb{R}$, a smooth function on the finite-dimensional manifold $S$. Since $\lambda$ is linear and bounded, $d_s\pi=\lambda|_{T_sS}$ for each $s\in S$. We claim $0$ is a regular value of $\pi$. Let $s\in S$ with $\pi(s)=0$, i.e. $s\in S\cap\ker\lambda=S\cap\partial X$, so $s\in(F|_{\partial X})^{-1}(y)$. Suppose, for contradiction, that $\pi$ is critical at $s$: then $d_s\pi=\lambda|_{T_sS}=0$, i.e.
> $$\ker d_sF=T_sS\subseteq\ker\lambda=T_s\partial X.\tag{iii.1}$$
> Now bring in regularity on the boundary. Both of the following operators are surjective onto $T_yY$: the full differential $d_sF\colon T_sX=E\to T_yY$ (regularity of $F$), and its restriction $d_s(F|_{\partial X})=d_sF|_{\ker\lambda}\colon\ker\lambda\to T_yY$ (regularity of $F|_{\partial X}$). The full map $d_sF$ induces an isomorphism $\overline{d_sF}\colon E/\ker d_sF\to T_yY$ (surjective with kernel $\ker d_sF$). By (iii.1) $\ker d_sF\subseteq\ker\lambda$, so the subspace $\ker\lambda/\ker d_sF\subseteq E/\ker d_sF$ is defined, and $\overline{d_sF}$ restricted to it is $\overline{d_sF|_{\ker\lambda}}$, which is *also* surjective onto $T_yY$ (regularity of $F|_{\partial X}$). Since $\overline{d_sF}$ is injective, its restriction to $\ker\lambda/\ker d_sF$ is injective; being surjective onto $T_yY=\overline{d_sF}(E/\ker d_sF)$ and injective, and mapping the subspace $\ker\lambda/\ker d_sF$ onto the same image as the whole of $E/\ker d_sF$, injectivity of $\overline{d_sF}$ forces
> $$\ker\lambda/\ker d_sF=E/\ker d_sF,\quad\text{hence}\quad\ker\lambda=E.$$
> But $\lambda\ne 0$, so $\ker\lambda\ne E$ — a contradiction. The contradiction is between "$\lambda$ is a nonzero functional" and the consequence "$\ker\lambda=E$" forced by assuming $\pi$ critical at $s$. Therefore $\pi$ is not critical at $s$, i.e. $d_s\pi\ne 0$; as $s\in\pi^{-1}(0)$ was arbitrary, $0$ is a regular value of $\pi$.
>
> **Step 3 — slice.** By Lemma 4 applied to the finite-dimensional manifold $S$ and $\pi=\lambda|_S$ with regular value $0$, the set $\{s\in S:\lambda(s)\ge 0\}=F^{-1}(y)$ is, near $x$, a smooth manifold with boundary of dimension $\dim S=\operatorname{index}F$, with boundary
> $$\pi^{-1}(0)=S\cap\{\lambda=0\}=F^{-1}(y)\cap\partial X=(F|_{\partial X})^{-1}(y).$$
> Assembling Case A (interior charts, no boundary) and Case B (boundary charts) over all of $F^{-1}(y)$ gives a smooth manifold-with-boundary structure with $\partial(F^{-1}(y))=F^{-1}(y)\cap\partial X$, of dimension $\operatorname{index}F$ on each component. This proves (iii).
>
> ---
> **The cobordism corollary.**
>
> Let $H\colon X\times[0,1]\to Y$ be a smooth Fredholm homotopy with $H(\cdot,0)=F_0$, $H(\cdot,1)=F_1$, and $y$ a regular value of $H$, $F_0$, $F_1$. The product $X\times[0,1]$ is a Banach manifold with boundary
> $$\partial\big(X\times[0,1]\big)=\big(X\times\{0\}\big)\sqcup\big(X\times\{1\}\big),$$
> modelled on half-spaces (the $[0,1]$-factor supplies the half-space direction, with $\lambda(v,t)=t$ near $t=0$ and $\lambda(v,t)=1-t$ near $t=1$). The restriction of $H$ to this boundary is $H|_{X\times\{0\}}=F_0$ and $H|_{X\times\{1\}}=F_1$, so "$y$ regular for $H|_{\partial}$" is precisely "$y$ regular for $F_0$ and for $F_1$", which holds by hypothesis. The map $H$ is Fredholm by assumption; its index at $(x,t)$ is $\operatorname{index}F+1$, because $T_{(x,t)}(X\times[0,1])=T_xX\oplus\mathbb{R}$ and enlarging the domain of the Fredholm operator $d_xH_t$ by the finite-dimensional line $\mathbb{R}$ raises the dimension of the kernel by at most $1$ and leaves the cokernel unchanged up to a finite adjustment, so that the index rises by exactly $1$ (concretely, $d_{(x,t)}H=(d_xH_t,\partial_tH)$ has kernel and cokernel differing from those of $d_xH_t$ by the single extra domain dimension, giving $\operatorname{index}=\operatorname{index}d_xH_t+1$). Applying part (iii) to $H$ on $X\times[0,1]$,
> $$\partial\big(H^{-1}(y)\big)=H^{-1}(y)\cap\partial\big(X\times[0,1]\big)=\big(F_0^{-1}(y)\times\{0\}\big)\sqcup\big(F_1^{-1}(y)\times\{1\}\big),$$
> and $H^{-1}(y)$ is a smooth manifold with boundary of dimension $\operatorname{index}F+1$ on each component. In particular, when $\operatorname{index}F=0$, $H^{-1}(y)$ is a $1$-manifold with boundary the two $0$-dimensional fibres. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Recovering the finite-dimensional regular value theorem, with the index made explicit.** Let $f\colon M^m\to N^n$ be a smooth map between finite-dimensional manifolds and $y$ a regular value. Every linear map between finite-dimensional spaces is Fredholm, with $\operatorname{index}d_xf=\dim\ker d_xf-\dim\operatorname{coker}d_xf=m-n$ independent of $x$; part (i) then says $f^{-1}(y)$ is a manifold of dimension $m-n$, the classical statement. This is a good first exercise because it forces one to see the finite-dimensional theorem as a Fredholm statement and to check that the index computation reproduces the familiar dimension count; the non-obvious point is that "index" and "$\dim M-\dim N$" coincide only after the cokernel is accounted for.

**The unitary group as a Fredholm level set.** On the (finite-dimensional) space of complex $n\times n$ matrices, the map $A\mapsto A^*A$ lands in Hermitian matrices, and $I$ is a regular value on the relevant domain; its preimage is the unitary group $U(n)$. Verifying transversality here is a concrete rehearsal of the surjectivity computation in part (i), and computing the index gives $\dim U(n)=n^2$. The exercise is instructive because the target is a *linear subspace* (Hermitian matrices) sitting inside all matrices, so it also previews the "value constrained to a submanifold" theme of part (ii).

**A semilinear elliptic equation and part (ii) with a constraint surface.** Take $F\colon H_{k+2}(M)\to H_k(M)$, $F(u)=\Delta u+u^3$, on a closed surface, a Fredholm map of index $0$, and let $Z\subseteq H_k(M)$ be a finite-dimensional submanifold of admissible right-hand sides (for instance the span of finitely many fixed functions, translated). Show that transversality $F\pitchfork Z$ makes $F^{-1}(Z)$ a finite-dimensional manifold of dimension $\dim Z$, and interpret this as the family of solutions whose right-hand side is allowed to range over $Z$. This is non-obvious because the ambient space is infinite-dimensional and the naive "codimension of $Z$" is infinite; the finite answer comes entirely from the index and $\dim Z$, exactly as Lemma 3(b) dictates.

---

# Bridges

- **The Sard–Smale theorem** — the genericity partner. Part (i) gives structure *at* a regular value; the Sard–Smale theorem gives that regular values are residual, hence dense, so a generic small perturbation of the value (or of the equation) puts one in the regular case. Concretely, one applies Sard–Smale to produce a regular value $y'$ near a given $y$, then part (i) at $y'$; this is the two-step template behind every "the moduli space is a smooth manifold after a generic perturbation" statement. See [[Thm - Sard-Smale Theorem|Sard–Smale theorem]].

- **The mod-2 degree** — built on part (iii). For a proper Fredholm map of index $0$, a regular value has a compact $0$-dimensional preimage (finite set) by part (i) and properness. The count modulo $2$ is independent of the regular value and homotopy-invariant precisely because part (iii) turns a homotopy into a compact $1$-manifold whose boundary is the two fibres, and a compact $1$-manifold has an even number of boundary points. The construction is carried out on [[Def - Mod-2 Degree of a Proper Fredholm Map|the mod-2 degree page]].

- **Parametric transversality** — part (ii) with the target enlarged to a family. When the value is fixed by a symmetry and cannot be perturbed, one instead perturbs the map through a parameter $w$ in a Banach manifold $W$ and studies the universal solution set $\mathcal{Z}=\mathcal{F}^{-1}(y)$, cut out by part (i) applied to the total map. The projection $\mathcal{Z}\to W$ is then a Fredholm map to which Sard–Smale applies, so a generic parameter has $y$ regular for the corresponding slice. This is the exact device that makes the Seiberg–Witten moduli space generically smooth; see [[Thm - Parametric Transversality|parametric transversality]].

- **The Kuranishi model at a non-regular point** — the same normal form, without the simplification. When $y$ is *not* regular, the cokernel direction $Y_1$ is nonzero and the local structure of $F^{-1}(y)$ is governed by the finite-dimensional equation $f_0=0$ rather than by a linear space; this is the obstruction theory that describes moduli spaces near reducible or singular solutions. Parts (i)–(iii) are precisely the corner of that theory where the obstruction vanishes. See [[Thm - Kuranishi Model for a Fredholm Map|Kuranishi model]].

---

# Unlocked by This

> [!tip] Generic smoothness of moduli spaces *(from Gauge Theory)*
> Combined with Sard–Smale and an elliptic Fredholm setup, part (i) is the statement that, after a generic perturbation, the space of solutions of a gauge-theoretic equation modulo symmetry is a finite-dimensional smooth manifold whose dimension is the index of the linearised operator. This is the structural input to both **Donaldson theory** and **Seiberg–Witten theory**.

> [!tip] Cobordism invariance of counts *(from Differential Topology)*
> The boundary version (iii) and its homotopy corollary are the abstract form of the principle that a signed or unsigned count of solutions is a cobordism invariant: two regular values, or two ends of a generic family, are joined by a compact $1$-manifold, and the boundary of a compact $1$-manifold is even. This underlies the well-definedness of both the mod-2 and the integer degree.
