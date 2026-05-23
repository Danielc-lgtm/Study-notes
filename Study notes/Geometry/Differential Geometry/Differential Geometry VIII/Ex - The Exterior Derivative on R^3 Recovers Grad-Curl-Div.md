---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Exterior Derivative on a Manifold"
  - "Def - The Wedge Product on a Manifold"
  - "Def - Differential k-Form on a Manifold"
  - "Thm - d-Squared-is-Zero"
tags: [geometry, differential-geometry, vector-calculus]
---

# Problem Statement

Construct explicit isomorphisms between the spaces $\mathfrak{X}(\mathbb{R}^3)$ (smooth vector fields) and $\Omega^1(\mathbb{R}^3), \Omega^2(\mathbb{R}^3)$ (smooth $1$- and $2$-forms), and between $C^\infty(\mathbb{R}^3)$ and $\Omega^0(\mathbb{R}^3), \Omega^3(\mathbb{R}^3)$. Show that under these identifications, the exterior derivative $d$ in degrees $0, 1, 2$ corresponds to the vector-calculus operators $\operatorname{grad}, \operatorname{curl}, \operatorname{div}$ respectively, so the diagram
$$\begin{array}{ccccccc} C^\infty(\mathbb{R}^3) & \xrightarrow{\operatorname{grad}} & \mathfrak{X}(\mathbb{R}^3) & \xrightarrow{\operatorname{curl}} & \mathfrak{X}(\mathbb{R}^3) & \xrightarrow{\operatorname{div}} & C^\infty(\mathbb{R}^3) \\ \big\Vert & & \big\downarrow\!\flat & & \big\downarrow\!\beta & & \big\downarrow\!\alpha \\ \Omega^0(\mathbb{R}^3) & \xrightarrow{d} & \Omega^1(\mathbb{R}^3) & \xrightarrow{d} & \Omega^2(\mathbb{R}^3) & \xrightarrow{d} & \Omega^3(\mathbb{R}^3) \end{array}$$
commutes. Use the diagram to derive the identities $\operatorname{curl}(\operatorname{grad} f) = 0$ and $\operatorname{div}(\operatorname{curl} \vec F) = 0$ from $d^2 = 0$ in a single step.

**Recall:**

The exterior derivative on $\Omega^k(\mathbb{R}^3)$:
$$d\left(\sum_I \omega_I\,dx^I\right) = \sum_I d\omega_I \wedge dx^I, \qquad d\omega_I = \sum_j(\partial_j \omega_I)\,dx^j.$$

The gradient, curl, and divergence on $\mathbb{R}^3$ (for vector field $\vec F = (P, Q, R)$ and function $f$):
$$\operatorname{grad} f = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}\right),$$
$$\operatorname{curl}\vec F = \left(\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z}, \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x}, \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right),$$
$$\operatorname{div}\vec F = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}.$$

The musical map $\flat : \mathfrak{X}(\mathbb{R}^3) \to \Omega^1(\mathbb{R}^3)$ is defined via the Euclidean metric: $\flat(\vec F)(\vec G) = \vec F \cdot \vec G$, i.e., $\flat(P, Q, R) = P\,dx + Q\,dy + R\,dz$.

The map $\beta : \mathfrak{X}(\mathbb{R}^3) \to \Omega^2(\mathbb{R}^3)$ is defined by $\beta(\vec F) = \iota_{\vec F}(dx \wedge dy \wedge dz)$, i.e., $\beta(P, Q, R) = P\,dy \wedge dz + Q\,dz \wedge dx + R\,dx \wedge dy$.

The map $\alpha : C^\infty(\mathbb{R}^3) \to \Omega^3(\mathbb{R}^3)$ is $\alpha(f) = f\,dx \wedge dy \wedge dz$.

---

# Convergent Strategy

**Problem class:** This is an "identify a known operator via its action on basis vectors" problem, specialized to dimension $3$ where each space $\Omega^k(\mathbb{R}^3)$ has the right dimension to be identified with a vector field or function. The route is to compute $d$ explicitly on a basis-form representative of each degree and read off the result in vector-calculus language.

**Assumption pattern:** The structure given is $\mathbb{R}^3$ with its standard Euclidean metric — needed to define $\flat$ and to identify $\beta$'s output as having the orientation of $\operatorname{curl}$. The forms are written in standard coordinates $(x, y, z)$. The dimensions $\binom{3}{0} = \binom{3}{3} = 1$ and $\binom{3}{1} = \binom{3}{2} = 3$ are what allow all six spaces to be identified with vector-field-like or function-like objects.

