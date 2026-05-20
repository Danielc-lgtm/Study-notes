---
type: exercise
subject: topology
difficulty: "⭐⭐"
prereqs:
  - "Def - Topological Group"
  - "Def - Connected Space"
  - "Def - Continuous Map"
tags: [analysis, topology, topological-group, connectedness]
---

# Problem Statement

Let $\operatorname{O}(n) := \{A \in M_n(\mathbb{R}) : AA^T = I\}$ be the orthogonal group, and $\operatorname{SO}(n) := \{A \in \operatorname{O}(n) : \det A = 1\}$ the special orthogonal group.

Show:

1. $\operatorname{O}(n)$ has exactly two connected components for $n \geq 1$, distinguished by the value of $\det \in \{+1, -1\}$.
2. The component of the identity is $\operatorname{SO}(n)$.
3. The other component is $\operatorname{SO}(n) \cdot D = \{AD : A \in \operatorname{SO}(n)\}$ for any fixed reflection $D \in \operatorname{O}(n)$ with $\det D = -1$ (for example, $D = \operatorname{diag}(-1, 1, 1, \dots, 1)$).

**Recall:**

$\operatorname{O}(n)$ is a [[Def - Topological Group|topological group]] under matrix multiplication, sitting in $\operatorname{GL}_n(\mathbb{R}) \subseteq \mathbb{R}^{n^2}$. The determinant $\det : \operatorname{O}(n) \to \{+1, -1\}$ is a continuous homomorphism. For $A \in \operatorname{O}(n)$, $(\det A)^2 = \det(AA^T) = \det I = 1$, so $\det A \in \{\pm 1\}$.

---

# Convergent Strategy

**Problem class:** Determine the connected components of a Lie group via a continuous invariant (the determinant).

**Assumption pattern:** $\operatorname{O}(n)$ is partitioned by $\det$ into two preimages $\det^{-1}(\{1\}) = \operatorname{SO}(n)$ and $\det^{-1}(\{-1\})$. Each preimage is closed (preimage of a closed set under continuous map). To show they are the connected components, we need (i) each is path-connected, (ii) they are disjoint.

**Theorem routing:** Use [[Ex - SO(n) is connected]] for (i)$_1$. For (i)$_2$, observe that $\operatorname{SO}(n) \cdot D$ is the image of $\operatorname{SO}(n)$ under the homeomorphism right-multiply-by-$D$, hence path-connected. For (ii), the determinant separates them: $\det = +1$ on $\operatorname{SO}(n)$, $\det = -1$ on $\operatorname{SO}(n) \cdot D$.

**Key decision point:** The continuous function $\det$ provides the "label" distinguishing the components. Since $\det$ takes only values in the discrete set $\{\pm 1\}$, no connected piece of $\operatorname{O}(n)$ can have both values. Combined with path-connectedness of each preimage, the two pieces are the components.

---

# Legal Operations Used

1. **Continuous image of a connected space is connected.** [[Thm - Continuous Image of a Connected Space]].

2. **Translation is a homeomorphism.** Right multiplication by a fixed element of a topological group is a homeomorphism — [[Thm - Translations are Homeomorphisms]].

3. **A continuous function to a discrete space separates components.** A continuous map $X \to \{a, b\}$ (discrete) separates $X$ into the preimages, each clopen.

---

# Hints

> [!note]- Hint 1
> The determinant $\det : \operatorname{O}(n) \to \{+1, -1\}$ is a continuous homomorphism. It takes only two values, so its preimages partition $\operatorname{O}(n)$ into two clopen pieces.

> [!note]- Hint 2
> Each piece is path-connected: $\operatorname{SO}(n) = \det^{-1}(\{1\})$ is path-connected by [[Ex - SO(n) is connected]]. The other piece $\det^{-1}(\{-1\})$ is $\operatorname{SO}(n) \cdot D$ for any reflection $D$; this is the image of $\operatorname{SO}(n)$ under right multiplication by $D$, a homeomorphism.

> [!note]- Hint 3
> Two clopen pieces that are each path-connected and disjoint are the connected components of their union.

---

# Solution

The proof breaks into five steps that use the determinant as a continuous invariant separating components. Step 1 verifies $\det: \operatorname{O}(n) \to \{+1, -1\}$ is continuous (polynomial in the entries, image in the discrete two-point set); Step 2 reads off that the preimages are clopen and partition $\operatorname{O}(n)$; Step 3 identifies $\det^{-1}(\{-1\}) = \operatorname{SO}(n) \cdot D$ for any fixed reflection $D$; Step 4 establishes path-connectedness of each piece (one by appeal to the connectedness of $\operatorname{SO}(n)$, the other by the right-translation homeomorphism); Step 5 concludes there are exactly two components. The non-obvious move is in Step 4 — translating $\operatorname{SO}(n)$ by $D$ via a *homeomorphism* (right multiplication in a topological group) immediately transports path-connectedness to the other coset, without any new construction.

**Step 1: $\det : \operatorname{O}(n) \to \{+1, -1\}$ is continuous.**

> [!note]- Derivation
> $\det$ is a polynomial in the entries of the matrix, so $\det : M_n(\mathbb{R}) \to \mathbb{R}$ is continuous. Restricted to $\operatorname{O}(n)$, it takes values in $\{+1, -1\}$ (since $A \in \operatorname{O}(n)$ implies $(\det A)^2 = 1$). As a continuous map to a discrete space $\{+1, -1\}$ (with the discrete topology, or as a closed subspace of $\mathbb{R}$), $\det$ is continuous.

**Step 2: The preimages of $+1$ and $-1$ are clopen in $\operatorname{O}(n)$.**

