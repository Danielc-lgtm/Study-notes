---
type: definition
subject: spinors
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Riemannian Manifold"
  - "Def - Vector Bundle"
  - "Def - Pin and Spin Groups"
tags: [geometry, spinors, differential-geometry, algebraic-topology]
---

# Notation

$M$ denotes an $n$-dimensional smooth manifold; we assume $M$ is oriented and Riemannian (or pseudo-Riemannian) with metric $g$. The **orthonormal frame bundle** is $P_{SO}(M) \to M$, a principal $SO(n)$-bundle whose fibre at $p$ is the set of positively-oriented orthonormal bases of $T_p M$. The structure group is $SO(n)$ (or $SO(p, q)$ for indefinite signature). For $n \geq 3$, $\mathrm{Spin}(n)$ is the double cover of $SO(n)$ (see [[Def - Pin and Spin Groups]]). The Stiefel–Whitney classes are $w_i(M) \in H^i(M; \mathbb{Z}/2)$, characteristic classes of the tangent bundle; we are concerned with $w_2(M)$. The cohomology group $H^1(M; \mathbb{Z}/2)$ classifies double covers of $M$.

---

# Axiom Motivation

A spin structure is the answer to: **on what kind of manifold can one consistently define spinor fields?** A spinor field is meant to be a section of a vector bundle whose typical fibre is the spinor module $\mathbb{C}^N$ (with $N = 2^{n/2}$ in even dimension, $2^{(n-1)/2}$ in odd), and whose transition functions transform under the spin group $\mathrm{Spin}(n)$ rather than just under $SO(n)$. The question is: when can we *lift* the $SO(n)$-frame bundle to a $\mathrm{Spin}(n)$-bundle, in a way that is consistent across patches?

The desiderata are:

1. We need a principal $\mathrm{Spin}(n)$-bundle $P_{\mathrm{Spin}}(M) \to M$ that **covers** the $SO(n)$-frame bundle, via a $2:1$ map $P_{\mathrm{Spin}} \to P_{SO}$ that restricts to the standard double cover $\mathrm{Spin}(n) \to SO(n)$ on each fibre.

2. The lift must be **consistent** with the principal-bundle structure: the right $\mathrm{Spin}(n)$-action on $P_{\mathrm{Spin}}$ must descend correctly to the right $SO(n)$-action on $P_{SO}$, and the projections must commute.

3. The lift should respect the **patch-by-patch** structure: in a trivialisation $\{U_\alpha\}$ of $P_{SO}$ with transition functions $c_{\alpha\beta}: U_\alpha \cap U_\beta \to SO(n)$, we need to find lifts $\tilde c_{\alpha\beta}: U_\alpha \cap U_\beta \to \mathrm{Spin}(n)$ such that the cocycle condition $\tilde c_{\alpha\beta} \tilde c_{\beta\gamma} = \tilde c_{\alpha\gamma}$ holds on triple overlaps $U_\alpha \cap U_\beta \cap U_\gamma$.

The obstruction is the following: each $c_{\alpha\beta}$ has *two* possible lifts $\pm \tilde c_{\alpha\beta}$ in $\mathrm{Spin}(n)$. We can choose one for each pair $(\alpha, \beta)$, but the cocycle condition $\tilde c_{\alpha\beta}\tilde c_{\beta\gamma}\tilde c_{\gamma\alpha} = I$ on triples might fail by a sign $\pm I$. The resulting **cocycle of signs** is an element of $H^2(M; \mathbb{Z}/2)$ — precisely the second Stiefel–Whitney class $w_2(M)$. The lift exists iff this class vanishes.

Why is $w_2$ the right invariant? It is the class measuring "the failure to lift the $SO(n)$-frame bundle to $\mathrm{Spin}(n)$". More structurally: the **Bockstein** of $w_2$ in the short exact sequence $1 \to \mathbb{Z}/2 \to \mathrm{Spin}(n) \to SO(n) \to 1$ (regarded as a sequence of sheaves) is exactly $w_2$, and the obstruction to lifting is by general principles in obstruction theory the connecting homomorphism in the cohomology long exact sequence.

