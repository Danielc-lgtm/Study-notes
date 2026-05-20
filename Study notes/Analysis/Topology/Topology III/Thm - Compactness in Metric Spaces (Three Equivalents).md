---
type: theorem
subject: topology
prereqs:
  - "Def - Metric Space"
  - "Def - Compact Space"
  - "Def - Sequentially Compact Space"
  - "Def - Cauchy Sequence and Complete Metric Space"
  - "Def - Totally Bounded Metric Space"
  - "Thm - Heine–Borel Theorem"
tags: [analysis, topology]
---

# Notation

$(X, d)$ is a metric space. **Compact** in the open-cover sense (every open cover has a finite subcover). **Sequentially compact** if every sequence has a convergent subsequence. **Complete**: every Cauchy sequence converges. **Totally bounded**: for every $\varepsilon > 0$, finitely many $\varepsilon$-balls cover $X$. The full registry is on [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact]].

---

# Statement

> **Compactness in Metric Spaces — Three Equivalents.** Let $(X, d)$ be a metric space. The following are equivalent:
>
> 1. $X$ is **compact** (every open cover has a finite subcover);
> 2. $X$ is **sequentially compact** (every sequence has a convergent subsequence);
> 3. $X$ is **complete and totally bounded**.
>
> Also known as the **Heine–Borel–Bolzano–Weierstrass theorem** in this generality.

---

# Motivation

Metric spaces are the setting where most of analysis happens, and compactness is the central tool. The theorem says that in a metric space, three apparently different conditions are equivalent, and one can freely interconvert between them. Each formulation is the right one in a different context:

- **Compactness** (open covers) is the universal topological definition; it is what is preserved under continuous maps and what gives Tychonoff-style theorems for products.
- **Sequential compactness** (convergent subsequences) is what analysts actually reach for: given a sequence of approximations, extract a convergent subsequence, take the limit, identify it as a solution. This is the form used in Bolzano–Weierstrass, the proof of attainment of extrema, the existence of fixed points, etc.
- **Complete + totally bounded** is the geometric / quantitative form: it decomposes compactness into a *topological* condition (every Cauchy converges) and a *geometric* condition (finite $\varepsilon$-nets at every scale). This is the form used to verify compactness in concrete examples — function spaces with Arzelà–Ascoli, Hilbert cubes, $L^p$-bounded equicontinuous families.

The equivalence is what makes compactness in metric spaces *tractable*: you can prove compactness by showing complete + totally bounded (often computational), use it via sequential compactness (often clean for analysis), and benefit from its open-cover form (often used in topology). The three views give complementary access to the same phenomenon.

The hardest direction is (3) ⇒ (1) or (3) ⇒ (2), depending on the proof strategy. The standard route is (3) ⇒ (2) via a diagonal extraction argument: given a sequence in $X$, use total boundedness to find $1$-balls containing infinitely many terms, then $1/2$-balls within those, then $1/4$-balls — diagonalize to extract a Cauchy subsequence, then complete to get convergence.

The theorem is special to metric spaces. In general topological spaces, compactness and sequential compactness are independent (neither implies the other): the long line is sequentially compact but not compact; an uncountable product of $[0, 1]$ with the product topology is compact but not sequentially compact. Metric (or even first-countable) structure is what makes the two coincide.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "metric space + (compact OR sequentially compact OR complete and totally bounded)". The skill is recognizing which form is most useful in a given problem.

The first source is **a bounded subset of a finite-dimensional Euclidean space**. Property $B$: a bounded subset of $\mathbb{R}^n$. The bridge: closed bounded subsets of $\mathbb{R}^n$ are compact by Heine–Borel; in particular sequentially compact, complete, totally bounded. *Example:* the Bolzano–Weierstrass theorem says every bounded sequence in $\mathbb{R}^n$ has a convergent subsequence, which is exactly the sequential compactness of closed balls.

The second source is **a family of functions that is equicontinuous and pointwise bounded**. Property $B$: a subset $F \subseteq C(K)$ (continuous real-valued functions on a compact metric $K$) that is equicontinuous and pointwise bounded. The bridge: by **Arzelà–Ascoli**, $F$ is totally bounded in the sup-norm metric; combined with completeness of $C(K)$ this gives compactness of $\overline F$. *Example:* a sequence of solutions to an ODE with a Lipschitz right-hand side is equicontinuous (by Gronwall) and pointwise bounded, hence has a convergent subsequence by sequential compactness.

