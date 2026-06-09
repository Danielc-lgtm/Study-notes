---
type: theorem
subject: commutative-algebra
prereqs:
  - "Thm - The Strong Nullstellensatz"
  - "Thm - The Weak Nullstellensatz"
  - "Def - Affine Variety and the Vanishing Set"
  - "Def - The Coordinate Ring and the Ideal of a Set"
  - "Def - Irreducible Algebraic Set"
  - "Def - Prime and Maximal Ideal"
  - "Def - Radical of an Ideal and the Nilradical"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Chapter standing data: a field $k$, an algebraically closed $\Omega \supseteq k$, affine space $\Omega^n$, the operations $V$ ([[Def - Affine Variety and the Vanishing Set]]) and $I$ ([[Def - The Coordinate Ring and the Ideal of a Set]]). We write $\operatorname{Spec}$ / $\operatorname{mSpec}$ for the sets of prime / maximal ideals; $\mathfrak m_x = (T_1 - x_1, \dots, T_n - x_n)$ for the ideal of a point. An ideal is **radical** if $\sqrt{\mathfrak a} = \mathfrak a$. This page is stated for a polynomial ring; it transports verbatim to the [[Def - The Coordinate Ring and the Ideal of a Set|coordinate ring]] $k[X]$ of any affine variety $X$. The full registry is on [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz]].

---

# Statement

> **Theorem (The Nullstellensatz Correspondence).** Let $k$ be a field, $\Omega \supseteq k$ algebraically closed, $n \geq 0$. The maps $X \mapsto I(X)$ and $\mathfrak a \mapsto V(\mathfrak a)$ are mutually inverse, **inclusion-reversing bijections**
> $$\{\, k\text{-algebraic subsets of } \Omega^n \,\} \quad\xleftrightarrow{\ \ V,\ I\ \ }\quad \{\, \text{radical ideals of } k[T_1, \dots, T_n] \,\}.$$
> Under this bijection the structure refines:
>
> 1. **(Varieties $\leftrightarrow$ primes.)** Irreducible algebraic sets correspond to **prime** ideals.
> 2. **(Points $\leftrightarrow$ maximals.)** When $k = \Omega$, single points $\{x\}$ correspond to **maximal** ideals $\mathfrak m_x = (T_1 - x_1, \dots, T_n - x_n)$, and $x \mapsto \mathfrak m_x$ is a bijection $\Omega^n \xrightarrow{\sim} \operatorname{mSpec}$.
> 3. **(Lattice operations.)** $V(\mathfrak a + \mathfrak b) = V(\mathfrak a) \cap V(\mathfrak b)$, $V(\mathfrak a \cap \mathfrak b) = V(\mathfrak a) \cup V(\mathfrak b)$, and dually $I(X \cup Y) = I(X) \cap I(Y)$, $I(X \cap Y) = \sqrt{I(X) + I(Y)}$. The bijection is an **anti-isomorphism of lattices**: union $\leftrightarrow$ intersection, intersection $\leftrightarrow$ sum-then-radical.

This is the **dictionary** of affine algebraic geometry: geometric objects and algebraic objects are the same data, read on two sides of an order-reversing bijection. It is assembled from the strong Nullstellensatz ($I(V(\mathfrak a)) = \sqrt{\mathfrak a}$) and the elementary fact $V(I(X)) = X$ for $X$ algebraic.

---

# Motivation

This is the theorem the whole chapter has been building toward — the precise, complete **algebra–geometry dictionary**. Up to now we had two loosely coupled worlds: shapes cut out by equations (algebraic sets) and ideals of polynomials. The correspondence welds them into one: *every geometric object is an algebraic object and vice versa, with no loss of information, and the translation reverses inclusions.* A bigger variety has a smaller ideal; a chain of subvarieties is a chain of ideals read upside down. Geometry can now be done entirely in commutative algebra, and the abstract ring theory of the previous chapters acquires geometric meaning.

