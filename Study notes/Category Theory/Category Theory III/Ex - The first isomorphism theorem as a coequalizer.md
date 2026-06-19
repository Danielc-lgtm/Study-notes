---
type: exercise
subject: category-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Equalizer and Coequalizer"
  - "Def - Pullback and Pushout"
  - "Thm - First Isomorphism Theorem"
  - "Def - Quotient Group"
tags: [category-theory, foundations]
---

# Problem Statement

Reinterpret the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] categorically. Let $\varphi : G \to H$ be a group homomorphism. Show that the quotient map $G \to G/\ker\varphi$ is a [[Def - Equalizer and Coequalizer|coequalizer]] — specifically, the coequalizer of the two projections of the **kernel pair** $G \times_H G \rightrightarrows G$ — and that the induced map $G/\ker\varphi \to \mathrm{im}\,\varphi$ is an isomorphism. Conclude that every homomorphism factors as a coequalizer (regular epimorphism) followed by a monomorphism, and that this image factorisation is the categorical content of the first isomorphism theorem.

**Recall:**

![[Thm - First Isomorphism Theorem#Statement]]

The **kernel pair** of $\varphi : G \to H$ is the [[Def - Pullback and Pushout|pullback]] $G \times_H G = \{(g, g') : \varphi(g) = \varphi(g')\}$ with its two projections $p_1, p_2 : G \times_H G \rightrightarrows G$. A **coequalizer** of $p_1, p_2$ is the universal map out of $G$ identifying $p_1$ and $p_2$.

---

# Convergent Strategy

**Problem class:** This is a "translate a classical theorem into universal-property language" problem at the hardest tier, because it requires recognising the quotient map as a colimit and the whole first isomorphism theorem as an image factorisation. The routine: identify the kernel pair, show its coequalizer is the quotient, and check the induced comparison is iso.

**Assumption pattern:** The structural assumption is that $\mathbf{Grp}$ is a category where every homomorphism has a kernel pair (a pullback) and a coequalizer (a quotient), and where these interact via "the coequalizer of the kernel pair is the quotient by the kernel". Recognising that "identify exactly the elements with the same image" is the kernel-pair coequalizer is the unlocking step.

**Theorem routing:** The route is: kernel pair $G \times_H G = \{(g,g') : \varphi(g) = \varphi(g')\}$ is the equivalence relation "same image under $\varphi$"; its [[Def - Equalizer and Coequalizer|coequalizer]] is $G$ modulo that relation $= G/\ker\varphi$ (the relation $\varphi(g) = \varphi(g')$ is $g^{-1}g' \in \ker\varphi$, i.e. same coset). The [[Thm - First Isomorphism Theorem|first isomorphism theorem]] supplies the iso $G/\ker\varphi \cong \mathrm{im}\,\varphi$. The factorisation $G \twoheadrightarrow G/\ker\varphi \cong \mathrm{im}\,\varphi \hookrightarrow H$ is (regular epi)-then-mono.

**Key decision point:** The deep choice is identifying *which* parallel pair to coequalize. The quotient $G/\ker\varphi$ is the coequalizer of the kernel-pair projections $p_1, p_2 : G \times_H G \rightrightarrows G$ — the two ways of extracting an element from a "same-image" pair — not the coequalizer of some pair into $G$ from the kernel as a subgroup. The insight is that the *relation* (kernel pair), not the *subgroup* (kernel), is the input to the coequalizer; the kernel is recovered as the fibre over the identity.

---

# Legal Operations Used

1. **Form the kernel pair as a pullback (from the topic page: pullback of $\varphi$ with itself).** $G \times_H G$ is the equivalence relation "same image", the input to the coequalizer.

2. **Coequalize the kernel pair to get the quotient (operation: quotient $=$ coequalizer).** The coequalizer of $p_1, p_2$ collapses $G$ by "same image", which is $G/\ker\varphi$.

3. **Invoke the first isomorphism theorem to identify the coequalizer with the image (operation: apply [[Thm - First Isomorphism Theorem]]).** The induced comparison $G/\ker\varphi \to \mathrm{im}\,\varphi$ is an isomorphism, completing the (epi, mono) factorisation.

---

# Hints

> [!note]- Hint 1
> The kernel pair $G \times_H G$ encodes the relation "$g$ and $g'$ have the same image under $\varphi$". What quotient of $G$ universally forces $p_1 = p_2$, i.e. identifies $g$ with $g'$ whenever $\varphi(g) = \varphi(g')$?

> [!note]- Hint 2
> $\varphi(g) = \varphi(g') \iff \varphi(g^{-1}g') = e \iff g^{-1}g' \in \ker\varphi \iff g\ker\varphi = g'\ker\varphi$. So "same image" is "same coset of $\ker\varphi$", and the coequalizer is $G/\ker\varphi$.

> [!note]- Hint 3
> The coequalizer map $q : G \to G/\ker\varphi$ satisfies $qp_1 = qp_2$ and is universal. The [[Thm - First Isomorphism Theorem|first isomorphism theorem]] then gives the iso to $\mathrm{im}\,\varphi$.

> [!note]- Hint 4
> Assemble the factorisation: $G \xrightarrow{q} G/\ker\varphi \xrightarrow{\cong} \mathrm{im}\,\varphi \hookrightarrow H$. The first map is a coequalizer (regular epi), the last a mono. This *is* the first isomorphism theorem.

---

# Solution

The plan: identify the kernel pair as the "same image" relation, show its coequalizer is the quotient $G/\ker\varphi$ (because "same image" equals "same coset"), invoke the first isomorphism theorem to identify this quotient with $\mathrm{im}\,\varphi$, and read off the (regular epi, mono) factorisation as the categorical form of the theorem.

**Step 1: The kernel pair is the "same image" equivalence relation.**

> [!note]- Derivation
> The kernel pair is the [[Def - Pullback and Pushout|pullback]] of $\varphi$ with itself: $G \times_H G = \{(g,g') \in G \times G : \varphi(g) = \varphi(g')\}$, with projections $p_1(g,g') = g$, $p_2(g,g') = g'$. This is exactly the equivalence relation "$g \sim g'$ iff $\varphi(g) = \varphi(g')$" on $G$, presented as a subobject of $G \times G$.

**Step 2: The coequalizer of the kernel pair is $G/\ker\varphi$.**

> [!note]- Derivation
> A homomorphism $z : G \to X$ satisfies $z p_1 = z p_2$ iff $z(g) = z(g')$ whenever $\varphi(g) = \varphi(g')$. Now $\varphi(g) = \varphi(g') \iff \varphi(g^{-1}g') = e \iff g^{-1}g' \in \ker\varphi \iff g\ker\varphi = g'\ker\varphi$. So the condition is "$z$ is constant on cosets of $\ker\varphi$", i.e. $z$ factors through the [[Def - Quotient Group|quotient]] $q : G \to G/\ker\varphi$. The factorisation is unique. Hence $q : G \to G/\ker\varphi$ is the [[Def - Equalizer and Coequalizer|coequalizer]] of $p_1, p_2$.

**Step 3: The first isomorphism theorem identifies the coequalizer with the image.**

> [!note]- Derivation
> By the [[Thm - First Isomorphism Theorem|first isomorphism theorem]], the map $\bar\varphi : G/\ker\varphi \to \mathrm{im}\,\varphi$, $g\ker\varphi \mapsto \varphi(g)$, is a well-defined isomorphism. Thus the coequalizer object $G/\ker\varphi$ is isomorphic to $\mathrm{im}\,\varphi$, and $\varphi$ factors as
> $$G \xrightarrow{\ q\ } G/\ker\varphi \xrightarrow{\ \cong\ } \mathrm{im}\,\varphi \xhookrightarrow{\ } H.$$

**Step 4: This is the (regular epi, mono) image factorisation.**

> [!note]- Derivation
> The map $q$ is a coequalizer, hence a **regular epimorphism**; the inclusion $\mathrm{im}\,\varphi \hookrightarrow H$ is a [[Def - Equalizer and Coequalizer|monomorphism]] (an injective homomorphism). So every homomorphism $\varphi$ factors as a regular epi followed by a mono, and the middle object is the image. The categorical content of the first isomorphism theorem is precisely: *$\mathbf{Grp}$ has (regular epi, mono) factorisations, and the image of $\varphi$ is the coequalizer of its kernel pair*. This makes $\mathbf{Grp}$ a **regular category**.

> [!note]- Complete formal solution
> Let $\varphi : G \to H$. The kernel pair $G \times_H G = \{(g,g') : \varphi(g) = \varphi(g')\}$ (the pullback of $\varphi$ with itself) carries projections $p_1, p_2$ and is the relation "same image". A homomorphism $z : G \to X$ coequalizes $p_1, p_2$ iff $z(g) = z(g')$ whenever $\varphi(g) = \varphi(g')$, i.e. iff $z$ is constant on cosets of $\ker\varphi$ (using $\varphi(g) = \varphi(g') \iff g^{-1}g' \in \ker\varphi \iff g\ker\varphi = g'\ker\varphi$), i.e. iff $z$ factors uniquely through $q : G \to G/\ker\varphi$. Hence $q$ is the [[Def - Equalizer and Coequalizer|coequalizer]] of the kernel pair. By the [[Thm - First Isomorphism Theorem|first isomorphism theorem]], $G/\ker\varphi \cong \mathrm{im}\,\varphi$, so $\varphi = (\mathrm{im}\,\varphi \hookrightarrow H) \circ (\cong) \circ q$ is a regular epi followed by a mono. This (regular epi, mono) image factorisation, with the image realised as the coequalizer of the kernel pair, is the categorical statement of the first isomorphism theorem. $\blacksquare$

---

# Key Takeaways

**The first isomorphism theorem is "every map factors as a quotient then an injection", and the quotient is a coequalizer.** The reusable reframing is that the classical statement $G/\ker\varphi \cong \mathrm{im}\,\varphi$ is, categorically, the existence of an image factorisation $\varphi = m \circ e$ with $e$ a regular epimorphism (a coequalizer) and $m$ a monomorphism. This dissolves the apparent specialness of the theorem to groups: the *same* factorisation exists in rings, modules, sets, and any **regular category**, because it follows from "coequalize the kernel pair, then include the image". The trigger to recognise: whenever a category has kernel pairs (pullbacks) and their coequalizers, every morphism has a canonical (epi, mono) factorisation, and the first-isomorphism-theorem shape is automatic.

**The input to the quotient is the kernel pair (a relation), not the kernel (a subgroup) — relations coequalize, subobjects equalize.** The hard conceptual move is realising that the coequalizer takes as input the *equivalence relation* $G \times_H G$ — the two projections $p_1, p_2$ — rather than the kernel subgroup. The kernel pair is the categorical avatar of "same image", and quotienting by it is quotienting by that relation; the kernel subgroup is recovered as the fibre of the kernel pair over the identity. This relation/subobject duality (kernel pair coequalizes to the quotient; kernel equalizes as a subobject) is the precise categorical bookkeeping behind "quotient by a normal subgroup", and it is what makes effective equivalence relations the defining feature of **exact categories**. See [[Ex - The kernel as a pullback]] for the complementary "kernel as pullback against the basepoint".

**"Same image" equals "same coset" is the bridge that turns a set-level relation into the group-theoretic quotient.** The computational heart is the chain $\varphi(g) = \varphi(g') \iff g^{-1}g' \in \ker\varphi \iff g\ker\varphi = g'\ker\varphi$, which identifies the kernel pair's equivalence classes with the cosets of $\ker\varphi$. This is why the coequalizer — a priori a set-level quotient by a generated equivalence relation — lands exactly on the group quotient $G/\ker\varphi$ with no extra normalisation needed: the relation "same image" is *already* the coset relation, which is already a congruence. The transferable diagnostic is that when a coequalizer is taken of a kernel pair (rather than an arbitrary pair), the generated equivalence relation is automatically the right congruence, so the quotient is clean — this is the categorical reason kernel pairs are "effective" and is the seed of the [[Thm - Representable Functors Preserve Limits|representable]] / regular-category formalism that underlies descent and the internal logic of a topos.
