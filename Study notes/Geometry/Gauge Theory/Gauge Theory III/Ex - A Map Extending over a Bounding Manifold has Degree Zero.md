---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - The Brouwer Degree is an Integer and a Homotopy Invariant"
  - "Def - Brouwer Degree of a Map"
  - "Def - Manifold with Boundary and Induced Orientation"
  - "Thm - Stokes' Theorem on Manifolds"
  - "Thm - Pull-Back Commutes with the Exterior Derivative"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $N$ be a closed connected oriented smooth $n$-manifold, and let $W$ be a compact oriented smooth $(n+1)$-manifold with boundary $\partial W = M$, so that $M$ is a closed oriented $n$-manifold with the orientation induced from $W$. Suppose $f\colon M\to N$ is a smooth map that **extends** over $W$: there is a smooth map $F\colon W\to N$ with $F|_{\partial W} = f$. Prove:
$$\deg f = 0.$$

This is the bordism-invariance clause — part (f) — of the degree theorem, and it is the single fact that makes the clutching classification of §3.6 work. Its two working consequences are the immediate targets of the exercise:

- **($U(1)$ case).** Let $X$ be a closed connected oriented surface ($n=2$), $D\subset X$ a closed coordinate disc with interior $D^\circ$ and boundary $S=\partial D\cong S^1$, and $a\colon X\setminus D^\circ\to U(1)$ a smooth map. Then the boundary value $a|_S\colon S^1\to U(1)$ has degree zero.
- **($SU(2)$ case).** Let $X$ be a closed connected oriented $4$-manifold ($n=4$), $D\subset X$ a closed coordinate disc with boundary $S=\partial D\cong S^3$, and $a\colon X\setminus D^\circ\to SU(2)$ a smooth map. Then $a|_S\colon S^3\to SU(2)\cong S^3$ has degree zero.

In both consequences the identification of the target with a closed oriented $n$-manifold is what lets "degree" be spoken of at all: $U(1)=S^1$ is a closed oriented $1$-manifold, and $SU(2)$ is diffeomorphic to the closed oriented $3$-manifold $S^3$.

**Recall:**

The objects in play are the Brouwer degree defined through pull-back of a normalised volume form, its bordism-invariance, the induced orientation on a boundary, Stokes' theorem, and the commutation of pull-back with the exterior derivative.

