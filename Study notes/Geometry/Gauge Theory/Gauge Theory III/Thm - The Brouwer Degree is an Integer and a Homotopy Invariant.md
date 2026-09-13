---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Brouwer Degree of a Map"
  - "Thm - The Top de Rham Cohomology of a Closed Connected Oriented Manifold is R"
  - "Thm - Sard's Theorem when the Source Dimension does not Exceed the Target Dimension"
  - "Thm - Change of Variables for Integration on Manifolds"
  - "Thm - Homotopy Invariance of de Rham Cohomology"
  - "Thm - Stokes' Theorem on Manifolds"
tags: [geometry, gauge-theory, differential-topology, degree-theory]
---

# Notation

Throughout, all manifolds are smooth, Hausdorff, and second countable, and "smooth" means $C^\infty$. A manifold is **closed** when it is compact and has empty boundary. An **orientation** of an $n$-manifold is a choice of nowhere-vanishing top-degree form up to multiplication by a positive smooth function, or equivalently a coherent choice of ordered basis of each tangent space (the convention of [[Def - Orientation of a Smooth Manifold|the orientation of a smooth manifold]]); $\int_M\alpha$ denotes the integral of a compactly supported $n$-form $\alpha$ over the oriented $n$-manifold $M$, in the sense of [[Thm - Integration is Well-Defined on Oriented Manifolds|the well-defined integral on oriented manifolds]].

We write $M$ and $N$ for closed oriented $n$-manifolds, with $N$ connected, and $f\colon M\to N$ for a smooth map. The space of smooth $p$-forms on $M$ is $\Omega^p(M)$, and $f^*\colon\Omega^p(N)\to\Omega^p(M)$ is the pullback. The differential of $f$ at a point $x\in M$ is the linear map $df_x\colon T_xM\to T_{f(x)}N$. A point $y\in N$ is a [[Def - Regular and Critical Points|regular value]] of $f$ when $df_x$ is surjective for every $x\in f^{-1}(y)$; since $\dim M=\dim N=n$, surjectivity of $df_x$ is the same as $df_x$ being a linear isomorphism. For such an isomorphism between the oriented spaces $T_xM$ and $T_yN$ we set
$$\operatorname{sign}\det df_x=\begin{cases}+1,&df_x\text{ carries the orientation of }T_xM\text{ to that of }T_yN,\\-1,&df_x\text{ reverses it,}\end{cases}$$
which in any pair of positively oriented local coordinates is the sign of the determinant of the Jacobian matrix of $f$ at $x$.

The [[Def - Brouwer Degree of a Map|Brouwer degree]] of $f$ is $\deg f:=\int_Mf^*\omega$ for any $\omega\in\Omega^n(N)$ with $\int_N\omega=1$; that this is well posed is part (a) below. A top-degree form on an $n$-manifold is automatically closed, since $\Omega^{n+1}$ vanishes; we use this repeatedly without further comment. The de Rham cohomology $H^n_{dR}(N)$ and its integration pairing are those of [[Def - de Rham Cohomology|de Rham cohomology]]. The full symbol registry for the chapter is on [[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles]].

> [!warning] Convention: normalisation of the degree
> We follow [[Def - Brouwer Degree of a Map|the definition of the Brouwer degree]] in normalising by $\int_N\omega=1$, so that $\deg f=\int_Mf^*\omega$ directly. Some authors (Milnor) instead fix a volume form and divide, $\deg f=\int_Mf^*\mu\big/\int_N\mu$; the two agree, since $\mu\big/\int_N\mu$ is a normalised form. In part (f) the orientation of the boundary $M=\partial W$ is the induced one of [[Def - Manifold with Boundary and Induced Orientation|the manifold-with-boundary and induced-orientation convention]] (outward normal first).

---

# Statement

> **Theorem (the Brouwer degree is an integer and a homotopy invariant).** Let $M$ and $N$ be closed oriented $n$-manifolds with $N$ connected, and let $f\colon M\to N$ be smooth. Let $\deg f=\int_Mf^*\omega$ for a form $\omega\in\Omega^n(N)$ with $\int_N\omega=1$. Then:
> - **(a) Independence of $\omega$.** The number $\deg f$ does not depend on the choice of normalised $\omega$; it depends only on $f$.
> - **(b) The regular-value formula, and integrality.** For every regular value $y\in N$ of $f$, the preimage $f^{-1}(y)$ is finite and
> $$\deg f=\sum_{x\in f^{-1}(y)}\operatorname{sign}\det df_x .$$
> In particular $\deg f\in\mathbb Z$, and the right-hand side is the same integer for every regular value $y$.
> - **(c) Homotopy invariance.** If $f_0,f_1\colon M\to N$ are smoothly homotopic, then $\deg f_0=\deg f_1$.
> - **(d) Nonzero degree forces surjectivity.** If $\deg f\ne0$, then $f$ is surjective.
> - **(e) Multiplicativity.** If $P$ is a further closed connected oriented $n$-manifold and $g\colon N\to P$ is smooth, then $\deg(g\circ f)=\deg g\cdot\deg f$.
> - **(f) Bounding maps have degree zero.** If $M=\partial W$ for a compact oriented $(n+1)$-manifold $W$ (with $M$ carrying the induced boundary orientation) and $f$ extends to a smooth map $F\colon W\to N$, then $\deg f=0$.
> - **(g) Additivity over components.** If $M$ is disconnected, with connected components $M_1,\dots,M_r$ (finitely many, as $M$ is compact), then $\deg f=\sum_{j=1}^r\deg(f|_{M_j})$.

The theorem re-proves in full, under the vault's Proof Standard, the homotopy-invariance and integrality statements that the definition page defers; it is the page that all later uses of the degree in this series invoke.