The third source is **a precompact subset of a complete metric space**. Property $B$: a subset $A$ whose closure is compact. The bridge: $\bar A$ is compact iff it is complete (which it is, being closed in the complete space $X$) and totally bounded. So total boundedness of $A$ (equivalently of $\bar A$) is the key check. *Example:* in **probability theory**, Prokhorov's theorem identifies precompact families of probability measures with tight families, where tightness is a form of total boundedness.

**Targets (Output Amplification)**

The conclusion is "$X$ is compact (in the equivalent forms)".

Combine the conclusion with **a continuous real-valued function**. Property $D$: a continuous $f : X \to \mathbb{R}$. The amplified result $E$: $f$ is bounded, attains its maximum and minimum, and is uniformly continuous (in the metric form). The combination gives **the extreme value theorem** and **uniform continuity on compacts**, two of the most-used results in analysis.

Combine the conclusion with **a sequence of subspaces**. Property $D$: a nested sequence of closed nonempty subsets $F_1 \supseteq F_2 \supseteq \cdots$. The amplified result $E$: $\bigcap_n F_n \neq \emptyset$ (compact + finite intersection property). The combination is the **finite intersection property** form of compactness, useful in proving existence of fixed points and intersection points of nested closed sets.

Combine the conclusion with **a continuous map to another metric space**. Property $D$: $f : X \to Y$ continuous with $Y$ metric. The amplified result $E$: $f$ is uniformly continuous (since $X$ is compact metric, the modulus of continuity can be chosen uniformly). The combination — compact metric + continuous to metric — gives **uniform continuity**, a much stronger condition than pointwise continuity.

---

# Why Is It True

The intuition behind each direction:

**(1) ⇒ (2): compactness ⇒ sequential compactness.** Take a sequence $\{x_n\}$. We must find a convergent subsequence. The idea: if no subsequence converges, then no point $x$ is the limit of a subsequence. By compactness one can produce a finite cover by neighborhoods, each containing only finitely many $x_n$ (since none is a cluster point of the sequence), which is impossible because the cover must contain infinitely many sequence terms. So some point is a cluster point, and (in metric spaces, where first countability holds) a cluster point of a sequence is the limit of a subsequence.

**(2) ⇒ (3): sequential compactness ⇒ complete + totally bounded.** Completeness is direct: a Cauchy sequence has a convergent subsequence (sequential compactness), and a Cauchy sequence with a convergent subsequence converges (triangle inequality). For total boundedness: suppose not. Then for some $\varepsilon > 0$, no finite $\varepsilon$-cover exists. Construct a sequence $x_1, x_2, \dots$ with $d(x_i, x_j) > \varepsilon$ for $i \neq j$ — keep picking points outside the union of previous $\varepsilon$-balls (possible because no finite cover exists). This sequence has no Cauchy subsequence (any two distinct terms are at distance $> \varepsilon$), hence no convergent subsequence, contradicting sequential compactness.

**(3) ⇒ (2): complete + totally bounded ⇒ sequential compactness.** This is the hardest direction. Given a sequence $\{x_n\}$, use total boundedness to find finitely many $1$-balls covering $X$; some ball contains infinitely many $x_n$. Take a subsequence in that ball. Repeat with $1/2$-balls inside the first ball, then $1/4$-balls, etc. The diagonal subsequence is Cauchy (within distance $1/k$ of itself eventually for every $k$). By completeness, it converges. So the original sequence has a convergent subsequence.

**(2) ⇒ (1) or (3) ⇒ (1): sequential / complete-totally-bounded ⇒ compact.** This direction uses the **Lebesgue number lemma** in spirit. Given a sequence of nested cover refinements, the diagonal argument plus completeness produces a contradiction if no finite subcover existed. The detailed argument: from sequential compactness, derive that the space is second countable (a countable dense subset exists via total boundedness, and balls around dense points form a countable basis), so every open cover has a countable subcover; then use sequential compactness to extract a finite subcover.

The whole picture: **completeness controls limits**; **total boundedness controls finite resolution**; **together they give compactness**. The diagonal argument is the technique that combines them. In one direction or the other, the same combinatorial machinery is run.

---

# What Makes This Hard

