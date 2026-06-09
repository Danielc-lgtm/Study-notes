---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Algebra over a Ring (R-algebra)"
  - "Def - Ring Homomorphism"
  - "Def - Tensor Product of Modules"
  - "Thm - Standard Isomorphisms of Tensor Products"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$; ring homomorphisms send $1\mapsto 1$. Let $R$ be a ring and $B, C$ (also $A$) be [[Def - Algebra over a Ring (R-algebra)|$R$-algebras]], i.e. rings equipped with structure maps $R\to B$, $R\to C$. We write $B\otimes_R C$ for their tensor product as $R$-modules ([[Def - Tensor Product of Modules]]), with pure tensors $b\otimes c$; $m_B : B\otimes_R B\to B$, $m_C : C\otimes_R C\to C$ for the linearised multiplications; $i_B : B\to B\otimes_R C$, $b\mapsto b\otimes 1$ and $i_C : C\to B\otimes_R C$, $c\mapsto 1\otimes c$ for the structure maps; and $\rho : R\to B$ for the algebra structure map of $B$. The full registry is on [[Commutative Algebra II — Tensor Products]].

---

# Axiom Motivation

We have two rings $B$ and $C$, both built over a common base ring $R$ (each has a structure map from $R$), and we want to *combine* them into a single ring. The combination should contain commuting copies of $B$ and $C$, should be as economical as possible, and — this is the design goal that determines everything — should be the **coproduct** of $R$-algebras: the universal ring receiving compatible maps from both $B$ and $C$. The $R$-module $B\otimes_R C$ already contains symbols $b\otimes 1$ and $1\otimes c$ for the two copies; the whole content of this page is to put a *multiplication* on it that makes those copies into subrings and the result universal.

**Why the multiplication must be $(b\otimes c)(b'\otimes c') = bb'\otimes cc'$.** We want $b\otimes 1$ to behave like $b$ and $1\otimes c$ like $c$, with the two copies commuting. Then a general pure tensor factors as $b\otimes c = (b\otimes 1)(1\otimes c)$, and the product of two pure tensors is forced:
$$(b\otimes c)(b'\otimes c') = (b\otimes 1)(1\otimes c)(b'\otimes 1)(1\otimes c') = (b\otimes 1)(b'\otimes 1)(1\otimes c)(1\otimes c') = bb'\otimes cc',$$
where the middle step *assumes the two copies commute*. So the formula is not a choice — it is the only multiplication compatible with "two commuting copies of $B$ and $C$". The reason it needs *proof* rather than mere definition is that a tensor can be written as a sum of pure tensors in many ways, so "multiply pure tensors by this rule and extend bilinearly" must be checked to be well-defined. This is done by assembling the multiplication from the linearised multiplications $m_B, m_C$ through the standard isomorphism $(B\otimes C)\otimes(B\otimes C)\cong(B\otimes B)\otimes(C\otimes C)$ — the universal property guarantees the result is well-defined, which is exactly why we route through it rather than defining things on representatives.

**Why the structure map sends $r\mapsto r(1\otimes 1)$, and the trap $r\otimes r$.** The base $R$ should map into $B\otimes_R C$ compatibly with both copies. The map $r\mapsto r(1\otimes 1)$ does this, and by sliding scalars ([[Def - Tensor Product of Modules|the tensor relations]]) $r(1\otimes 1) = (r\cdot 1)\otimes 1 = r\otimes 1 = 1\otimes r$ — going in through $B$ or through $C$ gives the *same* element. This agreement is what makes $B\otimes_R C$ an unambiguous $R$-algebra. The tempting error is to write the image as $r\otimes r$; but $r\otimes r = r(1\otimes r) = r\cdot r(1\otimes 1) = r^2(1\otimes 1)$, which doubles the scalar. A scalar from $R$ enters on *one* side only (either side, they coincide); putting it on both squares it. This is precisely why $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ is two-dimensional over $\mathbb{C}$, not one: the two complex structures are independent, not identified by the $\mathbb{R}$-scalars.

**What goes wrong if $R$ is not in the middle.** The construction is *over $R$* — the tensor is $\otimes_R$, and the relations identify $rb\otimes c$ with $b\otimes rc$ only for $r$ in the image of $R$. Change the base ring and you change the ring you get: $\mathbb{C}\otimes_{\mathbb{C}}\mathbb{C}\cong\mathbb{C}$ (one copy, since complex scalars slide freely), but $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$ (two copies, since only real scalars slide). The base ring is the "amount of identification" you are willing to make; the smaller it is, the larger and more reducible $B\otimes_R C$ becomes. Dropping the requirement that both algebras be over the *same* $R$ makes the construction meaningless — there would be no common scalars to tensor over.

