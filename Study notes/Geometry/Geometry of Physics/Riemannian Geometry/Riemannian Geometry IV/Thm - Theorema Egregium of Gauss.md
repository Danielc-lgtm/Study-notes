---
type: theorem
subject: riemannian-geometry
prereqs:
  - "Def - First Fundamental Form"
  - "Def - Second Fundamental Form"
  - "Def - Gauss Curvature and Mean Curvature"
  - "Thm - Equations of Gauss and Codazzi"
tags: [geometry, riemannian-geometry, surfaces, curvature, theorema-egregium]
---

# Notation

Let $M \subset \mathbb{R}^3$ be an oriented regular surface with [[Def - First Fundamental Form|first fundamental form]] $\mathrm{I} = g_{\alpha\beta}\, du^\alpha du^\beta$ and [[Def - Second Fundamental Form|second fundamental form]] $\mathrm{II} = b_{\alpha\beta}\, du^\alpha du^\beta$. The Christoffel symbols of $g_{\alpha\beta}$ are $\Gamma^\gamma_{\alpha\beta}$, and the Riemann curvature tensor of $g$ is $R^\tau_{\;\alpha\gamma\beta}$, computed from the Christoffel symbols by the standard formula. We write $R_{1212} = g_{1\sigma}R^\sigma_{\;212}$ for the unique non-redundant covariant component on a $2$-manifold, and $K$ for the Gauss curvature. Full registry on [[Riemannian Geometry IV — Classical Geometry of Surfaces in R^3]].

---

# Statement

> **Theorem (Theorema Egregium of Gauss, 1827).** The Gauss curvature of a regular surface $M \subset \mathbb{R}^3$ is **intrinsic**: it depends only on the first fundamental form $g_{\alpha\beta}$ and its derivatives, not on the embedding of $M$ in $\mathbb{R}^3$. Explicitly,
> $$
> K = \frac{R_{1212}}{\det g_{\alpha\beta}},
> $$
> where $R_{1212}$ is the unique non-redundant covariant component of the Riemann curvature tensor computed from the Christoffel symbols of $g_{\alpha\beta}$.

> **Corollary (Local isometry preserves $K$).** If $\phi : (M, g) \to (M', g')$ is a local isometry between two regular surfaces in $\mathbb{R}^3$, then $K(p) = K'(\phi(p))$ for every $p \in M$. In particular, "bending without stretching" — a deformation that preserves arc length — preserves the Gauss curvature, even though the principal curvatures $\kappa_1, \kappa_2$ and the mean curvature $H$ change.

> **Corollary (Cartography corollary).** No portion of the sphere of radius $a$ (which has $K = 1/a^2$) can be isometrically mapped to any portion of the Euclidean plane (which has $K = 0$). So every flat map of the Earth must introduce distortion.

---

# Motivation

Gauss discovered this theorem during his geodetic survey of the kingdom of Hannover in the 1820s, while developing the geometry of surfaces for the practical purpose of constructing accurate maps. The theorem answers the question: **which curvature invariants of a surface can be measured by an inhabitant of the surface alone, without reference to the ambient $3$-space?** The first fundamental form encodes everything an inhabitant can measure with a tape measure (lengths, angles, areas). The Gauss curvature, defined extrinsically as the product $K = \kappa_1\kappa_2$ or as the Jacobian of the Gauss normal map, *appears* to require the embedding (the principal curvatures depend on $\mathrm{II}$, which depends on $N$). The Egregium says: contrary to appearances, $K$ is intrinsic — it can be computed from the metric alone.

This is the historical seed of all of modern intrinsic differential geometry. Riemann's 1854 *Habilitationsvortrag* generalised the principle to arbitrary $n$-dimensional Riemannian manifolds, defining curvature intrinsically via the **Riemann curvature tensor**. Einstein's 1915 general relativity made this intrinsic curvature the *dynamical field* of gravity — the spacetime metric is a Lorentzian manifold whose curvature governs the motion of matter, and *no embedding into a higher-dimensional space is needed or available*. The entire intellectual lineage from Gauss → Riemann → Einstein hinges on the Egregium: it is what makes "curvature without embedding" coherent.

The name *Theorema Egregium* — Latin for "remarkable theorem" — reflects Gauss's own assessment. He published it in *Disquisitiones generales circa superficies curvas* (1827), with the word *egregium* signalling that this was unexpected, surprising, and important. It remains one of the most quoted theorems in differential geometry.

---

# Sources and Targets

**Sources (Input Broadening).**

