---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Fuchsian Group and the Quotient Surface"
  - "Def - Covering Space"
  - "Def - Path-Product and the Fundamental Group"
tags: [paper, topology, hyperbolic-geometry]
---

# Notation

- $\pi:\mathbb{H}^2\to X$ — the covering projection onto $X=\Gamma\backslash\mathbb{H}^2$
- $h\in\Gamma$ — a deck transformation: an isometry of $\mathbb{H}^2$ with $\pi\circ h=\pi$
- $x\in X$ — a basepoint; $\tilde x\in\pi^{-1}(x)$ a chosen lift
- $\omega : [0,t]\to X$ — a loop rooted at $x$, so $\omega(0)=\omega(t)=x$
- $\tilde\omega : [0,t]\to\mathbb{H}^2$ — its unique lift with $\tilde\omega(0)=\tilde x$
- $h_\omega\in\Gamma$ — the deck transformation recorded by $\omega$, defined by $\tilde\omega(t)=h_\omega\tilde x$
- $\pi_1(X,x)$ — the fundamental group of $X$ based at $x$

---

# In plain language

This is the dictionary that converts topology into group theory, and everything in §3 is written in it.

$\mathbb{H}^2$ covers $X$, and $\Gamma$ is the group of symmetries of that covering — the isometries $h$ of $\mathbb{H}^2$ that leave the projection unchanged, $\pi\circ h=\pi$. Now take a loop $\omega$ on $X$ rooted at $x$. Pick a point $\tilde x$ upstairs sitting over $x$. The loop lifts uniquely to a path $\tilde\omega$ upstairs starting at $\tilde x$; but a lifted loop need not close up, and in general it does not. What it does do is end somewhere in the fibre $\pi^{-1}(x)$, and since $\Gamma$ acts simply transitively on the fibre, there is a **unique** $h_\omega\in\Gamma$ with $\tilde\omega(t)=h_\omega\tilde x$.

That element $h_\omega$ is the topological content of the loop. It is the identity exactly when the lift closes up, which happens exactly when $\omega$ is contractible. Homotopic loops record the same element, so the assignment $\omega\mapsto h_\omega$ descends to an isomorphism $\pi_1(X,x)\cong\Gamma$ — one that depends on the choice of $\tilde x$, a dependence which is not a nuisance but the entire content of the next page.

**Why this matters analytically.** The heat kernel downstairs is a sum over $\Gamma$: $p_X(t,z,w)=\sum_{h\in\Gamma}p_{\mathbb{H}^2}(t,\tilde z,h\tilde w)$. So the analytic object arrives already decomposed by deck transformation, and by the dictionary that is the same as decomposed by topological type of loop. Restricting the sum to a conjugacy class *is* restricting the loop measure to a free homotopy class. That coincidence is the mechanism of the whole paper, and it is the reason a covering-space fact appears in a probability paper at all.

---

# The definition

> **Definition (deck transformation).** A **deck transformation** of the covering $\pi:\mathbb{H}^2\to X$ is an isometry $h$ of $\mathbb{H}^2$ satisfying $\pi\circ h=\pi$. For $X=\Gamma\backslash\mathbb{H}^2$ with $\Gamma$ torsion-free Fuchsian, the deck transformation group is exactly $\Gamma$, and it acts simply transitively on each fibre $\pi^{-1}(x)$.

> **Definition (the recorded element).** Fix $x\in X$ and $\tilde x\in\pi^{-1}(x)$. Any loop $\omega:[0,t]\to X$ with $\omega(0)=\omega(t)=x$ admits a **unique lift** $\tilde\omega:[0,t]\to\mathbb{H}^2$ with $\tilde\omega(0)=\tilde x$. Its endpoint lies in $\pi^{-1}(x)$, so
> $$\tilde\omega(t) = h_\omega\,\tilde x\qquad\text{for a unique }h_\omega\in\Gamma.$$
> The element $h_\omega$ records the deck transformation accumulated by $\omega$, and $h_\omega=\mathrm{id}$ if and only if $\omega$ is contractible.

The choice of $\tilde x$ determines an isomorphism $\pi_1(X,x)\cong\Gamma$. Since $\mathbb{H}^2$ is simply connected the covering is universal, and the covering is regular (Galois) because the deck group acts transitively on fibres — see [[Def - Regular (Galois) Covering]] and [[Thm - Galois Correspondence for Covering Spaces]].

