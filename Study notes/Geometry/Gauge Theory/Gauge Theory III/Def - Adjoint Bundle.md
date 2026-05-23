---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Adjoint Representation"
  - "Def - Connection 1-Form on a Principal Bundle"
  - "Def - Vector Bundle"
  - "Def - The Lie Algebra of a Lie Group"
tags: [geometry, gauge-theory, principal-bundles, associated-bundles]
---

# Notation

$P \to M$ is a principal $G$-bundle with structure group $G$ acting on itself by the adjoint action $\mathrm{Ad}_g : G \to G$, $h \mapsto ghg^{-1}$, and on its Lie algebra $\mathfrak{g}$ by the [[Def - Adjoint Representation|adjoint representation]] $\mathrm{Ad} : G \to \mathrm{GL}(\mathfrak{g})$, $\mathrm{Ad}_g(\xi) = g\xi g^{-1}$ (matrix-group case). The adjoint bundle is $\mathrm{Ad}\,P = P \times_{\mathrm{Ad}} \mathfrak{g}$; the associated $r$-form sections are $\Omega^r(M; \mathrm{Ad}\,P)$.

---

# Axiom Motivation

The fundamental geometric problem this definition solves: the curvature 2-form $\Omega$ of a connection on $P$ is a $\mathfrak{g}$-valued 2-form on the total space, and we want it to descend to a globally defined object on the base $M$. As we saw in [[Def - Curvature 2-Form on a Principal Bundle]], $\Omega$ is horizontal and equivariant, but it does *not* descend to a $\mathfrak{g}$-valued 2-form on $M$ — the equivariance under the adjoint action conflicts with global descent unless we account for it.

The adjoint bundle is the right home for the descent. It is the vector bundle over $M$ with fibre $\mathfrak{g}$ that "twists" by the adjoint action of the structure group $G$: locally on a trivialising patch $U_\alpha$, sections look like $\mathfrak{g}$-valued functions $\psi_\alpha : U_\alpha \to \mathfrak{g}$, but on overlaps $U_\alpha \cap U_\beta$ the transition rule is
$$
\psi_\beta = \mathrm{Ad}_{g_{\alpha\beta}^{-1}}\psi_\alpha = g_{\alpha\beta}^{-1}\psi_\alpha g_{\alpha\beta},
$$
where $g_{\alpha\beta} : U_\alpha \cap U_\beta \to G$ are the transition functions of $P$ and $\mathrm{Ad}_{g^{-1}}$ is conjugation by $g^{-1}$.

The curvature $F = s_\alpha^*\Omega$ in the local trivialisation given by $s_\alpha$ transforms under change of section exactly by this rule: $F_\beta = g_{\alpha\beta}^{-1}F_\alpha g_{\alpha\beta}$, no inhomogeneous term (in contrast to the gauge potential $A$). So $\{F_\alpha\}_\alpha$ is a coherent system of local $\mathfrak{g}$-valued 2-forms transforming as sections of $\mathrm{Ad}\,P$, and they assemble into a single global section $F \in \Omega^2(M; \mathrm{Ad}\,P)$.

This is the geometric content of the slogan "the field strength of a non-abelian gauge field lives in the adjoint bundle". For abelian $G$, the adjoint action is trivial ($\mathrm{Ad}_g\xi = g\xi g^{-1} = \xi$), so $\mathrm{Ad}\,P = M \times \mathfrak{g}$ is the trivial bundle, and the field strength is a globally defined ordinary $\mathfrak{g}$-valued 2-form on $M$. For non-abelian $G$, the adjoint action is non-trivial, $\mathrm{Ad}\,P$ is generically non-trivial, and the field strength is a section of a *non-trivial* bundle. This is one of the genuinely different features of non-abelian gauge theory.

Why the adjoint representation specifically? Three reasons.

**(i) It is the natural action of $G$ on $\mathfrak{g}$.** When $G$ acts on itself by conjugation (which is the action of a structure group on a "copy of itself" inside a principal bundle), its differential at the identity is precisely $\mathrm{Ad}$. So the adjoint representation is the *infinitesimal* version of the structure-group action on the bundle fibres.

**(ii) It is the representation in which the curvature transforms.** Under the gauge transformation $A \mapsto g^{-1}Ag + g^{-1}dg$, the curvature $F = dA + \tfrac{1}{2}[A, A]$ picks up no inhomogeneous term and transforms simply as $F \mapsto g^{-1}Fg$ — the adjoint action. So the curvature *naturally* takes values in the adjoint representation.

