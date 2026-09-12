---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Banach Manifold and Smooth Maps between Banach Spaces"
  - "Thm - The Contraction Mapping Principle"
  - "Thm - Banach–Steinhaus and Open Mapping (Application of Baire)"
  - "Def - Regular and Critical Points"
  - "Def - Embedded Submanifold"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $X$, $Y$, $X_1$, $X_2$ are real Banach spaces — complete normed vector spaces — with norms written $\lVert\cdot\rVert$ (the space is clear from the argument). A linear map $L\colon X\to Y$ is **bounded** if $\lVert L\rVert_{\mathrm{op}} := \sup_{\lVert x\rVert\le 1}\lVert Lx\rVert < \infty$; the space of all bounded linear maps $X\to Y$ is $\mathcal{L}(X,Y)$, itself a normed space with the operator norm, and $\mathcal{L}(X) := \mathcal{L}(X,X)$. A **bounded linear isomorphism** (we say simply *isomorphism*) is a bounded linear bijection $L\colon X\to Y$ whose set-theoretic inverse $L^{-1}$ is also bounded; the identity is $\operatorname{id}$.

For an open set $U\subseteq X$ a map $F\colon U\to Y$ is **differentiable** at $x\in U$ if there is a bounded linear map $d_xF\in\mathcal{L}(X,Y)$, the **(Fréchet) derivative**, with
$$F(x+h) = F(x) + d_xF\,h + o(\lVert h\rVert)\qquad (h\to 0),$$
meaning $\lVert F(x+h)-F(x)-d_xF\,h\rVert/\lVert h\rVert\to 0$; $F$ is $C^1$ if $x\mapsto d_xF\in\mathcal{L}(X,Y)$ is continuous, and $C^k$ ($k\ge 1$) or $C^\infty$ inductively, exactly as on the companion page **[[Def - Banach Manifold and Smooth Maps between Banach Spaces]]**, which also proves the chain rule $d_x(G\circ F) = d_{F(x)}G\circ d_xF$ used repeatedly below. A **$C^k$ diffeomorphism** $U'\to V'$ is a $C^k$ bijection with $C^k$ inverse. For a product $F\colon X_1\times X_2\to Y$ the **partial derivatives** $\partial_1 F(a,b)\in\mathcal{L}(X_1,Y)$ and $\partial_2 F(a,b)\in\mathcal{L}(X_2,Y)$ are the derivatives of $x_1\mapsto F(x_1,b)$ and $x_2\mapsto F(a,x_2)$, so that $d_{(a,b)}F(h_1,h_2) = \partial_1F(a,b)h_1 + \partial_2F(a,b)h_2$.

A closed subspace $K\subseteq X$ is **complemented** if there is a closed subspace $X_1\subseteq X$ with $X = K\oplus X_1$ (every $x$ is uniquely $k+x_1$) and the two projections $x\mapsto k$, $x\mapsto x_1$ bounded; equivalently $K$ is the image of a bounded idempotent $P = P^2\in\mathcal{L}(X)$. A subset $S$ of a Banach manifold is an **embedded submanifold** if near each of its points there is a chart of the ambient manifold carrying $S$ onto (a relatively open piece of) a closed complemented subspace of the model space, as on **[[Def - Banach Manifold and Smooth Maps between Banach Spaces]]**; its tangent space $T_xS$ is that subspace read back through the chart. For a $C^1$ map $F$ between Banach manifolds, $y$ is a **regular value** (in the sense of **[[Def - Regular and Critical Points]]**, transported to the Banach setting) if $d_xF\colon T_xX\to T_yY$ is surjective for every $x\in F^{-1}(y)$; the condition is vacuous when $F^{-1}(y)=\varnothing$.

> [!warning] Convention: what the source states versus what we prove
> Haydys (*Introduction to Gauge Theory*, §6.2, Step 2 of the proof of Theorem 166, p. 54) invokes "the inverse function theorem" for maps between Banach manifolds without stating or proving it — the item catalogued as A-I6.2.1 is precisely this appeal. We supply the full statement in its three standard forms (inverse function theorem, implicit function theorem, and the regular-value/local-submersion theorem for maps with complemented kernel) and prove all three at the vault's proof floor. The finite-dimensional templates are **[[Thm - The Inverse Function Theorem]]** and **[[Thm - The Implicit Function Theorem]]**; every step there survives verbatim once "$\mathbb{R}^n$" is replaced by "a Banach space", the completeness of $\mathbb{R}^n$ by the completeness of the Banach space, and the automatic continuity of finite-dimensional linear maps by an explicit boundedness hypothesis on the derivative — which is the only substantive change.

---

# Statement

> **Theorem (inverse function theorem on Banach spaces — part (i)).** Let $X$, $Y$ be Banach spaces, $U\subseteq X$ open, $x_0\in U$, and $F\colon U\to Y$ a $C^k$ map with $k\ge 1$. Suppose the derivative $d_{x_0}F\colon X\to Y$ is a bounded linear isomorphism. Then there are open sets $x_0\in U'\subseteq U$ and $F(x_0)\in V'\subseteq Y$ such that $F$ restricts to a $C^k$ diffeomorphism $F\colon U'\to V'$. Moreover $d_{x}F$ is an isomorphism for every $x\in U'$, and the inverse $g := (F|_{U'})^{-1}$ satisfies $d_yg = \bigl(d_{g(y)}F\bigr)^{-1}$ for all $y\in V'$.

> **Theorem (implicit function theorem — part (ii)).** Let $X_1$, $X_2$, $Y$ be Banach spaces, $W\subseteq X_1\times X_2$ open, $(a,b)\in W$, and $F\colon W\to Y$ a $C^k$ map ($k\ge 1$) with $F(a,b)=0$. Suppose the partial derivative $\partial_2 F(a,b)\colon X_2\to Y$ is a bounded linear isomorphism. Then there are open sets $a\in A\subseteq X_1$ and $b\in B\subseteq X_2$ with $A\times B\subseteq W$, and a $C^k$ map $g\colon A\to B$ with $g(a)=b$, such that for $(x_1,x_2)\in A\times B$,
> $$F(x_1,x_2) = 0 \iff x_2 = g(x_1).$$
> That is, the zero set of $F$ near $(a,b)$ is exactly the graph of $g$; and $d_a g = -\bigl(\partial_2F(a,b)\bigr)^{-1}\partial_1F(a,b)$.

> **Theorem (regular-value / local-submersion theorem — part (iii)).** Let $F\colon X\to Y$ be a $C^k$ map ($k\ge 1$) between Banach manifolds and let $y\in Y$ be a regular value of $F$. Suppose that for every $x\in F^{-1}(y)$ the kernel $\ker d_xF\subseteq T_xX$ is complemented. Then $F^{-1}(y)$ is a $C^k$ embedded submanifold of $X$, modelled near $x$ on $\ker d_xF$, with tangent space
> $$T_x F^{-1}(y) = \ker d_xF\qquad\text{for every } x\in F^{-1}(y).$$
> The complementedness hypothesis is automatic when each $d_xF$ is a Fredholm operator, because then $\ker d_xF$ is finite-dimensional.

These three are one statement seen from three sides. Part (i) is the base case: an isomorphic linearisation makes $F$ locally invertible. Part (ii) is (i) applied to the "graph map" $(x_1,x_2)\mapsto(x_1,F(x_1,x_2))$, and it repackages the conclusion as "the solution set of $F=0$ is a graph". Part (iii) is (ii) done invariantly on a manifold, with $X_2$ playing the role of a complement to the kernel: it is the theorem that turns the regular-value hypothesis into the manifold structure on $F^{-1}(y)$ used everywhere in this chapter.

---

# Motivation

