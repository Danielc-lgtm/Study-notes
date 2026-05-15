---
type: definition
subject: group-theory
prereqs:
  - "Def - Homomorphism"
  - "Def - Group"
tags: [algebra, group-theory]
---

# Notation

$\varphi : G \to H$ denotes a [[Def - Homomorphism|homomorphism]]; when it is an isomorphism we still write $\varphi$, and $\varphi^{-1} : H \to G$ for its inverse function. We write $G \cong H$ for "$G$ is isomorphic to $H$". An isomorphism from a group to itself is an **automorphism**, and the set of all of them is $\operatorname{Aut}(G)$. The full symbol registry is on [[Group Theory I — §1.1–1.2]].

---

# Axiom Motivation

When are two groups "the same"? They will never be *literally* identical — the symmetries of an equilateral triangle and the permutations of three labelled objects are built from different stuff, triangle-motions versus shuffles. Yet every group theorist will tell you they are *the same group*, $S_3$. We need to make this precise, because the entire enterprise of *classifying* groups depends on knowing when two groups should be counted as one. The motivating desideratum is: *define an equivalence relation on groups that holds exactly when they have identical group-theoretic structure, differing only in the names of their elements.*

"Identical structure, different names" means there is a perfect dictionary between the two groups: a way to translate each element of $G$ into an element of $H$ and back, such that the translation respects multiplication. A dictionary that is a perfect translation must be (i) a *bijection* — every element of each group has exactly one counterpart, nothing is left untranslated and nothing is translated twice — and (ii) compatible with the operation — the translation of a product is the product of the translations, so that the multiplication tables match up entry for entry. Condition (ii) is exactly the [[Def - Homomorphism|homomorphism]] condition. So the definition is forced: an isomorphism is a *bijective homomorphism*, and two groups are the same when one exists between them.

Why is *bijective homomorphism* exactly right, and not a near variant? Consider weakening. A homomorphism that is injective but not surjective — an *embedding* — exhibits $G$ as a *sub*-group of $H$, not as the same group; $\mathbb{Z}$ embeds in $\mathbb{Q}$ but $\mathbb{Z} \not\cong \mathbb{Q}$. A homomorphism that is surjective but not injective — like a [[Def - Quotient Group|quotient map]] — exhibits $H$ as a *smaller* group than $G$; the map $\mathbb{Z} \to \mathbb{Z}/2\mathbb{Z}$ is a surjective homomorphism but the two groups are wildly different. Drop the homomorphism condition and keep only the bijection: then *any* two groups of the same cardinality would be "the same", which is absurd — $\mathbb{Z}/4\mathbb{Z}$ and the Klein four-group $\mathbb{Z}/2 \times \mathbb{Z}/2$ are both four-element sets but are genuinely different groups (one has an element of order $4$, the other does not), and a mere bijection between them ignores exactly the structure we care about. So *both* conditions are load-bearing, and neither can be dropped.

Could one strengthen — demand more than bijective-homomorphism? There is nothing more to demand, and we can prove it: the set-theoretic inverse $\varphi^{-1}$ of a bijective homomorphism is *automatically* a homomorphism (derived below). So one does not need to separately require that the *inverse* dictionary also respects multiplication; it comes for free. This is the decisive check that the definition is correct. If the inverse were *not* automatically structure-preserving, "isomorphic" would not be a symmetric relation, and "same group" would be incoherent — $G$ same as $H$ but not $H$ same as $G$. The fact that the inverse is free is what makes $\cong$ a genuine equivalence relation, and an equivalence relation is exactly what "sameness" must be.

---

# The Definition

A homomorphism $\varphi : G \to H$ is an **isomorphism** if it is a bijection.

Two groups $G$ and $H$ are **isomorphic**, written $G \cong H$, if there exists an isomorphism between them. Isomorphic groups are regarded as "the same group with the elements relabelled": every group-theoretic statement true of one is true of the other.

**The inverse of an isomorphism is an isomorphism.** If $\varphi : G \to H$ is a bijective homomorphism, its set-theoretic inverse $\varphi^{-1} : H \to G$ is also a homomorphism (and a bijection, so an isomorphism). *Proof:* take $h_1, h_2 \in H$ and write $h_i = \varphi(g_i)$ with $g_i = \varphi^{-1}(h_i)$, possible since $\varphi$ is a bijection. Then, using that $\varphi$ is a homomorphism,
$$\varphi(g_1 g_2) = \varphi(g_1)\,\varphi(g_2) = h_1 h_2.$$
Applying $\varphi^{-1}$ to both ends gives $g_1 g_2 = \varphi^{-1}(h_1 h_2)$, that is,
$$\varphi^{-1}(h_1 h_2) = g_1 g_2 = \varphi^{-1}(h_1)\,\varphi^{-1}(h_2),$$
so $\varphi^{-1}$ preserves the operation. (Contrast linear algebra, where the inverse of a bijective linear map is automatically linear too — the same phenomenon — but unlike, say, continuous maps, where the inverse of a continuous bijection need *not* be continuous. For groups, as for vector spaces, structure-preservation of the inverse is free.)

