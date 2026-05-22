---
type: definition
subject: linear-algebra
prereqs:
tags: [algebra, linear-algebra, applied, graph-theory]
---

# Notation

A **directed graph** is a pair $G = (V, E)$ where $V = \{1, \dots, n\}$ is the vertex set and $E$ is the edge set with edges labelled $1, \dots, m$. Each edge $j$ has a **head** (the node it points to) and a **tail** (the node it points from). The incidence matrix is $A \in \mathbb R^{n \times m}$. Flows on edges form an $m$-vector $f$; node potentials and source flows form $n$-vectors $v$ and $s$.

---

# Axiom Motivation

The desideratum is to encode *all* the structure of a directed graph in a single matrix, in a way that exposes the natural linear-algebraic operations on flows and potentials. The graph has two natural types of data: data attached to *vertices* (an $n$-vector — temperatures, prices, populations) and data attached to *edges* (an $m$-vector — flows, currents, transports). The matrix should let us convert between these two types fluently.

The construction is forced once we ask: **what is the right matrix to encode "edge $j$ points from node $\operatorname{tail}(j)$ to node $\operatorname{head}(j)$"?** The natural choice is a matrix whose $(i, j)$ entry is $+1$ if edge $j$ points *into* node $i$ (i.e., $i = \operatorname{head}(j)$), $-1$ if it points *out of* node $i$ (i.e., $i = \operatorname{tail}(j)$), and $0$ otherwise. Each column of $A$ thus has exactly two nonzero entries — a $+1$ and a $-1$ — encoding the head and tail of one edge.

This sign convention is what makes the central identity work: **$Af$ is the net inflow at each node**. To see why: $(Af)_i = \sum_j A_{ij} f_j$, and only edges incident to node $i$ contribute. An incoming edge $j$ (with $A_{ij} = +1$) contributes $+f_j$; an outgoing edge $j$ (with $A_{ij} = -1$) contributes $-f_j$. So $(Af)_i$ sums the inflows minus the outflows at node $i$ — exactly the **net inflow**, called the **flow surplus**. If $(Af)_i > 0$, more flow comes in than goes out and node $i$ accumulates material; if $(Af)_i < 0$, it sheds material.

The dual identity is **$A^T v$ is the edge potential drop**. The transpose $A^T$ has dimensions $m \times n$; given a node potential vector $v$ (one number per node), its product $A^T v$ has one number per edge. Working through the algebra: $(A^T v)_j = \sum_i A_{ij} v_i$, and only the two nonzero rows contribute: $(A^T v)_j = v_{\operatorname{head}(j)} - v_{\operatorname{tail}(j)}$, the potential at the head minus at the tail. If $v$ represents an electrical potential or temperature, $A^T v$ is the voltage drop across each edge.

What happens if we **drop the sign convention** and use a $\{0, 1\}$ matrix instead, with $A_{ij} = 1$ iff edge $j$ is incident to node $i$? Then the matrix is unsigned: it tells you *which* edges touch each node but not *which direction* the edge points. The flow-conservation interpretation $Af = $ "net inflow" breaks, because the matrix cannot distinguish the contributions of incoming and outgoing edges. The unsigned incidence matrix is sometimes used in graph theory, but it loses the linear-algebra-of-flows interpretation.

What if we **strengthened** by including edge weights — replacing $\pm 1$ with $\pm w_j$ for some weights $w_j$? This gives a *weighted* incidence matrix, which corresponds to a network where each edge has a capacity or resistance. The unweighted version is the cleanest starting point; weighted versions arise naturally and easily as $A \operatorname{diag}(w)$ or $\operatorname{diag}(w) A^T$ depending on whether weights live on edges or nodes.

**Why two nonzero entries per column?** Because each edge has exactly two endpoints — a head and a tail. This is the structural constraint built into the directed-graph definition. It is also what gives the incidence matrix its sparse structure: exactly $2m$ nonzero entries out of $nm$, which is a tiny fraction for graphs with $m \ll n^2$ (the common case).

**Why is the construction asymmetric?** Because directed graphs are asymmetric: an edge from node $5$ to node $7$ is different from an edge from node $7$ to node $5$. The $\pm 1$ pattern records this asymmetry. For an *undirected* graph, one can choose an arbitrary orientation of each edge to define the incidence matrix; many quantities (like the graph Laplacian $A A^T$) come out the same regardless of the orientation choice.

---

# The Definition

Let $G = (V, E)$ be a directed graph with $n = |V|$ vertices and $m = |E|$ edges. The **incidence matrix** of $G$ is the $n \times m$ matrix $A$ with entries
$$
A_{ij} = \begin{cases} +1 & \text{if edge } j \text{ points to node } i \text{ (}i = \operatorname{head}(j)\text{)},\\ -1 & \text{if edge } j \text{ points from node } i \text{ (}i = \operatorname{tail}(j)\text{)},\\ 0 & \text{otherwise.} \end{cases}
$$
Each column of $A$ has exactly two nonzero entries: a $+1$ in the head row and a $-1$ in the tail row.

