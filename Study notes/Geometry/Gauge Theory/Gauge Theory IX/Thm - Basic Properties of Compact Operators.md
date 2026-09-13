---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Compact Operator"
  - "Def - Cauchy Sequence and Complete Metric Space"
  - "Def - Inner Product Space"
  - "Thm - Compactness in Metric Spaces (Three Equivalents)"
  - "Thm - Best Approximation by Orthogonal Projection"
  - "Thm - Heine–Borel Theorem"
tags: [geometry, gauge-theory, functional-analysis]
---

# Notation

Throughout, $X$, $Y$, $Z$, and $W$ are [[Def - Cauchy Sequence and Complete Metric Space|Banach spaces]] over a fixed scalar field $\mathbb{F} \in \{\mathbb{R}, \mathbb{C}\}$; a Banach space is a normed vector space that is complete as a [[Def - Metric Space|metric space]] under $d(u,v) = \lVert u - v \rVert$. We write $\lVert \cdot \rVert_X$ for the norm of $X$ and drop the subscript when the space is clear. The **closed unit ball** of $X$ is $B_X := \{x \in X : \lVert x \rVert_X \le 1\}$. A linear map $T : X \to Y$ is **bounded** if $\lVert T \rVert := \sup_{x \in B_X} \lVert Tx \rVert_Y < \infty$; then $\lVert Tx \rVert \le \lVert T \rVert \lVert x \rVert$ for all $x$, and for a linear map boundedness is the same as continuity. The space of all bounded linear operators $X \to Y$ is $\mathcal{B}(X,Y)$, a Banach space under the operator norm; we abbreviate $\mathcal{B}(X) := \mathcal{B}(X,X)$. For $S \subseteq Y$, $\overline{S}$ is its closure, $S$ is **relatively compact** if $\overline{S}$ is a [[Def - Compact Space|compact]] subset of $Y$, and $S$ is [[Def - Totally Bounded Metric Space|totally bounded]] if for every $\varepsilon > 0$ there is a finite set $\{y_1,\dots,y_N\} \subseteq Y$ — a *finite $\varepsilon$-net* — with $S \subseteq \bigcup_i \{y : \lVert y - y_i\rVert < \varepsilon\}$.

A bounded linear operator $K : X \to Y$ is a **[[Def - Compact Operator|compact operator]]** if $\overline{K(B_X)}$ is compact in $Y$. As proved on [[Def - Compact Operator]], for a bounded $K$ this is equivalent to each of: **(total boundedness)** $K(B_X)$ is totally bounded; and **(sequential criterion)** every bounded sequence $(x_j)_{j\ge1}$ in $X$ has a subsequence $(x_{j_i})$ with $(Kx_{j_i})$ convergent in $Y$. We write $\mathcal{K}(X,Y) \subseteq \mathcal{B}(X,Y)$ for the compact operators and $\mathcal{K}(X) := \mathcal{K}(X,X)$. An operator $F$ has **finite rank** if $\dim F(X) < \infty$; every bounded finite-rank operator is compact, as verified in the Examples section of [[Def - Compact Operator]].

For parts (iv) and (v) the domain and codomain are [[Def - Inner Product Space|Hilbert spaces]] $H_1$, $H_2$, $H$ — Banach spaces whose norm comes from an inner product $\lVert v \rVert = \sqrt{\langle v, v\rangle}$, complete in that norm. We follow the convention of [[Def - Inner Product Space]]: the inner product is **linear in its first slot** and conjugate-linear in its second, $\langle \lambda u, v\rangle = \lambda\langle u,v\rangle$ and $\langle u, \lambda v\rangle = \bar\lambda\langle u,v\rangle$, with $\bar\lambda = \lambda$ when $\mathbb{F} = \mathbb{R}$. The **Hilbert adjoint** of $T \in \mathcal{B}(H_1,H_2)$, whose existence part (v) rests on, is the operator $T^* \in \mathcal{B}(H_2,H_1)$ characterised by $\langle Tx, y\rangle_{H_2} = \langle x, T^*y\rangle_{H_1}$ for all $x \in H_1$, $y \in H_2$; it exists and is unique by Lemma 5 below.

> [!warning] Convention: what "compact operator" and "adjoint" mean here
> Haydys uses the compactness of the Sobolev embedding (Theorem 136(ii), item A-T5.1.1(ii)) and the notion of a bounded operator between Banach spaces in the definition of a Fredholm operator (item A-D5.2.6), but states the basic operator-theoretic facts by reference to Brezis, *Functional Analysis, Sobolev Spaces and Partial Differential Equations*, §6.1. The present page proves those facts in full and in the vault's conventions. The **Hilbert adjoint** $T^*$ of this page (a bounded operator on Hilbert spaces, defined through the inner products) must not be confused with the **formal adjoint** of a differential operator ([[Def - Formal Adjoint of a Differential Operator]]), which is a differential operator adjoint to the given one only in the $L^2$ pairing of smooth sections; the two notions are related on the Sobolev completions but are defined differently, and this page concerns only the former.

---

# Statement

> **Theorem (basic properties of compact operators).** Let $X$, $Y$, $Z$, $W$ be Banach spaces over $\mathbb{F}$ and $H_1$, $H_2$ Hilbert spaces over $\mathbb{F}$. Then:
>
> **(i) (Closed subspace.)** The set $\mathcal{K}(X,Y)$ of compact operators is a linear subspace of $\mathcal{B}(X,Y)$, and it is closed in the operator norm: if $(K_n) \subseteq \mathcal{K}(X,Y)$ and $\lVert K_n - K\rVert \to 0$ for some $K \in \mathcal{B}(X,Y)$, then $K \in \mathcal{K}(X,Y)$.
>
> **(ii) (Ideal property.)** If $A \in \mathcal{B}(W,X)$, $K \in \mathcal{K}(X,Y)$, and $B \in \mathcal{B}(Y,Z)$, then $BKA \in \mathcal{K}(W,Z)$. In particular, $\mathcal{K}(X)$ is a two-sided ideal of the algebra $\mathcal{B}(X)$.
>
> **(iii) (Sum.)** If $K_1, K_2 \in \mathcal{K}(X,Y)$ then $K_1 + K_2 \in \mathcal{K}(X,Y)$.
>
> **(iv) (Finite-rank approximation, Hilbert case.)** A bounded operator $K \in \mathcal{B}(H_1,H_2)$ is compact if and only if it is an operator-norm limit of finite-rank operators: there exist finite-rank $F_n \in \mathcal{B}(H_1,H_2)$ with $\lVert K - F_n\rVert \to 0$. Equivalently, $\mathcal{K}(H_1,H_2)$ is the operator-norm closure of the finite-rank operators.
>
> **(v) (Adjoint.)** If $K \in \mathcal{K}(H_1,H_2)$ then its Hilbert adjoint $K^* \in \mathcal{B}(H_2,H_1)$ is compact: $K^* \in \mathcal{K}(H_2,H_1)$.

Part (iii) is the additive-closure half of part (i); we list it separately because the sources (and the elliptic theory downstream) invoke "the sum of two compact operators is compact" on its own, and prove it first so that (i) may cite it.

---

# Motivation

Compactness is introduced on [[Def - Compact Operator]] as the property of a single operator that restores the Bolzano–Weierstrass principle lost in infinite dimensions. That definition, by itself, is inert: to *use* compact operators one needs to know that the class is stable under the operations one actually performs on it. This page supplies exactly that stability, and it is the reason the one-line phrase "$K$ is compact" can be wielded so freely in the elliptic theory that follows.

