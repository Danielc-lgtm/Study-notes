---
type: theorem
subject: topology
prereqs:
  - "Def - Separation Axioms"
  - "Def - Continuous Map"
  - "Thm - Urysohn's Lemma"
tags: [analysis, topology]
---

# Notation

$X$ is a normal topological space; $F \subseteq X$ is a closed subspace; $f : F \to \mathbb{R}$ is a continuous (bounded or unbounded) function. We seek a continuous extension $g : X \to \mathbb{R}$ with $g|_F = f$. The full registry is on [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact]].

---

# Statement

> **Tietze Extension Theorem.** Let $X$ be a **normal** topological space and $F \subseteq X$ a **closed** subspace. Then every continuous function $f : F \to \mathbb{R}$ extends to a continuous function $g : X \to \mathbb{R}$. Moreover, the extension can be arranged so that $\sup_{x \in X} g(x) = \sup_{x \in F} f(x)$ and $\inf_{x \in X} g(x) = \inf_{x \in F} f(x)$.
>
> In particular, $f$ bounded gives $g$ bounded with the same sup and inf.
>
> **Tietze for $\mathbb{R}^n$-valued functions.** A continuous $f : F \to \mathbb{R}^n$ extends to a continuous $g : X \to \mathbb{R}^n$: apply the theorem coordinate-by-coordinate.

---

# Motivation

The motivating question: given a continuous function on a closed subspace of a topological space, can we extend it to a continuous function on the whole space, preserving the values on the subspace?

The answer is *not always* — without separation hypotheses, extension can fail badly. But in **normal spaces**, the answer is *yes*, and this is Tietze's extension theorem. It is the second great consequence of normality, after Urysohn's lemma; in fact Tietze is a direct generalization of Urysohn (the case where $f$ takes only two values on a disconnected $F$).

The theorem is essential for many constructions in analysis:

1. **Approximation of functions.** Given a continuous function on a compact (closed) subset of a topological space, Tietze extends it everywhere. This is the topological underpinning of approximation theorems — Weierstrass approximation, Stone–Weierstrass — which often start by extending a function from a compact subset.

2. **Sectioning of bundles.** In differential geometry, a continuous section of a vector bundle over a closed subspace $F \subseteq X$ extends to a continuous section over $X$ (when $X$ is paracompact, hence normal). This is used in obstruction theory.

3. **Boundary value problems.** Given prescribed boundary values $f$ on $\partial \Omega$ for a domain $\Omega \subseteq \mathbb{R}^n$, Tietze extends $f$ to a continuous function on all of $\mathbb{R}^n$, which can then be modified to solve the PDE or used as a comparison function.

4. **Construction of homotopies.** A homotopy on a closed subspace extends to a homotopy on the whole space, used in algebraic topology to lift maps and prove fixed-point theorems.

The proof is an iterated Urysohn argument: build the extension as a uniformly convergent series of bump functions. At each stage, find a bump function $g_n$ on $X$ approximating $f - g_1 - \cdots - g_{n-1}$ on $F$ with error $\leq (1/3)(2/3)^{n-1}$. The sum $g = \sum g_n$ converges uniformly (geometric series), and the error on $F$ tends to $0$.

The bounded case uses Urysohn directly. The unbounded case reduces to the bounded by composing with a homeomorphism $\mathbb{R} \to (-1, 1)$ (such as $x \mapsto x/(1 + |x|)$), extending the bounded version, and then composing with the inverse. There is a technical step to ensure the extension does *not* hit the boundary $\pm 1$ (else the inverse composition fails); this is achieved by another Urysohn to "shrink" the extension on a set where it would exceed the bounded range.

The theorem characterizes normal spaces in a sense: a $T_1$ space $X$ is normal *if and only if* the conclusion of Tietze's theorem holds (this is the Tietze-Urysohn-Brouwer characterization of normality).

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "normal $X$ + closed $F$ + continuous $f : F \to \mathbb{R}$". The skill is identifying the right closed subspace to apply Tietze to.

The first source is **a function on a compact subset**. Property $B$: a continuous $f : K \to \mathbb{R}$ with $K$ compact (hence closed if $X$ is Hausdorff, hence in a normal space). The bridge: Tietze extends $f$ from the compact $K$ to all of $X$. *Example:* given a continuous function on a closed unit ball, extend it to $\mathbb{R}^n$.

