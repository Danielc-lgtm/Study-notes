---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Fibre Bundle"
  - "Def - Lie Group"
  - "Def - Smooth Action of a Lie Group"
tags: [geometry, gauge-theory, principal-bundles]
---

# Notation

A principal $G$-bundle is written $\pi : P \to M$ or $G \to P \to M$; the right action of $g \in G$ on a point $u \in P$ is denoted $u \cdot g$ or $R_g(u)$. The fibre over $p \in M$ is $\pi^{-1}(p)$ and is a single $G$-orbit, diffeomorphic to $G$ once a basepoint has been chosen. Local sections are written $s_U : U \to P$; choosing a local section is equivalent to choosing a local trivialization $\Phi_U(s_U(p) \cdot g) = (p, g)$. See [[Gauge Theory II — Principal Bundles, Representations, and Bundle Classification]] for the full registry.

---

# Axiom Motivation

A principal bundle is the **special fibre bundle in which the fibre is the structure group itself, with the natural left-translation transition functions**. Why specialize to this case? Because it is the **universal** case from which every other bundle with the same structure group is built. Once you have the principal bundle $P$ of frames, you build the associated vector bundle $P \times_G \mathbb{R}^k$, the unit-sphere bundle $P \times_G S^{k-1}$, the tensor bundle $P \times_G T^{r,s}$, the spinor bundle $P \times_G \Delta$, and in general $P \times_G F$ for any $G$-manifold $F$. The principal bundle is the "free" object: it knows about the structure group but has no particular fibre yet.

Why is the **right** $G$-action on $P$ intrinsic and the left action only local? In a local trivialization $P|_U \cong U \times G$, both left and right multiplication by $G$ are defined on the second factor. But the *left* action depends on the trivialization: in a different trivialization $P|_V \cong V \times G$, the same fibre point is represented by a different group element $g_V = c_{VU}(p) g_U$, and left multiplication does not commute with this change-of-trivialization map. Right multiplication, on the other hand, *does* commute: if $g_V = c_{VU} g_U$ then $g_V h = c_{VU} (g_U h)$ — the right multiplication by $h$ is the same in both trivializations. This is the mathematical reason left and right cancel each other out: left translations by $c_{VU}$ commute with right translations by $h$, so the right action is well-defined globally on $P$ while the left action is only well-defined fibre-by-fibre.

Why **freeness** of the right action? A right $G$-action on $P$ is *free* if $u \cdot g = u$ implies $g = e$. This is what makes the fibres "thin" — each fibre is a single $G$-orbit with no internal $G$-symmetry, so the fibre is literally a copy of $G$ (after choosing a basepoint). If we dropped freeness — i.e., allowed fixed points — the orbits would be quotients of $G$ by stabilizer subgroups, and we would no longer have a bundle with fibre $G$ but rather a bundle whose fibres are *coset spaces* $G/H_p$ with stabilizer $H_p$ depending on $p$. This is not a principal bundle at all; it is a more general associated bundle. The counterexample to allowing fixed points: $G = \mathrm{SO}(3)$ acting on $S^2$ by rotations has orbits $\{S^2\}$ (transitive) but fixed-point sets at each pole (kind of); the natural object is the orbit space, which is a point, but $\mathrm{SO}(3) \to S^2$ is *not* a principal bundle because the action on $S^2$ is not what we want — rather, $\mathrm{SO}(2) \to \mathrm{SO}(3) \to S^2$ is the principal $\mathrm{SO}(2)$-bundle.

Why **transitivity** on fibres? A right $G$-action is *transitive* on fibres of $\pi$ if $\pi(u) = \pi(v)$ implies $v = u \cdot g$ for some $g \in G$. Combined with freeness, this says every fibre is a single $G$-orbit, with $G$ acting simply transitively. This is what makes the fibre a copy of $G$: pick any $u \in \pi^{-1}(p)$, and the map $g \mapsto u \cdot g$ is a bijection $G \to \pi^{-1}(p)$. If transitivity fails, the fibre is a disjoint union of $G$-orbits, and the bundle is not "principal" in any useful sense — it is some kind of pseudo-principal object whose fibres are not group-like.

