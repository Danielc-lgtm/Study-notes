---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Principal G-Bundle"
  - "Thm - Free Proper Actions Give Principal Bundles"
  - "Def - Representation of a Lie Group"
  - "Def - Vector Bundle"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ is a smooth manifold and $\pi\colon P\to M$ is a **principal $G$-bundle** in the sense of [[Def - Principal G-Bundle|the principal-bundle definition]]: $G$ is a Lie group acting smoothly on the right on the total space $P$, the action is free, the orbits are exactly the fibres of $\pi$, and $P$ is locally trivial in a way compatible with the action. Following the series convention, **Lie groups act on principal bundles on the right**; we write $R_g(p)=p\cdot g$ for $g\in G$ and $p\in P$, and for a fixed base point $m\in M$ we write $P_m=\pi^{-1}(m)$ for the fibre over $m$. We write $\Gamma(E)$ for the space of smooth sections of a bundle $E$, and $GL(V)$ for the group of invertible linear maps of a finite-dimensional real or complex vector space $V$.

A **representation** of $G$ on $V$ is a smooth group homomorphism $\rho\colon G\to GL(V)$; representations are the standing example of a **left** action, $g\cdot v:=\rho(g)v$, and this is where our left/right conventions meet. See [[Def - Representation of a Lie Group|the representation definition]]. When $V$ is complex we still write $GL(V)$ and understand complex-linear maps.

On the product manifold $P\times V$ we define the right $G$-action
$$(p,v)\cdot g:=\big(p\cdot g,\ \rho(g^{-1})v\big)\qquad(p\in P,\ v\in V,\ g\in G),$$
and we write $[p,v]$ for the orbit (equivalence class) of $(p,v)$, and $\varpi\colon P\times V\to (P\times V)/G$, $\varpi(p,v)=[p,v]$, for the quotient projection. The associated bundle is the quotient $P\times_\rho V:=(P\times V)/G$; we still call its projection to $M$ by the letter $\pi$, so $\pi[p,v]=\pi(p)$. Finally,
$$C^\infty(P;V)^G:=\big\{\hat s\colon P\to V \ \text{smooth}\ \big|\ \hat s(p\cdot g)=\rho(g^{-1})\hat s(p)\ \ \forall p\in P,\ g\in G\big\}$$
is the space of **($\rho$-)equivariant functions** from $P$ to $V$. The full symbol registry for the chapter is on [[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles]].

This is a compound page: it defines three interlocking notions — the **associated vector bundle** $P\times_\rho V$, the space $C^\infty(P;V)^G$ of equivariant functions together with the section it induces, and the more general **associated fibre/principal bundle** attached to any $G$-space or Lie-group homomorphism — because they are one construction (quotient a product by the diagonal $G$-action) specialised to three different fibres, and they are used together at every later step: matter fields, adjoint bundles, and the frame–field dictionary are all instances.

> [!warning] Convention: the inverse in $\rho(g^{-1})$
> Both sources build the associated bundle with $\rho(g^{-1})$, not $\rho(g)$: Haydys writes the action $(p,v)\cdot g=(p\cdot g,\rho(g^{-1})v)$ (§2.2, equation (30)) and Bär writes the identical formula (Definition 2.2.12, p. 44). The inverse is **forced**: it is exactly what turns the left action $\rho$ into a right action of $G$ on $P\times V$, so that the quotient by the free right action is available. We prove this in the Axiom Motivation and record the failure of the naive $\rho(g)$ as a non-example below. A reader who has seen the "opposite" convention $[p,v]\cdot g=[pg,\rho(g)v]$ is looking at the associated bundle of the contragredient (dual) representation; the one-line conversion is to replace $\rho$ by $g\mapsto\rho(g^{-1})^{\mathsf T}$.

> [!warning] Convention: "properly discontinuous" in Haydys
> Haydys (§2.2, just after (30)) says the right action on $P\times V$ is "free and properly discontinuous". This is a slip: *properly discontinuous* is the correct hypothesis only for **discrete** groups, whereas a general Lie group $G$ (for example $U(1)$, which is not discrete) acts *properly*, not properly discontinuously. The correct and sufficient hypothesis is that the action is **free and proper**; the manifold structure on the quotient then comes from [[Thm - Free Proper Actions Give Principal Bundles|the free-proper theorem]]. We use "free and proper" throughout and never rely on discreteness.

---

# Axiom Motivation

The construction answers a single, sharply posed question. A principal $G$-bundle $P$ records, at each point $m\in M$, a $G$-torsor $P_m$ — think of it as the set of "frames" or "gauges" over $m$, any two related by a unique element of $G$. Separately, a representation $\rho\colon G\to GL(V)$ says how the abstract symmetry $G$ is to *act on data valued in $V$*. We would like to glue these two pieces of information into an honest **vector bundle** over $M$ whose fibre over $m$ is a copy of $V$ — the bundle in which "$V$-valued fields transforming under $\rho$" will live. The desideratum is precise: we want a rank-$\dim V$ vector bundle $E\to M$ whose transition functions are $\rho$ composed with the transition functions of $P$, so that a section of $E$ is exactly a $V$-valued object whose local descriptions transform by $\rho$ under a change of gauge.

