---
type: definition
subject: algebraic-topology
prereqs:
  - "Def - Singular Homology"
  - "Def - Singular Chain"
  - "Def - Homomorphism"
tags: [geometry, algebraic-topology, cohomology]
---

# Notation

$M$ is a topological space, $G$ an abelian coefficient group. $C_p(M; \mathbb{Z})$ is the integer singular chain group (we use integer chains as the base for cohomology). $C^p(M; G) = \mathrm{Hom}(C_p(M; \mathbb{Z}), G)$ is the **singular $p$-cochain group**. Elements of $C^p$ are written $\varphi, \psi$ — homomorphisms from $p$-chains to $G$.

$\delta : C^p(M; G) \to C^{p+1}(M; G)$ is the **coboundary operator**, the dual of $\partial$.

$Z^p(M; G) = \ker \delta$ are the **cocycles**, $B^p(M; G) = \mathrm{im}\, \delta$ are the **coboundaries**, and
$$
H^p(M; G) = Z^p(M; G) / B^p(M; G)
$$
is the **$p$-th singular cohomology group**.

For a continuous map $f : M \to N$, the induced cochain map $f^\# : C^p(N; G) \to C^p(M; G)$ is $\varphi \mapsto \varphi \circ f_\#$ — note the *reversal* of direction, making cohomology a **contravariant** functor.

---

# Axiom Motivation

Singular cohomology is the "dual" theory to singular homology, obtained by replacing chains $C_p$ with cochains $\mathrm{Hom}(C_p, G)$. Two questions: (i) why do we want a dual theory at all, when we already have homology? (ii) why specifically the $\mathrm{Hom}$-functor dualisation rather than something else?

The first question — why have cohomology — has several answers.

**Cohomology has a richer algebraic structure.** Singular cohomology is a *graded-commutative ring* under the **cup product** $H^p \otimes H^q \to H^{p+q}$, whereas homology has no analogous product. The ring structure of $H^*(M; G)$ distinguishes spaces that homology cannot — for instance, the lens spaces $L(7, 1)$ and $L(7, 2)$ have isomorphic homology but distinguishable cohomology rings. Cup product also represents the deepest topological invariants of complex projective varieties (cohomology of Grassmannians, Schubert calculus, intersection theory).

**Cohomology is the natural target of integration.** A closed differential form $\omega$ on a smooth manifold $M$ pairs with cycles by integration: $\omega \mapsto (c \mapsto \int_c \omega)$. The result of this pairing is a *cochain* (a homomorphism $C_p \to \mathbb{R}$), not a chain. So when we want to compare smooth-form invariants (de Rham cohomology) with topological invariants, the topological side has to be cohomology, not homology. This is the [[Thm - The de Rham Theorem (Full Proof)|de Rham theorem]]: $H^p_{dR}(M) \cong H^p(M; \mathbb{R})$.

**Cohomology is contravariant, which is geometrically natural.** A continuous map $f : M \to N$ induces $f_* : H_*(M) \to H_*(N)$ on homology (covariant: maps go in the same direction). It induces $f^* : H^*(N) \to H^*(M)$ on cohomology (contravariant: maps go in the opposite direction). The contravariance matches how forms transform: pullback of forms goes from $N$ to $M$, not from $M$ to $N$. So smooth differential geometry naturally uses cohomology (pullback of forms), and we want a singular theory that matches.

**Cohomology has finer information when integer coefficients are involved.** By the **universal coefficient theorem**, $H^p(M; G)$ is determined by $H_*(M; \mathbb{Z})$ via a non-canonical splitting: $H^p(M; G) \cong \mathrm{Hom}(H_p(M; \mathbb{Z}), G) \oplus \mathrm{Ext}(H_{p-1}(M; \mathbb{Z}), G)$. The $\mathrm{Ext}$ term is non-zero precisely when there is torsion in homology one degree down, and this torsion contributes to *both* adjacent cohomology degrees. So integer cohomology sees torsion in a different (and sometimes more revealing) way than integer homology.

The second question — why $\mathrm{Hom}$-dualisation — has a clean answer.

