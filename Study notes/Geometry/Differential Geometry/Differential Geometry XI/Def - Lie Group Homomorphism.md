---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Lie Group"
  - "Def - Smooth Map between Manifolds"
  - "Def - Homomorphism"
tags: [geometry, differential-geometry, lie-groups]
---

# Notation

$G$ and $H$ denote Lie groups with identity elements $e_G$ and $e_H$. A Lie group homomorphism is written $F : G \to H$. The differential at the identity, $dF_{e_G} : T_{e_G} G \to T_{e_H} H$, is denoted $F_* : \mathfrak{g} \to \mathfrak{h}$ or $dF_e$ when the identity is understood from context. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]] for the full notation registry.

---

# Axiom Motivation

A Lie group is two structures at once: a smooth manifold and a group. The natural morphisms between two Lie groups should respect both structures simultaneously — they should be smooth maps (preserving the manifold structure) and group homomorphisms (preserving the group operation). A Lie group homomorphism is precisely this: a smooth map that is also a group homomorphism. Dropping either condition gives a strictly weaker morphism with strictly less utility.

Why **both** conditions? Consider what happens if we keep only smoothness. A smooth map $F : G \to H$ between Lie groups that does not respect the group operation is just an arbitrary smooth map of manifolds — there are vastly many such (the space $C^\infty(G, H)$ is infinite-dimensional), and they have nothing to do with the algebraic content of $G$ and $H$. None of the structural theorems of Lie group theory — that Lie group homomorphisms have constant rank, that they induce Lie algebra homomorphisms, that they intertwine exponential maps — uses anything but the homomorphism property combined with smoothness. So discarding the homomorphism condition loses essentially everything that makes the theory interesting.

Conversely, if we keep only the homomorphism condition and drop smoothness, we get an arbitrary group homomorphism $G \to H$ of the underlying abstract groups. There are also vastly many such, and they have nothing to do with the manifold structure. Worse, abstract group homomorphisms between Lie groups can be pathological: there are non-continuous (hence non-measurable, by the axiom of choice) homomorphisms $(\mathbb{R}, +) \to (\mathbb{R}, +)$ that are not linear. Of course, **smoothness implies continuity**, and one might ask whether continuity could replace smoothness in the definition. Remarkably, the answer is yes: **every continuous group homomorphism between Lie groups is automatically smooth** (Lee Problem 20-11, originally due to von Neumann). So one could define a Lie group homomorphism as a continuous group homomorphism, and the theorem then promotes continuity to smoothness for free. We choose smoothness in the definition because it is the immediate property, but the redundancy is worth knowing — it is one of the rigidity facts of Lie theory.

The structural payoff of the joint condition is **constant rank** (Lee Thm 7.5): a Lie group homomorphism $F : G \to H$ has the same rank at every point of $G$, equal to $\mathrm{rank}(dF_e)$. The proof is a one-line equivariance argument: $F \circ L_g = L_{F(g)} \circ F$, so taking differentials at the identity gives $dF_g \circ d(L_g)_e = d(L_{F(g)})_e \circ dF_e$, and since left translations are diffeomorphisms (hence have invertible differentials), $dF_g$ and $dF_e$ have the same rank. Constant rank then unlocks the [[Thm - The Rank Theorem|rank theorem]]: $F$ factors locally as a submersion followed by an immersion, so $\ker F$ is automatically a properly embedded Lie subgroup (Lee Prop 7.16) and $\mathrm{im}(F)$ is an immersed Lie subgroup of $H$. Both kernel and image are immediate, structural Lie subgroups — no extra work is needed to put manifold structures on them.

What about **isomorphisms**? A **Lie group isomorphism** is a Lie group homomorphism that is bijective and whose inverse is also a Lie group homomorphism. The non-obvious fact (Lee Cor 7.6) is that bijectivity alone forces the inverse to be smooth: a bijective Lie group homomorphism has full rank everywhere (by constant rank, since it has full rank at $e$ by the inverse function theorem applied to the bijection), hence is a local diffeomorphism everywhere, hence is a diffeomorphism. So in the definition of "Lie group isomorphism" the smoothness of $F^{-1}$ is automatic — bijectivity is enough.

---

# The Definition

Let $G$ and $H$ be Lie groups. A **Lie group homomorphism** from $G$ to $H$ is a map $F : G \to H$ that is

1. **smooth** as a map of smooth manifolds, and
2. a **group homomorphism**: $F(g_1 g_2) = F(g_1) F(g_2)$ for all $g_1, g_2 \in G$.

A Lie group homomorphism is automatically a **Lie group isomorphism** if it is bijective: by Lee Corollary 7.6, the inverse map is then automatically smooth. We write $G \cong H$ to mean there exists a Lie group isomorphism $G \to H$.

