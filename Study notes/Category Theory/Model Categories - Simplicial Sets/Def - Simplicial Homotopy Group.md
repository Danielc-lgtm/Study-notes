---
type: definition
subject: model-categories
prereqs:
  - "Def - Kan Complex and the Nerve"
  - "Def - Kan Fibration and Anodyne Extension"
  - "Def - Homotopy"
  - "Def - Higher Homotopy Group"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $X$ is a [[Def - Kan Complex and the Nerve|Kan complex]] — a [[Def - Simplicial Set|simplicial set]] in which every horn fills — with a chosen basepoint $x \in X_0$, regarded interchangeably as a $0$-simplex or as the map $x : \Delta^0 \to X$. We write $s_0^{(n)} x$, or just $\ast$ when the dimension is clear, for the totally **degenerate** $n$-simplex at $x$ (apply degeneracies $n$ times). For $n$-simplices $\sigma$ the faces are $d_0\sigma, \dots, d_n\sigma$. Two $n$-simplices $\sigma, \tau$ with the same boundary are **homotopic rel $\partial$**, written $\sigma \sim \tau$, if there is an $(n+1)$-simplex $H$ realising a homotopy between them fixing the boundary (made precise below). The set of $n$-simplices with degenerate boundary, modulo this relation, is $\pi_n(X, x)$. The classical topological [[Def - Higher Homotopy Group|homotopy group]] of a [[Def - Topological Space|space]] $Y$ is written $\pi_n(Y, y)$. The full registry is on [[Model Categories — The Model Category of Simplicial Sets]].

---

# Axiom Motivation

We want homotopy groups for simplicial sets, defined so that they agree with the topological homotopy groups under [[Thm - Geometric Realization is a Quillen Equivalence|realisation]] — $\pi_n(\mathrm{Sing}\,Y) \cong \pi_n(Y)$ — but computed entirely combinatorially, without ever drawing a sphere or a continuous map. The whole question is how to say "a map $S^n \to X$ based at $x$, up to based homotopy" in the language of simplices, and why the construction *forces* the Kan condition on $X$.

Begin with the topological picture. A based map $S^n \to Y$ is the same as a map $D^n \to Y$ sending the boundary $\partial D^n = S^{n-1}$ to the basepoint — a disk with collapsed rim. The simplicial avatar of "an $n$-disk with collapsed boundary" is an **$n$-simplex with totally degenerate boundary**: an $n$-simplex $\sigma$ of $X$ all of whose faces $d_i\sigma$ are the degenerate simplex at $x$. So the *elements* of $\pi_n(X, x)$ should be these "spheroids" $\sigma$. This part needs no Kan condition; it is just a definition of the underlying set.

The difficulty is the *equivalence relation*. We want to identify two spheroids when they are homotopic rel boundary, and a homotopy between $n$-simplices $\sigma, \tau$ is naturally encoded by an $(n+1)$-simplex $H$ whose top and bottom faces are $\sigma$ and $\tau$ and whose remaining faces are degenerate (the homotopy fixes the boundary). The relation "$\sigma \sim \tau$ if such an $H$ exists" is the obvious candidate — and here is the crux: **this relation is reflexive and (with care) symmetric for any $X$, but it is transitive only when $X$ is a Kan complex.** Transitivity is the problem. Given homotopies $\sigma \sim \tau$ and $\tau \sim \rho$, witnessed by $(n+1)$-simplices $H_1, H_2$, we want to produce a single homotopy $\sigma \sim \rho$. The two simplices $H_1, H_2$ share the face $\tau$; together with the degenerate faces they assemble into a *horn* $\Lambda^{n+2}_j$ in $X$, and a filler of that horn supplies an $(n+2)$-simplex whose remaining face is exactly the desired homotopy $\sigma \sim \rho$. The filler exists precisely because $X$ is Kan. So **the Kan condition is not an extra hypothesis bolted on — it is the exact condition that makes the homotopy relation transitive, hence an equivalence relation, hence $\pi_n$ a well-defined set of classes.**

