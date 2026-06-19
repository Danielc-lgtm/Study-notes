---
type: exercise
subject: category-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - The Yoneda Lemma"
  - "Thm - The Yoneda Embedding is Fully Faithful"
  - "Def - Hom-Functor and Representable Functor"
  - "Def - Ring"
tags: [category-theory, foundations]
---

# Problem Statement

Work over a base ring $k$ (e.g. $k = \mathbb{Z}$); let $\mathbf{CRing}$ be commutative rings.

1. Recall that an **affine scheme** is a representable functor $\mathbf{CRing} \to \mathbf{Set}$, and that $\mathbf{Spec}$ is the (contravariant) [[Def - The Yoneda Embedding|Yoneda embedding]] $\mathbf{CRing}^{op} \to [\mathbf{CRing}, \mathbf{Set}]$, $R \mapsto \mathbf{CRing}(R, -)$.
2. Use [[Thm - The Yoneda Embedding is Fully Faithful|full faithfulness]] of Yoneda to prove $\mathbf{AffSch} \simeq \mathbf{CRing}^{op}$: a morphism of affine schemes $\mathbf{Spec}\,R \to \mathbf{Spec}\,S$ is *exactly* a ring homomorphism $S \to R$.
3. Conclude the slogan: **an affine scheme is completely determined by its functor of points** — by the sets of its $R$-points as $R$ ranges over all rings. Use the elliptic curve $C(R) = \{(a,b) \in R^2 : b^2 = a^3 - 1\}$ as the running example.

**Recall:**

