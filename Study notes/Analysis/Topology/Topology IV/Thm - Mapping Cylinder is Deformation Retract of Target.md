---
type: theorem
subject: topology
prereqs:
  - "Def - Mapping Cylinder and Mapping Cone"
  - "Def - Deformation Retract"
  - "Def - Homotopy Equivalence and Contractible Space"
tags: [analysis, topology, homotopy, mapping-cylinder]
---

# Notation

$f : X \to Y$ a continuous map; $M_f = (X \times I \sqcup Y) / (x, 0) \sim f(x)$ the mapping cylinder; $j : X \hookrightarrow M_f$, $x \mapsto [(x, 1)]$ the inclusion; $r : M_f \to Y$, $r[(x, t)] = f(x)$, $r[y] = y$, the canonical retraction. The full registry is on the topic page.

---

# Motivation

The mapping cylinder $M_f$ is built precisely so that any continuous map $f : X \to Y$ becomes — up to homotopy — the inclusion $X \hookrightarrow M_f$. For this trick to be useful, the cylinder $M_f$ must be *interchangeable with $Y$* in any homotopy-theoretic argument. This theorem provides the interchangeability: $Y$ is a strong deformation retract of $M_f$, so $Y \simeq M_f$, and any homotopy-invariant property of $Y$ transfers to $M_f$.

The picture is concrete: $M_f$ is "$Y$ with a cylinder attached to it along $f$". The cylinder $X \times I$ has $X$ at one end (the free end, $t = 1$) and is glued to $Y$ at the other end ($t = 0$). The retraction $r$ slides everything down the cylinder onto $Y$: each cylinder slice $X \times \{t\}$ deforms continuously to $X \times \{0\}$ (which is identified with $f(X) \subseteq Y$), while points already in $Y$ stay put. The deformation $H([x, s], t) = [x, (1-t)s]$ provides the homotopy.

The strong-deformation-retract property says: not only is $r$ a retraction (it fixes $Y$), but the deformation *throughout* the homotopy keeps $Y$ pointwise fixed. So $M_f$ and $Y$ are homotopy equivalent via maps that don't move $Y$ — the cleanest possible homotopy equivalence.

---

# Statement

Let $f : X \to Y$ be a continuous map, and let $M_f$ be its mapping cylinder. Then the canonical retraction $r : M_f \to Y$ is a **strong deformation retract**: there is a continuous map $H : M_f \times I \to M_f$ with

1. $H(z, 0) = z$ for all $z \in M_f$;
2. $H(z, 1) = r(z) \in Y \subseteq M_f$ for all $z \in M_f$;
3. $H(y, t) = y$ for all $y \in Y \subseteq M_f$ and all $t \in I$.

In particular, the inclusion $Y \hookrightarrow M_f$ is a homotopy equivalence, and $Y \simeq M_f$.

**Consequence.** Every continuous map $f : X \to Y$ factors as $f = r \circ j$ where $j : X \hookrightarrow M_f$ is the inclusion of a closed subspace and $r : M_f \to Y$ is a homotopy equivalence. So $f$ is "the same as" the inclusion $j$ in the homotopy category.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is just "$f : X \to Y$ is continuous" — no restriction on $X$ or $Y$. The natural enrichment of this is:

**$f$ a cofibration already.** Property $B$: $f$ is already an embedding (a homeomorphism onto its image) with the homotopy extension property. The bridge: in this case, $f(X) \subseteq Y$ is already a "nice" subspace, and $M_f \simeq Y$ for the cleaner reason that $f$ is essentially an inclusion. *Example:* embeddings of CW subcomplexes, where the mapping cylinder is homotopy equivalent to the target both ways.

**$f$ a homotopy equivalence.** Property $B$: $f$ is itself a homotopy equivalence. The bridge: $M_f \simeq Y$ via the canonical retract, but also $M_f \simeq X$ via a different retract along the cylinder. *Example:* showing that two homotopy equivalent spaces have the same homotopy invariants by using a mapping cylinder as a common reference.

