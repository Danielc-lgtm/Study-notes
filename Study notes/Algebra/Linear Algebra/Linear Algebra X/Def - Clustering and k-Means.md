---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Norm and Distance"
tags: [algebra, linear-algebra, applied, machine-learning]
---

# Notation

Throughout, $x_1, \dots, x_N$ are $n$-vectors (the **data points**), and $k$ is a positive integer at most $N$ (the **number of clusters**). The cluster assignment is an $N$-vector $c \in \{1, \dots, k\}^N$ with $c_i$ the cluster of point $i$. The **group representatives** are $n$-vectors $z_1, \dots, z_k$ — one per cluster. The Euclidean norm is $\|x\|$, distance is $\|x - y\|$. The set of indices in cluster $j$ is $G_j = \{i : c_i = j\}$.

This is a compound page: it defines four interlocking notions — the **clustering problem**, the **clustering objective** $J^\text{clust}$, the **$k$-means algorithm**, and the notion of **group centroids** — because they are bundled into a single conceptual unit and one cannot be understood without the others.

---

# Axiom Motivation

The desideratum is unsupervised: given a large collection of vectors in $\mathbb R^n$, find a way to *group them* into clusters of similar vectors, with no labels or training data provided. This is the workhorse of exploratory data analysis: clustering customer behaviour to identify market segments, clustering documents by topic, clustering pixels for image compression, clustering daily-energy-use vectors to identify customers with swimming pools versus solar panels.

What is a "good" clustering? The natural answer is: each data point should be close to its cluster's representative. Formally, with assignment $c$ and representatives $z_1, \dots, z_k$, the **clustering objective** is the mean squared distance to the assigned representative:
$$J^\text{clust}(c, z) = \frac{1}{N}\sum_{i=1}^N \|x_i - z_{c_i}\|^2.$$
Smaller $J^\text{clust}$ means tighter clusters. This is the quantity to minimise jointly over assignments $c$ and representatives $z_1, \dots, z_k$.

Why squared distance, not distance itself? The squared distance has two virtues. First, it is *differentiable* in $z_j$, so the optimal $z_j$ (with $c$ fixed) has a clean closed form — the centroid. Second, the squared-distance objective rewards minimising both the mean *and* the spread of distances, in the same way that least-squares regression does; it is the natural counterpart to variance and standard deviation. Using $\|x_i - z_{c_i}\|$ (not squared) gives a different objective whose optimal representatives are *medians* (in one [[Def - Dimension|dimension]]) or the more complicated geometric median (in higher [[Def - Dimension|dimensions]]), and the algorithm becomes harder. The squared objective is the Goldilocks choice for tractability.

The full optimisation — minimise $J^\text{clust}$ jointly over $c$ and $z$ — is NP-hard in general; one cannot find the global minimum in any tractable amount of computation for general data. So one resorts to a *heuristic*. The two-variable structure of the objective suggests alternating optimisation: fix one variable, minimise over the other; alternate.

**Step 1 (with $z$ fixed):** for each data point $x_i$, the term $\|x_i - z_{c_i}\|^2$ depends only on $c_i$, so we minimise it by setting $c_i$ to the index of the *nearest* representative: $c_i \in \arg\min_j \|x_i - z_j\|^2$. Each $c_i$ can be optimised independently, and the result is the **nearest-representative assignment**.

**Step 2 (with $c$ fixed):** for each cluster $j$, the contribution to $J^\text{clust}$ is $(1/N)\sum_{i \in G_j} \|x_i - z_j\|^2$, which depends only on $z_j$. The optimal $z_j$ is the **centroid** $(1/|G_j|)\sum_{i \in G_j} x_i$ — the average of the data points in cluster $j$. The proof is a one-line completing-the-square argument: $\sum_{i \in G_j}\|x_i - z\|^2$ as a function of $z$ has a unique global minimiser, the centroid $\bar x_j = (1/|G_j|)\sum_{i \in G_j} x_i$, with $\sum_{i \in G_j}\|x_i - z\|^2 = \sum_{i \in G_j}\|x_i - \bar x_j\|^2 + |G_j|\|z - \bar x_j\|^2$.

Alternating these two steps is the **$k$-means algorithm**, dating to Lloyd (1957). The crucial observation is that each step *decreases* (or holds constant) the objective: Step 1 minimises $J^\text{clust}$ over $c$ with $z$ fixed, Step 2 minimises over $z$ with $c$ fixed, so each step cannot increase $J^\text{clust}$. Since there are only finitely many partitions of $N$ data points into $k$ [[Def - Group|groups]] (at most $k^N$), the sequence of objective values reaches a constant in finitely many steps, and the algorithm terminates. See [[Thm - Convergence of k-Means]].