The power of the dictionary is in its *stratification*. The crude bijection is "radical ideals $\leftrightarrow$ algebraic sets". But the radical ideals are themselves layered: the **maximal** ideals sit at the bottom (smallest nonzero), the **prime** ideals form a middle stratum, general radicals are intersections of primes. The correspondence respects every layer: maximal ideals are the *points*, prime ideals are the *irreducible varieties* (the geometric atoms), and a general radical ideal is the *general algebraic set* (a finite union of irreducibles). So the algebraic hierarchy "maximal $\subseteq$ prime $\subseteq$ radical" is the geometric hierarchy "point $\subseteq$ irreducible variety $\subseteq$ algebraic set", read with inclusions reversed. This is the single most important organising picture in the subject: **the prime spectrum of the polynomial ring is affine space, with its irreducible subvarieties as the extra (non-closed) points.**

And the dictionary is *functorial in the lattice operations*. The geometric operations you actually perform — intersect two varieties, take a union, ask whether one is contained in another — all have clean algebraic translations: union becomes intersection of ideals, intersection becomes the radical of the sum, containment of varieties becomes reverse-containment of radicals. This is what makes the dictionary a *working tool* rather than a slogan: you compute with ideals and read off geometry, or compute with geometry and read off ideals, fluidly.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$\Omega$ algebraically closed; objects on either side of the bijection". The recognition is "translate a geometric question to algebra or vice versa".

The first disguised source is **"prove a set-theoretic statement about varieties"** (equality, containment, irreducibility, decomposition). The bridge: apply $I$ to convert to a statement about radical ideals, where ring theory is available. The non-obvious value is that geometric intuition guides, but algebra proves. *Example problem:* [[Ex - The ideal-variety correspondence and unions and intersections|show the union-intersection and intersection-sum-radical identities]] (ES3 Q6).

The second disguised source is **"prove an ideal is radical / prime / maximal"**. The bridge: translate to "its variety is an algebraic set / irreducible / a point", which may be geometrically obvious. The non-obvious payoff is that $\mathfrak a$ is radical iff $\mathfrak a = I(V(\mathfrak a))$ — testable by computing the variety and re-ideal-ising. *Example problem:* [[Ex - Irreducible iff the ideal is prime|irreducible iff the ideal is prime]].

The third disguised source is **"a finitely generated reduced $\Omega$-algebra $A$ is given"**. The bridge: $A = \Omega[T]/\mathfrak a$ with $\mathfrak a$ radical, so $A = \Omega[X]$ for the variety $X = V(\mathfrak a)$; the dictionary recovers $X$ as $\operatorname{mSpec} A$ and its irreducible components as the minimal primes. *Example problem:* identify the points and components of a variety from generators and relations.

**Targets (Output Amplification)**

The conclusion is the inclusion-reversing bijection and its refinements.

Combine with **the descending chain condition / Noetherian property**. Since $k[T_1, \dots, T_n]$ is Noetherian, the lattice of radical ideals has the descending chain condition on the *variety* side (ascending on ideals), so every algebraic set is a *finite* union of irreducible components, dual to "finitely many minimal primes". The further result $E$ is the **decomposition into irreducible components**, the structure theorem for varieties.

Combine with **transcendence degree / Krull dimension**. Chains of irreducible varieties $X_0 \subsetneq X_1 \subsetneq \dots$ correspond to chains of primes $\mathfrak p_0 \supsetneq \mathfrak p_1 \supsetneq \dots$; the longest such chain is the dimension. The further result $E$ is $\dim X = \dim k[X] = \operatorname{trdeg}_k \operatorname{Frac}(k[X])$ — dimension theory, with Noether normalization computing the trdeg.

Combine with **morphisms (regular maps)**. A regular map $\varphi : X \to Y$ corresponds to a $k$-algebra homomorphism $\varphi^* : k[Y] \to k[X]$; the dictionary upgrades from objects to *morphisms*, becoming the anti-equivalence of categories {affine varieties} $\simeq$ {finitely generated reduced $k$-algebras}$^{\mathrm{op}}$. The further result $E$ is the **functor of points** and the foundation of scheme theory.

---

# Why Is It True

The correspondence is **two inversion facts glued together: $V(I(X)) = X$ for $X$ algebraic (elementary), and $I(V(\mathfrak a)) = \sqrt{\mathfrak a}$ (the strong Nullstellensatz).** Restricting to radical ideals makes both into the identity, so $V$ and $I$ are mutually inverse there.

