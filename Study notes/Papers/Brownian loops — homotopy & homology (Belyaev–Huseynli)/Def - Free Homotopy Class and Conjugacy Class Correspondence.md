---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Deck Transformations and the Lift of a Rooted Loop"
  - "Def - Geometrically Finite Surfaces, Cusps and Funnels"
  - "Def - Conjugacy Class"
tags: [paper, topology, hyperbolic-geometry, group-theory]
---

# Signature

| symbol | type |
|---|---|
| $\simeq_X$ | free homotopy of oriented closed curves in $X$ — basepoint **not** fixed |
| $h_\omega$ | $\in\Gamma$, the [[Def - Deck Transformations and the Lift of a Rooted Loop\|recorded element]] of a rooted loop |
| $[h]_{\mathrm{conj}}$ | $=\{qhq^{-1}:q\in\Gamma\}$ |
| $\mathcal{P}_X$ | set of **primitive oriented** closed geodesics on $X$; countable |
| $\ell_\gamma$ | $\in(0,\infty)$ — length of $\gamma\in\mathcal{P}_X$; $=$ translation length of any representative |
| $\tau$ | $\in\Gamma$; a representative of the primitive hyperbolic class of $\gamma$ |
| $m$ | $\in\mathbb{Z}_{\geq1}$ — winding number |
| $\mathcal{C}_X(\gamma^m)$ | the free homotopy class winding $m$ times around $\gamma$ |
| $\bar\gamma$ | the orientation reversal of $\gamma$; an element of $\mathcal{P}_X$ distinct from $\gamma$ |

---

# Definition

> **Definition (free homotopy).** Oriented closed curves $c_0,c_1$ in $X$ are **freely homotopic**, $c_0\simeq_Xc_1$, if there is a continuous $H:S^1\times[0,1]\to X$ with $H(\cdot,0)=c_0$, $H(\cdot,1)=c_1$ — **no basepoint fixed**.

> **Correspondence.** The map $\{$free homotopy classes of oriented closed curves on $X\}\to\{$conjugacy classes in $\Gamma\}$ sending a class to $[h_\omega]_{\mathrm{conj}}$ (for any rooted representative $\omega$ and any lift) is a **bijection**.
>
> *Well defined*, and *why*: by [[Def - Deck Transformations and the Lift of a Rooted Loop|(F2)]], changing the lift from $\tilde x$ to $q\tilde x$ replaces $h_\omega$ by $qh_\omega q^{-1}$; and moving the basepoint along a free homotopy has the same effect. So $h_\omega$ is not an invariant of the free class, but $[h_\omega]_{\mathrm{conj}}$ is.

> **Definition (the classes indexed).** Under the standing convention [[Def - Geometrically Finite Surfaces, Cusps and Funnels|(D3)+(D4)]] — non-trivial, non-peripheral — the classes are exactly $\{\mathcal{C}_X(\gamma^m)\}$ for $\gamma\in\mathcal{P}_X$, $m\geq1$, with
> $$\mathcal{C}_X(\gamma^m)\ \longleftrightarrow\ [\tau^m]_{\mathrm{conj}}=\{h\tau^mh^{-1}:h\in\Gamma\},$$
> and each class contains a **unique** closed geodesic representative, the $m$-fold traversal of $\gamma$, of length $m\ell_\gamma$.

> **(F1) The data of a class is the pair $(\gamma,m)$.** $(\gamma,m)\mapsto\mathcal{C}_X(\gamma^m)$ is a bijection $\mathcal{P}_X\times\mathbb{Z}_{\geq1}\to\{$non-trivial non-peripheral classes$\}$. **Every formula in the paper is a function of $\ell_\gamma$ and $m$ alone.**
>
> **(F2) Orientation-sensitivity.** $\bar\gamma\neq\gamma$ in $\mathcal{P}_X$: a hyperbolic element of a torsion-free Fuchsian group is never conjugate to its inverse. Consequence: $N_{\mathrm{sys}}\geq2$ in [[Thm - Concentration on Systolic Classes]].

---

# Type card

