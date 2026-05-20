---
type: theorem
subject: topology
prereqs:
  - "Def - Metric Space"
  - "Def - Open and Closed Sets in a Metric Space"
  - "Def - Continuous Map"
tags: [analysis, topology]
---

# Notation

$(X, d)$ and $(Y, \rho)$ are metric spaces, $f : X \to Y$ a function. $B_\varepsilon(x) = \{y \in X : d(x, y) < \varepsilon\}$ is the open ball of radius $\varepsilon$ about $x$ in $X$, and similarly for balls in $Y$. The pointwise $\varepsilon$–$\delta$ definition of continuity says: $f$ is continuous at $x$ if for every $\varepsilon > 0$ there is $\delta > 0$ such that $d(x, x') < \delta \implies \rho(f(x), f(x')) < \varepsilon$. The full notation registry sits on [[Topology I — §1–3 Metric and Topological Spaces]].

---

# Statement

> **Theorem (continuity via open sets).** Let $(X, d)$ and $(Y, \rho)$ be metric spaces and $f : X \to Y$ a function. The following are equivalent:
>
> 1. $f$ is **continuous at every point** in the $\varepsilon$–$\delta$ sense: for every $x \in X$ and every $\varepsilon > 0$ there exists $\delta > 0$ such that $d(x, x') < \delta$ implies $\rho(f(x), f(x')) < \varepsilon$;
> 2. **$f^{-1}(U)$ is open in $X$ for every open set $U \subseteq Y$.**

---

# Motivation

The whole point of topology is to forget the metric and keep only the open sets, but we have to *earn* the right to forget. The earning happens here: this theorem is the bridge that proves continuity — the central notion of analysis — depends only on which sets are open, not on the particular numerical distances. Two metrics that produce the same open sets give exactly the same continuous functions, even though they may have wildly different "shapes" of balls (Euclidean versus taxicab metric in $\mathbb{R}^n$ being the standard example). The theorem licenses the abstraction from metric spaces to topological spaces.

Before stating it, observe that we already *have* the $\varepsilon$–$\delta$ definition of continuity, and it works perfectly well in metric spaces. So why move to the open-set formulation? Because (i) it is more economical — one verification per open set, rather than per point and per $\varepsilon$ — and (ii) it is the definition that *survives* the move to a general topological space where there is no metric, while the $\varepsilon$–$\delta$ version cannot even be stated. The theorem says these two definitions are equivalent in metric spaces, which is the empirical evidence that the open-set definition is the right generalization.

The bridge is mediated by the **open-ball basis**: in any metric space, the open sets are exactly the unions of open balls. So a statement about all open sets reduces, after a basis argument, to a statement about open balls — which is essentially the $\varepsilon$–$\delta$ statement in disguise. The two directions of the equivalence are: $\varepsilon$–$\delta$ at every point implies preimages of balls are open (chase definitions), and preimages of opens are open implies $\varepsilon$–$\delta$ at every point (specialize to balls in the target). Once one sees this, the theorem is not deep — but its consequences are foundational.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$f : (X, d) \to (Y, \rho)$ is $\varepsilon$–$\delta$ continuous at every point" (one direction of the equivalence) or "$f^{-1}(U)$ is open for every open $U \subseteq Y$" (the other). The skill is recognizing when either holds.

The first disguised source is **Lipschitz continuity** (or, more generally, Hölder continuity). Property $B$: $\rho(f(x), f(x')) \leq L \cdot d(x, x')$ for some constant $L > 0$ and all $x, x'$. The bridge: given $\varepsilon$, take $\delta = \varepsilon / L$. Lipschitz $\implies \varepsilon$–$\delta$ continuous at every point (with uniform constants), so the theorem applies. *Example:* the distance function $x \mapsto d(x, x_0)$ from a fixed point is $1$-Lipschitz by the triangle inequality, so it is continuous — and this is how Bredon proves continuity of distance functions in the early problems.

The second disguised source is **uniform continuity**: for every $\varepsilon > 0$ there is a *single* $\delta > 0$ (independent of $x$) such that $d(x, x') < \delta \implies \rho(f(x), f(x')) < \varepsilon$. This trivially implies pointwise $\varepsilon$–$\delta$ continuity, hence the open-set condition. *Example:* every continuous function on a compact metric space is uniformly continuous (Heine–Cantor), which is the typical route to applying uniform-continuity-type lemmas in subsequent work.

