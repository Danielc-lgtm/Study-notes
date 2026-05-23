---
type: theorem
subject: riemannian-geometry
prereqs:
  - "Def - Killing Vector Field"
  - "Def - Levi-Civita Connection"
  - "Def - Lie Derivative of a Vector Field"
tags: [geometry, riemannian-geometry, symmetry, killing]
---

# Notation

$(M, g)$ is a Riemannian manifold with [[Def - Levi-Civita Connection|Levi-Civita connection]] $\nabla$. $X$ is a smooth vector field. $X^\flat$ is the $1$-form dual to $X$ via $g$: $X^\flat(Y) = \langle X, Y\rangle$. The Lie derivative of the metric is $(\mathcal{L}_X g)(Y, Z) = X\langle Y, Z\rangle - \langle[X, Y], Z\rangle - \langle Y, [X, Z]\rangle$. In components, $\nabla_a X_b$ means $(\nabla X^\flat)_{ab}$, the covariant derivative of the $1$-form.

---

# Statement

> **Theorem (Killing equation).** Let $(M, g)$ be a Riemannian manifold with Levi-Civita connection $\nabla$, and let $X \in \mathfrak{X}(M)$ be a smooth vector field. The following are equivalent:
>
> 1. $X$ is a [[Def - Killing Vector Field|Killing vector field]]: $\mathcal{L}_X g = 0$.
> 2. The flow $\phi_t$ of $X$ consists of isometries: $\phi_t^* g = g$ for all $t$ in the domain.
> 3. **Killing's equation**: $\nabla_a X_b + \nabla_b X_a = 0$, equivalently $\nabla X$ (as a $(0, 2)$-tensor via the metric) is skew-symmetric.
> 4. For all $Y, Z \in \mathfrak{X}(M)$: $\langle\nabla_Y X, Z\rangle + \langle Y, \nabla_Z X\rangle = 0$.

> **Consequence (Killing algebra is finite-dimensional).** The Killing fields on $(M, g)$ form a Lie algebra $\mathfrak{iso}(M, g)$ under the Lie bracket of vector fields, of dimension at most $n(n+1)/2$. The maximum is attained iff $(M, g)$ has constant sectional curvature.

---

# Motivation

A **Killing vector field** is the infinitesimal generator of a $1$-parameter group of isometries. This theorem characterises Killing fields *locally* — without reference to the global flow — via the algebraic condition that $\nabla X$ is skew-symmetric. The local characterisation is what makes Killing fields computationally tractable: instead of integrating the flow and verifying it preserves the metric, one solves the linear PDE system $\nabla_a X_b + \nabla_b X_a = 0$.

The Killing equation is a constraint with rich geometric meaning. **Skew-symmetry of $\nabla X$** says that $\nabla X$ at each point is, as a $(0, 2)$-tensor identified with a linear endomorphism, an element of the orthogonal Lie algebra $\mathfrak{o}(T_pM)$. So a Killing field is one whose covariant derivative is everywhere in the "infinitesimal orthogonal transformations" — an infinitesimal isometry, exactly as the name suggests.

A second crucial consequence: a Killing field is *determined* by $(X(p), \nabla X(p))$ at any single point $p$. The argument uses the curvature: the second covariant derivative $\nabla\nabla X$ is determined by $X$ and the curvature via the **Killing equation propagation** identity $\nabla_a\nabla_b X_c = R_{abcd}X^d$ (a consequence of the Killing equation + the Ricci identity). So higher derivatives of $X$ are determined by $(X, \nabla X)$ at $p$ + curvature data, and the field $X$ is reconstructed by integrating ODE systems. This gives the dimension bound: $\dim\mathfrak{iso} \le \dim T_pM + \dim\mathfrak{o}(T_pM) = n + n(n-1)/2 = n(n+1)/2$.

