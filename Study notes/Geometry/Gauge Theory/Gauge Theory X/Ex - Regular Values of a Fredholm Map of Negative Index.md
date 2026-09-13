---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Sard-Smale Theorem"
  - "Thm - Regular Value and Transversality Theorems for Fredholm Maps"
  - "Def - Fredholm Map and Its Index"
  - "Def - Regular Value and Transversality for Fredholm Maps"
  - "Thm - Elliptic Operators on Closed Manifolds are Fredholm"
  - "Thm - Stability of the Fredholm Property under Small and Compact Perturbations"
tags: [geometry, gauge-theory]
---

# Problem Statement

The index of a Fredholm map is the *expected dimension* of a generic fibre: when $y$ is a regular value, $F^{-1}(y)$ is a smooth manifold of dimension $\operatorname{index}F$. A dimension cannot be negative, so a negative index is a signal that the generic fibre is empty — that the equation $F(x)=y$ has no solution for the overwhelming majority of right-hand sides $y$. This is the mechanism behind "the moduli space has negative expected dimension, hence is generically empty", which is used throughout gauge theory to switch off obstructions. This exercise makes the statement precise and proves it, then reads it in two concrete situations.

Let $F\colon X\to Y$ be a smooth Fredholm map between second countable Banach manifolds with
$$\operatorname{index}F<0.$$
Prove the following.

1. **(Regular values are exactly the non-values.)** A point $y\in Y$ is a regular value of $F$ if and only if $y\notin\operatorname{Im}F$. Equivalently, every point of the image is a critical value, and every regular value has empty preimage.

2. **(A residual set avoids the image.)** The set $Y\setminus\operatorname{Im}F$ is residual in $Y$, and therefore dense. Thus for a generic $y\in Y$ the equation $F(x)=y$ has no solution.

3. **(Two instances.)** Apply this to (a) a smooth map $F\colon\mathbb{R}\to\mathbb{R}^{2}$, and (b) a linear elliptic operator $L$ of negative index on a closed manifold perturbed by a smooth lower-order nonlinearity $N$, $F=L+N$.

**Recall:**

The objects in play are Fredholm maps and their index, regular and critical values, the regular-value theorem for Fredholm maps, the Sard–Smale theorem, and — for the applications — the Fredholm property of elliptic operators and the stability of the index under compact perturbation.

