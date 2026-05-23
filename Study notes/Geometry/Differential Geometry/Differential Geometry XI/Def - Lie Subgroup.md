---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Lie Group"
  - "Def - Immersed Submanifold"
  - "Def - Embedded Submanifold"
  - "Def - Subgroup"
tags: [geometry, differential-geometry, lie-groups]
---

# Notation

$G$ denotes a Lie group with identity $e$, and $H \leq G$ a subgroup. We write $H \hookrightarrow G$ for the inclusion. When $H$ is also a smooth submanifold of $G$ with its own Lie group structure, we say $H$ is a Lie subgroup. Embedded versus immersed submanifolds are distinguished as in [[Def - Embedded Submanifold]] and [[Def - Immersed Submanifold]]. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]] for the full notation registry.

---

# Axiom Motivation

When studying a Lie [[Def - Group|group]] $G$, we naturally encounter [[Def - Subgroup|subgroups]]: kernels of [[Def - Homomorphism|homomorphisms]], stabilizers of group actions, intersections of [[Def - Subgroup|subgroups]], centralizers, normalizers. Each is a subgroup of $G$ in the algebraic sense. The question is: when does such a subgroup acquire its own structure as a Lie group, and how does that structure relate to the ambient $G$?

There are three plausible answers, each capturing a different level of compatibility.

**The strongest demand: $H$ should be an [[Def - Embedded Submanifold|embedded submanifold]] of $G$.** This means there exists a smooth chart $(U, \varphi)$ of $G$ at every point of $H$ such that $\varphi(U \cap H) = \varphi(U) \cap (\mathbb{R}^k \times \{0\})$ — a slice chart. Embedded submanifolds inherit the [[Def - Subspace|subspace]] topology, so the inclusion $H \hookrightarrow G$ is a topological embedding; equivalently $H$ is locally closed in $G$. This is the cleanest scenario, but it is restrictive: not every Lie subgroup is embedded.

**The middle demand: $H$ should be an [[Def - Immersed Submanifold|immersed submanifold]].** This means $H$ comes equipped with its own smooth manifold structure (possibly distinct from the [[Def - Subspace|subspace]] topology) such that the inclusion is a smooth immersion — a smooth map whose differential is injective everywhere. Immersed submanifolds need not carry the subspace topology, and can in fact be dense subsets of $G$ that wind around inside without ever being "locally a slice".

**The weakest demand: just a subgroup, no submanifold structure.** This is too weak for the manifold-theoretic perspective to engage; we have an abstract subgroup, but no calculus on it.

The choice that makes the theory work is **immersed submanifold + group**: a **Lie subgroup** is a subgroup $H \leq G$ equipped with a smooth manifold structure that makes the inclusion an immersion and $H$ itself a Lie group. This admits the largest class of natural examples (in particular, all images of Lie group [[Def - Homomorphism|homomorphisms]] are Lie subgroups), and we then distinguish the **embedded** Lie subgroups as a subclass.

The principal motivating example for needing "immersed but not embedded" is the **irrational winding** of the torus: the map $\gamma : \mathbb{R} \to T^2$, $\gamma(t) = (e^{2\pi i t}, e^{2\pi i \alpha t})$, is a smooth injective immersion (its differential at every point is nonzero, hence injective for the $1$-dimensional source) and a group homomorphism, so $\gamma(\mathbb{R})$ inherits a Lie group structure from $\mathbb{R}$ via $\gamma$. But when $\alpha$ is irrational, $\gamma(\mathbb{R})$ is dense in $T^2$, and the subspace topology on $\gamma(\mathbb{R})$ — which is *not* the topology making it a Lie group — has the path-component of $0$ equal to a single point. So this Lie subgroup is genuinely immersed, not embedded. The remarkable rigidity of Lie [[Def - Group|groups]] is captured by Lee Theorem 7.21: **a Lie subgroup is embedded if and only if it is closed in $G$** (with no a priori topological assumption). This is the bridge between the topological condition "closed" and the geometric condition "embedded", and it is what makes the closed subgroup theorem (Cartan) so powerful: it goes one step further and says "topologically closed subgroup" alone — with no manifold assumption at all — implies "embedded Lie subgroup".

Why not just demand that the manifold structure on $H$ be the *unique* one compatible with the inclusion? Because there can be **multiple inequivalent immersed Lie subgroup structures** on the same image set. The irrational line $\gamma(\mathbb{R})$ in $T^2$ is one example: as a Lie group via $\gamma$ it is $\mathbb{R}$, but the closure $\overline{\gamma(\mathbb{R})} = T^2$ contains many other immersed Lie subgroup structures on overlapping sets. The convention is to specify both the underlying set and its manifold/Lie group structure, with the inclusion required to be an immersion and a homomorphism.