---

# Motivation

The degree of a map $f\colon M\to N$ is defined analytically, as a single real number $\int_Mf^*\omega$. Read naively, that number could be anything: it is an integral of a smooth density, and integrals of smooth densities are generically irrational, sensitive to the integrand, and unstable under deformation. The content of this theorem is that this particular integral does none of those things. It is an integer; it does not see which normalised form $\omega$ we integrate; it does not change when $f$ is deformed continuously; and it can be read off by the crudest possible geometric measurement — count the points over one generic value of $f$, attach a sign to each, and add. The theorem is the bridge between the analytic definition (good for proofs, functorial, coordinate-free) and the geometric meaning (good for computation and for intuition).

Each clause earns its place in the applications that motivate the section. Integrality (b) is what lets the degree count things — sheets of a covering, roots of a polynomial, times a transition function winds. Homotopy invariance (c) is what makes it an invariant at all: a quantity that survives every smooth deformation of $f$ separates homotopy classes and cannot be destroyed by any construction that only deforms the data. Surjectivity from nonvanishing degree (d) is the mechanism behind every "there must be a solution" argument, from the fundamental theorem of algebra to the existence of preimages of a prescribed value. Multiplicativity (e) turns the degree into a homomorphism-like bookkeeping device under composition, which is exactly what is needed to compute the degree of an iterated or factored map. The bounding criterion (f) is the obstruction statement: a map that extends over a filling has degree zero, so a nonzero degree certifies that no filling exists. These are the properties the classification of $SU(2)$-bundles, the hairy-ball theorem, and the quantisation of the instanton number in later chapters will use, each by name.

The smallest case to hold in mind is $M=N=S^1$. A smooth map $f\colon S^1\to S^1$ is, up to homotopy, $\theta\mapsto k\theta$ for a unique integer $k$, and $\deg f=k$ is its winding number: how many times the image circle runs around the target circle. Every clause of the theorem is visible there. The winding number is an integer (b); it does not change as the loop is deformed (c); a loop of nonzero winding number must hit every point of the target (d); winding numbers add under composition of covering maps (e); and a loop that bounds a disc — that extends to a map of the disc — has winding number zero (f). The theorem is the statement that this entire picture survives verbatim in every dimension and for every closed oriented target.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypothesis is mild: any smooth map between closed oriented equidimensional manifolds, target connected. The skill is recognising when a problem secretly hands you such a map so that a degree can be extracted.

The first disguised source is **a map presented only by an algebraic or closed-form expression**, with no mention of topology. A polynomial $P$ of degree $k$ extends to a smooth self-map of $\mathbb{CP}^1$; the power map $z\mapsto z^k$ is a self-map of $S^1$; the quaternionic power $q\mapsto q^k$ is a self-map of $S^3=Sp(1)$. In each case the bridge $B\Rightarrow A$ is that a formula defining a smooth self-map of a closed oriented manifold is exactly the input the degree needs, and (b) reduces its computation to counting the finite preimage of one convenient regular value with signs. The non-obvious part is that a purely algebraic quantity (the degree of a polynomial, the exponent $k$) is being computed by a geometric count that a priori has nothing to do with algebra. *Example problem:* show that $q\mapsto q^k$ on $S^3$ has degree $k$ by exhibiting a regular value with exactly $k$ preimages, all of the same sign.

The second disguised source is **a clutching or transition function of a bundle**, that is, a smooth map $g\colon S^{n-1}\to G$ into a Lie group used to glue a bundle over a sphere or over a manifold from two trivial pieces. Composing $g$ with a suitable map $G\to S^{n-1}$, or restricting attention to $U(1)$ where $S^{n-1}=S^1=U(1)$, turns $g$ into a self-map of a closed oriented manifold, and its degree is an invariant of the glued bundle. The bridge is that the degree of the clutching map is unchanged when $g$ is deformed, so by homotopy invariance (c) it depends only on the isomorphism class of the bundle; a nonzero value certifies nontriviality by (d)-type reasoning. *Example problem:* the Hopf bundle has clutching function $z\mapsto z/|z|$ of degree $1$, so it is nontrivial.

The third disguised source is **a vector field with isolated zeros**, or more generally a section of a bundle with isolated zeros. Around an isolated zero $p$ of a vector field $v$ on an oriented $n$-manifold, the normalised field $v/|v|$ is a smooth map from a small sphere $S^{n-1}_\varepsilon(p)$ to the unit sphere $S^{n-1}$, and its degree is the local index of the zero. The bridge is that a zero, which looks like a local and analytic object, produces a degree, which is a global and topological integer; summing these indices computes the Euler characteristic. *Example problem:* deduce that a nowhere-vanishing field on a closed manifold forces the sum of indices, hence a topological invariant, to vanish.

**Targets (Output Amplification).** The bare conclusions become powerful when combined with one more ingredient.

Combine **integrality and homotopy invariance (b), (c)** with **an explicit homotopy that changes the local sign count**. If one can homotope $f$ to a map whose degree is visibly different from the one computed directly, the contradiction proves that no such homotopy exists. This is the engine of the [[Thm - Hairy Ball Theorem|hairy-ball theorem]]: a nowhere-vanishing field on $S^{2n}$ would produce a homotopy from the identity (degree $+1$) to the antipodal map (degree $-1$), and $+1\ne-1$ forbids the field. The extra ingredient is the geometric construction of the offending homotopy.

Combine **surjectivity from nonvanishing degree (d)** with **a lower bound on the degree from the algebra of the map**. If a map is known to have nonzero degree for structural reasons — a nonconstant holomorphic map is orientation-preserving at every regular preimage, so its degree equals the positive number of preimages — then it is surjective, and surjectivity is exactly an existence theorem. The extra ingredient is the sign control that makes the count nonzero. *Payoff:* the fundamental theorem of algebra, and more generally the solvability of $f(x)=y$ for every $y$.

