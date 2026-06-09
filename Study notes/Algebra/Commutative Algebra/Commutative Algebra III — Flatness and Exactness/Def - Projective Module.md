---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Free Module"
  - "Def - Module Homomorphism"
  - "Def - Exact Sequence and Short Exact Sequence"
  - "Def - The Hom Functor and Left Exactness"
  - "Def - Quotient Module"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$ and all modules are unital. Let $R$ be a ring. For modules $N' \subseteq N$ we write $\pi : N \to N/N'$ for the [[Def - Quotient Module|quotient map]]. A diagram $M \xrightarrow{g} N \xrightarrow{\pi} N/N'$ *lifts* $\bar h : M \to N/N'$ when $\pi \circ g = \bar h$. We write $\operatorname{Hom}_R(M, -)$ for the [[Def - The Hom Functor and Left Exactness|covariant Hom functor]], $R^{\oplus I}$ for the [[Def - Free Module|free module]] on an index set $I$, and call a short exact sequence $0 \to A \xrightarrow{f} B \xrightarrow{g} C \to 0$ **split** if there is a section $s : C \to B$ with $g \circ s = \operatorname{id}_C$ (equivalently $B \cong A \oplus C$ compatibly with $f, g$ — see [[Ex - The splitting lemma]]). The full registry is on [[Commutative Algebra III — Flatness and Exactness]].

---

# Axiom Motivation

[[Def - Free Module|Free modules]] are wonderful and rare. They have bases, every map out of them is determined by where the basis goes, and they are flat for the cheapest possible reason. But most modules are not free, and one wants a class that keeps the *useful behaviour* of free modules while admitting far more examples. The single most useful behaviour of a free module is its **lifting property**, and projectivity is precisely the class of modules that share it.

Here is the property, isolated. Suppose $F = R^{\oplus I}$ is free, with basis $(e_i)$, and you are handed a surjection $\pi : N \twoheadrightarrow N/N'$ and a map $\bar h : F \to N/N'$. Can you *lift* $\bar h$ — find $g : F \to N$ with $\pi \circ g = \bar h$? For a free module the answer is a one-line yes: for each basis vector $e_i$, the target $\bar h(e_i)$ lies in $N/N'$; since $\pi$ is onto, choose any preimage $g(e_i) \in N$ with $\pi(g(e_i)) = \bar h(e_i)$; extend $g$ linearly using the basis. The lift exists because *a map out of a free module is just an arbitrary choice of images of the basis*, and "arbitrary choice" is exactly what surjectivity of $\pi$ lets you make. The definition of **projective** abstracts this: $M$ is projective if every map $M \to N/N'$ to a quotient lifts to a map $M \to N$ through $\pi$. Free modules satisfy it; the question is what else does.