Here is the difficulty that shapes the definition. A frame $p\in P_m$ gives a preferred identification $V\cong E_m$ — "read off the components of the field in the gauge $p$". But there is no *canonical* frame; changing the gauge by $g\in G$ replaces $p$ by $p\cdot g$, and the same physical field must then have its components acted on by $\rho$ so as to describe the same element of $E_m$. The fibre $E_m$ must therefore be the set of pairs (frame, components) **with pairs describing the same field identified**. That is exactly a quotient of $P_m\times V$ by the relation that ties $(p,v)$ to its regauged version. The construction is not optional: it is the only way to build a $V$-bundle from $P$ and $\rho$ that makes gauge changes act correctly.

**Why the quotient must be by a right action, and why $\rho(g^{-1})$.** The group $G$ already acts on $P$ on the right. To quotient the product $P\times V$ we need a *single* $G$-action on $P\times V$ whose orbits are the pairs we wish to identify. Try the most naive rule, moving $P$ by $g$ and $V$ by $\rho(g)$: set $(p,v)\bullet g:=(p\cdot g,\rho(g)v)$. For this to be a right action we need $\big((p,v)\bullet g\big)\bullet h=(p,v)\bullet(gh)$ for all $g,h\in G$. The left-hand side is $(p\cdot g\cdot h,\ \rho(h)\rho(g)v)=(p\cdot gh,\ \rho(hg)v)$, while the right-hand side is $(p\cdot gh,\ \rho(gh)v)$. These agree for all $g,h,v$ **if and only if** $\rho(hg)=\rho(gh)$ for all $g,h$, that is, only when $\rho$ has abelian image. For a general representation the naive rule is simply *not a right action*, so there is no quotient to take. Replacing $\rho(g)$ by $\rho(g^{-1})$ fixes this exactly: with $(p,v)\cdot g=(p\cdot g,\rho(g^{-1})v)$,
$$\big((p,v)\cdot g\big)\cdot h=\big(p\cdot g\cdot h,\ \rho(h^{-1})\rho(g^{-1})v\big)=\big(p\cdot gh,\ \rho(h^{-1}g^{-1})v\big)=\big(p\cdot gh,\ \rho((gh)^{-1})v\big)=(p,v)\cdot(gh),$$
using that $\rho$ is a homomorphism and $(gh)^{-1}=h^{-1}g^{-1}$. The inverse is the precise device that converts the *left* representation $\rho$ into a *right* action on the product, matching the right action on $P$. Drop the inverse and the whole construction collapses at the first step.

**Why the action must be free and proper.** Even granted a right action, the quotient $(P\times V)/G$ is a smooth manifold — and $E\to M$ a genuine bundle — only because the action is free and proper. Freeness of the $G$-action on $P$ (a defining property of a principal bundle) makes the diagonal action on $P\times V$ free: if $(p\cdot g,\rho(g^{-1})v)=(p,v)$ then $p\cdot g=p$, so $g=e$ by freeness on $P$. Properness of the action on $P$ (automatic when $G$ is compact, and part of the principal-bundle data in general) passes to the diagonal action because the $V$-factor is dragged along continuously. With freeness and properness in hand, [[Thm - Free Proper Actions Give Principal Bundles|the free-proper theorem]] delivers the quotient manifold, the submersion to $M$, and the local trivialisations. Were the action merely free but not proper, the quotient could fail to be Hausdorff or to be a manifold at all; freeness alone is the counterexample-rich weakening that the properness clause exists to exclude.

**Why we do not simply take $P\times V$ (the non-example, forward-referenced).** One might hope to skip the quotient and use $P\times V$ itself, or to identify only "along the fibres of $P$" without the $V$-twist. The first is a bundle over $P$, not over $M$, and has the wrong rank and base. The second — quotienting $P\times V$ by $(p,v)\sim(p\cdot g,v)$ with $V$ untouched — is $\big(P/G\big)\times V=M\times V$, the *trivial* bundle, and it forgets $\rho$ entirely; it can never reproduce a non-trivial bundle such as the tautological line bundle $\mathcal O(-1)$, which we exhibit below as a genuinely non-trivial associated bundle. The twist by $\rho(g^{-1})$ is exactly what lets a trivial-looking product carry non-trivial topology. This is the per-clause lesson: remove the inverse and there is no quotient; remove properness and the quotient is not a manifold; remove the $\rho$-twist and the quotient is trivial.

A reader who has internalised these four points could reconstruct the definition unaided: quotient $P\times V$ by the unique right $G$-action extending the right action on $P$, namely $(p,v)\cdot g=(p\cdot g,\rho(g^{-1})v)$, and read off the vector-space and bundle structure from the frames.

---

# The Definition

Let $\pi\colon P\to M$ be a principal $G$-bundle and $\rho\colon G\to GL(V)$ a finite-dimensional representation. Give $P\times V$ the right $G$-action $(p,v)\cdot g=(p\cdot g,\rho(g^{-1})v)$.

> **Definition (associated vector bundle).** The **vector bundle associated with $(P,\rho)$** is the quotient
> $$E=P\times_\rho V:=(P\times V)/G,$$
> equipped with the projection $\pi\colon P\times_\rho V\to M$, $\pi[p,v]=\pi(p)$, the fibrewise vector-space structure of clause (1) below, and the smooth structure and local trivialisations of clause (2) below. Its elements are written $[p,v]=\varpi(p,v)$. When $\rho$ and $V$ need naming we write $E(P,\rho,V)$.

We now verify, clause by clause, that this is a smooth vector bundle of rank $\dim V$.