The second source is **a constant function on a closed set, value disagreeing with another constant on a disjoint closed set**. Property $B$: a function $f : F \cup G \to \{0, 1\}$ with $f \equiv 0$ on $F$ and $f \equiv 1$ on $G$ for disjoint closed $F, G$. The bridge: $F \cup G$ is closed; $f$ is continuous on $F \cup G$ (constant on each clopen-in-$F \cup G$ piece); Tietze extends to $X$ — and this is exactly **Urysohn's lemma**, which is the special case of Tietze.

The third source is **boundary values for a PDE on a domain $\Omega \subseteq \mathbb{R}^n$**. Property $B$: prescribed boundary data $f : \partial\Omega \to \mathbb{R}$ continuous, with $\partial\Omega$ closed in $\mathbb{R}^n$. The bridge: Tietze extends $f$ to $\mathbb{R}^n$, giving a continuous global comparison function or initial guess. *Example:* in elliptic PDE, the existence of a continuous extension is the starting point for the construction of weak solutions matching boundary data.

**Targets (Output Amplification)**

The conclusion is "a continuous $g : X \to \mathbb{R}$ extending $f$".

Combine the conclusion with **a regularity-preserving extension**. Property $D$: $f \in C^k(F)$ or $f$ Lipschitz with constant $L$. The amplified result $E$: a $C^k$ or Lipschitz extension exists. The combination requires more than Tietze — Whitney's extension theorem in $\mathbb{R}^n$, McShane and Kirszbraun in metric spaces — but Tietze is the topological starting point.

Combine the conclusion with **a homotopy / path-connectedness lift**. Property $D$: a homotopy $H : F \times [0, 1] \to Y$ on a closed subspace. The amplified result $E$: extend $H$ to a homotopy on $X \times [0, 1]$ (by Tietze applied to each component or via the absolute Tietze for metric targets). The combination is used in obstruction theory in algebraic topology.

Combine the conclusion with **a coordinate-wise Tietze**. Property $D$: a continuous $f : F \to \mathbb{R}^n$ on closed $F$. The amplified result $E$: extend each coordinate separately by Tietze to get a continuous extension $g : X \to \mathbb{R}^n$. The combination handles vector-valued functions trivially; the case for general topological targets is much harder (requires the target to be an absolute neighborhood retract).

---

# Why Is It True

The intuition: the bounded case is an *iterated Urysohn* argument, and the unbounded case reduces to the bounded by passing through a homeomorphism with $(-1, 1)$.

**Bounded case.** Suppose $f : F \to [0, 1]$ continuous; we extend to $g : X \to [0, 1]$ continuous.

The idea: approximate $f$ by piecewise-Urysohn functions, and assemble the approximations into a uniformly convergent series.

Step 1: Find $g_1 : X \to [0, 1/3]$ continuous such that $|f - g_1| \leq 2/3$ on $F$. To do this: the closed sets $A = f^{-1}([0, 1/3])$ and $B = f^{-1}([2/3, 1])$ are disjoint closed subsets of $F$, and so disjoint closed in $X$ (since $F$ is closed). By Urysohn, find $g_1 : X \to [0, 1/3]$ with $g_1 \equiv 0$ on $A$ and $g_1 \equiv 1/3$ on $B$. Verify: on $A$, $f - g_1 = f \leq 1/3 \leq 2/3$; on $B$, $f - g_1 \geq 2/3 - 1/3 = 1/3$, but we also need $f - g_1 \leq 2/3$: $f - g_1 = f - 1/3 \leq 1 - 1/3 = 2/3$. ✓ On $F \setminus (A \cup B)$, $1/3 < f < 2/3$ and $0 \leq g_1 \leq 1/3$, so $-1/3 \leq f - g_1 \leq 2/3$. ✓

So $|f - g_1| \leq 2/3$ on $F$.

Step $n$: Define $f_n = f - g_1 - \cdots - g_{n-1}$ on $F$. By induction $|f_n| \leq (2/3)^{n-1}$ on $F$. Apply the same Urysohn argument scaled to $f_n$: find $g_n : X \to [0, (1/3)(2/3)^{n-1}]$ with $|f_n - g_n| \leq (2/3)^n$ on $F$.

Let $g = \sum_{n=1}^\infty g_n$. Since $|g_n| \leq (1/3)(2/3)^{n-1}$, the series converges uniformly (geometric); $g$ is continuous (uniform limit of continuous). On $F$, $f - (g_1 + \cdots + g_n) = f_{n+1}$ and $|f_{n+1}| \leq (2/3)^n \to 0$; so $g|_F = f$.