**(iii) It is the representation in which infinitesimal gauge transformations live.** An infinitesimal gauge transformation is parametrised by a $\mathfrak{g}$-valued function on $M$ — locally. Globally, it is a section of $\mathrm{Ad}\,P$. So the adjoint bundle is the **gauge algebra bundle**: sections of $\mathrm{Ad}\,P$ generate gauge transformations.

What if we used a different representation? We could form $P \times_\rho V$ for any representation $\rho$, and the curvature would not in general live there. Different representations are needed for different physical objects: the *defining* representation gives the **fundamental matter** bundle (e.g., quark colour-triplet bundle for $SU(3)$); the *trivial* representation gives the **trivial line bundle** $M \times \mathbb{R}$ (Higgs in some models); the *adjoint* representation is the gauge-field bundle. Each has its own associated bundle and its own role.

The adjoint bundle is also the natural home for **gauge transformations themselves**. A finite gauge transformation is a section of the *gauge group bundle* $\mathrm{Adj}\,P := P \times_{\mathrm{Adj}} G$ (where $G$ acts on itself by conjugation $\mathrm{Adj}_g(h) = ghg^{-1}$); its infinitesimal version is a section of the adjoint bundle $\mathrm{Ad}\,P$. The gauge group bundle is the *group* version, the adjoint bundle is the *Lie algebra* version, and the two are related by the exponential map fibrewise.

---

# The Definition

Let $P \to M$ be a principal $G$-bundle. The **adjoint bundle** of $P$ is the associated vector bundle
$$
\mathrm{Ad}\,P := P \times_{\mathrm{Ad}} \mathfrak{g} := (P \times \mathfrak{g}) / G,
$$
where $G$ acts on $P \times \mathfrak{g}$ from the right by $(p, \xi) \cdot g = (p \cdot g, \mathrm{Ad}_{g^{-1}}\xi) = (p \cdot g, g^{-1}\xi g)$ (in matrix-group notation). The fibre of $\mathrm{Ad}\,P$ over $x \in M$ is canonically isomorphic to $\mathfrak{g}$ once a representative $p \in \pi^{-1}(x)$ is chosen; the isomorphism changes by the adjoint action under change of representative.

In a local trivialisation by a section $s_\alpha : U_\alpha \to P$, a section $\psi \in \Gamma(\mathrm{Ad}\,P)$ is locally a $\mathfrak{g}$-valued function $\psi_\alpha : U_\alpha \to \mathfrak{g}$, with the cocycle rule on overlaps
$$
\psi_\beta(x) = \mathrm{Ad}_{g_{\alpha\beta}^{-1}(x)}\,\psi_\alpha(x) = g_{\alpha\beta}^{-1}(x)\,\psi_\alpha(x)\,g_{\alpha\beta}(x),
$$
where $g_{\alpha\beta} : U_\alpha \cap U_\beta \to G$ are the transition functions of $P$.

**$r$-form sections.** The space of $r$-form sections of $\mathrm{Ad}\,P$ is
$$
\Omega^r(M; \mathrm{Ad}\,P) := \Gamma(\Lambda^r T^*M \otimes \mathrm{Ad}\,P),
$$
locally $\mathfrak{g}$-valued $r$-forms on $U_\alpha$ with the same cocycle rule on overlaps: $\psi_\beta = g_{\alpha\beta}^{-1}\psi_\alpha g_{\alpha\beta}$.

**Connection induced from a principal connection.** A connection $\omega$ on $P$ induces (by [[Thm - Principal Connection Induces a Connection on Every Associated Bundle]]) a covariant derivative on sections of $\mathrm{Ad}\,P$:
$$
\nabla^{\mathrm{Ad}}\psi = d\psi + [A, \psi] \quad \text{in a local trivialisation},
$$
where $A$ is the local gauge potential. The extension to $r$-form sections is the [[Def - Exterior Covariant Derivative on Associated Bundles|exterior covariant derivative]] $d_\nabla$.

