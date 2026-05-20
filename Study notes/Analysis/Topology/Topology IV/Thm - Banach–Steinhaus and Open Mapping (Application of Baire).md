---
type: theorem
subject: topology
prereqs:
  - "Thm - Baire Category Theorem"
  - "Def - Cauchy Sequence and Complete Metric Space"
  - "Def - Nowhere Dense and Meager"
tags: [analysis, topology, functional-analysis, baire]
---

# Notation

$X, Y$ Banach spaces; $\|\cdot\|_X, \|\cdot\|_Y$ their norms. $B(X, Y)$ the space of bounded (continuous) linear operators $X \to Y$, with operator norm $\|T\| = \sup_{\|x\| \leq 1} \|Tx\|_Y$. A family $\{T_\alpha\}_{\alpha \in A} \subseteq B(X, Y)$. "Pointwise bounded" means $\sup_\alpha \|T_\alpha x\| < \infty$ for each $x$; "uniformly bounded" means $\sup_\alpha \|T_\alpha\| < \infty$. The full registry is on the topic page.

---

# Motivation

The Baire category theorem is a *topological* statement: in a complete metric space, certain "bad" sets are meager, so good sets are dense. The miracle of functional analysis is that this purely topological fact, applied to the right Banach space, produces *quantitative* analytical theorems with no obvious topological content: uniform boundedness from pointwise boundedness, openness of surjections, continuity from closed graphs.

The unified theme: a family of operators (or a single operator) has some seemingly weak property (pointwise boundedness, surjectivity, closed graph). We want to upgrade this to a strong uniform property (uniform boundedness, openness, continuity). The upgrade is impossible in general — but Baire forces it in the Banach setting, by ruling out the only way it could fail.

**Banach-Steinhaus** (uniform boundedness principle): a family of bounded operators that is pointwise bounded (each individual operator is bounded at each point, with bounds depending on the point) is in fact *uniformly bounded* (a single bound works for all operators and all unit vectors). The proof: the set of $x$ where the family fails to be bounded is, in some sense, "small" (meager), so it must be empty for a uniformly bounded family.

**Open mapping theorem**: a surjective continuous linear map between Banach spaces is open — i.e., it maps open sets to open sets. The proof: the image of the unit ball, being the union of translates of $T(B_1)$, must have nonempty interior somewhere (by Baire), hence everywhere (by linearity).

**Closed graph theorem** (corollary): a linear map between Banach spaces with closed graph is continuous. Consequence of open mapping applied to the projection from the graph.

All three theorems share the same proof structure: write a "bad" object as a countable union of nowhere dense sets, apply Baire, conclude the bad object is small enough that it cannot account for the entire space.

---

# Statement

**Banach-Steinhaus (Uniform Boundedness Principle).** Let $X$ be a Banach space, $Y$ a normed space, and $\{T_\alpha\}_{\alpha \in A}$ a family of bounded linear operators $X \to Y$. If
$$\sup_{\alpha \in A} \|T_\alpha x\|_Y < \infty \quad \text{for every } x \in X \quad (\text{pointwise bounded}),$$
then
$$\sup_{\alpha \in A} \|T_\alpha\| < \infty \quad (\text{uniformly bounded}).$$

**Open Mapping Theorem.** Let $X, Y$ be Banach spaces and $T : X \to Y$ a bounded linear operator. If $T$ is surjective, then $T$ is an **open map** — i.e., for every open $U \subseteq X$, $T(U)$ is open in $Y$. Equivalently, $T$ maps the open unit ball $B^X_1$ to an open neighborhood of $0$ in $Y$.

**Closed Graph Theorem (corollary).** Let $X, Y$ be Banach spaces and $T : X \to Y$ a linear map. If the graph $G_T := \{(x, Tx) : x \in X\} \subseteq X \times Y$ is closed, then $T$ is bounded (continuous).

---

# Sources and Targets

**Sources (Input Broadening)**

For Banach-Steinhaus, the precondition is "pointwise bounded family on a Banach space".

