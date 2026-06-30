---
type: definition
subject: special-relativity
prereqs:
  - "Def - Tensors on Minkowski Space"
  - "Def - Tensor Operations"
  - "Def - Metric Duality and Index Manipulation"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \mathrm{diag}(1,-1,-1,-1)$. $E$ is the four-dimensional vector space of [[Def - Minkowski Space and the Metric|Minkowski space]], $E^*$ its dual, $(e_\alpha)$ a basis with [[Def - Metric Duality and Index Manipulation|dual basis]] $(e^\alpha)$. $\mathscr{T}_{(0,p)}(E)$ is the space of type-$(0,p)$ [[Def - Tensors on Minkowski Space|tensors]] (multilinear forms eating $p$ vectors). $\mathscr{A}_p(E) \subseteq \mathscr{T}_{(0,p)}(E)$ denotes the space of $p$-forms. $\mathfrak{S}_p$ is the symmetric group on $p$ symbols; for $\sigma \in \mathfrak{S}_p$, $k(\sigma)$ is the number of transpositions in a decomposition of $\sigma$, so $(-1)^{k(\sigma)} = \mathrm{sgn}(\sigma)$ is its signature. Greek indices run $0$–$3$. Full registry on [[Special Relativity XVIII — Tensors, Alternate Forms and Hodge Duality]].

This is a compound page: it defines two interlocking notions — the **alternate ($p$-)form** and the **exterior (wedge) product** $\wedge$ — because the exterior product is the operation that makes the alternate forms a closed algebra, and the basis of $p$-forms cannot be built without it.

---

# Axiom Motivation

Among all [[Def - Tensors on Minkowski Space|tensors]], one subfamily is singled out by physics with surprising consistency: the **fully antisymmetric** ones. The angular momentum of a particle, the spin of a system, the four-torque, the four-rotation of an observer's [[Def - Local Frame and Four-Rotation|local frame]], and — decisively — the electromagnetic field are all antisymmetric type-$(0,2)$ tensors, and the [[Def - The Levi-Civita Tensor|Levi-Civita]] orientation tensor is an antisymmetric type-$(0,4)$ tensor. The motivation for this page is to ask *why antisymmetry is special* and to build the algebra those objects live in.

The deep reason antisymmetric forms matter is that they are the objects that **measure oriented volume**, and therefore the objects that **integrate over surfaces**. A $p$-form is the algebraic shadow of an oriented $p$-dimensional parallelepiped: it eats $p$ vectors and returns a signed number that flips when you swap two of them, exactly as the signed volume of a parallelepiped flips when you swap two edge-vectors (this is the determinant). A symmetric or generic tensor has no such interpretation. So if you want a quantity you can integrate over a curve, a surface, a hypersurface — flux, circulation, charge — it must be an alternate form, because only an alternate form transforms correctly under reparametrisation of the surface (the Jacobian determinant that appears is itself an alternating function). Antisymmetry is not a curiosity; it is the precondition for integration, which is why it recurs everywhere a flux or a circulation appears.

Why define a $p$-form by the condition "changes sign under any swap of two arguments" rather than some other antisymmetry? Because that condition is equivalent to "vanishes whenever two arguments are equal," and *that* is the geometrically meaningful statement: a parallelepiped with two coincident edges is degenerate and has zero volume. The two formulations are equivalent (set two arguments equal in the swap rule to get vanishing; conversely expand on a sum of two arguments to recover the swap), and the vanishing form is what forces the dimension count below. Demanding antisymmetry under *every* transposition (not just adjacent ones, not just some) is what makes the form fully alternating, which is what ties it to the determinant and to oriented volume.

Two consequences of the dimension of spacetime being $4$ are then forced, and they motivate the algebra. First, **there are no nonzero $p$-forms for $p > 4$**: a $p$-form's components $A_{\alpha_1\dots\alpha_p}$ vanish unless all $p$ indices are distinct, and in a four-dimensional space you cannot have five distinct values among $\{0,1,2,3\}$. So the exterior algebra is finite, capped at $p = 4$. Second, the dimensions are the binomial coefficients $\binom{4}{p} = 1,4,6,4,1$ — symmetric about $p=2$ — because an independent component is a choice of $p$ distinct indices out of $4$ up to order. This symmetry $\binom{4}{p} = \binom{4}{4-p}$ is precisely what later makes [[Def - The Hodge Star|Hodge duality]] possible: $\mathscr{A}_p$ and $\mathscr{A}_{4-p}$ have equal dimension, so there can be an isomorphism between them.