**Clause 0 — the quotient is a smooth fibre bundle.** The right $G$-action on $P\times V$ is free and proper (shown in the Axiom Motivation from freeness and properness of the action on $P$). We invoke the free-proper theorem in its associated-bundle form.

> [!note]- Restatement of the free-proper theorem (associated-bundle part)
> **Theorem** ([[Thm - Free Proper Actions Give Principal Bundles|free-proper theorem]], second part). Let $\pi\colon P\to M$ be a principal $G$-bundle and let $G$ act smoothly on the left on a manifold $F$. Then the diagonal right action $(p,f)\cdot g=(p\cdot g,\ g^{-1}\cdot f)$ on $P\times F$ is free and proper, the quotient $P\times_G F:=(P\times F)/G$ is a smooth manifold, the map $P\times_G F\to M$, $[p,f]\mapsto\pi(p)$, is a smooth surjective submersion (a fibre bundle with fibre $F$), and for every local section $s\in\Gamma(U;P)$ the map $U\times F\to P\times_G F$, $(m,f)\mapsto[s(m),f]$, is a diffeomorphism onto $\pi^{-1}(U)$.
>
> The complete proof — that the diagonal action inherits freeness and properness, that the quotient manifold theorem applies, and that the section-built maps are diffeomorphisms — is on that page.

Applying the theorem with $F=V$ and the left action $g\cdot v:=\rho(g)v$ (so that the diagonal action is $(p,v)\cdot g=(p\cdot g,\rho(g^{-1})v)$, precisely ours), we conclude that $P\times_\rho V$ is a smooth manifold, that $\pi\colon P\times_\rho V\to M$ is a fibre bundle with fibre $V$, and that each local section $s$ of $P$ over $U$ yields a diffeomorphism $\Phi_s\colon U\times V\to\pi^{-1}(U)$, $\Phi_s(m,v)=[s(m),v]$. It remains only to add the *linear* structure and check that the $\Phi_s$ respect it, which is what promotes the fibre bundle to a vector bundle.

**Clause 1 — the fibres are vector spaces, canonically.** Fix $m\in M$ and a frame $p\in P_m$. Define
$$\iota_p\colon V\to E_m,\qquad \iota_p(v):=[p,v].$$

