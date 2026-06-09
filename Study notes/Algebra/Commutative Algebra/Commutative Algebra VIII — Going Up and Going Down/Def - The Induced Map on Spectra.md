---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - The Prime Spectrum (Spec)"
  - "Def - Prime and Maximal Ideal"
  - "Def - Extension and Contraction of Ideals"
  - "Def - Local Ring and Residue Field"
  - "Def - Ring Homomorphism"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. For a ring homomorphism $f : A \to B$ we write $f^* : \operatorname{Spec} B \to \operatorname{Spec} A$ for the induced map, $\mathfrak{q} \mapsto f^{-1}(\mathfrak{q})$; when $f$ is an inclusion $A \subseteq B$ this is the contraction $\mathfrak{q} \mapsto \mathfrak{q} \cap A$, also written $\iota^*$. We write [[Def - The Prime Spectrum (Spec)|$\operatorname{Spec} R$]] for the set of prime ideals of $R$ with the Zariski topology, $\operatorname{mSpec} R$ for the maximal ideals, $V(I) = \{\mathfrak{p} : I \subseteq \mathfrak{p}\}$ for the closed set of an ideal $I$, and $\kappa(\mathfrak{p}) = A_{\mathfrak{p}}/\mathfrak{p}A_{\mathfrak{p}} = \operatorname{Frac}(A/\mathfrak{p})$ for the [[Def - Local Ring and Residue Field|residue field]] of $A$ at $\mathfrak{p}$. The **fibre** of $f^*$ over $\mathfrak{p}$ is $(f^*)^{-1}(\mathfrak{p}) = \{\mathfrak{q} \in \operatorname{Spec} B : f^{-1}(\mathfrak{q}) = \mathfrak{p}\}$. The full registry is on [[Commutative Algebra VIII — Going Up and Going Down]].

This is a compound page: it defines two interlocking notions — the **induced map $f^*$ on spectra** (the contraction map, with its continuity and functoriality) and the **fibre of $f^*$ over a prime** (together with its identification as the spectrum of the fibre ring) — because the fibre is the object the entire going-up/going-down chapter studies, and it cannot be analysed without first pinning down the map whose fibre it is.

---

# Axiom Motivation

The motivation here is not "why these axioms" but "why this is the *right* map", because there is a genuine choice to be made and the standard choice is, at first glance, backwards. A ring homomorphism $f : A \to B$ goes from $A$ to $B$. One naively expects an induced map of associated spaces going the *same* way, $\operatorname{Spec} A \to \operatorname{Spec} B$. Instead the induced map goes the *opposite* way, $\operatorname{Spec} B \to \operatorname{Spec} A$. Understanding why is understanding the whole functor.

**Why the map reverses direction.** Think of $A$ as functions on a space $X = \operatorname{Spec} A$ and $B$ as functions on $Y = \operatorname{Spec} B$. A ring map $f : A \to B$ is "pull back functions from $X$ to $Y$" — it takes a function on $X$ and produces a function on $Y$. But pulling back functions is what a map of spaces $Y \to X$ does (you pull a function on the target back along the map to get a function on the source). So a map of *function rings* $A \to B$ is the algebra of a map of *spaces* $Y \to X$, in the reverse direction. This is the same contravariance you have seen for the pullback of differential forms, of continuous functions, of sections of bundles: functions pull back, so the map on functions points oppositely to the map on spaces. The points of $\operatorname{Spec}$ are primes, so we need to say how $f$ moves primes, and it must move them from $B$ to $A$.

