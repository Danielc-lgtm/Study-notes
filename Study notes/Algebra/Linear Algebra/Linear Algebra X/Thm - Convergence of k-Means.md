---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Clustering and k-Means"
  - "Def - Norm and Distance"
tags: [algebra, linear-algebra, applied, machine-learning, convergence]
---

# Notation

Throughout, $x_1, \dots, x_N$ are $n$-vectors (the data), $k$ is the number of clusters, $c \in \{1, \dots, k\}^N$ is the assignment vector, $z_1, \dots, z_k$ are the representatives, and $J^\text{clust}(c, z) = (1/N)\sum_i \|x_i - z_{c_i}\|^2$ is the clustering objective.

---

# Statement

> **Theorem (Convergence of $k$-means).** The $k$-means algorithm applied to any finite dataset $x_1, \dots, x_N$ with any initial choice of representatives $z_1, \dots, z_k$ terminates in finitely many iterations, with each iteration weakly decreasing the clustering objective $J^\text{clust}$. The final assignment-representative pair is a local minimum of $J^\text{clust}$ with the following self-consistency:
> - **Assignment optimality:** each $x_i$ is assigned to the nearest representative.
> - **Centroid optimality:** each representative $z_j$ is the centroid of its assigned points.

> **Corollary (Bound on number of iterations).** Since each iteration either decreases $J^\text{clust}$ strictly or leaves $(c, z)$ unchanged, and there are at most $k^N$ possible assignments, the algorithm terminates in at most $k^N$ iterations. In practice, convergence typically occurs in tens to hundreds of iterations regardless of the data size.

The theorem says nothing about *global* optimality: the local minimum reached can be sub-optimal, and different initialisations can lead to different local minima with different objective values.

---

# Motivation

The $k$-means algorithm is a heuristic — it does not always find the global minimum of $J^\text{clust}$, which is an NP-hard combinatorial problem. The question this theorem answers is: *does the algorithm at least always terminate?* And: *does it always reduce the objective?* Without these two guarantees, the algorithm would not be reliable; with them, we know that running $k$-means is at least safe (the objective never grows) and finite (we get an answer in bounded time).

The argument is structural rather than analytical: the objective is a *finite-valued* function of a *finite* state space (the set of partitions), and each step either improves the state or leaves it fixed. By pigeonhole on the finitely many partitions, the algorithm must stabilise. This is the same argument that proves termination of many discrete optimisation algorithms (the simplex method on non-degenerate problems, local search on combinatorial problems).

The deeper question — *how fast* does the algorithm converge? — is more subtle and depends on the geometry of the data. In the worst case the algorithm can take exponentially many iterations to converge, but in practice it converges in well under $50$ iterations on most real datasets. The theorem guarantees finite convergence; it does not bound the rate.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis of the theorem is bare: *any finite set of vectors in $\mathbb R^n$*. The implicit hypothesis is that the squared Euclidean distance is used; this is what makes Step 2 (the centroid update) closed-form.

**Source 1 — alternative distance functions.** If we replace squared Euclidean distance by another **Bregman divergence** $D_\phi(x, z) = \phi(x) - \phi(z) - \nabla\phi(z)^T(x - z)$ for a strictly convex $\phi$, the same alternating algorithm works: Step 2 becomes the "minimiser of $\sum_i D_\phi(x_i, z)$ in $z$", which still has a closed form (the Bregman centroid). Convergence by the same monotonicity argument. The bridge: any Bregman divergence has a unique centroid that minimises the sum of divergences, mirroring the squared-Euclidean case.

**Source 2 — high-dimensional sparse data.** When $N$ is huge and $n$ is huge but each $x_i$ is sparse (most entries zero), the algorithm still converges, and each iteration costs $O(N k \cdot \text{nnz})$ rather than $O(Nkn)$ — sparsity is exploited at the assignment step (distance computations are fast when $x_i$ is sparse) and the update step (centroid is dense, but its update from a small change in assignments can be incremental). The bridge: structural sparsity does not affect the algorithm's correctness, only its computational cost.

**Source 3 — constrained $k$-means.** If some data points are required to be in specific clusters (semi-supervised clustering), or clusters are required to have balanced sizes, the algorithm modifies Step 1 to respect the constraints while still minimising $J^\text{clust}$ in each step. Convergence still holds, because the monotonicity argument is unaffected. The bridge: adding constraints does not break the alternating-minimisation structure.

**Targets (Output Amplification)**

