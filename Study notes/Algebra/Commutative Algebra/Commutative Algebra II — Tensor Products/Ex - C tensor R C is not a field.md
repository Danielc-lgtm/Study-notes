---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Tensor Product of Algebras"
  - "Thm - Universal Property of the Tensor Product of Algebras"
  - "Thm - Standard Isomorphisms of Tensor Products"
  - "Def - Ideal"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Show that, although $\mathbb{C}$ is a field, the tensor product of $\mathbb{R}$-algebras
$$\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$$
is **not** a field. Concretely, prove
$$\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\ \cong\ \mathbb{C}\times\mathbb{C}\quad\text{as }\mathbb{C}\text{-algebras},$$
exhibit explicit zero divisors and nontrivial idempotents, and explain the geometric meaning: a single $\mathbb{R}$-point splitting into two $\mathbb{C}$-points (failure of *geometric irreducibility*). Use the presentation $\mathbb{C} = \mathbb{R}[X]/(X^2+1)$ and the general fact $A\otimes_R B\cong B[X]/(\bar f)$ for $A = R[X]/(f)$.

**Recall:**

The objects in play are the tensor product of algebras, its coproduct universal property, and the quotient isomorphism for algebras.

![[Def - Tensor Product of Algebras#The Definition]]

The key general fact, an instance of the algebra quotient isomorphism: for $A = R[X]/(f)$ and any $R$-algebra $B$,
$$A\otimes_R B = \big(R[X]/(f)\big)\otimes_R B\ \cong\ B[X]/(\bar f),$$
where $\bar f$ is $f$ with coefficients pushed into $B$. This follows from $R[X]\otimes_R B\cong B[X]$ ([[Thm - Universal Property of the Tensor Product of Algebras|coproduct of polynomial algebras]]) and the quotient rule ([[Thm - Standard Isomorphisms of Tensor Products|standard isomorphisms]]): tensoring kills the relation $(f)$, becoming $(\bar f)$ over $B$.

The **Chinese Remainder Theorem** for a polynomial ring over a field: if $\bar f = g_1 g_2$ with $g_1, g_2$ coprime, then $B[X]/(\bar f)\cong B[X]/(g_1)\times B[X]/(g_2)$. A nonzero ring with zero divisors (such as a product $\mathbb{C}\times\mathbb{C}$) is not a [[Def - Ideal|field]].

---

# Convergent Strategy

**Problem class.** This is an *identify-a-tensor-product-of-algebras-concretely* problem, and it is the canonical example that a tensor product of fields need not be a field. As the [[Commutative Algebra II — Tensor Products#Problem-Solving Strategy|topic strategy]] records, an algebra presented as a quotient ($\mathbb{C} = \mathbb{R}[X]/(X^2+1)$) routes through $R[X]/(f)\otimes_R B\cong B[X]/(\bar f)$, after which the *factorisation of $\bar f$ over $B$* decides the structure.

**Assumption pattern.** The trigger is *a field given as a simple extension $R[X]/(f)$ with $f$ irreducible over $R$ but possibly reducible over $B$*. Here $f = X^2+1$ is irreducible over $\mathbb{R}$ (so $\mathbb{C}$ is a field) but factors as $(X-i)(X+i)$ over $\mathbb{C}$. The base change $\otimes_{\mathbb{R}}\mathbb{C}$ moves $f$ into $\mathbb{C}[X]$, where it splits — and a polynomial that splits gives a *product* of rings, never a field.

**Theorem routing.** The route is: write $\mathbb{C} = \mathbb{R}[X]/(X^2+1)$; apply $A\otimes_R B\cong B[X]/(\bar f)$ with $B = \mathbb{C}$ to get $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}[X]/(X^2+1)$; factor $X^2+1 = (X-i)(X+i)$ over $\mathbb{C}$; apply the Chinese Remainder Theorem to get $\mathbb{C}[X]/(X-i)\times\mathbb{C}[X]/(X+i)\cong\mathbb{C}\times\mathbb{C}$; read off zero divisors and idempotents from the product.

**Key decision point.** Two non-obvious points. First, *which copy of $\mathbb{C}$ supplies the variable $X$ and which supplies the coefficients* — the asymmetry is only apparent; $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ is symmetric, but presenting the *left* factor as $\mathbb{R}[X]/(X^2+1)$ and base-changing along the *right* breaks the symmetry usefully, turning the tensor into a polynomial ring over the right factor. Second, *the reason this is not a field is exactly the splitting of $f$*: the idempotents $\tfrac{1}{2}(1\pm\tfrac{X}{i})$ (equivalently the images of $\tfrac{1}{2}(1\mp i\otimes i)$) are the algebraic fingerprint of "two points", and recognising the idempotents *as* the two factors is the conceptual core. The geometric reading — $\operatorname{Spec}\mathbb{C}$ is one $\mathbb{R}$-point but two $\mathbb{C}$-points — is what "$\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$" *means*.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra II — Tensor Products#Legal Operations|the topic page's Legal Operations]]:

1. **Push $\otimes$ through a quotient (operation 5).** $\mathbb{R}[X]/(X^2+1)\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}[X]/(X^2+1)$ — tensoring carries the relation $(X^2+1)$ into $\mathbb{C}[X]$.

2. **Invoke the coproduct universal property for algebras (operation 9).** $\mathbb{R}[X]\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}[X]$ identifies the polynomial-ring base change.

3. **Build an isomorphism by maps both ways / via a known structure (operation 4).** The CRT isomorphism $\mathbb{C}[X]/(X^2+1)\cong\mathbb{C}\times\mathbb{C}$ is established by the coprime factorisation.

4. **Confirm $r\otimes r\neq r(1\otimes 1)$ (illegal-operation 4 awareness).** The two-dimensionality of $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ over $\mathbb{C}$ is exactly because the two complex structures are independent, not identified.

---

# Hints

> [!note]- Hint 1
> Present the *left* factor as a quotient: $\mathbb{C} = \mathbb{R}[X]/(X^2+1)$. Then $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C} = (\mathbb{R}[X]/(X^2+1))\otimes_{\mathbb{R}}\mathbb{C}$. What does tensoring a quotient algebra over $\mathbb{R}$ with $\mathbb{C}$ do to the relation $X^2+1$?