**Why "coproduct" is the right universal property and not "product".** A product would be the universal ring *mapping to* both $B$ and $C$; that is $B\times C$, with componentwise operations. We instead want the universal ring *receiving maps from* both — and that is $B\otimes_R C$. The distinction is geometric: under the algebra–geometry dictionary, ring maps reverse arrows, so the algebra coproduct $B\otimes_R C$ is the *space-level product* (fibre product) of $\mathbf{Spec}\,B$ and $\mathbf{Spec}\,C$. Demanding the coproduct universal property — and checking $h(a\otimes b) = f_1(a)f_2(b)$ is the unique algebra map — is what pins down the multiplication as the right one, and is verified on [[Thm - Universal Property of the Tensor Product of Algebras]].

---

# The Definition

Let $R$ be a commutative ring and $B, C$ be $R$-algebras.

## The ring structure

The $R$-module $B\otimes_R C$ ([[Def - Tensor Product of Modules]]) is made a commutative ring by the multiplication determined on pure tensors by
$$(b\otimes c)(b'\otimes c') = bb'\otimes cc',$$
extended $R$-bilinearly. Concretely, this map is the composite
$$(B\otimes_R C)\otimes_R(B\otimes_R C)\ \xrightarrow{\ \cong\ }\ (B\otimes_R B)\otimes_R(C\otimes_R C)\ \xrightarrow{\ m_B\otimes m_C\ }\ B\otimes_R C,$$
where the first map is the standard rearrangement $(b\otimes c)\otimes(b'\otimes c')\mapsto(b\otimes b')\otimes(c\otimes c')$ and $m_B, m_C$ are the linearised multiplications. The identity element is $1_{B\otimes C} = 1_B\otimes 1_C$.

## The algebra structure

$B\otimes_R C$ is an $R$-algebra via the structure ring homomorphism
$$R\to B\otimes_R C, \qquad r\mapsto r(1\otimes 1) = r\otimes 1 = 1\otimes r.$$
It is simultaneously a $B$-algebra via $i_B : B\to B\otimes_R C$, $b\mapsto b\otimes 1$, and a $C$-algebra via $i_C : C\to B\otimes_R C$, $c\mapsto 1\otimes c$; both ring homomorphisms restrict to the displayed $R$-algebra structure. Note $r(1\otimes 1)$ equals both $r\otimes 1$ and $1\otimes r$ but **not** $r\otimes r$ in general.

## The upgrading lemma

To verify that an $R$-linear map out of (or involving) $B\otimes_R C$ is an $R$-algebra homomorphism, it suffices to check it on a generating set: if $f : A\to A'$ is $R$-linear between $R$-algebras, $S\subseteq A$ generates $A$ as an $R$-module, $f(1) = 1$, and $f(s_1 s_2) = f(s_1)f(s_2)$ for all $s_1, s_2\in S$, then $f$ is an $R$-algebra homomorphism. Since $\{a\otimes b\}$ generates $B\otimes_R C$, multiplicativity need only be checked on pure tensors.

---

# Categorical / Structural Definition

$B\otimes_R C$ is the **coproduct** of $B$ and $C$ in the category of commutative $R$-algebras. The structure maps $i_B : B\to B\otimes_R C$ and $i_C : C\to B\otimes_R C$ are the coproduct injections, and the [[Thm - Universal Property of the Tensor Product of Algebras|universal property]] says: for any $R$-algebra $D$ and $R$-algebra maps $f_1 : B\to D$, $f_2 : C\to D$, there is a unique $R$-algebra map $h : B\otimes_R C\to D$ with $h\circ i_B = f_1$, $h\circ i_C = f_2$, namely $h(b\otimes c) = f_1(b)f_2(c)$. A coproduct is the "freest" object receiving maps from both factors; in other categories it takes other forms — disjoint union in sets, free product in groups, [[Def - Direct Sum of Modules|direct sum]] in modules. Dually, under the algebra–geometry correspondence (ring maps reverse to space maps), the coproduct of algebras is the **fibre product of spaces**: $\mathbf{Spec}(B\otimes_R C) = \mathbf{Spec}\,B\times_{\mathbf{Spec}\,R}\mathbf{Spec}\,C$.

---

# Relate to Other Fields / Compression

The cleanest compression: **$B\otimes_R C$ glues two rings along their common base, and geometrically it is the product of the two spaces they define.** Tensoring polynomial rings unites their variable sets; tensoring quotient rings unites their relations.

**True name:** the true name of $B\otimes_R C$ is *"the coproduct of $R$-algebras"* — the universal ring with commuting copies of $B$ and $C$. Operationally: to build a map *out of* $B\otimes_R C$, give two algebra maps $B\to D$, $C\to D$; to identify $B\otimes_R C$, recognise the candidate as the coproduct.