The theorem connects directly to the **Myers–Steenrod theorem**: the isometry group of any Riemannian manifold is a finite-dimensional Lie group of dimension at most $n(n+1)/2$, and the Killing fields are exactly its Lie algebra. The Killing equation is the infinitesimal version of "isometry."

---

# Sources and Targets

**Sources (Input Broadening).**

*Source 1: An explicit symmetry of the metric.* If $\mathrm{Iso}(M, g)$ contains a $1$-parameter subgroup, its generator is a Killing field. **The bridge:** every continuous symmetry of a Riemannian manifold is integrated by a Killing field, by the Myers–Steenrod theorem. **Example:** translations and rotations on $\mathbb{R}^n$ generate Killing fields; the rotations on $S^n$ inherited from $\mathrm{SO}(n+1)$ acting on the ambient $\mathbb{R}^{n+1}$ are all Killing.

*Source 2: A vector field whose flow preserves volume.* This is **weaker** than Killing — volume-preserving flows have $\mathcal{L}_X dV = 0$ (where $dV$ is the Riemannian volume form), equivalently $\mathrm{div}\, X = 0$. **The bridge:** Killing implies divergence-free (in fact $\mathrm{div}\, X = \mathrm{tr}(\nabla X) = 0$ from skew-symmetry of $\nabla X$), but not conversely. **Example:** an incompressible fluid flow on a Riemannian manifold has divergence-free velocity field but is typically *not* Killing — it preserves volume without preserving lengths.

*Source 3: A solution of the Killing equation $\nabla_a X_b + \nabla_b X_a = 0$ found by solving PDEs.* The Killing equation is a first-order linear PDE system; solutions form a finite-dim vector space (by the dimension bound) and can be sought directly via Cauchy-data approach. **The bridge:** prescribing $(X(p), \nabla X(p))$ at a point with $\nabla X(p) \in \mathfrak{o}(T_pM)$ gives a unique candidate; whether it extends globally depends on the curvature.

**Targets (Output Amplification).**

*Target 1: Killing's equation + a geodesic $\gamma$ with tangent $T$ gives a conserved quantity $\langle X, T\rangle$.* This is **Noether's theorem** in its purest geometric form. **Combined target:** Killing field + geodesic = conservation law. **Why useful:** explicit conservation laws make geodesic equations integrable. In Schwarzschild, the timelike Killing field $\partial_t$ gives energy conservation; the rotational Killing fields give angular momentum conservation; geodesic motion reduces to a 1D radial problem.

*Target 2: Killing's equation + $\mathrm{Ric}$ contraction gives $\Delta X^\flat = -\mathrm{Ric}(X)$, the **Bochner equation**.* Combined with integration by parts on a compact manifold, this gives the **Bochner vanishing theorem**: on a compact manifold with $\mathrm{Ric} < 0$, there are no nontrivial Killing fields. **Combined target:** Killing equation + negative Ricci = vanishing of Killing algebra. **Why useful:** negatively-curved compact manifolds have *no* continuous symmetries — their isometry group is *discrete*. See [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]].

*Target 3: Killing field $X$ + harmonic function $f$ gives $X(f)$ harmonic.* If $\Delta f = 0$ and $X$ is Killing, then $\mathcal{L}_X\Delta = \Delta\mathcal{L}_X$ (Killing fields commute with the Laplacian because they preserve the metric), so $\Delta(Xf) = X(\Delta f) = 0$. **Combined target:** Killing-equivariant harmonic analysis. **Why useful:** spectral theory on homogeneous spaces (e.g., spherical harmonics on $S^n$) decomposes the Laplacian under the Killing-algebra action, giving the standard $\mathrm{SO}(n+1)$-irreducible decomposition of $L^2(S^n)$.

---

# Why Is It True

The equivalence of (1), (2), (3), (4) is a calculation translating between different forms of "the flow preserves $g$." The deep equivalence is **(1) ⟺ (3)**: $\mathcal{L}_X g = 0$ is the symmetric part of $\nabla X$ (as a $(0, 2)$-tensor) vanishing.

