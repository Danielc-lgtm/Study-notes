---
type: definition
subject: category-theory
prereqs:
  - "Def - Category"
  - "Def - Opposite Category and Duality"
  - "Def - Isomorphism, Monomorphism, Epimorphism"
tags: [category-theory, foundations]
---

# Notation

A functor is written $F, G, H$. We write $F : \mathcal{C} \to \mathcal{D}$ for a functor from the [[Def - Category|category]] $\mathcal{C}$ to $\mathcal{D}$; it sends an object $A$ to $FA$ and a morphism $f : A \to B$ to $Ff : FA \to FB$. A **contravariant** functor is a functor out of the [[Def - Opposite Category and Duality|opposite category]], $F : \mathcal{C}^{\mathrm{op}} \to \mathcal{D}$, equivalently a rule sending $f : A \to B$ to $Ff : FB \to FA$. The hom-functor is $\mathcal{C}(A, -)$ or $\mathcal{C}(-, B)$. We write $(-)^*$ for the [[Def - Dual Space|dual-space]] functor and $\mathbf{Spec}$ for the prime-spectrum functor. The full registry is on [[Category Theory I — Categories, Functors, Natural Transformations]].

---

# Axiom Motivation

We have categories; now we need the maps between them. The guiding principle of all of mathematics — that the right notion of map is the one preserving the relevant structure — applies to categories themselves. The structure of a [[Def - Category|category]] is its objects, its morphisms, and the way morphisms compose. A map of categories should therefore carry objects to objects, morphisms to morphisms, and — crucially — **respect composition and identities**. That is a functor.

Why those two preservation conditions exactly, and no others? Consider what we want functors to do. The fundamental group assigns to each [[Def - Topological Space|space]] a [[Def - Group|group]] and to each [[Def - Continuous Map|continuous map]] a [[Def - Homomorphism|homomorphism]]; this assignment is the entire reason algebraic topology works, and it works *because* a composite of maps goes to the composite of homomorphisms: $\pi_1(g \circ f) = \pi_1(g) \circ \pi_1(f)$. If this failed, a topological factorization would tell you nothing algebraic, and the whole transfer of problems from topology to algebra would break. **Preservation of composition is the axiom that lets a functor transport relationships, not just objects.** Drop it and $F$ is a mere object-and-arrow relabelling with no structural content; you could not conclude anything about $FA$ from how $A$ sits among other objects.

**Preservation of identities, $F(1_A) = 1_{FA}$, is the axiom that makes a functor respect "sameness".** Drop it and the most basic consequence — that a functor sends [[Def - Isomorphism, Monomorphism, Epimorphism|isomorphisms]] to isomorphisms — fails. Indeed if $f$ has inverse $g$, then $Ff \circ Fg = F(f \circ g) = F(1) $, and only if $F(1) = 1$ does this say $Ff \circ Fg = 1$, i.e. $Ff$ is invertible. So the identity axiom is precisely what guarantees that "the same up to iso" is a functorial notion. (In fact, given composition-preservation, identity-preservation is *almost* automatic — $F(1_A) = F(1_A \circ 1_A) = F(1_A)F(1_A)$ makes $F(1_A)$ idempotent — but idempotents need not be identities in a general category, so the axiom is genuinely needed.)

There is one more design decision: which *direction* should a functor go? Most structure-assigning constructions are covariant — a map $f$ induces a map $Ff$ in the same direction. But some run backward. Pulling back functions along a map reverses arrows; taking the [[Def - Dual Space|dual space]] reverses linear maps; the spectrum of a ring reverses ring maps. Rather than invent a separate notion, we capture these as ordinary functors out of the [[Def - Opposite Category and Duality|opposite category]]: a **contravariant functor** $\mathcal{C} \to \mathcal{D}$ is just a functor $\mathcal{C}^{\mathrm{op}} \to \mathcal{D}$. The opposite-category construction was built for exactly this economy.

---

# The Definition

Let $\mathcal{C}, \mathcal{D}$ be [[Def - Category|categories]]. A **(covariant) functor** $F : \mathcal{C} \to \mathcal{D}$ consists of:

- an assignment $A \mapsto FA$ of an object of $\mathcal{D}$ to each object $A$ of $\mathcal{C}$;
- for each pair $A, B$, an assignment $\mathcal{C}(A, B) \to \mathcal{D}(FA, FB)$, $f \mapsto Ff$, of a morphism to each morphism;

subject to:

1. **Composition.** $F(g \circ f) = Fg \circ Ff$ for all composable $f, g$.
2. **Identities.** $F(1_A) = 1_{FA}$ for every object $A$.

A **contravariant functor** $F : \mathcal{C} \to \mathcal{D}$ is a functor $\mathcal{C}^{\mathrm{op}} \to \mathcal{D}$: it sends $f : A \to B$ to $Ff : FB \to FA$ and satisfies $F(g \circ f) = Ff \circ Fg$ (composition order reversed) and $F(1_A) = 1_{FA}$.

Functors compose ($G \circ F$ is a functor) and there is an identity functor $1_{\mathcal{C}}$ on each category, so small categories and functors themselves form a [[Def - Category|category]] $\mathbf{Cat}$.

---

# Relate to Other Fields / Compression

A functor is a [[Def - Homomorphism|homomorphism]] of categories — the exact analogue of a group homomorphism, a [[Def - Ring Homomorphism|ring homomorphism]], a [[Def - Continuous Map|continuous map]]. Just as a group homomorphism preserves products and identities, a functor preserves composition and identities. The compression is total: **everywhere you have seen "structure-preserving map", the categorical version is "functor", and the structure being preserved is composition.**

**True name:** *a composition-preserving assignment that transports relationships between objects into relationships between their images.* The operational consequence is that a functor lets you *export* problems: a hard question about $\mathcal{C}$ becomes a (sometimes easier) question about $\mathcal{D}$, and any relationship you establish downstream in $\mathcal{D}$ that is "reflected" comes back upstream. The fundamental group exports "is this space simply connected?" to "is this group trivial?"; the spectrum exports geometry to algebra.

---

# Examples / Corollaries

**Forgetful functors.** $U : \mathbf{Grp} \to \mathbf{Set}$ sends a [[Def - Group|group]] to its underlying set and a [[Def - Homomorphism|homomorphism]] to its underlying function. It forgets the group structure. It is faithful (different homomorphisms have different underlying functions) but not full (not every function between underlying sets is a homomorphism). Forgetful functors exist for every algebraic category: $\mathbf{Ring} \to \mathbf{Set}$, $\mathbf{Top} \to \mathbf{Set}$, $\mathbf{Vect}_k \to \mathbf{Set}$, and partial forgetters like $\mathbf{Ring} \to \mathbf{Ab}$.

**Free functors.** $F : \mathbf{Set} \to \mathbf{Grp}$ sends a set $S$ to the [[Def - Free Group and Free Product|free group]] on $S$ and a function $S \to T$ to the induced homomorphism between free groups. It is left adjoint to $U$ (the **free–forgetful adjunction** $F \dashv U$), the first and most important [[Def - Adjunction|adjunction]]. Similar free functors land in $\mathbf{Mod}_R$ (free modules), $\mathbf{Vect}_k$ (free vector space on a set, i.e. functions with finite support).

**Hom-functors.** Fix an object $A$ of $\mathcal{C}$. The **covariant hom-functor** $\mathcal{C}(A, -) : \mathcal{C} \to \mathbf{Set}$ sends $X \mapsto \mathcal{C}(A, X)$ and a morphism $f : X \to Y$ to post-composition $f \circ (-) : \mathcal{C}(A, X) \to \mathcal{C}(A, Y)$. The **contravariant hom-functor** $\mathcal{C}(-, B) : \mathcal{C}^{\mathrm{op}} \to \mathbf{Set}$ sends $X \mapsto \mathcal{C}(X, B)$ and $f : X \to Y$ to pre-composition $(-) \circ f : \mathcal{C}(Y, B) \to \mathcal{C}(X, B)$. These are the functors the **Yoneda lemma** is about, and they are exactly the functions that define mono and epi (see [[Def - Isomorphism, Monomorphism, Epimorphism]]).