**Isomorphism is an equivalence relation on groups.** It is *reflexive* ($\mathrm{id}_G : G \to G$ is an isomorphism, so $G \cong G$); *symmetric* (if $\varphi$ witnesses $G \cong H$, then $\varphi^{-1}$ witnesses $H \cong G$ — this is exactly the fact just proved); and *transitive* (if $\varphi : G \to H$ and $\psi : H \to K$ are isomorphisms, the composite $\psi \circ \varphi$ is a bijective homomorphism, so $G \cong K$).

An **automorphism** of $G$ is an isomorphism $G \to G$ — a relabelling of $G$ by itself. The automorphisms of $G$ form a group $\operatorname{Aut}(G)$ under composition, the **automorphism group** of $G$, which is itself a fundamental invariant.

---

# Categorical Definition

In the language of category theory, an isomorphism is exactly an **invertible morphism**. Recall that a category has objects and morphisms (arrows) with an associative composition and identity morphisms; in the category $\mathbf{Grp}$ the objects are groups and the morphisms are [[Def - Homomorphism|homomorphisms]]. A morphism $\varphi : G \to H$ is a *categorical isomorphism* if there is a morphism $\psi : H \to G$ with $\psi \circ \varphi = \mathrm{id}_G$ and $\varphi \circ \psi = \mathrm{id}_H$.

The substance is that this purely categorical notion *coincides* with "bijective homomorphism". If $\varphi$ has a two-sided inverse $\psi$ in $\mathbf{Grp}$, then $\psi$ is in particular a set-theoretic inverse, so $\varphi$ is a bijection. Conversely — and this is where the lemma above earns its keep — if $\varphi$ is a bijective homomorphism, its set-theoretic inverse $\varphi^{-1}$ is *automatically a homomorphism*, hence a genuine morphism in $\mathbf{Grp}$, providing the categorical inverse. So in $\mathbf{Grp}$ the categorical isomorphisms are precisely the bijective homomorphisms. This is *not* automatic in every category: in the category of topological spaces, a continuous bijection need not have a continuous inverse, so categorical isomorphisms (homeomorphisms) are strictly fewer than bijective morphisms. The clean coincidence for groups is a small piece of good fortune that makes "isomorphic" easy to check — find a bijective homomorphism and you are done.

This viewpoint also explains why $\cong$ is *the* equivalence relation of the subject: isomorphism is the intrinsic notion of sameness in *any* category, and "classify the objects" universally means "list them up to isomorphism".

---

# Relate to Other Fields / Compression

Isomorphism is the group instance of the universal pattern *structure-preserving bijection with structure-preserving inverse*, present in every mathematical category. A ring isomorphism is a bijective ring homomorphism; a *linear isomorphism* is a bijective linear map (an invertible matrix, up to choice of basis); a homeomorphism is a continuous bijection with continuous inverse; a diffeomorphism is the smooth version. In each category, "isomorphic" is the equivalence relation under which classification is conducted, and the objects of the field are studied only up to isomorphism. The group case is representative; the one subtlety, noted above, is that for groups (as for vector spaces and rings) the inverse map is automatically structure-preserving, whereas for topological spaces it is not — so for groups the definition can be stated as "bijective homomorphism" without separately insisting on the inverse.

The conceptual compression: an isomorphism is a proof that two descriptions are descriptions of *one object*. The symmetries of a triangle and the permutations of $\{1,2,3\}$ are the *same group* $S_3$ presented two ways; $\mathbb{R}^n$ and the space of degree-$<n$ polynomials are the *same vector space* presented two ways. To say $G \cong H$ is to say: every group-theoretic question has the same answer for $G$ and $H$, so they may be freely substituted. An *isomorphism invariant* — order, abelianness, the multiset of element orders, the [[Thm - Composition Series|composition factors]] — is any quantity that cannot tell isomorphic groups apart; the art of classification is finding enough invariants to tell *non*-isomorphic groups apart.

---

# Examples / Corollaries

