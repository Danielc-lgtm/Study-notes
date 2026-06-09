---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Ring"
  - "Def - Ideal"
  - "Def - Module"
  - "Def - Submodule"
  - "Def - Polynomial Ring"
  - "Def - Finitely Generated Module"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. A graded ring is written $A = \bigoplus_{n \geq 0} A_n$, the symbol $\bigoplus$ meaning an *internal* direct sum: every $a \in A$ has a unique expression $a = \sum_n a_n$ with $a_n \in A_n$ and all but finitely many $a_n$ equal to $0$. The piece $A_n$ is the **degree-$n$ component**; its elements (and $0$) are the **homogeneous elements of degree $n$**, written $\deg(a_n) = n$. We write $A_+ = \bigoplus_{n \geq 1} A_n$ for the **irrelevant ideal**. A graded module is $M = \bigoplus_{n \geq 0} M_n$ with components $M_n$. The standard example throughout is the [[Def - Polynomial Ring|polynomial ring]] $k[T_1, \dots, T_r]$ graded by total degree. The full registry is on [[Commutative Algebra XI — Graded Rings and the Artin-Rees Lemma]].

This is a compound page: it defines three interlocking notions — the **graded ring** $A = \bigoplus A_n$, the **graded $A$-module** $M = \bigoplus M_n$, and the **homogeneous component** of an element — because they are introduced together and none is fully usable without the others. The graded module is the natural representation theory of the graded ring; the homogeneous components are the coordinates in which both live.

---

# Axiom Motivation

A grading is bookkeeping made into structure. You already grade things without naming it: a polynomial $f = 3 + T_1 - 5T_1 T_2^2$ in $k[T_1, T_2]$ splits naturally into its constant part $3$, its linear part $T_1$, and its cubic part $-5T_1 T_2^2$, and when you multiply two polynomials the degrees add. The definition of a graded ring is nothing more than the demand that this splitting-by-degree be available abstractly, in a ring where there are no "variables" to read a degree off of. We want to record, for each element, *which degrees it is built from*, and we want the ring multiplication to respect that record. Watching what "respect" must mean is the whole content.

**Why the decomposition must be a direct sum, $A = \bigoplus_n A_n$.** The first axiom says every element decomposes into homogeneous pieces and the decomposition is unique. Uniqueness is the load-bearing half. If we only asked that $A = \sum_n A_n$ (each element is *some* sum of homogeneous pieces) without uniqueness, the notion of "the degree-$n$ part of $a$" would be ill-defined — the same element could be written $a = a_2 + a_3$ and $a = a_2' + a_3'$ with $a_2 \neq a_2'$, and then "extract the degree-$2$ component" is not a function. The projection maps $a \mapsto a_n$ onto each component are the single most-used operation on a graded ring (every proof on this page and the next applies one), and they exist *only because* the sum is direct. Drop directness and you keep a ring with a spanning family of subgroups but lose every degree argument. So the axiom is not "elements have homogeneous parts" but "elements have *unique* homogeneous parts".

**Why the multiplication must satisfy $A_m A_n \subseteq A_{m+n}$ ("degrees add").** This is the axiom that couples the grading to the ring structure, and without it the grading is inert. The desideratum is that the projections behave like derivations of degree: the degree-$d$ part of a product should be computable from the homogeneous parts of the factors, the way the cubic part of $fg$ comes only from (constant $\times$ cubic) $+$ (linear $\times$ quadratic) $+ \dots$. The clean way to guarantee this is to demand that a degree-$m$ element times a degree-$n$ element is *purely* of degree $m+n$. Suppose we weakened it to $A_m A_n \subseteq \bigoplus_{k \leq m+n} A_k$ (products can drop degree but not raise it, a "filtered" rather than "graded" condition): then the degree-$n$ piece of a product is no longer determined by matching degrees, and the associated-graded machinery of the next pages collapses, because the multiplication on $\bigoplus \mathfrak{a}^n/\mathfrak{a}^{n+1}$ is *defined* by "multiply representatives and keep the top degree", which needs degrees to add on the nose. The exact equality of degree is what makes "the degree-$n$ part of a product" a well-defined bilinear pairing $A_m \times A_n \to A_{m+n}$.

