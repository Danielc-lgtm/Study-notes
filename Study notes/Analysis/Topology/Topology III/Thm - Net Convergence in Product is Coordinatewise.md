---
type: theorem
subject: topology
prereqs:
  - "Def - Product Topology"
  - "Def - Directed Set and Net"
  - "Def - Net Convergence"
  - "Thm - Continuity via Nets"
tags: [analysis, topology]
---

# Notation

$\{X_\alpha\}_{\alpha \in A}$ is a family of topological spaces, $\prod_\alpha X_\alpha$ their product with the product topology. A net in the product is $\{x^{(\beta)}\}_{\beta \in D}$ where each $x^{(\beta)} = (x_\alpha^{(\beta)})_{\alpha \in A}$. The projection is $\pi_\alpha(x^{(\beta)}) = x_\alpha^{(\beta)}$. The full registry is on [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact]].

---

# Statement

> **Net Convergence in Product is Coordinatewise.** A net $\{x^{(\beta)}\}_{\beta \in D}$ in $\prod_\alpha X_\alpha$ converges to $x = (x_\alpha) \in \prod_\alpha X_\alpha$ in the product topology if and only if for every coordinate $\alpha \in A$, the projected net $\{x_\alpha^{(\beta)}\}_{\beta \in D}$ converges to $x_\alpha$ in $X_\alpha$.
>
> **Specialization to function spaces.** When $X^A = \prod_{a \in A} X$ is the space of functions $A \to X$ with the product topology, a net $\{f_\beta\}$ converges to $f$ in $X^A$ if and only if $f_\beta(a) \to f(a)$ in $X$ for every $a \in A$. The product topology on $X^A$ is therefore the **topology of pointwise convergence**.

---

# Motivation

The product topology was defined to make the projections continuous in the coarsest way. The natural question is: what does *convergence* look like in this topology? The answer should reflect the definition — since the projections are continuous, a net that converges in the product must project to convergent nets in each coordinate. The remarkable thing is that the converse also holds: pointwise convergence in each coordinate is *sufficient* for convergence in the product topology.

This is the defining characterization of the product topology. It is the reason the product topology is the *right* one: it is exactly the topology of pointwise convergence on function spaces $X^A$, which is the most natural notion of convergence for sequences or nets of functions when no stronger structure is assumed.

Two important remarks. First, the theorem fails for the **box topology**: a sequence converging coordinatewise need not converge in the box topology, as the standard counterexample $x^{(k)}_n = 1/k$ for all $n$ shows (converges to $0$ pointwise, but not in the box topology). The product topology is uniquely the one matching pointwise convergence.

Second, the theorem requires *nets*, not just sequences, in the infinite-product case. For uncountable products, sequential convergence is strictly weaker than topological convergence: even in $\mathbb{R}^\mathbb{R}$ (continuum many copies of $\mathbb{R}$), the topology of pointwise convergence is not first countable, so sequences are insufficient to characterize convergence. Nets are necessary.

Third, the theorem extends to **filter convergence** and **ultrafilter convergence** in obvious ways. A filter $\mathcal{F}$ on $\prod_\alpha X_\alpha$ converges to $x$ if and only if each pushforward $\pi_\alpha(\mathcal{F})$ converges to $x_\alpha$ in $X_\alpha$. This is the form used in some proofs of Tychonoff (the ultrafilter approach).

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "a net in a product space and a candidate limit". The skill is recognizing when one is dealing with such a structure, possibly in disguise.

The first source is **a sequence of functions and a candidate limit function**. Property $B$: a sequence $\{f_n\}$ of functions $A \to X$ converging pointwise to $f$. The bridge: view $\{f_n\}$ as a sequence in the product $X^A$ with the product topology; pointwise convergence is *exactly* product-topology convergence. *Example:* in measure theory and analysis, "pointwise convergence" is the dominant notion of convergence for general (not necessarily $L^p$) function sequences, and the relevant topology is exactly the product topology.

