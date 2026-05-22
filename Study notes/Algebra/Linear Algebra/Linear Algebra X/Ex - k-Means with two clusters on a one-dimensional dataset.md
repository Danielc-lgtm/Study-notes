---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Clustering and k-Means"
  - "Thm - Convergence of k-Means"
tags: [algebra, linear-algebra, applied, machine-learning]
---

# Problem Statement

Run the $k$-means algorithm with $k = 2$ on the one-dimensional dataset $x_1 = 1, x_2 = 2, x_3 = 3, x_4 = 8, x_5 = 9, x_6 = 10$ (each $x_i \in \mathbb R$). Use the initial representatives $z_1 = 0, z_2 = 5$.

(a) Run the algorithm step by step until convergence. Track the cluster assignments and representatives at each iteration.

(b) Show that the final partition is $G_1 = \{1, 2, 3\}$, $G_2 = \{4, 5, 6\}$ with representatives $z_1 = 2, z_2 = 9$, and that this corresponds to the threshold $5.5$ — points below $5.5$ are in cluster $1$, points above are in cluster $2$.

(c) Verify that this is a *global* minimum of the clustering objective $J^\text{clust}$ for this dataset with $k = 2$, by computing $J^\text{clust}$ for any other partition into two non-empty clusters and showing it is larger.

**Recall:**

The $k$-means algorithm alternates: (1) assign each point to the nearest representative, (2) update each representative to the centroid of its assigned points. See [[Def - Clustering and k-Means]].

The clustering objective is $J^\text{clust}(c, z) = (1/N)\sum_i \|x_i - z_{c_i}\|^2$, where $N$ is the number of data points. By [[Thm - Convergence of k-Means]], the algorithm converges in finitely many iterations to a local minimum of $J^\text{clust}$.

---

# Convergent Strategy

**Problem class.** This is a *direct algorithmic execution* — run $k$-means by hand on a small dataset, track the state, and verify convergence and optimality. This kind of exercise is essential for building intuition about how the algorithm works in practice.

**Assumption pattern.** Small dataset ($N = 6$), small $k = 2$, one-dimensional ($n = 1$). The smallness makes the algorithm tractable by hand. The initial representatives are specified — different initialisations would give the same final result on this dataset, but in general $k$-means is initialisation-dependent.

**Theorem routing.** Follow the [[Def - Clustering and k-Means|$k$-means algorithm]] definition mechanically: assignment step, update step, repeat until convergence. Convergence is guaranteed by [[Thm - Convergence of k-Means]]. To verify global optimality, enumerate all possible partitions of $\{1, 2, 3, 4, 5, 6\}$ into two non-empty groups (there are $2^6/2 - 1 = 31$ such partitions, but the symmetry $G_1 \leftrightarrow G_2$ cuts this in half), compute $J^\text{clust}$ for each with the centroids as representatives, and confirm the partition $\{\{1,2,3\}, \{4,5,6\}\}$ has the smallest.

**Key decision point.** The non-obvious insight is that for $k = 2$ on one-dimensional data, the optimal clustering is *threshold-based*: there exists a threshold $\theta$ such that all points $< \theta$ are in one cluster and all points $> \theta$ in the other. This follows because the Voronoi cell boundary between two centroids in $\mathbb R^1$ is the midpoint, so the cluster boundary is the midpoint of the two centroids. Recognising this structural fact reduces the search over partitions to a search over thresholds — much smaller.

---

# Legal Operations Used

1. **Operation 8 (iterate the dynamics matrix... wait, in this case "iterate the algorithm").** Adapted: run $k$-means iteratively, tracking how the objective decreases at each step.

2. **Operation 10 (invoke linear independence... here, invoke the Voronoi structure).** Adapted: the optimal partition's *structure* (threshold-based for $k = 2$ in $\mathbb R$) follows from the centroid-Voronoi self-consistency.

