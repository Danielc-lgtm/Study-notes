---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Sphere Bundles and Mapping Tori"
  - "Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map"
  - "Def - Fibre Bundle"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $F$ is a smooth manifold and $\phi\colon F\to F$ is a [[Def - Diffeomorphism|diffeomorphism]]. The group $\mathbb{Z}$ of integers acts on the product manifold $\mathbb{R}\times F$ on the left by
$$k\cdot(t,f) := (t+k,\ \phi^{k}(f)),\qquad k\in\mathbb{Z},\ (t,f)\in\mathbb{R}\times F,$$
where $\phi^{k}$ is the $k$-fold composite of $\phi$ (with $\phi^{0}=\operatorname{id}_{F}$ and $\phi^{-1}$ the inverse diffeomorphism). This is the action introduced on [[Def - Sphere Bundles and Mapping Tori|the mapping-torus definition page]]; it is smooth, free, and properly discontinuous. The **mapping torus** of $\phi$ is the orbit space
$$E_{\phi} := \mathbb{Z}\backslash(\mathbb{R}\times F),$$
and $q\colon\mathbb{R}\times F\to E_{\phi}$ denotes the quotient map, $q(t,f)=[t,f]$ (so $[t,f]=[t+k,\phi^{k}(f)]$ for every $k\in\mathbb{Z}$). We write $p\colon\mathbb{R}\to S^{1}:=\mathbb{Z}\backslash\mathbb{R}$ for the quotient of the translation action $k\cdot t=t+k$ (the mapping torus of the identity of a one-point fibre), $p(t)=[t]$; it is a smooth covering map and we identify $S^{1}$ with $\mathbb{Z}\backslash\mathbb{R}$. The projection
$$\pi\colon E_{\phi}\to S^{1},\qquad \pi([t,f])=[t],$$
is induced by $\operatorname{pr}_{1}\colon\mathbb{R}\times F\to\mathbb{R}$, $\operatorname{pr}_{1}(t,f)=t$, followed by $p$.

A [[Def - Fibre Bundle|fibre bundle with typical fibre $F$]] is a triple $(E,\pi,B)$ with $E,B,F$ smooth manifolds and $\pi\colon E\to B$ a surjective smooth map such that every point of $B$ has an open neighbourhood $U$ carrying a **local trivialisation**, a diffeomorphism $\psi_{U}\colon\pi^{-1}(U)\to U\times F$ with $\operatorname{pr}_{1}\circ\psi_{U}=\pi|_{\pi^{-1}(U)}$. The bundle is **trivial** if it is isomorphic (over $\operatorname{id}_{B}$) to the product $(B\times F,\operatorname{pr}_{1},B)$, equivalently if it admits a global trivialisation over $U=B$. We write $\operatorname{Diff}(F)$ for the group of diffeomorphisms of $F$ under composition. An **isotopy** from $\operatorname{id}_{F}$ to $\phi$ **through diffeomorphisms** is a smooth map $\Phi\colon[0,1]\times F\to F$ such that each $\phi_{s}:=\Phi(s,\cdot)$ is a diffeomorphism of $F$, with $\phi_{0}=\operatorname{id}_{F}$ and $\phi_{1}=\phi$; here "smooth on $[0,1]\times F$" means smooth on an open neighbourhood of $[0,1]\times F$ in $\mathbb{R}\times F$.

> [!warning] Convention: the sign of the twist
> With Bär's action $k\cdot(t,f)=(t+k,\phi^{k}(f))$, the seam of the mapping torus glues the fibre over $[0]$ to the fibre over $[1]$ by $\phi$ itself: passing to the representative window $[0,1]\times F$, the relation $(t,f)\sim(t+1,\phi(f))$ specialises at $t=0$ to $(0,f)\sim(1,\phi(f))$. Some texts write the action as $(t,f)\mapsto(t-k,\phi^{k}(f))$ or glue by $\phi^{-1}$; the resulting bundle is isomorphic (replace $\phi$ by $\phi^{-1}$, equivalently reverse the orientation of $\mathbb{R}$), and every occurrence of $\phi$ below is the diffeomorphism that appears in the gluing $(0,f)\sim(1,\phi(f))$.

---

# Statement

> **Theorem (mapping tori are circle bundles).** Let $F$ be a smooth manifold and $\phi\colon F\to F$ a diffeomorphism, and form the mapping torus $E_{\phi}=\mathbb{Z}\backslash(\mathbb{R}\times F)$ with the projection $\pi\colon E_{\phi}\to S^{1}=\mathbb{Z}\backslash\mathbb{R}$, $\pi([t,f])=[t]$. Then:
>
> **(I) Local triviality.** $(E_{\phi},\pi,S^{1})$ is a fibre bundle with typical fibre $F$. Explicitly, over the two arcs
> $$U_{1}=S^{1}\setminus\{[0]\},\qquad U_{2}=S^{1}\setminus\{[\tfrac12]\},$$
> which cover $S^{1}$, there are local trivialisations $\psi_{1},\psi_{2}$; the transition map $\psi_{2}\circ\psi_{1}^{-1}$ on the two components of $U_{1}\cap U_{2}$ is the identity on the "interior" arc $p\big((\tfrac12,1)\big)$ and the fibre diffeomorphism $\phi$ on the "seam" arc $p\big((0,\tfrac12)\big)$.
>
> **(II) The triviality criterion, sufficiency.** If $\phi$ is isotopic to $\operatorname{id}_{F}$ through diffeomorphisms, then $(E_{\phi},\pi,S^{1})$ is trivial: there is a bundle isomorphism $E_{\phi}\cong S^{1}\times F$ over $\operatorname{id}_{S^{1}}$.

The two parts of the criterion form a biconditional, of which only the sufficiency (II) is established here. The converse — **if $E_{\phi}$ is trivial then $\phi$ is isotopic to the identity through diffeomorphisms** — is the *only-if* direction; it requires the homotopy invariance of bundles over the circle and is proved in §3.5 as a corollary of the clutching construction, on the page **Thm - Clutching Construction for Bundles over a Closed Manifold**. It is stated here only to complete the picture and is not used below.

---

# Motivation

The mapping torus is the standard machine for turning a single self-map into a space one dimension higher, and Part I says the machine always outputs a fibre bundle. This matters for three reasons that recur throughout the chapter.

First, it is the elementary example that separates "fibre bundle" from "product". A product $S^{1}\times F$ is what one draws when the fibre never moves as the base point travels around the circle; the mapping torus is what one gets when the fibre is instructed to undergo the diffeomorphism $\phi$ over the course of one loop. Because $S^{1}$ is not simply connected, this instruction cannot always be undone, and the mapping torus is the exact record of the obstruction. The Möbius strip ($F=(-1,1)$, $\phi=-\operatorname{id}$) and the Klein bottle ($F=S^{1}$, $\phi$ a reflection) are the first two non-trivial bundles the reader meets, and both are mapping tori; the theorem is what licences calling them bundles at all.

Second, it is the prototype for the entire chapter's method of assembling a bundle from trivial pieces by gluing. Part I builds $E_{\phi}$ from two product charts over arcs and records the twist in a single transition map. This is precisely the cocycle description of §3.3 in its smallest instance: one overlap, one non-trivial transition, the diffeomorphism $\phi$. Reading the proof of Part I is the cheapest way to see why the [[Thm - Principal Bundles are Classified by Cocycles|cocycle classification of bundles]] is true before meeting it in generality.