In **algebraic geometry** this is the fibre product / product of varieties: $\mathbf{Spec}(A\otimes_R B) = \mathbf{Spec}\,A\times_{\mathbf{Spec}\,R}\mathbf{Spec}\,B$, with $R[X_*]\otimes_R R[T_*]\cong R[X_*,T_*]$ realising $\mathbb{A}^n\times\mathbb{A}^r = \mathbb{A}^{n+r}$. In **field theory**, for $A = R[X]/(f)$ one has $A\otimes_R B\cong B[X]/(\bar f)$, so the tensor product is a field iff $f$ stays irreducible over $B$ and splits into a product when $f$ factors — the mechanism behind $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$ and the theory of separable/étale algebras. In **representation theory** the tensor product of group algebras $k[G]\otimes_k k[H]\cong k[G\times H]$ is how the representations of a product group are built.

---

# Examples / Corollaries

**Is an instance — polynomial algebras glue variables.** $R[X_1,\dots,X_n]\otimes_R R[T_1,\dots,T_r]\cong R[X_1,\dots,X_n,T_1,\dots,T_r]$ as $R$-algebras, with $a\otimes b\mapsto ab$ on pure tensors (see [[Ex - Tensor product of polynomial algebras]]). Geometrically $\mathbb{A}^n\times\mathbb{A}^r = \mathbb{A}^{n+r}$. The quotient version glues relations: $R[X_*]/I\otimes_R R[T_*]/J\cong R[X_*,T_*]/(I^e + J^e)$.

**Is an instance — extension of an algebra along the base.** $S\otimes_R R[T_1,\dots,T_n]\cong S[T_1,\dots,T_n]$ as $S$-algebras, sending $s\otimes p\mapsto s\tilde f(p)$ where $\tilde f(p)$ applies the structure map to each coefficient; for $R\to\mathbb{C}$ this is $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{R}[T]\cong\mathbb{C}[T]$. This is base change of a polynomial algebra.

**Is NOT an instance of a field — $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$.** Although $\mathbb{C}$ is a field, $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}[X]/(X^2+1)\cong\mathbb{C}[X]/(X-i)(X+i)\cong\mathbb{C}\times\mathbb{C}$ is **not** a field: it has the zero divisors and idempotents of a product (see [[Ex - C tensor R C is not a field]]). The tensor product of fields over a smaller field is generally a product of fields, not a field — the algebra of a point that splits after base change.

**Is NOT $r\otimes r$ — the scalar trap.** In $B\otimes_R C$ the image of $r\in R$ is $r\otimes 1 = 1\otimes r$, *not* $r\otimes r$; indeed $r\otimes r = r^2(1\otimes 1)$. Putting a base scalar on both sides squares it. This is why $\dim_{\mathbb{C}}(\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}) = 2$, not $1$.

**Corollary — $A\otimes_R B$ distributes over finite products.** $A\otimes_R(B\times C)\cong(A\otimes_R B)\times(A\otimes_R C)$, hence $A\otimes_R B^n\cong(A\otimes_R B)^n$. This is the algebra-level shadow of distributivity of $\otimes$ over [[Def - Direct Sum of Modules|direct sums]], upgraded to a ring isomorphism by the upgrading lemma, and it is how $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$ ramifies into further splittings.

**Calibration check.** Verify $(b\otimes c)(b'\otimes c') = bb'\otimes cc'$ gives $1_B\otimes 1_C$ as the identity and is commutative. Confirm $r\otimes 1 = 1\otimes r$ but $r\otimes r = r^2(1\otimes1)$. Show $R[X]\otimes_R R[T]\cong R[X,T]$ on the monomial basis. Finally, compute $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ as $\mathbb{C}[X]/(X^2+1)$ and split it into $\mathbb{C}\times\mathbb{C}$, identifying the two idempotents.

---

# Unlocked by This

> [!tip] The fibre product of schemes *(from Algebraic Geometry)*
> $\mathbf{Spec}(B\otimes_R C) = \mathbf{Spec}\,B\times_{\mathbf{Spec}\,R}\mathbf{Spec}\,C$: the algebra tensor product *is* the fibre product of affine schemes, and gluing fibre products of affines builds the fibre product of general schemes. The product of varieties, base change of a variety, and the fibre of a morphism over a point are all this construction. The coproduct universal property of $B\otimes_R C$ is the (arrow-reversed) universal property of the fibre product.

> [!tip] Separable and étale algebras *(from Galois Theory / Algebraic Geometry)*
> A finite field extension $L/K$ is **separable** exactly when $L\otimes_K\bar K\cong\bar K\times\cdots\times\bar K$ is a product of copies of $\bar K$ (one per embedding); more generally an algebra is **étale** when it becomes a product of fields after base change to the separable closure. The splitting $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$ is the $\mathbb{R}$-point of $\mathbf{Spec}\,\mathbb{C}$ splitting into its two geometric (Galois-conjugate) points.

> [!tip] Hopf algebras and group schemes *(from Representation Theory)*
> The tensor product of algebras provides the multiplication of $k[G]\otimes_k k[H]\cong k[G\times H]$ and, dually, the comultiplication $\Delta : A\to A\otimes_k A$ that turns a coordinate ring into a **Hopf algebra** when $\mathbf{Spec}\,A$ is a group. Group schemes and their representation theory are built on the algebra tensor product.
