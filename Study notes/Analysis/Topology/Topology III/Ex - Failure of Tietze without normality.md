---
type: exercise
subject: topology
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Tietze Extension Theorem"
  - "Thm - Urysohn's Lemma"
  - "Def - Hausdorff Space"
tags: [analysis, topology]
---

# Problem Statement

The **Tychonoff plank** is the space
$$T = ([0, \omega_1] \times [0, \omega_0]) \setminus \{(\omega_1, \omega_0)\},$$
where $\omega_0$ denotes the first infinite ordinal (so $[0, \omega_0] = \mathbb{N} \cup \{\infty\}$ — countably many points with one limit) and $\omega_1$ the first uncountable ordinal (so $[0, \omega_1]$ is uncountable, with a single limit point at the top). The plank carries the product topology (each factor has the order topology); the deleted corner $(\omega_1, \omega_0)$ is the only point where things go wrong.

(a) Show that $T$ is Hausdorff.

(b) Show that the two closed subsets
$$F = \{\omega_1\} \times [0, \omega_0) \quad \text{(the right edge, minus the corner)}$$
$$G = [0, \omega_1) \times \{\omega_0\} \quad \text{(the top edge, minus the corner)}$$
of $T$ are *closed* in $T$, are *disjoint*, but *cannot be separated by a continuous function* $f : T \to [0, 1]$.

Conclude that $T$ is Hausdorff but *not* normal, and in particular Urysohn's lemma and the Tietze extension theorem can fail without normality.

**Recall:**

A space $X$ is **normal** if for every pair of disjoint closed sets $F, G \subseteq X$ there exist disjoint open sets $U \supseteq F$ and $V \supseteq G$. Equivalently (by [[Thm - Urysohn's Lemma|Urysohn's lemma]]), there exists a continuous $f : X \to [0, 1]$ with $f \equiv 0$ on $F$ and $f \equiv 1$ on $G$. *Normal* is strictly stronger than **Hausdorff** — the Tychonoff plank is the canonical counterexample.

An **ordinal** is the order type of a well-ordered set. $\omega_0$ is the first infinite ordinal; $\omega_1$ the first uncountable ordinal. Any countable union of countable sets below $\omega_1$ remains below $\omega_1$ (regularity of $\omega_1$). The order topology on an ordinal $[0, \alpha]$ has basis the open intervals $(\beta, \gamma)$ together with the initial intervals $[0, \beta)$ and final intervals $(\beta, \alpha]$.

---

# Convergent Strategy

**Problem class.** A *counterexample-construction* exercise: build a space where the standard tool (Urysohn/Tietze) fails. This requires (i) constructing the space, (ii) verifying it satisfies *some* properties (Hausdorff), (iii) exhibiting failure of *more* (normality, via a specific obstruction).

**Assumption pattern.** The plank has two infinite directions: the long ordinal $\omega_1$ (uncountable) and the short ordinal $\omega_0$ (countable). The deleted corner $(\omega_1, \omega_0)$ means functions on $T$ have no constraint at infinity — but the topological obstructions of the corner *do* propagate into $T$.

**Theorem routing.** The proof that $T$ is Hausdorff is straightforward — the product of Hausdorff is Hausdorff, see [[Ex - Product of Hausdorff is Hausdorff]]; the deleted subspace inherits. The proof of non-normality uses an ordinal pigeonhole argument: any continuous $f : T \to [0, 1]$ must satisfy that $f(\omega_1, n)$ stabilizes as one approaches $\omega_1$ from below (for each $n$), and the stable values cluster as $n \to \omega_0$, forcing $f|_F$ and $f|_G$ to be limits of the same family of values — preventing a clean separation.

**Key decision point.** The crux is the **pressing-down lemma** flavor argument: a continuous map from a closed unbounded subset of $[0, \omega_1)$ to a separable metric space (like $\mathbb{R}$) must be eventually constant — there are only countably many values it can take cofinally. This forces $f(\omega_1, n)$ to be defined as a single limiting value $a_n$ for each $n$, and the $a_n$ then converge (because $f$ is continuous along the second coordinate near $\omega_0$), contradicting the requirement that $f|_F = 0$, $f|_G = 1$.

---

# Legal Operations Used

1. **Use the order topology on an ordinal.** Open sets are unions of open intervals; for limit ordinals, "approaching from below" gives the standard convergence.