**The covariant and contravariant power-set functors.** The **covariant power set** $P : \mathbf{Set} \to \mathbf{Set}$ sends a set $X$ to its power set $P(X)$ and a function $f : X \to Y$ to the *image* map $P(f) : P(X) \to P(Y)$, $A \mapsto f(A)$. The **contravariant power set** $P^{\bullet} : \mathbf{Set}^{\mathrm{op}} \to \mathbf{Set}$ sends $X$ to $P(X)$ but a function $f : X \to Y$ to the *preimage* map $P^{\bullet}(f) : P(Y) \to P(X)$, $B \mapsto f^{-1}(B)$. The contrast is the cleanest illustration of variance: image pushes forward (covariant), preimage pulls back (contravariant), and preimage is the better-behaved of the two because it commutes with unions, intersections, and complements.

**The fundamental group as a functor.** $\pi_1 : \mathbf{Top}_* \to \mathbf{Grp}$ sends a based [[Def - Topological Space|space]] $(X, x_0)$ to its [[Def - Path-Product and the Fundamental Group|fundamental group]] $\pi_1(X, x_0)$ and a based [[Def - Continuous Map|continuous map]] $f$ to $\pi_1(f) = f_*$, $[\gamma] \mapsto [f \circ \gamma]$. Functoriality, $\pi_1(g \circ f) = \pi_1(g) \circ \pi_1(f)$, is what makes algebraic topology a transfer principle: a topological factorization becomes an algebraic one.

**Singular homology.** $H_n : \mathbf{Top} \to \mathbf{Ab}$ sends a space to its $n$-th [[Def - Singular Homology|singular homology group]] and a continuous map to the induced homomorphism on homology. Each $H_n$ is a functor; together they are the workhorse of homotopy-invariant algebraic topology.

**The dual space, contravariantly.** For a field $k$, the **dual-space functor** $(-)^* : \mathbf{Vect}_k^{\mathrm{op}} \to \mathbf{Vect}_k$ sends a [[Def - Vector Space|vector space]] $V$ to its [[Def - Dual Space|dual]] $V^* = \mathrm{Hom}_k(V, k)$ and a [[Def - Linear Map|linear map]] $f : V \to W$ to the [[Def - Dual Map|dual map]] $f^* : W^* \to V^*$, $\varphi \mapsto \varphi \circ f$. The variance is contravariant precisely *because* the dual map is defined by **precomposition**: to pull a functional on $W$ back to one on $V$ you compose with $f$, which reverses direction. The reversal of order, $(g \circ f)^* = f^* \circ g^*$, is the opposite-category law in action — $(-)^*$ is a genuine instance of $\mathbf{Vect}_k^{\mathrm{op}} \to \mathbf{Vect}_k$.

**Spec — a contravariant functor from rings to spaces.** This is the algebraic-geometry example; read the background first.

> [!note]- Algebraic geometry background (self-contained)
> A **commutative ring** $R$ is a [[Def - Ring|ring]] in which multiplication commutes, $ab = ba$ (think of $\mathbb{Z}$, or polynomial rings $k[x_1, \dots, x_n]$, or rings of functions). The central insight of algebraic geometry is that *a commutative ring should be regarded as the ring of functions on a hidden geometric space*, and that the space can be reconstructed from the ring.
>
> The points of that space are the **prime ideals** of $R$. An **ideal** $I \subseteq R$ is a subset closed under addition and under multiplication by any ring element ($r \in R$, $a \in I \Rightarrow ra \in I$); it is **prime** if $ab \in I$ implies $a \in I$ or $b \in I$ (and $I \neq R$). For the ring of functions on a space, the functions vanishing at a fixed point form a prime ideal, which is why "prime ideal" is the algebraic stand-in for "point". The **prime spectrum** $\mathrm{Spec}\, R$ is the set of all prime ideals of $R$.
>
> $\mathrm{Spec}\, R$ carries the **Zariski topology**: the closed sets are $V(I) = \{\mathfrak{p} : \mathfrak{p} \supseteq I\}$, the primes containing a given ideal $I$ — geometrically, "the locus where all functions in $I$ vanish". This makes $\mathrm{Spec}\, R$ a [[Def - Topological Space|topological space]]. The dictionary: ring $\leftrightarrow$ space, prime ideal $\leftrightarrow$ point, ideal $\leftrightarrow$ closed subset, ring element $\leftrightarrow$ function. An **affine scheme** is $\mathrm{Spec}\, R$ together with the bookkeeping of which ring of functions lives on each open set.