**Why $A_0$ is forced to be a subring, and why $1 \in A_0$.** These are not extra axioms — they are *consequences*, and seeing that they are forced is the test that the two axioms above are the right ones. Closure $A_0 A_0 \subseteq A_{0+0} = A_0$ is immediate from "degrees add", so $A_0$ is closed under multiplication. That $1 \in A_0$ takes one line and is worth doing because it is surprising: write $1 = \sum_{i=0}^m y_i$ with $y_i \in A_i$. For any homogeneous $z_n \in A_n$, the equation $z_n = 1 \cdot z_n = \sum_i y_i z_n$ has left side purely in degree $n$ while $y_i z_n \in A_{n+i}$; matching the degree-$n$ components forces $y_0 z_n = z_n$ and $y_i z_n = 0$ for $i > 0$. Taking $z_n$ to range over all homogeneous elements gives $y_0 a = a$ for all $a$, so $y_0 = 1$ and the higher pieces $y_i$ vanish: $1 \in A_0$. The payoff is structural: each $A_n$ is then an $A_0$-module (it absorbs multiplication by $A_0$ since $A_0 A_n \subseteq A_n$), so a graded ring is an $A_0$-algebra assembled out of $A_0$-modules, one in each degree. This is the frame for everything: **a graded ring is a tower of $A_0$-modules glued by a degree-additive multiplication.**

**Why we grade by $\mathbb{N}$ and not $\mathbb{Z}$, and why a module gets its *own* grading.** We index by $n \geq 0$ because the motivating examples — polynomial rings, the associated graded ring, the Rees algebra — have no negative degrees, and the $\mathbb{N}$-grading is what makes $A_+ = \bigoplus_{n \geq 1} A_n$ an ideal (it is the kernel of the projection $A \to A_0$ killing all positive degrees) and what makes finiteness arguments terminate. For a graded module $M = \bigoplus_{n \geq 0} M_n$ the compatibility axiom is $A_m M_n \subseteq M_{m+n}$: the ring's degrees act by *shifting* the module's degrees. The module needs its own grading rather than inheriting one because the same ring acts on many modules with different degree-distributions — this is exactly the freedom that lets the [[Def - The Hilbert Function and Hilbert Polynomial|Hilbert function]] $n \mapsto \dim_{A_0} M_n$ carry geometric information about $M$ that $A$ alone does not see.

---

# The Definition

## Graded ring

A **graded ring** is a [[Def - Ring|ring]] $A$ together with a family $(A_n)_{n \geq 0}$ of additive subgroups of $A$ such that
$$A = \bigoplus_{n=0}^{\infty} A_n \quad \text{(internal direct sum)} \qquad \text{and} \qquad A_m A_n \subseteq A_{m+n} \ \text{ for all } m, n \geq 0.$$
Here $A_m A_n$ denotes the set of finite sums of products $xy$ with $x \in A_m$, $y \in A_n$. The elements of $A_n$ are the **homogeneous elements of degree $n$**; a general element $a$ has a unique decomposition $a = \sum_n a_n$ into **homogeneous components** $a_n \in A_n$, almost all zero. As shown above, $A_0$ is a subring containing $1$, and each $A_n$ is an $A_0$-module.

The **irrelevant ideal** is $A_+ = \bigoplus_{n \geq 1} A_n$; it is the kernel of the projection $A \to A_0$, $\sum_n a_n \mapsto a_0$, hence an ideal of $A$, with $A/A_+ \cong A_0$.

## Graded module

Let $A = \bigoplus_{n \geq 0} A_n$ be a graded ring. A **graded $A$-module** is an [[Def - Module|$A$-module]] $M$ together with a family $(M_n)_{n \geq 0}$ of additive subgroups such that
$$M = \bigoplus_{n=0}^{\infty} M_n \qquad \text{and} \qquad A_m M_n \subseteq M_{m+n} \ \text{ for all } m, n \geq 0.$$
Each $M_n$ is then an $A_0$-module. An element $x \in M_n$ is **homogeneous of degree $n$**; every $y \in M$ has a unique decomposition $y = \sum_n y_n$ into homogeneous components $y_n \in M_n$, almost all zero.

A **homomorphism of graded $A$-modules** is an [[Def - Module Homomorphism|$A$-module homomorphism]] $f : M \to N$ that *preserves degree*: $f(M_n) \subseteq N_n$ for all $n$. (More generally one allows degree-shifting maps $f(M_n) \subseteq N_{n+d}$, a map "of degree $d$", but the default is $d = 0$.)

---

# Categorical / Structural Definition