Finally, why a *new* product $\wedge$ rather than the ordinary [[Def - Tensor Operations|tensor product]] $\otimes$? Because $\otimes$ does not preserve antisymmetry: the tensor product of two alternate forms is generally not alternate. To stay inside $\mathscr{A}_\bullet(E)$ one must antisymmetrise the tensor product, and the result is the **exterior product**. The normalisation (the $1/p!q!$ in the definition) is chosen so that $\wedge$ is associative and so that the wedge of dual-basis one-forms $e^{\alpha_1}\wedge\cdots\wedge e^{\alpha_p}$ ($\alpha_1 < \cdots < \alpha_p$) is an honest basis of $\mathscr{A}_p(E)$ with the *same* components as the form has as a tensor. With this product the alternate forms become the **exterior algebra**, a closed graded algebra, and the determinant, the cross product, the curl, and the electromagnetic field all become expressible within it.

---

# The Definition

A tensor $A \in \mathscr{T}_{(0,p)}(E)$ (with $p \geq 2$) is an **alternate form**, or **$p$-form**, if it changes sign whenever any two of its arguments are interchanged — equivalently, if it is fully antisymmetric:
$$
A(\vec v_{\sigma(1)}, \dots, \vec v_{\sigma(p)}) = (-1)^{k(\sigma)}\, A(\vec v_1, \dots, \vec v_p) \quad\text{for all } \sigma \in \mathfrak{S}_p.
$$
Equivalently, $A$ vanishes whenever two arguments coincide. The set of $p$-forms is a vector subspace $\mathscr{A}_p(E) \subseteq \mathscr{T}_{(0,p)}(E)$. By convention $\mathscr{A}_1(E) := E^*$ (every linear form is a $1$-form) and $\mathscr{A}_0(E) := \mathbb{R}$. A $p$-form has antisymmetric components $A_{\alpha_1\dots\alpha_p} = A(e_{\alpha_1}, \dots, e_{\alpha_p})$, and
$$
\mathscr{A}_p(E) = \{0\} \text{ for } p > 4, \qquad \dim\mathscr{A}_p(E) = \binom{4}{p} = (1,4,6,4,1) \text{ for } p = 0,1,2,3,4.
$$
Every $4$-form is proportional to the [[Def - The Levi-Civita Tensor|Levi-Civita tensor]]: $\forall A \in \mathscr{A}_4(E),\ \exists\lambda\in\mathbb{R},\ A = \lambda\varepsilon$.

**Exterior product.** The **exterior product** (or **wedge product**) is the map $\wedge : \mathscr{A}_p(E) \times \mathscr{A}_q(E) \to \mathscr{A}_{p+q}(E)$, $(A,B) \mapsto A\wedge B$, defined by the antisymmetrised tensor product
$$
(A\wedge B)(\vec v_1, \dots, \vec v_{p+q}) := \frac{1}{p!\,q!}\sum_{\sigma\in\mathfrak{S}_{p+q}} (-1)^{k(\sigma)}\, A(\vec v_{\sigma(1)}, \dots, \vec v_{\sigma(p)})\, B(\vec v_{\sigma(p+1)}, \dots, \vec v_{\sigma(p+q)}).
$$
For two one-forms ($p = q = 1$) this is
$$
a\wedge b = a\otimes b - b\otimes a, \qquad (a\wedge b)(\vec v, \vec w) = \langle a,\vec v\rangle\langle b,\vec w\rangle - \langle a,\vec w\rangle\langle b,\vec v\rangle, \qquad (a\wedge b)_{\mu\nu} = a_\mu b_\nu - a_\nu b_\mu.
$$
The wedge product is **associative**, $A\wedge(B\wedge C) = (A\wedge B)\wedge C$, and **graded-commutative**:
$$
\boxed{\ B\wedge A = (-1)^{pq}\, A\wedge B\ } \qquad (A \in \mathscr{A}_p,\ B \in \mathscr{A}_q).
$$
In particular two one-forms anticommute, $b\wedge a = -a\wedge b$, so $a\wedge a = 0$; a one-form and a two-form commute, $a\wedge B = B\wedge a$.

