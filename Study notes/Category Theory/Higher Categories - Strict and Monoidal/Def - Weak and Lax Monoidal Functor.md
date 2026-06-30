---
type: definition
subject: higher-categories
prereqs:
  - "Def - Monoidal Category"
  - "Def - Unbiased Monoidal Category"
  - "Def - Functor"
  - "Def - Natural Transformation"
tags: [category-theory, higher-categories, foundations]
---

# Notation

Let $(\mathcal{C}, \otimes, I)$ and $(\mathcal{D}, \boxtimes, J)$ be [[Def - Monoidal Category|monoidal categories]] (we use distinct symbols $\otimes, I$ in the source and $\boxtimes, J$ in the target to keep them apart). A functor between them comes with two pieces of comparison data: a **tensor comparison** $\varphi_{A,B} : F(A) \boxtimes F(B) \to F(A \otimes B)$, natural in $A, B$, and a **unit comparison** $\varphi_0 : J \to F(I)$. The direction of the arrows is the whole story: in a **lax** monoidal functor they point *into* $F$ of the tensor; in an **oplax** one they point out; in a **weak (strong)** monoidal functor they are isomorphisms; in a **strict** one they are identities. We write the structural natural transformations of the monoidal categories — associator, unitors — as $\alpha, \lambda, \rho$ on $\mathcal{C}$ and $\alpha', \lambda', \rho'$ on $\mathcal{D}$. The full registry is on [[Higher Categories — Strict n-Categories and Notions of Monoidal Category]].

This is a compound page: it defines four interlocking notions — the **lax**, **oplax**, **weak (strong)**, and **strict** monoidal functor — because they differ only in the *direction and invertibility* of the same two comparison maps, and the right notion for a given purpose depends on that single choice.

---

# Axiom Motivation

We have [[Def - Monoidal Category|monoidal categories]]; the inevitable next question is what a *map* between them should be. A plain [[Def - Functor|functor]] $F : \mathcal{C} \to \mathcal{D}$ knows nothing about the tensors — there is no reason $F(A \otimes B)$ should have anything to do with $F(A) \boxtimes F(B)$. To respect the monoidal structure, $F$ must come with a way to compare "tensor then apply $F$" against "apply $F$ then tensor." This comparison is the entire content of a monoidal functor, and the surprising lesson is that there are *four* useful notions, distinguished only by whether the comparison is an isomorphism and which way it points.

Start with the most permissive, the **lax** version. We provide a natural map $\varphi_{A,B} : F(A) \boxtimes F(B) \to F(A \otimes B)$ and a map $\varphi_0 : J \to F(I)$, with *no* requirement that they be invertible. Why is this the right default, and why this direction? Because in the most important examples the comparison is genuinely non-invertible and points exactly this way. The motivating case: a [[Def - Monoid in a Monoidal Category|monoid]] in $\mathcal{D}$ is the same as a lax monoidal functor from the *terminal* monoidal category $\mathbf{1}$ to $\mathcal{D}$ — the unit comparison $\varphi_0 : J \to M$ is the monoid's unit, and the tensor comparison $\varphi : M \boxtimes M \to M$ is its multiplication. A monoid's multiplication is *not* invertible, and it points *into* $M$; demanding invertibility would forbid all interesting monoids. So lax is the notion under which "monoid = lax functor from a point" works, and that is decisive.

What axioms must $\varphi$ and $\varphi_0$ satisfy? Exactly the conditions that make the comparison *coherent with associativity and units*. For three objects $A, B, C$, there are two ways to compare $F(A) \boxtimes F(B) \boxtimes F(C)$ with $F(A \otimes B \otimes C)$ — comparing the first two then the third, or the last two then the first — and they must agree, mediated by the associators. This is the **associativity (hexagon-shaped) coherence** of $\varphi$. Likewise $\varphi_0$ must be compatible with the unitors: comparing $J \boxtimes F(A)$ to $F(I \otimes A)$ via $\varphi_0$ and $\varphi$ must reduce, through the unitors, to the identity on $F(A)$. These are the **unit coherence** axioms. Drop the associativity coherence and "$F$ respects the tensor" loses meaning for products of three or more objects — the comparison ceases to determine a single canonical map on a long tensor, the exact failure the pentagon prevents inside a monoidal category. Drop the unit coherence and $\varphi_0$ stops being compatible with the unit, so $F(I)$ does not behave like the image of a unit.