Why is the algorithm a *heuristic* rather than a guaranteed optimum? Because alternating optimisation can stall at a *local* minimum of $J^\text{clust}$ that is not global. Different initialisations of $z_1, \dots, z_k$ can lead to different final partitions with different objective values. The standard remedy is to run $k$-means many times from random initialisations and keep the best result.

**Why this specific cost function and not some variant?** Two nearby variants are worth naming. (a) **Different distance**: replacing $\|x - z\|^2$ by some other dissimilarity $d(x, z)$ gives a different algorithm (e.g., $k$-medoids for non-Euclidean dissimilarities, the EM algorithm for Gaussian mixture models). (b) **Balanced clusters**: adding a penalty for unbalanced cluster sizes forces clusters to have comparable sizes, useful in applications like load-balancing but not in topic discovery. Boyd's $k$-means uses the simplest possible objective, which is sufficient for most applications.

**Why does the algorithm have $k$ in its name?** Because $k$ — the number of clusters — is the only free parameter. Choosing $k$ is the standard problem in practice: one often runs $k$-means for several values of $k$, plots $J^\text{clust}(k)$, and looks for an "elbow" in the curve where adding another cluster no longer dramatically reduces $J^\text{clust}$.

---

# The Definition

**Clustering.** Given data points $x_1, \dots, x_N \in \mathbb R^n$ and an integer $k \geq 1$, a **clustering** is a pair $(c, z)$ where $c \in \{1, \dots, k\}^N$ is the assignment vector and $z_1, \dots, z_k \in \mathbb R^n$ are the representatives. The clusters are the sets $G_j = \{i : c_i = j\}$ for $j = 1, \dots, k$.

**Clustering objective.** The objective is the mean squared distance to the assigned representative:
$$J^\text{clust}(c, z) = \frac{1}{N}\sum_{i=1}^N \|x_i - z_{c_i}\|^2 = \frac{1}{N}\sum_{j=1}^k \sum_{i \in G_j} \|x_i - z_j\|^2.$$

**Group centroid.** The **centroid** of cluster $j$ is the average of the data points in it:
$$\bar z_j = \frac{1}{|G_j|}\sum_{i \in G_j} x_i.$$
For fixed assignment $c$, the centroid is the unique minimiser of $J^\text{clust}$ over $z_j$.

**$k$-means algorithm.** Initialise $z_1, \dots, z_k$ (e.g., as $k$ randomly chosen data points). Repeat until convergence:
1. **Assignment step.** For each $i = 1, \dots, N$, set $c_i \in \arg\min_j \|x_i - z_j\|$. (Ties are broken by smallest index.)
2. **Update step.** For each $j = 1, \dots, k$ with $G_j \neq \emptyset$, set $z_j \leftarrow (1/|G_j|)\sum_{i \in G_j} x_i$. (Empty [[Def - Group|groups]] are dropped, giving fewer than $k$ clusters.)

**Convergence (see [[Thm - Convergence of k-Means]]).** Each step does not increase $J^\text{clust}$. Since there are only finitely many partitions of $N$ points into $k$ groups, the algorithm terminates after finitely many iterations. The final $(c, z)$ is a *local* minimum of $J^\text{clust}$; running from several random initialisations and keeping the best is the standard practice.

**Complexity.** Each iteration costs $O(Nkn)$ flops: $O(n)$ to compute one distance, $O(Nk)$ distance computations per iteration in Step 1, and $O(Nn)$ for the centroid averages in Step 2. Typically a few tens of iterations suffice for convergence.

---

# Relate to Other Fields / Compression

The $k$-means algorithm is the prototypical **alternating optimisation** algorithm: an objective function $J(c, z)$ that is hard to minimise jointly is easy to minimise in each variable with the other fixed. This pattern recurs throughout machine learning and optimisation: the **Expectation–Maximisation (EM) algorithm** is the probabilistic generalisation, alternating between "compute responsibilities" (the soft analogue of cluster assignments) and "update parameters" (the soft analogue of representatives). When the responsibilities and parameters come from a mixture of Gaussians, EM is essentially "soft $k$-means" — and $k$-means is itself a special case of EM under appropriate degenerate-Gaussian limits.

In information theory, $k$-means with squared-distance loss is the **rate-distortion encoder** for a Gaussian source: the optimal lossy compression of a continuous-valued vector to one of $k$ codewords is the assignment to the nearest centroid, and the optimal codebook consists of the centroids. This connection is exact: $k$-means is the Lloyd-Max scalar/vector quantization algorithm.

In statistics, $k$-means with the squared-distance loss is the **maximum-likelihood estimator** for a mixture of $k$ spherical Gaussians with shared variance, in the limit as the variance $\to 0$ — the "hard EM" limit. This gives the algorithm a principled statistical interpretation.

