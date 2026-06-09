---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Ring"
  - "Def - Ring Homomorphism"
  - "Def - Module"
  - "Def - Subring"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$, and ring homomorphisms send $1 \mapsto 1$. Let $R$ be a ring. An [[Def - Ring Homomorphism|$R$-algebra]] carries a **structural homomorphism** $\rho : R \to A$; for $r \in R$ and $x \in A$ we abbreviate $rx := \rho(r)x$ (the product in $A$ of $\rho(r)$ with $x$). We write $1_A$ for the identity of $A$, $\operatorname{End}(M)$ for the [[Def - Module|endomorphism]] ring of an abelian group $M$, and $R[T_1, \dots, T_n]$ for the [[Def - Polynomial Ring|polynomial algebra]]. The zero ring is $\{0\}$, the unique ring with $1 = 0$. The full registry is on [[Commutative Algebra I — Chain Conditions]].

This is a compound page: it defines two interlocking notions — the **$R$-algebra** (a ring $A$ with a fixed map $\rho : R \to A$) and the **$R$-algebra homomorphism** (a ring map respecting the two structural maps) — because the morphism is what gives the definition its teeth, and "ring containing $R$" is *not* an adequate substitute precisely because it forgets $\rho$ and hence forgets the morphisms.

---

# Axiom Motivation

The goal is to capture "a ring built on top of $R$" — a ring $A$ in which we may multiply not only by elements of $A$ but also, coherently, by elements of $R$. You already have the analogous notion one level down: a [[Def - Module|module]] is "an abelian group built on top of $R$", where $R$ acts by a ring homomorphism $R \to \operatorname{End}(M)$. The $R$-algebra is the same idea with the abelian group $M$ upgraded to a *ring* $A$, and the question that defines the concept is: *what is the cleanest data making a ring into an "$R$-object"?*

**Why a ring homomorphism $\rho : R \to A$ is exactly the right data.** A module $M$ is an abelian group with an action of $R$, and the action is packaged as a ring homomorphism $R \to \operatorname{End}(M)$ — each $r$ becomes an endomorphism $m \mapsto rm$, and the ring-homomorphism axioms ($r$ acts additively, $rs$ acts as $r$ then $s$, $1$ acts as identity) are exactly module-action axioms. Now upgrade $M$ to a ring $A$. The action of $r$ should still be "multiply by something", but now $A$ has its *own* multiplication, so the natural source of "multiply by $r$" is multiplication by a chosen element $\rho(r) \in A$. For this to be coherent — for $rx$ to distribute, for $(rs)x = r(sx)$, for $1 \cdot x = x$, and crucially for $r$ to interact correctly with $A$'s own multiplication — the assignment $r \mapsto \rho(r)$ must be a **ring homomorphism** $R \to A$. So the defining data is not a second multiplication but a *single ring homomorphism* $\rho : R \to A$, and the abbreviation $rx := \rho(r)x$ recovers the $R$-action. The whole definition is: "an $R$-algebra is a ring $A$ with a chosen ring homomorphism from $R$."

**Why this is genuinely more than a module structure.** Every $R$-algebra is automatically an $R$-module: from $\rho : R \to A$ build $R \to \operatorname{End}(A, +)$ by $r \mapsto (x \mapsto \rho(r)x)$, which is a ring homomorphism into the endomorphisms of the additive group, hence a module structure. But the algebra carries *strictly more* information than this underlying module, because $\rho$ lands in a *ring* and must respect *multiplication* — $\rho(rs) = \rho(r)\rho(s)$ — a constraint that a mere module action never sees. The superficial similarity to a module ("specify a homomorphism out of $R$") hides the real difference: for a module the target is $\operatorname{End}(M)$ and one only needs additive compatibility on $M$; for an algebra the target is the ring $A$ itself and one needs full multiplicative compatibility. This is exactly the gap between "$A$ is an $R$-module" and "$A$ is an $R$-algebra".

