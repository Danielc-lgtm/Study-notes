---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Fredholm Map and Its Index"
  - "Thm - Inverse Function Theorem on Banach Spaces"
  - "Def - Fredholm Operator and Index"
  - "Thm - Closed Range is Automatic for Finite-Dimensional Cokernel"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $X$ and $Y$ are real Banach spaces, that is, complete normed vector spaces over $\mathbb{R}$; $\lVert\cdot\rVert$ denotes the norm on whichever space is in view, and $\operatorname{Hom}(X,Y)$ is the space of bounded (equivalently, continuous) linear maps $X\to Y$ with the operator norm. A map $F\colon U\to Y$ defined on an open set $U\subseteq X$ is *smooth* ($C^\infty$) in the sense of the Banach-space calculus of **[[Def - Banach Manifold and Smooth Maps between Banach Spaces|the Banach differential calculus]]**: it is Fréchet differentiable at each point, its differential $d_xF\in\operatorname{Hom}(X,Y)$ depends continuously on $x$, and this persists for all higher differentials. We write $d_xF$ for the differential of $F$ at $x$; for a linear map $L$ we have $d_xL=L$ at every $x$.

A bounded linear map $L\colon X\to Y$ is a **[[Def - Fredholm Operator and Index|Fredholm operator]]** if its kernel $\ker L:=\{x\in X:Lx=0\}$ is finite-dimensional, its image $\operatorname{Im}L:=\{Lx:x\in X\}$ is closed, and its cokernel $\operatorname{coker}L:=Y/\operatorname{Im}L$ is finite-dimensional; its **index** is $\operatorname{index}L:=\dim\ker L-\dim\operatorname{coker}L\in\mathbb{Z}$. A smooth map $F$ is a **[[Def - Fredholm Map and Its Index|Fredholm map]]** if $d_xF$ is a Fredholm operator for every $x$; on a connected domain $\operatorname{index}d_xF$ is independent of $x$ and is written $\operatorname{index}F$.

For a closed subspace $A\subseteq Z$ of a Banach space $Z$, a *closed complement* is a closed subspace $B\subseteq Z$ with $A\cap B=\{0\}$ and $A+B=Z$; we then write $Z=A\oplus B$ and call the linear map $\pi_A\colon Z\to A$ sending $a+b\mapsto a$ (for $a\in A$, $b\in B$) the *projection onto $A$ along $B$*. The point $p\in X$ is a fixed zero of $F$, $F(p)=0$, and we abbreviate the linearisation there by $L:=d_pF\colon X\to Y$. We set $X_0:=\ker L$ and $Y_0:=\operatorname{Im}L$; a chosen closed complement of $X_0$ is called $X_1$, and a chosen closed complement of $Y_0$ is called $Y_1$, so that $X=X_0\oplus X_1$ and $Y=Y_0\oplus Y_1$. The associated projections are $\pi_{X_0}\colon X\to X_0$, $\pi_{X_1}\colon X\to X_1$, $\pi_{Y_0}\colon Y\to Y_0$, $\pi_{Y_1}\colon Y\to Y_1$. The symbol $T:=L|_{X_1}\colon X_1\to Y_0$ denotes the restriction of $L$ to $X_1$, regarded as a map into $Y_0$.

> [!warning] Convention: sign and register
> This page follows the series convention that "smooth" means $C^\infty$ throughout, and that a **[[Def - Fredholm Operator and Index|Fredholm operator]]** is defined by finite-dimensional kernel, closed image, and finite-dimensional cokernel. Haydys (Introduction to Gauge Theory, Theorem 162) states the Kuranishi model without the normalisations $f(0)=0$ and $d_0f=0$ and omits the proof; we add both normalisations — they hold automatically for the construction below and are what later chapters use — and supply the complete Lyapunov–Schmidt proof, following Donaldson–Kronheimer, *The Geometry of Four-Manifolds*, §4.2.5.

---

# Statement

> **Theorem (Kuranishi model for a Fredholm map).** Let $X$ and $Y$ be Banach spaces, let $F\colon X\to Y$ be a smooth Fredholm map, and let $p\in F^{-1}(0)$. Write $L:=d_pF$, $X_0:=\ker L$, $Y_0:=\operatorname{Im}L$, and choose closed complements
> $$X=X_0\oplus X_1,\qquad Y=Y_0\oplus Y_1,\qquad \dim X_0<\infty,\quad \dim Y_1<\infty.$$
> Then the restriction $T:=L|_{X_1}\colon X_1\to Y_0$ is a bounded linear isomorphism, and there exist an open neighbourhood $V$ of $0$ in $X=X_0\oplus X_1$, a smooth diffeomorphism $\phi\colon V\to\phi(V)$ onto an open neighbourhood of $p$ with $\phi(0)=p$, and a smooth map
> $$f\colon V\to Y_1,\qquad f(0)=0,\quad d_0f=0,$$
> such that, writing a point of $V$ as $(x_0,x_1)\in X_0\oplus X_1$,
> $$F\big(\phi(x_0,x_1)\big)=Tx_1+f(x_0,x_1)\qquad\text{for all }(x_0,x_1)\in V. \tag{$\ast$}$$
>
> **In particular**, set $f_0\colon X_0\to Y_1$, $f_0(x_0):=f(x_0,0)$. Then $\phi$ restricts to a homeomorphism from a neighbourhood of $0$ in the zero set $f_0^{-1}(0)\subseteq X_0$ onto a neighbourhood of $p$ in $F^{-1}(0)$. Here $X_0$ and $Y_1$ are finite-dimensional, with $\dim X_0=\dim\ker L$ and $\dim Y_1=\dim\operatorname{coker}L$, so the local structure of $F^{-1}(0)$ near $p$ is captured by the single finite-dimensional equation $f_0(x_0)=0$ for $\dim\ker L$ unknowns valued in a $\dim\operatorname{coker}L$-dimensional space.

