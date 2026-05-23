---
type: exercise
subject: algebraic-topology
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - The Hopf Map"
  - "Thm - Long Exact Sequence of a Fibration"
  - "Def - Higher Homotopy Group"
tags: [geometry, algebraic-topology, homotopy, hopf]
---

# Problem Statement

Write down the **full** long exact sequence of the Hopf fibration $S^1 \hookrightarrow S^3 \xrightarrow{\eta} S^2$ in all degrees from $\pi_1$ upward. Use it to deduce the homotopy groups of $S^2$ in terms of those of $S^3$ and $S^1$, and in particular show:

(a) $\pi_2(S^2) = \mathbb{Z}$;
(b) $\pi_3(S^2) = \pi_3(S^3) = \mathbb{Z}$ (the Hopf phenomenon);
(c) For $k \geq 3$, $\pi_k(S^2) \cong \pi_k(S^3)$ (an important identification — the high-degree homotopy of $S^2$ matches that of $S^3$, despite $S^2 \neq S^3$).

**Recall:**

![[Def - The Hopf Map#The Definition]]

![[Thm - Long Exact Sequence of a Fibration#Statement]]

Homotopy facts we will use:
- $\pi_1(S^1) = \mathbb{Z}$, $\pi_k(S^1) = 0$ for $k \geq 2$ (universal cover $\mathbb{R}$ contractible).
- $\pi_1(S^3) = \pi_2(S^3) = 0$ (since $S^3$ is 2-connected), $\pi_3(S^3) = \mathbb{Z}$.
- $\pi_1(S^2) = 0$ (since $S^2$ is simply connected).

---

# Convergent Strategy

**Problem class.** This is a **systematic computation of homotopy groups via a fibration** problem. Unlike a single-degree computation, this asks for the structural picture *across all degrees*, exploiting the recursive nature of the long exact sequence to pin down many groups at once.

**Assumption pattern.** The hypothesis is the existence of the Hopf fibration and the known low-degree homotopy of $S^1$, $S^3$. The pattern is that *in every degree above 1*, $\pi_k(S^1) = 0$, so the long exact sequence around degree $k$ simplifies to a short exact sequence $0 \to \pi_k(S^3) \to \pi_k(S^2) \to \pi_{k-1}(S^1) \to 0$. Since $\pi_{k-1}(S^1) = 0$ for $k \geq 3$, this further degenerates to an isomorphism. The degree-2 case is special: $\pi_1(S^1) = \mathbb{Z}$ enters, providing the only place where the boundary map $\partial$ is non-trivial.

**Theorem routing.** The route is to write the long exact sequence in each degree explicitly:
- Degree 1: $\pi_1(S^1) \to \pi_1(S^3) \to \pi_1(S^2) \to 1$, giving $\pi_1(S^2) = 0$.
- Degree 2: $\pi_2(S^1) \to \pi_2(S^3) \to \pi_2(S^2) \to \pi_1(S^1) \to \pi_1(S^3)$, i.e., $0 \to 0 \to \pi_2(S^2) \to \mathbb{Z} \to 0$, giving $\pi_2(S^2) = \mathbb{Z}$.
- Degree $k \geq 3$: $\pi_k(S^1) \to \pi_k(S^3) \to \pi_k(S^2) \to \pi_{k-1}(S^1)$, i.e., $0 \to \pi_k(S^3) \to \pi_k(S^2) \to 0$, giving $\pi_k(S^2) = \pi_k(S^3)$.

**Key decision point.** The structural insight is that *all* higher homotopy of $S^2$ (degrees $\geq 3$) is *equal to that of $S^3$*. This is striking because $S^2$ and $S^3$ are very different spaces: different cohomology, different fundamental class, different dimension. Yet their higher homotopy coincides — because the Hopf fibration $S^1 \to S^3 \to S^2$ has a "small" fibre ($S^1$, contributing nothing in higher degrees) that does not perturb the relationship. This is the genuine content of the exercise: the recursive long-exact-sequence reasoning produces a non-obvious equality.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Algebraic Topology III — Higher Homotopy and Chern Forms#Legal Operations|the topic page's Legal Operations]]:

1. **Compute $\pi_k$ via the long exact sequence of a fibration** (operation 1). Applied systematically across degrees, with the Hopf fibration providing the recurring fibration structure.

2. **Trivial-group sandwich** $0 \to A \to B \to 0 \implies A \cong B$, used repeatedly.

3. **Surjectivity from connectedness** of the fibre: $\pi_1(E) \to \pi_1(B)$ is surjective when the fibre is connected.

---

# Hints

> [!note]- Hint 1
> Write down the long exact sequence of the Hopf fibration *separately* at each degree $k$. The sequence is
> $$\cdots \to \pi_k(S^1) \to \pi_k(S^3) \to \pi_k(S^2) \to \pi_{k-1}(S^1) \to \pi_{k-1}(S^3) \to \cdots$$
> Identify which terms are zero for each $k$.

> [!note]- Hint 2
> $\pi_k(S^1) = 0$ for $k \geq 2$. So for $k \geq 3$, the relevant portion is $0 \to \pi_k(S^3) \to \pi_k(S^2) \to 0$, giving an isomorphism. The only interesting case is $k = 2$, where $\pi_1(S^1) = \mathbb{Z}$ appears.

> [!note]- Hint 3
> At $k = 2$: the relevant portion is $\pi_2(S^3) \to \pi_2(S^2) \to \pi_1(S^1) \to \pi_1(S^3)$, i.e., $0 \to \pi_2(S^2) \to \mathbb{Z} \to 0$ (using $\pi_2(S^3) = \pi_1(S^3) = 0$). So $\pi_2(S^2) = \mathbb{Z}$. The boundary map $\partial : \pi_2(S^2) \to \pi_1(S^1)$ is an isomorphism — the Hopf "winding number" maps to the fundamental class of the fibre $S^1$.

---

# Solution

The proof writes out the long exact sequence at each degree and reads off the resulting computation. The summary table at the end gives the full structure.

**Plan paragraph:** the proof breaks into three regimes: degree 1 (which uses $\pi_1$ of all three spheres), degree 2 (the critical case, where the boundary map $\partial$ from $\pi_2(S^2)$ to $\pi_1(S^1)$ becomes an isomorphism), and degrees $k \geq 3$ (where $\pi_*(S^1) = 0$ in the relevant slots and the long exact sequence collapses to isomorphisms $\pi_k(S^2) = \pi_k(S^3)$). The non-obvious move is in degree 2: the boundary $\partial$ is precisely the *Hopf class* construction — the geometric content of "lifting a 2-sphere in $S^2$ to a 2-disc in $S^3$ with boundary a circle in $S^1$".

**Step 1: Degree 1 — $\pi_1(S^2) = 0$.**

The long exact sequence at degree 1:
$$\pi_1(S^1) \to \pi_1(S^3) \to \pi_1(S^2) \to \pi_0(S^1) \to \pi_0(S^3).$$

> [!note]- Derivation
> Plug in $\pi_1(S^3) = 0$ (since $S^3$ is simply connected, by [[Ex - Pi_n of S^n is Z]] argument or directly), $\pi_0(S^1) = 0$ (since $S^1$ connected), $\pi_0(S^3) = 0$ (since $S^3$ connected):
> $$\mathbb{Z} \to 0 \to \pi_1(S^2) \to 0 \to 0.$$
>
> Exactness at $\pi_1(S^2)$: kernel of $\pi_1(S^2) \to 0$ is $\pi_1(S^2)$ itself; image of $0 \to \pi_1(S^2)$ is zero. So $\pi_1(S^2) = 0$, recovering the simply-connectedness of $S^2$.

**Step 2: Degree 2 — $\pi_2(S^2) = \mathbb{Z}$, with $\partial$ as the isomorphism.**

The long exact sequence at degree 2:
$$\pi_2(S^1) \to \pi_2(S^3) \to \pi_2(S^2) \xrightarrow{\partial} \pi_1(S^1) \to \pi_1(S^3).$$

> [!note]- Derivation
> Plug in $\pi_2(S^1) = 0$, $\pi_2(S^3) = 0$, $\pi_1(S^1) = \mathbb{Z}$, $\pi_1(S^3) = 0$:
> $$0 \to 0 \to \pi_2(S^2) \xrightarrow{\partial} \mathbb{Z} \to 0.$$
>
> Exactness at $\pi_2(S^2)$: $\ker \partial = \mathrm{im}(0 \to \pi_2(S^2)) = 0$, so $\partial$ is injective. Exactness at $\mathbb{Z}$: $\mathrm{im}\,\partial = \ker(\mathbb{Z} \to 0) = \mathbb{Z}$, so $\partial$ is surjective. So $\partial : \pi_2(S^2) \to \mathbb{Z}$ is an isomorphism.
>
> Hence $\pi_2(S^2) = \mathbb{Z}$.
>
> Geometric interpretation of $\partial$: given $[f] \in \pi_2(S^2) = [\mathrm{id}_{S^2}]$, lift $f = \mathrm{id}_{S^2}$ to a 2-disc in $S^3$ via the HLP. The boundary of this disc is a great circle on $S^3$, lying in the fibre $S^1$ over the basepoint of $S^2$. This circle represents a class in $\pi_1(S^1) = \mathbb{Z}$, and it is the *generator*: the lift of the identity sphere wraps the fibre exactly once. This is the Hopf invariant 1.

**Step 3: Degrees $k \geq 3$ — $\pi_k(S^2) = \pi_k(S^3)$.**

The long exact sequence at degree $k \geq 3$:
$$\pi_k(S^1) \to \pi_k(S^3) \to \pi_k(S^2) \to \pi_{k-1}(S^1) \to \pi_{k-1}(S^3).$$

> [!note]- Derivation
> For $k \geq 3$: $\pi_k(S^1) = 0$ and $\pi_{k-1}(S^1) = 0$ (since both $k, k-1 \geq 2$). So:
> $$0 \to \pi_k(S^3) \to \pi_k(S^2) \to 0 \to \cdots.$$
>
> Exactness gives $\pi_k(S^3) \xrightarrow{\sim} \pi_k(S^2)$ as an isomorphism, induced by the Hopf projection $\eta_* : \pi_k(S^3) \to \pi_k(S^2)$.
>
> So for every $k \geq 3$, $\pi_k(S^2) = \pi_k(S^3)$. This is a powerful and non-obvious identification: the higher homotopy of $S^2$ matches that of $S^3$, despite $S^2$ and $S^3$ being very different spaces (different dimension, different cohomology). In particular:
> $$\pi_3(S^2) = \pi_3(S^3) = \mathbb{Z}, \quad \pi_4(S^2) = \pi_4(S^3) = \mathbb{Z}/2, \quad \pi_5(S^2) = \pi_5(S^3) = \mathbb{Z}/2, \quad \ldots$$
> All these computations transfer.

> [!note]- Complete formal solution
> The Hopf fibration $S^1 \hookrightarrow S^3 \xrightarrow{\eta} S^2$ gives a long exact sequence of homotopy groups. We analyse it degree by degree.
>
> **Degree 1.** Using $\pi_1(S^3) = 0$ (since $S^3$ is simply connected) and $\pi_0$ of all three spheres is zero (all connected):
> $$\mathbb{Z} = \pi_1(S^1) \to \pi_1(S^3) = 0 \to \pi_1(S^2) \to 0,$$
> so $\pi_1(S^2) = 0$.
>
> **Degree 2.** Using $\pi_2(S^1) = 0$, $\pi_2(S^3) = 0$, $\pi_1(S^1) = \mathbb{Z}$, $\pi_1(S^3) = 0$:
> $$0 \to \pi_2(S^2) \xrightarrow{\partial} \mathbb{Z} \to 0,$$
> so $\partial$ is an isomorphism and $\pi_2(S^2) = \mathbb{Z}$.
>
> **Degrees $k \geq 3$.** Using $\pi_k(S^1) = \pi_{k-1}(S^1) = 0$:
> $$0 \to \pi_k(S^3) \to \pi_k(S^2) \to 0,$$
> so $\pi_k(S^2) \cong \pi_k(S^3)$ via $\eta_*$.
>
> Summary table:
>
> | $k$ | $\pi_k(S^2)$ | computed via |
> |---|---|---|
> | 1 | $0$ | exact sequence + $S^3$ simply connected |
> | 2 | $\mathbb{Z}$ | $\partial : \pi_2(S^2) \to \pi_1(S^1) = \mathbb{Z}$ isomorphism |
> | 3 | $\mathbb{Z}$ | $\pi_3(S^2) = \pi_3(S^3) = \mathbb{Z}$ (Hopf!) |
> | $k \geq 3$ | $\pi_k(S^3)$ | exact sequence collapses to isomorphism |
>
> $\blacksquare$

---

# Key Takeaways

**The Hopf fibration produces a striking identification: $\pi_k(S^2) = \pi_k(S^3)$ for all $k \geq 3$.** This is the *most surprising consequence* of the Hopf fibration. Two spaces of different dimensions, different singular homology, different cohomology rings — yet identical higher homotopy. The mechanism is that the fibre $S^1$ has trivial $\pi_k$ for $k \geq 2$, so all higher-degree information transfers without obstruction from total space to base. The lesson: *when the fibre is "small" (trivial higher homotopy), the base and total space share all higher homotopy*. This generalises: for any fibration $F \to E \to B$ with $\pi_k(F) = 0$ for $k \geq n$, we have $\pi_k(E) \cong \pi_k(B)$ for $k \geq n$. The Hopf fibration is the cleanest example.

**The boundary map $\partial$ is the geometric Hopf invariant.** In degree 2, $\partial : \pi_2(S^2) \to \pi_1(S^1) = \mathbb{Z}$ is constructed by lifting a 2-sphere in $S^2$ to a 2-disc in $S^3$ with boundary in the fibre $S^1$. The boundary circle is the *Hopf linking* of the lifted disc — and the integer it represents in $\pi_1(S^1) = \mathbb{Z}$ is the Hopf invariant. For the identity sphere $\mathrm{id}_{S^2}$, this is 1 — the linking number of two generic fibres of the Hopf fibration. The lesson: *the boundary map in a fibration's long exact sequence is the topological linking / winding measurement*, and recognising what it geometrically measures is the key to interpreting the algebra.

**Systematic exact-sequence reasoning is the engine of higher-homotopy computation.** This exercise illustrates the power of *writing the long exact sequence at every degree* rather than just one. The result is a complete description of $\pi_*(S^2)$ in terms of $\pi_*(S^3)$, which transfers all the higher-homotopy difficulty from $S^2$ to $S^3$ — a different, but possibly easier, space. The same strategy works for any fibration, and it is the methodology behind Bott periodicity (iterating $SU(n-1) \to SU(n) \to S^{2n-1}$), the computation of $\pi_*$ of all classical Lie groups, and the K-theory periodicity that drives the index theorem. The lesson: *don't compute one homotopy group; compute the whole exact sequence and read off everything*.
