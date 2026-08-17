---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Deck Transformations and the Lift of a Rooted Loop"
  - "Def - Conjugacy Class"
  - "Def - Geometrically Finite Surfaces, Cusps and Funnels"
tags: [paper, topology, hyperbolic-geometry, group-theory]
---

# Notation

- $\simeq_X$ — free homotopy of oriented closed curves in $X$
- $h_\omega\in\Gamma$ — the deck transformation recorded by a rooted loop, as on [[Def - Deck Transformations and the Lift of a Rooted Loop]]
- $[h]_{\mathrm{conj}}=\{qhq^{-1} : q\in\Gamma\}$ — the conjugacy class of $h$ in $\Gamma$
- $\mathcal{P}_X$ — the set of primitive oriented closed geodesics on $X$; $\ell_\gamma$ the length of $\gamma\in\mathcal{P}_X$
- $\mathcal{C}_X(\gamma^m)$ — the free homotopy class of oriented closed curves winding $m$ times around $\gamma$, $m\geq1$
- $\tau\in\Gamma$ — a chosen representative of the primitive hyperbolic conjugacy class corresponding to $\gamma$

---

# In plain language

A **free** homotopy class of loops is a homotopy class in which the basepoint is allowed to move. That is the right notion here because the loop measure has already integrated the basepoint away: a loop in $\mathcal{C}_X$ carries no marked point, so the only homotopy notion available to it is the basepoint-free one.

The previous page showed that a *rooted* loop records an element $h_\omega\in\Gamma$, and that changing the lift $\tilde x\mapsto q\tilde x$ changes the record to $qh_\omega q^{-1}$. Free homotopy is exactly the equivalence that forgets that ambiguity. So:

> **free homotopy classes of oriented closed curves on $X$ $\longleftrightarrow$ conjugacy classes in $\Gamma$.**

That single bijection is the paper's entire bridge between topology and algebra. Every mass computation in §3 begins by using it to replace "restrict the loop measure to a free homotopy class" by "restrict the periodised kernel to a conjugacy class", and the second is something an integral can see.

The refinement that makes the formulas explicit: on a hyperbolic surface, every non-trivial non-peripheral class contains a **unique closed geodesic representative**. That geodesic is $m\gamma$ — the $m$-fold traversal of a primitive closed geodesic $\gamma$ — of length $m\ell_\gamma$. On the group side, the class corresponds to $[\tau^m]_{\mathrm{conj}}$ for a [[Def - Primitive Hyperbolic Element and Translation Length|primitive hyperbolic]] $\tau$. So the data of a class is a pair $(\gamma,m)$, and every formula in the paper is a function of $\ell_\gamma$ and $m$ alone.

---

# The definition

> **Definition (free homotopy class).** Two oriented closed curves in $X$ are **freely homotopic**, written $\simeq_X$, if one can be deformed continuously into the other through closed curves, with no basepoint fixed. The equivalence classes are the **free homotopy classes of oriented closed curves**.

> **The correspondence.** In a free homotopy class the loops are not tied to any basepoint, so different loops start at different points of $X$ and lift to arcs starting at different points of $\mathbb{H}^2$. Each arc ends at $h_\omega$ applied to its own lifted starting point, but the element it records depends on which point of the fibre the arc begins at: changing the start from $\tilde x$ to $q\tilde x$ carries the whole arc to its $q$-translate, and the recorded element changes to the conjugate $qh_\omega q^{-1}$ — while the displacement length is unchanged. Hence
> $$\Big\{\text{free homotopy classes of oriented closed curves on }X\Big\} \;\longleftrightarrow\; \Big\{\text{conjugacy classes in }\Gamma\Big\},$$
> a bijection.

> **Standing convention (non-trivial, non-peripheral).** A class is **non-trivial** if its loops are not null-homotopic, and **non-peripheral** if its loops are neither freely homotopic into a cusp nor freely homotopic to a boundary component. From §3 onwards, unless otherwise stated, all free homotopy classes are assumed non-trivial and non-peripheral. **Each such class singles out a unique closed geodesic representative $m\gamma$ with length $m\ell_\gamma$.**

Writing $\mathcal{P}_X$ for the set of primitive oriented closed geodesics on $X$, each $\gamma\in\mathcal{P}_X$ corresponds to a primitive hyperbolic conjugacy class in $\Gamma$ with translation length $\ell_\gamma$, and for $m\geq1$ one writes $\mathcal{C}_X(\gamma^m)$ for the class winding $m$ times around $\gamma$, corresponding to
$$[\tau^m]_{\mathrm{conj}} = \{h\tau^m h^{-1} : h\in\Gamma\}.$$

