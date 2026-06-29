---
type: definition
subject: special-relativity
prereqs:
  - "Def - Minkowski Space and the Metric"
  - "Def - Four-Vector"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$. The metric is $g$, with matrix $\eta_{\mu\nu} = \mathrm{diag}(1,-1,-1,-1)$ in an orthonormal basis and inverse matrix $\eta^{\mu\nu}$ (numerically the same diagonal matrix), satisfying $\eta^{\mu\rho}\eta_{\rho\nu} = \delta^\mu{}_\nu$. The vector space is $E$; its **dual** $E^*$ is the space of linear forms $\omega : E \to \mathbb{R}$. The action of a form on a vector is written $\langle\omega, X\rangle = \omega(X)$. Vectors carry **upper** indices $X^\mu$; forms carry **lower** indices $\omega_\mu$. Full registry on [[Special Relativity III — Minkowski Spacetime and the Metric]].

This is a compound page: it defines two interlocking notions — the **dual space** with its musical isomorphism to $E$, and the **index manipulation** (raising and lowering) that this isomorphism is, in components — because the abstract isomorphism and its concrete index form are the same fact viewed two ways.

> [!warning] Convention: signature
> We use **"mostly minus"**, $\eta = \mathrm{diag}(1,-1,-1,-1)$, so lowering an index leaves the time component unchanged and flips the spatial signs: $X_0 = X^0$, $X_i = -X^i$. Gourgoulhon's opposite signature flips the *time* component instead. The mnemonic depends on the convention; here, "time stays, space flips".

---

# Axiom Motivation

A four-vector $X^\mu$ and a linear form $\omega_\mu$ are different kinds of object: the first lives in $E$, the second in the dual space $E^*$ of linear maps $E \to \mathbb{R}$. They transform differently under a change of frame — a vector by $\Lambda$, a form by the inverse-transpose — and in a general vector space there is no canonical way to turn one into the other. The motivation for this page is that a *metric* supplies exactly such a canonical identification, and that identification is what makes the entire index calculus of relativity work.

Start with the problem the dual space solves. To extract a number from a vector $X$ in a linear, frame-independent way, you apply a *linear form*: a map $\omega : E \to \mathbb{R}$ with $\omega(\lambda X + Y) = \lambda\omega(X) + \omega(Y)$. The forms make up the dual space $E^*$, itself four-dimensional, with a **dual basis** $(e^\mu)$ defined by $\langle e^\mu, e_\nu\rangle = \delta^\mu{}_\nu$ — the form $e^\mu$ reads off the $\mu$-th component of a vector. A form $\omega = \omega_\mu e^\mu$ acts by $\langle\omega, X\rangle = \omega_\mu X^\mu$, a contraction of a lower index with an upper one. So far this needs no metric: dual spaces exist for any vector space, and the gradient of a function is naturally a form, not a vector.

Now the key question: is there a *canonical* way to associate a form to each vector? Without extra structure, no — a vector space and its dual are isomorphic (same dimension) but not *canonically* so; any isomorphism requires a choice of basis. A **non-degenerate bilinear form** removes the choice. Given the [[Def - Minkowski Space and the Metric|metric]] $g$, define $\Phi_g : E \to E^*$ by $\Phi_g(X) = g(X, \cdot)$ — the form whose action on $Y$ is $g(X,Y) = X\cdot Y$. This is linear, and it is *injective* precisely because $g$ is non-degenerate: if $\Phi_g(X) = 0$ then $g(X,Y) = 0$ for all $Y$, forcing $X = 0$. Injective between spaces of equal finite dimension means bijective, so $\Phi_g$ is an *isomorphism* — a canonical one, depending only on $g$. This is the whole point of non-degeneracy: it is exactly the condition that the metric identifies $E$ with $E^*$. (A degenerate form would have a kernel, $\Phi_g$ would not be injective, and the identification would fail — which is why the Newtonian degenerate "metric" gives no such duality and no clean index calculus.)