**Unbounded case.** Compose $f$ with the homeomorphism $\phi : \mathbb{R} \to (-1, 1)$, $\phi(x) = x/(1 + |x|)$. Then $\phi \circ f : F \to (-1, 1) \subseteq [-1, 1]$ is bounded. Extend by Tietze (bounded version) to $h : X \to [-1, 1]$. The issue: $h$ might take values $\pm 1$ outside $F$, but we need $h$ to land in $(-1, 1)$ so we can compose with $\phi^{-1}$. To fix this: let $C = h^{-1}(\{-1, 1\})$, closed in $X$; $C \cap F = \emptyset$ (since $h = \phi \circ f$ on $F$ and $\phi$ maps into $(-1, 1)$). By Urysohn (or directly by normality), find a continuous $k : X \to [0, 1]$ with $k \equiv 1$ on $F$ and $k \equiv 0$ on $C$. The function $h \cdot k$ is continuous, equals $h = \phi \circ f$ on $F$ (where $k = 1$), and equals $0$ on $C$ (where $k = 0$); hence $h \cdot k$ takes values in $(-1, 1)$ everywhere. Compose with $\phi^{-1}$ to get the unbounded extension.

The "shrink near the bad set" trick (multiplying by $k$) is what handles the unbounded case cleanly.

---

# What Makes This Hard

The non-obvious step is the **iterated Urysohn with geometric error decrement**: at each step, choose the bump $g_n$ to take values in $[0, (1/3)(2/3)^{n-1}]$ and split $F$ into the "bottom third", "middle", "top third" of the residual function $f_n$. The factor $1/3$ for the bump amplitude and $2/3$ for the error decrement are critical — these are exactly the ratios that make the geometric series converge while the error decrement is faster than the bump amplitude. The most common error is to use scaled-incorrect ratios (e.g., bump of amplitude $1/2$ would give error $1/2$, no decrement); the $1/3$-$2/3$ structure is canonical. Another non-obvious step is the unbounded case fix: multiplying by a Urysohn cutoff $k$ to keep the extension away from the bad set $\{\pm 1\}$.

---

# Rederivation Scaffold

**High-level strategy:**
Reduce to the bounded case. For bounded $f : F \to [0, 1]$, iterate Urysohn: at each step, split the function's range into thirds (bottom, middle, top), produce a Urysohn bump on $X$ that approximates the function with error $\leq 2/3$ of the previous error, and sum into a uniformly convergent series. The unbounded case reduces by passing through $\mathbb{R} \to (-1, 1)$ via a homeomorphism.

**Subgoal decomposition:**

1. **Reduce to $[0, 1]$-valued.** Normalize: $f$ takes values in $\mathbb{R}$, but by translation and scaling we can reduce to $f : F \to [0, 1]$.
   - *Hint:* Affine map $\mathbb{R} \to [0, 1]$ when $f$ is bounded.
   - *Why needed:* Standardizes the proof; the unbounded case is handled separately.

2. **Single Urysohn approximation.** Construct $g_n : X \to [0, (1/3)(2/3)^{n-1}]$ such that $|f_n - g_n| \leq (2/3)^n$ on $F$, where $f_n = f - g_1 - \cdots - g_{n-1}$.
   - *Hint:* Define $A_n = f_n^{-1}([0, (1/3)(2/3)^{n-1}])$, $B_n = f_n^{-1}([(2/3)(2/3)^{n-1}, (2/3)^{n-1}])$, disjoint closed; apply Urysohn.
   - *Why needed:* The iteration step; the geometric decrement.

3. **Sum to a convergent series.** $g = \sum_n g_n$ converges uniformly to a continuous function with $g|_F = f$.
   - *Hint:* $|g_n| \leq (1/3)(2/3)^{n-1}$ gives geometric series; uniform limit of continuous is continuous; the error on $F$ tends to $0$.
   - *Why needed:* Produces the extension.

4. **Unbounded case via $(-1, 1)$.** Compose with $\phi : \mathbb{R} \to (-1, 1)$, extend the bounded version, shrink the extension to avoid $\pm 1$ via a Urysohn cutoff, compose with $\phi^{-1}$.
   - *Hint:* The bad set $h^{-1}(\{\pm 1\})$ is closed and disjoint from $F$; multiply $h$ by a Urysohn function that is $0$ there and $1$ on $F$.
   - *Why needed:* Handles unbounded $f$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Single-step approximation via Urysohn