**Targets (Output Amplification)**

The conclusion $Y \simeq M_f$ is amplified by combining with structural results about $M_f$.

Combine with **$M_f$'s inclusion property.** Property $D$: $X$ sits inside $M_f$ as a closed subspace via $j(x) = (x, 1)$. The amplified result $E$: any theorem about inclusions can be applied to $f$ via the substitution $f \mapsto (j, r)$. *Example:* the homotopy extension property for cofibrations: $X \hookrightarrow M_f$ is a cofibration for any $f$, so we can extend homotopies on $X$ to homotopies on $M_f$, and then transport via $r$ to homotopies on $Y$. This converts the inclusion-required theorem to a general one for any $f$.

Combine with **the cone construction.** Property $D$: the cone $C_f = M_f / X$ collapses the free copy of $X$ to a point. The amplified result $E$: the cofibre sequence $X \xrightarrow{f} Y \to C_f \to \Sigma X \to \cdots$ is exact in cohomology (any cohomology theory). The mapping cylinder's deformation retract structure is exactly what makes this work: $C_f \simeq Y/X$ in a precise sense.

Combine with **classifying spaces.** Property $D$: $f$ classifies some structure (a fiber bundle, a map to $BG$). The amplified result $E$: the mapping cylinder gives a "fattened" version that is sometimes more convenient for classifying-space arguments.

---

# Why Is It True

The mapping cylinder is *built* as $Y$ with $X \times I$ glued on at one end. Topologically, $Y$ is already a closed subspace of $M_f$ (via the inclusion $Y \hookrightarrow X \sqcup Y \twoheadrightarrow M_f$). The "extra stuff" in $M_f$ beyond $Y$ is the cylinder $X \times I$, with the bottom $X \times \{0\}$ identified with $f(X) \subseteq Y$.

To deformation-retract $M_f$ onto $Y$, we slide the cylinder down. The point $(x, s)$ for $s \in (0, 1]$ moves to $(x, (1-t)s)$ as $t$ increases from $0$ to $1$. At $t = 0$, no motion; at $t = 1$, the point arrives at $(x, 0)$, which equals $f(x) \in Y$ by the cylinder's identification. Points already in $Y$ are not in the cylinder portion, so they don't move — condition (3) of strong deformation retract.

The continuity of $H : M_f \times I \to M_f$ is the only nontrivial check. The formula is piecewise: $H([y], t) = [y]$ for $y \in Y$; $H([(x, s)], t) = [(x, (1-t)s)]$ for $(x, s) \in X \times I$. At the gluing $s = 0$, both formulas agree: $H([(x, 0)], t) = [(x, 0)] = [f(x)]$, and the $Y$-formula gives $H([f(x)], t) = [f(x)]$. So the two pieces match.

For full joint continuity, use the universal property of the quotient applied to the obvious continuous map on the disjoint union. The map $\tilde H : (X \times I \sqcup Y) \times I \to M_f$ is continuous on each piece, and agrees on the identification, so it descends to a continuous map $H : M_f \times I \to M_f$.

The intuition: the cylinder slice $X \times \{s\}$ is mapped homeomorphically to $X \times \{(1-t)s\}$, a slice closer to the base. The base $X \times \{0\} = f(X)$ is held fixed (as part of $Y$). So the entire deformation is the "shrinking the cylinder to its base" homotopy, parametrized continuously by $t$.

The reason to expect this: any space built by gluing a contractible "extra" piece to a base should be homotopy equivalent to the base. The cylinder $X \times I$ is contractible *as a fiber bundle over $X$* (its fibers, the intervals $I$, are contractible), and the gluing collapses the contractible direction to a point. The base $Y$ absorbs the cylinder via the deformation.

---

# What Makes This Hard

The non-obvious step is *checking continuity of $H$ at the gluing*. The map is defined piecewise on a quotient space, and verifying that the pieces agree at the boundary — and that the result is continuous through the quotient projection — requires invoking the universal property and the disjoint union topology. The common error is to write down the formula for $H$ on the cylinder portion and forget to specify it on $Y$, or to specify formulas that disagree at the boundary $s = 0$.