A grading is exactly an action of the monoid $(\mathbb{N}, +)$ "by degrees". Concretely, an $\mathbb{N}$-grading on an abelian group is a direct-sum decomposition indexed by $\mathbb{N}$, and the compatibility axioms $A_m A_n \subseteq A_{m+n}$, $A_m M_n \subseteq M_{m+n}$ say the multiplication and action are *graded maps*: they send the $(m,n)$ summand of the tensor product into the $(m+n)$ summand of the target. Equivalently, a graded ring is a monoid object in the category of $\mathbb{N}$-graded abelian groups, where the tensor product carries the convolution grading $(V \otimes W)_d = \bigoplus_{m+n=d} V_m \otimes W_n$, and a graded module is a module object over it.

The cleanest categorical packaging, and the one that makes the geometry inevitable: an $\mathbb{N}$-grading on $A$ is the *same data* as an action of the multiplicative monoid of the affine line on $\operatorname{Spec} A$, an element $\lambda$ acting on a degree-$n$ homogeneous element $x$ by $\lambda \cdot x = \lambda^n x$. The fixed structure of this scaling action is precisely what the **Proj** construction extracts to build a projective variety from $A$, and what the grading on the **associated graded ring** records as the scaling toward a point. The grading is the algebra of a scaling symmetry.

---

# Relate to Other Fields / Compression

The cleanest compression: **a graded ring is a ring in which every element knows its own degree, and multiplication adds degrees.** The polynomial ring is the universal instance, and a general graded ring is what you get by abstracting "degree" away from "number of variables multiplied".

**True name:** for problem-solving, the operational form of "$A$ is graded" is *"there is a degree-projection $a \mapsto a_n$ onto each $A_n$, and it is multiplicative in the sense that the degree-$d$ part of a product matches degrees: $(ab)_d = \sum_{m+n=d} a_m b_n$".* Almost every argument with graded rings is "compare homogeneous components of an equation degree by degree" — when you see an equation between graded elements, project onto a fixed degree and you have replaced one equation by infinitely many simpler ones. This is the graded analogue of "compare coefficients" in a power series.

The construction is the algebraic skeleton of two geometric objects. First, a graded ring generated in degree one over a field is the **homogeneous coordinate ring** of a projective variety: the variety is $\operatorname{Proj} A$, recovered from $A$ by remembering only the scaling-invariant data, exactly as projective space $\mathbb{P}^{r-1}$ is $\operatorname{Proj} k[T_1, \dots, T_r]$. Second, the grading on the associated graded ring $\operatorname{gr}_{\mathfrak{m}}(R) = \bigoplus \mathfrak{m}^n/\mathfrak{m}^{n+1}$ is the algebraic record of *infinitesimal scaling toward a point*, and its $\operatorname{Proj}$ is the projectivized tangent cone — the cone of limiting directions of the variety at that point. In both cases the grading is the algebra of a $\mathbb{G}_m$-scaling.

---

# Examples / Corollaries

**Is an instance — the polynomial ring by total degree.** Let $A = k[T_1, \dots, T_r]$ and $A_n$ the $k$-span of all monomials $T_1^{e_1} \cdots T_r^{e_r}$ with $e_1 + \dots + e_r = n$ (together with $0$): the homogeneous polynomials of degree $n$. Then $A = \bigoplus_n A_n$ because every polynomial splits uniquely into its degree-$n$ parts, and $A_m A_n \subseteq A_{m+n}$ because the product of a degree-$m$ and a degree-$n$ monomial has degree $m+n$. Here $A_0 = k$ and $\dim_k A_n = \binom{n+r-1}{r-1}$. This is the prototype, and the [[Def - The Hilbert Function and Hilbert Polynomial|Hilbert function]] of this grading is the entry point to dimension theory.

**Is an instance — a nonstandard grading.** On $A = k[T_1, T_2]$ declare $\deg'(T_1^{e_1} T_2^{e_2}) = e_1 + 2e_2$ instead of $e_1 + e_2$. The components $A_n$ (the $\deg'$-homogeneous polynomials of weight $n$) still satisfy both axioms — weights add under multiplication — so this is a perfectly good grading, just with $\dim_k A_n$ following a different, eventually-quasi-polynomial pattern (see [[Ex - A nonstandard grading and its Hilbert function]]). Gradings are *choices*, and different weightings of the same ring produce genuinely different graded structures. This is the source of weighted projective spaces.

**Is an instance — any ring, trivially graded.** Any ring $A$ is graded with $A_0 = A$ and $A_n = 0$ for $n > 0$. Then $A_+ = 0$ and every element is homogeneous of degree $0$. This degenerate grading is what makes ungraded statements special cases of graded ones, and it is why the trivial grading on $A_0$ is always lurking inside $A$ via the subring $A_0$.