In components this isomorphism is **lowering an index**. The form $\Phi_g(X)$ has components $(\Phi_g(X))_\mu = g(X, e_\mu) = \eta_{\mu\nu}X^\nu =: X_\mu$. So lowering is multiplication by $\eta$, and in our signature $X_0 = \eta_{00}X^0 = X^0$ while $X_i = \eta_{ii}X^i = -X^i$ — the time component is unchanged, the spatial components flip sign. The inverse isomorphism, **raising an index**, is multiplication by the inverse matrix $\eta^{\mu\nu}$: $X^\mu = \eta^{\mu\nu}X_\nu$. The motivation for the whole apparatus is now visible: once vectors and forms are identified, the scalar product becomes a contraction, $X\cdot Y = g(X,Y) = \langle\Phi_g(X), Y\rangle = X_\mu Y^\mu$, and *every* relativistic equation can be written as a sum over indices with the contracted index appearing once up and once down — the form in which Lorentz invariance is manifest, because an up-index and a down-index transform inversely and their contraction is a scalar.

One subtlety worth flagging, because it is a common confusion. A basis $(e_\mu)$ of $E$ has two associated families of forms: the *dual basis* $(e^\mu)$ defined purely combinatorially by $\langle e^\mu, e_\nu\rangle = \delta^\mu{}_\nu$, and the *metric duals* $(\underline{e}_\mu) = \Phi_g(e_\mu)$ defined by lowering. These do **not** coincide, because $\langle\underline{e}_\mu, e_\nu\rangle = g(e_\mu,e_\nu) = \eta_{\mu\nu} \neq \delta_{\mu\nu}$ (Gourgoulhon's Remark 1.16). The dual basis is metric-free; the metric dual uses $g$. Conflating them silently drops the minus signs of $\eta$.

---

# The Definition

The **dual space** $E^*$ of [[Def - Minkowski Space and the Metric|Minkowski space's]] vector space $E$ is the space of linear forms $\omega : E \to \mathbb{R}$. For a basis $(e_\mu)$ of $E$, the **dual basis** $(e^\mu)$ of $E^*$ is defined by $\langle e^\mu, e_\nu\rangle = \delta^\mu{}_\nu$; a form is $\omega = \omega_\mu e^\mu$, and its action on a vector $X = X^\nu e_\nu$ is the contraction
$$
\langle\omega, X\rangle = \omega_\mu X^\mu.
$$

Because $g$ is **non-degenerate**, the **musical isomorphism** (metric duality)
$$
\Phi_g : E \to E^*, \qquad \Phi_g(X) = g(X, \cdot),
$$
is a vector-space isomorphism. In components it **lowers indices**: writing $X_\mu := (\Phi_g(X))_\mu$,
$$
\boxed{\ X_\mu = \eta_{\mu\nu}\,X^\nu\ } \qquad\Longrightarrow\qquad X_0 = X^0,\quad X_i = -X^i.
$$
The inverse $\Phi_g^{-1} : E^* \to E$ **raises indices** with the inverse matrix $\eta^{\mu\nu}$:
$$
\boxed{\ X^\mu = \eta^{\mu\nu}\,X_\nu\ }, \qquad \eta^{\mu\rho}\eta_{\rho\nu} = \delta^\mu{}_\nu.
$$
The two are inverse: lowering then raising returns the original, $\eta^{\mu\rho}\eta_{\rho\nu}X^\nu = X^\mu$. The maps $\flat$ (flat, lower) and $\sharp$ (sharp, raise) are the **musical isomorphisms**: $X^\flat = \Phi_g(X)$, $\omega^\sharp = \Phi_g^{-1}(\omega)$.

The scalar product is the contraction of a vector with the lowered form of another:
$$
X\cdot Y = g(X,Y) = X_\mu Y^\mu = \eta_{\mu\nu}X^\mu Y^\nu = X^0Y^0 - X^1Y^1 - X^2Y^2 - X^3Y^3.
$$
Indices may be raised and lowered on any tensor by the same rule, one $\eta$ per index; the operation commutes with contraction, and the contracted index in any scalar must appear once up and once down.

---

# Categorical / Structural Definition

The dual space $E^*$ is the **representing object for linear functionals**: it is the vector space $\mathrm{Hom}(E, \mathbb{R})$ of linear maps $E \to \mathbb{R}$, and the assignment $E \mapsto E^*$ is a contravariant functor on vector spaces (a linear map $f : E \to F$ induces $f^* : F^* \to E^*$ by precomposition). For a *finite-dimensional* space, $E$ and $E^*$ are isomorphic but not canonically — there is no natural transformation $\mathrm{id} \Rightarrow (-)^*$ — which is exactly why a *choice* (here, a metric) is needed to identify them.

The metric provides that choice as a **non-degenerate bilinear form**, equivalently an isomorphism $\Phi_g : E \xrightarrow{\sim} E^*$ that is its own "transpose" (symmetric). In the language of representations of the [[Def - The Lorentz Group|Lorentz group]], $E$ carries the defining representation and $E^*$ the dual (contragredient) representation; a generic group has these as *inequivalent* representations, but the existence of an invariant non-degenerate bilinear form $\eta$ makes them *equivalent*, and $\Phi_g$ is the intertwiner realising the equivalence. This is the representation-theoretic content of "indices can be raised and lowered": the up-index and down-index representations are isomorphic via $\eta$, so a tensor with indices in any positions is the same abstract object, with $\eta$ translating between presentations.

The musical isomorphisms $\flat, \sharp$ are the special-relativistic, flat-space case of the musical isomorphisms on a (pseudo-)Riemannian manifold, where $g$ varies from point to point and $\Phi_g$ identifies the tangent and cotangent bundles fibrewise.

---

# Relate to Other Fields / Compression

Metric duality is the **Riesz representation** of finite-dimensional pseudo-inner-product spaces: every linear functional $\omega$ is "inner product with a fixed vector", $\omega(\cdot) = g(\omega^\sharp, \cdot)$, with $\omega^\sharp$ the unique vector representing it. In a Hilbert space the Riesz theorem gives the same identification of a space with its dual via the inner product; metric duality is the algebraic, finite-dimensional, indefinite-signature version. The difference from the Hilbert case is only that the form is indefinite, so the "representing vector" of a form can be timelike, spacelike, or null.

The raising/lowering calculus is the **contravariant/covariant** bookkeeping of tensor analysis. A four-vector (upper index) is contravariant; its metric dual (lower index) is covariant; the gradient of a scalar is naturally covariant, $\partial_\mu f$, and its raised version $\partial^\mu f = \eta^{\mu\nu}\partial_\nu f$ is the contravariant gradient four-vector. The whole point is that contraction of an upper with a lower index produces a Lorentz scalar, because the two indices transform inversely.

**True name:** metric duality is *the non-degeneracy of $g$, made into a canonical isomorphism $E \cong E^*$*; in components it is *raising and lowering indices with $η$*, with the operational rule "one $\eta$ per index, contracted indices once up once down". The reflex it installs: whenever an equation's indices do not match up-and-down, lower or raise with $\eta$ until they do.

---

# Examples / Corollaries

**Is an instance — lowering a four-velocity.** For $U^\mu = (\gamma, \gamma\mathbf{v})$, the dual form has components $U_\mu = (\gamma, -\gamma\mathbf{v})$ (time unchanged, space flipped). Then $U_\mu U^\mu = \gamma^2 - \gamma^2|\mathbf{v}|^2 = \gamma^2(1 - |\mathbf{v}|^2) = 1$, the correct invariant normalisation $U\cdot U = 1$.

**Is an instance — the gradient one-form.** For a scalar field $\phi$, the gradient $\partial_\mu\phi = (\partial_t\phi, \nabla\phi)$ is naturally a *form* (lower index); its raised version $\partial^\mu\phi = \eta^{\mu\nu}\partial_\nu\phi = (\partial_t\phi, -\nabla\phi)$ is the four-vector. The wave operator $\Box = \partial_\mu\partial^\mu = \partial_t^2 - \nabla^2$ is the contraction, manifestly a scalar.

**Is NOT an instance — copying components unchanged.** Setting $X_\mu = X^\mu$ (same numbers) is *wrong* in our signature: it gives the right time component but the wrong sign on all three spatial components, since $X_i = -X^i$. The check: $X_\mu X^\mu$ computed from the wrong rule would give $(X^0)^2 + |\mathbf{X}|^2$ (Euclidean), not the correct $(X^0)^2 - |\mathbf{X}|^2 = X\cdot X$.

**Is NOT an instance — the dual basis equals the metric dual.** The dual basis $e^\mu$ (defined by $\langle e^\mu, e_\nu\rangle = \delta^\mu{}_\nu$) is *not* the metric dual $\underline{e}_\mu = \Phi_g(e_\mu)$: the latter satisfies $\langle\underline{e}_\mu, e_\nu\rangle = \eta_{\mu\nu} \neq \delta_{\mu\nu}$. They differ exactly because $\eta \neq I$ (Remark 1.16). Confusing them drops the metric.

**Corollary — raising then lowering is the identity.** $\eta_{\mu\nu}\eta^{\nu\rho}X_\rho = \delta_\mu{}^\rho X_\rho = X_\mu$: applying $\sharp$ then $\flat$ (or vice versa) returns the original, since $\eta$ and $\eta^{-1}$ are inverse. This is the calibration check that the rule is being applied correctly.

**Corollary — the scalar product is basis-independent.** $X_\mu Y^\mu = \eta_{\mu\nu}X^\mu Y^\nu$ is a contraction of an upper with a lower index, hence a Lorentz scalar, hence frame-independent — the same number in every orthonormal frame.

**Calibration check.** If you have understood the definition you can: (i) lower the index on $X^\mu = (5,3,0,0)$ to get $X_\mu = (5,-3,0,0)$ and verify $X_\mu X^\mu = 25 - 9 = 16 = X\cdot X$; (ii) explain why non-degeneracy is exactly the condition for $\Phi_g$ to be an isomorphism; (iii) distinguish the dual basis $e^\mu$ from the metric dual $\underline{e}_\mu$ and say why they differ.

---

# Unlocked by This

> [!tip] Tensors and Contraction *(from §3.3 and QFT)*
> Raising and lowering extends to tensors of any rank, one $\eta$ per index; combined with **contraction** (summing an upper against a lower index), it is the entire algebra of [[Def - Tensors on Minkowski Space|tensors on Minkowski space]]. The metric $\eta_{\mu\nu}$, the field-strength $F_{\mu\nu}$, and the energy-momentum tensor $T^{\mu\nu}$ all have their indices manipulated this way, and a Lorentz-scalar equation is one in which every free index matches and every summed index is once up, once down.

> [!tip] The Hodge Star and Differential Forms *(from Electromagnetism)*
> Metric duality on degree-one forms extends, via the [[Def - Spacetime Orientation|orientation]], to the **Hodge star** $\star$ mapping $k$-forms to $(4-k)$-forms; see [[Def - The Hodge Star]] and [[Def - Alternate Forms and the Exterior Product]]. This is what lets Maxwell's equations be written $dF = 0$, $d{\star}F = J$ — the inhomogeneous pair using the metric (through $\star$) and the homogeneous pair not — the cleanest, manifestly invariant statement of **electromagnetism**.

> [!tip] The Cotangent Bundle and the Curved Musical Isomorphisms *(from General Relativity)*
> On a curved spacetime the musical isomorphisms $\flat, \sharp$ become fibrewise maps between the tangent and cotangent bundles, with the position-dependent $g_{\mu\nu}(x)$ doing the raising and lowering at each point; see the covariant calculus of [[Special Relativity XIX — Fields on Spacetime and the Covariant Derivative]]. The flat $\eta$ of this page is the constant case, and the index gymnastics carry over unchanged, now with $g(x)$ in place of $\eta$.