Now the variants, each obtained by changing one design decision. **Oplax**: reverse the comparison arrows, $\psi_{A,B} : F(A \otimes B) \to F(A) \boxtimes F(B)$ and $\psi_0 : F(I) \to J$. This is the right notion when the natural map goes the other way — for instance a **comonoid** in $\mathcal{D}$ is an oplax functor from $\mathbf{1}$, with comultiplication $F(I) \to F(I)\boxtimes F(I)$. **Weak (also called strong)**: insist the lax comparisons be *[[Def - Isomorphism|isomorphisms]]*. This is the notion for which monoidal functors compose into an honest $2$-category and for which "monoidal equivalence" makes sense; it is the level at which one says two monoidal categories are "the same." **Strict**: insist the comparisons be *identities*, $F(A) \boxtimes F(B) = F(A\otimes B)$ on the nose. Strictness is rare and rigid, useful mainly as the target of strictification theorems.

Why keep all four rather than picking one? Because they answer different questions, and conflating them is a classic error. If you want monoids, loop spaces, or measures, you want **lax** (the structure maps are non-invertible and point inward). If you want to say two monoidal categories are equivalent, or to transport monoidal structure along an equivalence, you want **weak**. If you are strictifying, you want **strict**. The single most important takeaway of this page is that "monoidal functor" is ambiguous until you say *lax, oplax, weak, or strict*, and the correct choice is forced by whether your comparison maps are invertible and which way they point.

---

# The Definition