**Theorem routing:** The route is the [[Thm - Coordinate Expression for the Exterior Derivative|chart formula for d]] applied to each basic form $dx^j$ and $dx^i \wedge dx^j$ in turn. Each output is reduced to standard form by collecting terms using the wedge anticommutativity. The result is compared to the explicit formulas for $\operatorname{grad}, \operatorname{curl}, \operatorname{div}$.

**Key decision point:** The non-obvious step is recognizing which sign convention to use for the maps $\flat, \beta, \alpha$. The standard choice — with $\beta(\vec F) = \iota_{\vec F}(dx \wedge dy \wedge dz)$ rather than $\flat \circ (\star\text{-isomorphism})$ — is what makes the diagram commute *without* extra signs. With the "wrong" sign convention, one gets curl with reversed sign, which would muddle the connection to physics; the chosen convention reproduces standard vector calculus.

---

# Legal Operations Used

1. **Expand a form in coordinates and apply $d$ mechanically** (operation 1 from the topic page). The whole exercise is mechanical application of this operation, with attention to the wedge signs.

2. **Convert grad/curl/div to $d$ to access higher-dimensional identities** (operation 8). Once the diagram is established, the vector-calculus identities are corollaries of $d^2 = 0$.

3. **Use the wedge as a determinant** (operation 9). The map $\beta(\vec F) = \iota_{\vec F}(dx \wedge dy \wedge dz)$ expands via the cofactor formula for the determinant, which is what produces the curl-style components.

---

# Hints

> [!note]- Hint 1
> Compute $df$ for a function $f$ explicitly: $df = (\partial f/\partial x)\,dx + (\partial f/\partial y)\,dy + (\partial f/\partial z)\,dz$. Compare with the components of $\operatorname{grad} f$.

> [!note]- Hint 2
> For a $1$-form $\omega = P\,dx + Q\,dy + R\,dz$, expand $d\omega = dP \wedge dx + dQ \wedge dy + dR \wedge dz$ and collect terms by the basic $2$-form $dy\wedge dz, dz\wedge dx, dx\wedge dy$. Compare with the components of $\operatorname{curl}\vec F$.

> [!note]- Hint 3
> For a $2$-form $\omega = P\,dy\wedge dz + Q\,dz\wedge dx + R\,dx\wedge dy$, expand $d\omega$ and collect into $dx\wedge dy\wedge dz$. The coefficient should be the divergence.

> [!note]- Hint 4
> Once the diagram commutes, $d^2 = 0$ on $\Omega^0$ becomes $\operatorname{curl}\operatorname{grad} = 0$, and $d^2 = 0$ on $\Omega^1$ becomes $\operatorname{div}\operatorname{curl} = 0$. Verify the chain.

---

# Solution

The proof breaks into three computational steps, one for each degree. Step 1 verifies $d \circ \operatorname{id} = \flat \circ \operatorname{grad}$ on $\Omega^0$, by computing $df$ explicitly. Step 2 verifies $d \circ \flat = \beta \circ \operatorname{curl}$ on $\Omega^1$. Step 3 verifies $d \circ \beta = \alpha \circ \operatorname{div}$ on $\Omega^2$. The diagram then commutes, and the vector-calculus identities follow from $d^2 = 0$ in a single application.

**Step 1: $d$ on $\Omega^0$ recovers the gradient.**

For $f \in C^\infty(\mathbb{R}^3)$, $df = (\partial_x f)\,dx + (\partial_y f)\,dy + (\partial_z f)\,dz$. The components are exactly $\operatorname{grad} f$. Under $\flat$, the gradient vector $(\partial_x f, \partial_y f, \partial_z f)$ corresponds to the $1$-form $(\partial_x f)\,dx + (\partial_y f)\,dy + (\partial_z f)\,dz = df$. So $df = \flat(\operatorname{grad} f)$.

> [!note]- Derivation
> $df = \sum_j (\partial_j f)\,dx^j$ by the chart formula for $d$. In coordinates $(x, y, z)$ on $\mathbb{R}^3$, this is $(\partial_x f)\,dx + (\partial_y f)\,dy + (\partial_z f)\,dz$. The components $(\partial_x f, \partial_y f, \partial_z f)$ are the components of $\nabla f$. Under the musical isomorphism $\flat$ (which sends a vector $(P, Q, R)$ to the $1$-form $P\,dx + Q\,dy + R\,dz$), the gradient becomes $df$. So the diagram commutes in degree $0$.

