---
type: theorem
subject: topology
prereqs:
  - "Def - Topological Group"
  - "Thm - Translations are Homeomorphisms"
tags: [analysis, topology, topological-group, neighborhoods]
---

# Notation

$G$ a topological group with identity $e$. A subset $A \subseteq G$ is **symmetric** if $A^{-1} = A$. A **neighborhood basis** at $e$ is a collection of neighborhoods such that any neighborhood of $e$ contains one. The full registry is on the topic page.

---

# Motivation

When working with a topological group, one wants to *reduce* questions about the global topology to questions about a neighborhood basis at $e$ — exploiting homogeneity ([[Thm - Translations are Homeomorphisms]]). But the standard neighborhood bases need not have nice algebraic structure. A neighborhood $V$ of $e$ might fail to be closed under inversion: $V^{-1}$ could be a different (also-open) neighborhood, with different content. This complicates arguments where one wants to "go forward and backward in $V$" — e.g., proving regularity, building local cross-sections, or constructing Haar measure.

Symmetric neighborhoods solve this. A symmetric neighborhood $V = V^{-1}$ contains $h$ iff it contains $h^{-1}$, so "moving in $V$ and reversing direction" stays within $V$. The theorem says: *every* neighborhood of $e$ contains a symmetric one. So we lose nothing by restricting to symmetric neighborhoods in any local argument. This becomes the workhorse for all "neighborhood at $e$" constructions.

The proof is a one-liner: given a neighborhood $V$, the set $V \cap V^{-1}$ is symmetric, open (intersection of two opens), and contains $e$ (since $e^{-1} = e \in V \cap V^{-1}$). So it is the symmetric neighborhood we want.

---

# Statement

Let $G$ be a topological group with identity $e$. The collection of **symmetric open neighborhoods** of $e$ — open sets $V$ containing $e$ with $V = V^{-1}$ — forms a neighborhood basis at $e$: every neighborhood of $e$ contains a symmetric open neighborhood of $e$.

**Strengthening (Bredon Proposition 15.8).** If $U$ is any neighborhood of $g$ in a topological group $G$, then there is a symmetric neighborhood $V$ of $e$ such that $VgV^{-1} \subseteq U$.

**Iteration (Bredon Proposition 15.9).** If $U$ is any neighborhood of $e$ and $n$ is a positive integer, then there is a symmetric neighborhood $V$ of $e$ such that $V^n \subseteq U$.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is just "any neighborhood of $e$".

A disguised source: **a continuous map $G \to G$ taking $e$ to $e$ (or any fixed point).** Property $B$: such a map's preimage of a neighborhood of $e$ is a neighborhood of $e$, hence contains a symmetric neighborhood. *Example:* the squaring map $h \mapsto h^2$; the conjugation map $h \mapsto ghg^{-1}$; the inversion. Each preserves neighborhoods of $e$ and admits a symmetric base.

**Targets (Output Amplification)**

The conclusion "symmetric neighborhoods are cofinal" lets us assume *without loss of generality* that any neighborhood of $e$ is symmetric — a small but essential simplification.

Combine with **squaring and shrinking.** Property $D$: we want $V^2 \subseteq U$ for given $U$. By continuity of $\mu$ at $(e, e)$, there is a neighborhood $W$ with $WW \subseteq U$. The amplified result $E$ (via this theorem): a symmetric $V \subseteq W$ exists with $V^2 \subseteq U$. *Example:* the proof of [[Thm - Topological Group is Regular]] uses this. Every step that "shrinks $U$ to $V$ with $V^2 \subseteq U$" implicitly uses this combination.

Combine with **iterated squaring (Bredon 15.9).** Property $D$: we want $V^n \subseteq U$ for given $U, n$. The amplified result $E$: a symmetric $V$ exists with $V^n \subseteq U$. Proof by induction using the above. *Example:* proving connectedness of $G$ from local connectedness at $e$.

Combine with **conjugation-stable neighborhoods (Bredon 15.8).** Property $D$: we want a neighborhood $V$ of $e$ with $gV g^{-1} \subseteq U$ for a given neighborhood $U$ of $e$. The amplified result $E$: such a $V$ exists. *Example:* in proving that the connected component of $e$ is normal.

---

# Why Is It True

The construction is forced. Given a neighborhood $V$ of $e$, we want a symmetric neighborhood $W \subseteq V$. The candidate is $W := V \cap V^{-1}$.