**Target 1 — local minimum + initialization sensitivity.** Knowing that $k$-means converges to a local minimum tells us nothing about the global minimum, but combined with the observation that *different initialisations give different local minima*, it gives a practical algorithm: run $k$-means from many random initialisations and keep the best result. This is the standard practice. The combination of "finite convergence" and "initialisation-dependent local minima" is what makes the multi-start strategy work.

**Target 2 — finite-time termination + objective monotonicity = useful as a heuristic.** Combined with the observation that the objective is bounded below by $0$, the monotonicity gives a *convergence check*: stop the algorithm when $J^\text{clust}$ no longer decreases (typically when the relative decrease falls below some threshold like $10^{-4}$). This is the standard early-stopping criterion.

**Target 3 — Voronoi partition structure.** The final assignment satisfies a Voronoi property: $c_i = j$ iff $z_j$ is closer to $x_i$ than any other $z_l$. So the partition of $\mathbb R^n$ induced by the final $z_1, \dots, z_k$ is exactly the Voronoi diagram of the representatives, and the data points are assigned to their Voronoi cells. Combined with the centroid property, this gives the **Lloyd-Max** vector quantizer condition: the codebook is the centroid of its Voronoi cell. This is the source–target combination underlying optimal vector quantization in information theory.

---

# Why Is It True

**The mechanism in one bolded line: both steps of the algorithm minimise the same objective function over a single variable each (with the other fixed), so neither step can increase the objective; and the state space (the set of partitions) is finite, so the strictly-decreasing sequence of distinct objective values must terminate.**

Step 1 minimises $J^\text{clust}$ over assignments $c$ with representatives $z$ fixed: since $J^\text{clust} = (1/N)\sum_i \|x_i - z_{c_i}\|^2$ decomposes as a sum where the $i$-th term depends only on $c_i$, the minimum is achieved by choosing each $c_i$ independently to minimise $\|x_i - z_{c_i}\|^2$, i.e., the nearest representative. Step 2 minimises $J^\text{clust}$ over representatives $z$ with assignment $c$ fixed: again the objective decomposes as $\sum_j \sum_{i \in G_j} \|x_i - z_j\|^2$ where the $j$-th group of terms depends only on $z_j$, and the minimum is the centroid. So both steps move from $(c, z)$ to a new $(c', z')$ with $J^\text{clust}(c', z') \leq J^\text{clust}(c, z)$.

The finiteness argument is even simpler: there are at most $k^N$ possible assignments (each of $N$ data points is assigned to one of $k$ clusters). For each fixed assignment $c$, the optimal representatives are uniquely determined (centroids). So the joint state space, after each iteration, lies in a finite set of "canonical" $(c, z)$ pairs where $z$ is the centroid of $c$. The sequence of objective values, being weakly decreasing and bounded below by $0$, can take only finitely many distinct values. So the algorithm reaches a state where Step 1 does not change the assignment (otherwise $J^\text{clust}$ would strictly decrease), and at that point Step 2 also leaves $z$ fixed. Convergence.

A subtle point: the algorithm *strictly* decreases the objective on each iteration unless $(c, z)$ is at a fixed point. So either $J^\text{clust}$ decreases strictly (which can happen only finitely many times among the $k^N$ partitions) or the iteration is at a fixed point. Combining: the algorithm reaches a fixed point in $\leq k^N$ steps, in the worst case.

---

# What Makes This Hard

The proof is short and the structure is elementary, but the subtlety lies in seeing that Step 1 and Step 2 *both* minimise the same objective. A common misunderstanding is that the two steps optimise different criteria — they do not. They each minimise $J^\text{clust}$ over one variable with the other fixed; this is what makes the algorithm an alternating *minimisation* procedure rather than, say, an alternating gradient step or some other heuristic. Recognising this is the key step.

A second subtlety is the difference between *convergence* and *convergence to the global optimum*. The theorem guarantees only finite convergence to a local minimum. Many naive presentations of $k$-means overstate its guarantees; the careful statement is that the algorithm always terminates and never makes things worse, not that it always finds the best clustering.

A third subtle point: the algorithm can converge to a state where one or more clusters are *empty*. This is technically possible if a representative ends up far from every data point in the assignment step. Boyd's convention is to drop empty clusters; alternative implementations re-initialise empty clusters by perturbing the largest cluster.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Show that each step of the algorithm weakly decreases the clustering objective. Since the algorithm visits only finitely many distinct partitions and the objective takes finitely many distinct values on those partitions, it must stabilise.

**Subgoal decomposition:**