**Why contraction, and why it is forced.** A point of $X = \operatorname{Spec} A$ is a prime $\mathfrak{p}$, and the "value of a function $a \in A$ at $\mathfrak{p}$" is its image $\bar a$ in the residue field $\kappa(\mathfrak{p})$. Given a point $\mathfrak{q}$ of $Y$, where should it go in $X$? Its image should be the point of $X$ "underneath" it. The only natural prime of $A$ attached to $\mathfrak{q}$ is the contraction $f^{-1}(\mathfrak{q})$, and three checks confirm it is forced. First, $f^{-1}(\mathfrak{q})$ *is* a prime ideal: if $ab \in f^{-1}(\mathfrak{q})$ then $f(a)f(b) = f(ab) \in \mathfrak{q}$, so $f(a) \in \mathfrak{q}$ or $f(b) \in \mathfrak{q}$ (as $\mathfrak{q}$ is prime), i.e. $a \in f^{-1}(\mathfrak{q})$ or $b \in f^{-1}(\mathfrak{q})$; and $1 \notin f^{-1}(\mathfrak{q})$ since $f(1) = 1 \notin \mathfrak{q}$. So contraction lands in $\operatorname{Spec} A$, which extension does *not*: the image $f(\mathfrak{p})$ or the extended ideal $f(\mathfrak{p})B$ of a prime need not be prime (think of $\mathbb{Z} \to \mathbb{Z}$, $\mathfrak{p} = (0)$, and a non-injective $f$, or simply that $f(\mathfrak{p})$ need not even be an ideal). Contraction is the only one of the two operations that always produces a prime, so it is the only candidate for a map *to* $\operatorname{Spec} A$. Second, contraction is *functorial*: $(g \circ f)^* = f^* \circ g^*$ and $\operatorname{id}^* = \operatorname{id}$, exactly the bookkeeping a map of spaces must satisfy. Third, contraction is *continuous* for the Zariski topology, as the next paragraph records — so $f^*$ is a genuine map of topological spaces, not just of sets.

**Why the fibre is the object of interest, and why it is itself a spectrum.** The chapter ahead is entirely about the *fibres* of $f^*$ — for each point $\mathfrak{p}$ of the base, the set of points $\mathfrak{q}$ of $\operatorname{Spec} B$ lying over it. A bare set of primes is hard to reason about; the decisive structural fact is that this set is *itself the spectrum of a ring*. Concretely, the primes of $B$ lying over $\mathfrak{p}$ are in natural bijection with the primes of the **fibre ring** $B \otimes_A \kappa(\mathfrak{p})$, equivalently $(B/\mathfrak{p}B)_{\mathfrak{p}}$ — the ring obtained by killing $\mathfrak{p}$ and inverting everything outside it, i.e. base-changing $B$ to the residue field at the point. The reason to insist on this: it converts every geometric question about a fibre (is it empty? finite? zero-dimensional?) into an algebraic question about a single ring over a field (is it non-zero? finite-dimensional? Artinian?). The definition would be *usable* without the fibre ring, but it would not be *powerful*; the going-up/going-down theorems are, almost without exception, statements about this fibre ring in disguise.

**Why continuity, and the formula that delivers it.** For $f^*$ to be a map of *spaces* and not merely of sets, it must be continuous. The clean way to see this is to compute the preimage of a basic closed set. For an ideal $I \trianglelefteq A$, the closed set $V(I) \subseteq \operatorname{Spec} A$ pulls back to $(f^*)^{-1}(V(I)) = \{\mathfrak{q} : f^{-1}(\mathfrak{q}) \supseteq I\} = \{\mathfrak{q} : \mathfrak{q} \supseteq f(I)\} = V(f(I)B)$, again a closed set. So $f^*$ pulls closed sets back to closed sets — it is continuous. This formula is also the workhorse for the geometric statements later: "going up $\iff$ $f^*$ closed" is a statement about images of closed sets, and it is read off the interplay of $V$, contraction, and extension.

---

# The Definition

Let $f : A \to B$ be a homomorphism of commutative rings.

## The induced map on spectra

The **induced map** (or **contraction map**) is
$$f^* : \operatorname{Spec} B \longrightarrow \operatorname{Spec} A, \qquad f^*(\mathfrak{q}) = f^{-1}(\mathfrak{q}) = \{a \in A : f(a) \in \mathfrak{q}\}.$$
For each $\mathfrak{q} \in \operatorname{Spec} B$ the set $f^{-1}(\mathfrak{q})$ is a prime ideal of $A$, so $f^*$ is well-defined. It is **functorial**: $(g \circ f)^* = f^* \circ g^*$ and $(\operatorname{id}_A)^* = \operatorname{id}_{\operatorname{Spec} A}$. It is **continuous** for the Zariski topology, with
$$(f^*)^{-1}\big(V(I)\big) = V\big(f(I)B\big) \qquad \text{for every ideal } I \trianglelefteq A.$$
When $f$ is an inclusion $\iota : A \hookrightarrow B$, this is $\iota^*(\mathfrak{q}) = \mathfrak{q} \cap A$, contraction of ideals along the inclusion.

## The fibre over a prime