Why **smooth orbit space**? This is the hypothesis that $P/G$ has a smooth manifold structure such that $\pi$ is a smooth submersion. For free, proper actions of Lie groups on manifolds, this is automatic (the quotient manifold theorem), so the condition is often subsumed under the freeness/properness hypothesis. The reason it must hold: without it, the base $M = P/G$ is not a manifold and the bundle machinery does not apply. The counterexample: $G = \mathbb{R}$ acting on $\mathbb{R}^2$ by $t \cdot (x, y) = (x + t, y + t\alpha)$ with $\alpha$ irrational has free orbits, but the orbit space $\mathbb{R}^2/G$ is not Hausdorff (the irrational winding makes orbits dense), so this is not a principal bundle. The standard repair: require the action to be **proper** in addition to free, which guarantees the orbit space is Hausdorff and smooth.

In summary: a principal $G$-bundle is a smooth manifold $P$ with a free, fibre-preserving, transitive right $G$-action whose orbit space is the smooth base $M = P/G$. The structure-group / left-translation transition functions in the fibre-bundle formulation are *equivalent* to this right-action description, and the equivalence is the content of [[Thm - Principal Bundles are Locally Trivial via G-Action]].

---

# The Definition

A **principal $G$-bundle** $\pi : P \to M$ over a smooth manifold $M$, with structure group a Lie group $G$, is a fibre bundle whose typical fibre is $G$ and whose transition functions act on $F = G$ by **left translation**: in any two trivializations $\Phi_U, \Phi_V$ the change of trivialization is
$$\Phi_U \circ \Phi_V^{-1}(p, g) = (p, c_{UV}(p) \cdot g)$$
for transition functions $c_{UV} : U \cap V \to G$ satisfying the cocycle condition.

Equivalently, a principal $G$-bundle is a smooth manifold $P$ with a smooth **right action**
$$P \times G \to P, \qquad (u, g) \mapsto u \cdot g = R_g(u)$$
such that:

1. The action is **free**: $u \cdot g = u$ implies $g = e$.
2. The action is **proper**: the map $P \times G \to P \times P$, $(u, g) \mapsto (u, u \cdot g)$, is proper (preimages of compact sets are compact).
3. The orbit space $M = P/G$ inherits a smooth manifold structure and the quotient map $\pi : P \to M$ is a smooth surjective submersion.
4. The bundle is **locally trivial in a $G$-equivariant way**: $M$ is covered by open sets $U$ together with $G$-equivariant diffeomorphisms $\Phi_U : \pi^{-1}(U) \to U \times G$ — that is, $\Phi_U(u \cdot g) = (\pi(u), \mathrm{pr}_2(\Phi_U(u)) \cdot g)$.

The two formulations are equivalent: see [[Thm - Principal Bundles are Locally Trivial via G-Action]].

A **local section** of $P$ over $U \subseteq M$ is a smooth $s_U : U \to P$ with $\pi \circ s_U = \mathrm{id}_U$. Local sections are in bijection with local trivializations via $\Phi_U^{-1}(p, g) = s_U(p) \cdot g$. The bundle is **trivial** if and only if it admits a **global** section.

---

# Categorical Definition

A principal $G$-bundle on $M$ is a $G$-torsor object in the category of smooth manifolds over $M$. Concretely: in the slice category $\mathbf{Man}/M$ (smooth manifolds equipped with a smooth map to $M$), a principal $G$-bundle is an object $P \to M$ together with a $G$-action $P \times G \to P$ (over $M$) such that the map $(\mathrm{pr}_1, \mu) : P \times G \to P \times_M P$ is a $G$-equivariant diffeomorphism — that is, $P$ is a **$G$-torsor** in the relative category over $M$. The torsor condition is the categorical reformulation of "free and transitive on fibres". On a single fibre this says $G$ acts simply transitively; over $M$ it says this holds smoothly and uniformly.

The classification of principal $G$-bundles over $M$ up to isomorphism is the set $[M, BG]$ of homotopy classes of maps from $M$ to the **classifying space** $BG$: pulling back the universal principal $G$-bundle $EG \to BG$ along $f : M \to BG$ produces $f^*EG$, and every principal $G$-bundle is of this form. This is the categorical statement: the functor "principal $G$-bundles on $M$" from $\mathbf{Man}$ to $\mathbf{Set}$ is representable by $BG$ (in the homotopy category).