1. **Step 1 weakly decreases $J^\text{clust}$.** Given $(c, z)$, the new assignment $c'$ (Step 1) satisfies $J^\text{clust}(c', z) \leq J^\text{clust}(c, z)$.
   - *Hint:* $J^\text{clust}(c, z) = (1/N)\sum_i \|x_i - z_{c_i}\|^2$ is a sum of $N$ terms; the $i$-th term depends only on $c_i$ (with $z$ fixed). Optimising each term independently gives the nearest-representative assignment.
   - *Why needed:* This is one half of the monotonicity argument.

2. **Step 2 weakly decreases $J^\text{clust}$.** Given $(c, z)$, the new representatives $z'$ (centroids; Step 2) satisfy $J^\text{clust}(c, z') \leq J^\text{clust}(c, z)$.
   - *Hint:* $J^\text{clust}(c, z) = (1/N)\sum_j \sum_{i \in G_j}\|x_i - z_j\|^2$ is a sum of $k$ groups of terms; the $j$-th group depends only on $z_j$. The minimiser of $\sum_{i \in G_j}\|x_i - z\|^2$ over $z$ is the centroid $\bar x_j = (1/|G_j|)\sum_{i \in G_j} x_i$.
   - *Why needed:* This is the other half of the monotonicity argument.

3. **Centroid uniquely minimises the squared-distance sum.** $\sum_{i \in G}\|x_i - z\|^2$ has a unique minimiser at $z = \bar x = (1/|G|)\sum_{i \in G} x_i$.
   - *Hint:* Expand $\sum_i\|x_i - z\|^2 = \sum_i\|x_i\|^2 - 2 z^T \sum_i x_i + |G|\|z\|^2$, a quadratic in $z$; complete the square.
   - *Why needed:* Justifies Step 2's centroid update as the optimal choice.

4. **Finite-state termination.** The number of distinct assignments is at most $k^N$. Since each step weakly decreases $J^\text{clust}$ and the algorithm visits only finitely many distinct $(c, z)$ pairs (because $z$ is determined by $c$ via centroids), the sequence of objective values is finite and decreasing, hence stabilises in at most $k^N$ steps.
   - *Hint:* If the algorithm did not terminate, it would visit infinitely many distinct $(c, z)$ pairs; but there are only finitely many.
   - *Why needed:* This converts monotonicity into finite-time termination.

---

# Lemma Decomposition

> [!note]- Lemma 1: Centroid minimises sum of squared distances
> **Statement:** Let $x_1, \dots, x_L \in \mathbb R^n$. The function $J(z) = \sum_{i=1}^L \|x_i - z\|^2$ has a unique global minimiser at the centroid $\bar x = (1/L)\sum_i x_i$.
>
> **Hint:** Expand the squared norm using $\|x_i - z\|^2 = \|x_i - \bar x\|^2 - 2(x_i - \bar x)^T(z - \bar x) + \|z - \bar x\|^2$. The cross-term sums to zero.
>
> **Why needed:** This is the closed-form solution for Step 2 of $k$-means.
>
> > [!note]- Full proof
> > For any $z$, write each summand as $\|x_i - \bar x - (z - \bar x)\|^2$. Expanding:
> > $$\|x_i - z\|^2 = \|x_i - \bar x\|^2 - 2(x_i - \bar x)^T(z - \bar x) + \|z - \bar x\|^2.$$
> > Summing over $i$:
> > $$J(z) = \sum_i\|x_i - \bar x\|^2 - 2(z - \bar x)^T \sum_i(x_i - \bar x) + L\|z - \bar x\|^2.$$
> > The middle sum is $\sum_i(x_i - \bar x) = \sum_i x_i - L\bar x = L\bar x - L\bar x = 0$. So
> > $$J(z) = \sum_i\|x_i - \bar x\|^2 + L\|z - \bar x\|^2.$$
> > The first term is independent of $z$. The second is non-negative and zero iff $z = \bar x$. So $J(z) \geq \sum_i\|x_i - \bar x\|^2$, with equality iff $z = \bar x$. Hence $\bar x$ is the unique global minimiser.