**Why $\rho(r) = r \cdot 1_A$, and why this declutters but does not trivialise.** A pleasant simplification: since $\rho$ is a ring homomorphism, $\rho(r) = \rho(r) \cdot 1_A = r \cdot 1_A$ in the abbreviated notation, so the structural map is *determined* by where $1_A$ sits — there is at most one $R$-algebra structure refining a given "$R$ acts on $1_A$" rule. This lets one drop $\rho$ from the notation and just write $r \cdot 1_A$. But it would be a mistake to conclude $\rho$ is redundant: the point is that $\rho$ is *part of the data*, and two different choices of "where $R$ goes" give two different algebras even on the same ring. The simplification says the data is economical (one homomorphism), not that it is absent.

**Why "a ring containing $R$" is the wrong definition — the role of the morphism.** It is tempting to define an $R$-algebra as "a ring $A$ that contains $R$ as a subring", and for non-zero algebras over a *field* $k$ this is even nearly accurate ($\rho$ is then injective, so $A$ does contain a copy of $k$). But this throws away $\rho$, and with it the notion of *morphism*. An **$R$-algebra homomorphism** must be a ring map $\varphi : A \to B$ compatible with the two structural maps, $\varphi \circ \rho_A = \rho_B$ — it must send $r \cdot 1_A$ to $r \cdot 1_B$ for every $r$. The same ring can be an $R$-algebra in genuinely different ways, with genuinely different morphisms: make $\mathbb{C}$ a $\mathbb{C}$-algebra once via $\rho = \operatorname{id}$ and once via $\rho = $ complex conjugation; then the identity map $\mathbb{C} \to \mathbb{C}$ is a ring isomorphism but *not* a $\mathbb{C}$-algebra homomorphism between these two structures, because it fails $\varphi \circ \rho_{\text{conj}} = \rho_{\text{id}}$. The "ring containing $k$" definition cannot even express this distinction, and that failure is the precise reason the structural map $\rho$ must be carried explicitly. The morphism is where the definition earns its keep.

---

# The Definition

Let $R$ be a ring.

## $R$-algebra

An **$R$-algebra** is a ring $A$ together with a fixed ring homomorphism
$$\rho : R \longrightarrow A,$$
the **structural homomorphism**. For $r \in R$, $x \in A$ one writes $rx := \rho(r)x$. Since $\rho(r) = r \cdot 1_A$, the structure is determined by $\rho$, and $\rho$ may be suppressed in notation.

Every $R$-algebra $A$ is in particular an $R$-module, via $r \cdot x := \rho(r)x$; the module structure forgets the multiplication on $A$. Two basic facts:

- **Every ring is a $\mathbb{Z}$-algebra in exactly one way**, because there is a unique ring homomorphism $\mathbb{Z} \to A$ (sending $1 \mapsto 1_A$, hence $n \mapsto n \cdot 1_A$).
- **A non-zero $k$-algebra over a field $k$ contains a copy of $k$**: the structural map $\rho : k \to A$ has $\rho(1) = 1_A \neq 0$, so $\ker \rho$ is a proper ideal of $k$; but a field has only the ideals $0$ and $k$, so $\ker \rho = 0$ and $\rho$ is injective.

## Subalgebra

A **subalgebra** of an $R$-algebra $A$ is a [[Def - Subring|subring]] $B \subseteq A$ such that $rx \in B$ for all $r \in R$, $x \in B$ (equivalently, $B$ contains $\rho(R) = \{r \cdot 1_A : r \in R\}$). For a subset $S \subseteq A$, the **subalgebra generated by $S$** is the smallest subalgebra containing $S$; it consists of all $p(x_1, \dots, x_m)$ with $p \in R[T_1, \dots, T_m]$ and $x_1, \dots, x_m \in S$.

## $R$-algebra homomorphism

For $R$-algebras $(A, \rho_A)$ and $(B, \rho_B)$, an **$R$-algebra homomorphism** is a ring homomorphism $\varphi : A \to B$ with
$$\varphi \circ \rho_A = \rho_B,$$
equivalently $\varphi(r \cdot 1_A) = r \cdot 1_B$ for all $r \in R$. Equivalently again, $\varphi$ is an $R$-linear map with $\varphi(1_A) = 1_B$ and $\varphi(a_1 a_2) = \varphi(a_1)\varphi(a_2)$.