> [!note]- Proof that $\iota_p$ is a bijection and that the resulting vector-space structure is independent of $p$
> **Goal.** Show that $\iota_p$ is a bijection for each $p\in P_m$, transport the vector-space structure of $V$ through it, and show the transported structure does not depend on the choice of $p\in P_m$; equivalently, that $[p,v]+[p,w]:=[p,v+w]$ and $c\cdot[p,v]:=[p,cv]$ are independent of the representative.
>
> **$\iota_p$ is surjective.** Let $[q,w]\in E_m$, so $\pi(q)=m=\pi(p)$, meaning $q\in P_m$. Since $G$ acts transitively on the fibre $P_m$ (a defining property of a principal bundle), there is $g\in G$ with $q=p\cdot g$. Then $[q,w]=[p\cdot g,w]=[p,\rho(g)w]=\iota_p(\rho(g)w)$, where the middle equality holds because $(p,\rho(g)w)\cdot g=\big(p\cdot g,\ \rho(g^{-1})\rho(g)w\big)=(p\cdot g,w)$ puts $(p,\rho(g)w)$ and $(p\cdot g,w)$ in the same orbit (definition of the equivalence relation; $\rho(g^{-1})\rho(g)=\operatorname{id}$). Hence $\iota_p$ is onto $E_m$.
>
> **$\iota_p$ is injective.** Suppose $\iota_p(v)=\iota_p(w)$, that is $[p,v]=[p,w]$. Then there is $g\in G$ with $(p,w)=(p\cdot g,\rho(g^{-1})v)$; comparing first coordinates gives $p=p\cdot g$, so $g=e$ (by freeness of the $G$-action on $P$), and comparing second coordinates gives $w=\rho(e^{-1})v=v$. Hence $\iota_p$ is injective.
>
> **Transport of structure.** Since $\iota_p\colon V\to E_m$ is a bijection, there is a unique vector-space structure on $E_m$ making $\iota_p$ a linear isomorphism: $\iota_p(v)+\iota_p(w):=\iota_p(v+w)$ and $c\cdot\iota_p(v):=\iota_p(cv)$, i.e. $[p,v]+[p,w]:=[p,v+w]$ and $c[p,v]:=[p,cv]$.
>
> **Independence of the frame $p$.** Let $p'\in P_m$ be another frame; by transitivity $p'=p\cdot g$ for a unique $g\in G$ (unique by freeness). For every $v\in V$,
> $$\iota_{p'}(v)=[p\cdot g,v]=[p,\rho(g)v]=\iota_p\big(\rho(g)v\big)\qquad\text{(definition of the equivalence relation, as in the surjectivity step),}$$
> so $\iota_{p'}=\iota_p\circ\rho(g)$. Because $\rho(g)\in GL(V)$ is a linear isomorphism, $\iota_p$ and $\iota_{p'}$ differ by precomposition with a linear isomorphism, hence induce the *same* vector-space structure on $E_m$: for any $\alpha,\beta\in E_m$, writing $\alpha=\iota_{p'}(v)$, $\beta=\iota_{p'}(w)$, we have $\alpha+\beta=\iota_{p'}(v+w)=\iota_p(\rho(g)(v+w))=\iota_p(\rho(g)v+\rho(g)w)=\iota_p(\rho(g)v)+\iota_p(\rho(g)w)=\alpha+\beta$ computed in the $\iota_p$-structure, and likewise for scalars. Therefore the two structures coincide.
>
> **Conclusion.** Each fibre $E_m$ carries a canonical (frame-independent) vector-space structure isomorphic to $V$, with $\dim E_m=\dim V$. In particular $[p,v]+[p,w]=[p,v+w]$ and $c[p,v]=[p,cv]$ are well defined. $\blacksquare$

**Clause 2 — the local trivialisations are fibrewise-linear diffeomorphisms, so $E$ is a vector bundle of rank $\dim V$.** Let $s\in\Gamma(U;P)$ be a local section over an open $U\subseteq M$. By Clause 0 the map $\Phi_s\colon U\times V\to\pi^{-1}(U)$, $\Phi_s(m,v)=[s(m),v]$, is a diffeomorphism. Its restriction to the fibre over $m$ is $v\mapsto[s(m),v]=\iota_{s(m)}(v)$, which by Clause 1 is a linear isomorphism $V\to E_m$. Hence $\psi_U:=\Phi_s^{-1}\colon\pi^{-1}(U)\to U\times V$ is a diffeomorphism that is linear on each fibre — a **vector-bundle local trivialisation**. Two such trivialisations, from sections $s,s'$ over $U\cap U'$ related by $s'=s\cdot g$ with a transition map $g\colon U\cap U'\to G$, are compared by
$$\psi_{U'}\circ\psi_U^{-1}(m,v)=\psi_{U'}[s(m),v]=\psi_{U'}[s'(m)\cdot g(m)^{-1},v]=\psi_{U'}[s'(m),\rho(g(m))v]=(m,\rho(g(m))v),$$
so the transition functions of $E$ are $m\mapsto\rho(g(m))\in GL(V)$ — smooth, because $g$ is smooth and $\rho$ is smooth. This is exactly the desideratum from the Axiom Motivation: the transition functions of $E$ are $\rho$ applied to the transition functions of $P$. Therefore $E=P\times_\rho V$ is a smooth vector bundle over $M$ of rank $\dim V$.

## Equivalent description: sections as equivariant functions

The frame-dependence encoded in $[p,v]$ can be repackaged as a genuine function on the total space $P$, obeying an equivariance law. This is the description on which every later computation with associated bundles rests.

> **Definition (equivariant function and induced section).** An element $\hat s\in C^\infty(P;V)^G$ is a smooth map $\hat s\colon P\to V$ with $\hat s(p\cdot g)=\rho(g^{-1})\hat s(p)$ for all $p,g$. To it we associate the section $s\in\Gamma(P\times_\rho V)$ characterised by the requirement that the diagram
> $$P\xrightarrow{\ (\operatorname{id},\hat s)\ }P\times V\xrightarrow{\ \varpi\ }P\times_\rho V,\qquad s\circ\pi=\varpi\circ(\operatorname{id},\hat s),$$
> commute; explicitly $s(\pi(p))=[p,\hat s(p)]$.

That the formula $m\mapsto[p,\hat s(p)]$ (any $p\in P_m$) is a well-defined section is a short check, given here in full; the deeper statement that $\hat s\mapsto s$ is a *bijection* — indeed a $C^\infty(M)$-module isomorphism — is proved on its own page and restated where we use it.

> [!note]- Proof that $\hat s\in C^\infty(P;V)^G$ induces a well-defined smooth section $s$
> **Goal.** Show that $p\mapsto\varpi(p,\hat s(p))=[p,\hat s(p)]$ is constant on the fibres of $\pi$, hence descends to a map $s\colon M\to P\times_\rho V$ with $s\circ\pi=\varpi\circ(\operatorname{id},\hat s)$; that $\pi\circ s=\operatorname{id}_M$; and that $s$ is smooth.
>
> **Constant on fibres (uses equivariance).** Let $p\in P$ and $g\in G$. Then
> $$[p\cdot g,\ \hat s(p\cdot g)]=[p\cdot g,\ \rho(g^{-1})\hat s(p)]\qquad(\text{equivariance of }\hat s)$$
> $$=[p,\ \hat s(p)]\qquad(\text{definition of the equivalence relation: }(p,\hat s(p))\cdot g=(p\cdot g,\rho(g^{-1})\hat s(p))).$$
> Thus $\varpi\circ(\operatorname{id},\hat s)$ takes the same value on all points of an orbit $p\cdot G=P_{\pi(p)}$, so it factors through $\pi$: there is a unique set-map $s\colon M\to P\times_\rho V$ with $s\circ\pi=\varpi\circ(\operatorname{id},\hat s)$.
>
> **$s$ is a section.** For any $p$, $\pi(s(\pi(p)))=\pi[p,\hat s(p)]=\pi(p)$, so $\pi\circ s=\operatorname{id}_M$.
>
> **$s$ is smooth.** Smoothness is local, so fix $m_0\in M$ and a local section $t\in\Gamma(U;P)$ with $m_0\in U$; let $\Phi_t\colon U\times V\to\pi^{-1}(U)$ be the trivialisation of Clause 2. For $m\in U$, taking the representative $p=t(m)\in P_m$ gives
> $$s(m)=[t(m),\hat s(t(m))]=\Phi_t\big(m,\hat s(t(m))\big),$$
> so in the trivialisation, $\psi_U\circ s(m)=(m,\hat s(t(m)))$. The map $m\mapsto\hat s(t(m))=\hat s\circ t(m)$ is smooth, being a composite of the smooth maps $t\colon U\to P$ and $\hat s\colon P\to V$. Hence $s$ is smooth on $U$, and since $m_0$ was arbitrary, $s\in\Gamma(P\times_\rho V)$. $\blacksquare$

> [!note] The bijection $C^\infty(P;V)^G\cong\Gamma(P\times_\rho V)$
> The assignment $\hat s\mapsto s$ is a bijection, and a $C^\infty(M)$-module isomorphism; the inverse sends a section $s$ to the function $\hat s(p):=$ the unique $v\in V$ with $s(\pi(p))=[p,v]$ (unique by Clause 1). The complete proof — including equivariance of the inverse and its smoothness — is on [[Thm - Sections of an Associated Bundle are Equivariant Functions|the equivariant-sections theorem]] and is restated wherever we need it. We use only the well-definedness proved above until that theorem is invoked.

## The general associated fibre and principal bundle

Nothing above used that $V$ is a vector space beyond Clause 1; the quotient construction works for any smooth left $G$-space, and specialises to a principal bundle when the fibre is a group.

> **Definition (associated fibre bundle; associated principal bundle).** Let $\pi\colon P\to M$ be a principal $G$-bundle.
> 1. If $G$ acts smoothly on the left on a manifold $F$, the **associated fibre bundle with fibre $F$** is $P\times_G F:=(P\times F)/G$ for the diagonal action $(p,f)\cdot g=(p\cdot g,\ g^{-1}\cdot f)$, a fibre bundle over $M$ with fibre $F$ (Clause 0). The associated vector bundle is the case $F=V$, $g\cdot v=\rho(g)v$.
> 2. If $\varphi\colon G\to H$ is a Lie-group homomorphism, let $G$ act on $H$ on the left by $g\cdot h=\varphi(g)h$. The **associated principal $H$-bundle** is
> $$P\times_\varphi H:=(P\times H)/G,\qquad (p,h)\cdot g=(p\cdot g,\ \varphi(g^{-1})\,h),$$
> with the right $H$-action $[p,h]\cdot h'=[p,hh']$ and projection $[p,h]\mapsto\pi(p)$. It is a principal $H$-bundle (proved on [[Thm - Free Proper Actions Give Principal Bundles|the free-proper theorem]] page and, for the general structure group, restated where used). When $\varphi$ is the inclusion of a subgroup, passing from $P$ to $P\times_\varphi H$ is **extension of the structure group**; a $G$-bundle whose extension is isomorphic to a given $H$-bundle $Q$ is a **reduction** of $Q$ to $G$ (see [[Def - Reduction and Extension of the Structure Group|reduction and extension]]).

The right $H$-action $[p,h]\cdot h'=[p,hh']$ is well defined because it commutes with the $G$-action being quotiented: $\big((p,h)\cdot g\big)$ then right-multiplied by $h'$ is $(p\cdot g,\varphi(g^{-1})h\,h')$, the same orbit as $(p,hh')\cdot g$. This is exactly the datum Bär records (Definition 2.2.10, p. 44), restated here in the series' notation.

---

# Categorical / Structural Definition

The associated-bundle construction is a **functor**, and this is the cleanest way to see why it commutes with every linear-algebra operation.

Fix the principal bundle $P\to M$. Let $\operatorname{Rep}(G)$ be the category whose objects are finite-dimensional representations $\rho\colon G\to GL(V)$ and whose morphisms $T\colon(V,\rho)\to(W,\sigma)$ are $G$-**equivariant** linear maps, meaning $T\circ\rho(g)=\sigma(g)\circ T$ for all $g\in G$; let $\operatorname{Vect}(M)$ be the category of smooth vector bundles over $M$ and bundle maps covering the identity. Define
$$P\times_G(-)\colon\operatorname{Rep}(G)\longrightarrow\operatorname{Vect}(M),\qquad (V,\rho)\mapsto P\times_\rho V,\quad T\mapsto\big(P\times_G T\big),$$
where $P\times_G T\colon P\times_\rho V\to P\times_\sigma W$ is $[p,v]\mapsto[p,Tv]$.

> [!note]- Verification that $P\times_G T$ is well defined, linear, smooth, and functorial
> **Well defined (uses equivariance of $T$).** If $[p,v]=[p',v']$, then $p'=p\cdot g$ and $v'=\rho(g^{-1})v$ for some $g$; then $[p',Tv']=[p\cdot g,\ T\rho(g^{-1})v]=[p\cdot g,\ \sigma(g^{-1})Tv]$ (equivariance $T\rho(g^{-1})=\sigma(g^{-1})T$) $=[p,Tv]$ (definition of the equivalence relation for $\sigma$). So the value depends only on the class.
>
> **Fibrewise linear.** On the fibre over $m$, $P\times_G T$ is $\iota^\sigma_p\circ T\circ(\iota^\rho_p)^{-1}$ for any $p\in P_m$ (where $\iota^\rho_p(v)=[p,v]$ in $P\times_\rho V$ and likewise $\iota^\sigma_p$), a composite of linear maps, hence linear.
>
> **Smooth.** In trivialisations from a common local section $s$, $P\times_G T$ reads $(m,v)\mapsto(m,Tv)$, smooth because $T$ is a fixed linear map.
>
> **Functorial.** $P\times_G\operatorname{id}_V=\operatorname{id}_{P\times_\rho V}$ and $P\times_G(T'\circ T)=(P\times_G T')\circ(P\times_G T)$ are immediate from $[p,v]\mapsto[p,Tv]$. $\blacksquare$

This functor is **additive and monoidal**: it carries $\oplus$, $\otimes$, duals, and $\Lambda^p$ of representations to the corresponding operations on the associated bundles, because a natural isomorphism such as $P\times_\rho V\oplus P\times_\sigma W\cong P\times_{\rho\oplus\sigma}(V\oplus W)$ is $[p,v]\oplus[p,w]\mapsto[p,(v,w)]$, well defined by the same equivariance check. These identifications are the content of [[Thm - Vector Bundles are Associated to Their Frame Bundles|the frame-bundle theorem]], where each is proved.

**The principal bundle as the universal frame.** The construction has a universal-property reading. The quotient map $\varpi\colon P\times V\to P\times_\rho V$ is the universal $G$-invariant smooth map out of $P\times V$: for any manifold $N$, precomposition with $\varpi$ is a bijection
$$\{\text{smooth }f\colon P\times_\rho V\to N\}\ \xrightarrow{\ \sim\ }\ \{\text{smooth }F\colon P\times V\to N\ \text{with } F\circ R_g=F\ \forall g\in G\},\qquad f\mapsto f\circ\varpi,$$
since $\varpi$ is a surjective submersion whose fibres are exactly the $G$-orbits (this is the defining property of the quotient by a free proper action, from [[Thm - Free Proper Actions Give Principal Bundles|the free-proper theorem]]). Concretely, a principal bundle is a "bundle of frames without a preferred fibre model": once a representation $V$ is chosen, $P\times_\rho V$ *is* the bundle whose sections are $V$-valued fields in every gauge at once, and the equivariant-function description $C^\infty(P;V)^G$ is the same statement — a field is a rule assigning components to every frame, transforming by $\rho$ between frames. Taking $P=\operatorname{Fr}(E)$ the frame bundle of a vector bundle $E$ and $\rho$ the standard representation recovers $E$ itself, so every vector bundle is $\operatorname{Fr}(E)\times_{GL}\mathbb R^k$: the principal bundle is the universal frame from which all associated bundles are cut.

---

# Relate to Other Fields / Compression

**True name.** Operationally, the associated bundle is "the representation $V$, attached to the frame data $P$, glued by $\rho$". A section of $P\times_\rho V$ is neither more nor less than a $\rho$-equivariant function $\hat s\colon P\to V$ (the description above): a $V$-valued quantity written in every gauge, with the gauge-change law $\hat s(p\cdot g)=\rho(g^{-1})\hat s(p)$ built in. This is the definition in the form one actually computes with; the quotient $[p,v]$ is the coordinate-free packaging of the same data.

In gauge theory this is the home of **matter fields**: a Yang–Mills field in a representation $V$ of the structure group is a section of the associated bundle $P\times_\rho V$, and the covariant derivative of chapter IV acts on exactly these sections. When $\rho$ is the **adjoint representation** on $\mathfrak g$ one obtains the bundle $\operatorname{ad}P=P\times_{\operatorname{Ad}}\mathfrak g$ in which the curvature of a principal connection lives, and when $\rho$ is conjugation of $G$ on itself one obtains $\operatorname{Ad}P=P\times_\alpha G$ whose sections are the gauge transformations (see [[Def - Adjoint Bundles ad P and Ad P|the adjoint-bundle definitions]]).

The construction recurs across geometry. **Homogeneous vector bundles**: for a closed subgroup $H\le G$, the coset projection $G\to G/H$ is a principal $H$-bundle, and $G\times_\rho V\to G/H$ for a representation $\rho$ of $H$ is the associated homogeneous bundle — the natural bundles on a symmetric space. **Flat bundles and monodromy**: for the universal cover $\widetilde M\to M$, a principal $\pi_1(M)$-bundle, and a representation $\rho\colon\pi_1(M)\to GL(V)$, the associated bundle $\widetilde M\times_\rho V$ is the flat bundle with holonomy $\rho$, the geometric form of a linear representation of the fundamental group. **Tensor and spinor fields**: every tensor bundle on a Riemannian manifold is associated to the orthonormal frame bundle via a representation of $O(n)$, and spinor bundles are associated to a spin structure via a representation of $\operatorname{Spin}(n)$ (chapter VIII). The single compression is that *all natural bundles of a geometry are associated bundles of one principal bundle*, and choosing the geometry is choosing the structure group.

---

# Examples / Corollaries

**Is an instance — the trivial principal bundle gives the trivial vector bundle.** Let $P=M\times G$ with the right action $(m,g)\cdot h=(m,gh)$ and $\pi(m,g)=m$; this is the trivial principal bundle. Then $P\times_\rho V\cong M\times V$.

> [!note]- Verification, clause by clause
> Define $\Psi\colon P\times_\rho V\to M\times V$ by $\Psi[(m,g),v]=(m,\rho(g)v)$.
> **Well defined (uses the equivalence relation).** If $[(m,g),v]=[(m',g'),v']$, then $(m',g',v')=(m,g,v)\cdot h=(m,gh,\rho(h^{-1})v)$ for some $h\in G$; so $m'=m$, $g'=gh$, $v'=\rho(h^{-1})v$, and $\rho(g')v'=\rho(gh)\rho(h^{-1})v=\rho(g)v$ (homomorphism property $\rho(gh)\rho(h^{-1})=\rho(g)$). Hence $\Psi$ is independent of the representative.
> **Fibrewise linear.** For fixed $(m,g)$, $v\mapsto(m,\rho(g)v)$ is linear, and $\rho(g)\in GL(V)$, so it is a linear isomorphism $V\to\{m\}\times V$.
> **Smooth with smooth inverse.** $\Psi$ is smooth because it lifts to the smooth map $(m,g,v)\mapsto(m,\rho(g)v)$ on $P\times V$ and descends through the submersion $\varpi$. Its inverse is $(m,v)\mapsto[(m,e),v]$, smooth as $\varpi\circ(m,v)\mapsto((m,e),v)$.
> **Conclusion.** $\Psi$ is a fibrewise-linear diffeomorphism covering $\operatorname{id}_M$, hence a vector-bundle isomorphism $P\times_\rho V\cong M\times V$. $\blacksquare$

