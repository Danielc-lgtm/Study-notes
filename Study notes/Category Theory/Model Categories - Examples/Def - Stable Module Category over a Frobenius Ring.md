---
type: definition
subject: model-categories
prereqs:
  - "Def - Model Category"
  - "Def - Module"
  - "Def - Ring"
  - "Def - Projective Module"
  - "Def - Cofibrant and Fibrant Objects"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $R$ is a ring and "module" means left $R$-[[Def - Module|module]]; $\mathbf{Mod}_R$ is the category of all left $R$-modules. A module $P$ is **projective** if $\mathrm{Hom}(P, -)$ is exact (equivalently, $P$ is a direct summand of a free module); a module $I$ is **injective** if $\mathrm{Hom}(-, I)$ is exact. We write $\operatorname{Hom}(M,N)$ for the abelian group of $R$-module maps, and $\operatorname{PHom}(M,N) \subseteq \operatorname{Hom}(M,N)$ for those maps that **factor through a projective**: $f \in \operatorname{PHom}(M,N)$ if $f = \beta \alpha$ for some $\alpha : M \to P$, $\beta : P \to N$ with $P$ projective. The **stable hom** is $\underline{\operatorname{Hom}}(M,N) = \operatorname{Hom}(M,N) / \operatorname{PHom}(M,N)$. The **stable module category** is written $\underline{\mathbf{Mod}}_R$ (also $\operatorname{StMod}(R)$). For a module $M$, the **syzygy** $\Omega M$ is the kernel of a projective cover $P \twoheadrightarrow M$; the **cosyzygy** $\Sigma M$ is the cokernel of an injective hull $M \hookrightarrow I$. The full symbol registry is on [[Model Categories — Examples in Detail]].

This page defines two interlocking notions — the **Frobenius ring** and the **stable module category** it supports — because the second is only well-behaved over the first: it is the Frobenius condition (projective = injective) that makes the suspension an autoequivalence and the stable category triangulated.

---

# Axiom Motivation

In modular representation theory — the study of [[Def - Module|modules]] over a group algebra $k[G]$ for a *finite* group $G$ and a field $k$ whose characteristic divides $|G|$ — the projective modules are uninteresting. They are the "free part" of the theory: every projective is a sum of indecomposable projectives, they carry no cohomological information, and they appear and disappear as one resolves modules. The interesting invariants — group cohomology, the structure of the representation category, the support varieties — all live in the *complement* of the projectives. So one wants a category in which **projective modules become zero**, leaving only the information that survives after discarding them. The stable module category is exactly that quotient.

How should one make projectives zero? The naive idea — delete the projective objects — fails, because projectives appear inside non-projective modules and inside the maps between them. The correct move is to kill the *maps* that pass through a projective: declare $f : M \to N$ to be zero if $f$ factors as $M \to P \to N$ with $P$ projective. The set $\operatorname{PHom}(M,N)$ of such maps is the thing to quotient by. Why is this the right object? Because a module $P$ is projective if and only if $\mathrm{id}_P$ factors through a projective (namely $P$ itself), so $\underline{\operatorname{Hom}}(P,P) = 0$ exactly when $P$ is projective — projectives become zero objects, which was the goal. And $\operatorname{PHom}$ is a two-sided ideal of the category (closed under pre- and post-composition with arbitrary maps, because composing a factor-through-projective with anything still factors through that projective), so the quotient $\underline{\mathbf{Mod}}_R$ is a genuine [[Def - Category|category]]. If instead we quotiented by maps factoring through *injectives*, we would get the costable category; the two coincide precisely when projective = injective, which is the next condition.

Now, why **Frobenius**? We want the stable category to be a *homotopy category of a model structure*, and specifically a **triangulated** one, with an invertible suspension. The suspension should be the cosyzygy $\Sigma M$ (cokernel of an injective hull) and its inverse the syzygy $\Omega M$ (kernel of a projective cover). For $\Sigma$ and $\Omega$ to be mutually inverse autoequivalences, every module must have *both* a projective cover and an injective hull, and crucially the projectives used by $\Omega$ must be the same objects as the injectives used by $\Sigma$ — otherwise the two operations live in different worlds and cannot cancel. The condition that makes projective = injective is exactly **self-injectivity** of the ring, the Frobenius condition. Drop it, and the syzygy is still defined but is not invertible, so the stable category is only *pre-triangulated*, not triangulated; the cofiber and fiber sequences do not become the same. The Frobenius condition is the per-axiom necessity: it is precisely what upgrades the stable category from a quotient category to a triangulated, stable homotopy category.