*Source 1: A surface given by an explicit metric, with no embedding in sight.* Whenever one has a Riemannian metric on a $2$-dimensional space — the hyperbolic plane in upper-half-plane form $g = (dx^2 + dy^2)/y^2$, the torus with the flat quotient metric, a surface of revolution defined by a metric ansatz like $g = du^2 + f(u)^2 dv^2$ — the Egregium gives an algorithm for computing $K$: compute the Christoffel symbols, then $R^\tau_{\;\alpha\gamma\beta}$, then $K = R_{1212}/\det g$. **Why $B \Rightarrow A$:** The Egregium asserts the formula's validity; without it, one would expect $K$ to be computable only from an embedding. **Example problem:** Compute $K$ for the upper half-plane metric — the answer is $K = -1$ (the hyperbolic plane is constantly negatively curved), derived purely from the metric.

*Source 2: Two surfaces suspected to be locally isometric.* If two surfaces $M, M'$ have parametrisations giving different $g_{\alpha\beta}$ formulae but suspected of being isometric (via some change of coordinates), the Egregium provides a test: compute $K(p)$ and $K'(p')$ at corresponding points. If $K \neq K'$, they are *not* locally isometric — done. **Why $B \Rightarrow A$:** The Egregium says local isometry preserves $K$; this is a necessary condition that can rule out isometry. **Example problem:** Is the sphere of radius $a$ locally isometric to the sphere of radius $b$? Compute $K_a = 1/a^2$ vs $K_b = 1/b^2$; equal iff $a = b$. So spheres of different radii are not locally isometric — a slightly surprising rigidity result.

*Source 3: A surface with a clear geometric symmetry making one computation easier.* For a surface of revolution, the intrinsic formula often involves only one variable (the radial distance $r$), simplifying $K = K(r)$ to an ODE; for a developable surface (one with $K = 0$), the Egregium identifies it as locally isometric to the plane. **Why $B \Rightarrow A$:** The Egregium reduces the computation of $K$ to operations on the metric alone, which becomes simple when the metric has symmetry. **Example problem:** For a surface of revolution with meridian curve $(\rho(t), z(t))$ parametrised by arc length (so $\rho'^2 + z'^2 = 1$), the metric is $g = dt^2 + \rho^2 d\theta^2$, and the Egregium gives $K = -\rho''/\rho$ — a simple ODE expression, derivable purely from the meridian profile.

**Targets (Output Amplification).**

*Target 1: Detect impossibility of certain isometric embeddings (rigidity).* If a surface $M$ has $K(p_0) > 0$ at some point, then $M$ cannot be locally isometric to any *flat* surface at $p_0$. So $S^2$ cannot be unrolled onto the plane locally. **Why nonobvious:** It is not at all obvious *a priori* that $K$ blocks the isometry — but the Egregium says it does, completely. **Application:** The cartography corollary, ruling out distortion-free flat maps of the Earth.

*Target 2: Identify "intrinsically flat" surfaces.* A surface with $K \equiv 0$ everywhere is locally isometric to the plane (Beltrami–Minding theorem, a strong converse). Such surfaces are called **developable** and include cylinders, cones (away from the vertex), and tangent-developable surfaces (the surface swept out by tangent lines to a space curve). **Why nonobvious:** $K = 0$ extrinsically just means one principal curvature vanishes; intrinsically it means flat (locally isometric to $\mathbb{R}^2$). The Egregium plus the Beltrami–Minding converse make these equivalent. **Application:** Industrial design — flat sheet metal can only be bent into developable surfaces without stretching.

*Target 3: Compute the intrinsic curvature of abstract Riemannian $2$-manifolds.* The Egregium provides the *definition* of curvature for surfaces given without an embedding (e.g., abstract Riemannian metrics on a topological surface). This is the entry point to **intrinsic Riemannian geometry**: in the higher-dimensional case, the Riemann curvature tensor $R^\sigma_{\;\rho\mu\nu}$ generalises $R_{1212}$, and curvature is defined entirely from the metric without any ambient space. **Why nonobvious:** Without the Egregium, one might think one needed an embedding to define curvature; the theorem shows the intrinsic definition is consistent and complete.

---

# Why Is It True

The proof of the Egregium has two layers: (i) the **Gauss equations** ([[Thm - Equations of Gauss and Codazzi]]) express the Riemann curvature components of the induced metric in terms of $b_{\alpha\beta}$ via $R^\tau_{\;\alpha\gamma\beta} = b^\tau_{\;\gamma}b_{\alpha\beta} - b^\tau_{\;\beta}b_{\alpha\gamma}$, and (ii) for the particular component $R_{1212}$, this expression collapses to $b_{11}b_{22} - b_{12}^2 = \det b_{\alpha\beta}$, dividing by $\det g$ gives $K$. But the magic is that *the other side* of the equation — $R^\tau_{\;\alpha\gamma\beta}$ computed from the Christoffel symbols — depends *only* on the metric. So both sides are equal, and one side is intrinsic, hence the other side ($K$) is too.

**The deep mechanism: $K$ measures the failure of second covariant derivatives to commute, and that failure is built into the metric.** In intrinsic Riemannian language, the Riemann tensor $R(X, Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X, Y]}Z$ measures the non-commutativity of covariant derivatives — an intrinsic quantity, since $\nabla$ is the Levi-Civita connection of the metric (intrinsic). The Egregium is the surface case of the much more general fact that the Riemann tensor is an intrinsic invariant of any Riemannian manifold.

