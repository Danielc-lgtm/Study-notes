---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Vector Bundle"
  - "Def - Principal G-Bundle"
  - "Def - Local Trivialization"
tags: [geometry, gauge-theory, frame-bundles]
---

# Notation

For a real rank-$k$ vector bundle $\pi : E \to M$, the **frame bundle** is denoted $\mathrm{Fr}(E)$ or $FE$, with projection $\pi_{\mathrm{Fr}} : \mathrm{Fr}(E) \to M$. A point of $\mathrm{Fr}(E)$ over $p \in M$ is an ordered basis $(f_1, \ldots, f_k)$ of $E_p$. The right action of $g = (g^\alpha{}_\beta) \in \mathrm{GL}(k, \mathbb{R})$ is $(f \cdot g)_\beta = f_\alpha g^\alpha{}_\beta$ (using Einstein summation). For $E = TM$, the frame bundle is denoted $\mathrm{Fr}(TM)$ or simply $\mathrm{Fr}(M)$. See [[Gauge Theory II — Fibre Bundles, Principal Bundles, and Gauss–Bonnet]] for the full registry.

---

# Axiom Motivation

The frame bundle is the **principal-bundle incarnation of a vector bundle**. Given a rank-$k$ real vector bundle $E$, we want to extract the data that encodes "linear structure on each fibre, varying smoothly" *without* committing to a particular basis. The frame bundle does exactly this: it remembers *all* ordered bases of all fibres simultaneously, and a single choice within $\mathrm{Fr}(E)_p$ amounts to a choice of basis for $E_p$. The structure group $\mathrm{GL}(k, \mathbb{R})$ acts on $\mathrm{Fr}(E)_p$ by changing the basis. Two key features make this the right construction.

First, the **right action is intrinsic** — it does not depend on any local trivialization. Given a frame $(f_1, \ldots, f_k)$ of $E_p$ and a matrix $g \in \mathrm{GL}(k)$, the new frame $(f \cdot g)_\beta = f_\alpha g^\alpha{}_\beta$ is determined intrinsically by $E_p$ and $g$. By contrast, the *left* action — multiplying the column vector of components by $g^{-1}$ — depends on the choice of frame, so it is *not* intrinsic. This is the precise mathematical reason gauge transformations act on the right in the principal bundle: only the right action is well-defined globally.

Second, the **vector bundle is recovered from its frame bundle** as the associated bundle $E = \mathrm{Fr}(E) \times_{\mathrm{GL}(k)} \mathbb{R}^k$, where $\mathrm{GL}(k)$ acts on $\mathbb{R}^k$ by matrix multiplication. This is the universality: every rank-$k$ vector bundle comes from its frame bundle via the associated-bundle construction, and the frame bundle is the universal source. Connection theory on $E$ is connection theory on $\mathrm{Fr}(E)$ specialized to the defining representation; tensor bundles $\otimes^r E \otimes \otimes^s E^*$ are associated bundles of $\mathrm{Fr}(E)$ with the appropriate tensor representation; and reductions of structure group (e.g., to $\mathrm{O}(k)$ if $E$ has a metric, to $\mathrm{SO}(k)$ if $E$ is also oriented) are subbundles of $\mathrm{Fr}(E)$.

Why is the **action free**? A frame $(f_1, \ldots, f_k)$ at $p$ is a basis of $E_p$, hence linearly independent. If $(f \cdot g)_\beta = f_\beta$ for all $\beta$, then $\sum f_\alpha (g^\alpha{}_\beta - \delta^\alpha_\beta) = 0$, and linear independence gives $g^\alpha{}_\beta = \delta^\alpha_\beta$, i.e., $g = I$. Without linear independence — for instance if we allowed "degenerate frames" with $f_1 = f_2$ — the action would have fixed points and the bundle would fail to be principal. The linear-independence condition is what makes $\mathrm{Fr}(E)$ a principal $\mathrm{GL}(k)$-bundle rather than some weaker object.

Why is the **action transitive on fibres**? Given any two ordered bases $(f_1, \ldots, f_k)$ and $(f'_1, \ldots, f'_k)$ of the same vector space $E_p$, there is a unique invertible linear map taking one to the other: this is the change-of-basis matrix $g \in \mathrm{GL}(k)$. So the action is not only transitive on $\mathrm{Fr}(E)_p$ but *simply* transitive (free + transitive), making each fibre a $\mathrm{GL}(k)$-torsor.

---

# The Definition

