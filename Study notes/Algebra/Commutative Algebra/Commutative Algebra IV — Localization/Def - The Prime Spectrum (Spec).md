---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Ring"
  - "Def - Ideal"
  - "Def - Prime and Maximal Ideal"
  - "Def - Radical of an Ideal and the Nilradical"
  - "Def - Multiplicative Set and Localization"
  - "Def - Extension and Contraction of Ideals"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Write $\operatorname{Spec} R$ for the set of all [[Def - Prime and Maximal Ideal|prime ideals]] of $R$ and $\operatorname{mSpec} R$ (or $\operatorname{mspec} R$) for the set of maximal ideals. Points of $\operatorname{Spec} R$ are denoted $\mathfrak{p}, \mathfrak{q}$ (lower-case fraktur, to remind you that a point *is* a prime ideal). For an [[Def - Ideal|ideal]] $I \trianglelefteq R$ we write $V(I) = \{\mathfrak{p} \in \operatorname{Spec} R : I \subseteq \mathfrak{p}\}$ for its **vanishing set**, and for $f \in R$ we write $D(f) = \{\mathfrak{p} : f \notin \mathfrak{p}\} = \operatorname{Spec} R \setminus V((f))$ for the corresponding **basic open set**. The **value** of $r \in R$ at the point $\mathfrak{p}$ is its image $r(\mathfrak{p}) := r \bmod \mathfrak{p}$ in the [[Def - Local Ring and Residue Field|residue field]] $\kappa(\mathfrak{p}) = \operatorname{Frac}(R/\mathfrak{p})$; "$r$ vanishes at $\mathfrak{p}$" means $r \in \mathfrak{p}$. The closure of a subset $T \subseteq \operatorname{Spec} R$ is written $\overline{T}$. The full registry is on [[Commutative Algebra IV — Localization]].

This is a compound page: it defines four interlocking notions — the **set** $\operatorname{Spec} R$, the **Zariski topology** via its closed sets $V(I)$, **closed points** (maximal ideals), and **generic points** (non-maximal primes and their closures) — because the topology is what turns the bare set of primes into the geometric object that localization manipulates, and none of the pieces is usable alone.

---

# Axiom Motivation

Here is the move that founds modern algebraic geometry: **take a ring and decide to regard it as a ring of functions on a space — then reconstruct the space from the ring.** The space you get is $\operatorname{Spec} R$, the set of prime ideals, and the whole task of this definition is to explain why *primes* are the right points and why the *Zariski topology* is the right notion of nearness. Everything is reverse-engineered from one demand: an element $r \in R$ should behave like a function, so it must have a *value* at each point, and two points should be "close" when no function separates them cleanly.

**Why points should be prime ideals, not just maximal ones.** Suppose $r \in R$ is to be a function on a space $X$. A function has a value at each point $x$, and the natural value of $r$ at $x$ is "$r$ reduced modulo the data of the point". If a point is a maximal ideal $\mathfrak{m}$, then $R/\mathfrak{m}$ is a field and $r \bmod \mathfrak{m}$ is an honest element of that field — this is the classical picture, where points of $k^n$ are the maximal ideals $(X_1 - a_1, \dots, X_n - a_n)$ of $k[X_1,\dots,X_n]$ and the value of a polynomial is its value at $a$. So *maximal ideals are certainly points*. The decisive enlargement is to allow *all* prime ideals as points. The reason is that you want the construction to be **functorial**: a ring map $\varphi : A \to B$ should induce a map of spaces $\operatorname{Spec} B \to \operatorname{Spec} A$, and the only ideal-theoretic operation that always produces a point from a point is [[Def - Extension and Contraction of Ideals|contraction]] $\mathfrak{q} \mapsto \varphi^{-1}(\mathfrak{q})$ — which *preserves primes but not maximality*. Maximal ideals are not preserved by contraction (the contraction of a maximal ideal can be non-maximal), so a space made only of maximal ideals would have no functorial map between its instances. Primes are the smallest enlargement that fixes this: $\operatorname{Spec}$ becomes a functor exactly when you admit every prime. The price is that non-maximal primes are *not* ordinary points — they are **generic points**, "fat points" that spread over a whole subvariety, and learning to read them is most of the conceptual content.