**True name:** The $k$-means algorithm is *alternating minimisation of the sum-of-squared-distances objective*. The cluster representatives are *centroids* of their assigned points. The clustering is a *Voronoi partition* of $\mathbb R^n$ around the representatives — the assignment region for representative $z_j$ is exactly the set of points closer to $z_j$ than to any other $z_l$.

---

# Examples / Corollaries

**Is an instance — clustering MNIST digits.** Boyd's example: $N = 60000$ images of $28 \times 28$ grayscale handwritten digits, each represented as a vector in $\mathbb R^{784}$. Running $k$-means with $k = 20$ on this dataset produces 20 representative images that, visually, look like prototypes of digits (with some predictable confusions: 4/9, 3/8). The algorithm "discovers" the digit structure with no labels.

**Is an instance — topic discovery from Wikipedia.** A corpus of 500 Wikipedia articles, each represented as a word-count histogram in $\mathbb R^{4423}$. With $k = 9$, $k$-means clusters articles by theme — sports, holidays, biographies, films, music albums — and the cluster representatives' top words make the themes interpretable. The algorithm has not been told what "topic" means; the clustering structure emerges from the data.

**Is an instance — two clusters on a line.** With $k = 2$ and one-dimensional data $\{1, 2, 3, 8, 9, 10\}$, $k$-means typically converges to $G_1 = \{1, 2, 3\}$, $G_2 = \{8, 9, 10\}$, with centroids $z_1 = 2$, $z_2 = 9$. The assignment region is "less than $5.5$" for cluster $1$ and "greater than $5.5$" for cluster $2$, with the boundary at the midpoint of the two centroids.

**Is NOT an instance — non-convex clusters.** $k$-means assumes clusters are roughly spherical (Voronoi cells are convex). For data arranged in two concentric [[Def - Ring|rings]], $k$-means with $k = 2$ does *not* recover the two [[Def - Ring|rings]] — it produces two half-rings, because Voronoi cells cannot wrap around. This is the canonical failure case, motivating spectral clustering and other non-linear methods.

**Is NOT an instance — initialization-dependent failure.** For some datasets, a bad random initialisation leads $k$-means to a poor local minimum. Example: data with three obvious clusters but $k = 3$ initial representatives all near the same cluster. The algorithm converges with two representatives in that cluster and one in a different one, missing the third cluster entirely. The remedy is multiple random restarts.

**Corollary — pre-assigned data points.** If some data points are constrained to specific clusters (semi-supervised clustering), Step 1 is modified to respect the constraints: the assignment $c_i$ is fixed for constrained points, and only unconstrained points are reassigned. The algorithm still converges, by the same monotonicity argument.

**Corollary — non-negativity preservation.** If all data points $x_i$ have non-negative entries, then so do the centroids $\bar z_j$ (averages of non-negative vectors are non-negative). If the data points are histograms (non-negative entries summing to one), the centroids are also histograms. This is what makes $k$-means cluster representatives interpretable as "average word distributions" in topic discovery.

**Corollary — linear separability of $k = 2$ partition.** For $k = 2$, the resulting Voronoi partition is a **hyperplane**: the set of points equidistant from $z_1, z_2$ is the perpendicular bisector of the segment $z_1 z_2$. So two-way $k$-means produces a *linear classifier* in disguise, with weight vector $w = z_1 - z_2$ and intercept $v = (\|z_2\|^2 - \|z_1\|^2)/2$.

**Calibration check.** Verify that the centroid of a one-element cluster is the data point itself (so a singleton cluster has zero contribution to $J^\text{clust}$). Verify that the assignment-step ties can be broken arbitrarily without affecting convergence (the objective value is the same either way). Verify that running $k$-means with $k = N$ gives $J^\text{clust} = 0$ — every point is its own cluster.

---

# Unlocked by This

> [!tip] Expectation–Maximisation Algorithm *(from Probability and Statistics)*
> The **EM algorithm** generalises $k$-means: cluster memberships are *soft* (probabilities $r_{ij}$ summing to $1$ over clusters), and centroids are *weighted averages* (with weights $r_{ij}$). EM converges to a local maximum of a log-likelihood function, with $k$-means recovered as the zero-variance limit. EM is the workhorse of unsupervised learning with latent variables.

> [!tip] Vector Quantization and Lloyd-Max *(from Information Theory)*
> The $k$-means algorithm is the **Lloyd-Max** scalar/vector quantization algorithm, used for lossy data compression (e.g., colour palettes in image compression, speech codecs). The cluster representatives are codewords, the assignment is the encoder, and the objective $J^\text{clust}$ is the average distortion.

> [!tip] Spectral Clustering and Graph Laplacians *(from Machine Learning)*
> When $k$-means fails on non-convex cluster shapes, **spectral clustering** embeds the data into a low-dimensional space via the eigenvectors of a graph Laplacian, then runs $k$-means in the embedded space. This recovers complex cluster shapes by linearising the problem after a non-linear embedding — the spectral version of the kernel trick.
