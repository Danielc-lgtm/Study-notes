---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Lie Group"
  - "Def - The Lie Algebra of a Lie Group"
  - "Def - Lie Group Homomorphism"
  - "Def - The Differential of a Smooth Map"
tags: [geometry, differential-geometry, lie-groups]
---

# Notation

$G$ is a Lie group with Lie algebra $\mathfrak{g}$. For each $g \in G$, conjugation by $g$ is the smooth map $C_g : G \to G$, $C_g(h) = ghg^{-1}$. The adjoint representation of $G$ on $\mathfrak{g}$ is $\mathrm{Ad} : G \to \mathrm{GL}(\mathfrak{g})$, with $\mathrm{Ad}_g = d(C_g)_e$. The Lie algebra adjoint is $\mathrm{ad} : \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g}) = \mathrm{End}(\mathfrak{g})$, with $\mathrm{ad}_X(Y) = [X, Y]$. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]] for the full notation registry.

This is a compound page: it defines two interlocking notions — the adjoint representation of a Lie group $\mathrm{Ad} : G \to \mathrm{GL}(\mathfrak{g})$ and the adjoint representation of a Lie algebra $\mathrm{ad} : \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g})$ — because they are linked by the differential $\mathrm{ad} = d(\mathrm{Ad})_e$ and neither is fully usable without the other.

---

# Axiom Motivation

Every Lie group $G$ acts on itself by conjugation: $g \cdot h = ghg^{-1}$. This is a smooth action, and for each fixed $g$ the conjugation map $C_g : G \to G$ is a Lie group **automorphism** (it preserves multiplication: $C_g(h_1 h_2) = g h_1 h_2 g^{-1} = (g h_1 g^{-1})(g h_2 g^{-1}) = C_g(h_1) C_g(h_2)$). So conjugation is a structured action — it preserves not just smoothness but the entire algebraic structure.

The question is: what is the **linearization** of conjugation? The Lie functor sends each Lie group automorphism $C_g : G \to G$ to a Lie algebra automorphism $d(C_g)_e : \mathfrak{g} \to \mathfrak{g}$. Collecting these over all $g \in G$, we get a map

$$\mathrm{Ad} : G \to \mathrm{Aut}(\mathfrak{g}) \subseteq \mathrm{GL}(\mathfrak{g}), \qquad \mathrm{Ad}_g = d(C_g)_e.$$

This is the **adjoint representation** of $G$: a Lie group representation of $G$ on its own Lie algebra. It is the canonical example of a Lie group representation, available on every Lie group, and it is the linearization of the conjugation action.

Why is this called a "representation"? Because $\mathrm{Ad}$ is a Lie group homomorphism $G \to \mathrm{GL}(\mathfrak{g})$, which is exactly what a representation of $G$ on the vector space $\mathfrak{g}$ is. The check that $\mathrm{Ad}_{g_1 g_2} = \mathrm{Ad}_{g_1} \circ \mathrm{Ad}_{g_2}$ is the functoriality of the differential: $C_{g_1 g_2} = C_{g_1} \circ C_{g_2}$, hence $d(C_{g_1 g_2})_e = d(C_{g_1})_e \circ d(C_{g_2})_e$ (chain rule).

The adjoint representation has a Lie algebra counterpart, the **Lie algebra adjoint** $\mathrm{ad} : \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g})$, defined by $\mathrm{ad}_X(Y) = [X, Y]$. This is also a Lie algebra representation: $\mathrm{ad}_{[X, Y]} = [\mathrm{ad}_X, \mathrm{ad}_Y]$ in $\mathfrak{gl}(\mathfrak{g}) = \mathrm{End}(\mathfrak{g})$ (under the commutator bracket on $\mathrm{End}(\mathfrak{g})$), which is exactly the Jacobi identity in another guise.

The link between $\mathrm{Ad}$ and $\mathrm{ad}$ is the central identity (Lee Thm 20.27): $\mathrm{ad} = d(\mathrm{Ad})_e$, i.e., the Lie algebra adjoint is the differential of the Lie group adjoint at the identity. Combined with naturality of $\exp$, this gives the operational form:

$$\mathrm{Ad}_{\exp X} = \exp(\mathrm{ad}_X)$$

— meaning, conjugation by $\exp(X)$ on the Lie algebra is the matrix exponential of "bracket with $X$".

The motivation for naming and studying $\mathrm{Ad}$ specifically (rather than just "conjugation"):