3. **Operation 1 (encode the phenomenon as a vector or matrix).** The dataset is already in vector form — six points on the line.

---

# Hints

> [!note]- Hint 1
> Iteration 1, Step 1: compute $|x_i - z_1|$ and $|x_i - z_2|$ for each $i$, assign $x_i$ to the closer representative.

> [!note]- Hint 2
> Iteration 1, Step 2: for each cluster, average the points assigned to it. The new representative is the centroid.

> [!note]- Hint 3
> Iterate until the assignments do not change. For this dataset, two iterations should suffice.

> [!note]- Hint 4
> For part (c) on global optimality: the optimal partition is threshold-based (all points below threshold in one cluster, all above in the other). Enumerate the $5$ possible thresholds (between each adjacent pair of points), compute the resulting $J^\text{clust}$, and find the minimum.

---

# Solution

The proof has three steps. Step 1 runs $k$-means by hand, tracking the state at each iteration. Step 2 verifies convergence and identifies the threshold structure of the final partition. Step 3 enumerates alternative partitions and confirms global optimality.

**Step 1: Run $k$-means iterations until convergence.**

> [!note]- Derivation
> Initial state: $z_1 = 0$, $z_2 = 5$. No assignments yet.
>
> **Iteration 1, Step 1 (Assignment).** Compute distances:
> | $i$ | $x_i$ | $|x_i - z_1| = |x_i - 0|$ | $|x_i - z_2| = |x_i - 5|$ | Nearest |
> |---|---|---|---|---|
> | 1 | 1 | 1 | 4 | $z_1$ |
> | 2 | 2 | 2 | 3 | $z_1$ |
> | 3 | 3 | 3 | 2 | $z_2$ |
> | 4 | 8 | 8 | 3 | $z_2$ |
> | 5 | 9 | 9 | 4 | $z_2$ |
> | 6 | 10 | 10 | 5 | $z_2$ |
>
> So $c = (1, 1, 2, 2, 2, 2)$: $G_1 = \{1, 2\}$, $G_2 = \{3, 4, 5, 6\}$.
>
> **Iteration 1, Step 2 (Update).** Compute centroids:
> $$z_1 \leftarrow (1 + 2)/2 = 1.5, \quad z_2 \leftarrow (3 + 8 + 9 + 10)/4 = 30/4 = 7.5.$$
>
> **Iteration 2, Step 1 (Assignment).** Compute distances with new representatives:
> | $i$ | $x_i$ | $|x_i - 1.5|$ | $|x_i - 7.5|$ | Nearest |
> |---|---|---|---|---|
> | 1 | 1 | 0.5 | 6.5 | $z_1$ |
> | 2 | 2 | 0.5 | 5.5 | $z_1$ |
> | 3 | 3 | 1.5 | 4.5 | $z_1$ |
> | 4 | 8 | 6.5 | 0.5 | $z_2$ |
> | 5 | 9 | 7.5 | 1.5 | $z_2$ |
> | 6 | 10 | 8.5 | 2.5 | $z_2$ |
>
> So $c = (1, 1, 1, 2, 2, 2)$: $G_1 = \{1, 2, 3\}$, $G_2 = \{4, 5, 6\}$. The assignment of $x_3$ changed from cluster $2$ to cluster $1$.
>
> **Iteration 2, Step 2 (Update).** Compute centroids:
> $$z_1 \leftarrow (1 + 2 + 3)/3 = 2, \quad z_2 \leftarrow (8 + 9 + 10)/3 = 9.$$
>
> **Iteration 3, Step 1.** With $z_1 = 2$, $z_2 = 9$, distances are $|x_i - 2|$ vs $|x_i - 9|$. For $i = 1, 2, 3$: distances are $(1, 0, 1)$ vs $(8, 7, 6)$, all closer to $z_1$. For $i = 4, 5, 6$: distances are $(6, 7, 8)$ vs $(1, 0, 1)$, all closer to $z_2$. So the assignment is unchanged: $c = (1, 1, 1, 2, 2, 2)$. By [[Thm - Convergence of k-Means|the convergence theorem]], if assignments do not change, the algorithm has converged.
>
> **Final state.** $z_1 = 2$, $z_2 = 9$, $G_1 = \{1, 2, 3\}$, $G_2 = \{4, 5, 6\}$.