The map $f_0$ (equivalently, the pair $(X_0,Y_1,f_0)$) is the **Kuranishi model** of $F$ at $p$; the neighbourhoods on which $\phi$ and $f$ are defined can always be shrunk without disturbing $(\ast)$.

---

# Motivation

Gauge theory studies solution sets of nonlinear partial differential equations — the anti-self-dual Yang–Mills equations, the Seiberg–Witten equations — reorganised as zero sets $F^{-1}(0)$ of a smooth map $F\colon X\to Y$ between infinite-dimensional Banach (or Hilbert) spaces of sections. The single geometric fact one wants about such a zero set is its *local shape*: near a given solution $p$, is $F^{-1}(0)$ a smooth manifold, and of what dimension? When the linearisation $L=d_pF$ is surjective the answer is immediate from the **[[Thm - Inverse Function Theorem on Banach Spaces|implicit function theorem on Banach spaces]]**, and $F^{-1}(0)$ is a smooth manifold of dimension $\operatorname{index}F$. But at the solutions that matter most — reducible connections, points of higher symmetry, the singularities that carry the topological information — $L$ fails to be surjective, and the implicit function theorem says nothing.

The Kuranishi model is the tool that governs exactly this failing case. It says that a Fredholm map, near any zero, looks in suitable coordinates like a linear isomorphism in most directions plus a genuinely nonlinear correction confined to the finitely many directions where the linearisation misbehaves. The isomorphic part can be solved away once and for all by the inverse function theorem; what is left is a finite-dimensional map $f_0\colon X_0\to Y_1$ between a space of dimension $\dim\ker L$ (the *deformations*) and a space of dimension $\dim\operatorname{coker}L$ (the *obstructions*), whose zero set is locally homeomorphic to $F^{-1}(0)$. An infinite-dimensional problem about the zero set of $F$ has been reduced, without any loss of information near $p$, to a finite-dimensional problem about the zero set of $f_0$.

The alternative, without this reduction, would be to work with $F^{-1}(0)$ as an abstract subset of an infinite-dimensional space, where none of the finite-dimensional tools — Sard's theorem, degree theory, the intersection-theoretic count of points — is available; Lebesgue measure and "almost every point" have no meaning there. The Kuranishi model is precisely what re-imports those tools: it is the technical heart behind the **[[Thm - Regular Value and Transversality Theorems for Fredholm Maps|regular-value theorem for Fredholm maps]]**, the **[[Thm - Sard-Smale Theorem|Sard–Smale theorem]]**, and the degree theory that follows, and it is the standard description of the local structure of moduli spaces near non-regular points in Seiberg–Witten and Donaldson theory.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's stated hypothesis is that $F$ is a Fredholm map — that every $d_xF$ has finite-dimensional kernel and cokernel and closed range. In practice this hypothesis is almost never verified by hand from the definition; it arrives disguised, and recognising the disguise is the working skill.

The first disguised source is **an elliptic differential operator plus a lower-order nonlinearity**. If $L_0$ is a linear elliptic operator on a closed manifold and $N$ is a nonlinear term of strictly lower order, then $F(u)=L_0u+N(u)$, read between the right Sobolev completions, has each differential $d_uF=L_0+(\text{lower order})$, and the lower-order piece is *compact* by the **[[Thm - Rellich Compactness Theorem|Rellich compactness theorem]]**. The bridge is that $L_0$ is Fredholm by **[[Thm - Elliptic Operators on Closed Manifolds are Fredholm|elliptic Fredholm theory]]** and the Fredholm property is stable under compact perturbations, so $F$ is a Fredholm map without any direct estimate on $F$ itself. *Example problem:* show that $F(u)=\Delta u+u^3$ on a closed surface is a Fredholm map of index $0$ between Sobolev spaces, and read off that its zero set near any solution has a Kuranishi model with $X_0=\ker(\Delta+3u^2)$.

The second disguised source is **a map whose linearisation is a bounded isomorphism up to finite rank**. If at some point $d_pF=A+K$ with $A$ invertible and $K$ of finite rank, then $d_pF$ is Fredholm of index $0$; more generally any invertible-plus-compact linearisation is Fredholm of index $0$. The bridge is Atkinson's characterisation of Fredholm operators (a bounded operator is Fredholm exactly when it is invertible modulo compacts), so one need only exhibit an approximate inverse, not compute kernel and cokernel. *Example problem:* recognise that a boundary-value operator of the form "invertible principal part plus trace terms" is Fredholm, hence has a Kuranishi model at every zero.

The third disguised source is **a finite-dimensional smooth map**, which is the degenerate but instructive case. Every smooth map $F\colon\mathbb{R}^m\to\mathbb{R}^n$ has $d_xF$ automatically Fredholm — kernel and cokernel are finite-dimensional because the whole spaces are — of index $m-n$. The bridge is that finite dimensionality forces the Fredholm property for free, so the Kuranishi model specialises to the classical normal form of a smooth map near a critical point, and one can test every clause of the theorem on a concrete polynomial. *Example problem:* for $F(x,y)=xy$ at the origin, exhibit $X_0,X_1,Y_0,Y_1$, $\phi$, and $f_0$ explicitly and confirm that $f_0(x_0)$ is the quadratic whose zero set is the crossing pair of lines (worked out on **[[Ex - Kuranishi Models in the Plane|the plane exercises page]]**).

**Targets (Output Amplification)**

The bare conclusion is a local normal form $(\ast)$. Combined with further inputs it yields the structural theorems of the chapter.