**1. It converts a non-linear action to a linear one.** The conjugation action of $G$ on $G$ is a smooth action but not linear. The adjoint action of $G$ on $\mathfrak{g}$ is **linear** by construction (each $\mathrm{Ad}_g$ is a linear map). This makes it tractable to representation theory, and in particular all linear-algebraic tools — eigenvalues, invariant subspaces, characters — become available.

**2. It encodes the center.** The kernel of $\mathrm{Ad} : G \to \mathrm{GL}(\mathfrak{g})$ is the **center** $Z(G)$ of $G$ (for connected $G$, by Lee Problem 20-20). So $G/Z(G) \hookrightarrow \mathrm{GL}(\mathfrak{g})$ as a matrix group — even for abstract Lie groups, the adjoint representation provides a matrix realization of $G$ modulo its center.

**3. It connects ideals and normal subgroups.** A connected Lie subgroup $H \leq G$ of a connected Lie group is normal iff $\mathfrak{h}$ is an ideal in $\mathfrak{g}$ (Lee Thm 20.28). The bridge is exactly the adjoint representation: $H$ normal in $G$ means $\mathrm{Ad}_g(\mathfrak{h}) \subseteq \mathfrak{h}$ for all $g$, which (via the exponential and differentiating in $g$) is equivalent to $\mathrm{ad}_X(\mathfrak{h}) \subseteq \mathfrak{h}$ for all $X \in \mathfrak{g}$ — the ideal condition.

For matrix Lie groups $G \leq \mathrm{GL}(n, \mathbb{R})$, the adjoint representation has an explicit form: $\mathrm{Ad}_g(A) = g A g^{-1}$ for $g \in G$, $A \in \mathfrak{g} \subseteq \mathfrak{gl}(n)$ (Lee Problem 20-21). And $\mathrm{ad}_A(B) = [A, B] = AB - BA$, the matrix commutator.

---

# The Definition

**Lie group adjoint representation.** Let $G$ be a [[Def - Lie Group|Lie group]] with Lie algebra $\mathfrak{g}$. For each $g \in G$, define the **conjugation map** $C_g : G \to G$ by $C_g(h) = ghg^{-1}$. It is a Lie group automorphism, hence its differential at the identity, $d(C_g)_e : \mathfrak{g} \to \mathfrak{g}$, is a Lie algebra automorphism. The **adjoint representation** of $G$ is the Lie group homomorphism

$$\mathrm{Ad} : G \to \mathrm{GL}(\mathfrak{g}), \qquad \mathrm{Ad}_g = d(C_g)_e.$$

It satisfies $\mathrm{Ad}_{g_1 g_2} = \mathrm{Ad}_{g_1} \circ \mathrm{Ad}_{g_2}$ (so $\mathrm{Ad}$ is a group homomorphism) and is smooth (Lee Prop 20.24).

**Lie algebra adjoint representation.** For a [[Def - Lie Algebra|Lie algebra]] $\mathfrak{g}$, the **adjoint representation** of $\mathfrak{g}$ is the Lie algebra homomorphism

$$\mathrm{ad} : \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g}) = \mathrm{End}(\mathfrak{g}), \qquad \mathrm{ad}_X(Y) = [X, Y].$$

It satisfies $\mathrm{ad}_{[X, Y]} = [\mathrm{ad}_X, \mathrm{ad}_Y]$ — the Jacobi identity in another form — so $\mathrm{ad}$ is a Lie algebra homomorphism into the Lie algebra $\mathfrak{gl}(\mathfrak{g})$ of linear endomorphisms of $\mathfrak{g}$ under the commutator bracket.

**Link.** The Lie algebra adjoint is the differential of the Lie group adjoint at the identity (Lee Thm 20.27):

$$\mathrm{ad} = d(\mathrm{Ad})_e : \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g}).$$

By naturality of $\exp$ applied to $\mathrm{Ad} : G \to \mathrm{GL}(\mathfrak{g})$, this gives the central formula

$$\mathrm{Ad}_{\exp X} = \exp(\mathrm{ad}_X) \quad \in \mathrm{GL}(\mathfrak{g}),$$

where the right-hand exponential is the matrix exponential of $\mathrm{ad}_X \in \mathrm{End}(\mathfrak{g})$.

**Matrix form.** For matrix Lie groups $G \leq \mathrm{GL}(n, \mathbb{R})$, $\mathrm{Ad}_g(A) = g A g^{-1}$ and $\mathrm{ad}_A(B) = [A, B] = AB - BA$.

---

# Relate to Other Fields / Compression

The adjoint representation is the **canonical linear action of a Lie group on its own algebra**, obtained by linearizing the conjugation action. It is a natural example of a Lie group representation, available on every Lie group, and it is the algebraic shadow of conjugation.