---

# Rederivation Scaffold

**High-level strategy:**
Define $H$ on the disjoint union $X \times I \sqcup Y$ first, then descend to $M_f$ via the universal property. Verify the gluing $(x, 0) \sim f(x)$ is respected.

**Subgoal decomposition:**

1. **Define $H$ on disjoint union.** $\tilde H : (X \times I \sqcup Y) \times I \to M_f$ by $\tilde H((x, s), t) = [(x, (1-t)s)]$ on the cylinder portion and $\tilde H(y, t) = [y]$ on the $Y$ portion.
   - *Hint:* Each piece is a composition of continuous maps.
   - *Why needed:* This is the continuous map to descend.

2. **Verify the gluing.** Check $\tilde H((x, 0), t) = \tilde H(f(x), t)$ for all $x \in X, t \in I$, so $\tilde H$ respects $\sim$.
   - *Hint:* $\tilde H((x, 0), t) = [(x, 0)] = [f(x)]$ (using the identification in $M_f$); $\tilde H(f(x), t) = [f(x)]$. Same.

3. **Descend via universal property.** By [[Thm - Universal Property of the Quotient]] applied to $(X \times I \sqcup Y) \times I \to M_f \times I$ (with the second factor unchanged), $\tilde H$ descends to a continuous $H : M_f \times I \to M_f$.
   - *Hint:* This requires the fact that the product of an identification with the identity is still an identification (true here because $I$ is locally compact Hausdorff — Proposition 13.19 in Bredon).

4. **Verify deformation retract conditions.** Check $H(z, 0) = z$ (identity at $t = 0$), $H(z, 1) \in Y$ (lands in $Y$), $H(y, t) = y$ for $y \in Y$ (fixes $Y$).

---

# Lemma Decomposition

> [!note]- Lemma 1: Product of identification with identity is identification
> **Statement:** If $p : X \to X'$ is an identification map and $K$ is locally compact Hausdorff, then $p \times 1_K : X \times K \to X' \times K$ is an identification map.
>
> **Hint:** Bredon's Proposition 13.19.
>
> **Why needed:** Lets us descend $\tilde H : (X \times I \sqcup Y) \times I \to M_f$ to $H : M_f \times I \to M_f$ (with $I$ playing the role of $K$).
>
> > [!note]- Full proof
> > See Bredon, Proposition 13.19. The argument uses the tube lemma / local compactness to show the product map is open as well as continuous and surjective, hence an identification.

> [!note]- Lemma 2: The deformation formula respects the gluing
> **Statement:** The map $\tilde H : (X \times I \sqcup Y) \times I \to M_f$, defined by $\tilde H((x, s), t) = [(x, (1-t)s)]$ on the cylinder portion and $\tilde H(y, t) = [y]$ on $Y$, is well-defined on the quotient.
>
> **Hint:** Check the values agree on $(x, 0) \in X \times I$ and $f(x) \in Y$.
>
> **Why needed:** Allows descent to $M_f \times I$.
>
> > [!note]- Full proof
> > On the cylinder side: $\tilde H((x, 0), t) = [(x, (1-t) \cdot 0)] = [(x, 0)]$. On the $Y$ side: $\tilde H(f(x), t) = [f(x)]$. But in $M_f$, $[(x, 0)] = [f(x)]$ by the defining identification. So the two values agree.

---

# Formal Proof