---

# Types and signatures

- $\pi : \mathbb{H}^2\to X$ — a covering map and a local isometry; each fibre $\pi^{-1}(x)$ is a $\Gamma$-torsor, in bijection with $\Gamma$ once a basepoint is chosen
- $h : \mathbb{H}^2\to\mathbb{H}^2$ — an isometry, an element of $\Gamma\subset\mathrm{PSL}(2,\mathbb{R})$
- the lifting map $\omega\mapsto\tilde\omega$ — a bijection from loops at $x$ to paths starting at $\tilde x$ and ending in $\pi^{-1}(x)$; **depends on $\tilde x$**
- $\omega\mapsto h_\omega$ — a map from loops at $x$ to $\Gamma$, constant on homotopy classes rel basepoint, inducing $\pi_1(X,x)\xrightarrow{\ \sim\ }\Gamma$; **depends on $\tilde x$**

---

# Example

Take $X$ the hyperbolic cylinder $\langle\tau\rangle\backslash\mathbb{H}^2$ with $\tau:z\mapsto e^\ell z$, and let $x=\pi(i)$, $\tilde x=i$. The loop that runs once around the cylinder along the core geodesic lifts to the segment of the imaginary axis from $i$ to $e^\ell i$, which does **not** close up; its endpoint is $\tau\,\tilde x$, so $h_\omega=\tau$. Running around $m$ times gives $h_\omega=\tau^m$; running the other way gives $\tau^{-1}$; a small loop that bounds a disc lifts to a closed loop and gives $h_\omega=\mathrm{id}$. This is the entire dictionary visible in one picture, and it is the case §3 reduces every general situation to.

**Near-miss non-example — the dependence on $\tilde x$ is real.** Keep the same loop but start the lift at $q\tilde x$ instead of $\tilde x$, for some $q\in\Gamma$. The whole lifted arc is carried to its $q$-translate, so the new lift runs from $q\tilde x$ to $qh_\omega\tilde x = (qh_\omega q^{-1})(q\tilde x)$, and the recorded element becomes $qh_\omega q^{-1}$ — a **conjugate**, not the same element. So $h_\omega$ is not an invariant of the loop; only its conjugacy class is. Since the loop measure has already forgotten the basepoint, that is exactly the right amount of information to keep, and it is the content of [[Def - Free Homotopy Class and Conjugacy Class Correspondence]].

---

# Used in this paper at

- [[Def - Free Homotopy Class and Conjugacy Class Correspondence]] — the conjugation ambiguity just described *is* the correspondence
- [[Constr - The Periodised Kernel]] — the $\Gamma$-indexed sum whose terms are indexed by recorded deck transformations
- [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces|Theorem 3.2]] — Step 1 is the bridge decomposition $W^{t,\mathcal{E}}_{z\to z,X}=\sum_{h\in\Gamma}\pi_*W^{t,\mathcal{E}}_{\tilde z\to h\tilde z,\mathbb{H}^2}$, which is this dictionary applied to bridge measures rather than to individual loops
- [[Constr - Loop Mass in a Homotopy Class for Jump Processes]] — the place where the lifting fails: a càdlàg path admits no canonical lift, because the path-lifting theorem needs continuity
- [[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds|Theorem 7.1]] — the same dictionary with $\mathbb{H}^3$ and a Kleinian $\Gamma$

---

# Where this sits in my DAG

**This is one of the genuinely non-anchor rungs**, since *Algebraic Topology* is 🔵 (1,10) in the DAG. It reduces to vault pages that already exist: [[Def - Covering Space]], [[Def - Regular (Galois) Covering]], [[Def - Path-Product and the Fundamental Group]] and [[Thm - Galois Correspondence for Covering Spaces]] under Geometry of Physics / Algebraic Topology II. Those cover the unique path-lifting property, the simply-transitive action of the deck group on fibres of a universal cover, and the isomorphism $\pi_1(X,x)\cong\Gamma$.

The one thing to notice about the reduction is *which* covering-space fact is load-bearing: it is **unique path lifting**, and it requires the path to be continuous. That is exactly why the jump case of the paper needs a separate convention, and the dependency is recorded on [[Constr - Loop Mass in a Homotopy Class for Jump Processes]].