The assignment $R \mapsto \mathrm{Spec}\, R$ is a **contravariant** functor $\mathbf{Spec} : \mathbf{CRing}^{\mathrm{op}} \to \mathbf{Top}$. Given a [[Def - Ring Homomorphism|ring homomorphism]] $\varphi : A \to B$, define $\mathbf{Spec}\,\varphi : \mathrm{Spec}\, B \to \mathrm{Spec}\, A$ by **pulling back primes**: $\mathfrak{q} \mapsto \varphi^{-1}(\mathfrak{q})$. The preimage of a prime ideal under a ring map is again prime (if $\varphi(a)\varphi(b) = \varphi(ab) \in \mathfrak{q}$ then $ab \in \varphi^{-1}(\mathfrak{q})$ forces $a$ or $b$ into it), and this map is continuous for the Zariski topology. The direction reversal — a map $A \to B$ of rings yields a map $\mathrm{Spec}\, B \to \mathrm{Spec}\, A$ of spaces — is the formal expression of "functions pull back": if $B$ is the functions on a space $Y$ and $A$ the functions on $X$, a geometric map $Y \to X$ is the same as an algebraic map $A \to B$ pulling functions back from $X$ to $Y$. **This is the prototypical contravariant functor, and it previews the equivalence $\mathbf{CRing}^{\mathrm{op}} \simeq$ affine schemes** that founds modern algebraic geometry.

**Is NOT a functor.** The assignment $G \mapsto Z(G)$ (the centre of a group) does *not* extend to a functor $\mathbf{Grp} \to \mathbf{Grp}$: a homomorphism $f : G \to H$ need not carry $Z(G)$ into $Z(H)$ (a central element can map to a non-central one), so there is no functorial action on morphisms. Likewise "the set of generators of minimal size" is not functorial. The lesson: an object-assignment is only the *first* half of a functor; the existence of a coherent action on morphisms is a real condition that can fail.

**Calibration check.** Verify that a functor sends [[Def - Isomorphism, Monomorphism, Epimorphism|isomorphisms]] to isomorphisms (use $F(f^{-1}) = (Ff)^{-1}$, which needs both axioms). Verify that the composite of two functors is a functor, and that a functor between one-object categories $\mathbf{B}G \to \mathbf{B}H$ is exactly a group [[Def - Homomorphism|homomorphism]] $G \to H$. Confirm you can say in one sentence why $(-)^*$ on vector spaces is contravariant rather than covariant (it is defined by precomposition, which reverses arrows).

---

# Unlocked by This

> [!tip] Representable Functors and Yoneda *(from this subject, Chapter II)*
> The hom-functors $\mathcal{C}(A, -)$ and $\mathcal{C}(-, B)$ are the **representable functors**, and the [[Def - The Yoneda Embedding|Yoneda embedding]] $\mathbf{y} : \mathcal{C} \hookrightarrow [\mathcal{C}^{\mathrm{op}}, \mathbf{Set}]$ realizes every object as the presheaf it represents. The **Yoneda lemma** says an object is completely determined by its hom-functor — "an object is what it does".

> [!tip] Spec and the Functor of Points *(from Algebraic Geometry)*
> The contravariant functor **Spec** is half of the equivalence $\mathbf{CRing}^{\mathrm{op}} \simeq$ **affine schemes**. Dually, a **scheme** can be defined as a functor $\mathbf{CRing} \to \mathbf{Set}$ (its **functor of points**), recovering the geometry from how the ring maps into test rings — an application of representability and Yoneda to geometry.

> [!tip] Derived Functors and Homological Algebra *(from Homological Algebra)*
> When a functor between **abelian categories** fails to be exact (fails to preserve short exact sequences), one measures the failure with its **derived functors** — $\mathrm{Tor}$ and $\mathrm{Ext}$ are the derived functors of $\otimes$ and $\mathrm{Hom}$. The functoriality of $H_n$ above is the entry point.
