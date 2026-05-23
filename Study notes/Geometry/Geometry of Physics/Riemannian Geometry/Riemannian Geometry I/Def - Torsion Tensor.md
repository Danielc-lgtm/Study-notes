---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Affine Connection on a Vector Bundle"
  - "Def - The Lie Bracket of Vector Fields"
  - "Def - Christoffel Symbols"
tags: [geometry, riemannian-geometry, connections]
---

# Notation

$(M, \nabla)$ — a smooth manifold with an affine connection on $TM$. $X, Y, Z$ — smooth vector fields on $M$. $[X, Y]$ — the [[Def - The Lie Bracket of Vector Fields|Lie bracket]]. $\Gamma^k_{ij}$ — the Christoffel symbols of $\nabla$ in a coordinate frame; $\omega^k_{ij}$ or $\omega^k{}_j(e_i)$ — the connection coefficients in a general frame. Full notation registry on [[Riemannian Geometry I — Connections and Covariant Differentiation]].

---

# Axiom Motivation

The torsion tensor measures **how much the connection fails to be symmetric**, or equivalently **how much infinitesimal parallelograms fail to close**. Here is the picture. Take two vector fields $X, Y$ at a point $p$. Walk from $p$ a tiny distance $\varepsilon$ in direction $X$, then a tiny distance $\varepsilon$ in direction $Y$ — arriving at a point $q_1$. Now from $p$, walk first $\varepsilon$ in direction $Y$, then $\varepsilon$ in direction $X$ — arriving at $q_2$. The discrepancy $q_2 - q_1$ to leading order in $\varepsilon$ is $\varepsilon^2[X, Y]$, the Lie bracket. So the Lie bracket is the *first-order failure of the manifold's coordinate system to be commutative*.

Now repeat this thought experiment with **parallel transport**. Start with a small vector $\varepsilon X$ at $p$, parallel-transport it along the direction $Y$ by $\varepsilon$; in parallel, take $\varepsilon Y$ at $p$ and parallel-transport it along $X$ by $\varepsilon$. Compose the two displacements and ask: does the parallelogram close? On a flat manifold with the flat connection, the answer is yes — the four corners form an actual parallelogram. With a non-flat or non-torsion-free connection, the parallelogram has a "twist" — a leftover displacement encoded in the *torsion*. Specifically, the leftover displacement at $p$ to leading order in $\varepsilon$ is $\varepsilon^2 T(X, Y) = \varepsilon^2(\nabla_X Y - \nabla_Y X - [X, Y])$. The Lie-bracket term $-[X, Y]$ subtracts off the failure-to-commute that is built into the smooth structure of the manifold, leaving only the failure-to-close that comes from the connection itself. The result is the torsion.

The minus sign in front of $[X, Y]$ is essential: without it, even the flat connection on $\mathbb{R}^2$ in polar coordinates would have nonzero "torsion" (because $[\partial_r, \partial_\theta] = 0$ but the Christoffel symbols are nonzero, so $\nabla_{\partial_r}\partial_\theta - \nabla_{\partial_\theta}\partial_r = (\Gamma^k_{r\theta} - \Gamma^k_{\theta r})\partial_k$). The subtraction makes the torsion measure exactly the "extra" failure of $\nabla_X Y - \nabla_Y X$ to match $[X, Y]$ — and for the Levi-Civita connection these are equal (the connection is torsion-free), so $T \equiv 0$ everywhere.

**Why is the torsion a tensor?** This is the most important and most surprising structural fact about it. The definition $T(X, Y) = \nabla_X Y - \nabla_Y X - [X, Y]$ involves derivatives, so a priori one would expect the value at $p$ to depend on the values of $X$ and $Y$ in a neighbourhood. But $T$ is actually $C^\infty(M)$-bilinear: $T(fX, Y) = fT(X, Y)$, so its value at $p$ depends only on $X(p)$ and $Y(p)$. The reason is a cancellation: $\nabla_{fX}Y = f\nabla_X Y$ ($C^\infty$-linearity of $\nabla$ in the first slot), $\nabla_Y(fX) = Y(f)X + f\nabla_Y X$ (Leibniz of $\nabla$ in the second slot), and $[fX, Y] = f[X, Y] - Y(f)X$ (Leibniz of the Lie bracket). Putting these together: $T(fX, Y) = f\nabla_X Y - (Y(f)X + f\nabla_Y X) - (f[X, Y] - Y(f)X) = f(\nabla_X Y - \nabla_Y X - [X, Y]) = fT(X, Y)$. The $Y(f)X$ terms from the Leibniz rule and from the Lie bracket *exactly cancel*, leaving the $C^\infty$-linear result. This is the prototype of "two derivatives can combine to give a tensor": the failures of $C^\infty$-linearity of two derivative operations can cancel, leaving the combination tensorial. The same kind of cancellation gives that the Riemann curvature tensor $R(X, Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X,Y]}Z$ is a tensor.