There is a final design question: why is this a model structure at all, and not just a quotient construction? Because we can package it as one, and doing so connects it to the rest of the subject. Take weak equivalences to be the **stable equivalences** (maps becoming isomorphisms in $\underline{\mathbf{Mod}}_R$), cofibrations to be the monomorphisms, and fibrations to be the epimorphisms. Then *every object is cofibrant* (every $0 \to M$ is mono) and *every object is fibrant* (every $M \to 0$ is epi), so every object is bifibrant — and the [[Thm - The Homotopy Category of a Model Category|fundamental theorem]] says the homotopy category is computed with no replacement step at all, directly as the quotient by stable equivalence. This is the simplest possible shape a model structure can take, and it is what makes the stable category its own homotopy category.

---

# The Definition

A ring $R$ is **Frobenius** (or **self-injective**, in the Noetherian case quasi-Frobenius) if $R$ is injective as a left module over itself. The decisive consequence is that the classes of **projective** and **injective** modules coincide.

> A **Frobenius ring** is a ring $R$ such that a [[Def - Module|module]] is projective if and only if it is injective.

Over such a ring, the **stable module category** $\underline{\mathbf{Mod}}_R$ is defined as follows.

> The **stable module category** $\underline{\mathbf{Mod}}_R$ has the same objects as $\mathbf{Mod}_R$, and morphisms
> $$\underline{\operatorname{Hom}}(M, N) \;=\; \operatorname{Hom}(M, N) \,/\, \operatorname{PHom}(M, N),$$
> where $\operatorname{PHom}(M,N)$ is the subgroup of maps factoring through a [[Def - Projective Module|projective]] module. Composition is induced from $\mathbf{Mod}_R$; it is well-defined because $\operatorname{PHom}$ is a two-sided ideal.

This is the homotopy category of the **stable model structure** on $\mathbf{Mod}_R$:

> **Weak equivalences** are the **stable equivalences** (maps that are isomorphisms in $\underline{\mathbf{Mod}}_R$).
>
> **Cofibrations** are the **monomorphisms**.
>
> **Fibrations** are the **epimorphisms**.

Since every $0 \to M$ is a monomorphism and every $M \to 0$ is an epimorphism, **every object is bifibrant**, so $\mathrm{Ho}(\mathbf{Mod}_R) = \underline{\mathbf{Mod}}_R$ with no (co)fibrant replacement required.

