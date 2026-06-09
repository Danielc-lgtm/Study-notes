---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Module"
  - "Def - Submodule"
  - "Def - Module Homomorphism"
  - "Def - Quotient Module"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$; modules are unital. Let $R$ be a ring. We write $f : M \to N$ for an [[Def - Module Homomorphism|R-linear map]] (a homomorphism of $R$-modules), $\ker f = \{m \in M : f(m) = 0\} \subseteq M$ for its kernel, and $\operatorname{im} f = f(M) \subseteq N$ for its image; both are [[Def - Submodule|submodules]]. The symbol $0$ denotes the zero module, and an arrow $0 \to M$ or $M \to 0$ is the unique (zero) map. We write $\xrightarrow{f}$ to label an arrow by the map $f$, $i$ for an injection (often $\hookrightarrow$), and $p$ for a surjection (often $\twoheadrightarrow$). The full registry is on [[Commutative Algebra I — Chain Conditions]].

This is a compound page: it defines two interlocking notions — the **exact sequence** (the general bookkeeping of "image equals kernel at every spot") and the **short exact sequence** (the three-term special case that packages "$M$ is built from a submodule $N$ and the quotient $M/N$") — because the short exact sequence is the case of overwhelming importance and is unintelligible without the general definition that frames it.

---

# Axiom Motivation

The goal is a single piece of notation that records, compactly and composably, how modules and maps fit together — in particular how a module decomposes into a submodule and a quotient. The notion you are inventing, *exactness*, is the condition "image equals kernel", and the reason it is the right condition is that it simultaneously expresses injectivity, surjectivity, and "$L$ is exactly the quotient $M/N$", in one uniform language that chains together.

**Why "image equals kernel" and not merely "image inside kernel".** Start with two composable maps $M_0 \xrightarrow{f} M_1 \xrightarrow{g} M_2$. The weakest interesting compatibility is $g \circ f = 0$, i.e. $\operatorname{im} f \subseteq \ker g$ — "what $f$ produces, $g$ destroys". This is the condition that defines a *chain complex*, and it is genuinely useful, but it loses information: it does not record *how much* of $\ker g$ is hit by $f$. **Exactness** strengthens it to the equality $\operatorname{im} f = \ker g$, which says $f$ hits *all* of $\ker g$ — nothing in the kernel of $g$ is missed by $f$. The reason to demand equality rather than inclusion is that equality is exactly what makes the sequence *lossless*: the failure of exactness (the quotient $\ker g / \operatorname{im} f$, the *homology* at that spot) is precisely the information an exact sequence promises is zero. If you only ask for inclusion you are doing homological algebra and measuring the gap; if you ask for equality you are asserting the gap vanishes, and that assertion is what lets you read off isomorphisms.

**Why exactness encodes injectivity and surjectivity as boundary cases.** The genius of the definition is that the same condition, applied at a terminal spot, recovers the two basic properties of a map — which is what makes the notation uniform. Place a zero module at the left end: in $0 \to M \xrightarrow{f} N$, exactness at $M$ says $\operatorname{im}(0 \to M) = \ker f$, and the image of the zero map is $\{0\}$, so $\ker f = 0$ — **$f$ is injective**. Dually, place a zero at the right: in $M \xrightarrow{g} N \to 0$, exactness at $N$ says $\operatorname{im} g = \ker(N \to 0) = N$ — **$g$ is surjective**. So "injective" and "surjective" are not separate axioms bolted on; they are exactness against a zero module, which is exactly why the three-term sequence $0 \to N \to M \to L \to 0$ can say "injective, surjective, and image-equals-kernel" all at once with no extra words.