> [!note]- Hint 2
> $R[X]/(f)\otimes_R B\cong B[X]/(\bar f)$: tensoring with $B$ moves the polynomial ring and its relation into $B[X]$. So $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}[X]/(X^2+1)$, a polynomial ring over $\mathbb{C}$ modulo $X^2+1$.

> [!note]- Hint 3
> Over $\mathbb{C}$, $X^2+1$ factors: $X^2+1 = (X-i)(X+i)$, and $(X-i), (X+i)$ are coprime in $\mathbb{C}[X]$. Apply the Chinese Remainder Theorem to split the quotient into a product.

> [!note]- Hint 4
> $\mathbb{C}[X]/(X-i)\cong\mathbb{C}$ (evaluate at $X = i$) and similarly for $X+i$. So $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$. The idempotents $(1,0)$ and $(0,1)$ pull back to nontrivial idempotents; their product is $0$, so they are zero divisors — and a ring with zero divisors is not a field.

---

# Solution

The proof base-changes a presentation of $\mathbb{C}$ and reads off the splitting. Step 1 rewrites $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ as $\mathbb{C}[X]/(X^2+1)$; Step 2 factors $X^2+1$ over $\mathbb{C}$ and applies CRT to get $\mathbb{C}\times\mathbb{C}$; Step 3 exhibits the explicit zero divisors and idempotents; Step 4 gives the geometric interpretation. The non-obvious move is breaking the symmetry by presenting one factor as a quotient, so that base change converts the tensor into a polynomial ring whose defining polynomial visibly splits.

**Step 1: $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}[X]/(X^2+1)$.**

Presenting the left factor as $\mathbb{R}[X]/(X^2+1)$ and base-changing gives a polynomial ring over $\mathbb{C}$.

> [!note]- Derivation
> Write $\mathbb{C} = \mathbb{R}[X]/(X^2+1)$ (the left factor). By the [[Thm - Universal Property of the Tensor Product of Algebras|coproduct property]], $\mathbb{R}[X]\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}[X]$ (the polynomial ring over $\mathbb{C}$ is the coproduct of $\mathbb{R}[X]$ and $\mathbb{C}$ over $\mathbb{R}$). Tensoring the [[Thm - Standard Isomorphisms of Tensor Products|quotient]] $\mathbb{R}[X]/(X^2+1)$ with $\mathbb{C}$ carries the relation ideal $(X^2+1)\subseteq\mathbb{R}[X]$ to its extension $(X^2+1)\subseteq\mathbb{C}[X]$:
> $$\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C} = \big(\mathbb{R}[X]/(X^2+1)\big)\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}[X]/(X^2+1).$$
> Concretely, the isomorphism sends $(p(x)+(X^2+1))\otimes z\mapsto z\cdot p(X) + (X^2+1)$, where $x = X + (X^2+1)$ is the generator of the left $\mathbb{C}$. As a $\mathbb{C}$-vector space this is $2$-dimensional (basis $1, X$), confirming $\dim_{\mathbb{C}}(\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}) = 2$ — *not* $1$, because the two complex structures are independent (the trap $i\otimes 1 = 1\otimes i$ is false; $i\otimes 1$ and $1\otimes i$ are different elements, corresponding to $i$ and $X$).