The **kernel** $\ker F = \{g \in G : F(g) = e_H\}$ is a properly embedded Lie subgroup of $G$ (Lee Prop 7.16). The **image** $\mathrm{im}(F) = F(G)$ is an immersed Lie subgroup of $H$ (Lee Prop 7.17), and is embedded when $F$ has constant rank equal to $\dim H$ — equivalently, when $F$ is a submersion.

A Lie group homomorphism has **constant rank** (Lee Thm 7.5): $\mathrm{rank}(dF_g) = \mathrm{rank}(dF_e)$ for all $g \in G$.

---

# Categorical Definition

A Lie group homomorphism is, in the categorical language of [[Def - Lie Group|Lie groups as group objects in Man]], a **morphism of group objects** in $\mathbf{Man}$. Concretely: $F : G \to H$ is a smooth map (morphism in $\mathbf{Man}$) such that the squares

$$
\begin{array}{ccc}
G \times G & \xrightarrow{m_G} & G \\
F \times F \downarrow & & \downarrow F \\
H \times H & \xrightarrow{m_H} & H
\end{array}
\quad \text{and} \quad
\begin{array}{ccc}
G & \xrightarrow{i_G} & G \\
F \downarrow & & \downarrow F \\
H & \xrightarrow{i_H} & H
\end{array}
$$

commute (and consequently $F(e_G) = e_H$, since the unit is determined by multiplication and inversion). These are the same diagrams that define a homomorphism in the category of (abstract) groups, lifted to $\mathbf{Man}$.

Lie groups and Lie group homomorphisms together form the **category $\mathbf{LieGrp}$**. The **Lie functor** $\mathrm{Lie} : \mathbf{LieGrp} \to \mathbf{LieAlg}$ sends $G \mapsto \mathfrak{g} = T_e G$ and $F \mapsto F_* = dF_e$, with the bracket on $\mathfrak{g}$ coming from left-invariant vector fields. Functoriality is the statement that $(F \circ G)_* = F_* \circ G_*$, which is the chain rule at the identity, and that $\mathrm{id}_* = \mathrm{id}$, which is immediate. The fact that $F_*$ is a Lie algebra homomorphism (preserves the bracket) is [[Thm - Lie Group Homomorphism Induces Lie Algebra Homomorphism]].

---

# Relate to Other Fields / Compression

A Lie group homomorphism is **simultaneously a homomorphism of groups and a smooth map of manifolds**, the natural notion of morphism between objects carrying both structures. In the universal-construction language, it is the morphism in the category $\mathbf{LieGrp}$.

From the [[Def - Homomorphism|group-theoretic side]], a Lie group homomorphism is a group homomorphism that, additionally, is smooth. From the smooth-manifold side, it is a smooth map that, additionally, respects multiplication. The two perspectives are intertwined and equivalent.

**True name:** A Lie group homomorphism is, operationally, **a Lie algebra homomorphism that has been integrated**. The Lie correspondence on the simply-connected side (Lee Thm 20.19) says that every Lie algebra homomorphism $\varphi : \mathfrak{g} \to \mathfrak{h}$ with $G$ simply connected lifts uniquely to a Lie group homomorphism $F : G \to H$ with $F_* = \varphi$. So at the level of objects-and-morphisms, Lie group homomorphisms out of a simply connected $G$ are equivalent to Lie algebra homomorphisms out of $\mathfrak{g}$ — and the latter are linear maps satisfying a single algebraic identity, vastly more tractable than smooth manifold morphisms.

---

# Examples / Corollaries

**Is an instance: the determinant $\det : \mathrm{GL}(n, \mathbb{R}) \to \mathbb{R}^\times$.** The determinant is a polynomial in the matrix entries, hence smooth. It is a group homomorphism because $\det(AB) = \det(A) \det(B)$. Its kernel is $\mathrm{SL}(n, \mathbb{R}) = \{A : \det A = 1\}$, a properly embedded Lie subgroup of codimension $1$.

**Is an instance: the inclusion $\iota : S^1 \hookrightarrow \mathbb{C}^\times$.** The unit circle embeds smoothly in $\mathbb{C}^\times$ as a properly embedded submanifold. The inclusion is multiplicative (the product of two unit complex numbers is a unit complex number), so it is a Lie group homomorphism. It is injective with image $S^1$.

**Is an instance: $\varepsilon : \mathbb{R} \to S^1$, $\varepsilon(t) = e^{2\pi i t}$.** This is the universal covering map of $S^1$. It is smooth (as the composition of $t \mapsto 2\pi i t$ and $z \mapsto e^z$) and a group homomorphism from $(\mathbb{R}, +)$ to $(S^1, \cdot)$ because $e^{2\pi i (s + t)} = e^{2\pi i s} e^{2\pi i t}$. Its kernel is $\mathbb{Z}$.

