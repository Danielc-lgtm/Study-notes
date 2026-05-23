---
type: exercise
subject: differential-geometry
difficulty: "⭐"
prereqs:
  - "Def - Vector Bundle"
  - "Def - Local Frame"
  - "Def - The Tangent Bundle"
  - "Def - Vector Field on a Manifold"
tags: [geometry, differential-geometry, bundles, trivialization]
---

# Problem Statement

Show that the tangent bundle $TS^1$ of the unit circle $S^1$ is trivial — that is, $TS^1 \cong S^1 \times \mathbb{R}$ as smooth vector bundles over $S^1$.

**Recall:**

A smooth rank-$k$ [[Def - Vector Bundle|vector bundle]] $\pi : E \to M$ is **trivial** if it is isomorphic over $M$ to the product bundle $M \times \mathbb{R}^k \to M$. Equivalently, by [[Def - Local Frame|the local frame / trivialization equivalence]], a vector bundle is trivial if and only if it admits a smooth **global frame** — a tuple of smooth global sections whose values are a basis of every fibre.

The [[Def - The Tangent Bundle|tangent bundle]] $TS^1 = \bigsqcup_{p \in S^1} T_p S^1$ is a smooth rank-$1$ vector bundle over $S^1$. To show $TS^1 \cong S^1 \times \mathbb{R}$, it suffices to find a nowhere-vanishing smooth global vector field on $S^1$ — a smooth global section of $TS^1$ that is nonzero at every point.

---

# Convergent Strategy

**Problem class:** Triviality of a rank-$1$ vector bundle. A line bundle is trivial if and only if it has a nowhere-vanishing global section, by the local-frame criterion. So the strategy is to exhibit such a section.

**Assumption pattern:** $S^1$ is a 1-dimensional manifold with a natural global vector field — the angular velocity field $\partial/\partial\theta$, well-defined globally because the chart transition between $\theta$ and $\theta + 2\pi$ has trivial Jacobian (equal to $1$). So we have a candidate nowhere-vanishing global section in hand.

**Theorem routing:** Use the equivalence between global frames and global trivializations ([[Def - Local Frame]] applied with $U = M$). A nowhere-vanishing smooth global section of a rank-$1$ bundle is a global frame, hence yields a global trivialization $TS^1 \to S^1 \times \mathbb{R}$. The trivialization explicitly is $v \cdot (\partial/\partial\theta)_p \mapsto (p, v)$.

**Key decision point:** The non-obvious choice is to use the *angular* coordinate's vector field rather than trying to construct a global trivialization from scratch. The angular coordinate $\theta$ is not a single globally-defined function on $S^1$ (different branches differ by $2\pi$), but its differential $d\theta$ and its dual coordinate vector field $\partial/\partial\theta$ are both globally defined because of the trivial Jacobian.

---

# Legal Operations Used

1. **Operation 4 from the topic page (write a section in a local frame).** The single global section $\partial/\partial\theta$ trivializes the bundle.

2. **Operation 10 from the topic page (read off transition functions).** The transition function between two angular charts (say, $S^1 \setminus \{1\}$ and $S^1 \setminus \{-1\}$) has trivial Jacobian, because both charts use angle coordinates with $\tilde\theta = \theta + 2\pi k$ for some integer $k$ — the chart transition has Jacobian $1$.

3. **Operation 1 from the topic page (trivialize locally — extended to global).** Exhibiting a global frame is a global trivialization; the local-frame-trivialization equivalence does the work.

---

# Hints

> [!note]- Hint 1
> Recall that a rank-$1$ vector bundle is trivial if and only if it admits a nowhere-vanishing global section. The question reduces to: does $S^1$ admit a nowhere-vanishing smooth vector field?

> [!note]- Hint 2
> Consider the angular coordinate $\theta$ on $S^1$. Although $\theta$ is multi-valued (defined only modulo $2\pi$), the vector field $\partial/\partial\theta$ is globally well-defined. Why?

> [!note]- Hint 3
> In two charts $\theta$ and $\tilde\theta = \theta + 2\pi$ (or any shift), the Jacobian $\partial\tilde\theta/\partial\theta = 1$. So $\partial/\partial\tilde\theta = \partial/\partial\theta$ on the overlap. The vector field $\partial/\partial\theta$ does not depend on the choice of $\theta$ branch.

---

# Solution

**Plan:** Exhibit the angular vector field $\partial/\partial\theta$ as a smooth nowhere-vanishing global section of $TS^1$. This is a global frame for the rank-$1$ bundle, hence the bundle is trivial. The explicit trivialization is the map sending a tangent vector $v \cdot (\partial/\partial\theta)_p$ to the pair $(p, v) \in S^1 \times \mathbb{R}$.

**Step 1: The angular vector field $\partial/\partial\theta$ is a smooth, nowhere-vanishing global section of $TS^1$.**

> [!note]- Derivation
> Choose two charts on $S^1$: $(U_1, \theta_1)$ with $U_1 = S^1 \setminus \{1\}$ and $\theta_1$ taking values in $(0, 2\pi)$, and $(U_2, \theta_2)$ with $U_2 = S^1 \setminus \{-1\}$ and $\theta_2$ taking values in $(-\pi, \pi)$. On each chart, the coordinate vector field $\partial/\partial\theta_i$ is a smooth nowhere-vanishing local section.
>
> On the overlap $U_1 \cap U_2$, which consists of the upper and lower open arcs, the chart transition is $\theta_2 = \theta_1$ on the upper arc (when $\theta_1 \in (0, \pi)$, $\theta_2 = \theta_1$) and $\theta_2 = \theta_1 - 2\pi$ on the lower arc (when $\theta_1 \in (\pi, 2\pi)$, $\theta_2 = \theta_1 - 2\pi$). In both cases the Jacobian $\partial\theta_2/\partial\theta_1 = 1$.
>
> So $\partial/\partial\theta_1 = (\partial\theta_1/\partial\theta_2) \partial/\partial\theta_2 = 1 \cdot \partial/\partial\theta_2 = \partial/\partial\theta_2$ on the overlap.
>
> The two local vector fields agree on the overlap, so they glue into a single smooth global vector field on all of $S^1$. Call it $X = \partial/\partial\theta$. It is nowhere vanishing because in each chart it is the nonzero coordinate vector field.