Combine **the regular-value formula (b)** with **Chern–Weil theory** to quantise a curvature integral. When the degree of a clutching map equals a characteristic number expressed as an integral of a curvature polynomial, integrality of the degree forces the a priori real curvature integral to be an integer. This is the mechanism by which the second Chern number of an $SU(2)$-bundle over a closed four-manifold, and hence the instanton number, is an integer; the degree supplies the integrality, Chern–Weil supplies the identification of the two numbers. The extra ingredient is the Chern–Weil identity computed in a later chapter.

---

# Why Is It True

The whole theorem rests on one structural fact about integration on a closed manifold and one structural fact about local diffeomorphisms.

The first fact is that **on a closed manifold the integral of an exact form vanishes**, because $\int_Md\eta=\int_{\partial M}\eta=0$ when $\partial M=\emptyset$. Everything about stability of the degree flows from this. Two normalised forms on $N$ differ by an exact form (their difference has integral zero, and on a closed connected oriented manifold that is precisely the condition to be exact); pulling back preserves exactness; so the two degrees differ by the integral of an exact form, which is zero. That is independence of $\omega$, and the same one line, applied to the two ends of a homotopy, is homotopy invariance. The degree is stable because the only way it could change is by an exact correction, and exact corrections integrate to nothing on a closed manifold.

The second fact is that **at a regular value the map looks like finitely many separate copies of a diffeomorphism**. If $y$ is a regular value, its finitely many preimages each have a neighbourhood on which $f$ is a diffeomorphism onto a common neighbourhood $V$ of $y$; the preimage of $V$ is the disjoint union of these sheets. Concentrate the normalised form near $y$. Then the integral over $M$ splits into one integral per sheet, and change of variables turns each sheet's integral into $\pm1$ — the sign recording whether that sheet preserves or reverses orientation. The degree is therefore a signed count of sheets, which is why it is an integer. That the count is independent of $y$ is not proved by comparing values of $y$ directly; it is inherited from the analytic definition, which already knows nothing about $y$.

> **The mechanism in one sentence.** The degree is stable because a closed manifold has no boundary for Stokes to detect, and it is an integer because over a generic value the map is a finite union of local diffeomorphisms whose orientation behaviours are each worth exactly $\pm1$.

The remaining clauses are corollaries of these two facts. Surjectivity: if a point is missed, put the form near it and every pullback vanishes, so the degree is zero — contrapositive gives (d). Multiplicativity: pull back through the composite in two stages and use that a form on $N$ with integral $\deg g$ is $\deg g$ times a normalised form (up to an exact error that integrates to nothing). Bounding: the extension over $W$ makes the pulled-back form exact on $W$ in the sense that its integral over $\partial W$ equals the integral over $W$ of a form that is closed, so Stokes gives zero. Additivity: integration splits over connected components.

---

# What Makes This Hard

The one genuinely delicate step is part (b): assembling the finitely many local diffeomorphisms into a single evenly covered neighbourhood $V$ of the regular value $y$ over which $f$ is a disjoint union of diffeomorphisms. The naive attempt — take a neighbourhood of $y$ inside each $f(U_i)$ — is not enough, because points of $M$ far from the preimages could still map into that neighbourhood; one must additionally subtract the (compact, hence closed) image of the complement of the chosen neighbourhoods, and check that what remains is still an open neighbourhood of $y$ evenly covered by exactly the sheets $U_i$. The common errors are to forget this subtraction, to forget that the sign $\operatorname{sign}\det df_x$ must be constant on each connected sheet (so the sheets must be taken connected), and to conflate "regular value $y$ exists" (Sard) with "the formula is independent of $y$" (which here is deduced from independence of $\omega$, not proved by moving $y$).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove the two stability clauses (a), (c) by the single observation that the integral of an exact form over a closed manifold is zero. Prove integrality (b) by concentrating a normalised form near a regular value and applying change of variables sheet by sheet. Derive (d), (e), (f), (g) as short corollaries of these together with Stokes and additivity of the integral.

**Subgoal decomposition:**

1. **A normalised form supported anywhere.** Show that in any nonempty open set of an oriented $n$-manifold there is an $n$-form with total integral $1$.
   - *Hint:* Take a positively oriented bump form in a coordinate ball and rescale by its integral, which is positive.
   - *Why needed:* Both the definition (Step 0) and parts (b), (d) require a normalised form supported in a prescribed small set.

2. **Exact forms integrate to zero on a closed manifold.** Show $\int_Md\eta=0$ for $\eta\in\Omega^{n-1}(M)$, $M$ closed.
   - *Hint:* Stokes' theorem, with $\partial M=\emptyset$.
   - *Why needed:* It is the sole mechanism behind (a), (c), and the $\deg g=0$ case of (e).

3. **Local model at a regular value.** Show that a regular value $y$ has finitely many preimages, and an evenly covered connected neighbourhood $V$ over which $f^{-1}(V)$ is a disjoint union of connected open sets each mapped diffeomorphically onto $V$.
   - *Hint:* Inverse function theorem at each preimage; then subtract the image of the complement of the sheets.
   - *Why needed:* It reduces $\int_Mf^*\omega$ to a sum of one-sheet integrals in (b).

4. **The sign of a one-sheet integral.** Show that for a diffeomorphism $\varphi\colon U\to V$ of oriented $n$-manifolds and a compactly supported $\omega$ on $V$, $\int_U\varphi^*\omega=\varepsilon\int_V\omega$ with $\varepsilon=+1$ if $\varphi$ preserves orientation and $-1$ otherwise, and that for $\varphi=f|_{U_i}$ this sign is $\operatorname{sign}\det df_{x_i}$.
   - *Hint:* Change of variables for integration on manifolds; the sign is that of the Jacobian in oriented charts.
   - *Why needed:* It turns each sheet's contribution into $\pm1$, giving the integer count.