What about a final option: demand $H$ be a topological subgroup (closed under multiplication and inversion) with the subspace topology and require this topology to coincide with a smooth manifold structure? This is exactly the embedded case, but with a subtlety: not every closed subgroup is automatically a smooth submanifold *a priori*. The miracle is that it always is (the closed subgroup theorem), but that requires proof. So in the definition we stipulate "immersed submanifold + Lie group structure" as the basic notion, and then enumerate the special cases (embedded, closed) as theorems.

---

# The Definition

Let $G$ be a Lie group. A **Lie subgroup** of $G$ is a subgroup $H \leq G$ equipped with a topology and smooth manifold structure such that:

1. $H$ is an [[Def - Immersed Submanifold|immersed submanifold]] of $G$: the inclusion $\iota : H \hookrightarrow G$ is a smooth immersion (its differential $d\iota$ is injective at every point);
2. $H$ is itself a [[Def - Lie Group|Lie group]] with respect to the inherited group operations (restriction of multiplication and inversion of $G$).

A Lie subgroup $H$ is called an **embedded Lie subgroup** if $\iota : H \hookrightarrow G$ is an [[Def - Embedded Submanifold|embedding]] — that is, $\iota$ is a topological embedding and the topology on $H$ coincides with the subspace topology from $G$.

A Lie subgroup is called a **closed Lie subgroup** if $H$ is a closed subset of $G$ in the topology of $G$.

The following equivalences hold (Lee Cor 20.13):

> A Lie subgroup $H \leq G$ is closed (as a subset of $G$) if and only if it is embedded if and only if it is a properly embedded submanifold.

So **closed = embedded** for Lie subgroups, even though the equivalence fails for general subsets and submanifolds. This is one of the rigidity facts of Lie group theory.

---

# Relate to Other Fields / Compression

A Lie subgroup is the **simultaneous smooth and group-theoretic** notion of subobject: a subset closed under the group operations *and* equipped with a smooth manifold structure compatible with the ambient one. This pairs the [[Def - Subgroup|abstract subgroup]] concept from group theory with the [[Def - Immersed Submanifold|immersed submanifold]] concept from manifold theory.

The distinction between *immersed* and *embedded* mirrors the analogous distinction in [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds|submanifold theory]]: every embedded submanifold is immersed, but the reverse fails in the presence of "winding" — the immersed line winding densely around the torus. For Lie subgroups, the gap closes under the topological condition of closedness: **closed Lie subgroup $\iff$ embedded Lie subgroup**, an equivalence that does not hold for general immersed submanifolds.

**True name:** A Lie subgroup is **a subgroup that is locally a slice of $G$ in directions of $\mathfrak{h} \subseteq \mathfrak{g}$**. Concretely: a subset $H \subseteq G$ is a Lie subgroup if and only if there exists a vector subspace $\mathfrak{h} \subseteq \mathfrak{g}$ such that in some neighborhood $U$ of $e$, $\exp$ is a diffeomorphism on $U$ and $\exp(\mathfrak{h} \cap U) = H \cap \exp(U)$, with the same condition at every other point of $H$ via left translation. The vector subspace $\mathfrak{h}$ turns out to be the Lie algebra of $H$ in $\mathfrak{g}$, and $\mathfrak{h}$ is automatically a [[Def - Lie Algebra|Lie subalgebra]] of $\mathfrak{g}$. This "slice in algebra directions" picture is what is constructed explicitly in the proof of the closed subgroup theorem.

---

# Examples / Corollaries

**Is an instance: $\mathrm{SO}(n) \subset \mathrm{O}(n) \subset \mathrm{GL}(n, \mathbb{R})$.** A chain of embedded Lie subgroups: $\mathrm{SO}(n)$ is the identity component of $\mathrm{O}(n)$ (closed, hence embedded), $\mathrm{O}(n)$ is closed in $\mathrm{GL}(n, \mathbb{R})$ (preimage of $I$ under $A \mapsto A^T A$), hence embedded.

**Is an instance: $\mathrm{SL}(n, \mathbb{R}) \subset \mathrm{GL}(n, \mathbb{R})$.** The special linear group is the kernel of $\det : \mathrm{GL}(n) \to \mathbb{R}^\times$, which is a closed normal Lie subgroup of codimension $1$ — embedded by closure.

**Is an instance: an open subgroup.** Any open subgroup $H \subseteq G$ is automatically embedded (as an open subset, it is locally a slice with codimension $0$). Lee Lemma 7.12 shows that an open subgroup is automatically closed as well (its complement is a union of open [[Def - Coset|cosets]]), hence is a union of connected components of $G$.

**Is an instance: the identity component $G^0$.** The connected component of $e$ in $G$ is a closed normal Lie subgroup of $G$, of full [[Def - Dimension|dimension]] (Lee Prop 7.15).

**Is an instance: the discrete subgroup $\mathbb{Z} \subset \mathbb{R}$.** Embedded, closed, $0$-dimensional. Its quotient $\mathbb{R}/\mathbb{Z} \cong S^1$ is a Lie group.