This is the workhorse of the entire chapter, and of infinite-dimensional differential topology generally. Every later structural theorem of Gauge Theory X is, at bottom, an application of it. The **[[Thm - Kuranishi Model for a Fredholm Map|Kuranishi model]]** solves a nonlinear Fredholm equation in the directions where the linearisation is invertible by applying part (i) and leaves a finite-dimensional remainder; the **[[Thm - Regular Value and Transversality Theorems for Fredholm Maps|regular-value theorem for Fredholm maps]]** is part (iii) with the finite cokernel absorbed; the local diffeomorphism that makes the degree count **[[Thm - The Degree Count is Locally Constant on Regular Values|locally constant]]** is again part (i). When chapter XI builds the Seiberg–Witten moduli space as the zero set of a section, it is part (iii) that gives that zero set the structure of a manifold.

The question the theorem answers is the oldest one in analysis: given a nonlinear equation $F(x) = y$, when can we solve for $x$, and how does the solution depend on $y$? In finite dimensions this is the ordinary inverse and implicit function theorems, and the answer is local and linear-algebraic: solve it whenever the linearisation $d_{x_0}F$ is invertible. The content of the present theorem is that *the same answer holds in infinite dimensions*, provided one reads "invertible" correctly. In infinite dimensions a linear bijection need not have a bounded inverse, and a bounded linear map need not be closed-range or surjective; so "the linearisation is an isomorphism" must mean a *bounded* linear isomorphism, and the proof must produce a solution operator that is genuinely continuous. The mechanism that delivers this is not linear algebra — there is no rank–nullity theorem to lean on — but iteration: the nonlinear map is a small perturbation of its (invertible) linear part, and Picard iteration against that linear part converges. This is why the theorem sits directly on top of **[[Thm - The Contraction Mapping Principle|the contraction mapping principle]]**, the one existence theorem that never mentions dimension.

The smallest concrete case is instructive and worth carrying through the whole page. Take $X = Y = \mathbb{R}$ and $F(x) = x + \tfrac12 x^2$, with $x_0 = 0$. Then $d_0F = 1$, an isomorphism of $\mathbb{R}$, and the theorem promises a local $C^\infty$ inverse near $0$; indeed $g(y) = -1 + \sqrt{1+2y}$ inverts $F$ for $y > -\tfrac12$, and one sees the locality (the other branch $-1-\sqrt{1+2y}$ is excluded). The map $\varphi(x) = x - F(x) = -\tfrac12 x^2$ has $\varphi'(0) = 0$ and is a contraction on a small interval; solving $F(x) = y$ is solving the fixed-point equation $x = y + \varphi(x)$, and the fixed point is found by iterating $x\mapsto y - \tfrac12 x^2$. Everything in the general proof is this picture with $\mathbb{R}$ replaced by a Banach space and the derivative replaced by a bounded operator.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis of part (i) is "$d_{x_0}F$ is a bounded linear isomorphism". The skill is recognising when a problem hands you an isomorphic linearisation without saying so.

The first disguised source is **an injective Fredholm operator of index zero.** Property $B$: the linearisation $L := d_{x_0}F$ is a **[[Def - Fredholm Operator and Index|Fredholm operator]]** — closed range, finite-dimensional kernel and cokernel — of index $0$, and it happens to be injective. The bridge is a two-line piece of linear algebra with an analytic tail: index $0$ means $\dim\ker L = \dim\operatorname{coker}L$, so injectivity ($\ker L = 0$) forces $\operatorname{coker}L = 0$, that is, $L$ is a bounded bijection; and a bounded linear bijection between Banach spaces is automatically an isomorphism by the bounded inverse theorem (a corollary of the open mapping theorem, restated below). So a purely algebraic check — "the linearisation is index-zero Fredholm and has no kernel" — certifies the analytic hypothesis. *Example problem:* at an irreducible Seiberg–Witten solution the linearised operator is index-zero Fredholm; showing it is injective (no infinitesimal deformations) makes the solution isolated and non-degenerate, exactly the input part (i) wants.

The second disguised source is **an invertible operator plus a small perturbation.** Property $B$: $d_{x_0}F = L_0 + K$ where $L_0$ is a known isomorphism and $\lVert K\rVert_{\mathrm{op}} < 1/\lVert L_0^{-1}\rVert_{\mathrm{op}}$. The bridge is the Neumann series (Lemma 2 below): under that smallness bound $L_0 + K$ is again an isomorphism, with inverse $\sum_{n\ge 0}(-L_0^{-1}K)^nL_0^{-1}$. So one never has to invert the full operator; it suffices to invert a nearby model and control the difference. *Example problem:* a nonlinear elliptic equation whose linearisation is $\Delta + V$ with $V$ a small potential — invert $\Delta$ on the relevant Sobolev spaces and treat $V$ perturbatively.

The third disguised source is **a bounded linear bijection with no evident inverse estimate.** Property $B$: one has shown $d_{x_0}F$ is bounded, injective, and surjective, but has no direct estimate on $\lVert(d_{x_0}F)^{-1}\rVert$. The bridge is again the bounded inverse theorem: between Banach spaces, bijectivity plus boundedness *is* isomorphism, and no separate inverse estimate need be produced. The subtlety is that this fails without completeness of both spaces — the theorem quietly consumes the Banach hypothesis. *Example problem:* verifying that a change of variables built from a bounded linear bijection of Sobolev spaces is a chart, without estimating the inverse map by hand.

**Targets (Output Amplification)**

The bare conclusion is a local inverse (or a local graph). Combined with other structure it produces the chapter's main objects.

Combine part (i) with **the Fredholm decomposition of the domain and codomain.** Extra ingredient $D$: split $X = \ker d_pF\oplus X_1$ and $Y = \operatorname{im}d_pF\oplus Y_1$ using the Fredholm property. The payoff $E$ is the **[[Thm - Kuranishi Model for a Fredholm Map|Kuranishi model]]**: applying part (i) to the invertible block $d_pF|_{X_1}\colon X_1\to\operatorname{im}d_pF$ reduces the equation $F = 0$ to a finite-dimensional equation $f_0\colon\ker d_pF\to Y_1$. This is the single most important consequence in the chapter, and it is non-obvious because it converts an infinite-dimensional nonlinear problem into a finite-dimensional one purely by isolating the invertible directions.

Combine part (iii) with **the index of a Fredholm map.** Extra ingredient $D$: $\operatorname{index} d_xF = \dim\ker d_xF - \dim\operatorname{coker}d_xF$ is locally constant (chapter IX). The payoff $E$ is that $F^{-1}(y)$, when $y$ is a regular value, is a manifold of dimension exactly $\operatorname{index} F$ — the **[[Thm - Regular Value and Transversality Theorems for Fredholm Maps|regular-value theorem for Fredholm maps]]**. The count is non-obvious because dimension is being read off an analytic invariant of the linearisation rather than from any coordinate description.

Combine part (i) with **properness of the map.** Extra ingredient $D$: $F$ is a proper index-zero Fredholm map, so preimages of compact sets are compact. The payoff $E$ is that near a regular value $y$ the map $F$ is a finite covering — the local diffeomorphisms from part (i) glue to a locally constant preimage count — which is the definition-making step behind the **[[Def - Mod-2 Degree of a Proper Fredholm Map|mod-2 degree]]**. The non-obviousness is that local invertibility (analysis) plus properness (topology) together, and neither alone, give a well-defined count.

---

# Why Is It True