**Is an instance — the tautological line bundle $\mathcal O(-1)$ over $\mathbb{CP}^n$.** Take the Hopf bundle $\pi\colon S^{2n+1}\to\mathbb{CP}^n$, $z\mapsto[z]$, with the right $U(1)$-action $z\cdot\lambda=z\lambda$ (see [[Def - The Hopf Bundle|the Hopf bundle]]), and the one-dimensional representation $\varrho_1\colon U(1)\to GL(\mathbb C)=\mathbb C^\times$, $\varrho_1(\lambda)w=\lambda w$. Then $S^{2n+1}\times_{\varrho_1}\mathbb C$ is a complex line bundle, and the map $[z,w]\mapsto([z],wz)$ realises it as the tautological line bundle
$$\mathcal O(-1)=\big\{([z],u)\in\mathbb{CP}^n\times\mathbb C^{n+1}\ \big|\ u\in\mathbb C z\big\},$$
whose fibre over $[z]$ is the complex line $\mathbb C z\subseteq\mathbb C^{n+1}$ that $[z]$ represents.

> [!note]- Verification that the map is well defined and lands in the tautological line
> Define $\Theta\colon S^{2n+1}\times_{\varrho_1}\mathbb C\to\mathbb{CP}^n\times\mathbb C^{n+1}$ by $\Theta[z,w]=([z],wz)$, where $wz\in\mathbb C^{n+1}$ is the scalar $w$ times the vector $z$.
> **Well defined (uses the equivalence relation and commutativity of $\mathbb C$).** A general representative of $[z,w]$ is $(z,w)\cdot\lambda=(z\lambda,\varrho_1(\lambda^{-1})w)=(z\lambda,\lambda^{-1}w)$ for $\lambda\in U(1)$. Its image is $\big([z\lambda],(\lambda^{-1}w)(z\lambda)\big)=\big([z],\ \lambda^{-1}w\lambda\,z\big)=\big([z],wz\big)$, using $[z\lambda]=[z]$ and that scalars commute so $\lambda^{-1}w\lambda=w$. Hence $\Theta$ is independent of the representative.
> **Image lies in $\mathcal O(-1)$.** $wz$ is a complex scalar multiple of $z$, so $wz\in\mathbb C z$; thus $([z],wz)\in\mathcal O(-1)$.
> **It is an isomorphism.** That $\Theta$ is a smooth isomorphism of complex line bundles onto $\mathcal O(-1)$ — in particular fibrewise complex-linear and bijective — is worked out in full on [[Ex - The Tautological Line Bundle over CP^n is Associated to the Hopf Bundle|the tautological-line-bundle exercise]]; the representation is exactly $\varrho_1$, as the well-definedness computation above already pins down. $\blacksquare$

