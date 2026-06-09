---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Prime and Maximal Ideal"
  - "Def - Noetherian Ring"
  - "Def - The Prime Spectrum (Spec)"
  - "Def - Local Ring and Residue Field"
  - "Def - Ideal"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $R$ be a ring and $\operatorname{Spec} R$ its [[Def - The Prime Spectrum (Spec)|prime spectrum]], the set of [[Def - Prime and Maximal Ideal|prime ideals]] of $R$; $\operatorname{mSpec} R$ is the set of maximal ideals. We write $\mathfrak{p}, \mathfrak{q}$ for primes, $\mathfrak{m}$ for a maximal ideal, $I, \mathfrak{a}$ for ideals. A **chain of primes of length $d$** is a strictly increasing sequence $\mathfrak{p}_0 \subsetneq \mathfrak{p}_1 \subsetneq \cdots \subsetneq \mathfrak{p}_d$ of $d+1$ distinct primes; the *length* is the number of strict inclusions, $d$, not the number of primes. We write $\operatorname{ht}\mathfrak{p}$ for the **height** of $\mathfrak{p}$, $\dim R$ for the **Krull dimension**, and $R_{\mathfrak{p}}$ for the [[Def - Local Ring and Residue Field|localization]] of $R$ at $\mathfrak{p}$. The full registry is on [[Commutative Algebra XII — Dimension Theory]].

This is a compound page: it defines three interlocking notions — the **length of a chain of primes**, the **height** $\operatorname{ht}\mathfrak{p}$ of a prime (and more generally $\operatorname{ht} I$ of an ideal), and the **Krull dimension** $\dim R$ — because they are introduced together and none is fully usable without the others.

---

# Axiom Motivation

We want a purely algebraic number attached to a ring $R$ that deserves to be called its **dimension** — a number that, when $R = k[X_1, \dots, X_n]$ is a polynomial ring, comes out to $n$, and when $R = k[X_1,\dots,X_n]/I$ is the coordinate ring of a geometric object, comes out to the geometric dimension of that object: $0$ for a finite set of points, $1$ for a curve, $2$ for a surface, and so on. The problem is that a ring is not a vector space; there is no obvious notion of "number of independent coordinates". The whole of dimension theory is the search for the right surrogate, and this page installs the one that turns out to work.

The clue comes from how dimension behaves in linear algebra, where it *is* defined by chains. For a vector space $V$, $\dim_k V$ is the supremum of lengths of strictly increasing chains of subspaces $\{0\} = V_0 \subsetneq V_1 \subsetneq \cdots \subsetneq V_d = V$. In $\mathbb{R}^2$ the longest such chain is $\{0\} \subsetneq (\text{a line}) \subsetneq \mathbb{R}^2$, of length $2$. The reason this measures dimension is that each strict inclusion of subspaces must increase the dimension by at least one, so the longest chain has exactly $\dim V$ steps. We want to copy this idea — *dimension is the length of the longest chain* — but with the right notion of "subobject".

The right subobjects are **prime ideals**, not subspaces and not arbitrary ideals. Here is why. Geometrically, a prime ideal $\mathfrak{p}$ of the coordinate ring $A = k[X_1,\dots,X_n]/I$ corresponds to an irreducible closed subvariety of the variety $V(I)$ — an irreducible curve, surface, point, and so on inside $V(I)$. A strict inclusion $\mathfrak{p} \subsetneq \mathfrak{q}$ of primes corresponds to a *reverse* strict inclusion of subvarieties, $V(\mathfrak{q}) \subsetneq V(\mathfrak{p})$: the bigger prime cuts out the smaller variety. So a chain of primes $\mathfrak{p}_0 \subsetneq \cdots \subsetneq \mathfrak{p}_d$ is exactly a tower of irreducible subvarieties
$$V(\mathfrak{p}_0) \supsetneq V(\mathfrak{p}_1) \supsetneq \cdots \supsetneq V(\mathfrak{p}_d),$$
each strictly inside the previous — point inside curve inside surface inside the whole space. In affine $3$-space we have the chain $(0) \subsetneq (X) \subsetneq (X,Y) \subsetneq (X,Y,Z)$ of primes in $k[X,Y,Z]$, dual to the tower $\mathbb{A}^3 \supsetneq \{X=0\} \supsetneq \{X=Y=0\} \supsetneq \{X=Y=Z=0\}$, that is, $3$-space $\supsetneq$ plane $\supsetneq$ line $\supsetneq$ point. The length is $3$ — exactly the dimension we want. So we *define* dimension to be the longest such chain.