**Flow conservation.** For an $m$-vector $f$ of edge flows and an $n$-vector $s$ of source/sink flows (positive at sources, negative at sinks), the **flow conservation equation** is
$$A f + s = 0.$$
The $i$-th component reads: (net inflow from edges) $+$ (external source flow) $= 0$ at node $i$.

**Potential differences.** For an $n$-vector $v$ of node potentials, the **edge potential drops** are
$$A^T v \in \mathbb R^m, \quad (A^T v)_j = v_{\operatorname{head}(j)} - v_{\operatorname{tail}(j)}.$$

**Circulation.** A flow vector $f$ with $Af = 0$ is called a **circulation**: there is no net inflow or outflow at any node, and the flow simply circulates around the graph.

**Dirichlet energy.** For a node potential $v \in \mathbb R^n$, the **Dirichlet energy** is
$$D(v) = \|A^T v\|^2 = \sum_{\text{edges } (k, l)} (v_l - v_k)^2,$$
the sum of squared potential differences across the edges. The Dirichlet energy measures the roughness of $v$ across the graph: small $D(v)$ means $v$ varies smoothly (adjacent nodes have similar potentials), while large $D(v)$ means $v$ is rough (sharp variations across edges).

**Graph Laplacian.** The matrix $L = A A^T$ is the **graph Laplacian** (up to sign convention). It is symmetric positive semidefinite, with $\mathbf 1$ in its kernel (a constant potential has Dirichlet energy zero), and its second-smallest eigenvalue (the **Fiedler value**) measures graph connectivity.

---

# Relate to Other Fields / Compression

The incidence matrix is the bridge from linear algebra to graph theory. The same matrix encodes the directed-graph structure, the flow-conservation laws (Kirchhoff's current law in electrical networks), the potential-drop laws (Kirchhoff's voltage law), and the heat-equation Laplacian. The graph Laplacian $L = AA^T$ is the discrete analog of the continuous Laplacian operator $-\Delta$, with the boundary conditions encoded by the graph's structure.

In **physics**, networks of resistors, capacitors, and inductors are encoded by their incidence matrices, with flow conservation being conservation of charge and potential drops being voltages. The classic Tellegen's theorem of network analysis — power into the network equals power dissipated — is a direct consequence of $f^T(A^T v) = (Af)^T v = -s^T v$, which says that power flowing out equals minus the power supplied by the sources.

In **probability**, the graph Laplacian is the generator of the simple random walk on the graph: the transition matrix of the random walk is $P = I - L/d_{\max}$, where $d_{\max}$ is the maximum degree, and the random walk's mixing time is controlled by the spectral gap of $L$ (the Fiedler value).

In **machine learning and unsupervised learning**, the graph Laplacian is the central object of **spectral graph theory** and **spectral clustering**: cluster the nodes of a similarity graph by taking the eigenvectors of $L$ corresponding to the smallest eigenvalues, then $k$-means in that embedded space.

**True name:** The incidence matrix is *the linear map that converts edge data to node data via signed summation*. Equivalently, it is *the coboundary operator from $0$-cochains to $1$-cochains in the simplicial cohomology of the graph*, in the language of algebraic topology.

---

# Examples / Corollaries

**Is an instance — Boyd's $4$-node graph.** A graph with $4$ vertices and $5$ edges (the diamond with one diagonal), with edges labelled $1, \dots, 5$. The incidence matrix is
$$A = \begin{pmatrix} -1 & -1 & 0 & 1 & 0 \\ 1 & 0 & -1 & 0 & 0 \\ 0 & 0 & 1 & -1 & -1 \\ 0 & 1 & 0 & 0 & 1 \end{pmatrix}.$$
Each column has a $+1$ and a $-1$. The flow vector $f = (1, -1, 1, 0, 1)$ satisfies $Af = 0$, so it is a circulation: a unit clockwise flow on the outer edges with no flow on the diagonal.

**Is an instance — chain graph.** For a chain graph with $n$ nodes connected in a line and $n - 1$ edges (each edge going from node $i$ to node $i+1$), the incidence matrix is $n \times (n-1)$ with structure
$$A = \begin{pmatrix} -1 & 0 & \cdots & 0 \\ 1 & -1 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & & \ddots & \\ 0 & 0 & \cdots & 1 \end{pmatrix}.$$
The transpose $A^T$ is exactly the **difference matrix** $D$ acting on $n$-vectors: $(A^T v)_j = v_{j+1} - v_j$. So the chain incidence matrix encodes the discrete first-derivative operator.

