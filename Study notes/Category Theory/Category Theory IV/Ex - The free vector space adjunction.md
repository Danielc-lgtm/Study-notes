---
type: exercise
subject: category-theory
difficulty: "⭐"
prereqs:
  - "Def - Adjunction"
  - "Def - Free-Forgetful Adjunction"
  - "Def - Vector Space"
tags: [category-theory, foundations]
---

# Problem Statement

Fix a field $k$. Let $U : \mathbf{Vect}_k \to \mathbf{Set}$ be the forgetful functor and let $F : \mathbf{Set} \to \mathbf{Vect}_k$ send a set $S$ to the **free vector space** $FS = k^{(S)}$, the space of finitely-supported functions $S \to k$ (equivalently, formal finite $k$-linear combinations of elements of $S$), which has $S$ as a basis.

**(a)** Establish the natural bijection $\mathbf{Vect}_k(k^{(S)}, V) \cong \mathbf{Set}(S, UV)$, so that $F \dashv U$.

**(b)** Identify the unit and counit, and explain what "a linear map is determined by its values on a basis, and those values may be chosen freely" means in adjunction language.

**Recall:**

A [[Def - Vector Space|vector space]] over $k$ is an abelian group with a compatible $k$-scalar action; a linear map preserves both. The free vector space $k^{(S)}$ has basis $\{e_s : s\in S\}$ where $e_s$ is the indicator function of $s$; a general element is a finite sum $\sum_{s} c_s e_s$ with $c_s\in k$.