Every use of compactness in this series routes through one of these five facts. When [[Thm - Elliptic Operators on Closed Manifolds are Fredholm]] argues that the kernel of an elliptic operator $L$ is finite-dimensional, it does so by exhibiting the inclusion of $\ker L$ into a Sobolev space as compact *and* as the identity — a contradiction with the non-compactness of the identity unless $\ker L$ is finite-dimensional; the argument needs the ideal property (ii) to compose the Rellich inclusion with the elliptic estimate and stay compact. When [[Thm - Riesz-Schauder Theory for Compact Perturbations of the Identity]] studies $\mathrm{Id} + K$, it approximates $K$ by finite-rank operators and reduces to finite-dimensional linear algebra — that reduction is part (iv). When the Hodge theorem and the Fredholm alternative pass from an operator to its adjoint, they need the adjoint of a compact operator to be compact — part (v). Part (i), closedness, is what lets one *construct* compact operators as limits (the diagonal operators, the Rellich inclusion via Fourier truncation) rather than verifying compactness from the definition each time. The theorem is therefore not a collection of technical lemmas but the operating manual for the single most important operator class in the analysis of this series.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypotheses are mild — "$K$ is compact", "$A,B$ bounded" — so the real question is how a problem hands you compactness without announcing it.

The first disguised source is **an operator presented as a limit**. If an operator $K$ arises as an operator-norm limit $K = \lim_n K_n$ of operators already known to be compact — most often finite-rank truncations — then $K$ is compact, by part (i). The bridge $B \Rightarrow A$ here is "norm-convergent sequence of compacts $\Rightarrow$ compact", and it is non-obvious because norm convergence is a strong hypothesis one must first establish by a tail estimate. *Example problem:* show that a diagonal operator $Ke_j = \lambda_j e_j$ on $\ell^2$ with $\lambda_j \to 0$ is compact by truncating to the first $N$ coordinates and estimating $\lVert K - K_N\rVert \le \sup_{j > N}|\lambda_j| \to 0$; this is exactly the route taken on [[Def - Compact Operator]], which cites part (i).

The second disguised source is **an operator that factors through a compact one**. If $T = BKA$ with $K$ compact and $A,B$ merely bounded, then $T$ is compact by the ideal property (ii), and one often meets $T$ without any $K$ named — the compact factor is hidden in a chain of localisations, extensions, and restrictions. The bridge is "factors through a compact operator $\Rightarrow$ compact", and its subtlety is recognising which link in the chain is the compact one. *Example problem:* a pseudodifferential smoothing $E : W^{k}(M) \to W^{k}(M)$ that factors as $W^{k} \xrightarrow{\iota} W^{k+1} \xrightarrow{P} W^{k}$ through the Rellich inclusion $\iota$ is compact because $\iota$ is; $P$ need only be bounded.

The third disguised source is **the Sobolev inclusion on a compact manifold**. Any operator built from $W^{k,p}(M;E)$ by first including into a lower-order Sobolev space (with a strict gain of regularity) is compact, because that inclusion is the Rellich operator ([[Thm - Rellich Compactness Theorem]]). The bridge is "a bounded map that lands *after* a compact Sobolev inclusion is compact", again by (ii). *Example problem:* multiplication by a smooth function followed by the Rellich inclusion is compact, so the difference of two elliptic operators of the same principal symbol is a compact perturbation.

**Targets (Output Amplification).** The bare conclusions combine with a little extra structure to do much more.

Combine (i) and (iii) with **the fact that finite-rank operators are compact** to conclude that $\mathcal{K}(X)$ is the operator-norm closure of the finite-rank operators, and hence a *Banach* space in its own right (a closed subspace of the Banach space $\mathcal{B}(X)$ is complete). The extra ingredient is completeness of $\mathcal{B}(X)$; the payoff is that limiting constructions stay inside $\mathcal{K}(X)$, which is what makes Fredholm perturbation theory possible.

Combine the ideal property (ii) with **the Rellich theorem** to obtain that an elliptic operator $L$ on a closed manifold has *compact resolvent* on the appropriate scale: the inclusion of $\ker(L - \lambda)$ into a Sobolev space is compact, forcing finite dimension. The extra ingredient is the elliptic estimate; the payoff is the entire Fredholm theory of [[Thm - Elliptic Operators on Closed Manifolds are Fredholm]].

Combine the adjoint property (v) with **self-adjointness and the spectral theorem for compact self-adjoint operators** to diagonalise a compact self-adjoint operator: it has an orthonormal eigenbasis with eigenvalues accumulating only at $0$. The extra ingredient is the spectral theorem; the payoff is the Hodge decomposition, where the Green's operator of an elliptic Laplacian is compact and self-adjoint and its eigenspaces are the finite-dimensional pieces on [[Thm - Hodge Theorem for Elliptic Complexes]].

---

# Why Is It True

The whole theorem follows from a single principle, and it is worth isolating it before any computation.

> **Compactness is stability under every operation that does not enlarge the image of the unit ball.** A compact operator is one whose unit-ball image is within bounded reach of a compact set; any operation whose output image is a bounded continuous shuffle of that image — a bounded linear map applied before or after, a uniform limit, a finite sum, passage to the adjoint — cannot destroy the total boundedness, so it cannot destroy compactness.

Read the five parts through this lens. **The ideal property (ii)** is the principle in its purest form: precomposing with $A$ only feeds $K$ a ball scaled by $\lVert A\rVert$, and $K$ sends bounded sets to relatively compact sets; postcomposing with the continuous $B$ carries a relatively compact set to a relatively compact set, because continuous images of compact sets are compact. Nothing has enlarged the reach of the image. **The sum (iii)** succeeds because a diagonal (double) subsequence extracts convergence for $K_1$ and then for $K_2$ simultaneously, and the sum of two convergent sequences converges. **Closedness (i)** is the $\varepsilon/3$ principle: if $K_n$ is uniformly close to $K$, then a finite $\varepsilon/3$-net for the totally bounded $K_n(B_X)$ is, after adding another $\varepsilon/3$ of slack twice, a finite $\varepsilon$-net for $K(B_X)$. **Finite-rank approximation (iv)** is compactness read backwards: total boundedness gives a finite $\varepsilon$-net $y_1,\dots,y_N$ of $K(B_X)$, and projecting orthogonally onto the finite-dimensional span of the net changes $K$ by at most $\varepsilon$, because the orthogonal projection produces the *best* approximation in that span and the net points are already within $\varepsilon$. **The adjoint (v)** inherits compactness through (iv): the adjoint of a finite-rank operator is finite-rank, and adjunction is an isometry ($\lVert T^*\rVert = \lVert T\rVert$), so the finite-rank approximants of $K$ hand over, verbatim, finite-rank approximants of $K^*$.

Every part is the same sentence specialised: whatever you do to a compact operator, as long as it does not blow up the image of the ball, the result is compact.

---

# What Makes This Hard

