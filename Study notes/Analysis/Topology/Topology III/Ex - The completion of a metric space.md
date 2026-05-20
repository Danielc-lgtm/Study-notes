---
type: exercise
subject: topology
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Cauchy Sequence and Complete Metric Space"
  - "Def - Metric Space"
tags: [analysis, topology]
---

# Problem Statement

Let $(X, d)$ be a metric space. The **completion** of $X$ is constructed as follows. Let
$$\mathcal{C}(X) = \{\{x_n\}_{n=1}^\infty : \{x_n\} \text{ is a Cauchy sequence in } X\}$$
and define an equivalence relation on $\mathcal{C}(X)$ by
$$\{x_n\} \sim \{y_n\} \iff d(x_n, y_n) \to 0.$$
Let $\widehat{X} = \mathcal{C}(X)/\sim$, the set of equivalence classes, and define
$$\widehat{d}([\{x_n\}], [\{y_n\}]) = \lim_{n \to \infty} d(x_n, y_n).$$

(a) Show that $\widehat{d}$ is a well-defined metric on $\widehat{X}$: the limit exists, is independent of representatives, satisfies the metric axioms.

(b) Show that the map $\iota : X \to \widehat{X}$, $x \mapsto [\{x, x, x, \dots\}]$ (the class of the constant sequence at $x$), is an **isometric embedding** with **dense image**.

(c) Show that $\widehat{X}$ is **complete**.

**Recall:**

A **Cauchy sequence** in $(X, d)$ is $\{x_n\}$ with $d(x_n, x_m) \to 0$ as $n, m \to \infty$ — equivalently, for every $\varepsilon > 0$ there is $N$ with $d(x_n, x_m) < \varepsilon$ for all $n, m \geq N$. A metric space is **complete** if every Cauchy sequence converges.