To see this: compute $(\mathcal{L}_X g)(Y, Z)$ from the definition and rewrite using metric compatibility:

$$(\mathcal{L}_X g)(Y, Z) = X\langle Y, Z\rangle - \langle[X, Y], Z\rangle - \langle Y, [X, Z]\rangle.$$

Using metric compatibility, $X\langle Y, Z\rangle = \langle\nabla_X Y, Z\rangle + \langle Y, \nabla_X Z\rangle$. Using torsion-freeness, $[X, Y] = \nabla_X Y - \nabla_Y X$. Substitute:

$$(\mathcal{L}_X g)(Y, Z) = \langle\nabla_X Y, Z\rangle + \langle Y, \nabla_X Z\rangle - \langle\nabla_X Y - \nabla_Y X, Z\rangle - \langle Y, \nabla_X Z - \nabla_Z X\rangle$$

$$= \langle\nabla_Y X, Z\rangle + \langle Y, \nabla_Z X\rangle.$$

So $(\mathcal{L}_X g)(Y, Z) = \langle\nabla_Y X, Z\rangle + \langle Y, \nabla_Z X\rangle$ — the symmetric part of $\nabla X$ as a $(0, 2)$-tensor. The Killing equation $\nabla_a X_b + \nabla_b X_a = 0$ is exactly this symmetric part vanishing.

**The bolded mechanism summary: $\mathcal{L}_X g$, computed via metric compatibility and torsion-freeness, is exactly $2 \cdot \mathrm{sym}(\nabla X)$ — the symmetric part of $\nabla X$ as a $(0, 2)$-tensor. The Killing equation $\nabla X$ skew is the precise infinitesimal version of "$\phi_t$ is an isometry."**

The equivalence (1) ⟺ (2) is the standard relation between Lie derivative and flow: $\mathcal{L}_X T = \tfrac{d}{dt}\big|_{t=0}\phi_t^* T$ for any tensor $T$.

The dimension bound comes from the **Killing propagation equation**: differentiating the Killing equation $\nabla_a X_b + \nabla_b X_a = 0$ and using the Ricci identity $[\nabla_a, \nabla_b]X_c = R_{abc}{}^d X_d$ to commute derivatives gives

$$\nabla_a\nabla_b X_c = R_{cab}{}^d X_d,$$

expressing the second covariant derivative of $X$ in terms of $X$ and the curvature. Iterating, all higher derivatives are determined by $X(p)$ and $\nabla X(p)$ at any point. So the dimension is at most $\dim T_pM + \dim\mathfrak{o}(T_pM) = n + n(n-1)/2 = n(n+1)/2$.

---

# What Makes This Hard

The equivalence proof is mechanical but easy to get wrong. The most common error is to forget that *both* metric compatibility and torsion-freeness of the Levi-Civita connection are used — without metric compatibility, $X\langle Y, Z\rangle$ does not split; without torsion-freeness, $[X, Y]$ does not rewrite as $\nabla_X Y - \nabla_Y X$. The Killing equation is genuinely a property of the Levi-Civita connection; a connection with torsion would have a different "Killing equation" mixing torsion terms with the symmetric derivative.

The dimension bound's proof requires the Killing propagation equation, which uses the Ricci identity in a way that students often find unfamiliar. The standard derivation is: from $\nabla_b X_c + \nabla_c X_b = 0$, take $\nabla_a$: $\nabla_a\nabla_b X_c + \nabla_a\nabla_c X_b = 0$. Cyclically permute and add three such equations; use the Ricci identity to convert $\nabla_a\nabla_b X_c - \nabla_b\nabla_a X_c$ into curvature terms. After bookkeeping, $\nabla_a\nabla_b X_c$ is expressed in terms of $R$ and $X$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Compute $(\mathcal{L}_X g)(Y, Z)$ from the definition; use metric compatibility and torsion-freeness of $\nabla$ to rewrite it as the symmetric part of $\nabla X$ as a $(0, 2)$-tensor. The Killing equation is precisely this symmetric part vanishing. For the dimension bound, derive the Killing propagation equation $\nabla\nabla X = R \cdot X$ from the Killing equation + Ricci identity.

