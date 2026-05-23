---
type: theorem
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Separation Axioms"
  - "Def - Continuous Map"
  - "Thm - Metric Spaces are Normal"
tags: [analysis, topology]
---

# Notation

$X$ is a topological space, presumed normal. $F, G$ disjoint closed subsets; $F \subseteq U$ with $U$ open is the "closed-inside-open" form Bredon uses. We work with **dyadic rationals** in $[0, 1]$ — numbers of the form $m/2^n$ for $m, n \in \mathbb{N}$, $0 \leq m \leq 2^n$. The full registry is on [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact]].

---

# Statement

> **Urysohn's Lemma.** Let $X$ be a normal topological space, and let $F \subseteq U \subseteq X$ where $F$ is closed and $U$ is open. Then there exists a continuous map $f : X \to [0, 1]$ such that:
>
> $$f \equiv 0 \text{ on } F \quad \text{and} \quad f \equiv 1 \text{ on } X \setminus U.$$
>
> Equivalent statement: in a normal space $X$, for any two disjoint closed sets $F, G$, there is a continuous $f : X \to [0, 1]$ with $f \equiv 0$ on $F$ and $f \equiv 1$ on $G$. (Set $U = X \setminus G$ in the form above.)

---

# Motivation

Normality says: any two disjoint closed sets in $X$ can be separated by disjoint open neighborhoods. This is a *qualitative* separation by sets. Urysohn's lemma upgrades it to a *quantitative* separation by a function: a continuous $f : X \to [0, 1]$ that *takes value $0$ on one closed set and $1$ on the other*. The function is the "indicator-like" object — between $0$ and $1$, continuous, with a controlled level set structure.

The lemma is the cornerstone of the theory of continuous functions in general topology. It is:

1. **What makes separation arithmetic.** Once you have a continuous $f$ separating $F$ from $G$ on $[0, 1]$, you can do *arithmetic* with it: take affine combinations $\alpha + (\beta - \alpha) f$ to get functions separating $F$ from $G$ on any prescribed interval. You can multiply functions to localize: $f \cdot g$ vanishes wherever either does. You can sum: $f + g$ controls supports. This is why normality + Urysohn gives a *function-rich* setting.

2. **The engine of metrization and embedding theorems.** [[Thm - Urysohn Metrization Theorem|Urysohn metrization]] uses families of separating functions to embed spaces in $[0, 1]^\mathbb{N}$. [[Thm - Tietze Extension Theorem|Tietze extension]] is a generalization of Urysohn (Urysohn is Tietze for the special case of a function on $F \cup G$ taking values $0$ and $1$). Together they characterize normal spaces as "function-rich".

3. **The model for partition of unity construction.** A partition of unity needs continuous functions $\rho_\alpha$ supported in $U_\alpha$. Urysohn produces exactly such functions (or, more precisely, bump functions equal to $1$ on a sub-closed-set). The partition is then a normalization.

The proof is a beautiful inductive construction. Given normal $X$ and $F \subseteq U$, we want to interpolate continuously from $F$ (where $f = 0$) to $X \setminus U$ (where $f = 1$). Define open sets $U_r$ for every dyadic rational $r \in [0, 1]$, with the property that $\overline{U_r} \subseteq U_s$ whenever $r < s$. Start with $U_0 =$ a smaller open set with $F \subseteq U_0$ and $\overline{U_0} \subseteq U$ (using normality on $F$ and $X \setminus U$); $U_1 = U$. Recursively insert $U_{1/2}$ between $\overline{U_0}$ and $U_1$ (using normality on $\overline{U_0}$ and $X \setminus U_1$); then $U_{1/4}$ between $\overline{U_0}$ and $U_{1/2}$, and $U_{3/4}$ between $\overline{U_{1/2}}$ and $U_1$; iterate at each dyadic level.

The function $f(x) = \inf\{r : x \in U_r\}$ (with $f \equiv 1$ outside all $U_r$) is the Urysohn function. Continuity comes from the fact that the level sets are determined by the $U_r$ structure: $f^{-1}([0, r)) = \bigcup_{s < r} U_s$ (open) and $f^{-1}((r, 1]) = \bigcup_{s > r} (X \setminus \overline{U_s})$ (open).

The construction is *explicit* and *no choice axiom is needed* — only the recursive application of normality at countably many dyadic steps.