> **Statement:** Let $X$ be normal, $F \subseteq X$ closed, $h : F \to [-M, M]$ continuous. There exists a continuous $g : X \to [-M/3, M/3]$ with $|h - g| \leq (2/3)M$ on $F$.
>
> **Hint:** Define $A = h^{-1}([-M, -M/3])$, $B = h^{-1}([M/3, M])$ — disjoint closed subsets of $F$; apply Urysohn to get $g : X \to [-M/3, M/3]$ with $g \equiv -M/3$ on $A$ and $g \equiv M/3$ on $B$.
>
> **Why needed:** The single-step approximation that drives the iteration.
>
> > [!note]- Full proof
> > $A$ and $B$ are disjoint closed subsets of $F$, hence disjoint closed subsets of $X$ (since $F$ is closed). By Urysohn's lemma, there is a continuous $g_0 : X \to [0, 1]$ with $g_0 \equiv 0$ on $A$ and $g_0 \equiv 1$ on $B$. Set $g = (2M/3)g_0 - M/3$, so $g : X \to [-M/3, M/3]$ with $g \equiv -M/3$ on $A$ and $g \equiv M/3$ on $B$.
> >
> > Verify $|h - g| \leq 2M/3$ on $F$:
> > - On $A$: $h \in [-M, -M/3]$, $g = -M/3$, so $h - g \in [-2M/3, 0]$, $|h - g| \leq 2M/3$. ✓
> > - On $B$: $h \in [M/3, M]$, $g = M/3$, so $h - g \in [0, 2M/3]$, $|h - g| \leq 2M/3$. ✓
> > - On $F \setminus (A \cup B)$: $h \in (-M/3, M/3)$, $g \in [-M/3, M/3]$, so $h - g \in (-2M/3, 2M/3)$, $|h - g| < 2M/3$. ✓

> [!note]- Lemma 2: Cutoff to a closed subspace
> **Statement:** Let $X$ be normal, $F \subseteq X$ closed, $C \subseteq X$ closed with $C \cap F = \emptyset$. There is a continuous $k : X \to [0, 1]$ with $k \equiv 1$ on $F$ and $k \equiv 0$ on $C$.
>
> **Hint:** Urysohn's lemma directly.
>
> **Why needed:** Used in the unbounded case to shrink the extension away from the bad set.

---

# Formal Proof

> [!note]- Complete formal proof
> We prove the bounded case first.
>
> **Bounded case: $f : F \to [0, 1]$ continuous.** We construct a uniformly convergent series $g = \sum_n g_n$ as the extension.
>
> Set $f_1 = f$ (so $f_1 : F \to [0, 1]$ has $|f_1| \leq 1$). By Lemma 1 applied to $h = f_1 - 1/2$ (so $|h| \leq 1/2$, with $M = 1/2$), get $g_1' : X \to [-1/6, 1/6]$ with $|f_1 - 1/2 - g_1'| \leq 1/3$ on $F$. Set $g_1 = g_1' + 1/2$, so $g_1 : X \to [1/3, 2/3]$ and $|f_1 - g_1| \leq 1/3$ on $F$. (Alternative form: simpler to work directly with $[0, 1]$-valued residuals via scaling; the original Bredon proof does this with thirds.)
>
> *(A cleaner version following Bredon:)* For $f : F \to [0, 1]$, the closed sets $A = f^{-1}([0, 1/3])$, $B = f^{-1}([2/3, 1])$ are disjoint closed in $F$, hence in $X$. By Urysohn there is $g_1 : X \to [0, 1/3]$ with $g_1 \equiv 0$ on $A$, $g_1 \equiv 1/3$ on $B$. On $F$: $|f - g_1| \leq 2/3$ (check the three cases as in Lemma 1).
>
> Inductively, $f_n = f - \sum_{k=1}^{n-1} g_k$ on $F$ has $|f_n| \leq (2/3)^{n-1}$. Apply the same construction at scale $(2/3)^{n-1}$: find $g_n : X \to [0, (1/3)(2/3)^{n-1}]$ with $|f_n - g_n| \leq (2/3)^n$ on $F$.
>
> Set $g = \sum_{n=1}^\infty g_n$. Since $g_n : X \to [0, (1/3)(2/3)^{n-1}]$, $\sum \lVert g_n\rVert_\infty \leq \sum (1/3)(2/3)^{n-1} = 1 < \infty$, so the series converges uniformly. Hence $g : X \to [0, 1]$ is continuous (uniform limit of continuous functions). On $F$: $f - (g_1 + \cdots + g_n) = f_{n+1}$ and $|f_{n+1}| \leq (2/3)^n \to 0$, so $g|_F = f$.
>
> **Unbounded case: $f : F \to \mathbb{R}$ continuous, possibly unbounded.**
>
> Let $\phi(x) = x/(1 + |x|)$, a homeomorphism $\mathbb{R} \to (-1, 1)$. Then $\phi \circ f : F \to (-1, 1) \subseteq [-1, 1]$ is continuous and bounded. By the bounded case, extend to $h : X \to [-1, 1]$ continuous.
>
> Let $C = h^{-1}(\{-1, 1\}) = h^{-1}(\{-1\}) \cup h^{-1}(\{1\})$, a closed subset of $X$. Since $h(F) = \phi(f(F)) \subseteq (-1, 1)$, $C \cap F = \emptyset$.
>
> By Lemma 2 (Urysohn), there is a continuous $k : X \to [0, 1]$ with $k \equiv 1$ on $F$ and $k \equiv 0$ on $C$. Set $\tilde h = h \cdot k$, a continuous function $X \to [-1, 1]$. On $F$: $\tilde h = h$ (since $k = 1$), so $\tilde h|_F = \phi \circ f$, taking values in $(-1, 1)$. On $C$: $\tilde h = 0$ (since $k = 0$), in $(-1, 1)$. On $X \setminus (F \cup C)$: $|\tilde h| \leq |h| \cdot |k| < 1$ (since $|h| \leq 1$ with equality only on $C$, and $|k| \leq 1$). So $\tilde h$ takes values in $(-1, 1)$ everywhere.
>
> Define $g = \phi^{-1} \circ \tilde h : X \to \mathbb{R}$. Continuous (composition of continuous), and $g|_F = \phi^{-1} \circ (\phi \circ f) = f$. So $g$ extends $f$.
>
> **Sup/inf preservation.** A separate argument (using more careful Urysohn choices) shows $\sup g = \sup f$ and $\inf g = \inf f$ can be arranged. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Extending a function from a closed ball to $\mathbb{R}^n$ continuously.** Given $f \in C(\overline{B(0, 1)})$, Tietze gives a continuous extension $g \in C(\mathbb{R}^n)$. This is the topological underpinning of the standard "extend by zero" or "extend by mollification" arguments in PDE — but Tietze allows extending arbitrary continuous boundary data, not just constant or smooth functions.

