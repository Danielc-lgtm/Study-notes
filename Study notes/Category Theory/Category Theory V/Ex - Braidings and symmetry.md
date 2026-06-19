---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Monoidal Category"
  - "Def - Monoid in a Monoidal Category"
  - "Def - Tensor Product of Vector Spaces"
tags: [category-theory, foundations]
---

# Problem Statement

**(a)** Show that $(\mathbf{Vect}_k, \otimes_k, k)$ is a **symmetric** [[Def - Monoidal Category|monoidal category]]: the braiding $\beta_{V,W}(v\otimes w) = w\otimes v$ satisfies $\beta_{W,V}\circ\beta_{V,W} = 1$.

**(b)** Show that the [[Def - Functor Category|endofunctor category]] $([\mathcal{C},\mathcal{C}], \circ, 1)$ is **not braided** in general: there is no natural isomorphism $F\circ G\cong G\circ F$.

**(c)** Show that a one-object symmetric monoidal category (a symmetric monoidal category with a single object, equivalently a commutative [[Def - Monoid in a Monoidal Category|monoid]] in some sense) corresponds to a **commutative monoid**, and explain how the symmetry axiom produces commutativity.

**Recall:**

![[Def - Monoidal Category#The Definition]]

A **braided** monoidal category has $\beta_{A,B} : A\otimes B\to B\otimes A$ satisfying the hexagon axioms; it is **symmetric** if $\beta_{B,A}\circ\beta_{A,B} = 1_{A\otimes B}$. A [[Def - Monoid in a Monoidal Category|monoid object]] $(M,m,e)$ in a braided category is **commutative** if $m\circ\beta_{M,M} = m$.

---

# Convergent Strategy

**Problem class:** A "distinguish braided / symmetric / non-braided" problem — calibrating the three levels of monoidal structure (legal operation 4 from the illegal-but-tempting list). The skill is recognizing which categories have a swap and which do not.

**Assumption pattern:** A symmetry is "the right to swap tensor factors, with swapping twice trivial." The assumption to leverage is that $\otimes$ on $\mathbf{Vect}_k$ comes from a *bilinear* universal property symmetric in its arguments (so a swap exists), while $\circ$ on endofunctors is genuinely non-commutative (so no swap).

**Theorem routing:** Route (a) through the universal property of $\otimes$ (the swap is the unique map induced by the bilinear $v\times w\mapsto w\otimes v$). Route (b) through an explicit counterexample: two endofunctors with $F\circ G\not\cong G\circ F$. Route (c) through the [[Def - Monoid in a Monoidal Category|commutative-monoid-object]] definition, showing $m\circ\beta = m$ becomes $ab = ba$.

**Key decision point:** The discriminating move in (b) is to exhibit *concrete* endofunctors whose composites differ even on objects — e.g. the constant functor and a non-constant one — so that no natural isomorphism can exist. The temptation (warned against in the topic page) is to assume a tensor always admits a braiding; the endofunctor category is the standard refutation.

---

# Legal Operations Used

1. **Operation 8 from the topic page (invoke coherence to drop parentheses).** Throughout we suppress $\alpha, \lambda, \rho$ by [[Thm - Mac Lane Coherence Theorem|coherence]], focusing on the braiding.

2. **Illegal-but-tempting operation 4 (do not assume monoidal ⟹ symmetric).** Part (b) is the explicit refutation: the endofunctor category is monoidal but admits no braiding.

3. **Operation 7 from the topic page (unwind a monoid object).** Part (c) translates "commutative monoid object" via $m\circ\beta = m$ into ordinary commutativity.

---

# Hints

> [!note]- Hint 1
> For (a), the swap $\beta_{V,W} : V\otimes W\to W\otimes V$ is the unique linear map induced (by the universal property of $\otimes$) from the bilinear map $(v,w)\mapsto w\otimes v$. Composing two swaps sends $v\otimes w\mapsto w\otimes v\mapsto v\otimes w$, the identity.

> [!note]- Hint 2
> For (b), pick endofunctors of $\mathbf{Set}$ whose composites differ. Let $K_1$ be the constant functor at a one-point set and $F$ the identity. Compare $K_1\circ F$ and $F\circ K_1$, or better, use $A\mapsto A+1$ and $A\mapsto A\times A$ and compare the composites on a small set.

> [!note]- Hint 3
> If $F(A) = A+1$ and $G(A) = A\times A$, then $F\circ G(A) = (A\times A)+1$ while $G\circ F(A) = (A+1)\times(A+1)$. For $A = \{*\}$ these have $2$ and $4$ elements: no isomorphism $FG\cong GF$ can exist. So no braiding.

> [!note]- Hint 4
> For (c), a one-object monoidal category has a single object whose endomorphisms (or whose tensor structure) form a monoid; commutativity of the monoid object, $m\circ\beta = m$, says "multiply-then-swap = multiply," i.e. $ab = ba$.

---

# Solution

The plan: build the swap on $\mathbf{Vect}_k$ from the universal property and check it squares to the identity (Step 1); refute braiding on endofunctors with an explicit cardinality counterexample (Step 2); translate the commutative-monoid-object condition into ordinary commutativity (Step 3). The crux is that a tensor admits a symmetry exactly when its universal property is symmetric in its arguments.

**Step 1 (a): $\mathbf{Vect}_k$ is symmetric.**

> [!note]- Derivation
> By the universal property of the [[Def - Tensor Product of Vector Spaces|tensor product]], a linear map out of $V\otimes_k W$ is the same as a bilinear map $V\times W\to(-)$. The bilinear map $(v,w)\mapsto w\otimes v \in W\otimes_k V$ induces a unique linear map $\beta_{V,W} : V\otimes W\to W\otimes V$, $v\otimes w\mapsto w\otimes v$. It is natural in $V, W$ (functoriality of $\otimes$). The hexagon axioms hold because swapping past a tensor $W\otimes U$ is the same as swapping past $W$ then $U$ (the symmetric group acts on tensor factors). Finally,
> $$\beta_{W,V}\circ\beta_{V,W}(v\otimes w) = \beta_{W,V}(w\otimes v) = v\otimes w,$$
> so $\beta_{W,V}\circ\beta_{V,W} = 1_{V\otimes W}$: the braiding is a **symmetry**. Hence $(\mathbf{Vect}_k,\otimes_k,k)$ is symmetric monoidal.

**Step 2 (b): Endofunctors are not braided.**

> [!note]- Derivation
> In $([\mathbf{Set},\mathbf{Set}],\circ,1)$, the tensor is composition. Take $F(A) = A + 1$ (maybe) and $G(A) = A\times A$ (squaring). Then
> $$F\circ G(A) = G(A) + 1 = (A\times A) + 1, \qquad G\circ F(A) = F(A)\times F(A) = (A+1)\times(A+1).$$
> Evaluate at $A = \{*\}$ (one element): $F\circ G(\{*\}) = (\{*\}\times\{*\}) + 1$ has $1 + 1 = 2$ elements, while $G\circ F(\{*\}) = (\{*\}+1)\times(\{*\}+1)$ has $2\times 2 = 4$ elements. A natural isomorphism $FG\cong GF$ would force these to be isomorphic sets, but $2\neq 4$. So no natural isomorphism $F\circ G\cong G\circ F$ exists, and $([\mathbf{Set},\mathbf{Set}],\circ)$ is **not braided** (a fortiori not symmetric). Composition of functors is genuinely non-commutative — which is exactly why [[Def - Monad and Comonad|monads]] (monoid objects here) need not commute.

**Step 3 (c): One-object symmetric monoidal = commutative monoid.**

> [!note]- Derivation
> Consider a symmetric monoidal category with one object — concretely, take a monoid object $(M,m,e)$ in a symmetric monoidal category and impose **commutativity** $m\circ\beta_{M,M} = m$. Reading on elements (in $\mathbf{Set}$ or $\mathbf{Ab}$), $\beta_{M,M}$ swaps the two factors, so $m\circ\beta(a\otimes b) = m(b\otimes a) = b\cdot a$, and commutativity says $b\cdot a = m(a\otimes b) = a\cdot b$. So a commutative monoid object is exactly a [[Def - Monoid in a Monoidal Category|monoid]] with $ab = ba$ — a **commutative monoid** (in $\mathbf{Set}$) or commutative ring (in $\mathbf{Ab}$), as in [[Ex - Monoids in Vect are algebras and in Ab are rings]]. The symmetry $\beta$ is precisely the structure that lets "commutativity" even be *stated*: without a braiding there is no map $M\otimes M\to M\otimes M$ swapping factors, so $ab = ba$ has no meaning. This is why commutative rings live in the *symmetric* monoidal $(\mathbf{Ab},\otimes)$, while monads (in the non-braided endofunctor category) have no notion of commutativity.

> [!note]- Complete formal solution
> **(a)** The bilinear map $(v,w)\mapsto w\otimes v$ induces $\beta_{V,W} : v\otimes w\mapsto w\otimes v$, natural and satisfying the hexagons; $\beta\circ\beta = 1$, so $\mathbf{Vect}_k$ is symmetric.
>
> **(b)** With $F(A) = A+1$, $G(A) = A\times A$ in $[\mathbf{Set},\mathbf{Set}]$: at $A = \{*\}$, $FG$ has $2$ elements and $GF$ has $4$, so $FG\not\cong GF$ and no braiding exists.
>
> **(c)** A commutative monoid object satisfies $m\circ\beta = m$, i.e. $ba = ab$; the symmetry $\beta$ is what makes commutativity expressible, so a one-object symmetric monoidal structure is a commutative monoid. $\blacksquare$

> [!tip] The hierarchy and the periodic table
> Monoidal ⊃ braided ⊃ symmetric is a strict hierarchy: $(\mathbf{Vect}_k,\otimes)$ is symmetric, the representation category of a quantum group is braided but not symmetric (the double braid is a non-trivial $R$-matrix), and $([\mathcal{C},\mathcal{C}],\circ)$ is monoidal but not even braided. This is the bottom of the **periodic table** of $n$-categories: degree of commutativity = how far up you can categorify before structure runs out.

---

# Key Takeaways

**A tensor admits a symmetry exactly when its universal property is symmetric in its arguments.** The reusable diagnostic from part (a) is that the braiding on $\mathbf{Vect}_k$ exists because the tensor product classifies *bilinear* maps, and "bilinear in $(v,w)$" is symmetric under swapping $v$ and $w$ — so the swap map is induced canonically. Whenever a monoidal product comes from a universal property symmetric in its inputs (products, coproducts, tensor of modules), a symmetry exists. Conversely, when the product is composition — inherently ordered, "do $G$ then $F$" — there is no symmetric universal property and no braiding. The trigger for "is this symmetric?" is to ask whether the defining universal property treats the two factors interchangeably.

**Composition of functors is non-commutative, and that is why monads do not commute.** Part (b)'s cardinality counterexample is the canonical refutation of the tempting assumption that every monoidal category is symmetric. The endofunctor category $([\mathcal{C},\mathcal{C}],\circ)$ has no braiding because $F\circ G$ and $G\circ F$ can differ even in cardinality, and this is not a pathology but the source of important structure: it is exactly why two [[Def - Monad and Comonad|monads]] do not automatically compose to a monad (you need a distributive law), and why there is no notion of a "commutative monad" in the naive sense. The transferable lesson is to *check* for a braiding rather than assume one, with the endofunctor category as the standard non-example to keep in mind.

**The braiding is what makes commutativity expressible at all.** The deepest point of part (c) is that "commutative" is not a property a monoid object can have in an arbitrary monoidal category — it requires a braiding to even *state* the condition $m\circ\beta = m$, because without a swap map there is nothing comparing $ab$ to $ba$. This explains the placement of structures: commutative rings live in the *symmetric* $(\mathbf{Ab},\otimes)$ where the swap exists; monads live in the *non-braided* endofunctor category where commutativity is undefinable. The general principle, which ascends the periodic table of $n$-categories, is that each added level of commutativity (braided, then symmetric) requires one more dimension of categorical structure, and the symmetry axiom $\beta^2 = 1$ is the statement that "swapping is an involution" — the algebraic shadow of strands passing through each other rather than knotting. See [[Ex - Monoids in Vect are algebras and in Ab are rings]] for how the symmetric structure distinguishes commutative from non-commutative rings.
