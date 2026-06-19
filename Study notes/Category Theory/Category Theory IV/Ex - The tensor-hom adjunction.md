---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Adjunction"
  - "Def - Tensor Product of Modules"
  - "Def - The Hom Functor and Left Exactness"
  - "Thm - Universal Property of the Tensor Product of Modules"
tags: [category-theory, foundations]
---

# Problem Statement

Let $R$ be a commutative ring and $M$ a fixed $R$-[[Def - Module|module]]. Consider the two functors on $\mathbf{Mod}_R$:
$$- \otimes_R M : \mathbf{Mod}_R \to \mathbf{Mod}_R \qquad\text{and}\qquad \mathrm{Hom}_R(M, -) : \mathbf{Mod}_R \to \mathbf{Mod}_R.$$

**(a)** Construct a natural isomorphism
$$\mathrm{Hom}_R(A \otimes_R M, B) \;\cong\; \mathrm{Hom}_R(A, \mathrm{Hom}_R(M, B))$$
for all $R$-modules $A, B$.

**(b)** Conclude that $- \otimes_R M \dashv \mathrm{Hom}_R(M, -)$, identify the unit and counit, and explain why this implies $\otimes_R M$ is right exact while $\mathrm{Hom}_R(M, -)$ is left exact.

**Recall:**