Let $\pi : E \to M$ be a smooth real rank-$k$ vector bundle. The **frame bundle** of $E$ is the set
$$\mathrm{Fr}(E) = \bigsqcup_{p \in M} \mathrm{Fr}(E)_p, \qquad \mathrm{Fr}(E)_p = \{(f_1, \ldots, f_k) : f_\alpha \in E_p, \; (f_1, \ldots, f_k) \text{ is a basis of } E_p\},$$
with projection $\pi_{\mathrm{Fr}} : \mathrm{Fr}(E) \to M$ sending each frame to its basepoint $p$. The right action of $\mathrm{GL}(k, \mathbb{R})$ is
$$(f_1, \ldots, f_k) \cdot g = (f \cdot g)_\beta = f_\alpha g^\alpha{}_\beta,$$
where $g = (g^\alpha{}_\beta) \in \mathrm{GL}(k)$.

$\mathrm{Fr}(E)$ inherits a smooth manifold structure of dimension $\dim M + k^2$ as follows: given a local frame $(\sigma_1, \ldots, \sigma_k)$ of $E$ over $U$ (i.e., a local section of $\mathrm{Fr}(E)$ over $U$), the local trivialization is
$$\Phi_U : \pi_{\mathrm{Fr}}^{-1}(U) \to U \times \mathrm{GL}(k, \mathbb{R}), \qquad \Phi_U(\sigma(p) \cdot g) = (p, g).$$
With this smooth structure and the right $\mathrm{GL}(k)$-action, $\mathrm{Fr}(E)$ is a **principal $\mathrm{GL}(k, \mathbb{R})$-bundle** over $M$ in the sense of [[Def - Principal G-Bundle]]. The transition functions of $\mathrm{Fr}(E)$ between two local trivializations from frames $\sigma_U$ and $\sigma_V$ coincide with the transition functions of $E$.

---

# Relate to Other Fields / Compression

The frame bundle is **a vector bundle with the linear structure stripped away, replaced by the change-of-basis $\mathrm{GL}(k)$-action**. The vector bundle $E$ has fibres that are vector spaces $E_p \cong \mathbb{R}^k$; the frame bundle $\mathrm{Fr}(E)$ has fibres that are bases of those vector spaces. The forgetful direction is: $\mathrm{Fr}(E)$ remembers the basis but forgets the vector space; the recovery direction is: $E = \mathrm{Fr}(E) \times_{\mathrm{GL}(k)} \mathbb{R}^k$ rebuilds the vector space using the standard representation.

The frame bundle is a **functor** from the category of vector bundles to the category of principal $\mathrm{GL}$-bundles: a vector bundle morphism $E \to E'$ over the identity on $M$ that is an isomorphism on each fibre induces a principal $\mathrm{GL}(k)$-bundle map $\mathrm{Fr}(E) \to \mathrm{Fr}(E')$ in an obvious way. This is part of an equivalence of categories: vector bundles of rank $k$ with isomorphisms $\leftrightarrow$ principal $\mathrm{GL}(k, \mathbb{R})$-bundles with $\mathrm{GL}(k)$-equivariant maps.

**True name:** the frame bundle is **the moduli space of bases for $E$, with $\mathrm{GL}(k)$ acting by change of basis**. Operationally, working with $\mathrm{Fr}(E)$ is what you do when you want to *not* commit to a basis — for instance when working with connection forms (which depend on a frame), curvature forms, or characteristic classes (which are basis-independent in their final form but computed from basis-dependent ingredients). The frame bundle is the home where all bases live equally, and the right $\mathrm{GL}(k)$-action records the freedom to choose one.

---

# Examples / Corollaries

**Is an instance: $\mathrm{Fr}(M \times \mathbb{R}^k) = M \times \mathrm{GL}(k, \mathbb{R})$.** For the trivial vector bundle, the frame bundle is the trivial principal $\mathrm{GL}(k)$-bundle: $\mathrm{Fr}(M \times \mathbb{R}^k)_p$ is the set of bases of $\mathbb{R}^k$, which is $\mathrm{GL}(k)$.

**Is an instance: $\mathrm{Fr}(T\mathbb{R}^n) = \mathbb{R}^n \times \mathrm{GL}(n)$.** The tangent bundle of $\mathbb{R}^n$ is trivial, so its frame bundle is trivial. A global frame is the coordinate frame $(\partial/\partial x^1, \ldots, \partial/\partial x^n)$; using it as a global section trivializes the bundle. See [[Ex - Frame Bundle of R^n is Trivial]].

**Is an instance: $\mathrm{Fr}(TS^2)$ is a nontrivial principal $\mathrm{GL}(2, \mathbb{R})$-bundle over $S^2$.** Triviality would give a global frame, hence a global nowhere-vanishing section of $TS^2$ (i.e., a continuous unit tangent vector field), contradicting the hairy-ball theorem ($\chi(S^2) = 2 \neq 0$). The reduction $\mathrm{Fr}^{\mathrm{SO}}(S^2)$ to the orthonormal frame bundle is the principal $\mathrm{SO}(2) = U(1)$-bundle whose total space is $\mathrm{SO}(3)$, and the Hopf-fibration-style identification $\mathrm{SO}(2) \to \mathrm{SO}(3) \to S^2$ exhibits this nontriviality concretely.