2. **Exploit the regularity of $\omega_1$ (countable cofinality is impossible).** A countable subset of $[0, \omega_1)$ is bounded above by some ordinal $< \omega_1$.

3. **Use the pigeonhole on continuous maps to $\mathbb{R}$.** A continuous function $[0, \omega_1] \to \mathbb{R}$ is eventually constant, since $[0, \omega_1]$ is compact and continuous images of compact are compact, but the value at $\omega_1$ is the limit of values approaching, forcing eventual stability.

---

# Hints

> [!note]- Hint 1
> *(a) Hausdorff.* Product of Hausdorff is Hausdorff ([[Ex - Product of Hausdorff is Hausdorff]]); a subspace of Hausdorff is Hausdorff. Each ordinal $[0, \alpha]$ with the order topology is Hausdorff. So $T$ is Hausdorff.

> [!note]- Hint 2
> *(b) Closedness.* $F = \{\omega_1\} \times [0, \omega_0)$ and $G = [0, \omega_1) \times \{\omega_0\}$ are closed in $T$, since the ambient $[0, \omega_1] \times [0, \omega_0]$ is compact Hausdorff and each is the intersection of a closed set with $T$. *Disjointness:* immediate, $F$ has first coordinate $\omega_1$, $G$ has second coordinate $\omega_0$, but their intersection in $[0, \omega_1] \times [0, \omega_0]$ is the single deleted point.

> [!note]- Hint 3
> *Key ordinal lemma.* A continuous $\phi : [0, \omega_1] \to \mathbb{R}$ (or any separable metric space) is *eventually constant*: there is $\alpha < \omega_1$ with $\phi(\beta) = \phi(\omega_1)$ for all $\beta \in [\alpha, \omega_1]$. Proof: by continuity, $\phi^{-1}(\phi(\omega_1) - 1/n, \phi(\omega_1) + 1/n)$ contains a neighborhood of $\omega_1$, hence an interval $(\alpha_n, \omega_1]$. Set $\alpha = \sup_n \alpha_n < \omega_1$ (countable sup of ordinals $< \omega_1$ is $< \omega_1$ by regularity of $\omega_1$). For $\beta > \alpha$, $|\phi(\beta) - \phi(\omega_1)| < 1/n$ for all $n$, so $\phi(\beta) = \phi(\omega_1)$.

> [!note]- Hint 4
> Suppose $f : T \to [0, 1]$ continuous with $f|_F = 0$, $f|_G = 1$. For each $n < \omega_0$, the slice $[0, \omega_1] \to \mathbb{R}$, $\beta \mapsto f(\beta, n)$, has a well-defined continuous extension to $\beta = \omega_1$ given by $f(\omega_1, n) = 0$ (since $(\omega_1, n) \in F$). By the lemma, this map is eventually constant — equal to $0$ on $[\alpha_n, \omega_1]$ for some $\alpha_n < \omega_1$.

> [!note]- Hint 5
> Set $\alpha = \sup_n \alpha_n$. Since $\{\alpha_n\}_{n < \omega_0}$ is a countable family of countable ordinals, $\alpha < \omega_1$ (regularity). So $f(\alpha + 1, n) = 0$ for all $n$. But $(\alpha + 1, n) \to (\alpha + 1, \omega_0)$ as $n \to \omega_0$, and $(\alpha + 1, \omega_0) \in G$ (since $\alpha + 1 < \omega_1$), so $f(\alpha + 1, \omega_0) = 1$. Continuity: $0 = \lim_n f(\alpha + 1, n) = f(\alpha + 1, \omega_0) = 1$. Contradiction.

---

# Solution

The Tychonoff plank is the canonical Hausdorff non-normal space. The obstruction is a deep ordinal phenomenon: continuous maps to a separable space must be "eventually constant" approaching $\omega_1$ from below, and this stability forces the two closed edges to agree on a continuous function — preventing separation.

**Step 1: $T$ is Hausdorff.**