![[Def - Free-Forgetful Adjunction#The Definition]]

---

# Convergent Strategy

**Problem class:** This is the simplest instance of "exhibit a free-forgetful adjunction directly" (⭐), the same machine as [[Ex - The free-forgetful adjunction for groups|the free group adjunction]] but in the friendliest possible category, where freeness is just "having a basis".

**Assumption pattern:** The assumption that does all the work is the universal property of a basis: a linear map out of $k^{(S)}$ is determined by, and freely chooses, its values on the basis $S$. This is the linear-algebra fact "to define a linear map, say where the basis goes" — recognised as the free-forgetful bijection.

**Theorem routing:** Universal property of the basis $\Rightarrow$ bijection $\mathbf{Vect}(k^{(S)}, V)\cong\mathbf{Set}(S, UV)$ $\Rightarrow$ naturality (linear maps determined on the basis) $\Rightarrow$ $F\dashv U$ by [[Def - Adjunction|definition]]. The unit and counit are then transposes of identities.

**Key decision point:** The only subtlety is to remember that $k^{(S)}$ uses *finitely-supported* functions (the direct sum $k^{(S)}$), not all functions ($k^S$, the product). The free object is the coproduct-flavoured one; using $k^S$ would break the universal property for infinite $S$ because a linear map into $V$ cannot be defined by arbitrary values on an infinite basis-with-infinite-support.

---

# Legal Operations Used

1. **Operation 2 from the topic page (recognise a forgetful functor and produce its free left adjoint).** $U : \mathbf{Vect}_k\to\mathbf{Set}$ is forgetful; its free left adjoint is $S\mapsto k^{(S)}$.

2. **Operation 5 from the topic page (use the universal property of the unit).** To define a linear map out of $k^{(S)}$ we specify a function $S\to UV$ and extend linearly — the universal property of the unit (insertion of the basis).

3. **Operation 3 from the topic page (build the unit and counit).** Part (b) transposes identities to read off insertion-of-basis and evaluation.

---

# Hints

> [!note]- Hint 1
> "A linear map is determined by its values on a basis" already says $\mathbf{Vect}(k^{(S)}, V)\cong\mathbf{Set}(S, UV)$. The right side is the values on the basis.

> [!note]- Hint 2
> Given $g : S\to UV$, the corresponding linear map sends $\sum c_s e_s\mapsto\sum c_s g(s)$. Check this is linear and that the correspondence is a bijection.

> [!note]- Hint 3
> The unit $\eta_S : S\to U k^{(S)}$ is $s\mapsto e_s$ (insert the basis). The counit $\varepsilon_V : k^{(UV)}\to V$ sums a formal linear combination of actual vectors: $\sum c_v e_v\mapsto\sum c_v\cdot v$.

---

# Solution

Freeness for vector spaces is the existence of a basis. The bijection is "values on the basis"; naturality is "linear maps are determined on the basis"; the unit inserts the basis and the counit sums a formal combination.

**Step 1: The bijection (part a).**

Define $\Phi : \mathbf{Vect}_k(k^{(S)}, V)\to\mathbf{Set}(S, UV)$ by $\Phi(T) = UT\circ\eta_S$ (restrict $T$ to the basis), with inverse extending a function linearly. This is a bijection, natural in $S$ and $V$.

> [!note]- Derivation
> Let $\eta_S : S\to U k^{(S)}$, $s\mapsto e_s$. Given a linear $T : k^{(S)}\to V$, set $\Phi(T) = UT\circ\eta_S$, the function $s\mapsto T(e_s)$. Given a function $g : S\to UV$, define $\Phi^{-1}(g) = \widehat{g}$ by $\widehat{g}\big(\sum_s c_s e_s\big) = \sum_s c_s\, g(s)$; this is well-defined because the sum is finite, and linear because the $e_s$ form a basis. Then:
> - $\Phi(\widehat{g})(s) = \widehat{g}(e_s) = g(s)$, so $\Phi\Phi^{-1} = \mathrm{id}$.
> - $\widehat{\Phi(T)}\big(\sum c_s e_s\big) = \sum c_s T(e_s) = T\big(\sum c_s e_s\big)$ by linearity of $T$, so $\Phi^{-1}\Phi = \mathrm{id}$.
>
> Naturality in $V$ (postcompose with a linear $k : V\to V'$): $\Phi(kT) = U(kT)\eta_S = Uk\,UT\,\eta_S = Uk\,\Phi(T)$. Naturality in $S$ (precompose with $h : S'\to S$, where $Fh(e_{s'}) = e_{h(s')}$): $\Phi(T\circ Fh)(s') = T(Fh(e_{s'})) = T(e_{h(s')}) = \Phi(T)(h(s'))$, i.e. $\Phi(T\circ Fh) = \Phi(T)\circ h$. So $\Phi$ is a natural isomorphism and $F\dashv U$.

**Step 2: Unit and counit (part b).**

The unit $\eta_S : S\to U k^{(S)}$, $s\mapsto e_s$, inserts the basis. The counit $\varepsilon_V : k^{(UV)}\to V$, $\sum c_v e_v\mapsto\sum c_v\cdot v$, sums a formal linear combination of actual vectors.

> [!note]- Derivation
> $\eta_S = \Phi(1_{k^{(S)}})$ sends $s\mapsto 1_{k^{(S)}}(e_s) = e_s$ — the insertion of the basis. $\varepsilon_V = \Phi^{-1}(1_{UV})$ is the unique linear map $k^{(UV)}\to V$ extending the identity function $UV\to UV$: it sends a formal combination $\sum_v c_v e_v$ (over actual vectors $v\in V$) to $\sum_v c_v\cdot v$, the genuine linear combination in $V$.
>
> The statement "a linear map is determined by its values on a basis, and those values are free" is exactly the bijectivity of $\Phi$: *determined* is injectivity (a linear map $T$ is recovered from $T\circ\eta_S$), and *free* is surjectivity (every function on the basis extends to some linear map). The triangle identity $\varepsilon_{FS}\circ F\eta_S = 1_{FS}$ says: insert the basis, freely build the free space on those basis vectors, then sum each one back — recovering $k^{(S)}$.

> [!note]- Complete formal solution
> Let $\eta_S : S\to U k^{(S)}$, $s\mapsto e_s$.
>
> **(a)** $\Phi(T) = s\mapsto T(e_s)$ and $\Phi^{-1}(g) = \big(\sum c_s e_s\mapsto\sum c_s g(s)\big)$ are mutually inverse: $\Phi\Phi^{-1}(g)(s) = g(s)$ and $\Phi^{-1}\Phi(T) = T$ by linearity. Naturality in $V$ is postcomposition; naturality in $S$ uses $Fh(e_{s'}) = e_{h(s')}$. Hence $\mathbf{Vect}_k(k^{(S)}, V)\cong\mathbf{Set}(S, UV)$ naturally, so $F\dashv U$.
>
> **(b)** Unit $\eta_S(s) = e_s$ (insert the basis). Counit $\varepsilon_V\big(\sum c_v e_v\big) = \sum c_v\cdot v$ (sum the formal combination). The adjunction bijection is precisely the linear-algebra fact that a linear map is freely determined by its action on a basis. $\blacksquare$

---

# Key Takeaways

**"Having a basis" is exactly "being a free object", and a basis is the unit of the free-forgetful adjunction.** The familiar slogan "to define a linear map, say where the basis goes, and it can go anywhere" is the bijection $\mathbf{Vect}(k^{(S)}, V)\cong\mathbf{Set}(S, UV)$ — the free vector space adjunction. The basis vectors are the image of the unit $\eta_S$, and the universal property of a basis is the universal property of the unit. This recasts a first-week linear algebra fact as a categorical structure, and it explains why bases behave the way they do: they are the generators of a free object, and free objects are governed by maps *out* of them. Every vector space is a quotient of a free one (via the counit), which is the categorical content of "every space has a basis".

**The free functor uses the direct sum (coproduct), not the product.** The free vector space on $S$ is $k^{(S)}$ — *finitely-supported* functions — not $k^S$, all functions. This matters because the free functor is a *left* adjoint and left adjoints preserve coproducts: $k^{(S\sqcup T)}\cong k^{(S)}\oplus k^{(T)}$, the direct sum. If you used $k^S$ the universal property would fail for infinite $S$, because a linear map out of $k^S$ is *not* freely determined by its values on the standard basis vectors (there are linear functionals on $k^S$ not supported on finitely many coordinates). The lesson generalizes: the free object on a set is built from a coproduct/direct-sum, and confusing it with the product is the standard error — it is the same trap as "the free group preserves products".

**This is the template every free-forgetful adjunction follows, in its cleanest form.** Because $\mathbf{Vect}_k$ is so well-behaved (every module is free, i.e. every space has a basis), the free vector space adjunction is the calibration example: the unit inserts the basis, the counit sums a formal combination, naturality is "determined on the basis", and the bijection is "values on the basis". When a free-forgetful adjunction in a harder category ([[Ex - The free-forgetful adjunction for groups|groups]], modules over a non-field, monoids) feels opaque, map it back to this one — the structure is identical, only the construction of the free object changes. The companion exercise [[Ex - The free-forgetful adjunction for groups|The free-forgetful adjunction for groups]] runs the same steps where "basis" is replaced by "free generating set" and "sum the combination" by "multiply the word out".