Why is $W$ symmetric? $W^{-1} = (V \cap V^{-1})^{-1} = V^{-1} \cap (V^{-1})^{-1} = V^{-1} \cap V = W$. The intersection is symmetric because we are intersecting two sets that are each other's inverses.

Why is $W$ open? $V$ is open by hypothesis. $V^{-1} = \iota(V)$ where $\iota$ is inversion; inversion is a continuous bijection with continuous inverse (it is itself, by $\iota^2 = 1$), so $\iota$ is a homeomorphism (by [[Thm - Translations are Homeomorphisms]]). The image of an open set under a homeomorphism is open. So $V^{-1}$ is open, and the intersection $V \cap V^{-1}$ is open.

Why does $W$ contain $e$? $e = e^{-1}$, so $e \in V \implies e \in V^{-1}$, so $e \in V \cap V^{-1} = W$.

The strengthened versions (Bredon 15.8 and 15.9) use the same idea plus continuity of multiplication. For 15.8: $g, U$ given, with $g \in U$. Conjugation $C_g$ is continuous (sends $e$ to $e$). The preimage $C_g^{-1}(U)$ is a neighborhood of $e$. By the symmetric basis, it contains a symmetric neighborhood $V$ of $e$, so $C_g(V) = gVg^{-1} \subseteq U$.

For 15.9: by continuity of $\mu$ at $(e, e)$, for any neighborhood $U$ of $e$ there is a neighborhood $W_1$ of $e$ with $W_1 W_1 \subseteq U$. Iterating: $W_2 W_2 \subseteq W_1$, so $W_2^4 \subseteq W_1^2 \subseteq U$. After $\log_2 n$ iterations, $W_k^n \subseteq U$. Take $V = W_k \cap W_k^{-1}$ to make it symmetric.

