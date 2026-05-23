---
type: exercise
subject: topology
difficulty: "⭐⭐"
prereqs:
  - "Def - Quotient Topology and Identification Map"
  - "Thm - Universal Property of the Quotient"
  - "Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism"
tags: [analysis, topology, quotient, projective]
---

# Problem Statement

The real projective plane $\mathbb{R}P^2$ has two standard definitions:

1. $P_1 := S^2 / \{\pm x\}$, the sphere with antipodal points identified.
2. $P_2 := D^2 / \{x \sim -x \text{ on } S^1\}$, the disk with antipodal points on the boundary identified.

Show that $P_1 \cong P_2$ as topological spaces.

**Recall:**

A [[Def - Quotient Topology and Identification Map|quotient topology]] is the finest topology making the projection continuous. The [[Thm - Universal Property of the Quotient|universal property]] descends $\sim$-respecting maps. [[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism]] gives the upgrade.

The disk $D^2$ embeds into the sphere $S^2$ as the upper closed hemisphere (under the projection map that pushes interior of $D^2$ to the interior of the hemisphere).

---

# Convergent Strategy

**Problem class:** Identification of two quotient definitions of the same space.

**Assumption pattern:** Both $P_1$ and $P_2$ are quotients of compact spaces; the targets in our intermediate constructions are Hausdorff. The compact-Hausdorff upgrade applies.

**Theorem routing:** Construct a continuous map $i : D^2 \to S^2/\{\pm x\}$ via the embedding of $D^2$ as the upper hemisphere. Check it respects the antipodal identification on the boundary. Descend to a continuous map $\bar i : P_2 \to P_1$. Check bijectivity. Upgrade via compact-Hausdorff.

**Key decision point:** Identifying $D^2$ with the upper hemisphere of $S^2$. The map sends $D^2$ continuously into $S^2$, hence into $P_1 = S^2/\sim$. On the boundary of $D^2$, the embedding sends $S^1 \to S^1$ (equator of $S^2$), and the antipodal identification on this equator is the same as the antipodal identification of the original boundary.

---

# Legal Operations Used

1. **Embed disk as upper hemisphere.** A continuous map $D^2 \to S^2$ realizing the hemisphere identification.

2. **Descend via universal property.** Compose the embedding with the quotient projection; verify $\sim$-respecting on the boundary.

3. **Compact-Hausdorff upgrade.** Both quotients are compact (image of compact) and Hausdorff (proven via separation arguments).

---

# Hints

> [!note]- Hint 1
> Find the explicit map $D^2 \to S^2$ that hits the upper closed hemisphere bijectively. The standard choice: $(x, y) \in D^2$ to $(x, y, \sqrt{1 - x^2 - y^2})$.

> [!note]- Hint 2
> The boundary of $D^2$ (the circle $S^1$) maps to the equator of $S^2$ (the set $\{z = 0\}$). The antipodal map on $D^2$'s boundary is $x \mapsto -x$ on $S^1$; this matches the antipodal map on $S^2$ restricted to the equator.

> [!note]- Hint 3
> Compose with the quotient projection $S^2 \to P_1$. The resulting $D^2 \to P_1$ sends the boundary $S^1$ to the equator's quotient (the projective $\mathbb{R}P^1$); the antipodal identification on $S^1 \subseteq D^2$ matches the antipodal identification in $P_1$ on the equator. So the map descends to $P_2 \to P_1$.

> [!note]- Hint 4
> Bijectivity: any point of $P_1$ is the class of some point on $S^2$; if it's not on the equator, it has a unique representative on the upper hemisphere (the one with $z > 0$), corresponding to a unique point in the interior of $D^2$. If it's on the equator, it has exactly two antipodal representatives, identified in $P_2$. So the map is a bijection.

---

# Solution

The proof breaks into six steps that execute the "construct + descend + upgrade" recipe with the hemisphere embedding as the bridge. Step 1 builds the embedding $\iota: D^2 \to S^2$ via $\iota(x,y) = (x, y, \sqrt{1 - x^2 - y^2})$, mapping the disk onto the upper hemisphere; Step 2 composes with the antipodal quotient projection $\pi: S^2 \to P_1$; Step 3 verifies that the resulting $f = \pi \circ \iota$ respects the boundary antipodal identification (since the equator maps to itself and antipodes there are identified in $P_1$); Step 4 descends via the universal property; Step 5 checks bijectivity by case-analysing what $\iota(x, y) = \pm \iota(x', y')$ forces; Step 6 upgrades by compact-to-Hausdorff. The non-obvious move is in Step 5 — the case $z = -z'$ forces both to be zero (boundary points), revealing exactly why the boundary identification on $D^2$ has to match the antipodal identification on the equator of $S^2$.

**Step 1: Define the embedding $D^2 \to S^2$.**

Let $\iota : D^2 \to S^2$, $\iota(x, y) := (x, y, \sqrt{1 - x^2 - y^2})$, the upper hemisphere parametrization. Continuous (square-root of nonnegative continuous function is continuous). Image is exactly the upper closed hemisphere $H^+ = \{(x, y, z) \in S^2 : z \geq 0\}$. Bijective onto $H^+$: $z = \sqrt{1 - x^2 - y^2}$ determined by $(x, y) \in D^2$.

**Step 2: Compose with the quotient projection $S^2 \to P_1$.**

Let $\pi : S^2 \to P_1 = S^2/\{\pm x\}$ be the quotient projection. Define $f := \pi \circ \iota : D^2 \to P_1$. Continuous (composition).

**Step 3: Verify $f$ respects the boundary antipodal identification.**