**Is NOT an instance — $\mathbb{Z}$ with $\mathbb{Z}_0 = \mathbb{Z}$, $\mathbb{Z}_1 = \mathbb{Z}$.** Suppose one tried to grade $\mathbb{Z}$ by putting *every* integer into both degree $0$ and degree $1$. This fails the direct-sum axiom: an integer would have two homogeneous expressions, so the decomposition is not unique and the degree-projection is undefined. A family of subgroups spanning the ring is not a grading unless the sum is *direct*. This is the non-example that pins down why uniqueness, not mere spanning, is the axiom.

**Is NOT an instance — a filtered ring that is not graded.** The ring $R = k[T]$ with subgroups $F_n = (T^n) = \{$ polynomials with all terms of degree $\geq n \}$ is *filtered* ($F_m F_n \subseteq F_{m+n}$ and $F_n \supseteq F_{n+1}$) but is not graded by the $F_n$: the $F_n$ are nested, not complementary, so $R \neq \bigoplus F_n$. Filtration is the weaker, "degrees add but pieces overlap" cousin; passing from a filtration to its associated graded ring is exactly the act of forcing a filtered ring to become graded (see [[Def - The Associated Graded Ring and the Rees Algebra]]).

**Calibration check.** Confirm that in any graded ring $1 \in A_0$ by the degree-matching argument, and deduce $A_0$ is a subring and each $A_n$ an $A_0$-module. Check that the projection $A \to A_0$ has kernel $A_+ = \bigoplus_{n \geq 1} A_n$, so $A_+$ is an ideal with $A/A_+ \cong A_0$. Finally verify $(ab)_d = \sum_{m+n=d} a_m b_n$ from the two axioms, and use it to show that a homogeneous element is a zero-divisor in $A$ if and only if it is a zero-divisor "against homogeneous elements".

---

# Unlocked by This

> [!tip] Projective varieties and the Proj construction *(from Algebraic Geometry)*
> A graded ring $A = \bigoplus_{n \geq 0} A_n$, finitely generated **in degree one** over a field $A_0 = k$, is the **homogeneous coordinate ring** of a **projective variety** $\operatorname{Proj} A$. The points of $\operatorname{Proj} A$ are the homogeneous prime ideals not containing the irrelevant ideal $A_+$; the grading is what implements the rule "scale all coordinates together and get the same point". The model is $A = k[T_0, \dots, T_r]$, whose Proj is projective space $\mathbb{P}^r_k$. Generation in degree one is exactly the condition that $\operatorname{Proj} A$ comes with a **projective embedding** into some $\mathbb{P}^r$ — the degree-one piece $A_1$ supplies the coordinate functions. This is why the next theorem, that a graded ring is Noetherian if and only if it is finitely generated, is the algebraic gateway to projective geometry: it says exactly the projective varieties are the ones with finitely many homogeneous coordinates.

> [!tip] The tangent cone of a variety at a point *(from Algebraic Geometry)*
> When the grading comes from the powers of a [[Def - Prime and Maximal Ideal|maximal ideal]] $\mathfrak{m}$, the graded ring $\operatorname{gr}_{\mathfrak{m}}(R) = \bigoplus_n \mathfrak{m}^n/\mathfrak{m}^{n+1}$ is the coordinate ring of the **tangent cone** of the variety $\operatorname{Spec} R$ at the point $\mathfrak{m}$ — the cone of all limiting secant directions through the point, the best conical approximation to the variety there. The degree-one piece $\mathfrak{m}/\mathfrak{m}^2$ is the **cotangent space**, so the linear part of the tangent cone is the tangent space; the higher degrees record how the variety curves away from its tangent space. A smooth point has tangent cone equal to its tangent space (a linear subspace); a singular point has a genuinely conical, higher-degree tangent cone — a node, for instance, has the union of its two branch directions. The grading is the engine that turns the filtration by order of vanishing into this geometric cone.

> [!tip] Weighted projective space *(from Algebraic Geometry)*
> A *nonstandard* grading — assigning weights $w_1, \dots, w_r$ to the variables, $\deg(T_i) = w_i$ — produces the homogeneous coordinate ring of a **weighted projective space** $\mathbb{P}(w_1, \dots, w_r)$, where points are identified under the scaling $(x_1, \dots, x_r) \sim (\lambda^{w_1} x_1, \dots, \lambda^{w_r} x_r)$. These spaces have orbifold singularities exactly where the weights fail to be coprime, and the failure of the Hilbert function to be eventually polynomial (only eventually quasi-polynomial) — the phenomenon of [[Ex - A nonstandard grading and its Hilbert function]] — is the arithmetic shadow of this.
