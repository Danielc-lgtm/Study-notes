---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Adjunction"
  - "Def - Free-Forgetful Adjunction"
  - "Def - Free Group and Free Product"
  - "Def - Group"
tags: [category-theory, foundations]
---

# Problem Statement

Let $U : \mathbf{Grp} \to \mathbf{Set}$ be the forgetful functor (it sends a group to its underlying set and a homomorphism to its underlying function) and $F : \mathbf{Set} \to \mathbf{Grp}$ the free-group functor (it sends a set $S$ to the [[Def - Free Group and Free Product|free group]] $FS$ on $S$).

**(a)** Construct a bijection $\Phi_{S, H} : \mathbf{Grp}(FS, H) \xrightarrow{\cong} \mathbf{Set}(S, UH)$ for every set $S$ and group $H$, and describe its inverse.

**(b)** Prove that $\Phi$ is natural in both variables, so that $F \dashv U$.

**(c)** Identify the unit $\eta_S : S \to UFS$ and the counit $\varepsilon_H : FUH \to H$ as the transposes of identity morphisms.

**Recall:**

A [[Def - Free Group and Free Product|free group]] $FS$ on a set $S$ has the **universal property**: there is a function $\iota : S \to UFS$ (insertion of generators) such that for every group $H$ and every function $g : S \to UH$, there is a *unique* homomorphism $\widehat{g} : FS \to H$ with $U\widehat{g} \circ \iota = g$. Concretely $FS$ is the set of reduced words in the symbols $s$ and $s^{-1}$ for $s \in S$, with concatenation-and-reduction as the group operation.

