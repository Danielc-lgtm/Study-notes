---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Differential k-Form on a Manifold"
  - "Def - The Wedge Product on a Manifold"
  - "Def - Exterior Derivative on a Manifold"
  - "Def - Interior Product (Contraction with a Vector Field)"
  - "Def - Lie Derivative of a Differential Form"
  - "Def - Volume Form"
tags: [geometry, differential-geometry, vector-calculus, dictionary]
---

# Notation

This page is a reference card on the manifold $\mathbb{R}^3$ with the standard Euclidean metric, standard orientation $dx \wedge dy \wedge dz$, and the **musical isomorphisms** $\flat : TM \to T^*M$ and $\sharp : T^*M \to TM$ supplied by the metric. The dictionary survives unchanged on any oriented Riemannian $3$-manifold; the only thing that depends on the metric is the conversion between vectors and $1$-forms, and the only thing that depends on the orientation is the conversion between $2$-forms / $3$-forms and vectors / scalars via the Hodge star $\star$. Throughout, $f, g \in C^\infty(\mathbb{R}^3)$ are scalar fields and $\vec u, \vec v, \vec F, \vec G \in \mathfrak{X}(\mathbb{R}^3)$ are vector fields, written $\vec F = F^1 \partial_x + F^2 \partial_y + F^3 \partial_z$.

- $\vec F^\flat = F^1\,dx + F^2\,dy + F^3\,dz$ — the metric dual of $\vec F$, a $1$-form.
- $\star\vec F^\flat = F^1\,dy\wedge dz + F^2\,dz\wedge dx + F^3\,dx\wedge dy$ — the $2$-form Hodge-dual to the $1$-form $\vec F^\flat$; this is the "flux" $2$-form of $\vec F$.
- $f\,dV = f\,dx\wedge dy\wedge dz$ — the "scalar density" $3$-form associated with $f$.
- $\nabla f$, $\nabla\times\vec F$, $\nabla\cdot\vec F$ — gradient, curl, divergence in the classical notation.
- $d$ — the [[Def - Exterior Derivative on a Manifold|exterior derivative]]; $\iota_X = X \lrcorner$ — the [[Def - Interior Product (Contraction with a Vector Field)|interior product]]; $\mathcal{L}_X$ — the [[Def - Lie Derivative of a Differential Form|Lie derivative]]; $\wedge$ — the [[Def - The Wedge Product on a Manifold|wedge product]]; $\star$ — the **Hodge star** (built later in [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]]). The full notation registry is in [[Differential Geometry VIII — Differential Forms]].

> [!warning] Convention
> Frankel uses the determinant convention $\omega \wedge \eta$ throughout — the same convention used in [[Differential Geometry VIII — Differential Forms]]. The dictionary entries below are written in this convention. Sources using the Alt convention pick up combinatorial $k!\,\ell!/(k+\ell)!$ factors in some wedge formulas; the underlying identifications are unchanged.

---

# Axiom Motivation

The dictionary exists because the calculus of $\mathbb{R}^3$ that you learned in multivariable calculus — gradient, curl, divergence, the cross product, the various Stokes-type theorems — is *not* an accident of three dimensions. It is the shadow cast on the small case $n = 3$ by a single set of operations on differential forms that work in every dimension and on every manifold. Once you accept that this shadow exists, the question becomes: which operation on forms is gradient, which is curl, which is divergence? The dictionary answers this question, and it makes the entire structure of $\mathbb{R}^3$ vector calculus transparent rather than mysterious.

The reason the dictionary is needed *at all* is that the classical formulas package two different kinds of information together. The gradient $\nabla f$ is built from $df$ and the metric: $df$ is intrinsically a $1$-form, but the gradient is a vector, so the conversion uses $\sharp$. The curl $\nabla\times\vec F$ is built from $d$ applied to a $1$-form (giving a $2$-form) and then converted back to a vector via $\star$ and $\sharp$. The divergence $\nabla\cdot\vec F$ is built from $d$ applied to a $2$-form (giving a $3$-form) and then converted to a scalar via $\star$. Each classical operation is a *composition* of (i) a metric-dependent lowering or raising step, (ii) an intrinsic exterior derivative, and (iii) a metric-and-orientation-dependent Hodge step. The classical notation hides the composition; the dictionary makes it visible.