> [!note]- Complete formal proof
> Define $\tilde H : (X \times I \sqcup Y) \times I \to M_f$ by:
> - $\tilde H((x, s), t) = [(x, (1-t)s)]_{M_f}$ on the cylinder portion;
> - $\tilde H(y, t) = [y]_{M_f}$ on the $Y$ portion.
>
> Continuity of $\tilde H$ on each piece: on the cylinder portion, it factors as $(x, s, t) \mapsto (x, (1-t)s)$ (continuous) followed by the projection $X \times I \hookrightarrow X \times I \sqcup Y \twoheadrightarrow M_f$ (continuous). On the $Y$ portion, it is the projection $Y \hookrightarrow X \times I \sqcup Y \twoheadrightarrow M_f$ (continuous), independent of $t$.
>
> Continuity on the disjoint union: a function on a disjoint union is continuous iff its restriction to each piece is continuous. So $\tilde H : (X \times I \sqcup Y) \times I \to M_f$ is continuous.
>
> Gluing condition (Lemma 2): $\tilde H$ respects the equivalence $(x, 0) \sim f(x)$, so it factors through the quotient $M_f \times I = ((X \times I \sqcup Y) \times I) / \sim$.
>
> Descent via universal property: by Lemma 1 (Bredon 13.19), $M_f \times I$ has the quotient topology from $(X \times I \sqcup Y) \times I$. So $\tilde H$ descends to a continuous $H : M_f \times I \to M_f$.
>
> Verification of deformation retract conditions:
> - $H(z, 0) = z$: on cylinder portion, $[(x, s)] \mapsto [(x, (1-0)s)] = [(x, s)]$; on $Y$ portion, $[y] \mapsto [y]$. So $H(\cdot, 0) = 1_{M_f}$.
> - $H(z, 1) \in Y$: on cylinder portion, $[(x, s)] \mapsto [(x, 0)] = [f(x)] \in Y$; on $Y$ portion, $[y] \mapsto [y] \in Y$. So $H(\cdot, 1) = r$.
> - $H(y, t) = y$ for $y \in Y$: by definition, $H([y], t) = [y]$ for all $t$.
>
> So $H$ is a strong deformation retraction of $M_f$ onto $Y$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Replacement of fibrations.** In a model category, there is a dual "mapping cocylinder" (or path object) construction that replaces any morphism by a fibration up to weak equivalence. The mapping cylinder is the cofibration replacement; the cocylinder is the fibration replacement. Both rely on the same homotopy-equivalence trick.

**Reduced suspensions and loops.** The reduced mapping cylinder $\tilde M_f = M_f / (\{x_0\} \times I)$ for based maps has the same deformation-retract property in the based category. Iterating gives the loop space $\Omega Y$ as a "homotopy inverse" to suspension $\Sigma X$, via the adjunction $\operatorname{Map}_*(\Sigma X, Y) \simeq \operatorname{Map}_*(X, \Omega Y)$.

**Mapping cylinder of an inclusion.** If $f$ is itself an inclusion of a closed subspace, $M_f$ is homotopy equivalent to $Y$ in two ways: by the deformation retract (sliding the cylinder to $Y$) and by collapsing the cylinder (since the inclusion already lives in $Y$). The two equivalences are compatible up to homotopy.

---

# Bridges

- **[[Def - Mapping Cylinder and Mapping Cone]]** — defines the object whose homotopy properties this theorem establishes.

- **[[Def - Deformation Retract]]** — the technical notion this theorem proves.

- **[[Thm - Universal Property of the Quotient]]** — the engine for descending the explicit deformation formula to the quotient $M_f$.

- **[[Def - Homotopy Equivalence and Contractible Space]]** — the consequence: $Y \simeq M_f$, i.e., they are homotopy equivalent.

---

# Unlocked by This

> [!tip] Cofibration *(from Algebraic Topology)*
> The inclusion $j : X \hookrightarrow M_f$ is a **cofibration** for any $f$ — it has the homotopy extension property. This is the universal way to replace any continuous map by a cofibration, the dual of fibration replacement.

> [!tip] Puppe Sequence *(from Stable Homotopy Theory)*
> The mapping cone $C_f$ and its iterated suspensions form the **Puppe sequence** $X \to Y \to C_f \to \Sigma X \to \Sigma Y \to \cdots$, a long exact sequence in any cohomology theory. The mapping cylinder's deformation-retract property is what makes the Puppe sequence work — it ensures $C_f$ has the "right" homotopy type.
