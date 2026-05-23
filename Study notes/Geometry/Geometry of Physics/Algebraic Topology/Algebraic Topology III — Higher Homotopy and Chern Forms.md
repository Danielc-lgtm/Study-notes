---
type: topic
subject: algebraic-topology
chapter: "22.1-22.5"
title: "Algebraic Topology III — Higher Homotopy and Chern Forms"
tags: [geometry, algebraic-topology, characteristic-classes, gauge-theory, homotopy]
---

# Notation Registry

A standing convention for this topic: **all spaces are pointed, all maps preserve base points, and "manifold" means smooth Hausdorff second-countable.** Higher homotopy groups depend on the base point only up to (canonical) isomorphism on path-connected spaces, but writing them base-pointed is technically necessary. For Chern forms, the **structure group** is $U(n)$ unless we say otherwise, and the **connection 1-form** $\omega$ and **curvature 2-form** $\theta = d\omega + \omega \wedge \omega$ are $\mathfrak{u}(n)$-valued — that is, $n \times n$ anti-Hermitian. Frankel uses an unusual normalisation: the factor $i/(2\pi)$ in front of the curvature is chosen so that the periods of $c_r$ are integers; some authors absorb the $i$ into a different sign convention. The result is the same de Rham class.

> [!warning] Convention: $\mathfrak{u}(n)$ as anti-Hermitian
> Mathematicians often take $\mathfrak{u}(n)$ as anti-Hermitian matrices ($X^* = -X$); physicists often take $\mathfrak{u}(n)$ as Hermitian ($X^* = X$) and absorb an $i$ into the exponential map $g = \exp(itX)$. The two conventions differ by a factor of $i$ in $\omega$ and a factor of $i^2 = -1$ in $\omega \wedge \omega$. Frankel follows the mathematician's convention; we do the same.

- $X, Y, M$ — topological spaces or smooth manifolds (always path-connected unless stated)
- $x_0, p_0 \in X$ — base point
- $S^k$ — the unit $k$-sphere in $\mathbb{R}^{k+1}$, base-pointed at the north pole
- $D^{k+1}$ — the closed unit $(k+1)$-ball; $\partial D^{k+1} = S^k$
- $I^k = [0,1]^k$ — the unit $k$-cube; $\partial I^k = \dot I^k$ — its boundary
- $\pi_k(X, x_0)$ or $\pi_k(X)$ — the $k$-th homotopy group of $X$ based at $x_0$
- $[f]$ — the homotopy class of the map $f$
- $f + g$ — composition of based maps $S^k \to X$ in the $\pi_k$ group law (concatenate along first coordinate)
- $f \simeq g$ — $f$ is homotopic to $g$ (base-point preserving)
- $F \hookrightarrow E \xrightarrow{\pi} B$ — a fibration with total space $E$, base $B$, fibre $F = \pi^{-1}(b_0)$
- $\partial : \pi_k(B) \to \pi_{k-1}(F)$ — the connecting (boundary) homomorphism of a fibration
- $H_k(X; \mathbb{Z})$ — singular homology with integer coefficients (see [[Algebraic Topology I — Singular Homology and the de Rham Theorem]])
- $h : \pi_k(X) \to H_k(X; \mathbb{Z})$ — the Hurewicz map
- $E \to M$ — a complex vector bundle of rank $n$ with structure group $U(n)$
- $\omega = \omega_U$ — a connection 1-form on $E$ in local frame $e_U$; $\mathfrak{u}(n)$-valued 1-form
- $\theta = \theta_U = d\omega + \omega \wedge \omega$ — the curvature 2-form; $\mathfrak{u}(n)$-valued 2-form
- $c_r(E)$ — the $r$-th **Chern form** of $E$, a closed $2r$-form on $M$
- $c(E) = 1 + c_1(E) + c_2(E) + \cdots = \det\!\big(I + \tfrac{i}{2\pi}\theta\big)$ — the **total Chern form**
- $[c_r(E)] \in H^{2r}_{\mathrm{dR}}(M; \mathbb{R})$ — the $r$-th **Chern class** of $E$ (the de Rham cohomology class)
- $\langle c_r(E), z \rangle = \int_z c_r(E)$ — the pairing with a $2r$-cycle (always an integer when $z$ is integral)
- $\eta$, $\mathrm{Hopf}$ — the Hopf map $S^3 \to S^2$
- $SU(n), U(n), SO(n)$ — the special unitary, unitary, special orthogonal groups
- $\mathfrak{su}(n), \mathfrak{u}(n)$ — their Lie algebras
- $\mathbb{CP}^n$ — complex projective $n$-space; $\mathbb{CP}^1 \cong S^2$ is the Riemann sphere
- $j(c_2)$ — the **instanton number**, $\int_{\mathbb{R}^4} c_2$ for an $SU(n)$ instanton

---

# Motivation

Here is the entire topic in one sentence: **the obstruction to extending a section, the integer cohomology of a sphere, and the curvature integrals of a connection are all the same thing.** This is the discovery that ties together the last three loose ends of [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds|Riemannian geometry]], [[Algebraic Topology I — Singular Homology and the de Rham Theorem|de Rham cohomology]], and [[Algebraic Topology II — Fundamental Group and Covering Spaces|the fundamental group]] — and it produces in one stroke both the framework of **characteristic classes** (the cohomology classes attached to vector bundles, classifying them up to isomorphism) and the framework of **higher homotopy groups** (the abelian generalisations of $\pi_1$ that record how spheres of every dimension can be mapped into a space). The two are tied together by the Chern–Weil construction, which builds cohomology classes from curvature, and by the obstruction-cocycle picture, which interprets the resulting integers as the number of times a section "wraps" around a higher-dimensional sphere of fibre data. Higher homotopy is the bookkeeping, Chern forms are the analytic representative, and the integers $\int_z c_r$ are the answer.

The story starts with the question Frankel poses at the top of Chapter 22: *how can we construct closed $p$-forms from the matrix of curvature forms?* We already know one answer, from [[Gauge Theory II — Fibre Bundles, Principal Bundles, and Gauss–Bonnet|Gauss–Bonnet]]: on a Riemannian surface the Gaussian curvature 2-form integrates to $2\pi\chi(M^2)$. Chern's discovery is that this is the simplest case of a *general* construction. For any complex vector bundle with structure group $U(n)$, certain polynomials in the curvature — the Chern forms $c_1, c_2, \ldots, c_n$ — are always *closed*, define *connection-independent* de Rham classes, and have *integer periods* on integer cycles. The reason for each of these is a separate small miracle of multilinear algebra and the Bianchi identity, and assembling them into one theorem produces the **Chern–Weil construction**: invariant polynomials of curvature give characteristic cohomology classes. This is what makes $\int_{M^4} \mathrm{tr}(F \wedge F)$ — the instanton number that appears as a topological term in Yang–Mills theory — a topological invariant of the bundle, not a property of the particular connection used to compute it.

Why should the analytic integers $\int_z c_r$ be topological? The conceptual reason is the **obstruction-cocycle picture** of §22.5. Given a $U(n)$ bundle over a $2r$-cycle $z$, you try to construct a global frame, simplex by simplex up the dimension. The obstruction to extending the frame across a $2r$-cell is the homotopy class of the boundary $(2r-1)$-sphere mapped into the fibre — an element of $\pi_{2r-1}(U(n))$. For $r = 1$ this is $\pi_1(U(1)) = \pi_1(S^1) = \mathbb{Z}$; for $r = 2$ this is $\pi_3(SU(n)) = \mathbb{Z}$. Summing these obstructions over the cells of $z$ gives an integer — the **obstruction cocycle** $\int_z c_r$ — and the Chern–Weil theorem is the analytic incarnation of this combinatorial integer. Chern forms are the *de Rham representatives of obstructions to global trivialisation*, and the integer they integrate to is the number of cells where a smooth section necessarily develops a singularity.

The other half of the chapter is **higher homotopy theory**: the apparatus that makes the obstruction picture work. The fundamental group $\pi_1(X)$ records homotopy classes of based loops $S^1 \to X$; the *higher* homotopy groups $\pi_k(X)$ record homotopy classes of based maps $S^k \to X$ for every $k \geq 1$. For $k \geq 2$ these groups are *abelian* (the Eckmann–Hilton argument: enough room to slide the second map past the first), which is why we can speak of $\mathbb{Z}$-valued obstructions and integer-valued cocycles. The recurring tool for computing $\pi_k$ is the **long exact sequence of a fibration**: for any "nice" map $E \to B$ with fibre $F$, there is an exact sequence