The reason to *expect* this result: any topological group has built-in symmetry from inversion (a homeomorphism that's its own inverse), so the natural neighborhood-basis structure should also have this symmetry built in. The lemma is just verifying that we can always extract the symmetric subneighborhood.

---

# What Makes This Hard

The proof is two lines — there is no real difficulty. The "hardness" is in *recognizing when to use symmetric neighborhoods*. The common error is to work with a non-symmetric neighborhood when a symmetric one would simplify the proof — particularly in the regularity argument where one needs $h^{-1} \in V$ as well as $h \in V$.

---

# Rederivation Scaffold

**High-level strategy:**
$V \cap V^{-1}$ is automatically symmetric (because $(V \cap V^{-1})^{-1} = V^{-1} \cap V$). It is open as the intersection of two opens (using inversion is a homeomorphism). It contains $e$ since $e^{-1} = e$.

**Subgoal decomposition:**

1. **Define $W = V \cap V^{-1}$.**
2. **Show $W$ is symmetric.** $(V \cap V^{-1})^{-1} = V^{-1} \cap V = W$.
3. **Show $W$ is open.** Inversion $\iota$ is a homeomorphism, so $V^{-1} = \iota(V)$ is open; intersection of opens is open.
4. **Show $W$ contains $e$.** $e \in V \implies e = e^{-1} \in V^{-1}$, so $e \in W$.

For Bredon 15.8: apply to the preimage of $U$ under $C_g$ (continuous, $C_g(e) = e$). For 15.9: iterate with continuity of $\mu$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Main theorem.** Let $V$ be a neighborhood of $e$ in $G$. Set $W := V \cap V^{-1}$.
>
> $W$ is symmetric: $W^{-1} = (V \cap V^{-1})^{-1} = V^{-1} \cap V = W$.
>
> $W$ is open: $V$ is open by assumption; $V^{-1} = \iota(V)$ is open because $\iota : G \to G$ is a homeomorphism (by [[Thm - Translations are Homeomorphisms]]), and homeomorphisms send open sets to open sets. So $W = V \cap V^{-1}$ is the intersection of two open sets, hence open.
>
> $W$ contains $e$: $e \in V$ (given) and $e = e^{-1} \in V^{-1}$, so $e \in V \cap V^{-1} = W$. $\blacksquare$
>
> **Strengthening to $VgV^{-1} \subseteq U$ (Bredon 15.8).** Let $U$ be a neighborhood of $g$. The map $\sigma : G \to G$, $\sigma(h) = ghg^{-1}$ — wait, we want $V$ with $VgV^{-1} \subseteq U$. Consider the map $G \times G \to G$, $(v, w) \mapsto vgw^{-1}$. This is continuous (multiplication and inversion are continuous) and sends $(e, e)$ to $g$. So the preimage of $U$ is an open neighborhood of $(e, e)$ in $G \times G$, which contains a basic open $W_1 \times W_2$ with $W_1, W_2$ neighborhoods of $e$. Let $W = W_1 \cap W_2$. Take a symmetric neighborhood $V \subseteq W$ (by the main theorem). Then for $v, w \in V$: $vgw^{-1} \in U$. So $VgV \subseteq U$, equivalently (using $V^{-1} = V$) $VgV^{-1} \subseteq U$. $\blacksquare$
>
> **Iteration to $V^n \subseteq U$ (Bredon 15.9).** Induct on $n$.
>
> Base case $n = 1$: trivially $V \subseteq U$ for $V = U \cap U^{-1}$.
>
> Inductive step: assume for $n$ there is a symmetric $V_n$ with $V_n^n \subseteq U$. For $n + 1$: by continuity of $\mu$ at $(e, e)$, there is a neighborhood $W$ of $e$ with $WW \subseteq V_n$. By the main theorem, take symmetric $V_{n+1} \subseteq W$. Then $V_{n+1}^{n+1} = V_{n+1} \cdot V_{n+1}^n \subseteq V_{n+1} \cdot W^n$. We need to bound $W^n$. By the inductive hypothesis applied to $V_n$: $V_n^n \subseteq U$. And $W \subseteq V_n$ (since $WW \subseteq V_n$ and $W$ contains $e$), so $W^n \subseteq V_n^n \subseteq U$. Hmm — this is not quite what we want; we want $V_{n+1}^{n+1} \subseteq U$. Let me redo. We have $V_{n+1} \subseteq W$ and $WW \subseteq V_n$. So $V_{n+1}^2 \subseteq V_n$, hence $V_{n+1}^{2n} \subseteq V_n^n \subseteq U$. So pick $V$ for $2n$-power, etc. The cleaner inductive argument: define $V_1 = $ symmetric in $U$. Given $V_k$ symmetric with $V_k^{2^k} \subseteq U$, find $W$ with $WW \subseteq V_k$, and let $V_{k+1}$ be symmetric in $W$. Then $V_{k+1}^{2^{k+1}} = (V_{k+1}^2)^{2^k} \subseteq V_k^{2^k} \subseteq U$. So for any $n$, taking $k = \lceil \log_2 n \rceil$ gives $V$ symmetric with $V^n \subseteq V^{2^k} \subseteq U$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Symmetric neighborhoods in Banach spaces.** A Banach space $V$ is a topological group $(V, +)$. A symmetric neighborhood of $0$ is a set $A = -A$. The unit ball, balanced absorbing sets, and seminorm balls are all symmetric. This is the foundation of the theory of bornology and locally convex spaces.

**Symmetric vs balanced sets.** In a topological vector space, "symmetric" generalizes to "balanced" ($\lambda A \subseteq A$ for $|\lambda| \leq 1$). A balanced neighborhood basis at $0$ exists in any topological vector space — the field-coefficient version of this theorem.

**Hausdorff property from symmetric neighborhoods.** A topological group is Hausdorff iff $\{e\}$ is closed iff for every $g \neq e$, there is a symmetric neighborhood $V$ of $e$ with $g \notin V$. The symmetric neighborhood basis is the natural setting for this argument.

---

# Bridges

- **[[Def - Topological Group]]** — provides the joint continuity of multiplication needed to construct nested symmetric neighborhoods.

- **[[Thm - Translations are Homeomorphisms]]** — used to show $V^{-1}$ is open (inversion is a homeomorphism).

- **[[Thm - Topological Group is Regular]]** — uses symmetric neighborhoods to construct disjoint open sets around closed sets.

---

# Unlocked by This

> [!tip] Regularity of Topological Groups *(from this topic)*
> The standard proof that every topological group is regular uses symmetric neighborhoods of $e$ in an essential way: choose $V$ with $V^2 \subseteq U$ (where $U$ is the given neighborhood); the closure $\overline{V}$ is contained in $V^2 \subseteq U$, exhibiting the regularity property.

> [!tip] Construction of Haar Measure *(from Measure Theory)*
> The construction of a left-invariant Radon measure on a locally compact group uses iterated symmetric neighborhoods to define an "approximate identity" and pass to a limit. The countable intersection of symmetric neighborhoods at $e$ — if it equals $\{e\}$ — gives metrizability of $G$ (Kakutani-Birkhoff theorem).