The second source is **a net of measures viewed as evaluation functionals**. Property $B$: a net of finite measures $\mu_\beta$ on a space $X$, treated as elements of $\mathbb{R}^{C(X)}$ via $\mu_\beta(f) = \int f\, d\mu_\beta$. The bridge: convergence of $\mu_\beta \to \mu$ pointwise on $C(X)$ — i.e., $\int f\, d\mu_\beta \to \int f\, d\mu$ for every $f$ — is convergence in the product topology on $\mathbb{R}^{C(X)}$. *Example:* this is exactly the notion of **weak-$*$ convergence** in the dual of $C(X)$, and it is the topology in which Banach–Alaoglu compactness lives.

The third source is **a net of operators on a Banach space**. Property $B$: a net of bounded linear operators $T_\beta : V \to W$, with $T_\beta(v) \to T(v)$ for every $v \in V$. The bridge: this is the **strong operator topology**, which is the product topology on $W^V$ restricted to $\mathcal{B}(V, W)$. *Example:* a sequence of finite-rank projections approximating a compact operator converges in SOT exactly because it converges pointwise.

**Targets (Output Amplification)**

The conclusion is "$\{x^{(\beta)}\}$ converges to $x$ in the product topology iff coordinatewise".

Combine the conclusion with **the continuity of a function defined coordinatewise.** Property $D$: a function $f : Z \to \prod_\alpha X_\alpha$ given by $f(z) = (f_\alpha(z))_\alpha$ with each $f_\alpha : Z \to X_\alpha$ continuous. The amplified result $E$: $f$ is continuous as a map into the product. The combination is the universal property of the product, derived from the net characterization: by [[Thm - Continuity via Nets]], it suffices to check that $z_\beta \to z$ implies $f(z_\beta) \to f(z)$, which by the present theorem reduces to $f_\alpha(z_\beta) \to f_\alpha(z)$ for each $\alpha$, true by continuity of $f_\alpha$.

Combine the conclusion with **the universality of nets in the Tychonoff proof.** Property $D$: a universal net in $\prod_\alpha X_\alpha$. The amplified result $E$: the projection to each coordinate is a universal net in $X_\alpha$, which converges in compact spaces. This is the engine of [[Thm - Tychonoff Theorem]].

Combine the conclusion with **the closedness of a graph.** Property $D$: a subset $G \subseteq X \times Y$ defined by equations involving only one coordinate at a time, e.g., the graph of a function. The amplified result $E$: $G$ is closed in $X \times Y$ when the defining conditions are preserved under pointwise limits. The combination is the standard way to verify closedness in product spaces.

---

# Why Is It True

The intuition is just to unfold the definitions.

The product topology has subbasis $\{\pi_\alpha^{-1}(U_\alpha) : \alpha \in A, U_\alpha \subseteq X_\alpha \text{ open}\}$, equivalently a basis of finite intersections — sets of the form $\prod V_\alpha$ where $V_\alpha = X_\alpha$ for all but finitely many $\alpha$. A net $\{x^{(\beta)}\}$ converges to $x$ in this topology if and only if it is eventually in every neighborhood of $x$.

**$(\Rightarrow)$** If $\{x^{(\beta)}\} \to x$ in the product, then in particular it is eventually in every subbasic neighborhood $\pi_\alpha^{-1}(U_\alpha)$ of $x$ — but $x^{(\beta)} \in \pi_\alpha^{-1}(U_\alpha)$ means $x_\alpha^{(\beta)} \in U_\alpha$, so $\{x_\alpha^{(\beta)}\}$ is eventually in every neighborhood $U_\alpha$ of $x_\alpha$, i.e., $x_\alpha^{(\beta)} \to x_\alpha$. (This direction is equivalently: projection $\pi_\alpha$ is continuous, and continuity preserves net convergence.)