**Is an instance, NOT embedded: the irrational winding $\mathbb{R} \to T^2$.** For irrational $\alpha$, the map $\gamma(t) = (e^{2\pi i t}, e^{2\pi i \alpha t})$ is an injective immersion and a group homomorphism, but its image $H = \gamma(\mathbb{R})$ is dense in $T^2$. As a Lie subgroup, $H$ carries the smooth manifold structure of $\mathbb{R}$ (transported via $\gamma$), but the subspace topology on $H$ from $T^2$ is finer than the topology of $\mathbb{R}$ — in fact, in the subspace topology, $H$ is not even locally connected, while in the Lie-group topology $H \cong \mathbb{R}$ is path-connected and simply connected. So $H$ is immersed but not embedded.

**Is NOT an instance: an arbitrary subgroup that fails to be a submanifold.** Consider $\mathbb{Q} \subset \mathbb{R}$. As an abstract subgroup of $(\mathbb{R}, +)$, $\mathbb{Q}$ is a subgroup. But $\mathbb{Q}$ is not locally Euclidean — it is totally disconnected — and cannot be given any compatible smooth manifold structure as a subset of $\mathbb{R}$. So $\mathbb{Q}$ is not a Lie subgroup of $(\mathbb{R}, +)$ in any reasonable sense. (One could put the discrete topology on $\mathbb{Q}$, but then the inclusion $\mathbb{Q} \hookrightarrow \mathbb{R}$ is not an immersion in any useful sense — the source is $0$-dimensional, the target $1$-dimensional, and the inclusion is continuous but not a smooth map of manifolds.)

**Is NOT an instance: $\mathrm{GL}(n, \mathbb{Q}) \subset \mathrm{GL}(n, \mathbb{R})$.** The rational matrices form a subgroup, but they do not constitute a smooth submanifold of $\mathrm{GL}(n, \mathbb{R})$ — they are a dense subset of a different cardinality from the ambient group's connected components, with no smooth structure as a subset.

**Corollary (kernels are Lie subgroups).** For any Lie group homomorphism $F : G \to H$, $\ker F$ is a properly embedded Lie subgroup of $G$ (Lee Prop 7.16). The closedness comes from continuity of $F$ and closedness of $\{e_H\}$; the manifold structure comes from constant rank of $F$ and the [[Thm - The Rank Theorem|rank theorem]].

**Corollary (closed subgroup = embedded Lie subgroup).** By Lee Thm 7.21, a Lie subgroup of $G$ is embedded if and only if it is closed in $G$. Going further (the [[Thm - The Closed Subgroup Theorem|closed subgroup theorem]]), even a subgroup with no a priori smooth structure is automatically an embedded Lie subgroup as soon as it is topologically closed. *Calibration check:* if you can state both the "closed = embedded" equivalence for Lie subgroups and the strengthening "closed subgroup ⟹ Lie subgroup" of the closed subgroup theorem, you have understood the distinction.

**Corollary (Lie subalgebra of $\mathfrak{g}$).** Every Lie subgroup $H \leq G$ has a Lie algebra $\mathfrak{h} \subseteq \mathfrak{g}$ — a vector subspace closed under the bracket of $\mathfrak{g}$. Concretely $\mathfrak{h} = T_e H$ regarded as a subspace of $T_e G = \mathfrak{g}$, with the inherited bracket from left-invariant vector fields.

**Calibration check.** If you can (i) construct the irrational winding example and explain why it is immersed but not embedded; (ii) verify that $\mathrm{O}(n) \subset \mathrm{GL}(n, \mathbb{R})$ is a closed (hence embedded) Lie subgroup; and (iii) state the "closed = embedded" equivalence for Lie subgroups — you have understood the definition correctly.

---

# Unlocked by This

> [!tip] Closed Subgroup Theorem *(from this chapter)*
> Cartan's [[Thm - The Closed Subgroup Theorem|closed subgroup theorem]] is the central result of §11.3: **any topologically closed subgroup of a Lie group is automatically an embedded Lie subgroup**. This is the strongest version of "closed implies embedded" possible, and it converts the manifold question "is this subgroup smooth?" into the topological question "is it closed?", which is usually trivial.

> [!tip] Homogeneous Spaces $G/H$ *(from this chapter)*
> For any closed Lie subgroup $H \leq G$, the quotient $G/H$ inherits a unique smooth manifold structure (the **homogeneous space**) of dimension $\dim G - \dim H$. The closedness of $H$ is precisely what is needed for the quotient to be Hausdorff. See [[Def - Homogeneous Space]] and [[Thm - Homogeneous Space is a Smooth Manifold]].

> [!tip] Normal Lie Subgroups and Ideals *(from this chapter)*
> A connected Lie subgroup $H \leq G$ of a connected Lie group is normal if and only if its Lie algebra $\mathfrak{h}$ is an **ideal** in $\mathfrak{g}$ — closed under bracket with all of $\mathfrak{g}$. This is Lee Theorem 20.28, and it converts the group-theoretic notion of normality into the linear-algebraic notion of ideal, with the [[Def - Adjoint Representation|adjoint representation]] as the bridge.
