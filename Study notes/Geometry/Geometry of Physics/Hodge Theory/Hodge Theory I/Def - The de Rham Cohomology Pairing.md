---
type: definition
subject: hodge-theory
prereqs:
  - "Def - de Rham Cohomology"
  - "Def - The Wedge Product on a Manifold"
  - "Thm - Stokes' Theorem on Manifolds"
  - "Def - Orientation of a Smooth Manifold"
tags: [geometry, hodge-theory, cohomology, duality]
---

# Notation

$M$ is a closed oriented smooth $n$-manifold (compact, without boundary, with a chosen orientation). $H^k_{dR}(M)$ denotes the [[Def - de Rham Cohomology|k-th de Rham cohomology]] with real coefficients, computed from the de Rham complex $0 \to \Omega^0 \xrightarrow{d} \Omega^1 \xrightarrow{d} \cdots \xrightarrow{d} \Omega^n \to 0$ as $H^k_{dR}(M) = Z^k(M)/B^k(M)$ where $Z^k = \ker d$ and $B^k = \operatorname{im}\,d$. For closed forms $\alpha \in Z^k(M)$ and $\beta \in Z^{n-k}(M)$, the cohomology classes are $[\alpha], [\beta]$. The Betti numbers are $b_k = \dim H^k_{dR}(M)$.

---

# Axiom Motivation

The de Rham cohomology pairing is the natural bilinear form
$$H^k_{dR}(M) \times H^{n-k}_{dR}(M) \to \mathbb{R}, \qquad ([\alpha], [\beta]) \mapsto \int_M \alpha \wedge \beta.$$
Three structural pressures force this definition.

**Why pair $H^k$ with $H^{n-k}$?** Two reasons. First, dimensional matching: $\alpha \wedge \beta$ is a $(k + (n-k)) = n$-form, which can be integrated over the $n$-manifold $M$ to give a real number. Pairing $H^k$ with $H^\ell$ for $\ell \neq n - k$ produces a wedge of degree $k + \ell$, which is either not top-degree (if $k + \ell < n$, hence not integrable) or zero (if $k + \ell > n$, since $\Omega^{k+\ell}(M) = 0$ on an $n$-manifold). Second, abstract: $H^k$ is the $k$-th cohomology of $M$, and $H^{n-k}$ pairs with it in the "Poincaré dual" sense — the pairing is the bilinear form realizing this duality concretely.

**Why is the pairing well-defined on classes?** The integrand $\alpha \wedge \beta$ for $\alpha, \beta$ closed is a closed $n$-form (computation: $d(\alpha\wedge\beta) = d\alpha\wedge\beta + (-1)^k\alpha\wedge d\beta = 0$), and the integral over a closed orientable $n$-manifold of a closed $n$-form depends only on the cohomology class — by Stokes' theorem applied to $\alpha\wedge\beta + d\eta$ for any $\eta$. More carefully: replacing $\alpha$ by $\alpha + d\eta$ for a $(k-1)$-form $\eta$ changes the wedge product by $d\eta\wedge\beta = d(\eta\wedge\beta) - (-1)^{k-1}\eta\wedge d\beta = d(\eta\wedge\beta)$ (since $\beta$ closed). Integrating $d(\eta\wedge\beta)$ over a closed manifold gives zero by Stokes' theorem (no boundary). So the integral depends only on $[\alpha]$. By symmetry it depends only on $[\beta]$. The pairing descends to cohomology.

**Why nondegenerate?** This is the deep content. On a closed orientable $n$-manifold, the pairing $H^k \times H^{n-k} \to \mathbb{R}$ is nondegenerate — for every nonzero class $[\alpha] \in H^k$, there is a class $[\beta] \in H^{n-k}$ with $\int_M\alpha\wedge\beta \neq 0$. This is **Poincaré duality**, and Hodge theory makes it concrete via the Hodge star: the harmonic representative $h$ of $[\alpha]$ is paired nontrivially with $\star h$, since $\int_M h\wedge\star h = \langle h, h\rangle_{L^2} > 0$ if $h \neq 0$. So the harmonic representative is its own dual pairing partner (up to $\star$), and nondegeneracy is built into the metric structure.

**Why orientation?** The pairing $\int_M\alpha\wedge\beta$ requires integration of an $n$-form over $M$, which requires an orientation. On a non-orientable manifold (e.g., $\mathbb{RP}^2$, the Möbius strip, the Klein bottle), $n$-forms cannot be integrated globally without extra structure (they only integrate against [[Def - Pseudoform (Twisted Form)|pseudoforms]] / densities). Poincaré duality in this setting holds with twisted coefficients (twisted by the orientation sheaf), but the simple wedge-product pairing fails. We assume orientation throughout.