**Basis of $p$-forms.** The wedge products of dual-basis one-forms, taken with strictly increasing indices, form a basis of $\mathscr{A}_p(E)$, and any $p$-form expands as
$$
A = \frac{1}{p!}\, A_{\alpha_1\dots\alpha_p}\, e^{\alpha_1}\wedge\cdots\wedge e^{\alpha_p} = \sum_{\alpha_1 < \cdots < \alpha_p} A_{\alpha_1\dots\alpha_p}\, e^{\alpha_1}\wedge\cdots\wedge e^{\alpha_p},
$$
with the *same* numbers $A_{\alpha_1\dots\alpha_p}$ as its components as a type-$(0,p)$ tensor. Explicitly, a $2$-form is $A = \tfrac{1}{2}A_{\alpha\beta}\, e^\alpha\wedge e^\beta = \sum_{\alpha<\beta} A_{\alpha\beta}\, e^\alpha\wedge e^\beta$. The basis monomials are
$$
\mathscr{A}_1 : (e^0, e^1, e^2, e^3); \quad
\mathscr{A}_2 : (e^0\wedge e^1, e^0\wedge e^2, e^0\wedge e^3, e^1\wedge e^2, e^1\wedge e^3, e^2\wedge e^3); \quad
\mathscr{A}_4 : (e^0\wedge e^1\wedge e^2\wedge e^3).
$$

---

# Categorical / Structural Definition

$\mathscr{A}_p(E)$ is the $p$-th **exterior power** $\Lambda^p E^*$, the antisymmetric part of $(E^*)^{\otimes p}$, and $\bigoplus_{p=0}^{4}\mathscr{A}_p(E) = \Lambda^\bullet E^*$ is the **exterior algebra** of $E^*$ — the universal associative algebra generated by $E^*$ subject to $a\wedge a = 0$ for every $a \in E^*$. The universal property is: any linear map $f : E^* \to \mathcal A$ into an associative algebra $\mathcal A$ with $f(a)^2 = 0$ extends uniquely to an algebra homomorphism $\Lambda^\bullet E^* \to \mathcal A$. The wedge product is the multiplication of this algebra; graded-commutativity $B\wedge A = (-1)^{pq}A\wedge B$ and the truncation at $p = \dim E = 4$ are structural consequences of the relation $a\wedge a = 0$ together with $\dim E^* = 4$.

The dimensions $\dim\Lambda^p E^* = \binom{4}{p}$ are the binomial coefficients because a basis monomial is a choice of $p$ distinct generators out of $4$; the total dimension $\sum_p\binom{4}{p} = 2^4 = 16$. The symmetry $\binom{4}{p} = \binom{4}{4-p}$ is the equality $\dim\Lambda^p E^* = \dim\Lambda^{4-p}E^*$ that makes the [[Def - The Hodge Star|Hodge star]] an isomorphism. Antisymmetrisation $(E^*)^{\otimes p} \to \Lambda^p E^*$ is the projector $\mathrm{Alt} = \frac{1}{p!}\sum_\sigma \mathrm{sgn}(\sigma)\,\sigma$, and the wedge product is $A\wedge B = \frac{(p+q)!}{p!q!}\,\mathrm{Alt}(A\otimes B)$ — the normalisation in the definition is exactly what implements this projector while keeping the basis components unchanged.

This is the flat, single-fibre case of the **bundle of differential forms** $\Lambda^p T^*M$ over a manifold; a [[Def - Exterior Derivative on a Manifold|differential p-form]] is a smooth section of it, and the algebra here is the fibrewise algebra of [[Differential Geometry VIII — Differential Forms|differential forms]].

---

# Relate to Other Fields / Compression

The exterior algebra is the home of the **determinant**: the top form $e^0\wedge e^1\wedge e^2\wedge e^3$ is one-dimensional, and a linear map $L$ acts on it by multiplication by $\det L$ — that is the basis-free definition of the determinant. In three dimensions the wedge of two one-forms encodes the **cross product** (via [[Def - Metric Duality and Index Manipulation|metric duality]] and the [[Def - The Levi-Civita Tensor|Levi-Civita]] tensor), and the exterior derivative of a one-form encodes the **curl**. The whole of vector calculus — gradient, curl, divergence — is the exterior derivative acting on $0$-, $1$-, and $2$-forms, with the metric used to translate between forms and vector fields. In relativity the payoff is that the electromagnetic field is a $2$-form $F$, its potential a $1$-form $A$, and Maxwell's equations the cleanest statements in the exterior algebra.

**True name:** a $p$-form is *the algebraic measurer of oriented $p$-volume — the thing that eats $p$ vectors, returns the signed volume of the parallelepiped they span, and therefore integrates over $p$-surfaces*; the wedge product is *the antisymmetrised tensor product, the unique associative product keeping you inside the alternate forms*. The reflexes installed: whenever you see a quantity to be integrated over a $p$-dimensional surface (flux, circulation, charge), it is a $p$-form; whenever you wedge a thing with itself, you get zero; whenever you swap two factors in a wedge, you pick up $(-1)$ for each pair of odd-degree factors crossing.

