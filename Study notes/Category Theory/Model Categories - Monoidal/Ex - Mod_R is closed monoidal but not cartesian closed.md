---
type: exercise
subject: model-categories
difficulty: "⭐"
prereqs:
  - "Def - Closed Monoidal Category"
  - "Def - Cartesian Closed Category"
  - "Def - Tensor Product of Modules"
  - "Def - Module"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $R$ be a commutative ring and $\mathbf{Mod}_R$ the category of $R$-modules. Show that $(\mathbf{Mod}_R, \otimes_R, R)$ is a [[Def - Closed Monoidal Category|closed symmetric monoidal category]], with internal hom $\mathrm{Hom}_R(M, N)$. Then show that $\mathbf{Mod}_R$ is **not** [[Def - Cartesian Closed Category|cartesian closed]] (for $R$ not the zero ring), by identifying the categorical product and observing that the tensor-hom adjunction is not a product-hom adjunction.

**Recall:**

A [[Def - Closed Monoidal Category|closed monoidal category]] is a monoidal category $(\mathcal{C}, \otimes, I)$ in which every functor $- \otimes B$ has a right adjoint $[B, -]$, so $\mathcal{C}(A \otimes B, C) \cong \mathcal{C}(A, [B, C])$ naturally.

A [[Def - Cartesian Closed Category|cartesian closed category]] is a category with finite products in which $- \times B$ has a right adjoint $(-)^B$; the monoidal product *is* the categorical product $\times$.