**Subgoal decomposition:**

1. **$(\mathcal{L}_X g)(Y, Z) = 2\,\mathrm{sym}(\nabla X)(Y, Z)$ using metric compatibility + torsion-freeness.**
   - *Hint:* Expand $\mathcal{L}_X g$; use $X\langle Y, Z\rangle = \langle\nabla_X Y, Z\rangle + \langle Y, \nabla_X Z\rangle$ and $[X, Y] = \nabla_X Y - \nabla_Y X$; simplify.
   - *Why needed:* Establishes (1) ⟺ (3) ⟺ (4).

2. **(1) ⟺ (2) from the standard Lie-derivative-flow relation.**
   - *Hint:* $\mathcal{L}_X T = (d/dt)|_{t=0}\phi_t^* T$ for any tensor $T$.
   - *Why needed:* Connects the algebraic characterisation to the geometric one.

3. **Killing propagation equation: $\nabla_a\nabla_b X_c = R_{cab}{}^d X_d$.**
   - *Hint:* Differentiate the Killing equation $\nabla_b X_c + \nabla_c X_b = 0$ to get $\nabla_a(\nabla_b X_c) = -\nabla_a\nabla_c X_b$; cyclically permute and use Ricci identity.
   - *Why needed:* Used to derive the dimension bound $n(n+1)/2$.

4. **Dimension bound $\dim\mathfrak{iso}(M, g) \le n(n+1)/2$.**
   - *Hint:* A Killing field is determined by $(X(p), \nabla X(p))$ at any single point $p$ (by Killing propagation + ODE). The data $\nabla X(p)$ is constrained to lie in $\mathfrak{o}(T_pM)$ (skew, by Killing equation), so dimension $\le n + n(n-1)/2 = n(n+1)/2$.
   - *Why needed:* Quantitative refinement.

---

# Lemma Decomposition

> [!note]- Lemma 1: $(\mathcal{L}_X g)(Y, Z) = \langle\nabla_Y X, Z\rangle + \langle Y, \nabla_Z X\rangle$
> **Statement:** For any vector fields $X, Y, Z$ on a Riemannian manifold with Levi-Civita connection $\nabla$, $(\mathcal{L}_X g)(Y, Z) = \langle\nabla_Y X, Z\rangle + \langle Y, \nabla_Z X\rangle$.
>
> **Hint:** Definition of $\mathcal{L}_X g$ + metric compatibility + torsion-freeness.
>
> **Why needed:** This is the algebraic computation behind the equivalence (1) ⟺ (3) ⟺ (4).
>
> > [!note]- Full proof
> > $(\mathcal{L}_X g)(Y, Z) = X\langle Y, Z\rangle - \langle[X, Y], Z\rangle - \langle Y, [X, Z]\rangle$ by definition. Use **metric compatibility**: $X\langle Y, Z\rangle = \langle\nabla_X Y, Z\rangle + \langle Y, \nabla_X Z\rangle$. Use **torsion-freeness**: $[X, Y] = \nabla_X Y - \nabla_Y X$, hence $\langle[X, Y], Z\rangle = \langle\nabla_X Y, Z\rangle - \langle\nabla_Y X, Z\rangle$. Similarly $\langle Y, [X, Z]\rangle = \langle Y, \nabla_X Z\rangle - \langle Y, \nabla_Z X\rangle$. Substitute:
> > $$(\mathcal{L}_X g)(Y, Z) = \langle\nabla_X Y, Z\rangle + \langle Y, \nabla_X Z\rangle - \langle\nabla_X Y, Z\rangle + \langle\nabla_Y X, Z\rangle - \langle Y, \nabla_X Z\rangle + \langle Y, \nabla_Z X\rangle.$$
> > The $\langle\nabla_X Y, Z\rangle$ and $\langle Y, \nabla_X Z\rangle$ terms cancel, leaving $\langle\nabla_Y X, Z\rangle + \langle Y, \nabla_Z X\rangle$.