**Step 2: $d$ on $\Omega^1$ recovers the curl.**

For $\omega = P\,dx + Q\,dy + R\,dz \in \Omega^1$, computing $d\omega$ via the chart formula and collecting into basic $2$-forms gives
$$d\omega = (\partial_y R - \partial_z Q)\,dy \wedge dz + (\partial_z P - \partial_x R)\,dz \wedge dx + (\partial_x Q - \partial_y P)\,dx \wedge dy.$$
The coefficient triple is $\operatorname{curl}(P, Q, R)$. Applying $\beta^{-1}$ — which sends $A\,dy\wedge dz + B\,dz \wedge dx + C\,dx \wedge dy$ to the vector $(A, B, C)$ — gives back the curl vector. So $d \circ \flat = \beta \circ \operatorname{curl}$.

> [!note]- Derivation
> Expand $d\omega = dP \wedge dx + dQ \wedge dy + dR \wedge dz$. Each $dP, dQ, dR$ is a $1$-form: $dP = (\partial_x P)\,dx + (\partial_y P)\,dy + (\partial_z P)\,dz$, etc.
>
> Compute $dP \wedge dx$: $(\partial_x P)\,dx \wedge dx + (\partial_y P)\,dy \wedge dx + (\partial_z P)\,dz \wedge dx = -(\partial_y P)\,dx \wedge dy - (\partial_z P)\,dx \wedge dz$ (using $dx \wedge dx = 0$ and $dy \wedge dx = -dx \wedge dy$).
>
> Similarly $dQ \wedge dy = (\partial_x Q)\,dx \wedge dy - (\partial_z Q)\,dy \wedge dz$ and $dR \wedge dz = (\partial_x R)\,dx \wedge dz + (\partial_y R)\,dy \wedge dz$ (after sign normalization to increasing multi-indices).
>
> Wait, let me be more careful. $dR \wedge dz = (\partial_x R)\,dx \wedge dz + (\partial_y R)\,dy \wedge dz + (\partial_z R)\,dz \wedge dz = (\partial_x R)\,dx \wedge dz + (\partial_y R)\,dy \wedge dz$. To normalize, $dx \wedge dz = -dz \wedge dx$.
>
> Summing all three:
> $d\omega = -(\partial_y P)\,dx \wedge dy - (\partial_z P)\,dx \wedge dz + (\partial_x Q)\,dx \wedge dy - (\partial_z Q)\,dy \wedge dz + (\partial_x R)\,dx \wedge dz + (\partial_y R)\,dy \wedge dz$.
>
> Collect by basis: 
> - $dy \wedge dz$: $(\partial_y R - \partial_z Q)$.
> - $dx \wedge dz = -dz \wedge dx$: $(\partial_x R - \partial_z P)$, equivalently $dz \wedge dx$ has coefficient $-(∂_x R - ∂_z P) = (∂_z P - ∂_x R)$.
> - $dx \wedge dy$: $(\partial_x Q - \partial_y P)$.
>
> So $d\omega = (∂_y R - ∂_z Q)\,dy\wedge dz + (∂_z P - ∂_x R)\,dz\wedge dx + (∂_x Q - ∂_y P)\,dx\wedge dy$. The components match the curl exactly. Applying $\beta^{-1}$, we get the curl vector $((∂_y R - ∂_z Q), (∂_z P - ∂_x R), (∂_x Q - ∂_y P))$.

**Step 3: $d$ on $\Omega^2$ recovers the divergence.**

For $\eta = P\,dy\wedge dz + Q\,dz\wedge dx + R\,dx\wedge dy \in \Omega^2$, computing $d\eta$ gives
$$d\eta = (\partial_x P + \partial_y Q + \partial_z R)\,dx \wedge dy \wedge dz = (\operatorname{div}(P, Q, R))\,dx \wedge dy \wedge dz.$$
Under $\alpha$ (which sends a function $h$ to the $3$-form $h\,dx \wedge dy \wedge dz$), the divergence is identified with $d\eta$. So $d \circ \beta = \alpha \circ \operatorname{div}$.