**$(\Leftarrow)$** Suppose $x_\alpha^{(\beta)} \to x_\alpha$ for every $\alpha$. To show convergence in the product, take a basic open neighborhood of $x$: it has the form $V = \prod V_\alpha$ where $V_\alpha = X_\alpha$ for all but a finite set $F \subseteq A$, and $V_\alpha$ is an open neighborhood of $x_\alpha$ for $\alpha \in F$. For each $\alpha \in F$, there is $\beta_\alpha$ such that $x_\alpha^{(\beta)} \in V_\alpha$ for $\beta \geq \beta_\alpha$. Since $D$ is directed, there is $\beta^*$ with $\beta^* \geq \beta_\alpha$ for all $\alpha \in F$ (a *finite* family, so directedness suffices). Then for $\beta \geq \beta^*$, $x_\alpha^{(\beta)} \in V_\alpha$ for all $\alpha \in F$, and $x_\alpha^{(\beta)} \in X_\alpha = V_\alpha$ trivially for $\alpha \notin F$ — so $x^{(\beta)} \in V$. Hence the net is eventually in every basic open neighborhood of $x$, hence eventually in every open neighborhood, hence converges to $x$ in the product.

The reason this argument works is that **basic opens in the product restrict only finitely many coordinates**. If they restricted infinitely many (as in the box topology), the directedness argument would fail — we cannot find a common $\beta^*$ majorizing infinitely many $\beta_\alpha$. This is the precise topological reason the product topology, not the box topology, matches pointwise convergence.

---

# What Makes This Hard

The non-obvious step in the $(\Leftarrow)$ direction is recognizing that **basic open sets in the product topology only constrain finitely many coordinates**, so the directedness of $D$ (which gives a common upper bound for finitely many $\beta_\alpha$) suffices. The most common error is to attempt the same argument in the box topology, where basic opens constrain *all* coordinates, and the same directedness argument fails because you would need a common $\beta^*$ majorizing infinitely many $\beta_\alpha$ — which directedness does not generally provide. Another common slip is conflating "coordinatewise convergent" with "convergent in box topology", forgetting that the latter is strictly stronger on infinite products.

---

# Rederivation Scaffold

**High-level strategy:**
Two directions, each direct. $(\Rightarrow)$ follows from continuity of projections. $(\Leftarrow)$ follows from the fact that basic open sets in the product restrict only finitely many coordinates, so a common $\beta^*$ majorizing finitely many $\beta_\alpha$ exists by directedness.

**Subgoal decomposition:**

1. **Forward direction: projections preserve convergence.** Show $x^{(\beta)} \to x \implies x_\alpha^{(\beta)} \to x_\alpha$ for each $\alpha$.
   - *Hint:* $\pi_\alpha$ is continuous; continuity preserves net convergence.
   - *Why needed:* This direction is essentially trivial but worth stating.

2. **Backward direction: identify basic opens.** Recall that basic open sets in the product topology have the form $\prod V_\alpha$ with $V_\alpha = X_\alpha$ for all but finitely many $\alpha$.
   - *Hint:* This is the *definition* of the product topology and is the key step.
   - *Why needed:* The finiteness of constrained coordinates is what makes directedness applicable.

3. **Backward direction: combine via directedness.** For each constrained coordinate $\alpha \in F$ (finite set), find $\beta_\alpha$ such that $x_\alpha^{(\beta)} \in V_\alpha$ for $\beta \geq \beta_\alpha$; take a common upper bound $\beta^* \geq \beta_\alpha$ for all $\alpha \in F$.
   - *Hint:* Directedness gives upper bounds for finite sets.
   - *Why needed:* Produces the witness $\beta^*$ for convergence in the product.

---

# Lemma Decomposition

> [!note]- Lemma 1: Continuity preserves net convergence
> **Statement:** If $f : X \to Y$ is continuous and $\{x_\beta\}$ converges to $x$ in $X$, then $\{f(x_\beta)\}$ converges to $f(x)$ in $Y$.
>
> **Hint:** This is the net version of continuity ([[Thm - Continuity via Nets]]).
>
> **Why needed:** Forward direction of the main theorem.
>
> > [!note]- Full proof
> > Let $V$ be an open neighborhood of $f(x)$ in $Y$. By continuity, $f^{-1}(V)$ is an open neighborhood of $x$ in $X$. Since $x_\beta \to x$, $\{x_\beta\}$ is eventually in $f^{-1}(V)$, so $\{f(x_\beta)\}$ is eventually in $V$. Hence $f(x_\beta) \to f(x)$.