**Why prime ideals and not all ideals.** If we allowed *arbitrary* ideals in the chain, the number would be wrong — and infinite even for simple rings. In $k[X]$ we can build $(X^2) \subsetneq (X) \subsetneq k[X]$ and refine forever with $(X^n)$, so chains of arbitrary ideals have no longest length even though $k[X]$ is one-dimensional. Restricting to primes is what makes the count finite and geometric: only primes correspond to irreducible subvarieties, and a non-prime ideal like $(X^2)$ cuts out the same set as $(X)$ but with multiplicity — it is not a genuinely smaller *space*. The Krull dimension is built to see *spaces*, so it must ignore the non-reduced and reducible structure that non-prime ideals carry, which is exactly what passing to primes does.

**Why height is "codimension from below".** The dimension counts the longest chain in the *whole* ring; but we also want a local quantity, attached to a single prime $\mathfrak{p}$, measuring "how deep is $\mathfrak{p}$". The **height** of $\mathfrak{p}$ counts chains ending at $\mathfrak{p}$ — the supremum of $d$ over chains $\mathfrak{p}_0 \subsetneq \cdots \subsetneq \mathfrak{p}_d = \mathfrak{p}$. Geometrically this is the codimension of the subvariety $V(\mathfrak{p})$: the number of independent conditions needed to cut $V(\mathfrak{p})$ out of an irreducible component of $\operatorname{Spec} R$ that contains it. A minimal prime has height $0$ (no shorter prime below it — it is a whole irreducible component); a prime of height $1$ is a divisor, codimension one. The defining identity $\operatorname{ht}\mathfrak{p} = \dim R_{\mathfrak{p}}$ then says that height is genuinely a *local* invariant: to measure how deep $\mathfrak{p}$ sits, [[Def - Local Ring and Residue Field|localize at $\mathfrak{p}$]] — throw away everything not near the point — and take the dimension of the resulting local ring, whose chains are precisely the chains below $\mathfrak{p}$. This is why dimension theory of general rings reduces to dimension theory of *local* rings, the subject of the [[Thm - The Dimension Theorem for Noetherian Local Rings|dimension theorem]].

The one delicacy is the **convention for length**: a chain $\mathfrak{p}_0 \subsetneq \cdots \subsetneq \mathfrak{p}_d$ has $d+1$ primes but length $d$. We count *steps*, not *primes*, because we want the length of the trivial one-prime chain $\{\mathfrak{p}\}$ to be $0$ (a single point has codimension $0$ inside itself), and we want $\dim$ of a field to be $0$ (a field has only the prime $(0)$, one prime, no steps). If we counted primes the field would have dimension $1$, breaking the analogy with $\dim_k V = 0$ for $V = 0$. The off-by-one is the price of making the trivial cases come out right.

---

# The Definition

Let $R$ be a commutative ring.

## Length of a chain of primes

A **chain of prime ideals of length $d$** is a strictly increasing sequence
$$\mathfrak{p}_0 \subsetneq \mathfrak{p}_1 \subsetneq \cdots \subsetneq \mathfrak{p}_d, \qquad \mathfrak{p}_i \in \operatorname{Spec} R,$$
of $d+1$ distinct primes. Its **length** is $d$ (the number of strict inclusions).

## Height of a prime, and of an ideal

The **height** of a prime $\mathfrak{p} \in \operatorname{Spec} R$ is
$$\operatorname{ht}\mathfrak{p} = \sup\{\, d : \text{there is a chain } \mathfrak{p}_0 \subsetneq \cdots \subsetneq \mathfrak{p}_d = \mathfrak{p} \text{ of primes contained in } \mathfrak{p}\,\} \in \mathbb{Z}_{\geq 0} \cup \{\infty\}.$$
For an arbitrary ideal $I \subsetneq R$, the **height** of $I$ is the infimum of the heights of the primes above it:
$$\operatorname{ht} I = \inf\{\, \operatorname{ht}\mathfrak{p} : I \subseteq \mathfrak{p} \in \operatorname{Spec} R \,\}.$$
(For $\mathfrak{p}$ prime the two definitions agree, since $\mathfrak{p}$ is itself the smallest prime above $\mathfrak{p}$.)

## Krull dimension

The **Krull dimension** of $R$ is the supremum of the lengths of all chains of primes:
$$\dim R = \sup\{\, \operatorname{ht}\mathfrak{p} : \mathfrak{p} \in \operatorname{Spec} R \,\} = \sup\{\, d : \mathfrak{p}_0 \subsetneq \cdots \subsetneq \mathfrak{p}_d \text{ in } \operatorname{Spec} R \,\}.$$
By convention $\dim R = -1$ (or $-\infty$) for the zero ring, which has no primes.