**A sequence converging pointwise.** Property $B$: $T_n x \to T x$ for each $x$. The bridge: pointwise convergent implies pointwise bounded (each $\|T_n x\|$ is a bounded sequence, hence bounded). *Example:* if a sequence of operators converges pointwise to $T$, then the $T_n$ are uniformly bounded — by Banach-Steinhaus.

**A family with a domination by a constant function.** Property $B$: $\|T_\alpha x\| \leq M(x)$ for some function $M : X \to \mathbb{R}$ depending only on $x$. The bridge: pointwise boundedness with explicit bound.

For Open Mapping, the precondition is "surjective continuous linear map between Banach spaces".

**An invertible operator.** Property $B$: $T : X \to Y$ is a continuous linear bijection. The bridge: $T$ surjective is the OMT input; $T^{-1}$ is then bounded (the *bounded inverse theorem*). *Example:* showing the inverse of a continuous linear bijection between Banach spaces is continuous — what makes Banach algebras well-defined.

**Targets (Output Amplification)**

The conclusions amplify to:

Combine Banach-Steinhaus with **a weak* convergent sequence.** Property $D$: $f_n \to f$ in the weak* topology on a dual space. The amplified result $E$: $\|f_n\|$ is bounded (uniform boundedness of the family of linear functionals applied to each $x$). This is the "weak* sequential limits are bounded" lemma.

Combine OMT with **the bounded inverse theorem.** Property $D$: $T$ is a continuous linear bijection. The amplified result $E$: $T^{-1}$ is continuous. *Example:* equivalence of norms on a Banach space — if two norms make $X$ a Banach space and one is dominated by the other, they are equivalent.

Combine OMT with **the closed graph theorem.** Property $D$: $T$ has closed graph. The amplified result $E$: $T$ is continuous (closed graph $\Rightarrow$ continuous). The proof uses OMT applied to the projection $G_T \to X$.

---

# Why Is It True

**Banach-Steinhaus.** Define, for each $k \geq 1$, the set
$$E_k := \{x \in X : \sup_\alpha \|T_\alpha x\| \leq k\}.$$
Each $E_k$ is closed: $E_k = \bigcap_\alpha \{x : \|T_\alpha x\| \leq k\}$, an intersection of closed sets (preimages of $[0, k]$ under continuous $\|T_\alpha \cdot\|$).

Pointwise boundedness means $X = \bigcup_k E_k$ — every $x$ is in some $E_k$.

By the **Baire category theorem** ([[Thm - Baire Category Theorem]]) applied to the Banach (complete metric) space $X$: $X$ is not meager in itself, so at least one $E_k$ is not nowhere dense. Since $E_k$ is closed, "not nowhere dense" means $E_k$ has nonempty interior. So there is $x_0 \in X$ and $r > 0$ with $B_r(x_0) \subseteq E_k$.

For any $x \in X$ with $\|x\| < r$, we have $x_0 + x \in B_r(x_0) \subseteq E_k$, so $\|T_\alpha(x_0 + x)\| \leq k$ for all $\alpha$. Then $\|T_\alpha x\| = \|T_\alpha(x_0 + x) - T_\alpha x_0\| \leq 2k$ (using the triangle inequality and $\|T_\alpha x_0\| \leq k$). So $\|T_\alpha\| = \sup_{\|x\| < r} \|T_\alpha x\| / r \leq 2k / r$ for all $\alpha$. Uniformly bounded.

**Open Mapping.** Write $X = \bigcup_n nB_1$ (where $B_1$ is the unit ball). Then $Y = T(X) = \bigcup_n T(nB_1) = \bigcup_n nT(B_1)$, since $T$ is surjective. By **Baire**, some $\overline{n T(B_1)}$ has nonempty interior, hence so does $\overline{T(B_1)}$ (by scaling). So there is $y_0 \in Y$ and $r > 0$ with $B_r(y_0) \subseteq \overline{T(B_1)}$. By symmetry ($\overline{T(B_1)}$ is centrally symmetric, since $B_1$ is), we get $B_r(-y_0) \subseteq \overline{T(B_1)}$. Convexity then gives $B_r(0) \subseteq \overline{T(B_1)}$.