---

# Categorical / Structural Definition

The clean categorical statement is that an **$R$-algebra is an object of the coslice (under) category $R \downarrow \mathbf{CRing}$** — a ring $A$ equipped with a morphism *from* $R$. An $R$-algebra homomorphism is a morphism in this coslice: a ring map $\varphi : A \to B$ making the triangle with $\rho_A, \rho_B$ commute. This single sentence explains every feature of the definition:

- The structural map $\rho$ is the morphism *from $R$*, carried as data — exactly why it cannot be forgotten.
- A $\mathbb{Z}$-algebra is just a ring, because $\mathbb{Z}$ is the **initial object** of $\mathbf{CRing}$ (unique map from $\mathbb{Z}$ to any ring), so $\mathbb{Z} \downarrow \mathbf{CRing} \cong \mathbf{CRing}$.
- The polynomial algebra $R[T_1, \dots, T_n]$ is the **free $R$-algebra** on $n$ generators: it satisfies the universal property that an $R$-algebra map out of it to any $A$ is the *same data* as a choice of $n$ elements of $A$ (the images of the $T_i$). This is the algebra-level analogue of "a module map out of a free module is a choice of images of the basis", and it is what makes Hilbert's basis theorem reduce to polynomial rings.

The functor forgetting the multiplication, $R\text{-}\mathbf{Alg} \to R\text{-}\mathbf{Mod}$, is the precise sense in which "every algebra is a module"; it has a left adjoint, the **tensor algebra** (symmetric algebra in the commutative case), which freely builds an algebra from a module.

---

# Relate to Other Fields / Compression

The cleanest compression: **an $R$-algebra is a ring under $R$ — a ring $A$ with a chosen map $R \to A$ — exactly as a module is an abelian group under $R$, with the difference that $\rho$ must respect multiplication.** The slogan is "module : abelian group :: algebra : ring", with $R$ acting through a homomorphism in both cases.

**True name:** for problem-solving, an $R$-algebra is **"a ring $A$ together with the recipe $r \mapsto r \cdot 1_A$ for multiplying by scalars from $R$"**, and an algebra map is **"a ring map that is also $R$-linear"** — the operative content is always "respect both the ring structure and the $R$-action". When you need maps *out of* a polynomial algebra, recall the free property: such a map is just a choice of images for the variables.

The notion appears wherever a base object acts on a structured object: a $k$-algebra in linear algebra is a vector space with a compatible multiplication (matrix algebras, group algebras, the Weyl algebra); a $C^\infty(M)$-algebra in geometry is a sheaf of functions; the structural map $\rho : k \to A$ is the algebraic shadow of "constants embed in functions". In algebraic geometry the *anti*-equivalence between finitely generated reduced $k$-algebras and affine varieties is the foundational dictionary — and the structural map $\rho : k \to A$ corresponds to the map from a variety to a point. The morphism-respecting-$\rho$ condition is what makes that dictionary an *equivalence of categories* rather than a loose correspondence.

---

# Examples / Corollaries

**Is an instance — the polynomial algebra $R[T_1, \dots, T_n]$.** With $\rho : R \to R[T_1, \dots, T_n]$ the inclusion of constants, this is the prototypical $R$-algebra and the free one on $n$ generators. It is an $R$-algebra and an $R$-module; it is finitely generated as an *algebra* (by the $T_i$) but, for $n \geq 1$, *not* as a module (it needs the infinite basis of monomials).

**Is an instance — any ring as a $\mathbb{Z}$-algebra.** Every ring $A$ is uniquely a $\mathbb{Z}$-algebra via the unique map $\mathbb{Z} \to A$, $n \mapsto n \cdot 1_A$. So "$\mathbb{Z}$-algebra" and "ring" are interchangeable; this is why theorems about $R$-algebras specialise to theorems about rings by taking $R = \mathbb{Z}$.