**Step 2: Factor $X^2+1$ over $\mathbb{C}$ and split via CRT.**

$X^2+1 = (X-i)(X+i)$ with coprime factors, so $\mathbb{C}[X]/(X^2+1)\cong\mathbb{C}\times\mathbb{C}$.

> [!note]- Derivation
> Over $\mathbb{C}$, $X^2+1 = (X-i)(X+i)$. The factors $X-i$ and $X+i$ are coprime in $\mathbb{C}[X]$: their difference is $2i\neq 0$, a unit, so $(X-i) + (X+i) = \mathbb{C}[X]$. By the **Chinese Remainder Theorem**,
> $$\mathbb{C}[X]/(X^2+1)\cong\mathbb{C}[X]/(X-i)\times\mathbb{C}[X]/(X+i).$$
> Evaluation at $X = i$ gives $\mathbb{C}[X]/(X-i)\cong\mathbb{C}$, and at $X = -i$ gives $\mathbb{C}[X]/(X+i)\cong\mathbb{C}$. Hence
> $$\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$$
> as $\mathbb{C}$-algebras. The isomorphism sends the class of $p(X)$ to $(p(i), p(-i))$.

**Step 3: Explicit zero divisors and idempotents.**

$\mathbb{C}\times\mathbb{C}$ has the orthogonal idempotents $(1,0), (0,1)$, which are zero divisors; pulled back, $e_\pm = \tfrac12(1\otimes 1\mp i\otimes i)$.

> [!note]- Derivation
> In $\mathbb{C}\times\mathbb{C}$, the elements $(1,0)$ and $(0,1)$ are nontrivial **idempotents** ($(1,0)^2 = (1,0)$) and **zero divisors** ($(1,0)(0,1) = (0,0)$ with neither factor zero). A field has no zero divisors and no idempotents besides $0, 1$, so $\mathbb{C}\times\mathbb{C}$ — and hence $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ — is **not a field**.
>
> Pulling back through the isomorphisms, the idempotent $(1,0)$ corresponds to the class of $\tfrac{X-(-i)}{i-(-i)} = \tfrac{X+i}{2i}$ in $\mathbb{C}[X]/(X^2+1)$, which is the Lagrange interpolation idempotent. In $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$, writing $x = i\otimes 1$ (the left $i$) and $y = 1\otimes i$ (the right $i$), the two idempotents are
> $$e_+ = \tfrac12(1\otimes1 - x y^{-1})\quad\text{i.e.}\quad e_\pm = \tfrac12\big(1\otimes1\ \mp\ i\otimes i\big)\cdot(\pm\text{sign convention}),$$
> satisfying $e_+ + e_- = 1\otimes1$, $e_+ e_- = 0$, $e_\pm^2 = e_\pm$. Concretely $(i\otimes1)(i\otimes1) = i^2\otimes1 = -1\otimes1$ but $(i\otimes1)(1\otimes i) = i\otimes i\neq -1\otimes 1$ — the two square roots of $-1$ are independent, and that independence is precisely what produces the splitting.

**Step 4: Geometric meaning — failure of geometric irreducibility.**

$\operatorname{Spec}\mathbb{C}$ is one point over $\mathbb{R}$ but two points over $\mathbb{C}$.

> [!note]- Derivation
> Under the algebra–geometry dictionary, $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ is the coordinate ring of the **fibre product** $\operatorname{Spec}\mathbb{C}\times_{\operatorname{Spec}\mathbb{R}}\operatorname{Spec}\mathbb{C}$, i.e. the base change of the $\mathbb{R}$-point $\operatorname{Spec}\mathbb{C}$ to $\mathbb{C}$. Over $\mathbb{R}$, $\operatorname{Spec}\mathbb{C}$ is a *single* point (the maximal ideal $(X^2+1)$ of $\mathbb{R}[X]$ is irreducible). After base change to $\mathbb{C}$, it becomes $\operatorname{Spec}(\mathbb{C}\times\mathbb{C})$ — **two** points, corresponding to the two embeddings $\mathbb{C}\hookrightarrow\mathbb{C}$ (the identity and complex conjugation), equivalently the two roots $\pm i$ of $X^2+1$. This is the prototypical *failure of geometric irreducibility*: an $\mathbb{R}$-variety that is irreducible over $\mathbb{R}$ can split into several components over the algebraic closure, and the number of components is counted by the Galois-conjugate embeddings. More generally, $L\otimes_K\bar K\cong\bar K^{[L:K]}$ for a separable extension $L/K$ — the tensor product detects how a single point spreads out after base change.

