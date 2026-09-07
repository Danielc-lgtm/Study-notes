---
type: definition
subject: algebraic-topology
prereqs:
  - "Def - Covering Space"
  - "Def - Deck Transformation Group"
  - "Def - Normal Subgroup"
tags: [geometry, algebraic-topology, topology]
---

# Notation

$p : \tilde X \to X$ is a [[Def - Covering Space|covering map]] with $\tilde X$ connected. $\mathrm{Deck}(\tilde X / X)$ is the [[Def - Deck Transformation Group|deck transformation group]]. $p_* : \pi_1(\tilde X, \tilde x_0) \to \pi_1(X, x_0)$ is the induced map on fundamental groups (always injective for a covering — see Examples). See [[Algebraic Topology II — Fundamental Group and Covering Spaces]] for the full registry.

---

# Axiom Motivation

Not every cover is symmetric. The cover $\mathbb{R} \to S^1$ has a deck group $\mathbb{Z}$ that acts transitively on each fibre — every fibre point can be moved to every other by a deck transformation. By contrast, a cover corresponding to a non-normal subgroup of $\pi_1$ has fewer deck transformations than fibre points, and the deck group fails to act transitively. The **regular** (or **Galois**) covers are precisely the symmetric ones: the deck group acts transitively on each fibre, and the cover is its own "Galois closure."

The condition is exactly the analogue of normality in field theory. In Galois theory, a finite extension $L/K$ is **Galois** (= normal + separable) when the Galois group acts transitively on the roots of any minimal polynomial; equivalently, $L$ is the splitting field of some polynomial over $K$; equivalently, $L^{\mathrm{Gal}(L/K)} = K$ (fixed field is the base field). In covering theory, $\tilde X \to X$ is regular when the deck group acts transitively on each fibre; equivalently, the subgroup $p_*\pi_1(\tilde X) \leq \pi_1(X)$ is normal; equivalently, $\tilde X / \mathrm{Deck}(\tilde X / X) = X$ (quotient by deck group is the base). The three characterisations are exactly parallel.

Why does normality of the subgroup encode this? Under the [[Thm - Galois Correspondence for Covering Spaces|Galois correspondence]], a cover $\tilde X \to X$ at a chosen base point corresponds to a subgroup $H = p_*\pi_1(\tilde X) \leq \pi_1(X)$. Changing the base point in $\tilde X$ to another point in the same fibre conjugates $H$ by an element of $\pi_1(X)$. So the cover-up-to-base-point-change corresponds to a *conjugacy class* of subgroups. The cover is "intrinsically" defined (not dependent on a base-point choice) precisely when all conjugates of $H$ equal $H$ — i.e., when $H$ is normal. So normal subgroups are the ones whose covers are "base-point free", and these are the regular covers.

Three equivalent characterisations of regularity:
1. **Deck group acts transitively on each fibre.** Most operational.
2. **$p_*\pi_1(\tilde X) \leq \pi_1(X)$ is normal.** Most algebraic.
3. **The cover is the same regardless of which fibre point you choose as base.** Most conceptual.

When the cover is regular, the deck group equals the quotient $\pi_1(X) / p_*\pi_1(\tilde X)$ — that is, the quotient is well-defined because the subgroup is normal, and it gives the Galois group of the cover. The universal cover is the extremal case: trivial subgroup (always normal), deck group $\pi_1(X) / \{1\} = \pi_1(X)$ acts transitively on the fibre, and the cover is automatically regular.

What if we *dropped* the regularity condition? Non-regular covers still exist and are useful — but the deck group is smaller than $\pi_1$, and you cannot recover the base as a quotient of the cover. The example to keep in mind: the index-3 subgroup of $S_3 = \pi_1$ of the figure-eight-like space (more precisely, a CW complex with $\pi_1 = S_3$) generates a 3-sheeted cover whose deck group is *trivial*, not $\mathbb{Z}/3$ — the subgroup is not normal, so no deck-transformation symmetry exists between sheets.

What if we *strengthened* by also demanding the deck group to be abelian? You get **abelian covers** — corresponding to subgroups containing the commutator subgroup $[\pi_1, \pi_1]$. The **maximal abelian cover** corresponds to the commutator subgroup itself and has deck group $\pi_1(X)^{\mathrm{ab}} = H_1(X; \mathbb{Z})$. These are useful in their own right (they correspond to the abelian invariants of $X$), but they are a strict subclass of regular covers.

---

# The Definition

Let $p : \tilde X \to X$ be a [[Def - Covering Space|covering map]] with $\tilde X$ connected, $X$ path-connected and locally path-connected. The cover is **regular** (or **Galois**, or **normal**) if any of the following equivalent conditions holds:

1. **Deck transitivity.** The deck group $\mathrm{Deck}(\tilde X / X)$ acts transitively on each fibre $p^{-1}(x)$.
2. **Subgroup normality.** The subgroup $p_*\pi_1(\tilde X, \tilde x_0) \leq \pi_1(X, x_0)$ is a [[Def - Normal Subgroup|normal subgroup]] of $\pi_1(X, x_0)$ for some (equivalently, every) choice of base point $\tilde x_0 \in p^{-1}(x_0)$.
3. **Quotient equals base.** The quotient map $\tilde X / \mathrm{Deck}(\tilde X / X) \to X$ is a homeomorphism.

When the cover is regular, the deck group is
$$
\mathrm{Deck}(\tilde X / X) \cong \pi_1(X, x_0) / p_*\pi_1(\tilde X, \tilde x_0).
$$

**Special cases.**
- The **universal cover** $\widetilde X \to X$ is regular (trivial subgroup is normal), with deck group equal to $\pi_1(X)$.
- The **trivial cover** $X \to X$ is regular (the full subgroup $\pi_1(X)$ is normal in itself), with trivial deck group.
- The **abelian covers** are regular covers with abelian deck group — equivalently, the subgroup contains the commutator subgroup $[\pi_1(X), \pi_1(X)]$. The maximal abelian cover has deck group $\pi_1(X)^{\mathrm{ab}} = H_1(X; \mathbb{Z})$.

---

# Categorical / Structural Definition

In the category of pointed covers of $X$, a pointed cover $(\tilde X, \tilde x_0) \to (X, x_0)$ is **regular** when the corresponding subgroup of $\pi_1(X, x_0)$ does not depend on the choice of base point $\tilde x_0 \in p^{-1}(x_0)$ — equivalently, when all conjugates of the subgroup coincide. Equivalently, in the unpointed category of covers, a cover $\tilde X \to X$ is regular when it is isomorphic to itself by every fibre permutation — the cover has "full Galois symmetry."

In the language of [[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles|fibre bundles]], regular covers are exactly the **principal $G$-bundles** for $G$ a discrete group: the deck group acts freely and transitively on fibres, making each fibre a $G$-torsor. Non-regular covers are associated bundles to principal bundles via the action of $G$ on a set with non-trivial stabilisers.

---

# Relate to Other Fields / Compression

A regular cover is a **principal $G$-bundle with discrete structure group $G =$ deck group**. The non-regular covers are the *associated bundles* of the universal cover (which is the principal $\pi_1$-bundle): given a non-trivial subgroup $H \leq \pi_1$ that is not normal, the associated bundle $\widetilde X \times_\pi_1 (\pi_1 / H)$ is the non-regular cover corresponding to $H$. So *every* connected cover is built from the universal cover by an associated-bundle construction; the regular ones are the principal ones.

**True name:** "regular" = "principal bundle in the discrete-structure-group sense" = "self-similar Galois symmetry" = "subgroup is normal" = "deck group acts transitively on fibres" = "you can recover $X$ as $\tilde X$ modulo the deck group." These five characterisations describe the same property from five angles, and which one is most operational depends on the problem.

---

# Examples / Corollaries

**Is an instance: the universal cover $\widetilde X \to X$ is always regular.** Trivial subgroup is normal; deck group is $\pi_1(X)$.

**Is an instance: $\mathbb{R} \to S^1$.** Deck group $\mathbb{Z}$ acts by translation, transitive on fibres. Subgroup $0 \leq \mathbb{Z}$ is normal. The quotient $\mathbb{R}/\mathbb{Z} = S^1$ recovers the base.

**Is an instance: $S^n \to \mathbb{RP}^n$ for $n \geq 2$.** Deck group $\mathbb{Z}/2$, transitive on the 2-element fibre. Subgroup $0 \leq \mathbb{Z}/2$ is normal. $S^n / \{\pm 1\} = \mathbb{RP}^n$.

**Is an instance: $z \mapsto z^n : S^1 \to S^1$.** Deck group $\mathbb{Z}/n$ acts transitively on the $n$-element fibres. Subgroup $n\mathbb{Z} \leq \mathbb{Z}$ is normal (every subgroup of an abelian group is normal). Deck group $\mathbb{Z}/n\mathbb{Z}$ matches the quotient.

**Is an instance: any cover with abelian $\pi_1(X)$.** Every subgroup of an abelian group is normal, so *every* connected cover of a space with abelian $\pi_1$ is regular. Tori, spheres of dimension $\geq 2$, projective spaces, $\mathrm{SO}(2)$, $\mathrm{SU}(n)$, and all topological groups (abelian by [[Ex - Pi_1 of a Topological Group is Abelian]]) have only regular covers.