From the [[Def - Lie Group Homomorphism|homomorphism side]], $\mathrm{Ad}$ is the unique Lie group homomorphism $G \to \mathrm{GL}(\mathfrak{g})$ whose derivative at $e$ is $\mathrm{ad}$. From the conjugation side, it is the differential of conjugation at the identity.

**True name:** $\mathrm{Ad}_g$ is the operator on $\mathfrak{g}$ that records **"how conjugation by $g$ acts on infinitesimal generators"**. Equivalently, by naturality, it satisfies $\exp(\mathrm{Ad}_g X) = g \exp(X) g^{-1}$ — so it is the operator on $\mathfrak{g}$ corresponding to the conjugation action on the image of $\exp$. The operational form: **conjugation in $G$, viewed through $\exp^{-1}$, becomes the adjoint representation in $\mathfrak{g}$**.

---

# Examples / Corollaries

**Is an instance: $\mathrm{Ad}$ on $\mathrm{GL}(n, \mathbb{R})$.** For $g \in \mathrm{GL}(n)$ and $A \in \mathfrak{gl}(n) = M(n, \mathbb{R})$, $\mathrm{Ad}_g(A) = g A g^{-1}$. This is matrix conjugation, restricted to the Lie algebra. The corresponding $\mathrm{ad}$ is $\mathrm{ad}_A(B) = [A, B] = AB - BA$.

**Is an instance: $\mathrm{Ad}$ on $\mathrm{SO}(3)$.** Under the identification $\mathfrak{so}(3) \cong \mathbb{R}^3$ via the hat map ($v \mapsto \widehat v$), the adjoint representation $\mathrm{Ad}_g : \mathfrak{so}(3) \to \mathfrak{so}(3)$ becomes the linear map $\mathrm{Ad}_g(\widehat v) = \widehat{gv}$ — i.e., $\mathrm{Ad}$ on $\mathrm{SO}(3)$ is the **defining representation** $\mathrm{SO}(3) \hookrightarrow \mathrm{GL}(\mathbb{R}^3)$. See [[Ex - The Adjoint Representation of SO(3) is the Defining Representation]]. This means $\mathrm{Ad} : \mathrm{SO}(3) \to \mathrm{GL}(\mathfrak{so}(3))$ is injective and its image is $\mathrm{SO}(3) \subseteq \mathrm{GL}(\mathfrak{so}(3)) = \mathrm{GL}(3, \mathbb{R})$.

**Is an instance: $\mathrm{Ad}$ on an abelian Lie group.** If $G$ is abelian, conjugation is trivial: $ghg^{-1} = h$ for all $g, h$. So $C_g = \mathrm{id}_G$ for every $g$, and $\mathrm{Ad}_g = \mathrm{id}_\mathfrak{g}$ for every $g$. The adjoint representation is the trivial representation. Correspondingly $\mathrm{ad}_X = 0$ for all $X$ (since $[X, Y] = 0$ when $\mathfrak{g}$ is abelian).

**Is an instance: $\mathrm{Ad}$ on $\mathrm{SU}(2)$.** The double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ is literally the adjoint representation of $\mathrm{SU}(2)$ on $\mathfrak{su}(2) \cong \mathbb{R}^3$, with kernel $\{\pm I\}$. So $\mathrm{Ad}(\mathrm{SU}(2)) = \mathrm{SO}(3) \subseteq \mathrm{GL}(\mathfrak{su}(2))$. This is the cleanest realization of the double cover.

**Is NOT an instance: a non-conjugation-based linear action.** Take $G = \mathrm{GL}(n, \mathbb{R})$ acting on $V = \mathbb{R}^n$ by matrix multiplication. This is a representation of $G$ on $V$, but it is *not* the adjoint representation (it acts on $\mathbb{R}^n$, not on $\mathfrak{gl}(n) = M(n, \mathbb{R})$). It is the **defining** representation, which is different.

**Corollary (faithfulness modulo center).** $\ker \mathrm{Ad} = Z(G)$ for connected $G$ (Lee Problem 20-20). *Proof:* $\mathrm{Ad}_g = \mathrm{id}$ iff $d(C_g)_e = \mathrm{id}$, iff $C_g$ is the identity on a neighborhood of $e$ (by the local diffeomorphism property of $\exp$), iff $ghg^{-1} = h$ for all $h$ in that neighborhood. Since connected $G$ is generated by any neighborhood of $e$ (Lee Prop 7.14), this propagates to all of $G$, hence $g \in Z(G)$.