**What is the geometric meaning of torsion-freeness?** Two equivalent forms: (i) infinitesimal parallelograms close (the four corners "fit together"); (ii) the Christoffel symbols in a coordinate frame are symmetric in their lower indices, $\Gamma^k_{ij} = \Gamma^k_{ji}$. The first is the geometric picture; the second is the computational form. The two are equivalent because in a coordinate frame $[\partial_i, \partial_j] = 0$, so $T^k_{ij} = \Gamma^k_{ij} - \Gamma^k_{ji}$, and torsion-freeness is the symmetry condition.

**Why is the Levi-Civita connection torsion-free?** Because we demand it. Torsion-freeness is one of the two conditions in the definition of the Levi-Civita connection. It is forced *not* by Riemannian geometry but by a separate, structural choice. There are perfectly good connections on $TM$ that have nonzero torsion — the **Weitzenböck connection** on a Lie group ($\nabla_X Y = 0$ on left-invariant fields, with $T(X, Y) = -[X, Y]$), Cartan-Schouten connections, the spin connection in Einstein-Cartan gravity, the connections on a principal bundle with non-vanishing structure constants. Torsion-freeness is the convention chosen for Riemannian geometry because it makes the formalism cleanest: with $T = 0$, the symmetrisation move in the Koszul formula goes through, and the connection is uniquely determined by the metric. In **Einstein-Cartan gravity** (a modification of general relativity in which fermions source torsion through their spin), the torsion is nonzero and proportional to the spin angular momentum density.

**Torsion is the dual of curvature.** The pair (torsion, curvature) jointly characterise the local structure of a connection: torsion measures the antisymmetric *first-order* failure of $\nabla$ to commute ($\nabla_X Y - \nabla_Y X$ vs $[X, Y]$), while curvature measures the antisymmetric *second-order* failure ($\nabla_X\nabla_Y - \nabla_Y\nabla_X$ vs $\nabla_{[X, Y]}$). Both are antisymmetric in $X, Y$, both are tensors, and both vanish for the flat connection on $\mathbb{R}^n$. The combination of torsion-freeness and metric-compatibility is what selects the Levi-Civita connection out of the affine space of all connections; for general affine connections, the torsion and curvature are the two independent local invariants.

---

# The Definition

Let $(M, \nabla)$ be a smooth manifold with an affine connection on $TM$. The **torsion tensor** of $\nabla$ is the $(1, 2)$-tensor field $T \in \Gamma(\mathrm{Hom}(TM \otimes TM, TM))$ defined for vector fields $X, Y \in \mathfrak{X}(M)$ by
$$
T(X, Y) := \nabla_X Y - \nabla_Y X - [X, Y].
$$

The torsion tensor is **antisymmetric**: $T(X, Y) = -T(Y, X)$. It is **$C^\infty(M)$-bilinear**: $T(fX, Y) = T(X, fY) = fT(X, Y)$ for any $f \in C^\infty(M)$, so its value at $p$ depends only on the values $X(p)$ and $Y(p)$ — this is the assertion that $T$ is a tensor.

In a local coordinate frame $(x^i)$ with coordinate vector fields $\partial_i$ satisfying $[\partial_i, \partial_j] = 0$, the components are
$$
T^k_{ij} := \omega^k{}_j(\partial_i) - \omega^k{}_i(\partial_j) = \Gamma^k_{ij} - \Gamma^k_{ji}.
$$
In a general frame $(e_a)$ with $[e_a, e_b] = c^c_{ab}\,e_c$ (the structure functions of the frame), the components are
$$
T^c_{ab} = \omega^c_{ab} - \omega^c_{ba} - c^c_{ab}.
$$

A connection is **torsion-free** (also called **symmetric**) if $T \equiv 0$, equivalently
$$
\nabla_X Y - \nabla_Y X = [X, Y] \quad \text{for all } X, Y \in \mathfrak{X}(M).
$$
In a coordinate frame this becomes $\Gamma^k_{ij} = \Gamma^k_{ji}$ — the Christoffel symbols are symmetric in their lower indices.

**As a vector-valued 2-form.** The torsion tensor can be packaged as a $TM$-valued 2-form $\tau \in \Omega^2(M; TM) \cong \Gamma(\Lambda^2 T^*M \otimes TM)$:
$$
\tau = e_a \otimes \tau^a, \qquad \tau^a = \tfrac{1}{2}T^a_{bc}\,\sigma^b \wedge \sigma^c.
$$
In this language Cartan's first structural equation reads $d\sigma^a + \omega^a{}_b \wedge \sigma^b = \tau^a$ — see [[Thm - Cartan's First Structural Equation]].