**Why the closed sets are the vanishing sets $V(I)$.** A function should vanish somewhere, and the locus where it vanishes should be closed — that is the one non-negotiable demand on a topology of functions. The value of $r$ at $\mathfrak{p}$ lives in $R/\mathfrak{p}$, and "$r$ vanishes at $\mathfrak{p}$" means exactly $r \in \mathfrak{p}$. So the zero set of $r$ is $\{\mathfrak{p} : r \in \mathfrak{p}\} = V((r))$, and the zero set of a *collection* of functions, i.e. an ideal $I$, is $V(I) = \{\mathfrak{p} : I \subseteq \mathfrak{p}\}$. **Declaring these to be the closed sets is forced** once you accept that simultaneous vanishing loci should be closed. One then checks the axioms of a topology, and they hold for clean algebraic reasons: $V(I) \cup V(J) = V(IJ) = V(I \cap J)$ because a prime contains a product of ideals iff it contains one of them; $\bigcap_\alpha V(I_\alpha) = V(\sum_\alpha I_\alpha)$ because containing every $I_\alpha$ is the same as containing their sum; and $V((0)) = \operatorname{Spec} R$, $V((1)) = \varnothing$. So the Zariski topology is not an arbitrary choice — it is the unique topology whose closed sets are the vanishing loci of functions, and the topology axioms are theorems about primes.

**Why this topology is strange, and why the strangeness is correct.** The Zariski topology is almost never Hausdorff, and that offends intuition trained on metric spaces. But the failure is meaningful. In $\operatorname{Spec}\mathbb{Z}$, the closed points are the maximal ideals $(p)$, but there is one extra point, the generic point $(0)$, whose closure is *all* of $\operatorname{Spec}\mathbb{Z}$ — it is "everywhere at once". Two closed points cannot be separated by disjoint opens because every nonempty open set is enormous (it omits only finitely many primes). The topology is *coarse* on purpose: it records exactly the information a polynomial can see, no more. A function cannot tell two points apart unless it vanishes at one and not the other, and over an infinite field polynomials are so rigid that they cannot isolate single points with small neighbourhoods. The right reaction is not to fix the topology but to *add structure*: the bare topological space $\operatorname{Spec} R$ is upgraded to a **scheme** by remembering, at each open set $D(f)$, the ring of functions $R_f$ that live there — and that ring-of-functions data is exactly what localization computes.

**Why closed points are maximal and generic points are non-maximal primes.** The closure of a single point $\{\mathfrak{p}\}$ is the smallest closed set containing it, which is $V(\mathfrak{p}) = \{\mathfrak{q} : \mathfrak{p} \subseteq \mathfrak{q}\}$. So $\overline{\{\mathfrak{p}\}} = \{\mathfrak{p}\}$ — the point is **closed** — exactly when no prime strictly contains $\mathfrak{p}$, i.e. exactly when $\mathfrak{p}$ is **maximal**. A non-maximal prime $\mathfrak{p}$ is *not* closed: its closure $V(\mathfrak{p})$ is a whole irreducible subset, the subvariety it "is generic in". This is the precise sense in which $\mathfrak{p}$ is a generic point of $V(\mathfrak{p})$: it lies in every nonempty open subset of $V(\mathfrak{p})$, so it sees the *generic* behaviour of that subvariety. The inclusion order on primes becomes the *specialization* order on points: $\mathfrak{p} \subseteq \mathfrak{q}$ means $\mathfrak{q} \in \overline{\{\mathfrak{p}\}}$, read "$\mathfrak{q}$ is a specialization of $\mathfrak{p}$", or "$\mathfrak{p}$ degenerates to $\mathfrak{q}$".

---

# The Definition

Let $R$ be a commutative ring.

## The prime spectrum as a set

The **prime spectrum** of $R$ is the set
$$\operatorname{Spec} R := \{\mathfrak{p} \trianglelefteq R : \mathfrak{p} \text{ is a prime ideal}\}.$$
By convention $\operatorname{Spec} R = \varnothing$ if and only if $R = 0$ (a nonzero ring has a maximal ideal, hence a prime). The subset of maximal ideals is $\operatorname{mSpec} R$.