$$\cdots \to \pi_k(F) \to \pi_k(E) \to \pi_k(B) \xrightarrow{\partial} \pi_{k-1}(F) \to \cdots$$

that connects the homotopy of total space, fibre, and base in a single algebraic chain. Plugging in the Hopf fibration $S^1 \hookrightarrow S^3 \to S^2$ gives $\pi_3(S^2) = \pi_3(S^3) = \mathbb{Z}$ — the spectacular fact that there is a non-contractible map from a higher-dimensional sphere to a lower-dimensional one, contradicting the naive intuition that "lower-dimensional targets cannot host higher-dimensional homotopy". Plugging in $SU(n-1) \hookrightarrow SU(n) \to S^{2n-1}$ gives $\pi_3(SU(n)) = \pi_3(SU(2)) = \pi_3(S^3) = \mathbb{Z}$, which is the source of the integer obstruction in the §22.5 picture.

The arc of the chapter is therefore:

$$\text{curvature}\ \theta \;\xrightarrow{\text{Chern forms}}\; \text{closed } 2r\text{-forms} \;\xrightarrow{\text{integrate}}\; \mathbb{Z} \;\xleftarrow{\text{obstruction degree in }\pi_{2r-1}}\; \text{global section}$$

This single backbone identifies analytic invariants (curvature integrals), topological invariants (homotopy classes), and structural invariants (obstructions to triviality of a bundle) — the conceptual content of characteristic class theory. The physical incarnation is **topological quantisation**: the magnetic charge of a Dirac monopole is $\int_{S^2} c_1$ (an integer because $\pi_1(U(1)) = \mathbb{Z}$); the instanton number of a Yang–Mills field on $\mathbb{R}^4$ is $\int_{S^3_\infty} \mathrm{Tr}(g^{-1}dg)^3 / (24\pi^2) = -\int_{\mathbb{R}^4} c_2 \in \mathbb{Z}$ (an integer because $\pi_3(SU(n)) = \mathbb{Z}$). The integrality of these physical quantities — and the fact that they label distinct vacuum sectors of gauge theories — is exactly the obstruction picture.

The reader is assumed to have worked through [[Algebraic Topology I — Singular Homology and the de Rham Theorem]] (singular homology, de Rham cohomology, the de Rham theorem), [[Algebraic Topology II — Fundamental Group and Covering Spaces]] ($\pi_1$, covering spaces, the lifting picture), [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|de Rham cohomology on manifolds]], [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|Lie groups]], and [[Gauge Theory II — Fibre Bundles, Principal Bundles, and Gauss–Bonnet|principal and vector bundles]] (the geometric setup). [[Gauge Theory III — Connections in Principal and Associated Bundles|Connections and curvature on principal bundles]] are the right preparation for the Chern-form material; [[Gauge Theory IV — Yang–Mills Fields and Instantons|Yang–Mills theory]] is the destination chapter for the obstruction-as-instanton-number application.

---

# Concept Map

## §3.1 Higher Homotopy Groups

- **[[Def - Higher Homotopy Group]]**
	- The $k$-th homotopy group $\pi_k(X, x_0) = [(S^k, \mathrm{pt}), (X, x_0)]$ is the set of homotopy classes of based continuous maps from the pointed $k$-sphere into the pointed space $X$, with group operation given by concatenation along the first coordinate. For $k = 1$ this recovers the [[Algebraic Topology II — Fundamental Group and Covering Spaces|fundamental group]]; for $k \geq 2$ it is automatically abelian. Examples: $\pi_k(\mathbb{R}^n) = 0$ for all $k$; $\pi_k(S^n) = 0$ for $k < n$; $\pi_n(S^n) = \mathbb{Z}$ (the degree); and the spectacular $\pi_3(S^2) = \mathbb{Z}$ generated by the Hopf map.

- **[[Thm - Higher Homotopy Groups are Abelian]]**
	- For every $k \geq 2$ and every pointed space $(X, x_0)$, the group $\pi_k(X, x_0)$ is abelian. The proof is the **Eckmann–Hilton argument**: when there is room to slide one map past another (which is what "$k \geq 2$ means: two transverse directions"), the concatenation operation is forced to be commutative by the very fact that it interacts with itself nicely. This is why the higher homotopy groups can be added with $+$, why characteristic classes take integer values, and why obstruction cocycles live in honest abelian groups.

- **[[Def - Hurewicz Map]]**
	- The Hurewicz map $h_k : \pi_k(X, x_0) \to H_k(X; \mathbb{Z})$ sends a homotopy class $[f]$ of a map $f : S^k \to X$ to the homology class of the singular cycle $f_*([S^k]) \in H_k(X)$, where $[S^k]$ is the fundamental class of the $k$-sphere. It is a homomorphism, natural in $X$. For $k = 1$ it factors through the abelianisation, giving the famous identification $\pi_1^{\mathrm{ab}}(X) \cong H_1(X; \mathbb{Z})$; for higher $k$ it is the bridge from homotopy (which is hard) to homology (which is computable).

- **[[Thm - Hurewicz Theorem (Statement)]]**
	- If $X$ is path-connected and $(n-1)$-connected (meaning $\pi_k(X) = 0$ for $0 \leq k \leq n-1$) with $n \geq 1$, then $\pi_n(X) \cong H_n(X; \mathbb{Z})$, and the isomorphism is the Hurewicz map. For $n = 1$ the statement is that $\pi_1^{\mathrm{ab}} \cong H_1$ always (no connectivity hypothesis is needed for the *first* nonvanishing group). This is the only general computational tool that converts homotopy into homology, and most explicit computations of $\pi_k$ ultimately depend on it: knowing $H_k$ pins down $\pi_k$ in the first nonzero degree.

> [!tip] Unlocked: Eilenberg–MacLane Spaces *(from Algebraic Topology / Homotopy Theory)*
> A space $K(\pi, n)$ with $\pi_n = \pi$ and all other $\pi_k = 0$ is an **Eilenberg–MacLane space**, and Hurewicz gives $H_n(K(\pi, n); \mathbb{Z}) = \pi$. These are the building blocks of **postnikov towers** — every space is filtered by Eilenberg–MacLane stages. The space $\mathbb{CP}^\infty$ is $K(\mathbb{Z}, 2)$ and is the **classifying space** $BU(1)$ for complex line bundles, so $[X, \mathbb{CP}^\infty] = H^2(X; \mathbb{Z})$ — line bundles on $X$ are classified by their first Chern class, the connection to characteristic classes that closes the chapter.