> [!note]- Derivation
> The order topology on $[0, \omega_1]$ is Hausdorff: given distinct $\alpha < \beta$ in $[0, \omega_1]$, the open intervals $[0, \gamma)$ and $(\gamma, \omega_1]$ for any $\gamma$ strictly between them give disjoint open neighborhoods. (For consecutive ordinals $\beta = \alpha + 1$, use $[0, \beta) = [0, \alpha + 1) = [0, \alpha]$ and $\{\beta\}$; the singleton $\{\beta\}$ is open in the order topology when $\beta$ is a successor.) Similarly $[0, \omega_0]$ is Hausdorff.
>
> The product of Hausdorff is Hausdorff ([[Ex - Product of Hausdorff is Hausdorff]]). A subspace of Hausdorff is Hausdorff (any pair of points in $T$ are also distinct in the ambient $[0, \omega_1] \times [0, \omega_0]$, so are separated by disjoint opens whose restrictions to $T$ are disjoint opens in $T$). Hence $T$ is Hausdorff.

**Step 2: $F$ and $G$ are closed and disjoint in $T$.**

> [!note]- Derivation
> *Closedness.* In the ambient $[0, \omega_1] \times [0, \omega_0]$ (compact Hausdorff), $\{\omega_1\} \times [0, \omega_0]$ is closed (preimage of the closed set $\{\omega_1\}$ under the projection). Intersecting with $T$ (an open subset) gives a relatively closed set. The set $F = \{\omega_1\} \times [0, \omega_0) = (\{\omega_1\} \times [0, \omega_0]) \cap T$ is the intersection of this closed set with $T$, hence closed in $T$. Similarly $G$ is closed in $T$.
>
> *Disjointness.* $F \cap G$ would consist of points $(x, y)$ with $x = \omega_1$ *and* $y = \omega_0$, i.e. the single point $(\omega_1, \omega_0)$ — but this point has been removed from $T$. So $F \cap G = \emptyset$.

**Step 3: The key ordinal lemma — continuous maps $[0, \omega_1] \to \mathbb{R}$ are eventually constant.**

For every continuous $\phi : [0, \omega_1] \to \mathbb{R}$, there exists $\alpha_\phi < \omega_1$ with $\phi(\beta) = \phi(\omega_1)$ for all $\beta \in [\alpha_\phi, \omega_1]$.

> [!note]- Derivation
> By continuity at $\omega_1$, for each $n \geq 1$, $\phi^{-1}(\phi(\omega_1) - 1/n, \phi(\omega_1) + 1/n)$ is an open neighborhood of $\omega_1$, hence contains some basic open $(\gamma_n, \omega_1]$ with $\gamma_n < \omega_1$. Set $\alpha_\phi = \sup_n \gamma_n$.
>
> *Claim: $\alpha_\phi < \omega_1$.* This uses the **regularity of $\omega_1$**: a countable family $\{\gamma_n\}_n$ of ordinals $< \omega_1$ has a supremum strictly less than $\omega_1$. (If the supremum were $\omega_1$, then $\omega_1$ would be the sup of a countable cofinal sequence, making $\omega_1$ a countable union of countable ordinals — hence countable — contradicting the definition of $\omega_1$ as the first *uncountable* ordinal.)
>
> *Claim: $\phi$ is constant equal to $\phi(\omega_1)$ on $(\alpha_\phi, \omega_1]$.* For $\beta \in (\alpha_\phi, \omega_1]$, $\beta > \gamma_n$ for every $n$, so $\beta \in (\gamma_n, \omega_1] \subseteq \phi^{-1}(\phi(\omega_1) - 1/n, \phi(\omega_1) + 1/n)$. Hence $|\phi(\beta) - \phi(\omega_1)| < 1/n$ for every $n$, so $\phi(\beta) = \phi(\omega_1)$.
>
> By taking $\alpha_\phi + 1$ if necessary (so that $\alpha_\phi$ is itself in the "constant zone"), we may assume $\phi(\alpha_\phi) = \phi(\omega_1)$. This is the "eventually constant" property — the values of $\phi$ approaching $\omega_1$ from below stabilize at $\phi(\omega_1)$ once you pass some countable ordinal.

**Step 4: Use the lemma to derive a contradiction from a supposed continuous separator.**

Suppose for contradiction $f : T \to [0, 1]$ is continuous with $f|_F = 0$ and $f|_G = 1$. For each $n < \omega_0$, consider the slice $\phi_n : [0, \omega_1] \to [0, 1]$ defined by $\phi_n(\beta) = f(\beta, n)$ — well-defined because for every $\beta \leq \omega_1$ and every $n < \omega_0$, the point $(\beta, n) \in T$ (only the corner $(\omega_1, \omega_0)$ is missing). The function $\phi_n$ is continuous as a composition of the continuous inclusion $[0, \omega_1] \hookrightarrow T$ with $f$.