> [!note]- Complete formal solution
> **Claim.** $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$, which is not a field.
>
> Write $\mathbb{C} = \mathbb{R}[X]/(X^2+1)$. Then
> $$\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}[X]/(X^2+1)$$
> by $R[X]/(f)\otimes_R B\cong B[X]/(\bar f)$. Over $\mathbb{C}$, $X^2+1 = (X-i)(X+i)$ with coprime factors, so by CRT
> $$\mathbb{C}[X]/(X^2+1)\cong\mathbb{C}[X]/(X-i)\times\mathbb{C}[X]/(X+i)\cong\mathbb{C}\times\mathbb{C},$$
> the last by evaluation at $\pm i$. The product $\mathbb{C}\times\mathbb{C}$ has nontrivial idempotents $(1,0), (0,1)$ and zero divisors $(1,0)(0,1) = 0$, so it is not a field. Geometrically, the single $\mathbb{R}$-point $\operatorname{Spec}\mathbb{C}$ splits into the two $\mathbb{C}$-points $\operatorname{Spec}(\mathbb{C}\times\mathbb{C})$ after base change — the failure of geometric irreducibility. $\blacksquare$

---

# Key Takeaways

**A tensor product of fields is rarely a field — the structure is dictated by how the defining polynomial factors after base change.** The headline lesson, and the reason this example is canonical, is that $A\otimes_R B$ for $A = R[X]/(f)$ becomes $B[X]/(\bar f)$, and *the factorisation of $\bar f$ over $B$ controls everything*: $\bar f$ irreducible $\Rightarrow$ a field; $\bar f$ a product of distinct coprime factors $\Rightarrow$ a product of fields (by CRT); $\bar f$ with a repeated factor $\Rightarrow$ a non-reduced ring with nilpotents. The trigger for spaced recall: whenever you tensor two field extensions over a common subfield, *do not assume the result is a field* — present one as $K[X]/(f)$ and factor $f$ over the other. This is the gateway to separable and étale algebras: $L\otimes_K\bar K\cong\bar K\times\cdots\times\bar K$ (one factor per $K$-embedding) is precisely the statement that $L/K$ is separable, and the number of factors is $[L:K]$.

**The two complex structures are independent — $\dim_{\mathbb{C}}(\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}) = 2$, not $1$, because $i\otimes 1\neq 1\otimes i$.** The seductive error is to think the two $i$'s should be identified, collapsing the tensor to $\mathbb{C}$. They are not: a base scalar from $\mathbb{R}$ slides across $\otimes$, but the *imaginary units* of the two factors are different elements ($x = i\otimes 1$ and $y = 1\otimes i$ satisfy $x^2 = y^2 = -1$ but $x\neq\pm y$). The independence of these two square roots of $-1$ is exactly the source of the splitting — the idempotents $\tfrac12(1\mp xy^{-1})$ exist precisely because $x$ and $y$ are not forced equal. The transferable diagnostic: in $B\otimes_R C$, only scalars from the *common base $R$* slide; structure internal to $B$ and to $C$ stays separate, which is why the tensor product can be much larger and more reducible than either factor. This is the same warning as illegal-operation 4 on the [[Commutative Algebra II — Tensor Products#Legal Operations|topic page]] ($r\otimes r\neq r(1\otimes1)$).

**Base change can break irreducibility — a single point over the small field becomes several over the large one, counted by Galois conjugates.** The geometric content is that $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$ is one $\mathbb{R}$-point spreading into two $\mathbb{C}$-points, and this is the universal phenomenon of *geometric reducibility*: a variety irreducible over its field of definition can decompose after base change to the algebraic closure, with the components permuted by the Galois group. The diagnostic for spaced practice: when an algebra $A$ over $R$ is a domain (or $\operatorname{Spec}A$ is irreducible) but $A\otimes_R\bar R$ is a product, the variety is *not geometrically irreducible*, and the number of geometric components measures the "arithmetic" of $A$ — how many ways the defining data factors over $\bar R$. This is why extension of scalars to the algebraic closure ([[Thm - Extension of Scalars and the Adjunction|base change]]) is the standard tool for separating "arithmetic" from "geometric" properties, and it foreshadows the role of the tensor product as the fibre product $\operatorname{Spec}(A\otimes_R B) = \operatorname{Spec}A\times_{\operatorname{Spec}R}\operatorname{Spec}B$ in [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz|the Nullstellensatz chapter]].
