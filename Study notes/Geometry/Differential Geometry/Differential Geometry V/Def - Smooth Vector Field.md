---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Vector Field on a Manifold"
  - "Def - Smooth Map between Manifolds"
  - "Def - The Smooth Functions Ring"
  - "Def - Module"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth $n$-manifold. $TM$ is the [[Def - The Tangent Bundle|tangent bundle]], $\pi : TM \to M$ the projection. A [[Def - Vector Field on a Manifold|vector field]] $X$ on $M$ is a map $X : M \to TM$ with $\pi \circ X = \mathrm{id}_M$. In a chart $(U, (x^i))$, write $X = X^i \partial/\partial x^i$ with component functions $X^i : U \to \mathbb{R}$. $C^\infty(M)$ is the [[Def - The Smooth Functions Ring|ring of smooth real-valued functions]] on $M$. The set of *smooth* vector fields on $M$ is denoted $\mathfrak{X}(M)$ (Lee's notation) or $\Gamma(TM)$ (the section space of $TM$). See [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]] for the full notation registry.

---

# Axiom Motivation

A bare [[Def - Vector Field on a Manifold|vector field]] is just an assignment $p \mapsto X_p \in T_p M$ — a section of $TM$ with no regularity demands. But all the substance of differential geometry — integral curves, flows, derivations of functions, the Lie bracket — requires the assignment to depend on $p$ smoothly. So we need a smoothness axiom, and there are several reasonable candidates. The point of this definition is that they all coincide.

The most natural candidate is **smoothness as a map between manifolds**: since both $M$ and $TM$ are smooth manifolds, $X : M \to TM$ has a well-defined notion of smoothness in the usual sense (smooth in every pair of charts). This is the categorically clean definition. But it is not the easiest to *check*: one would need to verify smoothness of the chart-by-chart expression of $X$ as a map $\mathbb{R}^n \to \mathbb{R}^{2n}$, which is awkward when all you really care about is the $\mathbb{R}^n$-component (the components $X^i$).

The second candidate is **smooth component functions in every chart**: $X = X^i \partial/\partial x^i$ in $(U, (x^i))$, and we demand each $X^i$ be smooth on $U$. This is the easiest condition to verify in practice, but it is chart-dependent on its face — we have to check that it survives a change of chart. The transformation rule for components under a chart change $\tilde x = \tilde x(x)$ is $\tilde X^j = X^i \frac{\partial \tilde x^j}{\partial x^i}$, which is smooth-of-smooth-times-smooth, so the smoothness *does* survive. But we need a proof to know that, so the definition is hostage to that proof.

The third candidate is the **derivation criterion**: $X$ is smooth if, for every $f \in C^\infty(M)$ and every open $U \subseteq M$, the function $Xf$ defined by $(Xf)(p) = X_p f$ is smooth on $U$. This is the most powerful for theoretical work because it converts a question about $X$ into a question about its action on functions, and the function-[[Def - Ring|ring]] $C^\infty(M)$ is something we already understand. But it is not what one would *guess* the definition should be — it has to be earned, by showing it agrees with the other two.

The mathematical content of the definition is that all three candidates *are equivalent*, and so we can use any one of them as definition and prove the others as theorems. This is Lee Proposition 8.1 and 8.14. The traditional choice is the first (smooth as a map of manifolds), with the others recovered as criteria; this is the choice we make.

A reader who has never seen this would invent the definition by asking: "What is the cheapest smoothness condition on $X : M \to TM$ that lets all the constructions of the chapter go through?" The answer is the smooth-map definition, supplemented by the equivalent characterizations that make the definition operationally useful in different contexts.

Why not, say, just $C^1$ vector fields? Because the manifold $M$ is $C^\infty$ and the theorems of the chapter — smoothness of the flow, smooth dependence on initial data in Picard–Lindelöf, the smooth Straightening Theorem — all assume and produce $C^\infty$ regularity. Demanding only $C^1$ would force a parallel theory with weaker conclusions; better to have one strong theory.

Why insist on smoothness *globally*, rather than just locally? A vector field smooth on every chart of an atlas is automatically smooth as a map $M \to TM$, because smoothness for maps between manifolds is itself a local condition. So global vs local smoothness is not a real distinction here — it is a confusing redundancy that the equivalent characterizations clear up.

---

# The Definition

A **smooth vector field** on a smooth manifold $M$ is a [[Def - Vector Field on a Manifold|vector field]] $X : M \to TM$ that is **smooth as a map between smooth manifolds**.

Equivalently (Lee Proposition 8.1 and 8.14):

1. In every smooth chart $(U, (x^i))$, the component functions $X^i$ in the expansion $X = X^i \partial/\partial x^i$ are smooth on $U$.
2. For every $f \in C^\infty(M)$, the function $Xf : M \to \mathbb{R}$ defined by $(Xf)(p) = X_p f$ is smooth.
3. For every open $U \subseteq M$ and every $f \in C^\infty(U)$, the function $Xf : U \to \mathbb{R}$ is smooth.

The set of all smooth vector fields on $M$ is denoted $\mathfrak{X}(M) = \Gamma(TM)$.

$\mathfrak{X}(M)$ is a real vector space under pointwise addition and scalar multiplication:

$$(X + Y)_p = X_p + Y_p, \qquad (cX)_p = c\, X_p,$$

and a [[Def - Module|module]] over the [[Def - Ring|ring]] $C^\infty(M)$ under pointwise multiplication by smooth functions:

$$(fX)_p = f(p)\, X_p.$$

---

# Categorical / Structural Definition

In the category of smooth manifolds, $\pi : TM \to M$ is a vector bundle, and $\mathfrak{X}(M) = \Gamma(TM)$ is the space of smooth sections. The categorical structure is:

- **$\mathfrak{X}(M)$ as a $C^\infty(M)$-[[Def - Module|module]].** Vector fields form a [[Def - Module|module]] over the commutative ring $C^\infty(M)$. This is the general fact: sections of any [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle|vector bundle]] $E \to M$ form a $C^\infty(M)$-module $\Gamma(E)$.

