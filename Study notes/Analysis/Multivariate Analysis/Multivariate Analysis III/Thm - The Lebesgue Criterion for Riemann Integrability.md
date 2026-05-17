---
type: theorem
subject: multivariate-analysis
prereqs:
  - "Def - The Riemann Integral in Several Variables"
  - "Def - Jordan Measure"
tags: [analysis, multivariate-analysis]
---

# Notation

$R \subseteq \mathbb{R}^n$ is a [[Def - The Riemann Integral in Several Variables|cell]]; $f : R \to \mathbb{R}$ is bounded. The **set of discontinuities** of $f$ is $\operatorname{Disc}(f) = \{x \in R : f \text{ is not continuous at } x\}$. A set $\Sigma$ has **content zero** (is a **nil set**) if $\operatorname{cont}^+(\Sigma) = 0$ — coverable by *finitely many* cells of arbitrarily small total volume. A set $S$ has **Lebesgue outer measure zero**, written $m^*(S) = 0$, if it is coverable by *countably many* cells of arbitrarily small total volume:
$$m^*(S) = \inf\Big\{ \sum_{k \geq 1} V(R_k) : S \subseteq \bigcup_{k \geq 1} R_k \Big\} = 0.$$
Content zero implies outer measure zero, never the reverse. The full symbol registry is on [[Multivariate Analysis III — Integration in Several Variables]].

---

# Statement

> **The Lebesgue Criterion for Riemann Integrability.** Let $R \subseteq \mathbb{R}^n$ be a cell and $f : R \to \mathbb{R}$ a bounded function, with discontinuity set $\operatorname{Disc}(f)$. Then
> $$f \text{ is Riemann integrable on } R \quad \Longleftrightarrow \quad m^*\big(\operatorname{Disc}(f)\big) = 0,$$
> that is, $f \in \mathcal{R}(R)$ if and only if the set of points where $f$ is discontinuous has Lebesgue outer measure zero — can be covered by countably many cells of arbitrarily small total volume.
>
> In particular, a bounded function whose discontinuity set has *content* zero, or is countable, or is a finite union of graphs of continuous functions, is Riemann integrable; and applied to an indicator $f = \chi_S$, whose discontinuity set is $\partial S$, the criterion states that $S$ is [[Def - Jordan Measure|Jordan measurable]] if and only if $m^*(\partial S) = 0$.

---

# Motivation

The definition of [[Def - The Riemann Integral in Several Variables|Riemann integrability]] — upper integral equals lower integral — is unusable as a test. It quantifies over all partitions of the cell, of which there are uncountably many, and there is no procedure that inspects them. To *decide* whether a given function is integrable you need a criterion phrased in terms of the function itself, not in terms of partitions.

There is an obvious candidate: continuity. A continuous function on a compact cell is integrable, because uniform continuity makes the Darboux gap close. But continuity is far too strong as a *characterization* — the indicator of a disk is discontinuous all along a circle and is plainly integrable, the volume of the disk being a number we can compute. So integrability tolerates *some* discontinuity. The question this theorem answers is the exact one: **how much discontinuity, and of what kind, can a Riemann integrable function have?**

The first guess is "the discontinuity set has content zero", and this is sufficient — it is the working criterion. But it is not sharp. A function can be discontinuous on a set that is *not* nil and still be integrable, because content zero, built from finite covers, is itself a flawed notion of smallness (it is exactly the flaw that makes Jordan measure fail countable additivity). The correct, sharp answer has to be stated with *countable* covers — in the language of [[Def - Lebesgue Measure|Lebesgue]] outer measure. The theorem says: a bounded function is Riemann integrable if and only if its discontinuity set has *Lebesgue outer measure zero*.

This is a remarkable statement, and its value is twofold. Practically, it converts an infinite verification into a finite geometric one: find where $f$ jumps, and check that set is small. Conceptually, it is the bridge between two theories — it diagnoses Riemann integrability in the language of Lebesgue measure, decades before the Riemann integral knew it needed that language. It is the precise reason measure theory is the right setting for integration: even the *Riemann* integral is secretly governed by the measure of a set.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition for *concluding integrability* is "$\operatorname{Disc}(f)$ has Lebesgue outer measure zero". The skill is recognizing that a given discontinuity set is null.