**Hom is the natural categorical operation for "functionals on a module."** A $p$-cochain $\varphi : C_p \to G$ assigns a value in $G$ to every chain — it is a "$G$-valued linear functional" on chains. The coboundary $(\delta \varphi)(c) = \varphi(\partial c)$ then says "the coboundary of $\varphi$ evaluated on $c$ is $\varphi$ evaluated on the boundary of $c$." This is exactly the integration-by-parts formula $\int_c d\omega = \int_{\partial c} \omega$ from Stokes's theorem, with $\varphi$ playing the role of "integrate against $\omega$" and $\delta$ being the formal adjoint of $\partial$. So the cohomology coboundary is the algebraic shadow of the exterior derivative.

**Why $\delta = \partial^*$, the dual of $\partial$?** Because we want the de Rham pairing to work: $\langle \delta \varphi, c \rangle = \langle \varphi, \partial c \rangle$. This is the only choice making cohomology dual to homology in the way Stokes's theorem requires. It is also the only choice making $\delta^2 = 0$: $(\delta^2 \varphi)(c) = \varphi(\partial^2 c) = \varphi(0) = 0$. So $\delta^2 = 0$ is automatic from $\partial^2 = 0$ under the $\mathrm{Hom}$-dualisation.

**Why use integer chains as the base, with coefficients in $G$?** Because then cohomology with coefficients in any $G$ is determined by integer homology via universal coefficients, and the coefficient group $G$ enters only through the "value group" of the cochains. This is the most flexible formulation. (One can also dualise from $G$-chains to $G$-valued cochains directly, but this is wastefully equivalent for nice coefficient groups, and the integer-chain version makes the universal coefficient theorem cleanest.)

---

# The Definition

Let $M$ be a topological space, $G$ an abelian coefficient group, $p \geq 0$ an integer.

The **singular $p$-cochain group** is the dual of the integer chain group:
$$
C^p(M; G) \;=\; \mathrm{Hom}_{\mathbb{Z}}(C_p(M; \mathbb{Z}),\, G).
$$
A $p$-cochain $\varphi \in C^p$ is a homomorphism assigning to each singular $p$-simplex $\sigma : \Delta^p \to M$ an element $\varphi(\sigma) \in G$, extended $\mathbb{Z}$-linearly to chains.

The **coboundary operator** $\delta : C^p(M; G) \to C^{p+1}(M; G)$ is the dual of $\partial$:
$$
(\delta \varphi)(c) \;=\; \varphi(\partial c) \qquad \text{for all } c \in C_{p+1}(M; \mathbb{Z}).
$$
Equivalently, on a singular $(p+1)$-simplex $\sigma$,
$$
(\delta \varphi)(\sigma) \;=\; \sum_{k=0}^{p+1} (-1)^k \varphi(\sigma \circ f_k).
$$

Since $\partial^2 = 0$, $\delta^2 = 0$: $(\delta^2 \varphi)(c) = \varphi(\partial^2 c) = 0$.

The **group of singular $p$-cocycles** is $Z^p(M; G) = \ker \delta$; the **group of singular $p$-coboundaries** is $B^p(M; G) = \mathrm{im}\,\delta$. By $\delta^2 = 0$, $B^p \subseteq Z^p$.

The **$p$-th singular cohomology group** of $M$ with coefficients in $G$ is the quotient
$$
H^p(M; G) \;=\; Z^p(M; G) / B^p(M; G).
$$