---

# Relate to Other Fields / Compression

The compression: **torsion is the failure of "infinitesimal parallelograms to close" under parallel transport.** It measures the difference between $\nabla_X Y$ and $\nabla_Y X$ that is *not* accounted for by the Lie bracket $[X, Y]$. For the Levi-Civita connection torsion vanishes, which is what makes Riemannian geometry "well-behaved": geodesics correspond to extrema of arc length, the second-derivative test for length is clean, and the structural equations simplify.

In **physics**, the most prominent role of torsion is in **Einstein-Cartan gravity**, a generalisation of general relativity in which the torsion is sourced by the **spin angular momentum** of matter. The Einstein-Cartan field equations include both a metric equation (Einstein equations) and a torsion equation: $T^\lambda_{\mu\nu} = 8\pi G\,S^\lambda_{\mu\nu}$ where $S$ is the spin tensor. For ordinary matter (no spin) the torsion is zero and the theory reduces to GR; for fermionic matter the torsion is microscopic but non-vanishing, leading to a four-fermion contact interaction at short scales. The theory has experimental implications only at very high densities and is mainly of theoretical interest.

In **gauge theory**, torsion has a different role: connections on principal bundles do not naturally have torsion (torsion is a feature specific to connections on $TM$, where the bundle has the special role of being the tangent bundle of the base). The analogue in the principal-bundle setting is the **soldering form** — a $V$-valued 1-form on a principal $GL(V)$-bundle that identifies the bundle as the frame bundle of $M$ — and torsion is the covariant derivative of the soldering form.

**True name:** The "true name" of torsion is **the antisymmetric part of the connection minus the Lie bracket**. The connection $\nabla$ generates many quantities; torsion is the unique tensorial measure of "how antisymmetric is $\nabla$?" beyond what the smooth structure forces via the Lie bracket. Operationally: whenever you see $\nabla_X Y - \nabla_Y X$, replace it with $[X, Y] + T(X, Y)$. For the Levi-Civita connection the second term vanishes and you get the clean Lie-bracket form, which is what makes the Koszul-formula symmetrisation work.

---

# Examples / Corollaries

**Example: zero torsion for the Levi-Civita connection.** By definition $T \equiv 0$. In coordinates, the Christoffel formula $\Gamma^k_{ij} = \tfrac{1}{2}g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$ is manifestly symmetric in $(i, j)$ — swap $i$ and $j$ and the formula is unchanged, since the third term $-\partial_l g_{ij}$ is invariant under the swap. So torsion-freeness is built into the explicit Christoffel formula.

**Example: nonzero torsion of the Weitzenböck connection on $S^3$.** Take $S^3 = SU(2)$ with the global trivialisation given by left-invariant vector fields. Declare $\nabla X = 0$ for every left-invariant $X$ — i.e., left-invariant fields are parallel. Then for left-invariant $X, Y$ we have $\nabla_X Y = 0$ and $\nabla_Y X = 0$, so $T(X, Y) = -[X, Y]$. The torsion is the *negative* of the Lie bracket! Since $SU(2)$ is non-abelian (its Lie algebra is $\mathfrak{su}(2) \cong \mathbb{R}^3$ with the cross-product bracket), the torsion is nonzero everywhere. The connection is *flat* (curvature zero) because parallel-transport along any loop using parallel left-invariant fields returns the identity, but the torsion encodes the non-commutativity of the group. This is the prototype of "flat + nonzero torsion". See [[Ex - The Tangent Bundle of a Lie Group has a Canonical Flat Connection]].

**Example: an explicit connection with both nonzero torsion and nonzero curvature.** On $\mathbb{R}^2$ with coordinates $(x, y)$, define $\nabla$ by $\nabla_{\partial_x}\partial_x = y\,\partial_y$, $\nabla_{\partial_y}\partial_y = x\,\partial_x$, and all other $\nabla_{\partial_i}\partial_j = 0$. Then $\Gamma^y_{xx} = y$, $\Gamma^x_{yy} = x$. Torsion: $T^k_{xy} = \Gamma^k_{xy} - \Gamma^k_{yx} = 0 - 0 = 0$, so this particular example is torsion-free. (Modifying to $\nabla_{\partial_x}\partial_y = x\partial_y$, $\nabla_{\partial_y}\partial_x = 0$ gives $T^y_{xy} = x - 0 = x \neq 0$, nonzero torsion.) Curvature is computable from the second-derivative formula and is generally nonzero in either case.

**Non-example: $T$ as just $\nabla_X Y - \nabla_Y X$.** Without the $-[X, Y]$ subtraction, the expression $\nabla_X Y - \nabla_Y X$ is *not* a tensor — it has the wrong Leibniz behaviour, picking up terms involving $Y(f)X$. Only the combination $\nabla_X Y - \nabla_Y X - [X, Y]$ is tensorial, because the Leibniz terms from $\nabla_Y X$ and from $[X, Y]$ cancel exactly. This is one of the cleanest examples of "the failures of two derivative operations cancel to give a tensor".