**Step 2: Identify the threshold structure.**

> [!note]- Derivation
> With representatives $z_1 = 2$ and $z_2 = 9$, the Voronoi boundary in $\mathbb R$ is the midpoint $(2 + 9)/2 = 5.5$. Points with $x_i < 5.5$ are closer to $z_1$ and assigned to cluster $1$; points with $x_i > 5.5$ are closer to $z_2$ and assigned to cluster $2$.
>
> Checking: $x_1, x_2, x_3 = 1, 2, 3$ are all $< 5.5$, assigned to cluster $1$. $x_4, x_5, x_6 = 8, 9, 10$ are all $> 5.5$, assigned to cluster $2$. ✓
>
> In general for $k = 2$ in $\mathbb R^1$, the optimal partition is *always* threshold-based, because Voronoi cells are half-lines.

**Step 3: Verify global optimality by enumeration.**

> [!note]- Derivation
> For $k = 2$ in $\mathbb R^1$ on this dataset, the optimal partition is threshold-based. Enumerate the $5$ possible thresholds (between consecutive data points): $\theta \in \{1.5, 2.5, 5.5, 8.5, 9.5\}$.
>
> For each threshold, compute the centroids and $J^\text{clust}$ (we use $\sum_i \|x_i - z_{c_i}\|^2$, omitting the $1/N$ factor):
>
> - $\theta = 1.5$: $G_1 = \{1\}$, $G_2 = \{2, 3, 4, 5, 6\}$. $z_1 = 1$, $z_2 = (2+3+8+9+10)/5 = 6.4$. $J = 0 + (4.4^2 + 3.4^2 + 1.6^2 + 2.6^2 + 3.6^2) = 0 + 19.36 + 11.56 + 2.56 + 6.76 + 12.96 = 53.2$.
> - $\theta = 2.5$: $G_1 = \{1, 2\}$, $G_2 = \{3, 4, 5, 6\}$. $z_1 = 1.5$, $z_2 = (3+8+9+10)/4 = 7.5$. $J = (0.5^2 + 0.5^2) + (4.5^2 + 0.5^2 + 1.5^2 + 2.5^2) = 0.5 + 20.25 + 0.25 + 2.25 + 6.25 = 29.5$.
> - $\theta = 5.5$: $G_1 = \{1, 2, 3\}$, $G_2 = \{4, 5, 6\}$. $z_1 = 2$, $z_2 = 9$. $J = (1^2 + 0^2 + 1^2) + (1^2 + 0^2 + 1^2) = 2 + 2 = 4$.
> - $\theta = 8.5$: $G_1 = \{1, 2, 3, 4\}$, $G_2 = \{5, 6\}$. $z_1 = (1+2+3+8)/4 = 3.5$, $z_2 = (9+10)/2 = 9.5$. $J = (2.5^2 + 1.5^2 + 0.5^2 + 4.5^2) + (0.5^2 + 0.5^2) = 6.25 + 2.25 + 0.25 + 20.25 + 0.25 + 0.25 = 29.5$.
> - $\theta = 9.5$: $G_1 = \{1, 2, 3, 4, 5\}$, $G_2 = \{6\}$. $z_1 = (1+2+3+8+9)/5 = 4.6$, $z_2 = 10$. $J = (3.6^2 + 2.6^2 + 1.6^2 + 3.4^2 + 4.4^2) + 0 = 12.96 + 6.76 + 2.56 + 11.56 + 19.36 + 0 = 53.2$.
>
> The minimum is at $\theta = 5.5$ with $J = 4$, which matches the $k$-means output. Hence the $k$-means result is a *global* minimum for this dataset.