## Two structural identities

Because a chain of primes that does not end at a maximal ideal can always be extended upward, the supremum is achieved at maximal ideals:
$$\dim R = \sup\{\, \operatorname{ht}\mathfrak{m} : \mathfrak{m} \in \operatorname{mSpec} R \,\}.$$
And because the primes contained in $\mathfrak{p}$ are exactly the primes of the localization $R_{\mathfrak{p}}$ (which has unique maximal ideal $\mathfrak{p}R_{\mathfrak{p}}$),
$$\operatorname{ht}\mathfrak{p} = \dim R_{\mathfrak{p}}, \qquad \text{hence} \qquad \dim R = \sup\{\, \dim R_{\mathfrak{m}} : \mathfrak{m} \in \operatorname{mSpec} R \,\}.$$
This is the reduction of global dimension to *local* dimension.

---

# Relate to Other Fields / Compression

The cleanest compression: **Krull dimension is the vector-space dimension formula $\dim V = (\text{longest chain of subspaces})$, with "subspace" replaced by "prime ideal" and the chain run the other way.** A chain of subspaces ascends to bigger subspaces; a chain of primes ascends to *smaller* subvarieties, because $V(-)$ is inclusion-reversing. So Krull dimension counts how many times you can strictly shrink an irreducible subvariety, which is the geometric codimension drop summed from the bottom — exactly the dimension.

**True name:** the operational name of $\dim R$ is *not* "supremum of chain lengths" — that is the definition, and chains are hard to enumerate directly. The operational name, valid for [[Def - Noetherian Ring|Noetherian]] local rings, is **"the degree of the Hilbert–Samuel polynomial" or, equivalently, "the minimal number of elements generating an ideal whose radical is the maximal ideal"**: $\dim(A,\mathfrak{m}) = \deg \ell(A/\mathfrak{m}^n) = \min\{r : \exists\, x_1,\dots,x_r \text{ with } \sqrt{(x_1,\dots,x_r)} = \mathfrak{m}\}$. This is the content of the [[Thm - The Dimension Theorem for Noetherian Local Rings|dimension theorem]], and it is what you actually compute with — you never chase chains of primes in practice.

**Height is codimension.** For $A$ a finitely generated domain over a field, $\operatorname{ht}\mathfrak{p} = \dim A - \dim A/\mathfrak{p}$, so height is literally codimension: the dimension of the ambient space minus the dimension of the subvariety $V(\mathfrak{p})$. A height-one prime is a divisor; **Krull's principal ideal theorem** is the statement that one equation cuts codimension exactly one, the algebraic core of intersection theory.

The construction is the same one used to define the **dimension of a topological space** combinatorially: the Krull dimension of $\operatorname{Spec} R$ in its Zariski topology equals the supremum of lengths of chains of irreducible closed subsets, which is one version of the *combinatorial dimension* of a space. So $\dim R$ is a topological invariant of $\operatorname{Spec} R$, not merely an algebraic one.

---

# Examples / Corollaries

**Is an instance — a field has dimension $0$.** A [[Def - Unit and Field|field]] $k$ has exactly one prime ideal, $(0)$. The only chain is $\{(0)\}$, of length $0$, so $\dim k = 0$. More generally any Artinian ring has dimension $0$: every prime is maximal, so no chain has a strict inclusion.

**Is an instance — $\mathbb{Z}$ and PIDs have dimension $1$.** In $\mathbb{Z}$ the primes are $(0)$ and the $(p)$ for $p$ prime, and the only strict inclusions are $(0) \subsetneq (p)$, so the longest chain has length $1$ and $\dim \mathbb{Z} = 1$. The same argument gives $\dim R = 1$ for any [[Def - Principal Ideal Domain|principal ideal domain]] that is not a field: $(0)$ is prime (the ring is a domain), every nonzero prime is maximal, and there is at least one nonzero prime. Here $\operatorname{ht}(p) = 1$ for each prime $p$, and $\operatorname{ht}(0) = 0$.

**Is an instance — $k[X_1,\dots,X_n]$ has dimension $n$.** The chain $(0) \subsetneq (X_1) \subsetneq (X_1,X_2) \subsetneq \cdots \subsetneq (X_1,\dots,X_n)$ exhibits $\dim k[X_1,\dots,X_n] \geq n$; equality is the content of [[Thm - Dimension of a Polynomial Ring|the dimension of a polynomial ring]]. Geometrically this is $\dim \mathbb{A}^n_k = n$. The prime $(X_1,\dots,X_i)$ has height $i$: it cuts out the codimension-$i$ linear subspace $\{X_1 = \cdots = X_i = 0\}$.