**Is an instance: the exponential $\exp : \mathbb{R} \to \mathbb{R}^\times$.** From the additive Lie group $(\mathbb{R}, +)$ to the multiplicative Lie group $(\mathbb{R}^\times, \cdot)$, $\exp(s + t) = \exp(s) \exp(t)$. Smooth, injective with image $\mathbb{R}_+^\times$, restricting to a Lie group isomorphism $\mathbb{R} \cong \mathbb{R}_+^\times$.

**Is an instance: the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$.** The map sends $g \in \mathrm{SU}(2)$ to the rotation $v \mapsto g v g^{-1}$ on $\mathfrak{su}(2) \cong \mathbb{R}^3$. It is a smooth Lie group homomorphism with kernel $\{\pm I\}$ and image $\mathrm{SO}(3)$. It is *not* an isomorphism — it is two-to-one — but at the Lie algebra level $\mathfrak{su}(2) \cong \mathfrak{so}(3)$ via the differential. This is the canonical illustration of the Lie correspondence failing without simple connectivity, and is worked out in [[Ex - SU(2) is Diffeomorphic to S^3]].

**Is NOT an instance: a discontinuous group homomorphism $\mathbb{R} \to \mathbb{R}$.** Using a Hamel basis of $\mathbb{R}$ over $\mathbb{Q}$, one can construct group homomorphisms $\mathbb{R} \to \mathbb{R}$ (with respect to addition) that are not $\mathbb{Q}$-linear and hence not continuous — they take infinitely many values on every uncountable subset. These are abstract group homomorphisms but **not** Lie group homomorphisms, because they are not smooth (in fact not even measurable). The smoothness condition rules them out.

**Is NOT an instance: a smooth map that is not a group homomorphism.** The map $f : \mathrm{GL}(n) \to \mathrm{GL}(n)$, $f(A) = A^2$, is smooth, but it is not a group homomorphism: $f(AB) = ABAB \neq A^2 B^2 = f(A) f(B)$ unless $A$ and $B$ commute. So $f$ is a smooth map but not a Lie group homomorphism. (It is, however, a [[Def - Smooth Map between Manifolds|smooth map of manifolds]] — illustrating that "smooth + map between Lie groups" is strictly weaker than "Lie group homomorphism".)

**Corollary (constant rank).** Every Lie group homomorphism $F : G \to H$ has constant rank. *Proof.* Equivariance $F \circ L_g = L_{F(g)} \circ F$ gives, on taking differentials at $e$, $dF_g \circ d(L_g)_e = d(L_{F(g)})_e \circ dF_e$. Since $d(L_g)_e$ and $d(L_{F(g)})_e$ are vector space isomorphisms (left translation is a diffeomorphism), composing with them preserves rank, so $\mathrm{rank}(dF_g) = \mathrm{rank}(dF_e)$ for every $g$.

**Corollary (kernel is closed).** $\ker F$ is a closed normal subgroup, hence (by the closed subgroup theorem) an embedded Lie subgroup of $G$.

**Corollary (bijection implies isomorphism).** A bijective Lie group homomorphism is automatically a Lie group isomorphism — Lee Cor 7.6, via constant rank plus the global rank theorem.

**Calibration check.** If you can verify (i) $\det : \mathrm{GL}(n) \to \mathbb{R}^\times$ is a Lie group homomorphism and compute its kernel; (ii) the constant-rank theorem from the equivariance argument; (iii) a bijective Lie group homomorphism is automatically a diffeomorphism — you have understood the definition correctly.

---

# Unlocked by This

> [!tip] Functorial Lie Algebra Homomorphism *(from this chapter)*
> Every Lie group homomorphism $F : G \to H$ induces a Lie algebra homomorphism $F_* = dF_e : \mathfrak{g} \to \mathfrak{h}$, and the assignment $G \mapsto \mathfrak{g}$, $F \mapsto F_*$ is the **Lie functor**, the cornerstone of the categorical formulation of the theory. See [[Thm - Lie Group Homomorphism Induces Lie Algebra Homomorphism]].

> [!tip] Lie Group Representation *(from Representation Theory)*
> A **representation** of a Lie group $G$ on a vector space $V$ is a Lie group homomorphism $\rho : G \to \mathrm{GL}(V)$. Differentiating gives a Lie algebra homomorphism $\rho_* : \mathfrak{g} \to \mathfrak{gl}(V)$, a **Lie algebra representation**. For compact Lie groups, the Peter–Weyl theorem decomposes $L^2(G)$ into a sum of finite-dimensional irreducible representations, the foundation of harmonic analysis on compact groups.

> [!tip] Covering Theory of Lie Groups *(from Lie Groups, Advanced)*
> Every connected Lie group $G$ has a unique simply connected covering Lie group $\widetilde G$ with a Lie group homomorphism $\pi : \widetilde G \to G$ that is a smooth covering map. The kernel of $\pi$ is a discrete central subgroup of $\widetilde G$, and conversely the discrete central subgroups of $\widetilde G$ classify the connected Lie groups with Lie algebra $\mathfrak{g}$.
