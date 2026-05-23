---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Frame Bundle of a Vector Bundle"
  - "Def - Riemannian Metric"
  - "Def - Principal G-Bundle"
tags: [geometry, gauge-theory, riemannian, frame-bundles]
---

# Notation

For an oriented Riemannian manifold $(M, g)$ of dimension $n$, the **orthonormal frame bundle** is denoted $\mathrm{Fr}^{\mathrm{SO}}(M)$ or $\mathrm{Fr}^+_{\mathrm{O}}(M)$, a principal $\mathrm{SO}(n)$-bundle. If $M$ is Riemannian but not oriented, the **full orthonormal frame bundle** $\mathrm{Fr}^{\mathrm{O}}(M)$ is a principal $\mathrm{O}(n)$-bundle. For a Riemannian *vector bundle* $E \to M$ (with metric on fibres), $\mathrm{Fr}^{\mathrm{O}}(E)$ denotes the corresponding orthonormal frame bundle. See [[Gauge Theory II — Fibre Bundles, Principal Bundles, and Gauss–Bonnet]] for the full registry.

---

# Axiom Motivation

The orthonormal frame bundle is the **reduction of the full frame bundle from $\mathrm{GL}(n)$ to $\mathrm{O}(n)$ (or $\mathrm{SO}(n)$) made possible by the Riemannian metric**. The metric on $M$ gives meaning to "orthonormal basis": a basis $(e_1, \ldots, e_n)$ of $T_pM$ is orthonormal if $g_p(e_\alpha, e_\beta) = \delta_{\alpha\beta}$. Restricting to orthonormal frames gives a subbundle $\mathrm{Fr}^{\mathrm{O}}(M) \subset \mathrm{Fr}(TM)$, and the action of $\mathrm{GL}(n)$ on the full frame bundle restricts to an action of the subgroup $\mathrm{O}(n)$ (precisely those matrices preserving the standard inner product) on the orthonormal frames.

Why is **reduction even possible**? In general, reducing the structure group of a principal $G$-bundle along an inclusion $H \hookrightarrow G$ is obstructed: the obstruction lives in cohomology and can be nonzero. For the inclusion $\mathrm{O}(n) \hookrightarrow \mathrm{GL}(n, \mathbb{R})$, the reduction is **always possible** because the inclusion is a deformation retract: the Gram-Schmidt process defines a deformation retraction $\mathrm{GL}(n, \mathbb{R}) \to \mathrm{O}(n)$, and applying it fibrewise to local frames produces orthonormal local frames. So *every* real vector bundle with a fibre metric admits a reduction to $\mathrm{O}(n)$, and a Riemannian manifold automatically has an orthonormal frame bundle.

The same is true for further reduction to $\mathrm{SO}(n)$ provided $M$ is **orientable**: the inclusion $\mathrm{SO}(n) \hookrightarrow \mathrm{O}(n)$ has obstruction class the first Stiefel-Whitney class $w_1(M) \in H^1(M; \mathbb{Z}/2)$, and orientability is exactly $w_1(M) = 0$. So reducing further to $\mathrm{SO}(n)$ requires (and is equivalent to) an orientation. If we wished to reduce further still — to $\mathrm{Spin}(n)$, the double cover of $\mathrm{SO}(n)$ — the obstruction would be $w_2(M) \in H^2(M; \mathbb{Z}/2)$, and the reduction is the choice of a **spin structure**.

Why specialize from the full frame bundle to the orthonormal one at all? Three reasons. First, **the curvature tensor of the Levi-Civita connection is naturally $\mathfrak{so}(n)$-valued** (skew-symmetric in its last two indices, after lowering with the metric), so working on the orthonormal frame bundle puts the curvature in its natural home. Second, **the Pfaffian polynomial** that produces the Euler class is $\mathrm{SO}(n)$-invariant but not $\mathrm{GL}(n)$-invariant, so the Euler-class construction lives intrinsically on $\mathrm{Fr}^{\mathrm{SO}}(M)$. Third, **gauge transformations of Riemannian geometry are $\mathrm{O}(n)$-valued** (orthogonal changes of frame), not $\mathrm{GL}(n)$-valued.

---

# The Definition

Let $(M, g)$ be a smooth Riemannian manifold of dimension $n$. The **orthonormal frame bundle** of $M$ is
$$\mathrm{Fr}^{\mathrm{O}}(M) = \{(p, e_1, \ldots, e_n) : p \in M, \; (e_\alpha) \text{ is an orthonormal basis of } T_pM\},$$
with projection $\pi : \mathrm{Fr}^{\mathrm{O}}(M) \to M$ sending each frame to its basepoint $p$. The right action of $\mathrm{O}(n)$ is $(e_1, \ldots, e_n) \cdot g = (e \cdot g)_\beta = e_\alpha g^\alpha{}_\beta$ for $g \in \mathrm{O}(n)$. With this structure $\mathrm{Fr}^{\mathrm{O}}(M)$ is a principal $\mathrm{O}(n)$-bundle over $M$, a subbundle of the full frame bundle $\mathrm{Fr}(TM)$.