The payoff of making the dictionary visible is that the *failures* of classical vector calculus to generalize become transparent. The cross product is a special $3$-dimensional accident — it identifies $\Lambda^2(\mathbb{R}^3)^* \cong \mathbb{R}^3$ using the Hodge star, but in dimension $4$ a $2$-form has $\binom{4}{2} = 6$ independent components and cannot be a vector. The curl of a vector field exists in $\mathbb{R}^3$ but not in $\mathbb{R}^4$; what exists in every dimension is $d$ acting on $1$-forms, and that operation always produces a $2$-form. The identities $\nabla\times\nabla f = 0$ and $\nabla\cdot(\nabla\times\vec F) = 0$ are the two cases of $d^2 = 0$, and they generalize because $d^2 = 0$ generalizes. The dictionary is what lets you see "vector calculus is a 3-dimensional special case of $d, \wedge, \iota_X, \mathcal{L}_X, \star$" rather than a body of disconnected identities.

A second motivation is **operational**. When solving a problem on $\mathbb{R}^3$ — Maxwell's equations, fluid mechanics, an electromagnetic boundary value problem — you typically work in the classical language because the formulas are familiar. The dictionary lets you translate the problem into the forms language to use the cleaner machinery (intrinsic, coordinate-free, metric-free for $d$, naturally compatible with Stokes's theorem in every dimension), then translate the answer back. The form-language proof of "curl of grad is zero" is one symbol; the form-language statement of Maxwell's equations is one line; the form-language change-of-variables formula has no $|\det|$ in it. Working in the right language saves bookkeeping.

The dictionary is not unique: there are choices to make. Should a vector field be sent to a $1$-form (via $\flat$) or a $2$-form (via $\iota_{\vec F}\,dV$)? The answer is *both*, and they are dual to each other under $\star$: the same vector field has a "circulation" $1$-form $\vec F^\flat$ and a "flux" $2$-form $\star\vec F^\flat = \iota_{\vec F}\,dV$. Line integrals pair with the first, surface integrals with the second. The dictionary distinguishes the two, and this is exactly where the apparently arbitrary distinction between "first kind" and "second kind" integrals in physics comes from.

---

# The Definition

The **Frankel dictionary** is the following identification between operations on scalar and vector fields on oriented Riemannian $\mathbb{R}^3$ and operations on differential forms in $\Omega^\bullet(\mathbb{R}^3)$.

**Objects (the four kinds of fields).**

| Form degree | Form type | Vector-calculus object | Conversion |
|---|---|---|---|
| $0$ | function $f$ | scalar field $f$ | identity |
| $1$ | $1$-form $\omega = F^i\,dx^i$ | vector field $\vec F$ ("circulation" view) | $\omega = \vec F^\flat$, $\vec F = \omega^\sharp$ |
| $2$ | $2$-form $\beta$ | vector field $\vec F$ ("flux" view) | $\beta = \iota_{\vec F}\,dV = \star\vec F^\flat$ |
| $3$ | $3$-form $f\,dV$ | scalar field $f$ ("density" view) | $f\,dV = \star f$ |

In coordinates, $\vec F = F^1\partial_x + F^2\partial_y + F^3\partial_z$ corresponds to $\vec F^\flat = F^1\,dx + F^2\,dy + F^3\,dz$ (the "circulation" $1$-form) and to $\star\vec F^\flat = F^1\,dy\wedge dz + F^2\,dz\wedge dx + F^3\,dx\wedge dy$ (the "flux" $2$-form). Both correspondences are bijections, and they swap under the Hodge star.

**Operations (the three classical differential operators).**

| Classical operator | Form-language formula | Note |
|---|---|---|
| $\nabla f$ (gradient) | $(\nabla f)^\flat = df$, so $\nabla f = (df)^\sharp$ | $d$ on a $0$-form |
| $\nabla\times\vec F$ (curl) | $(\nabla\times\vec F)^\flat = \star\,d(\vec F^\flat)$ | $d$ on a $1$-form, then $\star$ |
| $\nabla\cdot\vec F$ (divergence) | $(\nabla\cdot\vec F)\,dV = d(\iota_{\vec F}\,dV) = d(\star\vec F^\flat)$ | $d$ on a $2$-form |

The single operation behind all three is the **exterior derivative** $d$. The three classical operators are $d$ applied to $0$-forms, to $1$-forms, and to $2$-forms respectively, with the lower/upper musical isomorphisms and the Hodge star handling the conversions between the form world and the vector/scalar world.

**Cross product.**

For vectors $\vec u, \vec v \in T_p\mathbb{R}^3$,
$$(\vec u \times \vec v)^\flat = \star(\vec u^\flat \wedge \vec v^\flat).$$
Equivalently, the cross product is the Hodge-dual of the wedge of two $1$-forms, identifying $\Lambda^2(\mathbb{R}^3)^*$ with $(\mathbb{R}^3)^*$ via $\star$, and then converting back to a vector via $\sharp$. This identification works *only* in dimension $3$, because only there does $\binom{n}{2} = n$.

