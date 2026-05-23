---
type: exercise
subject: differential-geometry
difficulty: "⭐"
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Smooth Map between Manifolds"
  - "Thm - Smooth Maps are Continuous"
tags: [geometry, differential-geometry]
---

# Problem Statement

Let $M, N, P$ be smooth manifolds and let $F : M \to N$ and $G : N \to P$ be smooth maps. Show that the composition $G \circ F : M \to P$ is smooth.

**Recall:**

A smooth map $F : M \to N$ is smooth in the sense of:

![[Def - Smooth Map between Manifolds#The Definition]]

A key consequence is:

![[Thm - Smooth Maps are Continuous#Statement]]

The Euclidean-space fact we will use is that *composition of smooth Euclidean maps is smooth*: if $\widehat F : \widetilde U \to \widetilde V$ and $\widehat G : \widetilde V \to \widetilde W$ are smooth maps between open subsets of Euclidean spaces, then $\widehat G \circ \widehat F$ is smooth (by the chain rule applied iteratively to all partial derivatives).

---

# Convergent Strategy

**Problem class:** Verification of smoothness for an explicitly constructed map. This is the canonical "chart-pulling-back" verification problem in §2.1 — the routine is to pick charts on each manifold, write the coordinate representation, recognize it as a composition of smooth Euclidean maps. The problem-solving strategy of the topic page applies directly: smoothness of a manifold map reduces to smoothness of its Euclidean coordinate representation.

**Assumption pattern:** We have two smooth maps $F$ and $G$. Each "smooth" comes with the package: for any point in the source, there is a chart pair where the coordinate representation is smooth, *and* the source chart's image is contained in the target chart (the chart-containment condition). For the composition $G \circ F$, we need to build a chart pair at any given $p \in M$ that witnesses smoothness of $G \circ F$ at $p$. The chart at $p$ comes from $F$'s smoothness; the chart at $G(F(p))$ comes from $G$'s smoothness; the middle chart, at $F(p)$, must witness both $F$'s smoothness at $p$ (mapping into) and $G$'s smoothness at $F(p)$ (mapping out of). The non-obvious work is reconciling these two different chart choices at $F(p)$ — and continuity of $F$ saves the day.

**Theorem routing:** Pick a chart $(W, \rho)$ on $P$ around $G(F(p))$ such that some chart $(V, \psi)$ on $N$ around $F(p)$ satisfies $G(V) \subseteq W$ and $\rho \circ G \circ \psi^{-1}$ is smooth (from $G$'s smoothness). Then pick a chart $(U, \varphi)$ on $M$ around $p$ such that $F(U) \subseteq V$ and $\psi \circ F \circ \varphi^{-1}$ is smooth — but this needs care: the chart provided by "$F$ is smooth at $p$" maps into *some* chart around $F(p)$, not necessarily $V$. The fix uses **continuity of $F$** (from [[Thm - Smooth Maps are Continuous]]): $F^{-1}(V)$ is open, and we can shrink $U$ to $U \cap F^{-1}(V)$ to ensure $F(U) \subseteq V$.

**Key decision point:** The non-obvious move is recognizing that we should *not* directly use the chart from "$F$ smooth at $p$" — that chart might map into a chart around $F(p)$ that is *not* the one we picked for $G$. Instead, we work *backwards*: first pick the chart on $N$ around $F(p)$ that we want $G$ to act on; then shrink the chart on $M$ around $p$ to ensure $F$ maps into that chosen chart on $N$. The shrinking step uses continuity, which is provided by [[Thm - Smooth Maps are Continuous]].

---

# Legal Operations Used

1. **Pull back to charts to check smoothness (operation 1 from the topic page).** We reduce smoothness of $G \circ F$ at $p$ to smoothness of a Euclidean coordinate representation, which is the chart-pull-back trick.

2. **Use chart containment $F(U) \subseteq V$ (operation 2 from the topic page).** We ensure the coordinate composition is well-defined by shrinking $U$ to satisfy the containment.

3. **Build smooth maps by composition (operation 3 from the topic page).** Once the Euclidean coordinate representation is a composition of smooth Euclidean maps, we invoke the Euclidean-level fact that compositions of smooth maps are smooth — applied to the composition $\widehat G \circ \widehat F$.

---

# Hints

> [!note]- Hint 1
> Fix a point $p \in M$. You want to find a chart pair on $M$ and $P$ that witnesses smoothness of $G \circ F$ at $p$. You have two smoothness hypotheses — start by picking the chart on $P$ around $G(F(p))$ from $G$'s smoothness, and figure out the chart on $N$ around $F(p)$ that comes with it.

> [!note]- Hint 2
> Once you have a chart $(V, \psi)$ on $N$ around $F(p)$ from $G$'s smoothness data, you need a chart $(U, \varphi)$ on $M$ around $p$ with $F(U) \subseteq V$. Continuity of $F$ (from [[Thm - Smooth Maps are Continuous]]) gives you $F^{-1}(V)$ open, and intersecting with the chart from $F$'s smoothness data shrinks to a chart contained in $F^{-1}(V)$.

> [!note]- Hint 3
> The coordinate representation of $G \circ F$ in the chart pair $((U, \varphi), (W, \rho))$ is $\rho \circ G \circ F \circ \varphi^{-1}$. Insert $\psi^{-1} \psi$ in the middle to write it as $(\rho \circ G \circ \psi^{-1}) \circ (\psi \circ F \circ \varphi^{-1}) = \widehat G \circ \widehat F$ — a composition of smooth Euclidean maps.

---

# Solution

The proof is the canonical "chart-pulling-back" argument: at any point $p \in M$, pick charts that witness both $F$'s and $G$'s smoothness around $p$, $F(p)$, $G(F(p))$ respectively, ensure the chart-containment conditions by shrinking via continuity, then write the coordinate representation of $G \circ F$ as a composition of smooth Euclidean maps. The three steps are: pick charts via the smoothness hypotheses, shrink the source chart via continuity to satisfy the containment, and recognize the resulting coordinate representation as a composition of smooth Euclidean maps. The non-obvious step is the shrinking, which requires continuity of $F$ (a separate theorem).

**Step 1: pick charts using the smoothness of $G$.**

Since $G$ is smooth at $F(p)$, there exist smooth charts $(V, \psi)$ on $N$ with $F(p) \in V$ and $(W, \rho)$ on $P$ with $G(F(p)) \in W$ such that $G(V) \subseteq W$ and the coordinate representation $\widehat G = \rho \circ G \circ \psi^{-1} : \psi(V) \to \rho(W)$ is smooth.

> [!note]- Derivation
> The smoothness of $G$ at $F(p) \in N$ is invoked, directly from [[Def - Smooth Map between Manifolds]]. The definition supplies the existence of the chart pair $((V, \psi), (W, \rho))$ with the chart containment $G(V) \subseteq W$ and the smoothness of $\widehat G$. Nothing more is needed for this step.

**Step 2: shrink the source chart using continuity of $F$.**

Since $F$ is smooth, it is continuous (by [[Thm - Smooth Maps are Continuous]]). Hence $F^{-1}(V)$ is open in $M$ and contains $p$ (since $F(p) \in V$). The smoothness of $F$ at $p$ gives a chart $(U_0, \varphi)$ on $M$ with $p \in U_0$ and some chart $(V_0, \psi_0)$ on $N$ with $F(p) \in V_0$, $F(U_0) \subseteq V_0$, and $\psi_0 \circ F \circ \varphi^{-1}$ smooth. Set $U = U_0 \cap F^{-1}(V)$, an open neighbourhood of $p$ in $M$; restrict $\varphi$ to $U$ (still a smooth chart, on the smaller open set, with the smooth structure inherited).

On $U$, $F(U) \subseteq F(U_0) \cap V = (F(U_0) \cap V) \subseteq V$.

> [!note]- Derivation
> The chart-containment in the smoothness of $F$ at $p$ gives some chart on $N$, but it might not be $V$ — it might be a different chart $V_0$ around $F(p)$. To get a chart on $M$ that maps into $V$ (not just into $V_0$), we use continuity.
>
> Continuity of $F$ (Theorem [[Thm - Smooth Maps are Continuous]]) gives $F^{-1}(V)$ open in $M$, and it contains $p$. The intersection $U_0 \cap F^{-1}(V)$ is open in $M$, contains $p$, and is contained in $U_0$ (where $F$ has the chart-by-chart smoothness data we can use).
>
> The restriction of $\varphi$ to $U$ is still a smooth chart: any restriction of a smooth chart to an open subset is a smooth chart (compatible with the maximal atlas). On $U$, $F(U) \subseteq V$ by construction.
>
> Furthermore, on $U$, the coordinate representation $\psi \circ F \circ \varphi^{-1}$ (mapping $\varphi(U) \to \psi(V)$) is well-defined and smooth, because:
> - The chart-pulled-back map $\psi_0 \circ F \circ \varphi^{-1}|_{\varphi(U_0)}$ is smooth (from $F$'s smoothness data);
> - On $U$, restricting to $\varphi(U) \subseteq \varphi(U_0)$, this is $\psi_0 \circ F \circ \varphi^{-1}|_{\varphi(U)}$;
> - Composing with the transition map $\psi \circ \psi_0^{-1} : \psi_0(V \cap V_0) \to \psi(V \cap V_0)$ (smooth, since $\{V, V_0\}$ are both in the smooth atlas of $N$), we get $\psi \circ F \circ \varphi^{-1}$ on $\varphi(U)$.
>
> So $\widehat F = \psi \circ F \circ \varphi^{-1}$ is smooth on $\varphi(U)$, taking values in $\psi(V)$.

**Step 3: recognize $\widehat{G \circ F}$ as a composition of smooth Euclidean maps.**

The coordinate representation of $G \circ F$ in the chart pair $((U, \varphi), (W, \rho))$ is
$$\widehat{G \circ F} = \rho \circ (G \circ F) \circ \varphi^{-1} = (\rho \circ G \circ \psi^{-1}) \circ (\psi \circ F \circ \varphi^{-1}) = \widehat G \circ \widehat F : \varphi(U) \to \rho(W).$$

Both $\widehat G$ and $\widehat F$ are smooth Euclidean maps (by Steps 1 and 2), so their composition $\widehat{G \circ F}$ is smooth.

The chart pair $((U, \varphi), (W, \rho))$ with $(G \circ F)(U) \subseteq G(F(U)) \subseteq G(V) \subseteq W$ thus witnesses the smoothness of $G \circ F$ at $p$.

> [!note]- Derivation
> The composition manipulation $\rho \circ G \circ F \circ \varphi^{-1} = (\rho \circ G \circ \psi^{-1}) \circ (\psi \circ F \circ \varphi^{-1})$ is the standard "insert $\psi^{-1} \psi$" trick. We rewrite the composition by inserting an extra pair $(\psi^{-1}, \psi)$ that cancels itself, but allows the composition to be parsed as $\widehat G$ applied to $\widehat F$.
>
> Verifying the chart-containment $(G \circ F)(U) \subseteq W$:
> $F(U) \subseteq V$ from Step 2, $G(V) \subseteq W$ from Step 1, so $(G \circ F)(U) = G(F(U)) \subseteq G(V) \subseteq W$.
>
> The smoothness of $\widehat G \circ \widehat F$ as a Euclidean map is the standard chain-rule fact: composition of smooth maps between Euclidean open sets is smooth. (This is multivariable calculus, not a manifold theorem.)

Since $p$ was arbitrary, $G \circ F$ is smooth at every point of $M$, hence smooth on $M$. $\quad\blacksquare$

> [!note]- Complete formal solution
> **Theorem.** If $F : M \to N$ and $G : N \to P$ are smooth maps between smooth manifolds, then $G \circ F : M \to P$ is smooth.
>
> *Proof.* Let $p \in M$. We show smoothness of $G \circ F$ at $p$.
>
> Since $G$ is smooth at $F(p)$, there are smooth charts $(V, \psi)$ on $N$ with $F(p) \in V$ and $(W, \rho)$ on $P$ with $G(F(p)) \in W$ such that $G(V) \subseteq W$ and $\widehat G = \rho \circ G \circ \psi^{-1} : \psi(V) \to \rho(W)$ is smooth.
>
> Since $F$ is smooth at $p$, there are smooth charts $(U_0, \varphi)$ on $M$ with $p \in U_0$ and $(V_0, \psi_0)$ on $N$ with $F(p) \in V_0$ such that $F(U_0) \subseteq V_0$ and $\psi_0 \circ F \circ \varphi^{-1} : \varphi(U_0) \to \psi_0(V_0)$ is smooth.
>
> Since $F$ is continuous ([[Thm - Smooth Maps are Continuous]]) and $V$ is open in $N$, $F^{-1}(V)$ is open in $M$. Set $U = U_0 \cap F^{-1}(V)$, an open neighbourhood of $p$ in $M$ contained in $U_0$. On $U$, $F(U) \subseteq V$ by construction, and the chart $(U, \varphi|_U)$ is a smooth chart on $M$ (restriction of a smooth chart to an open subset).
>
> The transition map $\psi \circ \psi_0^{-1}$ is smooth (both charts in the smooth atlas of $N$). On $\varphi(U)$,
> $$\psi \circ F \circ \varphi^{-1} = (\psi \circ \psi_0^{-1}) \circ (\psi_0 \circ F \circ \varphi^{-1})$$
> is the composition of smooth Euclidean maps, hence smooth.
>
> Then the coordinate representation of $G \circ F$ in the chart pair $((U, \varphi|_U), (W, \rho))$ is
> $$\widehat{G \circ F} = \rho \circ (G \circ F) \circ \varphi^{-1} = (\rho \circ G \circ \psi^{-1}) \circ (\psi \circ F \circ \varphi^{-1}),$$
> a composition of smooth Euclidean maps, hence smooth. The chart containment $(G \circ F)(U) \subseteq W$ holds because $F(U) \subseteq V$ and $G(V) \subseteq W$.
>
> So $G \circ F$ is smooth at $p$. Since $p$ was arbitrary, $G \circ F$ is smooth on $M$. $\quad\blacksquare$

---

# Key Takeaways

**Smoothness verification routes through chart-pulling-back.** The proof template is the same in every smoothness verification problem: pick charts on each manifold around the relevant points, satisfy the chart-containment conditions, write the coordinate representation, recognize it as a composition of smooth Euclidean maps. The verification at the manifold level *always* reduces to a verification at the Euclidean level, and the Euclidean-level work is multivariable calculus. The trigger to recognize this routine is any sentence demanding smoothness of a constructed map — and the smooth-atlas axiom is what makes the chart-pull-back well-defined. This pattern repeats in every chapter of differential geometry: every operation defined at the manifold level reduces to operations on Euclidean coordinate representations via charts, and the smoothness of the manifold-level operation reduces to the smoothness of the Euclidean version.

**The chart-containment $F(U) \subseteq V$ is the technical pivot.** The smoothness definition demands not just that the coordinate representation be smooth, but that the source chart's image be contained in the target chart. This is not a technicality — it is what makes smoothness imply continuity, and what makes the proof of "composition is smooth" require continuity as a separate input. Whenever you construct a chart pair witnessing smoothness, *always* shrink the source chart to satisfy the containment; the shrinking uses continuity, which is itself a consequence of smoothness. The recurring trigger-reaction is: "I need a chart pair, but my source chart doesn't map into the target chart I want" $\Rightarrow$ "shrink the source chart by intersecting with $F^{-1}(\text{target chart})$, using continuity of $F$".

**The "insert $\psi^{-1} \psi$" trick is the basic compositional move.** When writing the coordinate representation of a composition, the natural manipulation is to insert a chart and its inverse in the middle: $\rho \circ G \circ F \circ \varphi^{-1} = (\rho \circ G \circ \psi^{-1}) \circ (\psi \circ F \circ \varphi^{-1})$. This converts a single coordinate representation involving four maps (chart, $F$, $G$, chart) into a composition of two coordinate representations, each of which is recognized as smooth by hypothesis. The trick generalizes: whenever a chain of manifold maps needs to be analyzed in coordinates, insert chart-inverse pairs at each "joint" of the chain to break the analysis into smaller pieces, each tractable by the smoothness hypotheses of the individual maps. This is the same algebraic move as inserting identity in the middle of a matrix product to insert a basis change, and it is the conceptual core of "composition of smooth maps is smooth".

This exercise sets the routine for every smoothness verification — projections, inclusions, quotient maps, [[Def - Group|group]] operations on Lie [[Def - Group|groups]] — and the move "chart on the target, then shrink the source chart via continuity, then recognize the coordinate composition as smooth" is the constant move throughout differential geometry.
