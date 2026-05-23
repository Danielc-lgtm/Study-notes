---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Smooth Atlas and Smooth Structure"
  - "Def - Transition Function"
  - "Def - Vector Space"
  - "Def - Linear Map"
  - "Def - Direct Sum"
  - "Thm - Smooth Structure from Maximal Atlas"
tags: [geometry, differential-geometry, algebra]
---

# Problem Statement

Let $V$ be an $n$-dimensional real vector space and let $0 < k < n$. The **Grassmannian** $G_k(V)$ is the set of all $k$-dimensional linear [[Def - Subspace|subspaces]] of $V$. Show that $G_k(V)$ can be given the structure of a smooth manifold of [[Def - Dimension|dimension]] $k(n-k)$, called the **Grassmann manifold**.

(a) For each choice of complementary [[Def - Subspace|subspaces]] $V = P \oplus Q$ with $\dim P = k$, $\dim Q = n - k$, construct a chart $\varphi_{P,Q}$ on the open subset $U_Q \subseteq G_k(V)$ consisting of $k$-dimensional subspaces $S$ with $S \cap Q = \{0\}$. The chart sends such an $S$ to the linear map $X : P \to Q$ whose graph is $S$.

(b) Verify $\varphi_{P,Q}$ is a bijection onto $L(P, Q) \cong \mathbb{R}^{k(n-k)}$ (with basis choice).

(c) Compute the transition function between two charts $\varphi_{P,Q}$ and $\varphi_{P', Q'}$ and verify smoothness.

(d) Apply the smooth manifold chart lemma (Lee 1.35) to conclude $G_k(V)$ is a smooth manifold of dimension $k(n-k)$.

In the special case $V = \mathbb{R}^n$, the Grassmannian is denoted $G_k(\mathbb{R}^n)$ or $G_{k, n}$. The case $k = 1$ recovers $\mathbb{RP}^{n-1}$ (one-dimensional subspaces are lines through the origin).

**Recall:**

The smooth atlas / smooth structure framework:

![[Def - Smooth Atlas and Smooth Structure#The Definition]]

The **smooth manifold chart lemma** (Lee 1.35) is the workhorse: given a set $M$ with a covering family of maps $\varphi_\alpha : U_\alpha \to \mathbb{R}^N$ satisfying suitable bijectivity, open-image, smooth-overlap, countable-covering, and Hausdorff-separation conditions, $M$ has a unique topology and smooth structure making each $(U_\alpha, \varphi_\alpha)$ a smooth chart.

A **direct sum decomposition** $V = P \oplus Q$ means every $v \in V$ has a unique decomposition $v = p + q$ with $p \in P$, $q \in Q$. The associated projections $\pi_P : V \to P$ and $\pi_Q : V \to Q$ are linear maps satisfying $v = \pi_P(v) + \pi_Q(v)$.

---

# Convergent Strategy

**Problem class:** Constructing a smooth manifold from a set without a priori topology — type 3 of the problem-solving routine in [[Differential Geometry I — Smooth Manifolds and Atlases#Problem-Solving Strategy]]. The space $G_k(V)$ is a set of subspaces, and we need to manufacture both a topology and a smooth structure. The smooth manifold chart lemma is the heavyweight tool that does both simultaneously.

**Assumption pattern:** $V$ is a finite-dimensional vector space; subspaces are sets that we want to organize into a topological space. The key observation is that a $k$-dimensional subspace $S$ "near" a fixed subspace $P$ (in the sense that $S \cap Q = 0$ for a fixed complement $Q$ of $P$) is the *graph* of a unique linear map $X : P \to Q$. So we have a natural bijection $U_Q \leftrightarrow L(P, Q)$, and $L(P, Q)$ has a natural vector-space structure (and hence topology and smooth structure). This is the source of charts.

**Theorem routing:** The route is: (i) construct chart bijections $\varphi_{P,Q} : U_Q \to L(P, Q)$ via the graph interpretation; (ii) compute the transition function between two such charts using projection identities; (iii) verify smoothness by recognizing the transition as a matrix-Möbius transformation $X' = (B + DX)(A + CX)^{-1}$; (iv) verify the chart-lemma hypotheses, including covering, smoothness, countability, and Hausdorff-separation; (v) conclude via the chart lemma.

**Key decision point:** The non-obvious move is interpreting a $k$-dimensional subspace $S$ near $P$ as the *graph* of a linear map $X : P \to Q$. The intuition: $S$ has dimension $k$, $P$ has dimension $k$, and the assumption $S \cap Q = 0$ means $S$ projects injectively (and hence isomorphically) to $P$. So $S$ is determined by a section of the projection — a map $P \to V$ landing in $S$, which decomposes as $\mathrm{id}_P \oplus X$ for the unique $X : P \to Q$ making the graph land in $S$. This is the key geometric fact that makes the chart construction work.

---

# Legal Operations Used

1. **Operation 1 from the topic page (cover with charts).** The chart domains $\{U_Q : Q \text{ is an } (n-k)\text{-complement of some } k\text{-subspace}\}$ cover $G_k(V)$: every $k$-subspace $S$ has *some* $(n-k)$-complement $Q$ with $S \cap Q = 0$.

2. **Operation 2 from the topic page (compute transition functions explicitly).** We compute the transition between two charts as a matrix-Möbius transformation and verify smoothness.

3. **Operation 3 from the topic page (apply the smooth manifold chart lemma, Lee 1.35).** This is the heavyweight tool: a set with chart-like maps satisfying five conditions becomes a smooth manifold.

4. **Operation 8 from the topic page (verify Hausdorff and second countability).** Hausdorff via the separating chart-lemma condition; second countability via finite covering by chart domains.

---

# Hints

> [!note]- Hint 1
> Fix a direct sum decomposition $V = P \oplus Q$ with $\dim P = k$, $\dim Q = n - k$. The Grassmannian chart domain $U_Q = \{S \in G_k(V) : S \cap Q = 0\}$ — equivalently, $S$ projects isomorphically onto $P$ via $\pi_P$.

> [!note]- Hint 2
> The chart map $\varphi_{P,Q} : U_Q \to L(P, Q)$ sends $S$ to the linear map $X$ whose graph $\{p + Xp : p \in P\} = S$. Explicitly: $X = (\pi_Q|_S) \circ (\pi_P|_S)^{-1} : P \to Q$, where $\pi_P|_S : S \to P$ is an isomorphism by the $S \cap Q = 0$ assumption.

> [!note]- Hint 3
> For the transition $\varphi_{P', Q'} \circ \varphi_{P, Q}^{-1}$: given $X \in L(P, Q)$, the subspace is $S = \mathrm{graph}(X)$; the projection $\pi_{P'}|_S$ corresponds to a linear map $P \to P'$ that involves the inclusion $\mathrm{id}_P + X : P \to V$ followed by $\pi_{P'} : V \to P'$.

> [!note]- Hint 4
> Define $A = \pi_{P'}|_P, B = \pi_{Q'}|_P, C = \pi_{P'}|_Q, D = \pi_{Q'}|_Q$. Then $\pi_{P'}|_{\mathrm{graph}(X)} = A + CX : P \to P'$, and the transition function is
> $$X' = (B + DX)(A + CX)^{-1}.$$
> This is a *matrix-Möbius transformation* — a rational matrix function with denominator $A + CX$.

> [!note]- Hint 5
> The smoothness of the matrix-Möbius transformation: by Cramer's rule, $(A + CX)^{-1}$ has matrix entries that are rational functions in the entries of $X$, with denominator $\det(A + CX)$. This is nonzero on the domain of definition (where $\mathrm{graph}(X)$ has trivial intersection with $Q'$, ensuring $A + CX$ is invertible). Hence the transition is smooth.

---

# Solution

The proof breaks into five steps. Step 1 sets up the bijection $U_Q \leftrightarrow L(P, Q)$ via the graph interpretation. Step 2 verifies the bijection. Step 3 computes the transition function explicitly. Step 4 verifies smoothness via Cramer's rule. Step 5 applies the smooth manifold chart lemma. The key non-obvious step is Step 3, where the matrix-Möbius form of the transition is derived; from there, smoothness is immediate.

**Step 1: The graph interpretation of subspaces near $P$.**

Fix $V = P \oplus Q$ with $\dim P = k, \dim Q = n - k$. Let $U_Q = \{S \in G_k(V) : S \cap Q = \{0\}\}$. For $S \in U_Q$, the projection $\pi_P|_S : S \to P$ is a linear isomorphism (it is injective by $S \cap Q = 0$ and has rank $\leq k = \dim S$; equating [[Def - Dimension|dimensions]] makes it an isomorphism). Define $X = (\pi_Q|_S) \circ (\pi_P|_S)^{-1} : P \to Q$. Then $S = \{p + X(p) : p \in P\} = \mathrm{graph}(X)$.

> [!note]- Derivation
> *Linear isomorphism $\pi_P|_S$.* Suppose $s \in S$ satisfies $\pi_P(s) = 0$; then $s \in Q$ (the kernel of $\pi_P$ is $Q$). Combined with $s \in S$, this gives $s \in S \cap Q = \{0\}$, so $s = 0$. Hence $\pi_P|_S$ is injective. By dimension equality $\dim S = \dim P = k$, it is bijective, so a linear isomorphism.
>
> *Construct $X$.* Define $X = \pi_Q \circ (\pi_P|_S)^{-1} : P \to Q$. This is a composition of linear maps, hence linear.
>
> *$S = \mathrm{graph}(X)$.* Given $p \in P$, set $s = (\pi_P|_S)^{-1}(p) \in S$. By the direct sum decomposition, $s = \pi_P(s) + \pi_Q(s) = p + X(p)$. So every element of $S$ has the form $p + X(p)$, and conversely every such element is in $S$. Hence $S = \{p + X(p) : p \in P\} = \mathrm{graph}(X)$.

**Step 2: The bijection $\varphi_{P,Q} : U_Q \to L(P, Q)$.**

Define $\varphi_{P,Q}(S) = X$ as in Step 1. Conversely, given $X \in L(P, Q)$, let $S = \mathrm{graph}(X) = \{p + X(p) : p \in P\}$. Then $S \in U_Q$, and $\varphi_{P,Q}(S) = X$. So $\varphi_{P,Q}$ is a bijection.

> [!note]- Derivation
> *Inverse.* For $X \in L(P, Q)$, let $S = \mathrm{graph}(X)$. $S$ is a subspace (closed under addition and scalar multiplication via linearity of $X$). $S \cap Q = 0$: if $p + X(p) \in Q$, the $P$-component gives $p = 0$, hence $X(p) = 0$. $\dim S = k$ (basis $\{e_i + X(e_i)\}_{i=1}^k$ for $\{e_i\}$ a basis of $P$). So $S \in U_Q$.
>
> *Inversion verification.* The chart $\varphi_{P,Q}(S)$ for $S = \mathrm{graph}(X)$: $(\pi_P|_S)(p + X(p)) = p$, so $(\pi_P|_S)^{-1}(p) = p + X(p)$, so $X = \pi_Q \circ (\pi_P|_S)^{-1}$ sends $p$ to $\pi_Q(p + X(p)) = X(p)$. Hence $\varphi_{P,Q}(S) = X$. ✓
>
> *$L(P, Q)$ is a vector space of dimension $k(n-k)$.* Choose bases for $P$ and $Q$; each $X : P \to Q$ is a $(n-k) \times k$ matrix, so $L(P, Q) \cong \mathbb{R}^{k(n-k)}$ as a vector space, and the bijection is a [[Def - Homeomorphism|homeomorphism]] in the standard topology.

**Step 3: Compute the transition function between two charts.**

Take another direct sum decomposition $V = P' \oplus Q'$ with $\dim P' = k, \dim Q' = n - k$, and the corresponding chart $\varphi_{P', Q'} : U_{Q'} \to L(P', Q')$. The transition function $\varphi_{P', Q'} \circ \varphi_{P, Q}^{-1}$ is defined on the open subset $\varphi_{P, Q}(U_Q \cap U_{Q'}) \subseteq L(P, Q)$ and is given by
$$X' = (B + DX)(A + CX)^{-1},$$
where $A, B, C, D$ are the linear maps
$$A = \pi_{P'}|_P : P \to P', \quad B = \pi_{Q'}|_P : P \to Q', \quad C = \pi_{P'}|_Q : Q \to P', \quad D = \pi_{Q'}|_Q : Q \to Q'.$$

> [!note]- Derivation
> Take $X \in \varphi_{P, Q}(U_Q \cap U_{Q'})$. Let $S = \mathrm{graph}(X) \subseteq V$, the corresponding subspace. We need to compute $X' = \varphi_{P', Q'}(S) = \pi_{Q'}|_S \circ (\pi_{P'}|_S)^{-1}$.
>
> *Express the relevant linear maps in terms of $A, B, C, D$.* For any $p \in P$ and $q \in Q$, decompose using $V = P' \oplus Q'$:
> $$p = \pi_{P'}(p) + \pi_{Q'}(p) = A(p) + B(p), \quad q = \pi_{P'}(q) + \pi_{Q'}(q) = C(q) + D(q).$$
> So $p + q = (A + B)(p) + (C + D)(q)$ as an element of $P' \oplus Q'$.
>
> *Compute the projections $\pi_{P'}|_S, \pi_{Q'}|_S$.* The graph map $P \to S$ is $p \mapsto p + X(p)$. Composing with $\pi_{P'}$:
> $$\pi_{P'}(p + X(p)) = \pi_{P'}(p) + \pi_{P'}(X(p)) = A(p) + C(X(p)) = (A + CX)(p).$$
> So $\pi_{P'}|_S \circ (P \xrightarrow{\mathrm{graph}} S) = A + CX : P \to P'$.
>
> Similarly, $\pi_{Q'}|_S \circ (P \to S) = B + DX : P \to Q'$.
>
> *Invertibility of $A + CX$.* The map $A + CX : P \to P'$ is the composition $\pi_{P'}|_S \circ (\pi_P|_S)^{-1}$. It is invertible iff $S \cap Q' = 0$, i.e., iff $S \in U_{Q'}$. This is precisely the domain condition: $X \in \varphi_{P, Q}(U_Q \cap U_{Q'})$ iff $A + CX$ is invertible.
>
> *Compute $X'$.* $X' = \pi_{Q'}|_S \circ (\pi_{P'}|_S)^{-1} = (B + DX) \circ [(A + CX) \circ (\pi_P|_S)^{-1}]^{-1} \circ (\pi_P|_S)^{-1}$ — but to relate it cleanly, note that $\pi_{P'}|_S = (A + CX) \circ (\pi_P|_S)$ (both maps from $S$ to $P'$ agreeing on the basis), so $(\pi_{P'}|_S)^{-1} = (\pi_P|_S)^{-1} \circ (A + CX)^{-1}$ on $P'$. Then $X' = \pi_{Q'}|_S \circ (\pi_{P'}|_S)^{-1}$. As a map $P' \to Q'$, evaluate at $p' \in P'$: $(\pi_{P'}|_S)^{-1}(p') = (\pi_P|_S)^{-1}((A + CX)^{-1}(p'))$, and applying $\pi_{Q'}|_S$ gives
> $$X'(p') = (B + DX)(A + CX)^{-1}(p').$$
> Hence $X' = (B + DX)(A + CX)^{-1}$ as elements of $L(P', Q')$.

**Step 4: Verify smoothness of the transition function.**

The transition $X \mapsto (B + DX)(A + CX)^{-1}$ is a *matrix-Möbius transformation*. Each component is a rational function of the entries of $X$ with denominator $\det(A + CX)$, which is nonzero on the domain (by the invertibility of $A + CX$). By Cramer's rule, $(A + CX)^{-1}$ has entries that are rational functions of $X$'s entries with denominator $\det(A + CX)$, hence smooth on the domain.

> [!note]- Derivation
> *Cramer's rule.* For an invertible $k \times k$ matrix $M$, $M^{-1}_{ij} = \mathrm{cof}_{ji}(M) / \det M$, where $\mathrm{cof}$ denotes the cofactor (a polynomial in the entries). So $(A + CX)^{-1}$ has entries that are polynomial in the entries of $A + CX$ — hence polynomial in the entries of $X$ — divided by $\det(A + CX)$, another polynomial in the entries of $X$.
>
> *Product with $B + DX$.* The product $(B + DX)(A + CX)^{-1}$ has entries that are polynomial in the entries of $X$ divided by $\det(A + CX)$. Since $\det(A + CX) \neq 0$ on the domain (precisely $\varphi_{P,Q}(U_Q \cap U_{Q'})$), the rational function is smooth on this open domain.
>
> *Domain is open in $L(P, Q)$.* The condition $\det(A + CX) \neq 0$ is the locus where a continuous (polynomial) function is nonzero, hence open.
>
> *Inverse transition.* By symmetry (swap roles of $(P, Q)$ and $(P', Q')$), the inverse transition is also a matrix-Möbius transformation, also smooth on its open domain.
>
> So the two charts $(U_Q, \varphi_{P,Q})$ and $(U_{Q'}, \varphi_{P', Q'})$ are smoothly compatible.

**Step 5: Apply the smooth manifold chart lemma (Lee 1.35).**

The chart lemma's hypotheses:
- (i) Each $\varphi_{P, Q}$ is a bijection onto $L(P, Q) \cong \mathbb{R}^{k(n-k)}$ (Step 2). ✓
- (ii) For two charts, the image $\varphi_{P, Q}(U_Q \cap U_{Q'})$ is open in $L(P, Q)$ (it is the locus where $\det(A + CX) \neq 0$, the open set where a polynomial is nonzero). ✓
- (iii) The transition functions are smooth (Step 4). ✓
- (iv) Countably many charts cover $G_k(V)$. In fact, *finitely many* charts cover: choose a basis $(e_1, \dots, e_n)$ of $V$; for each subset $J \subseteq \{1, \dots, n\}$ with $|J| = n - k$, let $P_J = \mathrm{span}(e_i : i \notin J)$ and $Q_J = \mathrm{span}(e_j : j \in J)$. By Lee Exercise B.9, every $k$-subspace $S$ has trivial intersection with $Q_J$ for some $J$ — hence is in some $U_{Q_J}$. The total number of such charts is $\binom{n}{n-k} = \binom{n}{k}$. ✓
- (v) Hausdorff: any two distinct $k$-subspaces $S_1, S_2 \in G_k(V)$ can be placed in a common chart (find a $(n-k)$-subspace $Q$ disjoint from both $S_1$ and $S_2$; both lie in $U_Q$, where they are separated by the Hausdorff topology of $L(P, Q) \cong \mathbb{R}^{k(n-k)}$). ✓

By Lee 1.35, $G_k(V)$ inherits a unique topology and smooth manifold structure such that each chart $(U_Q, \varphi_{P, Q})$ is smooth. The dimension is $\dim L(P, Q) = k(n-k)$.

> [!note]- Derivation
> *Hypothesis (v) in detail.* Given distinct $S_1, S_2 \in G_k(V)$, we need a chart containing both. Since $\dim(S_1 + S_2) \leq 2k$, the union $S_1 \cup S_2$ does not span $V$ (assuming $2k < n$; the case $2k \geq n$ needs separate treatment but is similar). Find a basis of $V$ extending a basis of $S_1 + S_2$ and choose $Q$ to be the span of basis elements outside $S_1 + S_2$ — then $\dim Q = n - \dim(S_1 + S_2) \geq n - 2k$. For $2k < n$, $\dim Q \geq 1$. We need $\dim Q = n - k$, which we can ensure by choosing $Q$ of that dimension disjoint from $S_1 \cup S_2$ (a generic choice in the appropriate Grassmannian of complements). Then $S_1, S_2 \in U_Q$. The Hausdorff condition in $L(P, Q) \cong \mathbb{R}^{k(n-k)}$ separates $\varphi_{P, Q}(S_1) \neq \varphi_{P, Q}(S_2)$.

> [!note]- Complete formal solution
> **Claim.** The Grassmannian $G_k(V)$ is a smooth manifold of dimension $k(n - k)$, with the smooth structure determined by the charts $(U_Q, \varphi_{P, Q})$ described below.
>
> *Proof.*
>
> **Chart construction.** Fix $V = P \oplus Q$ with $\dim P = k, \dim Q = n - k$. Let $U_Q = \{S \in G_k(V) : S \cap Q = 0\}$. For $S \in U_Q$, define
> $$\varphi_{P, Q}(S) = \pi_Q \circ (\pi_P|_S)^{-1} \in L(P, Q).$$
> The projection $\pi_P|_S : S \to P$ is an isomorphism (injective because $\ker \pi_P \cap S = Q \cap S = 0$, bijective by dimension equality), so the expression is well-defined.
>
> **Bijection $\varphi_{P, Q} : U_Q \to L(P, Q)$.** For any $X \in L(P, Q)$, set $S = \mathrm{graph}(X) = \{p + X(p) : p \in P\}$. $S$ is a $k$-dimensional subspace; $S \cap Q = 0$ (if $p + X(p) = q \in Q$ then projecting to $P$ gives $p = 0$, hence $X(0) = 0 = q$). So $S \in U_Q$, and $\varphi_{P, Q}(S) = X$. The map is a bijection.
>
> **Transition function.** Given another decomposition $V = P' \oplus Q'$, define $A = \pi_{P'}|_P$, $B = \pi_{Q'}|_P$, $C = \pi_{P'}|_Q$, $D = \pi_{Q'}|_Q$. For $X \in \varphi_{P, Q}(U_Q \cap U_{Q'})$ (the open subset where $A + CX$ is invertible), the transition is
> $$\varphi_{P', Q'} \circ \varphi_{P, Q}^{-1}(X) = (B + DX)(A + CX)^{-1} \in L(P', Q').$$
> The derivation: for $S = \mathrm{graph}(X)$, the projection $\pi_{P'}|_S$ corresponds to $p \mapsto (A + CX)(p) \in P'$, the projection $\pi_{Q'}|_S$ to $p \mapsto (B + DX)(p) \in Q'$; the new chart value is $X' = \pi_{Q'}|_S \circ (\pi_{P'}|_S)^{-1} = (B + DX)(A + CX)^{-1}$.
>
> **Smoothness.** By Cramer's rule, $(A + CX)^{-1}$ has entries that are polynomial in $X$'s entries divided by $\det(A + CX) \neq 0$ on the domain. Composition with $B + DX$ (a polynomial in $X$'s entries) gives entries that are rational in $X$'s entries with nonvanishing denominator, hence smooth. By symmetry, the inverse transition is also smooth.
>
> **Smooth manifold chart lemma (Lee 1.35).** The chart maps $\varphi_{P, Q}$ satisfy:
> - (i) bijections onto $L(P, Q) \cong \mathbb{R}^{k(n-k)}$;
> - (ii) chart-image overlaps $\varphi_{P, Q}(U_Q \cap U_{Q'})$ are open in $L(P, Q)$ (locus $\det(A + CX) \neq 0$);
> - (iii) transition functions are smooth;
> - (iv) finitely many chart domains $\{U_{Q_J} : J \subseteq \{1, \dots, n\}, |J| = n - k\}$ cover $G_k(V)$ (Lee Exercise B.9);
> - (v) any two subspaces $S_1, S_2 \in G_k(V)$ are contained in a common chart (find $Q$ trivially intersecting both, by genericity).
>
> By Lee 1.35, $G_k(V)$ has a unique topology and smooth manifold structure such that each $(U_Q, \varphi_{P, Q})$ is a smooth chart, of dimension $\dim L(P, Q) = k(n - k)$. $\blacksquare$

> [!warning] Sanity-check: special cases
> - $k = 1$: $G_1(V) = \mathbb{RP}^{n-1}$, of dimension $1 \cdot (n - 1) = n - 1$. ✓
> - $k = n - 1$: $G_{n-1}(V)$ is the space of hyperplanes (codimension-1 subspaces) in $V$, of dimension $(n-1) \cdot 1 = n - 1$. There is a natural duality $G_{n-1}(V) \cong G_1(V^*) = \mathbb{P}(V^*)$ (the dual projective space).
> - $k = n$: $G_n(V) = \{V\}$, a single point, dimension $0$. The formula $k(n-k) = 0$ confirms.
> - $k = 0$: $G_0(V) = \{0\}$, a single point. Formula $0 \cdot n = 0$.
>
> The Grassmannian $G_k(V)$ is a smooth manifold for all $0 \leq k \leq n$, with $G_0$ and $G_n$ being trivial (one-point) and the interesting cases having $k(n-k) > 0$.

---

# Key Takeaways

**The chart construction via complementary subspaces is the structural prototype.** The argument generalizes: whenever a set of "geometric objects" (subspaces, planes, configurations) parametrized by some auxiliary data (complements, affine slices, base points), one can produce charts by *localizing* to a region where the auxiliary data unambiguously identifies each object. For Grassmannians, the auxiliary data is "a complementary subspace $Q$", and the localization restricts to subspaces "transverse to $Q$". This pattern recurs in flag varieties, classifying spaces, moduli spaces in algebraic geometry, and Higgs bundles. The Grassmannian is the simplest non-trivial example of a moduli space.

**The transition is a *matrix-Möbius transformation* — the projective-geometry analogue of the Möbius transformation on $\mathbb{C}$.** Just as the Möbius transformations $z \mapsto (az + b)/(cz + d)$ are the natural transition functions between charts on the Riemann sphere $\mathbb{CP}^1 = G_1(\mathbb{C}^2)$, the matrix-Möbius transformations $X \mapsto (B + DX)(A + CX)^{-1}$ are the natural transitions on higher-dimensional Grassmannians. This is the deep reason that *the same algebraic structure governs* both classical projective geometry and modern Grassmannian geometry: both are quotients of $\mathrm{GL}$-actions.

**Cramer's rule is the secret weapon for smoothness verification.** The inverse $(A + CX)^{-1}$ might look like a serious obstruction to smoothness, but Cramer's rule writes it as rational functions of the entries — and rational functions with nonvanishing denominators are smooth. This is the same trick used in $\mathbb{RP}^n$ transitions and in the verification that matrix [[Def - Group|groups]] are smooth manifolds. The pattern "matrix inverse via Cramer" appears constantly in differential geometry whenever transition functions involve matrix inversion.

**The Grassmannian has dimension $k(n - k)$ — symmetric in $k$ and $n - k$.** The dimension formula $k(n-k)$ is symmetric in $k$ and $n - k$, reflecting the duality $G_k(V) \cong G_{n-k}(V^*)$ — a $k$-subspace of $V$ corresponds bijectively to an $(n-k)$-subspace of $V^*$ (its [[Def - Annihilator|annihilator]]). This duality is one of the most beautiful structural features of Grassmannian geometry and is the starting point of *projective duality* in algebraic geometry.

**Grassmannians are the *classifying spaces* for vector bundles.** This is the deepest structural fact about Grassmannians. Every smooth rank-$k$ vector bundle $E \to M$ on a paracompact smooth manifold $M$ is the pullback of the *tautological bundle* on $G_k(\mathbb{R}^N)$ for some $N$ — specifically, the bundle whose fibre over $S \in G_k(\mathbb{R}^N)$ is $S$ itself. This is the foundation of **characteristic-class theory** (Chern classes, Stiefel-Whitney classes, Pontryagin classes), which assigns topological invariants to bundles via the cohomology of the Grassmannian. The Grassmannian is the simplest case where the smooth manifold framework crosses into the deep territory of algebraic topology.

**The chart lemma (Lee 1.35) is the master tool for constructing smooth structures.** For most spaces in this chapter ($S^n$, $\mathbb{RP}^n$, $T^n$, matrix Lie [[Def - Group|groups]]), the topology comes "free" from an ambient space or quotient construction, and we don't need the chart lemma. The Grassmannian is an example where the topology is *constructed* from the chart maps — the chart lemma is the right tool. The lemma's five hypotheses are a checklist: bijection-onto-open-set, open chart-overlap-images, smooth transitions, countable cover, Hausdorff separation. Once verified, both topology and smooth structure are produced. This is the *most powerful* construction tool in the chapter.