> [!note]- Derivation
> $\{+1\}$ and $\{-1\}$ are clopen in the discrete space $\{+1, -1\}$. Continuous preimages of clopen sets are clopen. So $\det^{-1}(\{+1\}) = \operatorname{SO}(n)$ and $\det^{-1}(\{-1\})$ are both clopen in $\operatorname{O}(n)$. They are disjoint (one has $\det = +1$, the other $\det = -1$), and their union is $\operatorname{O}(n)$.

**Step 3: $\det^{-1}(\{-1\}) = \operatorname{SO}(n) \cdot D$ for any fixed reflection $D$.**

> [!note]- Derivation
> Choose any $D \in \operatorname{O}(n)$ with $\det D = -1$ (e.g., $D = \operatorname{diag}(-1, 1, 1, \dots, 1)$, the reflection in the first axis).
>
> $(\subseteq)$: For $A \in \det^{-1}(\{-1\})$, set $B := A D^{-1} = A D$ (since $D = D^{-1}$ for a reflection). Then $\det B = \det A \cdot \det D = (-1)(-1) = 1$, so $B \in \operatorname{SO}(n)$. So $A = BD \in \operatorname{SO}(n) \cdot D$.
>
> $(\supseteq)$: For $A = BD$ with $B \in \operatorname{SO}(n)$: $\det A = \det B \cdot \det D = 1 \cdot (-1) = -1$. So $A \in \det^{-1}(\{-1\})$.

**Step 4: Each preimage is path-connected.**

> [!note]- Derivation
> $\operatorname{SO}(n) = \det^{-1}(\{+1\})$ is path-connected by [[Ex - SO(n) is connected]].
>
> $\operatorname{SO}(n) \cdot D = \det^{-1}(\{-1\})$ is path-connected: it is the image of $\operatorname{SO}(n)$ under the right-multiplication map $R_{D^{-1}} : \operatorname{O}(n) \to \operatorname{O}(n)$, $X \mapsto X \cdot D$. This is a homeomorphism by [[Thm - Translations are Homeomorphisms]] (Bredon's convention has $R_g(h) = hg^{-1}$, so $R_{D^{-1}}(h) = h \cdot (D^{-1})^{-1} = hD$). The image of a path-connected space under a continuous map is path-connected.

**Step 5: Conclude $\operatorname{O}(n)$ has exactly two components.**

> [!note]- Derivation
> $\operatorname{O}(n) = \operatorname{SO}(n) \sqcup (\operatorname{SO}(n) \cdot D)$ as clopen sets. Each is path-connected. A path-connected clopen subset of a topological space is a union of connected components — in fact, a single component (path-connected implies connected, and clopen = closed + open means it's a maximal connected subset, hence a component).
>
> The two pieces are distinct because their determinants are $+1$ and $-1$. So $\operatorname{O}(n)$ has exactly two components.

> [!note]- Complete formal solution
> $\det : \operatorname{O}(n) \to \{+1, -1\}$ is continuous (polynomial), and its preimages $\operatorname{SO}(n) = \det^{-1}(\{+1\})$ and $\operatorname{SO}(n) D = \det^{-1}(\{-1\})$ (for any fixed reflection $D$) partition $\operatorname{O}(n)$ into disjoint clopen subsets.
>
> $\operatorname{SO}(n)$ is path-connected by [[Ex - SO(n) is connected]]. $\operatorname{SO}(n) D$ is path-connected as the image of $\operatorname{SO}(n)$ under the right-translation homeomorphism $X \mapsto XD$.
>
> Hence each preimage is a single connected component of $\operatorname{O}(n)$, and there are exactly two. $\blacksquare$

---

# Key Takeaways

**Continuous invariants to a discrete space detect components.** Any continuous function from a topological space $X$ to a discrete set $\{a, b, \dots\}$ separates $X$ into clopen preimages, one per value. If $X$ is connected, the function is constant. The trigger-reaction pattern: "want to show two points are in different components $\Rightarrow$ find a continuous invariant separating them". For $\operatorname{O}(n)$, this is the determinant. For groups in general, continuous homomorphisms to discrete quotients (like $G \to G/G^0$, with $G^0$ the identity component) are the universal invariants.

**The identity component is the "kernel" of a continuous discrete map.** $\operatorname{SO}(n) = \det^{-1}(\{+1\})$ is the identity component because (i) it contains the identity, (ii) it is clopen, (iii) it is path-connected. The general principle: the identity component $G^0$ of any topological group is a closed normal subgroup, and the quotient $G/G^0$ is a (totally disconnected) topological group encoding the component structure.

**Translation moves components to components.** Right multiplication by $D$ is a homeomorphism sending $\operatorname{SO}(n)$ to $\operatorname{SO}(n) \cdot D$. So the topological structure of the two components is identical — they look like each other, distinguished only by the determinant label. This is the homogeneity of topological groups in action: all cosets of $\operatorname{SO}(n)$ in $\operatorname{O}(n)$ are homeomorphic.

**Generalization to other matrix groups.**
- $\operatorname{GL}_n(\mathbb{R})$ has two components, distinguished by $\operatorname{sgn}(\det)$ (positive vs negative determinant).
- $\operatorname{GL}_n(\mathbb{C})$ has *one* component, because $\det$ takes values in $\mathbb{C}^\times$ (connected) rather than $\mathbb{R}^\times$ (two components).
- $\operatorname{SL}_n(\mathbb{R})$ has one component (connected).

The general principle: the component group $\pi_0(G)$ of a Lie group $G$ is detected by continuous homomorphisms to discrete groups.