> [!note]- Lemma 2: Nearest-representative assignment minimises $J^\text{clust}$ over $c$
> **Statement:** Given fixed representatives $z_1, \dots, z_k$, the assignment $c^* \in \{1, \dots, k\}^N$ defined by $c^*_i = \arg\min_j \|x_i - z_j\|$ achieves $J^\text{clust}(c^*, z) = \min_c J^\text{clust}(c, z)$.
>
> **Hint:** The objective decomposes as $J^\text{clust} = (1/N)\sum_i\|x_i - z_{c_i}\|^2$, with the $i$-th term depending only on $c_i$. Minimise term by term.
>
> **Why needed:** This is the optimality of Step 1 of $k$-means.
>
> > [!note]- Full proof
> > $J^\text{clust}(c, z) = (1/N)\sum_{i=1}^N\|x_i - z_{c_i}\|^2$. For each $i$, the $i$-th term $\|x_i - z_{c_i}\|^2$ depends only on $c_i$ (since $z$ is fixed). To minimise the sum over $c$, minimise each term independently: choose $c_i$ to make $\|x_i - z_{c_i}\|^2$ as small as possible, i.e., set $c^*_i = \arg\min_j \|x_i - z_j\|^2 = \arg\min_j \|x_i - z_j\|$. Ties can be broken by smallest index (or arbitrarily). The resulting $c^*$ minimises every term, hence minimises the sum.