Combine the Kuranishi model with **surjectivity of $L=d_pF$ at every zero**. Then $Y_0=\operatorname{Im}L=Y$, so the complement $Y_1=\{0\}$, so $f\equiv 0$ and $f_0\equiv 0$; the zero set $f_0^{-1}(0)$ is all of a neighbourhood of $0$ in $X_0$. The extra ingredient — regularity of the value $0$ — collapses the model to a chart, and the payoff is the **[[Thm - Regular Value and Transversality Theorems for Fredholm Maps|regular-value theorem]]**: $F^{-1}(0)$ is a smooth manifold of dimension $\dim X_0=\operatorname{index}F$. This is the single most-used consequence of the theorem.

Combine the Kuranishi model with **Sard's theorem applied slice by slice**. In a Kuranishi chart, the critical values of $F$ are controlled by the finite-dimensional map $f_0$ (more precisely by $x_0\mapsto f(x_0,\cdot)$), so the finite-dimensional **[[Thm - Sard's Theorem for Smooth Maps|Sard theorem]]** applies in each chart. The extra ingredient is local properness, which turns "measure zero in every slice" into "closed with empty interior"; the payoff is the **[[Thm - Sard-Smale Theorem|Sard–Smale theorem]]**, that the regular values of a Fredholm map are residual, hence dense.

Combine the Kuranishi model with **an equivariant symmetry group at $p$**. When a compact group $\Gamma$ fixes $p$ and commutes with $F$, the splitting $X=X_0\oplus X_1$, $Y=Y_0\oplus Y_1$ can be taken $\Gamma$-invariant, so $f_0\colon X_0\to Y_1$ is an equivariant map between finite-dimensional representations. The extra ingredient is the invariant splitting; the payoff is the local model of a moduli space near a symmetric (for example reducible) solution as $f_0^{-1}(0)/\Gamma$ — the cone structure that drives Donaldson's theorem and the description of the Seiberg–Witten moduli space near reducibles.

---

# Why Is It True

Picture the differential $L=d_pF$ acting on the Banach space $X$. It has a finite-dimensional kernel $X_0$ — the directions it kills — and its image misses a finite-dimensional slice $Y_1$ — the directions it cannot reach. On the complementary directions $X_1$, however, $L$ is as good as invertible: it maps $X_1$ bijectively and boundedly onto its image $Y_0$, so on $X_1$ the map $F$ is, to first order, a linear isomorphism onto $Y_0$. The inverse function theorem is exactly the statement that a smooth map whose linearisation is a bounded isomorphism can be inverted near the point; the difficulty is only that here $L$ is invertible on part of the space, not all of it.

The trick is to *enlarge* the map so that its linearisation becomes invertible on the whole space, invert that, and then restrict back. Alongside $F$ we remember the $X_0$-coordinate of the input: we form $\Phi(x)=\big(\pi_{X_0}x,\ \pi_{Y_0}F(p+x)\big)$, which records where we are in the kernel directions and what $F$ does in the reachable directions. Its linearisation at $0$ is $(v_0,v_1)\mapsto(v_0,Tv_1)$, and this *is* invertible on all of $X$: the identity on $X_0$, and $T$ on $X_1$. So the inverse function theorem straightens $\Phi$ into a coordinate map. Undoing $\Phi$ and reading off the remaining $Y_1$-coordinate of $F$ leaves exactly one thing uncontrolled — a smooth map $f$ into the finite-dimensional space $Y_1$ — and the reachable part of $F$ has become the honest linear isomorphism $Tx_1$.

> **The mechanism in one sentence:** solve the equation in the directions where the linearisation is invertible by the inverse function theorem, and what remains is a finite-dimensional equation on the kernel $X_0$ with values in the cokernel $Y_1$.

Once $(\ast)$ holds, the "in particular" is bookkeeping in a direct sum. A point $\phi(x_0,x_1)$ is a zero of $F$ exactly when $Tx_1+f(x_0,x_1)=0$; but $Tx_1$ lives in $Y_0$ and $f(x_0,x_1)$ lives in the complement $Y_1$, and the only way an element of $Y_0$ plus an element of $Y_1$ can vanish is for both to vanish. Since $T$ is injective, $Tx_1=0$ forces $x_1=0$, and then the surviving condition is $f(x_0,0)=f_0(x_0)=0$. So $F^{-1}(0)$ near $p$ is, after the change of coordinates $\phi$, exactly the zero set of $f_0$ inside the finite-dimensional kernel $X_0$. The infinite-dimensional directions have been spent entirely on making $\phi$ a diffeomorphism; all of the surviving geometry sits in $f_0$.

---

# What Makes This Hard

The one genuinely non-trivial input is that $T=L|_{X_1}\colon X_1\to Y_0$ is a *topological* isomorphism, not merely a bijection: its algebraic inverse must be bounded, since the inverse function theorem needs a bounded linearisation to invert. This is where completeness enters and where the Fredholm hypothesis does real work — one needs $Y_0=\operatorname{Im}L$ to be *closed* (so that it is itself a Banach space) and then the open mapping theorem to upgrade the bounded bijection $T$ to a homeomorphism; skipping the closedness of the range is the standard gap, and it is exactly the point Haydys omits. The second, subtler trap is to confuse the two decompositions: $x_1=0$ (a statement in $X$) is forced by $Tx_1=0$ only because $T$ is *injective*, while $f(x_0,x_1)=0$ separates from $Tx_1=0$ only because $Y=Y_0\oplus Y_1$ is a *direct* sum; conflating "the sum vanishes" with "each summand vanishes" in a space that is not a direct sum would break the reduction.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Enlarge $F$ to a map $\Phi$ whose linearisation at $0$ is invertible on all of $X$, invert $\Phi$ by the inverse function theorem to get a chart $\phi$, and define $f$ as the leftover $Y_1$-component of $F\circ\phi$. Then check the normal form $(\ast)$, the normalisations $f(0)=0$, $d_0f=0$, and finally decode the zero set in the direct sum.

