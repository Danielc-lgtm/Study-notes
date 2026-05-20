---
type: theorem
subject: topology
prereqs:
  - "Def - Quotient Topology and Identification Map"
  - "Def - Continuous Map"
tags: [analysis, topology, quotient, universal-property]
---

# Notation

$X, Y, Z$ topological spaces; $f : X \to Y$ a surjection equipped with the quotient topology on $Y$ (i.e., an identification map). $g : Y \to Z$ a function (not assumed continuous a priori). The composition is $g \circ f : X \to Z$. The full registry is on the topic page.

---

# Motivation

The defining property of the quotient topology is "$V \subseteq Y$ open iff $f^{-1}(V)$ open in $X$". This is a definition by *test*, not by *construction*: it tells you when something is open in $Y$, but doesn't tell you the structural content of working with $Y$ as a space. The universal property does — it says that maps *out of* $Y$ are determined by maps *out of* $X$ that respect the equivalence.

This is the rule that makes quotients usable. When we want to define a continuous function $g$ on the quotient space, we don't define it directly on the equivalence classes; we define a continuous function $\tilde g$ on the original space $X$ that is constant on equivalence classes (i.e., $\tilde g = g \circ f$ for the descended $g$), and the universal property guarantees that the descended $g$ is automatically continuous. This is the recipe behind every "well-defined continuous map on the quotient" argument.

---

# Statement

Let $f : X \to Y$ be a surjection. The following are equivalent:

1. $f$ is an identification map (i.e., $Y$ carries the quotient topology induced by $f$);
2. For every space $Z$ and every function $g : Y \to Z$, $g$ is continuous if and only if $g \circ f : X \to Z$ is continuous.

The "$(\Rightarrow)$" direction is the **universal property of the quotient**: a function out of the quotient is continuous iff its precomposition with the projection is continuous. The "$(\Leftarrow)$" direction shows that the universal property characterizes the quotient topology — among surjections, the quotient topology is the *only* one with this property.

---

# Sources and Targets

**Sources (Input Broadening)**

The natural starting point is "we have a quotient" — for instance, $X/{\sim}$ for some equivalence relation, or an adjunction space, or a mapping cylinder. Any space defined as the quotient of a known space is the *source* domain for applying the universal property.

A more disguised source: **a continuous surjection $f : X \to Y$ that we suspect is an identification map but haven't proven it.** Property $B$: $f$ is continuous, surjective, and open (or closed). The bridge: an open surjection equipped with the quotient topology is a quotient map; an open surjection with *any* topology on $Y$ making $f$ continuous is a quotient map (since openness ensures the topology is the finest possible). *Example:* the projection $\mathbb{R}^2 \to \mathbb{R}$, $(x, y) \mapsto x$, is an open continuous surjection, hence an identification map. So functions on $\mathbb{R}$ are continuous iff their pullback to $\mathbb{R}^2$ is.

Another disguised source: **a continuous bijection from a compact space to a Hausdorff space.** Property $B$: $f$ is a continuous bijection, $X$ compact, $Y$ Hausdorff. The bridge: by [[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism]], $f$ is a homeomorphism, hence trivially an identification map. *Example:* once you've factored a map through a quotient and verified it's a continuous bijection from a compact quotient to a Hausdorff target, the universal property applies — and the result is a homeomorphism.

**Targets (Output Amplification)**

The conclusion lets you check continuity of $g : Y \to Z$ by checking continuity of $\tilde g = g \circ f : X \to Z$. The amplification: combine with **a specific construction of $\tilde g$ that respects the equivalence**, and you obtain a continuous map on the quotient *for free*.

Combine with **the compact-to-Hausdorff upgrade.** Property $D$: the descended $g : Y \to Z$ is a continuous bijection, $Y$ compact (as a quotient of a compact $X$), $Z$ Hausdorff. The amplified result $E$: $g$ is a homeomorphism. This is the standard recipe for proving "$Y$ is homeomorphic to $Z$" when $Y$ is a quotient: descend via the universal property, then upgrade via compact-to-Hausdorff. See [[Ex - The torus has four definitions, all equivalent]].