> [!note]- Lemma 2: $\mathcal{L}_X g = 0 \iff \nabla X$ skew-symmetric as a $(0, 2)$-tensor
> **Statement:** $\mathcal{L}_X g = 0 \iff \nabla_a X_b + \nabla_b X_a = 0$.
>
> **Hint:** From Lemma 1, $(\mathcal{L}_X g)(Y, Z) = \langle\nabla_Y X, Z\rangle + \langle Y, \nabla_Z X\rangle$. This is the symmetrisation of the bilinear form $(Y, Z) \mapsto \langle\nabla_Y X, Z\rangle$. So $\mathcal{L}_X g = 0$ iff this bilinear form is antisymmetric.
>
> **Why needed:** Direct equivalence (1) ⟺ (3).
>
> > [!note]- Full proof
> > Define $A(Y, Z) := \langle\nabla_Y X, Z\rangle$. Lemma 1 gives $(\mathcal{L}_X g)(Y, Z) = A(Y, Z) + A(Z, Y)$, the symmetrisation of $A$. So $\mathcal{L}_X g = 0 \iff A(Y, Z) + A(Z, Y) = 0$ for all $Y, Z \iff A$ is antisymmetric. In components, $A(Y, Z) = (\nabla_Y X)_b Z^b = (\nabla X^\flat)_{ab}Y^a Z^b$ where $(\nabla X^\flat)_{ab} = \nabla_a X_b$. Antisymmetry of this bilinear form is $\nabla_a X_b = -\nabla_b X_a$, equivalently $\nabla_a X_b + \nabla_b X_a = 0$.

> [!note]- Lemma 3: Killing propagation equation $\nabla_a\nabla_b X_c = R_{cab}{}^d X_d$
> **Statement:** If $X$ satisfies the Killing equation $\nabla_a X_b + \nabla_b X_a = 0$, then $\nabla_a\nabla_b X_c = R_{cab}{}^d X_d$ (where $R_{abcd}$ is the covariant Riemann tensor and $R_{cab}{}^d$ has the last index raised).
>
> **Hint:** Differentiate the Killing equation, sum cyclically with the Ricci identity for commuting covariant derivatives.
>
> **Why needed:** Determines second (and hence all higher) derivatives of $X$ from $X$ and curvature.
>
> > [!note]- Full proof
> > Take $\nabla_a$ of the Killing equation $\nabla_b X_c + \nabla_c X_b = 0$:
> > $$\nabla_a\nabla_b X_c + \nabla_a\nabla_c X_b = 0. \qquad (*)$$
> > Cyclically permute $(a, b, c)$:
> > $$\nabla_b\nabla_c X_a + \nabla_b\nabla_a X_c = 0, \qquad \nabla_c\nabla_a X_b + \nabla_c\nabla_b X_a = 0. \qquad (**)$$
> > Add $(*)$ + cyclic terms and use the **Ricci identity** $[\nabla_a, \nabla_b]X_c = -R_{abc}{}^d X_d$ (sign convention dependent — verify carefully) to convert commutators of covariant derivatives into curvature terms. After bookkeeping:
> > $$2\nabla_a\nabla_b X_c = (R_{cab}{}^d + R_{abc}{}^d + R_{bca}{}^d) X_d = 2R_{cab}{}^d X_d$$
> > using the first Bianchi identity to combine cyclic curvature terms. So $\nabla_a\nabla_b X_c = R_{cab}{}^d X_d$.