**The bolded one-liner:** **the Egregium works because the Gauss equation $R^\tau_{\;\alpha\gamma\beta} = b^\tau_{\;\gamma}b_{\alpha\beta} - b^\tau_{\;\beta}b_{\alpha\gamma}$ expresses an intrinsic quantity (Riemann curvature of $g$) as a function of an extrinsic quantity ($b_{\alpha\beta}$), forcing certain combinations of the extrinsic data to be intrinsic — and $\det b/\det g$ is the surviving combination.**

A geometric perspective. The Gauss curvature equals the **holonomy** of parallel transport around an infinitesimal loop, divided by the loop's enclosed area:
$$
K(p) = \lim_{\text{loop} \to p}\frac{\text{rotation angle of parallel transport}}{\text{area enclosed}}.
$$
Both the parallel transport (intrinsic, defined by the Levi-Civita connection) and the area (intrinsic, defined by the metric) are intrinsic, so their ratio is intrinsic — and this ratio is $K$. This is one of the cleanest "why is it true" pictures: $K$ is an intrinsic ratio of two intrinsic quantities.

Another perspective. The Gauss equation can be rewritten as a Pythagorean-like identity for areas: if you parametrise a small piece of $M$ near $p$ and parallel-transport a vector around its boundary, the parallel transport returns to its original direction rotated by an angle equal to $K(p)$ times the enclosed area. The plane has zero rotation (zero curvature); a great circle on $S^2$ enclosing a region of area $A$ returns parallel-transported vectors rotated by $A/a^2$ for the sphere of radius $a$ — exactly $\int K\, dA = A\cdot K$.

---

# What Makes This Hard

The proof itself is calculation — the Egregium follows in a few lines from the Gauss equation. **The hard part is identifying which combination of $(b_{\alpha\beta}, g_{\alpha\beta})$ survives as intrinsic.** Out of the components $b_{11}, b_{12}, b_{22}$ separately, none is intrinsic; out of polynomial combinations, $\det b/\det g$ is the unique combination that turns out intrinsic. The Gauss equations *tell* us this combination — they make the appearance of $K = \det b/\det g$ on the right side of $R^\tau_{\;\alpha\gamma\beta} = b^\tau_{\;\gamma}b_{\alpha\beta} - b^\tau_{\;\beta}b_{\alpha\gamma}$ the mechanism that forces intrinsicity. Without first deriving the Gauss equations, the identification of the intrinsic combination is mysterious.

A common confusion: students sometimes try to "prove" $K$ is intrinsic by direct manipulation of the embedding-defined formula $K = \det b/\det g$, finding no obvious way to eliminate dependence on $b_{\alpha\beta}$. The trick is that the Gauss equation *expresses* $\det b/\det g$ as $R_{1212}/\det g$, and *this* is manifestly intrinsic. So one cannot avoid invoking the Gauss equation; trying to prove the Egregium "directly" without it leads nowhere.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy.** Derive the Gauss equations relating $R^\tau_{\;\alpha\gamma\beta}$ to $b_{\alpha\beta}$ (via the surface equations $\mathbf{x}_{\alpha\beta} = \Gamma^\gamma_{\alpha\beta}\mathbf{x}_\gamma + b_{\alpha\beta}N$ and the equality $\mathbf{x}_{\alpha\beta\gamma} = \mathbf{x}_{\alpha\gamma\beta}$). Take the $(1, 2, 1, 2)$ component to get $R^1_{\;212} = b^1_{\;1}b_{22} - b^1_{\;2}b_{21}$. Lower an index: $R_{1212} = g_{1\sigma}R^\sigma_{\;212} = b_{11}b_{22} - b_{12}^2 = \det b_{\alpha\beta}$. Divide by $\det g$: $K = \det b/\det g = R_{1212}/\det g$.

**Subgoal decomposition:**