The genuinely non-trivial content is concentrated in (iv) and (v), and it is analytic, not formal. In (iv), the "$\Rightarrow$" direction is easy to state but its proof hides the one construction of the whole page — the orthogonal projection $P$ onto the span of a finite $\varepsilon$-net — and the key inequality $\lVert Kx - PKx\rVert \le \lVert Kx - y_i\rVert$ is *not* the triangle inequality but the best-approximation property of orthogonal projection; a reader who tries to bound $\lVert K - PK\rVert$ by hand without invoking best approximation typically gets stuck. In (v), the difficulty is that the Hilbert adjoint does not exist by fiat: its construction requires the Riesz representation theorem, which in turn requires the projection theorem for closed subspaces of a Hilbert space — infinite-dimensional facts that this page must prove, since only their finite-dimensional cousins are elsewhere in the vault. The common error is to treat "$K^*$" as given and prove only $\lVert (PK)^* - K^*\rVert = \lVert PK - K\rVert$; the isometry of adjunction and the existence of the adjoint are the substance.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Establish first the two metric-space facts that translate between the three faces of compactness (Lemma 1) and that finite-rank operators are compact (Lemma 2). Prove (iii) by a double-subsequence argument and (ii) by pushing a bounded sequence through $A$, $K$, $B$. Prove (i) by the $\varepsilon/3$ argument on finite nets. For (iv) build the orthogonal projection onto the span of an $\varepsilon$-net and use best approximation; the reverse direction is (i) plus Lemma 2. For (v) build the Hilbert adjoint from scratch — the projection theorem (Lemma 3), the Riesz representation theorem (Lemma 4), the adjoint and its isometry and finite-rank preservation (Lemma 5) — and then transport the finite-rank approximants of (iv) across the adjoint.

**Subgoal decomposition:**

1. **Metric bridge.** In a complete space, "relatively compact", "totally bounded", and "every sequence has a convergent subsequence" agree.
   - *Hint:* Compact $\Leftrightarrow$ complete and totally bounded $\Leftrightarrow$ sequentially compact, from [[Thm - Compactness in Metric Spaces (Three Equivalents)]]; closures of totally bounded sets are totally bounded, and closed subsets of complete spaces are complete.
   - *Why needed:* It lets each part use whichever face of compactness is most convenient.

2. **Finite rank is compact.** $\dim F(X) < \infty \Rightarrow F$ compact.
   - *Hint:* $F(B_X)$ is bounded in the finite-dimensional space $F(X)$, where bounded sets are relatively compact.
   - *Why needed:* It is the base case of (iv)'s reverse direction and the source of the approximants in (v).

3. **Sum, ideal, closedness.** Parts (iii), (ii), (i) in that order.
   - *Hint:* Double subsequence for (iii); push a bounded sequence through $A,K,B$ for (ii); $\varepsilon/3$ nets for (i).
   - *Why needed:* (iii) supplies additive closure to (i); (i) is used in (iv) and (v).

4. **Finite-rank approximation.** $K$ compact $\Leftrightarrow$ norm-limit of finite-rank (Hilbert).
   - *Hint:* "$\Leftarrow$" is Lemma 2 plus (i). "$\Rightarrow$": finite $\varepsilon$-net of $K(B_{H_1})$, orthogonal projection $P$ onto its span, $\lVert K - PK\rVert \le \varepsilon$ by best approximation.
   - *Why needed:* It is the algebraic description of $\mathcal{K}$ and the engine of (v).

5. **Adjoint theory.** Projection theorem $\to$ Riesz $\to$ existence/isometry/finite-rank of the adjoint.
   - *Hint:* Project onto $\ker\phi$ to represent a functional; define $T^*y$ as the Riesz vector of $x \mapsto \langle Tx, y\rangle$; show $\lVert T^*\rVert = \lVert T\rVert$ and that the adjoint of $\sum_i\langle\cdot,a_i\rangle b_i$ is $\sum_i\langle\cdot,b_i\rangle a_i$.
   - *Why needed:* Without it part (v) cannot even be stated, let alone proved.

6. **Assemble (v).** Approximate $K$ by finite-rank $F_n$ (part iv); then $F_n^*$ is finite-rank and $\lVert K^* - F_n^*\rVert = \lVert K - F_n\rVert \to 0$; conclude by (iv) reverse.

---

# Lemma Decomposition

> [!note]- Lemma 1: The three faces of compactness agree in a complete space
> **Statement:** Let $Y$ be a complete metric space and $S \subseteq Y$. The following are equivalent: (a) $\overline{S}$ is compact; (b) $S$ is totally bounded; (c) every sequence in $S$ has a subsequence converging in $Y$.
>
> **Hint:** Use [[Thm - Compactness in Metric Spaces (Three Equivalents)]]. For (b) $\Rightarrow$ (a), the closure of a totally bounded set is totally bounded and, being closed in a complete space, is complete. For (c), a sequence in $\overline{S}$ can be approximated by a sequence in $S$.
>
> **Why needed:** Parts (i)–(iv) each use whichever of (a), (b), (c) is most convenient, and this lemma certifies the switches. It is the metric-space substrate under the operator theory.
>
> > [!note]- Full proof
> > We invoke the following, restated at its point of use.
> > > **Theorem (compactness in metric spaces).** For a metric space $(M,d)$, the following are equivalent: $M$ is compact; $M$ is sequentially compact; $M$ is complete and totally bounded. See [[Thm - Compactness in Metric Spaces (Three Equivalents)]].
> >
> > **(b) $\Rightarrow$ (a).** Assume $S$ is totally bounded. *First, $\overline{S}$ is totally bounded.* Fix $\varepsilon > 0$ and pick a finite $(\varepsilon/2)$-net $\{y_1,\dots,y_N\}$ for $S$ (definition of total boundedness of $S$). For $z \in \overline{S}$ there is $s \in S$ with $\lVert z - s\rVert < \varepsilon/2$ (definition of closure) and an index $i$ with $\lVert s - y_i\rVert < \varepsilon/2$ (the net covers $S$), so $\lVert z - y_i\rVert \le \lVert z - s\rVert + \lVert s - y_i\rVert < \varepsilon$ (triangle inequality); hence $\{y_i\}$ is a finite $\varepsilon$-net for $\overline{S}$. *Second, $\overline{S}$ is complete:* it is a closed subset of the complete space $Y$, and a Cauchy sequence in $\overline{S}$ converges in $Y$ (completeness of $Y$) with limit in $\overline{S}$ (closedness). Being complete and totally bounded, $\overline{S}$ is compact by the three-equivalents theorem.
> >
> > **(a) $\Rightarrow$ (b).** Assume $\overline{S}$ is compact. By the three-equivalents theorem it is totally bounded, and $S \subseteq \overline{S}$, so any finite $\varepsilon$-net of $\overline{S}$ is a finite $\varepsilon$-net of $S$ (each point of $S$ lies in $\overline{S}$, hence within $\varepsilon$ of a net point). Thus $S$ is totally bounded.
> >
> > **(a) $\Rightarrow$ (c).** Assume $\overline{S}$ compact, and let $(s_j)$ be a sequence in $S \subseteq \overline{S}$. By the three-equivalents theorem $\overline{S}$ is sequentially compact, so $(s_j)$ has a subsequence converging to a point of $\overline{S} \subseteq Y$. This is (c).
> >
> > **(c) $\Rightarrow$ (a).** Assume (c); we show $\overline{S}$ is sequentially compact, hence compact by the three-equivalents theorem. Let $(z_j) \subseteq \overline{S}$. For each $j$ pick $s_j \in S$ with $\lVert z_j - s_j\rVert < 1/j$ (definition of closure). By (c) there is a subsequence $s_{j_i} \to w \in Y$; then
> > $$\lVert z_{j_i} - w\rVert \le \lVert z_{j_i} - s_{j_i}\rVert + \lVert s_{j_i} - w\rVert < \tfrac1{j_i} + \lVert s_{j_i} - w\rVert \xrightarrow{\ i\to\infty\ } 0 \qquad \text{(triangle inequality; both terms} \to 0\text{)},$$
> > so $z_{j_i} \to w$, and $w \in \overline{S}$ (limit of points $s_{j_i} \in S$). Hence $\overline{S}$ is sequentially compact.
> >
> > The four directions give (a) $\Leftrightarrow$ (b) and (a) $\Leftrightarrow$ (c), so (a), (b), (c) are equivalent. $\blacksquare$