**Triple product.**

$$\vec u \cdot (\vec v \times \vec w) = \star(\vec u^\flat \wedge \vec v^\flat \wedge \vec w^\flat) = \det\begin{pmatrix} u^1 & v^1 & w^1 \\ u^2 & v^2 & w^2 \\ u^3 & v^3 & w^3 \end{pmatrix}.$$

The triple product is just the volume $3$-form evaluated on the three vectors — exactly the determinant identity for forms in the [[Def - Alternating Tensor and Lambda k V Dual|alternating-tensor]] formulation.

**Interior product and dot product.**

$$\iota_{\vec u}\vec v^\flat = \vec u \cdot \vec v.$$

The interior product of the $1$-form $\vec v^\flat$ with the vector field $\vec u$ is exactly the dot product, as expected from $\iota_X(F^i\,dx^i)(Y) = F^i\,dx^i(X)\,Y$ specializing on a single argument.

**Lie derivative and the convective derivative.**

For a scalar field $f$, $\mathcal{L}_{\vec u} f = \vec u \cdot \nabla f$ — the classical **convective** or **material** derivative of fluid mechanics. For a vector field $\vec v$, $\mathcal{L}_{\vec u}\vec v = [\vec u, \vec v]$ is the Lie bracket, which in Cartesian coordinates reads $(\vec u \cdot \nabla)\vec v - (\vec v \cdot \nabla)\vec u$. The form $\mathcal{L}_{\vec u}\vec v = (\vec u \cdot \nabla)\vec v - (\vec v \cdot \nabla)\vec u$ is sometimes itself called "Lie derivative" in fluid-mechanics texts.

**The four classical identities are $d^2 = 0$ and one wedge identity.**

| Classical | Form-language |
|---|---|
| $\nabla\times\nabla f = 0$ | $d(df) = 0$ |
| $\nabla\cdot(\nabla\times\vec F) = 0$ | $d(d(\vec F^\flat)) = 0$ (after applying $\star$ and translating) |
| $\nabla\cdot(f\vec F) = (\nabla f)\cdot\vec F + f\nabla\cdot\vec F$ | $d(f\beta) = df\wedge\beta + f\,d\beta$ for $\beta = \iota_{\vec F}\,dV$ |
| $\nabla\times(f\vec F) = \nabla f\times\vec F + f\nabla\times\vec F$ | $d(f\omega) = df\wedge\omega + f\,d\omega$ for $\omega = \vec F^\flat$ |

The first two are the two cases of $d^2 = 0$. The second two are the Leibniz rule for $d$ applied to forms of degrees $2$ and $1$.

**The classical Stokes theorems are all instances of one statement.**