**Subgoal decomposition:**

1. **$T$ is a bounded linear isomorphism $X_1\to Y_0$.**
   - *Hint:* $\ker T=X_0\cap X_1=\{0\}$ gives injectivity; $\operatorname{Im}L=L(X_1)$ (because $L$ kills $X_0$) gives surjectivity onto $Y_0$; $Y_0$ is closed hence Banach, so the open mapping theorem makes $T^{-1}$ bounded.
   - *Why needed:* Without $T$ an isomorphism, $\Phi$ has no invertible linearisation and the inverse function theorem does not apply.

2. **The projections are bounded.**
   - *Hint:* For a Banach space split into two closed complementary subspaces, the map "external direct sum $\to$ space, $(a,b)\mapsto a+b$" is a bounded bijection; invert it by the open mapping theorem.
   - *Why needed:* $\Phi$ and $f$ are built from the projections; they must be smooth, which for a linear map means bounded.

3. **$\Phi(x):=(\pi_{X_0}x,\pi_{Y_0}F(p+x))$ is smooth with $d_0\Phi=(v_0,v_1)\mapsto(v_0,Tv_1)$, an isomorphism.**
   - *Hint:* Differentiate: the first slot is linear, the second is $\pi_{Y_0}\circ L$; evaluate on $v=v_0+v_1$ and use $Lv_0=0$, $Lv_1=Tv_1\in Y_0$.
   - *Why needed:* This is the hypothesis of the inverse function theorem for $\Phi$.

4. **Produce $\phi$ and $f$; verify $(\ast)$.**
   - *Hint:* Let $\Psi=\Phi^{-1}$ near $0$; set $\phi(x_0,x_1):=p+\Psi(x_0,Tx_1)$ and $f:=\pi_{Y_1}\circ F\circ\phi$; the definition of $\Phi$ gives $\pi_{Y_0}F(\phi(x_0,x_1))=Tx_1$, and adding the $Y_1$-part gives $(\ast)$.
   - *Why needed:* This is the normal form itself.

5. **$f(0)=0$ and $d_0f=0$.**
   - *Hint:* $f(0)=\pi_{Y_1}F(p)=0$; and $d_0f=\pi_{Y_1}\circ L\circ d_0\phi$ with $d_0\phi=\operatorname{id}$, while $\pi_{Y_1}|_{\operatorname{Im}L}=0$.
   - *Why needed:* These normalisations are used by the regular-value theorem and by later chapters.

6. **Decode $F^{-1}(0)$ near $p$.**
   - *Hint:* $Tx_1+f\in Y_0\oplus Y_1$ vanishes iff $Tx_1=0$ and $f=0$; injectivity of $T$ gives $x_1=0$; the survivor is $f_0(x_0)=0$.
   - *Why needed:* This is the "in particular" and the whole point.

---

# Lemma Decomposition

> [!note]- Lemma 1: The restriction $T=L|_{X_1}$ is a bounded linear isomorphism onto $Y_0$
> **Statement:** With $L=d_pF$ a Fredholm operator, $X_0=\ker L$, $X=X_0\oplus X_1$ (closed complement), and $Y_0=\operatorname{Im}L$, the map $T\colon X_1\to Y_0$, $T:=L|_{X_1}$, is a well-defined bounded linear bijection, and its inverse $T^{-1}\colon Y_0\to X_1$ is bounded.
>
> **Hint:** Injectivity from $X_0\cap X_1=\{0\}$; surjectivity from $L(X)=L(X_1)$; boundedness of the inverse from closedness of $Y_0$ and the open mapping theorem.
>
> **Why needed:** It supplies the bounded isomorphism on which the inverse function theorem for $\Phi$ rests, and it is the exact place where the Fredholm hypothesis (closed range) is spent.
>
> > [!note]- Full proof
> > We must show four things: $T$ maps $X_1$ into $Y_0$; $T$ is injective; $T$ is surjective onto $Y_0$; and $T^{-1}$ is bounded.
> >
> > **$T$ is well-defined into $Y_0$ and bounded.** For $x_1\in X_1$ we have $Tx_1=Lx_1\in\operatorname{Im}L=Y_0$, so $T$ takes values in $Y_0$. It is linear as a restriction of the linear map $L$, and bounded because $\lVert Tx_1\rVert=\lVert Lx_1\rVert\le\lVert L\rVert\,\lVert x_1\rVert$ (the operator-norm bound for $L$), where $\lVert L\rVert$ is finite since $L=d_pF$ is a bounded operator.
> >
> > **$T$ is injective.** Suppose $Tx_1=0$ for some $x_1\in X_1$. Then $Lx_1=0$, so $x_1\in\ker L=X_0$. Thus $x_1\in X_0\cap X_1$, and since $X=X_0\oplus X_1$ is a direct sum we have $X_0\cap X_1=\{0\}$ (by the definition of a closed complement), so $x_1=0$. Hence $\ker T=\{0\}$.
> >
> > **$T$ is surjective onto $Y_0$.** Let $y\in Y_0=\operatorname{Im}L$, so $y=Lx$ for some $x\in X$. Write $x=x_0+x_1$ with $x_0\in X_0$, $x_1\in X_1$ (unique by the direct-sum decomposition). Then, since $x_0\in\ker L$,
> > $$y=Lx=Lx_0+Lx_1=0+Lx_1=Tx_1\qquad(\text{because }x_0\in\ker L\text{ and }x_1\in X_1),$$
> > so $y\in\operatorname{Im}T$. Hence $T$ is onto $Y_0$.
> >
> > **$T^{-1}$ is bounded.** By the **[[Thm - Closed Range is Automatic for Finite-Dimensional Cokernel|closed-range theorem]]** — a bounded linear operator between Banach spaces with finite-dimensional kernel and finite-dimensional cokernel has closed image — the image $Y_0=\operatorname{Im}L$ is a closed subspace of the Banach space $Y$; a closed subspace of a complete space is complete, so $Y_0$ is itself a Banach space. Likewise $X_1$, being a closed complement, is a closed subspace of the Banach space $X$, hence a Banach space. Thus $T\colon X_1\to Y_0$ is a bounded linear bijection between Banach spaces. By the **[[Thm - Banach–Steinhaus and Open Mapping (Application of Baire)|open mapping theorem]]** — a surjective bounded linear map between Banach spaces is open, so a bounded linear bijection between Banach spaces has a bounded inverse — the inverse $T^{-1}\colon Y_0\to X_1$ is bounded. Therefore $T$ is a topological isomorphism. $\blacksquare$