**The bolded one-liner: $I$ and $V$ form a Galois connection; the strong Nullstellensatz computes its closure operators as "take the radical" on the ideal side and "take the Zariski closure" on the geometry side — so the closed objects are exactly the radical ideals and the algebraic sets, and the connection restricts to a bijection between them.**

Unpack. A Galois connection between two posets gives a bijection between its "closed" elements — those fixed by the round-trip closure operators $\mathfrak a \mapsto I(V(\mathfrak a))$ and $X \mapsto V(I(X))$. We must identify the closed elements on each side. On the *geometry* side: $V(I(X))$ is the smallest algebraic set containing $X$ (its Zariski closure), so $X$ is closed iff $X$ is algebraic — and then $V(I(X)) = X$. On the *algebra* side: $I(V(\mathfrak a)) = \sqrt{\mathfrak a}$ by the strong Nullstellensatz, so $\mathfrak a$ is closed iff $\mathfrak a = \sqrt{\mathfrak a}$, i.e. iff $\mathfrak a$ is radical. The Galois connection therefore restricts to a bijection {algebraic sets} $\leftrightarrow$ {radical ideals}, inverse maps $V, I$. *That is the whole theorem* — the strong Nullstellensatz is precisely the computation of the algebra-side closure operator.

The refinements are then read off the algebra of the ideals.
- **Primes $\leftrightarrow$ irreducibles:** $\mathfrak p$ prime $\iff k[T]/\mathfrak p$ a domain $\iff V(\mathfrak p)$ irreducible (a product $fg$ vanishing on $V(\mathfrak p)$ means $V(\mathfrak p)$ is covered by $V(f) \cup V(g)$, and irreducibility forces one to contain it — exactly the prime condition; this is [[Ex - Irreducible iff the ideal is prime|the irreducible-iff-prime exercise]]).
- **Maximals $\leftrightarrow$ points:** maximal ideals are the bottom of the prime order; geometrically the smallest nonempty irreducible sets are single points; over $\Omega$ closed, [[Thm - The Weak Nullstellensatz|the weak Nullstellensatz]] makes these exactly the $\mathfrak m_x$.
- **Lattice anti-isomorphism:** $V$ turns $+$ into $\cap$ and $\cap$ into $\cup$ ([[Def - Affine Variety and the Vanishing Set|formal properties of the vanishing operation]]); dualizing, $I$ turns $\cup$ into $\cap$ and $\cap$ into $\sqrt{(+)}$. The radical on $I(X \cap Y) = \sqrt{I(X) + I(Y)}$ is forced because $I(X) + I(Y)$ need not be radical even when $I(X), I(Y)$ are (e.g. two circles tangent at a point — the sum ideal has a nilpotent recording the tangency).

---

# What Makes This Hard

The correspondence itself is easy once the [[Thm - The Strong Nullstellensatz|strong Nullstellensatz]] is in hand — the difficulty is conceptual, in *internalising* that the algebraic and geometric hierarchies are the same object read upside down, and in *not forgetting the radical*. The single most common error is to write $I(X \cap Y) = I(X) + I(Y)$ without the radical: the sum of two radical ideals need not be radical, and the correct statement $I(X \cap Y) = \sqrt{I(X) + I(Y)}$ requires it (the failure is exactly tangency/non-transverse intersection, where the sum ideal carries a nilpotent). The second subtlety is that *primes correspond to irreducibles* requires the strong Nullstellensatz (to know $I(X)$ is the prime, not just radical), and that the points-as-maximals refinement needs algebraic closure — over $\mathbb{R}$, the maximal ideal $(T^2+1)$ corresponds to the conjugate pair $\{i, -i\}$, not a single point.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Establish the two round-trip identities ($V(I(X)) = X$ for algebraic $X$; $I(V(\mathfrak a)) = \sqrt{\mathfrak a}$), conclude $V, I$ are inverse bijections on algebraic sets / radical ideals; then read the prime-, maximal-, and lattice-refinements off the ideal structure.

**Subgoal decomposition:**