1. **Derive the Gauss surface equations.** Show that $\mathbf{x}_{\alpha\beta} = \Gamma^\gamma_{\alpha\beta}\mathbf{x}_\gamma + b_{\alpha\beta}N$, with $\Gamma^\gamma_{\alpha\beta}$ being the Christoffel symbols of $g_{\alpha\beta}$.
   - *Hint:* Decompose $\mathbf{x}_{\alpha\beta}$ into tangential and normal parts; the normal coefficient is $\langle\mathbf{x}_{\alpha\beta}, N\rangle = b_{\alpha\beta}$; the tangential coefficients $\Gamma^\gamma_{\alpha\beta}$ are computed by dotting with $\mathbf{x}_\mu$ and using the chain rule on $\partial g_{\alpha\mu}/\partial u^\beta$.
   - *Why needed:* This is the bridge between embedding data (second derivatives of $\mathbf{x}$) and intrinsic + extrinsic data ($\Gamma^\gamma_{\alpha\beta}$ and $b_{\alpha\beta}$).

2. **Take the third partial derivative and use commutativity.** From $\mathbf{x}_{\alpha\beta\gamma} = \mathbf{x}_{\alpha\gamma\beta}$, extract the integrability conditions. These give the Gauss equations $R^\tau_{\;\alpha\gamma\beta} = b^\tau_{\;\gamma}b_{\alpha\beta} - b^\tau_{\;\beta}b_{\alpha\gamma}$ and the Codazzi equations.
   - *Hint:* Differentiate the Gauss equation $\mathbf{x}_{\alpha\beta} = \Gamma^\gamma_{\alpha\beta}\mathbf{x}_\gamma + b_{\alpha\beta}N$ with respect to $u^\gamma$, apply the Gauss equation again to $\mathbf{x}_{\gamma\mu}$ and the Weingarten equation $N_\gamma = -b^\sigma_{\;\gamma}\mathbf{x}_\sigma$, swap $\beta \leftrightarrow \gamma$, subtract. The tangential part gives the Gauss equation for $R^\tau$; the normal part gives Codazzi.
   - *Why needed:* The integrability conditions force a relation between the intrinsic Riemann curvature (built from metric) and the extrinsic shape operator data.

3. **Extract the $(1, 2, 1, 2)$ component.** With $\tau = 1$, $\alpha = 2$, $\gamma = 1$, $\beta = 2$: $R^1_{\;212} = b^1_{\;1}b_{22} - b^1_{\;2}b_{21}$. Lower the index $\tau$ via $g_{1\sigma}$: $R_{1212} = g_{1\sigma}R^\sigma_{\;212} = b_{11}b_{22} - b_{12}^2$ (using $b^\sigma_{\;\beta} = g^{\sigma\tau}b_{\tau\beta}$).
   - *Hint:* This is straightforward index gymnastics — compute the matrix product and remember $b^\sigma_{\;\beta} = g^{\sigma\tau}b_{\tau\beta}$.
   - *Why needed:* The combination $b_{11}b_{22} - b_{12}^2 = \det b_{\alpha\beta}$ appears, and $\det b/\det g = K$.

4. **Conclude $K = R_{1212}/\det g$.** Combining steps 1–3: $R_{1212} = \det b_{\alpha\beta}$, and $K = \det b/\det g$, so $K = R_{1212}/\det g$. The right side is intrinsic (built from $g$ alone), hence $K$ is intrinsic.
   - *Hint:* Just substitute.
   - *Why needed:* This is the Theorema Egregium.

---

# Lemma Decomposition