> [!note]- Lemma 2: Basic opens in the product topology constrain finitely many coordinates
> **Statement:** A basic open subset of $\prod_\alpha X_\alpha$ in the product topology has the form $\prod_\alpha V_\alpha$ where each $V_\alpha \subseteq X_\alpha$ is open and $V_\alpha = X_\alpha$ for all but finitely many $\alpha$.
>
> **Hint:** Direct from the definition of the product topology (cylinders as subbasis, finite intersections as basis).
>
> **Why needed:** Backward direction — gives the finite cardinality needed for directedness.
>
> > [!note]- Full proof
> > The subbasis of the product topology is $\{\pi_\alpha^{-1}(U_\alpha) : \alpha \in A, U_\alpha \subseteq X_\alpha \text{ open}\}$. A basic open is a finite intersection of subbasis elements: $\pi_{\alpha_1}^{-1}(U_{\alpha_1}) \cap \cdots \cap \pi_{\alpha_k}^{-1}(U_{\alpha_k}) = \prod_\alpha V_\alpha$ where $V_{\alpha_i} = U_{\alpha_i}$ and $V_\alpha = X_\alpha$ for $\alpha \notin \{\alpha_1, \dots, \alpha_k\}$.

---

# Formal Proof

> [!note]- Complete formal proof
> $(\Rightarrow)$ Suppose $\{x^{(\beta)}\} \to x$ in the product topology. For each $\alpha$, $\pi_\alpha$ is continuous (as $\pi_\alpha^{-1}(U) = \pi_\alpha^{-1}(U)$ is a subbasis element, hence open). By Lemma 1, $\pi_\alpha(x^{(\beta)}) = x_\alpha^{(\beta)} \to \pi_\alpha(x) = x_\alpha$ in $X_\alpha$.
>
> $(\Leftarrow)$ Suppose $x_\alpha^{(\beta)} \to x_\alpha$ in $X_\alpha$ for every $\alpha \in A$. Let $V$ be an open neighborhood of $x$ in the product topology. We show that $\{x^{(\beta)}\}$ is eventually in $V$.
>
> Take a basic open neighborhood $V_0$ of $x$ with $V_0 \subseteq V$. By Lemma 2, $V_0 = \prod_\alpha V_\alpha$ where each $V_\alpha$ is open in $X_\alpha$, $V_\alpha = X_\alpha$ for $\alpha \notin F$ (a finite subset of $A$), and $x_\alpha \in V_\alpha$ for $\alpha \in F$.
>
> For each $\alpha \in F$, since $x_\alpha^{(\beta)} \to x_\alpha$ and $V_\alpha$ is an open neighborhood of $x_\alpha$, there exists $\beta_\alpha \in D$ such that $x_\alpha^{(\beta)} \in V_\alpha$ for all $\beta \geq \beta_\alpha$.
>
> Since $F$ is finite and $D$ is directed, there exists $\beta^* \in D$ with $\beta^* \geq \beta_\alpha$ for all $\alpha \in F$. (Directedness: any finite subset of a directed set has an upper bound.)
>
> For $\beta \geq \beta^*$: $x_\alpha^{(\beta)} \in V_\alpha$ for $\alpha \in F$ (by choice of $\beta_\alpha$), and $x_\alpha^{(\beta)} \in X_\alpha = V_\alpha$ trivially for $\alpha \notin F$. So $x^{(\beta)} \in V_0 \subseteq V$.
>
> Hence $\{x^{(\beta)}\}$ is eventually in $V$, for every neighborhood $V$ of $x$, so $x^{(\beta)} \to x$ in the product topology. $\blacksquare$
>
> **Specialization to function spaces:** for $X^A$ viewed as the product of $|A|$ copies of $X$, with $\pi_a(f) = f(a)$, the theorem reads: $f_\beta \to f$ in $X^A$ iff $f_\beta(a) \to f(a)$ for every $a$, i.e., pointwise convergence is exactly product-topology convergence on $X^A$.