1. **Geometry-side round trip.** $V(I(X)) = X$ for $X$ algebraic, and $V(I(X))$ is the Zariski closure in general.
   - *Hint:* $X \subseteq V(I(X))$ always; if $X = V(\mathfrak b)$ then $V(I(X)) \subseteq V(I(V(\mathfrak b))) \subseteq V(\mathfrak b) = X$ using $\mathfrak b \subseteq I(V(\mathfrak b))$.
   - *Why needed:* The geometry-side closure operator; identifies closed objects as algebraic sets.

2. **Algebra-side round trip.** $I(V(\mathfrak a)) = \sqrt{\mathfrak a}$.
   - *Hint:* This is the [[Thm - The Strong Nullstellensatz|strong Nullstellensatz]].
   - *Why needed:* The algebra-side closure operator; identifies closed objects as radical ideals.

3. **The bijection.** On radical ideals, $I(V(\mathfrak a)) = \mathfrak a$; on algebraic sets, $V(I(X)) = X$; both inclusion-reversing.
   - *Hint:* Combine Steps 1–2 with $\mathfrak a$ radical $\iff \mathfrak a = \sqrt{\mathfrak a}$.
   - *Why needed:* The core statement.

4. **Refinements.** Primes $\leftrightarrow$ irreducibles ([[Ex - Irreducible iff the ideal is prime|via the irreducible–prime equivalence]]); maximals $\leftrightarrow$ points ([[Thm - The Weak Nullstellensatz|weak Nullstellensatz]]); lattice anti-isomorphism (formal properties of $V$ and $I$, with the radical on the sum).
   - *Hint:* Read each off the corresponding ideal property of the quotient ring.
   - *Why needed:* The stratified, working form of the dictionary.

---

# Lemma Decomposition

> [!note]- Lemma 1: $V(I(X)) = X$ for $X$ algebraic
> **Statement:** For any $X \subseteq \Omega^n$, $V(I(X))$ is the smallest algebraic set containing $X$; in particular $V(I(X)) = X$ iff $X$ is algebraic.
>
> **Hint:** $X \subseteq V(I(X))$ is immediate; for minimality, if $X \subseteq Y = V(\mathfrak b)$ then $I(Y) \subseteq I(X)$ so $V(I(X)) \subseteq V(I(Y)) \subseteq V(\mathfrak b) = Y$.
>
> **Why needed:** It is the geometry-side closure operator, identifying the closed objects of the Galois connection as the algebraic sets.
>
> > [!note]- Full proof
> > $X \subseteq V(I(X))$: every $x \in X$ is a zero of every $f \in I(X)$ (that is the definition of $I(X)$), so $x \in V(I(X))$. $V(I(X))$ is algebraic by construction. For minimality, suppose $X \subseteq Y$ with $Y = V(\mathfrak b)$ algebraic. Since $I$ reverses inclusions, $I(Y) \subseteq I(X)$, so $V(I(X)) \subseteq V(I(Y))$. And $\mathfrak b \subseteq I(V(\mathfrak b)) = I(Y)$, so $V(I(Y)) \subseteq V(\mathfrak b) = Y$. Hence $V(I(X)) \subseteq Y$. So $V(I(X))$ is the smallest algebraic set containing $X$, and equals $X$ exactly when $X$ is algebraic.