---

# Types and signatures

- $\simeq_X$ — an equivalence relation on the set of oriented closed curves in $X$; **orientation-sensitive**, so $\gamma$ and $\bar\gamma$ are distinct classes
- the correspondence — a bijection between two sets, both countable when $\Gamma$ is geometrically finite
- $\mathcal{P}_X$ — a countable set; the counting function $N_X(R)=\#\{\gamma : \ell_\gamma\leq R\}$ is finite for every $R$
- $(\gamma,m)\mapsto\mathcal{C}_X(\gamma^m)$ — a bijection from $\mathcal{P}_X\times\mathbb{Z}_{\geq1}$ onto the non-trivial non-peripheral classes
- $\ell_\gamma\in(0,\infty)$ — the length of the primitive geodesic, equal to the translation length of $\tau$

---

# Example

The hyperbolic cylinder $X=\langle\tau\rangle\backslash\mathbb{H}^2$ with $\tau:z\mapsto e^\ell z$. Here $\Gamma$ is abelian, so every conjugacy class is a single element, and the correspondence reads: the free homotopy classes are indexed by $\mathbb{Z}$, with $\tau^m$ corresponding to "wind $m$ times around the core geodesic". The non-trivial ones are $m\neq0$; the positive $m$ give $\mathcal{C}_X(\gamma^m)$, and the negative ones give $\mathcal{C}_X(\bar\gamma^{|m|})$ for the reverse-oriented core geodesic. Each class contains exactly one closed geodesic, the $|m|$-fold traversal of the core, of length $|m|\ell$.

**Near-miss non-example — orientation matters, and it has consequences.** The curve $\bar\gamma$ obtained by traversing $\gamma$ backwards is **not** freely homotopic to $\gamma$ as an oriented curve, and on the group side $\tau$ is **not** conjugate to $\tau^{-1}$ in a torsion-free Fuchsian group. (An element conjugating $\tau$ to $\tau^{-1}$ would have to reverse the axis of $\tau$, and no orientation-preserving hyperbolic isometry in a torsion-free discrete group does that.) So $\gamma$ and $\bar\gamma$ are two distinct elements of $\mathcal{P}_X$ of the same length. **That is exactly why $N_{\mathrm{sys}}\geq2$** in [[Thm - Concentration on Systolic Classes|the s→∞ analysis of §6.1]] — the limiting measure is uniform on at least two atoms rather than a point mass, and the reason is a fact about orientation stated here.

**Second near-miss.** A loop around a cusp records a non-identity **parabolic** element, so its class is non-trivial. But it is peripheral: it has no closed geodesic representative, its length infimum is $0$ and is not attained, and there is no $\ell_\gamma$ for it. Every formula in §3 fails to parse for such a class, which is why they are excluded by convention rather than handled. See [[Def - Geometrically Finite Surfaces, Cusps and Funnels]].

---

# Used in this paper at

- [[Def - Centraliser and Coset Enumeration of a Conjugacy Class]] — the next step: enumerating $[\tau^m]_{\mathrm{conj}}$ without repetition
- [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces|Theorem 3.2]] — the correspondence is what makes "restrict to $\mathcal{C}_X(\gamma^m)$" equal "restrict the sum to $[\tau^m]_{\mathrm{conj}}$"
- [[Constr - Loop Mass in a Homotopy Class for Jump Processes]] — the correspondence fails for càdlàg paths, and the restriction to $[\tau^m]_{\mathrm{conj}}$ is promoted from a consequence to a definition
- [[Def - Marked Length Spectrum]] — the marked length spectrum is a function on exactly these classes
- [[Constr - The Mass in a Homology Class]] — homology is the abelianisation, so passing from conjugacy classes to homology classes is a further, much coarser, quotient
- [[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds|Theorem 7.1]] — the same correspondence for a Kleinian group, with loxodromic in place of hyperbolic

---

# Where this sits in my DAG

Two non-anchor rungs, both already in the vault. The topology side reduces to [[Def - Deck Transformations and the Lift of a Rooted Loop]] and thence to covering-space theory ([[Def - Covering Space]], [[Thm - Galois Correspondence for Covering Spaces]]) — *Algebraic Topology* is 🔵 so this genuinely needs the pages. The algebra side is [[Def - Conjugacy Class]] from Group Theory II, elementary and already written.

Not reduced here: the existence and uniqueness of the closed geodesic representative in each non-trivial non-peripheral class. That is standard hyperbolic geometry, quoted from Buser or Katok; it is the geometric input that makes the correspondence *useful* rather than merely true, since it is what attaches a length to a class.