**Curvature as a section.** The curvature $F = dA + \tfrac{1}{2}[A, A]$ in any local trivialisation is a section of $\Omega^2(U_\alpha; \mathfrak{g})$, and the cocycle rule gives $F_\beta = g_{\alpha\beta}^{-1}F_\alpha g_{\alpha\beta}$ — so the local field strengths assemble into a global section
$$
F \in \Omega^2(M; \mathrm{Ad}\,P).
$$
This is the **field strength of the connection** as a global geometric object on $M$.

---

# Categorical / Structural Definition

In the language of associated bundles, the adjoint bundle is the result of the **associated-bundle functor** applied to the adjoint representation. Specifically, the functor 
$$
\rho \mapsto P \times_\rho V
$$
from the category of representations of $G$ on vector spaces $V$ to the category of vector bundles over $M$ sends the adjoint representation $\mathrm{Ad} : G \to \mathrm{GL}(\mathfrak{g})$ to $\mathrm{Ad}\,P$. This functor preserves direct sums, tensor products, and duals (with the corresponding bundle operations), making the adjoint bundle the "natural" vector-bundle home of $\mathfrak{g}$ over $M$.

Equivalently, the adjoint bundle is the **vertical tangent bundle** of $P$ modulo the $G$-action: $\mathrm{Ad}\,P = VP/G$ where $VP = \ker(d\pi)$ is the vertical bundle of $P$ and $G$ acts by right-translation. The vertical-space isomorphism $\mathfrak{g} \to V_p P$ at each point gives the identification of fibres with $\mathfrak{g}$, and the quotient by $G$ folds the right action into the adjoint action on $\mathfrak{g}$.

A third equivalent description: $\mathrm{Ad}\,P$ is the bundle of **fibrewise Lie algebras** of the bundle of groups $P \times_{\mathrm{Adj}} G$ (the gauge group bundle), in the same way that $\mathfrak{g}$ is the Lie algebra of $G$. The fibrewise Lie bracket on sections of $\mathrm{Ad}\,P$ is defined pointwise from the Lie bracket on $\mathfrak{g}$.

---

# Relate to Other Fields / Compression

In **gauge theory**, the adjoint bundle is the home of every $\mathfrak{g}$-valued gauge-theoretic object on $M$: the field strength $F$, infinitesimal gauge transformations $\lambda$ (so that the gauge group is locally $\exp(\lambda)$ for $\lambda \in \Gamma(\mathrm{Ad}\,P)$), gauge-fixing functionals (BRST ghosts), etc. The Yang-Mills Lagrangian density, which involves $\mathrm{tr}(F \wedge \star F)$ and similar invariants, is built from sections of $\mathrm{Ad}\,P$ via the invariant bilinear form $\mathrm{tr}$ on $\mathfrak{g}$ (assuming the bilinear form is $\mathrm{Ad}$-invariant, which holds for the Killing form on a semisimple Lie algebra).

In **Lie theory**, the adjoint bundle is the **family of Lie algebras** parametrised by $M$: at each $x \in M$, the fibre $(\mathrm{Ad}\,P)_x$ is canonically isomorphic to $\mathfrak{g}$ once a frame in $P$ over $x$ is chosen, with frame change inducing an inner automorphism of $\mathfrak{g}$. For abelian $G$, all inner automorphisms are trivial, so all the fibre isomorphisms agree and $\mathrm{Ad}\,P$ is trivial.

In **Yang-Mills theory and instanton physics**, the *topology* of $\mathrm{Ad}\,P$ determines the topological invariants of the bundle. For $SU(2)$-bundles over $S^4$, the **second Chern class** $c_2 \in H^4(S^4; \mathbb{Z}) = \mathbb{Z}$ classifies the bundle (and equals the instanton number); $c_2$ is computable as $\int_{S^4} \mathrm{tr}(F \wedge F)/8\pi^2$, a Chern-Weil integral of a section of $\Lambda^4 T^*M \otimes \mathrm{End}(\mathrm{Ad}\,P)$.

**True name:** the adjoint bundle is *the canonical vector bundle on $M$ whose fibre is the Lie algebra of the gauge group and whose transition functions are the adjoint actions of the principal-bundle transition functions*. Operationally: sections are "$\mathfrak{g}$-valued objects on $M$ that transform in the adjoint representation under gauge transformations" — like the field strength $F$, like infinitesimal gauge parameters $\lambda$, like the differences of gauge potentials $A_1 - A_2$.

---

# Examples / Corollaries