**Is an instance — $\mathbb{C}$ as an $\mathbb{R}$-algebra.** The inclusion $\rho : \mathbb{R} \hookrightarrow \mathbb{C}$ makes $\mathbb{C}$ an $\mathbb{R}$-algebra; here $\rho$ is injective (as it must be over a field), and $\mathbb{C}$ *is* finitely generated both as an $\mathbb{R}$-algebra (by $i$) and as an $\mathbb{R}$-module (basis $1, i$) — the case where the two notions of finite generation agree, because $i$ is integral over $\mathbb{R}$.

**Is NOT a well-posed $R$-algebra structure without specifying $\rho$ — $\mathbb{C}$ "as a $\mathbb{C}$-algebra".** The ring $\mathbb{C}$ admits (at least) two distinct $\mathbb{C}$-algebra structures: $\rho_1 = \operatorname{id}$ and $\rho_2 = $ complex conjugation. These are different algebras: the identity map $\mathbb{C} \to \mathbb{C}$ is a ring isomorphism but is a $\mathbb{C}$-algebra homomorphism $(\mathbb{C}, \rho_2) \to (\mathbb{C}, \rho_1)$ only if $\operatorname{id} \circ \rho_2 = \rho_1$, i.e. conjugation $= $ identity, which is false. This is the example that refutes "an algebra is just a ring containing $k$" — see [[Ex - A finitely generated algebra need not be a finitely generated module]] for the related distinction and the [[Commutative Algebra I — Chain Conditions#Legal Operations|topic page's illegal-operations list]].

**Is NOT an instance — there is no $\{0\} \to A$ structural map for non-zero $A$ making $A$ a non-zero-ring-algebra.** The zero ring $\{0\}$ has $1 = 0$, and there is no ring homomorphism $\{0\} \to A$ to a non-zero ring (it would force $1_A = \rho(1) = \rho(0) = 0$). So one cannot make a non-zero ring into an algebra over the zero ring; conversely every ring is uniquely a $\{0\}$-algebra is false too. This probes that $\rho$ being a *unital* ring homomorphism is a real constraint.

**Calibration check.** Verify that the structural map of a non-zero $k$-algebra is injective, using that a field has only the ideals $0$ and $k$. Confirm that $R[T]$ is finitely generated as an algebra but not as a module for $R \neq 0$. Confirm that an $R$-algebra homomorphism is exactly a ring map that is $R$-linear and unital. If you can exhibit two different $\mathbb{C}$-algebra structures on $\mathbb{C}$ and explain why the identity fails to be a morphism between them, you have understood why $\rho$ is irreducible data.

---

# Unlocked by This

> [!tip] Affine schemes and the algebra–geometry dictionary *(from Algebraic Geometry)*
> The functor $A \mapsto \operatorname{Spec} A$ is a contravariant equivalence between commutative rings and affine schemes, and an $R$-algebra $A$ corresponds to a scheme **over $\operatorname{Spec} R$** — a morphism $\operatorname{Spec} A \to \operatorname{Spec} R$ induced by $\rho$. The whole relative theory of schemes (families, base change, fibres) is the geometric face of $R$-algebra theory; "$R$-algebra homomorphism" becomes "morphism over the base". This relative viewpoint is the organising principle of modern algebraic geometry.

> [!tip] Finitely generated $k$-algebras are coordinate rings *(from Algebraic Geometry)*
> A finitely generated reduced $k$-algebra over an algebraically closed field is exactly the **coordinate ring** $k[T_1, \dots, T_n]/I$ of an affine variety, and $k$-algebra homomorphisms correspond contravariantly to polynomial maps of varieties. The structural map $k \to A$ records that the variety lives over a point. This anti-equivalence, made precise by the Nullstellensatz, is developed in [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz]].

> [!tip] Group algebras and representation theory *(from Representation Theory)*
> For a group $G$ and field $k$, the **group algebra** $k[G]$ is a $k$-algebra whose modules are exactly the linear representations of $G$. Casting representation theory as module theory over the algebra $k[G]$ is what makes the machinery of this chapter — composition series, length, Jordan–Hölder — available to representations, where the composition factors are the irreducible constituents.