Forget the ε–δ bookkeeping and picture the geometry. Near $x_0$ the map $F$ agrees with its linear part $L = d_{x_0}F$ to first order: $F(x) = F(x_0) + L(x-x_0) + \text{error}$, where the error is $o(\lVert x-x_0\rVert)$ — genuinely negligible compared with the linear term on a small enough ball. If there were *no* error, $F$ would be the affine map $x\mapsto F(x_0)+L(x-x_0)$, which is invertible precisely because $L$ is; solving $F(x)=y$ would be the single linear step $x = x_0 + L^{-1}(y-F(x_0))$. The theorem says the error does not spoil this, and the reason is that the error is small *relative to the linear part*, not merely small.

Make this exact by trying to solve $F(x) = y$ as a fixed-point problem. Rearranging, $x = x + L^{-1}(y - F(x)) =: G_y(x)$, where the correction $L^{-1}(y-F(x))$ vanishes exactly when $F(x)=y$. The derivative of $G_y$ is $\operatorname{id} - L^{-1}d_xF$, which is $\operatorname{id} - L^{-1}L = 0$ at $x_0$ and, by continuity of the derivative, stays smaller than $\tfrac12$ in norm on a small ball. A map whose derivative is uniformly below $\tfrac12$ moves any two points at most half as far apart as they started — it is a contraction — and the contraction mapping principle then produces a unique fixed point, hence a unique solution $x = g(y)$, and organises the solutions into a continuous (indeed Lipschitz) function of $y$. Differentiating $F(g(y)) = y$ by the chain rule gives $d_{g(y)}F\cdot d_yg = \operatorname{id}$, so the inverse is differentiable with derivative $(d_{g(y)}F)^{-1}$; that the operator-inverse depends smoothly on its argument (the Neumann series) then bootstraps $g$ from continuous to $C^k$.

**The mechanism in one sentence: a map whose linearisation is a bounded isomorphism is invertible near the point, because solving it is a fixed-point problem in which the nonlinear error is a contraction relative to the invertible linear part.**

The only place infinite dimensions intrude is where finite-dimensional intuition silently uses compactness or automatic continuity: the contraction mapping principle needs the domain complete (a closed ball in a Banach space is complete, so this is free), and the linear part needs a *bounded* inverse (this is a hypothesis, and where the domain is only algebraically split we recover boundedness from the open mapping theorem). Everything else is the finite-dimensional argument unchanged.

---

# What Makes This Hard

The delicate points are three, and each is a place where a finite-dimensional habit fails silently. First, **the inverse must be shown continuous, not merely to exist**: a bijection with a linear-algebraic inverse can have an unbounded inverse in infinite dimensions, so the proof must produce a Lipschitz solution operator by hand (from the contraction estimate) rather than quoting invertibility of a matrix. Second, **the smoothness of the inverse is not automatic and is where the Banach-space machinery genuinely earns its keep**: differentiability of $g$ needs the map $L\mapsto L^{-1}$ on operators to be differentiable, which is the Neumann-series computation, and the common error is to assert $C^k$-ness of $g$ without it. Third, in part (iii) **complementedness is a real hypothesis, not a formality**: not every closed subspace of a Banach space admits a bounded projection, so "the kernel is complemented" must be checked (it is automatic in Hilbert spaces and for finite-dimensional or finite-codimensional subspaces, and hence for Fredholm operators — but this is a theorem, invoked below, not a triviality).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove part (i) by turning $F(x)=y$ into a fixed-point equation $x = G_y(x)$ whose map is a contraction on a small closed ball; the contraction mapping principle gives a unique continuous solution operator $g$, the Neumann series gives invertibility of $d_xF$ nearby and smoothness of operator inversion, and these upgrade $g$ to $C^k$. Derive part (ii) by applying part (i) to the graph map, and part (iii) by applying part (i) in charts to the "kernel-plus-map" coordinates.

**Subgoal decomposition:**

1. **Mean value inequality on Banach spaces.** Bound the increment of a $C^1$ map by the supremum of its derivative's operator norm along the segment.
   - *Hint:* Reduce to a scalar sup argument along the path $t\mapsto\varphi(a+t(b-a))$; no vector-valued integration is needed.
   - *Why needed:* It converts the pointwise smallness $\lVert d_x\varphi\rVert\le\tfrac12$ into the global contraction estimate.

2. **Neumann series: invertibles are open and inversion is smooth.** Show a small perturbation of an isomorphism is an isomorphism, and $L\mapsto L^{-1}$ is $C^\infty$ with derivative $H\mapsto -L^{-1}HL^{-1}$.
   - *Hint:* $(L+H)^{-1} = (\operatorname{id}+L^{-1}H)^{-1}L^{-1} = \sum_n(-L^{-1}H)^nL^{-1}$.
   - *Why needed:* It gives invertibility of $d_xF$ near $x_0$ and the smoothness that bootstraps the inverse to $C^k$.

3. **Local solution by contraction.** For $F$ with $d_{x_0}F$ an isomorphism, produce $r,s>0$ so that each $y$ near $F(x_0)$ has a unique preimage $g(y)$ in $\overline{B}_r(x_0)$, with $g$ Lipschitz.
   - *Hint:* Reduce to $x_0=0$, $F(0)=0$, $d_0F=\operatorname{id}$; set $\varphi = \operatorname{id}-F$ and $G_y = y+\varphi$; use subgoals 1 and the contraction mapping principle.
   - *Why needed:* This is the analytic heart of part (i).

4. **Finite-dimensional subspaces are complemented.** Any finite-dimensional subspace of a Banach space is the range of a bounded projection.
   - *Hint:* Biorthogonal functionals, extended off the subspace by the Hahn–Banach theorem.
   - *Why needed:* It makes the complementedness hypothesis of part (iii) automatic for Fredholm linearisations.

---

# Lemma Decomposition