**Is an instance — power grid.** For an electrical power grid with $n$ substations and $m$ transmission lines, $A$ is the incidence matrix, $f$ is the vector of line currents, $s$ is the vector of substation injections (generators positive, loads negative). Kirchhoff's current law $Af + s = 0$ at every substation is exactly the flow conservation equation.

**Is NOT an instance — adjacency matrix.** The **adjacency matrix** $\operatorname{Adj}(G) \in \{0, 1\}^{n \times n}$ has $\operatorname{Adj}(G)_{ik} = 1$ iff there is an edge from $k$ to $i$. This is a *different* matrix from the incidence matrix — different dimensions ($n \times n$ vs $n \times m$), different sign structure, different operational role. The adjacency matrix is used for counting paths via $\operatorname{Adj}(G)^\ell$ (see [[Linear Algebra X — Applied I — Vectors, Distance, Equations, Dynamics|Boyd §10.3]]) but does not interact with flows in the linear-algebraic way the incidence matrix does.

**Is NOT an instance — self-loops.** An edge from a vertex to itself (a self-loop) would have $\operatorname{head}(j) = \operatorname{tail}(j)$, so $A_{ij}$ would be both $+1$ and $-1$, hence $0$. The incidence matrix cannot represent self-loops; these need a separate convention (e.g., a diagonal correction).

**Corollary — rows sum to zero in each column.** The sum of entries in each column of $A$ is $+1 + (-1) = 0$. Equivalently, $\mathbf 1^T A = 0$ (the all-ones row vector is in the left null space of $A$). This is the algebraic statement of "every edge has one head and one tail, contributing nothing to the total".

**Corollary — flow conservation implies $\mathbf 1^T s = 0$.** Multiplying $Af + s = 0$ on the left by $\mathbf 1^T$ gives $\mathbf 1^T A f + \mathbf 1^T s = 0$, and since $\mathbf 1^T A = 0$, we get $\mathbf 1^T s = 0$: the total external injection equals the total external extraction. Sources must balance sinks. In electrical networks: the total power into the network equals the total power out.

**Corollary — Dirichlet energy is zero iff potential is constant on each component.** $\|A^T v\|^2 = 0$ iff $A^T v = 0$ iff $v_{\operatorname{head}(j)} = v_{\operatorname{tail}(j)}$ for every edge $j$, iff $v$ is constant on each connected component of the graph. For a connected graph, this is exactly the case $v = c \mathbf 1$ for some constant $c$.

**Corollary — circulations form the null space of $A$.** The set of circulations is $\{f : Af = 0\} = \ker A$. By the rank-nullity theorem, $\dim \ker A = m - \operatorname{rank}(A) = m - (n - c)$, where $c$ is the number of connected components — exactly the **cyclomatic number** of the graph. So the dimension of the circulation space equals the number of independent cycles.

**Calibration check.** Verify that for the chain graph, $\ker A = \{0\}$ — a chain has no cycles. Verify that for a cycle graph with $n$ nodes and $n$ edges (a single closed loop), $\dim \ker A = 1$ — there is exactly one independent circulation, going around the cycle. Verify that $\mathbf 1$ is in $\ker A^T$ for any connected graph: a constant potential gives zero potential drop across every edge.

---

# Unlocked by This

> [!tip] Graph Laplacians and Spectral Graph Theory *(from Discrete Mathematics)*
> The matrix $L = AA^T$ — the graph Laplacian — is the central object of spectral graph theory. Its eigenvalues control connectivity (the Fiedler value), random-walk mixing times, expansion (Cheeger's inequality), and the number of spanning trees (Kirchhoff's matrix-tree theorem). The Laplacian eigenvectors give natural coordinate systems for graph data (Laplacian eigenmaps in machine learning) and underlie spectral clustering.

> [!tip] Network Flow Optimization *(from Operations Research)*
> The incidence matrix appears in **max-flow / min-cut**, **shortest path**, and **transportation problems** as the constraint matrix encoding flow conservation. The fundamental algorithms (Ford-Fulkerson, push-relabel, network simplex) exploit the special structure of the incidence matrix to achieve polynomial-time complexity, even though general linear programming is harder.

> [!tip] Simplicial Cohomology and Algebraic Topology *(from Topology)*
> The incidence matrix of a graph is the **coboundary operator** $\delta : C^0 \to C^1$ in simplicial cohomology, taking $0$-cochains (functions on vertices) to $1$-cochains (functions on edges). The kernel of $\delta$ consists of locally constant functions (one constant per connected component), corresponding to $H^0$ of the graph. The cokernel of $\delta$ — functions on edges modulo coboundaries — corresponds to $H^1$ and has dimension equal to the number of independent cycles. This is the toy case of de Rham cohomology of manifolds, with the incidence matrix playing the role of $d$ on $0$-forms.
