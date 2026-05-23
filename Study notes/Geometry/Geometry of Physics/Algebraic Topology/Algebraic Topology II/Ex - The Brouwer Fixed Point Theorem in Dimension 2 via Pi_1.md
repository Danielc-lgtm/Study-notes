---
type: exercise
subject: algebraic-topology
difficulty: "⭐⭐"
prereqs:
  - "Thm - Pi_1 of S^1 is Z"
  - "Def - Path-Product and the Fundamental Group"
  - "Def - Continuous Map"
tags: [geometry, algebraic-topology, fixed-points]
---

# Problem Statement

Prove the **Brouwer fixed-point theorem in dimension 2**: every continuous map $f : D^2 \to D^2$ from the closed unit disc to itself has a fixed point ($f(x) = x$ for some $x \in D^2$).

The strategy uses $\pi_1(S^1) = \mathbb{Z}$ via the **no-retraction theorem**: there is no continuous retraction $D^2 \to S^1 = \partial D^2$. Assume $f$ has no fixed point; construct a continuous retraction $D^2 \to S^1$; obtain a contradiction.

**Recall:**

The fundamental group of the circle:

![[Thm - Pi_1 of S^1 is Z#Statement]]

The fundamental group (definition):

![[Def - Path-Product and the Fundamental Group#The Definition]]

**Definition (retraction).** A continuous map $r : X \to A$ for $A \subseteq X$ is a **retraction** if $r|_A = \mathrm{id}_A$. Equivalently, $r \circ i = \mathrm{id}_A$ where $i : A \hookrightarrow X$ is the inclusion.

---

# Convergent Strategy

**Problem class:** Topological obstruction argument using $\pi_1$ functoriality. The pattern is: assume the conclusion fails; derive a continuous map (here, a retraction) whose existence is forbidden by a $\pi_1$-computation. The proof crystallises the use of $\pi_1$ as an obstruction tool — it converts a geometric impossibility into an algebraic impossibility.

**Assumption pattern:** Suppose $f : D^2 \to D^2$ has no fixed point. Then for each $x \in D^2$, the ray from $f(x)$ through $x$ is well-defined (since $f(x) \neq x$) and uniquely intersects $\partial D^2 = S^1$ in a single point — call it $r(x)$. The function $r : D^2 \to S^1$ is continuous (joint-continuity of "intersection point of a ray with a circle" in the ray's data), and on the boundary $r|_{S^1} = \mathrm{id}_{S^1}$ (because for $x \in S^1$, the ray from $f(x)$ through $x$ exits the disc at $x$ itself). So $r$ is a continuous retraction.

**Theorem routing:** Apply $\pi_1$ functoriality. The inclusion $i : S^1 \hookrightarrow D^2$ induces $i_* : \pi_1(S^1) = \mathbb{Z} \to \pi_1(D^2) = 0$. The retraction $r : D^2 \to S^1$ induces $r_* : \pi_1(D^2) = 0 \to \pi_1(S^1) = \mathbb{Z}$. The composition $r \circ i = \mathrm{id}_{S^1}$, so $r_* \circ i_* = \mathrm{id}_{\mathbb{Z}}$. But this requires the trivial group $0$ to surject onto $\mathbb{Z}$ (via $r_*$) — impossible. Contradiction.

**Key decision point:** The geometric construction of the retraction $r$ from the no-fixed-point assumption is the crux. People often see "ray from $f(x)$ through $x$" without realising continuity. The continuity argument: the ray's data ($f(x)$ and $x$) are continuous in $x$, and the intersection of a ray with a circle (a smooth curve in the plane of disc-radius coordinates) is continuous in the ray's data. The technical step is the joint continuity, not the formula. Once the retraction exists, the $\pi_1$-obstruction is immediate.

---

# Legal Operations Used

1. **Operation 7 from the topic page (use functoriality to obstruct or construct).** The continuous retraction $r : D^2 \to S^1$ would induce a homomorphism $r_* : \pi_1(D^2) = 0 \to \pi_1(S^1) = \mathbb{Z}$. The composition with the inclusion $i_*$ would equal the identity on $\mathbb{Z}$. But the composition factors through $\pi_1(D^2) = 0$, so the composition is the zero map, not the identity. Contradiction.

2. **Operation 1 from the topic page (lift a path).** The argument that $\pi_1(D^2) = 0$ uses path-lifting / direct contraction (the disc is convex, so every loop contracts via straight-line homotopy).

3. **Operation 5 from the topic page (Seifert-van Kampen, indirectly).** $\pi_1(D^2) = 0$ can also be deduced from contractibility of $D^2$; or via Seifert-van Kampen with $D^2 = D^2 \cup D^2$ (silly but valid: $D^2$ as a CW complex has a single 0-cell, no 1-cells, one 2-cell; Seifert-van Kampen with the 2-cell attached to the trivial 1-skeleton gives $\pi_1 = 0$).

---

# Hints

> [!note]- Hint 1
> Suppose for contradiction $f : D^2 \to D^2$ has no fixed point. For each $x \in D^2$, can you define a continuous map $r(x) \in S^1$ using the geometry of $f(x)$ and $x$?

> [!note]- Hint 2
> For each $x$, the vector from $f(x)$ to $x$ points in a definite direction (since $f(x) \neq x$). Extend this ray from $f(x)$ through $x$ until it hits the boundary $\partial D^2 = S^1$ at some point $r(x)$. Define $r : D^2 \to S^1$ by this construction.

> [!note]- Hint 3
> Verify: $r$ is continuous (the ray's intersection with $S^1$ is a continuous function of the ray's data). $r$ restricted to $S^1$ is the identity (for $x \in S^1$, the ray from $f(x)$ through $x$ exits at $x$ itself). So $r$ is a continuous retraction $D^2 \to S^1$.

> [!note]- Hint 4
> Apply $\pi_1$ functoriality. $r \circ i = \mathrm{id}_{S^1}$ implies $r_* \circ i_* = \mathrm{id}_{\pi_1(S^1)} = \mathrm{id}_{\mathbb{Z}}$. But $r_*$ factors through $\pi_1(D^2) = 0$, so $r_* \circ i_*$ is the zero homomorphism, not the identity. Contradiction.

---

# Solution

**Plan:** Three steps. (1) Assume no fixed point and construct the retraction $r : D^2 \to S^1$ geometrically. (2) Apply $\pi_1$ functoriality to derive an impossible factorisation through the trivial group. (3) Conclude $f$ must have a fixed point.

**Step 1: Construct the retraction $r : D^2 \to S^1$ from the no-fixed-point assumption.**

> [!note]- Derivation
> Assume $f : D^2 \to D^2$ is continuous with no fixed point: $f(x) \neq x$ for all $x \in D^2$.
>
> For each $x \in D^2$, the vector $x - f(x) \neq 0$, so the ray $\{f(x) + t(x - f(x)) : t \geq 0\}$ is well-defined. This ray starts at $f(x)$ (when $t = 0$), passes through $x$ (when $t = 1$), and extends outward. The ray must exit the unit disc $D^2$ at exactly one point on the boundary $S^1$ (since the disc is convex and the ray is a half-line). Call this exit point $r(x) \in S^1$.
>
> *Explicit formula:* $r(x) = f(x) + t^*(x - f(x))$ where $t^* = t^*(x) \geq 1$ is the unique solution to $|f(x) + t(x - f(x))| = 1$. This is a quadratic in $t$ with one root in $[1, \infty)$ (the exit) and possibly another in $(-\infty, 0]$ (the entry, if applicable); pick the positive larger root.
>
> *Continuity of $r$:* The exit point varies continuously in the ray's data $(f(x), x)$ by continuity of $f$ and continuity of "ray-circle intersection" in the ray's parameters. (Standard exercise in real analysis or basic topology; one can compute $t^*$ explicitly as the positive root of $|f(x)|^2 + 2t \langle f(x), x - f(x) \rangle + t^2 |x - f(x)|^2 = 1$, a quadratic with continuous coefficients, so its larger root depends continuously on coefficients.)
>
> *Retraction property:* For $x \in S^1$ (the boundary), $|x| = 1$. The ray from $f(x)$ through $x$ exits $D^2$ at $x$ itself (the ray heads outward from $x$ since $|x - f(x)| > 0$ and $x$ is already on $\partial D^2$). So $r(x) = x$ for all $x \in S^1$, i.e., $r|_{S^1} = \mathrm{id}_{S^1}$.
>
> So $r : D^2 \to S^1$ is a continuous retraction.

**Step 2: Derive a contradiction via $\pi_1$ functoriality.**

> [!note]- Derivation
> Let $i : S^1 \hookrightarrow D^2$ be the inclusion. The relation $r \circ i = \mathrm{id}_{S^1}$ implies on $\pi_1$:
> $$r_* \circ i_* = (\mathrm{id}_{S^1})_* = \mathrm{id}_{\pi_1(S^1)}.$$
> Now apply $\pi_1$:
> - $\pi_1(S^1, *) = \mathbb{Z}$ by [[Thm - Pi_1 of S^1 is Z|the flagship theorem]].
> - $\pi_1(D^2, *) = 0$: the disc is convex, hence every loop contracts via the straight-line homotopy $H(s, t) = (1 - t)\gamma(s) + t \cdot *$.
>
> So $i_* : \mathbb{Z} \to 0$ is the zero homomorphism (the only homomorphism into the trivial group), and $r_* : 0 \to \mathbb{Z}$ is also the zero homomorphism (the only homomorphism from the trivial group). The composition $r_* \circ i_* : \mathbb{Z} \to \mathbb{Z}$ is therefore the zero homomorphism.
>
> But we derived $r_* \circ i_* = \mathrm{id}_{\mathbb{Z}}$. So $0 = \mathrm{id}_{\mathbb{Z}}$ as homomorphisms $\mathbb{Z} \to \mathbb{Z}$, i.e., $1 = 0$ in $\mathbb{Z}$. Contradiction.

**Step 3: Conclude.**

> [!note]- Derivation
> The assumption that $f$ has no fixed point led to a contradiction. So every continuous $f : D^2 \to D^2$ has a fixed point. This is the Brouwer fixed-point theorem in dimension 2.

> [!note]- Complete formal solution
> **Theorem (Brouwer in dimension 2).** Every continuous map $f : D^2 \to D^2$ has a fixed point.
>
> *Proof.* Assume for contradiction that $f$ has no fixed point. For each $x \in D^2$, the vector $x - f(x)$ is non-zero, so the ray $\{f(x) + t(x - f(x)) : t \geq 0\}$ from $f(x)$ through $x$ is well-defined. The disc $D^2$ is convex, so this ray exits $D^2$ at exactly one boundary point $r(x) \in S^1 = \partial D^2$.
>
> Computing $r(x)$ explicitly: $r(x) = f(x) + t^*(x) \cdot (x - f(x))$ where $t^*(x) \geq 1$ is the unique positive solution to
> $$|f(x) + t(x - f(x))|^2 = 1,$$
> i.e., the larger root of $t^2 |x - f(x)|^2 + 2t \langle f(x), x - f(x) \rangle + (|f(x)|^2 - 1) = 0$. This root depends continuously on the coefficients, hence on $x$, so $r$ is continuous.
>
> For $x \in S^1$, the ray exits at $x$ (since $|x| = 1$ already), so $r(x) = x$. Thus $r|_{S^1} = \mathrm{id}_{S^1}$, making $r : D^2 \to S^1$ a continuous retraction.
>
> Let $i : S^1 \hookrightarrow D^2$ be the inclusion. Then $r \circ i = \mathrm{id}_{S^1}$, so on $\pi_1$, $r_* \circ i_* = \mathrm{id}_{\pi_1(S^1)} = \mathrm{id}_\mathbb{Z}$. But $\pi_1(D^2) = 0$ (the disc is contractible), so $r_*$ factors through $0$, giving $r_* \circ i_* = 0 \neq \mathrm{id}_\mathbb{Z}$. Contradiction.
>
> So $f$ has a fixed point. $\qquad\blacksquare$

> [!warning] Illegal but tempting alternative route: avoid the no-retraction step
> One might try to prove Brouwer directly by some analytical fixed-point argument (Banach contraction, etc.) without invoking $\pi_1$. The Banach contraction theorem requires the map to be a contraction (some $L < 1$ such that $d(f(x), f(y)) \leq L \cdot d(x, y)$), which is much stronger than continuity. So direct analytical approaches give weaker fixed-point theorems and miss the topological content. The no-retraction argument is essential because it captures the *topological* obstruction to extending the identity on $S^1$ to all of $D^2$ — a genuinely topological fact that no analytical assumption alone produces.
>
> Another common attempted shortcut: "the image $f(D^2) \subseteq D^2$ is compact convex (closed image of compact), so by Schauder/Kakutani-like arguments..." — but Schauder requires $f$ to map into a compact convex set in a Banach space, which doesn't give a fixed point for continuous maps without further hypotheses. The $\pi_1$ proof is the cleanest known route to the topological content.

---

# Key Takeaways

**Functoriality of $\pi_1$ converts geometric impossibility into algebraic impossibility.** The Brouwer argument is the prototype: a continuous retraction would induce a section of $i_*$, but $\pi_1$ of the disc is trivial, so $i_*$ is the zero map, with no section. The trigger condition: any setup where an "extension" or "retraction" or "section" would induce a $\pi_1$-homomorphism in a forbidden direction. The transferable diagnostic: when faced with "show no continuous map $f : X \to Y$ exists with property $P$", consider the induced $f_* : \pi_1(X) \to \pi_1(Y)$ and check whether $P$ would force $f_*$ to be a homomorphism that cannot exist (e.g., bijective when the groups have different orders, surjective when the target is "larger"). The same pattern proves: no continuous map $S^n \to S^{n-1}$ with $n \geq 2$ is a retraction of $D^n$; no continuous map $\mathbb{RP}^2 \to S^1$ except null-homotopic ones; the impossibility of continuous orientation choices on non-orientable manifolds.

**The "no-retraction" theorem and its higher-dimensional analogues are the structural content of Brouwer.** Brouwer in dimension $n$ ($n \geq 1$) is equivalent to: there is no continuous retraction $D^n \to S^{n-1}$. The two-dimensional case uses $\pi_1$; higher dimensions need higher homotopy or homology. The general theorem uses $H_{n-1}(D^n) = 0 \neq H_{n-1}(S^{n-1}) = \mathbb{Z}$ (singular homology). The trigger condition: a fixed-point problem on a disc. The transferable diagnostic: the topological invariant that distinguishes the boundary from the interior is what obstructs retractions, and any such invariant gives a Brouwer-style fixed-point theorem in that dimension.

**The fundamental theorem of algebra is a sibling theorem via the same $\pi_1$-trick.** A polynomial $p(z)$ of degree $n \geq 1$ with no roots would give a continuous map $z \mapsto p(z)/|p(z)| : \mathbb{C} \to S^1$. Restricted to circles of radius $R$ and varied with $R$, the winding number must remain constant — but it is $n$ for large $R$ (asymptotic to $z^n / |z^n|$) and $0$ for $R = 0$. Contradiction. The same conceptual move ("winding number is a $\pi_1$-invariant; varying $R$ continuously forces consistency; explicit computation gives different values at the extremes") is the heart of both Brouwer-via-no-retraction and FTA-via-winding. The trigger pattern: a topological invariant is computed at two limits and must be the same by continuity, but explicit calculation shows it is different.

**Sperner's lemma gives a combinatorial route to Brouwer that avoids $\pi_1$.** A different proof of Brouwer goes through **Sperner's lemma**: a labelling of vertices of a triangulation of $D^n$ has at least one "complete simplex" (with all $n + 1$ labels). This combinatorial fact directly implies Brouwer via a limit argument. Sperner's lemma is also a $\pi_1$ statement in disguise (it can be derived from the degree of a certain map of triangulations to $S^{n-1}$), but the combinatorial proof avoids any explicit $\pi_1$ machinery. Both routes lead to Brouwer; the $\pi_1$-route is conceptually cleaner and generalises to other obstruction problems, while Sperner gives effective computability for approximate fixed points.