For an oriented compact submanifold with boundary,
$$\int_{\partial M}\omega = \int_M d\omega \qquad ([[Thm - Stokes' Theorem on Manifolds]]).$$
Specializing to $\mathbb{R}^3$:

| $\dim M$ | $\omega$ | Specialization |
|---|---|---|
| $1$ | $f$ ($0$-form) | $\int_a^b df = f(b) - f(a)$ — Fundamental Theorem of Calculus |
| $2$ in $\mathbb{R}^2$ | $P\,dx + Q\,dy$ ($1$-form) | Green's theorem |
| $2$ in $\mathbb{R}^3$ | $\vec F^\flat$ ($1$-form on a surface) | **Kelvin–Stokes**: $\oint \vec F\cdot d\vec\ell = \iint (\nabla\times\vec F)\cdot d\vec A$ |
| $3$ in $\mathbb{R}^3$ | $\iota_{\vec F}\,dV$ ($2$-form) | **Divergence theorem**: $\iint \vec F\cdot d\vec A = \iiint \nabla\cdot\vec F\,dV$ |

All four are the same theorem written in different dimensional guises.

---

# Relate to Other Fields / Compression

**True name.** The dictionary's true name is *"vector calculus on $\mathbb{R}^3$ is $d : \Omega^0 \to \Omega^1 \to \Omega^2 \to \Omega^3$, with the metric and orientation supplying the conversions to scalars and vectors."* Internalize this and you stop memorizing identities — every classical formula is a consequence of $d^2 = 0$ plus the graded Leibniz rule, translated by the dictionary. The bridge to higher dimensions is immediate: in $\mathbb{R}^n$, $d$ still exists, but a $2$-form is no longer dual to a vector (it has $\binom{n}{2}$ components), so the curl becomes the bilinear "tensor" version $dF$ where $F = \vec F^\flat$, and the divergence becomes $d\star F$ — both of which generalize without trouble. The cross product does not generalize, and the dictionary makes the obstruction quantitative: it would require $\binom{n}{2} = n$, which forces $n = 3$.

**Maxwell as the test case.** The dictionary's worth is most visible in Maxwell's equations. In Cartesian language, Maxwell's four equations are an apparently unrelated jumble — two are "div" equations and two are "curl" equations, two involve $\vec E$ and two involve $\vec B$, and the time derivatives are scattered. In the form language on Minkowski space $\mathbb{R}^{1,3}$, the Faraday $2$-form $F = -E_i\,dt\wedge dx^i + \tfrac{1}{2}\epsilon_{ijk}B^k\,dx^i\wedge dx^j$ packages $\vec E$ and $\vec B$ into one object, and the four equations are *two equations*: $dF = 0$ (the Bianchi identity, which packages Faraday's law and the source-free divergence of $\vec B$) and $d\star F = J$ (which packages the inhomogeneous equations). This is the dictionary at its most dramatic — a four-equation system collapses to two equations once you stop fighting the geometry. The full statement is in [[Ex - Maxwell's Equations as Two Form Equations on Minkowski Space]].

**$d^2 = 0$ subsumes two classical identities.** The single intrinsic fact $d^2 = 0$ on a manifold contains both $\nabla\times\nabla f = 0$ (read $d^2$ acting on a $0$-form, then translate) and $\nabla\cdot(\nabla\times\vec F) = 0$ (read $d^2$ acting on a $1$-form, then translate). These two identities, which look like distinct lucky cancellations in classical notation, are *the same identity* — the operator $d$ satisfies $d^2 = 0$, and the dictionary makes this single identity visible as two classical formulas because the two intermediate spaces ($1$-forms / vector fields, $2$-forms / vector fields) accidentally coincide in dimension three.

---

# Examples / Corollaries

**Gradient in coordinates is the formula for $d$ on a function.** Given $f \in C^\infty(\mathbb{R}^3)$, the exterior derivative is $df = \partial_x f\,dx + \partial_y f\,dy + \partial_z f\,dz$. Applying $\sharp$ (which on $\mathbb{R}^3$ replaces $dx^i$ by $\partial_{x^i}$) gives $\nabla f = \partial_x f\,\partial_x + \partial_y f\,\partial_y + \partial_z f\,\partial_z$ — the classical gradient. The conversion is literally "raise the indices using the Euclidean metric," and on Euclidean space the metric is the identity so the formula is unchanged.

**Curl in coordinates emerges from $d$ on a $1$-form.** For $\omega = P\,dx + Q\,dy + R\,dz = \vec F^\flat$, the exterior derivative is $d\omega = (\partial_y R - \partial_z Q)\,dy\wedge dz + (\partial_z P - \partial_x R)\,dz\wedge dx + (\partial_x Q - \partial_y P)\,dx\wedge dy$. Translating each $dy\wedge dz, dz\wedge dx, dx\wedge dy$ back to a vector via $\star$ and $\sharp$ gives $(\nabla\times\vec F) = (\partial_y R - \partial_z Q)\,\partial_x + (\partial_z P - \partial_x R)\,\partial_y + (\partial_x Q - \partial_y P)\,\partial_z$ — exactly the classical curl. The non-obvious step is recognizing that the $2$-form has three independent components in dimension $3$, matching a vector.

**Divergence in coordinates is $d$ on a $2$-form.** With $\beta = P\,dy\wedge dz + Q\,dz\wedge dx + R\,dx\wedge dy = \iota_{\vec F}\,dV$, the exterior derivative is $d\beta = (\partial_x P + \partial_y Q + \partial_z R)\,dx\wedge dy\wedge dz$. The coefficient of $dV$ is exactly $\nabla\cdot\vec F$. This formula generalizes verbatim to any oriented Riemannian manifold, where the same coordinate calculation gives the **invariant divergence formula** $\nabla\cdot\vec F = \frac{1}{\sqrt{\det g}}\partial_i(\sqrt{\det g}\,F^i)$ — a cleaner identity than the classical formula even on $\mathbb{R}^3$.

**$d^2 = 0$ recovers two famous identities at once.** Applying $d$ twice to $f$ gives $d(df) = 0$; translating, this is $\nabla\times\nabla f = 0$. Applying $d$ twice to $\vec F^\flat$ gives $d(d\vec F^\flat) = 0$; the inner derivative produces the $2$-form for curl, the outer derivative produces a $3$-form whose coefficient is $\nabla\cdot(\nabla\times\vec F)$. Setting the coefficient to zero is $\nabla\cdot(\nabla\times\vec F) = 0$. Both classical identities are absorbed by a single line of forms-language algebra. This is the [[Ex - The Exterior Derivative on R^3 Recovers Grad-Curl-Div|grad-curl-div exercise]] in full.

**Is NOT an instance: a 4-dimensional "curl".** In $\mathbb{R}^4$, the exterior derivative $d$ still sends a $1$-form to a $2$-form, but a $2$-form on $\mathbb{R}^4$ has $\binom{4}{2} = 6$ independent components, while a vector field has only $4$ components. So there is no natural way to write $d\vec F^\flat$ as a vector field. The "curl in $\mathbb{R}^4$" does not exist as a vector; it exists as a $2$-form, and this is the only honest generalization. Trying to force a $4$-dimensional cross product on the same grounds fails for the same reason: $\Lambda^2(\mathbb{R}^4)^* \not\cong (\mathbb{R}^4)^*$. The dictionary makes the failure quantitative.

**Calibration check.** First, write $\vec F = (xz, y^2, x+y)$ and compute $\nabla\times\vec F$ classically, then redo it as $\star d(\vec F^\flat)$ and check the two agree. Second, prove $\nabla\cdot(\vec F\times\vec G) = \vec G\cdot(\nabla\times\vec F) - \vec F\cdot(\nabla\times\vec G)$ by translating both sides into form language and applying the Leibniz rule for $d$ on $\vec F^\flat\wedge\vec G^\flat$. Third, verify that on $\mathbb{R}^3$ the Hodge star is $\star\,dx = dy\wedge dz$, $\star\,dy = dz\wedge dx$, $\star\,dz = dx\wedge dy$, $\star 1 = dV$, $\star\,dV = 1$, and that $\star^2 = \mathrm{id}$ in three Euclidean dimensions (no minus sign — that arises only in Lorentzian signature or even dimensions).

---

# Unlocked by This

> [!tip] Hodge Decomposition *(from Hodge Theory)*
> The dictionary's three operators $d : \Omega^0 \to \Omega^1, d : \Omega^1 \to \Omega^2, d : \Omega^2 \to \Omega^3$ on a compact oriented Riemannian $3$-manifold each have a **formal adjoint** $\delta = -\star d\star$ in the opposite direction. On a closed manifold every $k$-form decomposes uniquely as $\omega = d\alpha + \delta\beta + h$ with $h$ harmonic ($\Delta h = (d\delta + \delta d)h = 0$). For $\vec F^\flat$ on a closed $3$-manifold this is the **Helmholtz decomposition** of vector calculus: $\vec F = \nabla\phi + \nabla\times\vec A + \vec H$ where $\vec H$ is "harmonic" (curl- and divergence-free). The dictionary upgrades the classical fact ("a smooth vector field on $\mathbb{R}^3$ decomposes into a gradient plus a curl") into the full Hodge theorem; see [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]].

> [!tip] Maxwell's Equations in Spacetime *(from General Relativity / Gauge Theory)*
> Reading the dictionary one dimension higher — on Lorentzian $\mathbb{R}^{1,3}$ — packages all four Maxwell equations into the two form-equations $dF = 0$ and $d\star F = J$, where $F$ is the Faraday $2$-form (encoding both $\vec E$ and $\vec B$) and $J$ is the current $3$-form. The dictionary's separation of "$d$" from "$\star$" reveals that one of the two equations ($dF = 0$) is metric-independent — a *topological* statement, the Bianchi identity for a $U(1)$ connection — while the other ($d\star F = J$) is genuinely metric-dependent because $\star$ uses the metric. This is the first hint that gauge theory and topology cannot be separated; see [[Ex - Maxwell's Equations as Two Form Equations on Minkowski Space]] and **Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection**.

> [!tip] Vector Calculus on Riemannian Manifolds *(from Riemannian Geometry)*
> The classical formulas for gradient, divergence, and Laplacian on $\mathbb{R}^n$ in Cartesian coordinates *do not* generalize to a curved Riemannian manifold — but their form-language counterparts do. The invariant formulas $\nabla f = (df)^\sharp$, $\nabla\cdot\vec F = \frac{1}{\sqrt{\det g}}\partial_i(\sqrt{\det g}\,F^i)$, and $\Delta f = \frac{1}{\sqrt{\det g}}\partial_i(\sqrt{\det g}\,g^{ij}\partial_j f)$ are forced by the dictionary plus the metric. The **Laplace-Beltrami operator** $\Delta = \delta d + d\delta$ on a Riemannian manifold reduces to the classical Laplacian on $\mathbb{R}^n$ but is meaningful (and important) on every Riemannian manifold; see **Riemannian Geometry I — Connections and Covariant Differentiation**.