- **$\mathfrak{X}(M)$ as a Lie algebra.** The Lie bracket $[X, Y]f = X(Yf) - Y(Xf)$ — see [[Def - The Lie Bracket of Vector Fields]] — makes $\mathfrak{X}(M)$ into a Lie algebra over $\mathbb{R}$. Note: it is a Lie algebra over $\mathbb{R}$, not over $C^\infty(M)$, because the bracket does not satisfy $C^\infty(M)$-bilinearity — see the function-product rule.

- **$\mathfrak{X}(M)$ as the derivations of $C^\infty(M)$.** Identification: $\mathfrak{X}(M) \cong \mathrm{Der}_\mathbb{R}(C^\infty(M))$ as Lie algebras under the bracket. This is the **algebraic characterization** of smooth vector fields: they are exactly the $\mathbb{R}$-linear maps $C^\infty(M) \to C^\infty(M)$ satisfying the Leibniz rule $D(fg) = f Dg + g Df$, and the bracket on the vector-field side matches the commutator on the derivation side.

The third identification — vector fields *are* derivations — is the most useful one in proofs, because it converts geometric statements about $TM$ into algebraic statements about the function ring. It is also the bridge from differential geometry to **synthetic differential geometry** and to the theory of **Lie algebroids**, where a Lie algebroid is the natural categorification of "Lie algebra of derivations with a smooth-function module structure".

---

# Relate to Other Fields / Compression

A smooth vector field on $\mathbb{R}^n$ is just a smooth map $\mathbb{R}^n \to \mathbb{R}^n$, viewed as "vector at every point". The lift to a smooth manifold is the natural generalisation: replace $\mathbb{R}^n$ on the target with the tangent bundle $TM$, and replace "smooth function" with "smooth section". Everything else — the module structure, the Lie bracket on $\mathbb{R}^n$ vector fields (which is also $\partial_i Y^j - Y^i \partial_i X^j$) — is identical.

**True name:** $\mathfrak{X}(M)$ is **the Lie algebra of derivations of $C^\infty(M)$**. This is the operational characterization for any problem involving the bracket, the Lie derivative, or the algebraic structure of vector fields. The "official" definition (smooth sections of $TM$) is the right thing to *visualize*; the derivation viewpoint is the right thing to *compute with*.

---

# Examples / Corollaries

**Is an instance: the coordinate vector field $\partial/\partial x^i$ in a chart.** Its components are constants $X^j = \delta_i^j$, so the smoothness condition (i) is trivially satisfied on the chart domain. As an operator on functions, $\partial/\partial x^i$ acts as partial differentiation in the $i$-th coordinate — visibly smooth.

**Is an instance: a sum of smooth vector fields and a smooth-function multiple.** If $X, Y \in \mathfrak{X}(M)$ and $f \in C^\infty(M)$, then $fX + Y \in \mathfrak{X}(M)$ — the components transform smoothly because both the components of $X, Y$ and the function $f$ are smooth. This is the module-structure compatibility.