**Why the short exact sequence is the case that matters, and what its three conditions force.** Specialise to $0 \to N \xrightarrow{i} M \xrightarrow{p} L \to 0$. Exactness at the three internal spots forces, in order: at $N$, that $i$ is injective; at $L$, that $p$ is surjective; at $M$, that $\operatorname{im} i = \ker p$. Unwind the consequences. Since $i$ is injective, $N \cong i(N)$, so $N$ is (a copy of) a submodule of $M$. Since $p$ is surjective with kernel $i(N)$, the [[Thm - Isomorphism Theorems for Modules|first isomorphism theorem]] gives $L = \operatorname{im} p \cong M/\ker p = M/i(N)$. So a short exact sequence is *exactly the same data* as "a submodule $N \subseteq M$ together with the identification $L = M/N$": the left term is the sub, the right term is the quotient, and $M$ in the middle is the *extension* glueing them. This is why one phrase — "$M$ is an extension of $L$ by $N$" — captures every situation where a module sits between a sub and a quotient, and it is the reason the next theorem about chain conditions can be stated once, for the whole sequence, instead of separately for subs and quotients.

**Why the end maps are forced to be zero, and why that is a feature.** In $0 \to N \xrightarrow{i} M$, the only map $0 \to N$ is the zero map, and likewise $L \to 0$ is zero; these are not choices but the unique arrows in and out of the zero module. The value of insisting on the zero modules at the ends is purely notational economy: they turn "injective" and "surjective" into instances of the *single* condition "exact", so that a reader scanning $0 \to N \to M \to L \to 0$ knows, with no further annotation, that the first nonzero map is monic, the last is epic, and the inner spot glues them. The definition was engineered so that one symbol stream carries all three facts.

---

# The Definition

Let $R$ be a ring.

## Exact sequence

A sequence of $R$-modules and $R$-linear maps
$$\cdots \longrightarrow M_{i-1} \xrightarrow{\;f_i\;} M_i \xrightarrow{\;f_{i+1}\;} M_{i+1} \longrightarrow \cdots$$
(finite or infinite) is **exact at $M_i$** if
$$\operatorname{im} f_i = \ker f_{i+1}.$$
The sequence is **exact** if it is exact at every internal module $M_i$ (every spot that has both an incoming and an outgoing map).

In particular, for a single map $f : M \to N$:
- $0 \to M \xrightarrow{f} N$ is exact (at $M$) $\iff$ $f$ is injective;
- $M \xrightarrow{f} N \to 0$ is exact (at $N$) $\iff$ $f$ is surjective;
- $0 \to M \xrightarrow{f} N \to 0$ is exact $\iff$ $f$ is an isomorphism.

## Short exact sequence

A **short exact sequence** (SES) is an exact sequence of the form
$$0 \longrightarrow N \xrightarrow{\;i\;} M \xrightarrow{\;p\;} L \longrightarrow 0.$$
Exactness at the three internal spots is equivalent to the conjunction:

1. $i$ is **injective** (exactness at $N$);
2. $p$ is **surjective** (exactness at $L$);
3. $\operatorname{im} i = \ker p$ (exactness at $M$).

Consequently $N \cong i(N)$ is a submodule of $M$, and $L \cong M/i(N)$ is the corresponding [[Def - Quotient Module|quotient]] (by [[Thm - Isomorphism Theorems for Modules|the first isomorphism theorem]]). One says **$M$ is an extension of $L$ by $N$**. The maps $0 \to N$ and $L \to 0$ are necessarily the zero maps.

---

# Categorical / Structural Definition