The metric-space special case: $f(x) = d(x, F)/(d(x, F) + d(x, G))$ is the explicit Urysohn function. This formula bypasses the dyadic construction by exploiting the metric — the distance function does the interpolation for free.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "normal space + disjoint closed sets (or closed $\subseteq$ open)". The skill is recognizing situations where normality is available, sometimes implicitly.

The first source is **a compact Hausdorff space**. Property $B$: a compact Hausdorff space $X$. The bridge: compact Hausdorff implies normal (a standard result from Topology II); so Urysohn applies. *Example:* on any compact subset of $\mathbb{R}^n$, Urysohn's lemma is available. This is the prototypical use.

The second source is **a metric space**. Property $B$: any metric space. The bridge: metric spaces are normal ([[Thm - Metric Spaces are Normal]]); Urysohn applies. *Example:* the explicit formula $f(x) = d(x, F)/(d(x, F) + d(x, G))$ bypasses the abstract construction.

The third source is **a paracompact Hausdorff space**. Property $B$: a paracompact Hausdorff space. The bridge: paracompact Hausdorff implies normal ([[Thm - Paracompact Implies Normal]]); Urysohn applies. *Example:* this is what powers the existence of partitions of unity on paracompact spaces — Urysohn produces the bump functions, paracompactness gives the local-finite refinement.

**Targets (Output Amplification)**

The conclusion is "a continuous $f : X \to [0, 1]$ with prescribed values on $F$ and $G$".

Combine the conclusion with **post-composition by a continuous map $[0, 1] \to \mathbb{R}$**. Property $D$: any continuous $g : [0, 1] \to \mathbb{R}$ — say a smooth bump, a step, a logistic. The amplified result $E$: $g \circ f : X \to \mathbb{R}$ is continuous with prescribed values on $F$ and $G$ controllable by $g$. The combination gives **Urysohn-like functions with prescribed shapes**: not just $0$ and $1$, but bumps, ramps, mollifiers.

Combine the conclusion with **product / multiplication of Urysohn functions**. Property $D$: multiple disjoint closed sets $F_1, \dots, F_n$ in $X$. The amplified result $E$: continuous functions $f_i$ with $f_i \equiv 0$ on $F_i$, $f_i \equiv 1$ on the others; the product $\prod (1 - f_i)$ vanishes on the union, and normalizing gives a partition of unity. The combination is the recipe for **partitions of unity on normal spaces** (with finitely many parts; for infinite ones, paracompactness is needed).