> [!note]- Derivation
> *Boundary value.* At $\beta = \omega_1$, $\phi_n(\omega_1) = f(\omega_1, n)$. Since $(\omega_1, n) \in F$ (as $n < \omega_0$, $n \neq \omega_0$), $f(\omega_1, n) = 0$. So $\phi_n(\omega_1) = 0$.
>
> *Eventual constancy.* By Step 3, there exists $\alpha_n < \omega_1$ with $\phi_n(\beta) = \phi_n(\omega_1) = 0$ for all $\beta \in [\alpha_n, \omega_1]$.
>
> *Combine countably many $\alpha_n$.* Set $\alpha = \sup_{n < \omega_0} \alpha_n$. The supremum of countably many ordinals $< \omega_1$ is $< \omega_1$ (regularity of $\omega_1$ again). So $\alpha < \omega_1$, and $\alpha + 1 < \omega_1$ as well.
>
> *Force a contradiction.* For every $n < \omega_0$, $\alpha + 1 > \alpha \geq \alpha_n$, so $\phi_n(\alpha + 1) = 0$, that is $f(\alpha + 1, n) = 0$ for every $n < \omega_0$.
>
> Now slide $n \to \omega_0$. The point $(\alpha + 1, \omega_0)$ is in $T$ (since $\alpha + 1 < \omega_1$, the corner is not removed), and in fact lies in $G$ (since $\alpha + 1 < \omega_1$ and second coordinate is $\omega_0$). So $f(\alpha + 1, \omega_0) = 1$.
>
> By continuity of the map $n \mapsto f(\alpha + 1, n)$ on $[0, \omega_0]$,
> $$f(\alpha + 1, \omega_0) = \lim_{n \to \omega_0} f(\alpha + 1, n).$$
> The left side is $1$ (in $G$); the right side is $\lim_n 0 = 0$ (by the eventual constancy). So $0 = 1$ — contradiction.

**Step 5: Conclude $T$ is not normal.**

> [!note]- Derivation
> Were $T$ normal, [[Thm - Urysohn's Lemma|Urysohn's lemma]] would produce the continuous separator $f$ for the disjoint closed sets $F$ and $G$ — contradicting Step 4. So $T$ is not normal.
>
> Moreover, the continuous function $h : F \cup G \to [0, 1]$ defined by $h|_F = 0$, $h|_G = 1$ (well-defined and continuous on the closed $F \cup G$ since $F$ and $G$ are disjoint closed) does *not* extend to a continuous function on $T$ — the extension would witness the failed separation. So [[Thm - Tietze Extension Theorem|Tietze]] fails on $T$ as well.

> [!note]- Complete formal solution
> *(a)* Product of Hausdorff is Hausdorff (see [[Ex - Product of Hausdorff is Hausdorff]]); subspace of Hausdorff is Hausdorff.
>
> *(b) Closed disjoint.* $F = \{\omega_1\} \times [0, \omega_0)$, $G = [0, \omega_1) \times \{\omega_0\}$ are intersections of closed sets in the ambient product with $T$, hence closed; intersection is empty in $T$ (would require the deleted corner).
>
> *Lemma.* Continuous $\phi : [0, \omega_1] \to \mathbb{R}$ is constant on $[\alpha_\phi, \omega_1]$ for some $\alpha_\phi < \omega_1$ (regularity of $\omega_1$: countable cofinal in $\omega_1$ is impossible).
>
> *Failure.* If $f : T \to [0, 1]$ continuous with $f|_F = 0$, $f|_G = 1$: each slice $\phi_n(\beta) = f(\beta, n)$ has $\phi_n(\omega_1) = 0$ (since $(\omega_1, n) \in F$), so by the lemma $\phi_n \equiv 0$ on $[\alpha_n, \omega_1]$. Setting $\alpha = \sup_n \alpha_n < \omega_1$ (countable sup), $f(\alpha + 1, n) = 0$ for all $n < \omega_0$. But $(\alpha + 1, \omega_0) \in G$ gives $f(\alpha + 1, \omega_0) = 1$, contradicting continuity of $n \mapsto f(\alpha + 1, n)$ at $n = \omega_0$. So $T$ is not normal. Urysohn and Tietze fail. $\blacksquare$