> [!note]- Lemma 1: Gauss surface equations decompose $\mathbf{x}_{\alpha\beta}$ into intrinsic + extrinsic parts
> **Statement:** For a regular surface $M = F(U) \subset \mathbb{R}^3$ with position vector $\mathbf{x}(u, v)$ and unit normal $N$,
> $$
> \mathbf{x}_{\alpha\beta} = \Gamma^\gamma_{\alpha\beta}\mathbf{x}_\gamma + b_{\alpha\beta}N,
> $$
> where $\Gamma^\gamma_{\alpha\beta} = \tfrac{1}{2}g^{\gamma\tau}(\partial_\beta g_{\alpha\tau} + \partial_\alpha g_{\beta\tau} - \partial_\tau g_{\alpha\beta})$ are the Christoffel symbols of the induced metric.
>
> **Hint:** Decompose $\mathbf{x}_{\alpha\beta}$ orthogonally into tangential and normal parts; the normal part is $\langle\mathbf{x}_{\alpha\beta}, N\rangle N = b_{\alpha\beta}N$. For the tangential coefficients, dot with $\mathbf{x}_\mu$ and use $\partial g_{\alpha\mu}/\partial u^\beta = \langle\mathbf{x}_{\alpha\beta}, \mathbf{x}_\mu\rangle + \langle\mathbf{x}_\alpha, \mathbf{x}_{\mu\beta}\rangle$.
>
> **Why needed:** This identifies the *intrinsic* coefficients $\Gamma^\gamma_{\alpha\beta}$ (depending on $g$ alone) and *extrinsic* coefficient $b_{\alpha\beta}$, separating the embedding data into the two pieces.
>
> > [!note]- Full proof
> > Decompose $\mathbf{x}_{\alpha\beta} \in \mathbb{R}^3 = T_pM \oplus \mathbb{R}N$ as $\mathbf{x}_{\alpha\beta} = c^\gamma_{\;\alpha\beta}\mathbf{x}_\gamma + d_{\alpha\beta}N$ for some scalars $c, d$. Taking $\langle\cdot, N\rangle$: $\langle\mathbf{x}_{\alpha\beta}, N\rangle = d_{\alpha\beta}$, i.e., $d_{\alpha\beta} = b_{\alpha\beta}$ by definition of the second fundamental form. Taking $\langle\cdot, \mathbf{x}_\mu\rangle$: $\langle\mathbf{x}_{\alpha\beta}, \mathbf{x}_\mu\rangle = c^\gamma_{\;\alpha\beta}g_{\gamma\mu} =: c_{\alpha\beta,\mu}$. From $\partial_\beta g_{\alpha\mu} = \partial_\beta\langle\mathbf{x}_\alpha, \mathbf{x}_\mu\rangle = \langle\mathbf{x}_{\alpha\beta}, \mathbf{x}_\mu\rangle + \langle\mathbf{x}_\alpha, \mathbf{x}_{\mu\beta}\rangle = c_{\alpha\beta,\mu} + c_{\mu\beta,\alpha}$, and cyclic permutations,
> > $$
> > c_{\alpha\beta,\mu} = \tfrac{1}{2}(\partial_\beta g_{\alpha\mu} + \partial_\alpha g_{\beta\mu} - \partial_\mu g_{\alpha\beta}).
> > $$
> > Raising the $\mu$ index: $c^\gamma_{\;\alpha\beta} = g^{\gamma\mu}c_{\alpha\beta,\mu} = \Gamma^\gamma_{\alpha\beta}$. Done.

> [!note]- Lemma 2: Integrability of the surface equations gives Gauss + Codazzi
> **Statement:** Differentiating the Gauss surface equation and applying $\mathbf{x}_{\alpha\beta\gamma} = \mathbf{x}_{\alpha\gamma\beta}$ yields the **Gauss equations**
> $$
> R^\tau_{\;\alpha\gamma\beta} = b^\tau_{\;\gamma}b_{\alpha\beta} - b^\tau_{\;\beta}b_{\alpha\gamma}
> $$
> and the **Codazzi equations**
> $$
> \partial_\gamma b_{\alpha\beta} - \Gamma^\tau_{\alpha\gamma}b_{\tau\beta} = \partial_\beta b_{\alpha\gamma} - \Gamma^\tau_{\alpha\beta}b_{\tau\gamma}.
> $$
>
> **Hint:** Compute $\mathbf{x}_{\alpha\beta\gamma}$ by differentiating $\mathbf{x}_{\alpha\beta} = \Gamma^\delta_{\alpha\beta}\mathbf{x}_\delta + b_{\alpha\beta}N$ with respect to $u^\gamma$, using $\mathbf{x}_{\delta\gamma}$ given by the Gauss equation again and $N_\gamma = -b^\sigma_{\;\gamma}\mathbf{x}_\sigma$ (Weingarten). Symmetrise over $\beta \leftrightarrow \gamma$; the difference must be zero. The tangential part gives the Gauss equations; the normal part gives the Codazzi equations.
>
> **Why needed:** The Gauss equations are the bridge from extrinsic ($b$) to intrinsic ($R$) — without them the Egregium has no entry point. The Codazzi equations are the second integrability condition; they constrain how $b$ changes from point to point but do not feature directly in the Egregium proof.
>
> > [!note]- Full proof (sketch)
> > Differentiate $\mathbf{x}_{\alpha\beta} = \Gamma^\delta_{\alpha\beta}\mathbf{x}_\delta + b_{\alpha\beta}N$ with respect to $u^\gamma$:
> > $$
> > \mathbf{x}_{\alpha\beta\gamma} = \partial_\gamma\Gamma^\delta_{\alpha\beta}\mathbf{x}_\delta + \Gamma^\delta_{\alpha\beta}\mathbf{x}_{\delta\gamma} + \partial_\gamma b_{\alpha\beta}N + b_{\alpha\beta}N_\gamma.
> > $$
> > Substitute $\mathbf{x}_{\delta\gamma} = \Gamma^\sigma_{\delta\gamma}\mathbf{x}_\sigma + b_{\delta\gamma}N$ (Gauss equation again) and $N_\gamma = -b^\sigma_{\;\gamma}\mathbf{x}_\sigma$ (Weingarten):
> > $$
> > \mathbf{x}_{\alpha\beta\gamma} = \big[\partial_\gamma\Gamma^\delta_{\alpha\beta} + \Gamma^\sigma_{\alpha\beta}\Gamma^\delta_{\sigma\gamma} - b_{\alpha\beta}b^\delta_{\;\gamma}\big]\mathbf{x}_\delta + \big[\Gamma^\delta_{\alpha\beta}b_{\delta\gamma} + \partial_\gamma b_{\alpha\beta}\big]N.
> > $$
> > Symmetrise: $\mathbf{x}_{\alpha\beta\gamma} - \mathbf{x}_{\alpha\gamma\beta} = 0$. The tangential part gives
> > $$
> > \partial_\gamma\Gamma^\delta_{\alpha\beta} - \partial_\beta\Gamma^\delta_{\alpha\gamma} + \Gamma^\sigma_{\alpha\beta}\Gamma^\delta_{\sigma\gamma} - \Gamma^\sigma_{\alpha\gamma}\Gamma^\delta_{\sigma\beta} = b_{\alpha\beta}b^\delta_{\;\gamma} - b_{\alpha\gamma}b^\delta_{\;\beta}.
> > $$
> > The left side is exactly $R^\delta_{\;\alpha\gamma\beta}$ (by definition of the Riemann tensor in terms of Christoffel symbols), so $R^\delta_{\;\alpha\gamma\beta} = b_{\alpha\beta}b^\delta_{\;\gamma} - b_{\alpha\gamma}b^\delta_{\;\beta}$ — the Gauss equations. The normal part gives the Codazzi equations.