When the obstruction vanishes, how many lifts are there? The choice of $\tilde c_{\alpha\beta}$ for each pair, modulo gauge changes by $\pm$, gives a torsor over $H^1(M; \mathbb{Z}/2)$. So the *set* of spin structures (when nonempty) has $|H^1(M; \mathbb{Z}/2)|$ elements. Two spin structures differ by an "extra sign" on every loop in $M$, captured by an element of $\mathrm{Hom}(\pi_1(M), \mathbb{Z}/2) = H^1(M; \mathbb{Z}/2)$.

Concretely: $S^n$ ($n \geq 2$) has $H^1(S^n; \mathbb{Z}/2) = 0$, so it has a *unique* spin structure. The circle $S^1$ has $H^1(S^1; \mathbb{Z}/2) = \mathbb{Z}/2$, so it has *two* spin structures (the "periodic" and "antiperiodic" boundary conditions for fermion fields). The torus $T^n$ has $H^1(T^n; \mathbb{Z}/2) = (\mathbb{Z}/2)^n$, so $2^n$ spin structures.

What if we dropped orientability? Then we could ask about a **pin structure** instead, which lifts $O(n)$ to $\mathrm{Pin}(n)$. The pin obstructions are slightly different ($w_2$ or $w_1^2 + w_2$ depending on $\mathrm{Pin}^\pm$), and pin structures exist on some non-orientable manifolds (the Klein bottle admits a $\mathrm{Pin}^-$ structure but not $\mathrm{Pin}^+$).

What if we strengthened the requirement to **$\mathrm{Spin}^c$ structure** — a lift to $\mathrm{Spin}^c(n) = \mathrm{Spin}(n) \times_{\mathbb{Z}/2} U(1)$? The $\mathrm{Spin}^c$ obstruction is the *integral* lift of $w_2$ to $H^2(M; \mathbb{Z})$; this is a weaker condition, and every almost-complex manifold (in particular every $\mathbb{CP}^n$, including those that are not spin) carries a $\mathrm{Spin}^c$ structure. This is why $\mathrm{Spin}^c$ is used in the Seiberg–Witten equations.

---

# The Definition

Let $M$ be an oriented $n$-dimensional Riemannian (or pseudo-Riemannian) manifold with $n \geq 3$, and let $P_{SO}(M) \to M$ be the bundle of oriented orthonormal frames (a principal $SO(n)$-bundle, or $SO^+(p, q)$-bundle in indefinite signature).

A **spin structure** on $M$ is a pair $(P_{\mathrm{Spin}}(M), \xi)$ consisting of:

1. A principal $\mathrm{Spin}(n)$-bundle $P_{\mathrm{Spin}}(M) \to M$ (or principal $\mathrm{Spin}^+(p, q)$-bundle).

2. A bundle map $\xi: P_{\mathrm{Spin}}(M) \to P_{SO}(M)$ over $M$ (i.e., commuting with the projections to $M$) such that the restriction of $\xi$ to each fibre is the standard double cover $\mathrm{Spin}(n) \to SO(n)$, and $\xi$ is equivariant with respect to the right actions:
$$\xi(p \cdot s) = \xi(p) \cdot \pi(s) \quad \text{for all } p \in P_{\mathrm{Spin}}, \; s \in \mathrm{Spin}(n),$$
where $\pi: \mathrm{Spin}(n) \to SO(n)$ is the covering homomorphism.

A manifold admitting a spin structure is called a **spin manifold**.

**Existence criterion.** $M$ admits a spin structure iff the second Stiefel–Whitney class $w_2(M) \in H^2(M; \mathbb{Z}/2)$ vanishes.

**Classification of spin structures.** When $w_2(M) = 0$, the set of inequivalent spin structures on $M$ is a torsor (free transitive action) over $H^1(M; \mathbb{Z}/2)$. So:
- If $H^1(M; \mathbb{Z}/2) = 0$, there is a unique spin structure (when one exists).
- If $H^1(M; \mathbb{Z}/2) \neq 0$, there are $|H^1(M; \mathbb{Z}/2)|$ inequivalent spin structures.