> [!note]- Lemma 2: Projections onto closed complementary subspaces are bounded
> **Statement:** Let $Z$ be a Banach space with $Z=A\oplus B$ for closed subspaces $A,B$. Then the projection $P\colon Z\to A$ onto $A$ along $B$, defined by $P(a+b)=a$ for $a\in A$, $b\in B$, is a bounded linear map; likewise the complementary projection $\operatorname{id}-P$ onto $B$ is bounded.
>
> **Hint:** The external direct sum $A\oplus B$ (with norm $\lVert(a,b)\rVert=\lVert a\rVert+\lVert b\rVert$) is a Banach space; the summation map to $Z$ is a bounded bijection; invert it by the open mapping theorem.
>
> **Why needed:** The map $\Phi$ and the leftover $f$ are assembled from $\pi_{X_0},\pi_{Y_0},\pi_{Y_1}$; smoothness of $\Phi$ and $f$ requires these projections to be bounded (a linear map is smooth exactly when it is bounded).
>
> > [!note]- Full proof
> > **Step 0 — the external direct sum is Banach.** Since $A$ and $B$ are closed subspaces of the complete space $Z$, each is complete, hence a Banach space. Form the external direct sum $A\times B$ with the norm $\lVert(a,b)\rVert:=\lVert a\rVert+\lVert b\rVert$; a product of two Banach spaces with this norm is complete (a Cauchy sequence in $A\times B$ is Cauchy in each coordinate, and the coordinatewise limits assemble to a limit in $A\times B$), so $A\times B$ is a Banach space.
> >
> > **Step 1 — the summation map is a bounded bijection.** Define $S\colon A\times B\to Z$ by $S(a,b)=a+b$. It is linear, and bounded because
> > $$\lVert S(a,b)\rVert=\lVert a+b\rVert\le\lVert a\rVert+\lVert b\rVert=\lVert(a,b)\rVert\qquad(\text{triangle inequality}).$$
> > It is surjective because $Z=A+B$ (every $z\in Z$ is $a+b$ for some $a\in A$, $b\in B$), and injective because $A\cap B=\{0\}$ forces the decomposition to be unique: if $a+b=a'+b'$ then $a-a'=b'-b\in A\cap B=\{0\}$, so $a=a'$ and $b=b'$.
> >
> > **Step 2 — invert.** By the **[[Thm - Banach–Steinhaus and Open Mapping (Application of Baire)|open mapping theorem]]**, the bounded linear bijection $S$ between the Banach spaces $A\times B$ and $Z$ has a bounded inverse $S^{-1}\colon Z\to A\times B$, $S^{-1}(z)=(Pz,(\operatorname{id}-P)z)$. The coordinate projections $\operatorname{pr}_A\colon A\times B\to A$ and $\operatorname{pr}_B\colon A\times B\to B$ are bounded ($\lVert\operatorname{pr}_A(a,b)\rVert=\lVert a\rVert\le\lVert a\rVert+\lVert b\rVert=\lVert(a,b)\rVert$, and $\lVert\operatorname{pr}_B(a,b)\rVert=\lVert b\rVert\le\lVert a\rVert+\lVert b\rVert=\lVert(a,b)\rVert$). Therefore $P=\operatorname{pr}_A\circ S^{-1}$ and $\operatorname{id}-P=\operatorname{pr}_B\circ S^{-1}$ are compositions of bounded maps, hence bounded. $\blacksquare$