The same mechanism supplies the *group operation*. To add two spheroids $\sigma, \tau \in \pi_n(X, x)$ one wants their "concatenation". One builds a horn $\Lambda^{n+1}_k$ whose faces are $\sigma$, $\tau$, and degenerate simplices, fills it by the Kan condition, and reads off the composite as the remaining face. Filling is what produces the sum; the Kan condition supplies the filler; and a second round of horn-filling shows the result is independent of choices and that the operation is associative with inverses. For $n \ge 2$ a further horn argument (the simplicial **Eckmann–Hilton** argument) shows the operation is abelian, recovering the classical fact that [[Def - Higher Homotopy Group|higher homotopy groups are abelian]]. Every single piece of the group structure is a horn-filling, which is why the definition lives or dies by fibrancy.

What goes wrong if we ignore the Kan condition and define $\pi_n(X)$ for arbitrary $X$ by the same formula? The relation fails to be transitive, so the "quotient" is not even a well-defined set of equivalence classes, let alone a group. The standard witness is $\Delta^1$: the vertices $0$ and $1$ are joined by the edge $0 \to 1$, so they are "homotopic" in the candidate sense for $\pi_0$, but there is no edge $1 \to 0$, so the relation is not symmetric and the naive $\pi_0(\Delta^1)$ is ill-defined as a quotient. The repair, for a general simplicial set, is to first take a [[Def - Cofibrant and Fibrant Objects|fibrant replacement]] $X \xrightarrow{\sim} RX$ (an anodyne map to a Kan complex) and *define* $\pi_n(X) := \pi_n(RX)$; this is forced, and it is why the homotopy groups are an invariant of the homotopy type rather than of the point-set simplicial set.

---

# The Definition

Let $X$ be a [[Def - Kan Complex and the Nerve|Kan complex]] with basepoint $x \in X_0$.

**The underlying set.** For $n \ge 1$, let
$$Z_n(X, x) = \{\sigma \in X_n : d_i\sigma = s_0^{(n-1)} x \text{ for all } 0 \le i \le n\},$$
the set of $n$-simplices all of whose faces are the degenerate simplex at $x$ (the **spheroids** based at $x$). For $n = 0$, $Z_0(X, x) = X_0$.

**The homotopy relation.** Two spheroids $\sigma, \tau \in Z_n(X, x)$ are **homotopic rel basepoint**, $\sigma \sim \tau$, if there is an $(n+1)$-simplex $H \in X_{n+1}$ whose last two faces are $\sigma$ and $\tau$ and all of whose other faces are the degenerate spheroid at $x$:
$$d_n H = \sigma, \qquad d_{n+1} H = \tau, \qquad d_i H = s_0^{(n)} x \ \text{ for } 0 \le i \le n-1.$$
So $H$ has $\sigma$ and $\tau$ as two adjacent faces and all remaining faces totally degenerate at $x$ — the combinatorial picture of "a homotopy from $\sigma$ to $\tau$ that fixes the basepoint". On a Kan complex this is an equivalence relation.

**The homotopy group.** The **$n$th simplicial homotopy group** (or set, for $n = 0$) is
$$\pi_n(X, x) = Z_n(X, x) / {\sim}.$$
For $n \ge 1$ it is a group, with multiplication defined by horn-filling: given classes $[\sigma], [\tau]$, choose an $(n+1)$-simplex $\omega$ that is a filler of the horn $\Lambda^{n+1}_n$ with $d_{n-1}\omega = \sigma$, $d_{n+1}\omega = \tau$ and the other listed faces degenerate; then $[\sigma]\cdot[\tau] := [d_n\omega]$. This is well-defined (independent of the filler and of representatives) and gives a group structure, abelian for $n \ge 2$. The basepoint class $[\ast]$ is the identity. For $n = 0$, $\pi_0(X)$ is the set of **connected components** $X_0 / {\sim}$, where $x \sim x'$ when there is an edge $x \to x'$ (a pointed set, with basepoint $[x]$).

**Functoriality and weak equivalence.** A map of Kan complexes $f : X \to X'$ with $f(x) = x'$ induces $f_* : \pi_n(X, x) \to \pi_n(X', x')$ for all $n$. A map of Kan complexes is a **weak equivalence** if and only if it induces a bijection on $\pi_0$ and an isomorphism on $\pi_n$ for every basepoint and every $n \ge 1$; this is the *internal* characterisation of the weak equivalences of the Kan–Quillen [[Thm - Simplicial Sets Form a Model Category|model structure]].