Exactness is a condition on a *sequence in an abelian category*, and modules over $R$ form the prototypical abelian category. In any such category, every morphism $f$ has a kernel and an image (a monomorphism through which $f$ factors with a cokernel-zero condition), and "$\operatorname{im} f_i = \ker f_{i+1}$" is the statement that two subobjects of $M_i$ coincide. A short exact sequence $0 \to N \to M \to L \to 0$ is then precisely the data exhibiting $N$ as the kernel of $p$ and $L$ as the cokernel of $i$:
$$N = \ker p, \qquad L = \operatorname{coker} i = M / \operatorname{im} i.$$
This is the abstract reason short exact sequences are the *atoms* of homological algebra: every map factors as $M \twoheadrightarrow \operatorname{im} f \hookrightarrow N$, giving two short exact sequences $0 \to \ker f \to M \to \operatorname{im} f \to 0$ and $0 \to \operatorname{im} f \to N \to \operatorname{coker} f \to 0$, and any long exact sequence is assembled by splicing these. A short exact sequence **splits** if $M \cong N \oplus L$ compatibly with $i$ and $p$ — the case where the extension is trivial — but exactness alone does not force splitting; that is the difference between $0 \to \mathbb{Z} \xrightarrow{\times 2} \mathbb{Z} \to \mathbb{Z}/2 \to 0$ (non-split) and $0 \to \mathbb{Z} \to \mathbb{Z}^2 \to \mathbb{Z} \to 0$ (split).

---

# Relate to Other Fields / Compression

The cleanest compression: **a short exact sequence is the categorical statement "$N$ is the kernel, $L$ is the cokernel, $M$ is the extension between them" — it is the universal way to say a module decomposes into a sub and a quotient.** Everywhere a structure has subobjects and quotients, short exact sequences appear: in group theory $1 \to N \to G \to Q \to 1$ records a normal subgroup and its quotient (the multiplicative notation reflecting non-abelian groups), in topology $0 \to H_n(A) \to H_n(X) \to H_n(X, A) \to \cdots$ records a subspace's homology, in vector spaces $0 \to \ker f \to V \to \operatorname{im} f \to 0$ *is* the rank–nullity theorem.

**True name:** for problem-solving, the operational meaning of a short exact sequence is **"$N$ is a submodule of $M$ and $L = M/N$"** — whenever you see one, immediately identify which module is the sub, which is the quotient, and which is the extension; whenever you have a submodule, immediately write down its short exact sequence. The whole utility of the notation is that conservation laws (chain conditions, length, Euler characteristics) hold across it.

In homological algebra exactness is the condition under which the **snake lemma**, the **long exact sequence of a pair**, and **derived functors** operate; the failure of a left- or right-exact functor to preserve a short exact sequence is precisely what the $\operatorname{Tor}$ and $\operatorname{Ext}$ groups measure. In linear algebra a short exact sequence of vector spaces *always* splits and reduces to dimension addition $\dim M = \dim N + \dim L$ — the degenerate case where extensions are trivial. The genuinely interesting content of the notion lives over rings, where extensions need not split.

---

# Examples / Corollaries

**Is an instance — the canonical sequence of a submodule.** For any submodule $N \subseteq M$, the sequence
$$0 \longrightarrow N \xrightarrow{\;\subseteq\;} M \xrightarrow{\;\text{quot}\;} M/N \longrightarrow 0$$
is short exact: the inclusion is injective, the quotient map is surjective, and its kernel is exactly $N$. This is the *universal* short exact sequence — every short exact sequence is isomorphic to one of this form, with $N$ replaced by $i(N)$. It is the form to write down the instant any submodule appears.

**Is an instance — multiplication by $2$ on $\mathbb{Z}$.** The sequence $0 \to \mathbb{Z} \xrightarrow{\times 2} \mathbb{Z} \xrightarrow{\bmod 2} \mathbb{Z}/2 \to 0$ is short exact: $\times 2$ is injective (the integers have no $2$-torsion), its image is $2\mathbb{Z} = \ker(\bmod 2)$, and reduction mod $2$ is surjective. This exhibits $\mathbb{Z}$ as a non-split extension of $\mathbb{Z}/2$ by $\mathbb{Z}$ — note $\mathbb{Z} \not\cong \mathbb{Z} \oplus \mathbb{Z}/2$, since the left side is torsion-free, so exactness does *not* imply splitting.

**Is an instance (longer) — rank–nullity.** For an $R$-linear $f : M \to N$, the sequence $0 \to \ker f \to M \xrightarrow{f} \operatorname{im} f \to 0$ is short exact by definition of kernel and image. Over a field this is rank–nullity; over a general ring it is the universal factorisation of $f$ through its image.

