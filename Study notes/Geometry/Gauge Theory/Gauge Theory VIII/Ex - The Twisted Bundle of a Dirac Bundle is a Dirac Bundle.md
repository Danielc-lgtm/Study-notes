---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Spinor Bundle and Dirac Operator"
  - "Def - Operations on Vector Bundles and Pull-Back Bundles"
  - "Def - Clifford Bundle and Bundle of Clifford Modules"
  - "Def - Metric-Compatible Connection"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $M$ be an oriented Riemannian manifold of dimension $n$, and let $E \to M$ be a **Dirac bundle**: a bundle of $\mathrm{Cl}(M)$-modules, carrying a Hermitian metric $\langle\cdot,\cdot\rangle_E$ and a connection $\nabla^E$, subject to the three Dirac-bundle conditions

$$
(1)\ \ \nabla^E \text{ is metric}; \qquad (2)\ \ \langle v\cdot e_1, v\cdot e_2\rangle_E = |v|^2\langle e_1, e_2\rangle_E; \qquad (3)\ \ \nabla^E(\phi\cdot s) = (\nabla^{LC}\phi)\cdot s + \phi\cdot\nabla^E s,
$$

for all $v \in T_mM$, all $e_1, e_2 \in E_m$, all $\phi \in \Gamma(\mathrm{Cl}(M))$, and all $s \in \Gamma(E)$. Let $F \to M$ be a Hermitian vector bundle equipped with a **unitary connection** $\nabla^F$ — that is, a connection metric with respect to the Hermitian metric $\langle\cdot,\cdot\rangle_F$ of $F$.

Endow the tensor-product bundle $E \otimes F$ (tensor product over $\mathbb{C}$, fibrewise $E_m \otimes_{\mathbb{C}} F_m$) with

- **Clifford multiplication acting through the $E$-factor:** $v\cdot(e\otimes f) := (v\cdot e)\otimes f$ for $v \in T_mM$, $e \in E_m$, $f \in F_m$, extended $\mathbb{C}$-bilinearly;
- **the product Hermitian metric:** $\langle e_1\otimes f_1,\, e_2\otimes f_2\rangle := \langle e_1, e_2\rangle_E\,\langle f_1, f_2\rangle_F$, extended sesquilinearly;
- **the tensor-product connection:** $\nabla^{E\otimes F} := \nabla^E\otimes 1 + 1\otimes\nabla^F$, meaning $\nabla^{E\otimes F}_X(e\otimes f) = (\nabla^E_X e)\otimes f + e\otimes(\nabla^F_X f)$ on decomposable sections and extended by additivity and the Leibniz rule.

**Show that $E\otimes F$ is again a Dirac bundle** — that is, verify that the Clifford multiplication is a genuine $\mathrm{Cl}(M)$-module structure and that conditions (1), (2), (3) all hold — **and compute its Dirac operator $D_{E\otimes F}$ in a local orthonormal frame** $(e_1,\dots,e_n)$ of $TM$, expressing it through the Dirac operator $D_E$ of $E$ and the connection $\nabla^F$.

This is the construction that turns the spin Dirac operator $\slashed D$ on the spinor bundle $\slashed S$ into the **twisted Dirac operator** $\slashed D_A$ on $\slashed S\otimes E$, where $E = P\times_{G,\rho}\mathbb{C}^k$ is the bundle associated to a principal $G$-bundle $P$ with connection $A$; it is the linear-algebraic content behind the definition of $\slashed D_A$ and is used throughout Seiberg–Witten theory.

**Recall:**

The objects in play are a Dirac bundle and its three defining conditions, the tensor product of two vector bundles with its product metric and tensor-product connection, and the Dirac operator built by Clifford-contracting the covariant derivative.

