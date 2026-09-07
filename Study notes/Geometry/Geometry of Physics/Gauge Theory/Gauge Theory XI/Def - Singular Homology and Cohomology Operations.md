---
type: definition
subject: gauge-theory
prereqs: []
tags: [algebraic-topology, homology, cohomology]
---
# Chain-level construction
The singular chain group $C_k(X;R)$ is the free $R$-module on continuous simplices $\sigma:\Delta^k\to X$. The alternating face map
$$\partial\sigma=\sum_{j=0}^k(-1)^j\sigma|_{[v_0,\ldots,\widehat v_j,\ldots,v_k]}$$
satisfies $\partial^2=0$. Thus $H_k(X;R)=\ker\partial_k/\operatorname{im}\partial_{k+1}$. Cochains are $C^k=\operatorname{Hom}(C_k,R)$ with coboundary $\delta\phi=\phi\partial$, and $H^k=\ker\delta/\operatorname{im}\delta$.

# Legal operations
A continuous map induces homology and cohomology maps; homotopic maps induce the same maps. Pairs give long exact sequences. Open decompositions give Mayer–Vietoris. Tensor and Tor terms control products through Künneth and coefficients through the universal coefficient theorem. The cup product
$$H^p(X;R)\otimes H^q(X;R)\to H^{p+q}(X;R)$$
is associative, unital, natural, and graded commutative.

# Core computations
$H_k(S^n;\mathbb Z)$ is $\mathbb Z$ for $k=0,n$ and zero otherwise. $H_{2j}(\mathbb{CP}^n;\mathbb Z)\cong\mathbb Z$ for $0\le j\le n$, with all other groups zero. For connected oriented $n$-manifolds, the top-dimensional class becomes the fundamental class.

# Bridge
The Hurewicz theorem identifies the first nonzero homotopy group of a sufficiently connected space with its first nonzero reduced homology group. It explains why homology is the computable linear shadow of homotopy.