---

# Key Takeaways

**The Tychonoff plank is the canonical Hausdorff-but-not-normal space and the standard witness that Urysohn/Tietze require normality.** It is a *compact* space (with the corner deleted from the compact $[0, \omega_1] \times [0, \omega_0]$, the result is locally compact, not compact — but this distinction does not save it). Normality is genuinely needed for Urysohn and Tietze — the abstract proofs cannot be weakened. This justifies the "illegal but tempting" warning about claiming Urysohn/Tietze for non-normal spaces ([[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact#Legal Operations]]). Always check normality before invoking these tools; in compact Hausdorff, in metric, or in paracompact Hausdorff spaces, normality is automatic, but elsewhere it must be verified.

**The pressing-down / closing-up phenomenon on $\omega_1$: continuous maps must "stabilize" approaching $\omega_1$.** This is a set-theoretic fact about uncountable ordinals: any countable family of countable ordinals has a countable supremum (regularity of $\omega_1$), so a continuous map to a separable space picks up only countably many values cofinally, hence eventually only one. This is the *real* mechanism by which the plank is non-normal — the obstruction is the topological-set-theoretic interplay between $\omega_1$'s cofinality and the separability of $[0, 1]$. The general principle: any continuous map from $[0, \omega_1]$ to a metric space is eventually constant. This generalizes to *pressing-down* and *closing-up* lemmas in set theory.

**Trigger-reaction: "I want to construct a Hausdorff-but-not-X counterexample" ⇒ "use ordinal spaces, especially $[0, \omega_1]$".** Ordinal spaces are the workhorses of pathological examples in general topology: $[0, \omega_1]$ is sequentially compact (every sequence has a convergent subsequence — in fact, by the lemma, all sequences are eventually constant) but is *not* first countable at $\omega_1$ (no countable neighborhood base). The plank is Hausdorff non-normal. The long line is Hausdorff, manifold, but not paracompact (see [[Ex - A non-paracompact space]]). $\omega_1$ itself (without the top point) is countably compact but not compact. Each of these is built from set-theoretic features of ordinals. Knowing these standard examples lets one quickly check the *necessity* of various hypotheses.

**Normality is "not preserved by all standard constructions" and is genuinely subtle.** Subspaces of normal spaces need not be normal (the closed subspace $F \cup G$ of the plank is normal, but the plank itself is not; the *open* subspace of the plank obtained by deleting just one edge is normal). Products of normal spaces need not be normal (the Sorgenfrey line is normal, but its square is not). The class of normal spaces is *not* closed under nice operations, which is why one often weakens to "paracompact" or strengthens to "metrizable" to get a class closed under more operations. The intuition: normality is a "global" property and is more fragile than the "local" properties like Hausdorffness or local compactness.

**The plank reveals where the separation hierarchy gets nontrivial.** The chain $T_1 \subseteq T_2 = $ Hausdorff $\subseteq T_3 = $ regular $\subseteq T_{3.5} = $ completely regular $\subseteq T_4 = $ normal is a strict chain — every inclusion has a counterexample, and the plank lives precisely in $T_{3.5} \setminus T_4$ (completely regular but not normal). Counterexamples for the other inclusions exist but are less famous: the Sierpinski space ($T_0$ but not $T_1$); the cofinite topology ($T_1$ but not $T_2$); the Moore plane / Niemytzki plane ($T_3$ but not $T_{3.5}$). Recognizing where on the hierarchy a given space sits, and what hypotheses each step buys, is part of the topology curriculum.

**Subtle interplay between non-normality and global function-extension.** The plank is *completely regular* (Tychonoff), meaning points can be separated from closed sets by continuous functions — so it has plenty of continuous real-valued functions for "local" purposes, and in fact embeds into a cube $[0, 1]^I$ for some index set $I$, hence is a subspace of a normal space. But its global structure (two closed edges) cannot be separated by a single continuous function. This shows that pointwise / local function-richness ≠ normality, and explains why the Stone–Čech compactification (which uses only complete regularity, not normality — see [[Thm - Stone–Čech Compactification]]) is the right "function-rich" compactification.