---

# Cross-Field Exercise Suggestions

**Pointwise convergence of $L^1$ functions.** Let $f_n \in L^1([0, 1])$ with $f_n(x) \to f(x)$ for every $x \in [0, 1]$. View $f_n$ as elements of $\mathbb{R}^{[0, 1]}$ — the space of functions $[0, 1] \to \mathbb{R}$ with the product topology. Then $f_n \to f$ in this product topology. But this is far weaker than $L^1$ or pointwise *a.e.* convergence; the example $f_n(x) = n\mathbf{1}_{[0, 1/n]}$ has $f_n(x) \to 0$ pointwise (except at $x = 0$) but $\int f_n = 1$ for all $n$. This is the canonical illustration that product-topology convergence is weak — it captures pointwise behavior but not integration behavior.

**Strong operator topology on $\mathcal{B}(V)$.** A net of bounded operators $T_\beta$ converges in SOT to $T$ iff $T_\beta v \to T v$ for every $v \in V$. This is product-topology convergence on $V^V$ restricted to $\mathcal{B}(V) \subseteq V^V$. The standard application: a sequence of orthogonal projections $P_n$ onto $\text{span}(e_1, \dots, e_n)$ converges in SOT to the identity, even though it does not converge in norm.

**Banach–Alaoglu via pointwise convergence.** A net of bounded linear functionals $\varphi_\beta$ converges in the weak-$*$ topology to $\varphi$ iff $\varphi_\beta(x) \to \varphi(x)$ for every $x \in V$. This is product-topology convergence on $\mathbb{R}^V$. The unit ball in $V^*$ is closed in this topology (pointwise limits preserve linearity and the norm bound), and is contained in the Tychonoff-compact product $\prod_x [-\lVert x\rVert, \lVert x\rVert]$, hence compact.

---

# Bridges

- **[[Def - Product Topology]]** — the topology being characterized. The theorem is the defining property of the product topology: it is the unique topology in which net convergence is coordinatewise.

- **[[Thm - Tychonoff Theorem]]** — uses this theorem at the key step (universal subnet of the product converges iff each coordinate converges, which holds by compactness of each factor).

- **[[Thm - Continuity via Nets]]** — gives the forward direction via continuity of projections, and lets us check continuity of maps into the product by checking each coordinate.

- **[[Def - Subnet and Universal Net]]** — universal nets preserved by projection (a special case of "any function preserves universality") is the key combinatorial fact in Tychonoff.

- **Topology of pointwise convergence** — the specialization to $X^A$, the function-space realization.

---

# Unlocked by This

> [!tip] Weak-$*$ Topology *(from Functional Analysis)*
> The weak-$*$ topology on $V^*$ is the product topology on $\mathbb{R}^V$ restricted to $V^* \subseteq \mathbb{R}^V$. Convergence is pointwise on $V$; compactness of the unit ball is Tychonoff in disguise.

> [!tip] Strong Operator Topology *(from Functional Analysis)*
> The SOT on $\mathcal{B}(V, W)$ is the product topology on $W^V$ restricted to $\mathcal{B}(V, W)$. It is strictly weaker than norm topology and strictly stronger than weak operator topology.

> [!tip] Pointwise Convergence of Probability Measures *(from Probability)*
> A net of probability measures $\mu_\beta$ on a compact $K$ converges in the topology of pointwise convergence on $C(K)$ iff $\int f\, d\mu_\beta \to \int f\, d\mu$ for every $f \in C(K)$. This is **weak-$*$** (or **weak**) convergence of measures, and it is the topology of the Riesz representation isomorphism with $C(K)^*$.