5. **Assemble (a)–(g).** Combine subgoals 1–4 with Stokes and pullback functoriality.
   - *Hint:* (a), (c) from subgoal 2; (b) from 1, 3, 4; (d) from 1; (e) from 2 and the top-cohomology theorem; (f) from Stokes on $W$; (g) from additivity of the integral.
   - *Why needed:* These are the seven conclusions.

---

# Lemma Decomposition

> [!note]- Lemma 1: A normalised top-form supported in any nonempty open set
> **Statement:** Let $N$ be an oriented $n$-manifold and $V\subseteq N$ a nonempty open set. Then there exists $\omega\in\Omega^n(N)$ with $\operatorname{supp}\omega$ a compact subset of $V$ and $\int_N\omega=1$.
>
> **Hint:** A positively oriented bump form on a coordinate ball has strictly positive integral; rescale.
>
> **Why needed:** Step 0 (a normalised form exists at all), part (b) (a form concentrated near a regular value), and part (d) (a form concentrated near a missed point) all need this.
>
> > [!note]- Full proof
> > Pick a point $q\in V$ and an oriented chart $(\Phi,U)$ with $q\in U\subseteq V$ and $\Phi(U)\subseteq\mathbb R^n$ open; "oriented" means $\Phi$ is orientation-preserving from $U$ (with the orientation of $N$) to $\mathbb R^n$ (with its standard orientation), which is possible by the definition of an orientation. Choose $r>0$ with the closed ball $\overline{B_r(\Phi(q))}\subseteq\Phi(U)$. By [[Thm - Existence of Smooth Bump Functions|the existence of smooth bump functions]] — for a point in an open set of $\mathbb R^n$ there is a smooth $\chi\ge0$ with compact support in that set and $\chi>0$ on a neighbourhood of the point — take $\chi\colon\mathbb R^n\to[0,\infty)$ smooth with $\operatorname{supp}\chi\subseteq B_r(\Phi(q))$ and $\chi(\Phi(q))>0$.
> >
> > Define $\alpha=\chi\,dx^1\wedge\cdots\wedge dx^n$ on $\mathbb R^n$, an $n$-form with compact support in $B_r(\Phi(q))$, and set $\omega_0=\Phi^*\alpha$ on $U$, extended by zero to all of $N$; the extension is smooth because $\operatorname{supp}\omega_0=\Phi^{-1}(\operatorname{supp}\alpha)$ is a compact subset of $U$ (a homeomorphic image of the compact $\operatorname{supp}\alpha$), so $\omega_0$ vanishes on a neighbourhood of $N\setminus U$. Then
> > $$\int_N\omega_0=\int_U\Phi^*\alpha=\int_{\Phi(U)}\alpha=\int_{\mathbb R^n}\chi\,dx^1\cdots dx^n\qquad(\text{definition of the integral in an oriented chart, }\Phi\text{ orientation-preserving}),$$
> > and this is strictly positive because $\chi\ge0$ is continuous and positive at $\Phi(q)$, hence positive on a set of positive Lebesgue measure. Call this number $c>0$. Set $\omega=c^{-1}\omega_0$. Then $\operatorname{supp}\omega=\operatorname{supp}\omega_0$ is a compact subset of $U\subseteq V$ and $\int_N\omega=c^{-1}\cdot c=1$. $\blacksquare$