> [!note]- Lemma 3: $R_{1212} = \det b_{\alpha\beta}$
> **Statement:** Lowering the upper index in the $(1, 2, 1, 2)$ component of the Gauss equation gives $R_{1212} = b_{11}b_{22} - b_{12}^2 = \det b_{\alpha\beta}$.
>
> **Hint:** Plug $\alpha = 2, \gamma = 1, \beta = 2$ into the Gauss equation; you get $R^\tau_{\;212} = b^\tau_{\;1}b_{22} - b^\tau_{\;2}b_{21}$. Take $\tau = 1$, then lower via $g_{1\sigma}$: $R_{1212} = g_{1\sigma}(b^\sigma_{\;1}b_{22} - b^\sigma_{\;2}b_{21}) = b_{11}b_{22} - b_{12}b_{21}$ (using $g_{1\sigma}b^\sigma_{\;\beta} = b_{1\beta}$). Since $b$ is symmetric ($b_{21} = b_{12}$), the result is $\det b_{\alpha\beta}$.
>
> **Why needed:** This identifies the unique non-redundant covariant component of $R$ on a $2$-manifold with $\det b$, the numerator of $K = \det b/\det g$.
>
> > [!note]- Full proof
> > From the Gauss equation $R^\tau_{\;\alpha\gamma\beta} = b^\tau_{\;\gamma}b_{\alpha\beta} - b^\tau_{\;\beta}b_{\alpha\gamma}$ with $\alpha = 2, \gamma = 1, \beta = 2$: $R^\tau_{\;212} = b^\tau_{\;1}b_{22} - b^\tau_{\;2}b_{21}$. Take $\tau = 1$ and lower: $R_{1212} = g_{1\sigma}R^\sigma_{\;212} = g_{1\sigma}(b^\sigma_{\;1}b_{22} - b^\sigma_{\;2}b_{21}) = b_{11}b_{22} - b_{12}b_{21} = b_{11}b_{22} - b_{12}^2$ since $b$ is symmetric. This equals $\det b_{\alpha\beta}$.

---

# Formal Proof

> [!note]- Complete formal proof
> Combine the three lemmas. By Lemma 1, the surface equations express $\mathbf{x}_{\alpha\beta}$ in terms of intrinsic ($\Gamma$) and extrinsic ($b$) data. By Lemma 2, the integrability $\mathbf{x}_{\alpha\beta\gamma} = \mathbf{x}_{\alpha\gamma\beta}$ forces the Gauss equations $R^\tau_{\;\alpha\gamma\beta} = b^\tau_{\;\gamma}b_{\alpha\beta} - b^\tau_{\;\beta}b_{\alpha\gamma}$. By Lemma 3, the $(1, 2, 1, 2)$ component gives $R_{1212} = \det b_{\alpha\beta}$.
>
> Dividing by $\det g_{\alpha\beta}$:
> $$
> \frac{R_{1212}}{\det g_{\alpha\beta}} = \frac{\det b_{\alpha\beta}}{\det g_{\alpha\beta}} = K,
> $$
> the Gauss curvature. The left side is *intrinsic* — $R_{1212}$ is computed from the Christoffel symbols and their derivatives, which involve only $g_{\alpha\beta}$ and its derivatives. So $K$ is intrinsic, depending only on the first fundamental form. $\square$