**Is an instance: $\mathrm{Fr}(L) = M \times \mathbb{R}^*$ for a trivial real line bundle $L = M \times \mathbb{R}$.** For a rank-1 real bundle, $\mathrm{GL}(1, \mathbb{R}) = \mathbb{R}^* = \mathbb{R} \setminus \{0\}$, and a frame is just a nonzero element of each fibre. For the Möbius line bundle over $S^1$, the frame bundle is the orientation double cover of $S^1$ times $\mathbb{R}^*_+$ — nontrivial.

**Is NOT an instance: the bundle whose fibre at $p$ is the set of *linearly dependent* tuples $(v_1, \ldots, v_k)$ in $E_p$.** This is not a principal $\mathrm{GL}(k)$-bundle because the action is not free: $(v_1, v_1)$ is fixed by $\mathrm{diag}(1, 1) + \cdots$, i.e., infinitely many group elements. It is some kind of bad quotient, not a frame bundle.

**Corollary (local sections of $\mathrm{Fr}(E)$ are local frames of $E$, and vice versa).** A smooth local section $s : U \to \mathrm{Fr}(E)$ assigns to each $p \in U$ an ordered basis of $E_p$, varying smoothly — i.e., a local frame $(\sigma_1(p), \ldots, \sigma_k(p))$. Conversely, a local frame *is* a local section. So global sections of $\mathrm{Fr}(E)$ are global frames of $E$, and $E$ is trivial iff $\mathrm{Fr}(E)$ admits a global section.

**Corollary (every rank-$k$ vector bundle is recovered from its frame bundle).** $E = \mathrm{Fr}(E) \times_{\mathrm{GL}(k, \mathbb{R})} \mathbb{R}^k$, where $\mathrm{GL}(k)$ acts on $\mathbb{R}^k$ by the defining representation. This is the universal property: the frame bundle generates the vector bundle, and any *other* bundle with the same structure group (dual bundle, tensor bundle, etc.) is obtained as $\mathrm{Fr}(E) \times_{\mathrm{GL}(k)} F$ for the appropriate $\mathrm{GL}(k)$-representation $F$.

**Corollary (frame bundle has dimension $\dim M + k^2$).** Local triviality gives $\mathrm{Fr}(E)|_U \cong U \times \mathrm{GL}(k, \mathbb{R})$, and $\mathrm{GL}(k, \mathbb{R})$ has dimension $k^2$.

**Calibration check.** Verify (i) $\mathrm{Fr}(T\mathbb{R}^n)$ is trivial by constructing the explicit global section from coordinate vector fields; (ii) the right action of $\mathrm{GL}(k)$ is intrinsic by writing the action in two different local trivializations and verifying they agree; (iii) the transition functions of $\mathrm{Fr}(E)$ match those of $E$.

---

# Unlocked by This

> [!tip] Reduction of Structure Group *(from G-Structures)*
> A **reduction** of $\mathrm{Fr}(E)$ along an inclusion $H \hookrightarrow \mathrm{GL}(k)$ is a principal $H$-subbundle $\mathrm{Fr}^H(E) \subset \mathrm{Fr}(E)$. Reductions correspond to geometric structures: $H = \mathrm{O}(k)$ (Riemannian metric on $E$), $H = \mathrm{SO}(k)$ (oriented Riemannian), $H = \mathrm{GL}(k, \mathbb{C}) \hookrightarrow \mathrm{GL}(2k, \mathbb{R})$ (complex structure), $H = \mathrm{Sp}(k, \mathbb{R})$ (symplectic structure), $H = \mathrm{Spin}(k)$ (spin structure, obstructed by $w_2 \in H^2(M; \mathbb{Z}/2)$). The whole theory of *G-structures on manifolds* lives at this level.

> [!tip] Connection on the Frame Bundle *(from Gauge Theory)*
> A connection on the vector bundle $E$ — a covariant derivative $\nabla : \Gamma(E) \to \Gamma(E \otimes T^*M)$ — corresponds bijectively to a **principal connection** on $\mathrm{Fr}(E)$: a $\mathfrak{gl}(k)$-valued 1-form $\omega$ on $\mathrm{Fr}(E)$ satisfying $R_g^*\omega = \mathrm{Ad}(g^{-1})\omega$ and reproducing the Maurer-Cartan form on fibres. The principal-bundle connection is *globally defined* on $\mathrm{Fr}(E)$, while the local matrix-of-1-forms description on $E$ depends on a frame. This is the key reason to work with frame bundles: connection forms become global. See [[Gauge Theory III — Connections in Principal and Associated Bundles]].