---

# Categorical / Structural Definition

The structural description packages all the spheroids and homotopies at once. A based $n$-spheroid is a map of pointed simplicial sets $\Delta^n / \partial\Delta^n \to X$ (the quotient $\Delta^n/\partial\Delta^n$ is the simplicial $n$-sphere $S^n_s$ with collapsed boundary), and the homotopy relation is left [[Def - Cylinder Object, Path Object, and Homotopy|simplicial homotopy]] with respect to the cylinder $\Delta^1 \times (-)$. So
$$\pi_n(X, x) = [\,S^n_s,\, X\,]_* = \pi_0\big(\mathrm{Map}_*(S^n_s, X)\big),$$
the set of based homotopy classes of maps from the simplicial $n$-sphere, equivalently the components of the pointed function complex. The Kan condition on $X$ is what makes $\mathrm{Map}_*(S^n_s, X)$ itself a Kan complex (the [[Def - Quillen Adjunction and Quillen Equivalence|simplicial mapping space]] into a fibrant object is fibrant), so that taking $\pi_0$ yields a homotopy-invariant set with a group structure inherited from the co-group structure of $S^n_s$.

This is exactly the model-categorical definition of homotopy groups specialised to $\mathbf{sSet}$: in any pointed [[Def - Model Category|model category]], $\pi_n(X) = [\Sigma^n S^0, X]$ where $\Sigma$ is the suspension and $[-,-]$ is maps in the homotopy category, and the simplicial $n$-sphere $S^n_s$ is the suspension $\Sigma^n$ of the simplicial $0$-sphere. The horn-filling definition above is the *computable* unwinding of this *conceptual* one, valid because every object is [[Def - Cofibrant and Fibrant Objects|cofibrant]] and $X$ is fibrant.

---

# Relate to Other Fields / Compression

The simplicial homotopy group is the combinatorial twin of the classical [[Def - Higher Homotopy Group|topological homotopy group]]. The compression: **replace "based map of a sphere, up to homotopy" by "simplex with degenerate boundary, up to horn-fillable homotopy"** — and the Kan condition is exactly the price of making the second phrase well-defined. The agreement theorem $\pi_n(\mathrm{Sing}\,Y, y) \cong \pi_n(Y, y)$ says the two twins are literally the same group, so all of classical homotopy theory can be computed by manipulating finite sets of simplices.

When $X$ is a simplicial *abelian group* (or more generally has abelian-group structure level-wise), the [[Def - Homotopy|Dold–Kan correspondence]] identifies $\pi_n(X)$ with the homology $H_n(NX)$ of the normalised chain complex $NX$. Under this identification the simplicial homotopy group *is* a homology group, and the horn-filling that defines the group operation becomes the cycle-modulo-boundary quotient of homological algebra. This is the precise sense in which homotopy groups generalise homology groups: homology is the *abelian* (or *stable*, or *linearised*) shadow of homotopy.

**True name:** $\pi_n(X, x)$ is **"degenerate-boundary $n$-simplices modulo horn-fillable homotopy"** — and the operational fact to carry is that it is *only defined for Kan $X$*, with the Kan condition supplying both the equivalence relation and the group law. When you see $\pi_n$ of a non-fibrant simplicial set, mentally insert a fibrant replacement.

---

# Examples / Corollaries

**Is an instance — $\pi_n(\mathrm{Sing}\,Y) \cong \pi_n(Y)$.** For any [[Def - Topological Space|space]] $Y$, $\mathrm{Sing}(Y)$ is a [[Def - Kan Complex and the Nerve|Kan complex]] and its simplicial homotopy groups are canonically isomorphic to the topological homotopy groups of $Y$. A spheroid in $\mathrm{Sing}(Y)$ is a singular simplex $|\Delta^n| \to Y$ collapsing $\partial|\Delta^n|$ to $y$, i.e. a based map $|\Delta^n|/\partial \cong S^n \to Y$, and the simplicial homotopy is a singular homotopy. This is the agreement theorem and the reason the definition is the right one.

**Is an instance — $\pi_n(\Delta^0) = 0$.** The point $\Delta^0$ is a Kan complex with a single simplex in each dimension (all degenerate above dimension $0$). The only spheroid is the degenerate one, so $\pi_n(\Delta^0)$ is trivial for all $n$, and $\pi_0(\Delta^0)$ is a single point. The point is contractible, as it must be.