![[Def - Cauchy Sequence and Complete Metric Space#The Definition]]

An **isometric embedding** is a map $\iota : (X, d) \to (Y, d')$ with $d'(\iota(x), \iota(y)) = d(x, y)$ for all $x, y$ — it preserves distances exactly. Such a map is automatically injective and continuous (in fact a homeomorphism onto its image). The image $\iota(X)$ is **dense** in $Y$ if every nonempty open set in $Y$ contains a point of $\iota(X)$, equivalently $\overline{\iota(X)} = Y$.

---

# Convergent Strategy

**Problem class.** This is the canonical *universal construction* problem: build a "completion" of a structure by adjoining limit points of all Cauchy sequences. The structure of the proof is essentially fixed across all such constructions (completion of metric spaces, completion of normed spaces to Banach spaces, completion of inner product spaces to Hilbert spaces, completion of fields with absolute value to $p$-adic fields, completion of topological groups, completion of uniform spaces). Once you understand this one, you understand all of them.

**Assumption pattern.** Cauchy sequences fail to converge in $X$ but *would* converge in a hypothetical larger space; the construction declares each Cauchy sequence to *be* its own limit point in $\widehat X$, modulo the natural equivalence "two sequences should have the same limit iff their distance goes to zero". The triangle inequality $|d(x_n, y_n) - d(x_m, y_m)| \leq d(x_n, x_m) + d(y_n, y_m)$ — the *reverse triangle inequality* for distances — is the technical engine making everything work.

**Theorem routing.** Three separate arguments:
- (a) *Well-definedness:* the distance function $n \mapsto d(x_n, y_n)$ is itself Cauchy in $\mathbb{R}$ (by the reverse triangle inequality), so its limit exists; representative-independence comes from another application of reverse triangle inequality.
- (b) *Embedding:* constant sequences have $d(x_n, y_n) = d(x, y)$ for all $n$, so the limit is $d(x, y)$ — distance preservation is immediate. Density: given $[\{x_n\}] \in \widehat X$, approximate by the constants $\iota(x_N)$ for large $N$.
- (c) *Completeness:* given a Cauchy sequence $\{[\alpha^{(m)}]\}$ in $\widehat X$, choose representatives carefully (each $\alpha^{(m)} = \{\alpha^{(m)}_n\}$ has its own Cauchy slow-down rate), then use a *diagonal* sequence $y_m = \alpha^{(m)}_{n(m)}$ for cleverly chosen $n(m)$.

**Key decision point.** The diagonal extraction in (c) is the technically hardest step — choose $n(m)$ growing fast enough that $d(\alpha^{(m)}_{n(m)}, \alpha^{(m)}_n) < 1/m$ for all $n \geq n(m)$, so that the *single* sequence $\{y_m\}$ inherits Cauchy-ness from the sequence-of-classes' Cauchy-ness. Without this rate-management, completeness fails.

---

# Legal Operations Used

1. **The reverse triangle inequality $|d(a, c) - d(b, c)| \leq d(a, b)$** — the workhorse for stability arguments about distance functions. Applied repeatedly: to show the limit of $d(x_n, y_n)$ exists, to show representative-independence, to show the diagonal sequence is Cauchy.

2. **Equivalence-class arithmetic: define an operation on representatives, prove independence of choice.** Standard technique whenever a quotient set is being made into a structure.

3. **Density via approximation.** To show $\iota(X)$ is dense in $\widehat X$, show every $[\{x_n\}]$ is the limit of constant sequences $\iota(x_N)$.

4. **Diagonal extraction.** When you have a sequence of Cauchy sequences, the limit point is built by choosing one element from each sequence with carefully managed indices.

---

# Hints

> [!note]- Hint 1
> *(a, limit exists).* Use $|d(x_n, y_n) - d(x_m, y_m)| \leq d(x_n, x_m) + d(y_n, y_m)$. This shows $\{d(x_n, y_n)\}$ is a Cauchy sequence in $\mathbb{R}$ (since $\{x_n\}, \{y_n\}$ are Cauchy in $X$), so it converges in $\mathbb{R}$ by completeness of $\mathbb{R}$.

> [!note]- Hint 2
> *(a, well-defined).* Suppose $\{x_n\} \sim \{x_n'\}$ and $\{y_n\} \sim \{y_n'\}$. Then $|d(x_n, y_n) - d(x_n', y_n')| \leq d(x_n, x_n') + d(y_n, y_n') \to 0$, so the two limits are equal.

> [!note]- Hint 3
> *(b, density).* Given $[\{x_n\}] \in \widehat X$, set $\xi_N = \iota(x_N) = [\{x_N, x_N, x_N, \dots\}]$. Show $\widehat d(\xi_N, [\{x_n\}]) = \lim_n d(x_N, x_n) \to 0$ as $N \to \infty$ (by Cauchy-ness of $\{x_n\}$).

> [!note]- Hint 4
> *(c, diagonal).* Let $\{[\alpha^{(m)}]\}$ be Cauchy in $\widehat X$. For each $m$, choose $n(m)$ with $d(\alpha^{(m)}_{n(m)}, \alpha^{(m)}_n) < 1/m$ for all $n \geq n(m)$. Set $y_m = \alpha^{(m)}_{n(m)}$. Show $\{y_m\}$ is Cauchy in $X$ and that $[\{y_m\}]$ is the limit of $\{[\alpha^{(m)}]\}$ in $\widehat X$.

---

# Solution

The completion construction realizes every Cauchy sequence of $X$ as a *bona fide* point of a larger space $\widehat X$ — by definition, taking the Cauchy sequence and *calling it* its own limit, with two sequences identified when they should have had the same limit. The structure of the proof is identical to every other "completion" in mathematics, and pivots on the reverse triangle inequality.

**Step 1: The limit $\lim d(x_n, y_n)$ exists in $\mathbb{R}$.**

For Cauchy $\{x_n\}, \{y_n\}$ in $X$, the sequence $\{d(x_n, y_n)\}$ is Cauchy in $\mathbb{R}$, hence converges.

> [!note]- Derivation
> The reverse triangle inequality gives
> $$|d(x_n, y_n) - d(x_m, y_m)| \leq d(x_n, x_m) + d(y_n, y_m).$$
> The right side tends to $0$ as $n, m \to \infty$ (by Cauchy-ness of $\{x_n\}$ and $\{y_n\}$), so the sequence $\{d(x_n, y_n)\}_n$ is Cauchy in $\mathbb{R}$. Since $\mathbb{R}$ is complete, the limit exists.
>
> Proof of the reverse triangle inequality: by the regular triangle inequality, $d(x_n, y_n) \leq d(x_n, x_m) + d(x_m, y_m) + d(y_m, y_n)$, so $d(x_n, y_n) - d(x_m, y_m) \leq d(x_n, x_m) + d(y_n, y_m)$; swapping $n \leftrightarrow m$ gives the reverse, hence the absolute value.

**Step 2: $\widehat d$ is independent of representatives, hence well-defined.**

If $\{x_n\} \sim \{x_n'\}$ and $\{y_n\} \sim \{y_n'\}$, then $\lim d(x_n, y_n) = \lim d(x_n', y_n')$.

> [!note]- Derivation
> Apply the reverse triangle inequality again:
> $$|d(x_n, y_n) - d(x_n', y_n')| \leq d(x_n, x_n') + d(y_n, y_n') \to 0$$
> by the equivalence-relation conditions $d(x_n, x_n'), d(y_n, y_n') \to 0$. So the two limits agree, and $\widehat d$ depends only on the equivalence classes.

**Step 3: $\widehat d$ satisfies the metric axioms.**

> [!note]- Derivation
> *Non-negativity and reflexivity.* $\widehat d \geq 0$ obvious. $\widehat d([\{x_n\}], [\{y_n\}]) = 0$ iff $\lim d(x_n, y_n) = 0$ iff $\{x_n\} \sim \{y_n\}$ iff their classes are equal.
>
> *Symmetry.* $\widehat d([\{x_n\}], [\{y_n\}]) = \lim d(x_n, y_n) = \lim d(y_n, x_n) = \widehat d([\{y_n\}], [\{x_n\}])$ by symmetry of $d$.
>
> *Triangle inequality.* For three classes $[\{x_n\}], [\{y_n\}], [\{z_n\}]$, $d(x_n, z_n) \leq d(x_n, y_n) + d(y_n, z_n)$ for every $n$; taking limits preserves the inequality:
> $$\widehat d([\{x_n\}], [\{z_n\}]) \leq \widehat d([\{x_n\}], [\{y_n\}]) + \widehat d([\{y_n\}], [\{z_n\}]).$$

**Step 4: $\iota$ is an isometric embedding.**

For $x, y \in X$, $\widehat d(\iota(x), \iota(y)) = d(x, y)$. In particular $\iota$ is injective and continuous (a homeomorphism onto its image).

> [!note]- Derivation
> $\iota(x) = [\{x, x, x, \dots\}]$, so
> $$\widehat d(\iota(x), \iota(y)) = \lim_{n \to \infty} d(x, y) = d(x, y).$$
> Distance preservation is automatic from the constant representative. Distance preservation implies injectivity ($d(x, y) = 0 \iff x = y$), and any distance-preserving map between metric spaces is continuous.

**Step 5: $\iota(X)$ is dense in $\widehat X$.**

Every $\xi \in \widehat X$ is a limit of points in $\iota(X)$.

> [!note]- Derivation
> Take $\xi = [\{x_n\}] \in \widehat X$. Set $\xi_N = \iota(x_N) = [\{x_N, x_N, \dots\}]$. Then
> $$\widehat d(\xi_N, \xi) = \lim_{n \to \infty} d(x_N, x_n).$$
> Since $\{x_n\}$ is Cauchy, given $\varepsilon > 0$ there is $N_0$ with $d(x_N, x_n) < \varepsilon$ for all $N, n \geq N_0$; the limit in $n$ is $\leq \varepsilon$, so $\widehat d(\xi_N, \xi) \leq \varepsilon$ for $N \geq N_0$. Hence $\xi_N \to \xi$ as $N \to \infty$ in $\widehat X$, so $\iota(X)$ is dense.

**Step 6: $\widehat X$ is complete (the diagonal argument).**

A Cauchy sequence $\{\eta^{(m)}\}$ in $\widehat X$ converges to some $\eta \in \widehat X$.

> [!note]- Derivation
> Write $\eta^{(m)} = [\alpha^{(m)}]$ with $\alpha^{(m)} = \{\alpha^{(m)}_n\}_{n=1}^\infty$ a Cauchy sequence in $X$. For each $m$, by Cauchy-ness of $\alpha^{(m)}$ in $X$, pick $n(m)$ with
> $$d(\alpha^{(m)}_n, \alpha^{(m)}_{n'}) < \frac{1}{m} \quad \text{for all } n, n' \geq n(m).$$
> Define the *diagonal sequence* $y_m = \alpha^{(m)}_{n(m)}$ in $X$.
>
> *Claim 1: $\{y_m\}$ is Cauchy in $X$.* Estimate
> $$d(y_m, y_{m'}) = d(\alpha^{(m)}_{n(m)}, \alpha^{(m')}_{n(m')}).$$
> We need to bridge between the $m$ and $m'$ representatives. The key observation: for the constant sequence at $y_m$ (i.e. $\iota(y_m)$),
> $$\widehat d(\iota(y_m), \eta^{(m)}) = \lim_n d(y_m, \alpha^{(m)}_n) \leq \frac{1}{m}$$
> (taking $n \geq n(m)$ in the choice). Then
> $$d(y_m, y_{m'}) = \widehat d(\iota(y_m), \iota(y_{m'})) \leq \widehat d(\iota(y_m), \eta^{(m)}) + \widehat d(\eta^{(m)}, \eta^{(m')}) + \widehat d(\eta^{(m')}, \iota(y_{m'}))$$
> $$\leq \frac{1}{m} + \widehat d(\eta^{(m)}, \eta^{(m')}) + \frac{1}{m'} \to 0$$
> as $m, m' \to \infty$ (Cauchy-ness of $\{\eta^{(m)}\}$ in $\widehat X$). So $\{y_m\}$ is Cauchy in $X$, i.e. defines an element $\eta = [\{y_m\}] \in \widehat X$.
>
> *Claim 2: $\eta^{(m)} \to \eta$ in $\widehat X$.* Compute
> $$\widehat d(\eta^{(m)}, \eta) \leq \widehat d(\eta^{(m)}, \iota(y_m)) + \widehat d(\iota(y_m), \eta) \leq \frac{1}{m} + \widehat d(\iota(y_m), \eta).$$
> The second term is $\lim_n d(y_m, y_n)$, which tends to $0$ as $m \to \infty$ since $\{y_n\}$ is Cauchy in $X$ (so the tails are uniformly small). Hence $\widehat d(\eta^{(m)}, \eta) \to 0$, completing the proof.

> [!note]- Complete formal solution
> *(a) Metric.* The reverse triangle inequality gives that $\{d(x_n, y_n)\}$ is Cauchy in $\mathbb{R}$ for Cauchy $\{x_n\}, \{y_n\}$, so the limit exists. Independence of representatives, and the three metric axioms, follow from the same inequality and basic limit operations.
>
> *(b) Embedding.* $\widehat d(\iota(x), \iota(y)) = \lim d(x, y) = d(x, y)$, an isometric embedding. For density: $\widehat d(\iota(x_N), [\{x_n\}]) = \lim_n d(x_N, x_n) \leq \varepsilon$ for $N$ large, by Cauchy-ness of $\{x_n\}$.
>
> *(c) Completeness.* Given Cauchy $\{\eta^{(m)} = [\alpha^{(m)}]\}$ in $\widehat X$, choose $n(m)$ with $d(\alpha^{(m)}_n, \alpha^{(m)}_{n(m)}) < 1/m$ for $n \geq n(m)$, and let $y_m = \alpha^{(m)}_{n(m)}$. Triangle inequality shows $\{y_m\}$ Cauchy in $X$, $\eta = [\{y_m\}] \in \widehat X$, and $\widehat d(\eta^{(m)}, \eta) \to 0$. $\blacksquare$

---

# Key Takeaways

**Completion realizes every "would-be limit" as an honest point of a larger space.** This construction is the prototype for an enormous range of "adjoin limits" constructions in mathematics: completing a normed space gives a Banach space, completing an inner product space gives a Hilbert space, completing $\mathbb{Q}$ with respect to the $p$-adic absolute value gives $\mathbb{Q}_p$, completing $\mathbb{Q}$ with respect to the usual absolute value gives $\mathbb{R}$, completing a topological group gives a complete topological group. In each case the recipe is the same: equivalence classes of Cauchy sequences, with the operations (norm, inner product, group operation) extended by continuity. Understanding this one construction is understanding all of them. The reverse triangle inequality is the universal stability tool; the diagonal extraction is the universal completeness mechanism.

**The reverse triangle inequality is the workhorse of "stability" arguments.** $|d(a, c) - d(b, c)| \leq d(a, b)$ says that distance is itself a $1$-Lipschitz function, and this fact is what allows the entire completion construction: limits of distances exist because distances are continuous, representative-independence holds because small distances between representatives propagate to small differences in the limit. The general principle: any time you have a function defined on a metric space and need to control how it varies under small perturbations, the reverse triangle inequality for distance functions is the first thing to reach for. It is also what makes the metric continuous as a function of its arguments, which underlies essentially every topological reformulation of metric facts.

**Diagonal extraction is the standard trick to build a single Cauchy sequence from a sequence of Cauchy sequences.** When the input is "a Cauchy sequence of Cauchy sequences" and the output needs to be "a single Cauchy sequence representing the limit class", you cannot just pick the first element of each — you have to pick later and later elements as the index increases, with the rate of "going later" controlled by both the inner Cauchy-ness and the outer Cauchy-ness. This pattern — choose $n(m)$ growing fast enough — appears across analysis: in the proof that complete + totally bounded ⇒ compact (see [[Ex - Compactness via complete and totally bounded]]); in the proof that $L^p$ is complete; in the construction of weak limits in Banach spaces; in the convergence of approximate identities; in the existence of solutions to ODEs via Picard iteration. Whenever you have a "sequence of approximations to a limit, each of which is itself a sequence", diagonalization is the move.

**Universal property characterizes the completion uniquely up to isometry.** Beyond the construction, the completion satisfies a universal property: every uniformly continuous map $f : X \to Y$ to a complete metric space extends uniquely to a uniformly continuous map $\widehat f : \widehat X \to Y$. This characterizes $\widehat X$ up to canonical isometry. Universal properties are the way mathematicians actually use completions — not by Cauchy-class representatives, but by extending continuous maps. The completion is "the right" completion because of this universal property, and the Cauchy-class construction is one model of it. The same pattern recurs throughout the topic — products are universal among spaces with projections to each factor, Stone–Čech is universal among compactifications, one-point compactification is universal among $X \hookrightarrow $ compact spaces with $|X^c| = 1$. Recognizing the universal property is recognizing the *right* abstract object, and the construction is just one of many ways to build a witness.

**Trigger-reaction: "I have a metric space but Cauchy sequences fail to converge" ⇒ "pass to the completion".** This is the second most-used trick in metric space analysis (after "use that the space is compact"). The completion turns a "Cauchy doesn't converge" obstruction into a converging-limit fact in a larger space, and then if the desired property is invariant under the embedding, you have proved it. Concrete examples: every bounded linear operator on a normed space extends uniquely to its completion; the Cauchy completion of polynomial functions on $[0, 1]$ under the sup norm is the space of continuous functions ($C[0,1]$, via Weierstrass approximation); the completion of compactly supported continuous functions under the $L^p$ norm is $L^p$ itself. Recognizing this trigger short-circuits many "existence of limit" arguments.