Third, Part II is the first appearance of the untwisting argument that underlies homotopy invariance of bundles. The statement "$\phi$ isotopic to $\operatorname{id}$ implies $E_{\phi}$ trivial" is the assertion that a fibre map deformable to the identity carries no twist. The proof does the deformation explicitly, threading the isotopy parameter through the base coordinate so that the accumulated twist is continuously unwound. The same idea, run over a general base rather than the circle, becomes the theorem that **homotopic maps pull back isomorphic bundles**, which drives the classification in §3.5–§3.6.

We assume the reader knows what a fibre bundle is (from [[Def - Fibre Bundle|the definition page]]) and that a properly discontinuous action of a discrete group has a smooth manifold quotient with the quotient map a covering — both are recalled at the point of use.

---

# Sources and Targets

**Sources (Input Broadening).** The theorem's literal hypothesis is mild: a manifold $F$ and a diffeomorphism $\phi$. The skill is recognising when a space handed to you *is* a mapping torus, so that Part I immediately makes it a bundle and Part II tests its triviality.

The first disguised source is **a manifold presented as a quotient of a cylinder $\mathbb{R}\times F$ (or $[0,1]\times F$) by a shift-and-fibre-map rule.** Whenever a construction glues the two ends of a cylinder $[0,1]\times F$ by a map $g\colon F\to F$, or quotients $\mathbb{R}\times F$ by $(t,f)\mapsto(t+1,g(f))$, that space is the mapping torus $E_{g}$ — provided the gluing map $g$ is a diffeomorphism. The non-obvious bridge is exactly this proviso: one must check that $g$ is smooth with smooth inverse, because if $g$ is merely continuous the quotient is only a topological bundle, and if $g$ fails to be injective the fibre dimension can jump and the quotient is not a bundle at all (this is the non-example on the definition page). *Example problem:* the total space of the tangent bundle of the Klein bottle, presented as $[0,1]\times(\mathbb{R}^{2}/\Gamma)$ with the ends glued by the differential of the reflection, is a mapping torus and hence a fibre bundle over $S^{1}$.

The second disguised source is **the suspension of a discrete dynamical system.** A diffeomorphism $\phi\colon F\to F$ is a discrete-time dynamical system; its *suspension* is the flow on $E_{\phi}$ that translates the $\mathbb{R}$-coordinate. Whenever one wishes to convert an iterated map into a continuous-time flow — to apply the tools of continuous dynamics to the study of $\phi$ — the phase space of the resulting flow is a mapping torus, and Part I guarantees it fibres over the circle with the flow transverse to the fibres. The bridge is that the return map of the suspension flow to a single fibre recovers $\phi$, so no dynamical information is lost. *Example problem:* the geodesic flow's first-return structure on a surface, or the suspension of an Anosov diffeomorphism of the torus, both live on mapping tori and inherit the bundle projection.

The third disguised source is **a fibre bundle over $S^{1}$ given by an abstract clutching datum.** Any fibre bundle over $S^{1}$ with fibre $F$ is, up to isomorphism, a mapping torus: cover $S^{1}$ by two arcs, trivialise over each, and the single essential transition function on one overlap component is a map $S^{0}$-worth of data into $\operatorname{Diff}(F)$, i.e. a diffeomorphism $\phi$. The bridge is Part I read backwards together with the cocycle theorem: a bundle over $S^{1}$ is determined by its clutching diffeomorphism, and reconstituting it as $E_{\phi}$ is exactly Part I. *Example problem:* classify all rank-one real vector bundles over $S^{1}$ by observing that the clutching map lands in $\operatorname{GL}_{1}(\mathbb{R})=\mathbb{R}^{\times}$, whose two components give the trivial bundle and the Möbius bundle.

**Targets (Output Amplification).** The bare conclusion is "$E_{\phi}$ is a bundle, trivial when $\phi\simeq\operatorname{id}$". Combined with other facts it does much more.

Combine Part II with **the classification of $\operatorname{Diff}(F)$ up to isotopy — the mapping class group $\pi_{0}\operatorname{Diff}(F)$.** Part II says the isomorphism class of $E_{\phi}$ depends only on the isotopy class of $\phi$; the (deferred) converse says it depends on *exactly* that. Together they give a bijection between isomorphism classes of $F$-bundles over $S^{1}$ and conjugacy classes in $\pi_{0}\operatorname{Diff}(F)$. The payoff is a complete classification of circle bundles from a purely group-theoretic invariant of the fibre. The extra ingredient is the group structure of $\pi_{0}\operatorname{Diff}(F)$, computed case by case.

Combine Part I with **an orientation of the fibre and of the base to test orientability of the total space.** If $F$ is oriented, then $E_{\phi}$ is orientable if and only if $\phi$ preserves the orientation of $F$: the two charts $U_{i}\times F$ are oriented by the product orientation, and the transition map is the identity times $\phi$, whose Jacobian sign on the seam arc is the sign with which $\phi$ acts on the orientation. The payoff is an instant orientability criterion. The extra ingredient is the [[Def - Orientation of a Smooth Manifold|orientation]] machinery of DG IX; this is exactly what makes the Klein bottle ($\phi$ orientation-reversing on $S^{1}$) non-orientable and hence non-trivial.

Combine Part I with **a fibrewise geometric structure preserved by $\phi$ to descend that structure to the total space.** If $\phi$ is an isometry of a Riemannian metric on $F$, the metric on $\mathbb{R}\times F$ (product of the standard metric on $\mathbb{R}$ with that on $F$) is $\mathbb{Z}$-invariant and descends to $E_{\phi}$, making $\pi$ a Riemannian submersion with totally geodesic fibres. The payoff is a supply of homogeneous-looking metrics on non-trivial bundles. The extra ingredient is the invariance check, which is where the hypothesis that $\phi$ is a diffeomorphism (indeed an isometry) is spent.

---

# Why Is It True

Picture the cylinder $\mathbb{R}\times F$ as an infinite stack of copies of $F$, one over each real number $t$. The group $\mathbb{Z}$ acts by sliding the stack one notch to the right and simultaneously applying $\phi$ to the fibre. Rolling the real line into the circle $S^{1}=\mathbb{Z}\backslash\mathbb{R}$ identifies the copy of $F$ over $t$ with the copy over $t+1$, but only after twisting it by $\phi$. The mapping torus is the result: a circle of copies of $F$, seamless everywhere except across the one point $[0]$ where the identification carries the extra twist $\phi$.

Now the bundle structure is forced. Away from any single point of the circle, we are looking at a genuine interval of the real line, over which the stack is an honest product $I\times F$ — no identifications happen inside an interval shorter than one full turn, because two points of such an interval never differ by an integer. So over the arc $U_{1}=S^{1}\setminus\{[0]\}$ the mapping torus is literally $U_{1}\times F$, and over the complementary arc $U_{2}=S^{1}\setminus\{[\tfrac12]\}$ it is $U_{2}\times F$. These two product pieces cover the circle, and that is the local triviality. When we compare the two trivialisations on their overlap, they agree on the arc that misses the seam and differ by $\phi$ on the arc that crosses it.

> A mapping torus is a cylinder whose two ends have been glued by $\phi$; away from the seam it is a product, and the entire twist is the single transition diffeomorphism $\phi$ living on the one arc that crosses the seam.