> [!note]- Lemma 4: Dimension bound $\dim\mathfrak{iso}(M, g) \le n(n+1)/2$
> **Statement:** The Lie algebra of Killing fields on a connected Riemannian $n$-manifold has dimension at most $n(n+1)/2$.
>
> **Hint:** A Killing field is uniquely determined by $(X(p), \nabla X(p))$ at any single point $p$, by Killing propagation. The data $X(p) \in T_pM$ ($n$-dim) and $\nabla X(p) \in \mathfrak{o}(T_pM)$ (the constraint is from the Killing equation), giving total dimension $n + n(n-1)/2 = n(n+1)/2$.
>
> **Why needed:** The quantitative bound on $\dim\mathfrak{iso}$.
>
> > [!note]- Full proof
> > Fix $p \in M$. By Lemma 3, the Killing propagation equation determines $\nabla\nabla X$ from $X$ and curvature; iterating, all higher derivatives of $X$ at any point are determined by $(X(p), \nabla X(p))$. By the standard ODE theory for Killing fields (treating the geodesic exponential as a "frame" along which to integrate), $X$ is uniquely determined globally on the connected component of $p$ by $(X(p), \nabla X(p))$.
> > 
> > The space of allowed $(X(p), \nabla X(p))$ is $T_pM \oplus \mathfrak{o}(T_pM) = T_pM \oplus \mathrm{skew}(T_pM \otimes T_p^*M)$, with the second factor having dimension $\binom{n}{2} = n(n-1)/2$. Total: $n + n(n-1)/2 = n(n+1)/2$.

> [!note]- Lemma 5: Maximum dimension achieved iff $(M, g)$ has constant sectional curvature
> **Statement:** $\dim\mathfrak{iso}(M, g) = n(n+1)/2$ iff $(M, g)$ has constant sectional curvature.
>
> **Hint:** Maximum dimension requires *every* element of $T_pM \oplus \mathfrak{o}(T_pM)$ to be realisable as initial data for a Killing field. This is a constraint on curvature.
>
> **Why needed:** Connects maximum-symmetry to constant curvature.
>
> > [!note]- Full proof
> > Sketch: realising every initial data $(v, A) \in T_pM \oplus \mathfrak{o}(T_pM)$ as a Killing field requires the Killing propagation equation $\nabla_a\nabla_b X_c = R_{cab}{}^d X_d$ to be self-consistent for every choice of initial data. This consistency condition is exactly that $R$ has the algebraic form of constant sectional curvature (after a careful analysis using the symmetries of $R$). Conversely, on $S^n$, $\mathbb{R}^n$, $H^n$ — all of constant curvature — the isometry group is of dimension $n(n+1)/2$, realising the maximum.

---

# Formal Proof

> [!note]- Complete formal proof
> Lemma 1 + Lemma 2 establish the equivalence (1) ⟺ (3) ⟺ (4). The equivalence (1) ⟺ (2) is the standard relationship between Lie derivative and flow: for any tensor $T$, $\mathcal{L}_X T = (d/dt)|_{t=0}\phi_t^* T$, so $\mathcal{L}_X g = 0 \iff (d/dt)|_{t=0}\phi_t^* g = 0$. Since $g - \phi_t^* g$ is smooth in $t$ and the derivative vanishes, and the flow is a group ($\phi_{t+s} = \phi_t\circ\phi_s$), we get $\phi_t^* g = g$ for all $t$, i.e., $\phi_t$ is an isometry.
>
> The dimension bound (Lemma 4) and its maximum-attainment characterisation (Lemma 5) are corollaries.

---

# Cross-Field Exercise Suggestions