For $\mathfrak{p} \in \operatorname{Spec} A$, the **fibre** of $f^*$ over $\mathfrak{p}$ is
$$(f^*)^{-1}(\mathfrak{p}) = \{\mathfrak{q} \in \operatorname{Spec} B : f^{-1}(\mathfrak{q}) = \mathfrak{p}\}.$$
With $S = f(A \setminus \mathfrak{p})$ and the **fibre ring** $B_{\mathfrak{p}} := S^{-1}B$ in the inclusion case (more generally $B \otimes_A \kappa(\mathfrak{p}) \cong (B/\mathfrak{p}B)_{\mathfrak{p}}$), there is a canonical bijection
$$(f^*)^{-1}(\mathfrak{p}) \;\longleftrightarrow\; \operatorname{Spec}\big(B \otimes_A \kappa(\mathfrak{p})\big),$$
identifying the fibre with the prime spectrum of the fibre ring — an algebra over the field $\kappa(\mathfrak{p})$. For an integral extension this restricts to $(\iota^*)^{-1}(\mathfrak{p}) \leftrightarrow \operatorname{mSpec} B_{\mathfrak{p}}$.

---

# Categorical / Structural Definition

The assignment $R \mapsto \operatorname{Spec} R$, $f \mapsto f^*$ is a **contravariant functor** from the category of commutative rings to the category of topological spaces: it reverses the direction of arrows and respects composition, $(g \circ f)^* = f^* \circ g^*$. (Upgraded to ringed spaces by equipping $\operatorname{Spec} R$ with its structure sheaf, it becomes a *fully faithful* contravariant functor onto **affine schemes** — the foundational equivalence "commutative rings $=$ affine schemes, arrows reversed".) The fibre of $f^*$ over $\mathfrak{p}$ has a clean categorical description as a **base change**: it is $\operatorname{Spec}$ of the pushout-along-$f$ of the residue field, $B \otimes_A \kappa(\mathfrak{p})$, which is the fibre product $\operatorname{Spec} B \times_{\operatorname{Spec} A} \operatorname{Spec}\kappa(\mathfrak{p})$ in the category of schemes. This is why "the fibre is a spectrum": fibres of maps of affine schemes are computed by tensoring, and tensoring rings is the coproduct in commutative rings, dual to the fibre product of spaces.

---

# Relate to Other Fields / Compression

The cleanest compression: **$f^*$ is "pullback of functions", and the fibre is "restrict to the point and base-change".** A ring map is the algebra of pulling functions back along a map of spaces, which is why $\operatorname{Spec}$ is contravariant; the fibre over a point is what you get by tensoring with the residue field at that point, i.e. by literally restricting attention to that point and asking what the source looks like above it.

**True name:** the true name of the fibre over $\mathfrak{p}$ is *not* "the set of primes contracting to $\mathfrak{p}$" but "**the spectrum of the fibre ring $B \otimes_A \kappa(\mathfrak{p})$**". This is the form you use in every proof: lying over is "the fibre ring is non-zero", incomparability is "the fibre ring is zero-dimensional", finiteness of the fibre is "the fibre ring is finite-dimensional over $\kappa(\mathfrak{p})$".

The construction is the algebraic mirror of the **pullback of a continuous map** in topology: given $\phi : Y \to X$ continuous and a function $a : X \to \mathbb{R}$, the pullback $a \circ \phi : Y \to \mathbb{R}$ is a function on $Y$; the assignment $a \mapsto a \circ \phi$ is a ring map $C(X) \to C(Y)$ pointing oppositely to $\phi$. Reading this backwards, every ring map $A \to B$ *is* such a pullback for a unique map of spectra $\operatorname{Spec} B \to \operatorname{Spec} A$ — and that map is $f^*$. The fibre $(f^*)^{-1}(\mathfrak{p})$ corresponds to $\phi^{-1}(\text{point})$, the preimage of a point.

---

# Examples / Corollaries

**Is an instance — the inclusion $\mathbb{Z} \subseteq \mathbb{Z}[i]$.** Here $\iota^* : \operatorname{Spec}\mathbb{Z}[i] \to \operatorname{Spec}\mathbb{Z}$ sends a Gaussian prime $\mathfrak{q}$ to $\mathfrak{q} \cap \mathbb{Z}$. The fibre over $(p)$ has fibre ring $\mathbb{Z}[i] \otimes_{\mathbb{Z}} \mathbb{F}_p = \mathbb{Z}[i]/p\mathbb{Z}[i] \cong \mathbb{F}_p[X]/(X^2+1)$, whose primes are read off the factorisation of $X^2+1$ over $\mathbb{F}_p$ — one prime when $X^2+1$ is irreducible ($p \equiv 3 \bmod 4$), two when it splits ($p \equiv 1 \bmod 4$), one (with multiplicity) when it has a repeated root ($p = 2$). See [[Ex - Primes of Z[i] over a rational prime]].