![[Thm - Universal Property of the Tensor Product of Modules#Statement]]

The [[Def - Tensor Product of Modules|tensor product]] $A\otimes_R M$ is the universal target of $R$-**bilinear** maps out of $A\times M$: a bilinear map $A\times M\to B$ corresponds to a unique [[Def - Module Homomorphism|R-linear map]] (an $R$-module homomorphism) $A\otimes_R M\to B$.

$\mathrm{Hom}_R(M, B)$ is the $R$-module of $R$-linear maps $M\to B$ (see [[Def - The Hom Functor and Left Exactness]]). An [[Def - Adjunction|adjunction]] $L\dashv R$ is a natural bijection $\mathcal{C}(LA, B)\cong\mathcal{C}(A, RB)$.

---

# Convergent Strategy

**Problem class:** This is an "identify a known isomorphism as an adjunction" problem. The currying isomorphism for modules is classical; the categorical task is to recognise it as the adjunction $-\otimes M\dashv\mathrm{Hom}(M,-)$ and then harvest the consequences (right/left exactness) via [[Thm - Right Adjoints Preserve Limits|RAPL/LAPC]].

**Assumption pattern:** The key assumption is the [[Thm - Universal Property of the Tensor Product of Modules|universal property of the tensor product]]: maps out of $A\otimes M$ are bilinear maps on $A\times M$. The bridge to the adjunction is that a bilinear map $A\times M\to B$ is the same as a linear map $A\to\mathrm{Hom}(M,B)$ — "fix the first argument, get a linear map in the second". This is the same currying that defines a [[Def - Cartesian Closed Category|cartesian closed category]], but for the monoidal product $\otimes$ rather than $\times$.

**Theorem routing:** The route is: universal property of $\otimes$ (maps out $=$ bilinear maps) $\Rightarrow$ bilinear maps $=$ linear maps into $\mathrm{Hom}(M,B)$ (currying) $\Rightarrow$ the hom-iso $\Rightarrow$ adjunction by [[Def - Adjunction|definition]]. Then [[Thm - Right Adjoints Preserve Limits|RAPL]] gives that the right adjoint $\mathrm{Hom}(M,-)$ preserves limits (kernels) hence is left exact, and LAPC gives that the left adjoint $-\otimes M$ preserves colimits (cokernels) hence is right exact.

**Key decision point:** The non-obvious move is to route *through bilinearity*. Instead of constructing the isomorphism on elements of the tensor product (which requires choosing representatives and checking well-definedness), use the universal property to turn "linear maps out of $A\otimes M$" into "bilinear maps on $A\times M$", which curry transparently. This avoids ever touching a general element of $A\otimes_R M$.

---

# Legal Operations Used

1. **Operation 1 from the topic page (transpose a morphism across the adjunction).** The entire isomorphism is the transposition $f\mapsto\widehat{f}$, currying a linear-out-of-tensor map into a linear-into-hom map.

2. **Operation 4 from the topic page (apply RAPL/LAPC to transport (co)limits).** Part (b) deduces right/left exactness by applying preservation of colimits/limits to the left/right adjoint.

3. **Operation 10 from the topic page (curry).** The tensor-hom adjunction is currying for the monoidal product $\otimes$; recognising it as such is the conceptual content.

---

# Hints

> [!note]- Hint 1
> Do not work with elements of $A\otimes_R M$. Use the universal property: a linear map $A\otimes_R M\to B$ is *the same data* as a bilinear map $A\times M\to B$.

> [!note]- Hint 2
> A bilinear map $\beta : A\times M\to B$ can be curried: for fixed $a\in A$, $\beta(a, -) : M\to B$ is linear, so $a\mapsto\beta(a,-)$ is a map $A\to\mathrm{Hom}_R(M, B)$. Check this map is $R$-linear in $a$ and that currying is a bijection.

> [!note]- Hint 3
> For exactness in part (b): the right adjoint preserves limits, and a kernel is a limit (an equalizer with the zero map); so $\mathrm{Hom}(M,-)$ preserves kernels, i.e. is left exact. Dually $-\otimes M$, a left adjoint, preserves cokernels, i.e. is right exact. The *failure* of $-\otimes M$ to be left exact is measured by $\mathrm{Tor}$.

---

# Solution

The solution composes two bijections. First, the universal property of the tensor product turns linear maps out of $A\otimes M$ into bilinear maps on $A\times M$. Second, currying turns bilinear maps on $A\times M$ into linear maps $A\to\mathrm{Hom}(M,B)$. Naturality is inherited from both. Part (b) then reads exactness off the adjunction's handedness.

**Step 1: Linear-out-of-tensor $=$ bilinear (universal property).**

By the [[Thm - Universal Property of the Tensor Product of Modules|universal property]], $\mathrm{Hom}_R(A\otimes_R M, B)\cong\mathrm{Bilin}_R(A\times M, B)$, the set of $R$-bilinear maps $A\times M\to B$, naturally in $A$ and $B$.

> [!note]- Derivation
> The universal property says: the canonical bilinear map $\otimes : A\times M\to A\otimes_R M$ is universal, so precomposition with $\otimes$ is a bijection $\mathrm{Hom}_R(A\otimes_R M, B)\xrightarrow{\cong}\mathrm{Bilin}_R(A\times M, B)$, $f\mapsto f\circ\otimes$. Naturality in $B$ is postcomposition; naturality in $A$ is precomposition with $h\times 1_M$. This is just the representability of $\mathrm{Bilin}_R(-\times M, B)$ by $-\otimes_R M$.

**Step 2: Bilinear $=$ linear-into-hom (currying).**

$\mathrm{Bilin}_R(A\times M, B)\cong\mathrm{Hom}_R(A, \mathrm{Hom}_R(M, B))$, naturally.

> [!note]- Derivation
> Given a bilinear $\beta : A\times M\to B$, define $\widehat{\beta} : A\to\mathrm{Hom}_R(M, B)$ by $\widehat{\beta}(a) = \beta(a, -)$. Bilinearity in the second slot makes $\beta(a,-)$ $R$-linear (so it lands in $\mathrm{Hom}_R(M,B)$); bilinearity in the first slot makes $a\mapsto\widehat{\beta}(a)$ $R$-linear:
> $$\widehat{\beta}(ra + a') = \beta(ra+a', -) = r\beta(a,-) + \beta(a',-) = r\widehat{\beta}(a) + \widehat{\beta}(a').$$
> Conversely a linear $g : A\to\mathrm{Hom}_R(M,B)$ uncurries to $\widetilde{g}(a, m) = g(a)(m)$, which is bilinear. Currying and uncurrying are mutually inverse, giving the bijection; it is natural in $A$ (precomposition) and $B$ (postcomposition).

**Step 3: Compose and conclude the adjunction (part b).**

Composing Steps 1 and 2 gives $\mathrm{Hom}_R(A\otimes_R M, B)\cong\mathrm{Hom}_R(A, \mathrm{Hom}_R(M, B))$, natural in $A, B$, so $-\otimes_R M\dashv\mathrm{Hom}_R(M,-)$.

> [!note]- Derivation
> The composite of the Step 1 and Step 2 bijections is natural in both variables (composite of natural isomorphisms). By [[Def - Adjunction|the definition of an adjunction]] with left adjoint $L = -\otimes_R M$ and right adjoint $R = \mathrm{Hom}_R(M,-)$, this is $L\dashv R$.
>
> **Unit** $\eta_A : A\to\mathrm{Hom}_R(M, A\otimes_R M)$ is the transpose of $1_{A\otimes M}$: it sends $a\mapsto(m\mapsto a\otimes m)$.
>
> **Counit** $\varepsilon_B : \mathrm{Hom}_R(M, B)\otimes_R M\to B$ is **evaluation**: it sends $\phi\otimes m\mapsto\phi(m)$.
>
> **Exactness.** A short exact sequence is a (co)limit datum: a kernel is a [[Def - Limit and Colimit|limit]], a cokernel a colimit. By [[Thm - Right Adjoints Preserve Limits|RAPL]], the right adjoint $\mathrm{Hom}_R(M,-)$ preserves limits, in particular kernels, so applying it to $0\to B'\to B\to B''$ keeps exactness on the left — it is **left exact**. By LAPC, the left adjoint $-\otimes_R M$ preserves colimits, in particular cokernels, so it keeps exactness on the right — it is **right exact**. Neither preserves the *other* end in general; the failure of $-\otimes M$ to be left exact is measured by the derived functors $\mathrm{Tor}^R_n(-, M)$.

> [!note]- Complete formal solution
> Fix the commutative ring $R$ and module $M$.
>
> **(a)** By the universal property of the tensor product, precomposition with the canonical bilinear map gives a natural bijection $\mathrm{Hom}_R(A\otimes_R M, B)\cong\mathrm{Bilin}_R(A\times M, B)$. Currying gives a natural bijection $\mathrm{Bilin}_R(A\times M, B)\cong\mathrm{Hom}_R(A, \mathrm{Hom}_R(M, B))$ via $\beta\mapsto(a\mapsto\beta(a,-))$, with inverse $g\mapsto((a,m)\mapsto g(a)(m))$; both directions are $R$-linear by bilinearity. Composing yields the natural isomorphism
> $$\mathrm{Hom}_R(A\otimes_R M, B)\cong\mathrm{Hom}_R(A, \mathrm{Hom}_R(M, B)).$$
>
> **(b)** This natural isomorphism is exactly the adjunction $-\otimes_R M\dashv\mathrm{Hom}_R(M,-)$. The unit is $\eta_A(a) = (m\mapsto a\otimes m)$ and the counit is evaluation $\varepsilon_B(\phi\otimes m) = \phi(m)$. By RAPL the right adjoint $\mathrm{Hom}_R(M,-)$ preserves limits (hence kernels), so it is left exact; by LAPC the left adjoint $-\otimes_R M$ preserves colimits (hence cokernels), so it is right exact. $\blacksquare$

---

# Key Takeaways

**Tensor-hom is currying for the monoidal product — the same adjunction as the exponential, with $\otimes$ in place of $\times$.** The isomorphism $\mathrm{Hom}(A\otimes M, B)\cong\mathrm{Hom}(A,\mathrm{Hom}(M,B))$ has exactly the shape of the [[Def - Cartesian Closed Category|cartesian closed]] currying $\mathcal{C}(A\times B, C)\cong\mathcal{C}(A, C^B)$, with the categorical product replaced by the tensor product and the exponential replaced by the internal hom $\mathrm{Hom}_R(M,-)$. This is the defining feature of a *closed monoidal category*: $\mathbf{Mod}_R$ is closed for $\otimes$ even though it is not cartesian closed for its product. The trigger to expect such an adjunction is any "bilinear/multilinear" or "two-argument" structure — wherever maps-out-of-a-product-like-object are governed by a universal multilinear property, currying produces an internal-hom right adjoint.

**Route through the universal property, never through elements.** The decisive technique was to use the universal property of $\otimes$ to convert "linear maps out of the tensor product" into "bilinear maps", which curry transparently, rather than constructing the isomorphism on general elements $\sum a_i\otimes m_i$. General tensors are awkward (the representation is not unique), but maps *out of* the tensor product are governed entirely by bilinearity. This is the universal-property discipline: to understand a universal object, study the maps out of it, not its elements. The same discipline makes every tensor-product computation tractable.

**Exactness is handedness — right exact means left adjoint, left exact means right adjoint.** The most reusable consequence is that the homological behaviour of $\otimes$ and $\mathrm{Hom}$ is *forced* by their roles in the adjunction. A left adjoint preserves colimits, hence cokernels, hence is right exact ($\otimes$); a right adjoint preserves limits, hence kernels, hence is left exact ($\mathrm{Hom}$). You never need to recompute this for a new pair of adjoint functors between abelian categories: identify which is the left adjoint, and you instantly know which exactness it has and which it can fail. The failure is exactly what derived functors ($\mathrm{Tor}$ for the right-exact $\otimes$, $\mathrm{Ext}$ for the left-exact $\mathrm{Hom}$) are built to measure — this is the doorway from adjunctions to homological algebra. See the companion preservation drill [[Ex - Right adjoints preserve limits in practice|Right adjoints preserve limits in practice]].