**Alternative proof — Cartan's method via structural equations.** Choose an orthonormal frame $(e_1, e_2)$ on $M$ with dual coframe $(\theta^1, \theta^2)$, so $\mathrm{I} = (\theta^1)^2 + (\theta^2)^2$. The Levi-Civita connection is captured by a single connection $1$-form $\omega^1_{\;2} = -\omega^2_{\;1}$ satisfying Cartan's **first structural equation**
$$
d\theta^a + \omega^a_{\;b}\wedge\theta^b = 0, \qquad a, b \in \{1, 2\},
$$
with the antisymmetry $\omega^1_{\;2} = -\omega^2_{\;1}$ ensuring metric compatibility. The **second structural equation** defines the curvature $2$-form $\Omega^a_{\;b} = d\omega^a_{\;b} + \omega^a_{\;c}\wedge\omega^c_{\;b}$. In dimension $2$, $\Omega^1_{\;2} = K\,\theta^1\wedge\theta^2$ — this *defines* $K$. Since $\omega^1_{\;2}$ is determined by the first structural equation from the metric alone (the $\theta^a$ encode the metric), $K$ is built entirely from the metric: $K\, dA = d\omega^1_{\;2}$. This is the modern, frame-theoretic proof, equivalent to the classical Gauss-equations derivation but more easily generalising to higher dimensions and to bundles.

---

# Cross-Field Exercise Suggestions