> [!note]- Lemma 2: Primes correspond to irreducible varieties
> **Statement:** A radical ideal $\mathfrak p$ is prime iff $V(\mathfrak p)$ is irreducible; equivalently $\mathfrak a$ is prime iff $k[T]/\mathfrak a$ is a domain iff $V(\mathfrak a)$ is irreducible.
>
> **Hint:** $V(\mathfrak p) = V(f) \cup V(g)$ relative to $V(\mathfrak p)$ corresponds to $fg \in I(V(\mathfrak p)) = \mathfrak p$ with $f, g \notin \mathfrak p$ — the prime condition.
>
> **Why needed:** It is the first refinement, identifying the geometric atoms with prime ideals; full proof on [[Ex - Irreducible iff the ideal is prime]].
>
> > [!note]- Full proof
> > Suppose $\mathfrak p = I(X)$ is prime and $X = X_1 \cup X_2$ with $X_i$ proper closed. Then $I(X) = I(X_1) \cap I(X_2)$ with both $I(X_i) \supsetneq I(X)$. A prime equal to a finite intersection of ideals equals one of them (ES2 Q2(a)), so $I(X) = I(X_i)$ for some $i$, giving $X = V(I(X)) = V(I(X_i)) = X_i$, contradicting properness — so $X$ is irreducible. Conversely if $X$ is irreducible and $fg \in I(X)$, then $X \subseteq V(f) \cup V(g)$, so $X = (X \cap V(f)) \cup (X \cap V(g))$; irreducibility forces $X \subseteq V(f)$ (say), i.e. $f \in I(V(f)) \subseteq I(X)$ — wait, more directly $f$ vanishes on $X$, so $f \in I(X)$. Hence $I(X)$ is prime. (Nonemptiness of $X$ gives $1 \notin I(X)$, so the ideal is proper.)

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\Omega \supseteq k$ be algebraically closed.
>
> **The bijection.** By **Lemma 1**, $V(I(X)) = X$ for every $k$-algebraic set $X$, and $I(X)$ is a radical ideal ([[Def - The Coordinate Ring and the Ideal of a Set|always]]). By the [[Thm - The Strong Nullstellensatz|strong Nullstellensatz]], $I(V(\mathfrak a)) = \sqrt{\mathfrak a}$, so for a *radical* ideal $\mathfrak a$, $I(V(\mathfrak a)) = \mathfrak a$. Therefore:
> - $X \mapsto I(X)$ sends algebraic sets to radical ideals, with $V \circ I = \mathrm{id}$ on algebraic sets;
> - $\mathfrak a \mapsto V(\mathfrak a)$ sends radical ideals to algebraic sets, with $I \circ V = \mathrm{id}$ on radical ideals.
>
> These are mutually inverse, hence bijections. Both reverse inclusions ($I$ and $V$ are individually inclusion-reversing), so the bijection is order-reversing.
>
> **Refinement 1 (primes $\leftrightarrow$ irreducibles).** By **Lemma 2**, $\mathfrak p$ radical is prime iff $V(\mathfrak p)$ is irreducible. So the bijection restricts to {irreducible algebraic sets} $\leftrightarrow$ {prime ideals}.
>
> **Refinement 2 (points $\leftrightarrow$ maximals, $k = \Omega$).** By the [[Thm - The Weak Nullstellensatz|weak Nullstellensatz]] (point form), $x \mapsto \mathfrak m_x = (T_1 - x_1, \dots, T_n - x_n)$ is a bijection $\Omega^n \to \operatorname{mSpec}$, with $V(\mathfrak m_x) = \{x\}$ and $I(\{x\}) = \mathfrak m_x$. So single points correspond to maximal ideals.
>
> **Refinement 3 (lattice anti-isomorphism).** From the [[Def - Affine Variety and the Vanishing Set|formal properties of the vanishing operation]]: $V(\mathfrak a + \mathfrak b) = V(\mathfrak a) \cap V(\mathfrak b)$ and $V(\mathfrak a \cap \mathfrak b) = V(\mathfrak a) \cup V(\mathfrak b)$. Dualizing via the bijection: $I(X \cup Y) = I(X) \cap I(Y)$ (a function vanishes on a union iff on each piece), and $I(X \cap Y) = \sqrt{I(X) + I(Y)}$ (apply $I$ to $V(I(X) + I(Y)) = V(I(X)) \cap V(I(Y)) = X \cap Y$ and use the strong Nullstellensatz to insert the radical). The radical is necessary: $I(X) + I(Y)$ may fail to be radical. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Solving geometric problems by ideal arithmetic.** To find the intersection of two surfaces in $\mathbb{C}^3$, compute $\sqrt{I_1 + I_2}$; to find their union, compute $I_1 \cap I_2$. The application is nonobvious because a *geometric* construction (intersect/union of shapes) is performed entirely by *ideal* operations and a radical, computable by Gröbner bases — the engine of every computer algebra system's geometry module.

**Galois descent and fields of definition.** Over $k = \mathbb{R}$, $\Omega = \mathbb{C}$, the maximal $\mathbb{R}$-ideals correspond not to single complex points but to Galois orbits $\{x, \bar x\}$ under $\operatorname{Gal}(\mathbb{C}/\mathbb{R})$; the dictionary becomes "Galois-stable algebraic sets $\leftrightarrow$ $\mathbb{R}$-radical ideals". The application battle-tests the points-as-maximals refinement against non-closed base fields, and is the entry to arithmetic geometry's **fields of definition**.