The genuinely hard direction is (3) ⇒ (2) — extracting a convergent subsequence from a sequence in a complete totally bounded space. The non-obvious step is the **diagonal extraction**: rather than extracting one subsequence at a time and hoping to converge, one extracts *nested* subsequences at each scale $\varepsilon_k = 1/k$ and then *diagonalizes* to combine them into a single Cauchy subsequence. The most common error is to try to extract directly without iterating the total-boundedness argument — at scale $1$ you get a subsequence in a $1$-ball, but you have no control on scales smaller than $1$; you must iterate. A second common slip is forgetting to invoke completeness — total boundedness gives a Cauchy subsequence, but Cauchy implies convergent only in complete spaces.

---

# Rederivation Scaffold

**High-level strategy:**
Prove the three equivalences in a cycle: (1) ⇒ (2), (2) ⇒ (3), (3) ⇒ (1). The hardest step is the diagonal argument for (3) ⇒ (2) (or (3) ⇒ (1) via sequence extraction), and the other steps are direct.

**Subgoal decomposition:**

1. **(1) ⇒ (2): cluster points give convergent subsequences.** Show every sequence has a convergent subsequence using compactness.
   - *Hint:* If no point is a cluster point, each $x \in X$ has a neighborhood meeting finitely many sequence terms; cover by such neighborhoods and use compactness.
   - *Why needed:* Compactness gives sequential compactness in metric (first countable) spaces.

2. **(2) ⇒ completeness.** Show every Cauchy sequence converges using sequential compactness.
   - *Hint:* Cauchy sequence has a convergent subsequence (by SC), and Cauchy + convergent subsequence implies convergent.
   - *Why needed:* Half of "complete + totally bounded".

3. **(2) ⇒ totally bounded.** Show $X$ is totally bounded using sequential compactness.
   - *Hint:* Contrapositive: if not totally bounded, there is $\varepsilon$ and a sequence with pairwise distance $> \varepsilon$, which has no Cauchy (hence no convergent) subsequence.
   - *Why needed:* Other half of "complete + totally bounded".

4. **(3) ⇒ (2): diagonal extraction.** Given a sequence in complete + totally bounded $X$, extract a Cauchy subsequence by nested $\varepsilon$-ball arguments and then converge by completeness.
   - *Hint:* For each $k$, partition $X$ into finitely many balls of radius $1/k$; one contains infinitely many sequence terms; iterate; diagonalize.
   - *Why needed:* The hardest direction.

5. **(2) ⇒ (1): sequential compactness gives compactness.** Use SC to extract a finite subcover from an open cover.
   - *Hint:* Show $X$ is second countable (using total boundedness, which is implied by SC); pass to a countable subcover; use SC to extract a finite subcover via the Lebesgue number lemma in spirit.
   - *Why needed:* Closes the cycle.

---

# Lemma Decomposition

> [!note]- Lemma 1: A Cauchy sequence with a convergent subsequence converges
> **Statement:** Let $\{x_n\}$ be a Cauchy sequence in a metric space, and suppose a subsequence $x_{n_k} \to x$. Then $x_n \to x$.
>
> **Hint:** Use triangle inequality with the Cauchy bound and the subsequence's convergence.
>
> **Why needed:** Used in (2) ⇒ completeness and (3) ⇒ (2) (Cauchy + complete = convergent).
>
> > [!note]- Full proof
> > Let $\varepsilon > 0$. By Cauchy, find $N$ with $d(x_n, x_m) < \varepsilon/2$ for $n, m \geq N$. By $x_{n_k} \to x$, find $K$ with $d(x_{n_k}, x) < \varepsilon/2$ and $n_K \geq N$. Then for $n \geq N$, $d(x_n, x) \leq d(x_n, x_{n_K}) + d(x_{n_K}, x) < \varepsilon$. So $x_n \to x$.