> [!tip] Unlocked: Stable Homotopy Theory *(from Modern Algebraic Topology)*
> The groups $\pi_k(S^n)$ stabilise as $n \to \infty$: for fixed $k$, the sequence $\pi_{n+k}(S^n)$ becomes constant when $n$ is large enough (Freudenthal's theorem). The limiting groups $\pi_k^s := \lim_n \pi_{n+k}(S^n)$ are the **stable homotopy groups of spheres** — the foundation of **stable homotopy theory** and the home of **Adams operations**, **Bott periodicity**, and the **Adams spectral sequence**. Computing $\pi_k^s$ for large $k$ is a notoriously difficult open problem, equivalent in difficulty to large pieces of arithmetic geometry.

- **[[Ex - Pi_n of S^n is Z]]** (⭐⭐)
	- Show that $\pi_n(S^n) = \mathbb{Z}$, generated by the identity map, with the integer attached to a map being its Brouwer degree. Uses the Hurewicz theorem applied to the $(n-1)$-connected space $S^n$.

> [!note] Exercise Index — §3.1
> [[Exercise Index - §3.1 Higher Homotopy Groups]]

## §3.2 Fibrations and the Long Exact Sequence

- **[[Def - Fibration]]**
	- A continuous map $\pi : E \to B$ is a **Hurewicz fibration** if it has the homotopy lifting property: given any space $W$, any homotopy $F : W \times [0,1] \to B$, and any lift $\tilde f : W \to E$ of $f = F(\cdot, 0)$, there exists a lift $\tilde F : W \times [0,1] \to E$ of $F$ with $\tilde F(\cdot, 0) = \tilde f$. Every fibre bundle (in particular, every smooth principal or vector bundle) is a Hurewicz fibration. The fibre $F = \pi^{-1}(b_0)$ is well-defined up to homotopy equivalence and is the conceptual "kernel" of the projection.

- **[[Def - Exact Sequence of Groups]]**
	- A sequence of groups and homomorphisms $\cdots \to G_{i-1} \xrightarrow{f_i} G_i \xrightarrow{f_{i+1}} G_{i+1} \to \cdots$ is **exact at $G_i$** if $\mathrm{im}\, f_i = \ker f_{i+1}$. The entire sequence is exact if it is exact at every term. Short exact sequences $0 \to A \to B \to C \to 0$ are equivalent to *quotient* relations $C \cong B/A$ when the groups are abelian. Long exact sequences are the principal computational tool of homological algebra: they propagate vanishing and isomorphism statements across long chains of groups.

- **[[Def - The Hopf Map]]**
	- The Hopf map $\eta : S^3 \to S^2$ sends $(z_0, z_1) \in S^3 \subset \mathbb{C}^2$ (with $|z_0|^2 + |z_1|^2 = 1$) to the line $[z_0 : z_1] \in \mathbb{CP}^1 \cong S^2$. The fibre over each point is a great circle $\{(e^{i\theta} z_0, e^{i\theta} z_1) : \theta \in [0, 2\pi)\}$, and the resulting fibration $S^1 \hookrightarrow S^3 \to S^2$ is the **Hopf fibration**. It is the prototypical example of a non-trivial fibration and the source of $\pi_3(S^2) = \mathbb{Z}$.

- **[[Thm - Long Exact Sequence of a Fibration]]**
	- For a fibration $F \hookrightarrow E \xrightarrow{\pi} B$ with connected fibre $F$, there is a long exact sequence of homotopy groups
	  $$\cdots \to \pi_k(F) \xrightarrow{i_*} \pi_k(E) \xrightarrow{\pi_*} \pi_k(B) \xrightarrow{\partial} \pi_{k-1}(F) \to \cdots \to \pi_1(B) \to 1.$$
	  The boundary map $\partial$ comes from the homotopy lifting property: a sphere in $B$ is lifted to a disc in $E$, whose boundary lies in the fibre. This single sequence is the central computational tool of higher homotopy, allowing $\pi_k(B)$ and $\pi_k(F)$ to be related to $\pi_k(E)$ when one of them is known.

> [!tip] Unlocked: Serre Spectral Sequence *(from Homological Algebra)*
> The long exact sequence of a fibration is the bottom row of a much more general apparatus: the **Serre spectral sequence**, which relates $H_*(F)$, $H_*(B)$, and $H_*(E)$ via a filtration. When the fibration is a principal bundle, this becomes the spectral sequence of a group action, and in characteristic classes it computes $H^*(BG)$ in terms of $H^*(G)$ — the cohomology of classifying spaces, the home of universal characteristic classes.

> [!tip] Unlocked: K-theory *(from Topology / Index Theory)*
> The homotopy groups $\pi_k(BU)$ of the classifying space of $U = \lim U(n)$ are periodic with period $2$: $\pi_{2k}(BU) = \mathbb{Z}$, $\pi_{2k+1}(BU) = 0$ (**Bott periodicity**). This stunning fact is the foundation of complex **K-theory**, the cohomology theory whose cycles are virtual vector bundles. **K-theory** is computed using the long-exact-sequence apparatus iterated, and the **index theorem (Atiyah–Singer)** computes the index of an elliptic operator as a topological invariant in K-theory.

- **[[Ex - Pi_3 of S^2 is Z via the Hopf Map]]** (⭐⭐)
	- Use the long exact sequence of the Hopf fibration $S^1 \to S^3 \to S^2$ to compute $\pi_3(S^2) = \mathbb{Z}$, generated by the Hopf map itself.

- **[[Ex - Long Exact Sequence of the Hopf Fibration]]** (⭐⭐⭐)
	- Write down the full long exact sequence for the Hopf fibration and deduce as many homotopy groups as possible: $\pi_k(S^2)$ for $k \leq 3$ in terms of $\pi_k(S^1)$ and $\pi_k(S^3)$. Identify the unexpected isomorphism $\pi_k(S^2) \cong \pi_k(S^3) \oplus \pi_{k-1}(S^1)$ for $k \geq 3$ (the latter is zero for $k \geq 3$, so we recover $\pi_k(S^2) = \pi_k(S^3)$, which is highly nontrivial information about higher $S^2$ homotopy).

> [!note] Exercise Index — §3.2
> [[Exercise Index - §3.2 Fibrations and the Long Exact Sequence]]

## §3.3 Chern Forms and Characteristic Classes

- **[[Def - Chern Forms of a U(n) Bundle]]**
	- For a rank-$n$ complex vector bundle $E \to M$ with $U(n)$ structure group and connection $\omega$ with curvature 2-form $\theta = d\omega + \omega \wedge \omega$ (a $\mathfrak{u}(n)$-valued 2-form, locally an $n \times n$ matrix of 2-forms), the **$r$-th Chern form** is the coefficient of $\lambda^{n-r}$ in $\det(I + \tfrac{i\theta}{2\pi})$ — equivalently the $r$-th elementary symmetric polynomial of $\tfrac{i}{2\pi}$ times the eigenvalues of $\theta$. Explicitly $c_1 = \tfrac{i}{2\pi} \mathrm{Tr}(\theta)$ and $c_2 = \tfrac{1}{8\pi^2}[\mathrm{Tr}(\theta) \wedge \mathrm{Tr}(\theta) - \mathrm{Tr}(\theta \wedge \theta)]$. Each $c_r$ is a globally defined closed real $2r$-form whose de Rham class depends only on $E$, not on the choice of connection.

- **[[Def - Total Chern Class]]**
	- The **total Chern form** is $c(E) = \det\!\big(I + \tfrac{i\theta}{2\pi}\big) = 1 + c_1(E) + c_2(E) + \cdots + c_n(E)$, a sum of forms of even degrees. The **total Chern class** is the corresponding sum of de Rham cohomology classes $[c(E)] \in H^{\mathrm{even}}_{\mathrm{dR}}(M; \mathbb{R})$. It is multiplicative under Whitney sum: $c(E \oplus F) = c(E) \cdot c(F)$ — a key formal property that allows Chern classes of complicated bundles to be computed from those of simpler ones.

- **[[Def - First Chern Class]]**
	- $c_1(E) = \tfrac{i}{2\pi}\mathrm{Tr}(\theta)$ — a closed real 2-form whose de Rham class depends only on $E$. For a complex *line* bundle ($n = 1$) this is the only Chern class: $c(E) = 1 + c_1(E)$. The first Chern class is the **complete invariant** for complex line bundles over CW complexes — two line bundles are isomorphic if and only if their first Chern classes coincide — and for surfaces, $\int_{M^2} c_1 \in \mathbb{Z}$ counts the zeros (with sign) of a generic section. Physically: $c_1$ of the $U(1)$ electromagnetic bundle is $F/(2\pi)$, and its integrality is **Dirac quantisation**.

- **[[Def - Second Chern Class]]**
	- $c_2(E) = \tfrac{1}{8\pi^2}[\mathrm{Tr}(\theta) \wedge \mathrm{Tr}(\theta) - \mathrm{Tr}(\theta \wedge \theta)]$. For an $SU(n)$ bundle ($\mathrm{Tr}(\theta) = 0$) this simplifies to $c_2 = \tfrac{1}{8\pi^2}\mathrm{Tr}(\theta \wedge \theta)$. The integral $\int_{M^4} c_2 \in \mathbb{Z}$ on a closed oriented 4-manifold is the **second Chern number**; for an $SU(n)$ instanton on $\mathbb{R}^4$ it is the **instanton number**, counting the homotopy class in $\pi_3(SU(n)) = \mathbb{Z}$ of the gauge transformation at infinity. This is the integer that labels distinct vacuum sectors of Yang–Mills theory.

- **[[Def - Characteristic Class]]**
	- A **characteristic class** of a real or complex vector bundle is a cohomology class natural under bundle pullback: for every $f : N \to M$ and every bundle $E \to M$, $c(f^* E) = f^* c(E)$. Equivalently, a characteristic class is a natural transformation from the functor of isomorphism classes of bundles to a cohomology functor. The Chern classes $c_r$ are the universal characteristic classes for complex bundles; **Stiefel–Whitney classes** $w_r \in H^r(M; \mathbb{Z}/2)$ are universal for real bundles; **Pontryagin classes** $p_r = (-1)^r c_{2r}(E \otimes \mathbb{C}) \in H^{4r}(M; \mathbb{Z})$ are universal for real bundles in integer cohomology. The unifying frame is that *characteristic classes obstruct global structure* — a vanishing $w_1$ permits orientability, vanishing $w_2$ permits a spin structure, vanishing $c_1$ permits a Calabi–Yau structure.

- **[[Thm - Chern-Weil Theorem (Statement)]]**
	- For any complex vector bundle $E \to M$ with a $U(n)$ connection and curvature $\theta$, and for every $\mathrm{Ad}$-invariant polynomial $P$ on $\mathfrak{u}(n)$, the form $P(\theta)$ is a **closed differential form**, and its de Rham cohomology class is **independent of the choice of connection**. The total Chern form $\det(I + \tfrac{i\theta}{2\pi})$ is the special case where $P$ is the determinant polynomial. This is the analytic engine of characteristic class theory: it manufactures topological invariants out of geometric data (the curvature).

- **[[Thm - Chern Forms are Closed and Their Cohomology Class is Independent of Connection]]**
	- Each Chern form $c_r(E)$ satisfies $dc_r = 0$, and if $\omega$ and $\omega'$ are two connections on the same bundle with respective Chern forms $c_r(\omega)$ and $c_r(\omega')$, then $c_r(\omega) - c_r(\omega') = d\nu_r$ for some globally defined $(2r-1)$-form $\nu_r$ on $M$. The proof goes through the **Chern–Simons form** transgression: the convex combination $\omega(t) = t\omega + (1-t)\omega'$ produces a 1-parameter family of curvatures, and differentiating $c_r(\omega(t))$ with respect to $t$ gives an exact form $d\nu_r$. The closedness alone follows directly from the Bianchi identity $d_\nabla \theta = 0$.

- **[[Thm - First Chern Class Classifies Line Bundles over a CW Complex]]**
	- For a CW complex $X$, the map $L \mapsto c_1(L) \in H^2(X; \mathbb{Z})$ is a bijection between isomorphism classes of complex line bundles on $X$ and integer cohomology classes in degree 2. Equivalently, the classifying space of $U(1)$ is $\mathbb{CP}^\infty = K(\mathbb{Z}, 2)$, and the universal bundle is the tautological line bundle. This is the simplest case of the general statement "complex $n$-plane bundles on $X$ correspond to maps $X \to BU(n)$, whose cohomology is generated by Chern classes". For surfaces, the integer $\int_M c_1 \in \mathbb{Z}$ is the **degree** of the line bundle.

> [!tip] Unlocked: Stiefel–Whitney Classes *(from Algebraic Topology / Real Vector Bundles)*
> For a real vector bundle $E \to M$, the **Stiefel–Whitney classes** $w_r(E) \in H^r(M; \mathbb{Z}/2)$ are defined via a Chern–Weil-type construction (or axiomatically by their behaviour under pullback and Whitney sum). The first $w_1$ is the obstruction to orientability ($w_1 = 0 \iff M$ orientable); the second $w_2$ is the obstruction to a spin structure ($w_2 = 0$ permits lifting the structure group from $SO(n)$ to $\mathrm{Spin}(n)$, which is what allows spinor bundles — see [[Spinors and the Dirac Equation]]). Stiefel–Whitney classes are integer-cohomology-mod-2 versions of Chern classes; the failure of integer lifts is the source of their mod-2 nature.

> [!tip] Unlocked: Pontryagin Classes *(from Real Characteristic Classes)*
> For a real vector bundle $E \to M$, the **Pontryagin classes** are $p_r(E) = (-1)^r c_{2r}(E \otimes \mathbb{C}) \in H^{4r}(M; \mathbb{Z})$. They arise because complexifying a real bundle gives a complex bundle whose odd Chern classes vanish (by an involution argument), leaving only the even ones in degrees divisible by 4. The integral $\int_{M^4} p_1$ on a closed oriented 4-manifold appears in the **signature theorem**: $\sigma(M^4) = \tfrac{1}{3}\int_M p_1$, and more generally in the **Hirzebruch signature formula** linking $p_r$ to the topological signature.

> [!tip] Unlocked: Cobordism and the Index Theorem *(from Differential Topology)*
> The **cobordism ring** $\Omega_*$ is graded by dimension and has elements [closed oriented $n$-manifolds]; multiplication is Cartesian product. Pontryagin and Stiefel–Whitney numbers $\int_M w_{i_1} \cdots w_{i_r}$ and $\int_M p_{j_1} \cdots p_{j_s}$ are **cobordism invariants**, and Thom's theorem identifies $\Omega_*$ up to torsion as a polynomial ring generated by these numbers. The **index theorem (Atiyah–Singer)** asserts that for any elliptic differential operator $D$ on a closed manifold, the analytic index ($\dim\ker D - \dim\mathrm{coker}\, D$) equals an integral of characteristic classes — the most spectacular use of Chern–Weil theory, unifying analysis (Fredholm theory), geometry (curvature), and topology (cohomology) in a single equation.

- **[[Ex - Computing c_1 of a Line Bundle from a Connection]]** (⭐⭐)
	- Explicitly compute $c_1$ for the tautological line bundle on $\mathbb{CP}^1 = S^2$ using a $U(1)$ connection in standard coordinates, and verify $\int_{S^2} c_1 = -1$.

- **[[Ex - The Chern Number of the Hopf Line Bundle over CP^1]]** (⭐⭐)
	- Compute the first Chern number of the tautological line bundle on $\mathbb{CP}^1$ (equivalently, the Hopf line bundle), confirming it is $-1$ via the curvature of the Fubini–Study connection or by direct identification of the sections that vanish.

> [!note] Exercise Index — §3.3
> [[Exercise Index - §3.3 Chern Forms and Characteristic Classes]]

## §3.4 Topological Quantisation in Physics

This section recapitulates the apparatus of §§3.1–3.3 in two physical settings: the **magnetic monopole** (a $U(1)$ bundle over $S^2$ with $\int c_1 =$ monopole charge) and the **Yang–Mills instanton** (an $SU(n)$ bundle over $\mathbb{R}^4$ extended to $S^4$ with $\int c_2 =$ instanton number). The mathematics is identical to §§3.1–3.3; the language shifts to physical observables.

> [!tip] Unlocked: Yang–Mills Theory and the BPST Instanton *(from Gauge Theory)*
> The **Yang–Mills equations** $d_A \star F = 0$ for an $SU(n)$ connection $A$ on $\mathbb{R}^4$ are second-order. Their *self-dual* and *anti-self-dual* solutions ($\star F = \pm F$) are first-order and automatically solve Yang–Mills. The simplest non-trivial example is the **BPST instanton**, an $SU(2)$ self-dual connection on $\mathbb{R}^4$ with $\int_{\mathbb{R}^4} c_2 = 1$. The **moduli space** of $SU(2)$ instantons of charge $k$ has dimension $8k - 3$ (with subtle gauge-fixing); these moduli are the data of **Donaldson theory** and lead to invariants of smooth 4-manifolds. See [[Gauge Theory IV — Yang–Mills Fields and Instantons]] for the full development.

> [!tip] Unlocked: Dirac Monopole Quantisation *(from Quantum Mechanics in a Magnetic Field)*
> A magnetic monopole with charge $g$ at the origin of $\mathbb{R}^3$ corresponds to a $U(1)$ bundle on $S^2$ whose first Chern number $\int_{S^2} c_1 = 2g/\hbar c$ must be an integer for the quantum-mechanical wavefunction (a section of the bundle) to be globally well-defined. This is the **Dirac quantisation condition** $eg = n\hbar c/2$. The mathematical content is that line bundles on $S^2 = \mathbb{CP}^1$ are classified by $\mathbb{Z}$ (their first Chern number), and the monopole charge is precisely this integer.

- **[[Ex - Winding Number of the BPST Instanton is 1]]** (⭐⭐⭐)
	- Compute $\int_{\mathbb{R}^4} c_2$ for the BPST instanton $A = \mathrm{Im}(g^{-1}dg)$ with $g(x) = (x^4 + i\vec{x}\cdot\vec{\sigma})/|x|$, verifying that the answer is $1$. Uses Frankel's identity (22.5): $\int_{\mathbb{R}^4} \mathrm{Tr}(\theta \wedge \theta) = \tfrac{1}{3}\int_{S^3_\infty} \mathrm{Tr}(g^{-1}dg)^3$.

- **[[Ex - The Magnetic Monopole and Dirac Quantization via c_1]]** (⭐⭐)
	- Compute $c_1$ of the $U(1)$ bundle on $S^2 \subset \mathbb{R}^3$ surrounding a magnetic monopole of charge $g$, and derive the Dirac quantisation condition by demanding integrality.

> [!note] Exercise Index — §3.4
> [[Exercise Index - §3.4 Topological Quantization in Physics]]

---

# Sources and Targets

**Targets — what do we usually try to prove?**

The exercises and theorems of this topic chase a small recurring set of goals. The most common is to **compute a homotopy group $\pi_k(X)$**, where $X$ is a sphere, a Lie group, a homogeneous space $G/H$, a fibre bundle total space, or a CW complex. These computations are settled either by the long exact sequence of a fibration (the dominant technique), or by the Hurewicz theorem when $X$ is sufficiently connected, or — in rare cases — by direct construction of a degree map. A second target is to **compute a Chern number $\int_z c_r$** for a specific bundle: this is settled by choosing a convenient connection (often a flat connection on the complement of a singularity, or the canonical Fubini–Study connection on a projective space), computing the curvature, and evaluating the polynomial. A third target is to **prove that a section of a vector bundle exists** (or, more often, *cannot* exist), which is settled by showing the relevant characteristic class is non-zero — the obstruction picture. A fourth target is to **identify a bundle up to isomorphism**, particularly for line bundles, where the first Chern class is a complete invariant; for higher-rank bundles, the full collection of Chern classes is necessary but not always sufficient. A fifth target, in physical contexts, is to **identify a topological quantum number** — the monopole charge, the instanton number, the winding number of a defect — and to show that it is *integer-valued* by reading it as a Chern number, hence forced to lie in $H^*_{\mathrm{dR}}(M; \mathbb{Z}) \cap H^*_{\mathrm{dR}}(M; \mathbb{R})$.

**Sources — what assumptions do we usually leverage?**

The hypotheses fall into a few stereotyped patterns. **A fibration $F \to E \to B$ is given**, immediately producing the long exact sequence and letting us compute $\pi_k$ of any one of $F, E, B$ when we know two. The Hopf fibration, the principal bundle $SU(n) \to SU(n+1) \to S^{2n+1}$, and the universal bundle $G \to EG \to BG$ are the canonical examples. **A connection on a vector bundle is given**, allowing direct computation of the curvature and hence the Chern forms. The connection is often canonical or natural (Fubini–Study on $\mathbb{CP}^n$, the trivial connection on the complement of a singularity, the Levi-Civita-induced unitary connection on a complex Riemannian manifold). **A bundle is given as a quotient or pullback**, allowing the Chern class to be transported: $c_r(f^* E) = f^* c_r(E)$, and a quotient bundle has Chern classes that follow Whitney sum rules. **Connectivity hypotheses** — "$X$ is simply connected", "$X$ is $(n-1)$-connected" — unlock Hurewicz and let us identify $\pi_n \cong H_n$. **A specific homotopy type** — sphere, Lie group, projective space, classifying space — anchors the computation to known data: $\pi_k(S^n)$ tables, $\pi_k(U(n))$ via Bott, $H^*(BG)$ as polynomial rings.

Threading through the source-target routing is a single meta-principle: **convert geometric or analytic data into topological invariants by integration, then interpret the integer as a homotopy class**. The Chern–Weil construction is the converter from analysis to topology; the obstruction picture is the converter from topology to combinatorics; the homotopy long exact sequence is the computational engine that connects them.

---

# Legal Operations

**Legal operations:**

1. **Compute $\pi_k$ via the long exact sequence of a fibration.** When given $F \to E \to B$, write out the chain $\pi_k(F) \to \pi_k(E) \to \pi_k(B) \xrightarrow{\partial} \pi_{k-1}(F) \to \cdots$ and use known terms (often trivial groups or known $\mathbb{Z}$s) to pin down the unknown ones via exactness. The trivial group sandwich is the workhorse: if $0 \to A \to B \to 0$ is exact, then $A \cong B$. *Trigger:* any computation of $\pi_k$ of a homogeneous space, sphere, or bundle total space. *Pattern:* identify the fibration, recognise that two of the three groups are known, and read off the third.

2. **Compute $\pi_n$ via Hurewicz.** When $X$ is $(n-1)$-connected, $\pi_n(X) \cong H_n(X; \mathbb{Z})$, and $H_n$ is computable by singular-homology techniques (Mayer–Vietoris, CW chain complexes, the long exact sequence of a pair). *Trigger:* the first nonzero homotopy group of a simply connected space. *Pattern:* check $(n-1)$-connectedness (often via the long exact sequence of a fibration), compute $H_n$ by your favourite homological method, conclude $\pi_n$.

3. **Pull back a bundle and its characteristic classes.** For $f : N \to M$ and a complex vector bundle $E \to M$, $f^* E \to N$ is a bundle on $N$, and $c_r(f^* E) = f^* c_r(E)$. *Trigger:* a bundle is given on a manifold mapped from another; the source manifold is easier to compute on (e.g., $S^2 \to \mathbb{CP}^n$ embedding). *Pattern:* compute the integer cohomology pullback and read off the Chern number on $N$.

4. **Use the Whitney sum formula $c(E \oplus F) = c(E) \cdot c(F)$.** When a bundle decomposes (often as a direct sum of line bundles via splitting principle), the total Chern class multiplies. *Trigger:* a direct-sum decomposition, or a short exact sequence of bundles $0 \to E' \to E \to E'' \to 0$ (which splits non-canonically but at the level of Chern classes splits canonically). *Pattern:* break the bundle, compute Chern classes term by term, multiply.

5. **Compute Chern forms from curvature in a chosen frame.** Given a connection $\omega$ and a local frame, write $\theta = d\omega + \omega \wedge \omega$ explicitly, then expand $\det(I + i\theta/(2\pi))$ to read off $c_1, c_2, \ldots$. *Trigger:* a concrete bundle whose curvature is computable. *Pattern:* often $\omega$ has a clean form (e.g., $\omega = -i A$ for an EM potential) and the algebra is just polynomial expansion.

6. **Integrate Chern forms over cycles to get integers.** $\int_z c_r(E) \in \mathbb{Z}$ for any integer cycle $z$; if the integer is non-zero, the bundle is non-trivial. *Trigger:* you have a candidate bundle and want to know if it has a global frame, or you want to identify a topological quantum number. *Pattern:* pick a representative cycle (often a sphere or a closed 4-manifold), parametrise, integrate.

7. **Lift via the homotopy lifting property.** Given a fibration $E \to B$ and a homotopy $F : W \times I \to B$ with a lift of $F(\cdot, 0)$ to $E$, produce a lift of the whole homotopy. *Trigger:* you need to lift a map from a contractible piece (a disc, an interval) into the total space, with a constraint on its restriction. *Pattern:* invoke HLP, then use the lifted endpoint to extract a fibre-valued cycle (this is the construction of $\partial$ in the long exact sequence).

8. **Use Eckmann–Hilton to commute concatenations.** When working with $\pi_k$ for $k \geq 2$, freely commute the concatenation $f + g$ and $g + f$ in homotopy classes. *Trigger:* writing $\pi_k$ additively or recognising sums of homotopy classes commute. *Pattern:* "+ is commutative on $\pi_k$ for $k \geq 2$" is the implicit licence underlying all abelian-group manipulations.

9. **Recognise a Chern number as a degree.** $\int_M c_1$ on a closed Riemann surface, $\int_{S^4} c_2$ on a $SU(2)$ bundle — these are *degrees of induced maps to classifying spaces*, $X \to BU(n)$, or equivalently of clutching maps $S^k \to U(n)$. *Trigger:* an integer-valued Chern number with no obvious geometric interpretation. *Pattern:* identify the map whose degree it computes (e.g., the gauge transformation at infinity for instantons), and use degree theory to reason about its value.

10. **Use the obstruction-cocycle interpretation.** $\int_z c_r$ is the sum, over $2r$-cells of $z$, of the homotopy class of the boundary $(2r-1)$-sphere mapped into $\pi_{2r-1}(U(n))$. *Trigger:* you want to understand *why* a Chern number is non-zero. *Pattern:* find the cells where a global frame must develop a singularity; the integer counts these with multiplicity.

11. **Chern–Simons transgression: $c_r(\omega) - c_r(\omega') = d\nu_r$.** Two connections on the same bundle differ by an exact form in Chern; this is computed via a 1-parameter family $\omega(t)$. *Trigger:* you want to show two computations of a Chern class agree, or you need an explicit boundary term in Stokes-type arguments. *Pattern:* convex-combine the connections, differentiate $c_r(\omega(t))$, integrate over $t \in [0,1]$ to get $\nu_r$.

**Illegal but tempting operations:**

> [!warning] 1. Assuming $\pi_k(X \times Y) = \pi_k(X) \oplus \pi_k(Y)$ and then assuming the same for fibrations
> The product formula $\pi_k(X \times Y) \cong \pi_k(X) \times \pi_k(Y)$ is true, and it is the special case of the long exact sequence of the *trivial* fibration. The temptation is to assume the same for a general (non-trivial) fibration $F \to E \to B$ — that $\pi_k(E) \cong \pi_k(F) \oplus \pi_k(B)$ — which is false in general. The Hopf fibration is the classical counterexample: $\pi_3(S^3) = \mathbb{Z}$ but $\pi_3(S^1) = 0$ and $\pi_3(S^2) = \mathbb{Z}$, so the would-be product formula gives the right answer here, but $\pi_2(S^3) = 0$ while $\pi_2(S^1) \oplus \pi_2(S^2) = 0 \oplus \mathbb{Z} \neq 0$. The operation becomes legal exactly when the boundary maps $\partial$ in the long exact sequence vanish, which happens for principal bundles with contractible structure group or for split fibrations.

> [!warning] 2. Assuming Hurewicz gives all $\pi_k \cong H_k$
> The Hurewicz theorem identifies $\pi_n$ with $H_n$ only at the *first nonzero degree* (assuming the appropriate connectivity). For higher degrees the map $h : \pi_k(X) \to H_k(X)$ is in general neither injective nor surjective. The classical example is $S^2$: $\pi_2(S^2) = H_2(S^2) = \mathbb{Z}$ (Hurewicz), but $\pi_3(S^2) = \mathbb{Z}$ (Hopf map) while $H_3(S^2) = 0$. The Hurewicz map $h_3 : \pi_3(S^2) \to H_3(S^2)$ is zero. The operation becomes legal only at the first nonzero degree; for higher degrees, the discrepancy is measured by **Postnikov invariants** and other higher-order homotopy data.

> [!warning] 3. Treating the de Rham Chern form as "the" Chern class
> The Chern form $c_r$ is a *specific* closed differential form depending on the connection; the **Chern class** is its de Rham cohomology *class*, an element of $H^{2r}_{\mathrm{dR}}(M; \mathbb{R})$. The temptation is to identify them: write $\int_z c_r$ without specifying which connection. This is fine for integration (the integral is connection-independent) but illegal when manipulating $c_r$ pointwise or pulling back along non-smooth maps. The genuine **Chern class** also lives in *integer* cohomology $H^{2r}(M; \mathbb{Z})$, not just real cohomology — but the de Rham construction only sees the image in real cohomology. The integral lift requires Čech-cohomology methods or classifying-space arguments. To recover the integer Chern class from the form, integrate against generators of integer homology.

> [!warning] 4. Trying to compute $\pi_k(S^n)$ for $k > n$ by direct construction
> The higher homotopy of spheres is *unspeakably* complicated: $\pi_4(S^2) = \mathbb{Z}/2$, $\pi_5(S^2) = \mathbb{Z}/2$, $\pi_6(S^2) = \mathbb{Z}/12$, and the pattern only gets worse. There is no closed-form answer, no nice combinatorial description, and computing $\pi_{n+k}(S^n)$ for fixed $k$ as $n$ varies is one of the central open problems of stable homotopy theory. The temptation is to attempt a direct geometric construction (visualise the map $S^4 \to S^2$). The operation is legal only for the small cases the long exact sequences pin down (essentially the Hopf fibrations and their iterates), and for general computations one needs the **Serre spectral sequence**, **Adams spectral sequence**, or other advanced machinery.

> [!warning] 5. Computing Chern numbers without checking orientability or compactness
> The integrality $\int_z c_r \in \mathbb{Z}$ requires $z$ to be an *integer cycle* on an *oriented* manifold, and (for non-compact manifolds) requires compactness of support or rapid falloff at infinity. The BPST instanton on $\mathbb{R}^4$ has $\int_{\mathbb{R}^4} c_2 = 1$ because the integral converges (curvature falls off like $1/|x|^4$) and the connection extends to $S^4 = \mathbb{R}^4 \cup \{\infty\}$ with the boundary contribution playing the role of the homotopy class at infinity. For a generic curvature without these conditions, the integral might diverge or might not be an integer. The operation becomes legal once you check: compact orientable $z$, or non-compact with curvature in $L^2$ and connection extending to a compactification.

---

# Problem-Solving Strategy

Every problem in this topic divides into one of three routes: **compute a homotopy group**, **compute a Chern number**, or **interpret an integer as a topological invariant of a bundle or map**. The strategy for each is structurally different but conceptually unified by the obstruction picture.

If the problem **asks for a homotopy group $\pi_k(X)$**, the first move is to look for a fibration involving $X$. Spheres sit in the Hopf-type fibrations $S^1 \to S^{2n+1} \to \mathbb{CP}^n$; Lie groups sit in $H \to G \to G/H$ for closed subgroups $H$; homogeneous spaces are bases of principal $H$-bundles. Once a fibration is identified, write down the long exact sequence (legal operation 1) and look for $0 \to ? \to ?$ or $? \to ? \to 0$ patterns that pin down unknown groups. If no fibration is available but $X$ is sufficiently connected, apply Hurewicz (operation 2): identify the first nonzero degree, compute $H_k$ by singular-homology techniques, conclude $\pi_k$. If $X$ is a sphere $S^n$ in low degree, you can also use the cellular-CW-complex picture and direct construction (degree of a map for $\pi_n(S^n)$). Almost every concrete computation in the chapter uses either Hopf-fibration arguments or the Hurewicz isomorphism — these two tools cover the vast majority of cases at this depth.

If the problem **asks to compute a Chern number $\int_z c_r$**, the route is mechanical: choose a connection on the bundle (operation 5), compute the curvature, expand $\det(I + i\theta/(2\pi))$, extract $c_r$, integrate over $z$. The strategic decision is the *choice of connection*. The cleanest choice is often a connection that is *flat away from a singularity* (Frankel's §22.5 setup): the bundle restricted to a neighbourhood of a singularity has $c_r$ supported there, and the integral localises. Alternatively, on a Kähler manifold the **Chern connection** (the unique unitary connection compatible with the holomorphic structure) has explicit curvature in coordinates — this is how $c_1$ of the tautological line bundle on $\mathbb{CP}^n$ is computed. Or, for low-rank bundles, the Whitney sum formula (operation 4) reduces to line-bundle calculations.

If the problem **asks to interpret an integer as a topological quantum number**, the conceptual move is the obstruction-cocycle picture (operation 10). Frankel's §22.5 is the model: the integer $\int c_2 = \sum_\alpha j_\alpha$, where each $j_\alpha$ is the degree of a map $S^3 \to SU(2)$ at a fibre singularity, an element of $\pi_3(SU(2)) = \mathbb{Z}$. Recognising a physical integer (instanton number, monopole charge, vortex winding) as such a degree is what makes its conservation, integrality, and topological character transparent. The recipe: identify the fibration whose long exact sequence produces a $\mathbb{Z}$ obstruction in the relevant degree, identify the gauge or section that the cocycle measures, and write the integer as a Chern number.

Threading through all three routes is one meta-principle: **integers in algebraic topology come from degrees, and degrees come from $\pi_n(S^n) = \mathbb{Z}$**. Every Chern number is — somewhere in its derivation — a degree of a map between spheres or between fibres of bundles; every homotopy invariant is — at the bottom of the chain — a count of how many times a sphere wraps another sphere. The chapter's purpose is to make this degree-counting apparatus *algebraic* and *computable* via Chern–Weil and the homotopy long exact sequence. Every question in the chapter is the question "*what is being counted, and how do I count it from the curvature?*".

---

# Most Reusable Properties

- **[[Thm - Long Exact Sequence of a Fibration|The long exact sequence of a fibration]]**: $\cdots \to \pi_k(F) \to \pi_k(E) \to \pi_k(B) \to \pi_{k-1}(F) \to \cdots$. **Typical use:** the single most-used computational tool in higher homotopy theory. Whenever you encounter a fibre bundle, a principal bundle, a homogeneous space, a covering space, a path-loop fibration, or any other situation with a "projection with fibres", this sequence relates the homotopy of total space, fibre, and base. The strategic recognition pattern is: identify the fibration, identify two of the three groups $\pi_k(F), \pi_k(E), \pi_k(B)$, use exactness to solve for the third. The trivial-group sandwich $0 \to A \to B \to 0 \implies A \cong B$ is the workhorse.

- **[[Thm - Hurewicz Theorem (Statement)|The Hurewicz isomorphism]]**: for $(n-1)$-connected $X$, $\pi_n(X) \cong H_n(X; \mathbb{Z})$. **Typical use:** when the long exact sequence cannot pin down a group (typically because too few terms are known), the Hurewicz theorem reduces the question to a homology calculation, which is approachable by completely different techniques (Mayer–Vietoris, CW chain complexes, Euler characteristic counting). The combined arc "use fibrations to establish connectivity, then Hurewicz to compute" is the dominant pattern.

- **[[Thm - Chern-Weil Theorem (Statement)|Chern–Weil]]**: invariant polynomials of curvature give closed forms whose cohomology class is connection-independent. **Typical use:** the analytic engine that builds *all* characteristic classes for vector bundles. Recognise it whenever you compute a topological invariant from local geometric data — Gauss–Bonnet, Hirzebruch signature, Chern character, $\hat A$-genus, all are instances. The same machinery applies to **gauge theories**: the action $\int F \wedge \star F$ has a topological cousin $\int \mathrm{Tr}(F \wedge F)$, which is the second Chern character and a topological invariant.

- **[[Thm - First Chern Class Classifies Line Bundles over a CW Complex|$c_1$ classifies line bundles]]**: complex line bundles on a CW complex are in bijection with $H^2(X; \mathbb{Z})$. **Typical use:** in physics, this is the statement that the electromagnetic field $F$ is a curvature on a $U(1)$ bundle whose isomorphism class is determined by $[F]/2\pi \in H^2(\text{spacetime}; \mathbb{Z})$. Dirac quantisation of magnetic charge is the integrality of $c_1$ on $S^2$. In algebraic geometry, line bundles on a complex variety form the **Picard group**, and the first Chern class is the map from Picard to $H^2$.

- **[[Def - The Hopf Map|The Hopf fibration $S^1 \to S^3 \to S^2$]]**: the simplest non-trivial fibration, generator of $\pi_3(S^2) = \mathbb{Z}$. **Typical use:** the prototype of *all* non-trivial bundle examples. Recognise it whenever you encounter $S^3 = SU(2)$, the quaternions, the magnetic monopole, the Berry phase, the BPST instanton (an "iterated Hopf"), or any $U(1)$ bundle over a 2-sphere. The integer that arises is always the first Chern number of the bundle and is always a homotopy class in $\pi_3(S^2)$.

- **The obstruction-cocycle picture (Frankel §22.5)**: $\int_z c_r =$ sum of integer obstructions to extending a section across each $2r$-cell. **Typical use:** the conceptual bridge from analytic Chern numbers to combinatorial homotopy classes. Whenever an integer arises as a topological invariant in physics or geometry, the obstruction picture explains *what is being counted*: zeros of a section, wrappings of a gauge transformation, defects in a continuous medium, vortices, monopoles. Use it to give physical meaning to formulas of the form $\int F \wedge F$.

---

# Bridges

1. **Differential geometry — Chern forms are curvature invariants of connections on vector bundles.** The Chern forms are built directly from the curvature 2-form $\theta = d\omega + \omega \wedge \omega$ of a [[Gauge Theory III — Connections in Principal and Associated Bundles|connection on a principal bundle]] (or equivalently a [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection|connection on the associated vector bundle]]). The analytic operation "form determinant of $I + i\theta/(2\pi)$ and read off polynomial coefficients" is purely linear-algebraic at each point of $M$, applied to a matrix of 2-forms in a chosen frame. The miracle is that the result is independent of the frame (because conjugation $\theta \to g\theta g^{-1}$ preserves the determinant) and is closed (because of the Bianchi identity). So Chern–Weil is the formal mechanism that turns local geometric data — a curvature 2-form — into global topological data — a de Rham cohomology class.

2. **Algebraic topology I — Hurewicz connects homotopy to homology in the first nonzero degree.** Singular homology $H_k(X; \mathbb{Z})$ counts cycles modulo boundaries — it sees "all $k$-dimensional features" of $X$. Homotopy $\pi_k(X)$ sees only those features detectable by *spheres*. For a sufficiently connected space these coincide in the first nonzero degree, but in higher degrees homotopy is strictly more refined: the homotopy class of the Hopf map $S^3 \to S^2$ is non-zero, but its homology image vanishes because $H_3(S^2) = 0$. The information about the Hopf class is captured in homology only via more refined cup-product structure (the **Hopf invariant**), and in general the gap between $\pi_*$ and $H_*$ is the subject of higher homotopy theory.

3. **Algebraic topology II — the long exact sequence generalises covering-space theory.** [[Algebraic Topology II — Fundamental Group and Covering Spaces|Covering spaces]] are the special case of fibrations where the fibre is discrete: for a covering $\tilde X \to X$ with deck group $G$, the long exact sequence reduces to the short exact sequence $1 \to \pi_1(\tilde X) \to \pi_1(X) \to G \to 1$ (with $\pi_k(\tilde X) = \pi_k(X)$ for $k \geq 2$, the lifting isomorphism). For general fibrations the fibre is non-discrete and the higher $\pi_k$ enter, but the structural picture is the same: there is an interplay between $\pi_k$ of total space, fibre, and base mediated by a boundary map. This is why covering-space theory is a special chapter of fibration theory, and why the fundamental group is just one of many "homotopy groups" with a natural exact sequence connecting them.

4. **Gauge theory — the second Chern class is the instanton number.** For an $SU(n)$ principal bundle on $\mathbb{R}^4$ with curvature 2-form $F$ (Yang–Mills field strength), the topological invariant
   $$j = \frac{1}{8\pi^2}\int_{\mathbb{R}^4} \mathrm{Tr}(F \wedge F) = -\int_{\mathbb{R}^4} c_2 \in \mathbb{Z}$$
   is the **instanton number** — the homotopy class of the gauge transformation $g : S^3_\infty \to SU(n)$ that defines the bundle's clutching, an element of $\pi_3(SU(n)) = \mathbb{Z}$. This identification is the bridge from analysis ($F$ is a connection 2-form solving Yang–Mills equations) to topology ($j$ is an obstruction integer). The full content of [[Gauge Theory IV — Yang–Mills Fields and Instantons|Yang–Mills instanton theory]] runs on this identification: instantons of charge $k$ are minimisers of the action in the sector with $c_2 = k$, the moduli space has dimension $8k - 3$ (for $SU(2)$), and the resulting **Donaldson invariants** distinguish smooth 4-manifolds.

5. **Quantum mechanics — Dirac quantisation is integrality of $c_1$.** The wavefunction of a charged quantum-mechanical particle in the field of a magnetic monopole is a section of a $U(1)$ bundle over $\mathbb{R}^3 \setminus \{0\} \simeq S^2$. For the wavefunction to be globally well-defined, this bundle must be a *complex line bundle*, and its isomorphism class is determined by $c_1 \in H^2(S^2; \mathbb{Z}) = \mathbb{Z}$. The monopole charge is the integer $\int_{S^2} c_1$, and the **Dirac quantisation condition** $eg/\hbar c = n/2$ is the statement that this integer must be a half-integer multiple (after the appropriate normalisation factors). The bridge is precisely the classification theorem [[Thm - First Chern Class Classifies Line Bundles over a CW Complex]] applied to $S^2$, with the integer interpreted as monopole charge.

6. **Riemannian geometry — Gauss–Bonnet is the first Chern number of the tangent bundle.** The classical **Gauss–Bonnet** theorem $\int_{M^2} K\, dA = 2\pi\chi(M)$ on a closed Riemannian surface is the case $\int_M c_1(TM^{1,0})$ for the holomorphic tangent line bundle of $M$ viewed as a complex 1-manifold. The Euler characteristic $\chi(M) = 2 - 2g$ is the first Chern number, and the Gaussian curvature is (up to a factor of $2\pi$) the first Chern form. The general **Gauss–Bonnet–Chern theorem** for higher-dimensional even manifolds expresses $\chi(M^{2n})$ as the integral of a specific characteristic form — the **Pfaffian** of the curvature, which is the top-degree Euler class. See [[Gauge Theory II — Fibre Bundles, Principal Bundles, and Gauss–Bonnet]] for the full statement.

7. **Algebraic geometry — Chern classes lift Picard and divisor theory to higher rank.** For a complex algebraic variety $X$, line bundles are equivalent to divisors modulo linear equivalence (the **Picard group** $\mathrm{Pic}(X)$). The first Chern class is the map $\mathrm{Pic}(X) \to H^2(X; \mathbb{Z})$, which is an isomorphism for projective curves and surjective with computable kernel in general. For higher-rank bundles the analogue is the **Grothendieck group of vector bundles** $K^0(X)$, and the Chern character $\mathrm{ch} : K^0(X) \to H^{\mathrm{even}}(X; \mathbb{Q})$ is the bridge from algebraic K-theory to cohomology. The **Hirzebruch–Riemann–Roch theorem** expresses $\chi(X, E) = \int_X \mathrm{ch}(E) \mathrm{Td}(X)$ — holomorphic Euler characteristic as an integral of Chern character and Todd class — the genuine bridge between algebraic geometry and topology.

8. **Condensed matter physics — topological insulators are classified by characteristic classes.** A band structure in a translationally invariant condensed-matter system defines a complex vector bundle over the **Brillouin zone** (a torus $T^d$). The **Chern numbers** of the filled-band sub-bundle are topological invariants — the most famous is the **TKNN integer** $\sigma_{xy} = e^2/h \cdot \int_{T^2} c_1$ in the **integer quantum Hall effect**, where the Hall conductivity is quantised in units of $e^2/h$ times the first Chern number. More refined invariants — $\mathbb{Z}_2$ classes from time-reversal symmetry, Stiefel–Whitney-type classes for symmetry-protected phases — classify **topological insulators** and **topological superconductors** into "ten-fold way" phases. The bridge is that Chern–Weil applies to vector bundles whose base is the momentum-space Brillouin zone, with the same integrality and obstruction-cocycle interpretation.

---

# Insights

**The unifying frame: integers in algebraic topology come from degrees, and degrees are everywhere.** Every integer-valued invariant in this chapter — a Chern number, a winding number, an instanton number, a monopole charge, a Euler characteristic, a degree of a map between spheres — is at bottom an instance of $\pi_n(S^n) = \mathbb{Z}$, the fact that maps from a sphere to itself are classified by their degree. The Chern number $\int_{M^{2r}} c_r$ for a $U(n)$ bundle is the degree of the classifying map $M^{2r} \to BU(n)$ pushed forward; the instanton number is the degree of the gauge transformation $S^3 \to SU(2)$ at infinity; the monopole charge is the degree of the transition function $S^1 \to U(1)$ between two coordinate patches on $S^2$. Once one believes this — that *every integer in topology is a degree* — the conceptual unity of the chapter snaps into place. Characteristic class theory is the apparatus that makes these degrees computable from analytic data.

**The true name of a characteristic class is "obstruction to global structure".** The formal definition of a characteristic class — natural transformation, polynomial in curvature, cohomology class — is the right thing to *compute* with but the wrong thing to *think*. The operational picture is that each characteristic class is the obstruction to extending some structure globally: $w_1$ is the obstruction to orientability, $w_2$ to spin structure, $c_1$ to a non-vanishing section (for line bundles) or to a global trivialisation, $c_2$ to a global frame on a 4-manifold, the Euler class to a non-vanishing vector field. Whenever you can extend a structure simplex-by-simplex up to dimension $k - 1$ but get stuck at dimension $k$, the obstruction lives in $H^k(X; \pi_{k-1}(\text{fibre}))$, and the leading characteristic class is what measures this obstruction in the principal bundle of frames. Frankel's §22.5 makes this concrete for $c_2$: the obstruction to a global $SU(n)$ frame is exactly $\sum j(\Delta^4)$, an element of $H^4(X; \pi_3(SU(n))) = H^4(X; \mathbb{Z})$, and Chern–Weil computes this integer as an integral of curvature.

**A trigger-reaction pattern: "see an integer that has no business being an integer" → "Chern–Weil".** Whenever you encounter an integral $\int_M \Omega$ that you suspect (or know) to be an integer for topological reasons — the Berry phase of a quantum system, the topological charge of a soliton, the index of an elliptic operator, the winding number of a vortex — the right reaction is to ask: *which characteristic class is this?* The answer is almost always one of $c_1, c_2,$ Euler class, signature class, $\hat A$-genus, or a polynomial combination of Chern classes. Once identified, Chern–Weil tells you the integral is connection-independent, the obstruction picture tells you what is being counted, and the long exact sequence machinery places the integer in the appropriate $\pi_k$.

**Inheritance — where does the integrality come from?** Every integrality statement in this chapter ultimately inherits from the integrality of $\pi_1(S^1) = \mathbb{Z}$. The Hopf fibration carries this to $\pi_3(S^2) = \mathbb{Z}$; the $SU(n)$ bundle structure carries it to $\pi_3(SU(n)) = \mathbb{Z}$; the obstruction picture carries it to the integrality of Chern numbers. When asked why $\int c_r$ is an integer, the chain is: the integral is the degree of a classifying map, which is a homotopy class in $\pi_{2r-1}$ of a fibre, which is $\mathbb{Z}$ because it ultimately reduces to winding-number questions about circles. The whole edifice of characteristic class theory is built on top of the integrality of $\pi_1(S^1)$.

**The Eckmann–Hilton frame: dimension creates commutativity.** The fundamental group $\pi_1$ is non-abelian in general because loops on a curve cannot slide past each other — there is "no room". For $\pi_2$ and higher, the maps are from $k$-spheres or $k$-cubes with $k \geq 2$, and the extra dimensions provide room to slide one map past another in the concatenation — forcing the group operation to be commutative. This is the **Eckmann–Hilton argument**: any set with two compatible binary operations $+$ and $\cdot$ sharing a unit must have $+ = \cdot$ and both must be commutative. Higher homotopy groups carry two compatible concatenations (along the first coordinate or the second), so they are forced abelian. The conceptual lesson: **dimension is what makes addition commutative**. This is why $H_1$ (the abelianisation of $\pi_1$) drops to $\pi_1^{\mathrm{ab}}$, but $H_k = \pi_k$ for $k \geq 2$ on sufficiently connected spaces — the Hurewicz isomorphism — needs no abelianisation step.

**The chapter's single meta-question:** every problem in this chapter is some version of "*can this structure (frame, section, gauge transformation) be extended globally, and if not, how many obstructions are there?*". The answer is always an element of a characteristic-class group, computable analytically via Chern–Weil and interpretable topologically via obstruction theory. The chapter assembles, in one piece, the machinery for posing and answering this question across every situation in geometry and physics where a global continuous structure must be patched from local data.