**Example (abelian: $G = U(1)$).** $\mathfrak{u}(1) = i\mathbb{R}$. The adjoint action is $\mathrm{Ad}_g(i\theta) = g \cdot i\theta \cdot g^{-1} = i\theta$ for all $g \in U(1)$ (since $U(1)$ is abelian). So the adjoint representation is trivial, and $\mathrm{Ad}\,P = M \times i\mathbb{R}$ for any $U(1)$-bundle $P$ — the trivial line bundle. Consequence: the electromagnetic field strength $F$ is a globally defined ordinary 2-form on $M$ (or $i\mathbb{R}$-valued, depending on convention). The triviality of $\mathrm{Ad}\,P$ in the abelian case is what makes electromagnetism "look much more like geometry" than non-abelian gauge theory. See [[Ex - Adjoint Bundle of a U(1)-Bundle is Trivial]] for the verification.

**Example ($SU(2)$-bundle).** $\mathfrak{su}(2) = \{i\sigma_a/2 : a = 1, 2, 3\} \cong \mathbb{R}^3$ as a real vector space, with adjoint action $\mathrm{Ad}_g\xi = g\xi g^{-1}$ for $g \in SU(2)$, $\xi \in \mathfrak{su}(2)$. The adjoint representation $\mathrm{Ad} : SU(2) \to \mathrm{GL}(\mathfrak{su}(2)) = \mathrm{GL}(3)$ has image the rotation group $SO(3)$ — that is, $\mathrm{Ad}$ for $SU(2)$ is the **double cover map** $SU(2) \to SO(3)$ followed by the standard inclusion. So for an $SU(2)$-bundle $P$, the adjoint bundle $\mathrm{Ad}\,P$ is a rank-3 real vector bundle that is "$\mathbb{R}^3$ rotated by the structure group". For non-trivial $SU(2)$-bundles (e.g., the BPST instanton bundle on $S^4$), $\mathrm{Ad}\,P$ is a non-trivial rank-3 bundle.

**Example (orthonormal frame bundle).** For $(M, g)$ Riemannian, $P = F^O(M)$ the orthonormal frame bundle (a principal $O(n)$-bundle), $\mathfrak{o}(n)$ the antisymmetric matrices. The adjoint bundle $\mathrm{Ad}\,F^O(M)$ has fibre $\mathfrak{o}(n) \cong \Lambda^2 \mathbb{R}^n$ — the space of antisymmetric $n \times n$ matrices, which is canonically isomorphic to 2-forms on $\mathbb{R}^n$. The Riemann curvature tensor, viewed as a 2-form valued in $\mathfrak{o}(n)$, is a section of $\Lambda^2 T^*M \otimes \mathrm{Ad}\,F^O(M)$ — exactly Frankel's "curvature 2-form" $\Omega^a{}_b$ in this framework.

**Is NOT an instance:** the tangent bundle $TM$ is not an adjoint bundle in general — it is the associated bundle for the *defining* representation of $\mathrm{GL}(n)$ on $\mathbb{R}^n$, not the adjoint representation on $\mathfrak{gl}(n)$. The adjoint bundle of the linear frame bundle is the *endomorphism bundle* $\mathrm{End}(TM)$, which has rank $n^2$, not $n$.

**Is NOT an instance:** the spinor bundle is not an adjoint bundle — it is the associated bundle for the *spinor representation* of $\mathrm{Spin}(n)$ on the spinor space $S$, not the adjoint representation. Spinor bundles, gauge-field bundles, and tangent bundles are *different* associated bundles of (possibly different) principal bundles.

**Corollary (functoriality).** A principal bundle homomorphism $f : P \to Q$ (with structure groups $G \to H$) induces a vector bundle homomorphism $\mathrm{Ad}\,P \to \mathrm{Ad}\,Q$ in a functorial way. So the adjoint bundle is a *natural* construction on principal bundles.

**Corollary (Lie bracket on sections).** The Lie bracket on $\mathfrak{g}$ extends fibrewise to a $C^\infty(M)$-bilinear bracket on $\Gamma(\mathrm{Ad}\,P)$, making it a *Lie algebra* (over $C^\infty(M)$). This is the **gauge Lie algebra** of $P$: its elements are infinitesimal gauge transformations, and the bracket is the infinitesimal commutator of gauge transformations.