**Is an instance — the quotient map $\pi : A \to A/I$.** The induced $\pi^* : \operatorname{Spec}(A/I) \to \operatorname{Spec} A$ is a *closed embedding* onto $V(I)$: the primes of $A/I$ correspond exactly to the primes of $A$ containing $I$ ([[Thm - Maximal and Prime Ideals via Quotients|via the quotient]]), and $\pi^*$ is the inclusion of that closed set. Here the fibres are either a single point (over $\mathfrak{p} \supseteq I$) or empty (over $\mathfrak{p} \not\supseteq I$), so quotient maps are the maps with at most one point in each fibre.

**Is an instance — the localization map $A \to S^{-1}A$.** The induced map is an *open* embedding of spectra onto $\{\mathfrak{p} : \mathfrak{p} \cap S = \varnothing\}$ ([[Thm - Prime Ideals of a Localization|prime correspondence for localizations]]); again at most one point sits in each fibre. Localization and quotient are the two ways a ring map can have "trivial" (at most singleton) fibres — they restrict to subsets rather than covering.

**Is NOT an instance of surjectivity — a general $f^*$ need not be onto.** Surjectivity of $f^*$ is exactly [[Def - Lying Over, Going Up, Going Down|lying over]], and it *fails* for general $f$. The localization $\mathbb{Z} \to \mathbb{Q}$ has $\operatorname{Spec}\mathbb{Q} = \{(0)\}$ mapping to $\{(0)\} \subsetneq \operatorname{Spec}\mathbb{Z}$ — every prime $(p)$ is missed. So the *existence* of the map $f^*$ is free, but its good behaviour (onto, closed, finite fibres) is exactly what integrality buys.

**Corollary — closed points need not map to closed points, but for integral maps they do.** A maximal ideal $\mathfrak{q}$ (closed point of $\operatorname{Spec} B$) contracts to a prime $\mathfrak{q} \cap A$ that need not be maximal in general — for the localization $\mathbb{Z} \hookrightarrow \mathbb{Q}$ the unique maximal ideal $(0)$ of $\mathbb{Q}$ contracts to the *non-maximal* prime $(0)$ of $\mathbb{Z}$ — but for an *integral* extension, $\mathfrak{q}$ maximal $\iff \mathfrak{q}\cap A$ maximal ([[Thm - Integral Extensions and Fields (Domain Criterion)|domain criterion]]). So integral maps send closed points to closed points, a defining feature of finite morphisms.

**Calibration check.** Verify that $f^{-1}(\mathfrak{q})$ is prime directly from primeness of $\mathfrak{q}$, and that $(f^*)^{-1}(V(I)) = V(f(I)B)$ by unwinding "$\mathfrak{q} \supseteq f(I)$". Confirm that for $\mathbb{Z} \subseteq \mathbb{Z}[i]$ the fibre over $(5)$ has two points and the fibre over $(7)$ has one, by factoring $X^2+1$ mod $5$ and mod $7$. Finally check that the quotient map $A \to A/I$ has $\pi^*$ injective with image $V(I)$, so its fibres are singletons or empty.

---

# Unlocked by This

> [!tip] The functor of points and affine schemes *(from Algebraic Geometry)*
> The assignment $R \mapsto \operatorname{Spec} R$, $f \mapsto f^*$ is the object half of the contravariant equivalence between commutative rings and **affine schemes**. Equipping $\operatorname{Spec} R$ with the **structure sheaf** $\mathcal{O}_{\operatorname{Spec} R}$ (built from the localizations $R_g$) turns it into a locally ringed space, and the equivalence becomes "a ring is its affine scheme, and ring maps are scheme maps with arrows reversed". The induced map $f^*$ defined here is the underlying continuous map of the corresponding morphism of schemes.

> [!tip] Fibres, base change, and families *(from Algebraic Geometry)*
> The identification "fibre over $\mathfrak{p}$ $=$ $\operatorname{Spec}(B \otimes_A \kappa(\mathfrak{p}))$" is the affine case of computing the fibre of a morphism by **base change** to the residue field. Viewing $\operatorname{Spec} B \to \operatorname{Spec} A$ as a *family* of varieties parametrised by $\operatorname{Spec} A$, the fibre over a point is the member of the family sitting over it. The going-up/going-down theorems are then statements about how the members of an *integral* (finite) family vary — they do not jump in number unboundedly, do not disappear, and (for normal base) do not jump in dimension.