Part II is the statement that if the gluing map $\phi$ can be *slid back* to the identity through diffeomorphisms, the twist can be combed out. Imagine walking once around the circle. If, as you walk, you continuously apply more and more of the reverse isotopy $\phi_{s}^{-1}$ — none of it at the start, all of it by the time you return — then the twist you accumulate exactly cancels the twist $\phi$ built into the seam, and what remains is an untwisted product. The proof makes "how far along the isotopy you are" a smooth function of the base coordinate $t$, and the requirement that the correction wraps up to exactly $\phi^{-1}$ over one period is precisely the recursion $\alpha_{t+1}=\alpha_{t}\circ\phi^{-1}$ that the untwisting family must satisfy.

---

# What Makes This Hard

Three steps are easy to get wrong. The first is the injectivity that makes a chart: it is *not* true that any product $I\times F$ maps injectively into $E_{\phi}$ — only intervals $I$ of length at most one do, because on a longer interval two points can differ by an integer and be identified. Choosing arcs of length exactly one, and proving that the covering map restricts to a diffeomorphism there, is the whole content of local triviality. The second is smoothness of the untwisting in Part II: the naïve family $\alpha_{t}=\phi_{t}^{-1}$ has the right values at the integers but generally the wrong derivatives there, so the family assembled over $\mathbb{R}$ has corners at every integer. One must first reparametrise the isotopy to be constant near its endpoints, a standard but essential smoothing. The third is the hypothesis "isotopic **through diffeomorphisms**": mere homotopy of $\phi$ to $\operatorname{id}$ is not enough — the intermediate maps must all be invertible, or the descended map fails to be a diffeomorphism. On the interval $F=(-1,1)$ the map $\phi=-\operatorname{id}$ is homotopic to the identity but not isotopic to it through diffeomorphisms, and that is exactly why the Möbius strip is non-trivial.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** For Part I, cut the circle into two arcs of length one; over each, the covering map $q$ restricts to a diffeomorphism from an interval-times-fibre onto the preimage arc, and its inverse is the trivialisation. For Part II, build a smooth family of "corrections" $\alpha_{t}\in\operatorname{Diff}(F)$ that wind up to $\phi^{-1}$ over one period, use it to define an equivariant diffeomorphism of $\mathbb{R}\times F$ intertwining the $\phi$-action with the trivial action, and descend to the quotient.

**Subgoal decomposition:**

1. **Basic structure of $E_{\phi}$, $q$, $p$, $\pi$.** Establish that the $\mathbb{Z}$-action is smooth, free, properly discontinuous, so $E_{\phi}$ is a manifold and $q$ a covering; then that $\pi$ is well-defined, smooth, and surjective.
   - *Hint:* Properness/wandering: for $(t_{0},f_{0})$ take the slab $(t_{0}-\tfrac12,t_{0}+\tfrac12)\times W$; its translates by $k\neq0$ have disjoint first factors. Smoothness of $\pi$ from $\pi\circ q=p\circ\operatorname{pr}_{1}$ and the covering universal property.
   - *Why needed:* Everything downstream uses that $q$ is a local diffeomorphism and that $\pi$ is a smooth surjection.

2. **The chart lemma (Lemma 1).** For an open interval $I\subset\mathbb{R}$ of length $\le 1$, $q$ restricts to a diffeomorphism $I\times F\xrightarrow{\ \sim\ }\pi^{-1}(p(I))$, and $p$ restricts to a diffeomorphism $I\xrightarrow{\ \sim\ }p(I)$.
   - *Hint:* Injectivity of $q|_{I\times F}$: $q(t,f)=q(t',f')$ forces $t'=t+k$ with $t,t'\in I$, so $k=0$. Then use that $q$ is an open local diffeomorphism.
   - *Why needed:* Its inverse composed with $p\times\operatorname{id}_{F}$ is the local trivialisation.

3. **Assemble Part I.** Take $I_{1}=(0,1)$, $I_{2}=(\tfrac12,\tfrac32)$; set $\psi_{i}=(p\times\operatorname{id}_{F})\circ(q|_{I_{i}\times F})^{-1}$; check $\operatorname{pr}_{1}\circ\psi_{i}=\pi$ and that $U_{1},U_{2}$ cover $S^{1}$.
   - *Hint:* $\pi^{-1}(U_{i})=q(I_{i}\times F)$ by Lemma 1 with $p(I_{i})=U_{i}$.
   - *Why needed:* This is the definition of a fibre bundle satisfied on the nose.

4. **Compute the transition map.** On each component of $U_{1}\cap U_{2}$, express a point's $I_{2}$-representative in terms of its $I_{1}$-representative and read off $\psi_{2}\circ\psi_{1}^{-1}$.
   - *Hint:* On $p((\tfrac12,1))$ the representatives coincide; on $p((0,\tfrac12))$ the $I_{2}$-representative is $t+1$, and $[t+1,f]=[t,\ ?]$ needs the action.
   - *Why needed:* It exhibits the twist as $\phi$ concentrated on one arc — the cocycle datum.

5. **The descent lemma (Lemma 2).** A $\mathbb{Z}$-equivariant diffeomorphism of $\mathbb{R}\times F$ covering $\operatorname{id}_{\mathbb{R}}$, intertwining the $\phi$-action with the trivial action, descends to a bundle isomorphism $E_{\phi}\to S^{1}\times F$ over $\operatorname{id}_{S^{1}}$.
   - *Hint:* Well-defined by equivariance; smooth because $q$ has local smooth sections; inverse descends from the inverse map.
   - *Why needed:* It converts the upstairs untwisting into a downstairs isomorphism.

6. **The untwisting family (Lemma 3).** From an isotopy $\phi_{s}$ ($\phi_{0}=\operatorname{id}$, $\phi_{1}=\phi$) build a smooth family $\alpha\colon\mathbb{R}\to\operatorname{Diff}(F)$ with $\alpha_{0}=\operatorname{id}$ and $\alpha_{t+1}=\alpha_{t}\circ\phi^{-1}$.
   - *Hint:* Reparametrise so the isotopy is constant near $s=0,1$; then set $\alpha_{t}=\phi_{\beta(s)}^{-1}\circ\phi^{-n}$ for $t=n+s$, $n=\lfloor t\rfloor$.
   - *Why needed:* The recursion $\alpha_{t+1}=\alpha_{t}\circ\phi^{-1}$ is exactly the equivariance condition for the map in Lemma 2.

7. **Assemble Part II.** Define $\tilde\Psi(t,f)=(t,\alpha_{t}(f))$, verify equivariance, and apply Lemma 2.
   - *Hint:* Equivariance is the recursion; the descended map lands in $S^{1}\times F=E_{\operatorname{id}}$.
   - *Why needed:* This produces the global trivialisation, so the bundle is trivial.

---

# Lemma Decomposition