> [!note]- Derivation
> Expand $d\eta = dP \wedge dy \wedge dz + dQ \wedge dz \wedge dx + dR \wedge dx \wedge dy$.
>
> $dP \wedge dy \wedge dz$: the only non-vanishing contribution comes from $(\partial_x P)\,dx$, since $dy \wedge dy \wedge dz = 0$ and $dz \wedge dy \wedge dz = 0$. So $dP \wedge dy \wedge dz = (\partial_x P)\,dx \wedge dy \wedge dz$.
>
> $dQ \wedge dz \wedge dx$: only the $(\partial_y Q)\,dy$ term survives, giving $(\partial_y Q)\,dy \wedge dz \wedge dx = (\partial_y Q)\,dx \wedge dy \wedge dz$ (since $dy \wedge dz \wedge dx = dx \wedge dy \wedge dz$ — cyclic permutation, two swaps).
>
> $dR \wedge dx \wedge dy$: only the $(\partial_z R)\,dz$ term, giving $(\partial_z R)\,dz \wedge dx \wedge dy = (\partial_z R)\,dx \wedge dy \wedge dz$ (cyclic permutation).
>
> Summing: $d\eta = (\partial_x P + \partial_y Q + \partial_z R)\,dx \wedge dy \wedge dz$. The coefficient is $\operatorname{div}(P, Q, R)$.

**Conclusion: the diagram commutes.**

The three steps verify that $d$ in each degree corresponds to the appropriate vector-calculus operator under the identifications $\flat, \beta, \alpha$.

**Corollary: $\operatorname{curl}\operatorname{grad} = 0$ and $\operatorname{div}\operatorname{curl} = 0$.**

$d^2 = 0$ applied to a $0$-form $f$ gives $d(df) = 0$, which under the identifications $\flat, \beta$ becomes $\beta(\operatorname{curl}\operatorname{grad} f) = 0$, hence $\operatorname{curl}\operatorname{grad} f = 0$ (since $\beta$ is an isomorphism). Similarly $d^2 = 0$ on a $1$-form $\omega = \flat(\vec F)$ gives $d(d\omega) = 0$, equivalently $\alpha(\operatorname{div}\operatorname{curl}\vec F) = 0$, hence $\operatorname{div}\operatorname{curl}\vec F = 0$.

> [!note]- Complete formal solution
> **The maps.** Define the isomorphisms $\flat : \mathfrak{X}(\mathbb{R}^3) \to \Omega^1(\mathbb{R}^3)$, $\beta : \mathfrak{X}(\mathbb{R}^3) \to \Omega^2(\mathbb{R}^3)$, and $\alpha : C^\infty(\mathbb{R}^3) \to \Omega^3(\mathbb{R}^3)$:
> $$\flat(P, Q, R) = P\,dx + Q\,dy + R\,dz,$$
> $$\beta(P, Q, R) = P\,dy \wedge dz + Q\,dz \wedge dx + R\,dx \wedge dy,$$
> $$\alpha(f) = f\,dx \wedge dy \wedge dz.$$
> All three are $C^\infty(\mathbb{R}^3)$-linear isomorphisms.
>
> **Compute $d$ on each degree.**
>
> $d$ on $\Omega^0$: $df = (\partial_x f)\,dx + (\partial_y f)\,dy + (\partial_z f)\,dz = \flat(\operatorname{grad} f)$.
>
> $d$ on $\Omega^1$: for $\omega = P\,dx + Q\,dy + R\,dz$, expanding $d\omega = dP\wedge dx + dQ\wedge dy + dR\wedge dz$ and collecting into the basic $2$-form basis gives $d\omega = (∂_y R - ∂_z Q)\,dy\wedge dz + (∂_z P - ∂_x R)\,dz\wedge dx + (∂_x Q - ∂_y P)\,dx\wedge dy = \beta(\operatorname{curl}(P, Q, R))$.
>
> $d$ on $\Omega^2$: for $\eta = P\,dy\wedge dz + Q\,dz\wedge dx + R\,dx\wedge dy$, expanding $d\eta = dP\wedge dy\wedge dz + dQ\wedge dz\wedge dx + dR\wedge dx\wedge dy$ and collecting gives $d\eta = (∂_x P + ∂_y Q + ∂_z R)\,dx\wedge dy\wedge dz = \alpha(\operatorname{div}(P, Q, R))$.
>
> **Diagram commutes.** Each of the three computations is a verification that $d$ on the form side equals the appropriate vector-calculus operator on the vector-field side.
>
> **Identity corollaries.** $d^2 = 0$ on $\Omega^0$: $d(df) = 0 \Leftrightarrow d(\flat(\operatorname{grad} f)) = 0 \Leftrightarrow \beta(\operatorname{curl}\operatorname{grad} f) = 0 \Leftrightarrow \operatorname{curl}\operatorname{grad} f = 0$. $d^2 = 0$ on $\Omega^1$: $d(d\omega) = 0 \Leftrightarrow d(\beta(\operatorname{curl}\vec F)) = 0 \Leftrightarrow \alpha(\operatorname{div}\operatorname{curl}\vec F) = 0 \Leftrightarrow \operatorname{div}\operatorname{curl}\vec F = 0$ (for $\omega = \flat(\vec F)$).
>
> $\blacksquare$