Let $(\mathcal{C}, \otimes, I, \alpha, \lambda, \rho)$ and $(\mathcal{D}, \boxtimes, J, \alpha', \lambda', \rho')$ be [[Def - Monoidal Category|monoidal categories]].

A **lax monoidal functor** $(F, \varphi, \varphi_0) : \mathcal{C} \to \mathcal{D}$ consists of a [[Def - Functor|functor]] $F : \mathcal{C} \to \mathcal{D}$, a [[Def - Natural Transformation|natural transformation]]
$$\varphi_{A,B} : F(A) \boxtimes F(B) \longrightarrow F(A \otimes B),$$
and a morphism $\varphi_0 : J \to F(I)$, such that:

- **Associativity coherence:** for all $A, B, C$,
$$F(\alpha_{A,B,C}) \circ \varphi_{A \otimes B, C} \circ (\varphi_{A,B} \boxtimes 1) = \varphi_{A, B \otimes C} \circ (1 \boxtimes \varphi_{B,C}) \circ \alpha'_{FA, FB, FC};$$
- **Left unit coherence:** $F(\lambda_A) \circ \varphi_{I,A} \circ (\varphi_0 \boxtimes 1) = \lambda'_{FA}$;
- **Right unit coherence:** $F(\rho_A) \circ \varphi_{A,I} \circ (1 \boxtimes \varphi_0) = \rho'_{FA}$.

An **oplax monoidal functor** is the same data with the comparison arrows reversed: $\psi_{A,B} : F(A\otimes B) \to F(A) \boxtimes F(B)$ and $\psi_0 : F(I) \to J$, satisfying the formally dual coherence equations.

A **weak monoidal functor** (also **strong monoidal functor**) is a lax monoidal functor in which $\varphi_{A,B}$ and $\varphi_0$ are *isomorphisms*. (Equivalently, an oplax one with invertible comparisons; the two notions of "invertible monoidal functor" coincide.)

A **strict monoidal functor** is one in which $\varphi_{A,B}$ and $\varphi_0$ are *identities*: $F(A) \boxtimes F(B) = F(A \otimes B)$ and $F(I) = J$, with the comparison maps the identity morphisms.

In the **unbiased** language (see [[Def - Unbiased Monoidal Category]]), all four are uniform: a lax monoidal functor between unbiased monoidal categories is a functor $F$ with, for each $n$, a natural comparison
$$\varphi_n : \boxtimes_n(F A_1, \dots, F A_n) \longrightarrow F(\otimes_n(A_1, \dots, A_n)),$$
compatible with the composition isomorphisms $\gamma$; weak when every $\varphi_n$ is invertible, strict when every $\varphi_n$ is an identity. The single family $\varphi_n$ replaces the binary $\varphi$ plus nullary $\varphi_0$ plus the coherence equations.

---

# Categorical / Structural Definition

The structural slogan is that **a lax monoidal functor is a morphism of (pseudo-)algebras**, and the four flavours are the four kinds of algebra morphism. Recall that an [[Def - Unbiased Monoidal Category|unbiased monoidal category]] is a pseudo-algebra for the free-monoidal-category $2$-monad $M$ on $\mathbf{Cat}$. In $2$-monad theory, between two pseudo-algebras there are exactly the four standard notions of morphism: **strict** (commutes with the algebra actions on the nose), **pseudo/strong = weak** (commutes up to invertible coherence cell), **lax** (commutes up to a not-necessarily-invertible cell pointing one way), and **oplax** (the cell points the other way). A monoidal functor of each kind is precisely an algebra morphism of the corresponding kind for $M$. The comparison $\varphi$ is the coherence cell witnessing that $F$ commutes with the tensor action; its invertibility and direction are exactly the lax/oplax/pseudo/strict distinction.

This is why the four notions are not an arbitrary menu: they are forced by the general theory of maps between pseudo-algebras, which always has exactly these four. The most operationally useful corollary is the one already used in the motivation: a (lax) algebra morphism from the **terminal** algebra (the unit monoidal category $\mathbf{1}$, the free $M$-algebra on a point, whose underlying object plays the role of "the [[Def - Operad|operad]]'s identity") into $\mathcal{D}$ is the same as a [[Def - Monoid in a Monoidal Category|monoid]] in $\mathcal{D}$. So **monoids are lax functors out of a point**, comonoids are oplax functors out of a point, and this is the precise sense in which lax monoidal functors *are* the morphisms that carry algebraic structure.

---

# Relate to Other Fields / Compression

Lax monoidal functors are the maps that **transport algebra**: they send [[Def - Monoid in a Monoidal Category|monoids]] to monoids, modules to modules, and algebraic structure to algebraic structure, because the comparison $\varphi$ lets the image of a multiplication compose. This is their reason for existing across mathematics — homology with the Künneth map, the chains functor, the global-sections functor on sheaves, the free functors of algebra are all naturally lax (or oplax) monoidal, and that laxness is exactly what makes them preserve the relevant algebraic gadgets.

**True name:** a lax monoidal functor is "a functor together with a coherent, possibly-non-invertible, possibly-directional rule for comparing $F$ of a tensor with the tensor of $F$'s." The four flavours are one decision tree: *Is the comparison an isomorphism?* If no, *which way does it point?* — into $F$(tensor) is lax, out of it is oplax. If yes, *is it an identity?* — no is weak/strong, yes is strict. When you meet a structure-preserving functor in the wild and want to know if it carries monoids along, ask exactly these questions.

The compression unifying this with the rest of the chapter: **everything in the weak monoidal world is "the same data, with equalities relaxed to coherent cells, and a choice of direction."** Objects relax equalities to get [[Def - Monoidal Category|monoidal categories]]; functors relax them to get lax monoidal functors; and the morphisms-of-morphisms (monoidal natural transformations) relax them again. This is the single pattern — strict, then weak, then lax/oplax — that organises categorified algebra, and the monoidal functor is its clearest one-dimensional instance.

---

# Examples / Corollaries

**Is an instance (lax) — a monoid as a functor from a point.** A [[Def - Monoid in a Monoidal Category|monoid]] $(M, \mu, \eta)$ in $(\mathcal{D}, \boxtimes, J)$ is exactly a lax monoidal functor $\mathbf{1} \to \mathcal{D}$ from the terminal (one-object, one-morphism) monoidal category: the functor picks out $M = F(\ast)$, the tensor comparison is the multiplication $\varphi = \mu : M \boxtimes M \to M$, the unit comparison is $\varphi_0 = \eta : J \to M$, and the lax coherence axioms are exactly associativity and unitality of the monoid. The non-invertibility of $\mu$ is why "lax" is essential here.

**Is an instance (oplax) — a comonoid as a functor from a point.** Dually, a comonoid in $\mathcal{D}$ is an oplax monoidal functor $\mathbf{1} \to \mathcal{D}$, with comultiplication $\psi : F(I) \to F(I)\boxtimes F(I)$ and counit $\psi_0 : F(I) \to J$. In $(\mathbf{Vect}_k, \otimes)$ this is a coalgebra.

**Is an instance (weak/strong) — the free vector space functor.** The free functor $k[-] : (\mathbf{Set}, \times) \to (\mathbf{Vect}_k, \otimes)$ sending a set $X$ to the vector space on basis $X$ is **strong** monoidal: $k[X] \otimes k[Y] \cong k[X \times Y]$ canonically (a basis of the tensor is pairs of basis elements), and $k[1] \cong k$. Because it is strong, it sends monoids to monoids — a monoid in $\mathbf{Set}$ (an ordinary monoid) becomes its monoid algebra $k[M]$.

**Is an instance (lax, genuinely non-invertible) — singular chains.** The singular chains functor $C_\bullet : (\mathbf{Top}, \times) \to (\mathbf{Ch}_k, \otimes)$ carries the **Eilenberg–Zilber / Alexander–Whitney** comparison $C_\bullet(X) \otimes C_\bullet(Y) \to C_\bullet(X \times Y)$, which is a lax structure (a chain [[Def - Homotopy|homotopy]] equivalence, not an isomorphism on the nose). Its laxness is what makes the cup product on cohomology exist.

**Is an instance (strict) — an identity functor, or a strictly structure-preserving inclusion.** The identity functor on any monoidal category is strict, as is the inclusion of a strict monoidal subcategory closed under the literal tensor. Strictness is rare precisely because most comparisons are at best isomorphisms.

**Is NOT a monoidal functor — a plain functor with no comparison.** The functor $\mathbf{Vect}_k \to \mathbf{Set}$ forgetting the linear structure has no natural map $U(V) \times U(W) \to U(V \otimes W)$ (the underlying set of $V \otimes W$ is not built from pairs $(v,w)$ — a general tensor is a *sum* of pure tensors). So the forgetful functor is **not** monoidal for $(\otimes, \times)$, which is exactly why a $k$-algebra's multiplication is not recovered by forgetting to sets. (It *is* lax monoidal for the other pairing, but not this one.)

**Calibration check.** Verify that a lax monoidal functor $\mathbf{1} \to \mathcal{D}$ unwinds to precisely the [[Def - Monoid in a Monoidal Category|monoid]] axioms in $\mathcal{D}$, with $\varphi$ the multiplication and $\varphi_0$ the unit. Confirm that a weak monoidal functor that is also an equivalence of underlying categories is a **monoidal equivalence**, and that under it monoids correspond to monoids. And check that "strict $\Rightarrow$ weak $\Rightarrow$ lax" as a hierarchy of conditions (identity is invertible; invertible is a map), so the four notions are genuinely nested for the non-oplax three.

---

# Unlocked by This

> [!tip] Biased = Unbiased *(from this chapter)*
> The comparison functors witnessing [[Thm - Biased and Unbiased Monoidal Categories Coincide]] are weak (strong) monoidal functors, and the equivalence is a **monoidal equivalence**. Lax/weak functors are the morphisms in which "the two notions of monoidal category are the same" is even stated.

> [!tip] Monoidal Monads and Commutative Algebraic Theories *(from this chapter)*
> A **monoidal monad** is a monad whose endofunctor is lax monoidal compatibly with the monad structure; its algebras then form a monoidal category. This is how the tensor product of modules, the convolution of measures, and the **probability monad** of Markov categories all acquire their monoidal structure.

> [!tip] TQFT and Symmetric Monoidal Functors *(from Mathematical Physics)*
> A **topological quantum field theory** is a *symmetric weak* monoidal functor $\mathrm{Cob}_n \to \mathbf{Vect}_k$. The weakness (isomorphism, not equality) is what lets "disjoint union goes to tensor product" hold canonically rather than on the nose, and the symmetry encodes that the order of components does not matter.