**Is NOT an instance — a chain complex with non-zero homology.** The sequence $0 \to \mathbb{Z} \xrightarrow{\times 2} \mathbb{Z} \to 0$ (no quotient term) satisfies $\operatorname{im}(0 \to \mathbb{Z}) = 0 \subseteq \ker(\times 2) = 0$, so it is exact at the first $\mathbb{Z}$; but at the second $\mathbb{Z}$, $\operatorname{im}(\times 2) = 2\mathbb{Z} \neq \mathbb{Z} = \ker(\mathbb{Z} \to 0)$, so it is **not** exact there — the homology $\mathbb{Z}/2\mathbb{Z}$ is non-zero. This probes the difference between "complex" ($\operatorname{im} \subseteq \ker$) and "exact" ($\operatorname{im} = \ker$).

**Is NOT a short exact sequence — $0 \to \mathbb{Z} \xrightarrow{\times 2} \mathbb{Z} \to \mathbb{Z}/3 \to 0$ with the obvious maps.** If the last map were the surjection $\mathbb{Z} \twoheadrightarrow \mathbb{Z}/3$, then $\ker(\mathbb{Z} \to \mathbb{Z}/3) = 3\mathbb{Z}$, but $\operatorname{im}(\times 2) = 2\mathbb{Z} \neq 3\mathbb{Z}$, so exactness at the middle fails. This probes that the three terms cannot be glued arbitrarily — the middle exactness condition $\operatorname{im} i = \ker p$ is a genuine constraint linking the two maps.

**Calibration check.** Verify that $0 \to M \xrightarrow{f} N$ exact $\iff$ $f$ injective, and $M \xrightarrow{f} N \to 0$ exact $\iff$ $f$ surjective, directly from "image of the zero map is $\{0\}$" and "kernel of the zero map is everything". Confirm that in any short exact sequence $0 \to N \to M \to L \to 0$ you can read off $L \cong M/i(N)$ via the first isomorphism theorem. If you can write down, from memory, the short exact sequence attached to an arbitrary submodule and the non-split example $0 \to \mathbb{Z} \xrightarrow{\times 2} \mathbb{Z} \to \mathbb{Z}/2 \to 0$, you have understood the definition.

---

# Unlocked by This

> [!tip] The long exact sequence and derived functors *(from Homological Algebra)*
> Splicing short exact sequences produces **long exact sequences**, and applying a functor that is only *left-* or *right-exact* (such as $\operatorname{Hom}$ or $\otimes$) to a short exact sequence produces a sequence that fails exactness at one end. The measure of that failure is a sequence of **derived functors** — $\operatorname{Ext}$ for $\operatorname{Hom}$, $\operatorname{Tor}$ for $\otimes$ — assembled into a long exact sequence by the snake lemma. This is the entire engine of homological algebra; the notion of [[Def - Flat Module|flatness]] (Commutative Algebra III) is exactly "tensoring preserves short exact sequences".

> [!tip] Group extensions and $H^2$ *(from Group Cohomology)*
> The non-abelian analogue $1 \to N \to G \to Q \to 1$ is a **group extension**, and the classification of extensions of $Q$ by an abelian $N$ (with fixed action) is the second cohomology group $H^2(Q, N)$. The failure of a short exact sequence to split is a cohomology class; this is the prototype of every obstruction theory.

> [!tip] The splitting lemma and projective modules *(from Commutative Algebra)*
> A short exact sequence $0 \to A \to B \to C \to 0$ **splits** ($B \cong A \oplus C$) if and only if there is a section $s : C \to B$ with $p \circ s = \operatorname{id}_C$, if and only if there is a retraction $r : B \to A$ with $r \circ i = \operatorname{id}_A$. When $C$ is [[Def - Projective Module|projective]] every such sequence splits — this is one characterisation of projectivity, developed in Commutative Algebra III.