**Corollary (matrix conjugation formula).** For matrix Lie groups, $\mathrm{Ad}_g(A) = g A g^{-1}$ (Lee Problem 20-21). The proof differentiates $C_g(h) = ghg^{-1}$ at $h = I$: writing $h(t) = I + tA + O(t^2)$, $C_g(h(t)) = g(I + tA + O(t^2))g^{-1} = I + t(gAg^{-1}) + O(t^2)$, so the differential at $h = I$ is $A \mapsto gAg^{-1}$.

**Corollary ($\mathrm{ad}_X = [X, \cdot]$).** The Lie algebra adjoint $\mathrm{ad}_X : \mathfrak{g} \to \mathfrak{g}$ is the linear map $Y \mapsto [X, Y]$. This is a derivation of the bracket: $\mathrm{ad}_X[Y, Z] = [\mathrm{ad}_X Y, Z] + [Y, \mathrm{ad}_X Z]$ — the Jacobi identity rewritten. Hence $\mathrm{ad}$ is a Lie algebra homomorphism into $\mathfrak{gl}(\mathfrak{g})$ (with commutator bracket).

**Corollary (exponentiation).** $\mathrm{Ad}_{\exp X} = \exp(\mathrm{ad}_X)$, where the right-hand side is the matrix exponential of $\mathrm{ad}_X \in \mathrm{End}(\mathfrak{g})$. *Proof:* naturality of $\exp$ applied to the Lie group homomorphism $\mathrm{Ad} : G \to \mathrm{GL}(\mathfrak{g})$, whose differential at $e$ is $\mathrm{ad}$.

**Calibration check.** If you can (i) verify $\mathrm{Ad}_g(A) = g A g^{-1}$ for matrix Lie groups by differentiating; (ii) compute $\mathrm{ad}_X(Y) = [X, Y]$ from the definition; (iii) state $\mathrm{Ad}_{\exp X} = \exp(\mathrm{ad}_X)$ and explain its role; and (iv) prove $\ker \mathrm{Ad} = Z(G)$ for connected $G$ — you have understood the definition correctly.

---

# Unlocked by This

> [!tip] Killing Form *(from Lie Algebra Theory)*
> The **Killing form** on $\mathfrak{g}$ is $B(X, Y) = \mathrm{tr}(\mathrm{ad}_X \circ \mathrm{ad}_Y)$, a symmetric bilinear form built entirely from the adjoint representation. **Cartan's criterion** says $\mathfrak{g}$ is semisimple iff $B$ is non-degenerate. The Killing form is $\mathrm{Ad}$-invariant: $B(\mathrm{Ad}_g X, \mathrm{Ad}_g Y) = B(X, Y)$, and on compact simple Lie groups it (with a sign) integrates to the unique bi-invariant Riemannian metric up to scaling.

> [!tip] Coadjoint Orbits *(from Symplectic Geometry and Geometric Quantization)*
> The dual representation $\mathrm{Ad}^* : G \to \mathrm{GL}(\mathfrak{g}^*)$ on the dual space of $\mathfrak{g}$ is the **coadjoint representation**. Its orbits in $\mathfrak{g}^*$ — the **coadjoint orbits** — carry a canonical symplectic structure (Kirillov–Kostant–Souriau), making them symplectic manifolds. Coadjoint orbits are the geometric setting for geometric quantization, and for $\mathfrak{u}(n)$ they are exactly the Hermitian symmetric spaces (flag manifolds).

> [!tip] Adjoint Orbits and Conjugacy Classes *(from this chapter)*
> The orbits of $\mathrm{Ad}$ on $\mathfrak{g}$ correspond to conjugacy classes of $G$ near the identity (via $\exp$). For compact $G$, every adjoint orbit is closed and is a homogeneous space $G/Z_G(X) = G/\{g : \mathrm{Ad}_g X = X\}$. For $\mathrm{SO}(3)$ acting on $\mathfrak{so}(3) \cong \mathbb{R}^3$, the orbits are concentric spheres — corresponding to the fact that rotations are classified up to conjugacy by their rotation angle.

> [!tip] Ideals and Normal Subgroups *(from this chapter)*
> A connected Lie subgroup $H \leq G$ of a connected Lie group is **normal** if and only if $\mathfrak{h}$ is an **ideal** in $\mathfrak{g}$ — closed under bracket with arbitrary $\mathfrak{g}$ elements (Lee Thm 20.28). The bridge is the adjoint representation: $H$ normal iff $\mathrm{Ad}_g(\mathfrak{h}) \subseteq \mathfrak{h}$ for all $g$, iff $\mathrm{ad}_X(\mathfrak{h}) \subseteq \mathfrak{h}$ for all $X \in \mathfrak{g}$.