> [!note]- Lemma 2: Every bounded finite-rank operator is compact
> **Statement:** Let $F \in \mathcal{B}(X,Y)$ have finite rank, $\dim F(X) = r < \infty$. Then $F$ is compact.
>
> **Hint:** $F(B_X)$ is a bounded subset of the finite-dimensional normed space $F(X)$; bounded subsets of finite-dimensional normed spaces are relatively compact.
>
> **Why needed:** It is the base case of part (iv)'s reverse direction and supplies the finite-rank approximants transported across the adjoint in part (v).
>
> > [!note]- Full proof
> > Write $V := F(X)$, a finite-dimensional linear subspace of $Y$ with $\dim V = r$. We use the sequential criterion. Let $(x_j)$ be bounded in $X$, $\lVert x_j\rVert \le M$. Then $Fx_j \in V$ and $\lVert Fx_j\rVert \le \lVert F\rVert\,\lVert x_j\rVert \le \lVert F\rVert M$, so $(Fx_j)$ is a bounded sequence in the finite-dimensional normed space $V$.
> >
> > **Bounded sequences in $V$ have convergent subsequences.** This is the finite-dimensional Bolzano–Weierstrass property, proved in full in the finite-rank example of [[Def - Compact Operator]]: fixing a basis $b_1,\dots,b_r$ of $V$ gives a linear isomorphism $T : \mathbb{F}^r \to V$, $T(a) = \sum_i a_i b_i$, which is bounded and bounded below (there are $0 < c \le C_1$ with $c\lVert a\rVert_2 \le \lVert Ta\rVert \le C_1\lVert a\rVert_2$, the lower bound coming from compactness of the Euclidean unit sphere via [[Thm - Heine–Borel Theorem]]); a bounded sequence $Fx_j = Ta^{(j)}$ then has $\lVert a^{(j)}\rVert_2 \le \lVert Fx_j\rVert / c$ bounded, so $(a^{(j)})$ lies in a Euclidean closed ball, which is compact by [[Thm - Heine–Borel Theorem|Heine–Borel]] and hence sequentially compact by [[Thm - Compactness in Metric Spaces (Three Equivalents)|the three-equivalents theorem]]; a convergent subsequence $a^{(j_i)} \to a^\ast$ gives $Fx_{j_i} = Ta^{(j_i)} \to Ta^\ast \in V$ by continuity of $T$.
> >
> > Thus $(Fx_j)$ has a subsequence converging in $V \subseteq Y$, so $F$ satisfies the sequential criterion and is compact. $\blacksquare$

> [!note]- Lemma 3: Orthogonal projection onto a complete subspace
> **Statement:** Let $H$ be an inner product space and $M \subseteq H$ a linear subspace that is complete in the induced norm. For each $x \in H$ there is a unique $m_0 \in M$ minimising $\lVert x - m\rVert$ over $m \in M$; it is characterised by $x - m_0 \perp M$ (that is, $\langle x - m_0, m\rangle = 0$ for all $m \in M$). The map $P_M : x \mapsto m_0$ is linear with $\lVert P_M x\rVert \le \lVert x\rVert$, and $\lVert x - P_M x\rVert = \inf_{m \in M}\lVert x - m\rVert = \operatorname{dist}(x, M)$.
>
> **Hint:** A minimising sequence is Cauchy by the parallelogram law; completeness of $M$ gives the minimiser. Orthogonality comes from differentiating $t \mapsto \lVert x - m_0 - tm\rVert^2$ at $t = 0$.
>
> **Why needed:** It is the geometric core of the Riesz representation theorem (Lemma 4), which the Hilbert adjoint of part (v) requires; the vault's [[Thm - Best Approximation by Orthogonal Projection]] covers only finite-dimensional subspaces, and Riesz needs the closed hyperplane $\ker\phi$.
>
> > [!note]- Full proof
> > **Parallelogram law.** For all $a, b \in H$, expanding with $\lVert v\rVert^2 = \langle v,v\rangle$ and sesquilinearity,
> > $$\lVert a + b\rVert^2 + \lVert a - b\rVert^2 = \big(\langle a,a\rangle + \langle a,b\rangle + \langle b,a\rangle + \langle b,b\rangle\big) + \big(\langle a,a\rangle - \langle a,b\rangle - \langle b,a\rangle + \langle b,b\rangle\big) = 2\lVert a\rVert^2 + 2\lVert b\rVert^2. \qquad (\ast)$$
> >
> > **Step 1 — existence of the minimiser.** Set $\delta := \inf_{m \in M}\lVert x - m\rVert \ge 0$ and choose $m_n \in M$ with $\lVert x - m_n\rVert^2 \to \delta^2$ (definition of infimum). Apply $(\ast)$ with $a = x - m_n$ and $b = x - m_k$:
> > $$\lVert (x - m_n) + (x - m_k)\rVert^2 + \lVert m_k - m_n\rVert^2 = 2\lVert x - m_n\rVert^2 + 2\lVert x - m_k\rVert^2 \qquad \text{(parallelogram law }(\ast)\text{)}.$$
> > The first term equals $4\big\lVert x - \tfrac{m_n + m_k}{2}\big\rVert^2 \ge 4\delta^2$, since $\tfrac{m_n+m_k}2 \in M$ (a subspace) and $\delta$ is the infimum over $M$. Rearranging,
> > $$\lVert m_k - m_n\rVert^2 = 2\lVert x - m_n\rVert^2 + 2\lVert x - m_k\rVert^2 - 4\Big\lVert x - \tfrac{m_n+m_k}2\Big\rVert^2 \le 2\lVert x - m_n\rVert^2 + 2\lVert x - m_k\rVert^2 - 4\delta^2 \xrightarrow{\ n,k\to\infty\ } 2\delta^2 + 2\delta^2 - 4\delta^2 = 0,$$
> > using $\lVert x - m_n\rVert^2 \to \delta^2$ and $\lVert x - m_k\rVert^2 \to \delta^2$. Hence $(m_n)$ is Cauchy in $M$; as $M$ is complete, $m_n \to m_0 \in M$, and $\lVert x - m_0\rVert = \lim_n\lVert x - m_n\rVert = \delta$ (continuity of the norm). So a minimiser $m_0$ exists.
> >
> > **Step 2 — orthogonality characterises $m_0$.** Suppose $m_0 \in M$ attains $\delta$. Fix $m \in M$ and $\lambda \in \mathbb{F}$. Since $m_0 - \lambda m \in M$,
> > $$\delta^2 \le \lVert x - m_0 + \lambda m\rVert^2 = \lVert x - m_0\rVert^2 + 2\operatorname{Re}\big(\bar\lambda\langle x - m_0, m\rangle\big) + |\lambda|^2\lVert m\rVert^2 = \delta^2 + 2\operatorname{Re}\big(\bar\lambda\langle x - m_0,m\rangle\big) + |\lambda|^2\lVert m\rVert^2,$$
> > so $2\operatorname{Re}\big(\bar\lambda\langle x - m_0, m\rangle\big) + |\lambda|^2\lVert m\rVert^2 \ge 0$ for all $\lambda$. Writing $\langle x - m_0, m\rangle = \rho e^{i\theta}$ and taking $\lambda = t e^{i\theta}$ with $t \in \mathbb{R}$ small, this reads $2t\rho + t^2\lVert m\rVert^2 \ge 0$ for all real $t$; dividing by $t > 0$ and letting $t \downarrow 0$ gives $\rho \ge 0$, while $t < 0$ gives $\rho \le 0$, so $\rho = 0$ and $\langle x - m_0, m\rangle = 0$. Thus $x - m_0 \perp M$. Conversely, if $x - m_0 \perp M$ with $m_0 \in M$, then for any $m \in M$, by the Pythagorean identity (which holds because $x - m_0 \perp m_0 - m \in M$),
> > $$\lVert x - m\rVert^2 = \lVert (x - m_0) + (m_0 - m)\rVert^2 = \lVert x - m_0\rVert^2 + \lVert m_0 - m\rVert^2 \ge \lVert x - m_0\rVert^2,$$
> > so $m_0$ minimises. This also gives **uniqueness**: if $m_0, m_0'$ both minimise then both satisfy the orthogonality condition, and the displayed identity with $m = m_0'$ forces $\lVert m_0 - m_0'\rVert^2 = \lVert x - m_0'\rVert^2 - \lVert x - m_0\rVert^2 = \delta^2 - \delta^2 = 0$, so $m_0 = m_0'$.
> >
> > **Step 3 — linearity and norm bound of $P_M$.** For $x, x' \in H$ and $\lambda \in \mathbb{F}$, the vector $\lambda P_M x + P_M x' \in M$ satisfies $(\lambda x + x') - (\lambda P_M x + P_M x') = \lambda(x - P_M x) + (x' - P_M x') \perp M$ (a linear combination of two vectors orthogonal to $M$); by the orthogonality characterisation of Step 2, this identifies $\lambda P_M x + P_M x'$ as $P_M(\lambda x + x')$. Hence $P_M$ is linear. For the norm bound, $x = P_M x + (x - P_M x)$ with $P_M x \perp (x - P_M x)$, so by Pythagoras $\lVert x\rVert^2 = \lVert P_M x\rVert^2 + \lVert x - P_M x\rVert^2 \ge \lVert P_M x\rVert^2$, giving $\lVert P_M x\rVert \le \lVert x\rVert$. The identity $\lVert x - P_M x\rVert = \operatorname{dist}(x, M)$ is the definition of $m_0$ as the minimiser. $\blacksquare$