This is the promised genuinely non-trivial associated bundle: $\mathcal O(-1)$ is not isomorphic to the trivial line bundle (it has non-zero first Chern number), even though it is cut from the trivial product $\mathbb{CP}^n\times\mathbb C^{n+1}$ — the twist by $\varrho_1$ carries all the topology.

**Is an instance — tensor powers of a line bundle.** Let $P\to M$ be any principal $U(1)$-bundle and, for $k\in\mathbb Z$, let $\varrho_k\colon U(1)\to\mathbb C^\times$, $\varrho_k(\lambda)w=\lambda^k w$, be the weight-$k$ representation (these are all the irreducible complex representations of $U(1)$; see [[Thm - Complex Representations of U(1) and SU(2)|the classification of representations]]). Then $P\times_{\varrho_k}\mathbb C$ is a complex line bundle (rank $\dim_{\mathbb C}\mathbb C=1$, by Clause 2), and, writing $L:=P\times_{\varrho_1}\mathbb C$, there is a canonical isomorphism $P\times_{\varrho_k}\mathbb C\cong L^{\otimes k}$ (with $L^{\otimes(-1)}=L^*$ and $L^{\otimes 0}=M\times\mathbb C$).

> [!note]- Verification that $P\times_{\varrho_k}\mathbb C$ is a line bundle, and the tensor-power identification
> By the definition, $P\times_{\varrho_k}\mathbb C$ is the associated vector bundle for the representation $\varrho_k$ on $\mathbb C$; by Clause 2 it is a smooth complex vector bundle of rank $\dim_{\mathbb C}\mathbb C=1$, that is, a line bundle, with transition functions $m\mapsto\varrho_k(g_{\alpha\beta}(m))=g_{\alpha\beta}(m)^k$ where $g_{\alpha\beta}\colon U_\alpha\cap U_\beta\to U(1)$ are the transition functions of $P$. Since the transition functions of a $k$-fold tensor product multiply, $L^{\otimes k}$ has transition functions $g_{\alpha\beta}^k$ as well; the induced fibrewise map $L^{\otimes k}\to P\times_{\varrho_k}\mathbb C$ agreeing on the trivialising cover is therefore a well-defined isomorphism. The section-level form of this identification (weight-$k$ equivariant functions are sections of $L^{\otimes k}$) is proved on [[Ex - Sections of the Tensor Powers of a Line Bundle as Equivariant Functions|the tensor-powers exercise]]. $\blacksquare$