The hard part: upgrade $B_r(0) \subseteq \overline{T(B_1)}$ to $B_{r/2}(0) \subseteq T(B_1)$ (without the closure). This is a geometric series argument: given $y$ with $\|y\| < r/2$, find $x_1 \in B_{1/2}$ with $\|y - T x_1\| < r/4$; then $x_2 \in B_{1/4}$ with $\|y - Tx_1 - Tx_2\| < r/8$; etc. The sum $x = \sum x_n$ converges (geometric in the Banach space) with $\|x\| < 1$, and $Tx = y$. So $y \in T(B_1)$.

Hence $T(B_1)$ contains a ball around $0$, and by linearity, $T$ maps open sets to open sets.

**Closed Graph.** $G_T \subseteq X \times Y$ is closed by hypothesis. $X \times Y$ is a Banach space (product norm). So $G_T$ is a closed subspace of a Banach space, hence itself a Banach space. The projections $\pi_X : G_T \to X$ and $\pi_Y : G_T \to Y$ are continuous linear maps. $\pi_X$ is bijective: it's a bijection because $G_T = \{(x, Tx) : x \in X\}$ and $T$ is a (defined as) a function on $X$.

By OMT, $\pi_X$ is open, hence $\pi_X^{-1} : X \to G_T$ is continuous, $x \mapsto (x, Tx)$. The composition $\pi_Y \circ \pi_X^{-1} : X \to Y$ is $T$, a composition of continuous maps. So $T$ is continuous.

The reason to expect these: the Baire category theorem is structurally an "existence of large set" theorem, and "large set" in Banach space context means "open ball". Once Baire gives us an open ball inside the image of some set, linearity propagates the ball everywhere, giving the uniform/open statement.

---

# What Makes This Hard

The non-obvious step in each is *the right partition of the Banach space into countably many closed sets*. For Banach-Steinhaus, it's $E_k = \{x : \sup_\alpha \|T_\alpha x\| \leq k\}$ — these *exhaust* the space because of pointwise boundedness. For OMT, it's $X = \bigcup n B_1$ — trivial, but the image side $\bigcup n T(B_1)$ exhausts $Y$ because of surjectivity. The common error is to omit the closure: $E_k$ must be closed for Baire's "not nowhere dense + closed = has interior" to apply; similarly $\overline{T(B_1)}$ is the closed set with interior, and the geometric-series upgrade is needed to remove the closure.

---

# Rederivation Scaffold

**High-level strategy:**
For each theorem, partition the Banach space into countably many closed sets whose union is everything. By Baire, one has nonempty interior. Use this to construct the bound (BS) or the open mapping (OMT).

**Subgoal decomposition (Banach-Steinhaus):**

1. **Partition by uniform bound.** $E_k = \{x : \sup_\alpha \|T_\alpha x\| \leq k\}$, closed, with $X = \bigcup E_k$ by pointwise boundedness.

2. **Apply Baire.** Some $E_k$ has nonempty interior.

3. **Translate to bound on operator norm.** If $B_r(x_0) \subseteq E_k$, then $\|T_\alpha x\| \leq 2k$ for $\|x\| < r$, giving $\|T_\alpha\| \leq 2k/r$.

**Subgoal decomposition (Open Mapping):**

1. **Partition image by ball size.** $Y = \bigcup n \overline{T(B_1)}$ by surjectivity.

2. **Apply Baire.** $\overline{T(B_1)}$ has nonempty interior.

3. **Use symmetry/convexity.** $B_r(0) \subseteq \overline{T(B_1)}$ for some $r$.

4. **Remove closure via geometric series.** Construct preimage iteratively, $\|x_n\| < 2^{-n}$, sum converges to $x$ with $Tx = y$.

---

# Lemma Decomposition

> [!note]- Lemma 1: A closed convex symmetric set with nonempty interior contains a ball around 0
> **Statement:** If $K \subseteq Y$ is closed, convex, symmetric ($K = -K$), and contains an interior point, then $K$ contains a ball around $0$.
>
> **Hint:** Symmetry + interior point $y_0 \implies$ ball around $-y_0$ also in $K$; convexity gives midpoint $0$ has a ball.
>
> **Why needed:** OMT step from "interior point of $\overline{T(B_1)}$" to "ball around 0 in $\overline{T(B_1)}$".
>
> > [!note]- Full proof
> > Let $y_0 \in K$ with $B_r(y_0) \subseteq K$. By symmetry, $-y_0 \in K$ and $B_r(-y_0) \subseteq K$. For any $y$ with $\|y\| < r$, both $y_0 + y$ and $-y_0 + y$ are within distance $r$ of $\pm y_0$, hence both in $K$. By convexity, the midpoint $(y_0 + y + (-y_0 + y))/2 = y$ is in $K$. So $B_r(0) \subseteq K$.