For a continuous map $f : M \to N$, the induced map on cochains is the *pullback*
$$
f^\# : C^p(N; G) \to C^p(M; G), \qquad (f^\# \varphi)(c) = \varphi(f_\# c).
$$
This commutes with $\delta$ (because $f_\#$ commutes with $\partial$), so it descends to
$$
f^* : H^p(N; G) \to H^p(M; G).
$$
Note the *reversal of direction*: cohomology is a **contravariant** functor $\mathbf{Top}^{\mathrm{op}} \to \mathbf{Ab}$, satisfying $(g \circ f)^* = f^* \circ g^*$ and $\mathrm{id}^* = \mathrm{id}$.

**Cup product.** Cohomology carries an associative bilinear product
$$
\smile \;:\; H^p(M; G) \otimes H^q(M; G) \to H^{p+q}(M; G),
$$
defined on cocycles by $(\varphi \smile \psi)(\sigma) = \varphi(\sigma|_{[v_0, \dots, v_p]}) \cdot \psi(\sigma|_{[v_p, \dots, v_{p+q}]})$ for a singular $(p+q)$-simplex $\sigma$ (where the multiplication on the right is in $G$, when $G$ is a ring). This makes $H^*(M; G) = \bigoplus_p H^p(M; G)$ into a **graded ring** under cup product, **graded-commutative**: $\alpha \smile \beta = (-1)^{pq} \beta \smile \alpha$ for $\alpha \in H^p$, $\beta \in H^q$.

---

# Categorical / Structural Definition

Singular cohomology is the composition
$$
H^p \;=\; H^p(C^\bullet) \circ \mathrm{Hom}(-, G) \circ C_\bullet(-; \mathbb{Z}) \circ \mathrm{Sing} \;:\; \mathbf{Top}^{\mathrm{op}} \to \mathbf{Ab},
$$
where:
1. $\mathrm{Sing} : \mathbf{Top} \to \mathbf{sSet}$ — singular simplicial set.
2. $C_\bullet(-; \mathbb{Z}) : \mathbf{sSet} \to \mathbf{Ch}(\mathbf{Ab})$ — free integer chain complex.
3. $\mathrm{Hom}(-, G) : \mathbf{Ch}(\mathbf{Ab})^{\mathrm{op}} \to \mathbf{CoCh}(\mathbf{Ab})$ — $\mathrm{Hom}$-dualisation, converting a chain complex into a cochain complex.
4. $H^p : \mathbf{CoCh}(\mathbf{Ab}) \to \mathbf{Ab}$ — $p$-th cohomology of a cochain complex.

The composition is **contravariant** (because step 3 reverses arrows), giving the functor
$$
H^p(-; G) \;:\; \mathbf{Top}^{\mathrm{op}} \to \mathbf{Ab}.
$$

The cup product makes $H^*(M; G)$ a graded-commutative ring, and $H^*(-; G)$ becomes a functor $\mathbf{Top}^{\mathrm{op}} \to \mathbf{GradedRing}$. The morphisms $f^* : H^*(N) \to H^*(M)$ are ring homomorphisms.

By the **Eilenberg–Steenrod axioms** for cohomology, singular cohomology is the unique contravariant functor $\mathbf{Top}^{\mathrm{op}} \to \mathbf{Ab}$ satisfying (i) homotopy invariance, (ii) the long exact sequence of a pair, (iii) excision, (iv) additivity (product of disjoint union is direct product), (v) the dimension axiom $H^p(\text{point}; G) = G$ for $p = 0$, zero for $p > 0$.

---

# Relate to Other Fields / Compression

Singular cohomology is the **dual theory to singular homology** in the precise categorical sense: cochains are the $\mathrm{Hom}$-dual of chains, coboundaries are the duals of boundaries. The cohomology groups are *not* simply the linear duals of homology groups in general — the universal coefficient theorem shows there is an additional $\mathrm{Ext}$ contribution. But over a field of characteristic zero, $H^p(M; K) = \mathrm{Hom}_K(H_p(M; K), K)$ exactly, and the two theories carry the same information (the linear dual reverses everything but loses no information).

It is also the **target of the de Rham pairing**: the integration map $\int : \Omega^p_{\text{closed}}(M) \to C^p(M; \mathbb{R})$, $\omega \mapsto (\sigma \mapsto \int_\sigma \omega)$, sends closed forms to cocycles and descends to an isomorphism $H^p_{dR}(M) \to H^p(M; \mathbb{R})$.

In algebraic geometry, the singular cohomology $H^*(X; \mathbb{Q})$ of a smooth complex projective variety $X$ is the **Betti cohomology** — one of the four "classical" cohomology theories (alongside de Rham, étale, and crystalline). The comparison isomorphisms between these — Betti, de Rham, étale — form the central machinery of arithmetic geometry. The de Rham theorem of our chapter is the simplest such comparison, between Betti and de Rham over $\mathbb{R}$.

**True name:** singular cohomology is the **graded-commutative ring of (equivalence classes of) functionals on chains that vanish on boundaries**, with the cup product as multiplication. The ring structure is what distinguishes cohomology from homology and is the source of most of cohomology's distinguishing power.

---

# Examples / Corollaries

**$H^*(\text{point}; G)$.** A point has $H^0(\text{point}; G) = G$ and $H^p(\text{point}; G) = 0$ for $p \geq 1$. Same as the homology, in this case.

**$H^*(\mathbb{R}^n; G)$.** Contractible, so $H^0 = G$ and $H^p = 0$ for $p \geq 1$ (homotopy invariance).

**$H^*(S^n; G)$.** $H^0 = G$, $H^n = G$, zero in other degrees. The generator in $H^n$ is dual to the fundamental class $[S^n] \in H_n$.

**$H^*(T^n; G)$.** $H^k(T^n; G) = G^{\binom{n}{k}}$, generated as a ring by $n$ classes $\alpha_1, \dots, \alpha_n \in H^1(T^n; G)$ corresponding to the $n$ angular forms, satisfying $\alpha_i \alpha_j = -\alpha_j \alpha_i$ (graded commutativity) and $\alpha_i^2 = 0$. The cohomology ring is the **exterior algebra** $\bigwedge(\alpha_1, \dots, \alpha_n)$ on $n$ degree-$1$ generators.

**$H^*(\mathbb{CP}^n; \mathbb{Z})$.** $H^{2k}(\mathbb{CP}^n; \mathbb{Z}) = \mathbb{Z}$ for $0 \leq k \leq n$, zero in odd degrees. The cohomology ring is the **truncated polynomial ring** $\mathbb{Z}[x]/(x^{n+1})$, generated by a single class $x \in H^2(\mathbb{CP}^n; \mathbb{Z})$ — the **hyperplane class**. The ring structure $x^k \in H^{2k}$ distinguishes $\mathbb{CP}^n$ from a wedge sum of even-dimensional spheres (which would have all cup products zero) — even though the additive cohomology groups agree.

**$H^*(\mathbb{RP}^n; \mathbb{Z}/2)$.** With mod-$2$ coefficients, $H^k(\mathbb{RP}^n; \mathbb{Z}/2) = \mathbb{Z}/2$ for $0 \leq k \leq n$. The cohomology ring is $\mathbb{Z}/2[x]/(x^{n+1})$ with $x \in H^1(\mathbb{RP}^n; \mathbb{Z}/2)$ — analogous to the complex projective case but with one-half the dimension.

**Is NOT an instance: a non-cocycle as a cohomology generator.** A $p$-cochain $\varphi$ is a cohomology generator only if it is a cocycle ($\delta \varphi = 0$), and even then only its cohomology class $[\varphi] \in H^p$ matters — the explicit cochain $\varphi$ is one of many representatives. Trying to "use" a non-cocycle as a cohomology class is meaningless; the coboundary $\delta \varphi$ measures the failure.

**Corollary (universal coefficient theorem).** For each $p \geq 0$, there is a non-canonical splitting
$$
H^p(M; G) \;\cong\; \mathrm{Hom}(H_p(M; \mathbb{Z}), G) \oplus \mathrm{Ext}^1(H_{p-1}(M; \mathbb{Z}), G).
$$
When $G$ is a field of characteristic zero (e.g. $G = \mathbb{R}$, $\mathbb{Q}$), the $\mathrm{Ext}$ term vanishes (because $G$ is divisible, hence injective as $\mathbb{Z}$-module), and the formula simplifies to $H^p(M; G) = \mathrm{Hom}(H_p(M; \mathbb{Z}), G) = H_p(M; G)^*$.

**Corollary (cohomology over a field is the dual of homology).** When $G$ is a field of characteristic zero, $\dim H^p(M; G) = \dim H_p(M; G) = b_p(M)$ — cohomology and homology have the same Betti numbers, and one is the linear dual of the other.

**Corollary (cup product is graded-commutative).** For $\alpha \in H^p(M; G)$, $\beta \in H^q(M; G)$:
$$
\alpha \smile \beta = (-1)^{pq}\, \beta \smile \alpha.
$$
In particular, $\alpha \smile \alpha = 0$ when $p$ is odd and $2 \neq 0$ in $G$. So in $H^*(T^n; \mathbb{R})$, the degree-$1$ generators satisfy $\alpha_i^2 = 0$.

**Calibration check.** If you have understood the definition you should be able to: (1) compute $H^0(M; G)$ for a discrete space of $k$ points (answer: $G^k$); (2) explain why the universal coefficient theorem makes the cohomology of $\mathbb{RP}^2$ with $\mathbb{Z}/2$ coefficients have dimension $(1, 1, 1)$ while $H_*(\mathbb{RP}^2; \mathbb{Z})$ has rank pattern $(1, 0, 0)$ — extracting the role of $\mathbb{Z}/2$ torsion; (3) describe the cup product on $H^*(T^2; \mathbb{R})$ as the exterior algebra $\bigwedge(\alpha_1, \alpha_2)$, and verify that $\alpha_1 \smile \alpha_2 \neq 0$ in $H^2$.

---

# Unlocked by This

> [!tip] The de Rham Theorem *(from Algebraic Topology — this same topic)*
> Singular cohomology with real coefficients agrees with de Rham cohomology: $H^p(M; \mathbb{R}) \cong H^p_{dR}(M)$, via integration of forms against cycles. This is the bridge between smooth and topological cohomology on smooth manifolds — see [[Thm - The de Rham Theorem (Full Proof)]]. The de Rham theorem also identifies cup product with wedge product: $[\omega] \smile [\eta] = [\omega \wedge \eta]$.

> [!tip] **Poincaré Duality** *(from Algebraic Topology)*
> For a compact oriented $n$-manifold $M$, cap product with the fundamental class $[M] \in H_n(M; \mathbb{Z})$ gives an isomorphism $H^k(M; G) \cong H_{n-k}(M; G)$. The cohomology ring with rational coefficients then has a **Poincaré pairing** $H^k(M; \mathbb{Q}) \otimes H^{n-k}(M; \mathbb{Q}) \to H^n(M; \mathbb{Q}) = \mathbb{Q}$ given by cup product followed by evaluation against $[M]$; this is a perfect pairing for compact oriented manifolds.

> [!tip] **Characteristic Classes** *(from Algebraic Topology and Differential Geometry)*
> For a vector bundle $E \to M$, one can construct cohomology classes $c_i(E) \in H^{2i}(M; \mathbb{Z})$ (Chern classes), $p_i(E) \in H^{4i}(M; \mathbb{Z})$ (Pontryagin classes), $e(E) \in H^n(M; \mathbb{Z})$ (Euler class) — the **characteristic classes** that encode the topological non-triviality of $E$. By **Chern–Weil theory**, these classes are computable from a connection on $E$ as integrals of curvature forms, giving explicit smooth-form representatives. The de Rham theorem makes this match precise.

> [!tip] **Sheaf Cohomology** *(from Algebraic Geometry and Complex Geometry)*
> Singular cohomology is the prototype of the more general **sheaf cohomology** $H^p(M; \mathcal{F})$ — cohomology with coefficients in any sheaf $\mathcal{F}$ on $M$. For the constant sheaf $\mathcal{F} = G$, $H^p(M; G) = H^p_{\text{sing}}(M; G)$ — singular cohomology is sheaf cohomology of the constant sheaf. For sheaves of differential forms, sections of vector bundles, holomorphic functions, etc., sheaf cohomology becomes a much more refined invariant carrying the geometry of the sheaf.

> [!tip] **Steenrod Algebra and Cohomology Operations** *(from Algebraic Topology)*
> Beyond the cup product, $H^*(M; \mathbb{Z}/2)$ carries operations $\mathrm{Sq}^i : H^p \to H^{p+i}$ (**Steenrod squares**) generated by the squaring operation $\alpha \mapsto \alpha \smile \alpha$. The Steenrod algebra acts on mod-$2$ cohomology and distinguishes spaces that ordinary cohomology cannot — the original applications include proofs that $S^n$ admits no nowhere-zero vector field for $n$ even (Steenrod-square obstruction) and that the Hopf invariant takes value $1$ only in dimensions $1, 3, 7$ (Adams's solution to the Hopf invariant problem).