The **suspension** $\Sigma M$ is the cosyzygy: choose an injective hull $M \hookrightarrow I$ (with $I$ injective = projective) and set $\Sigma M = I/M$. The **loop** $\Omega M$ is the syzygy: choose a projective cover $P \twoheadrightarrow M$ and set $\Omega M = \ker(P \to M)$. These are well-defined functors on $\underline{\mathbf{Mod}}_R$ (independent of the choices up to stable isomorphism by Schanuel's lemma) and are mutually inverse autoequivalences. The **distinguished triangles** are the images of short exact sequences $0 \to M \to E \to N \to 0$, and these make $\underline{\mathbf{Mod}}_R$ a **triangulated category**.

---

# Categorical / Structural Definition

Structurally, $\underline{\mathbf{Mod}}_R$ is an **additive quotient category**: one quotients the abelian category $\mathbf{Mod}_R$ by the ideal of morphisms factoring through the full subcategory of projective-injective objects. This is an instance of the general construction "kill an ideal of morphisms" — the same construction that produces the [[Def - Cylinder Object, Path Object, and Homotopy|homotopy category]] of any [[Def - Model Category|model category]] when the ideal is "homotopic to zero". Indeed, that is the content of the model-structure presentation: in the stable model structure on $\mathbf{Mod}_R$, two maps are [[Def - Cylinder Object, Path Object, and Homotopy|homotopic]] precisely when their difference factors through a projective, so $\operatorname{PHom}$ *is* the "null-homotopic maps" ideal and the abstract homotopy category is the concrete stable category.

The triangulated structure is best seen through the autoequivalence $\Sigma$. A triangulated category is an additive category with a shift autoequivalence and a class of distinguished triangles satisfying the octahedral and related axioms; here the shift is the cosyzygy $\Sigma$, invertible because Frobenius gives projective = injective, and the distinguished triangles come from short exact sequences. The fact that $\Sigma$ is an *equivalence* (not just an endofunctor) is what the word **stable** means: looping and suspending are inverse, so there is no difference between the "spaces" and the "spectra" point of view — the category is its own stabilization.

---

# Relate to Other Fields / Compression

The stable module category is the algebraic, finite-dimensional rehearsal of the **stable homotopy category** of spectra. In topology one must formally invert the suspension functor on pointed spaces (because the topological suspension is not invertible) to obtain spectra and their stable homotopy category; over a Frobenius ring the suspension is *already* invertible, so the stabilization is free. The triangulated structure — distinguished triangles, the octahedral axiom, the long exact sequences — is identical in both settings, which is why $\underline{\mathbf{Mod}}_R$ is the cleanest place to first meet triangulated categories.

It is also the natural home of **Tate cohomology**. For $R = k[G]$ with $G$ finite, $\hat{H}^n(G; M) = \underline{\operatorname{Hom}}(\Omega^n k, M)$ splices ordinary group cohomology (positive degrees) with group homology (negative degrees) across degree zero, with the projective-summand information stripped out — exactly what passing to the stable category does. The compression here: the stable category is "representation theory after discarding the free part", and Tate cohomology is the cohomology you compute there.

**True name:** the operational characterisation is *"work modulo projectives, where projectives are zero and the syzygy is the loop functor"*. When computing in $\underline{\mathbf{Mod}}_R$ you reach for "this map factors through a projective, so it is zero" and "$\Omega$ shifts the triangle", which is this true name applied; the formal quotient-of-hom-groups definition is what you check well-definedness with.

---

# Examples / Corollaries

**Is an instance — a finite group algebra.** For a finite group $G$ and a field $k$ with $\operatorname{char} k \mid |G|$, the group algebra $k[G]$ is a Frobenius ring (indeed a symmetric algebra). Its stable module category $\underline{\mathbf{Mod}}_{k[G]}$ is the central object of modular representation theory; the projective-injective modules are the free summands, and the stable category sees the genuinely modular phenomena (the non-semisimplicity).

**Is an instance — the dual numbers, and exterior algebras.** The ring $k[x]/(x^2)$ is Frobenius: it is self-injective because it is a finite-dimensional commutative Frobenius algebra. More generally any finite-dimensional commutative Frobenius algebra (a Gorenstein Artinian local ring) qualifies, and exterior algebras $\Lambda(V)$ on finite-dimensional $V$ are Frobenius.

**Is an instance — projectives are the zero objects.** For any projective $P$, $\underline{\operatorname{Hom}}(P, M) = 0$ for all $M$ (every map $P \to M$ factors through $P$, which is projective), and similarly $\underline{\operatorname{Hom}}(M, P) = 0$. So $P \cong 0$ in $\underline{\mathbf{Mod}}_R$. This is the defining feature: the stable category is the world where the free part has been collapsed.

**Is NOT an instance — a non-self-injective ring.** The ring $R = k[x]$ of polynomials is *not* Frobenius: it is not self-injective (its injective hull is the field of fractions, much larger than $R$), and projective $\neq$ injective. One can still form the quotient $\operatorname{Hom}/\operatorname{PHom}$, but the syzygy functor is not invertible, so the resulting category is only **pre-triangulated**, not triangulated — the cofiber and fiber sequences fail to coincide. This is the per-condition witness that the Frobenius hypothesis is genuinely needed.

**Is NOT an instance — the integers.** $R = \mathbb{Z}$ is not Frobenius: $\mathbb{Z}$ is projective but not injective over itself (injective $\mathbb{Z}$-modules are the divisible groups, and $\mathbb{Z}$ is not divisible). So there is no stable module category of $\mathbb{Z}$ in this sense; the homotopy theory of $\mathbb{Z}$-modules is instead the derived category $D(\mathbb{Z})$, built from the [[Def - Projective Model Structure on Chain Complexes|projective model structure on chain complexes]].

**Calibration check.** Verify that (i) $\operatorname{PHom}$ is closed under composition on both sides (so the quotient is a category); (ii) a module $P$ is zero in $\underline{\mathbf{Mod}}_R$ if and only if $P$ is projective; and (iii) for $R$ Frobenius, the syzygy $\Omega$ and cosyzygy $\Sigma$ are inverse on $\underline{\mathbf{Mod}}_R$ by exhibiting the short exact sequences $0 \to \Omega M \to P \to M \to 0$ and $0 \to M \to I \to \Sigma M \to 0$ and using projective = injective. If you can do these three, you have understood the construction.

---

# Unlocked by This

> [!tip] Triangulated Categories *(from Homological Algebra)*
> The stable module category is one of the three founding examples of a **triangulated category** (alongside the derived category and the stable homotopy category): an additive category with an invertible shift $\Sigma$ and distinguished triangles satisfying TR1–TR4 including the octahedral axiom. The Frobenius condition is exactly what makes the shift invertible, and Frobenius categories are in fact the standard *source* of triangulated categories (Happel's theorem).

> [!tip] Tate Cohomology and Support Varieties *(from Modular Representation Theory)*
> For $R = k[G]$, the stable category computes **Tate cohomology** $\hat{H}^*(G; M) = \underline{\operatorname{Hom}}(\Omega^* k, M)$, and the geometry of the stable category (its thick subcategories, support varieties) is governed by the spectrum of the cohomology ring — the Benson–Carlson–Rickard theory of stable module categories.

> [!tip] Comodules, Hopf Algebras, and the Adams Spectral Sequence *(from Stable Homotopy Theory)*
> The dual construction for **comodules** over a Hopf algebra carries an analogous stable model structure; for the dual Steenrod algebra this is the algebraic model whose Ext computes the $E_2$-page of the **Adams spectral sequence**, one rung below the model category of **spectra** itself.