**The associated spinor bundle.** Given a spin structure $(P_{\mathrm{Spin}}, \xi)$ and the spinor module $\mathbb{C}^N$ (with $N = 2^{n/2}$ in even dimension, $N = 2^{(n-1)/2}$ in odd dimension) on which $\mathrm{Spin}(n)$ acts via the spinor representation $\rho_{\mathrm{spin}}$, the **spinor bundle** is the associated vector bundle
$$SM := P_{\mathrm{Spin}}(M) \times_{\rho_{\mathrm{spin}}} \mathbb{C}^N \to M.$$
A **spinor field** is a smooth section of $SM$.

---

# Categorical / Structural Definition

The condition $w_2(M) = 0$ can be reformulated via the **Wu formula** and various other characterisations. The most useful structural perspectives:

1. **As a lifting of a classifying map.** A vector bundle $E \to M$ of rank $n$ corresponds to a classifying map $M \to BSO(n)$ (the classifying space of $SO(n)$). The double cover $\mathrm{Spin}(n) \to SO(n)$ induces a fibration $B\mathrm{Spin}(n) \to BSO(n)$ with fibre $K(\mathbb{Z}/2, 1) = \mathbb{RP}^\infty$. A spin structure on $E$ is exactly a lift $M \to B\mathrm{Spin}(n)$ of the classifying map; the obstruction to lifting (a section of the fibration over $M$) is the class $w_2 \in H^2(M; \mathbb{Z}/2)$ pulled back from $BSO(n)$.

2. **As a square root of the determinant bundle.** In low dimensions (and with $\mathrm{Spin}^c$ in any dimension), a spin structure on a complex manifold can be understood as a square root $K_M^{1/2}$ of the canonical line bundle $K_M = \det(T^*M_{\mathbb{C}})$. The choice of square root, which exists when $c_1(K_M)$ is divisible by $2$ in $H^2(M; \mathbb{Z})$, is exactly a spin structure modulo torsion.

3. **As a parity assignment to loops.** Given any loop $\gamma$ in $M$, parallel-transport an orthonormal frame around $\gamma$ to obtain a rotation $R_\gamma \in SO(n)$; this lifts to $\pm \tilde R_\gamma \in \mathrm{Spin}(n)$. A spin structure assigns one of the two lifts to each loop, consistently: $\tilde R_{\gamma_1 \cdot \gamma_2} = \tilde R_{\gamma_1} \tilde R_{\gamma_2}$. This gives a homomorphism $\pi_1(M) \to \mathbb{Z}/2$ describing how the spin lift behaves on closed loops, and different spin structures correspond to different such homomorphisms.

Categorically, **$\mathrm{Spin}$-structures on $M$ form a torsor over $H^1(M; \mathbb{Z}/2)$**; the set of spin structures has either $0$ elements (when $w_2 \neq 0$) or $|H^1(M; \mathbb{Z}/2)|$ elements.

---

# Relate to Other Fields / Compression

**True name:** A spin structure is a **principal $\mathrm{Spin}(n)$-bundle covering the orthonormal frame bundle**, or equivalently **a parity assignment to oriented orthonormal frames that respects continuous deformation**. The existence/uniqueness statements are entirely topological and computable from the cohomology of $M$.

In the language of obstruction theory, a spin structure is the *first non-trivial* obstruction in the tower
$$O(n) \supset SO(n) \supset \mathrm{Spin}(n) \supset \mathrm{String}(n) \supset \mathrm{Fivebrane}(n) \supset \ldots$$
of higher coverings, with obstructions $w_1, w_2$, half-Pontryagin class $\tfrac{1}{2}p_1$, etc. These correspond to *orientability*, *spinability*, *string-ability*, *fivebrane-ability*, and so on — each requiring the vanishing of a particular characteristic class. Spin structures are the most commonly encountered in physics; string structures appear in heterotic string theory.

Connections:

- **$\mathrm{Spin}^c$ structures and Seiberg–Witten theory:** $\mathrm{Spin}^c(n) = \mathrm{Spin}(n) \times_{\mathbb{Z}/2} U(1)$ admits a lift whenever $w_2$ has an integral lift, which always holds for almost-complex manifolds. The Seiberg–Witten equations live on $\mathrm{Spin}^c$ 4-manifolds; they revolutionized low-dimensional topology in the mid-1990s.
- **Pin structures and non-orientable manifolds:** for non-orientable $M$, one can ask about $\mathrm{Pin}^\pm$-structures (lifts of $O(n)$). The Klein bottle has $\mathrm{Pin}^-$ but no $\mathrm{Pin}^+$ structure.
- **Spin in physics:** the existence of a spin structure is the precondition for defining a Dirac operator on a curved spacetime. If $M$ is not spin, no Dirac equation can be written on $M$.

---

# Examples / Corollaries

**Example 1: Spheres $S^n$ (all $n \geq 2$).** Use the bundle isomorphism $TS^n \oplus \mathbb{R} \cong S^n \times \mathbb{R}^{n+1}$ (the tangent bundle stabilizes to a trivial bundle). All Stiefel–Whitney classes of a trivial bundle vanish, so $w_2(TS^n) = w_2(TS^n \oplus \mathbb{R}) = 0$ (Stiefel–Whitney is stable under adding trivial summands). So $S^n$ admits a spin structure. Moreover, $H^1(S^n; \mathbb{Z}/2) = 0$ for $n \geq 2$, so the spin structure is unique. (For $n = 1$, $H^1(S^1; \mathbb{Z}/2) = \mathbb{Z}/2$ so $S^1$ has two spin structures.) See [[Ex - Spin Structure on the Sphere S^n]].

**Example 2: Orientable surfaces.** Every closed orientable surface $\Sigma_g$ of genus $g$ has $w_2(\Sigma_g) = 0$ (this follows from the Wu formula in dimension $2$, or direct calculation). The number of spin structures is $|H^1(\Sigma_g; \mathbb{Z}/2)| = 2^{2g}$. Two of these are special (called *even* and *odd* spin structures based on the parity of the dimension of harmonic spinors), but all $2^{2g}$ are inequivalent.

**Example 3: Torus $T^n$.** $T^n = \mathbb{R}^n/\mathbb{Z}^n$ has trivial tangent bundle (since $\mathbb{R}^n$ does), so all Stiefel–Whitney classes vanish: spin structures exist. $H^1(T^n; \mathbb{Z}/2) = (\mathbb{Z}/2)^n$, so there are $2^n$ spin structures. Physically, these correspond to the $2^n$ choices of *periodic* vs *antiperiodic* boundary conditions for fermion fields along each of the $n$ independent loops.

**Example 4: $\mathbb{CP}^n$.** Use the relation $w_2(\mathbb{CP}^n) \equiv c_1(\mathbb{CP}^n) \pmod 2 = (n + 1)a \pmod 2$ where $a \in H^2(\mathbb{CP}^n; \mathbb{Z})$ is the hyperplane class. So $w_2(\mathbb{CP}^n) = 0$ iff $n$ is odd. Conclusion: $\mathbb{CP}^1 = S^2$, $\mathbb{CP}^3$, $\mathbb{CP}^5$, ... are spin; $\mathbb{CP}^2$, $\mathbb{CP}^4$, ... are *not* spin (but are $\mathrm{Spin}^c$).

**Non-example: $\mathbb{CP}^2$.** As above, $w_2(\mathbb{CP}^2) \neq 0$, so no spin structure exists. However, $\mathbb{CP}^2$ does have a $\mathrm{Spin}^c$ structure (in fact a canonical one, since it is Kähler).

**Non-example: $\mathbb{HP}^n$ (the quaternionic projective space).** For $n \geq 1$, $\mathbb{HP}^n$ is simply-connected with $w_2 = 0$ (it has a quaternionic structure, which is stronger than spin). So all quaternionic projective spaces are spin.

**Non-example: Wu manifold $SU(3)/SO(3)$.** This is a 5-manifold with $w_2 \neq 0$, so it is *not* spin. It is one of the simplest non-spin examples in higher dimensions; the non-vanishing $w_2$ is detected via Steenrod squares.