> [!note]- Lemma 4: Riesz representation theorem for Hilbert spaces
> **Statement:** Let $H$ be a Hilbert space and $\phi : H \to \mathbb{F}$ a bounded linear functional. Then there is a unique $z \in H$ with $\phi(x) = \langle x, z\rangle$ for all $x \in H$, and $\lVert z\rVert = \lVert \phi\rVert$.
>
> **Hint:** If $\phi = 0$ take $z = 0$. Otherwise $M := \ker\phi$ is a proper closed subspace; a nonzero vector orthogonal to $M$ generates $z$.
>
> **Why needed:** It converts the linear functional $x \mapsto \langle Tx, y\rangle$ into a vector, which is exactly how the Hilbert adjoint $T^*y$ is defined in Lemma 5.
>
> > [!note]- Full proof
> > **Uniqueness.** If $\langle x, z\rangle = \langle x, z'\rangle$ for all $x$, then $\langle x, z - z'\rangle = 0$ for all $x$; taking $x = z - z'$ gives $\lVert z - z'\rVert^2 = 0$, so $z = z'$.
> >
> > **Existence.** If $\phi = 0$, then $z = 0$ works. Assume $\phi \ne 0$. The kernel $M := \ker\phi = \{x : \phi(x) = 0\}$ is a linear subspace, and it is closed because $\phi$ is continuous (the preimage of the closed set $\{0\}$). A closed subset of the complete space $H$ is complete, so Lemma 3 applies to $M$. Since $\phi \ne 0$ there is $x_0 \in H$ with $\phi(x_0) \ne 0$, hence $x_0 \notin M$. Set $u := x_0 - P_M x_0$, where $P_M$ is the projection of Lemma 3. Then $u \perp M$ (Lemma 3), and $u \ne 0$: otherwise $x_0 = P_M x_0 \in M$, contradicting $x_0 \notin M$. Note also $\phi(u) = \phi(x_0) - \phi(P_M x_0) = \phi(x_0) \ne 0$ since $P_M x_0 \in M = \ker\phi$.
> >
> > **Construction of $z$.** Put $z := \dfrac{\overline{\phi(u)}}{\lVert u\rVert^2}\, u$. We verify $\phi(x) = \langle x, z\rangle$ for all $x \in H$. Given $x$, the vector
> > $$w := x - \frac{\phi(x)}{\phi(u)}\, u \quad\text{satisfies}\quad \phi(w) = \phi(x) - \frac{\phi(x)}{\phi(u)}\phi(u) = 0, \qquad \text{so } w \in M = \ker\phi,$$
> > hence $\langle w, u\rangle = 0$ (as $u \perp M$). Therefore
> > $$\langle x, z\rangle = \Big\langle \tfrac{\phi(x)}{\phi(u)} u + w,\ \tfrac{\overline{\phi(u)}}{\lVert u\rVert^2} u\Big\rangle = \frac{\phi(x)}{\phi(u)}\cdot\frac{\phi(u)}{\lVert u\rVert^2}\langle u, u\rangle + \frac{\phi(u)}{\lVert u\rVert^2}\langle w, u\rangle = \phi(x) + 0 = \phi(x),$$
> > where we used $x = \tfrac{\phi(x)}{\phi(u)}u + w$, sesquilinearity (the scalar $\tfrac{\overline{\phi(u)}}{\lVert u\rVert^2}$ in the second slot conjugates to $\tfrac{\phi(u)}{\lVert u\rVert^2}$), $\langle u,u\rangle = \lVert u\rVert^2$, and $\langle w, u\rangle = 0$.
> >
> > **Norm.** By the Cauchy–Schwarz inequality $|\langle x, z\rangle| \le \lVert x\rVert\lVert z\rVert$ (valid in any inner product space: for $z \ne 0$ expand $0 \le \lVert x - \tfrac{\langle x,z\rangle}{\lVert z\rVert^2}z\rVert^2$), so $\lVert\phi\rVert = \sup_{\lVert x\rVert\le 1}|\phi(x)| = \sup_{\lVert x\rVert\le1}|\langle x,z\rangle| \le \lVert z\rVert$. Conversely, if $z \ne 0$ then $\phi(z/\lVert z\rVert) = \langle z/\lVert z\rVert, z\rangle = \lVert z\rVert$, so $\lVert\phi\rVert \ge \lVert z\rVert$; and if $z = 0$ then $\phi = 0$ and $\lVert\phi\rVert = 0 = \lVert z\rVert$. Hence $\lVert\phi\rVert = \lVert z\rVert$. $\blacksquare$