![[Def - Tensor Product of Modules#The Definition]]

The categorical **product** in $\mathbf{Mod}_R$ of two modules is their direct sum $M \oplus N$ (for finitely many factors, product and coproduct coincide), with projections $\pi_M, \pi_N$.

---

# Convergent Strategy

**Problem class:** This is a *verify-a-structure* problem of the kind catalogued in the topic page's problem-solving strategy: we are checking that a candidate $(\otimes, I, [-,-])$ satisfies the closed-monoidal axioms, then producing a *non-example* of a stronger property by exhibiting the relevant adjunction does not hold. The closed-monoidal half is direct from the universal property of the tensor product; the not-cartesian-closed half is a structural observation about which product the monoidal product is.

**Assumption pattern:** The key assumption is that $\otimes_R$ has a universal property: $R$-bilinear maps $M \times N \to P$ correspond to $R$-linear maps $M \otimes_R N \to P$. This universal property *is* the adjunction once you fix one variable. The second assumption to leverage is that the categorical product in $\mathbf{Mod}_R$ is $\oplus$, *different from* $\otimes_R$ — that difference is the entire reason $\mathbf{Mod}_R$ is closed but not cartesian closed.

**Theorem routing:** The closed-monoidal claim routes through the [[Thm - Universal Property of the Tensor Product of Modules|universal property of the tensor product]]: $\mathrm{Hom}_R(M \otimes_R N, P) \cong \mathrm{Hom}_R(M, \mathrm{Hom}_R(N, P))$, which is exactly $\mathcal{C}(M \otimes N, P) \cong \mathcal{C}(M, [N, P])$. The not-cartesian-closed claim routes through identifying the categorical product as $\oplus$ and noting $\otimes_R \neq \oplus$, so the monoidal product is not the categorical product.

**Key decision point:** The non-obvious move is to resist "proving" $\mathbf{Mod}_R$ is *not* closed (it is!) and instead pin down the precise sense in which it fails to be *cartesian* closed: the failure is not that an internal hom is missing, but that the monoidal product $\otimes_R$ is not the product $\oplus$. One must compute $|M \otimes_R N|$ versus $|M \oplus N|$ on a small example to see they differ, and recall that cartesian closedness is a statement about $\times$, not about $\otimes$.

---

# Legal Operations Used

1. **Operation 4-analogue (closedness as adjunction), from the topic page's Legal Operations.** We use that closedness *is* the right-adjointness of $- \otimes B$; rather than constructing $[B, -]$ ad hoc, we exhibit the tensor-hom adjunction and read off the internal hom as the right adjoint. This is the "transpose a tensor into an internal hom" reflex applied to objects.

2. **Operation 1-analogue (identify the categorical product).** To show non-cartesian-closedness we first identify the categorical product in $\mathbf{Mod}_R$, which is the direct sum, and then contrast it with the monoidal product $\otimes_R$.

---

# Hints

> [!note]- Hint 1
> Closedness is not something to build from scratch — it is a restatement of a universal property you already know. Which adjunction does the tensor product of modules satisfy?

> [!note]- Hint 2
> For the non-example: cartesian closed means the *monoidal product is the categorical product*. What is the categorical product in $\mathbf{Mod}_R$, and is it equal to $\otimes_R$?

> [!note]- Hint 3
> Take $R = \mathbb{Z}$ and $M = N = \mathbb{Z}/2$. Compute $M \otimes_{\mathbb{Z}} N$ and $M \oplus N$; they have different sizes, so $\otimes$ and $\times$ are genuinely different bifunctors, and the tensor-hom adjunction is not a product-exponential adjunction.

---

# Solution

The proof has two halves. First we exhibit the tensor-hom adjunction, which *is* closedness, and check symmetry. Second we identify the categorical product as $\oplus$ and observe $\otimes_R \neq \oplus$, so $\mathbf{Mod}_R$ is closed for $\otimes_R$ but not cartesian closed. The decisive computation is a tiny one showing $\otimes$ and $\oplus$ differ in size.

**Step 1: $\otimes_R$ has internal hom $\mathrm{Hom}_R(-,-)$, so $\mathbf{Mod}_R$ is closed monoidal.**

> [!note]- Derivation
> By the [[Thm - Universal Property of the Tensor Product of Modules|universal property of the tensor product]], for $R$-modules $L, M, N$ there is a natural bijection
> $$\mathrm{Hom}_R(L \otimes_R M, N) \;\cong\; \mathrm{Hom}_R\big(L, \mathrm{Hom}_R(M, N)\big),$$
> sending a linear map $f : L \otimes_R M \to N$ to $\ell \mapsto (m \mapsto f(\ell \otimes m))$, and back by uncurrying. This is exactly the statement that $- \otimes_R M$ has right adjoint $\mathrm{Hom}_R(M, -)$, i.e. $[M, -] = \mathrm{Hom}_R(M, -)$. The unit object is $R$, since $R \otimes_R M \cong M$ naturally (the unitor). Associativity $(L \otimes_R M) \otimes_R N \cong L \otimes_R (M \otimes_R N)$ and symmetry $M \otimes_R N \cong N \otimes_R M$ hold for the tensor product of modules over a commutative ring, with the pentagon, triangle, and hexagon coherences following from the corresponding identities on simple tensors. Hence $(\mathbf{Mod}_R, \otimes_R, R, \mathrm{Hom}_R)$ is a [[Def - Closed Monoidal Category|closed symmetric monoidal category]].

**Step 2: The categorical product in $\mathbf{Mod}_R$ is $\oplus$, which is not $\otimes_R$.**

> [!note]- Derivation
> The categorical product of $M$ and $N$ is the module $M \oplus N$ with projections $\pi_M : M \oplus N \to M$, $\pi_N : M \oplus N \to N$: any pair of maps $f : P \to M$, $g : P \to N$ assembles uniquely into $(f, g) : P \to M \oplus N$. This is the categorical product, and it is *not* the tensor product. Concretely, take $R = \mathbb{Z}$, $M = N = \mathbb{Z}/2$. Then
> $$M \oplus N = \mathbb{Z}/2 \oplus \mathbb{Z}/2 \quad (\text{4 elements}), \qquad M \otimes_{\mathbb{Z}} N = \mathbb{Z}/2 \otimes_{\mathbb{Z}} \mathbb{Z}/2 \cong \mathbb{Z}/2 \quad (\text{2 elements}).$$
> So $\otimes_{\mathbb{Z}}$ and $\oplus$ are different bifunctors. A [[Def - Cartesian Closed Category|cartesian closed]] structure requires the *monoidal product to be the categorical product*; here the monoidal product is $\otimes_R$, which differs from the product $\oplus$, so $\mathbf{Mod}_R$ is not cartesian closed with its standard monoidal structure. (One can ask separately whether $- \oplus M$ has a right adjoint; it does not in general — $- \oplus M$ does not even preserve the terminal object correctly to be a product-with-exponential, and the additive structure forces $\mathrm{Hom}(M \oplus N, P) \cong \mathrm{Hom}(M,P) \times \mathrm{Hom}(N,P)$, the wrong shape for an exponential adjunction.)

> [!note]- Complete formal solution
> **Closed monoidal.** Over a commutative ring $R$, the tensor product $\otimes_R$ is a symmetric monoidal product on $\mathbf{Mod}_R$ with unit $R$ (since $R \otimes_R M \cong M$), associator and symmetry inherited from simple tensors, satisfying the coherence axioms. By the [[Thm - Universal Property of the Tensor Product of Modules|universal property of the tensor product]], $\mathrm{Hom}_R(L \otimes_R M, N) \cong \mathrm{Hom}_R(L, \mathrm{Hom}_R(M, N))$ naturally in $L$ and $N$, so $- \otimes_R M \dashv \mathrm{Hom}_R(M, -)$ and the internal hom is $[M, N] = \mathrm{Hom}_R(M, N)$. Thus $\mathbf{Mod}_R$ is closed symmetric monoidal.
>
> **Not cartesian closed.** The categorical product in $\mathbf{Mod}_R$ is the direct sum $M \oplus N$ (with the usual projections satisfying the universal property of the product). Cartesian closedness requires the monoidal product to be the categorical product. But the monoidal product is $\otimes_R$, and $\otimes_R \neq \oplus$: for $R = \mathbb{Z}$, $\mathbb{Z}/2 \otimes_{\mathbb{Z}} \mathbb{Z}/2 \cong \mathbb{Z}/2$ has two elements while $\mathbb{Z}/2 \oplus \mathbb{Z}/2$ has four. Therefore $\mathbf{Mod}_R$ (with its standard monoidal structure) is closed monoidal but not cartesian closed. $\qquad\blacksquare$

---

# Key Takeaways

**Closed monoidal is a strictly weaker, more common condition than cartesian closed, and $\mathbf{Mod}_R$ is the example that teaches the difference.** The reflex many people have is to conflate "has an internal hom" with "cartesian closed", but cartesian closedness specifically demands that the monoidal product be the *categorical product*. Modules are the cleanest place to feel the gap: $\otimes_R$ is a perfectly good monoidal product with a perfectly good internal hom $\mathrm{Hom}_R$, yet it is not the product $\oplus$, so the category is closed but not cartesian closed. Whenever you meet a "linear" or "resource-sensitive" category — modules, chain complexes, vector spaces, spectra, Banach spaces — expect closed monoidal with $\otimes$, not cartesian closed; the cartesian closed examples ($\mathbf{Set}$, $\mathbf{Cat}$, $\mathbf{sSet}$) are the ones whose objects can be freely duplicated.

**Closedness is never something to construct from scratch — it is a universal property you already know, transposed.** The entire first half of this exercise is the observation that the tensor-hom adjunction *is* closedness. This is the operational content of the "true name" of closed monoidal: tensor-with-$B$ has a right adjoint. The transferable diagnostic is that whenever you are asked "is this monoidal category closed?", the productive move is to ask "do I already know an adjunction $- \otimes B \dashv (\text{something})$?" — and for any algebraic category the answer is the tensor-hom adjunction from its representation/module theory. You rarely build the internal hom; you recognize it as a right adjoint you have met before.

**The size computation $\mathbb{Z}/2 \otimes \mathbb{Z}/2 = \mathbb{Z}/2 \neq \mathbb{Z}/2 \oplus \mathbb{Z}/2$ is a portable sanity check for distinguishing tensor from product.** Tensor "multiplies" while direct sum "adds"; over a field, $\dim(V \otimes W) = \dim V \cdot \dim W$ while $\dim(V \oplus W) = \dim V + \dim W$. This single contrast is the fingerprint of a non-cartesian monoidal structure and is worth keeping at hand: whenever a monoidal product makes objects *bigger multiplicatively* rather than gluing them side by side, it is a tensor, the category is (at best) closed monoidal not cartesian closed, and you should reach for the tensor-hom adjunction rather than currying-into-exponentials. This same fingerprint distinguishes the smash product of spectra and the derived tensor of complexes from any cartesian structure, and it is exactly the structure this chapter makes homotopy-invariant. See also [[Ex - The internal hom of chain complexes]].