![[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant#Statement]]

The clause we prove here is part **(f)**: *if $M=\partial W$ for a compact oriented $(n+1)$-manifold $W$ and $f$ extends smoothly to $W$, then $\deg f=0$.* We also use the **definition** of the degree recorded on that page and reproved from [[Def - Brouwer Degree of a Map]]: for closed oriented $n$-manifolds $M,N$ with $N$ connected and a smooth $f\colon M\to N$,
$$\deg f := \int_M f^*\omega\qquad\text{for any }\omega\in\Omega^n(N)\text{ with }\int_N\omega=1,$$
and clause **(a)** of the theorem is exactly the statement that this number does not depend on the choice of such an $\omega$. We shall also use the integrality clause **(b)** (the regular-value formula $\deg f=\sum_{x\in f^{-1}(y)}\operatorname{sign}\det df_x$) only to interpret the result, not in the proof.

![[Def - Manifold with Boundary and Induced Orientation#The Definition]]

The **induced (boundary) orientation** on $M=\partial W$ is the "outward-normal-first" orientation: a basis $(v_1,\dots,v_n)$ of $T_pM$ is positive if and only if $(\nu,v_1,\dots,v_n)$ is a positive basis of $T_pW$, where $\nu$ is an outward-pointing vector. This is the convention under which Stokes' theorem holds with no extra sign.

![[Thm - Stokes' Theorem on Manifolds#Statement]]

**Stokes' theorem.** For a compact oriented $(n+1)$-manifold $W$ with boundary $\partial W$ carrying the induced orientation, and any smooth $n$-form $\eta\in\Omega^n(W)$,
$$\int_W d\eta = \int_{\partial W}\eta,$$
where on the right $\eta$ means its restriction $\iota^*\eta$ along the inclusion $\iota\colon\partial W\hookrightarrow W$.

![[Thm - Pull-Back Commutes with the Exterior Derivative#Statement]]

**Naturality of $d$.** For a smooth map $F\colon W\to N$ and any form $\omega\in\Omega^\bullet(N)$, $d(F^*\omega)=F^*(d\omega)$.

---

# Convergent Strategy

**Problem class.** This is a *prove-a-vanishing* problem, and it belongs to the most characteristic family in the whole degree calculus: **an integral invariant vanishes because the integrand is exact and the domain is closed** — or, one dimension up, because the domain has a filling. The degree is by definition the integral over $M$ of a pulled-back top form; the hypothesis "$M$ bounds $W$ and $f$ extends to $W$" is precisely the input that turns that integral over the closed manifold $M$ into an integral of an exact form over the filling $W$, where Stokes reduces it to a boundary integral and the boundary is where we started. The vanishing is a fixed-point of that circle of reasoning: the only value consistent with the manoeuvre is $0$.

**Assumption pattern.** Two hypotheses do all the work, and they are used exactly once each. The hypothesis *$N$ is an $n$-manifold* forces every $n$-form on $N$ to be closed for the trivial reason that $\Omega^{n+1}(N)=0$ — there are no $(n+1)$-forms on an $n$-dimensional manifold. The hypothesis *$f$ extends to $F\colon W\to N$* is what lets us write $f^*\omega$ as the restriction to $\partial W$ of the globally-defined form $F^*\omega$ on $W$; without a global extension there would be nothing on $W$ to which Stokes could be applied. The recognisable trigger for the whole method is the phrase "the map on the boundary extends over the interior": whenever a degree, a winding number, or a period is computed on a boundary that is filled by a map, expect it to vanish.

**Theorem routing.** The route is short and rigid. Pick $\omega\in\Omega^n(N)$ with $\int_N\omega=1$; this exists because $N$ is closed, connected, oriented, so [[Thm - The Top de Rham Cohomology of a Closed Connected Oriented Manifold is R|its top de Rham cohomology is ℝ via integration]]. Write $\deg f=\int_M f^*\omega$ (definition, clause (a) for well-definedness). Use $f=F\circ\iota$ to get $f^*\omega=\iota^*(F^*\omega)$. Apply [[Thm - Stokes' Theorem on Manifolds|Stokes]] to the $n$-form $\eta:=F^*\omega\in\Omega^n(W)$: $\int_{\partial W}\iota^*\eta=\int_W d\eta$. Rewrite $d\eta=d(F^*\omega)=F^*(d\omega)$ by [[Thm - Pull-Back Commutes with the Exterior Derivative|naturality of the exterior derivative]], and note $d\omega=0$ since $d\omega\in\Omega^{n+1}(N)=0$. Hence the boundary integral is $\int_W F^*0=0$.

**Key decision point.** The one genuinely load-bearing observation, and the only place the argument could go wrong, is *why $\omega$ is closed*. It is closed not because it is special but because of a dimension count: $d\omega$ is an $(n+1)$-form on an $n$-manifold, and $\Lambda^{n+1}T^*_yN=0$ at every point $y\in N$ since $\dim N=n$. A reader who forgets this and tries to argue "$\omega$ is a volume form, hence closed only because volume forms happen to be closed" is relying on the wrong reason; the correct reason works for *any* $n$-form on $N$, which is exactly why the definition of degree is allowed to use an arbitrary normalised $\omega$. The second decision is orientational: the induced orientation on $\partial W$ must be the outward-normal-first one for Stokes to carry no sign, and it is under exactly this orientation that "$\deg f$" is computed; both consequences below are insensitive to a global orientation flip of $S$ because a flip changes $\deg(a|_S)$ by an overall sign and $0$ is fixed by it.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles#Legal Operations|the topic page's Legal Operations]]:

1. **Represent the degree as the period of a pulled-back normalised top form.** Replace the combinatorial "signed count of preimages" reading of $\deg f$ by the analytic reading $\deg f=\int_M f^*\omega$, $\int_N\omega=1$; this is the reading on which Stokes can act.

2. **Factor a boundary map through the inclusion.** Write $f=F\circ\iota$ with $\iota\colon\partial W\hookrightarrow W$ the boundary inclusion and $F$ the given extension, so that $f^*\omega=\iota^*(F^*\omega)$ becomes the restriction of a form defined on all of $W$.

3. **Convert a boundary integral to an interior integral by Stokes.** Apply Stokes' theorem to the $n$-form $F^*\omega$ on the $(n+1)$-manifold $W$, turning $\int_{\partial W}\iota^*(F^*\omega)$ into $\int_W d(F^*\omega)$.

4. **Commute pull-back past the exterior derivative.** Rewrite $d(F^*\omega)=F^*(d\omega)$ by naturality of $d$, moving the differentiation onto the target $N$ where it can be evaluated.

5. **Kill a top-degree derivative by a dimension count.** Observe $d\omega=0$ because $d\omega\in\Omega^{n+1}(N)$ and $N$ is $n$-dimensional, so there are no nonzero $(n+1)$-forms on $N$; hence $F^*(d\omega)=0$.

6. **Realise the complement of a disc as a bordism of its boundary sphere.** For the two consequences, recognise $X\setminus D^\circ$ (respectively $D$ itself) as a compact oriented manifold whose boundary is $S$, and the given map $a$ (respectively its restriction to the disc) as an extension of $a|_S$ over that manifold; then apply the vanishing just proved.

---

# Hints

> [!note]- Hint 1
> The degree is defined analytically: $\deg f=\int_M f^*\omega$ for any $n$-form $\omega$ on $N$ with $\int_N\omega=1$. You are given that $f$ is the restriction to $M=\partial W$ of a map $F$ defined on all of $W$. Which theorem relates an integral over a boundary to an integral over the interior it bounds?

> [!note]- Hint 2
> Stokes' theorem says $\int_{\partial W}\eta=\int_W d\eta$. Take $\eta=F^*\omega$, a genuine $n$-form on the $(n+1)$-manifold $W$. Its restriction to $\partial W=M$ is $f^*\omega$ (because $f=F\circ\iota$). So $\deg f=\int_M f^*\omega=\int_W d(F^*\omega)$. Now you only have to evaluate $d(F^*\omega)$.

> [!note]- Hint 3
> Push the derivative onto the target: $d(F^*\omega)=F^*(d\omega)$ (pull-back commutes with $d$). What is $d\omega$, given that $\omega$ is an $n$-form and $N$ is an $n$-dimensional manifold? Count degrees — $d\omega$ would be an $(n+1)$-form on an $n$-manifold.

> [!note]- Hint 4
> $d\omega=0$ because $\Omega^{n+1}(N)=0$ when $\dim N=n$. Hence $F^*(d\omega)=0$ and $\deg f=\int_W 0=0$. For the two consequences: $X\setminus D^\circ$ is a compact oriented manifold with boundary $S$, and the map $a$ *is* an extension of $a|_S$ over it; apply what you just proved with $W=X\setminus D^\circ$, $M=S$, $N=U(1)$ or $SU(2)$. (The map $a|_S$ also extends over the disc $D$ — either filling gives the same conclusion.)

---

# Solution

The proof is one line of Stokes with a dimension count attached. The degree is the integral over $M$ of the pulled-back normalised form $\omega$; because $f$ extends to $F$ on the filling $W$, this equals the integral over $W$ of $d(F^*\omega)=F^*(d\omega)$; and $d\omega=0$ for the purely dimensional reason that $N$ carries no nonzero $(n+1)$-forms. The two consequences are then instances got by taking $W$ to be the complement of a coordinate disc (or the disc), whose boundary is the sphere on which the degree is measured.

**Step 0: Fix a normalised top form on $N$ and recall that the degree is its period.**

Because $N$ is a closed connected oriented $n$-manifold, integration $\int_N\colon H^n_{dR}(N)\to\mathbb{R}$ is an isomorphism, so an $n$-form of unit integral exists; fix one.

> [!note]- Derivation
> By [[Thm - The Top de Rham Cohomology of a Closed Connected Oriented Manifold is R|the top-cohomology theorem]] — for a closed connected oriented $n$-manifold $N$ the map $[\omega]\mapsto\int_N\omega$ is an isomorphism $H^n_{dR}(N)\xrightarrow{\sim}\mathbb{R}$ — the number $\int_N$ takes every value in $\mathbb{R}$, and in particular there exists $\omega\in\Omega^n(N)$ with
> $$\int_N\omega = 1.$$
> Fix such an $\omega$ once and for all. By the definition of the Brouwer degree recorded on [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|the degree page]] and reproved there from [[Def - Brouwer Degree of a Map]],
> $$\deg f = \int_M f^*\omega,$$
> and by clause **(a)** of that theorem this value is independent of which normalised $\omega$ we chose. We shall not need clause (a) again, but it is what makes the single number $\deg f$ well defined before we compute it.

**Step 1: Factor $f$ through the boundary inclusion and identify $f^*\omega$ as a restriction.**

Writing $\iota\colon M=\partial W\hookrightarrow W$ for the inclusion and $F$ for the given extension, $f=F\circ\iota$, hence $f^*\omega=\iota^*(F^*\omega)$.

> [!note]- Derivation
> The extension hypothesis is that $F\colon W\to N$ is smooth with $F|_{\partial W}=f$. In terms of the inclusion $\iota\colon\partial W\hookrightarrow W$ this is precisely the identity of smooth maps
> $$f = F\circ\iota\colon M\longrightarrow N .$$
> Applying the contravariant functoriality of pull-back, $(F\circ\iota)^*=\iota^*\circ F^*$, to the $n$-form $\omega$ gives
> $$f^*\omega = (F\circ\iota)^*\omega = \iota^*\big(F^*\omega\big).$$
> Set $\eta := F^*\omega$. Since $F$ is a smooth map into $N$ and $\omega$ is a smooth $n$-form on $N$, the pull-back $\eta=F^*\omega$ is a smooth $n$-form on the $(n+1)$-manifold $W$, that is $\eta\in\Omega^n(W)$; and $\iota^*\eta$ is exactly the $n$-form $f^*\omega$ appearing in the degree. This is the whole point of the extension: $f^*\omega$ is not merely a form on $M$ but the restriction to $\partial W$ of a form living on all of $W$.

**Step 2: Apply Stokes to $\eta=F^*\omega$ over $W$.**

Stokes' theorem turns the degree, an integral over $\partial W$, into the integral of $d\eta$ over $W$.

> [!note]- Derivation
> The manifold $W$ is compact and oriented with boundary $\partial W=M$, and $M$ carries the induced (outward-normal-first) orientation; this is exactly the setting in which [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] holds with no correction sign. Applied to $\eta=F^*\omega\in\Omega^n(W)$ it reads
> $$\int_{\partial W}\iota^*\eta = \int_W d\eta \qquad\text{(Stokes' theorem, }W\text{ compact oriented with induced boundary orientation)}.$$
> Combining with Step 1, where $\iota^*\eta=\iota^*(F^*\omega)=f^*\omega$, and with the definition of the degree from Step 0,
> $$\deg f = \int_M f^*\omega = \int_{\partial W}\iota^*\eta = \int_W d\eta = \int_W d\big(F^*\omega\big) \qquad\text{(Step 0 definition; Step 1 identity; Stokes).}$$
> Every equality here is now justified: the first by the definition of degree, the second because $M=\partial W$ with the matching orientation, the third by Stokes, the fourth by the definition $\eta=F^*\omega$.

**Step 3: Evaluate $d(F^*\omega)$ and conclude it vanishes.**

Pull-back commutes with $d$, and $d\omega=0$ for dimensional reasons, so $d(F^*\omega)=0$ pointwise on $W$ and the integral is zero.

> [!note]- Derivation
> By [[Thm - Pull-Back Commutes with the Exterior Derivative|naturality of the exterior derivative]] — for any smooth map $F\colon W\to N$ and any form $\omega$, $d(F^*\omega)=F^*(d\omega)$ — we may move the derivative onto the target:
> $$d\big(F^*\omega\big) = F^*\big(d\omega\big) \qquad\text{(pull-back commutes with }d\text{).}$$
> Now examine $d\omega$. Here $\omega\in\Omega^n(N)$, so $d\omega\in\Omega^{n+1}(N)$. But $N$ is an $n$-dimensional manifold, and the bundle of alternating $(n+1)$-forms on an $n$-dimensional space is the zero bundle: for every $y\in N$,
> $$\Lambda^{n+1}T^*_yN = 0 \qquad\text{(an alternating }(n+1)\text{-form on the }n\text{-dimensional space }T_yN\text{ is identically zero),}$$
> so $\Omega^{n+1}(N)=\{0\}$ and therefore $d\omega=0$. This is the one place the hypothesis $\dim N=n$ is used, and it is used as a dimension count, not as any property peculiar to $\omega$. Consequently
> $$d\big(F^*\omega\big) = F^*\big(d\omega\big) = F^*(0) = 0 \in\Omega^{n+1}(W),$$
> and hence, integrating the zero form over $W$,
> $$\deg f = \int_W d\big(F^*\omega\big) = \int_W 0 = 0.$$
> Therefore $\deg f=0$, as claimed.

> [!note]- Complete formal solution
> **Claim.** Let $N$ be a closed connected oriented $n$-manifold and $W$ a compact oriented $(n+1)$-manifold with $\partial W=M$ (induced orientation). If a smooth $f\colon M\to N$ extends to a smooth $F\colon W\to N$, then $\deg f=0$.
>
> Since $N$ is closed, connected, and oriented, [[Thm - The Top de Rham Cohomology of a Closed Connected Oriented Manifold is R|its top de Rham cohomology is ℝ]], so there is $\omega\in\Omega^n(N)$ with $\int_N\omega=1$. By definition (and clause (a) of [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|the degree theorem]], which makes the choice of $\omega$ irrelevant),
> $$\deg f = \int_M f^*\omega .$$
> Let $\iota\colon M=\partial W\hookrightarrow W$ be the inclusion. The extension hypothesis is $f=F\circ\iota$, so $f^*\omega=\iota^*(F^*\omega)$. Put $\eta:=F^*\omega\in\Omega^n(W)$. As $W$ is compact and oriented with $\partial W=M$ in the induced orientation, [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] gives
> $$\int_M f^*\omega = \int_{\partial W}\iota^*\eta = \int_W d\eta = \int_W d(F^*\omega).$$
> By [[Thm - Pull-Back Commutes with the Exterior Derivative|naturality of the exterior derivative]], $d(F^*\omega)=F^*(d\omega)$; and $d\omega\in\Omega^{n+1}(N)=\{0\}$ because $\dim N=n$, so $d\omega=0$ and $F^*(d\omega)=0$. Hence
> $$\deg f = \int_W 0 = 0. \qquad\blacksquare$$
>
> **Consequence ($U(1)$, $n=2$).** Let $X$ be a closed connected oriented surface, $D\subset X$ a closed coordinate disc with boundary $S=\partial D\cong S^1$, and $a\colon X\setminus D^\circ\to U(1)$ smooth. Then $W:=X\setminus D^\circ$ is a compact oriented $2$-manifold with $\partial W=S$; the map $a$ is a smooth extension of $a|_S$ over $W$; and $N:=U(1)=S^1$ is a closed connected oriented $1$-manifold. By the claim, $\deg(a|_S)=0$.
>
> **Consequence ($SU(2)$, $n=4$).** Let $X$ be a closed connected oriented $4$-manifold, $D\subset X$ a closed coordinate disc with boundary $S=\partial D\cong S^3$, and $a\colon X\setminus D^\circ\to SU(2)$ smooth. Then $W:=X\setminus D^\circ$ is a compact oriented $4$-manifold with $\partial W=S$; $a$ extends $a|_S$ over $W$; and $N:=SU(2)\cong S^3$ (via [[Ex - SU(2) is the Group of Unit Quaternions|the identification of SU(2) with the unit quaternions]]) is a closed connected oriented $3$-manifold. By the claim, $\deg(a|_S)=0$. $\blacksquare$

> [!warning] Illegal but tempting shortcut: "$a|_S$ is null-homotopic because $X\setminus D^\circ$ is filled, hence its degree is zero."
> It is tempting to argue that $a|_S$ extends over the manifold $X\setminus D^\circ$, therefore $a|_S$ is null-homotopic, therefore $\deg(a|_S)=0$ by homotopy invariance (clause (c)). The final conclusion is correct, but the middle step is **false in general**: extending a map over a manifold $W$ with $\partial W=S$ does **not** make the boundary map null-homotopic unless $W$ is a disc (or more generally has $S$ null-homotopic in it). For example, when $W=X\setminus D^\circ$ is the complement of a disc in a surface of positive genus, $a|_S$ need not be contractible in $W$, and yet its degree still vanishes. The genuinely correct reason is bordism, not homotopy: Stokes needs only a *filling* of $S$ by a map, and a filling is much weaker than a contraction. The homotopy argument *does* work in the disc case $W=D$, where $S=\partial D$ is contractible in $D$; that is why we may also fill $a|_S$ by the disc. The extra condition that would rescue the shortcut in general is precisely "$S$ bounds a disc in $W$", which is not available for $X\setminus D^\circ$.

> [!note]- Independent check on the smallest case
> Take $X=S^2$, $D$ a closed hemisphere disc, $S$ the equator $\cong S^1$, $N=U(1)=S^1$. Let $a\colon X\setminus D^\circ\to U(1)$ be constant, $a\equiv 1$. Then $a|_S\equiv 1$ is constant, its degree is $0$ by the regular-value count (a constant map is not surjective, so by clause (d) its degree is $0$), matching the theorem. Now take $a$ non-constant, say on the lower hemisphere disc $D'=X\setminus D^\circ$ parametrised by $(r,\phi)\in[0,1]\times S^1$ (with $r=1$ the equator $S$) set $a(r,\phi)=e^{i\,\rho(r)\phi}$ with $\rho$ smooth, $\rho\equiv 0$ near $r=0$, $\rho(1)=m\in\mathbb{Z}$; this is smooth and single-valued only if $m=0$, because $e^{i\rho(r)\phi}$ must agree at $\phi=0$ and $\phi=2\pi$, forcing $\rho(r)\in\mathbb{Z}$ for all $r$, hence $\rho\equiv 0$ by continuity from $\rho\equiv0$ near the centre. So the only smooth $a$ of this rotationally-symmetric form has $a|_S$ of winding number $0$ — the theorem is not merely satisfied, it is forced: a nonzero winding number on the equator obstructs any smooth extension over the disc. This is the obstruction-theoretic content of the result seen by hand.

---

# Key Takeaways

**When an integral invariant is defined by pulling a top form back to a boundary, filling the boundary makes the invariant vanish — this is Stokes read as a conservation law.** The proof pattern is completely mechanical and worth internalising as a single reflex: degree $=\int_M f^*\omega$; if $M=\partial W$ and $f=F|_{\partial W}$ then $\int_M f^*\omega=\int_W dF^*\omega=\int_W F^*d\omega$, and $d\omega=0$ because $\omega$ is already top-degree on the target. The invariant is an obstruction to filling: a nonzero degree is a certificate that the boundary map does *not* extend over any oriented filling. The same three lines, with "degree" replaced by "winding number", "period", "flux", or "linking number", prove that each of those vanishes on a filled boundary; the only ingredients are that the invariant is the integral of a closed pulled-back form and that the domain bounds. The trigger to reach for this argument is the co-occurrence of two phrases in a problem: "a map on the boundary" and "which extends over the interior".

**The hypothesis that does the killing is a dimension count, not a property of the chosen form.** The step $d\omega=0$ holds for *every* $n$-form on the $n$-manifold $N$, because $\Omega^{n+1}(N)=0$ when $\dim N=n$; it has nothing to do with $\omega$ being a volume form or being closed for some special reason. This is exactly why the definition of the Brouwer degree is permitted to use an arbitrary normalised top form rather than a distinguished one, and it is the reason clause (a) — independence of $\omega$ — and clause (f) — bordism invariance — are two faces of the same fact. When transferring the argument to a setting where the target has dimension $> n$ (say the domain is a hypersurface in a higher-dimensional manifold), this step fails and the vanishing is generally false; the diagnostic to run first is always "is the pulled-back form top-degree on its target?".

**In the clutching classification, this lemma is the engine that makes the degree of a clutching function well defined.** A principal bundle $P$ over a closed manifold $X$ that is trivial over $X\setminus D^\circ$ and over $D$ is described by a clutching map $g\colon S\to G$ on the boundary sphere $S=\partial D$, and two clutching maps give isomorphic bundles exactly when $g'=(a|_S)\,g\,(b|_S)$ for smooth $a\colon X\setminus D^\circ\to G$ and $b\colon D\to G$ (see [[Thm - Clutching Construction for Bundles over a Closed Manifold|the clutching theorem]]). For $G=U(1)$ or $G=SU(2)$ the degree (winding number, respectively $\deg$ into $S^3$) is additive under pointwise products, so $\deg g'=\deg(a|_S)+\deg g+\deg(b|_S)$; and *both* correction terms vanish by this exercise, because $a|_S$ extends over $X\setminus D^\circ$ and $b|_S$ extends over $D$. Hence $\deg g$ is an invariant of the bundle, independent of the trivialisations used to read off $g$. This is precisely how $\deg$ becomes the degree of a line bundle over a surface and $k(P)$ becomes the Chern number of an $SU(2)$-bundle over a four-manifold; the vanishing proved here is what removes the ambiguity in both. The companion exercise [[Ex - Degree of the Power Maps on the Circle and on SU(2)|the degrees of the power maps]] then supplies the concrete clutching maps of every possible degree, so that between the two exercises the classification of §3.6 has both its well-definedness and its existence half in hand.