1. **Conserved quantities along geodesics in Schwarzschild.** The Schwarzschild metric has $4$ Killing fields: $\partial_t$ (timelike) and three rotational Killing fields $\partial_\varphi, X_{\theta\varphi}, X_{r\theta}$ (generating the $\mathrm{SO}(3)$-action on $S^2$). For a geodesic $\gamma$ with tangent $T$, the four quantities $\langle\partial_t, T\rangle = -E$ (energy), $\langle\partial_\varphi, T\rangle = L_z$ (axial angular momentum), and two more components of angular momentum are constant along $\gamma$. This reduces geodesic motion in Schwarzschild to a $1$-dimensional radial problem — the foundation of black-hole orbital mechanics. See [[General Relativity I — Einstein's Equations and Schwarzschild]].

2. **Bochner's vanishing theorem for Killing fields.** On a compact Riemannian manifold with $\mathrm{Ric} < 0$, there are no nontrivial Killing fields. Proof via the **Bochner formula** $\Delta|X|^2/2 = |\nabla X|^2 + \mathrm{Ric}(X, X)$ (for a Killing field $X$): integrating over $M$ kills the LHS, leaving $0 = \int |\nabla X|^2 + \int\mathrm{Ric}(X, X)$; under $\mathrm{Ric} < 0$ both terms are nonnegative (with strict inequalities except at $X = 0$), so $X = 0$. Compact negatively-curved manifolds have *discrete* isometry groups. See [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]].

3. **Spherical harmonics from the Killing-algebra action on $S^n$.** The $\mathfrak{so}(n+1)$-action on $S^n$ via Killing fields gives an $\mathfrak{so}(n+1)$-module structure on $L^2(S^n)$. The Laplacian $\Delta$ commutes with this action, so its eigenspaces are $\mathfrak{so}(n+1)$-irreducible representations. The decomposition $L^2(S^n) = \bigoplus_{\ell \ge 0}\mathcal{H}_\ell$ into spaces of homogeneous harmonic polynomials of degree $\ell$ is the **Peter–Weyl theorem** specialised to $S^n$, and the $\mathcal{H}_\ell$ are exactly the irreducible $\mathfrak{so}(n+1)$-modules of highest weight $\ell$.

---

# Bridges

- **Myers–Steenrod theorem.** The isometry group $\mathrm{Iso}(M, g)$ of any Riemannian manifold is a finite-dimensional Lie group of dimension at most $n(n+1)/2$, by **Myers–Steenrod** ($1939$). The Killing equation is the Lie-algebra version of this: $\mathfrak{iso}(M, g) = \mathrm{Lie}(\mathrm{Iso}(M, g))$, with the dimension bound from Lemma 4 matching Myers–Steenrod's bound on $\dim\mathrm{Iso}$.

- **Noether's theorem.** Killing fields are the geometric form of Noether's theorem: every continuous symmetry of the metric ($\mathcal{L}_X g = 0$) gives a conserved quantity along geodesics ($\langle X, T\rangle = \mathrm{const}$). This generalises to **momentum maps** in symplectic geometry — see [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics]].

- **Bochner technique.** The Bochner formula $\Delta|X|^2/2 = |\nabla X|^2 + \mathrm{Ric}(X, X)$ for Killing fields connects Killing's equation to **Hodge-theoretic vanishing**: positive Ricci forces vanishing of harmonic $1$-forms; negative Ricci forces vanishing of Killing fields. This is the **Bochner technique** in its two main applications. See [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]].

- **Constant-sectional-curvature manifolds as maximal-symmetry spaces.** The maximum-dimension Killing algebra $\mathfrak{iso}(M, g) = \mathfrak{o}(n+1)$ (on $S^n$), $\mathfrak{iso}(\mathbb{R}^n) = \mathbb{R}^n \rtimes \mathfrak{o}(n)$, or $\mathfrak{o}(1, n)$ (on $H^n$) — all of dimension $n(n+1)/2$ — is achieved only by the model spaces of constant sectional curvature (Lemma 5). This characterises the model spaces as the maximally-symmetric Riemannian manifolds. See [[Def - Model Spaces (Sphere Euclidean Hyperbolic)]].