**Is NOT an instance — the naive action $(p\cdot g,\rho(g)v)$.** Setting $(p,v)\bullet g:=(p\cdot g,\rho(g)v)$ (without the inverse) does *not* in general define a right $G$-action, so there is no quotient bundle of the intended type. As computed in the Axiom Motivation, $\big((p,v)\bullet g\big)\bullet h=(p\cdot gh,\rho(hg)v)$ while $(p,v)\bullet(gh)=(p\cdot gh,\rho(gh)v)$, and these disagree whenever $\rho(hg)\ne\rho(gh)$.

> [!note]- A concrete witness of failure and what the correct object is
> Take $G=GL_2(\mathbb R)$ and $\rho=\operatorname{id}$ its defining representation on $V=\mathbb R^2$. Choose $g=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ and $h=\begin{pmatrix}1&0\\1&1\end{pmatrix}$; then $gh=\begin{pmatrix}2&1\\1&1\end{pmatrix}$ and $hg=\begin{pmatrix}1&1\\1&2\end{pmatrix}$ are different matrices, so $\rho(gh)\ne\rho(hg)$ and $\bullet$ violates the associativity axiom of a right action. Thus $(P\times V,\bullet)$ has no well-defined orbit space of the required kind. If one *insists* on the formula $[p,v]\cdot g=[p\cdot g,\rho(g)v)]$ as a right action, one is forced to read $g\mapsto\rho(g)$ as a right action of $G$, i.e. an *anti*-homomorphism, which is the same as the associated bundle of the contragredient representation $\rho^{\mathrm{op}}(g)=\rho(g^{-1})^{\mathsf T}$; this is a different bundle (the dual $E^*$), not $E$. The lesson of the definition is that the inverse in $\rho(g^{-1})$ is not cosmetic. $\blacksquare$