![[Def - Adjunction#The Definition]]

An [[Def - Free-Forgetful Adjunction|adjunction]] $F \dashv U$ is a natural bijection $\mathbf{Grp}(FS, H) \cong \mathbf{Set}(S, UH)$; the [[Def - Unit and Counit of an Adjunction|unit]] is $\eta_S = \Phi(1_{FS})$ and the counit is $\varepsilon_H = \Phi^{-1}(1_{UH})$.

---

# Convergent Strategy

**Problem class:** This is an "exhibit an adjunction directly" problem of the kind described in the [[Category Theory IV — Adjunctions#Problem-Solving Strategy|topic page strategy]] — you work in the hom-set face, write the candidate bijection, and verify it is a natural isomorphism. It is the prototypical such problem because the bijection *is* a universal property restated.

**Assumption pattern:** The decisive assumption is the universal property of the free group: "a homomorphism out of $FS$ is uniquely determined by, and freely chooses, where the generators go". This is exactly a statement that homomorphisms $FS \to H$ correspond to functions $S \to UH$ — the bijection is handed to you by the definition of "free", so part (a) is almost immediate, and the work concentrates in naturality (b).

**Theorem routing:** The route is: universal property of $FS$ $\Rightarrow$ pointwise bijection $\Phi$ (part a) $\Rightarrow$ naturality via uniqueness of the induced homomorphism (part b) $\Rightarrow$ $F\dashv U$ by [[Def - Adjunction|the definition of adjunction]]. Part (c) then reads off the [[Def - Unit and Counit of an Adjunction|unit and counit]] by transposing identities, using $\eta_S = \Phi(1_{FS})$.

**Key decision point:** The non-obvious choice is to verify naturality using the *uniqueness* clause of the universal property rather than by manipulating reduced words. Two homomorphisms out of $FS$ that agree on generators are equal, so to check a naturality square commutes it suffices to check it on the generating set $S$ — collapsing an identity of homomorphisms to an identity of functions on $S$. Trying to verify naturality by direct word computation is possible but far messier.

---

# Legal Operations Used

1. **Operation 2 from the topic page (recognise a forgetful functor and produce its free left adjoint).** We identify $U : \mathbf{Grp}\to\mathbf{Set}$ as the forgetful functor and $F$ as its free left adjoint, which is what licenses writing the bijection $\mathbf{Grp}(FS, H)\cong\mathbf{Set}(S, UH)$ in the first place.

2. **Operation 5 from the topic page (use the universal property of the unit as an initial object).** To *define* a homomorphism $FS\to H$ we specify a function $S\to UH$ and invoke the universal property; this is how $\Phi^{-1}$ is built and is the heart of part (a).

3. **Operation 3 from the topic page (build the unit and counit from the hom-set isomorphism).** In part (c) we transpose $1_{FS}$ and $1_{UH}$ to extract the unit and counit.

---

# Hints

> [!note]- Hint 1
> The definition of "free group" already says what homomorphisms out of $FS$ are. Read the universal property as a bijection and you have part (a) almost for free.

> [!note]- Hint 2
> For part (b), naturality in $H$ asks that postcomposing a homomorphism $FS\to H$ with $k : H\to H'$ corresponds, on the other side, to postcomposing the function $S\to UH$ with $Uk$. Check both sides agree as functions on $S$, using that homomorphisms agreeing on generators are equal.

> [!note]- Hint 3
> For part (c): the unit is $\eta_S = \Phi(1_{FS})$. By the formula $\Phi(f) = Uf\circ\eta_S$... but wait — $\eta_S$ *is* what we are computing. Instead recall $\eta_S$ is the transpose of the *identity* $1_{FS} : FS\to FS$, which under the universal property is the insertion of generators $\iota : S\to UFS$. The counit $\varepsilon_H : FUH\to H$ is the unique homomorphism extending the identity function $UH\to UH$ — it multiplies a formal word of elements of $H$ out.

---

# Solution

The solution has three parts. Part (a) reads the bijection straight off the universal property of the free group. Part (b) proves naturality by checking the two squares on generators, using that homomorphisms out of $FS$ are determined by their values on $S$. Part (c) transposes the identities to find that the unit is insertion of generators and the counit is "multiply the word out". The single idea threaded through all three is *a homomorphism out of $FS$ is a function on $S$*.

**Step 1: The bijection (part a).**

The universal property gives, for each function $g : S \to UH$, a unique homomorphism $\widehat{g} : FS \to H$ with $U\widehat{g}\circ\iota = g$. Define $\Phi^{-1}(g) = \widehat{g}$ and $\Phi(f) = Uf\circ\iota$ for a homomorphism $f : FS\to H$. These are mutually inverse, so $\Phi : \mathbf{Grp}(FS, H)\cong\mathbf{Set}(S, UH)$ is a bijection.

> [!note]- Derivation
> Given $f : FS\to H$, set $\Phi(f) = Uf\circ\iota : S\to UH$ (restrict $f$ to the generators). Given $g : S\to UH$, the universal property yields the unique $\widehat{g} : FS\to H$ with $U\widehat{g}\circ\iota = g$; set $\Phi^{-1}(g) = \widehat{g}$.
> - $\Phi(\Phi^{-1}(g)) = U\widehat{g}\circ\iota = g$ by the defining equation of $\widehat{g}$.
> - $\Phi^{-1}(\Phi(f))$: we need the unique homomorphism whose restriction to generators is $Uf\circ\iota$. But $f$ itself is a homomorphism with $Uf\circ\iota = Uf\circ\iota$, and uniqueness in the universal property forces $\Phi^{-1}(\Phi(f)) = f$.
>
> So $\Phi$ is a bijection with inverse $g\mapsto\widehat{g}$.

**Step 2: Naturality (part b).**

$\Phi$ is natural in $H$ (postcomposition) and in $S$ (precomposition). Each square is verified by evaluating on the generating set $S$ and using that homomorphisms out of $FS$ are determined by their restriction to $S$.

> [!note]- Derivation
> **Naturality in $H$.** Let $k : H\to H'$. We must show $\Phi_{S,H'}(k\circ f) = Uk\circ\Phi_{S,H}(f)$ for $f : FS\to H$. Left side: $\Phi(k\circ f) = U(k\circ f)\circ\iota = Uk\circ Uf\circ\iota$. Right side: $Uk\circ(Uf\circ\iota) = Uk\circ Uf\circ\iota$. They are equal as functions $S\to UH'$. (No uniqueness needed here, since $\Phi$ is restriction.)
>
> **Naturality in $S$.** Let $h : S'\to S$. We must show $\Phi_{S',H}(f\circ Fh) = \Phi_{S,H}(f)\circ h$ for $f : FS\to H$, where $Fh : FS'\to FS$ is the homomorphism induced by $h$ (it sends a generator $s'$ to the generator $h(s')$). Left side: $\Phi(f\circ Fh) = U(f\circ Fh)\circ\iota_{S'} = Uf\circ U(Fh)\circ\iota_{S'}$. Now $U(Fh)\circ\iota_{S'} = \iota_S\circ h$ (the functor $F$ on the morphism $h$ is *defined* so that on generators it is $h$ followed by insertion — this is naturality of $\iota$). So the left side is $Uf\circ\iota_S\circ h = \Phi(f)\circ h$, the right side.
>
> Hence $\Phi$ is natural in both variables, and $F\dashv U$.

**Step 3: Unit and counit (part c).**

The unit $\eta_S : S\to UFS$ is the insertion of generators $\iota$. The counit $\varepsilon_H : FUH\to H$ is the homomorphism that multiplies a formal word out: $\varepsilon_H(h_1^{\pm}\cdots h_n^{\pm}) = h_1^{\pm}\cdots h_n^{\pm}$ computed in $H$.

> [!note]- Derivation
> **Unit.** $\eta_S = \Phi_{S, FS}(1_{FS}) = U(1_{FS})\circ\iota = \iota : S\to UFS$. So the unit is exactly the insertion of generators.
>
> **Counit.** $\varepsilon_H = \Phi^{-1}_{UH, H}(1_{UH})$ is the unique homomorphism $FUH\to H$ whose restriction to the generators $UH$ is the identity function $1_{UH} : UH\to UH$. The free group $FUH$ has the *elements of $H$* as generators; the unique homomorphism sending each generator $h\in UH$ to itself in $H$ takes a reduced word $h_1^{\epsilon_1}\cdots h_n^{\epsilon_n}$ (with $h_i\in H$, $\epsilon_i = \pm 1$) to the product $h_1^{\epsilon_1}\cdots h_n^{\epsilon_n}$ evaluated in $H$. This is "multiply the formal word out".
>
> The first triangle identity $\varepsilon_{FS}\circ F\eta_S = 1_{FS}$ reads: insert generators of $S$, freely build the free group on those one-letter words, then multiply each one-letter word out — recovering the generators. The second, $U\varepsilon_H\circ\eta_{UH} = 1_{UH}$, reads: include the elements of $H$ as one-letter words, then multiply them out — the identity on $UH$.

> [!note]- Complete formal solution
> Let $\iota_S : S\to UFS$ be the insertion of generators, with the universal property: for every $g : S\to UH$ there is a unique homomorphism $\widehat{g} : FS\to H$ with $U\widehat{g}\circ\iota_S = g$.
>
> **(a)** Define $\Phi_{S,H} : \mathbf{Grp}(FS, H)\to\mathbf{Set}(S, UH)$ by $\Phi(f) = Uf\circ\iota_S$ and $\Psi = \Phi^{-1}$ by $\Psi(g) = \widehat{g}$. Then $\Phi\Psi(g) = U\widehat{g}\circ\iota_S = g$, and $\Psi\Phi(f) = f$ by uniqueness (since $f$ restricts to $Uf\circ\iota_S$ on generators). So $\Phi$ is a bijection.
>
> **(b)** *Naturality in $H$:* for $k : H\to H'$, $\Phi(k f) = U(kf)\iota_S = Uk\, Uf\,\iota_S = Uk\,\Phi(f)$. *Naturality in $S$:* for $h : S'\to S$, using $U(Fh)\iota_{S'} = \iota_S h$ (naturality of insertion), $\Phi(f\,Fh) = Uf\,U(Fh)\,\iota_{S'} = Uf\,\iota_S\,h = \Phi(f)\,h$. Hence $\Phi$ is a natural isomorphism and $F\dashv U$.
>
> **(c)** $\eta_S = \Phi(1_{FS}) = \iota_S$ (insertion of generators). $\varepsilon_H = \Psi(1_{UH})$ is the unique homomorphism $FUH\to H$ extending $1_{UH}$, i.e. the map sending a reduced word $h_1^{\epsilon_1}\cdots h_n^{\epsilon_n}$ (letters in $H$) to its product in $H$. The triangle identities hold by construction of $\Phi$ via the universal property. $\blacksquare$

---

# Key Takeaways

**The universal property of a free object is literally an adjunction — recognising this is the whole point.** The phrase "a homomorphism out of $FS$ is a function out of $S$" is not an informal slogan; it is the precise statement $\mathbf{Grp}(FS, H)\cong\mathbf{Set}(S, UH)$, and that bijection, once shown natural, *is* the adjunction $F\dashv U$. The trigger to apply this pattern is any construction described as "the free X on generators", "the X freely generated by", or "the most efficient X containing". When you see it, write the hom-set bijection immediately; you have an adjunction, and with it the unit (insertion of generators), the counit (evaluation), uniqueness of the free object, and the (co)limit-preservation behaviour, all for free. This single recognition replaces a page of ad-hoc verification with a one-line invocation.

**Naturality is checked on generators, not on all elements.** The reusable technique in part (b) is that an identity of homomorphisms out of a free object can be verified on the generating set, because the universal property guarantees that homomorphisms agreeing on generators are equal. This collapses a naturality square — an equation between morphisms in $\mathbf{Grp}$ — into an equation between functions in $\mathbf{Set}$, which is almost always trivial to check. The same move works for any free or presented object: to prove two maps out of it coincide, evaluate on generators. This is the categorical version of "a linear map is determined by its action on a basis".

**The unit and counit have stable concrete meanings: insertion and evaluation.** Across every free-forgetful adjunction the unit inserts generators (the embedding $S\hookrightarrow UFS$) and the counit evaluates (the structure map $FUH\to H$ that interprets a formal expression in the actual object). For the free group this is "include generators" and "multiply the word out"; for the free module it is "include basis vectors" and "sum the formal linear combination"; for the free monoid it is "the length-one strings" and "concatenate". Whenever you meet a new free-forgetful adjunction, the fastest way to understand it is to ask: what does the unit insert, and what does the counit evaluate? The triangle identities then say these two operations undo each other in the precise whiskered sense, and checking them on generators is routine. This exercise is the template; the companion exercises [[Ex - The free vector space adjunction|The free vector space adjunction]] and [[Ex - Unit and counit of the free-forgetful adjunction|Unit and counit of the free-forgetful adjunction]] run the same machine in different categories.