**Why a lifting property and not a universal property.** Notice the lift $g$ is *not unique* — at each basis vector you chose a preimage, and any other choice (differing by an element of $N'$) gives another valid lift. So projectivity is a *lifting* property, an existence statement with no uniqueness, and emphatically not a universal property in the categorical sense (which would pin $g$ down uniquely). This non-uniqueness is not a defect; it is what gives the class room. A universal property would force $M$ to be a very specific object; the mere existence of *some* lift is a far weaker, far more inclusive demand, satisfied by every direct summand of a free module, not just free modules themselves.

**Why this is the same as "summand of a free module".** The deep content, proved in [[Thm - Projective iff Direct Summand of a Free Module|the characterization theorem]], is that the abstract lifting property is equivalent to a concrete structural one: $M$ is projective if and only if $M \oplus N \cong R^{\oplus I}$ for some $N$, i.e. $M$ is a *direct summand of a free module*. The motivation for believing this: present $M$ as a quotient of a free module, $F \twoheadrightarrow M$ — always possible, send a basis to a generating set. Apply the lifting property to lift the identity $\operatorname{id}_M : M \to M = F/(\ker)$ back to $F$; the lift is a section, which splits the surjection and exhibits $M$ as a summand of $F$. Conversely a summand of free inherits the lifting property because free modules have it and it passes to summands. So "lifts maps to quotients" and "is a piece of a free module" are two faces of one notion — the abstract dynamical property and the static structural one.

**Why projective sits exactly one rung below free and one above flat.** Strengthen projective to free and you demand an actual basis — too strong, as the summand $\mathbb{Z}/2$ of the free $\mathbb{Z}/6$-module $\mathbb{Z}/6 = \mathbb{Z}/2 \oplus \mathbb{Z}/3$ shows: it is a summand of a free module (hence projective) but has only two elements, while every non-zero free $\mathbb{Z}/6$-module has at least six, so it is not free. Weaken projective and you lose the lifting property that makes it useful; the natural weakening is **flat**, and indeed projective $\Rightarrow$ flat because a summand of a free (hence flat) module is flat — but flat is strictly weaker, since $\mathbb{Q}$ is flat over $\mathbb{Z}$ and not projective (a projective $\mathbb{Q}$ would be a summand of a free abelian group, impossible for a divisible group). So projective is the precise middle rung: it keeps the lifting/splitting power of free without the basis, and it implies the exactness power of flat without being merely flat.

**The functorial reading, for completeness.** [[Thm - Hom is Left Exact|Hom(M, −) is always left exact]] — it preserves the injection at the front of an exact sequence. The one thing it may lose is the *surjection* at the back: a surjection $N \twoheadrightarrow N/N'$ need not induce a surjection $\operatorname{Hom}(M, N) \to \operatorname{Hom}(M, N/N')$, and inducing one is *exactly* the lifting property (every map $M \to N/N'$ comes from a map $M \to N$). So "$M$ is projective" is identically "$\operatorname{Hom}(M, -)$ is a fully exact functor." Projective is to $\operatorname{Hom}(M,-)$ what flat is to $M \otimes (-)$: the condition that upgrades a half-exact functor to a fully exact one.

---

# The Definition

Let $R$ be a commutative ring and $M$ an $R$-module.

## Projective module (lifting form)

$M$ is **projective** if for every $R$-module $N$, every submodule $N' \subseteq N$, and every $R$-linear map $\bar h : M \to N/N'$, there exists an $R$-linear map $g : M \to N$ with
$$\pi \circ g = \bar h, \qquad \text{where } \pi : N \to N/N' \text{ is the quotient map.}$$
The lift $g$ is not required to be unique.

## Equivalent forms

By [[Thm - Projective iff Direct Summand of a Free Module|the characterization theorem]], for an $R$-module $M$ the following are equivalent:

1. **(Lifting)** $M$ is projective in the sense above.
2. **(Exactness)** The functor $\operatorname{Hom}_R(M, -)$ is exact.
3. **(Splitting)** Every short exact sequence $0 \to A \to B \to M \to 0$ splits.
4. **(Summand)** $M$ is a direct summand of a [[Def - Free Module|free module]]: there is a module $N$ with $M \oplus N \cong R^{\oplus I}$.

Form 4 is the most concrete and is the one usually used to *recognise* projectives and to deduce **projective $\Rightarrow$ flat** (a summand of a free module is flat).

---

# Categorical / Structural Definition

Structurally, **$M$ is projective exactly when $\operatorname{Hom}_R(M, -)$ is an exact functor.** The functor $\operatorname{Hom}_R(M, -)$ is always [[Thm - Hom is Left Exact|left exact]] — it carries $0 \to A \to B \to C$ to $0 \to \operatorname{Hom}(M,A) \to \operatorname{Hom}(M,B) \to \operatorname{Hom}(M,C)$ — and the only exactness it can lose is the surjectivity at the right end. Projectivity is precisely the hypothesis restoring it, making $\operatorname{Hom}(M,-)$ fully exact. In the categorical picture this is the lifting property drawn as a diagram: for any epimorphism $\pi : N \twoheadrightarrow Q$ and any $\bar h : M \to Q$, a lift $g : M \to N$ exists with $\pi g = \bar h$ — $M$ is a *projective object* of the category of $R$-modules, dual to the notion of an injective object (defined by the mirror-image lifting against monomorphisms). The derived-functor reading: projectives are the $\operatorname{Hom}(-, P)$-acyclic objects used to build projective resolutions and compute $\operatorname{Ext}$ and $\operatorname{Tor}$, the exact dual of how injectives compute the right-derived theory. The full proof of the four-way equivalence is on [[Thm - Projective iff Direct Summand of a Free Module]].

---

# Relate to Other Fields / Compression

The cleanest compression: **projective means "free, but only locally / up to a complement" — a piece of a free module that need not be the whole thing.** A [[Def - Free Module|free module]] is a piece that fills out a free module by itself; a projective module is a piece that fills out a free module once you add a complement. Everything free does *with* a basis, projective does *with the help of a partner module* $N$ such that $M \oplus N$ is free.

**True name:** the true name of projective is *not* the lifting property but **"$M$ is a direct summand of a free module."** This is the form you use to recognise and produce projectives: exhibit a free module containing $M$ as a summand, or equivalently a surjection $F \twoheadrightarrow M$ that splits. The lifting and exactness forms are how you *reason about* projectives once you have one; the summand form is how you *find* them.

In algebraic geometry and topology the compression is the **Serre–Swan dictionary**: a finitely generated projective module over the ring of functions on a space is exactly a **vector bundle** over that space, with [[Def - Free Module|free]] modules corresponding to *trivial* bundles. The summand characterization $M \oplus N \cong R^n$ is the algebraic form of "every vector bundle is a sub-bundle of a trivial bundle with a complementary bundle," which holds over compact and over affine spaces. So projective-but-not-free is the algebra of *non-trivial* bundles, and the lifting property is the algebra of the homotopy lifting that defines fibrations. The same notion appears in homological algebra as the building block of *projective resolutions*, the exact dual of injective resolutions in sheaf cohomology.

---

# Examples / Corollaries

**Is an instance — free modules.** Every [[Def - Free Module|free module]] $R^{\oplus I}$ is projective: it is a direct summand of itself (take the complement $N = 0$), and the lifting property holds by choosing preimages of basis images. This is the top of the projective class.

**Is an instance — summands cut out by idempotents.** If $e \in R$ is an idempotent ($e^2 = e$), then $R = Re \oplus R(1-e)$ as $R$-modules, so $Re$ is a direct summand of the free module $R$, hence projective. Over $R = \mathbb{Z}/6$ the idempotent $e = (1,0)$ under $\mathbb{Z}/6 \cong \mathbb{Z}/2 \times \mathbb{Z}/3$ gives the projective summand $Re \cong \mathbb{Z}/2$. This is the mechanism behind the projective-not-free example.

**Is an instance — non-principal ideals in a Dedekind domain.** In $R = \mathbb{Z}[\sqrt{-5}]$ the ideal $(2, 1+\sqrt{-5})$ is projective (every ideal of a Dedekind domain is projective) but not free (it is not principal, so not free of rank one, and rank considerations exclude other ranks). It represents the non-trivial element of the ideal class group.

**Is NOT an instance — $\mathbb{Q}$ over $\mathbb{Z}$.** The module $\mathbb{Q}$ is flat but *not* projective over $\mathbb{Z}$ ([[Ex - Q is a flat but not projective Z-module]]). If it were projective it would be a direct summand of a free abelian group, hence a subgroup of a free abelian group; but $\mathbb{Q}$ is divisible and a non-zero divisible subgroup of a free abelian group cannot exist (free abelian groups have no non-trivial divisible elements). So projective is strictly stronger than flat.

**Is NOT an instance — $\mathbb{Z}/2$ over $\mathbb{Z}$.** Over $\mathbb{Z}$ the module $\mathbb{Z}/2$ is neither flat nor projective: the surjection $\mathbb{Z} \twoheadrightarrow \mathbb{Z}/2$ does not split (no section, as $\mathbb{Z}$ is torsion-free), so $\mathbb{Z}/2$ is not a summand of $\mathbb{Z}$, and more generally it has torsion. (Contrast: over $\mathbb{Z}/6$, the module $\mathbb{Z}/2$ *is* projective — base ring matters.)

**Corollary — projective $\Rightarrow$ flat.** Since a projective module is a direct summand of a free module, and free modules are flat, and direct summands of flat modules are flat, every projective module is flat. The converse fails ($\mathbb{Q}$ over $\mathbb{Z}$).

**Corollary — over a PID or a local ring, projective $=$ free** (for finitely generated modules; for general modules over a PID by a theorem of Kaplansky). This is why the projective-not-free phenomenon only appears over rings that are neither local nor principal.

**Calibration check.** Verify that for an idempotent $e$, $R = Re \oplus R(1-e)$, so $Re$ is projective — and check $e = (1,0)$ gives $Re \cong \mathbb{Z}/2$ over $\mathbb{Z}/6$. Confirm that "$\operatorname{Hom}(M,-)$ exact" is the same as the lifting property by writing out what surjectivity of $\operatorname{Hom}(M, N) \to \operatorname{Hom}(M, N/N')$ means. Finally, explain from the summand form why projective implies flat, and produce from memory the reason $\mathbb{Q}$ is not projective over $\mathbb{Z}$.

---

# Unlocked by This

> [!tip] Vector bundles and the Serre–Swan theorem *(from Algebraic Geometry / Topology)*
> A finitely generated projective module over the ring of functions on a space is exactly a **vector bundle** over the space, free modules corresponding to *trivial* bundles. The summand characterization $M \oplus N \cong R^n$ is the algebraic shadow of "every bundle embeds in a trivial bundle with a complement." The **Serre–Swan theorem** makes this an equivalence of categories, and projective-not-free modules are the algebra of globally twisted, locally trivial bundles — the $\mathbb{Z}/6$ summand and the ideal $(2, 1+\sqrt{-5})$ being the smallest witnesses.

> [!tip] The ideal class group *(from Algebraic Number Theory)*
> Over a **Dedekind domain** every ideal is projective, and the rank-one projective modules modulo the free ones form the **ideal class group**, the central invariant measuring the failure of unique factorization. A non-principal ideal like $(2, 1+\sqrt{-5})$ is a non-free projective module representing a non-trivial class; the class group is finite for rings of integers and is the quantitative form of this page's projective-not-free gap.

> [!tip] Projective resolutions and Ext *(from Homological Algebra)*
> Because $\operatorname{Hom}(M, -)$ is exact for projective $M$, projective modules are the building blocks of **projective resolutions** $\cdots \to P_1 \to P_0 \to M \to 0$, from which the derived functors $\operatorname{Ext}^n(M, -)$ and $\operatorname{Tor}_n(M, -)$ are computed. Projectives are the acyclic objects of this theory, exactly dual to injective resolutions in sheaf cohomology.