**Calibration check.** Three quick verifications from what is on the page. First, $\operatorname{rank}(P\times_\rho V)=\dim V$: immediate from Clause 1, since each fibre $E_m\cong V$ via $\iota_p$. Second, for the **trivial representation** $\rho\equiv\operatorname{id}_V$ (that is, $\rho(g)=\operatorname{id}$ for all $g$), $P\times_{\operatorname{triv}}V\cong M\times V$ for *every* principal bundle $P$: the action is $(p,v)\cdot g=(p\cdot g,v)$, so the quotient is $(P/G)\times V=M\times V$, the trivial bundle — the $\rho$-twist has been switched off. Third, taking $P=\operatorname{Fr}(E)$ the frame bundle of a rank-$k$ bundle $E$ and $\rho$ the standard representation of $GL_k$ on $\mathbb R^k$ recovers $E$, $\operatorname{Fr}(E)\times_{\operatorname{std}}\mathbb R^k\cong E$ (proved on [[Thm - Vector Bundles are Associated to Their Frame Bundles|the frame-bundle theorem]]); this is the consistency check that the construction inverts the passage from a vector bundle to its frames.

---

# Unlocked by This

> [!tip] Adjoint bundles ad P and Ad P *(from this chapter)*
> The representations most used in gauge theory are the adjoint ones: $\operatorname{ad}P=P\times_{\operatorname{Ad}}\mathfrak g$, a vector bundle carrying the curvature of a principal connection, and $\operatorname{Ad}P=P\times_\alpha G$ (conjugation on $G$), a bundle of groups whose sections are the gauge transformations. Both are associated bundles; see [[Def - Adjoint Bundles ad P and Ad P|the adjoint-bundle definitions]].

> [!tip] Sections are equivariant functions *(from this chapter)*
> The bijection $C^\infty(P;V)^G\cong\Gamma(P\times_\rho V)$ turns every question about sections of an associated bundle into a question about equivariant functions on $P$, where the group action is explicit; this is the computational engine for the rest of the theory. See [[Thm - Sections of an Associated Bundle are Equivariant Functions|the equivariant-sections theorem]].

> [!tip] Bundle-valued forms as basic equivariant forms *(from this chapter)*
> The same repackaging upgrades from functions to differential forms: $\Omega^q(M;P\times_\rho V)\cong\Omega^q_{\mathrm{bas}}(P;V)^G$, the identity that lets curvature and Chern–Weil forms be computed upstairs on $P$ and descend to $M$. See [[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space|the basic-forms theorem]].

> [!tip] Induced connections and covariant derivatives *(from Gauge Theory IV)*
> A connection on the principal bundle $P$ induces, through the representation $\rho$, a covariant derivative on **every** associated bundle $P\times_\rho V$ at once — the mechanism by which one gauge field differentiates all matter fields. This is developed in **Connections on Associated Bundles and Induced Covariant Derivatives** in chapter IV.