> [!warning] Illegal but tempting alternative route
> One might be tempted to define $\beta(\vec F)$ as the $\flat$-image, "by analogy with $\flat$ on $1$-forms". But $\flat$ is a metric-and-degree-specific isomorphism, not a universal device, and $\flat(\vec F)$ would be a $1$-form, not a $2$-form. The correct definition uses the volume form contracted with $\vec F$ — equivalently, the Hodge star $\star\flat$ — which is what gives a $2$-form whose components are the curl-style cyclic combinations.

---

# Key Takeaways

**Vector calculus on $\mathbb{R}^3$ is a special case of the calculus of forms in disguise.** The three "different" operators $\operatorname{grad}, \operatorname{curl}, \operatorname{div}$ are not three separate things — they are the *one* exterior derivative $d$ acting in degrees $0, 1, 2$ respectively. The reason the operators look different in classical vector calculus is the coincidence $\binom{3}{1} = \binom{3}{2} = 3$, which lets $1$-forms and $2$-forms both be disguised as vector fields under the metric identification. In any other dimension, the disguise fails. The lesson for problem-solving: when a vector-calculus identity needs proving in $\mathbb{R}^n$ for $n \neq 3$, translate to forms and reduce to graded Leibniz or $d^2 = 0$ — the result will be true automatically. The trigger pattern is "a derivative-of-a-derivative-of-something" or "a product rule on a derivative" — both have one-line proofs in the form language and dimension-$n$ generalizations that are otherwise inaccessible.

**$d^2 = 0$ is the single identity behind every vector-calculus chain-of-derivatives identity.** $\operatorname{curl}\operatorname{grad} = 0$ and $\operatorname{div}\operatorname{curl} = 0$ are two faces of the same fact: the de Rham complex is a *complex*, so $d \circ d = 0$. The exterior derivative does not see the distinction between "curl" and "div" — there is just $d$, and the composition $d^2$ is always zero. The same identity in higher dimensions gives chain identities for higher-degree wedge products, all derivable by one application of $d^2 = 0$ plus the appropriate musical identifications. When in vector calculus you see "derivative of derivative of something is zero", the underlying mechanism is always $d^2 = 0$, and tracing the mechanism is a one-line exercise.

**The maps $\flat, \beta, \alpha$ are metric-dependent identifications, and changing the metric changes the identifications.** On $\mathbb{R}^3$ with the standard Euclidean metric, the musical isomorphisms are determined; on a general Riemannian $3$-manifold, the analogous identifications still exist but depend on the metric. The vector-calculus operators $\operatorname{grad}, \operatorname{curl}, \operatorname{div}$ are *not* metric-free: they implicitly use the metric to identify vector fields with covectors and $2$-forms. By contrast, $d$ is metric-free — it depends only on the smooth structure of the manifold. This is why the form description is more fundamental: it isolates the genuinely topological/smooth content (the operator $d$, the cohomology $H^k_{dR}$) from the metric-dependent identification (the musical map, the Hodge star).

**On $\mathbb{R}^3$, the cohomology of the de Rham complex is zero in positive degrees** because $\mathbb{R}^3$ is contractible. So *every* closed $1$-form on $\mathbb{R}^3$ is exact (every curl-free vector field is a gradient — i.e., conservative), and every closed $2$-form is exact (every divergence-free vector field is a curl). The translation: in $\mathbb{R}^3$, the converse-to-the-identities holds — if $\operatorname{curl}\vec F = 0$, then $\vec F = \operatorname{grad} f$; if $\operatorname{div}\vec G = 0$, then $\vec G = \operatorname{curl}\vec H$. On non-contractible regions (like the punctured plane or punctured space), the converse can fail, and the failure is measured by de Rham cohomology — this is the prototype of the closed-but-not-exact phenomenon. See [[Ex - A Form that is Closed but Not Exact on the Punctured Plane]].