Combine with **functoriality.** Property $D$: a continuous map $h : X \to X'$ that respects the equivalence relations on both sides. The amplified result $E$: an induced map $h_* : X/{\sim} \to X'/{\sim'}$ is continuous. The universal property gives you the induced map; together with similar constructions, it gives a functor from a category of "spaces with relations" to topological spaces.

---

# Why Is It True

The universal property is *what the quotient topology is for*. Let's see why it must hold.

If $f$ is an identification map and $g : Y \to Z$ is given, we want to show $g$ continuous $\iff g \circ f$ continuous. The "only if" direction is trivial: if $g$ is continuous and $f$ is continuous (every identification map is), then the composition $g \circ f$ is continuous.

The "if" direction is the substantive content. Suppose $g \circ f$ is continuous. We want $g$ continuous, i.e., for every open $W \subseteq Z$, $g^{-1}(W)$ is open in $Y$. By the definition of the quotient topology on $Y$, $g^{-1}(W)$ is open in $Y$ iff $f^{-1}(g^{-1}(W))$ is open in $X$. But $f^{-1}(g^{-1}(W)) = (g \circ f)^{-1}(W)$, which is open by continuity of $g \circ f$. So $g^{-1}(W)$ is open. Done.

The argument is pure unwinding: the quotient topology says "test openness by pulling back to $X$", and continuity of $g$ asks "is the preimage of every open open?". These two questions coincide because $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$.

The converse — that any surjection with this property must carry the quotient topology — is the second part of Proposition 13.5 in Bredon. The proof is by uniqueness: any topology on $Y$ finer than the quotient topology has more opens, hence the test "$g^{-1}(W)$ open" is stricter, and would fail to capture all continuous $g$; conversely, any coarser topology has fewer opens, and the test would be too permissive. The quotient topology is uniquely characterized as the one where this test exactly captures continuity.

This is the structural reason the universal property is "the right" definition of quotient: any space and projection satisfying the universal property is uniquely the quotient.

---

# What Makes This Hard

The proof is almost trivial — pure unwinding of definitions. The actual difficulty is *applying* the universal property correctly. The non-obvious step is recognizing that to descend a continuous map $\tilde g : X \to Z$ to a continuous map $g : Y \to Z$, you must check $\tilde g$ is *constant on equivalence classes* (i.e., $x \sim x' \implies \tilde g(x) = \tilde g(x')$). A common error is to skip this check and descend a map that's not well-defined as a function on the quotient.

---

# Rederivation Scaffold

**High-level strategy:**
The quotient topology declares $V$ open iff $f^{-1}(V)$ open. Continuity of $g$ asks $g^{-1}(W)$ open for open $W$. By unwinding the quotient topology test, both reduce to the same statement: $(g \circ f)^{-1}(W) = f^{-1}(g^{-1}(W))$ open in $X$.

**Subgoal decomposition:**

1. **Forward implication:** If $f$ is an identification map and $g \circ f$ continuous, then $g$ continuous.
   - *Hint:* For open $W \subseteq Z$, check $g^{-1}(W)$ open in $Y$ via the quotient topology criterion.
   - *Why needed:* This is the universal property.

2. **Reverse implication:** If the property holds, then $Y$ carries the quotient topology.
   - *Hint:* Specialize to $Z = Y$ as a set with the identification topology and $g = 1_Y$.
   - *Why needed:* Establishes that the universal property characterizes the quotient.

---

# Lemma Decomposition

> [!note]- Lemma 1: The quotient topology is the finest making the projection continuous
> **Statement:** Among all topologies on $Y$ making $f : X \to Y$ continuous, the quotient topology is the finest (largest).
>
> **Hint:** A topology makes $f$ continuous iff $f^{-1}(V)$ open in $X$ for every $V$ open in the topology. The largest such collection is precisely $\{V : f^{-1}(V) \text{ open}\}$.
>
> **Why needed:** Justifies the choice of "finest" topology in the definition.
>
> > [!note]- Full proof
> > Let $\tau$ be a topology on $Y$ making $f$ continuous. Then for every $V \in \tau$, $f^{-1}(V)$ is open in $X$. So $\tau \subseteq \tau_f := \{V : f^{-1}(V) \text{ open}\}$. Conversely, $\tau_f$ itself is a topology: it contains $\emptyset, Y$; finite intersections and arbitrary unions of preimages are preimages of intersections/unions, which are open if the originals are. And $f$ is continuous with respect to $\tau_f$ by construction. So $\tau_f$ is the largest such topology.