**Prime spectrum as a space, and generic points.** The correspondence "primes $\leftrightarrow$ irreducible varieties" says $\operatorname{Spec} k[T_1, \dots, T_n]$ *is* affine space enriched with a point for each irreducible subvariety (its **generic point**), whose closure is that subvariety. The application is nonobvious because it reveals classical $\Omega^n$ as the *closed points* of a larger space, the move that founds scheme theory and explains why generic-versus-special arguments work.

---

# Bridges

- **[[Thm - The Strong Nullstellensatz|The Strong Nullstellensatz]]** — the load-bearing input. The correspondence is "$V$ and $I$ are inverse bijections between the closed objects of a Galois connection", and the strong Nullstellensatz is exactly the computation of the algebra-side closure operator $\mathfrak a \mapsto I(V(\mathfrak a)) = \sqrt{\mathfrak a}$, identifying the closed ideals as the radical ones. Without it, $I(V(\mathfrak a))$ would be an unknown ideal $\supseteq \mathfrak a$ and the bijection would have no algebra side.

- **[[Def - Irreducible Algebraic Set|Irreducible algebraic sets]]** — the primes-stratum. "$X$ irreducible $\iff I(X)$ prime $\iff k[X]$ a domain" is the geometric reading of primality, refining the bijection to the geometric atoms; the [[Ex - Irreducible iff the ideal is prime|irreducible–prime exercise]] is its proof.

- **[[Thm - The Weak Nullstellensatz|The Weak Nullstellensatz]]** — the points-stratum. The weak form's point bijection $\Omega^n \to \operatorname{mSpec}$ is the bottom rung of the dictionary; the correspondence extends it upward from points/maximals to varieties/primes to algebraic-sets/radicals.

- **[[Commutative Algebra IX — Primary Decomposition|Primary decomposition]]** — the structural downstream. Decomposing a radical ideal into minimal primes is decomposing a variety into irreducible components; primary decomposition refines this to non-radical ideals, where the embedded primes record the scheme-theoretic thickening invisible to the radical correspondence.

---

# Unlocked by This

> [!tip] The full dictionary of affine algebraic geometry *(from Algebraic Geometry)*
> This is *the* foundational correspondence, and its complete form is an **anti-equivalence of categories**:
> $$\{\text{affine } \Omega\text{-varieties, regular maps}\} \ \simeq\ \{\text{finitely generated reduced } \Omega\text{-algebras}\}^{\mathrm{op}}.$$
> A variety $X$ is its coordinate ring $\Omega[X]$; a regular map $X \to Y$ is a $\Omega$-algebra homomorphism $\Omega[Y] \to \Omega[X]$; points are maximal ideals, irreducible subvarieties are primes, dimension is Krull dimension is transcendence degree, the local geometry at a point is the local ring $\Omega[X]_{\mathfrak m_x}$. Every geometric notion has an exact algebraic translation. Dropping "reduced" (keeping nilpotents) extends varieties to **affine schemes** $\operatorname{Spec} A$, and gluing affine schemes gives general **schemes** — the framework that absorbs arithmetic ($\operatorname{Spec} \mathbb{Z}$), infinitesimals (nilpotents), and non-closed fields into one geometry. This page is the affine, classical heart of that entire edifice.

> [!tip] Spec, the Zariski topology, and generic points *(from Algebraic Geometry / Scheme Theory)*
> Reading the correspondence on *all* primes (not just maximals) realises $\operatorname{Spec} \Omega[T_1, \dots, T_n]$ as affine space with one extra point per irreducible subvariety — its **generic point** $\eta$, whose closure $\overline{\{\eta\}} = V(\mathfrak p)$ is that subvariety. The **Zariski topology** on $\operatorname{Spec}$ has the $V(\mathfrak a)$ as closed sets, refining the classical Zariski topology on $\Omega^n$ (which appeared already from [[Commutative Algebra IV — Localization|localization]] as the spectrum's topology). Generic points make precise the classical phrase "a general point of the variety": a property holds generically iff it holds at the generic point, the cornerstone of moduli theory and of arguments that spread a property from one point to a whole component.