The boundary of $D^2$ is $S^1 = \{(x, y, 0) : x^2 + y^2 = 1\}$, and $\iota|_{S^1}$ is the identity (since $z = 0$ on the boundary). So $\iota(S^1) =$ equator of $S^2$. For $u \in S^1$ on the boundary of $D^2$: $f(u) = \pi(\iota(u)) = \pi(u)$ (treating $u$ as a point on the equator of $S^2$). For $-u \in S^1$ on the boundary of $D^2$ (antipodal): $f(-u) = \pi(-u) = \pi(u)$ since the antipodal map identifies $u$ and $-u$ on $S^2$. So $f(u) = f(-u)$ for antipodal boundary points. Hence $f$ respects the equivalence on $D^2$ that identifies $u \sim -u$ on $S^1$.

**Step 4: Descend to $\bar f : P_2 \to P_1$ via universal property.**

By [[Thm - Universal Property of the Quotient]], $f$ descends to a continuous $\bar f : P_2 = D^2/\sim \to P_1$. By construction, $\bar f([(x, y)]) = \pi(\iota(x, y))$ for the descended map.

**Step 5: Show $\bar f$ is bijective.**

> [!note]- Derivation — bijectivity
> *Surjectivity.* Any class in $P_1$ has a representative in $S^2$; that representative is in the upper hemisphere $H^+$ (after applying the antipodal map if needed). The upper hemisphere is the image of $\iota$, so the class has a preimage in $D^2$. Hence in $P_2$.
>
> *Injectivity.* Suppose $\bar f([(x, y)]) = \bar f([(x', y')])$, i.e., $\pi(\iota(x, y)) = \pi(\iota(x', y'))$ in $P_1$. So $\iota(x, y) = \pm \iota(x', y')$ in $S^2$.
> - Case 1: $\iota(x, y) = \iota(x', y')$. Then $(x, y, z) = (x', y', z')$, so $(x, y) = (x', y')$, hence $[(x, y)] = [(x', y')]$.
> - Case 2: $\iota(x, y) = -\iota(x', y')$. Then $(x, y, z) = (-x', -y', -z')$, so $z = -z'$. Since $z, z' \geq 0$, we have $z = z' = 0$, meaning both points are on the boundary of $D^2$. So $(x, y), (x', y') \in S^1$ and $(x, y) = -(x', y')$, hence $[(x, y)] = [(x', y')]$ in $P_2$ (by the antipodal identification on the boundary).

**Step 6: Upgrade $\bar f$ to a homeomorphism.**

> [!note]- Derivation — compact-Hausdorff upgrade
> $P_2 = D^2/\sim$ is compact (continuous image of compact $D^2$). $P_1 = S^2/\{\pm x\}$ is Hausdorff: separation by $\{\pm x\}$ orbits — for two distinct orbits, choose disjoint open neighborhoods (use that $S^2$ is metrizable and the antipodal map is a homeomorphism with disjoint orbits). By [[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism]], $\bar f$ is a homeomorphism.

> [!note]- Complete formal solution
> Define $f : D^2 \to P_1$ as the composition $D^2 \xrightarrow{\iota} S^2 \xrightarrow{\pi} P_1$, where $\iota(x, y) = (x, y, \sqrt{1 - x^2 - y^2})$ embeds the disk as the upper hemisphere and $\pi$ is the quotient projection.
>
> The map $f$ respects the equivalence on $\partial D^2 = S^1$: for $u, -u \in S^1$, $\iota(u) = u$ and $\iota(-u) = -u$ (both on the equator), so $\pi(u) = \pi(-u)$ in $P_1$.
>
> By [[Thm - Universal Property of the Quotient]], $f$ descends to a continuous $\bar f : P_2 \to P_1$.
>
> $\bar f$ is bijective (Step 5).
>
> $P_2$ is compact, $P_1$ is Hausdorff. By [[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism]], $\bar f$ is a homeomorphism. $\blacksquare$

---

# Key Takeaways

**Hemisphere embedding is the bridge between disk and sphere quotients.** Many constructions in topology bridge between disks and spheres by viewing the disk as a hemisphere of the sphere. The upper hemisphere $H^+$ of $S^n$ is homeomorphic to $D^n$ via the projection that forgets the $(n+1)$-st coordinate. This connects "disk-based" definitions of spaces (like the projective plane as a disk with boundary antipodes identified) to "sphere-based" definitions (the same space as a sphere with all antipodes identified).

**The trigger-reaction pattern.** When two definitions of a space are given as quotients, the standard approach is: (i) find an explicit continuous map between the source spaces that respects the equivalences; (ii) descend via universal property; (iii) check bijectivity; (iv) upgrade via compact-Hausdorff. This is the same pattern used in [[Ex - The torus has four definitions, all equivalent]] and most "identify two definitions" exercises.

**$\mathbb{R}P^n$ generalizes immediately.** The same proof gives $\mathbb{R}P^n = S^n/\{\pm x\} \cong D^n/\{u \sim -u \text{ on } S^{n-1}\}$ for any $n$, via the hemisphere embedding. The complex projective space $\mathbb{C}P^n$ has a similar disk-based description: $D^{2n}/\sim$ where $\sim$ identifies points related by the $S^1$-action on the boundary $S^{2n-1}$.

**Hausdorffness of the sphere quotient.** The Hausdorff property of $P_1 = S^2/\{\pm x\}$ is the only non-trivial check. It uses that $\{\pm x\}$-orbits are *finite* (size 2) and the antipodal map is a free homeomorphism. For a general $G$-action on a space, the quotient $X/G$ is Hausdorff iff the orbits are closed and the orbit map is closed — a structural condition.