> [!note]- Lemma 1: Mean value inequality for $C^1$ maps between Banach spaces
> **Statement:** Let $X$, $Y$ be Banach spaces, $U\subseteq X$ open, $\varphi\colon U\to Y$ of class $C^1$, and let $a,b\in U$ with the segment $[a,b] := \{a+t(b-a) : t\in[0,1]\}$ contained in $U$. Then
> $$\lVert\varphi(b)-\varphi(a)\rVert \;\le\; \Bigl(\sup_{t\in[0,1]}\lVert d_{a+t(b-a)}\varphi\rVert_{\mathrm{op}}\Bigr)\,\lVert b-a\rVert.$$
>
> **Hint:** Apply a scalar "supremum along the path" argument to $g(t) := \varphi(a+t(b-a))$, whose derivative is $g'(t) = d_{a+t(b-a)}\varphi\,(b-a)$; no vector-valued integral is required.
>
> **Why needed:** In Lemma 3 the auxiliary map $\varphi = \operatorname{id}-F$ has $\lVert d_x\varphi\rVert\le\tfrac12$ on a small ball; this lemma turns that pointwise bound into the contraction estimate $\lVert\varphi(x)-\varphi(x')\rVert\le\tfrac12\lVert x-x'\rVert$.
>
> > [!note]- Full proof
> > **Set up the path.** Define $g\colon[0,1]\to Y$ by $g(t) := \varphi\bigl(a+t(b-a)\bigr)$. The affine map $t\mapsto a+t(b-a)$ is $C^\infty$ with derivative $b-a$, and $\varphi$ is $C^1$, so by the chain rule ([[Def - Banach Manifold and Smooth Maps between Banach Spaces]]) $g$ is $C^1$ on $[0,1]$ with $g'(t) = d_{a+t(b-a)}\varphi\,(b-a)$. Put $M := \sup_{t\in[0,1]}\lVert d_{a+t(b-a)}\varphi\rVert_{\mathrm{op}}$, which is finite because $t\mapsto d_{a+t(b-a)}\varphi$ is continuous on the compact interval $[0,1]$. Then for every $t$,
> > $$\lVert g'(t)\rVert \;\le\; \lVert d_{a+t(b-a)}\varphi\rVert_{\mathrm{op}}\,\lVert b-a\rVert \;\le\; M\lVert b-a\rVert \qquad\text{(operator-norm bound applied to } b-a\text{).}$$
> > Write $N := M\lVert b-a\rVert$; it remains to show $\lVert g(1)-g(0)\rVert\le N$.
> >
> > **The connectedness estimate.** Fix $\varepsilon>0$ and define
> > $$S := \bigl\{\,t\in[0,1] : \lVert g(t)-g(0)\rVert \le (N+\varepsilon)t + \varepsilon\,\bigr\}.$$
> > The set $S$ is closed in $[0,1]$ because $t\mapsto\lVert g(t)-g(0)\rVert-(N+\varepsilon)t-\varepsilon$ is continuous and $S$ is the preimage of $(-\infty,0]$; and $0\in S$ since the left side is $0\le\varepsilon$. Let $s := \sup S$; by closedness $s\in S$. We claim $s = 1$.
> >
> > **Rule out $s<1$.** Suppose $s<1$. Since $g$ is differentiable at $s$ with $\lVert g'(s)\rVert\le N$, there is $h_0>0$ with $s+h_0\le 1$ and, for $0<h\le h_0$,
> > $$\lVert g(s+h)-g(s)-h\,g'(s)\rVert \le \varepsilon h \qquad\text{(definition of the derivative of } g \text{ at } s\text{),}$$
> > whence, by the triangle inequality and $\lVert g'(s)\rVert\le N$,
> > $$\lVert g(s+h)-g(s)\rVert \le h\lVert g'(s)\rVert + \varepsilon h \le (N+\varepsilon)h.$$
> > Combining with $s\in S$,
> > $$\lVert g(s+h)-g(0)\rVert \le \lVert g(s+h)-g(s)\rVert + \lVert g(s)-g(0)\rVert \le (N+\varepsilon)h + (N+\varepsilon)s + \varepsilon = (N+\varepsilon)(s+h)+\varepsilon,$$
> > so $s+h\in S$, contradicting $s=\sup S$. Hence $s=1$.
> >
> > **Conclude.** From $1\in S$ we get $\lVert g(1)-g(0)\rVert\le (N+\varepsilon)+\varepsilon = N + 2\varepsilon$. Letting $\varepsilon\to 0$ gives $\lVert g(1)-g(0)\rVert\le N = M\lVert b-a\rVert$. Since $g(1)-g(0) = \varphi(b)-\varphi(a)$, this is the claim. $\blacksquare$

> [!note]- Lemma 2: Neumann series — invertible operators are open and inversion is smooth
> **Statement:** Let $X$, $Y$ be Banach spaces and $L\in\mathcal{L}(X,Y)$ a bounded linear isomorphism. **(a)** If $H\in\mathcal{L}(X,Y)$ satisfies $\lVert H\rVert_{\mathrm{op}} < 1/\lVert L^{-1}\rVert_{\mathrm{op}}$, then $L+H$ is an isomorphism, with
> $$(L+H)^{-1} = \sum_{n=0}^\infty (-L^{-1}H)^n\,L^{-1}\qquad\text{(convergent in operator norm),}\qquad \lVert(L+H)^{-1}\rVert_{\mathrm{op}} \le \frac{\lVert L^{-1}\rVert_{\mathrm{op}}}{1-\lVert L^{-1}\rVert_{\mathrm{op}}\lVert H\rVert_{\mathrm{op}}}.$$
> **(b)** The set $\operatorname{Iso}(X,Y)$ of isomorphisms is open in $\mathcal{L}(X,Y)$, and the inversion map $\iota\colon\operatorname{Iso}(X,Y)\to\mathcal{L}(Y,X)$, $\iota(L) = L^{-1}$, is $C^\infty$, with derivative $d_L\iota(H) = -L^{-1}HL^{-1}$.
>
> **Hint:** Factor $L+H = L(\operatorname{id}+L^{-1}H)$ and sum the geometric series for $(\operatorname{id}+R)^{-1}$ with $R = L^{-1}H$, $\lVert R\rVert<1$.
>
> **Why needed:** Part (a) shows $d_xF$ stays invertible near $x_0$ (needed for the inverse's derivative to exist at every nearby point); part (b) is what bootstraps the inverse $g$ from continuous to $C^k$.
>
> > [!note]- Full proof
> > **Completeness of the operator space.** Since $Y$ is complete, $\mathcal{L}(X,Y)$ is complete in the operator norm: a Cauchy sequence $(T_m)$ is pointwise Cauchy (as $\lVert T_mx-T_{m'}x\rVert\le\lVert T_m-T_{m'}\rVert_{\mathrm{op}}\lVert x\rVert$), so $T_mx\to Tx$ for a limit map $T$, which is linear, bounded ($\lVert T\rVert\le\sup_m\lVert T_m\rVert<\infty$), and the operator-norm limit of $(T_m)$. The same holds for $\mathcal{L}(X) = \mathcal{L}(X,X)$. This is what lets us sum operator series.
> >
> > **Part (a).** Set $R := -L^{-1}H\in\mathcal{L}(X)$; then $\lVert R\rVert_{\mathrm{op}}\le\lVert L^{-1}\rVert_{\mathrm{op}}\lVert H\rVert_{\mathrm{op}} =: q < 1$ (hypothesis on $\lVert H\rVert$). The partial sums $S_m := \sum_{n=0}^m R^n$ form a Cauchy sequence in the complete space $\mathcal{L}(X)$, because for $m'>m$, $\lVert S_{m'}-S_m\rVert_{\mathrm{op}}\le\sum_{n=m+1}^{m'}\lVert R\rVert_{\mathrm{op}}^n\le\sum_{n>m}q^n\to 0$ (submultiplicativity $\lVert R^n\rVert\le\lVert R\rVert^n$ and the geometric tail). Let $S := \sum_{n\ge 0}R^n$ be their limit. Then
> > $$(\operatorname{id}-R)S = \lim_m(\operatorname{id}-R)S_m = \lim_m(\operatorname{id}-R^{m+1}) = \operatorname{id}\qquad(\lVert R^{m+1}\rVert\le q^{m+1}\to 0),$$
> > and likewise $S(\operatorname{id}-R) = \operatorname{id}$, so $\operatorname{id}-R = \operatorname{id}+L^{-1}H$ is invertible with inverse $S$. Since $L+H = L(\operatorname{id}+L^{-1}H)$ (expand: $L+LL^{-1}H = L+H$) is a composition of two isomorphisms, it is an isomorphism, and
> > $$(L+H)^{-1} = (\operatorname{id}+L^{-1}H)^{-1}L^{-1} = S\,L^{-1} = \sum_{n=0}^\infty(-L^{-1}H)^n L^{-1}.$$
> > The norm bound follows from $\lVert(L+H)^{-1}\rVert\le\lVert S\rVert\,\lVert L^{-1}\rVert\le\bigl(\sum_n q^n\bigr)\lVert L^{-1}\rVert = \lVert L^{-1}\rVert/(1-q)$.
> >
> > **Part (b), openness.** By part (a), the open ball of radius $1/\lVert L^{-1}\rVert_{\mathrm{op}}$ about $L$ in $\mathcal{L}(X,Y)$ consists of isomorphisms; hence $\operatorname{Iso}(X,Y)$ is open.
> >
> > **Part (b), differentiability.** Using the series with the $n=0$ and $n=1$ terms split off,
> > $$(L+H)^{-1}-L^{-1} = \sum_{n\ge 1}(-L^{-1}H)^n L^{-1} = -L^{-1}HL^{-1} + \underbrace{\sum_{n\ge 2}(-L^{-1}H)^nL^{-1}}_{=:E(H)}.$$
> > The remainder is bounded by $\lVert E(H)\rVert\le\sum_{n\ge 2}q^n\lVert L^{-1}\rVert = \lVert L^{-1}\rVert\,q^2/(1-q)$ with $q = \lVert L^{-1}\rVert\lVert H\rVert$, so $\lVert E(H)\rVert = O(\lVert H\rVert^2) = o(\lVert H\rVert)$ as $H\to 0$. The map $H\mapsto -L^{-1}HL^{-1}$ is bounded and linear in $H$, so it is the derivative: $d_L\iota(H) = -L^{-1}HL^{-1}$.
> >
> > **Part (b), $C^\infty$.** The derivative can be written $d_L\iota = -m\circ(\iota\times\iota)\circ\Delta$, where $\Delta(L) = (L,L)$ and $m(A,B)(H) = A H B$ is the bounded bilinear "sandwich" map, itself $C^\infty$ (a continuous bilinear map is smooth, with constant second derivative). Thus $d\iota$ is built by composition from $\iota$ (one order less differentiable a priori) and smooth maps. Inductively: $\iota$ is continuous by part (a) (the norm bound shows $\lVert(L+H)^{-1}-L^{-1}\rVert\to 0$), hence $d\iota = -m\circ(\iota\times\iota)\circ\Delta$ is continuous, so $\iota\in C^1$; if $\iota\in C^k$ then $d\iota$, a composition of $C^k$ maps, is $C^k$, so $\iota\in C^{k+1}$. Therefore $\iota\in C^\infty$. $\blacksquare$

> [!note]- Lemma 3: Local solution operator by contraction
> **Statement:** Let $X$, $Y$ be Banach spaces, $U\subseteq X$ open, $x_0\in U$, and $F\colon U\to Y$ of class $C^1$ with $L := d_{x_0}F$ a bounded linear isomorphism. Then there exist radii $r>0$ and $s>0$ such that:
> - $F$ is injective on the closed ball $\overline{B}_r(x_0)\subseteq U$, and $d_xF$ is an isomorphism for every $x\in\overline{B}_r(x_0)$;
> - for every $y\in B_s(F(x_0))$ there is a unique $g(y)\in\overline{B}_r(x_0)$ with $F(g(y)) = y$, and the resulting map $g\colon B_s(F(x_0))\to\overline{B}_r(x_0)$ is Lipschitz with constant $2\lVert L^{-1}\rVert_{\mathrm{op}}$.
>
> **Hint:** Reduce to $x_0=0$, $F(0)=0$, $L=\operatorname{id}$ by pre-composing with $L^{-1}$ and translating; then $\varphi := \operatorname{id}-F$ has $d_0\varphi = 0$, and $G_y := y+\varphi$ is a contraction on $\overline{B}_r$.
>
> **Why needed:** This is the existence-and-continuity core of part (i); differentiability and $C^k$-ness are added afterwards in the Formal Proof.
>
> > [!note]- Full proof
> > **Step 0 — reduction to the normalised case.** Define $\widetilde F\colon (U-x_0)\to X$ by $\widetilde F(u) := L^{-1}\bigl(F(x_0+u)-F(x_0)\bigr)$. Since $L^{-1}$ and the translations are $C^\infty$ diffeomorphisms (affine with bounded linear part, or bounded linear isomorphisms), $\widetilde F$ is $C^1$, and by the chain rule $d_0\widetilde F = L^{-1}\,d_{x_0}F = L^{-1}L = \operatorname{id}$, with $\widetilde F(0) = 0$. A conclusion for $\widetilde F$ near $0$ transfers to $F$ near $x_0$: $F(x) = y$ is equivalent to $\widetilde F(x-x_0) = L^{-1}(y-F(x_0))$, so a solution operator for $\widetilde F$ conjugates to one for $F$, with Lipschitz constants multiplied by the fixed factors $\lVert L^{-1}\rVert$ and $\lVert L\rVert$. We may therefore assume $x_0=0$, $F(0)=0$, and $L = d_0F = \operatorname{id}$, and afterwards restore $\lVert L^{-1}\rVert$ into the Lipschitz constant.
> >
> > **Step 1 — a contraction estimate for $\varphi := \operatorname{id}-F$.** The map $\varphi\colon U\to X$ is $C^1$ with $d_x\varphi = \operatorname{id}-d_xF$, so $d_0\varphi = \operatorname{id}-\operatorname{id} = 0$. Since $x\mapsto d_x\varphi$ is continuous ($F$ is $C^1$) and vanishes at $0$, choose $r>0$ with $\overline{B}_r(0)\subseteq U$ and
> > $$\lVert d_x\varphi\rVert_{\mathrm{op}} \le \tfrac12 \qquad\text{for all } x\in\overline{B}_r(0)\qquad\text{(continuity of the derivative at } 0\text{).}$$
> > As $\overline{B}_r(0)$ is convex, Lemma 1 gives, for all $x,x'\in\overline{B}_r(0)$,
> > $$\lVert\varphi(x)-\varphi(x')\rVert \le \tfrac12\lVert x-x'\rVert. \tag{$\ast$}$$
> >
> > **Step 2 — invertibility of $d_xF$ on the ball.** For $x\in\overline{B}_r(0)$, $d_xF = \operatorname{id}-d_x\varphi$ and $\lVert d_x\varphi\rVert_{\mathrm{op}}\le\tfrac12 < 1 = 1/\lVert\operatorname{id}^{-1}\rVert$, so by Lemma 2(a) (with $L=\operatorname{id}$, $H = -d_x\varphi$) $d_xF$ is an isomorphism, with $\lVert(d_xF)^{-1}\rVert_{\mathrm{op}}\le 1/(1-\tfrac12) = 2$.
> >
> > **Step 3 — the fixed-point map.** Put $s := r/2$. For $y\in B_s(0)$ define $G_y\colon\overline{B}_r(0)\to X$ by $G_y(x) := y + \varphi(x) = x - F(x) + y$; then $F(x) = y\iff G_y(x) = x$. First, $G_y$ maps $\overline{B}_r(0)$ into itself: using $\varphi(0) = 0-F(0) = 0$ and $(\ast)$,
> > $$\lVert G_y(x)\rVert \le \lVert y\rVert + \lVert\varphi(x)-\varphi(0)\rVert \le s + \tfrac12\lVert x\rVert \le \tfrac r2 + \tfrac r2 = r.$$
> > Second, $G_y$ is a contraction with constant $\tfrac12$: for $x,x'\in\overline{B}_r(0)$, $G_y(x)-G_y(x') = \varphi(x)-\varphi(x')$, so $\lVert G_y(x)-G_y(x')\rVert\le\tfrac12\lVert x-x'\rVert$ by $(\ast)$.
> >
> > **Step 4 — existence, uniqueness, continuity.** The closed ball $\overline{B}_r(0)$ is a closed subset of the Banach space $X$, hence a non-empty complete metric space in the induced metric. By the contraction mapping principle — restated: *a contraction of a non-empty complete metric space into itself has a unique fixed point* ([[Thm - The Contraction Mapping Principle]]) — $G_y$ has a unique fixed point $g(y)\in\overline{B}_r(0)$, that is, a unique $x\in\overline{B}_r(0)$ with $F(x) = y$. Injectivity of $F$ on $\overline{B}_r(0)$ is exactly this uniqueness. For Lipschitz continuity, let $y,y'\in B_s(0)$ with $x = g(y)$, $x' = g(y')$; then
> > $$\lVert x-x'\rVert = \lVert G_y(x)-G_{y'}(x')\rVert \le \lVert y-y'\rVert + \lVert\varphi(x)-\varphi(x')\rVert \le \lVert y-y'\rVert + \tfrac12\lVert x-x'\rVert,$$
> > so $\tfrac12\lVert x-x'\rVert\le\lVert y-y'\rVert$, i.e. $\lVert g(y)-g(y')\rVert\le 2\lVert y-y'\rVert$. Restoring the reduction of Step 0 multiplies this constant by $\lVert L^{-1}\rVert_{\mathrm{op}}$, giving Lipschitz constant $2\lVert L^{-1}\rVert_{\mathrm{op}}$. $\blacksquare$

> [!note]- Lemma 4: Finite-dimensional subspaces are complemented
> **Statement:** Let $X$ be a Banach space and $K\subseteq X$ a finite-dimensional subspace. Then $K$ is complemented: there is a bounded projection $P\in\mathcal{L}(X)$ with image $K$, and $X_1 := \ker P$ is a closed subspace with $X = K\oplus X_1$.
>
> **Hint:** Take a basis $e_1,\dots,e_m$ of $K$ with coordinate functionals $\lambda_i$ on $K$; extend each to a bounded functional on $X$ and set $P = \sum_i\lambda_i(\cdot)\,e_i$.
>
> **Why needed:** It makes the complementedness hypothesis of part (iii) automatic when $d_xF$ is a Fredholm operator, whose kernel is finite-dimensional; this is the parenthetical clause of the statement.
>
> > [!note]- Full proof
> > Let $e_1,\dots,e_m$ be a basis of the finite-dimensional space $K$. Define linear functionals $\lambda_i\colon K\to\mathbb{R}$ by $\lambda_i\bigl(\sum_j a_j e_j\bigr) = a_i$; on the finite-dimensional space $K$ every linear functional is continuous, so each $\lambda_i$ is bounded on $K$.
> >
> > **External input — the Hahn–Banach theorem.** By the Hahn–Banach theorem (a bounded linear functional on a subspace of a normed space extends to a bounded linear functional on the whole space with the same norm), each $\lambda_i$ extends to some $\Lambda_i\in X^*$ with $\Lambda_i|_K = \lambda_i$; in particular $\Lambda_i(e_j) = \delta_{ij}$.
> >
> > **The projection.** Define $P\colon X\to X$ by $Px := \sum_{i=1}^m\Lambda_i(x)\,e_i$. It is linear and bounded ($\lVert Px\rVert\le\sum_i\lVert\Lambda_i\rVert_{X^*}\lVert e_i\rVert\,\lVert x\rVert$), its image lies in $K$, and for $x = \sum_j a_j e_j\in K$ we compute $Px = \sum_i\Lambda_i(x)e_i = \sum_i a_i e_i = x$, so $P$ fixes $K$ pointwise; hence $P^2 = P$ (as $Px\in K$) and $\operatorname{im}P = K$. Then $X_1 := \ker P$ is closed ($P$ continuous), and every $x$ decomposes uniquely as $x = Px + (x-Px)$ with $Px\in K$ and $x-Px\in\ker P$ (since $P(x-Px) = Px-P^2x = 0$); uniqueness holds because $K\cap X_1 = 0$ ($x\in K$ gives $Px = x$, and $x\in X_1$ gives $Px = 0$). Thus $X = K\oplus X_1$ with bounded projections $P$ and $\operatorname{id}-P$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> We prove the three parts in order; parts (ii) and (iii) reduce to part (i).
>
> ## Part (i) — the inverse function theorem
>
> Let $F\colon U\to Y$ be $C^k$ ($k\ge 1$) with $L := d_{x_0}F$ a bounded linear isomorphism.
>
> **Step 1 — local bijection with continuous inverse.** By Lemma 3 there are $r,s>0$ such that $F$ is injective on $\overline{B}_r(x_0)$, each $d_xF$ ($x\in\overline{B}_r(x_0)$) is an isomorphism, and every $y\in B_s(F(x_0))$ has a unique preimage $g(y)\in\overline{B}_r(x_0)$, with $g$ Lipschitz. Set
> $$V' := B_s(F(x_0)),\qquad U' := F^{-1}(V')\cap B_r(x_0).$$
> Then $V'$ is open and $U'$ is open ($F$ continuous, $B_r(x_0)$ open). For $y\in V'$ we have $g(y)\in\overline{B}_r(x_0)$ with $F(g(y)) = y\in V'$; thus $g(y)\in F^{-1}(V')$, and in fact $g(y)\in B_r(x_0)$ (an interior point, since $\lVert g(y)-x_0\rVert$ is controlled: were $g(y)$ on the boundary sphere one shrinks $s$ so that $g(B_s)\subseteq B_r$, which the Lipschitz bound $\lVert g(y)-x_0\rVert = \lVert g(y)-g(F(x_0))\rVert\le 2\lVert L^{-1}\rVert\lVert y-F(x_0)\rVert < 2\lVert L^{-1}\rVert s$ secures after replacing $s$ by $\min(s, r/(4\lVert L^{-1}\rVert))$). Hence $g(y)\in U'$, so $F\colon U'\to V'$ is surjective; it is injective as a restriction of the injective $F|_{\overline{B}_r(x_0)}$. Therefore $F\colon U'\to V'$ is a continuous bijection with continuous inverse $g = (F|_{U'})^{-1}$: a homeomorphism.
>
> **Step 2 — the inverse is differentiable.** Fix $y\in V'$ and $x := g(y)\in U'$; by Step 1 (via Lemma 3, Step 2) $A := d_xF$ is an isomorphism. Let $k\in Y$ be small enough that $y+k\in V'$, put $x' := g(y+k)$ and $h := x'-x$. The Lipschitz bound gives $\lVert h\rVert\le 2\lVert L^{-1}\rVert\,\lVert k\rVert$, so $h\to 0$ as $k\to 0$. By differentiability of $F$ at $x$,
> $$k = F(x')-F(x) = A h + R,\qquad \lVert R\rVert = o(\lVert h\rVert)\quad(h\to 0).$$
> Apply $A^{-1}$: $h = A^{-1}k - A^{-1}R$. Now $\lVert A^{-1}R\rVert\le\lVert A^{-1}\rVert\,o(\lVert h\rVert) = o(\lVert h\rVert) = o(\lVert k\rVert)$, the last equality because $\lVert h\rVert\le 2\lVert L^{-1}\rVert\lVert k\rVert$. Therefore
> $$g(y+k)-g(y) = h = A^{-1}k + o(\lVert k\rVert),$$
> which says $g$ is differentiable at $y$ with $d_yg = A^{-1} = (d_{g(y)}F)^{-1}$.
>
> **Step 3 — the inverse is $C^k$.** The derivative of $g$ is the composite
> $$d_yg = \iota\bigl(d_{g(y)}F\bigr),\qquad\text{i.e.}\qquad dg = \iota\circ (dF)\circ g,$$
> where $dF\colon U'\to\operatorname{Iso}(X,Y)$, $x\mapsto d_xF$, and $\iota$ is operator inversion. We bootstrap. The map $g$ is continuous (Step 1); $dF$ is continuous ($F$ is $C^1$, and $k\ge 1$); $\iota$ is $C^\infty$, in particular continuous (Lemma 2(b)). Hence $dg = \iota\circ dF\circ g$ is continuous, so $g\in C^1$. Inductively, suppose $F\in C^k$ and we have shown $g\in C^j$ for some $1\le j<k$. Then $dF\in C^{k-1}\subseteq C^{j}$ (since $j\le k-1$), $g\in C^j$, and $\iota\in C^\infty$, so the composite $dg = \iota\circ dF\circ g$ is $C^{j}$; therefore $g\in C^{j+1}$. Iterating from $j=1$ up to $j = k-1$ yields $g\in C^k$. Thus $F\colon U'\to V'$ is a $C^k$ diffeomorphism, completing part (i). $\square$
>
> ## Part (ii) — the implicit function theorem
>
> Let $F\colon W\to Y$ be $C^k$ with $F(a,b)=0$ and $\partial_2F(a,b)$ an isomorphism.
>
> **Step 1 — the graph map.** Define $\Phi\colon W\to X_1\times Y$ by $\Phi(x_1,x_2) := (x_1, F(x_1,x_2))$. It is $C^k$ (its components are $C^k$), $\Phi(a,b) = (a,0)$, and its derivative at $(a,b)$ is
> $$d_{(a,b)}\Phi(h_1,h_2) = \bigl(h_1,\ \partial_1F(a,b)h_1 + \partial_2F(a,b)h_2\bigr).$$
>
> **Step 2 — $d_{(a,b)}\Phi$ is an isomorphism.** Write $P := \partial_1F(a,b)\in\mathcal{L}(X_1,Y)$ and $Q := \partial_2F(a,b)\in\mathcal{L}(X_2,Y)$, with $Q$ an isomorphism by hypothesis. The map $T(h_1,h_2) = (h_1, Ph_1 + Qh_2)$ is bounded and linear; it is bijective with bounded inverse
> $$T^{-1}(u,v) = \bigl(u,\ Q^{-1}(v - Pu)\bigr),$$
> as the two compositions verify: $T\,T^{-1}(u,v) = T\bigl(u,Q^{-1}(v-Pu)\bigr) = \bigl(u, Pu + Q Q^{-1}(v-Pu)\bigr) = (u,v)$, and $T^{-1}T(h_1,h_2) = T^{-1}\bigl(h_1, Ph_1+Qh_2\bigr) = \bigl(h_1, Q^{-1}(Ph_1+Qh_2-Ph_1)\bigr) = (h_1,h_2)$. Both $T$ and $T^{-1}$ are bounded (built from the bounded maps $P$, $Q$, $Q^{-1}$), so $T = d_{(a,b)}\Phi$ is an isomorphism.
>
> **Step 3 — invert $\Phi$ and read off the graph.** By part (i), $\Phi$ restricts to a $C^k$ diffeomorphism from an open $W_0\ni(a,b)$ onto an open neighbourhood of $(a,0)$; choose open $a\in A\subseteq X_1$ and $b\in B\subseteq X_2$ with $A\times B\subseteq W_0$ and $A\times\{0\}\subseteq\Phi(W_0)$ (shrinking $A$). Because $\Phi$ preserves the first coordinate, its inverse has the form $\Phi^{-1}(x_1,z) = (x_1,\psi(x_1,z))$ for a $C^k$ map $\psi$ (the second component of the $C^k$ map $\Phi^{-1}$). Define $g\colon A\to X_2$ by $g(x_1) := \psi(x_1,0)$, a $C^k$ map; from $\Phi(a,b) = (a,0)$ we get $\Phi^{-1}(a,0) = (a,b)$, so $\psi(a,0) = b$, i.e. $g(a) = b$. After shrinking $A$ we may assume $g(A)\subseteq B$. Now for $(x_1,x_2)\in A\times B\subseteq W_0$,
> $$F(x_1,x_2) = 0 \iff \Phi(x_1,x_2) = (x_1,0) \iff (x_1,x_2) = \Phi^{-1}(x_1,0) = (x_1,\psi(x_1,0)) \iff x_2 = g(x_1),$$
> each step using that $\Phi$ is a bijection on $W_0$. So the zero set of $F$ in $A\times B$ is exactly the graph of $g$.
>
> **Step 4 — the derivative of $g$.** Differentiate the identity $F(x_1,g(x_1)) = 0$ at $x_1 = a$ by the chain rule: $\partial_1F(a,b) + \partial_2F(a,b)\,d_ag = 0$, whence $d_ag = -\bigl(\partial_2F(a,b)\bigr)^{-1}\partial_1F(a,b)$. This completes part (ii). $\square$
>
> ## Part (iii) — the regular-value / local-submersion theorem
>
> Let $F\colon X\to Y$ be $C^k$ between Banach manifolds, $y$ a regular value, and fix $x\in F^{-1}(y)$ with $\ker d_xF$ complemented. We produce a chart of $X$ near $x$ carrying $F^{-1}(y)$ onto an open piece of a closed complemented subspace; since $x$ is arbitrary this gives the submanifold structure and the tangent space, and $x$ was arbitrary in $F^{-1}(y)$.
>
> **Step 0 — pass to charts.** Choose a chart of $X$ about $x$ and of $Y$ about $y$, so that (renaming) $X$, $Y$ are Banach spaces (the model spaces), $x = 0$, $y = 0$, and $F\colon\mathcal{O}\to Y$ is $C^k$ on an open $\mathcal{O}\ni 0$ with $F(0)=0$; the derivative $d_0F\colon X\to Y$ is the chart representative of $d_xF$, hence surjective (regular value) with complemented kernel. Being a chart, an embedded-submanifold statement in these coordinates is exactly the required statement for $F^{-1}(y)$ near $x$.
>
> **Step 1 — split the domain and identify the invertible block.** Write $K := \ker d_0F$ and pick a closed complement $X_1$ with $X = K\oplus X_1$ and bounded projections (the complementedness hypothesis). Let $T := d_0F|_{X_1}\colon X_1\to Y$. Then:
> - $T$ is injective, since $X_1\cap K = 0$ and $K = \ker d_0F$;
> - $T$ is surjective, since $d_0F(X) = d_0F(K) + d_0F(X_1) = 0 + T(X_1)$ and $d_0F$ is surjective (regular value).
>
> So $T$ is a bounded linear bijection between the Banach spaces $X_1$ and $Y$. **By the bounded inverse theorem** — restated: *a bounded linear bijection between Banach spaces has bounded inverse*, the immediate corollary of the open mapping theorem ([[Thm - Banach–Steinhaus and Open Mapping (Application of Baire)]]) obtained by noting the theorem makes such a map open, hence its inverse continuous — $T$ is an isomorphism.
>
> **Step 2 — the straightening map.** Writing points of $X = K\oplus X_1$ as $(u,v)$ with $u\in K$, $v\in X_1$, define
> $$H\colon \mathcal{O}\to K\times Y,\qquad H(u,v) := \bigl(u,\ F(u,v)\bigr).$$
> Then $H$ is $C^k$, $H(0,0) = (0,0)$, and its derivative at $0$ is
> $$d_0H(a,b) = \bigl(a,\ d_0F(a,b)\bigr) = \bigl(a,\ d_0F|_K\,a + d_0F|_{X_1}\,b\bigr) = (a,\ Tb)\qquad(a\in K,\ b\in X_1),$$
> using $d_0F|_K = 0$ (as $K = \ker d_0F$). The map $(a,b)\mapsto(a,Tb)$ is an isomorphism $K\times X_1\to K\times Y$ (its inverse is $(a,c)\mapsto(a,T^{-1}c)$, bounded because $T^{-1}$ is bounded by Step 1). Hence $d_0H$ is a bounded linear isomorphism.
>
> **Step 3 — apply part (i).** By part (i), $H$ restricts to a $C^k$ diffeomorphism from an open $\mathcal{O}'\ni 0$ in $X = K\oplus X_1$ onto an open $\mathcal{N}\ni 0$ in $K\times Y$. In these straightened coordinates the level set is a slice: for $(u,v)\in\mathcal{O}'$,
> $$F(u,v) = 0 \iff H(u,v)\in K\times\{0\} \iff H(u,v)\in\mathcal{N}\cap(K\times\{0\}),$$
> the first equivalence because the second component of $H$ is $F$, the second because $H(u,v)\in\mathcal{N}$ already. Therefore $H$ carries $F^{-1}(0)\cap\mathcal{O}'$ homeomorphically onto the relatively open piece $\mathcal{N}\cap(K\times\{0\})$ of the closed subspace $K\times\{0\}$ of $K\times Y$. Composing the chart of Step 0 with the $C^k$ diffeomorphism $H$ yields a chart of $X$ about $x$ in which $F^{-1}(y)$ is an open subset of the closed complemented subspace corresponding to $K$ (it is complemented in $X$ by hypothesis, and $K\times\{0\}$ is complemented in $K\times Y$ by $\{0\}\times Y$). By the definition of an embedded submanifold ([[Def - Banach Manifold and Smooth Maps between Banach Spaces]], [[Def - Embedded Submanifold]]), $F^{-1}(y)$ is a $C^k$ embedded submanifold near $x$, modelled on $K = \ker d_xF$.
>
> **Step 4 — the tangent space.** The submanifold is $H^{-1}\bigl(K\times\{0\}\bigr)$ near $0$, so its tangent space at $0$ is the preimage of $K\times\{0\}$ under the isomorphism $d_0H$:
> $$T_0\,F^{-1}(0) = (d_0H)^{-1}\bigl(K\times\{0\}\bigr) = \{(a,b)\in K\times X_1 : (a,Tb)\in K\times\{0\}\} = \{(a,b) : Tb = 0\} = K\times\{0\},$$
> because $T$ is injective. Read back through the chart, $K\times\{0\}$ is $K = \ker d_xF$. Hence $T_xF^{-1}(y) = \ker d_xF$.
>
> **Step 5 — the Fredholm case.** If each $d_xF$ is a Fredholm operator, then $\ker d_xF$ is finite-dimensional, hence complemented by Lemma 4; so the complementedness hypothesis is automatic and the conclusion holds unconditionally for Fredholm $F$ at a regular value.
>
> Combining Steps 0–5 over all $x\in F^{-1}(y)$: $F^{-1}(y)$ is a $C^k$ embedded submanifold of $X$ with $T_xF^{-1}(y) = \ker d_xF$ at every point. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Nonlinear ordinary differential equations and the flow map.** Consider the map sending an initial condition and a time to the solution of $\dot x = V(x)$, realised as a fixed point of the Picard integral operator on the Banach space $C^0([0,T];\mathbb{R}^n)$. The linearisation of the "residual" map $x(\cdot)\mapsto x(\cdot) - x_0 - \int_0^{\cdot}V(x)$ in the direction of the unknown path is $\operatorname{id}$ minus a Volterra operator, which is an isomorphism by the Neumann series (Lemma 2). Part (ii) then exhibits the solution as a $C^k$ function of the initial data — smooth dependence on initial conditions — with the theorem applying because the phase space is finite-dimensional but the *path space* is not. The point of the exercise is to see that the natural setting is infinite-dimensional even for a finite-dimensional dynamical system.

**Bifurcation from a simple eigenvalue.** Let $F(u,\mu) = 0$ describe an equilibrium of a parameter-dependent nonlinear equation, with $\partial_uF(0,\mu_0)$ Fredholm of index $0$ and a one-dimensional kernel. Part (ii) fails exactly because $\partial_uF$ is not an isomorphism there; the Lyapunov–Schmidt reduction — which is the **[[Thm - Kuranishi Model for a Fredholm Map|Kuranishi model]]** — splits off the invertible block by part (i) and reduces to a scalar bifurcation equation on the kernel. The exercise is to recognise that the *failure* of the implicit function theorem is precisely what makes bifurcation possible, and that part (i) still does the infinite-dimensional work.

**The Nash–Moser boundary and why $C^\infty$ is not Banach.** On the Fréchet space $C^\infty(M)$ the inverse function theorem *fails* — there are smooth maps with invertible linearisation and no local inverse — because the operator inversion of Lemma 2 loses derivatives and no fixed Banach norm controls the iteration. The exercise is to locate exactly which step of the present proof breaks on a Fréchet space (completeness of the metric survives, but the derivative bound and the Neumann series do not close on a single norm), motivating the Sobolev-space formulation used throughout this chapter, where every space is Banach (indeed Hilbert) and the theorem holds.

---

# Bridges

- **[[Thm - Kuranishi Model for a Fredholm Map|Kuranishi model for a Fredholm map]].** This is the principal client of part (i). Given a Fredholm map $F$ with $F(p) = 0$, split $X = \ker d_pF\oplus X_1$ and $Y = \operatorname{im}d_pF\oplus Y_1$ with $\dim\ker d_pF,\dim Y_1<\infty$. The block $d_pF|_{X_1}\colon X_1\to\operatorname{im}d_pF$ is a bounded bijection, hence an isomorphism (bounded inverse theorem), so the map $x\mapsto(\pi_{\ker}(x-p), \pi_{\operatorname{im}}F(x))$ has invertible linearisation at $p$; part (i) inverts it, and in the new coordinates $F$ becomes $Tx_1 + f(x_0,x_1)$ with $f$ valued in the finite-dimensional $Y_1$. The infinite-dimensional problem has become the finite-dimensional equation $f_0 = 0$ on the kernel.

- **[[Thm - Regular Value and Transversality Theorems for Fredholm Maps|Regular value and transversality theorems for Fredholm maps]].** Part (iii) is the special case in which the cokernel is trivial (regular value); the general regular-value theorem for Fredholm maps adds only the observation that the model dimension $\dim\ker d_xF$ equals the (locally constant) index, so $F^{-1}(y)$ is a manifold of dimension $\operatorname{index} F$. Transversality to a finite-dimensional submanifold $Z$ is reduced to this by composing $F$ with a local defining submersion of $Z$.

- **[[Thm - The Degree Count is Locally Constant on Regular Values|Local constancy of the degree count]].** For a proper index-zero Fredholm map, at a regular value $y$ each preimage point $x_j$ has $d_{x_j}F$ a Fredholm isomorphism (index $0$ plus surjective forces injective), so part (i) gives a local diffeomorphism $F\colon V_j\to U_j$; properness then confines the whole preimage of a small $U\subseteq\bigcap_jU_j$ to $\bigsqcup_jV_j$, and the preimage count is constant on $U$. This is the mechanism that makes the **[[Def - Mod-2 Degree of a Proper Fredholm Map|mod-2 degree]]** well defined.

- **[[Thm - The Inverse Function Theorem|Finite-dimensional inverse function theorem]] and [[Thm - The Implicit Function Theorem|its implicit form]].** The finite-dimensional statements are the case $X = Y = \mathbb{R}^n$: there every linear bijection is automatically an isomorphism and every subspace is complemented, so the hypotheses simplify, but the proof — reduce to $d = \operatorname{id}$, contract, differentiate the inverse, bootstrap — is the same argument. The present theorem is the recognition that only completeness and an explicit bounded-inverse hypothesis were ever used.

---

# Unlocked by This

> [!tip] The bounded inverse theorem as a working tool *(from Functional Analysis)*
> Part (iii) uses, and this page restates, the fact that a bounded linear bijection between Banach spaces is automatically an isomorphism. Once available, it turns the analytically awkward hypothesis "the linearisation is an isomorphism" into the checkable pair "bounded, injective, surjective", which is how the hypothesis is verified in every application in this chapter. See **[[Thm - Banach–Steinhaus and Open Mapping (Application of Baire)]]**.

> [!tip] Smoothness of moduli spaces *(from Gauge Theory)*
> Part (iii), applied to the defining map of a moduli problem at a regular value, is exactly the statement that the moduli space is a smooth manifold of dimension equal to the index of the linearised operator. This is the template for the smoothness of the Seiberg–Witten moduli space in chapter XI, where the parameter must be chosen generically (by **[[Thm - Sard-Smale Theorem|Sard–Smale]]**) precisely to make the value regular.