> [!note]- Lemma 1: length-one intervals give trivialising charts
> **Statement:** Let $I=(a,a+\ell)\subset\mathbb{R}$ be an open interval of length $\ell\le 1$. Then:
> (a) $p|_{I}\colon I\to p(I)$ is a diffeomorphism onto the open arc $p(I)\subset S^{1}$;
> (b) $q|_{I\times F}\colon I\times F\to q(I\times F)$ is a diffeomorphism onto the open set $q(I\times F)\subset E_{\phi}$;
> (c) $q(I\times F)=\pi^{-1}\big(p(I)\big)$.
>
> **Hint:** For injectivity, two points of $I$ (or of $I\times F$) that are identified differ by a translation by a nonzero integer, impossible inside a length-$\le 1$ interval. Then use that $p$ and $q$ are open local diffeomorphisms (covering maps) to upgrade a continuous bijection onto its image to a diffeomorphism.
>
> **Why needed:** Its inverse is half of the local trivialisation; part (c) identifies the domain of that trivialisation as a genuine preimage arc.
>
> > [!note]- Full proof
> > We use throughout that $q\colon\mathbb{R}\times F\to E_{\phi}$ and $p\colon\mathbb{R}\to S^{1}$ are smooth covering maps, hence open maps and local diffeomorphisms, by the [[Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map|quotient theorem for properly discontinuous actions]] — *if a discrete group $\Gamma$ acts smoothly and properly discontinuously on a manifold $M$, then $\Gamma\backslash M$ has a unique smooth structure making the quotient map $M\to\Gamma\backslash M$ a smooth covering map, in particular a local diffeomorphism.* The $\mathbb{Z}$-actions defining $E_{\phi}$ and $S^{1}$ satisfy this hypothesis (Step 0 of the formal proof).
> >
> > **Part (a): $p|_{I}$ is a diffeomorphism onto its image.**
> > *Injectivity.* Suppose $t,t'\in I$ with $p(t)=p(t')$. By definition of $S^{1}=\mathbb{Z}\backslash\mathbb{R}$ this means $t'-t=k\in\mathbb{Z}$. Since $t,t'\in I=(a,a+\ell)$ with $\ell\le 1$, we have $|t'-t|<\ell\le 1$, so the integer $k$ satisfies $|k|<1$, forcing $k=0$ and $t'=t$ (definition of the translation action, length bound).
> > *Image is open and the map is a diffeomorphism.* Since $p$ is an open map, $p(I)$ is open. The restriction $p|_{I}\colon I\to p(I)$ is a smooth bijection (surjective onto its image by definition, injective just shown). It is a local diffeomorphism, being the restriction of the local diffeomorphism $p$ to an open set. A bijective local diffeomorphism is a diffeomorphism: its inverse is continuous (a bijective open map has continuous inverse) and locally it agrees with the smooth local inverses of $p$, hence is smooth. Thus $p|_{I}$ is a diffeomorphism onto $p(I)$.
> >
> > **Part (b): $q|_{I\times F}$ is a diffeomorphism onto its image.**
> > *Injectivity.* Suppose $(t,f),(t',f')\in I\times F$ with $q(t,f)=q(t',f')$. Then $(t',f')=k\cdot(t,f)=(t+k,\phi^{k}(f))$ for some $k\in\mathbb{Z}$ (definition of the orbit equivalence). The first coordinates give $t'=t+k$ with $t,t'\in I$, so as in part (a) the length bound $\ell\le 1$ forces $k=0$; then $t'=t$ and $f'=\phi^{0}(f)=f$. Hence $q|_{I\times F}$ is injective.
> > *Diffeomorphism onto its image.* Since $q$ is an open map and $I\times F$ is open in $\mathbb{R}\times F$, the image $q(I\times F)$ is open in $E_{\phi}$. The restriction $q|_{I\times F}\colon I\times F\to q(I\times F)$ is a smooth bijection and a local diffeomorphism (restriction of the local diffeomorphism $q$), hence, by the same argument as in part (a), a diffeomorphism.
> >
> > **Part (c): $q(I\times F)=\pi^{-1}(p(I))$.**
> > ($\subseteq$) For $(t,f)\in I\times F$ we compute $\pi(q(t,f))=\pi([t,f])=[t]=p(t)\in p(I)$ (definition of $\pi$), so $q(t,f)\in\pi^{-1}(p(I))$.
> > ($\supseteq$) Let $y\in\pi^{-1}(p(I))$, say $y=[s,g]$ with $s\in\mathbb{R}$, $g\in F$, and $\pi(y)=[s]\in p(I)$. Then $[s]=[t_{0}]$ for some $t_{0}\in I$, i.e. $s=t_{0}+k$ for some $k\in\mathbb{Z}$ (definition of $S^{1}$). Applying the orbit relation with this $k$,
> > $$[s,g]=[t_{0}+k,\ g]=[t_{0},\ \phi^{-k}(g)]\qquad\text{(since }k\cdot(t_{0},\phi^{-k}g)=(t_{0}+k,\phi^{k}\phi^{-k}g)=(t_{0}+k,g)\text{)}.$$
> > As $(t_{0},\phi^{-k}(g))\in I\times F$, we get $y=[s,g]=q(t_{0},\phi^{-k}(g))\in q(I\times F)$. This proves the two inclusions and hence the equality.