> [!note]- Lemma 2: $f \circ g$ continuous and $f$ open identification implies $g$ continuous
> **Statement:** If $f : X \to Y$ is an open identification map and $g : Y \to Z$ is a function with $g \circ f$ continuous (where $Z$ is any space), then $g$ is continuous.
>
> **Hint:** Direct from the universal property.
>
> **Why needed:** This is the formal restatement.
>
> > [!note]- Full proof
> > For $W \subseteq Z$ open, $(g \circ f)^{-1}(W) = f^{-1}(g^{-1}(W))$ is open in $X$ by continuity of $g \circ f$. By the quotient topology criterion, this means $g^{-1}(W)$ is open in $Y$. So $g$ is continuous.

---

# Formal Proof

> [!note]- Complete formal proof
> $(\Rightarrow)$ Assume $f$ is an identification map. Given $g : Y \to Z$.
>
> Suppose $g$ is continuous. Then $g \circ f$ is the composition of continuous maps, hence continuous.
>
> Suppose $g \circ f$ is continuous. For open $W \subseteq Z$,
> $$f^{-1}(g^{-1}(W)) = (g \circ f)^{-1}(W)$$
> is open in $X$. By the quotient topology on $Y$, this means $g^{-1}(W)$ is open in $Y$. Hence $g$ is continuous.
>
> $(\Leftarrow)$ Assume the property holds. Let $\tau_Y$ be the topology on $Y$, and let $\tau_f$ be the quotient topology induced by $f$.
>
> Specialize to $Z = Y$ as a set with topology $\tau_f$, and $g = 1_Y$ as a function. Then $g \circ f = f$ is continuous from $X$ (with original topology) to $Y$ (with topology $\tau_f$), since by definition $f^{-1}(V)$ is open for every $V \in \tau_f$. By the property, $g$ is continuous from $(Y, \tau_Y)$ to $(Y, \tau_f)$, meaning $\tau_f \subseteq \tau_Y$.
>
> Now specialize to $Z = Y$ as a set with $\tau_Y$, and $g = 1_Y$. Then $g \circ f$ is the original $f$, continuous by assumption. So $g$ is continuous from $(Y, \tau_f)$ to $(Y, \tau_Y)$, meaning $\tau_Y \subseteq \tau_f$.
>
> Together, $\tau_Y = \tau_f$. So $Y$ has the quotient topology, and $f$ is an identification map. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The free product of groups via universal property.** In group theory, the free product $G * H$ is defined by a universal property: any pair of homomorphisms $G \to K, H \to K$ extends uniquely to $G * H \to K$. The topological analogue is the wedge sum $X \vee Y$: any pair of continuous maps from $X$ and $Y$ that agree on the basepoint extends uniquely to $X \vee Y$. Both are coequalizers / pushouts and share the universal-property machinery.

**Sheafification.** In sheaf theory, the sheafification functor turns a presheaf into a sheaf via a universal property: any morphism from the presheaf to a sheaf factors uniquely through the sheafification. The construction is by a quotient (modding out by the local-section equivalence), and the universal property is structurally identical to the quotient topology's universal property.

---

# Bridges

- **[[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism]]** — the standard upgrade after applying the universal property to factor a map through a quotient. The two together form the workhorse "descend + upgrade" pattern for proving quotient homeomorphisms.

- **[[Def - Adjunction Space]]** — adjunction spaces also have a universal property (pushout), structurally the same as the quotient's. Maps out of $Y \cup_f X$ are determined by compatible pairs of maps out of $X$ and $Y$.

- **[[Def - Mapping Cylinder and Mapping Cone]]** — the mapping cylinder is a quotient, so the universal property applies: a continuous map $M_f \to Z$ is the same as continuous maps $X \times I \to Z$ and $Y \to Z$ agreeing on the identification $(x, 0) \sim f(x)$.

---

# Unlocked by This

> [!tip] Coequalizer *(from Category Theory)*
> The universal property is the topological instantiation of the **coequalizer** in a category: the quotient $X/{\sim}$ is the coequalizer of the two projections $R \rightrightarrows X$, where $R \subseteq X \times X$ is the equivalence relation. Coequalizers in $\mathbf{Top}$ are exactly quotient spaces.

> [!tip] Functoriality of Quotients *(from Algebraic Topology)*
> Functoriality of the quotient operation: a map $h : X \to X'$ respecting equivalences induces a map $h_* : X/{\sim} \to X'/{\sim'}$, continuous by the universal property. This is the input to all "induced maps on quotients" arguments in algebraic topology.