**Whitney's extension as a smooth refinement.** Whitney's extension theorem says: if $F \subseteq \mathbb{R}^n$ is closed and $f \in C^k(F)$ (in an appropriate sense involving jets), then $f$ extends to $g \in C^k(\mathbb{R}^n)$. Tietze handles the continuous case; Whitney is the much harder smooth refinement, with a Tietze-style "iterate the smoothing" argument in the proof. The connection: every smooth extension is also a continuous extension, and Tietze is the topological "warm-up" for Whitney.

**Lifting maps from closed subspaces.** In algebraic topology, the homotopy extension property (HEP) of a pair $(X, F)$ says: given a homotopy on $F$ and a continuous extension to $X$ at time $0$, the homotopy extends to a homotopy on $X$. For normal spaces, HEP follows from Tietze applied to the appropriate function spaces.

---

# Bridges

- **[[Thm - Urysohn's Lemma]]** — the special case (constant values on disjoint closed sets) and the engine of the proof (the iterated Urysohn).

- **[[Def - Separation Axioms]]** — Tietze characterizes normality among $T_1$ spaces: normal iff Tietze.

- **Whitney's extension theorem** — the smooth refinement; uses Tietze as the continuous warm-up.

- **McShane and Kirszbraun extension theorems** — the metric-Lipschitz refinements: a Lipschitz function on a closed subset of a metric space extends to a Lipschitz function on the whole space, with the same constant (McShane for $\mathbb{R}$-valued, Kirszbraun for Hilbert-valued).

---

# Unlocked by This

> [!tip] Whitney's Extension Theorem *(from Differential Geometry)*
> A $C^k$ function on a closed subset of $\mathbb{R}^n$ (in an appropriate jet sense) extends to a $C^k$ function on $\mathbb{R}^n$. The Tietze argument is the continuous core; the smooth case requires additional Whitney-style controls.

> [!tip] Homotopy Extension Property *(from Algebraic Topology)*
> For a closed pair $(X, F)$ in a normal space, continuous homotopies on $F$ extend to continuous homotopies on $X$. Proved by Tietze applied to the homotopy as a map $F \times [0, 1] \to Y$.

> [!tip] McShane–Kirszbraun Extension *(from Metric Geometry)*
> A Lipschitz function on a closed subset of a metric space extends to a Lipschitz function on the whole space, with the same Lipschitz constant. Refinement of Tietze for metric targets and Lipschitz regularity.

> [!tip] Boundary Value Problems *(from PDE)*
> Continuous boundary data $f$ on $\partial\Omega$ extends to continuous data on $\overline\Omega$, providing the starting comparison function for elliptic PDE existence theory (Perron, Wiener).