---

# Relate to Other Fields / Compression

A principal $G$-bundle is a **$G$-torsor in families, smoothly parametrized by $M$**. A $G$-torsor (or principal homogeneous $G$-space) is a set $X$ on which $G$ acts freely and transitively; choosing any point $x_0 \in X$ gives a bijection $G \to X$, $g \mapsto x_0 \cdot g$. The principal-bundle definition is the family version: each fibre is a $G$-torsor, varying smoothly over $M$. Once you know what a $G$-torsor is, the principal-bundle definition is just "smooth family of $G$-torsors with local triviality."

A principal $G$-bundle generalizes a **covering space** to the case of a Lie-group fibre. A connected covering $\tilde M \to M$ with deck transformation group $\Gamma$ is a principal $\Gamma$-bundle, with $\Gamma$ a discrete Lie group. The universal cover of $M$ is the principal $\pi_1(M)$-bundle; the classification of covering spaces of $M$ by subgroups of $\pi_1(M)$ is the special case of the principal-bundle classification for discrete structure group. See [[Algebraic Topology II — Fundamental Group and Covering Spaces]].

A principal $U(1)$-bundle over a manifold is the **geometric object underlying electromagnetism**. The total space encodes the gauge potential, the connection 1-form encodes $A_\mu$, the curvature encodes the field strength $F_{\mu\nu}$, and gauge transformations are smooth maps $M \to U(1)$. See [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]] for the EM-specific theory and [[Gauge Theory IV — Yang–Mills Fields and Instantons]] for the generalization to non-abelian $G$.

**True name:** a principal $G$-bundle is **a free smooth right $G$-action with smooth orbit space**. The "transition functions act by left translation" formulation from fibre bundles is the local picture; the "free right action" formulation is the global picture. The latter is operationally what you reach for: when constructing a principal bundle, identify the free $G$-action; when computing with one, exploit that the right action is intrinsic and well-defined everywhere.

---

# Examples / Corollaries

**Is an instance: the frame bundle $\mathrm{Fr}(E)$ of a real rank-$k$ vector bundle.** $\mathrm{Fr}(E)_p = \{\text{ordered bases of } E_p\}$, with right action $(f_1, \ldots, f_k) \cdot g = (\sum f_\alpha g^\alpha{}_1, \ldots, \sum f_\alpha g^\alpha{}_k)$ for $g \in \mathrm{GL}(k, \mathbb{R})$. This is the universal principal $\mathrm{GL}(k, \mathbb{R})$-bundle from which $E$ is recovered as $E = \mathrm{Fr}(E) \times_{\mathrm{GL}(k)} \mathbb{R}^k$.

**Is an instance: a Lie group $G$ as a principal $G$-bundle over a point.** Take $M = \mathrm{pt}$, $P = G$, with $G$ acting on itself by right multiplication. This is the trivial principal bundle over the point.

**Is an instance: the Hopf bundle $S^1 \to S^3 \to S^2$.** $S^3 \subset \mathbb{C}^2$ carries the free $U(1)$-action $(z_0, z_1) \cdot e^{i\theta} = (z_0 e^{i\theta}, z_1 e^{i\theta})$; the orbit space is $\mathbb{CP}^1 = S^2$. The bundle is nontrivial: there is no global section.

**Is an instance: the universal $H$-bundle $H \to G \to G/H$ from a closed subgroup.** For any closed Lie subgroup $H \leq G$, the right action of $H$ on $G$ by right multiplication is free, and Frankel Theorem 17.11 guarantees the orbit space $G/H$ is a smooth manifold of dimension $\dim G - \dim H$, making $G \to G/H$ a principal $H$-bundle.

**Is an instance: the orthonormal frame bundle $\mathrm{Fr}^{\mathrm{SO}}(M)$ of an oriented Riemannian manifold.** $\mathrm{Fr}^{\mathrm{SO}}(M)_p = \{\text{positively oriented orthonormal bases of } T_pM\}$, with the right $\mathrm{SO}(n)$-action by change of basis. This is the principal $\mathrm{SO}(n)$-bundle obtained from $\mathrm{Fr}(TM)$ by reduction to $\mathrm{SO}(n) \leq \mathrm{GL}(n)$.