**Step 2: A nowhere-vanishing global section of a rank-$1$ bundle is a global frame.**

> [!note]- Derivation
> A rank-$1$ vector bundle has 1-dimensional fibres. A single section whose value at $p$ is nonzero spans the fibre $E_p$ (a 1-dimensional vector space spanned by any nonzero vector). A nowhere-vanishing section therefore provides a basis at every point — a global frame in the sense of [[Def - Local Frame]].

**Step 3: A global frame gives a global trivialization.**

> [!note]- Derivation
> By the local-frame–trivialization equivalence ([[Def - Local Frame]]), a global frame $\sigma_1, \dots, \sigma_k$ for a rank-$k$ bundle gives the global trivialization
> $$\Phi : E \to M \times \mathbb{R}^k, \quad v^i \sigma_i(p) \mapsto (p, v^1, \dots, v^k).$$
> In our case $k = 1$ and the frame is $\sigma_1 = \partial/\partial\theta$. The trivialization is
> $$\Phi : TS^1 \to S^1 \times \mathbb{R}, \quad v \cdot (\partial/\partial\theta)_p \mapsto (p, v).$$
> This is a smooth bundle isomorphism over $S^1$.

> [!note]- Complete formal solution
> Define the smooth global vector field $X := \partial/\partial\theta$ on $S^1$ as follows. On the chart $(U_1, \theta_1)$ with $U_1 = S^1 \setminus \{1\}$ and $\theta_1 : U_1 \to (0, 2\pi)$, set $X|_{U_1} := \partial/\partial\theta_1$. On the chart $(U_2, \theta_2)$ with $U_2 = S^1 \setminus \{-1\}$ and $\theta_2 : U_2 \to (-\pi, \pi)$, set $X|_{U_2} := \partial/\partial\theta_2$. On the overlap $U_1 \cap U_2$ (two open arcs), the chart transition has Jacobian $\partial\theta_2 / \partial\theta_1 = 1$, so $\partial/\partial\theta_1 = \partial/\partial\theta_2$ on the overlap. The two local definitions of $X$ therefore agree on the overlap and glue into a smooth global section $X \in \Gamma(TS^1)$.
>
> $X$ is nowhere vanishing: on each chart, it equals the coordinate vector field, which is nowhere zero (a basis of the fibre at each point).
>
> Define $\Phi : TS^1 \to S^1 \times \mathbb{R}$ by $\Phi(v \cdot X_p) = (p, v)$. This is well-defined (every element of $T_p S^1$ has a unique expression $v \cdot X_p$ since $X_p$ is a basis), bijective, and smooth (smoothness in coordinates is immediate). The inverse $\Phi^{-1}(p, v) = v \cdot X_p$ is also smooth. So $\Phi$ is a smooth bundle isomorphism, and $TS^1 \cong S^1 \times \mathbb{R}$ as smooth vector bundles over $S^1$. $\qquad\blacksquare$

---

# Key Takeaways

**Triviality of a line bundle is detected by a nowhere-vanishing global section.** This is the cleanest test for line-bundle triviality, and it appears in every line-bundle problem. The pattern: to show a rank-$1$ bundle is trivial, exhibit a nowhere-vanishing global section. To show it is not trivial, prove no such section can exist (typically by a topological obstruction). For higher-rank bundles, the analogous criterion is the existence of a global frame ($k$ linearly independent global sections), which is strictly stronger than the existence of one nowhere-vanishing global section.

**The angular vector field $\partial/\partial\theta$ is globally well-defined despite the angular coordinate being multi-valued.** This is a subtle but important point. The coordinate $\theta$ is defined only modulo $2\pi$, so it is not a globally well-defined function on $S^1$. However, the coordinate vector field $\partial/\partial\theta$ *is* globally well-defined because the chart transition is a shift by $2\pi$, which has Jacobian $1$. The general principle: a coordinate-related geometric object survives globally if it is invariant under the chart transitions. Vector fields like $\partial/\partial\theta$ survive on $S^1$; the function $\theta$ itself does not.

**Manifolds with global vector fields are called "parallelizable", and they form a special class.** $S^1$ is parallelizable (has a global frame on $TM$); so are all Lie [[Def - Group|groups]] (left-invariant vector fields form a global frame); so are $S^3$ and $S^7$ via their quaternion and octonion structures. But $S^2, S^4, S^5, S^6, S^8, \dots$ are all *not* parallelizable — the hairy ball theorem says $S^2$ has no nowhere-vanishing vector field, and similar obstructions exist for higher even-dimensional spheres. The classification of parallelizable spheres (Bott, Milnor, Kervaire) is one of the deep results of algebraic topology: only $S^0, S^1, S^3, S^7$ are parallelizable. The companion exercise [[Ex - The Möbius Bundle is Nontrivial]] is the opposite extreme — a low-dimensional non-parallelizable bundle.