![[Def - Spinor Bundle and Dirac Operator#The Definition]]

A **[[Def - Spinor Bundle and Dirac Operator|Dirac bundle]]** over an oriented Riemannian manifold $M$ is a bundle of [[Def - Clifford Bundle and Bundle of Clifford Modules|Clifford modules]] $E$ — a vector bundle with a bundle morphism $TM\otimes E \to E$, $(v,e)\mapsto v\cdot e$, satisfying $v\cdot(v\cdot e) = -|v|^2 e$ — together with a metric $\langle\cdot,\cdot\rangle_E$ and a connection $\nabla^E$ obeying conditions (1)–(3) above. Its **Dirac operator** is the composite
$$
D_E : \Gamma(E) \xrightarrow{\ \nabla^E\ } \Gamma(T^*M\otimes E) \xrightarrow{\ \mathrm{Cl}\ } \Gamma(E), \qquad D_E s = \sum_{i=1}^n e_i\cdot\nabla^E_{e_i}s \ \text{ in a local orthonormal frame } (e_i).
$$
Here $\nabla^{LC}$ denotes the connection that the [[Def - Levi-Civita Connection|Levi-Civita connection]] induces on the Clifford bundle $\mathrm{Cl}(M)$; it is a derivation of the fibrewise Clifford product, which is what condition (3) refers to.

![[Def - Operations on Vector Bundles and Pull-Back Bundles#The Definition]]

Given two vector bundles $E, F \to M$ with connections $\nabla^E, \nabla^F$, the **[[Def - Operations on Vector Bundles and Pull-Back Bundles|tensor-product connection]]** on $E\otimes F$ is the unique connection with $\nabla^{E\otimes F}_X(e\otimes f) = (\nabla^E_X e)\otimes f + e\otimes(\nabla^F_X f)$; when $E, F$ carry metrics, the **product metric** on $E\otimes F$ is determined on decomposables by $\langle e_1\otimes f_1, e_2\otimes f_2\rangle = \langle e_1,e_2\rangle_E\langle f_1,f_2\rangle_F$.

A connection $\nabla$ is **[[Def - Metric-Compatible Connection|metric]]** (unitary, in the Hermitian case) when $X\langle s_1, s_2\rangle = \langle\nabla_X s_1, s_2\rangle + \langle s_1, \nabla_X s_2\rangle$ for all vector fields $X$ and sections $s_1, s_2$. Throughout, $\langle\cdot,\cdot\rangle$ denotes a Hermitian inner product taken $\mathbb{C}$-linear in its first argument and conjugate-linear in its second; $|v|^2 = g(v,v)$ is the Riemannian length of a real tangent vector $v$, so $|v|^2$ is a non-negative real number.

> [!note] Convention: the metric on $E$
> Haydys states the Dirac-bundle conditions for a *Euclidean* (real) scalar product; the series allows either a Euclidean or a Hermitian metric, because the case that matters — the twisted spinor bundle $\slashed S\otimes E$ — has $\slashed S$ and $E$ both complex Hermitian. We carry out the verification for Hermitian $E$ and $F$; the real Euclidean case is word-for-word identical with $\mathbb{R}$ in place of $\mathbb{C}$ and symmetric bilinear forms in place of Hermitian ones, since Clifford multiplication acts only on the $E$-factor and no complex structure is used in any step.

---

# Convergent Strategy

**Problem class.** This is a *closure-under-a-construction* verification: we are handed a structured object (a Dirac bundle $E$), a second bundle $F$ with strictly less structure (just a Hermitian bundle with a unitary connection), and a recipe for building a new candidate ($E\otimes F$), and we must check that the candidate satisfies the same axioms. Such problems are almost always proved by *reduction to the corresponding property of the factors*: every clause of the axiom for $E\otimes F$ is engineered to collapse, after one application of the definitions, onto the same clause for $E$ together with a compatibility of $F$. The only genuine content is to see *which* hypothesis on each factor each clause consumes.

**Assumption pattern.** The decisive structural fact is that **$\mathrm{Cl}(M)$ acts on $E\otimes F$ only through the $E$-factor**: $\phi\cdot(e\otimes f) = (\phi\cdot e)\otimes f$, with $F$ a passive spectator. Consequently every clause that mentions Clifford multiplication (the module axiom and conditions (2), (3)) is inherited from $E$ once the $F$-factor is carried along untouched, and the clause that does *not* mention Clifford multiplication — condition (1), metricity — is exactly where the hypothesis "$\nabla^F$ is unitary" is spent. The trigger for this whole approach is the shape of the three ingredients: a Clifford action defined *through one factor*, a *product* metric, and a *sum* connection $\nabla^E\otimes 1 + 1\otimes\nabla^F$.

**Theorem routing.** The route is: (Step 0) check $v\cdot(e\otimes f) := (v\cdot e)\otimes f$ is a well-defined $\mathrm{Cl}(M)$-module structure, using the module axiom of $E$ ([[Def - Spinor Bundle and Dirac Operator|Dirac bundle]] / [[Def - Clifford Bundle and Bundle of Clifford Modules|bundle of Clifford modules]]); (Step 1) condition (1) from metricity of $\nabla^E$ *and* $\nabla^F$ ([[Def - Metric-Compatible Connection|metric connection]]) together with the [[Def - Operations on Vector Bundles and Pull-Back Bundles|product metric and tensor-product connection]]; (Step 2) condition (2) from condition (2) for $E$; (Step 3) condition (3) from condition (3) for $E$ and the derivation form of $\nabla^{E\otimes F}$; (Step 4) assemble the Dirac operator by feeding $\nabla^{E\otimes F} = \nabla^E\otimes 1 + 1\otimes\nabla^F$ into $D = \mathrm{Cl}\circ\nabla$.

**Key decision point.** The one move that has to be *chosen* rather than computed is the reduction to decomposable sections $e\otimes f$. Conditions (1)–(3) are identities between sesquilinear or $\mathbb{C}$-linear expressions in the sections, and $\Gamma(E\otimes F)$ is locally spanned over $C^\infty(M)$ by decomposables $e\otimes f$; so it suffices to verify each identity on decomposables and extend by (bi/sesqui)linearity and the Leibniz rule. Recognising that this reduction is legitimate — that no identity being checked is nonlinear in a way that would break under the extension — is the crux; once granted, every step is a single substitution.

---

# Legal Operations Used

This solution deploys the following legal operations of the chapter (numbering to be reconciled with the topic page's Legal Operations once it is written):

1. **Verify a bundle-morphism identity fibrewise on decomposable tensors.** All three Dirac-bundle conditions and the module axiom are pointwise (fibrewise) statements; since $E_m\otimes_{\mathbb{C}} F_m$ is spanned by decomposables $e\otimes f$, it suffices to check each identity on such elements and extend by (sesqui)linearity.

2. **Push a factored Clifford action through a tensor product.** From $\phi\cdot(e\otimes f) = (\phi\cdot e)\otimes f$, every Clifford-flavoured axiom of $E\otimes F$ is rewritten as the corresponding axiom of $E$ with the inert factor $f$ (or the metric of $F$) attached.

3. **Use metricity of both factors for the tensor-product connection.** Expand $X\langle e_1\otimes f_1, e_2\otimes f_2\rangle$ by the Leibniz rule for the product of two functions, then apply metric compatibility of $\nabla^E$ (condition (1) for $E$) to the $E$-factor and unitarity of $\nabla^F$ to the $F$-factor; regroup into the tensor-product connection.

4. **Invoke a defining property of $E$ by name to discharge the twin property of $E\otimes F$.** Condition (2) for $E\otimes F$ is discharged by condition (2) for $E$ applied to the mixed pairs $(e_a, e_b')$; condition (3) for $E\otimes F$ by condition (3) for $E$ on the $E$-factor.

5. **Assemble a first-order operator from its symbol and connection.** The Dirac operator is $\mathrm{Cl}\circ\nabla$; feeding the sum connection $\nabla^E\otimes1 + 1\otimes\nabla^F$ into this composite splits $D_{E\otimes F}$ into the untwisted piece $D_E\otimes 1$ and a twisting piece built from $\nabla^F$.

---

# Hints

> [!note]- Hint 1
> Do not try to prove the three conditions for $E\otimes F$ directly from scratch. Each of them is the same statement as the corresponding condition for $E$, wearing a coat. First settle, once and for all, how $\mathrm{Cl}(M)$ acts on $E\otimes F$: only through the first factor, $\phi\cdot(e\otimes f) = (\phi\cdot e)\otimes f$. With that fixed, ask of each condition: which factor does it touch?

> [!note]- Hint 2
> For condition (1), the metricity of $\nabla^{E\otimes F}$, work on a decomposable section $\sigma = e\otimes f$ and differentiate the product metric $\langle e_1\otimes f_1, e_2\otimes f_2\rangle = \langle e_1, e_2\rangle_E\langle f_1, f_2\rangle_F$ along a vector field $X$. You are differentiating a *product of two scalar functions*; use the ordinary Leibniz rule, then feed each factor its own metric-compatibility identity. This is the only step that uses "$\nabla^F$ is unitary."

> [!note]- Hint 3
> For condition (2), Clifford multiplication never touches $F$: $\langle v\cdot(e_1\otimes f_1),\, v\cdot(e_2\otimes f_2)\rangle = \langle v\cdot e_1, v\cdot e_2\rangle_E\,\langle f_1, f_2\rangle_F$. Now apply condition (2) *for $E$*, which holds for every pair $e_1, e_2$, not just equal ones. For condition (3), differentiate $\phi\cdot(e\otimes f) = (\phi\cdot e)\otimes f$ with $\nabla^{E\otimes F}$ and apply the Leibniz rule of the tensor connection, then condition (3) for $E$ on the $E$-factor.

> [!note]- Hint 4
> For the Dirac operator, write $D_{E\otimes F}\sigma = \sum_i e_i\cdot\nabla^{E\otimes F}_{e_i}\sigma$ and substitute $\nabla^{E\otimes F}_{e_i}(e\otimes f) = (\nabla^E_{e_i}e)\otimes f + e\otimes(\nabla^F_{e_i}f)$. Clifford-multiply by $e_i$ (which acts through the $E$-factor) and sum. The first group of terms is exactly $D_E$ applied to the $E$-factor; the second group is the "twisting" term $\sum_i (e_i\cdot e)\otimes\nabla^F_{e_i}f$.

---

# Solution

The whole verification runs on one observation: in $E\otimes F$ the Clifford algebra acts only on the first factor, so every axiom that involves Clifford multiplication is the corresponding axiom of $E$ with the $F$-data carried along inertly, while the single axiom that does not — metricity — is where the unitarity of $\nabla^F$ is used. We check the module axiom (Step 0), then conditions (1), (2), (3) (Steps 1–3), then read off the Dirac operator (Step 4). Throughout, $(e_i)_{i=1}^n$ is a local orthonormal frame of $TM$, $X$ a vector field on $M$, and it suffices to verify each fibrewise identity on decomposable elements $e\otimes f$, $e\in\Gamma(E)$, $f\in\Gamma(F)$, because these span $\Gamma(E\otimes F)$ over $C^\infty(M)$ and every identity below is (sesqui)linear in the sections.

**Step 0: $v\cdot(e\otimes f) := (v\cdot e)\otimes f$ is a well-defined bundle of Clifford modules.**

The map is a genuine bundle morphism $TM\otimes(E\otimes F)\to E\otimes F$, and it satisfies the module relation $v\cdot(v\cdot\sigma) = -|v|^2\sigma$.

> [!note]- Derivation
> **Well-definedness.** Clifford multiplication on $E$ is a bundle morphism $c_E : TM\otimes E \to E$, $c_E(v\otimes e) = v\cdot e$. Tensoring with the identity of $F$ gives a bundle morphism $c_E\otimes\mathrm{id}_F : TM\otimes E\otimes F \to E\otimes F$; after the canonical reassociation $TM\otimes(E\otimes F)\cong (TM\otimes E)\otimes F$, this is precisely the assignment $v\otimes(e\otimes f)\mapsto (v\cdot e)\otimes f$ (by the definition of the tensor product of two morphisms). Being obtained from bundle morphisms by tensoring and reassociating, it is itself a bundle morphism, hence well defined and independent of the way an element of $E_m\otimes F_m$ is written as a sum of decomposables.
>
> **The Clifford relation.** For $v\in T_mM$ and a decomposable $e\otimes f$,
> $$v\cdot\big(v\cdot(e\otimes f)\big) = v\cdot\big((v\cdot e)\otimes f\big) \qquad \text{(definition of the action on } E\otimes F\text{)}$$
> $$= \big(v\cdot(v\cdot e)\big)\otimes f \qquad \text{(definition again, applied to the section } v\cdot e \text{ of } E\text{)}$$
> $$= (-|v|^2\,e)\otimes f \qquad \text{(module axiom } v\cdot(v\cdot e) = -|v|^2 e \text{ of the Dirac bundle } E\text{)}$$
> $$= -|v|^2\,(e\otimes f) \qquad \text{(} \mathbb{C}\text{-bilinearity of the tensor product; } |v|^2\in\mathbb{R}\text{ is a scalar).}$$
> By $\mathbb{C}$-bilinearity in $(v, \sigma)$ the relation $v\cdot(v\cdot\sigma) = -|v|^2\sigma$ then holds for every $\sigma\in E_m\otimes F_m$. Hence $E\otimes F$ is a bundle of $\mathrm{Cl}(M)$-modules, the action of the full Clifford bundle being $\phi\cdot(e\otimes f) = (\phi\cdot e)\otimes f$ for $\phi\in\Gamma(\mathrm{Cl}(M))$.

**Step 1: Condition (1) — $\nabla^{E\otimes F}$ is metric for the product metric.**

Metricity of $\nabla^E$ (given) and unitarity of $\nabla^F$ (given) together force $X\langle\sigma_1,\sigma_2\rangle = \langle\nabla^{E\otimes F}_X\sigma_1,\sigma_2\rangle + \langle\sigma_1,\nabla^{E\otimes F}_X\sigma_2\rangle$.

> [!note]- Derivation
> Take decomposable sections $\sigma_1 = e_1\otimes f_1$ and $\sigma_2 = e_2\otimes f_2$. By the definition of the product metric, $\langle\sigma_1,\sigma_2\rangle = \langle e_1,e_2\rangle_E\,\langle f_1,f_2\rangle_F$ is a product of two smooth $\mathbb{C}$-valued functions on $M$. Differentiating along $X$,
> $$X\langle\sigma_1,\sigma_2\rangle = \big(X\langle e_1,e_2\rangle_E\big)\langle f_1,f_2\rangle_F + \langle e_1,e_2\rangle_E\big(X\langle f_1,f_2\rangle_F\big) \qquad \text{(Leibniz rule for the product of two functions).}$$
> Apply metric compatibility of $\nabla^E$ (**condition (1) for $E$**) to the first factor and unitarity of $\nabla^F$ (**the hypothesis on $F$**) to the second:
> $$X\langle e_1,e_2\rangle_E = \langle\nabla^E_X e_1, e_2\rangle_E + \langle e_1, \nabla^E_X e_2\rangle_E, \qquad X\langle f_1,f_2\rangle_F = \langle\nabla^F_X f_1, f_2\rangle_F + \langle f_1, \nabla^F_X f_2\rangle_F.$$
> Substituting and expanding the product gives four terms:
> $$X\langle\sigma_1,\sigma_2\rangle = \langle\nabla^E_X e_1, e_2\rangle_E\langle f_1,f_2\rangle_F + \langle e_1, \nabla^E_X e_2\rangle_E\langle f_1,f_2\rangle_F + \langle e_1,e_2\rangle_E\langle\nabla^F_X f_1, f_2\rangle_F + \langle e_1,e_2\rangle_E\langle f_1, \nabla^F_X f_2\rangle_F.$$
> Regroup the first and third terms, and the second and fourth, using the definition of the product metric in reverse (for instance $\langle\nabla^E_X e_1, e_2\rangle_E\langle f_1,f_2\rangle_F = \langle(\nabla^E_X e_1)\otimes f_1,\, e_2\otimes f_2\rangle$):
> $$X\langle\sigma_1,\sigma_2\rangle = \big\langle (\nabla^E_X e_1)\otimes f_1 + e_1\otimes(\nabla^F_X f_1),\ \sigma_2\big\rangle + \big\langle \sigma_1,\ (\nabla^E_X e_2)\otimes f_2 + e_2\otimes(\nabla^F_X f_2)\big\rangle.$$
> By the definition of the tensor-product connection, $(\nabla^E_X e_k)\otimes f_k + e_k\otimes(\nabla^F_X f_k) = \nabla^{E\otimes F}_X\sigma_k$, so
> $$X\langle\sigma_1,\sigma_2\rangle = \langle\nabla^{E\otimes F}_X\sigma_1, \sigma_2\rangle + \langle\sigma_1, \nabla^{E\otimes F}_X\sigma_2\rangle.$$
> Both sides are additive in $\sigma_1$ and in $\sigma_2$ and satisfy the same Leibniz rule under multiplication of a section by a function $g\in C^\infty(M)$ (the left side because $\nabla^{E\otimes F}(g\sigma) = dg\otimes\sigma + g\nabla^{E\otimes F}\sigma$, the right side directly), so the identity extends from decomposables to all sections. Hence $\nabla^{E\otimes F}$ is metric: **condition (1) holds.**

**Step 2: Condition (2) — Clifford multiplication by a unit vector is an isometry of the product metric.**

The identity $\langle v\cdot\sigma_1, v\cdot\sigma_2\rangle = |v|^2\langle\sigma_1,\sigma_2\rangle$ follows from the same identity for $E$, because Clifford multiplication leaves the $F$-factor untouched.

> [!note]- Derivation
> On decomposables $\sigma_1 = e_1\otimes f_1$, $\sigma_2 = e_2\otimes f_2$, and $v\in T_mM$,
> $$\langle v\cdot\sigma_1, v\cdot\sigma_2\rangle = \big\langle (v\cdot e_1)\otimes f_1,\ (v\cdot e_2)\otimes f_2\big\rangle \qquad \text{(definition of the action on } E\otimes F\text{)}$$
> $$= \langle v\cdot e_1, v\cdot e_2\rangle_E\,\langle f_1, f_2\rangle_F \qquad \text{(definition of the product metric)}$$
> $$= |v|^2\,\langle e_1, e_2\rangle_E\,\langle f_1, f_2\rangle_F \qquad \text{(} \textbf{condition (2) for } E\text{, valid for the pair } (e_1, e_2)\text{)}$$
> $$= |v|^2\,\langle \sigma_1, \sigma_2\rangle \qquad \text{(definition of the product metric).}$$
> For general $\sigma_1 = \sum_a e_a\otimes f_a$ and $\sigma_2 = \sum_b e_b'\otimes f_b'$, expanding both sides by sesquilinearity produces $\sum_{a,b}\langle v\cdot e_a, v\cdot e_b'\rangle_E\langle f_a, f_b'\rangle_F$ on the left and $|v|^2\sum_{a,b}\langle e_a, e_b'\rangle_E\langle f_a, f_b'\rangle_F$ on the right; these agree term by term because **condition (2) for $E$** holds for every pair $(e_a, e_b')$, not merely for equal arguments. Hence **condition (2) holds** for $E\otimes F$.

**Step 3: Condition (3) — compatibility of $\nabla^{E\otimes F}$ with Clifford multiplication.**

For $\phi\in\Gamma(\mathrm{Cl}(M))$ and $\sigma\in\Gamma(E\otimes F)$, $\nabla^{E\otimes F}(\phi\cdot\sigma) = (\nabla^{LC}\phi)\cdot\sigma + \phi\cdot\nabla^{E\otimes F}\sigma$.

> [!note]- Derivation
> On a decomposable $\sigma = e\otimes f$, using $\phi\cdot(e\otimes f) = (\phi\cdot e)\otimes f$ from Step 0,
> $$\nabla^{E\otimes F}_X\big(\phi\cdot(e\otimes f)\big) = \nabla^{E\otimes F}_X\big((\phi\cdot e)\otimes f\big) \qquad \text{(action through the } E\text{-factor)}$$
> $$= \big(\nabla^E_X(\phi\cdot e)\big)\otimes f + (\phi\cdot e)\otimes(\nabla^F_X f) \qquad \text{(Leibniz rule of the tensor-product connection).}$$
> Apply **condition (3) for $E$** to $\nabla^E_X(\phi\cdot e) = (\nabla^{LC}_X\phi)\cdot e + \phi\cdot\nabla^E_X e$:
> $$= \big((\nabla^{LC}_X\phi)\cdot e\big)\otimes f + \big(\phi\cdot\nabla^E_X e\big)\otimes f + (\phi\cdot e)\otimes(\nabla^F_X f).$$
> The first term is $(\nabla^{LC}_X\phi)\cdot(e\otimes f)$ by the action through the $E$-factor. The last two terms both carry the factor $\phi\cdot$ acting on the $E$-slot, so by linearity of that action,
> $$\big(\phi\cdot\nabla^E_X e\big)\otimes f + (\phi\cdot e)\otimes(\nabla^F_X f) = \phi\cdot\Big((\nabla^E_X e)\otimes f + e\otimes(\nabla^F_X f)\Big) = \phi\cdot\nabla^{E\otimes F}_X(e\otimes f),$$
> the last equality being the definition of $\nabla^{E\otimes F}$. Collecting,
> $$\nabla^{E\otimes F}_X\big(\phi\cdot(e\otimes f)\big) = (\nabla^{LC}_X\phi)\cdot(e\otimes f) + \phi\cdot\nabla^{E\otimes F}_X(e\otimes f).$$
> Both sides are additive in $\sigma$ and obey the same function-Leibniz rule (the extra term $dg\otimes(\phi\cdot\sigma)$ produced by $\sigma\mapsto g\sigma$ matches on both sides because $\phi\cdot(g\sigma) = g(\phi\cdot\sigma)$, the action being $C^\infty(M)$-linear), so the identity extends to all $\sigma\in\Gamma(E\otimes F)$. Hence **condition (3) holds**, and $E\otimes F$ is a Dirac bundle.

**Step 4: The Dirac operator of $E\otimes F$ in a frame.**

In a local orthonormal frame $(e_i)$ of $TM$,
$$
D_{E\otimes F}(e\otimes f) = (D_E\,e)\otimes f + \sum_{i=1}^n (e_i\cdot e)\otimes\nabla^F_{e_i}f,
$$
so that as an operator $D_{E\otimes F} = D_E\otimes 1 + \sum_i (e_i\cdot)\otimes\nabla^F_{e_i}$.

> [!note]- Derivation
> By definition $D_{E\otimes F}\sigma = \sum_i e_i\cdot\nabla^{E\otimes F}_{e_i}\sigma$. On $\sigma = e\otimes f$,
> $$D_{E\otimes F}(e\otimes f) = \sum_i e_i\cdot\nabla^{E\otimes F}_{e_i}(e\otimes f) = \sum_i e_i\cdot\Big((\nabla^E_{e_i}e)\otimes f + e\otimes(\nabla^F_{e_i}f)\Big) \qquad \text{(definition of } \nabla^{E\otimes F}\text{)}$$
> $$= \sum_i (e_i\cdot\nabla^E_{e_i}e)\otimes f + \sum_i (e_i\cdot e)\otimes(\nabla^F_{e_i}f) \qquad \text{(Clifford multiplication acts through the } E\text{-factor, Step 0)}$$
> $$= \Big(\sum_i e_i\cdot\nabla^E_{e_i}e\Big)\otimes f + \sum_i (e_i\cdot e)\otimes(\nabla^F_{e_i}f) = (D_E\,e)\otimes f + \sum_i (e_i\cdot e)\otimes(\nabla^F_{e_i}f) \qquad \text{(definition of } D_E\text{).}$$
> The first summand is the Dirac operator of $E$ acting in the $E$-factor and leaving $F$ alone; the second is the *twisting term*, in which Clifford multiplication by the frame vectors is coupled to the $F$-connection. Because $D_{E\otimes F} = \mathrm{Cl}\circ\nabla^{E\otimes F}$ is defined frame-independently (the contraction $\mathrm{Cl}:\Gamma(T^*M\otimes E\otimes F)\to\Gamma(E\otimes F)$ is a tensorial, hence frame-independent, operation — see [[Def - Spinor Bundle and Dirac Operator|the Dirac operator's definition]]), this expression is independent of the chosen orthonormal frame, even though each summand is written frame-dependently. When $E = \slashed S$ is a spinor bundle and $F = P\times_{G,\rho}\mathbb{C}^k$ with connection $A$, this operator is exactly the twisted Dirac operator $\slashed D_A$.

> [!note]- Complete formal solution
> **Claim.** With Clifford multiplication $v\cdot(e\otimes f) = (v\cdot e)\otimes f$, the product Hermitian metric, and the tensor-product connection $\nabla^{E\otimes F} = \nabla^E\otimes 1 + 1\otimes\nabla^F$, the bundle $E\otimes F$ is a Dirac bundle, with Dirac operator $D_{E\otimes F}(e\otimes f) = (D_E e)\otimes f + \sum_i (e_i\cdot e)\otimes\nabla^F_{e_i}f$ in a local orthonormal frame $(e_i)$.
>
> Let $E$ be a Dirac bundle over the oriented Riemannian manifold $M$ and $F$ a Hermitian bundle with unitary connection $\nabla^F$. Fix a local orthonormal frame $(e_i)_{i=1}^n$ of $TM$ and a vector field $X$. Since $\Gamma(E\otimes F)$ is spanned over $C^\infty(M)$ by decomposable sections $e\otimes f$, and every identity below is (sesqui)linear in the sections and compatible with the function-Leibniz rule, it suffices to verify each on decomposables.
>
> *Module structure.* The morphism $c_E : TM\otimes E\to E$ tensored with $\mathrm{id}_F$ gives, after reassociation, the well-defined action $v\cdot(e\otimes f) = (v\cdot e)\otimes f$; and $v\cdot(v\cdot(e\otimes f)) = (v\cdot(v\cdot e))\otimes f = (-|v|^2 e)\otimes f = -|v|^2(e\otimes f)$ by the module axiom of $E$. So $E\otimes F$ is a bundle of $\mathrm{Cl}(M)$-modules with $\phi\cdot(e\otimes f) = (\phi\cdot e)\otimes f$.
>
> *Condition (1).* For $\sigma_k = e_k\otimes f_k$, the product metric gives $\langle\sigma_1,\sigma_2\rangle = \langle e_1,e_2\rangle_E\langle f_1,f_2\rangle_F$; the Leibniz rule for a product of functions plus metric compatibility of $\nabla^E$ and $\nabla^F$ yields $X\langle\sigma_1,\sigma_2\rangle = \langle\nabla^{E\otimes F}_X\sigma_1,\sigma_2\rangle + \langle\sigma_1,\nabla^{E\otimes F}_X\sigma_2\rangle$. This is where unitarity of $\nabla^F$ is used.
>
> *Condition (2).* $\langle v\cdot\sigma_1, v\cdot\sigma_2\rangle = \langle v\cdot e_1, v\cdot e_2\rangle_E\langle f_1,f_2\rangle_F = |v|^2\langle e_1,e_2\rangle_E\langle f_1,f_2\rangle_F = |v|^2\langle\sigma_1,\sigma_2\rangle$, the middle equality being condition (2) for $E$ (which holds for all pairs).
>
> *Condition (3).* $\nabla^{E\otimes F}_X(\phi\cdot(e\otimes f)) = \nabla^{E\otimes F}_X((\phi\cdot e)\otimes f) = (\nabla^E_X(\phi\cdot e))\otimes f + (\phi\cdot e)\otimes\nabla^F_X f$; applying condition (3) for $E$ to $\nabla^E_X(\phi\cdot e) = (\nabla^{LC}_X\phi)\cdot e + \phi\cdot\nabla^E_X e$ and regrouping gives $(\nabla^{LC}_X\phi)\cdot(e\otimes f) + \phi\cdot\nabla^{E\otimes F}_X(e\otimes f)$.
>
> *Dirac operator.* $D_{E\otimes F}(e\otimes f) = \sum_i e_i\cdot\nabla^{E\otimes F}_{e_i}(e\otimes f) = \sum_i (e_i\cdot\nabla^E_{e_i}e)\otimes f + \sum_i (e_i\cdot e)\otimes\nabla^F_{e_i}f = (D_E e)\otimes f + \sum_i(e_i\cdot e)\otimes\nabla^F_{e_i}f$.
>
> All three conditions hold and the module axiom is satisfied, so $E\otimes F$ is a Dirac bundle; its Dirac operator is $D_E\otimes 1$ plus the twisting term $\sum_i(e_i\cdot)\otimes\nabla^F_{e_i}$. $\blacksquare$

> [!warning] Illegal but tempting: acting with Clifford multiplication on the $F$-factor
> It is tempting to imagine that, to make $E\otimes F$ "more symmetric", Clifford multiplication should somehow involve $F$ as well. It must not. $F$ carries *no* $\mathrm{Cl}(M)$-module structure — it is merely a Hermitian bundle — so there is no action of $v$ on $f$ to speak of. Writing, say, $v\cdot(e\otimes f) = (v\cdot e)\otimes f + e\otimes(v\cdot f)$ is meaningless (the second term is undefined), and any attempt to define a Clifford action of $v$ on $F$ would generically fail the relation $v\cdot(v\cdot f) = -|v|^2 f$, breaking the module axiom. The construction is asymmetric on purpose: $F$ is the *coefficient* bundle, along for the ride, and this is exactly why twisting works for an *arbitrary* Hermitian bundle $F$ with unitary connection, with no compatibility with the Clifford structure required.

---

# Key Takeaways

**Twisting a Dirac bundle by a Hermitian bundle with unitary connection is a universal, structure-free operation, and its Dirac operator is the untwisted one plus a coupling term linear in the twisting connection.** The reusable principle is that the Dirac-bundle axioms partition cleanly: the module axiom and conditions (2), (3) speak only about Clifford multiplication, which the construction routes entirely through the $E$-factor, so they are inherited verbatim; condition (1), metricity, is the only axiom that sees $F$, and it is discharged by the single hypothesis that $\nabla^F$ is unitary. The trigger for recognising this pattern is any construction of the shape "tensor a structured bundle with a plain coefficient bundle", where the algebraic structure (here the Clifford action) is defined through one factor only: the verification will always reduce, factor by factor, to the axioms of the pieces. The transferable diagnostic is to ask, of each axiom, *which factor does it constrain?* — and to spend on each the minimal hypothesis about that factor. Here $F$ needs a metric (for the product metric and condition (2)) and a metric connection (for condition (1)); it needs nothing else, which is why $F$ may be *any* Hermitian bundle with unitary connection.

**The Dirac operator of a tensor product splits as $D_E\otimes 1$ plus a Clifford-contracted twisting term, and this is the origin of "coupling to a gauge field".** The computation $D_{E\otimes F} = D_E\otimes 1 + \sum_i (e_i\cdot)\otimes\nabla^F_{e_i}$ shows precisely how the extra connection $\nabla^F$ enters: linearly, through the Clifford contraction of $T^*M\otimes\operatorname{End}(F)$, with no second-order or cross terms. When $E = \slashed S$ and $F$ is associated to a principal bundle with connection $A$, replacing $A$ by $A + a$ changes $\nabla^F$ by $a$ and hence changes $\slashed D_A$ by exactly the twisted Clifford multiplication $a\cdot$ — this is the content of [[Thm - Variation of the Twisted and Spin-c Dirac Operators with the Connection|the variation formula]] $\slashed D_{A+a}\psi = \slashed D_A\psi + a\cdot\psi$, and it is what makes $\slashed D_A$ depend *affinely* on the gauge field, a fact on which the differential of the Seiberg–Witten map in [[Gauge Theory XI — Seiberg–Witten Theory|chapter XI]] rests. Whenever a first-order geometric operator is "coupled to a connection" in physics, this is the mechanism: contract the coupling connection into the operator's symbol.

**Verification-by-reduction to the factors is the standard method for closure statements, and the only skill it demands is bookkeeping of which hypothesis pays for which clause.** This exercise is a template: given a construction that combines structured objects, do not re-derive the target axioms from first principles; instead unfold each target axiom by one application of the construction's definitions until it becomes an axiom of a factor, then cite that axiom by name. The same pattern verifies that the [[Def - Clifford Bundle and Bundle of Clifford Modules|exterior bundle]] $\Lambda T^*M$ is a Dirac bundle, that a direct sum of Dirac bundles is a Dirac bundle, and that the pullback of a Dirac bundle under a Riemannian covering is one; in each case the work is entirely in matching hypotheses to clauses. The companion exercise [[Ex - Clifford Multiplication is Skew-Adjoint on a Dirac Bundle]] isolates the equivalent reformulation of condition (2) used implicitly here (that $v\cdot$ is skew-adjoint), and [[Ex - d plus d-star on Euclidean Space Squares to the Laplacian on Coefficients]] carries out the analogous frame computation for the Hodge–de Rham Dirac operator, where the "coefficient" structure is the Clifford grading of forms rather than a twisting bundle.