## The Zariski topology

For an ideal $I \trianglelefteq R$ define its **vanishing set**
$$V(I) := \{\mathfrak{p} \in \operatorname{Spec} R : I \subseteq \mathfrak{p}\}.$$
The collection $\{V(I) : I \trianglelefteq R\}$ is the family of **closed sets** of a topology on $\operatorname{Spec} R$, the **Zariski topology**. It satisfies
$$V((0)) = \operatorname{Spec} R, \quad V((1)) = \varnothing, \quad V(I) \cup V(J) = V(I \cap J) = V(IJ), \quad \bigcap_{\alpha} V(I_\alpha) = V\!\Big(\textstyle\sum_\alpha I_\alpha\Big).$$
Moreover $V(I) = V(\sqrt{I})$, so closed sets only depend on the [[Def - Radical of an Ideal and the Nilradical|radical]] of $I$, and $V(I) \subseteq V(J) \iff \sqrt{J} \subseteq \sqrt{I}$.

## Basic open sets

For $f \in R$, the **basic (or distinguished) open set** is
$$D(f) := \operatorname{Spec} R \setminus V((f)) = \{\mathfrak{p} : f \notin \mathfrak{p}\}.$$
The sets $\{D(f) : f \in R\}$ form a **basis** for the Zariski topology: every open set is a union of basic opens, $D(f) \cap D(g) = D(fg)$, $D(f) = \varnothing \iff f$ is [[Def - Radical of an Ideal and the Nilradical|nilpotent]], and $D(f) = \operatorname{Spec} R \iff f$ is a unit.

## Closed points and generic points

For $\mathfrak{p} \in \operatorname{Spec} R$, the closure of the singleton is
$$\overline{\{\mathfrak{p}\}} = V(\mathfrak{p}) = \{\mathfrak{q} \in \operatorname{Spec} R : \mathfrak{p} \subseteq \mathfrak{q}\}.$$
Hence $\mathfrak{p}$ is a **closed point** $\iff \overline{\{\mathfrak{p}\}} = \{\mathfrak{p}\} \iff \mathfrak{p}$ is **maximal**. A non-maximal prime $\mathfrak{p}$ is a **generic point**: its closure $V(\mathfrak{p})$ is the irreducible closed subset of which $\mathfrak{p}$ is the unique generic point. A closed set $Z$ is **irreducible** (not a union of two proper closed subsets) if and only if $Z = V(\mathfrak{p})$ for a unique prime $\mathfrak{p}$, the generic point of $Z$.

## Functions and values

Each $r \in R$ is regarded as a "function" on $\operatorname{Spec} R$ whose value at $\mathfrak{p}$ is $r(\mathfrak{p}) := (r \bmod \mathfrak{p}) \in \kappa(\mathfrak{p})$, where $\kappa(\mathfrak{p}) = \operatorname{Frac}(R/\mathfrak{p})$. Then $r$ vanishes at $\mathfrak{p} \iff r \in \mathfrak{p}$, the zero set of $r$ is $V((r))$, and a function vanishing at every point is exactly a [[Def - Radical of an Ideal and the Nilradical|nilpotent]] (it lies in $\bigcap_{\mathfrak{p}} \mathfrak{p} = \operatorname{nil} R$).

---

# Categorical / Structural Definition