> [!note]- Lemma 3: The enlarged map $\Phi$ is smooth with invertible linearisation at $0$
> **Statement:** Define $\Phi$ on a neighbourhood of $0$ in $X$ by $\Phi(x):=\big(\pi_{X_0}x,\ \pi_{Y_0}F(p+x)\big)\in X_0\oplus Y_0$. Then $\Phi$ is smooth, $\Phi(0)=0$, and its differential at $0$ is $d_0\Phi(v)=\big(\pi_{X_0}v,\ Tv_1\big)$ where $v=v_0+v_1$ with $v_1=\pi_{X_1}v$; this is a bounded linear isomorphism $X_0\oplus X_1\to X_0\oplus Y_0$ with inverse $(w_0,w_1)\mapsto\big(w_0,T^{-1}w_1\big)$.
>
> **Hint:** Differentiate slotwise; in the second slot the chain rule gives $\pi_{Y_0}\circ d_pF=\pi_{Y_0}\circ L$; evaluate on $v_0+v_1$ using $Lv_0=0$ and $Lv_1\in Y_0$.
>
> **Why needed:** It verifies the hypotheses of the inverse function theorem for $\Phi$, which is what produces the chart $\phi$.
>
> > [!note]- Full proof
> > **Smoothness.** The map $x\mapsto p+x$ is a smooth (affine) map $X\to X$; $F$ is smooth by hypothesis; and $\pi_{X_0}$, $\pi_{Y_0}$ are bounded linear maps, hence smooth, by Lemma 2. The target $X_0\oplus Y_0$ is the finite-times-Banach product of two Banach spaces, and a map into a product is smooth exactly when each component is smooth. The first component $x\mapsto\pi_{X_0}x$ is bounded linear, hence smooth; the second component $x\mapsto\pi_{Y_0}F(p+x)$ is a composition of smooth maps, hence smooth. Therefore $\Phi$ is smooth. Also $\Phi(0)=\big(\pi_{X_0}(0),\pi_{Y_0}F(p)\big)=(0,\pi_{Y_0}(0))=(0,0)$ since $F(p)=0$.
> >
> > **The differential at $0$.** By the chain rule and linearity of the projections,
> > $$d_0\Phi(v)=\big(\pi_{X_0}v,\ \pi_{Y_0}\,d_pF(v)\big)=\big(\pi_{X_0}v,\ \pi_{Y_0}Lv\big)\qquad(\text{chain rule; }d_p(x\mapsto p+x)=\operatorname{id}).$$
> > Write $v=v_0+v_1$ with $v_0=\pi_{X_0}v\in X_0$, $v_1=\pi_{X_1}v\in X_1$. Then $Lv=Lv_0+Lv_1=0+Lv_1$ (since $v_0\in\ker L$), and $Lv_1=Tv_1\in Y_0$, so $\pi_{Y_0}Lv=\pi_{Y_0}(Tv_1)=Tv_1$ (because $Tv_1\in Y_0$ and $\pi_{Y_0}$ restricts to the identity on $Y_0$). Hence
> > $$d_0\Phi(v)=(v_0,\ Tv_1).$$
> >
> > **Invertibility.** The map $J\colon X_0\oplus X_1\to X_0\oplus Y_0$, $J(v_0,v_1)=(v_0,Tv_1)$, is bounded (each slot is bounded: the identity on $X_0$ and $T$ on $X_1$). It is a bijection with inverse $J^{-1}(w_0,w_1)=(w_0,T^{-1}w_1)$: indeed $J^{-1}J(v_0,v_1)=(v_0,T^{-1}Tv_1)=(v_0,v_1)$ and $JJ^{-1}(w_0,w_1)=(w_0,TT^{-1}w_1)=(w_0,w_1)$, using that $T$ is a bijection with two-sided inverse $T^{-1}$ (Lemma 1). The inverse $J^{-1}$ is bounded because $T^{-1}$ is bounded (Lemma 1). Therefore $d_0\Phi=J$ is a bounded linear isomorphism. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> We are given Banach spaces $X,Y$, a smooth Fredholm map $F\colon X\to Y$, a point $p\in F^{-1}(0)$, the linearisation $L=d_pF$, the splittings $X=X_0\oplus X_1$ and $Y=Y_0\oplus Y_1$ with $X_0=\ker L$, $Y_0=\operatorname{Im}L$, $\dim X_0<\infty$, $\dim Y_1<\infty$. We must construct $\phi$, $T$, $f$ satisfying $(\ast)$ with $f(0)=0$, $d_0f=0$, and establish the local homeomorphism of zero sets. We write $\pi_{X_0},\pi_{X_1},\pi_{Y_0},\pi_{Y_1}$ for the projections of the two splittings.
>
> **Step 0 — preconditions.** The complements $X_1,Y_1$ are closed by hypothesis, so all four projections are bounded linear maps (Lemma 2). Since $L$ is Fredholm, its image $Y_0=\operatorname{Im}L$ is closed (**[[Thm - Closed Range is Automatic for Finite-Dimensional Cokernel|closed-range theorem]]**: a bounded operator with finite-dimensional kernel and cokernel has closed range), so $Y_0$ is a Banach space; and $\dim Y_1=\dim(Y/Y_0)=\dim\operatorname{coker}L<\infty$, $\dim X_0=\dim\ker L<\infty$, as required for the finite-dimensionality claims at the end. By Lemma 1 the restriction $T:=L|_{X_1}\colon X_1\to Y_0$ is a bounded linear isomorphism; this is the isomorphism named in the statement.
>
> **Step 1 — the enlarged map and its inverse.** Define, on a neighbourhood of $0$ in $X$,
> $$\Phi(x):=\big(\pi_{X_0}x,\ \pi_{Y_0}F(p+x)\big)\in X_0\oplus Y_0.$$
> By Lemma 3, $\Phi$ is smooth, $\Phi(0)=0$, and $d_0\Phi(v_0,v_1)=(v_0,Tv_1)$ is a bounded linear isomorphism $X_0\oplus X_1\to X_0\oplus Y_0$. By the **[[Thm - Inverse Function Theorem on Banach Spaces|inverse function theorem on Banach spaces]]** — a smooth map between Banach spaces whose differential at a point is a bounded linear isomorphism restricts to a smooth diffeomorphism between neighbourhoods of that point and its image — there are open neighbourhoods $U'$ of $0$ in $X$ and $W$ of $0$ in $X_0\oplus Y_0$ such that $\Phi\colon U'\to W$ is a smooth diffeomorphism. Write $\Psi:=(\Phi|_{U'})^{-1}\colon W\to U'$; it is smooth with $\Psi(0)=0$.
>
> **Step 2 — the chart $\phi$.** The map $J\colon X_0\oplus X_1\to X_0\oplus Y_0$, $J(x_0,x_1)=(x_0,Tx_1)$, is a bounded linear isomorphism (Step 0 and Lemma 3). Let $V:=J^{-1}(W)$, an open neighbourhood of $0$ in $X=X_0\oplus X_1$, and define
> $$\phi\colon V\to X,\qquad \phi(x_0,x_1):=p+\Psi\big(J(x_0,x_1)\big)=p+\Psi(x_0,Tx_1).$$
> As a composition of the linear isomorphism $J$, the diffeomorphism $\Psi$, and the translation by $p$, the map $\phi$ is a smooth diffeomorphism from $V$ onto the open neighbourhood $p+U'$ of $p$, and $\phi(0)=p+\Psi(0)=p+0=p$.
>
> **Step 3 — the normal form $(\ast)$.** Fix $(x_0,x_1)\in V$ and put $x:=\Psi(x_0,Tx_1)\in U'$, so that $\phi(x_0,x_1)=p+x$ and, applying $\Phi$ and using $\Phi\circ\Psi=\operatorname{id}$ on $W$,
> $$\Phi(x)=(x_0,Tx_1).$$
> By the definition of $\Phi$, the two coordinates of $\Phi(x)$ are $\pi_{X_0}x$ and $\pi_{Y_0}F(p+x)$; comparing second coordinates,
> $$\pi_{Y_0}F\big(\phi(x_0,x_1)\big)=\pi_{Y_0}F(p+x)=Tx_1\qquad(\text{second coordinate of }\Phi(x)=(x_0,Tx_1)).$$
> Now define $f\colon V\to Y_1$ by $f(x_0,x_1):=\pi_{Y_1}F\big(\phi(x_0,x_1)\big)$; it is smooth as a composition of smooth maps ($\phi$, $F$, and the bounded projection $\pi_{Y_1}$). Decomposing $F(\phi(x_0,x_1))\in Y=Y_0\oplus Y_1$ into its two projections,
> $$F\big(\phi(x_0,x_1)\big)=\pi_{Y_0}F\big(\phi(x_0,x_1)\big)+\pi_{Y_1}F\big(\phi(x_0,x_1)\big)=Tx_1+f(x_0,x_1)\qquad(\text{by the previous display and the definition of }f),$$
> which is exactly $(\ast)$.
>
> **Step 4 — the normalisations $f(0)=0$ and $d_0f=0$.** For the value: $f(0)=\pi_{Y_1}F(\phi(0))=\pi_{Y_1}F(p)=\pi_{Y_1}(0)=0$ (since $\phi(0)=p$ and $F(p)=0$). For the differential, first note $d_0\phi=\operatorname{id}_X$: from Step 2, $d_0\phi(v)=d_0\Psi\big(J v\big)=(d_0\Phi)^{-1}(Jv)$ (the differential of the inverse is the inverse of the differential, by the inverse function theorem), and since $d_0\Phi=J$ (Lemma 3) we get $d_0\phi(v)=J^{-1}Jv=v$. Then, by the chain rule,
> $$d_0f=d_0\big(\pi_{Y_1}\circ F\circ\phi\big)=\pi_{Y_1}\circ d_pF\circ d_0\phi=\pi_{Y_1}\circ L\circ\operatorname{id}=\pi_{Y_1}\circ L\qquad(\text{chain rule; }d_{\phi(0)}F=d_pF=L;\ d_0\phi=\operatorname{id}).$$
> For any $v\in X$ we have $Lv\in\operatorname{Im}L=Y_0$, and $\pi_{Y_1}|_{Y_0}=0$ (because $Y_0\cap Y_1=\{0\}$ and $\pi_{Y_1}$ is the projection along $Y_0$), so $\pi_{Y_1}Lv=0$. Hence $d_0f=0$.
>
> **Step 5 — the zero set near $p$.** Because $\phi\colon V\to p+U'$ is a bijection, the zeros of $F$ in $p+U'$ correspond bijectively, via $\phi$, to the solutions in $V$ of $F(\phi(x_0,x_1))=0$. By $(\ast)$ this equation reads
> $$Tx_1+f(x_0,x_1)=0.$$
> Here $Tx_1\in Y_0$ and $f(x_0,x_1)\in Y_1$, and $Y=Y_0\oplus Y_1$ is a direct sum, so an element of $Y_0$ plus an element of $Y_1$ equals $0$ only when each summand is $0$: the equation is equivalent to the pair
> $$Tx_1=0\quad\text{and}\quad f(x_0,x_1)=0.$$
> Since $T$ is injective (Lemma 1), $Tx_1=0$ is equivalent to $x_1=0$. Substituting $x_1=0$ into the second equation leaves $f(x_0,0)=f_0(x_0)=0$. Therefore
> $$\{(x_0,x_1)\in V:F(\phi(x_0,x_1))=0\}=\{(x_0,0)\in V:f_0(x_0)=0\},$$
> the graph over $\{x_1=0\}$ of the zero set of $f_0$. The map $x_0\mapsto(x_0,0)$ is a homeomorphism from a neighbourhood of $0$ in $X_0$ onto $V\cap(X_0\oplus\{0\})$, and $\phi$ is a homeomorphism (being a diffeomorphism), so their composition restricts to a homeomorphism
> $$\{x_0\in X_0:f_0(x_0)=0\}\cap(\text{nbhd of }0)\ \xrightarrow{\ x_0\mapsto\phi(x_0,0)\ }\ F^{-1}(0)\cap(\text{nbhd of }p).$$
> Finally $X_0$ and $Y_1$ are finite-dimensional with $\dim X_0=\dim\ker L$ and $\dim Y_1=\dim\operatorname{coker}L$ (Step 0), so $f_0\colon X_0\to Y_1$ is a smooth map between finite-dimensional spaces and its zero set is the promised finite-dimensional model of $F^{-1}(0)$ near $p$.
>
> This constructs $\phi$, $T$, and $f$ with all the stated properties and establishes the local homeomorphism of zero sets. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Bifurcation theory and the Lyapunov–Schmidt reduction.** In the study of bifurcations of solutions to a parameter-dependent equation $G(u,\lambda)=0$, one linearises at a solution where the operator $d_uG$ develops a kernel and reduces the full problem to a finite-dimensional *bifurcation equation* on that kernel. This is exactly the Kuranishi model applied to $F(u)=G(u,\lambda)$ at fixed $\lambda$: $X_0$ is the kernel of the linearisation, $Y_1$ the cokernel, and $f_0$ the bifurcation function whose zeros encode how solution branches split. The theorem applies because the operators of applied bifurcation theory (elliptic, or compact perturbations of invertible ones) are Fredholm; what is non-obvious is that the reduction is *canonical* near the point — the shape of the branching is intrinsic to $f_0$, not an artefact of the reduction chosen.

**Deformation theory and moduli of complex structures.** The local model of a moduli space of geometric structures — complex structures on a fixed manifold, holomorphic vector bundles, instantons — is a Kuranishi space: a finite-dimensional map $f_0\colon H^1\to H^2$ between cohomology groups of a deformation complex, with $H^1$ the infinitesimal deformations and $H^2$ the obstructions. The theorem applies because the deformation operator is elliptic, hence Fredholm, with $X_0\cong H^1$ and $Y_1\cong H^2$. The non-obvious content is that the *quadratic part* of $f_0$ is the primary obstruction (the bracket $H^1\times H^1\to H^2$), so the local geometry of the moduli space is read off from a cup-product pairing.

**Finite-dimensional critical-point normal forms.** For a smooth function $g\colon\mathbb{R}^m\to\mathbb{R}$ with a critical point at the origin, apply the Kuranishi model to $F=\nabla g\colon\mathbb{R}^m\to\mathbb{R}^m$ at $0$. Here $X_0=\ker\operatorname{Hess}g(0)$ is the *degenerate* subspace and $Y_1$ its image complement, and the reduction is the Morse–Bott splitting lemma: the non-degenerate directions are removed by a diffeomorphism, leaving a function on the kernel whose Hessian vanishes. The theorem applies trivially (finite dimensions force the Fredholm property), and the point is that even in the classical setting the Kuranishi reduction *is* the splitting lemma, so the infinite-dimensional and finite-dimensional normal-form theories are one theorem.

---

# Bridges

- **[[Thm - Regular Value and Transversality Theorems for Fredholm Maps|Regular-value theorem for Fredholm maps]].** When $0$ is a regular value of $F$, that is $L=d_pF$ is surjective at every $p\in F^{-1}(0)$, the cokernel vanishes, so $Y_0=Y$ and the complement $Y_1=\{0\}$. Then $f\colon V\to Y_1=\{0\}$ is the zero map, so $f_0\equiv 0$ and its zero set is a full neighbourhood of $0$ in $X_0$. The Kuranishi homeomorphism then says $F^{-1}(0)$ is locally homeomorphic — in fact diffeomorphic, since $\phi$ is smooth and $f$ is absent — to an open set of the finite-dimensional space $X_0$ of dimension $\dim\ker L=\operatorname{index}F$. This is precisely how the regular-value theorem is proved from this page.

- **[[Thm - Sard-Smale Theorem|Sard–Smale theorem]].** The Kuranishi model $F\circ\phi(x_0,x_1)=Tx_1+f(x_0,x_1)$ presents $F$ locally as an isomorphism $T$ in the $X_1$-directions plus a map $f$ whose behaviour is governed by finitely many variables. The critical values of $F$ in the chart are therefore controlled by a finite-dimensional map, to which the ordinary Sard theorem applies slice by slice; combined with the local properness that the same model supplies, this yields the density (indeed residuality) of regular values. The Kuranishi model is the reduction step that makes an infinite-dimensional Sard theorem possible at all.

- **[[Def - Regular Value and Transversality for Fredholm Maps|Transversality to a finite-dimensional submanifold]].** For a finite-dimensional embedded submanifold $Z\subseteq Y$, transversality $F\pitchfork Z$ reduces, by cutting $Z$ out locally as the zero set of a submersion $g$, to $0$ being a regular value of $g\circ F$; the Kuranishi model of $g\circ F$ then gives the local manifold structure and the dimension count $\dim F^{-1}(Z)=\operatorname{index}F+\dim Z$. The single normal form on this page thus underlies both the regular-value and the transversal-preimage statements.

- **Local model of a moduli space near a reducible point.** In gauge theory the zero set $F^{-1}(0)$ is quotiented by a symmetry group, and near a fixed point $p$ of a subgroup $\Gamma$ one takes $\Gamma$-invariant splittings $X=X_0\oplus X_1$, $Y=Y_0\oplus Y_1$. The Kuranishi map $f_0\colon X_0\to Y_1$ is then $\Gamma$-equivariant, and the local moduli space is $f_0^{-1}(0)/\Gamma$ — a cone when $f_0$ is homogeneous. This construction, resting entirely on the theorem of this page, produces the cone-on-$\mathbb{CP}^2$ neighbourhoods of reducibles that drive Donaldson's diagonalisation and the description of the Seiberg–Witten moduli space near reducibles.

---

# Unlocked by This

> [!tip] Kuranishi space of a deformation problem *(from Deformation Theory)*
> A deformation problem with elliptic deformation complex has a local moduli space modelled on $f_0^{-1}(0)$ for a finite-dimensional $f_0\colon H^1\to H^2$, the *Kuranishi space*; its expected dimension is $\dim H^1-\dim H^2=\operatorname{index}$. See **Def - Deformation Complex and Its Cohomology**.

> [!tip] Obstruction bundle and the virtual count *(from Gauge Theory and Enumerative Geometry)*
> When the cokernel $Y_1$ does not vanish, the finite-dimensional data $(X_0,Y_1,f_0)$ organise into a section $f_0$ of a rank-$\dim Y_1$ *obstruction bundle* over $X_0$; integrating its Euler class defines the virtual count that replaces a naive point count when the moduli space is not cut out transversally. See **Def - Obstruction Bundle**.