![[Thm - The Yoneda Embedding is Fully Faithful#Statement]]

The [[Thm - The Yoneda Embedding is Fully Faithful|Yoneda embedding is fully faithful]]: $\mathcal{C}(A, B) \cong \mathrm{Nat}(\mathbf{y}A, \mathbf{y}B)$.

> [!note]- Algebraic geometry background (self-contained)
> No prior AG is assumed. A **commutative ring** $R$ has commutative $+, \times$, $0, 1$, additive inverses, distributivity (see [[Def - Ring]]). A **ring homomorphism** preserves $+, \times, 0, 1$. The **functor of points** of a polynomial system records its solutions in every ring: fixing equations gives a functor $C : \mathbf{CRing} \to \mathbf{Set}$, $R \mapsto \{\text{solutions with coordinates in } R\}$, and $C(R)$ is the set of **$R$-points**. An **affine scheme** is by definition a representable such functor; the representing ring $A$ (so $C \cong \mathbf{CRing}(A, -)$) is its ring of functions, and $\mathbf{Spec}\,A$ denotes the affine scheme. For the elliptic curve, $C(R) = \{(a,b) : b^2 = a^3 - 1\}$ is represented by $A = \mathbb{Z}[x, y]/(y^2 - x^3 + 1)$, because a ring map $A \to R$ is a choice of images $(a, b)$ of $(x, y)$ subject to the one defining relation $b^2 = a^3 - 1$.

---

# Convergent Strategy

**Problem class:** This is the capstone "specialize Yoneda to found a subject" exercise — the algebraic-geometry payoff of the entire chapter. The routine is to recognize $\mathbf{Spec}$ as the Yoneda embedding for $\mathbf{CRing}^{op}$ and read off full faithfulness as the ring–geometry dictionary.

**Assumption pattern:** The decisive assumption is "affine scheme = representable functor of points", which makes the category of affine schemes the *essential image* of the Yoneda embedding. Once affine schemes are defined this way, all the structural facts are corollaries of full faithfulness — no new geometry is needed, only the categorical theorem.

**Theorem routing:** The route is: (i) $\mathbf{Spec}$ is the contravariant Yoneda embedding $\mathbf{CRing}^{op} \to [\mathbf{CRing}, \mathbf{Set}]$, fully faithful by [[Thm - The Yoneda Embedding is Fully Faithful]]; (ii) full faithfulness gives $\mathbf{CRing}^{op}(\mathbf{Spec}\,R, \mathbf{Spec}\,S) \cong \mathrm{Nat}(\mathbf{Spec}\,R, \mathbf{Spec}\,S)$, and $\mathbf{CRing}^{op}(R, S) = \mathbf{CRing}(S, R)$, so scheme morphisms are ring maps $S \to R$; (iii) restricting to the essential image gives the equivalence $\mathbf{AffSch} \simeq \mathbf{CRing}^{op}$, and the [[Thm - The Yoneda Lemma|Yoneda lemma]] gives "determined by $R$-points".

**Key decision point:** The crucial move is recognizing that the *contravariance* of $\mathbf{Spec}$ flips the direction: a morphism of schemes $\mathbf{Spec}\,R \to \mathbf{Spec}\,S$ is a ring map $S \to R$, *backwards*. Getting this arrow-reversal right — that geometry is algebra with arrows reversed — is the entire dictionary, and it comes from working in $\mathbf{CRing}^{op}$ rather than $\mathbf{CRing}$.

---

# Legal Operations Used

1. **Operation 9 from the topic page (apply Yoneda full faithfulness to identify morphisms).** Full faithfulness of $\mathbf{Spec}$ identifies scheme morphisms with ring homomorphisms (reversed).

2. **Operation 4 from the topic page (carve an equivalence out of a fully faithful functor).** Restricting $\mathbf{Spec}$ to its essential image, the affine schemes, upgrades the embedding to the equivalence $\mathbf{AffSch} \simeq \mathbf{CRing}^{op}$.

---

# Hints

> [!note]- Hint 1
> $\mathbf{Spec}$ sends a ring $R$ to its functor of points $\mathbf{CRing}(R, -)$. This is the contravariant Yoneda embedding for the category $\mathbf{CRing}^{op}$. What does full faithfulness say about its hom-sets?

> [!note]- Hint 2
> Full faithfulness: $\mathrm{Nat}(\mathbf{CRing}(R, -), \mathbf{CRing}(S, -)) \cong \mathbf{CRing}(S, R)$. The left side is "morphisms of functors of points" = morphisms of affine schemes; the right side is ring maps $S \to R$.

> [!note]- Hint 3
> Mind the variance: $\mathbf{Spec}$ is contravariant, so a *scheme* morphism $\mathbf{Spec}\,R \to \mathbf{Spec}\,S$ corresponds to a *ring* map $S \to R$ — arrows reverse.

> [!note]- Hint 4
> For the slogan: by the Yoneda lemma, two affine schemes with naturally isomorphic functors of points (the same $R$-points for all $R$, compatibly) are isomorphic — so the functor of points is a complete invariant.

---

# Solution

The plan: recognize $\mathbf{Spec}$ as the Yoneda embedding for $\mathbf{CRing}^{op}$, apply full faithfulness to identify scheme morphisms with (reversed) ring maps, restrict to the essential image for the equivalence, and read off "determined by $R$-points" from the Yoneda lemma — illustrated throughout on the elliptic curve.

**Step 1: Spec is the Yoneda embedding for $\mathbf{CRing}^{op}$.**

> [!note]- Derivation
> The functor $\mathbf{Spec} : \mathbf{CRing}^{op} \to [\mathbf{CRing}, \mathbf{Set}]$ sends a ring $R$ to its functor of points $\mathbf{Spec}\,R = \mathbf{CRing}(R, -)$. In the language of [[Def - The Yoneda Embedding]], this is exactly the (covariant on $\mathbf{CRing}^{op}$, i.e. contravariant on $\mathbf{CRing}$) Yoneda embedding $\mathbf{y}$ for the category $\mathbf{CRing}^{op}$: it sends an object to its representable functor. By [[Thm - The Yoneda Embedding is Fully Faithful]], $\mathbf{y} = \mathbf{Spec}$ is **fully faithful**.

**Step 2: Scheme morphisms are ring maps, reversed.**

> [!note]- Derivation
> Full faithfulness gives, for rings $R, S$,
> $$\mathrm{Hom}_{\mathbf{AffSch}}(\mathbf{Spec}\,R, \mathbf{Spec}\,S) = \mathrm{Nat}(\mathbf{CRing}(R, -), \mathbf{CRing}(S, -)) \cong \mathbf{CRing}(S, R).$$
> The middle term is by definition a morphism of functors of points — a morphism of affine schemes. The right term is a ring homomorphism $S \to R$. Note the variance: a scheme morphism $\mathbf{Spec}\,R \to \mathbf{Spec}\,S$ is a ring map $S \to R$, *with the arrow reversed*. This is the foundational dictionary of algebraic geometry. *Example:* a morphism from the elliptic curve $\mathbf{Spec}\,A$ ($A = \mathbb{Z}[x,y]/(y^2 - x^3 + 1)$) to the affine line $\mathbf{Spec}\,\mathbb{Z}[t]$ is a ring map $\mathbb{Z}[t] \to A$, i.e. a choice of element of $A$ (a polynomial function on the curve) — say $t \mapsto x$, the "$x$-coordinate" map.

**Step 3: The equivalence $\mathbf{AffSch} \simeq \mathbf{CRing}^{op}$.**

> [!note]- Derivation
> $\mathbf{AffSch}$ is defined as the essential image of $\mathbf{Spec}$ — the representable functors of points. A fully faithful functor is an equivalence onto its essential image, so
> $$\mathbf{Spec} : \mathbf{CRing}^{op} \xrightarrow{\ \simeq\ } \mathbf{AffSch}.$$
> Affine geometry *is* commutative algebra with all arrows reversed. Every algebraic operation on rings has a geometric counterpart on schemes, dualized: tensor products of rings become fibre products of schemes, surjections become closed immersions, and so on.

**Step 4: The slogan — schemes are their functors of points.**

> [!note]- Derivation
> By the [[Thm - The Yoneda Lemma|Yoneda lemma]], $\mathbf{Spec}\,R \cong \mathbf{Spec}\,S$ as functors of points if and only if $R \cong S$ as rings, if and only if the schemes are isomorphic. So the functor of points — the assignment $R \mapsto C(R)$ of the set of $R$-points, together with its functoriality — is a *complete invariant* of an affine scheme. **An affine scheme is completely determined by the sets of its $R$-points as $R$ ranges over all rings.** For the elliptic curve, knowing $C(R) = \{(a,b) \in R^2 : b^2 = a^3 - 1\}$ for *every* ring $R$ (and how these vary under ring maps) determines the curve up to isomorphism; no further geometric data is needed. This is the founding principle of the functor-of-points approach, and it extends from affine schemes to general **schemes** by gluing.

> [!note]- Complete formal solution
> $\mathbf{Spec} : \mathbf{CRing}^{op} \to [\mathbf{CRing}, \mathbf{Set}]$, $R \mapsto \mathbf{CRing}(R, -)$, is the Yoneda embedding for $\mathbf{CRing}^{op}$, hence fully faithful by [[Thm - The Yoneda Embedding is Fully Faithful]]. Therefore $\mathrm{Hom}_{\mathbf{AffSch}}(\mathbf{Spec}\,R, \mathbf{Spec}\,S) \cong \mathbf{CRing}(S, R)$: a scheme morphism $\mathbf{Spec}\,R \to \mathbf{Spec}\,S$ is a ring map $S \to R$, arrows reversed. Restricting $\mathbf{Spec}$ to its essential image, the affine schemes, gives the equivalence $\mathbf{AffSch} \simeq \mathbf{CRing}^{op}$. By the [[Thm - The Yoneda Lemma|Yoneda lemma]], isomorphism of functors of points equals isomorphism of schemes, so an affine scheme is determined up to isomorphism by its $R$-points across all $R$ — illustrated by the elliptic curve $C(R) = \{(a,b) : b^2 = a^3 - 1\}$ represented by $\mathbb{Z}[x,y]/(y^2 - x^3 + 1)$. $\blacksquare$

---

# Key Takeaways

**Algebraic geometry's foundational dictionary is Yoneda full faithfulness, with arrows reversed.** The single most important takeaway is that "$\mathbf{AffSch} \simeq \mathbf{CRing}^{op}$" and "scheme morphisms = ring maps backwards" are not deep geometric facts but immediate corollaries of the [[Thm - The Yoneda Embedding is Fully Faithful|Yoneda embedding being fully faithful]], applied to the category $\mathbf{CRing}^{op}$ with $\mathbf{Spec}$ as the embedding. The contravariance is the whole content of the dictionary: maps of spaces correspond to maps of functions in the opposite direction, exactly as continuous maps $X \to Y$ induce algebra maps $C(Y) \to C(X)$. Whenever you see a "spaces ↔ algebras, arrows reversed" equivalence — affine schemes and rings, compact Hausdorff spaces and commutative C*-algebras (Gelfand), Stone spaces and Boolean algebras — suspect a contravariant Yoneda embedding underneath.

**"Determined by its functor of points" is the Yoneda lemma stated for geometry.** The slogan that organizes modern algebraic geometry — a scheme is known by its $R$-points for all rings $R$ — is precisely the Yoneda lemma: an object is determined by the functor it represents. The functoriality of $R \mapsto C(R)$ (how solutions transform under ring maps) is essential; the bare sets of points without their functoriality would not suffice. This reframes geometric objects as *functors*, which is what allows constructions impossible with point-sets alone (formal neighborhoods, non-reduced structure, moduli problems) to be defined by specifying their points valued in *all* rings, including rings with nilpotents. The trigger is "I want to define a geometric object but the point-set is inadequate"; the reaction is "define it by its functor of points".

**The functor-of-points viewpoint is the bridge from this chapter to a whole field, and the elliptic curve makes it concrete.** Carrying the running example through, the curve $b^2 = a^3 - 1$ is not a set of points over one field but a functor assigning to each ring its solution set, represented by $\mathbb{Z}[x,y]/(y^2 - x^3 + 1)$. Its $\mathbb{Q}$-points, $\mathbb{F}_p$-points, and $\mathbb{Z}/n$-points are all packaged in one object, and arithmetic questions (rational points, reduction mod $p$) become questions about this single functor. This is why representability, the Yoneda lemma, and full faithfulness — the abstract spine of this chapter — are the literal foundation of arithmetic geometry, and why the AG examples have run through every section: they are not illustrations of category theory but instances where the categorical theorems *are* the definitions of the field's objects.