![[Def - Fredholm Map and Its Index#The Definition]]

A smooth map $F\colon X\to Y$ between Banach manifolds is a [[Def - Fredholm Map and Its Index|Fredholm map]] if its differential $d_xF\colon T_xX\to T_{F(x)}Y$ is a Fredholm linear operator at every $x$; the integer $\operatorname{index}d_xF=\dim\ker d_xF-\dim\operatorname{coker}d_xF$ is locally constant in $x$, hence constant on each component, and its value is denoted $\operatorname{index}F$.

![[Def - Regular Value and Transversality for Fredholm Maps#The Definition]]

A point $y\in Y$ is a [[Def - Regular Value and Transversality for Fredholm Maps|regular value]] of $F$ if $d_xF$ is **surjective** for every $x\in F^{-1}(y)$; otherwise $y$ is a **critical value**. When $F^{-1}(y)=\varnothing$ the condition holds vacuously, so every point outside the image is a regular value.

![[Thm - Regular Value and Transversality Theorems for Fredholm Maps#Statement]]

We use part (i) of the [[Thm - Regular Value and Transversality Theorems for Fredholm Maps|regular-value theorem for Fredholm maps]]: if $y$ is a regular value of the smooth Fredholm map $F$, then $F^{-1}(y)$ is a smooth embedded submanifold of $X$ of dimension $\operatorname{index}F$ (on each component), with tangent space $T_xF^{-1}(y)=\ker d_xF$.

![[Thm - Sard-Smale Theorem#Statement]]

The [[Thm - Sard-Smale Theorem|Sard–Smale theorem]] states that the set of regular values of a smooth Fredholm map between second countable Banach manifolds is residual in the target, in particular dense. (A set is **residual** if it contains a countable intersection of open dense sets; in a Banach manifold, which is a Baire space, a residual set is dense.)

For the second application we also recall two results from the elliptic theory. A linear [[Def - Elliptic Differential Operator and Principal Symbol|elliptic]] operator on a closed manifold, extended to the Sobolev completions, is Fredholm ([[Thm - Elliptic Operators on Closed Manifolds are Fredholm|elliptic Fredholm theorem]]); and if $T$ is a Fredholm operator and $K$ is compact then $T+K$ is Fredholm with $\operatorname{index}(T+K)=\operatorname{index}T$ ([[Thm - Stability of the Fredholm Property under Small and Compact Perturbations|stability of the index]]).

---

# Convergent Strategy

**Problem class.** This is a *dimension-obstruction* problem: a topological/analytic conclusion (the equation is generically unsolvable) is forced by an integer invariant (the index) being on the wrong side of zero. The pattern is "an object whose dimension must be $\geq0$ is asserted to have dimension $<0$, therefore it is empty". Parts 1 and 2 separate the argument into a pointwise linear-algebra fact and a global genericity fact.

**Assumption pattern.** The hypothesis $\operatorname{index}F<0$ is used exactly once, at the level of the differential: a Fredholm operator with negative index cannot be surjective, because surjectivity would kill the cokernel and leave $\dim\ker=\operatorname{index}<0$. Everything else is structural. The recognisable trigger is any statement of the form "for generic data the solution set is a manifold of dimension $d$" together with "$d<0$": the correct reading is never "a negative-dimensional manifold" but "no solutions".

**Theorem routing.** The route is short and rigid. First, pointwise: $\operatorname{index}d_xF<0$ forces $d_xF$ non-surjective at *every* $x$ (rank–nullity for Fredholm operators). Second, unwind the definition of regular value: since no differential is surjective, a point with nonempty preimage cannot be regular, and a point with empty preimage is vacuously regular; hence $\{\text{regular values}\}=Y\setminus\operatorname{Im}F$ *as sets*. Third, quote [[Thm - Sard-Smale Theorem|Sard–Smale]]: the left-hand side is residual, so the right-hand side is residual and dense. The [[Thm - Regular Value and Transversality Theorems for Fredholm Maps|regular-value theorem]] enters only as an independent geometric confirmation ("dimension $=\operatorname{index}F<0$, so the fibre is empty").

**Key decision point.** The one place a reader can go wrong is to invoke Sard–Smale *first* and then try to argue about preimages of regular values, which needs the pointwise non-surjectivity anyway. The efficient order is the reverse: settle the pointwise linear algebra, deduce the *set identity* {regular values} $=Y\setminus\operatorname{Im}F$, and only then apply Sard–Smale to transport "residual" across the identity. Recognising that the equality of these two sets is what makes the problem trivial once stated is the whole insight.

---

# Legal Operations Used

This solution deploys the following operations, referenced descriptively (the numbering on [[Gauge Theory X — Fredholm Maps, Transversality, and Degree#Legal Operations|the topic page's Legal Operations]] will be reconciled by the orchestrator).

1. **Read the index as a signed dimension count of the differential.** Use $\operatorname{index}d_xF=\dim\ker d_xF-\dim\operatorname{coker}d_xF$ pointwise, and that this equals $\operatorname{index}F$ on a connected component.

2. **Turn a sign of the index into a rank obstruction.** From $\operatorname{index}d_xF<0$ conclude $d_xF$ is not surjective, since surjectivity gives $\dim\operatorname{coker}d_xF=0$ and then $\dim\ker d_xF=\operatorname{index}d_xF<0$, impossible.

3. **Unwind the definition of regular value both ways.** A point with a preimage point of non-surjective differential is critical; a point with empty preimage is vacuously regular.

4. **Transport a topological largeness property across a set identity.** Once {regular values} $=Y\setminus\operatorname{Im}F$, apply Sard–Smale to conclude the right-hand side is residual and dense.

5. **Certify Fredholmness and compute the index of a perturbed operator** using the elliptic Fredholm theorem and the stability of the index under compact perturbation.

---

# Hints

> [!note]- Hint 1
> Forget the target for a moment and look at a single differential $d_xF$. It is a Fredholm operator of index $\operatorname{index}F<0$. Can such an operator be surjective? Write out what surjectivity does to the cokernel and to the index formula.

> [!note]- Hint 2
> A regular value is a point at which the differential is surjective *at every preimage point*. You have just shown no differential is surjective anywhere. So which points can possibly be regular values — those with a preimage, or those without?

> [!note]- Hint 3
> Prove the set equality {regular values of $F$} $=Y\setminus\operatorname{Im}F$ carefully, checking both inclusions and the vacuous case for points outside the image. Then you have not yet used Sard–Smale at all.

> [!note]- Hint 4
> Now apply Sard–Smale. It says the left-hand side is residual. Push residual across the equality. For the density conclusion, recall that a residual subset of a Banach manifold is dense.

> [!note]- Hint 5
> For 3(a), what is the index of a linear map $\mathbb{R}\to\mathbb{R}^{2}$? For 3(b), the map is $u\mapsto Lu+N(u)$; its differential is $L+d_uN$. If $d_uN$ is compact, what does the stability theorem say about the index of $L+d_uN$?

---

# Solution

The proof factors into a pointwise linear-algebra observation and a one-line global consequence. First we show that negative index makes the differential non-surjective everywhere, which by the definition of "regular value" forces the set of regular values to coincide *exactly* with the complement of the image. Then Sard–Smale, applied to $F$, says this set is residual, and residual sets in a Banach manifold are dense. The applications are index computations that put a concrete map into the hypothesis.

**Step 1: The differential is nowhere surjective.**

At every point the differential is a Fredholm operator of the same negative index, and a negative-index Fredholm operator cannot be onto.

> [!note]- Derivation
> Fix any $x\in X$. Since $F$ is a [[Def - Fredholm Map and Its Index|Fredholm map]], $d_xF\colon T_xX\to T_{F(x)}Y$ is a Fredholm operator, and (operation 1)
> $$\operatorname{index}d_xF=\dim\ker d_xF-\dim\operatorname{coker}d_xF=\operatorname{index}F<0\qquad\text{(index constant on the component of }x\text{; hypothesis).}$$
> **Suppose, toward the rank obstruction, that $d_xF$ were surjective** (operation 2). Then its cokernel $\operatorname{coker}d_xF=T_{F(x)}Y/\operatorname{Im}d_xF$ is the zero space, so $\dim\operatorname{coker}d_xF=0$, and the index formula gives
> $$\dim\ker d_xF=\operatorname{index}d_xF+\dim\operatorname{coker}d_xF=\operatorname{index}F+0=\operatorname{index}F<0\qquad\text{(rearranging the index identity).}$$
> This is impossible, since $\dim\ker d_xF\geq0$ is the dimension of a vector space. The contradiction is between $\dim\ker d_xF\geq0$ and $\dim\ker d_xF<0$. Therefore $d_xF$ is **not** surjective. As $x\in X$ was arbitrary, $d_xF$ fails to be surjective at every point of $X$.

**Step 2: Regular values are exactly the points outside the image (part 1).**

Using Step 1, we prove both inclusions of the set identity {regular values} $=Y\setminus\operatorname{Im}F$.

> [!note]- Derivation
> **Inclusion $\subseteq$: a regular value lies outside the image.** Let $y$ be a [[Def - Regular Value and Transversality for Fredholm Maps|regular value]] of $F$, and suppose for contradiction that $y\in\operatorname{Im}F$, so there is $x\in F^{-1}(y)$. By the definition of regular value, $d_xF$ must be surjective. But by Step 1, $d_xF$ is not surjective — a contradiction (operation 3). Hence $F^{-1}(y)=\varnothing$, i.e. $y\notin\operatorname{Im}F$.
>
> **Inclusion $\supseteq$: a point outside the image is a regular value.** Let $y\notin\operatorname{Im}F$, so $F^{-1}(y)=\varnothing$. The defining condition "$d_xF$ is surjective for every $x\in F^{-1}(y)$" is then a statement quantified over the empty set, hence vacuously true (operation 3). So $y$ is a regular value.
>
> **Combine.** The two inclusions give the equality of sets
> $$\{\,y\in Y : y\text{ is a regular value of }F\,\}=Y\setminus\operatorname{Im}F.$$
> Equivalently, every $y\in\operatorname{Im}F$ is a critical value, and every regular value has empty preimage, which is part 1.

**Step 3: The complement of the image is residual and dense (part 2).**

Sard–Smale supplies residuality of the left-hand side; the set identity transports it to the right-hand side.

> [!note]- Derivation
> By the [[Thm - Sard-Smale Theorem|Sard–Smale theorem]] — for a smooth Fredholm map between second countable Banach manifolds the set of regular values is residual in the target — the set of regular values of $F$ is residual in $Y$ (the hypotheses hold: $X,Y$ are second countable Banach manifolds and $F$ is smooth Fredholm). **Transport across the identity of Step 2** (operation 4): since that set equals $Y\setminus\operatorname{Im}F$,
> $$Y\setminus\operatorname{Im}F\ \text{ is residual in }Y.$$
> A residual subset of a Banach manifold is dense (a Banach manifold is a Baire space, so a set containing a countable intersection of dense open sets is dense). Hence $Y\setminus\operatorname{Im}F$ is dense in $Y$: for a generic $y\in Y$ the equation $F(x)=y$ has no solution. Dually, $\operatorname{Im}F$ is contained in the meagre set of critical values.
>
> **Geometric confirmation (independent check).** The [[Thm - Regular Value and Transversality Theorems for Fredholm Maps|regular-value theorem]] says that if $y$ *were* a regular value with a preimage, $F^{-1}(y)$ would be a smooth manifold of dimension $\operatorname{index}F<0$. The only manifold of negative dimension is the empty manifold, so again $F^{-1}(y)=\varnothing$ for every regular value — consistent with Step 2. This is the "negative expected dimension $\Rightarrow$ empty" reading, and it does not by itself give residuality, which is why Sard–Smale is needed for part 2.

**Step 4: Application (a) — a smooth map $F\colon\mathbb{R}\to\mathbb{R}^{2}$.**

Such a map is Fredholm of index $-1$, so its image misses a dense (indeed full-measure) set.

> [!note]- Derivation
> Let $F\colon\mathbb{R}\to\mathbb{R}^{2}$ be smooth. At each $t\in\mathbb{R}$ the differential $d_tF\colon\mathbb{R}\to\mathbb{R}^{2}$ is a linear map between finite-dimensional spaces, hence automatically Fredholm, with (operation 1, and [[Ex - Index of a Finite-Dimensional Linear Map|the finite-dimensional index formula]] $\operatorname{index}B=\dim(\text{domain})-\dim(\text{codomain})$)
> $$\operatorname{index}d_tF=\dim\mathbb{R}-\dim\mathbb{R}^{2}=1-2=-1<0.$$
> So $F$ is a Fredholm map of index $-1$, and Steps 1–3 apply: the regular values are exactly $\mathbb{R}^{2}\setminus\operatorname{Im}F$, a residual and dense set. Concretely, $d_tF$ has image a line (rank $\leq1$), so it is never onto $\mathbb{R}^{2}$; every point of the curve $\operatorname{Im}F$ is a critical value, and every point off the curve is a regular value with empty preimage. For example $F(t)=(t,t^{2})$ traces the parabola $\{(a,a^{2}):a\in\mathbb{R}\}$; a point $(a,b)$ with $b\neq a^{2}$ is a regular value and is not attained. Independently, [[Thm - Sard's Theorem for Smooth Maps|Sard's theorem for smooth maps]] shows the critical values $\operatorname{Im}F$ have Lebesgue measure zero in $\mathbb{R}^{2}$, so the regular values not only are dense but have full measure — a strengthening available in finite dimensions that matches the companion drill [[Ex - Sard's Theorem for Polynomial Maps]].

**Step 5: Application (b) — a negative-index elliptic operator plus a smooth nonlinearity.**

A lower-order nonlinearity is a compact perturbation of the linearisation, so it does not change the index; a negative-index elliptic equation is generically unsolvable.

> [!note]- Derivation
> Let $M$ be a closed manifold, $E,F\to M$ vector bundles, and $L\colon\Gamma(E)\to\Gamma(F)$ a linear [[Def - Elliptic Differential Operator and Principal Symbol|elliptic]] operator of order $\ell$. Extended to Sobolev completions,
> $$L\colon W^{k+\ell,2}(E)\longrightarrow W^{k,2}(F)$$
> is Fredholm by the [[Thm - Elliptic Operators on Closed Manifolds are Fredholm|elliptic Fredholm theorem]]; assume $\operatorname{index}L=d<0$. Let $N\colon W^{k+\ell,2}(E)\to W^{k,2}(F)$ be a smooth map arising from a fibrewise-smooth nonlinearity of order $\leq\ell-1$, that is $N(u)(x)=n\big(x,u(x),\dots,(\nabla^{\ell-1}u)(x)\big)$ for a smooth $n$. Its differential $d_uN$ at any $u$ is a differential operator of order $\leq\ell-1$, so it factors through the inclusion $W^{k+\ell,2}\hookrightarrow W^{k+\ell-1,2}$, which is compact by the [[Thm - Rellich Compactness Theorem|Rellich compactness theorem]]; hence $d_uN$ is a **compact** operator $W^{k+\ell,2}(E)\to W^{k,2}(F)$.
>
> Set $F:=L+N$. It is smooth, and its differential is $d_uF=L+d_uN$ (operation 5). Since $L$ is Fredholm and $d_uN$ is compact, the [[Thm - Stability of the Fredholm Property under Small and Compact Perturbations|stability theorem]] gives that $d_uF$ is Fredholm with
> $$\operatorname{index}d_uF=\operatorname{index}L=d<0\qquad\text{(index unchanged under compact perturbation).}$$
> So $F$ is a Fredholm map of index $d<0$, and Steps 1–3 apply verbatim on the Banach manifolds $W^{k+\ell,2}(E)$ and $W^{k,2}(F)$ (both separable Hilbert spaces, hence second countable Banach manifolds): **a residual, dense set of right-hand sides $g\in W^{k,2}(F)$ makes the semilinear equation $Lu+N(u)=g$ unsolvable.**
>
> A concrete negative-index elliptic operator on a closed oriented Riemannian four-manifold $M$ with $b_1(M)=0$ is $d^{*}+d^{+}\colon\Omega^{1}(M)\to\Omega^{0}(M)\oplus\Omega^{2}_{+}(M)$, obtained by folding the elliptic de Rham complex ([[Thm - The de Rham Complex is Elliptic and Harmonic Forms Represent de Rham Cohomology|de Rham ellipticity]]); its kernel and cokernel are computed by the [[Thm - Hodge Theorem for Elliptic Complexes|Hodge theorem]] to be $\ker=H^{1}_{\mathrm{dR}}(M)$ and $\operatorname{coker}=H^{0}(M)\oplus H^{2}_{+}(M)$, so
> $$\operatorname{index}(d^{*}+d^{+})=b_{1}-b_{0}-b_{2}^{+}=0-1-b_{2}^{+}=-(1+b_{2}^{+})<0.$$
> On $S^{4}$ this is $-1$. Adding any smooth lower-order nonlinearity leaves the index at $-(1+b_{2}^{+})$, and the corresponding semilinear system is unsolvable for a generic pair $(f,\omega)\in\Omega^{0}\oplus\Omega^{2}_{+}$. This is the same arithmetic that, in Seiberg–Witten theory, makes a moduli space of negative expected dimension generically empty (compare [[Thm - Dimension Formula for the Seiberg-Witten Moduli Space|the Seiberg–Witten dimension formula]]).

> [!note]- Complete formal solution
> **Claim.** If $F\colon X\to Y$ is a smooth Fredholm map of second countable Banach manifolds with $\operatorname{index}F<0$, then the regular values of $F$ are exactly the points of $Y\setminus\operatorname{Im}F$, and this set is residual and dense.
>
> *Step 1.* For every $x\in X$, $d_xF$ is Fredholm with $\operatorname{index}d_xF=\operatorname{index}F<0$. If $d_xF$ were surjective then $\dim\operatorname{coker}d_xF=0$, whence $\dim\ker d_xF=\operatorname{index}F<0$, impossible. So $d_xF$ is nowhere surjective.
>
> *Step 2.* If $y$ is a regular value and $x\in F^{-1}(y)$ existed, then $d_xF$ would be surjective, contradicting Step 1; so $F^{-1}(y)=\varnothing$. Conversely if $F^{-1}(y)=\varnothing$ then $y$ is vacuously a regular value. Hence {regular values} $=Y\setminus\operatorname{Im}F$.
>
> *Step 3.* By Sard–Smale the regular values are residual in $Y$; by Step 2 so is $Y\setminus\operatorname{Im}F$, and a residual subset of a Banach manifold is dense.
>
> *Applications.* (a) A smooth $F\colon\mathbb{R}\to\mathbb{R}^{2}$ has $\operatorname{index}F=1-2=-1$, so $\mathbb{R}^{2}\setminus\operatorname{Im}F$ is residual and dense (indeed full measure, by Sard). (b) For $L$ elliptic of index $d<0$ on a closed manifold and $N$ a smooth order-$(\leq\ell-1)$ nonlinearity, $d_uN$ is compact (Rellich), so $F=L+N$ is Fredholm of index $d<0$ (stability of the index), and $Lu+N(u)=g$ is unsolvable for a residual, dense set of $g$. $\blacksquare$

> [!warning] Illegal but tempting: reading $\dim=\operatorname{index}F<0$ as a negative-dimensional manifold
> The regular-value theorem returns "$F^{-1}(y)$ is a manifold of dimension $\operatorname{index}F$". When $\operatorname{index}F<0$ it is tempting to carry a "manifold of dimension $-1$" through further arguments — for instance to assign it a formal Euler characteristic or a fundamental class. This is meaningless: a manifold has dimension $\geq0$ by definition, and the only consistent interpretation of the theorem's output when $\operatorname{index}F<0$ is that the manifold is *empty*. The extra condition that would make a genuine dimension count legitimate is $\operatorname{index}F\geq0$; only then does a regular value carry a nonempty fibre and does the degree or moduli-space machinery of §10.3–§10.5 have content. Negative index is precisely the regime where the correct output is "no solutions", not "a strange solution set".

---

# Key Takeaways

**A negative Fredholm index is a solvability obstruction, not a dimension: the generic equation has no solution.** The reusable principle is that the index of a smooth Fredholm map is the expected dimension of a regular fibre, and expected dimensions below zero mean empty fibres. Concretely, the proof shows something sharper than "generic fibres are empty": when $\operatorname{index}F<0$ the differential is *nowhere* surjective, so *every* value in the image is critical and the regular values coincide with the unattained points. The trigger to deploy this is any appearance of a Fredholm (in finite dimensions, any smooth) map whose domain is "smaller" than its target in the index sense — a map $\mathbb{R}^{m}\to\mathbb{R}^{n}$ with $m<n$, an elliptic operator with more cokernel than kernel, a deformation operator whose expected moduli dimension came out negative. The diagnostic response is: do not look for solutions; prove there are generically none, and locate the residual set of unreachable data via Sard–Smale.

**The efficient argument settles the pointwise linear algebra first and quotes genericity last.** The transferable structure is the two-tier split. The pointwise tier is pure rank–nullity for one Fredholm operator: negative index forbids surjectivity, because surjectivity zeroes the cokernel and would force a negative kernel dimension. This tier already yields the *exact set identity* {regular values} $=Y\setminus\operatorname{Im}F$, with no analysis and no Baire category. The global tier is a single citation of Sard–Smale, whose only role is to certify that this set is residual, and hence — because a Banach manifold is a Baire space — dense. Keeping the tiers separate is what prevents the common misstep of trying to reason about preimages of "generic regular values" before establishing that regular values have no preimages at all. The same two-tier discipline recurs whenever an integer invariant obstructs a geometric conclusion: prove the pointwise obstruction, extract a set-theoretic identity, then invoke the one genericity theorem.

**Compact perturbations preserve the index, so nonlinearity of lower order cannot rescue a negative-index equation.** The final reusable fact is that adding a smooth lower-order nonlinearity to an elliptic operator does not move the index: the linearisation $L+d_uN$ is a compact perturbation of $L$ (the derivative of a lower-order term factors through a Rellich-compact inclusion), and the index is invariant under compact perturbations. Therefore the unsolvability verdict for the linear operator $L$ transfers intact to the semilinear operator $F=L+N$, at every point $u$ and hence globally. The trigger condition is a semilinear elliptic problem $Lu+N(u)=g$ with $N$ of strictly lower order than $L$; the pattern is "compute the index of $L$ alone, because $N$ is invisible to it". This is exactly the reasoning by which gauge theory reduces the transversality and dimension analysis of a nonlinear moduli problem to the index of a *linear* deformation operator, as in the derivation of [[Thm - Dimension Formula for the Seiberg-Witten Moduli Space|the Seiberg–Witten dimension formula]]. The residual set of regular values that this exercise shows to be entirely unhit is produced by the companion drill [[Ex - Residual Sets and Baire's Theorem in Banach Spaces]].