> [!note]- Lemma 2: equivariant diffeomorphisms descend to bundle isomorphisms
> **Statement:** Let $\tilde\Psi\colon\mathbb{R}\times F\to\mathbb{R}\times F$ be a diffeomorphism that covers $\operatorname{id}_{\mathbb{R}}$ — meaning $\operatorname{pr}_{1}\circ\tilde\Psi=\operatorname{pr}_{1}$ — and that intertwines the mapping-torus action $a$, $k\cdot_{a}(t,f)=(t+k,\phi^{k}f)$, with the product action $b$, $k\cdot_{b}(t,f)=(t+k,f)$; that is,
> $$\tilde\Psi\big(k\cdot_{a}(t,f)\big)=k\cdot_{b}\tilde\Psi(t,f)\qquad\text{for all }k\in\mathbb{Z},\ (t,f)\in\mathbb{R}\times F.$$
> Then $\tilde\Psi$ descends to a diffeomorphism $\Psi\colon E_{\phi}\to S^{1}\times F$ with $\operatorname{pr}_{1}\circ\Psi=\pi$; that is, a bundle isomorphism over $\operatorname{id}_{S^{1}}$. Consequently $E_{\phi}$ is trivial.
>
> **Hint:** Define $\Psi([t,f])=q_{b}(\tilde\Psi(t,f))$ where $q_{b}\colon\mathbb{R}\times F\to S^{1}\times F$ is the product quotient; equivariance makes it well-defined and smoothness follows because $q_{a}$ has local smooth sections.
>
> **Why needed:** It is the bridge from the explicit untwisting on the cover to an isomorphism of the bundles themselves.
>
> > [!note]- Full proof
> > Write $q_{a}=q\colon\mathbb{R}\times F\to E_{\phi}$ for the mapping-torus quotient (action $a$) and $q_{b}\colon\mathbb{R}\times F\to \mathbb{Z}\backslash_{b}(\mathbb{R}\times F)$ for the quotient by the product action $b$. The product action $b$ has orbit space $S^{1}\times F$ with $q_{b}(t,f)=([t],f)$, and this identification is a diffeomorphism: $b$ is the mapping-torus action of $\operatorname{id}_{F}$, whose torus is $E_{\operatorname{id}}=S^{1}\times F$ by direct inspection of the gluing $(0,f)\sim(1,\operatorname{id}(f))=(1,f)$. Both $q_{a}$ and $q_{b}$ are smooth covering maps by the [[Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map|quotient theorem]] (the two actions are smooth, free, properly discontinuous by Step 0).
> >
> > **Step 1 — $\Psi$ is well-defined as a map of sets.** Define $\Psi\colon E_{\phi}\to S^{1}\times F$ by $\Psi([t,f]):=q_{b}(\tilde\Psi(t,f))$. Suppose $[t,f]=[t',f']$, i.e. $(t',f')=k\cdot_{a}(t,f)$ for some $k\in\mathbb{Z}$. Then
> > $$q_{b}(\tilde\Psi(t',f'))=q_{b}\big(\tilde\Psi(k\cdot_{a}(t,f))\big)=q_{b}\big(k\cdot_{b}\tilde\Psi(t,f)\big)=q_{b}(\tilde\Psi(t,f))\qquad\text{(intertwining hypothesis; }q_{b}\text{ constant on }b\text{-orbits).}$$
> > So the value is independent of the representative and $\Psi$ is well-defined.
> >
> > **Step 2 — $\Psi$ is smooth.** Fix $y_{0}=[t_{0},f_{0}]\in E_{\phi}$. Since $q_{a}$ is a covering map, there is an open neighbourhood $O$ of $y_{0}$ and a smooth local section $\sigma\colon O\to\mathbb{R}\times F$ with $q_{a}\circ\sigma=\operatorname{id}_{O}$ (a local inverse of the local diffeomorphism $q_{a}$). On $O$,
> > $$\Psi|_{O}=q_{b}\circ\tilde\Psi\circ\sigma\qquad\text{(for }y\in O,\ \Psi(y)=q_{b}(\tilde\Psi(\sigma(y)))\text{ since }\sigma(y)\text{ represents }y),$$
> > a composite of smooth maps, hence smooth on $O$. As $y_{0}$ was arbitrary, $\Psi$ is smooth.
> >
> > **Step 3 — $\Psi$ covers $\operatorname{id}_{S^{1}}$.** For $[t,f]\in E_{\phi}$, using $\operatorname{pr}_{1}\circ\tilde\Psi=\operatorname{pr}_{1}$,
> > $$\operatorname{pr}_{1}^{S^{1}}\big(\Psi([t,f])\big)=\operatorname{pr}_{1}^{S^{1}}\big(q_{b}(\tilde\Psi(t,f))\big)=\big[\operatorname{pr}_{1}(\tilde\Psi(t,f))\big]=[\operatorname{pr}_{1}(t,f)]=[t]=\pi([t,f]).$$
> > Thus $\operatorname{pr}_{1}^{S^{1}}\circ\Psi=\pi$.
> >
> > **Step 4 — $\Psi$ is a diffeomorphism.** The inverse map $\tilde\Psi^{-1}$ is again a diffeomorphism covering $\operatorname{id}_{\mathbb{R}}$; applying the intertwining hypothesis to $\tilde\Psi$ and then substituting shows $\tilde\Psi^{-1}$ intertwines $b$ with $a$: from $\tilde\Psi(k\cdot_{a}x)=k\cdot_{b}\tilde\Psi(x)$, put $x=\tilde\Psi^{-1}(y)$ to get $\tilde\Psi(k\cdot_{a}\tilde\Psi^{-1}(y))=k\cdot_{b}y$, hence $k\cdot_{a}\tilde\Psi^{-1}(y)=\tilde\Psi^{-1}(k\cdot_{b}y)$. By Steps 1–3 applied to $\tilde\Psi^{-1}$ (with the roles of $a$ and $b$ exchanged), $\tilde\Psi^{-1}$ descends to a smooth map $\Xi\colon S^{1}\times F\to E_{\phi}$ with $q_{a}\circ\tilde\Psi^{-1}=\Xi\circ q_{b}$. Then for all $(t,f)$,
> > $$\Xi\big(\Psi([t,f])\big)=\Xi\big(q_{b}(\tilde\Psi(t,f))\big)=q_{a}\big(\tilde\Psi^{-1}(\tilde\Psi(t,f))\big)=q_{a}(t,f)=[t,f],$$
> > and symmetrically $\Psi(\Xi(z))=z$ for all $z\in S^{1}\times F$. So $\Xi=\Psi^{-1}$ is smooth, and $\Psi$ is a diffeomorphism.
> >
> > **Conclusion.** $\Psi\colon E_{\phi}\to S^{1}\times F$ is a diffeomorphism with $\operatorname{pr}_{1}^{S^{1}}\circ\Psi=\pi$, i.e. a fibre-bundle isomorphism over $\operatorname{id}_{S^{1}}$. Hence $(E_{\phi},\pi,S^{1})$ is trivial.

