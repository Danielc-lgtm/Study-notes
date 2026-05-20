---
type: theorem
subject: topology
prereqs:
  - "Def - Topological Group"
  - "Def - Homeomorphism"
tags: [analysis, topology, topological-group, homogeneity]
---

# Notation

$G$ a topological group with identity $e$, multiplication $\mu$, inversion $\iota$. For $g \in G$: left translation $L_g(h) = gh$; right translation $R_g(h) = hg^{-1}$ (Bredon's convention, ensuring $R_e = 1_G$); conjugation $C_g(h) = ghg^{-1}$; inversion $\iota(h) = h^{-1}$. The full registry is on the topic page.

---

# Motivation

A topological group is much more than a space with a continuous binary operation: the group structure injects a high degree of *rigidity*. The key fact is that every translation by a group element is a homeomorphism of the underlying space. This means: the topological structure looks exactly the same at every point of the group. A neighborhood of $e$ becomes, after translation by $g$, a neighborhood of $g$, and a neighborhood of $g$ becomes a neighborhood of $h$ after translation by $hg^{-1}$. The topology is **homogeneous**: every point is "topologically indistinguishable" from every other.

This is a hugely useful fact. It lets us reduce any topological question about $G$ to a local question about $e$. Want to know if $G$ is locally connected? Check at $e$. Want a basis for the topology? A basis at $e$ translates to a basis at every other point. Want to know about local compactness, second countability, paracompactness? All of these are equivalent to their assertion at $e$ alone.

The proof is essentially formal: $L_g$ is continuous (since multiplication is jointly continuous and $L_g = \mu(g, \cdot)$ is the restriction to $\{g\} \times G$), and $L_g$ has a continuous inverse $L_{g^{-1}}$ (the group axioms give $L_g \circ L_{g^{-1}} = L_e = 1_G$). Continuous with continuous inverse = homeomorphism.

---

# Statement

Let $G$ be a topological group and $g \in G$.

1. **Left translation:** $L_g : G \to G$, $h \mapsto gh$, is a homeomorphism, with inverse $L_{g^{-1}}$.
2. **Right translation:** $R_g : G \to G$, $h \mapsto hg^{-1}$, is a homeomorphism, with inverse $R_{g^{-1}}$.
3. **Conjugation:** $C_g : G \to G$, $h \mapsto ghg^{-1}$, is a homeomorphism (in fact a continuous group automorphism).
4. **Inversion:** $\iota : G \to G$, $h \mapsto h^{-1}$, is a homeomorphism (its own inverse).

**Composition relations:**

- $L_g \circ L_h = L_{gh}$ (so $g \mapsto L_g$ is a homomorphism $G \to \operatorname{Homeo}(G)$).
- $R_g \circ R_h = R_{gh}$ (with Bredon's convention).
- $C_g \circ C_h = C_{gh}$.

**Consequence (homogeneity).** For any two points $g, h \in G$, the map $L_{hg^{-1}}$ is a homeomorphism of $G$ sending $g$ to $h$. Hence the topological structure of $G$ at $g$ and at $h$ are identical: $G$ is a **homogeneous space**.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$G$ is a topological group" — joint continuity of multiplication and inversion.

A subtle source: **multiplication is "left-continuous" in the second variable for each fixed first variable.** Property $B$: for each fixed $g$, the map $h \mapsto gh$ is continuous. The bridge: joint continuity of $\mu$ implies separate continuity. *Example:* in any setting where you have a continuous action of a group $G$ on itself by left multiplication, the maps $L_g$ are continuous.

**Targets (Output Amplification)**

The conclusion "$L_g$ is a homeomorphism" amplifies enormously.

Combine with **a local property at $e$.** Property $D$: a property $P$ holds locally at $e$ (e.g., a neighborhood of $e$ is connected, or compact, or admits a local cross-section). The amplified result $E$: the same property $P$ holds locally at every point — translate via $L_g$. This is the key tool in proving structural properties of topological groups.

Combine with **second countability or first countability.** Property $D$: there is a countable neighborhood basis at $e$. The amplified result $E$: $G$ is first countable (countable basis at every point, by translation). And via metrization theorems (Kakutani-Birkhoff), a first countable topological group is metrizable.

Combine with **a Haar measure construction.** Property $D$: a left-translation-invariant Radon measure exists. The amplified result $E$: by translation, integrals are invariant under any group action, giving the foundation of harmonic analysis on $G$.

Combine with **regularity at $e$.** Property $D$: $e$ has a neighborhood whose closure is contained in any given neighborhood. The amplified result $E$: $G$ is regular (every point has the same property) — see [[Thm - Topological Group is Regular]].

---

# Why Is It True

A topological group has *two structures* — a topology and a group operation — and these are required to interact via continuity of multiplication and inversion. Translations are the most basic combination: they apply the group operation (multiplication by $g$) and ask if the result respects the topology.

The continuity of $L_g$ comes from the joint continuity of multiplication: $\mu : G \times G \to G$ is continuous, so for any fixed $g$, the restriction to $\{g\} \times G$ (which we can view as $G$) is continuous, and that restriction is exactly $L_g$. Or: $L_g$ is the composition of the inclusion $G \hookrightarrow G \times G$, $h \mapsto (g, h)$ (continuous, as the projection $G \times G \to G$ is continuous in each slot), with $\mu$.

The inverse of $L_g$ is $L_{g^{-1}}$, because $L_g \circ L_{g^{-1}}(h) = g(g^{-1}h) = h$ and similarly the other way. Both $L_g$ and $L_{g^{-1}}$ are continuous, so $L_g$ is a homeomorphism.

Conjugation $C_g = L_g \circ R_g^{-1}$ (well, $C_g(h) = ghg^{-1} = L_g(R_g^{-1}(h))$ depending on sign convention). It's a composition of homeomorphisms, hence a homeomorphism. Moreover, $C_g$ is a group homomorphism: $C_g(hk) = ghkg^{-1} = ghg^{-1} \cdot gkg^{-1} = C_g(h) C_g(k)$.

Inversion $\iota$ is continuous by definition of topological group. It is its own inverse: $\iota(\iota(h)) = (h^{-1})^{-1} = h$. So $\iota$ is a homeomorphism.

The homogeneity statement is purely a corollary: $L_{hg^{-1}}(g) = (hg^{-1})g = h$. So translation by $hg^{-1}$ sends $g$ to $h$, and being a homeomorphism, it carries neighborhoods of $g$ to neighborhoods of $h$. So the topology near $g$ and the topology near $h$ are isomorphic via this explicit homeomorphism.

The deep meaning: in a generic topological space, different points can have wildly different topologies (consider $[0, 1)$, where $0$ is a special "corner" point distinct from the interior). In a topological group, *every* point has the same local topology as $e$, because the group action moves $e$ to every point.

---

# What Makes This Hard

The proof is one line: continuity from joint continuity of $\mu$, and inverse is the other translation. The "hard" part is just *internalizing the homogeneity* — recognizing that you should reduce every topological question about $G$ to a question about $e$. The common error in topological group problems is to fail to translate to $e$ and instead try to argue at an arbitrary point, missing the simplifications.

---

# Rederivation Scaffold

**High-level strategy:**
$L_g$ is continuous as a restriction of the jointly-continuous $\mu$. Its inverse is $L_{g^{-1}}$, also continuous. So $L_g$ is a homeomorphism. The other claims follow similarly.

**Subgoal decomposition:**

1. **Show $L_g$ is continuous.** Factor $L_g$ through $G \hookrightarrow G \times G \xrightarrow{\mu} G$.
   - *Hint:* The inclusion is continuous (composition of constant map and identity).

2. **Show $L_g$ has inverse $L_{g^{-1}}$.** Compute $L_g \circ L_{g^{-1}} = L_e = 1_G$.

3. **Conclude $L_g$ is a homeomorphism.** Continuous bijection with continuous inverse.

4. **Same argument for $R_g$, $C_g$, $\iota$.**

5. **Homogeneity:** $L_{hg^{-1}}$ sends $g$ to $h$, hence the topology is uniform across $G$.

---

# Lemma Decomposition

> [!note]- Lemma 1: $L_g \circ L_h = L_{gh}$
> **Statement:** Composition of left translations corresponds to group multiplication.
>
> **Hint:** Just associativity.
>
> **Why needed:** Gives $L_g \circ L_{g^{-1}} = L_e = 1_G$, so $L_g$ is bijective with explicit inverse.
>
> > [!note]- Full proof
> > $L_g(L_h(k)) = L_g(hk) = g(hk) = (gh)k = L_{gh}(k)$.

> [!note]- Lemma 2: $L_g$ is continuous
> **Statement:** Each $L_g : G \to G$ is continuous.
>
> **Hint:** Restriction of $\mu$.
>
> **Why needed:** First half of "$L_g$ is a homeomorphism".
>
> > [!note]- Full proof
> > $L_g = \mu \circ \iota_g$ where $\iota_g : G \to G \times G$, $\iota_g(h) = (g, h)$. The inclusion $\iota_g$ is continuous (its components are the constant $g$ and the identity, both continuous). $\mu$ is continuous by definition of topological group. The composition is continuous.

---

# Formal Proof

> [!note]- Complete formal proof
> **(1) $L_g$ is a homeomorphism.**
>
> *Continuity:* $L_g = \mu \circ (g, 1_G) : G \to G$ where $(g, 1_G) : G \to G \times G$ is $h \mapsto (g, h)$. The map $(g, 1_G)$ is continuous: its first component is the constant function $g$ (continuous), its second is the identity (continuous), and a map into a product is continuous iff each component is. The composition with continuous $\mu$ is continuous.
>
> *Bijective with continuous inverse:* By Lemma 1, $L_g \circ L_{g^{-1}} = L_{gg^{-1}} = L_e = 1_G$, and similarly $L_{g^{-1}} \circ L_g = 1_G$. So $L_g$ is a bijection with $L_g^{-1} = L_{g^{-1}}$, which is also continuous by the same argument with $g^{-1}$ in place of $g$.
>
> Hence $L_g$ is a homeomorphism.
>
> **(2) $R_g$ is a homeomorphism.** $R_g(h) = hg^{-1} = \mu(h, g^{-1})$. With Bredon's convention, $R_g \circ R_h = R_{gh}$: $R_g(R_h(k)) = R_g(kh^{-1}) = kh^{-1}g^{-1} = k(gh)^{-1} = R_{gh}(k)$. So $R_g^{-1} = R_{g^{-1}}$. Same continuity argument as $L_g$, using continuity of $\iota$ in the second variable.
>
> **(3) Conjugation $C_g$ is a homeomorphism.** $C_g(h) = ghg^{-1} = L_g(R_g(h))$ — wait, let's check with convention. $R_g(h) = hg^{-1}$, so $L_g(R_g(h)) = L_g(hg^{-1}) = g \cdot hg^{-1} = ghg^{-1} = C_g(h)$. So $C_g = L_g \circ R_g$, a composition of homeomorphisms, hence a homeomorphism. Also a group homomorphism: $C_g(hk) = ghkg^{-1} = (ghg^{-1})(gkg^{-1}) = C_g(h) C_g(k)$.
>
> **(4) Inversion $\iota$ is a homeomorphism.** Continuous by definition. $\iota \circ \iota = 1_G$, so $\iota^{-1} = \iota$, continuous. Hence a homeomorphism.
>
> **(5) Homogeneity.** Given $g, h \in G$, let $k = hg^{-1}$. Then $L_k(g) = (hg^{-1})g = h$. So $L_k$ is a homeomorphism of $G$ sending $g$ to $h$. Hence the topological structure at $g$ and $h$ are isomorphic. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Vector spaces are translation-invariant.** A topological vector space $V$ is in particular a topological group $(V, +)$. Translations $L_v(w) = v + w$ are homeomorphisms. The topology at $0$ determines the topology everywhere — a key fact in functional analysis (locally convex topology defined by seminorms at $0$).

**Coset spaces $G/H$ are homogeneous.** If $H \leq G$ is a closed subgroup, $G/H$ inherits a transitive $G$-action by left translation: $g \cdot xH = (gx)H$. Each action map is a homeomorphism of $G/H$, so $G/H$ is a homogeneous space. This is the foundation of homogeneous space theory.

**Lie group exponential map.** The exponential map $\exp : \mathfrak{g} \to G$ at the Lie algebra is "translation-equivariant" in a precise sense: $\exp(\operatorname{Ad}(g)X) = g \exp(X) g^{-1}$. Conjugation is realized on the Lie algebra by the adjoint action, and the exponential intertwines.

---

# Bridges

- **[[Def - Topological Group]]** — the setting in which this theorem is the most basic structural result.

- **[[Thm - Symmetric Neighborhoods Form a Basis at the Identity]]** — combined with this theorem, shows that any neighborhood basis at $e$ translates to bases at every point.

- **[[Thm - Topological Group is Regular]]** — uses translation invariance to reduce regularity to a property at $e$.

---

# Unlocked by This

> [!tip] Homogeneous Space *(from Differential Geometry)*
> A **homogeneous space** for $G$ is a space with a transitive $G$-action by homeomorphisms. $G$ itself, acting by left translation, is the prototype. The structure of homogeneous spaces is much more rigid than that of arbitrary spaces.

> [!tip] Haar Measure *(from Measure Theory)*
> The existence of a left-translation-invariant Radon measure on a locally compact group rests on the homogeneity provided by this theorem: the measure at $e$ is translated to every other point.

> [!tip] Local Determination of Lie Groups
> Connected Lie groups are determined (up to coverings) by their Lie algebras — the tangent space at $e$. This is because translation makes everything at any point equivalent to information at $e$, and the smooth/analytic structure pulls back via $L_g^{-1}$ to make $G$ a "Lie algebra fattened up".