If $M$ is **oriented** (equivalently, $w_1(M) = 0$), the **oriented orthonormal frame bundle** is
$$\mathrm{Fr}^{\mathrm{SO}}(M) = \{(p, e_1, \ldots, e_n) \in \mathrm{Fr}^{\mathrm{O}}(M) : (e_\alpha) \text{ is positively oriented}\},$$
a principal $\mathrm{SO}(n)$-bundle and a connected component of $\mathrm{Fr}^{\mathrm{O}}(M)$ (which has two connected components per connected component of $M$).

More generally, for a real rank-$k$ vector bundle $E \to M$ equipped with a fibre metric, the **orthonormal frame bundle of $E$** is
$$\mathrm{Fr}^{\mathrm{O}}(E) = \bigsqcup_{p \in M} \{(f_1, \ldots, f_k) : f_\alpha \in E_p, \; \langle f_\alpha, f_\beta\rangle_p = \delta_{\alpha\beta}\},$$
a principal $\mathrm{O}(k)$-bundle (or $\mathrm{SO}(k)$-bundle if $E$ is oriented). The case $E = TM$ recovers the orthonormal frame bundle of $M$ above.

---

# Relate to Other Fields / Compression

The orthonormal frame bundle is **the frame bundle reduced via Gram-Schmidt to its compact subgroup**. The Gram-Schmidt process exhibits the homotopy equivalence $\mathrm{GL}(n, \mathbb{R}) \simeq \mathrm{O}(n)$ (a deformation retract) and provides an explicit map from any local frame of $E$ to a local orthonormal frame. Topologically, $\mathrm{Fr}^{\mathrm{O}}(M)$ and $\mathrm{Fr}(TM)$ are homotopy equivalent total spaces — the orthonormality cuts down the fibre from $\mathrm{GL}(n) \cong \mathbb{R}^{n^2}_+$ (an open subset of $\mathbb{R}^{n^2}$) to $\mathrm{O}(n)$ (a compact submanifold).

In the language of $G$-structures, the orthonormal frame bundle is **the $\mathrm{O}(n)$-structure on $TM$ provided by the Riemannian metric**. The general principle: a reduction of $\mathrm{Fr}(TM)$ to a subgroup $H \leq \mathrm{GL}(n)$ is a **classical geometry** — Riemannian ($H = \mathrm{O}(n)$), oriented Riemannian ($H = \mathrm{SO}(n)$), almost complex ($H = \mathrm{GL}(n/2, \mathbb{C})$), almost Hermitian ($H = U(n/2)$), symplectic ($H = \mathrm{Sp}(n, \mathbb{R})$), spin ($H = \mathrm{Spin}(n)$). Each geometry is precisely the data of the corresponding $H$-bundle.

**True name:** the orthonormal frame bundle is **the moduli space of orthonormal frames, with $\mathrm{O}(n)$ acting by orthogonal change of basis**. It is where the Levi-Civita connection lives most naturally as a global $\mathfrak{so}(n)$-valued 1-form, and where the curvature is a globally defined $\mathfrak{so}(n)$-valued 2-form. The Chern proof of Gauss–Bonnet works on this bundle precisely because the curvature can be both lifted and integrated there.

---

# Examples / Corollaries

**Is an instance: $\mathrm{Fr}^{\mathrm{SO}}(S^2) \cong \mathrm{SO}(3)$.** The orthonormal frame bundle of the round 2-sphere is the rotation group $\mathrm{SO}(3)$, via the identification: a point of $\mathrm{Fr}^{\mathrm{SO}}(S^2)$ is a positively oriented orthonormal frame at a point of $S^2$, equivalent to a positively oriented orthonormal basis of $\mathbb{R}^3$ with first basis vector pointing to the basepoint — i.e., a rotation matrix. The projection $\mathrm{SO}(3) \to S^2$ sends a rotation to where it sends the north pole. This realizes $S^2 = \mathrm{SO}(3)/\mathrm{SO}(2)$ as a homogeneous space and the principal bundle as $\mathrm{SO}(2) \to \mathrm{SO}(3) \to S^2$.

**Is an instance: $\mathrm{Fr}^{\mathrm{SO}}(\mathbb{R}^n) = \mathbb{R}^n \times \mathrm{SO}(n)$.** Trivial — pick the standard orthonormal frame globally; the principal bundle is trivial because there are no obstructions.

**Is an instance: $\mathrm{Fr}^{\mathrm{SO}}(T^n) = T^n \times \mathrm{SO}(n)$.** The $n$-torus is parallelizable (admits a global frame), and the flat metric makes that frame orthonormal globally; hence the orthonormal frame bundle is trivial.