**Is an instance — $(\mathbb{R}, +) \cong (\mathbb{R}_{>0}, \times)$.** The exponential $\varphi(x) = e^x$ is a bijection from the reals onto the positive reals, and $e^{x+y} = e^x e^y$ makes it a homomorphism from $(\mathbb{R},+)$ to $(\mathbb{R}_{>0},\times)$. Its inverse is the logarithm, automatically a homomorphism: $\log(ab) = \log a + \log b$. Two groups that look entirely different — one additive, one multiplicative — are the *same group*.

**Is an instance — every cyclic group of order $n$ is isomorphic to $\mathbb{Z}/n\mathbb{Z}$.** Any group generated by a single element $g$ of order $n$ is isomorphic to $\mathbb{Z}/n\mathbb{Z}$ via $g^k \mapsto k + n\mathbb{Z}$. So "cyclic of order $n$" describes *one* group up to isomorphism — which is why we may speak of *the* cyclic group $C_n$.

**Is an instance — automorphisms, e.g. conjugation.** For any fixed $a \in G$, the map $\varphi_a(x) = a x a^{-1}$ is an automorphism of $G$ (it is a bijection with inverse $\varphi_{a^{-1}}$, and $\varphi_a(xy) = axya^{-1} = (axa^{-1})(aya^{-1}) = \varphi_a(x)\varphi_a(y)$). These *inner automorphisms* are isomorphisms of $G$ with itself; complex conjugation $z \mapsto \bar z$ is similarly an automorphism of $(\mathbb{C}, +)$.

**Is NOT an instance — $\mathbb{Z}/4\mathbb{Z}$ versus $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$.** Both are groups of order $4$, so a *bijection* between them certainly exists — but no *isomorphism* does. The cyclic group $\mathbb{Z}/4\mathbb{Z}$ has an element of order $4$; in $\mathbb{Z}/2 \times \mathbb{Z}/2$ every non-identity element has order $2$. Since an isomorphism preserves element orders, none can exist. This is the canonical demonstration that bijection alone is not enough — the homomorphism condition is doing real work.

**Is NOT an instance — a surjective homomorphism need not be an isomorphism.** The [[Def - Quotient Group|quotient map]] $\mathbb{Z} \to \mathbb{Z}/2\mathbb{Z}$ is a homomorphism and is surjective, yet $\mathbb{Z} \not\cong \mathbb{Z}/2\mathbb{Z}$ (one is infinite, the other has two elements). It fails injectivity. Likewise the embedding $\mathbb{Z} \hookrightarrow \mathbb{Q}$ is an injective homomorphism but not an isomorphism — it fails surjectivity. *Both* halves of bijectivity are needed.

**Corollary — isomorphism preserves every group-theoretic invariant.** If $G \cong H$ then $|G| = |H|$, $G$ is abelian iff $H$ is, $G$ and $H$ have the same number of elements of each order, the same subgroup lattice up to relabelling, isomorphic centres, isomorphic automorphism groups, and the same [[Thm - Composition Series|composition factors]]. The *contrapositive* is the practical tool: to prove $G \not\cong H$, exhibit a single invariant on which they differ.

**Corollary — the first isomorphism theorem produces isomorphisms.** The [[Thm - First Isomorphism Theorem|first isomorphism theorem]] asserts $G/\ker\varphi \cong \operatorname{im}\varphi$; it is the principal *manufacturer* of isomorphisms in the subject. To prove $G/N \cong Q$ one builds a surjective homomorphism $G \to Q$ with kernel $N$ — never a bare bijection.

**Calibration check.** Reproduce the proof that the inverse of a bijective homomorphism is a homomorphism. Confirm that $\cong$ is reflexive, symmetric, and transitive. If you can explain why a bijection between $\mathbb{Z}/4\mathbb{Z}$ and $\mathbb{Z}/2 \times \mathbb{Z}/2$ exists but no isomorphism does, you have understood why *both* conditions in the definition are indispensable.

---

# Unlocked by This

> [!tip] Classification of Groups *(from Group Theory III)*
> To *classify* groups means to enumerate them up to isomorphism — for instance, the [[Group Theory III — §1.5–1.7|classification of finitely generated abelian groups]], or listing all groups of a given order. Isomorphism is the precise equivalence relation that makes "how many groups of order $n$ are there?" a well-posed question.

> [!tip] The Isomorphism Theorems *(from this topic)*
> The first, second, and third isomorphism theorems are all assertions that two specific groups are *isomorphic*. The notion defined here is the conclusion every one of them delivers; see [[Thm - First Isomorphism Theorem]].

> [!tip] Automorphism Groups and the Semidirect Product *(from Group Theory III)*
> The automorphisms of $G$ form the group $\operatorname{Aut}(G)$, and homomorphisms into $\operatorname{Aut}(N)$ are the data of a semidirect product $N \rtimes H$ — the construction that solves part of the extension problem.