> [!note]- Lemma 5: Existence and properties of the Hilbert adjoint
> **Statement:** Let $H_1, H_2$ be Hilbert spaces and $T \in \mathcal{B}(H_1,H_2)$. There is a unique operator $T^* \in \mathcal{B}(H_2,H_1)$ with $\langle Tx, y\rangle_{H_2} = \langle x, T^*y\rangle_{H_1}$ for all $x \in H_1$, $y \in H_2$. Moreover: $T^*$ is linear; $\lVert T^*\rVert = \lVert T\rVert$; $T^{**} = T$; $(ST)^* = T^*S^*$ for $S \in \mathcal{B}(H_2,H_3)$; and if $T$ has finite rank then so does $T^*$.
>
> **Hint:** For fixed $y$, $x \mapsto \langle Tx,y\rangle$ is a bounded functional; its Riesz vector (Lemma 4) is $T^*y$. Finite rank: a finite-rank operator is $\sum_i\langle\cdot,a_i\rangle b_i$, whose adjoint is $\sum_i\langle\cdot,b_i\rangle a_i$.
>
> **Why needed:** Part (v) is a statement about $K^*$; without existence and the isometry $\lVert T^*\rVert = \lVert T\rVert$ and finite-rank preservation, it cannot be proved.
>
> > [!note]- Full proof
> > **Existence and uniqueness.** Fix $y \in H_2$ and define $\phi_y : H_1 \to \mathbb{F}$ by $\phi_y(x) := \langle Tx, y\rangle_{H_2}$. It is linear in $x$ (as $T$ is linear and $\langle\cdot,\cdot\rangle$ is linear in its first slot) and bounded: $|\phi_y(x)| \le \lVert Tx\rVert\lVert y\rVert \le \lVert T\rVert\lVert y\rVert\lVert x\rVert$ (Cauchy–Schwarz, then boundedness of $T$), so $\lVert\phi_y\rVert \le \lVert T\rVert\lVert y\rVert$. By the Riesz representation theorem (Lemma 4) there is a unique $w \in H_1$ with $\phi_y(x) = \langle x, w\rangle_{H_1}$ for all $x$; define $T^*y := w$. This gives $\langle Tx,y\rangle = \langle x, T^*y\rangle$ for all $x,y$, and any operator satisfying this identity must send $y$ to the Riesz vector of $\phi_y$, which is unique — so $T^*$ is unique.
> >
> > **Linearity of $T^*$.** For $y, y' \in H_2$, $\lambda \in \mathbb{F}$ and all $x$,
> > $$\langle x, T^*(\lambda y + y')\rangle = \langle Tx, \lambda y + y'\rangle = \bar\lambda\langle Tx, y\rangle + \langle Tx, y'\rangle = \bar\lambda\langle x, T^*y\rangle + \langle x, T^*y'\rangle = \langle x, \lambda T^*y + T^*y'\rangle,$$
> > using conjugate-linearity in the second slot. As this holds for all $x$, $T^*(\lambda y + y') = \lambda T^*y + T^*y'$ (subtract and take $x$ equal to the difference).
> >
> > **Boundedness and isometry.** For $y \in H_2$, applying the defining identity with $x = T^*y$,
> > $$\lVert T^*y\rVert^2 = \langle T^*y, T^*y\rangle = \langle T(T^*y), y\rangle \le \lVert T(T^*y)\rVert\lVert y\rVert \le \lVert T\rVert\lVert T^*y\rVert\lVert y\rVert \qquad \text{(defining identity; Cauchy–Schwarz; boundedness of }T\text{)}.$$
> > If $T^*y \ne 0$, divide by $\lVert T^*y\rVert$ to get $\lVert T^*y\rVert \le \lVert T\rVert\lVert y\rVert$ (and this is trivial if $T^*y = 0$), so $T^* \in \mathcal{B}(H_2,H_1)$ with $\lVert T^*\rVert \le \lVert T\rVert$. **The identity $T^{**} = T$:** the operator $T^*$ has an adjoint $T^{**} \in \mathcal{B}(H_1,H_2)$ by the existence just proved, and for all $x,y$,
> > $$\langle y, T^{**}x\rangle_{H_2} = \langle T^*y, x\rangle_{H_1} = \overline{\langle x, T^*y\rangle_{H_1}} = \overline{\langle Tx, y\rangle_{H_2}} = \langle y, Tx\rangle_{H_2} \qquad \text{(defining identity of }T^{**}\text{; conjugate symmetry; defining identity of }T^*\text{)},$$
> > so $T^{**}x = Tx$ for all $x$, i.e. $T^{**} = T$. Applying $\lVert(\cdot)^*\rVert \le \lVert\cdot\rVert$ to $T^*$ gives $\lVert T\rVert = \lVert T^{**}\rVert \le \lVert T^*\rVert$, and combined with $\lVert T^*\rVert \le \lVert T\rVert$ this yields $\lVert T^*\rVert = \lVert T\rVert$.
> >
> > **Composition.** For $S \in \mathcal{B}(H_2,H_3)$, $T \in \mathcal{B}(H_1,H_2)$ and all $x \in H_1$, $z \in H_3$,
> > $$\langle x, (ST)^*z\rangle = \langle STx, z\rangle = \langle Tx, S^*z\rangle = \langle x, T^*S^*z\rangle \qquad \text{(defining identities of }(ST)^*, S^*, T^*\text{)},$$
> > so $(ST)^* = T^*S^*$.
> >
> > **Finite rank is preserved.** Suppose $T$ has finite rank, $\dim T(H_1) = r$, with basis $b_1,\dots,b_r$ of $T(H_1)$. Writing $Tx$ in this basis defines coordinate functionals $\psi_i : H_1 \to \mathbb{F}$ by $Tx = \sum_{i=1}^r \psi_i(x) b_i$; each $\psi_i$ is linear, and bounded because it is the composite of the bounded $T$ with the $i$-th coordinate map on the finite-dimensional space $T(H_1)$, which is bounded (the norm-equivalence on a finite-dimensional space established in [[Def - Compact Operator]] makes every coordinate functional continuous). By the Riesz representation theorem (Lemma 4), $\psi_i(x) = \langle x, a_i\rangle_{H_1}$ for some $a_i \in H_1$, so
> > $$Tx = \sum_{i=1}^r \langle x, a_i\rangle_{H_1}\, b_i.$$
> > Then for all $x \in H_1$, $y \in H_2$,
> > $$\langle Tx, y\rangle_{H_2} = \sum_{i=1}^r \langle x, a_i\rangle_{H_1}\langle b_i, y\rangle_{H_2} = \Big\langle x,\ \sum_{i=1}^r \langle y, b_i\rangle_{H_2}\, a_i\Big\rangle_{H_1} \qquad \text{(pull the scalars } \langle b_i,y\rangle = \overline{\langle y,b_i\rangle} \text{ into the second slot)},$$
> > so $T^*y = \sum_{i=1}^r \langle y, b_i\rangle_{H_2}\, a_i$. Hence $T^*(H_2) \subseteq \operatorname{span}\{a_1,\dots,a_r\}$ is finite-dimensional, and $T^*$ has finite rank. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Throughout, "compact" for a bounded operator means the image of the closed unit ball is relatively compact, equivalently (Lemma 1, applied in the complete codomain) totally bounded, equivalently the sequential criterion holds. We prove the parts in the order (iii), (ii), (i), (iv), (v), so that (iii) is available to (i) and (i), (iv) to (v).
>
> ---
>
> **Part (iii) — the sum of two compact operators is compact.** Let $K_1, K_2 \in \mathcal{K}(X,Y)$ and let $(x_j)$ be a bounded sequence in $X$; we produce a subsequence on which $(K_1 + K_2)x_j$ converges. Since $K_1$ is compact, by the sequential criterion there is a subsequence $(x_{j})_{j \in J_1}$ (an infinite index set $J_1$) with $K_1 x_j \to u$ along $J_1$. The subsequence $(x_j)_{j \in J_1}$ is still bounded, so since $K_2$ is compact there is a further infinite subset $J_2 \subseteq J_1$ with $K_2 x_j \to v$ along $J_2$. Along $J_2$: $K_1 x_j \to u$ (a subsequence of a convergent sequence has the same limit) and $K_2 x_j \to v$, so
> $$(K_1 + K_2)x_j = K_1 x_j + K_2 x_j \longrightarrow u + v \qquad \text{(sum of two convergent sequences; } J_2 \text{)}.$$
> Thus $(K_1 + K_2)$ satisfies the sequential criterion and is compact. The same argument with a single operator shows that for $\lambda \in \mathbb{F}$ and $K$ compact, $\lambda K$ is compact ($Kx_{j_i} \to u \Rightarrow \lambda K x_{j_i} \to \lambda u$), and the zero operator is compact ($\overline{0(B_X)} = \{0\}$ is compact). Therefore $\mathcal{K}(X,Y)$ contains $0$ and is closed under scalar multiplication and, by the above, under addition: it is a linear subspace of $\mathcal{B}(X,Y)$.
>
> ---
>
> **Part (ii) — the ideal property.** Let $A \in \mathcal{B}(W,X)$, $K \in \mathcal{K}(X,Y)$, $B \in \mathcal{B}(Y,Z)$; we show $BKA$ is compact via the sequential criterion. Let $(w_j)$ be bounded in $W$, $\lVert w_j\rVert \le M$. Then $(Aw_j)$ is bounded in $X$, since $\lVert Aw_j\rVert \le \lVert A\rVert\lVert w_j\rVert \le \lVert A\rVert M$ (boundedness of $A$). Because $K$ is compact, the sequential criterion gives an infinite subset $J$ with $KAw_j \to \eta$ along $J$ for some $\eta \in Y$. Applying the continuous (because bounded) operator $B$,
> $$BKAw_j = B(KAw_j) \longrightarrow B\eta \qquad \text{(continuity of } B \text{; } J \text{)}.$$
> Hence $(BKAw_j)$ converges along $J$, so $BKA$ satisfies the sequential criterion and is compact. Taking $W = Y = Z = X$ shows that for $K \in \mathcal{K}(X)$ and any $B, A \in \mathcal{B}(X)$ both $BK$ (take $A = \mathrm{Id}$) and $KA$ (take $B = \mathrm{Id}$) are compact, so $\mathcal{K}(X)$ is a two-sided ideal of $\mathcal{B}(X)$.
>
> ---
>
> **Part (i) — $\mathcal{K}(X,Y)$ is norm-closed.** That it is a linear subspace was shown in Part (iii). It remains to prove closedness. Let $(K_n) \subseteq \mathcal{K}(X,Y)$ with $\lVert K_n - K\rVert \to 0$, $K \in \mathcal{B}(X,Y)$; we show $K(B_X)$ is totally bounded, whence $K$ is compact by Lemma 1 (the codomain $Y$ is complete). Fix $\varepsilon > 0$.
>
> **Choose a close approximant.** Pick $n$ with $\lVert K - K_n\rVert < \varepsilon/3$ (norm convergence).
>
> **Take a net for the approximant.** Since $K_n$ is compact, $K_n(B_X)$ is totally bounded (Lemma 1), so there is a finite $(\varepsilon/3)$-net $\{y_1,\dots,y_N\} \subseteq Y$ with: for every $x \in B_X$, some $i$ has $\lVert K_n x - y_i\rVert < \varepsilon/3$.
>
> **Transfer the net to $K$.** Let $x \in B_X$ and choose $i$ as above. Then
> $$\lVert Kx - y_i\rVert \le \lVert Kx - K_n x\rVert + \lVert K_n x - y_i\rVert \le \lVert K - K_n\rVert\lVert x\rVert + \lVert K_n x - y_i\rVert < \tfrac{\varepsilon}{3}\cdot 1 + \tfrac{\varepsilon}{3} = \tfrac{2\varepsilon}{3} < \varepsilon,$$
> using the triangle inequality, $\lVert Kx - K_n x\rVert \le \lVert K - K_n\rVert\lVert x\rVert$ with $\lVert x\rVert \le 1$, and the choice of $n$ and $i$. Thus $\{y_1,\dots,y_N\}$ is a finite $\varepsilon$-net for $K(B_X)$. As $\varepsilon > 0$ was arbitrary, $K(B_X)$ is totally bounded, so $K$ is compact by Lemma 1. Therefore $\mathcal{K}(X,Y)$ is closed in $\mathcal{B}(X,Y)$.
>
> ---
>
> **Part (iv) — finite-rank approximation in the Hilbert case.** Let $H_1, H_2$ be Hilbert spaces and $K \in \mathcal{B}(H_1,H_2)$.
>
> **Direction ($\Leftarrow$): a norm-limit of finite-rank operators is compact.** Suppose finite-rank $F_n$ satisfy $\lVert K - F_n\rVert \to 0$. Each $F_n$ is compact by Lemma 2, and $\mathcal{K}(H_1,H_2)$ is norm-closed by Part (i); a norm-limit of compact operators is therefore compact, so $K$ is compact. (This direction uses only that $H_1, H_2$ are Banach.)
>
> **Direction ($\Rightarrow$): a compact operator is a norm-limit of finite-rank operators.** Suppose $K$ is compact and fix $\varepsilon > 0$; we build a finite-rank $F$ with $\lVert K - F\rVert \le \varepsilon$. Since $K(B_{H_1})$ is totally bounded (Lemma 1), there is a finite $\varepsilon$-net $\{y_1,\dots,y_N\} \subseteq H_2$: for every $x \in B_{H_1}$ some $i$ has $\lVert Kx - y_i\rVert < \varepsilon$. Let
> $$V := \operatorname{span}\{y_1,\dots,y_N\} \subseteq H_2, \qquad \dim V \le N < \infty,$$
> and let $P : H_2 \to H_2$ be the orthogonal projection onto the finite-dimensional (hence complete) subspace $V$; $P$ exists and $Pv = v$ for $v \in V$, and for any $w \in H_2$ the vector $Pw$ is the best approximation to $w$ in $V$, by the following, restated at its point of use.
> > **Theorem (best approximation by orthogonal projection).** Let $V$ be a finite-dimensional subspace of an inner product space, and $P$ the orthogonal projection onto $V$. Then for every $w$, $\lVert w - Pw\rVert = \min_{v \in V}\lVert w - v\rVert = \operatorname{dist}(w, V)$. See [[Thm - Best Approximation by Orthogonal Projection]].
>
> Set $F := PK$. Its range lies in $V$, so $F$ has finite rank ($\operatorname{rank} F \le \dim V \le N$); it is bounded as a composite of bounded operators. For $x \in B_{H_1}$, choose $i$ with $\lVert Kx - y_i\rVert < \varepsilon$; since $y_i \in V$,
> $$\lVert Kx - Fx\rVert = \lVert Kx - P(Kx)\rVert = \operatorname{dist}(Kx, V) \le \lVert Kx - y_i\rVert < \varepsilon \qquad \text{(best-approximation theorem; } y_i \in V\text{)}.$$
> As this holds for every $x \in B_{H_1}$, $\lVert K - F\rVert = \sup_{x \in B_{H_1}}\lVert Kx - Fx\rVert \le \varepsilon$. Applying this with $\varepsilon = 1/n$ produces finite-rank operators $F_n$ with $\lVert K - F_n\rVert \le 1/n \to 0$. Hence $K$ is an operator-norm limit of finite-rank operators. The two directions together identify $\mathcal{K}(H_1,H_2)$ with the norm-closure of the finite-rank operators.
>
> ---
>
> **Part (v) — the adjoint of a compact operator is compact.** Let $K \in \mathcal{K}(H_1,H_2)$; by Lemma 5 its adjoint $K^* \in \mathcal{B}(H_2,H_1)$ exists. By Part (iv), applied to the compact $K$, there are finite-rank operators $F_n \in \mathcal{B}(H_1,H_2)$ with $\lVert K - F_n\rVert \to 0$. By Lemma 5 each adjoint $F_n^*$ is finite-rank, and adjunction is linear with $\lVert(\cdot)^*\rVert = \lVert\cdot\rVert$, so
> $$\lVert K^* - F_n^*\rVert = \lVert (K - F_n)^*\rVert = \lVert K - F_n\rVert \longrightarrow 0 \qquad \text{(Lemma 5: } (K - F_n)^* = K^* - F_n^*, \text{ and } \lVert T^*\rVert = \lVert T\rVert\text{)}.$$
> Thus $K^*$ is an operator-norm limit of the finite-rank operators $F_n^*$; the codomain $H_1$ and domain $H_2$ are Hilbert, so by Part (iv), direction ($\Leftarrow$), $K^*$ is compact. Therefore $K^* \in \mathcal{K}(H_2,H_1)$.
>
> ---
>
> All five parts are established. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Integral operators and the Fredholm alternative.** Consider the integral operator $(Ku)(s) = \int_0^1 k(s,t)u(t)\,dt$ on $L^2([0,1])$ with a continuous kernel $k$. Approximating $k$ uniformly by polynomials (or by a finite double Fourier sum) gives finite-rank operators $K_n$ with $\lVert K - K_n\rVert \to 0$, so $K$ is compact by parts (i) and (iv). The theorem then makes the classical Fredholm alternative for $u - Ku = f$ available through [[Thm - Riesz-Schauder Theory for Compact Perturbations of the Identity]]. The application is non-obvious because the compactness is not visible in the integral formula; it is manufactured by the uniform approximation of the kernel, and the ideal and closedness properties are what let one pass from the approximants to $K$.

**Elliptic regularity as a compact-resolvent statement.** On a closed Riemannian manifold, the resolvent $(\Delta + 1)^{-1}$ of the Hodge Laplacian factors as $L^2 \to H_2 \hookrightarrow L^2$, where the first arrow is bounded (elliptic estimate) and the inclusion $H_2 \hookrightarrow L^2$ is the compact Rellich operator ([[Thm - Rellich Compactness Theorem]]). By the ideal property (ii), $(\Delta + 1)^{-1}$ is compact; being also self-adjoint, it is diagonalisable, which is the analytic heart of the Hodge theorem. The theorem applies because the compact factor sits in the middle of a bounded sandwich, exactly the situation (ii) governs; the non-obvious point is recognising the resolvent as such a factorisation.

**Hilbert–Schmidt operators on a sequence space.** An operator $K$ on $\ell^2$ with matrix $(k_{ij})$ satisfying $\sum_{i,j}|k_{ij}|^2 < \infty$ is compact: truncating to the top-left $N \times N$ block gives finite-rank $K_N$ with $\lVert K - K_N\rVert^2 \le \sum_{(i,j)\notin[N]^2}|k_{ij}|^2 \to 0$, so parts (i) and (iv) apply. Its adjoint has matrix $(\overline{k_{ji}})$, again Hilbert–Schmidt, consistent with part (v). This is a good drill on (iv) and (v) simultaneously, and it is non-obvious because the square-summability of the matrix, not any property of individual columns, is what forces the norm approximation.

---

# Bridges

- **The finite-rank operators and the approximation property.** Parts (i), (iii), and Lemma 2 together say that $\mathcal{K}(H_1,H_2)$ is exactly the operator-norm closure of the space of finite-rank operators between the two Hilbert spaces. This is the *approximation property* of Hilbert spaces; it fails for general Banach spaces (Enflo's counterexample), so the clean characterisation (iv) is a genuinely Hilbert-space phenomenon. The bridge is the orthogonal projection onto the span of a finite net, which is available precisely because a Hilbert space has orthogonal projections onto its finite-dimensional (indeed all its closed) subspaces.

- **The operator ideal and the Calkin algebra.** Part (ii) makes $\mathcal{K}(X)$ a closed two-sided ideal of the Banach algebra $\mathcal{B}(X)$, so the quotient $\mathcal{B}(X)/\mathcal{K}(X)$ — the Calkin algebra — is itself a Banach algebra. An operator is Fredholm exactly when its image in the Calkin algebra is invertible; this is the abstract source of the stability of the Fredholm property under compact perturbations proved on [[Thm - Stability of the Fredholm Property under Small and Compact Perturbations]]. The bridge from this page is that closedness (i) is what makes the quotient a Banach space and the ideal property (ii) what makes it an algebra.

- **The Rellich theorem as the one compact operator that matters here.** Everything analytic in chapters IX–XI runs on a single compact operator: the Sobolev inclusion $H_k(M;E) \hookrightarrow H_m(M;E)$ for $k > m$, proved compact on [[Thm - Rellich Compactness Theorem]]. The present theorem is what lets that one operator propagate: composed with bounded localisation, extension, and multiplication maps it stays compact (ii); assembled from Fourier truncations it is a norm-limit of finite-rank operators (i), (iv); and its role in the Fredholm alternative uses that adjoints of compacts are compact (v).

- **The spectral theorem for compact self-adjoint operators.** Combining part (v) with self-adjointness ($K = K^*$) puts one in the setting of the spectral theorem: a compact self-adjoint operator has an orthonormal eigenbasis with eigenvalues accumulating only at $0$. The bridge is that compactness forces the eigenvalues off any annulus $\{|\lambda| \ge \delta\}$ to be finite in number (else an orthonormal sequence of eigenvectors would have a non-Cauchy image, contradicting compactness), and self-adjointness supplies the orthogonality; this is the mechanism behind the finite-dimensionality of harmonic spaces on [[Thm - Hodge Theorem for Elliptic Complexes]].

---

# Unlocked by This

> [!tip] The Fredholm Property of Elliptic Operators *(from this chapter)*
> The ideal property (ii) composes the compact Rellich inclusion with the elliptic estimate to force the kernel of an elliptic operator to be finite-dimensional and its range closed, so that elliptic operators on closed manifolds are Fredholm. See [[Thm - Elliptic Operators on Closed Manifolds are Fredholm]].

> [!tip] Riesz–Schauder Theory *(from this chapter)*
> For $K$ compact, $\mathrm{Id} + K$ is Fredholm of index zero; the finite-rank approximation (iv) reduces the analysis of $\mathrm{Id}+K$ to finite-dimensional linear algebra plus a small remainder. See [[Thm - Riesz-Schauder Theory for Compact Perturbations of the Identity]].

> [!tip] The Fredholm Alternative for Elliptic Operators *(from this chapter)*
> The adjoint property (v) is what lets the solvability of $Ls = t$ be tested against $\ker L^*$: the cokernel of a Fredholm elliptic operator is identified with the kernel of its adjoint, both finite-dimensional. See [[Thm - Fredholm Alternative for Elliptic Operators]].