**Is an instance: $\mathrm{Fr}^{\mathrm{O}}(\text{Möbius band})$ is a nontrivial principal $\mathrm{O}(1) = \mathbb{Z}/2$-bundle.** The orthonormal frame bundle of the (non-orientable) Möbius band is the orientation double cover, a connected double cover of the Möbius band, which is topologically the cylinder $S^1 \times [-1, 1]$. The nontriviality reflects the failure of $w_1$ to vanish.

**Is NOT an instance: the bundle of *non-degenerate* (but not necessarily orthonormal) frames.** This is just the full frame bundle $\mathrm{Fr}(TM)$, a principal $\mathrm{GL}(n)$-bundle. It is not the orthonormal frame bundle because the structure group is too large.

**Corollary (dimension is $n + n(n-1)/2$).** Local triviality gives $\mathrm{Fr}^{\mathrm{SO}}(M)|_U \cong U \times \mathrm{SO}(n)$, and $\dim \mathrm{SO}(n) = n(n-1)/2$.

**Corollary (every Riemannian manifold has an orthonormal frame bundle, and every oriented Riemannian manifold has $\mathrm{Fr}^{\mathrm{SO}}(M)$).** The Gram-Schmidt process applied to any local frame produces a local orthonormal frame, and the principal-bundle structure descends.

**Corollary (reduction further to $\mathrm{Spin}(n)$ is obstructed by $w_2(M)$).** The double cover $\mathrm{Spin}(n) \to \mathrm{SO}(n)$ induces a principal-bundle question: does $\mathrm{Fr}^{\mathrm{SO}}(M)$ lift to a principal $\mathrm{Spin}(n)$-bundle? The obstruction is the second **Stiefel-Whitney class** $w_2(M) \in H^2(M; \mathbb{Z}/2)$; the lift exists iff $w_2 = 0$, and is a **spin structure** on $M$.

**Calibration check.** Verify (i) $\mathrm{Fr}^{\mathrm{SO}}(S^2) \cong \mathrm{SO}(3)$ explicitly by writing down the homeomorphism (a rotation determines a frame and vice versa); (ii) $\mathrm{Fr}^{\mathrm{SO}}(T^n)$ is trivial by exhibiting the global orthonormal frame; (iii) the Möbius band fails to be orientable by checking $w_1 \neq 0$.

---

# Unlocked by This

> [!tip] Levi-Civita Connection as an SO(n)-Valued 1-Form *(from Riemannian Geometry I)*
> The **Levi-Civita connection** of a Riemannian manifold is most naturally a $\mathfrak{so}(n)$-valued 1-form on $\mathrm{Fr}^{\mathrm{SO}}(M)$ — i.e., a principal connection on the orthonormal frame bundle. This is the global, gauge-invariant form of the connection; the more familiar Christoffel-symbol expression $\Gamma^k_{ij}$ is its pullback to $M$ via a local frame. See [[Riemannian Geometry I — Connections and Covariant Differentiation]] for the connection theory.

> [!tip] Spin Structure and the Dirac Operator *(from Spinors)*
> A **spin structure** on $M$ is a principal $\mathrm{Spin}(n)$-bundle $\mathrm{Fr}^{\mathrm{Spin}}(M)$ together with a double cover $\mathrm{Fr}^{\mathrm{Spin}}(M) \to \mathrm{Fr}^{\mathrm{SO}}(M)$ equivariant with respect to $\mathrm{Spin}(n) \to \mathrm{SO}(n)$. The obstruction is $w_2(M) \in H^2(M; \mathbb{Z}/2)$. When a spin structure exists, the associated bundle $\mathrm{Fr}^{\mathrm{Spin}}(M) \times_{\mathrm{Spin}} \Delta$ for the spinor representation $\Delta$ is the **spinor bundle**, and the **Dirac operator** acts on its sections. See [[Spinors and the Dirac Equation]].

> [!tip] Euler Class from Pfaffian of Curvature *(from Characteristic Classes)*
> The Pfaffian polynomial $\mathrm{Pf}: \mathfrak{so}(2n) \to \mathbb{R}$ is $\mathrm{SO}(2n)$-invariant, so $\mathrm{Pf}(\Omega)$ for the curvature 2-form $\Omega$ of the Levi-Civita connection produces a globally defined closed $2n$-form on $M$. Its de Rham cohomology class is the **Euler class** $e(TM) \in H^{2n}(M)$, and $\int_M e(TM) = \chi(M)$ is the Gauss–Bonnet–Chern theorem. The orthonormal frame bundle is essential here: the Pfaffian is not $\mathrm{GL}(2n)$-invariant, so this construction only makes sense on $\mathrm{Fr}^{\mathrm{SO}}(M)$.