$\operatorname{Spec}$ is a **contravariant functor** $\operatorname{Spec} : \mathbf{CRing}^{\mathrm{op}} \to \mathbf{Top}$. A ring homomorphism $\varphi : A \to B$ induces a continuous map
$$\operatorname{Spec}(\varphi) : \operatorname{Spec} B \to \operatorname{Spec} A, \qquad \mathfrak{q} \mapsto \varphi^{-1}(\mathfrak{q}) = \mathfrak{q}^c,$$
which is well defined because [[Def - Extension and Contraction of Ideals|contraction preserves primes]], and continuous because $\operatorname{Spec}(\varphi)^{-1}(V(I)) = V(I^e)$. The arrows reverse: a ring map $A \to B$ becomes a space map $\operatorname{Spec} B \to \operatorname{Spec} A$, just as a function $f : X \to Y$ pulls back functions on $Y$ to functions on $X$. Two structural features make this the foundation of scheme theory. First, the basic opens are themselves spectra: $D(f) \cong \operatorname{Spec}(R_f)$ as topological spaces, via the [[Thm - Prime Ideals of a Localization|prime-correspondence theorem]] applied to $S = \{f^n\}$ — so *localization at $f$ is restriction to the open set $D(f)$*. Second, attaching to each $D(f)$ the ring $R_f$, compatibly under inclusions $D(fg) \subseteq D(f)$ (which give restriction maps $R_f \to R_{fg}$), produces a **sheaf of rings** $\mathcal{O}_{\operatorname{Spec} R}$, the **structure sheaf**, and the pair $(\operatorname{Spec} R, \mathcal{O}_{\operatorname{Spec} R})$ is an **affine scheme**. A general scheme is glued from affine ones, exactly as a manifold is glued from charts.

---

# Relate to Other Fields / Compression

The cleanest compression: **$\operatorname{Spec} R$ is the space whose points are the prime ideals of $R$, topologised so that the closed sets are precisely the simultaneous zero loci of elements of $R$ — and under this topology a ring becomes the functions on its own spectrum.** The Zariski topology is the coarsest topology making every $r \in R$ "continuous with closed zero set".

**True name:** the true name of $\operatorname{Spec} R$ is "**the universal space on which $R$ is the ring of functions**". The classical zero-set picture (points of $k^n$, polynomials as functions) is the special case $R = k[X_1,\dots,X_n]$ with $k$ algebraically closed, where $\operatorname{mSpec} R = k^n$ by the Nullstellensatz; the generic points and the nilpotents are what $\operatorname{Spec}$ adds to make the picture functorial and to track infinitesimal/multiplicity information.

This is the algebraic mirror of the **Gelfand duality** of analysis, where a compact Hausdorff space $X$ is reconstructed from the commutative $C^*$-algebra $C(X)$ of continuous functions, the points of $X$ being the maximal ideals. $\operatorname{Spec}$ does the same for arbitrary commutative rings, with two differences forced by the algebra: primes (not just maximals) are admitted to gain functoriality, and the topology is Zariski (not the metric topology) because polynomials are far more rigid than continuous functions. The specialization order $\mathfrak{p} \subseteq \mathfrak{q}$ has no analogue in the Hausdorff world — it appears precisely because the Zariski topology is non-Hausdorff, and it encodes the **dimension theory** developed in [[Commutative Algebra XII — Dimension Theory]] (chains of primes $=$ chains of irreducible closed subsets $=$ Krull dimension).

---

# Examples / Corollaries

**Is an instance — $\operatorname{Spec}\mathbb{Z}$, the arithmetic line.** The primes of $\mathbb{Z}$ are $(0)$ and $(p)$ for each prime number $p$. So $\operatorname{Spec}\mathbb{Z} = \{(0)\} \cup \{(p) : p \text{ prime}\}$. The closed points are the $(p)$ (maximal); $(0)$ is the unique generic point, with $\overline{\{(0)\}} = V((0)) = \operatorname{Spec}\mathbb{Z}$. The basic open $D(n)$ omits exactly the finitely many primes dividing $n$. The value of $m \in \mathbb{Z}$ at $(p)$ is $m \bmod p \in \mathbb{F}_p = \kappa((p))$, and its value at the generic point $(0)$ is $m \in \mathbb{Q} = \kappa((0))$.

**Is an instance — $\operatorname{Spec} k[X]$ for $k$ algebraically closed, the affine line $\mathbb{A}^1$.** The primes are $(0)$ and $(X - a)$ for $a \in k$. The closed points $(X-a)$ are the points $a \in k$ of the line; $(0)$ is the generic point whose closure is the whole line. A polynomial $f$ "vanishes at $a$" iff $f \in (X-a)$ iff $f(a) = 0$ — the value-at-a-point picture is literal.