The first disguised source is **$f$ is continuous except on a finite union of continuous graphs**. The property $B$ is "$\operatorname{Disc}(f) \subseteq G_1 \cup \cdots \cup G_m$, each $G_j$ the graph of a continuous function over a closed bounded base". The bridge: the graph of a continuous function over a closed bounded base has *content zero* (Taylor's Proposition 3.1.7 — partition the base finely, the graph lies in a thin slab), and a finite union of content-zero sets has content zero, hence outer measure zero. The non-obvious part is that an $(n-1)$-dimensional surface, which "looks substantial", is measure-theoretically invisible in $\mathbb{R}^n$. *Example problem:* show the indicator of any region bounded by finitely many smooth surfaces is integrable.

The second disguised source is **$\operatorname{Disc}(f)$ is countable**. The property $B$ is "$f$ is discontinuous at only countably many points". The bridge: a countable set has Lebesgue outer measure zero — enumerate the points $x_1, x_2, \dots$ and cover $x_k$ by a cell of volume $\varepsilon 2^{-k}$, total volume $\varepsilon$. The non-obviousness: this is exactly where content zero and outer measure zero *diverge* — a countable dense set is not nil, but it is null, so this source is genuinely stronger than the content-zero criterion. *Example problem:* a bounded function on $[0,1]$ discontinuous exactly at the rationals — integrable (the rationals are countable).

The third disguised source is **$f$ is the image of an integrable function under a continuous map**, or **$f$ is a uniform limit of integrable functions**. The property $B$ is "$f = \psi \circ g$ with $g$ integrable and $\psi$ continuous", or "$f_\nu \to f$ uniformly with $f_\nu$ integrable". The bridge: a continuous $\psi$ does not create new discontinuities ($\operatorname{Disc}(\psi \circ g) \subseteq \operatorname{Disc}(g)$), and a uniform limit preserves integrability directly. The non-obviousness is that integrability is stable under operations that *a priori* could wreck the discontinuity set. *Example problem:* if $f$ is integrable then so is $|f|$, $f^2$, $\max(f,0)$.

**Targets (Output Amplification)**

The conclusion is "$f \in \mathcal{R}(R)$", and the criterion is an *equivalence*, so it also gives non-integrability.

Combine the criterion with **the indicator of a region**. Applied to $f = \chi_S$, the discontinuity set of $\chi_S$ is exactly $\partial S$. The further result $E$: **$S$ is [[Def - Jordan Measure|Jordan measurable]] if and only if $\partial S$ has outer measure zero** — Jordan measurability is a measure-theoretic condition on the boundary. This is non-obvious because Jordan measurability was defined through finite covers, yet the sharp criterion for it is the countable-cover (Lebesgue) condition on the boundary.

Combine the criterion with **the algebra of integrable functions**. Since $\operatorname{Disc}(f + g) \subseteq \operatorname{Disc}(f) \cup \operatorname{Disc}(g)$ and a finite (indeed countable) union of null sets is null, the criterion instantly yields $E$: **the integrable functions form an algebra** — closed under sums, products, max, min, absolute value. This is non-obvious from the upper-equals-lower definition (proving $fg$ integrable directly is fiddly), but immediate once integrability is recognized as a smallness condition on the discontinuity set, which only ever shrinks or stays put under these operations.

Combine the criterion with **a sequence of integrable functions**. If $f_k \to f$ pointwise and each $f_k$ is integrable, the criterion does *not* directly give integrability of $f$ — the discontinuity set of a pointwise limit can blow up (the Dirichlet function is a pointwise limit of integrable functions). The further result $E$ is a *negative* one: it pinpoints exactly why the Riemann integral cannot interchange limits with integration, and thereby why the Lebesgue theory and its [[Measure Theory II — §2 Integration|convergence theorems]] are needed. Recognizing what the criterion *cannot* deliver is as useful as what it can.

---

# Why Is It True

The criterion is believable once you see what the Darboux gap $\overline{I}_P(f) - \underline{I}_P(f) = \sum_\alpha (\sup_{R_\alpha} f - \inf_{R_\alpha} f) V(R_\alpha)$ is actually measuring. The quantity $\sup_{R_\alpha} f - \inf_{R_\alpha} f$ is the **oscillation** of $f$ on the subcell $R_\alpha$ — how much $f$ wobbles there. Integrability means this total weighted oscillation can be driven to zero.

Now ask: where can the oscillation *fail* to be small? Exactly at points where $f$ is discontinuous. At a point of continuity, $f$ barely changes in a small neighborhood, so any subcell around it contributes little oscillation. At a point of discontinuity, $f$ has a fixed gap $\geq \delta$ no matter how small the subcell. So the total oscillation is small precisely when the subcells where $f$ wobbles — the ones meeting $\operatorname{Disc}(f)$ — have *small total volume*. That is the heart of it: **integrability is the demand that the discontinuity set can be covered by subcells of small total volume.**

This already explains the *sufficient* direction with content zero. If $\operatorname{Disc}(f)$ is nil, cover it by finitely many cells of tiny total volume — those cells contribute at most (tiny volume)$\times$(total range of $f$) to the gap — and on the *remaining* cells $f$ is continuous, so by compactness a fine partition makes the oscillation there small too. The two contributions are each small; the gap closes.

Why does the sharp statement need *outer* measure — countable covers — rather than content? Because the discontinuity set must be split into pieces by *severity*. Let $D_\delta$ be the set of points where $f$ oscillates by at least $\delta$. Each $D_\delta$ turns out to be *closed*, hence compact, and for a compact set a countable cover can always be reduced to a finite subcover — so for the compact pieces $D_\delta$, "outer measure zero" and "content zero" coincide. The full discontinuity set is the countable union $\operatorname{Disc}(f) = \bigcup_k D_{1/k}$. If $\operatorname{Disc}(f)$ has outer measure zero, each $D_{1/k}$ does too, hence each $D_{1/k}$ (being compact) has content zero, and on each you run the content-zero argument. The countable union is handled because outer measure, unlike content, *is* countably subadditive — a countable union of null sets is null. This is the exact place the Lebesgue notion is forced: the discontinuity set is naturally a countable union, and only a countably-subadditive notion of smallness survives the union.

The *necessary* direction runs in reverse. If $\operatorname{Disc}(f)$ has positive outer measure, then some severity-level set $D_\delta$ has positive outer measure (a countable union of null sets would be null). But $D_\delta$ is a set where $f$ genuinely oscillates by $\geq \delta$, and any partition has subcells covering $D_\delta$ with total volume bounded below by a positive number — so the gap is bounded below by (positive volume)$\times \delta > 0$, and $f$ is not integrable. The discontinuity, if it lives on a non-negligible set, leaves a permanent positive residue in the Darboux gap.

So one should *expect* the criterion: the Darboux gap is total oscillation, oscillation concentrates on the discontinuity set, and the gap closes exactly when that set is too small — in the countably-additive sense — to carry positive weighted oscillation.

---

# What Makes This Hard

The non-obvious step is the **decomposition of the discontinuity set by oscillation severity**, $\operatorname{Disc}(f) = \bigcup_k D_{1/k}$ with $D_\delta = \{x : \operatorname{osc}_f(x) \geq \delta\}$ closed and hence compact: this is what allows the countable-cover (outer measure) hypothesis to be converted, level by level, into the finite-cover (content) estimates that the Darboux machinery actually uses. The most common error is to attempt the proof with content zero throughout and to be unable to handle a discontinuity set that is countable but dense — content zero simply does not survive the countable union, and one must see that compactness of each $D_\delta$ is the bridge. A second frequent slip is forgetting that $D_\delta$ is *closed*: without that, the finite subcover step has no justification.

---

# Rederivation Scaffold

**High-level strategy:**
Translate the Darboux gap into total oscillation. Stratify the discontinuity set into the closed sets $D_\delta$ where the oscillation is at least $\delta$. For sufficiency, cover each compact $D_\delta$ by finitely many small cells and use compactness on the complement; for necessity, show a non-null $D_\delta$ forces a permanent positive gap.

**Subgoal decomposition:**

1. **Define oscillation and prove $D_\delta$ is closed.** Set $\operatorname{osc}_f(x) = \lim_{r \to 0} (\sup_{B(x,r)} f - \inf_{B(x,r)} f)$, and $D_\delta = \{x : \operatorname{osc}_f(x) \geq \delta\}$.
   - *Hint:* $f$ is continuous at $x$ iff $\operatorname{osc}_f(x) = 0$, so $\operatorname{Disc}(f) = \bigcup_{k} D_{1/k}$. Show the complement of $D_\delta$ is open.
   - *Why needed:* Closedness makes each $D_\delta$ compact (it is bounded, inside $R$), which is what lets a countable cover be thinned to a finite one.

2. **Sufficiency.** Assume $m^*(\operatorname{Disc}(f)) = 0$. Fix $\delta > 0$; then $D_\delta$ has outer measure zero, hence — being compact — content zero.
   - *Hint:* Cover $D_\delta$ by finitely many open cells of total volume $< \varepsilon$. Off the union of those cells, $f$ oscillates by $< \delta$; refine to a partition. The gap splits into a "bad cells" part $\leq \varepsilon \cdot 2\sup|f|$ and a "good cells" part $\leq \delta \cdot V(R)$.
   - *Why needed:* Both pieces are small, so $\overline{I}_P(f) - \underline{I}_P(f)$ is small, giving $f \in \mathcal{R}(R)$.

3. **Necessity.** Assume $f \in \mathcal{R}(R)$. Show $D_\delta$ has content zero for every $\delta$.
   - *Hint:* In any partition, the subcells whose interior meets $D_\delta$ each contribute oscillation $\geq \delta$; their total volume times $\delta$ is at most the Darboux gap, which is $< \varepsilon$ for a fine partition.
   - *Why needed:* Each $D_\delta$ is then null; $\operatorname{Disc}(f) = \bigcup_k D_{1/k}$ is a countable union of null sets, hence null.

---

# Lemma Decomposition

> [!note]- Lemma 1: The oscillation function and the structure of the discontinuity set
> **Statement:** For bounded $f : R \to \mathbb{R}$ define $\operatorname{osc}_f(x) = \inf_{r > 0}\big(\sup_{B(x,r) \cap R} f - \inf_{B(x,r) \cap R} f\big)$. Then $f$ is continuous at $x$ if and only if $\operatorname{osc}_f(x) = 0$, the set $D_\delta = \{x : \operatorname{osc}_f(x) \geq \delta\}$ is closed for each $\delta > 0$, and $\operatorname{Disc}(f) = \bigcup_{k \geq 1} D_{1/k}$.
>
> **Hint:** Continuity at $x$ means the oscillation on small balls tends to $0$. For closedness, show $\{ \operatorname{osc}_f < \delta\}$ is open: if $\operatorname{osc}_f(x) < \delta$, some ball $B(x,r)$ already has oscillation $< \delta$, and every point of that ball inherits oscillation $< \delta$.
>
> **Why needed:** It turns the vague "discontinuity set" into a countable union of *closed* sets, the structure on which the whole proof runs.
>
> > [!note]- Full proof
> > If $f$ is continuous at $x$, then for every $\varepsilon > 0$ there is $r$ with $|f(y) - f(x)| < \varepsilon/2$ for $y \in B(x,r) \cap R$, so $\sup - \inf$ over that ball is $\leq \varepsilon$; thus $\operatorname{osc}_f(x) = 0$. Conversely if $\operatorname{osc}_f(x) = 0$, then for every $\varepsilon$ some ball has $\sup - \inf < \varepsilon$, which forces $|f(y) - f(x)| < \varepsilon$ there — continuity. Hence $\operatorname{Disc}(f) = \{\operatorname{osc}_f > 0\} = \bigcup_{k \geq 1}\{\operatorname{osc}_f \geq 1/k\}$.
> >
> > For closedness of $D_\delta$, take $x$ with $\operatorname{osc}_f(x) < \delta$. By definition of the infimum there is $r > 0$ with $\sup_{B(x,r) \cap R} f - \inf_{B(x,r) \cap R} f < \delta$. For any $y \in B(x, r/2)$, the ball $B(y, r/2) \subseteq B(x,r)$, so $\operatorname{osc}_f(y) \leq \sup_{B(x,r)} f - \inf_{B(x,r)} f < \delta$. Thus $B(x,r/2)$ lies in the complement of $D_\delta$, so the complement is open and $D_\delta$ is closed. Being a closed subset of the bounded cell $R$, each $D_\delta$ is compact.
>
> [!note]- Lemma 2: A compact set of outer measure zero has content zero
> **Statement:** If $K \subseteq \mathbb{R}^n$ is compact and $m^*(K) = 0$, then $\operatorname{cont}^+(K) = 0$.
>
> **Hint:** Outer measure zero gives a *countable* cover of small total volume by *open* cells; compactness extracts a finite subcover.
>
> **Why needed:** It is the exact mechanism by which the Lebesgue (countable-cover) hypothesis is fed into the Darboux machinery, which can only digest finite covers.
>
> > [!note]- Full proof
> > Let $\varepsilon > 0$. Since $m^*(K) = 0$, there are countably many cells $R_k$ with $K \subseteq \bigcup_k R_k$ and $\sum_k V(R_k) < \varepsilon/2$. Enlarge each $R_k$ slightly to an open cell $R_k'$ with $R_k \subseteq R_k'$ and $V(R_k') < V(R_k) + \varepsilon 2^{-k-1}$; then $\{R_k'\}$ is an open cover of $K$ with $\sum_k V(R_k') < \varepsilon$. Since $K$ is compact, finitely many $R_{k_1}', \dots, R_{k_m}'$ already cover $K$, and $\sum_{j} V(R_{k_j}') < \varepsilon$. This is a finite cell cover of $K$ of total volume $< \varepsilon$; as $\varepsilon$ was arbitrary, $\operatorname{cont}^+(K) = 0$.
>
> [!note]- Lemma 3: Content zero is finitely additive, outer measure zero is countably additive
> **Statement:** A finite union of content-zero sets has content zero. A countable union of outer-measure-zero sets has outer measure zero.
>
> **Hint:** For the countable case, cover the $j$th set by cells of total volume $< \varepsilon 2^{-j}$ and sum the geometric series.
>
> **Why needed:** The discontinuity set is a *countable* union $\bigcup_k D_{1/k}$; only the countably-additive notion survives it. This lemma is the precise reason outer measure, not content, appears in the theorem.
>
> > [!note]- Full proof
> > *Finite case.* If $\Sigma_1, \dots, \Sigma_m$ each have content zero, cover $\Sigma_j$ by finitely many cells of total volume $< \varepsilon/m$; the union of all these covers is a finite cell cover of $\bigcup_j \Sigma_j$ of total volume $< \varepsilon$.
> >
> > *Countable case.* If $m^*(S_j) = 0$ for each $j \in \mathbb{N}$, cover $S_j$ by countably many cells of total volume $< \varepsilon 2^{-j}$. The union over all $j$ is a countable cell cover of $\bigcup_j S_j$ with total volume $< \sum_j \varepsilon 2^{-j} = \varepsilon$. Hence $m^*(\bigcup_j S_j) = 0$. The countable case *fails* for content zero — the rationals in $[0,1]$ are a countable union of content-zero singletons but have content $1$ — which is exactly why the theorem cannot be stated with content.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $f : R \to \mathbb{R}$ be bounded, say $|f| \leq M$, with discontinuity set $D = \operatorname{Disc}(f)$. By Lemma 1, $D = \bigcup_{k \geq 1} D_{1/k}$ with each $D_\delta = \{\operatorname{osc}_f \geq \delta\}$ closed, hence compact in $R$.
>
> **($\Leftarrow$) Suppose $m^*(D) = 0$; we show $f \in \mathcal{R}(R)$.** Fix $\varepsilon > 0$ and fix $\delta > 0$ to be chosen. Since $D_\delta \subseteq D$, we have $m^*(D_\delta) = 0$, and $D_\delta$ is compact, so by Lemma 2, $\operatorname{cont}^+(D_\delta) = 0$. Cover $D_\delta$ by finitely many *open* cells of total volume $< \varepsilon$; call their union $U$. The set $K = R \setminus U$ is compact, and at every point of $K$ the oscillation of $f$ is $< \delta$ (such points are not in $D_\delta$). By a standard compactness argument (a finite covering by balls on each of which $\sup - \inf < \delta$), there is a partition $P$ of $R$ such that every subcell of $P$ not meeting $U$ has $\sup f - \inf f \leq \delta$, and the subcells meeting $U$ have total volume $< \varepsilon$. Split the partition $P = P' \cup P''$ into subcells contained in $K$-type good region and subcells meeting $U$. Then
> $$\overline{I}_P(f) - \underline{I}_P(f) = \sum_{R_\alpha \in P'} \big(\sup_{R_\alpha} f - \inf_{R_\alpha} f\big) V(R_\alpha) + \sum_{R_\alpha \in P''} \big(\sup_{R_\alpha} f - \inf_{R_\alpha} f\big) V(R_\alpha).$$
> The first sum is $\leq \delta \sum_{R_\alpha \in P'} V(R_\alpha) \leq \delta \, V(R)$. The second is $\leq 2M \sum_{R_\alpha \in P''} V(R_\alpha) \leq 2M\varepsilon$. Hence
> $$\overline{I}_P(f) - \underline{I}_P(f) \leq \delta\, V(R) + 2M\varepsilon.$$
> Choosing $\delta$ with $\delta \, V(R) < \varepsilon$, the gap is $< \varepsilon(1 + 2M)$. As $\varepsilon$ was arbitrary, $\overline{I}(f) = \underline{I}(f)$, so $f \in \mathcal{R}(R)$.
>
> **($\Rightarrow$) Suppose $f \in \mathcal{R}(R)$; we show $m^*(D) = 0$.** It suffices to show $\operatorname{cont}^+(D_\delta) = 0$ for every $\delta > 0$: then each $D_{1/k}$ is null, and by Lemma 3 the countable union $D = \bigcup_k D_{1/k}$ has $m^*(D) = 0$. Fix $\delta > 0$ and $\varepsilon > 0$. Since $f$ is integrable, there is a partition $P$ with $\overline{I}_P(f) - \underline{I}_P(f) < \varepsilon \delta$. Let $\mathcal{B}$ be the collection of subcells of $P$ whose interior meets $D_\delta$. Each such subcell $R_\alpha$ contains a point of $D_\delta$ in its interior, where $f$ oscillates by $\geq \delta$, so $\sup_{R_\alpha} f - \inf_{R_\alpha} f \geq \delta$. Therefore
> $$\delta \sum_{R_\alpha \in \mathcal{B}} V(R_\alpha) \leq \sum_{R_\alpha \in \mathcal{B}} \big(\sup_{R_\alpha} f - \inf_{R_\alpha} f\big) V(R_\alpha) \leq \overline{I}_P(f) - \underline{I}_P(f) < \varepsilon\delta,$$
> so $\sum_{R_\alpha \in \mathcal{B}} V(R_\alpha) < \varepsilon$. The cells of $\mathcal{B}$ cover $D_\delta$ except possibly for points lying on the boundaries between subcells; those boundary faces are finitely many graphs of constant functions, hence have content zero and can be absorbed into a further $\varepsilon$. Thus $D_\delta$ is covered by finitely many cells of total volume $< 2\varepsilon$, and since $\varepsilon$ was arbitrary, $\operatorname{cont}^+(D_\delta) = 0$.
>
> Both directions established, $f \in \mathcal{R}(R) \iff m^*(\operatorname{Disc}(f)) = 0$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Jordan measurability of a region via its boundary.** Apply the criterion to $f = \chi_S$: the discontinuities of an indicator are exactly the boundary points, $\operatorname{Disc}(\chi_S) = \partial S$. The criterion then reads "$S$ is [[Def - Jordan Measure|Jordan measurable]] iff $\partial S$ has outer measure zero". This is nonobvious because Jordan measurability was *defined* with finite covers, yet its sharp characterization is the countable-cover condition — the criterion silently upgrades the notion. Use it to certify that any region bounded by smooth surfaces is a legitimate domain of integration.

**The Riemann integrability of a derivative.** A classic surprise: there exist differentiable functions $F$ on $[0,1]$ whose derivative $f = F'$ is bounded but *not* Riemann integrable, because $\operatorname{Disc}(f)$ can have positive measure (Volterra's function). The criterion is the diagnostic tool — it locates the obstruction precisely in the size of $\operatorname{Disc}(F')$ — and it shows why the fundamental theorem of calculus needs the Lebesgue integral to hold in full generality. The application is out-of-distribution because one expects a derivative to be "nice".

**Stability of integrability under continuous post-composition.** If $g$ is integrable and $\psi$ is continuous, then $\psi \circ g$ is integrable, because $\operatorname{Disc}(\psi \circ g) \subseteq \operatorname{Disc}(g)$ — a continuous map creates no new discontinuities. This delivers, in one stroke, that $|f|, f^2, \max(f,0), \min(f,0)$ are all integrable when $f$ is. The application is nonobvious because proving $f^2$ integrable directly from Darboux sums is awkward, whereas the criterion makes it a one-line containment of discontinuity sets.

**Probability — measurability of events.** In probability, an "event" must be a [[Def - Jordan Measure|measurable]] set so that it can be assigned a probability $\int_S p \, dV$. The criterion, via the boundary characterization, tells you which geometric regions qualify: any region whose boundary is a finite union of smooth pieces. The application is nonobvious because the link runs "event has a probability" $\to$ "indicator is integrable" $\to$ "boundary is null", three reformulations deep.

---

# Bridges

- **[[Def - Jordan Measure|Jordan Measure]]** — the criterion specializes to the boundary characterization of Jordan measurability: $S$ is Jordan measurable iff $\operatorname{Disc}(\chi_S) = \partial S$ has outer measure zero. The integrability theory for functions and the measurability theory for sets are the same theorem applied to $f$ or to $\chi_S$.

- **[[Def - Lebesgue Measure|Lebesgue Measure]]** and **[[Def - Null Set and Completion|Null Sets]]** — the criterion is stated entirely in Lebesgue's language. The set "$\operatorname{Disc}(f)$ has outer measure zero" is the statement that $\operatorname{Disc}(f)$ is a [[Def - Null Set and Completion|null set]]. The theorem is the historical and conceptual reason the Riemann theory points beyond itself toward [[Measure Theory I — §1 Measure Spaces|measure theory]].

- **The Lebesgue integral** — in the [[Measure Theory II — §2 Integration|Lebesgue theory]], *every* bounded measurable function on a set of finite measure is integrable, with no constraint on its discontinuity set. The Lebesgue integral is the extension that removes the criterion's hypothesis; the criterion measures exactly the gap between the two theories.

- **Continuity and uniform continuity** — the sufficiency direction generalizes the basic fact that continuous functions on compact cells are integrable. Continuity is the special case $\operatorname{Disc}(f) = \emptyset$; the criterion is the precise quantification of "how much can continuity be relaxed".

---

# Unlocked by This

> [!tip] The Lebesgue Integral and Convergence Theorems *(from Measure Theory)*
> The criterion exposes the Riemann integral's defect — it cannot integrate functions with large discontinuity sets, and cannot interchange limits with integration. The **Lebesgue integral** of [[Measure Theory II — §2 Integration]], together with the monotone and dominated convergence theorems, is the repair, and the criterion is the precise diagnosis of what needed repairing.

> [!tip] Riemann–Stieltjes and beyond *(from Analysis)*
> The oscillation-and-negligible-set viewpoint generalizes: Riemann–Stieltjes integrability, and integrability against a general measure, are governed by analogous criteria comparing the discontinuity set of the integrand to the null sets of the integrator.