> [!note]- Lemma 2: Diagonal extraction from nested infinite-pigeon $\varepsilon$-balls
> **Statement:** Let $\{x_n\}$ be a sequence in a totally bounded metric space. For each $k \geq 1$, there exists a subsequence of $\{x_n\}$ contained in some ball of radius $1/k$ in $X$. Iteratively passing to subsequences and diagonalizing produces a Cauchy subsequence.
>
> **Hint:** At each step, the previous subsequence has infinitely many terms in some ball of the new finer cover.
>
> **Why needed:** The key step in (3) ⇒ (2).
>
> > [!note]- Full proof
> > Total boundedness gives a finite cover of $X$ by balls $B_1$ of radius $1$. By the pigeonhole principle, some $B_1$ contains $x_n$ for infinitely many $n$; let $\{x_n^{(1)}\}$ be the corresponding subsequence.
> >
> > Now $X$ (in particular $B_1$) admits a finite cover by balls of radius $1/2$; some ball $B_2$ contains $\{x_n^{(1)}\}$ for infinitely many $n$; let $\{x_n^{(2)}\}$ be that sub-subsequence, contained in $B_1 \cap B_2$.
> >
> > Continuing, at step $k$ we have a subsequence $\{x_n^{(k)}\}$ contained in $B_1 \cap \cdots \cap B_k$, where each $B_i$ has radius $1/i$. By the diagonal procedure, take $y_k = x_k^{(k)}$. For $j, k \geq K$, both $y_j, y_k \in B_1 \cap \cdots \cap B_K$, in particular in $B_K$ of radius $1/K$, so $d(y_j, y_k) < 2/K$. Hence $\{y_k\}$ is Cauchy.

---

# Formal Proof

> [!note]- Complete formal proof
> We prove the equivalences in the cycle (1) ⇒ (2) ⇒ (3) ⇒ (1).
>
> **(1) ⇒ (2): compactness ⇒ sequential compactness.**
> Let $\{x_n\}$ be a sequence in compact $X$. Suppose no subsequence converges; then no $x \in X$ is a limit of a subsequence. This means for each $x$ there is an open neighborhood $U_x$ containing $x_n$ for only finitely many $n$ (else $x$ would be a cluster point, and in a metric space — being first countable — a cluster point of a sequence is the limit of a subsequence). The collection $\{U_x : x \in X\}$ is an open cover; by compactness, finitely many $U_{x_1}, \dots, U_{x_k}$ cover $X$. But each $U_{x_i}$ contains only finitely many sequence terms, so $X = U_{x_1} \cup \cdots \cup U_{x_k}$ contains only finitely many sequence terms — contradicting the infinitude of $\{x_n\}$.
>
> **(2) ⇒ (3): sequential compactness ⇒ complete + totally bounded.**
>
> *Completeness:* Let $\{x_n\}$ be a Cauchy sequence. By (2), there is a convergent subsequence $x_{n_k} \to x$. By Lemma 1, $x_n \to x$, so $X$ is complete.
>
> *Total boundedness:* Suppose $X$ is not totally bounded. Then there is $\varepsilon > 0$ such that no finite $\varepsilon$-cover exists. Inductively choose $x_n$: $x_1$ arbitrary; given $x_1, \dots, x_n$, the union $B_\varepsilon(x_1) \cup \cdots \cup B_\varepsilon(x_n)$ does not cover $X$ (else a finite $\varepsilon$-cover), so pick $x_{n+1} \in X \setminus (B_\varepsilon(x_1) \cup \cdots \cup B_\varepsilon(x_n))$. Then $d(x_i, x_j) \geq \varepsilon$ for $i \neq j$. This sequence has no Cauchy subsequence (any two distinct terms are at distance $\geq \varepsilon$), hence no convergent subsequence, contradicting (2). So $X$ is totally bounded.
>
> **(3) ⇒ (2): complete + totally bounded ⇒ sequential compactness.**
>
> Let $\{x_n\}$ be a sequence in $X$. By Lemma 2 (diagonal extraction from total boundedness), there is a Cauchy subsequence $\{y_k\}$. By completeness, $\{y_k\}$ converges. Hence $\{x_n\}$ has a convergent subsequence, so (2) holds.
>
> **(2) ⇒ (1): sequential compactness ⇒ compactness.**
>
> Let $\{U_\alpha\}$ be an open cover of $X$. We will show it has a finite subcover.
>
> *Step 1: $X$ is separable.* By total boundedness (proved in (2) ⇒ (3)), for each $n$ choose a finite $1/n$-net $F_n$; the union $F = \bigcup_n F_n$ is countable and dense. So $X$ has a countable dense set.
>
> *Step 2: $X$ has a countable basis.* For each $x \in F$ and $n \in \mathbb{N}$, take $B_{1/n}(x)$; this gives a countable basis (every open set containing a point $y$ contains some $B_{1/n}(x)$ with $x \in F, n$ large enough that $B_{1/n}(x) \subseteq$ the open set).
>
> *Step 3: Pass to a countable subcover.* The open cover $\{U_\alpha\}$ has a countable subcover $\{U_n\}$ (each basis element is in some $U_\alpha$, and we take one per basis element used).
>
> *Step 4: Extract a finite subcover via SC.* Suppose for contradiction $\{U_n\}$ has no finite subcover. Then the closed sets $C_n = X \setminus (U_1 \cup \cdots \cup U_n)$ are nonempty. Pick $y_n \in C_n$. By (2), $\{y_n\}$ has a convergent subsequence $y_{n_k} \to y$. Then $y$ is in some $U_{n_0}$ (since the $U_n$ cover); but $y_{n_k} \in C_{n_k}$ for $n_k \geq n_0$ means $y_{n_k} \notin U_{n_0}$, so by closedness of $C_{n_0}$, $y \in C_{n_0}$, i.e., $y \notin U_{n_0}$ — contradiction. So a finite subcover exists. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Arzelà–Ascoli theorem.** A subset $F \subseteq C(K)$ for $K$ compact metric is relatively compact in the sup-norm if and only if it is **equicontinuous** and **pointwise bounded**. *Proof sketch:* Equicontinuity plus pointwise boundedness gives total boundedness in sup-norm (by a finite $\varepsilon$-net in $K$ combined with a finite $\varepsilon$-net in $\mathbb{R}$ for the values); $C(K)$ is complete (uniform limit of continuous is continuous); hence $\overline F$ is complete totally bounded = compact = sequentially compact. The application is the standard route to compactness in function spaces.