Combine the conclusion with **a continuous function on $F$**. Property $D$: a continuous bounded function $\varphi : F \to \mathbb{R}$. The amplified result $E$: by iterating Urysohn, $\varphi$ extends to a continuous function on $X$. This is [[Thm - Tietze Extension Theorem|Tietze's extension theorem]] — proved by an iterated Urysohn argument.

---

# Why Is It True

The intuition: in a normal space, you have a *qualitative* separation — disjoint opens around any two disjoint closed sets. Urysohn's lemma upgrades this to a *quantitative* function-based separation, but the upgrade is achieved by *iterating the qualitative separation infinitely many times* — specifically, at every dyadic rational level.

Imagine building $f$ level set by level set. The level set $\{f \leq r\}$ should be a closed set containing $F$ (where $f = 0$) and disjoint from $X \setminus U$ (where $f = 1$). For each $r$, define an open $U_r$ with $\{f \leq r\} = \overline{U_r}$ (roughly speaking). The conditions: $U_r$ should grow as $r$ grows (level sets nest), and $\overline{U_r} \subseteq U_s$ for $r < s$ (each level's closure is strictly inside the next level's open).

Why dyadic rationals? Because they are *dense* in $[0, 1]$ (so any value of $f$ can be approximated), and they form a *countable* set built by repeated bisection — exactly what you can iterate at via normality. The construction proceeds by *interpolating* a new open set between two existing ones using normality, then iterating: between $U_0$ and $U_1$, insert $U_{1/2}$ via normality on $\overline{U_0}$ and $X \setminus U_1$; between $U_0$ and $U_{1/2}$, insert $U_{1/4}$; between $U_{1/2}$ and $U_1$, insert $U_{3/4}$; continue at dyadic level $n$. Each step is a single application of normality, and the construction populates all dyadic rationals.

Once the family $\{U_r\}_r$ is built, the function $f(x) = \inf\{r : x \in U_r\}$ (extended by $1$ where $x \notin U_r$ for any $r$) is well-defined and continuous. Continuity is checked via the subbasis of $[0, 1]$ — the half-lines $[0, a)$ and $(a, 1]$:

- $f^{-1}([0, a)) = \bigcup_{r < a, r \in \mathbb{Q}_2} U_r$, a union of opens, hence open.
- $f^{-1}((a, 1]) = \bigcup_{r > a, r \in \mathbb{Q}_2} (X \setminus \overline{U_r})$, a union of opens, hence open.

So $f$ is continuous, and the values on $F$ and outside $U$ are $0$ and $1$ by construction ($F \subseteq U_r$ for all $r \geq 0$, so $f \equiv 0$ on $F$; $x \notin U_1 \supseteq U_r$ for all $r$, so $f(x) = 1$ outside $U$).

The deep insight is that **dyadic rationals are a countable scaffold dense in $[0, 1]$**, and **normality lets us interpolate at every dyadic step**. The function is built entirely from the discrete topology of $\mathbb{Q}_2 \cap [0, 1]$ via this interpolation.

---

# What Makes This Hard

The non-obvious step is the **recursive interpolation of opens at dyadic levels**: setting up the nested family $\{U_r\}_{r \in \mathbb{Q}_2 \cap [0, 1]}$ with $\overline{U_r} \subseteq U_s$ for $r < s$. Most people, when first attempting the proof, do not see why dyadics are the right indexing set or why "interpolate between two existing levels" is the recipe — they expect to construct the function directly, somehow. The non-obvious move is to *construct the level-set structure first*, then derive the function from it.

The most common errors: (a) trying to construct $f$ directly without going through the level sets; (b) forgetting the **closure-containment** condition $\overline{U_r} \subseteq U_s$ for $r < s$ (which is what gives continuity of $f$); (c) using non-dyadic indices, which produces an uncountable construction needing transfinite induction.

---

# Rederivation Scaffold

**High-level strategy:**
Build a nested family of open sets $\{U_r\}$ indexed by dyadic rationals in $[0, 1]$, with $\overline{U_r} \subseteq U_s$ when $r < s$, starting from $F \subseteq U_0$ and $U_1 = U$, and using normality to interpolate at each dyadic step. Then define $f(x) = \inf\{r : x \in U_r\}$ and verify continuity via the level sets.

**Subgoal decomposition:**

1. **Set up endpoints.** Use normality on $F$ and $X \setminus U$ to find an open $U_0$ with $F \subseteq U_0 \subseteq \overline{U_0} \subseteq U$. Set $U_1 = U$.
   - *Hint:* Normality: disjoint closed $F$ and $X \setminus U$ have disjoint open separating neighborhoods $U_0$ and $W$; then $\overline{U_0} \subseteq X \setminus W \subseteq U$.
   - *Why needed:* Initializes the construction at $r = 0$ and $r = 1$.

2. **Interpolate at each dyadic level.** Given $U_a, U_b$ with $\overline{U_a} \subseteq U_b$, use normality to find $U_c$ with $\overline{U_a} \subseteq U_c \subseteq \overline{U_c} \subseteq U_b$ (where $c = (a + b)/2$).
   - *Hint:* Apply normality to the disjoint closed sets $\overline{U_a}$ and $X \setminus U_b$.
   - *Why needed:* Populates all dyadic rationals by repeated bisection.

3. **Define $f$ via infimum.** $f(x) = \inf\{r \in \mathbb{Q}_2 : x \in U_r\}$ if such $r$ exists, $f(x) = 1$ otherwise.
   - *Hint:* Equivalently $f(x) = \inf\{r : x \in U_r\}$ over the constructed family.
   - *Why needed:* The function realized by the level structure.

4. **Verify continuity.** Show $f^{-1}([0, a))$ and $f^{-1}((a, 1])$ are open for every $a \in [0, 1]$.
   - *Hint:* $f^{-1}([0, a)) = \bigcup_{r < a} U_r$, $f^{-1}((a, 1]) = \bigcup_{r > a} (X \setminus \overline{U_r})$.
   - *Why needed:* The half-line subbasis of $[0, 1]$ determines continuity.

5. **Verify boundary values.** Check $f \equiv 0$ on $F$ and $f \equiv 1$ on $X \setminus U$.
   - *Hint:* $F \subseteq U_0 \subseteq U_r$ for all $r$, so $f \equiv 0$ on $F$; $X \setminus U = X \setminus U_1$, so $x \in X \setminus U$ has $x \notin U_r$ for any $r \leq 1$, giving $f(x) = 1$ (the infimum of the empty set is $\sup$ of the index set).
   - *Why needed:* Confirms the conclusion.

---

# Lemma Decomposition

> [!note]- Lemma 1: Inserting an open set between a closed and an open
> **Statement:** Let $X$ be normal, $F \subseteq U$ with $F$ closed and $U$ open. Then there is an open $V$ with $F \subseteq V \subseteq \overline V \subseteq U$.
>
> **Hint:** Apply normality to $F$ and $X \setminus U$ to find disjoint opens $V$ and $W$; then $V \subseteq X \setminus W$ closed, so $\overline V \subseteq X \setminus W \subseteq U$.
>
> **Why needed:** The basic insertion step used at each dyadic level.
>
> > [!note]- Full proof
> > $F$ and $X \setminus U$ are disjoint closed sets. By normality, there exist disjoint open sets $V \supseteq F$ and $W \supseteq X \setminus U$. Since $V \cap W = \emptyset$, $V \subseteq X \setminus W$, and $X \setminus W$ is closed, so $\overline V \subseteq X \setminus W$. Also $X \setminus W \subseteq X \setminus (X \setminus U) = U$. So $F \subseteq V \subseteq \overline V \subseteq U$.

> [!note]- Lemma 2: The inf-of-dyadic function is continuous
> **Statement:** Let $X$ be a topological space and $\{U_r\}_{r \in \mathbb{Q}_2 \cap [0, 1]}$ a family of open sets with $\overline{U_r} \subseteq U_s$ whenever $r < s$. Define $f : X \to [0, 1]$ by $f(x) = \inf\{r : x \in U_r\}$ (with $f(x) = 1$ if $x \notin U_r$ for any $r$). Then $f$ is continuous.
>
> **Hint:** Check that $f^{-1}([0, a))$ and $f^{-1}((a, 1])$ are open via the level-set description.
>
> **Why needed:** Step 4 of the main proof.
>
> > [!note]- Full proof
> > $f^{-1}([0, a))$: $f(x) < a$ iff there is a dyadic $r < a$ with $x \in U_r$, i.e., $x \in U_r$ for some $r < a$. So $f^{-1}([0, a)) = \bigcup_{r < a, r \in \mathbb{Q}_2} U_r$, a union of opens, hence open.
> >
> > $f^{-1}((a, 1])$: $f(x) > a$ iff $x \notin U_r$ for any $r \leq a$, i.e., $x \notin U_r$ for all dyadic $r$ with $r \leq a$. By the nesting $\overline{U_r} \subseteq U_s$ for $r < s$, $x \notin U_r$ for $r \leq a$ is equivalent to $x \notin \overline{U_s}$ for some $s > a$ (take $s$ slightly larger than $a$). So $f^{-1}((a, 1]) = \bigcup_{s > a, s \in \mathbb{Q}_2} (X \setminus \overline{U_s})$, a union of opens, hence open.
> >
> > The half-line preimages being open is equivalent to continuity into $[0, 1]$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $X$ be normal, $F \subseteq U$ with $F$ closed and $U$ open. We construct the family $\{U_r\}$ inductively.
>
> **Base case.** Set $U_1 = U$. By Lemma 1, find $U_0$ open with $F \subseteq U_0 \subseteq \overline{U_0} \subseteq U_1$.
>
> **Inductive step.** Suppose we have constructed $U_r$ for all dyadic rationals $r = m/2^n$ at level $\leq n$, with $\overline{U_r} \subseteq U_s$ whenever $r < s$. To construct $U_{(2k+1)/2^{n+1}}$ for $0 \leq k < 2^n$: let $a = k/2^n$ and $b = (k+1)/2^n$, so $\overline{U_a} \subseteq U_b$. By Lemma 1, find an open $V$ with $\overline{U_a} \subseteq V \subseteq \overline V \subseteq U_b$; set $U_{(2k+1)/2^{n+1}} = V$. The new family at level $n+1$ inherits the closure-containment property.
>
> So the family $\{U_r\}_{r \in \mathbb{Q}_2 \cap [0, 1]}$ is constructed with $\overline{U_r} \subseteq U_s$ for $r < s$.
>
> **Define $f$.** $f(x) = \inf\{r \in \mathbb{Q}_2 \cap [0, 1] : x \in U_r\}$ if the set is nonempty; $f(x) = 1$ otherwise. By Lemma 2, $f : X \to [0, 1]$ is continuous.
>
> **Boundary values.** For $x \in F$: $F \subseteq U_0 \subseteq U_r$ for every $r > 0$ (by the inductive construction, $U_0 \subseteq U_r$), so $f(x) = \inf\{r \geq 0 : x \in U_r\} \leq 0$, so $f(x) = 0$.
>
> For $x \in X \setminus U$: $x \notin U_1 = U$, and $U_r \subseteq U_1$ for $r \leq 1$ (by closure-containment), so $x \notin U_r$ for any $r \in [0, 1]$. Hence $f(x) = 1$.
>
> $f \equiv 0$ on $F$ and $f \equiv 1$ on $X \setminus U$. $\blacksquare$
>
> **Metric-space special case.** When $X$ is metric and $F, G$ are disjoint closed sets, $f(x) = d(x, F)/(d(x, F) + d(x, G))$ is continuous (a ratio with positive denominator on disjoint closeds), $f \equiv 0$ on $F$ (where $d(x, F) = 0$), $f \equiv 1$ on $G$ (where $d(x, G) = 0$). This bypasses the dyadic construction. The denominator $d(x, F) + d(x, G) > 0$ everywhere because $F \cap G = \emptyset$ closed implies positive minimum distance between the two on a compact set; in general $F \cap G = \emptyset$ closed and any $x$ has $\max(d(x, F), d(x, G)) > 0$ unless $x \in F \cap G$, which is empty.

---

# Cross-Field Exercise Suggestions

**Construction of bump functions on $\mathbb{R}^n$.** Given disjoint closed sets $F, G$ in $\mathbb{R}^n$ — e.g., a closed ball $\overline{B(0, 1)}$ and the complement of a larger open ball $B(0, 2)$ — Urysohn produces a continuous bump function equal to $1$ on the smaller ball and $0$ outside the larger. The metric formula $f(x) = d(x, G)/(d(x, F) + d(x, G))$ does this explicitly. Used everywhere in analysis: convolution mollifiers, smooth cutoffs in PDE, support manipulation in distribution theory.

**Tietze extension via iterated Urysohn.** The Tietze extension theorem says continuous bounded real-valued functions on closed subsets of normal spaces extend to the whole space. The proof is an iterated Urysohn argument: at each step, use Urysohn to construct a function approximating the given one with error $\leq 1/3$ on the closed set; sum the approximations into a uniformly convergent series. See [[Thm - Tietze Extension Theorem]].

**Separating points and closed sets in completely regular spaces.** A space is completely regular iff for every $x$ and closed $C \not\ni x$, there is a continuous $f$ separating them. In *normal* spaces, this is a direct consequence of Urysohn: take $F = \{x\}$ (singleton, closed in $T_1$) and $G = C$. So normal $T_1$ spaces are completely regular — which is Bredon's Corollary 10.3.

---

# Bridges

- **[[Thm - Metric Spaces are Normal]]** — metric spaces satisfy the hypotheses; the metric-formula version gives Urysohn explicitly without dyadic construction.

- **[[Thm - Tietze Extension Theorem]]** — the generalization. Urysohn is the special case where the function on the closed subspace is constant (specifically $0$ on one piece and $1$ on another disjoint piece).

- **[[Thm - Urysohn Metrization Theorem]]** — uses iterated Urysohn-style functions (specifically the regular + second countable lemma version) to embed $X$ in $[0, 1]^\mathbb{N}$.

- **[[Thm - Paracompact Has Partitions of Unity]]** — paracompact Hausdorff implies normal, so Urysohn is available, giving the bump functions for the partition.

- **[[Def - Completely Regular Space]]** — Urysohn shows that normal $T_1$ implies completely regular.

---

# Unlocked by This

> [!tip] Tietze Extension Theorem *(from this topic)*
> Every continuous bounded function on a closed subspace of a normal space extends to a continuous function on the whole space, by an iterated Urysohn construction. See [[Thm - Tietze Extension Theorem]].

> [!tip] Partitions of Unity on Paracompact Hausdorff Spaces *(from this topic)*
> The bumps in a partition of unity are constructed by Urysohn applied to (closed shrunken cover element, complement of original cover element). See [[Thm - Paracompact Has Partitions of Unity]].

> [!tip] Complete Regularity from Normality *(from this topic)*
> Every normal $T_1$ space is completely regular: Urysohn with $F = \{x\}$ and $G = C$ gives the separating function.

> [!tip] Mollifiers and Smooth Bump Functions *(from Analysis)*
> Smooth bump functions on $\mathbb{R}^n$ (used in convolution mollifiers and distribution theory) are smooth Urysohn-type functions, constructed by composing the explicit formula $d(x, F)/(d(x, F) + d(x, G))$ with smooth approximations.