> [!note]- Lemma 2: Exact forms integrate to zero on a closed manifold
> **Statement:** Let $M$ be a closed oriented $n$-manifold and $\eta\in\Omega^{n-1}(M)$. Then $\int_Md\eta=0$.
>
> **Hint:** Stokes, with empty boundary.
>
> **Why needed:** This is the entire content of independence of $\omega$ (a), homotopy invariance (c), and the degenerate case of multiplicativity (e).
>
> > [!note]- Full proof
> > By [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem on manifolds]] — for a compact oriented $n$-manifold $M$ with boundary $\partial M$ carrying the induced orientation and any $\eta\in\Omega^{n-1}(M)$, one has $\int_Md\eta=\int_{\partial M}\iota^*\eta$, where $\iota\colon\partial M\hookrightarrow M$ is the inclusion — we compute
> > $$\int_Md\eta=\int_{\partial M}\iota^*\eta\qquad(\text{Stokes' theorem}).$$
> > Since $M$ is closed, $\partial M=\varnothing$, and the integral of any form over the empty manifold is $0$. Therefore $\int_Md\eta=0$. $\blacksquare$

> [!note]- Lemma 3: Evenly covered neighbourhood of a regular value
> **Statement:** Let $M$ be a compact $n$-manifold, $N$ an $n$-manifold, $f\colon M\to N$ smooth, and $y\in N$ a regular value. Then $f^{-1}(y)=\{x_1,\dots,x_k\}$ is finite (possibly empty), and there is a connected open neighbourhood $V$ of $y$ together with pairwise disjoint connected open sets $U_1,\dots,U_k$ in $M$ with $x_i\in U_i$, such that $f^{-1}(V)=U_1\sqcup\cdots\sqcup U_k$ and each restriction $f|_{U_i}\colon U_i\to V$ is a diffeomorphism.
>
> **Hint:** Inverse function theorem at each $x_i$; then remove the image of the complement of the sheets, which is compact.
>
> **Why needed:** It reduces the degree integral over $M$ to a finite sum of integrals over sheets, each a diffeomorphism, which is where integrality comes from.
>
> > [!note]- Full proof
> > **Finiteness of $f^{-1}(y)$.** By [[Thm - Sard's Theorem when the Source Dimension does not Exceed the Target Dimension|the restricted Sard theorem]] — for a smooth map between manifolds of equal dimension with compact source, the preimage of a regular value is finite — the set $f^{-1}(y)$ is finite; write it $\{x_1,\dots,x_k\}$ (if empty, take $k=0$ and $V=N\setminus f(M)$ below, which is open and contains $y$; the remaining claims are vacuous). We give the argument for completeness: each $x\in f^{-1}(y)$ is isolated in $f^{-1}(y)$ because $df_x$ is an isomorphism, so by the inverse function theorem $f$ is injective near $x$; and $f^{-1}(y)$ is closed in the compact $M$, hence compact; a compact set all of whose points are isolated is finite.
> >
> > **Diffeomorphic sheets at each preimage.** Fix $x_i$. Since $y$ is regular and $\dim M=\dim N$, $df_{x_i}\colon T_{x_i}M\to T_yN$ is a linear isomorphism, so by [[Thm - The Rank Theorem|the rank theorem]] in its maximal-rank form — a smooth map whose differential at a point is an isomorphism restricts to a diffeomorphism of some open neighbourhood of that point onto an open neighbourhood of its image — there is an open set $W_i\ni x_i$ with $f(W_i)$ open and $f|_{W_i}\colon W_i\to f(W_i)$ a diffeomorphism. Because $M$ is Hausdorff and $\{x_1,\dots,x_k\}$ is finite, shrink the $W_i$ so that they are pairwise disjoint and each is connected (replace $W_i$ by the connected component of $x_i$ in $W_i\setminus\bigcup_{j\ne i}\{x_j\}$, still open).
> >
> > **Removing the far part of $M$.** The set $A=M\setminus\bigcup_{i=1}^kW_i$ is closed in the compact $M$, hence compact, so $f(A)$ is compact and therefore closed in $N$; and $y\notin f(A)$, since every preimage of $y$ lies in some $W_i$. Hence
> > $$V:=\Big(\bigcap_{i=1}^kf(W_i)\Big)\setminus f(A)$$
> > is open (a finite intersection of open sets minus a closed set) and contains $y$ (as $y\in f(W_i)$ for each $i$ and $y\notin f(A)$). Replace $V$ by the connected component of $y$ in $V$, which is open because $N$ is locally connected; call it $V$ again.
> >
> > **The sheets over $V$.** Set $U_i=W_i\cap f^{-1}(V)$. Each $U_i$ is open, contains $x_i$, and $f|_{U_i}\colon U_i\to V$ is a diffeomorphism: indeed $f|_{W_i}\colon W_i\to f(W_i)$ is a diffeomorphism and $V\subseteq f(W_i)$, so $f|_{W_i}$ restricts to a diffeomorphism from $(f|_{W_i})^{-1}(V)=U_i$ onto $V$. The $U_i$ are pairwise disjoint since the $W_i$ are, and each $U_i$ is connected (it is the diffeomorphic preimage under $f|_{W_i}$ of the connected $V$). Finally $f^{-1}(V)=\bigsqcup_iU_i$: if $x\in f^{-1}(V)$ then $f(x)\in V$, so $f(x)\notin f(A)$, whence $x\notin A$, i.e. $x\in\bigcup_iW_i$; and then $x\in W_i\cap f^{-1}(V)=U_i$ for that $i$. Conversely each $U_i\subseteq f^{-1}(V)$ by construction. $\blacksquare$

> [!note]- Lemma 4: The signed value of a one-sheet integral
> **Statement:** Let $\varphi\colon U\to V$ be a diffeomorphism between oriented $n$-manifolds and $\omega\in\Omega^n(V)$ compactly supported. Then $\int_U\varphi^*\omega=\varepsilon(\varphi)\int_V\omega$, where $\varepsilon(\varphi)=+1$ if $\varphi$ preserves orientation and $-1$ if it reverses it. If $\varphi=f|_{U_i}$ is the sheet of Lemma 3 through a preimage $x_i$ of a regular value, then $\varepsilon(\varphi)=\operatorname{sign}\det df_{x_i}$, and this sign is constant on the connected set $U_i$.
>
> **Hint:** Change of variables for integration on manifolds; the orientation behaviour of a diffeomorphism is measured by the sign of its Jacobian determinant in oriented charts.
>
> **Why needed:** It converts each diffeomorphic sheet's integral into $\pm1$, producing the integer count in part (b).
>
> > [!note]- Full proof
> > **The signed change of variables.** By [[Thm - Change of Variables for Integration on Manifolds|change of variables for integration on manifolds]] — if $\varphi\colon U\to V$ is a diffeomorphism of oriented $n$-manifolds and $\omega$ is a compactly supported $n$-form on $V$, then $\int_U\varphi^*\omega=\int_V\omega$ when $\varphi$ preserves orientation and $\int_U\varphi^*\omega=-\int_V\omega$ when $\varphi$ reverses it — we have directly
> > $$\int_U\varphi^*\omega=\varepsilon(\varphi)\int_V\omega\qquad(\text{change of variables, }\varepsilon(\varphi)=\pm1\text{ the orientation sign of }\varphi).$$
> >
> > **Identifying the sign with $\operatorname{sign}\det df_{x_i}$.** Take positively oriented charts around $x_i$ and around $y=f(x_i)$; in these coordinates $f$ is represented by a map $\widehat f$ between open subsets of $\mathbb R^n$, and orientation-preservation of $f|_{U_i}$ is by definition the positivity of $\det D\widehat f$. Since the charts are positively oriented, $\det D\widehat f(x_i)$ has the same sign as the orientation sign of $df_{x_i}\colon T_{x_i}M\to T_yN$, which is exactly $\operatorname{sign}\det df_{x_i}$ as fixed in the Notation. Thus $\varepsilon(f|_{U_i})=\operatorname{sign}\det df_{x_i}$.
> >
> > **Constancy on $U_i$.** The function $x\mapsto\det D\widehat f(x)$ is continuous on the connected set $U_i$ and never zero there (because $f|_{U_i}$ is a diffeomorphism, so $df_x$ is an isomorphism at every $x\in U_i$). A continuous nowhere-zero real function on a connected set has constant sign; hence $\operatorname{sign}\det df_x$ is constant on $U_i$, equal to its value $\operatorname{sign}\det df_{x_i}$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $M,N$ be closed oriented $n$-manifolds with $N$ connected and $f\colon M\to N$ smooth.
>
> **Step 0 — a normalised form exists, so the degree is defined.** Applying Lemma 1 with $V=N$ produces $\omega\in\Omega^n(N)$ with $\int_N\omega=1$. Hence $\deg f=\int_Mf^*\omega$ is a well-defined real number for at least one $\omega$; part (a) shows it is the same for all.
>
> **Part (a) — independence of $\omega$.** Let $\omega,\omega'\in\Omega^n(N)$ both satisfy $\int_N\omega=\int_N\omega'=1$. Then $\int_N(\omega'-\omega)=0$. By [[Thm - The Top de Rham Cohomology of a Closed Connected Oriented Manifold is R|the top de Rham cohomology theorem]] — on a closed connected oriented $n$-manifold $N$ an $n$-form is exact if and only if its integral over $N$ is zero — there is $\beta\in\Omega^{n-1}(N)$ with $\omega'-\omega=d\beta$; here we invoke the connectedness of $N$. Pulling back,
> $$f^*\omega'-f^*\omega=f^*(d\beta)=d(f^*\beta)\qquad(\text{linearity of }f^*\text{; }f^*\text{ commutes with }d\text{ by }[[\text{Thm - Pull-Back Commutes with the Exterior Derivative}]]).$$
> Integrating over $M$ and using Lemma 2 (the integral of an exact form over the closed manifold $M$ is zero),
> $$\int_Mf^*\omega'-\int_Mf^*\omega=\int_Md(f^*\beta)=0\qquad(\text{Lemma 2}).$$
> Therefore $\int_Mf^*\omega'=\int_Mf^*\omega$, so $\deg f$ does not depend on the normalised $\omega$.
>
> **Part (b) — the regular-value formula and integrality.** Let $y\in N$ be a regular value of $f$; such values exist and are dense by [[Thm - Sard's Theorem when the Source Dimension does not Exceed the Target Dimension|the restricted Sard theorem]] (the regular values of a map between equidimensional manifolds are dense), so the statement is non-vacuous. By Lemma 3 write $f^{-1}(y)=\{x_1,\dots,x_k\}$ and take the connected evenly covered neighbourhood $V$ of $y$ and the disjoint connected sheets $U_1,\dots,U_k$ with $f^{-1}(V)=\bigsqcup_iU_i$ and each $f|_{U_i}\colon U_i\to V$ a diffeomorphism.
>
> By Lemma 1 choose $\omega\in\Omega^n(N)$ with $\operatorname{supp}\omega$ a compact subset of $V$ and $\int_N\omega=1$; then $\int_V\omega=1$. Its pullback satisfies $\operatorname{supp}(f^*\omega)\subseteq f^{-1}(\operatorname{supp}\omega)\subseteq f^{-1}(V)=\bigsqcup_iU_i$, because at any $x$ with $f(x)\notin\operatorname{supp}\omega$ the form $\omega$ vanishes at $f(x)$ and so $(f^*\omega)_x=0$. Since the integral is additive over a partition of the support into disjoint open sets,
> $$\deg f=\int_Mf^*\omega=\int_{\bigsqcup_iU_i}f^*\omega=\sum_{i=1}^k\int_{U_i}f^*\omega\qquad(\text{support of }f^*\omega\subseteq\textstyle\bigsqcup_iU_i\text{; additivity of the integral}),$$
> where the first equality uses part (a) to identify $\int_Mf^*\omega$ (for this particular $\omega$) with $\deg f$. On each sheet, $f|_{U_i}\colon U_i\to V$ is a diffeomorphism and $\omega$ is compactly supported in $V$, so by Lemma 4,
> $$\int_{U_i}f^*\omega=\int_{U_i}(f|_{U_i})^*\omega=\operatorname{sign}(\det df_{x_i})\int_V\omega=\operatorname{sign}(\det df_{x_i})\qquad(\text{Lemma 4; }\int_V\omega=1).$$
> Combining the two displays,
> $$\deg f=\sum_{i=1}^k\operatorname{sign}(\det df_{x_i})=\sum_{x\in f^{-1}(y)}\operatorname{sign}\det df_x .$$
> The right-hand side is a finite sum of terms $\pm1$, hence an integer, so $\deg f\in\mathbb Z$. Since the left-hand side $\deg f$ was shown in part (a) to be independent of every choice, the value of the signed count is the same integer for every regular value $y$. (When $k=0$, both sides are $0$: the empty sum on the right, and on the left $f^*\omega=0$ since $\operatorname{supp}\omega\subseteq V$ with $f^{-1}(V)=\varnothing$.)
>
> **Part (c) — homotopy invariance.** Let $f_0,f_1\colon M\to N$ be smoothly homotopic and let $\omega\in\Omega^n(N)$ be normalised. As a top-degree form, $\omega$ is closed, so it represents a class $[\omega]\in H^n_{dR}(N)$. By [[Thm - Homotopy Invariance of de Rham Cohomology|the homotopy invariance of de Rham cohomology]] — smoothly homotopic maps induce equal pullback maps on de Rham cohomology, $f_0^*=f_1^*\colon H^n_{dR}(N)\to H^n_{dR}(M)$ — we have $f_0^*[\omega]=f_1^*[\omega]$ in $H^n_{dR}(M)$, that is, there is $\eta\in\Omega^{n-1}(M)$ with
> $$f_1^*\omega-f_0^*\omega=d\eta\qquad(\text{equality of cohomology classes }f_0^*[\omega]=f_1^*[\omega]).$$
> Integrating over the closed manifold $M$ and using Lemma 2,
> $$\deg f_1-\deg f_0=\int_Mf_1^*\omega-\int_Mf_0^*\omega=\int_Md\eta=0\qquad(\text{Lemma 2}).$$
> Therefore $\deg f_0=\deg f_1$.
>
> **Part (d) — nonzero degree forces surjectivity.** We prove the contrapositive: if $f$ is not surjective then $\deg f=0$. Suppose $y_0\in N\setminus f(M)$. Since $M$ is compact, $f(M)$ is compact, hence closed in $N$, so $N\setminus f(M)$ is open and there is an open set $V$ with $y_0\in V\subseteq N\setminus f(M)$. By Lemma 1 pick $\omega\in\Omega^n(N)$ with $\operatorname{supp}\omega$ a compact subset of $V$ and $\int_N\omega=1$. For every $x\in M$ we have $f(x)\in f(M)$, so $f(x)\notin V\supseteq\operatorname{supp}\omega$, whence $\omega_{f(x)}=0$ and $(f^*\omega)_x=0$. Thus $f^*\omega\equiv0$ on $M$, and
> $$\deg f=\int_Mf^*\omega=\int_M0=0\qquad(f^*\omega\equiv0).$$
> By part (a) this is the degree for every normalised form, so $\deg f=0$. Contrapositively, $\deg f\ne0$ implies $f$ is surjective.
>
> **Part (e) — multiplicativity.** Let $g\colon N\to P$ be smooth with $P$ closed connected oriented of dimension $n$. Choose $\omega\in\Omega^n(P)$ with $\int_P\omega=1$; then $\deg g=\int_Ng^*\omega$. By pullback functoriality, $(g\circ f)^*\omega=f^*(g^*\omega)$, so
> $$\deg(g\circ f)=\int_M(g\circ f)^*\omega=\int_Mf^*(g^*\omega)\qquad((g\circ f)^*=f^*g^*).$$
> Write $c=\int_Ng^*\omega=\deg g$. We consider two exhaustive cases.
>
> *Case 1: $c\ne0$.* Then $c^{-1}g^*\omega\in\Omega^n(N)$ is normalised, $\int_N(c^{-1}g^*\omega)=1$, so by the definition of the degree of $f$ (independent of the normalised form, part (a)),
> $$\int_Mf^*(c^{-1}g^*\omega)=\deg f\quad\Longrightarrow\quad\int_Mf^*(g^*\omega)=c\,\deg f=\deg g\cdot\deg f\qquad(\text{linearity of }f^*\text{ and of the integral}).$$
>
> *Case 2: $c=0$.* Then $\int_Ng^*\omega=0$, so by [[Thm - The Top de Rham Cohomology of a Closed Connected Oriented Manifold is R|the top de Rham cohomology theorem]] (an $n$-form on the closed connected oriented $N$ with integral zero is exact) there is $\gamma\in\Omega^{n-1}(N)$ with $g^*\omega=d\gamma$. Hence $f^*(g^*\omega)=f^*(d\gamma)=d(f^*\gamma)$ (pullback commutes with $d$), and by Lemma 2,
> $$\int_Mf^*(g^*\omega)=\int_Md(f^*\gamma)=0=\deg g\cdot\deg f\qquad(\text{Lemma 2; }\deg g=c=0).$$
>
> In both cases $\deg(g\circ f)=\deg g\cdot\deg f$, which are exhaustive since $c$ is either zero or not.
>
> **Part (f) — bounding maps have degree zero.** Suppose $M=\partial W$ for a compact oriented $(n+1)$-manifold $W$, with $M$ carrying the boundary orientation of [[Def - Manifold with Boundary and Induced Orientation|the induced-orientation convention]], and suppose $f$ extends to a smooth $F\colon W\to N$ with $F|_M=f$. Let $\omega\in\Omega^n(N)$ be normalised. Because $\omega$ is a top-degree form on the $n$-manifold $N$, $d\omega=0$, so
> $$d(F^*\omega)=F^*(d\omega)=F^*0=0\qquad(F^*\text{ commutes with }d\text{; }d\omega=0).$$
> Apply [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] to the $n$-form $F^*\omega$ on the compact oriented $(n+1)$-manifold $W$ with boundary $\partial W=M$:
> $$\int_WdF^*\omega=\int_{\partial W}\iota^*F^*\omega\qquad(\text{Stokes' theorem; }\iota\colon M\hookrightarrow W\text{ the inclusion}).$$
> The left side is $\int_W0=0$. On the right, $\iota^*F^*\omega=(F\circ\iota)^*\omega=f^*\omega$ because $F\circ\iota=f$, and the boundary orientation is the one used to define $\deg f$. Therefore
> $$0=\int_{\partial W}\iota^*F^*\omega=\int_Mf^*\omega=\deg f .$$
> Hence $\deg f=0$.
>
> **Part (g) — additivity over components.** Suppose $M$ is disconnected. Each connected component of $M$ is open (a manifold is locally connected) and closed; the components form a partition of the compact $M$ into disjoint open sets, and a compact space admits only finitely many disjoint nonempty open sets, so there are finitely many components $M_1,\dots,M_r$. Each $M_j$ is a closed oriented $n$-manifold with the orientation restricted from $M$, so $\deg(f|_{M_j})$ is defined ($N$ is connected). For a normalised $\omega\in\Omega^n(N)$, additivity of the integral over the disjoint pieces gives
> $$\deg f=\int_Mf^*\omega=\sum_{j=1}^r\int_{M_j}f^*\omega=\sum_{j=1}^r\int_{M_j}(f|_{M_j})^*\omega=\sum_{j=1}^r\deg(f|_{M_j})\qquad(\text{additivity of the integral over components}).$$
> This is the claimed formula, and it is consistent with parts (a)–(f), which never required $M$ connected. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Complex analysis — the fundamental theorem of algebra.** A polynomial $P(z)=z^k+a_{k-1}z^{k-1}+\cdots+a_0$ with $k\ge1$ extends to a smooth self-map of $\mathbb{CP}^1$. Because $P$ is holomorphic, at every regular preimage $df$ is complex-linear and hence orientation-preserving, so every term $\operatorname{sign}\det df_x$ equals $+1$; the regular-value formula (b) then gives $\deg P=k>0$. By (d) the map is surjective, so $0$ is attained and $P$ has a root. The theorem applies because a polynomial is exactly one of the "map given by a formula" disguised sources, and the non-obvious step is that the holomorphy pins every local sign to $+1$, forbidding cancellation.

**Differential topology — the hairy-ball theorem.** A nowhere-vanishing tangent field $v$ on $S^{2n}$ would give the smooth homotopy $F_t(x)=\cos(\pi t)\,x+\sin(\pi t)\,v(x)/|v(x)|$ from the identity to the antipodal map. Homotopy invariance (c) forces these to have equal degree, but the identity has degree $+1$ and the antipodal map of $S^{2n}$ has degree $(-1)^{2n+1}=-1$, computed from the regular-value formula (b) by writing the antipodal map as a composite of $2n+1$ reflections, each of degree $-1$, and using multiplicativity (e). The contradiction $+1=-1$ rules out $v$. The theorem applies because the field manufactures a homotopy whose two ends have computable, unequal degrees.

**Gauge theory — quantisation of the instanton number.** For a principal $SU(2)$-bundle over a closed oriented four-manifold, the clutching function $g\colon S^3\to SU(2)=S^3$ has an integer degree by (b). Later chapters identify this degree with the second Chern number $\int_Xc_2$, an a priori real integral of a curvature polynomial; integrality of the degree then forces that curvature integral — the instanton number — to be an integer. The theorem applies because the clutching function is a self-map of $S^3$, and the payoff is that a continuous physical quantity can only take integer values.

---

# Bridges

- **[[Thm - Winding Number of a Map from the Circle to U(1)|Winding number of a circle map]].** For $n=1$ and $N=U(1)=S^1$, the degree of $g\colon S^1\to U(1)$ is the winding number $w(g)=\tfrac1{2\pi}\int_{S^1}g^*d\theta$. This is the present theorem specialised to the abelian one-dimensional case: $d\theta/2\pi$ is a normalised form on $U(1)$, so $w(g)=\deg g$, and parts (b), (c), (e) become integrality, homotopy invariance, and additivity of winding numbers. The winding-number page builds on this one and adds the abelian features (additivity under pointwise product, the extension-over-the-disc criterion).

- **[[Thm - Hairy Ball Theorem|The hairy-ball theorem]].** As sketched above, the degree computation of the antipodal map, combined with homotopy invariance, gives the nonexistence of a nowhere-vanishing field on an even sphere. The hairy-ball page invokes this theorem by name for both the degree of the antipodal map (via the reflection factorisation) and the homotopy-invariance step.

- **[[Thm - Clutching Construction for Bundles over a Closed Manifold|The clutching construction]].** A bundle over a closed manifold, trivial off a disc, is determined by a clutching map on the boundary sphere; homotopic clutching maps give isomorphic bundles. The homotopy-invariance clause (c) of the degree is what makes the degree of the clutching map a bundle invariant, and the bounding clause (f) is what shows that a clutching map extending over one of the two pieces contributes nothing — the two facts together let the clutching page read off nontriviality of a bundle from a nonzero clutching degree.

- **[[Def - Brouwer Degree of a Map|The definition of the Brouwer degree]].** The definition page states the degree analytically and defers integrality and homotopy invariance; this theorem discharges those deferrals in full. Every later use of "the degree is an integer" or "the degree is a homotopy invariant" in this series routes through the present page rather than through the definition page's outline.

---

# Unlocked by This

> [!tip] The degree of the power maps *(from §3.5)*
> The self-maps $z\mapsto z^k$ of $S^1$ and $q\mapsto q^k$ of $S^3=Sp(1)$ have degree $k$, computed by the regular-value formula (b) on a conveniently chosen regular value with exactly $|k|$ preimages of a common sign. These feed the winding-number and Chern-number computations of the later sections.

> [!tip] Bundles over spheres and the classification of SU(2)-bundles *(from §3.6)*
> The integrality and homotopy invariance of the clutching degree, provided here, are the arithmetic backbone of the classification: principal $SU(2)$-bundles over $S^4$ are classified by an integer, the degree of the clutching map $S^3\to SU(2)$, which equals the second Chern number.

> [!tip] The gauge variation of the Chern–Simons functional *(from Gauge Theory VI)*
> Under a gauge transformation $g$, the Chern–Simons functional changes by an integer multiple of $8\pi^2$, the multiple being the degree of $g$ regarded as a map into the structure group. The integrality established here is exactly what makes the exponentiated Chern–Simons action gauge-invariant.