> [!abstract] Type card — the correspondence
> **Given.** **(H1)** $\Gamma$ torsion-free Fuchsian, $X=\Gamma\backslash\mathbb{H}^2$ geometrically finite. **(H2)** the standing convention (D3),(D4).
>
> **Produces.** A bijection $\{$free homotopy classes$\}\leftrightarrow\{$conjugacy classes in $\Gamma\}$, and an indexing of the non-trivial non-peripheral classes by $\mathcal{P}_X\times\mathbb{Z}_{\geq1}$ with a length $m\ell_\gamma$ attached to each.
>
> **Lets you.** Replace "restrict the loop measure to a free homotopy class" — which an integral cannot see — by "restrict the periodised kernel to a conjugacy class", which it can. **This is the paper's bridge between topology and analysis.**

---

# Depends on

- [[Def - Deck Transformations and the Lift of a Rooted Loop]] — (F2) there is the well-definedness here
- [[Def - Conjugacy Class]] — the target
- [[Def - Geometrically Finite Surfaces, Cusps and Funnels]] — (D3),(D4)
- [[Def - Primitive Hyperbolic Element and Translation Length]] — $\mathcal{P}_X$ and $\ell_\gamma$
- 🟢 existence and uniqueness of the closed geodesic in a non-trivial non-peripheral class — quoted (Buser, Katok)

---

# Checks

**Instance.** $X=\langle\tau\rangle\backslash\mathbb{H}^2$, $\tau:z\mapsto e^{\ell}z$. $\Gamma$ abelian $\Rightarrow$ every conjugacy class is a singleton, so classes are indexed by $\mathbb{Z}$: $\tau^m\leftrightarrow$ "wind $m$ times around the core". Non-trivial: $m\neq0$; $m>0$ gives $\mathcal{C}_X(\gamma^m)$, $m<0$ gives $\mathcal{C}_X(\bar\gamma^{\lvert m\rvert})$. Each contains exactly one closed geodesic, of length $\lvert m\rvert\ell$.

**Non-instance (fails F2 if orientation is forgotten).** $\bar\gamma$ is **not** freely homotopic to $\gamma$ as an oriented curve; on the group side, no $q\in\Gamma$ conjugates $\tau$ to $\tau^{-1}$, since such a $q$ would preserve the axis while reversing it — an orientation-reversing isometry, or an elliptic rotation by $\pi$, both excluded by torsion-freeness and $\Gamma\subseteq\mathrm{PSL}(2,\mathbb{R})$. So $\gamma,\bar\gamma$ are two distinct elements of $\mathcal{P}_X$ of equal length. **This is exactly why the $s\to\infty$ limit of $\mathbb{P}_s$ is uniform on $\geq2$ atoms rather than a point mass.**

**Non-instance (fails D4).** A loop around a cusp records a non-identity **parabolic**, so its class is non-trivial but peripheral. It has no closed geodesic, $\inf_\eta\ell_g(\eta)=0$ not attained, and no $\ell_\gamma$ exists. Every formula in §3 fails to parse.

---

# Used at

- [[Def - Centraliser and Coset Enumeration of a Conjugacy Class]] — enumerating $[\tau^m]_{\mathrm{conj}}$ without repetition
- [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces]] — Step 1: "restrict to $\mathcal{C}_X(\gamma^m)$" $=$ "restrict the sum to $[\tau^m]_{\mathrm{conj}}$"
- [[Constr - Loop Mass in a Homotopy Class for Jump Processes]] — where the correspondence fails and the restriction becomes a definition
- [[Def - Marked Length Spectrum]] — $\mathrm{MLS}$ is a function on exactly these classes
- [[Constr - The Mass in a Homology Class]] — homology is the further, much coarser, abelian quotient
- [[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds]] — same with loxodromic in place of hyperbolic

---

# Commentary

> [!note]- Commentary (skippable)
> Free homotopy is the right notion here because the loop measure has already integrated the basepoint away: a loop in $\mathcal{C}_X$ carries no marked point, so the only homotopy notion available to it is the basepoint-free one. And the conjugation ambiguity of the recorded element is *exactly* the ambiguity free homotopy introduces — which is why the correspondence is a bijection rather than a mere surjection.
>
> (F1) is the fact that makes §3 computable at all: after the correspondence, the mass of a class can only depend on $(\gamma,m)$, and after [[Ext - Wang–Xue Strip Identity|(WX)]] it depends only on $\ell_\gamma$ and $m$. Nothing about the genus, the other geodesics, or the global geometry can enter. That is why [[Thm - Loop Masses Determine the Marked Length Spectrum|Proposition 3.11]] can invert class-by-class instead of solving a global reconstruction problem.