**Is an instance — irreducibility detects primality.** A closed set $V(I)$ is irreducible iff $\sqrt{I}$ is prime. For $R = k[X,Y]$, $V((XY))$ is the union of the two coordinate axes $V((X)) \cup V((Y))$ — reducible — corresponding to $(XY)$ not being prime; whereas $V((Y - X^2))$ (a parabola) is irreducible because $(Y - X^2)$ is prime ($k[X,Y]/(Y-X^2) \cong k[X]$ is a domain).

**Is NOT an instance — the Zariski topology is not Hausdorff (and not $T_1$).** In $\operatorname{Spec}\mathbb{Z}$ the point $(0)$ cannot be separated from any $(p)$: every nonempty open set contains $(0)$ (it omits only closed points $(p)$). So $\{(0)\}$ is *not* closed, $\operatorname{Spec}\mathbb{Z}$ is not $T_1$, and certainly not Hausdorff. This is not a defect — it is the generic point doing its job. Contrast with a metric space, where every singleton is closed.

**Is NOT an instance — the empty spectrum.** $\operatorname{Spec} R = \varnothing$ iff $R = 0$, since every nonzero ring has a maximal ideal. So "$\operatorname{Spec} R$ has a point" is a faithful test for $R \neq 0$ — this is the engine behind detecting nilpotence via $R_f = 0 \iff D(f) = \varnothing \iff f$ nilpotent.

**Calibration check.** Verify the topology axiom $V(I) \cup V(J) = V(IJ)$ directly from the definition of a prime ideal (a prime contains $IJ$ iff it contains $I$ or $J$). Confirm $\overline{\{\mathfrak{p}\}} = V(\mathfrak{p})$ and deduce "closed point $\iff$ maximal ideal". Finally, list $\operatorname{Spec}\mathbb{Z}$, identify its one generic point, and check that the value of $6$ at $(2)$, $(3)$, $(5)$, $(0)$ is $0, 0, 1, 6$ respectively in the corresponding residue fields.

---

# Unlocked by This

> [!tip] Affine schemes and the structure sheaf *(from Algebraic Geometry)*
> The space $\operatorname{Spec} R$ is only the *underlying set with topology* of the real object: an **affine scheme** is $\operatorname{Spec} R$ together with its structure sheaf $\mathcal{O}_{\operatorname{Spec} R}$, the sheaf of rings whose sections over $D(f)$ are the localization $R_f$. Every basic open $D(f)$ is itself the affine scheme $\operatorname{Spec}(R_f)$ (by the [[Thm - Prime Ideals of a Localization|prime-correspondence theorem]]), so the local model is uniform, and a general scheme is obtained by gluing affine schemes along open subschemes — the algebraic analogue of building a manifold from coordinate charts. This is why $\operatorname{Spec}$ is *the* object of the subject: it converts all of commutative algebra into geometry, and localization into the operation of passing to an open set or a point.

> [!tip] Dimension as the length of a chain of points *(from Algebraic Geometry / Dimension Theory)*
> Because the specialization order on $\operatorname{Spec} R$ is the inclusion order on primes, a chain of irreducible closed subsets $Z_0 \subsetneq Z_1 \subsetneq \dots \subsetneq Z_n$ is the same as a chain of primes $\mathfrak{p}_0 \supsetneq \mathfrak{p}_1 \supsetneq \dots \supsetneq \mathfrak{p}_n$, and the supremum of such $n$ is the **Krull dimension**. The topology of $\operatorname{Spec}$ thereby carries the entire dimension theory of [[Commutative Algebra XII — Dimension Theory]]: a curve is one-dimensional because its generic point specializes to closed points in chains of length one, a surface in chains of length two, and so on.

> [!tip] Nilpotents and non-reduced schemes *(from Algebraic Geometry)*
> A nilpotent element vanishes at every point of $\operatorname{Spec} R$ yet may be nonzero, so the bare topological space cannot see it — but the structure sheaf can. This is the algebraic origin of **non-reduced schemes** and **infinitesimal/multiplicity data**: $\operatorname{Spec} k[\varepsilon]/(\varepsilon^2)$ is a single point with a "tangent vector's worth" of extra functions, the **dual number** scheme that defines tangent spaces. Reducedness — no nonzero nilpotents — is exactly the condition that functions are determined by their values, and it is a [[Def - Local Property (Localizable and Local-to-Global)|local property]].