**Calibration check.** A reader should verify: (i) compute $w_2$ for the trivial bundle (all $w_i$ vanish, so $w_2 = 0$); (ii) using $w(M \times N) = w(M) \cdot w(N)$, deduce the spin condition on products; (iii) on a closed orientable 3-manifold, $w_2 = 0$ automatically (a deeper fact, but worth knowing: all closed orientable 3-manifolds are spin and *parallelizable*).

---

# Unlocked by This

> [!tip] Dirac Operator on Spin Manifolds
> Once a spin structure is fixed, one can form the [[Def - Spin Connection and the Dirac Operator|spin connection]] $\nabla^S$ on the spinor bundle and the **Dirac operator** $\not D = \gamma^a e_a^\mu \nabla^S_\mu: \Gamma(SM) \to \Gamma(SM)$. This is a first-order linear elliptic operator (in Riemannian signature), the natural curved-spacetime analog of $\not\partial$ on flat space. Its index $\mathrm{ind}\,\not D^+$ is a topological invariant computed by the [[Thm - Lichnerowicz Formula|Lichnerowicz formula]] and the Atiyah–Singer index theorem; it is the central character of spin geometry.

> [!tip] Atiyah-Singer Index Theorem (Spin Version)
> For a closed oriented spin manifold $M^{2k}$, the Dirac operator splits by chirality as $\not D = \not D^+ + \not D^-$ with $\not D^\pm: \Gamma(S^\pm) \to \Gamma(S^\mp)$. The **index** is
> $$\mathrm{ind}\,\not D^+ = \dim\ker\not D^+ - \dim\mathrm{coker}\,\not D^+ = \int_M \hat A(M)$$
> where $\hat A(M)$ is the **$\hat A$-genus**, a characteristic class polynomial in the Pontryagin classes. This is the foundational example of the Atiyah–Singer index theorem; it computes a *topological* invariant (the analytical index) as the integral of *characteristic-class data*. The integrality of the $\hat A$-genus on spin manifolds — which is *not* obvious from the formula — is one of its surprising consequences.

> [!tip] Rokhlin's Theorem
> For a closed 4-dimensional spin manifold $M$, the **signature** $\mathrm{sgn}(M)$ is divisible by $16$. This is **Rokhlin's theorem** (1952), proven before the index theorem; it says that the obvious integrality bound $\mathrm{sgn}(M) \equiv 0 \pmod 8$ (which holds for all closed oriented 4-manifolds) is strengthened to $\equiv 0 \pmod{16}$ when $M$ is spin. The proof now follows from $\mathrm{ind}\,\not D^+ = \hat A(M)$ being an integer plus the relation $\mathrm{sgn}(M) = \tfrac{1}{16}\int p_1$ (Hirzebruch) restricted to spin manifolds. Rokhlin's theorem is a deep constraint on $4$-dimensional topology and is the source of the "Rokhlin invariant" of $3$-manifolds.

> [!tip] Spin Cobordism Theory
> Two closed spin $n$-manifolds $M_1, M_2$ are **spin cobordant** if there exists a compact spin $(n+1)$-manifold $W$ with $\partial W = M_1 \sqcup (-M_2)$ (where $-M_2$ is $M_2$ with reversed orientation). The set of equivalence classes forms the **spin cobordism group** $\Omega_n^{\mathrm{Spin}}$, with addition given by disjoint union. The first few groups: $\Omega_0^{\mathrm{Spin}} = \mathbb{Z}$, $\Omega_1^{\mathrm{Spin}} = \mathbb{Z}/2$ (from $S^1$ with antiperiodic spin structure), $\Omega_2^{\mathrm{Spin}} = \mathbb{Z}/2$, $\Omega_3^{\mathrm{Spin}} = 0$, $\Omega_4^{\mathrm{Spin}} = \mathbb{Z}$ (detected by signature / 16, the Rokhlin invariant). The full computation by Anderson–Brown–Peterson uses techniques of stable homotopy theory; the $\hat A$-genus and other characteristic numbers provide explicit invariants.