> [!note]- Lemma 2: Geometric series for the closure-removal step in OMT
> **Statement:** If $B_r(0) \subseteq \overline{T(B_1)}$ in a Banach space, then $B_{r/2}(0) \subseteq T(B_1)$.
>
> **Hint:** Iterative approximation.
>
> **Why needed:** Removes the closure to get the OMT.
>
> > [!note]- Full proof
> > Given $y$ with $\|y\| < r/2$. Choose $x_1 \in B_{1/2}$ with $\|y - Tx_1\| < r/4$ (possible: scale $y$ by 2 to get $2y \in B_r(0) \subseteq \overline{T(B_1)}$, so there's $x \in B_1$ with $\|2y - Tx\| < r/2$, i.e., $\|y - T(x/2)\| < r/4$; take $x_1 = x/2$). Inductively, having $x_1, \dots, x_n$ with $\|x_i\| < 2^{-i}$ and $\|y - T(\sum x_i)\| < r/2^{n+1}$, find $x_{n+1} \in B_{2^{-(n+1)}}$ with the next approximation.
> >
> > The series $x := \sum x_n$ converges in the Banach space ($\sum \|x_n\| < \sum 2^{-n} = 1$, so $\|x\| < 1$). By continuity of $T$, $Tx = \sum Tx_n = y$. So $y \in T(B_1)$.

---

# Formal Proof

> [!note]- Complete formal proof (Banach-Steinhaus)
> Let $X$ be Banach, $\{T_\alpha\}$ a family of bounded linear operators with $\sup_\alpha \|T_\alpha x\| < \infty$ for each $x$.
>
> For each $k \in \mathbb{N}$, define $E_k := \{x \in X : \sup_\alpha \|T_\alpha x\| \leq k\}$. $E_k$ is closed: write $E_k = \bigcap_\alpha (T_\alpha)^{-1}(\overline{B}^Y_k)$ where $\overline{B}^Y_k$ is the closed ball of radius $k$ in $Y$ — this is the intersection of preimages of closed sets under continuous maps, hence closed.
>
> By pointwise boundedness, $X = \bigcup_k E_k$. By [[Thm - Baire Category Theorem]] applied to Banach space $X$, $X$ is not meager in itself, so some $E_k$ is not nowhere dense. Being closed, "not nowhere dense" means $E_k$ has nonempty interior: there is $x_0 \in X$ and $r > 0$ with $B_r(x_0) \subseteq E_k$.
>
> For any $\alpha$ and any $x \in X$ with $\|x\| < r$: $x_0 + x \in B_r(x_0) \subseteq E_k$, so $\|T_\alpha(x_0 + x)\| \leq k$. By linearity, $T_\alpha x = T_\alpha(x_0 + x) - T_\alpha x_0$, so
> $$\|T_\alpha x\| \leq \|T_\alpha(x_0 + x)\| + \|T_\alpha x_0\| \leq k + k = 2k.$$
> (Here $\|T_\alpha x_0\| \leq k$ because $x_0 \in E_k$.)
>
> So $\sup_\alpha \|T_\alpha x\| \leq 2k$ for all $x$ with $\|x\| < r$, i.e., $\|T_\alpha\| \leq 2k/r$ for all $\alpha$. Uniformly bounded. $\blacksquare$

> [!note]- Complete formal proof (Open Mapping Theorem)
> Let $X, Y$ be Banach, $T : X \to Y$ continuous linear and surjective.
>
> **Step 1: $\overline{T(B_1)}$ has nonempty interior.** By surjectivity, $Y = T(X) = \bigcup_n T(nB_1) = \bigcup_n nT(B_1)$. Hence $Y = \bigcup_n \overline{nT(B_1)} = \bigcup_n n\overline{T(B_1)}$. By Baire, some $n\overline{T(B_1)}$ has nonempty interior, hence so does $\overline{T(B_1)}$ (scale).
>
> **Step 2: $\overline{T(B_1)}$ contains a ball around $0$.** $\overline{T(B_1)}$ is closed, convex (image of convex $B_1$, closure preserves convexity), and symmetric ($T(B_1) = -T(B_1)$ since $B_1 = -B_1$). By Lemma 1, $B_r(0) \subseteq \overline{T(B_1)}$ for some $r > 0$.
>
> **Step 3: Remove closure to $B_{r/2}(0) \subseteq T(B_1)$.** By Lemma 2.
>
> **Step 4: $T$ is open.** For any open $U \subseteq X$ and any $x \in U$ with $B_\delta(x) \subseteq U$, we have $T(U) \supseteq T(B_\delta(x)) = Tx + T(B_\delta) = Tx + \delta T(B_1) \supseteq Tx + \delta B_{r/2}(0) = B_{\delta r/2}(Tx)$. So $Tx$ is interior to $T(U)$, hence $T(U)$ is open. $\blacksquare$

> [!note]- Complete formal proof (Closed Graph Theorem)
> Let $T : X \to Y$ linear with closed graph $G_T \subseteq X \times Y$. $G_T$ is a closed subspace of the Banach space $X \times Y$ (with product norm), hence itself Banach.
>
> The projections $\pi_X : G_T \to X$ and $\pi_Y : G_T \to Y$ are continuous (restrictions of the projections on $X \times Y$).
>
> $\pi_X$ is a continuous linear bijection from the Banach space $G_T$ to the Banach space $X$: bijective because $G_T$ is parameterized by $X$ via $x \mapsto (x, Tx)$.
>
> By OMT applied to $\pi_X$: $\pi_X$ is open, so $\pi_X^{-1} : X \to G_T$ is continuous.
>
> Compose: $T = \pi_Y \circ \pi_X^{-1}$ is a composition of continuous maps, hence continuous. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Equivalence of norms on a Banach space.** If $\|\cdot\|_1$ and $\|\cdot\|_2$ are two norms making $X$ a Banach space, and $\|x\|_1 \leq C \|x\|_2$ for some $C$, then the norms are equivalent (each bounds a multiple of the other). Proof: the identity map $(X, \|\cdot\|_2) \to (X, \|\cdot\|_1)$ is a continuous linear bijection between Banach spaces; OMT gives the inverse is continuous, i.e., $\|x\|_2 \leq C' \|x\|_1$.

**Spectrum is non-empty for Banach algebra elements.** Every element of a unital complex Banach algebra has nonempty spectrum. The proof uses an application of Liouville's theorem to the resolvent map, but the uniform boundedness of resolvents on compact sets uses Banach-Steinhaus.

**Spectral mapping theorem.** For a bounded operator $T$ on Banach space and a polynomial $p$, $\sigma(p(T)) = p(\sigma(T))$. The proof uses OMT to show that resolvents are well-behaved.

---

# Bridges

- **[[Thm - Baire Category Theorem]]** — the engine of all three results.

- **[[Def - Cauchy Sequence and Complete Metric Space]]** — Banach spaces are complete; this is where Baire applies.

- **[[Def - Nowhere Dense and Meager]]** — the size notions.

---

# Unlocked by This

> [!tip] Bounded Inverse Theorem *(from Functional Analysis)*
> A continuous linear bijection between Banach spaces has continuous inverse. Immediate corollary of OMT. This is what makes Banach algebras work: if an operator is invertible algebraically, it's invertible topologically.

> [!tip] Hahn-Banach (companion) *(from Functional Analysis)*
> The other foundational theorem of functional analysis, Hahn-Banach, gives extensions of bounded linear functionals. It does *not* use Baire (uses Zorn's lemma instead), but together Hahn-Banach + Baire form the foundational toolkit.

> [!tip] Banach-Alaoglu *(from Functional Analysis)*
> The closed unit ball of the dual of a Banach space is compact in the weak* topology. This combines with the Baire-based theorems to give the variational principles of functional analysis.