**Corollary (Killing form).** For a Lie algebra $\mathfrak{g}$ with a non-degenerate $\mathrm{Ad}$-invariant symmetric bilinear form $\kappa$ (e.g., the Killing form on a semisimple $\mathfrak{g}$, or the trace form $-\mathrm{tr}(XY)$ on $\mathfrak{su}(n)$), $\kappa$ extends to a fibrewise bilinear form on $\mathrm{Ad}\,P$. This is what makes the Yang-Mills Lagrangian $-\tfrac{1}{4}\int \kappa(F, \star F)$ a *gauge-invariant* expression — $\kappa(F, \star F)$ is invariant under the adjoint action because $\kappa$ is $\mathrm{Ad}$-invariant.

**Calibration check.** If you have understood the definition, you should be able to: (i) write down the transition rule for sections of $\mathrm{Ad}\,P$ explicitly: $\psi_\beta = g_{\alpha\beta}^{-1}\psi_\alpha g_{\alpha\beta}$, and verify it satisfies the cocycle condition on triple overlaps; (ii) explain why for abelian $G$, the adjoint action is trivial and $\mathrm{Ad}\,P$ is the trivial bundle, by direct computation $g\xi g^{-1} = \xi$ in an abelian group; (iii) verify that the field strength $F = dA + \tfrac{1}{2}[A, A]$ transforms as a section of $\mathrm{Ad}\,P$ — that is, under a gauge transformation $A_\beta = g^{-1}A_\alpha g + g^{-1}dg$, the new field strength is $F_\beta = g^{-1}F_\alpha g$ (no inhomogeneous term).

---

# Unlocked by This

> [!tip] Curvature as a Section of $\mathrm{Ad}\,P$ *(from Gauge Theory III)*
> The field strength $F$ of a principal connection is a 2-form section of the adjoint bundle: $F \in \Omega^2(M; \mathrm{Ad}\,P)$. This is the *global* avatar of the local gauge-dependent field strengths, and it is the object on which the Yang-Mills action and Bianchi identity are formulated. See [[Def - Curvature 2-Form on a Principal Bundle]].

> [!tip] Chern-Weil Theory *(from Algebraic Topology)*
> An $\mathrm{Ad}$-invariant polynomial $p$ on $\mathfrak{g}$ pulls back the curvature $F \in \Omega^2(M; \mathrm{Ad}\,P)$ to an ordinary $p(F) \in \Omega^{2\deg p}(M; \mathbb{R})$. The closed form $p(F)$ represents a de Rham cohomology class independent of $\omega$ — a **characteristic class** of the bundle. Examples: Chern classes ($p = \mathrm{tr}(F^k)$ for $U(n)$), Pontryagin classes ($p = \mathrm{tr}(F^{2k})$ for $O(n)$), Euler class (Pfaffian for $SO(2k)$). This is the bridge from differential geometry to algebraic topology of principal bundles.

> [!tip] Gauge Group Bundle and Gauge Transformations *(from Gauge Theory)*
> The **gauge group bundle** $P \times_{\mathrm{Adj}} G$ is the associated bundle for the conjugation action of $G$ on itself. Its sections are *finite* gauge transformations; the infinitesimal version is the adjoint bundle. The gauge group $\mathcal{G}(P) := \Gamma(P \times_{\mathrm{Adj}} G)$ acts on the affine space $\mathcal{A}(P)$ of connections by $\omega \mapsto g^{-1}\omega g + g^{-1}dg$ (the gauge transformation law on the total space), with infinitesimal action $\delta\omega = -d_\omega \lambda$ for $\lambda \in \Gamma(\mathrm{Ad}\,P)$. The quotient $\mathcal{A}/\mathcal{G}$ is the moduli space of connections modulo gauge.

> [!tip] Instanton Moduli Space *(from Gauge Theory and Geometric Topology)*
> The moduli space of **self-dual connections** $F = \star F$ on a principal $SU(2)$-bundle over a 4-manifold is a finite-dimensional space whose geometry is the source of **Donaldson invariants** of 4-manifolds. The tangent space at a connection $\omega$ is the kernel of a linear operator on $\Omega^1(M; \mathrm{Ad}\,P)$, and the moduli space itself is a (singular) finite-dimensional manifold built from sections of bundles associated to $\mathrm{Ad}\,P$. This is the entry point to **Donaldson theory** of 4-manifolds and to **Seiberg-Witten theory**.