---

# Examples / Corollaries

**Is an instance — the electromagnetic field.** The field-strength $F \in \mathscr{A}_2(E)$ is an antisymmetric type-$(0,2)$ tensor; its six independent components $F_{\alpha\beta}$ ($\alpha < \beta$) are the three components of the electric field and three of the magnetic field relative to an observer. Its $2$-form character is why it integrates over surfaces to give flux; see [[Special Relativity XXI — The Electromagnetic Field]].

**Is an instance — the Levi-Civita tensor.** $\varepsilon \in \mathscr{A}_4(E)$ is the top-degree form, spanning the one-dimensional space $\mathscr{A}_4(E)$; every $4$-form is a scalar multiple of it.

**Is an instance — a wedge of basis forms.** $e^0\wedge e^1$ is a $2$-form with components $(e^0\wedge e^1)_{\mu\nu} = \delta^0_\mu\delta^1_\nu - \delta^1_\mu\delta^0_\nu$: it is $+1$ on $(e_0, e_1)$, $-1$ on $(e_1, e_0)$, and $0$ otherwise.

**Is NOT an instance — the metric.** $g$ is a type-$(0,2)$ tensor but is *symmetric*, $g_{\alpha\beta} = g_{\beta\alpha}$, hence **not** a $2$-form. Not all bilinear forms are $2$-forms: a $2$-form must be antisymmetric (Gourgoulhon's Remark 14.5). The symmetric and antisymmetric parts of a bilinear form are independent.

**Is NOT an instance — a $5$-form.** There is no nonzero alternate form of degree $5$ on a four-dimensional space: $\mathscr{A}_5(E) = \{0\}$, because five distinct indices cannot be chosen from four values. The exterior algebra stops at $p = 4$.

**Corollary — a one-form wedged with itself vanishes.** $a\wedge a = (-1)^{1\cdot 1}a\wedge a = -a\wedge a$, so $a\wedge a = 0$. More generally any odd-degree form squares to zero under $\wedge$.

**Corollary — the wedge of two one-forms in components.** $(a\wedge b)_{\mu\nu} = a_\mu b_\nu - a_\nu b_\mu$, manifestly antisymmetric; its six independent entries are the "bivector" spanned by $a$ and $b$.

**Calibration check.** If you have understood the definitions you can: (i) compute $\dim\mathscr{A}_2(E) = 6$ and list the basis $2$-forms; (ii) verify $a\wedge b = -b\wedge a$ for one-forms and conclude $a\wedge a = 0$; (iii) explain why the symmetric metric $g$ is not a $2$-form while the antisymmetric field $F$ is.

---

# Unlocked by This

> [!tip] The Levi-Civita Tensor and the Top Form *(from §18.3)*
> Because $\dim\mathscr{A}_4(E) = 1$, there is essentially one $4$-form up to scale, and fixing it (with the help of the [[Def - Minkowski Space and the Metric|metric]] and an [[Def - Spacetime Orientation|orientation]]) is the choice of the [[Def - The Levi-Civita Tensor|Levi-Civita tensor]] $\varepsilon$ — the volume form of Minkowski space. Everything about orientation and duality flows from this one-dimensionality.

> [!tip] The Hodge Star and Self-Duality *(from §18.3)*
> The symmetry $\dim\mathscr{A}_p = \dim\mathscr{A}_{4-p}$ is what permits the [[Def - The Hodge Star|Hodge star]] $\star : \mathscr{A}_p \to \mathscr{A}_{4-p}$. On $2$-forms it is an automorphism with $\star^2 = -1$, and the resulting splitting into self-dual and anti-self-dual parts is the $\mathbf{E} \pm i\mathbf{B}$ decomposition of the electromagnetic field; see [[Thm - Orthogonal Decomposition of 2-Forms]].

> [!tip] The Exterior Derivative and de Rham Cohomology *(from Electromagnetism and Topology)*
> Promoting alternate forms to fields and adding the [[Def - Exterior Derivative on a Manifold|exterior derivative]] $d$ (which raises degree by one, with $d^2 = 0$) gives the **de Rham complex**, whose cohomology measures the topology of spacetime. Maxwell's homogeneous equations are $dF = 0$, and the existence of a potential $F = dA$ is the statement that the relevant cohomology vanishes; see [[Special Relativity XX — Integration in Spacetime and Stokes' Theorem]] and [[Special Relativity XXII — Maxwell's Equations]].