> [!note]- Lemma 3: an isotopy to the identity yields a smooth untwisting family
> **Statement:** Suppose $\phi$ is isotopic to $\operatorname{id}_{F}$ through diffeomorphisms, witnessed by a smooth family $\{\phi_{s}\}_{s\in[0,1]}$ of diffeomorphisms of $F$ with $\phi_{0}=\operatorname{id}_{F}$, $\phi_{1}=\phi$. Then there is a smooth family $\{\alpha_{t}\}_{t\in\mathbb{R}}$ of diffeomorphisms of $F$ — smooth in the sense that $(t,f)\mapsto\alpha_{t}(f)$ and $(t,f)\mapsto\alpha_{t}^{-1}(f)$ are smooth maps $\mathbb{R}\times F\to F$ — such that
> $$\alpha_{0}=\operatorname{id}_{F}\qquad\text{and}\qquad \alpha_{t+1}=\alpha_{t}\circ\phi^{-1}\ \text{ for all }t\in\mathbb{R}.$$
>
> **Hint:** First reparametrise the isotopy by a smooth $\beta\colon\mathbb{R}\to[0,1]$ that is $0$ near integers from below and $1$ near integers from above, so the family becomes constant near the seam. Then define $\alpha_{t}=\phi_{\beta(t-\lfloor t\rfloor)}^{-1}\circ\phi^{-\lfloor t\rfloor}$.
>
> **Why needed:** The recursion $\alpha_{t+1}=\alpha_{t}\circ\phi^{-1}$ is precisely the equivariance identity required to apply Lemma 2, and the endpoint-constancy is what makes $\alpha$ smooth across the integers.
>
> > [!note]- Full proof
> > **Step 1 — reparametrise to be constant near the endpoints.** Choose a smooth non-decreasing function $\beta\colon[0,1]\to[0,1]$ with $\beta\equiv 0$ on $[0,\tfrac14]$ and $\beta\equiv 1$ on $[\tfrac34,1]$; such a $\beta$ exists by the standard construction of smooth cut-off functions from bump functions (a normalised integral of a non-negative bump supported in $(\tfrac14,\tfrac34)$), which is available on manifolds by [[Thm - Existence of Smooth Bump Functions|the existence of smooth bump functions]]. Define $\psi_{s}:=\phi_{\beta(s)}$ for $s\in[0,1]$. Each $\psi_{s}$ is a diffeomorphism (a value of the original family), $\psi_{0}=\phi_{\beta(0)}=\phi_{0}=\operatorname{id}_{F}$ and $\psi_{1}=\phi_{\beta(1)}=\phi_{1}=\phi$, the map $(s,f)\mapsto\psi_{s}(f)=\Phi(\beta(s),f)$ is smooth (composite of the smooth isotopy with the smooth $\beta$), and $\psi_{s}$ is constant equal to $\operatorname{id}_{F}$ for $s\in[0,\tfrac14]$ and constant equal to $\phi$ for $s\in[\tfrac34,1]$. In particular all $s$-derivatives of $(s,f)\mapsto\psi_{s}(f)$ vanish at $s=0$ and $s=1$.
> >
> > **Step 2 — define $\alpha$ and check the recursion.** For $t\in\mathbb{R}$ write $n=\lfloor t\rfloor\in\mathbb{Z}$ and $s=t-n\in[0,1)$, and set
> > $$\alpha_{t}:=\psi_{s}^{-1}\circ\phi^{-n}.$$
> > This is a composite of diffeomorphisms, hence a diffeomorphism of $F$. At $t=0$ we have $n=0$, $s=0$, so $\alpha_{0}=\psi_{0}^{-1}\circ\phi^{0}=\operatorname{id}_{F}$. For the recursion, fix $t$ with $n=\lfloor t\rfloor$, $s=t-n$; then $t+1$ has $\lfloor t+1\rfloor=n+1$ and fractional part $s$ again, so
> > $$\alpha_{t+1}=\psi_{s}^{-1}\circ\phi^{-(n+1)}=\psi_{s}^{-1}\circ\phi^{-n}\circ\phi^{-1}=\alpha_{t}\circ\phi^{-1}\qquad\text{(definition of }\alpha\text{; }\phi^{-(n+1)}=\phi^{-n}\circ\phi^{-1}\text{).}$$
> >
> > **Step 3 — smoothness of $(t,f)\mapsto\alpha_{t}(f)$ across the integers.** On the open strip $\{n<t<n+1\}$ the map is $(t,f)\mapsto\psi_{t-n}^{-1}(\phi^{-n}(f))$, smooth because inversion and evaluation of the smooth family $\psi$ are smooth (the map $(s,f)\mapsto\psi_{s}^{-1}(f)$ is smooth: $\psi$ is a smooth isotopy, and the inverse of a smooth isotopy is a smooth isotopy, since it is the fibrewise inverse of a diffeomorphism of $[0,1]\times F$ covering the identity of $[0,1]$, whose smoothness follows from the inverse function theorem applied to $(s,f)\mapsto(s,\psi_{s}(f))$). It remains to check smoothness at an integer $t=m$. Approaching from above ($t=m+s$, $s\to 0^{+}$, $n=m$): near such $t$, using $\psi_{s}=\operatorname{id}_{F}$ for $s\in[0,\tfrac14]$, the map equals $(t,f)\mapsto\phi^{-m}(f)$, a fixed smooth map, on the strip $(m,m+\tfrac14)$. Approaching from below ($t=m-1+s'$, $s'\to 1^{-}$, $n=m-1$): using $\psi_{s'}=\phi$ for $s'\in[\tfrac34,1]$, the map equals $(t,f)\mapsto\psi_{s'}^{-1}(\phi^{-(m-1)}(f))=\phi^{-1}(\phi^{-(m-1)}(f))=\phi^{-m}(f)$ on the strip $(m-\tfrac14,m)$. The two one-sided expressions coincide with the single smooth map $(t,f)\mapsto\phi^{-m}(f)$ on a full neighbourhood $(m-\tfrac14,m+\tfrac14)\times F$ of $\{m\}\times F$ (independent of $t$ there), so $\alpha$ is smooth across $t=m$. Since $m$ was an arbitrary integer, $(t,f)\mapsto\alpha_{t}(f)$ is smooth on all of $\mathbb{R}\times F$.
> >
> > **Step 4 — smoothness of the inverse family.** The inverse is $\alpha_{t}^{-1}=\phi^{n}\circ\psi_{s}$, and by the identical argument — using that $\psi_{s}=\operatorname{id}$ near $s=0$ and $\psi_{s}=\phi$ near $s=1$ — the map $(t,f)\mapsto\alpha_{t}^{-1}(f)$ equals $(t,f)\mapsto\phi^{m}(f)$ on the neighbourhood $(m-\tfrac14,m+\tfrac14)\times F$ of each integer $m$ and is smooth on each open strip, hence smooth on $\mathbb{R}\times F$.
> >
> > **Conclusion.** The family $\{\alpha_{t}\}$ is a smooth family of diffeomorphisms of $F$ with $\alpha_{0}=\operatorname{id}_{F}$ and $\alpha_{t+1}=\alpha_{t}\circ\phi^{-1}$, as required.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $F$ be a smooth manifold and $\phi\colon F\to F$ a diffeomorphism, with the notation of the first section.
>
> **Step 0 — the manifold $E_{\phi}$, the covering $q$, and the smooth surjection $\pi$.**
> *The action is smooth, free, and properly discontinuous.* Each map $k\cdot(-)\colon\mathbb{R}\times F\to\mathbb{R}\times F$, $(t,f)\mapsto(t+k,\phi^{k}(f))$, is a diffeomorphism (translation in the first factor and the diffeomorphism $\phi^{k}$ in the second), so the action is by diffeomorphisms and smooth. It is free: $k\cdot(t,f)=(t,f)$ gives $t+k=t$, so $k=0$. It is properly discontinuous: given $(t_{0},f_{0})$, take the open slab $V=(t_{0}-\tfrac12,t_{0}+\tfrac12)\times F$; for $k\neq 0$ the first factor of $k\cdot V=(t_{0}-\tfrac12+k,\ t_{0}+\tfrac12+k)\times F$ is disjoint from $(t_{0}-\tfrac12,t_{0}+\tfrac12)$ because $|k|\ge 1$, so $k\cdot V\cap V=\varnothing$; this wandering property, together with freeness, is proper discontinuity for the discrete group $\mathbb{Z}$ (as established on [[Def - Sphere Bundles and Mapping Tori|the mapping-torus definition page]] and [[Def - Discrete Group and Properly Discontinuous Action|the discrete-action page]]).
> *Manifold and covering.* By the [[Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map|quotient theorem]] — *if a discrete group $\Gamma$ acts smoothly and properly discontinuously on a manifold $M$, then $\Gamma\backslash M$ carries a unique smooth structure making the quotient map $M\to\Gamma\backslash M$ a smooth covering map, in particular a local diffeomorphism* — the orbit space $E_{\phi}=\mathbb{Z}\backslash(\mathbb{R}\times F)$ is a smooth manifold and $q$ is a smooth covering map. Taking $F$ a single point, the same theorem makes $S^{1}=\mathbb{Z}\backslash\mathbb{R}$ a smooth manifold and $p$ a smooth covering map.
> *The projection $\pi$.* The map $\pi([t,f])=[t]$ is well-defined: if $(t',f')=k\cdot(t,f)$ then $t'=t+k$, so $[t']=[t]$ (definition of $S^{1}$). It satisfies $\pi\circ q=p\circ\operatorname{pr}_{1}$, which is smooth; since $q$ is a smooth covering, it admits local smooth sections, and precomposing $\pi$ locally with such a section shows $\pi$ is smooth (the composite of the smooth $p\circ\operatorname{pr}_{1}$ with a local section of $q$). It is surjective because $p$ and $\operatorname{pr}_{1}$ are. This proves $\pi$ is a smooth surjection, so $(E_{\phi},\pi,S^{1})$ is a candidate bundle.
>
> **Part I — $(E_{\phi},\pi,S^{1})$ is a fibre bundle with typical fibre $F$.**
>
> **Step 1 — the covering arcs.** Put
> $$I_{1}=(0,1),\quad U_{1}:=p(I_{1})=S^{1}\setminus\{[0]\};\qquad I_{2}=(\tfrac12,\tfrac32),\quad U_{2}:=p(I_{2})=S^{1}\setminus\{[\tfrac12]\}.$$
> Indeed $p((0,1))=\{[t]:t\in(0,1)\}$ is everything in $S^{1}$ except $[0]$, since every real is congruent modulo $\mathbb{Z}$ to exactly one point of $[0,1)$ and $[0]$ is the only class with no representative in $(0,1)$; likewise $p((\tfrac12,\tfrac32))=S^{1}\setminus\{[\tfrac12]\}$. Because $[0]\ne[\tfrac12]$, we have $U_{1}\cup U_{2}=S^{1}$.
>
> **Step 2 — the local trivialisations.** Both $I_{1}$ and $I_{2}$ have length $1$, so Lemma 1 applies. By Lemma 1(c), $q(I_{i}\times F)=\pi^{-1}(p(I_{i}))=\pi^{-1}(U_{i})$, and by Lemma 1(b) the restriction $q|_{I_{i}\times F}\colon I_{i}\times F\to\pi^{-1}(U_{i})$ is a diffeomorphism. Define
> $$\psi_{i}:=\big(p|_{I_{i}}\times\operatorname{id}_{F}\big)\circ\big(q|_{I_{i}\times F}\big)^{-1}\colon\ \pi^{-1}(U_{i})\longrightarrow U_{i}\times F,$$
> a composite of diffeomorphisms (Lemma 1(a) makes $p|_{I_{i}}\times\operatorname{id}_{F}\colon I_{i}\times F\to U_{i}\times F$ a diffeomorphism), hence a diffeomorphism. Concretely, if $y\in\pi^{-1}(U_{i})$ has the unique representative $(t,f)$ with $t\in I_{i}$, then $\psi_{i}(y)=(p(t),f)$. It is a trivialisation over $U_{i}$: for such $y$,
> $$\operatorname{pr}_{1}\big(\psi_{i}(y)\big)=p(t)=\pi(y)\qquad\text{(definition of }\pi\text{ and of }\psi_{i}\text{),}$$
> so $\operatorname{pr}_{1}\circ\psi_{i}=\pi|_{\pi^{-1}(U_{i})}$.
>
> **Step 3 — conclusion of Part I.** The open sets $U_{1},U_{2}$ cover $S^{1}$ (Step 1) and carry local trivialisations $\psi_{1},\psi_{2}$ (Step 2). By the [[Def - Fibre Bundle|definition of a fibre bundle]], $(E_{\phi},\pi,S^{1})$ is a fibre bundle with typical fibre $F$. Its fibre over $[t]$ is $\pi^{-1}([t])=\{[t,f]:f\in F\}$, and $f\mapsto[t,f]$ is a diffeomorphism $F\to\pi^{-1}([t])$ (it is $y\mapsto\psi_{i}^{-1}([t],y)$ restricted to a point of the base), confirming the typical fibre is $F$.
>
> **Step 4 — the transition map.** We compute $\psi_{2}\circ\psi_{1}^{-1}$ on $(U_{1}\cap U_{2})\times F$, where $U_{1}\cap U_{2}=S^{1}\setminus\{[0],[\tfrac12]\}$ has two connected components,
> $$A:=p\big((\tfrac12,1)\big),\qquad B:=p\big((0,\tfrac12)\big).$$
> Fix $x=[t]\in U_{1}\cap U_{2}$ and $f\in F$; then $\psi_{1}^{-1}(x,f)=[\,t_{1},f\,]$ where $t_{1}\in I_{1}=(0,1)$ is the representative of $x$, and we must re-express this class with a representative in $I_{2}=(\tfrac12,\tfrac32)$ to apply $\psi_{2}$.
> *Component $A$ ($x=[t]$, $t\in(\tfrac12,1)$).* Here $t_{1}=t\in(\tfrac12,1)\subset I_{2}$ as well, so $[t_{1},f]$ already has its representative in $I_{2}$, giving $\psi_{2}([t_{1},f])=(x,f)$. Hence
> $$(\psi_{2}\circ\psi_{1}^{-1})(x,f)=(x,f)\qquad\text{on }A.$$
> *Component $B$ ($x=[t]$, $t\in(0,\tfrac12)$).* Here $t_{1}=t\in(0,\tfrac12)$, which is not in $I_{2}$, but $t_{1}+1\in(1,\tfrac32)\subset I_{2}$ is the $I_{2}$-representative of $x$. Using the orbit relation $1\cdot(t_{1},f)=(t_{1}+1,\phi(f))$,
> $$[t_{1},f]=[\,t_{1}+1,\ \phi(f)\,]\qquad\text{(definition of the action, }k=1\text{),}$$
> and $t_{1}+1\in I_{2}$, so $\psi_{2}([t_{1},f])=\psi_{2}([t_{1}+1,\phi(f)])=(x,\phi(f))$. Hence
> $$(\psi_{2}\circ\psi_{1}^{-1})(x,f)=(x,\phi(f))\qquad\text{on }B.$$
> Thus the transition cocycle $g_{21}\colon U_{1}\cap U_{2}\to\operatorname{Diff}(F)$, defined by $(\psi_{2}\circ\psi_{1}^{-1})(x,f)=(x,g_{21}(x)(f))$, is $g_{21}\equiv\operatorname{id}_{F}$ on the interior arc $A$ and $g_{21}\equiv\phi$ on the seam arc $B$. The entire twist of the bundle is carried by the single diffeomorphism $\phi$ on the one arc that crosses the seam $[0]$. This proves the transition-map claim of Part I.
>
> **Part II — if $\phi$ is isotopic to $\operatorname{id}_{F}$ through diffeomorphisms, then $E_{\phi}$ is trivial.**
>
> **Step 5 — the untwisting family.** By hypothesis there is a smooth family $\{\phi_{s}\}_{s\in[0,1]}$ of diffeomorphisms of $F$ with $\phi_{0}=\operatorname{id}_{F}$ and $\phi_{1}=\phi$. By Lemma 3 there is a smooth family $\{\alpha_{t}\}_{t\in\mathbb{R}}$ of diffeomorphisms of $F$, with $(t,f)\mapsto\alpha_{t}(f)$ and $(t,f)\mapsto\alpha_{t}^{-1}(f)$ smooth, satisfying
> $$\alpha_{0}=\operatorname{id}_{F},\qquad \alpha_{t+1}=\alpha_{t}\circ\phi^{-1}\quad(t\in\mathbb{R}).$$
>
> **Step 6 — the equivariant diffeomorphism upstairs.** Define
> $$\tilde\Psi\colon\mathbb{R}\times F\to\mathbb{R}\times F,\qquad \tilde\Psi(t,f)=(t,\ \alpha_{t}(f)).$$
> It is smooth (Step 5) with smooth inverse $\tilde\Psi^{-1}(t,g)=(t,\alpha_{t}^{-1}(g))$, hence a diffeomorphism, and it covers $\operatorname{id}_{\mathbb{R}}$ since $\operatorname{pr}_{1}\circ\tilde\Psi=\operatorname{pr}_{1}$. We check it intertwines the mapping-torus action $a$ ($k\cdot_{a}(t,f)=(t+k,\phi^{k}f)$) with the product action $b$ ($k\cdot_{b}(t,f)=(t+k,f)$). It suffices to check $k=1$, since both actions are generated by $1$ and an intertwiner for the generator intertwines all its powers (compose the identity with itself: if $\tilde\Psi(1\cdot_{a}x)=1\cdot_{b}\tilde\Psi(x)$ for all $x$, then $\tilde\Psi(k\cdot_{a}x)=\tilde\Psi(1\cdot_{a}((k-1)\cdot_{a}x))=1\cdot_{b}\tilde\Psi((k-1)\cdot_{a}x)$, and induction on $k\ge 0$ and on $k\le 0$ using $\tilde\Psi(-1\cdot_{a}x)=-1\cdot_{b}\tilde\Psi(x)$ gives all $k$). For the generator, using the recursion $\alpha_{t+1}=\alpha_{t}\circ\phi^{-1}$,
> $$\tilde\Psi\big(1\cdot_{a}(t,f)\big)=\tilde\Psi(t+1,\phi f)=\big(t+1,\ \alpha_{t+1}(\phi f)\big)=\big(t+1,\ \alpha_{t}(\phi^{-1}\phi f)\big)=\big(t+1,\ \alpha_{t}(f)\big)$$
> $$=1\cdot_{b}\,(t,\alpha_{t}(f))=1\cdot_{b}\,\tilde\Psi(t,f)\qquad\text{(recursion for }\alpha\text{; }\phi^{-1}\phi=\operatorname{id}_{F}\text{; definition of }b\text{ and of }\tilde\Psi\text{).}$$
> So $\tilde\Psi$ satisfies the intertwining hypothesis of Lemma 2.
>
> **Step 7 — descend and conclude.** By Lemma 2, $\tilde\Psi$ descends to a bundle isomorphism $\Psi\colon E_{\phi}\to S^{1}\times F$ over $\operatorname{id}_{S^{1}}$. Therefore $(E_{\phi},\pi,S^{1})$ is isomorphic to the product bundle $(S^{1}\times F,\operatorname{pr}_{1},S^{1})$, i.e. it is trivial.
>
> Combining Part I and Part II: $(E_{\phi},\pi,S^{1})$ is a fibre bundle with typical fibre $F$, and it is trivial whenever $\phi$ is isotopic to $\operatorname{id}_{F}$ through diffeomorphisms. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Dynamical systems: suspensions and return maps.** Given any diffeomorphism $\phi$ of a compact manifold $F$, the theorem makes the suspension phase space $E_{\phi}$ a smooth circle bundle, and the vector field $\partial_{t}$ on $\mathbb{R}\times F$ descends to a nowhere-vanishing flow on $E_{\phi}$ transverse to every fibre. A good exercise is to prove that the time-one Poincaré return map of this flow to the fibre $\pi^{-1}([0])\cong F$ is conjugate to $\phi$, so that the dynamics of $\phi$ are faithfully encoded in a continuous-time flow. The theorem applies because $\phi$, being a diffeomorphism, satisfies the hypothesis on the nose; the non-obvious part is that the transverse flow exists globally, which is exactly the local triviality of Part I glued across the seam.

**Low-dimensional topology: three-manifolds fibring over the circle.** Take $F$ a compact surface and $\phi$ a self-diffeomorphism; the theorem produces a closed three-manifold $E_{\phi}$ fibring over $S^{1}$. An exercise is to show that two such fibred three-manifolds $E_{\phi}$ and $E_{\phi'}$ are isomorphic as bundles when $\phi$ and $\phi'$ are conjugate in the mapping class group $\pi_{0}\operatorname{Diff}(F)$, and to use Part II to see that a surface diffeomorphism isotopic to the identity yields $S^{1}\times F$. This is non-obvious because it converts a question about three-manifolds into a question about the isotopy classes of surface diffeomorphisms — the entry point to Thurston's classification of surface diffeomorphisms and the geometry of fibred three-manifolds.

**Ergodic theory and geometry: invariant structures descend.** Suppose $F$ carries a volume form (or a metric) that $\phi$ preserves. An exercise is to show, using the product structure over the arcs from Part I and the invariance of the datum, that the volume form (respectively metric) descends to $E_{\phi}$, making $\pi$ a fibrewise-volume-preserving submersion. The theorem is what guarantees the local product charts in which the descent is checked; the subtlety is verifying that the two charts' data agree on the overlap, which is exactly the statement that the transition map $\phi$ preserves the structure.

---

# Bridges

- **The cocycle description of bundles (§3.3).** Part I's transition computation is the smallest non-trivial instance of a bundle assembled from a cocycle. Here the cover is the two arcs $U_{1},U_{2}$, the overlap $U_{1}\cap U_{2}$ has two components, and the single essential transition datum is the diffeomorphism $\phi$ on the seam component. Reconstituting $E_{\phi}$ from this datum is the two-set case of [[Thm - Principal Bundles are Classified by Cocycles|the cocycle classification]]: a bundle over $S^{1}$ is a recipe for gluing two trivial pieces, and the recipe is the clutching diffeomorphism $\phi$.

- **Homotopy invariance of bundles (§3.5).** Part II is the germ of the theorem that a fibre map deformable to the identity carries no twist. Run over a general base, the untwisting family $\alpha_{t}$ becomes a homotopy-parameter-dependent gauge transformation, and the argument becomes the proof that homotopic classifying data give isomorphic bundles, on **Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles**. The deferred converse of the triviality criterion — that a trivial $E_{\phi}$ forces $\phi\simeq\operatorname{id}$ — is proved there as a corollary of the clutching construction, using that $\pi_{0}\operatorname{Diff}(F)$ measures bundles over $S^{1}$.

- **The Möbius strip and the Klein bottle as non-examples.** With $F=(-1,1)$ and $\phi=-\operatorname{id}$, the mapping torus is the Möbius strip; with $F=S^{1}$ and $\phi$ complex conjugation $z\mapsto\bar z$, it is the Klein bottle. In each case $\phi$ reverses orientation and is *not* isotopic to the identity through diffeomorphisms, so Part II does not apply, and the bundle is in fact non-trivial. The verifications are the sibling exercises **Ex - The Möbius Strip as a Mapping Torus is a Nontrivial Bundle** (which identifies $E_{-\operatorname{id}}$ with the Möbius line bundle of [[Ex - The Möbius Bundle is Nontrivial|DG VI]] and deduces non-triviality from the absence of a nowhere-vanishing section) and **Ex - The Klein Bottle as a Mapping Torus** (which deduces non-triviality from non-orientability of the total space).

- **Universal covers and flat bundles (chapter V).** The construction $E_{\phi}=\mathbb{Z}\backslash(\mathbb{R}\times F)$ presents $\mathbb{R}$ as the universal cover of $S^{1}$ and $E_{\phi}$ as the bundle associated to the deck action of $\pi_{1}(S^{1})=\mathbb{Z}$ via the representation $\mathbb{Z}\to\operatorname{Diff}(F)$, $k\mapsto\phi^{k}$. This is the elementary case of the correspondence, developed on **Thm - Existence of the Universal Cover and the Deck Action of the Fundamental Group**, between representations of $\pi_{1}$ into a structure group and flat bundles; the mapping torus is the flat $F$-bundle with holonomy $\phi$.

---

# Unlocked by This

> [!tip] Suspension flow *(from Dynamical Systems)*
> The mapping torus of a diffeomorphism $\phi$, together with the descended translation flow, is the **suspension** of the discrete system $\phi$: a continuous-time flow whose first-return map recovers $\phi$. This is the standard device for importing the machinery of continuous dynamics (flows, invariant measures, Lyapunov exponents) into the study of a single map. See **Def - Suspension Flow of a Diffeomorphism**.

> [!tip] Mapping class group *(from Geometric Topology)*
> Part II together with its deferred converse says that isomorphism classes of $F$-bundles over $S^{1}$ are classified by conjugacy classes in $\pi_{0}\operatorname{Diff}(F)$, the **mapping class group** of the fibre. This is the first computation of a bundle classification from an invariant of the fibre alone, and the model for the general clutching classification over spheres. See **Def - Mapping Class Group**.