> [!note]- Complete formal solution
> Initial state: $z_1 = 0$, $z_2 = 5$, dataset $\{1, 2, 3, 8, 9, 10\}$.
>
> *Iteration 1.* Assignment: $x_1, x_2$ (distances $1, 2$ from $z_1$) closer to $z_1$; $x_3$ (distance $2$ from $z_2$ vs $3$ from $z_1$) closer to $z_2$; $x_4, x_5, x_6$ closer to $z_2$. So $G_1^{(1)} = \{1, 2\}$, $G_2^{(1)} = \{3, 4, 5, 6\}$. Update: $z_1 = 1.5$, $z_2 = 7.5$.
>
> *Iteration 2.* Assignment with new $z$: $x_3$ (distance $1.5$ from $z_1$ vs $4.5$ from $z_2$) now closer to $z_1$. So $G_1^{(2)} = \{1, 2, 3\}$, $G_2^{(2)} = \{4, 5, 6\}$. Update: $z_1 = 2$, $z_2 = 9$.
>
> *Iteration 3.* Assignment unchanged. Algorithm converges.
>
> *Final state.* $z_1 = 2$, $z_2 = 9$, $G_1 = \{1, 2, 3\}$, $G_2 = \{4, 5, 6\}$. The Voronoi boundary is at $5.5$, the midpoint of $z_1$ and $z_2$.
>
> *Global optimality.* Since $k = 2$ in $\mathbb R^1$ has threshold-based optimal partitions, enumerate the $5$ thresholds between consecutive points and compute $J^\text{clust}$. The threshold $\theta = 5.5$ yields the minimum value $J = 4$. Hence the $k$-means output is globally optimal for this dataset. $\quad\blacksquare$

---

# Key Takeaways

**$k$-means in one dimension with $k = 2$ produces a threshold classifier.** The Voronoi cell boundary between two representatives in $\mathbb R^1$ is the midpoint, so the cluster boundary at convergence is at $(z_1 + z_2)/2$. This is the cleanest example of the duality between $k$-means and linear classification: $k$-means with $k = 2$ produces a *separating hyperplane* (in $\mathbb R^n$, the perpendicular bisector of the segment connecting the two centroids), which acts as a linear classifier. In higher dimensions and with more clusters, the boundaries become piecewise-linear Voronoi diagrams, but the structural insight — "cluster boundary = perpendicular bisector of centroids" — generalises directly.

**Initialisation matters in general but not on simple datasets.** For this specific dataset, the initialisation $z_1 = 0, z_2 = 5$ leads to the global optimum. But other initialisations could lead to different local minima — for example, $z_1 = 1.5, z_2 = 8.5$ would converge to the same global optimum, but $z_1 = 2, z_2 = 3$ might converge to a *suboptimal* partition like $G_1 = \{1, 2\}, G_2 = \{3, 4, 5, 6\}$ with $J = 29.5$. The trigger-reaction pattern in practice: *run $k$-means from many random initialisations and keep the best result*. This is the standard remedy for the algorithm's initialisation-sensitivity.

**Enumerating partitions is feasible for small $N$, but the structural insight (threshold-based partition) is what scales.** For this six-point dataset, brute-force enumeration of $5$ thresholds takes a few seconds by hand. For $N = 100$ points there are $99$ thresholds — still tractable. For $N = 10^6$ points the threshold approach is $O(N \log N)$ if one sorts the data first (the sort is the dominant cost), and remains fast. The lesson is that *structural insight reduces the search space*: instead of considering all $2^{N-1} - 1$ partitions into two non-empty groups, the threshold structure shows that only $N - 1$ partitions are candidates. This kind of structural compression is what makes algorithms scale, and recognising the threshold structure here is the same kind of insight that makes spectral clustering tractable in high dimensions.