**Corollary (torsion is the antisymmetric part of the Christoffel symbols, modulo Lie brackets).** In a coordinate frame, the antisymmetric part of $\Gamma$ is half the torsion: $\Gamma^k_{[ij]} = \tfrac{1}{2}T^k_{ij}$. So a torsion-free connection has Christoffel symbols *symmetric* in the lower indices in any coordinate frame. In a non-coordinate frame the relationship is different: $\omega^c_{[ab]} = \tfrac{1}{2}(T^c_{ab} + c^c_{ab})$ where $c^c_{ab}$ are the structure functions of the frame.

**Corollary (the torsion 2-form in Cartan's structural equation).** The vector-valued 2-form $\tau^a = \tfrac{1}{2}T^a_{bc}\sigma^b \wedge \sigma^c$ appears in Cartan's first structural equation $d\sigma^a + \omega^a{}_b \wedge \sigma^b = \tau^a$. For torsion-free connections this reduces to $d\sigma^a + \omega^a{}_b \wedge \sigma^b = 0$, which is what allows the connection 1-forms to be read off from the coframe alone — see [[Thm - Cartan's First Structural Equation]] and [[Ex - Cartan Structural Equations on S^2]].

**Corollary (independence of torsion and curvature).** Torsion and curvature are independent local invariants: there are connections with any combination of $\{T = 0, T \neq 0\} \times \{R = 0, R \neq 0\}$. The flat connection on $\mathbb{R}^n$ has both zero. The Levi-Civita connection on a curved Riemannian manifold has $T = 0$, $R \neq 0$. The Weitzenböck connection on a non-abelian Lie group has $T \neq 0$, $R = 0$. A Cartan-Schouten connection on a Lie group can be tuned to have both nonzero. Confusing torsion-freeness with flatness is the most common conceptual error in a first course on connections.

**Calibration check.** If you can perform the following three verifications, you have understood the torsion tensor. (i) Verify the $C^\infty$-bilinearity of $T(X, Y) = \nabla_X Y - \nabla_Y X - [X, Y]$ by writing out $T(fX, Y)$ in detail and confirming the Leibniz cancellations. (ii) Compute the torsion of the Weitzenböck connection on $SU(2)$ (a left-invariant frame) and confirm $T(X, Y) = -[X, Y]$ — equivalently, $T^c_{ab} = -f^c_{ab}$, the negative structure constants. (iii) Verify in coordinates that the antisymmetric part of $\Gamma$ is $\Gamma^k_{[ij]} = \tfrac{1}{2}T^k_{ij}$, and hence that torsion-free is the same as $\Gamma^k_{ij}$ symmetric in $(i, j)$.

---

# Unlocked by This

> [!tip] The First Bianchi Identity *(from Riemannian Geometry)*
> For a torsion-free connection, the Riemann curvature tensor satisfies the **first Bianchi identity** (also called the **algebraic Bianchi identity**):
> $$
> R(X, Y)Z + R(Y, Z)X + R(Z, X)Y = 0.
> $$
> The proof is a direct manipulation using only torsion-freeness ($\nabla_X Y - \nabla_Y X = [X, Y]$) and the Jacobi identity for Lie brackets ($[[X, Y], Z] + [[Y, Z], X] + [[Z, X], Y] = 0$). For a connection with nonzero torsion, the first Bianchi identity acquires correction terms involving derivatives of $T$ — so torsion-freeness is a real input. This identity is one of the key algebraic symmetries of the Riemann tensor, reducing the number of independent components from the naive $n^4$ to $\tfrac{n^2(n^2-1)}{12}$.

> [!tip] Einstein-Cartan Gravity *(from General Relativity / Mathematical Physics)*
> **Einstein-Cartan gravity** is a generalisation of general relativity in which both the metric $g_{\mu\nu}$ and the torsion tensor $T^\lambda_{\mu\nu}$ are independent dynamical fields. The torsion is sourced by the **spin angular momentum tensor** $S^\lambda_{\mu\nu}$ of matter: $T^\lambda_{\mu\nu} = 8\pi G\,S^\lambda_{\mu\nu}$. For spin-0 matter (scalar fields, fluids) the source vanishes and Einstein-Cartan reduces to standard GR. For Dirac spinors the source is nonzero, leading to a small four-fermion contact term in the action at scales $\sim G\hbar/c^3$ — too small for current experimental detection but conceptually important. The theory shows that torsion is the geometric counterpart of spin, in the same sense that curvature is the geometric counterpart of energy-momentum.