1. **Hyperbolic plane via the intrinsic formula.** The upper half-plane with metric $g = (dx^2 + dy^2)/y^2$ does not embed isometrically in $\mathbb{R}^3$ (Hilbert's theorem). Compute the Christoffel symbols $\Gamma^\gamma_{\alpha\beta}$ from the metric directly (using $\Gamma = \tfrac{1}{2}g^{-1}\partial g$), compute $R^1_{\;212}$, and verify $K = -1$ everywhere. This is the prototypical "no embedding available — use the Egregium directly" computation. **Why nonobvious:** Without the Egregium one would have no idea what the curvature of the hyperbolic plane is, because there is no embedding. The Egregium *defines* $K$ for any abstract Riemannian $2$-metric.

2. **Pseudosphere ($K = -1$) as the local hyperbolic plane.** The pseudosphere is the surface of revolution of the tractrix, embedded in $\mathbb{R}^3$ with constant Gauss curvature $K = -1$. Compute its first fundamental form, verify $K = -1$ by *both* the extrinsic formula $K = (eg_\mathrm{II} - f^2)/(EG - F^2)$ and the intrinsic formula $K = R_{1212}/\det g$, and show that they agree — the Egregium in action. **Why nonobvious:** The two formulae use completely different data ($g + b$ vs. $g$ alone) and the agreement is forced by the Gauss equations.

3. **Conformal change of metric on a surface.** For $\tilde g = e^{2u}g$ on a Riemannian $2$-manifold, derive the formula $\tilde K = e^{-2u}(K - \Delta_g u)$ (the **uniformisation equation**) using the intrinsic Egregium formula. This is a fully intrinsic computation, possible because both $K$ and $\tilde K$ are intrinsic. **Why nonobvious:** Without the Egregium, one would need a separate proof that the conformal-change formula does not see the embedding; the intrinsic formula makes this automatic.

---

# Bridges

- **To the [[Riemannian Geometry III — Riemann Curvature and Topology|Riemann curvature tensor on a general manifold]].** The Egregium identifies $K$ as the $(1, 2, 1, 2)$ component of the Riemann tensor of the surface's induced metric. On a higher-dimensional Riemannian manifold $M^n$, the Riemann tensor $R^\sigma_{\;\rho\mu\nu}$ is defined entirely intrinsically by the same formula in terms of Christoffel symbols — and *its* components are the higher-dimensional intrinsic curvatures (sectional curvatures). The whole apparatus of abstract Riemannian curvature is the higher-dimensional generalisation of the Egregium's content. The conceptual point of the Egregium — that *one* component of the Riemann tensor is intrinsic — generalises to *all* components being intrinsic, by exactly the same proof structure (intrinsic Christoffel symbols give intrinsic Riemann tensor).

- **To the [[Thm - Gauss-Bonnet Theorem for Surfaces|Gauss–Bonnet theorem]].** The Egregium makes Gauss–Bonnet *meaningful*: the integrand $K\, dA$ is a $2$-form that depends only on the intrinsic geometry, so $\int_M K\, dA$ is an intrinsic invariant of the Riemannian surface. The Gauss–Bonnet theorem then asserts that *this intrinsic integral equals a topological invariant* (the Euler characteristic). The compatibility — that an intrinsic integral equals a topological invariant — would not be statable without the Egregium first making the intrinsic version of $K$ available.

- **To the **uniformisation theorem** of Riemann surfaces (Klein–Koebe–Poincaré).** Every closed orientable Riemannian $2$-manifold is, after a conformal change of metric, of constant Gauss curvature (positive, zero, or negative according to whether the genus is $0$, $1$, or $\geq 2$ — by Gauss–Bonnet). The Egregium is what makes "Gauss curvature" a well-defined invariant *of the metric* on a closed surface, allowing the constant-curvature normalisation to make sense without an embedding. Uniformisation is then a question about the Riemannian metric alone, and its proof uses the Egregium's intrinsic curvature crucially.

- **To **general relativity** ([[General Relativity I — Einstein's Equations and Schwarzschild]]).** Einstein's gravitational field equations express the (intrinsic) Ricci curvature of a Lorentzian $4$-manifold in terms of the energy-momentum tensor. Without the Egregium-style insight that intrinsic curvature exists, one might have searched (as Einstein and Grossmann did briefly) for an embedding of spacetime into a higher-dimensional flat space — a doomed effort, since gravitating spacetime cannot be isometrically embedded with any reasonable codimension. The Egregium's lineage — that intrinsic curvature is a complete description — is the conceptual foundation for general relativity's intrinsic differential geometry.

- **To the **Gauss–Bonnet–Chern theorem** ([[Gauge Theory II — Principal Bundles, Representations, and Bundle Classification]]).** The higher-dimensional generalisation of Gauss–Bonnet uses the **Pfaffian** of the curvature $2$-form of the Levi-Civita connection on a closed even-dimensional Riemannian manifold. The whole construction is intrinsic, in the lineage of the Egregium. The Cartan-style proof of the Egregium (with $K\, dA = d\omega^1_{\;2}$) generalises directly to Chern's proof of Gauss–Bonnet–Chern: $\chi(M^{2n}) = (1/(2\pi)^n)\int_M \mathrm{Pf}(\Omega)$, where $\Omega$ is the curvature $2$-form. The surface case is $n = 1$ and the Pfaffian collapses to the single component $K$.

---

# Unlocked by This

> [!tip] Intrinsic Differential Geometry of Riemann *(from Riemannian Geometry III)*
> The Egregium is the historical and conceptual seed of all of intrinsic differential geometry. Riemann's 1854 lecture, building on the Egregium's principle, defined curvature intrinsically for $n$-dimensional manifolds via the Riemann tensor $R^\sigma_{\;\rho\mu\nu}$. Every part of modern Riemannian geometry — sectional curvature, Ricci curvature, scalar curvature, the geodesic equation, Jacobi fields, the comparison theorems — flows from the principle "curvature is intrinsic, definable from the metric alone".

> [!tip] Cartography and the Mercator Projection *(historical / applied)*
> The corollary that no plane map of the sphere can be distortion-free explains why every cartographic projection sacrifices something. The Mercator projection preserves angles but inflates polar areas; the Lambert projection preserves areas but distorts shapes; the Robinson projection compromises both. The Egregium proves all such trade-offs are necessary and quantifies them — the integrated distortion is $\int K_{\text{sphere}}\, dA - \int K_{\text{map}}\, dA = 4\pi$, fixed by topology.

> [!tip] Bonnet's Fundamental Theorem of Surface Theory *(from §4.3)*
> The converse direction: given a pair $(g_{\alpha\beta}, b_{\alpha\beta})$ satisfying the Gauss and Codazzi equations on an open set $U \subset \mathbb{R}^2$, there exists a unique (up to rigid motion) surface in $\mathbb{R}^3$ with these as its first and second fundamental forms. So the integrability conditions are necessary and sufficient — the Egregium-Gauss equation is *the* relation that any intrinsic metric must satisfy to be realised as the metric of some embedding, given a compatible $b$.

> [!tip] **Mean Curvature Flow** Preserves the Topology, Not the Intrinsic Geometry *(from Geometric Analysis)*
> Under mean curvature flow $\partial_t \mathbf{x} = HN$, the extrinsic curvature $H$ drives the evolution; the intrinsic curvature $K$ generally changes too. The Egregium is what guarantees that $K$ has an intrinsic meaning at each stage of the flow, making intrinsic estimates on $K$ a key tool in proving long-time existence and singularity formation results.