**Is NOT an instance — height is not "number of generators of $\mathfrak{p}$".** It is tempting to read height off the number of generators of $\mathfrak{p}$, but the two can differ: a prime can require strictly more generators than its height. The general bound is one-directional — **$\operatorname{ht}\mathfrak{p} \leq \mu(\mathfrak{p})$**, where $\mu(\mathfrak{p})$ is the minimal number of generators — and this inequality is exactly [[Thm - Krull's Height Theorem (Principal Ideal Theorem)|Krull's height theorem]]. It is strict for the prime $\mathfrak{p} = (X^2 - YZ,\, Y^2 - XZ,\, Z^2 - XY)$ defining the twisted cubic in $k[X,Y,Z]$, which has height $2$ (the twisted cubic is a curve in $3$-space, codimension $2$) yet cannot be generated by fewer than $3$ elements. Reading height off the number of generators overcounts.

**Is NOT an instance — a Noetherian ring of infinite dimension.** Noetherianity bounds the height of each individual prime ($\operatorname{ht}\mathfrak{p} < \infty$ for all $\mathfrak{p}$, by Krull's height theorem) but does *not* bound the dimension: Nagata's example (see [[Ex - A Noetherian ring of infinite dimension]]) is a Noetherian ring with primes of arbitrarily large height, so $\dim R = \infty$. This shows $\dim R = \sup_{\mathfrak{p}} \operatorname{ht}\mathfrak{p}$ can be infinite even when every term in the supremum is finite.

**Calibration check.** Verify that $\dim k = 0$ by listing the primes of a field. Verify $\operatorname{ht}(X_1,\dots,X_i) = i$ in $k[X_1,\dots,X_n]$ by exhibiting a chain below it and (granting the polynomial-ring theorem) that none is longer. Confirm the length convention by checking that the one-prime chain $\{\mathfrak{p}\}$ has length $0$, so $\operatorname{ht}\mathfrak{p} = 0$ exactly when $\mathfrak{p}$ is a minimal prime. Finally, confirm $\operatorname{ht}\mathfrak{p} = \dim R_{\mathfrak{p}}$ by recalling that the primes of $R_{\mathfrak{p}}$ are exactly the primes of $R$ contained in $\mathfrak{p}$.

---

# Unlocked by This

> [!tip] Dimension of an affine variety *(from Algebraic Geometry)*
> For an affine variety $X = V(I) \subseteq \mathbb{A}^n_k$ over an algebraically closed field, with coordinate ring $A = k[X_1,\dots,X_n]/I(X)$, the **dimension of $X$** is *defined* to be $\dim A$, the Krull dimension of its coordinate ring. This is the algebraic definition that recovers the intuitive one: $\dim$ point $= 0$, $\dim$ curve $= 1$, $\dim$ surface $= 2$, $\dim \mathbb{A}^n = n$. A chain of primes in $A$ is a tower of irreducible subvarieties, so $\dim X$ is the length of the longest tower of irreducible closed subsets of $X$ — the **combinatorial dimension** of $X$ as a topological space with the Zariski topology. The local ring $A_{\mathfrak{p}}$ at a point has dimension equal to the dimension of the component through that point.

> [!tip] Codimension and the theory of divisors *(from Algebraic Geometry)*
> The **height** of a prime is the **codimension** of the corresponding subvariety: $\operatorname{ht}\mathfrak{p} = \operatorname{codim}(V(\mathfrak{p}), \operatorname{Spec} A)$. Height-one primes are the **prime divisors**, the codimension-one irreducible subvarieties, and the free abelian group they generate is the group of **Weil divisors** — the foundation of intersection theory and of the theory of line bundles. That a single nonzero non-unit cuts out exactly codimension one is **Krull's principal ideal theorem**, which is why a hypersurface in $\mathbb{A}^n$ has dimension exactly $n-1$.

> [!tip] The dimension of a scheme and catenary rings *(from Algebraic Geometry)*
> For a general **scheme**, dimension is defined locally as the Krull dimension of the local rings of the structure sheaf, glued. The identity $\operatorname{ht}\mathfrak{p} + \dim A/\mathfrak{p} = \dim A$ (valid for finitely generated domains over a field, see [[Ex - Height plus dimension of the quotient equals dimension]]) is the **catenary** property — that all maximal chains between two primes have the same length — which underlies the well-definedness of codimension and the dimension formula for fibres of morphisms.