**Is NOT an instance: $\mathbb{R} \times \mathbb{R} \to \mathbb{R}$ projecting to the first factor, with $G = \mathbb{R}$ acting on the second factor by addition.** This *is* a principal $\mathbb{R}$-bundle (the trivial one); the example illustrates that the trivial bundle is principal.

**Is NOT an instance: $\mathrm{SO}(3) \to S^2$, $g \mapsto g \cdot N$ (where $N$ is the north pole).** The action of $\mathrm{SO}(3)$ on $S^2$ is transitive but has nontrivial stabilizers ($\mathrm{SO}(2)$ at $N$), so the map is not the projection of a principal $\mathrm{SO}(3)$-bundle. It *is* the projection of a principal $\mathrm{SO}(2)$-bundle: $\mathrm{SO}(2) \to \mathrm{SO}(3) \to S^2$.

**Corollary (the bundle is trivial iff it admits a global section).** Given a global section $s : M \to P$, define $\Phi : M \times G \to P$ by $\Phi(p, g) = s(p) \cdot g$. The free transitive right action makes $\Phi$ a diffeomorphism. Conversely, a global trivialization $\Phi : M \times G \to P$ gives a global section $s(p) = \Phi(p, e)$.

**Corollary (the dimension is $\dim M + \dim G$).** Local triviality $P|_U \cong U \times G$ shows the dimensions add.

**Corollary (an associated bundle has fibre $F$ if $G$ acts on $F$).** $P \times_G F$ is a fibre bundle with typical fibre $F$ and structure group $G$ acting on $F$ as given. This is the universal property of the principal bundle: it generates all bundles with structure group $G$.

**Calibration check.** Verify (i) the Hopf bundle is nontrivial by showing that any global section would give a continuous unit vector field on $S^2$, contradicting the hairy-ball theorem; (ii) the principal bundle $\mathrm{SO}(2) \to \mathrm{SO}(3) \to S^2$ realizes $S^2$ as a coset space; (iii) the trivial principal bundle $M \times G \to M$ admits the canonical global section $p \mapsto (p, e)$.

---

# Unlocked by This

> [!tip] Connection on a Principal Bundle *(from Gauge Theory III)*
> A **connection** on a principal $G$-bundle is a $\mathfrak{g}$-valued 1-form $\omega \in \Omega^1(P; \mathfrak{g})$ on the total space, satisfying equivariance $R_g^* \omega = \mathrm{Ad}(g^{-1})\omega$ and reproducing the Maurer-Cartan form on fibres. Equivalently, a $G$-equivariant choice of horizontal subspace transverse to the orbits. Connections on principal bundles are the geometric language of gauge fields in physics. See [[Gauge Theory III — Connections in Principal and Associated Bundles]].

> [!tip] Curvature and Characteristic Classes *(from Chern–Weil Theory)*
> The curvature of a principal connection is $\Omega = d\omega + \tfrac{1}{2}[\omega, \omega] \in \Omega^2(P; \mathfrak{g})$, and Chern–Weil theory associates to every $G$-invariant polynomial $P$ on $\mathfrak{g}$ a closed differential form $P(\Omega) \in \Omega^{2k}(M)$ whose cohomology class is a characteristic class of the bundle, independent of the connection. The Pfaffian gives the Euler class, the elementary symmetric polynomials give the Chern (or Pontryagin) classes.

> [!tip] Gauge Group and Moduli Space of Connections *(from Yang-Mills Theory)*
> The **gauge group** $\mathcal{G}$ of a principal $G$-bundle $P \to M$ is the group of all $G$-equivariant automorphisms of $P$ covering the identity on $M$ — equivalently, sections of the adjoint bundle $\mathrm{Ad}(P) = P \times_G G$. The quotient of the space of connections $\mathcal{A}(P)$ by the gauge group is the **moduli space of connections** $\mathcal{A}/\mathcal{G}$, and this is the space on which Yang-Mills functionals are defined. The geometry of $\mathcal{A}/\mathcal{G}$ underlies all of modern gauge theory. See [[Gauge Theory IV — Yang–Mills Fields and Instantons]].