**Brouwer fixed-point theorem.** The closed unit ball $\overline{B} \subseteq \mathbb{R}^n$ is compact (Heine–Borel), and any continuous $f : \overline{B} \to \overline{B}$ has a fixed point. The proof (one of several) uses compactness essentially: one approximates $f$ by simplicial maps, the simplicial complex is compact, fixed points of approximations have a convergent subsequence (sequential compactness), and the limit is a fixed point of $f$. Compactness of the domain is the crucial input.

**Existence of best approximations.** Let $C \subseteq X$ be a nonempty closed subset of a complete metric space and $x \in X$. Does there exist $y \in C$ minimizing $d(x, y)$? If $C$ is *compact*, yes: $d(x, \cdot)$ is continuous, hence attains its minimum. In Banach space approximation theory, one wants to know whether the unit ball of a subspace has "best approximators"; the answer involves compactness (or weak compactness, via Banach–Alaoglu) of the subspace's unit ball.

---

# Bridges

- **[[Thm - Heine–Borel Theorem]]** — the special case for $\mathbb{R}^n$: closed bounded is compact. This is the prototype; the present theorem generalizes it to all metric spaces with the extra "complete + totally bounded" formulation.

- **[[Def - Cauchy Sequence and Complete Metric Space]]** — the completeness component of (3).

- **[[Def - Totally Bounded Metric Space]]** — the total boundedness component of (3).

- **[[Thm - Lebesgue Number Lemma]]** — a sibling theorem for compact metric spaces; the techniques (sequential compactness extracting a $\delta$-witness) are similar.

- **[[Thm - Continuity via Nets]]** — in metric spaces, sequences suffice for net characterizations (first countability), which is why compactness equals sequential compactness here.

---

# Unlocked by This

> [!tip] Bolzano–Weierstrass Theorem *(from Real Analysis)*
> Every bounded sequence in $\mathbb{R}^n$ has a convergent subsequence. This is the sequential compactness of closed bounded subsets of $\mathbb{R}^n$.

> [!tip] Arzelà–Ascoli Theorem *(from Functional Analysis)*
> The compact subsets of $C(K)$ for $K$ compact metric are characterized as the **equicontinuous, pointwise-bounded** ones. The criterion combines total boundedness (which is what equicontinuity gives) with completeness of $C(K)$.

> [!tip] Uniform Continuity on Compacts *(from Real Analysis)*
> Every continuous function from a compact metric space to a metric space is uniformly continuous. Proved by using sequential compactness on a sequence violating uniform continuity.

> [!tip] Prokhorov's Theorem *(from Probability)*
> A family of probability measures on a complete separable metric space is relatively compact in the weak topology iff it is **tight**. Tightness is the measure-theoretic analog of total boundedness.
