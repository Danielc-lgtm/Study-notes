---
type: exercise
subject: algebraic-topology
difficulty: "⭐"
prereqs:
  - "Def - Orientable Double Cover"
  - "Def - Covering Space"
  - "Def - Deck Transformation Group"
tags: [geometry, algebraic-topology, topology]
---

# Problem Statement

Let $M$ be the open Möbius strip: $M := ([0, 1] \times (-1, 1)) / \sim$, where $\sim$ identifies $(0, y) \sim (1, -y)$. (The closed Möbius strip uses closed intervals and is also non-orientable; the open version is more convenient for the cover construction.)

(a) Verify that $M$ is non-orientable by exhibiting a loop along which orientation reverses.

(b) Construct the **orientable double cover** $\widetilde M^{\mathrm{or}} \to M$ explicitly. Show that the total space is the cylinder $S^1 \times (-1, 1)$ (an *orientable* surface).

(c) Identify the non-trivial deck transformation as the "antipodal-and-flip" map $(z, t) \mapsto (-z, -t)$.

(d) Show that the orientation character $w_1 : \pi_1(M) \to \mathbb{Z}/2$ is *surjective*, i.e., the orientation-reversing loop is the non-trivial element of $\pi_1(M) = \mathbb{Z}$.

**Recall:**

Orientable double cover construction:

![[Def - Orientable Double Cover#The Definition]]

Covering space:

![[Def - Covering Space#The Definition]]

Deck transformations:

![[Def - Deck Transformation Group#The Definition]]

---

# Convergent Strategy

**Problem class:** Explicit construction of a double cover (the orientable double cover) for a small concrete example. The Möbius strip is the simplest non-orientable surface (the **simplest** example demonstrating the orientable double cover construction), and explicitly computing the cover reveals both the geometric picture (cylinder doubles the Möbius strip) and the algebraic picture (the orientation character is the non-trivial homomorphism $\pi_1(M) = \mathbb{Z} \to \mathbb{Z}/2$).

**Assumption pattern:** $M$ is non-orientable; its fundamental group is $\pi_1(M) = \mathbb{Z}$ (since $M$ deformation-retracts to its central circle). The orientation character is a homomorphism $w_1 : \mathbb{Z} \to \mathbb{Z}/2$, surjective if $M$ is non-orientable. The cover associated to its kernel ($2\mathbb{Z} \leq \mathbb{Z}$) is the 2-sheeted orientable double cover.

**Theorem routing:** Build $\widetilde M^{\mathrm{or}}$ via the general construction (pairs of point + local orientation) or via the explicit gluing-rectangle description. Verify it equals the cylinder $S^1 \times (-1, 1)$ via direct comparison of fundamental polygons. Identify the deck group as $\mathbb{Z}/2$. Verify the orientation character is non-trivial by computing it on the generator of $\pi_1(M) = \mathbb{Z}$.

**Key decision point:** The most efficient construction is to take *two copies of the rectangle* $[0, 1] \times (-1, 1)$ and identify the right edge of one with the right edge of the other in a way that flips orientation — giving a "long cylinder" $[0, 2] \times (-1, 1)$ with $(0, y) \sim (2, y)$. This is the cylinder $S^1 \times (-1, 1)$ if we re-parameterise. The non-obvious aspect: the cover is the cylinder, not "another Möbius strip" or "two disconnected Möbius strips." Connectedness follows because the cover is non-trivial (orientation reverses on the central circle of $M$), hence the two sheets get glued together.

---

# Legal Operations Used

1. **Operation 4 from the topic page (identify $\pi_1$ via a free properly discontinuous action).** The $\mathbb{Z}/2$-action $(z, t) \mapsto (-z, -t)$ on the cylinder $S^1 \times (-1, 1)$ is free (the only fixed point would be $(z, 0)$ with $-z = z$, requiring $z = -z$ on $S^1$, impossible). The quotient is the Möbius strip.

2. **Operation 8 from the topic page (deck transformation symmetry).** The deck transformation $\sigma : (z, t) \mapsto (-z, -t)$ on the cover is *orientation-reversing*. So orientation-reversing global symmetries of the cover descend to "orientation-reversal-by-deck" on the base — this is the trade.

3. **Operation 1 from the topic page (lift a loop).** The orientation-reversing loop on $M$ (going around the central circle once) lifts to a half-circle on the cylinder, connecting opposite fibre points. This makes the cover *connected* (a single half-circle gives a path between the two fibres), confirming non-trivial double cover.

---

# Hints

> [!note]- Hint 1
> The Möbius strip has a central circle (the image of the segment $[0, 1] \times \{0\}$). Try to follow an arrow along this central circle and see how it comes back after one full loop.

> [!note]- Hint 2
> Construct the orientable double cover by "unwrapping" the Möbius strip: take two copies of the fundamental rectangle, glue them along the identified edges in a way that "uses up" the orientation reversal. The result is a longer rectangle.

> [!note]- Hint 3
> Specifically: take the longer rectangle $[0, 2] \times (-1, 1)$ with the identification $(0, y) \sim (2, y)$ (now identifying *without* the flip). This is the cylinder.

> [!note]- Hint 4
> What is the projection $\pi : S^1 \times (-1, 1) \to M$? Identify $S^1$ as $[0, 2]/(0 \sim 2)$. Then $\pi(s, t) := \begin{cases} (s, t) & s \in [0, 1] \\ (s - 1, -t) & s \in [1, 2] \end{cases}$. This wraps the cylinder twice around the Möbius strip, with the second wrap flipping $t$.

> [!note]- Hint 5
> The deck transformation $\sigma$ is the involution making $\pi \circ \sigma = \pi$. Compute: $\sigma$ swaps the two halves of the cylinder, with a flip in $t$.

---

# Solution

**Plan:** Build the cover explicitly via the longer-rectangle picture. Verify it is a 2-sheeted cover via direct local-trivialisation argument. Identify the deck transformation as the antipodal-and-flip. Confirm the orientation character is non-trivial on the generator of $\pi_1(M)$.

**Step 1: Non-orientability of $M$ via the central circle.**

> [!note]- Derivation
> The central circle $C \subset M$ is the image of $[0, 1] \times \{0\}$ under the identification. Place a small frame (= orientation indicator) at the point $(0, 0)$: say "up" arrow points in the $+y$ direction. As you slide the frame along $C$ towards $(1, 0)$, the $+y$ arrow stays $+y$. At $(1, 0)$ you arrive, but $(1, y) \sim (0, -y)$, so the *point* $(1, 0)$ is identified with the *point* $(0, 0)$ — but the $+y$ arrow at $(1, 0)$ is now identified with the $-y$ arrow at $(0, 0)$. So the frame has *flipped*.
>
> So traversing the central circle once reverses orientation. Hence $M$ is non-orientable.

**Step 2: Construct the orientable double cover via longer-rectangle picture.**

> [!note]- Derivation
> Consider two copies of the fundamental rectangle $[0, 1] \times (-1, 1)$. The Möbius strip $M$ identifies $(0, y) \sim (1, -y)$ on a single copy. To "lift" the orientation, take two copies and "concatenate" them: place them side-by-side, $[0, 1] \times (-1, 1)$ and $[1, 2] \times (-1, 1)$. On the seam $x = 1$, glue the orientation-flipped way: $(1, y)$ in the first copy is identified with $(1, -y)$ in the second copy. This places the second copy "upside-down" relative to the first.
>
> Now glue the outer edges: $(0, y)$ in the first copy with $(2, y)$ in the second copy (this time *without* a flip). The result is a longer rectangle $[0, 2] \times (-1, 1)$ with the identification $(0, y) \sim (2, y)$ — i.e., the *cylinder* $S^1 \times (-1, 1)$ (parameterise $S^1$ as $[0, 2]/(0 \sim 2)$).
>
> Define the projection $\pi : S^1 \times (-1, 1) \to M$ by: for $s \in [0, 1]$, $\pi(s, t) = (s, t)$ in $M$; for $s \in [1, 2]$, $\pi(s, t) = (s - 1, -t)$ in $M$. The two halves of the cylinder are mapped to the same Möbius strip, but the second half is "flipped" so the gluing makes sense at the seams.
>
> $\pi$ is well-defined: at $s = 1$, both formulas give $(1, t) \in M$ in the first and $(0, -t) \in M$ in the second, which are identified in $M$ via $(0, -t) \sim (1, t)$ (Möbius identification). At $s = 0 \sim s = 2$, both formulas give $(0, t)$ and $(1, -t)$ respectively, again identified in $M$. So $\pi$ is continuous.
>
> $\pi$ is 2-to-1: each point of $M$ has two preimages, one in each half of the cylinder. Local triviality: a small open disc $U$ in $M$ has preimage two disjoint open discs in the cylinder (one in each half), each mapped homeomorphically to $U$ by $\pi$. So $\pi$ is a 2-sheeted covering map.

**Step 3: The deck transformation is $\sigma(s, t) = (s + 1 \mod 2, -t)$.**

> [!note]- Derivation
> A deck transformation $\varphi : S^1 \times (-1, 1) \to S^1 \times (-1, 1)$ satisfies $\pi \circ \varphi = \pi$. Compute: in the cylinder, $\sigma(s, t) := (s + 1 \mod 2, -t)$.
>
> Check $\pi \circ \sigma = \pi$: for $s \in [0, 1]$ with $\sigma(s, t) = (s + 1, -t) \in [1, 2] \times (-1, 1)$, $\pi(s + 1, -t) = (s + 1 - 1, -(-t)) = (s, t) = \pi(s, t)$. Similarly for $s \in [1, 2]$.
>
> $\sigma$ is a homeomorphism (it is its own inverse: $\sigma^2(s, t) = (s + 2 \mod 2, -(-t)) = (s, t)$). It is non-trivial: $\sigma(0, 0) = (1, 0) \neq (0, 0)$.
>
> So $\mathrm{Deck}(S^1 \times (-1, 1) / M) = \{\mathrm{id}, \sigma\} \cong \mathbb{Z}/2$. $\sigma$ is *orientation-reversing* on the cylinder (it reverses $t$, hence the sign of $dt$, hence the sign of $ds \wedge dt$).
>
> Identifying $S^1$ with the unit circle in $\mathbb{C}$ via $s \mapsto e^{i\pi s}$ (so $s \in [0, 2]$ goes once around), the half-translation $s \mapsto s + 1$ corresponds to $z \mapsto -z$ (since $e^{i\pi(s+1)} = e^{i\pi}e^{i\pi s} = -e^{i\pi s}$). So $\sigma$ becomes $(z, t) \mapsto (-z, -t)$ — the "antipodal-and-flip."

**Step 4: The orientation character is non-trivial.**

> [!note]- Derivation
> The Möbius strip $M$ deformation-retracts to its central circle $C$, so $\pi_1(M) = \pi_1(C) = \mathbb{Z}$. The generator $\gamma$ is the once-around traversal of $C$.
>
> The orientation character $w_1 : \pi_1(M) \to \mathbb{Z}/2$ records: traversing a loop in $M$, does orientation reverse? Step 1 verified that traversing $C$ once reverses orientation. So $w_1([\gamma]) = 1 \in \mathbb{Z}/2$, hence $w_1 : \mathbb{Z} \to \mathbb{Z}/2$ is non-trivial — it is the reduction mod 2 homomorphism.
>
> Equivalently: the subgroup $p_*\pi_1(\widetilde M^{\mathrm{or}}, *) \leq \pi_1(M, *)$ is the orientation-preserving subgroup $\ker w_1 = 2\mathbb{Z} \leq \mathbb{Z}$. By [[Thm - Galois Correspondence for Covering Spaces|Galois correspondence]], the orientable double cover corresponds to the subgroup $2\mathbb{Z}$ of index 2.

> [!note]- Complete formal solution
> **Theorem.** The Möbius strip $M = [0, 1] \times (-1, 1) / ((0, y) \sim (1, -y))$ is non-orientable. Its orientable double cover is the cylinder $S^1 \times (-1, 1)$, with covering map $\pi(s, t) = (s, t)$ for $s \in [0, 1]$ and $\pi(s, t) = (s - 1, -t)$ for $s \in [1, 2]$ (where $S^1 = [0, 2]/(0 \sim 2)$). The non-trivial deck transformation is $\sigma(z, t) = (-z, -t)$, an orientation-reversing involution. The orientation character $w_1 : \pi_1(M) = \mathbb{Z} \to \mathbb{Z}/2$ is the reduction-mod-2 homomorphism, non-trivial.
>
> *Proof.* Verified in the steps above.
>
> $\qquad\blacksquare$

> [!warning] Sanity-check: the cylinder is orientable
> Verify: the cylinder $S^1 \times (-1, 1)$ has a global non-vanishing 2-form $d\theta \wedge dt$ (where $\theta$ is the angle on $S^1$), so it is orientable. The deck transformation $\sigma$ reverses this form: $\sigma^*(d\theta \wedge dt) = d(-\theta) \wedge d(-t) = d\theta \wedge dt$... wait, both signs flip, so the product is unchanged. Hmm — let me recompute. $\sigma(z, t) = (-z, -t)$. With $z = e^{i\theta}$, $-z = e^{i(\theta + \pi)}$, so $\theta \to \theta + \pi$. Thus $d\theta \to d\theta$ (translation doesn't affect the form) and $dt \to -dt$. So $\sigma^*(d\theta \wedge dt) = d\theta \wedge (-dt) = -d\theta \wedge dt$. Confirmed: $\sigma$ is orientation-reversing.
>
> The cylinder is orientable, the Möbius strip is not, and the quotient by $\sigma$ (orientation-reversing) is consistent with this: the orientation form on the cylinder doesn't descend to a form on the Möbius strip (because it's negated by $\sigma$), confirming non-orientability of $M$.

---

# Key Takeaways

**The orientable double cover always "unwraps" the orientation reversal.** For any non-orientable manifold $M$, the orientable double cover is built by following each orientation-reversing loop in $M$ to its "other end" in $\widetilde M^{\mathrm{or}}$, where the orientation is consistent. The cover has *exactly* two sheets per fibre point (one for each local orientation), and is connected iff $M$ is non-orientable (a connected non-trivial cover witnesses that orientation cannot be globally chosen on $M$). The trigger condition: a non-orientable manifold with a recognisable orientation-reversing loop. The transferable diagnostic: the orientable double cover construction trivialises the orientation character — what was an obstruction on $M$ becomes a trivial homomorphism on $\widetilde M^{\mathrm{or}}$.

**The orientation character $w_1$ encodes the "topological obstruction" to orientability.** $w_1$ is the first Stiefel-Whitney class of the tangent bundle, viewed as a homomorphism $\pi_1(M) \to \mathbb{Z}/2$. It is trivial iff $M$ is orientable; non-trivial iff non-orientable. The orientable double cover corresponds to the kernel of $w_1$ — a subgroup of index 2 when $w_1$ is non-trivial. The trigger condition: a manifold $M$ with a possibly-non-trivial $w_1$. The transferable diagnostic: any closed loop along which orientation flips is a generator of $w_1$-non-triviality, and the orientable double cover trivialises it by lifting to a path between the two fibre points. This pattern generalises to higher characteristic classes: $w_2$ measures the obstruction to a spin structure, with the spin double cover trivialising it (see [[Spinors and the Dirac Equation]]).

**The orientable double cover doubles the area/volume.** Geometrically, the orientable double cover has twice the area of the original (when $M$ is non-orientable): each "tile" of $M$ corresponds to two tiles in $\widetilde M^{\mathrm{or}}$. Specifically: the Möbius strip has area $1$ (in suitable units), the cylinder has area $2$; the Klein bottle has area $1$, the torus (orientable double cover) has area $2$; $\mathbb{RP}^2$ has area $2\pi$ (for the round metric inherited from the antipodal quotient of unit $S^2$), $S^2$ has area $4\pi = 2 \cdot 2\pi$. This doubling pattern persists in higher dimensions and is the reason "$\int_M f \, d\mu = \tfrac12 \int_{\widetilde M^{\mathrm{or}}} f \circ \pi \, d\tilde\mu$" for $\sigma$-invariant $f$.

**The Möbius strip is the simplest non-orientable example, and the cylinder its orientable double cover.** This pattern repeats across surfaces:
- $\mathbb{RP}^2$ has orientable double cover $S^2$.
- Klein bottle $K$ has orientable double cover $T^2$.
- Non-orientable genus-$g$ surface $N_g$ has orientable double cover the orientable surface $\Sigma_{g-1}$ of genus $g - 1$.

The trigger condition: any non-orientable surface. The transferable diagnostic: the orientable double cover is always one "step up" in some surface classification — non-orientable genus $g$ → orientable genus $g - 1$. This relation is crucial for computing invariants of non-orientable surfaces by lifting to oriented covers. See [[Def - Orientable Double Cover]].