The third disguised source is **isometric embedding**. Property $B$: $\rho(f(x), f(x')) = d(x, x')$ for all $x, x'$. This is the Lipschitz case with $L = 1$, and the bridge to $\varepsilon$–$\delta$ continuity is automatic: take $\delta = \varepsilon$. *Example:* the inclusion of any subspace $(Y, d|_{Y \times Y}) \hookrightarrow (X, d)$ is an isometry, hence continuous, hence the subspace topology agrees with the metric subspace topology — see [[Def - Subspace Topology]].

The fourth disguised source is **continuity-by-composition**. Property $B$: $f$ is expressed as a composition $g \circ h$ of two functions each known to be continuous. The bridge: composition of continuous maps is continuous (the composition pulls open sets back to opens — preimage commutes with composition). *Example:* showing $x \mapsto \sin(\|x\|^2)$ is continuous on $\mathbb{R}^n$ by composing $\|\cdot\|^2$, $\sin$, both continuous.

**Targets (Output Amplification)**

The conclusion is "$f^{-1}(U)$ open whenever $U$ open" (with the other direction giving the $\varepsilon$–$\delta$ form).

Combine with **the basis structure on the target.** Property $D$: $Y$ has a basis $\mathcal{B}$ for its topology — for metric spaces, the open ball basis. The amplified result $E$: continuity of $f$ can be checked on $\mathcal{B}$ alone, i.e. $f^{-1}(B)$ open for every $B \in \mathcal{B}$ suffices. Combined with the metric ball basis, this reduces continuity verification to "the $\varepsilon$–$\delta$ statement at every point" — exactly the [[Thm - Continuity via Bases and Neighbourhood Bases|basis criterion]]. The combination is what makes practical continuity proofs short.

Combine with **compactness on the source.** Property $D$: $X$ is compact. The amplified result $E$: $f$ is automatically uniformly continuous (Heine–Cantor), and $f(X)$ is compact in $Y$. The pointwise $\varepsilon$–$\delta$ promoted to uniform $\varepsilon$–$\delta$ by compactness is one of the most-used analytic upgrades; it underlies the proof of uniform convergence of polynomial approximations on $[0, 1]$.

Combine with **connectedness on the source.** Property $D$: $X$ is connected. The amplified result $E$: $f(X)$ is connected in $Y$. Continuity from connected to discrete forces constancy — see the [[Topology I — §1–3 Metric and Topological Spaces#Legal Operations|discrete-valued map argument]] in Bredon §4. This is the route from continuity to the intermediate value theorem.

Combine with **the closed-set version.** Property $D$: rewrite the open-set condition as "preimages of closed sets are closed" (using complements). The amplified result $E$: a function is continuous if and only if $f^{-1}(F)$ is closed for every closed $F$. This dual formulation is often more useful when the target side comes with a natural closed-set description, e.g. when $Y = \mathbb{R}$ and one is testing where $f$ takes a given value.

---

# Why Is It True

The equivalence is, at heart, the equivalence between two ways of saying "$f$ does not jump":

The $\varepsilon$–$\delta$ formulation is *local* and *quantitative*. It says: pick a point $x$. Whatever target tolerance $\varepsilon$ you specify around $f(x)$, you can find a source tolerance $\delta$ around $x$ such that within $\delta$ of $x$, the function stays within $\varepsilon$ of $f(x)$. So locally, $f$ controls its own variation in a tunable way.

The open-set formulation is *global* and *qualitative*. It says: any open set $U$ on the target side pulls back to an open set on the source side. So the structural class of "open" is preserved by $f^{-1}$ — and openness is exactly the property "every point has a little room around it inside the set". So pulling back an open set means the preimage also has room around each of its points, which is the same as saying $f$ does not push interior points to boundary or exterior.

The bridge between the two is the **open-ball basis**. In a metric space, an open set is exactly a union of open balls, and "$f$ has $\varepsilon$–$\delta$ continuity at $x$" is precisely the statement that $f^{-1}(B_\varepsilon(f(x)))$ contains a ball $B_\delta(x)$ — *that one open set on the target side, namely the ball about $f(x)$, has open preimage at $x$*. Iterating this over every $x \in X$ and every $\varepsilon > 0$ gives the open-set condition for balls in $Y$, and since balls form a basis, it gives the condition for all open sets.

Why does the reverse direction work? Because to verify $\varepsilon$–$\delta$ continuity at $x$, you need only an open set around $f(x)$ — specifically, the ball $B_\varepsilon(f(x))$. Its preimage is open by hypothesis, and contains $x$, so by the definition of open in a metric space there is a $\delta$ with $B_\delta(x) \subseteq f^{-1}(B_\varepsilon(f(x)))$, which is precisely the $\varepsilon$–$\delta$ statement at $x$.

The reason to expect the theorem, beyond the line-by-line bridge: continuity is the statement that "nearby goes to nearby", and both formulations express this — one in metric language ("close in $d$" maps to "close in $\rho$") and one in topological language ("open in $X$" pulls back from "open in $Y$"). The open-set version is what survives once we no longer have a metric to measure "close" with, because openness is the metric-free condition encoding "nearby points have room around them".

---

# What Makes This Hard

The non-obvious step in the forward direction is recognizing that you do not need to verify "$f^{-1}(U)$ open" for *every* open $U$ — you only need it for the open balls $B_\varepsilon(y)$ in $Y$, because every open is a union of balls and $f^{-1}$ commutes with unions. The most common error is to chase the $\varepsilon$–$\delta$ statement at one point, get the right $\delta$, and then forget that one needs to choose $\delta$ uniformly *across all points of $f^{-1}(B_\varepsilon(y))$* — except that one does not! Open-set means "for each point in the set, *some* $\delta$ works for that point"; the $\delta$ may depend on the point, and that is exactly what makes the proof go through.

---

# Rederivation Scaffold

**High-level strategy:**
The equivalence is mediated by the open-ball basis. The forward direction translates $\varepsilon$–$\delta$ at each point into "preimage of each open ball is open" and uses the basis to extend to all opens. The reverse direction specializes the open-set condition to open balls in $Y$, recovering $\varepsilon$–$\delta$ at every point.

**Subgoal decomposition:**

1. **(Forward) Suppose $f$ is $\varepsilon$–$\delta$ continuous at every point; show $f^{-1}(B_\varepsilon(y))$ is open for every open ball.**
   - *Hint:* For $x \in f^{-1}(B_\varepsilon(y))$, $f(x) \in B_\varepsilon(y)$, so $\rho(f(x), y) < \varepsilon$. Set $\varepsilon' = \varepsilon - \rho(f(x), y) > 0$; the $\varepsilon$–$\delta$ statement at $x$ for target tolerance $\varepsilon'$ gives a $\delta$ such that $B_\delta(x) \subseteq f^{-1}(B_{\varepsilon'}(f(x))) \subseteq f^{-1}(B_\varepsilon(y))$.
   - *Why needed:* It gives the open-set condition for the open balls, the basis of the topology on $Y$.

2. **Extend to all opens of $Y$ using the basis structure.**
   - *Hint:* Every open $U \subseteq Y$ is a union of open balls $B_{\varepsilon_i}(y_i)$; $f^{-1}$ commutes with unions, so $f^{-1}(U) = \bigcup f^{-1}(B_{\varepsilon_i}(y_i))$, a union of opens, hence open.
   - *Why needed:* It completes the forward direction.

3. **(Reverse) Suppose $f^{-1}(U)$ open for every open $U$; show $\varepsilon$–$\delta$ at every point.**
   - *Hint:* Fix $x$ and $\varepsilon > 0$. $B_\varepsilon(f(x))$ is open in $Y$, so $f^{-1}(B_\varepsilon(f(x)))$ is open in $X$ and contains $x$; by definition of "open in a metric space" there is $\delta > 0$ with $B_\delta(x) \subseteq f^{-1}(B_\varepsilon(f(x)))$, i.e. $d(x, x') < \delta \implies \rho(f(x), f(x')) < \varepsilon$.
   - *Why needed:* It produces the $\varepsilon$–$\delta$ statement at $x$ directly from openness of the preimage.

---

# Lemma Decomposition

> [!note]- Lemma 1: Open balls form a basis for the metric topology
> **Statement:** In a metric space $(X, d)$, every open set is a union of open balls; equivalently the collection $\{B_\varepsilon(x) : x \in X, \varepsilon > 0\}$ is a basis for the topology.
>
> **Hint:** By definition of "open" in a metric space, every $x \in U$ open has some $B_\varepsilon(x) \subseteq U$.
>
> **Why needed:** It reduces "open-set condition for all opens" to "open-set condition for balls", which is what matches $\varepsilon$–$\delta$ exactly.
>
> > [!note]- Full proof
> > Let $U \subseteq X$ be open. By definition, for each $x \in U$ there is $\varepsilon_x > 0$ with $B_{\varepsilon_x}(x) \subseteq U$. Then $U = \bigcup_{x \in U} B_{\varepsilon_x}(x)$: each ball is contained in $U$ (right-hand side $\subseteq$ left-hand side), and each $x \in U$ is in $B_{\varepsilon_x}(x)$ (left-hand side $\subseteq$ right-hand side). So $U$ is the union of the family $\{B_{\varepsilon_x}(x)\}_{x \in U}$.

> [!note]- Lemma 2: Preimages commute with unions and intersections
> **Statement:** For $f : X \to Y$ and any family $\{V_\alpha\}_{\alpha \in I}$ of subsets of $Y$:
> $$f^{-1}\Big(\bigcup_\alpha V_\alpha\Big) = \bigcup_\alpha f^{-1}(V_\alpha), \qquad f^{-1}\Big(\bigcap_\alpha V_\alpha\Big) = \bigcap_\alpha f^{-1}(V_\alpha).$$
>
> **Hint:** Element-chase: $x \in f^{-1}(\bigcup_\alpha V_\alpha) \iff f(x) \in \bigcup_\alpha V_\alpha \iff \exists \alpha,\ f(x) \in V_\alpha \iff x \in \bigcup_\alpha f^{-1}(V_\alpha)$. Same for intersections.
>
> **Why needed:** It is the algebraic reason a basis-level open-set condition propagates to all opens.
>
> > [!note]- Full proof
> > *Unions:* $x \in f^{-1}(\bigcup V_\alpha) \iff f(x) \in \bigcup V_\alpha \iff \exists \alpha, f(x) \in V_\alpha \iff \exists \alpha, x \in f^{-1}(V_\alpha) \iff x \in \bigcup f^{-1}(V_\alpha)$.
> >
> > *Intersections:* $x \in f^{-1}(\bigcap V_\alpha) \iff f(x) \in \bigcap V_\alpha \iff \forall \alpha, f(x) \in V_\alpha \iff \forall \alpha, x \in f^{-1}(V_\alpha) \iff x \in \bigcap f^{-1}(V_\alpha)$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $f : (X, d) \to (Y, \rho)$ be a function between metric spaces.
>
> **($\Rightarrow$) Suppose $f$ is $\varepsilon$–$\delta$ continuous at every point.** We show $f^{-1}(U)$ is open whenever $U \subseteq Y$ is open. Let $x \in f^{-1}(U)$, so $f(x) \in U$. Since $U$ is open in $Y$, there is $\varepsilon > 0$ with $B_\varepsilon(f(x)) \subseteq U$. By $\varepsilon$–$\delta$ continuity at $x$, there is $\delta > 0$ with $d(x, x') < \delta \implies \rho(f(x), f(x')) < \varepsilon$, i.e. $B_\delta(x) \subseteq f^{-1}(B_\varepsilon(f(x))) \subseteq f^{-1}(U)$. So every $x \in f^{-1}(U)$ has an open ball about it inside $f^{-1}(U)$, and $f^{-1}(U)$ is open.
>
> **($\Leftarrow$) Suppose $f^{-1}(U)$ is open for every open $U \subseteq Y$.** We show $f$ is $\varepsilon$–$\delta$ continuous at every $x \in X$. Fix $x \in X$ and $\varepsilon > 0$. The ball $B_\varepsilon(f(x))$ is open in $Y$, so $f^{-1}(B_\varepsilon(f(x)))$ is open in $X$. Since $x \in f^{-1}(B_\varepsilon(f(x)))$, there is $\delta > 0$ with $B_\delta(x) \subseteq f^{-1}(B_\varepsilon(f(x)))$. This says $d(x, x') < \delta \implies f(x') \in B_\varepsilon(f(x)) \implies \rho(f(x), f(x')) < \varepsilon$, which is $\varepsilon$–$\delta$ continuity at $x$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Continuity of the distance function from a set.** For $A \subseteq X$ in a metric space, the function $d_A(x) = \inf_{a \in A} d(x, a)$ is $1$-Lipschitz: $|d_A(x) - d_A(x')| \leq d(x, x')$ by triangle inequality and infimum manipulation. So $d_A$ is continuous by the theorem. The application is nonobvious because the definition of $d_A$ involves an infimum — but the Lipschitz bound, which feeds directly into the $\varepsilon$–$\delta$ form, makes continuity automatic.

**The norm on a Banach space.** The norm $\|\cdot\| : V \to \mathbb{R}$ on a normed vector space is $1$-Lipschitz: $|\|x\| - \|y\|| \leq \|x - y\|$ (reverse triangle inequality). So it is continuous as a map from $V$ to $\mathbb{R}$. This is used silently every time one says "the norm is continuous, so it preserves limits".

**Sequential continuity in metric spaces.** A function $f : X \to Y$ between metric spaces is continuous if and only if it is **sequentially continuous**: $x_n \to x$ implies $f(x_n) \to f(x)$. The proof uses the equivalence in the theorem and the fact that closure equals sequential closure in metric (first countable) spaces — see [[Thm - Characterizations of the Closure]]. This is the bridge between "topological" continuity and "sequence-based" continuity that justifies $\varepsilon$–$N$ style proofs.

**Application to the matrix exponential.** The matrix exponential $\operatorname{Exp}(X) = \sum_n X^n / n!$ is the limit of polynomial maps on $M_n(\mathbb{R})$, each continuous in the operator norm; the sum converges uniformly on compact sets, so $\operatorname{Exp}$ is continuous. The argument uses the theorem to assert continuity of each polynomial piece, then uniform convergence to preserve continuity in the limit.

---

# Bridges

- **[[Thm - Continuity via Bases and Neighbourhood Bases]]** — the generalization to arbitrary topological spaces with bases. The metric ball basis is a special case, and the basis criterion is the abstract form that the present theorem specializes to.

- **[[Def - Continuous Map]]** — the open-set formulation is the actual definition of continuity for topological spaces. The present theorem says: in metric spaces, this abstract definition coincides with the pointwise $\varepsilon$–$\delta$ definition we already had.

- **[[Def - Equivalent Metrics]]** — two metrics on the same set are topologically equivalent if they produce the same open sets, which by this theorem is the same as "having the same continuous functions". The theorem is what makes "topologically equivalent" a useful notion: equivalent metrics differ in distance but agree on continuity.

- **[[Thm - The Pasting Lemma]]** — the pasting lemma uses the closed-set version of this theorem ("preimage of closed is closed") in its proof. The closed-set reformulation is dual to the open-set one and is obtained by taking complements.

---

# Unlocked by This

> [!tip] General Topological Continuity *(in this topic)*
> Once one knows that continuity is determined by the open sets, one can *define* continuity in arbitrary topological spaces as "preimage of open is open". This is [[Def - Continuous Map]] and is the start of general topology proper. The theorem is the calibration that says this abstract definition does not contradict the analytic one in the metric case.

> [!tip] Topological Equivalence of Metrics *(in this topic)*
> Two metrics on a set are **topologically equivalent** if they give the same open sets, by this theorem equivalently the same continuous functions. The three standard metrics on $\mathbb{R}^n$ — $\ell^1$, $\ell^2$, $\ell^\infty$ — are equivalent, even though their balls have different shapes (diamond, ball, cube). See [[Def - Equivalent Metrics]].

> [!tip] Continuity in Functional Analysis *(from Functional Analysis)*
> For a linear map $T : V \to W$ between normed spaces, the open-set definition of continuity collapses to a single condition: there is $C > 0$ with $\|Tv\|_W \leq C \|v\|_V$ — i.e., **continuity is the same as boundedness for linear maps**. This is the structural simplification that drives operator theory and the spectral theorem.