**Is an instance: $T \to K$ (torus → Klein bottle), the orientable double cover of $K$.** Deck group $\mathbb{Z}/2$ transitive on 2-element fibres. The subgroup $H = p_*\pi_1(T) = \mathbb{Z}^2$ inside $\pi_1(K) = \langle a, b \mid abab^{-1} \rangle$ is the orientation-preserving subgroup, which has index 2 and hence is normal. See [[Def - Orientable Double Cover]].

**Is NOT an instance: a 3-sheeted cover of a space with $\pi_1 = S_3$ corresponding to an index-3 *non-normal* subgroup.** Specifically, take $X =$ a 2-dimensional CW complex with $\pi_1(X) = S_3$, and choose $H = \langle (1\,2) \rangle \leq S_3$, a subgroup of order $2$ and index $3$. The corresponding cover is 3-sheeted, but $H$ is not normal in $S_3$ (its conjugates are $\langle (1\,3) \rangle$ and $\langle (2\,3) \rangle$, all distinct). So the deck group is $N_{S_3}(H)/H = H/H = \{1\}$ — trivial. The cover has no non-trivial symmetries, and the deck-group quotient is *not* the base $X$; instead it is a strictly larger space, the cover corresponding to the smallest normal subgroup containing $H$ (the normal closure of $H$, here $A_3$ — so the quotient is the 2-sheeted cover corresponding to $A_3$).

**Is NOT an instance: the universal cover of the figure-eight is *regular* but its proper covers corresponding to subgroups like $\langle a \rangle \leq F_2$ are *not regular*.** The subgroup $\langle a \rangle$ (generated by one of the free generators) is not normal in $F_2$, so the corresponding 1-sheeted cover (wait, this has infinite index) — corrected: $\langle a \rangle \leq F_2$ has infinite index, and the corresponding cover is the infinite "comb" — not regular because $\langle a \rangle$ is not normal.

**Corollary (deck group for non-regular cover):** for a connected cover $\tilde X \to X$ corresponding to subgroup $H = p_*\pi_1(\tilde X) \leq \pi_1(X)$, the deck group is
$$
\mathrm{Deck}(\tilde X / X) \cong N_{\pi_1(X)}(H) / H
$$
where $N_G(H) = \{g \in G : gHg^{-1} = H\}$ is the normaliser. The cover is regular iff $N_{\pi_1(X)}(H) = \pi_1(X)$, iff $H \trianglelefteq \pi_1(X)$.

**Corollary (orbits of the deck action):** the orbits of $\mathrm{Deck}(\tilde X / X)$ on a fibre $p^{-1}(x_0)$ are in bijection with **double cosets** $H \backslash \pi_1(X) / H$. For a regular cover, $H$ is normal, so all double cosets equal single cosets, and the orbits coincide with the fibre — the action is transitive.

**Calibration check.** If you can (a) state the three equivalent definitions of regular cover and explain why they are equivalent in one sentence each, (b) compute the deck group of a non-regular cover using the normaliser formula, and (c) explain why every cover of a space with abelian $\pi_1$ is regular, you have understood the definition. Bonus: give an explicit example of a non-regular cover and check by hand that the deck group is strictly smaller than the fibre.

---

# Unlocked by This

> [!tip] Galois Closure of a Cover *(in this topic)*
> Given any (possibly non-regular) cover $\tilde X \to X$ corresponding to subgroup $H \leq \pi_1(X)$, the **Galois closure** is the regular cover corresponding to the *normal closure* of $H$ (the smallest normal subgroup containing $H$). This is the smallest regular cover dominating $\tilde X$. The analogy with field theory is exact: the Galois closure of a separable extension $K \subseteq L$ is the smallest Galois extension containing $L$.

> [!tip] Branched Coverings and Riemann Surfaces *(from Complex Analysis)*
> Allowing "ramification" — points where sheets of the cover come together — gives **branched coverings**, a generalisation crucial for Riemann surfaces. The classification of branched coverings of $\mathbb{CP}^1$ in terms of permutation representations of the fundamental group of the punctured sphere is the **Riemann existence theorem**. This is the algebraic-geometric analogue of the topological Galois correspondence, and the ramification structure carries arithmetic information.

> [!tip] The Profinite Galois Group *(from Number Theory)*
> The profinite completion of $\pi_1(X)$ classifies *finite* regular covers; the limit over finite Galois extensions is the **absolute Galois group**. For $X = \mathrm{Spec}\,\mathbb{Q}$, this is one of the central objects of modern number theory.