> [!note]- Lemma 3: Finite state space and monotonicity imply finite termination
> **Statement:** Let $f : S \to \mathbb R$ be a function on a finite set $S$, and let $T : S \to S$ be a map with $f(T(s)) \leq f(s)$ for all $s$. Then for any $s_0 \in S$, the sequence $s_0, T(s_0), T^2(s_0), \dots$ becomes eventually constant: there exists $K$ with $T^k(s_0) = T^K(s_0)$ for all $k \geq K$.
>
> **Hint:** The sequence $f(s_0), f(T(s_0)), f(T^2(s_0)), \dots$ is weakly decreasing, and there are only finitely many possible values (since $S$ is finite). So the sequence is eventually constant.
>
> **Why needed:** This is the abstract reason $k$-means terminates: the state space is finite (one element per distinct partition, with $z$ determined by $c$), the objective is monotone non-increasing under iteration, hence the sequence is eventually constant.
>
> > [!note]- Full proof
> > The set $f(S) = \{f(s) : s \in S\}$ is finite (a subset of $\mathbb R$ of size $\leq |S|$). The sequence $f(T^k(s_0))$ is weakly decreasing and takes values in $f(S)$, so it must take some value $v$ infinitely often; by monotonicity, after the first occurrence of $v$, all later values equal $v$. So $f(T^k(s_0)) = v$ for all $k \geq K$ for some $K$. To see that $T^k(s_0)$ itself is eventually constant: the set $\{s \in S : f(s) = v\}$ is finite, and $T$ maps this set into itself (any image has objective $\leq v$, but in the "constant" regime the objective is exactly $v$). On a finite set, iteration of any map eventually cycles; if $f$ is strictly decreasing on any non-trivial cycle this contradicts $f = v$. So the iteration is eventually a fixed point. (For $k$-means, the relevant $T$ is two-step: Step 1 followed by Step 2; the argument works the same.)

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** The $k$-means algorithm applied to any finite dataset terminates in finitely many iterations, with each iteration weakly decreasing the clustering objective $J^\text{clust}$.
>
> *Proof.* The algorithm alternates two steps. We show each step weakly decreases $J^\text{clust}$, then use finiteness of the state space.
>
> **Step 1 (assignment) weakly decreases $J^\text{clust}$.** Let $(c, z)$ be the current state, and $c'$ be the assignment after Step 1. By Lemma 2, $c'$ minimises $J^\text{clust}(c, z)$ over $c$ with $z$ fixed. So $J^\text{clust}(c', z) \leq J^\text{clust}(c, z)$.
>
> **Step 2 (update) weakly decreases $J^\text{clust}$.** Let $(c, z)$ be the state after Step 1, and $z'$ be the representatives after Step 2. By the centroid update, $z'_j = \bar x_j = (1/|G_j|)\sum_{i \in G_j} x_i$ for each non-empty group $G_j$. By Lemma 1 applied to each group, this $z'_j$ minimises $\sum_{i \in G_j}\|x_i - z\|^2$ over $z$. Summing over $j$ and dividing by $N$, $z'$ minimises $J^\text{clust}(c, z)$ over $z$ with $c$ fixed. So $J^\text{clust}(c, z') \leq J^\text{clust}(c, z)$.
>
> Combining, each full iteration of $k$-means weakly decreases $J^\text{clust}$.
>
> **Finite termination.** At every iteration after Step 2, the state $(c, z)$ has $z$ uniquely determined by $c$ (via centroids on non-empty groups; empty groups are dropped). So the state space, post-Step-2, is in bijection with the set of partitions of $\{1, \dots, N\}$ into at most $k$ non-empty groups — a finite set of size at most $S(N, k) \leq k^N$ (Stirling-number bound).
>
> By Lemma 3, applied to the iteration map on this finite state space with objective $J^\text{clust}$, the sequence $(c^{(t)}, z^{(t)})$ becomes eventually constant: there is some $T$ with $(c^{(t)}, z^{(t)}) = (c^{(T)}, z^{(T)})$ for all $t \geq T$. At this $T$, Step 1 does not change the assignment (else $J^\text{clust}$ would strictly decrease), and Step 2 does not change the representatives (else $J^\text{clust}$ would strictly decrease). So the algorithm has converged.
>
> $\blacksquare$
>
> **Optimality of the converged state.** At convergence: every $x_i$ is assigned to a nearest representative (Step 1 fixed-point), and every representative is the centroid of its group (Step 2 fixed-point). These are the two "self-consistency" conditions defining a *local* minimum of $J^\text{clust}$. The local minimum is not in general the global minimum.

---

# Cross-Field Exercise Suggestions

**Information theory — Lloyd-Max scalar/vector quantization.** The same algorithm applied with the objective $\mathbb E\|X - z_{c(X)}\|^2$ (expected squared distortion) for a continuous source $X$ gives the **Lloyd-Max** quantizer, which is optimal for memoryless Gaussian sources. The "centroids are mean of cells / cells are nearest neighbours of centroids" alternation matches $k$-means exactly. Convergence is to a local minimum of expected distortion.

**Statistics — Expectation-Maximisation (EM) algorithm.** $k$-means is the zero-variance limit of the EM algorithm for fitting a mixture of $k$ Gaussians with shared spherical variance. The monotonicity and termination of EM is proven by an analogous argument: each step optimises a different surrogate function (the E-step's expected complete-data log-likelihood) over one variable, with the other fixed. The structural parallel is exact.

**Numerical linear algebra — alternating least squares for matrix factorization.** Fitting a low-rank approximation $X \approx UV^T$ by alternating: fix $V$, solve for $U$ by least-squares; fix $U$, solve for $V$. Each step is a closed-form least-squares problem, and each step weakly decreases the Frobenius reconstruction error. Convergence is to a local minimum, mirroring $k$-means.

**Operations research — facility location.** The continuous-relaxation of the **discrete facility location** problem — place $k$ facilities in $\mathbb R^n$ to minimise the sum of squared distances of demand points to their nearest facility — has $k$-means as its exact algorithm. The discrete version (where facilities must be at one of finitely many candidate locations) is harder, but the centroid update is replaced by "choose the best candidate within each group", and convergence by the same monotonicity argument holds.

---

# Bridges

- **[[Def - Clustering and k-Means|$k$-means as alternating minimisation]]** — the convergence theorem is the formal justification for the alternating-optimisation paradigm: when an objective is hard to minimise jointly in two variables but easy in each variable with the other fixed, alternating between them produces a monotone non-increasing sequence of objective values, hence finite convergence on finite state spaces. This pattern recurs across machine learning (EM, matrix factorization, ICA) and optimisation (coordinate descent, block coordinate descent, ADMM).

- **EM algorithm for Gaussian mixtures** — the EM algorithm for fitting mixtures of $k$ Gaussians is the *soft* version of $k$-means: cluster memberships become probabilities, centroids become weighted means. The monotonicity argument lifts directly: the E-step (compute responsibilities) and M-step (update parameters) each weakly increase a different quantity (the expected complete-data log-likelihood), and the algorithm converges to a local maximum. The connection becomes formal in the limit where the Gaussian variance goes to zero: EM literally becomes $k$-means.

- **Voronoi diagrams** — at convergence, $k$-means partitions $\mathbb R^n$ into the **Voronoi cells** of the representatives: the assignment region for $z_j$ is the set of points closer to $z_j$ than to any other $z_l$. This connects $k$-means to computational geometry: the Voronoi cells are convex polyhedra, the cells' faces lie on perpendicular bisectors between centroids, and the cell structure is the dual of the Delaunay triangulation.

- **Local-search heuristics in combinatorial optimisation** — the monotonicity-on-finite-state-spaces argument that proves $k$-means convergence is the same argument that proves termination of any *local-search* algorithm: define a finite state space, an objective, and a transition rule that never increases the objective; finite termination follows. Examples: $2$-opt for TSP, hill-climbing for SAT, the simplex method on non-degenerate LPs.

- **Initialization strategies and global optimisation** — the local-minimum nature of $k$-means convergence motivates **smart initialisation** (the $k$-means++ algorithm, which probabilistically selects initial representatives to be spread out) and **multi-start** (run from many random initialisations). These do not provide global-optimisation guarantees but in practice find near-optimal clusterings on most datasets. The theorem itself does not address how to escape local minima; that requires additional algorithmic ideas.