**Is an instance: the velocity field of a smooth flow.** If $\phi : \mathbb{R} \times M \to M$ is smooth and $\phi_0 = \mathrm{id}$, then $X_p = \frac{d}{dt}\big|_{t=0} \phi_t(p)$ is automatically smooth, because partial derivatives of a smooth function in $(t, p)$ are smooth in $p$. So *every* flow's infinitesimal generator is smooth.

**Is NOT an instance: a rough section that fails the derivation criterion.** Suppose on $\mathbb{R}$ we define $X = f(x) \partial_x$ where $f(x) = 1$ for $x > 0$ and $f(x) = 0$ for $x \leq 0$. This is a vector field in the rough sense — it assigns a tangent vector at every point — but $f$ is not smooth at $0$, so the component $X^1$ is not smooth, and the derivation criterion fails: take $g(x) = x$, then $Xg = f$ which is not smooth. This is not a smooth vector field.

**Is NOT an instance: a section that depends discontinuously on $p$.** Consider $X$ on $\mathbb{R}$ defined by $X_p = \partial_x|_p$ for $p$ rational and $X_p = -\partial_x|_p$ for $p$ irrational. This is a section of $T\mathbb{R}$ but is not even continuous, much less smooth.

**Corollary (the module structure makes sense).** Because $\mathfrak{X}(M)$ is closed under addition and scalar multiplication by smooth functions, the operations $(X, Y) \mapsto X + Y$ and $(f, X) \mapsto fX$ are well-defined on $\mathfrak{X}(M)$. The proof in coordinates uses only the smoothness of components and of $f$, and the identity $f X^i$ is smooth-times-smooth.

**Corollary (smoothness localizes).** A vector field on $M$ is smooth if and only if its restriction to every chart $(U, (x^i))$ has smooth components. This is because smoothness of a map between manifolds is a local notion (a chart-by-chart check), and the smoothness criteria above all become local statements.

**Corollary (derivations preserve smoothness).** If $X \in \mathfrak{X}(M)$ and $f \in C^\infty(M)$, then $Xf \in C^\infty(M)$ — the action of $X$ on smooth functions produces smooth functions. This is the basis for treating $X$ as a derivation $C^\infty(M) \to C^\infty(M)$.

**Calibration check.** You should be able to: (a) verify directly from the chart-component definition that $X = x \partial_x + y \partial_y$ on $\mathbb{R}^2$ is smooth (components are linear, hence smooth); (b) confirm that the derivation criterion gives the same answer (compute $Xg$ for $g(x, y) = x^2 + y^2$; the result is $2x^2 + 2y^2$, which is smooth); (c) explain why a vector field on $S^2$ with a single singular value (a continuity gap on the equator) is not smooth.

---

# Unlocked by This

> [!tip] Module of Sections of a Vector Bundle *(from Vector Bundle Theory)*
> The same construction with $TM$ replaced by any [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle|vector bundle]] $E \to M$ gives $\Gamma(E)$, the space of smooth sections — a [[Def - Module|module]] over $C^\infty(M)$. Sections of $T^*M$ are covector fields / one-forms; sections of $\bigwedge^k T^*M$ are differential $k$-forms; sections of $TM \otimes T^*M$ are $(1,1)$-tensor fields.

> [!tip] $\mathfrak{X}(M)$ as the Lie Algebra of the Diffeomorphism Group *(from Infinite-Dimensional Geometry)*
> The diffeomorphism group $\mathrm{Diff}(M)$ is an infinite-dimensional Lie group, and its Lie algebra is $\mathfrak{X}(M)$ with the **negative** of the Lie bracket: the sign comes from the convention that left-invariant vector fields go with right-translations. So the entire chapter is reading "the Lie algebra of $\mathrm{Diff}(M)$" via the identification of complete vector fields with one-parameter subgroups of $\mathrm{Diff}(M)$.

> [!tip] Lie Algebroid *(from Generalized Geometry)*
> A **Lie algebroid** is a vector bundle $A \to M$ whose sections form a Lie algebra and which has an "anchor" $A \to TM$ implementing the function product rule. The prototypical example is $A = TM$ itself with anchor $\mathrm{id}_{TM}$. Lie algebroids generalize both Lie algebras (when $M$ is a point) and the tangent bundle (when the anchor is the identity), and they are the language of Poisson geometry and gauge theory.