**Is an instance — $\pi_1$ of the nerve of a group.** For a group $G$, the [[Def - Kan Complex and the Nerve|nerve]] $N(G)$ of the one-object [[Def - Groupoid|groupoid]] with morphisms $G$ is a Kan complex, and $\pi_1(N(G), \ast) \cong G$ while $\pi_n(N(G)) = 0$ for $n \ne 1$. The spheroids in dimension $1$ are the elements of $G$ (edges based at the unique vertex), the homotopy relation is trivial (the boundary forces equality), and the horn-filling group law is exactly the group multiplication of $G$. So $|N(G)| = BG = K(G,1)$, the [[Def - Path-Product and the Fundamental Group|classifying space]].

**Is NOT computable this way — $\pi_n$ of a non-Kan simplicial set.** For $\Delta^1$ the candidate $\pi_0$ is ill-defined: the homotopy relation on vertices is "joined by an edge", which is *not symmetric* in $\Delta^1$ (there is an edge $0 \to 1$ but none $1 \to 0$), so the quotient is not a set of equivalence classes. The fix is to fibrantly replace: $\Delta^1 \xrightarrow{\sim} \Delta^0$ (the anodyne collapse, since $\Delta^1$ realises to a contractible interval), giving $\pi_n(\Delta^1) := \pi_n(\Delta^0) = 0$. This is the canonical reminder that the formula is meaningless without the Kan condition.

**Corollary — homotopy groups are abelian for $n \ge 2$.** The simplicial Eckmann–Hilton argument: for $n \ge 2$ there are two ways to fill the relevant horn (two "directions" in which to concatenate spheroids), they agree up to homotopy, and the agreement forces commutativity. This recovers the topological theorem that [[Def - Higher Homotopy Group|higher homotopy groups are abelian]] purely combinatorially.

**Corollary — Kan complexes with all $\pi_n$ trivial are contractible.** A Kan complex $X$ with $\pi_0$ a point and $\pi_n(X, x) = 0$ for all $n \ge 1$ and all basepoints is weakly equivalent to $\Delta^0$, hence (being fibrant and cofibrant) homotopy equivalent to a point. This is the Whitehead theorem in $\mathbf{sSet}$: a $\pi_n$-isomorphism between Kan complexes is a homotopy equivalence.

**Calibration check.** Verify that the homotopy relation is reflexive (use a degenerate $(n+1)$-simplex) and explain why transitivity needs a horn filler in dimension $n+2$ — pinpointing exactly where the Kan condition is used. Confirm that $\pi_0(\Delta^0)$ is a single point and that $\pi_1(N(G)) \cong G$ by matching edges with group elements. And state why $\pi_n$ of a non-fibrant simplicial set must be defined via fibrant replacement.

---

# Unlocked by This

> [!tip] The Internal Weak Equivalences *(from this chapter)*
> A map of [[Def - Kan Complex and the Nerve|Kan complexes]] is a weak equivalence of the Kan–Quillen [[Thm - Simplicial Sets Form a Model Category|model structure]] if and only if it is a $\pi_n$-isomorphism for all $n$ and all basepoints. The simplicial homotopy groups are therefore the *internal* definition of weak equivalence, removing the need to leave $\mathbf{sSet}$ for $\mathbf{Top}$.

> [!tip] The Long Exact Sequence of a Fibration *(from this chapter)*
> A [[Def - Kan Fibration and Anodyne Extension|Kan fibration]] $F \to E \to B$ gives a long exact sequence $\dots \to \pi_n F \to \pi_n E \to \pi_n B \to \pi_{n-1}F \to \dots$ of simplicial homotopy groups, the combinatorial form of the homotopy long exact sequence — the main computational tool of homotopy theory.

> [!tip] Homotopy Groups in Any Pointed Model Category *(from Model Categories — Pointed)*
> The pattern $\pi_n(X) = [\Sigma^n S^0, X]$ generalises to any **pointed model category** with a suspension $\Sigma$ and loop $\Omega$; the simplicial case is the prototype, and the resulting **stable homotopy groups** of spectra are its stabilisation.