**Why closedness of $M$ (no boundary)?** Stokes' theorem on a manifold with boundary gives $\int_M d(\eta\wedge\beta) = \int_{\partial M}\eta\wedge\beta$, generally nonzero. So the integral $\int_M\alpha\wedge\beta$ depends on the choice of representative $\alpha = \alpha_0 + d\eta$ — the pairing is *not* well-defined on cohomology. Replacing the simple cohomology $H^k(M)$ by the **relative cohomology** $H^k(M, \partial M)$ for one side restores duality, giving **Lefschetz duality** $H^k(M) \cong H^{n-k}(M, \partial M)$. Without boundary, the simpler statement $H^k(M) \cong H^{n-k}(M)$ holds.

**What if we strengthen — demand symmetry?** The pairing is *not* symmetric in general: $\int_M\alpha\wedge\beta = (-1)^{k(n-k)}\int_M\beta\wedge\alpha$. So the pairing is symmetric iff $k(n - k)$ is even, anti-symmetric iff odd. On a $4$-manifold and $k = 2$ ($n - k = 2$), the pairing is *symmetric*, defining the **intersection form** on $H^2(M; \mathbb{R})$, a fundamental invariant of $4$-manifolds.

---

# The Definition

Let $M$ be a closed oriented smooth $n$-manifold. The **de Rham cohomology pairing** in degrees $k$ and $n - k$ is the bilinear map
$$\langle\cdot, \cdot\rangle_{H} : H^k_{dR}(M) \times H^{n-k}_{dR}(M) \to \mathbb{R}, \qquad ([\alpha], [\beta]) \mapsto \int_M \alpha \wedge \beta.$$
The pairing is well-defined on cohomology classes (by Stokes' theorem applied to coboundaries), bilinear, and nondegenerate (**Poincaré duality**: for every nonzero $[\alpha] \in H^k$ there is $[\beta] \in H^{n-k}$ with $\langle[\alpha], [\beta]\rangle_H \neq 0$).

**Equivalent form via Hodge theory.** On a closed oriented Riemannian manifold with harmonic representatives $h_\alpha \in [\alpha]$ and $h_\beta \in [\beta]$,
$$\langle[\alpha], [\beta]\rangle_H = \int_M h_\alpha \wedge h_\beta = \int_M h_\alpha \wedge \star\star^{-1} h_\beta = \langle h_\alpha, \star^{-1}h_\beta\rangle_{L^2}.$$
The pairing of $[\alpha]$ with $\star^{-1}h_\beta$ as $L^2$ forms is the metric realization of the topological pairing.

**Self-pairing on middle dimension.** When $n = 2m$ and $k = m$, the pairing is on $H^m(M)$ with itself, giving a bilinear form $H^m(M)\times H^m(M)\to\mathbb{R}$ called the **intersection form**. It is symmetric when $m$ is even (in particular when $n = 4k$), antisymmetric when $m$ is odd. For $n = 4$ and $m = 2$, the intersection form is symmetric and an unimodular integer-valued lattice (when restricted to $H^2(M; \mathbb{Z})$); its signature and parity classify $4$-manifolds up to [[Def - Homeomorphism|homeomorphism]] (Donaldson, Freedman).

---

# Categorical / Structural Definition

The de Rham cohomology pairing is the *perfect pairing* of the **Poincaré duality** isomorphism
$$\mathrm{PD} : H^k_{dR}(M) \xrightarrow{\cong} H^{n-k}_{dR}(M)^*$$
sending $[\alpha]$ to the linear functional $[\beta] \mapsto \int_M\alpha\wedge\beta$. The fact that PD is an isomorphism (rather than merely an injection or surjection) is the nondegeneracy of the pairing — and is the categorical statement of **Poincaré duality** in the de Rham setting.

In sheaf-theoretic / categorical language: the de Rham complex $\Omega^\bullet_M$ on a smooth manifold computes the cohomology with real coefficients, and the cup product (wedge product) on cohomology, paired with the orientation class $[M] \in H^n(M)$, gives the duality pairing. The categorical generalization is **Verdier duality** for constructible sheaves, of which Poincaré duality is the smooth case.

**Hodge theory's role:** Hodge theory provides a *concrete realization* of Poincaré duality via the Hodge star. Specifically, $\star : \mathcal{H}^k \to \mathcal{H}^{n-k}$ is an isomorphism (since $\star$ commutes with $\Delta$), and the composition $\mathcal{H}^k \xrightarrow{\star} \mathcal{H}^{n-k} \to H^{n-k}_{dR}(M)$ (using $\mathcal{H}^{n-k} \cong H^{n-k}_{dR}$) gives an explicit isomorphism in cohomology, with the pairing $\langle[\alpha], [\beta]\rangle = \int\alpha\wedge\beta = \langle h_\alpha, \star^{-1}h_\beta\rangle_{L^2}$.

---

# Relate to Other Fields / Compression

**The pairing is the cap product / intersection pairing in singular homology.** In singular cohomology, $H^k(M; \mathbb{R}) \otimes H^{n-k}(M; \mathbb{R}) \to H^n(M; \mathbb{R}) \cong \mathbb{R}$ is the cup product followed by evaluation on the orientation class $[M]$. The de Rham theorem identifies $H^k_{dR}$ with $H^k(M; \mathbb{R})$ via integration over singular cycles, and under this identification the wedge product becomes the cup product, and the integral over $M$ becomes evaluation on $[M]$. So the de Rham pairing is the smooth incarnation of the topological **cup product pairing** with $[M]$.

**On Riemann surfaces, the pairing is the intersection of $1$-cycles.** For a closed Riemann surface $\Sigma_g$ of genus $g$, $H^1(\Sigma_g; \mathbb{R})$ has dimension $2g$ and is generated by $g$ pairs of $1$-cycles $a_i, b_i$ ($i = 1, \dots, g$) with intersection number $a_i \cdot b_j = \delta_{ij}$, $a_i \cdot a_j = b_i \cdot b_j = 0$. The de Rham pairing $\langle[\alpha], [\beta]\rangle = \int_{\Sigma_g}\alpha\wedge\beta$ on harmonic representatives $\alpha = \omega_{a_i}, \beta = \omega_{b_j}$ (the dual harmonic $1$-forms) recovers $\delta_{ij}$. This is the classical **abelian-differential pairing** of complex-analysis Riemann-surface theory.

**True name:** the de Rham pairing is the *concrete computation* of Poincaré duality, with the integration $\int_M\alpha\wedge\beta$ giving the explicit pairing number. The abstract statement "Poincaré duality is an isomorphism $H^k \cong H^{n-k}$" is *constructed* via this pairing on a smooth manifold.

A second "true name": **the de Rham pairing is the $L^2$ inner product of harmonic representatives (after a Hodge star).** Specifically $\langle[\alpha], [\beta]\rangle = \langle h_\alpha, \star^{-1}h_\beta\rangle_{L^2}$. The Hilbert-space structure on $\mathcal{H}^k$ from the $L^2$ inner product is the natural inner product on cohomology; Poincaré duality is the statement that $\star$ is an isometry between $\mathcal{H}^k$ and $\mathcal{H}^{n-k}$.

---

# Examples / Corollaries

**Is an instance: the volume pairing on a closed orientable $n$-manifold.** $\langle[1], [\operatorname{vol}_g]\rangle_H = \int_M 1 \wedge \operatorname{vol}_g = \mathrm{vol}(M) > 0$. So $[1]$ and $[\operatorname{vol}_g]$ pair nontrivially in $H^0\times H^n$ — verifying nondegeneracy in degree $0$.

**Is an instance: the intersection form on $H^2(K3)$.** The **K3 surface** is a closed simply-connected complex surface (real $4$-manifold) with $H^2 \cong \mathbb{Z}^{22}$, and the intersection form on $H^2 \otimes \mathbb{R}$ is symmetric and unimodular with signature $(3, 19)$. This is one of the two unimodular even forms of signature $(3, 19)$ — it is $-E_8 \oplus -E_8 \oplus 3H$ where $H$ is the hyperbolic plane lattice. The intersection form determines the homeomorphism type of K3 (in fact, every smooth K3 is homeomorphic to every other one, by Freedman's theorem).

**Is an instance: the symplectic pairing on $H^1$ of a Riemann surface.** $\Sigma_g$ has $H^1 \cong \mathbb{R}^{2g}$ with the intersection form being the standard symplectic form $\bigoplus_{i=1}^g \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$. The harmonic $1$-forms with this symplectic pairing form a symplectic vector space, and the moduli space of Riemann surfaces of genus $g$ inherits a natural symplectic structure (the **Goldman symplectic form**) from this pairing.

**Is NOT an instance: pairing on a manifold with boundary using just $H^k \otimes H^{n-k}$.** For $M = [0, 1]$ (a $1$-manifold with two boundary points), $H^0(M) = \mathbb{R}$ (one component) and $H^1(M) = 0$ (any $1$-form is exact). The "pairing" $H^0 \times H^1 \to \mathbb{R}$ is identically zero — not nondegenerate. Poincaré duality fails. To recover duality, use Lefschetz duality $H^0(M, \partial M) = 0$ and $H^1(M) = 0$, both zero, or compare $H^0(M) = \mathbb{R}$ with $H^1(M, \partial M) = \mathbb{R}$ (relative cohomology), which pair nontrivially.

**Is NOT an instance: non-orientable case.** On $\mathbb{RP}^2$, $H^0 = \mathbb{R}$ and $H^2 = 0$ (no global volume form, since $\mathbb{RP}^2$ is non-orientable). So the pairing $H^0 \times H^2 \to \mathbb{R}$ is identically zero, and Poincaré duality fails in real coefficients. The fix is **Poincaré duality with twisted coefficients**: $H^k(M; \mathbb{R}) \cong H^{n-k}(M; \mathcal{O}_M)$ where $\mathcal{O}_M$ is the orientation sheaf. On $\mathbb{RP}^2$ this gives $H^0(M; \mathbb{R}) \cong H^2(M; \mathcal{O}) = \mathbb{R}$, consistent with the twisted pairing.

**Corollary (Poincaré duality [[Def - Dimension|dimensions]]).** The pairing's nondegeneracy implies $\dim H^k_{dR}(M) = \dim H^{n-k}_{dR}(M)$ on a closed orientable $n$-manifold, i.e., $b_k = b_{n-k}$. So the Betti numbers are symmetric: $b_0 = b_n$, $b_1 = b_{n-1}$, etc.

**Corollary (Euler characteristic).** Combining $b_k = b_{n-k}$ with $\chi(M) = \sum_k(-1)^k b_k$, for $n$ odd the Euler characteristic of a closed orientable $n$-manifold is zero: pairs $b_k$ and $b_{n-k}$ contribute with opposite signs. This is why every closed orientable odd-dimensional manifold has $\chi = 0$ — a corollary of Poincaré duality.

**Corollary (signature of $4$-manifolds).** On a closed orientable $4$-manifold, the intersection form on $H^2$ is a symmetric nondegenerate bilinear form on a real vector space. Its **signature** $\sigma(M) = b^+_2 - b^-_2$ (the difference of the positive and negative eigenvalue counts) is a topological invariant. **Hirzebruch's signature theorem** computes $\sigma(M)$ as the integral of the Pontryagin class $p_1 / 3$ — an early instance of an index theorem.

**Calibration check.** If you can verify (i) the pairing is well-defined on cohomology classes via Stokes' theorem, (ii) the pairing is symmetric on even-degree forms in even dimensions and antisymmetric on odd-degree forms in odd dimensions, and (iii) nondegeneracy implies $b_k = b_{n-k}$, you have understood the structure of the pairing correctly.

---

# Unlocked by This

> [!tip] Intersection Theory on $4$-Manifolds *(from Differential Topology)*
> The de Rham pairing on $H^2$ of a closed orientable $4$-manifold gives the **intersection form**, a symmetric unimodular integer-valued bilinear form on $H^2(M; \mathbb{Z})$. **Donaldson's theorem** (1983) states that for a closed simply-connected smooth $4$-manifold with positive-definite intersection form, the form must be diagonalizable over $\mathbb{Z}$ — a sharp restriction not implied by topology alone. **Freedman's classification** (1982) of simply-connected closed topological $4$-manifolds shows the intersection form is a complete invariant up to homeomorphism. The combination — algebraic forms allowed topologically that are *not* realized smoothly — drives the rich theory of **exotic smooth structures on $4$-manifolds**.

> [!tip] Cup Product Structure on Cohomology *(from Algebraic Topology)*
> The wedge product on forms descends to a **cup product** $H^k \otimes H^\ell \to H^{k+\ell}$ on de Rham cohomology, making $H^*_{dR}(M) = \bigoplus_k H^k_{dR}(M)$ into a graded commutative ring (the **cohomology ring**). The de Rham pairing is the cup product into top-degree cohomology followed by integration over $[M]$. The full ring structure is a far richer invariant than the individual Betti numbers — it distinguishes spaces with the same cohomology groups, like $\mathbb{CP}^2$ from $S^2 \times S^2$ (both have $b_0 = b_2 = b_4 = 1$, $b_1 = b_3 = 0$, but their cohomology rings differ: $H^*(\mathbb{CP}^2) = \mathbb{R}[x]/(x^3)$ with a generator $x$ in degree $2$, versus $H^*(S^2 \times S^2) = \mathbb{R}[x, y]/(x^2, y^2)$ with two generators).

> [!tip] Hodge Index Theorem *(from Complex Geometry)*
> On a compact Kähler $n$-manifold, the de Rham pairing decomposes under the Hodge bidegree splitting $H^k(M; \mathbb{C}) = \bigoplus_{p+q=k}H^{p,q}(M)$, with pairings only between $H^{p,q}$ and $H^{n-p, n-q}$ (Serre duality). On a Kähler surface ($n = 2$, so a complex curve), the pairing $H^{1,1} \times H^{1,1} \to \mathbb{C}$ has signature $(1, h^{1,1} - 1)$ — almost negative-definite, with one positive direction (the Kähler class). This **Hodge index theorem** has dramatic consequences in algebraic geometry: the **Hodge-Riemann bilinear relations** constrain which cohomology classes can be Kähler, and underlie the proof of the **Lefschetz hyperplane theorem** and the **Hard Lefschetz theorem**.
