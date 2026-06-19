---
type: exercise
subject: category-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - The Yoneda Embedding is Fully Faithful"
  - "Thm - The Yoneda Lemma"
  - "Def - Group"
  - "Def - Group Action"
tags: [category-theory, foundations]
---

# Problem Statement

A group $G$ may be regarded as a one-object category $BG$ whose single object has the elements of $G$ as its morphisms, with composition the group multiplication. Show that the [[Def - The Yoneda Embedding|Yoneda embedding]], applied to $BG$, recovers **Cayley's theorem**: every group is isomorphic to a subgroup of a symmetric group.

Specifically:
1. Identify the representable presheaf $\mathbf{y}(\bullet) = BG(-, \bullet)$ as the right $G$-set $G$ (with right-multiplication action).
2. Use the [[Thm - The Yoneda Lemma|Yoneda lemma]] / [[Thm - The Yoneda Embedding is Fully Faithful|full faithfulness]] to show that the $G$-equivariant endomorphisms of this $G$-set are exactly left-multiplications by elements of $G$, and deduce $G \cong \mathrm{Aut}_{G\text{-Set}}(G)$.
3. Compose with the forgetful functor to embed $G$ into the symmetric group on the underlying set of $G$.

**Recall:**

A [[Def - Group|group]] $G$ as the category $BG$: one object $\bullet$, morphisms $\mathrm{Hom}(\bullet, \bullet) = G$, composition $=$ multiplication. A presheaf $BG^{op} \to \mathbf{Set}$ is a right [[Def - Group Action|G-set]] — a set with a right group action. The [[Thm - The Yoneda Embedding is Fully Faithful|Yoneda embedding is fully faithful]]: $\mathcal{C}(A, B) \cong \mathrm{Nat}(\mathbf{y}A, \mathbf{y}B)$.

---

# Convergent Strategy

**Problem class:** This is a "specialize a structural theorem to recover a classical one" exercise — the most satisfying kind, where an abstract machine (Yoneda) outputs a concrete named result (Cayley). The routine is to translate the categorical statement into the language of the special category $BG$, then read off the classical conclusion.

**Assumption pattern:** The whole exercise rests on the dictionary "group = one-object category" and "presheaf on $BG$ = right $G$-set". Once those translations are in place, the representable presheaf, natural transformations, and full faithfulness all have concrete group-theoretic meanings, and Cayley's theorem is what full faithfulness *says* in this dictionary.

**Theorem routing:** The route is: (i) compute $\mathbf{y}(\bullet) = BG(-, \bullet)$ as the right $G$-set $G$; (ii) apply [[Thm - The Yoneda Embedding is Fully Faithful|full faithfulness]] to get $G = BG(\bullet, \bullet) \cong \mathrm{Nat}(\mathbf{y}\bullet, \mathbf{y}\bullet) = \mathrm{End}_{G\text{-Set}}(G)$; (iii) observe these endomorphisms are left-multiplications, all invertible, so $G \cong \mathrm{Aut}_{G\text{-Set}}(G)$; (iv) the forgetful functor to $\mathbf{Set}$ embeds this into the symmetric group.

**Key decision point:** The non-obvious step is recognizing that a natural transformation $\mathbf{y}\bullet \Rightarrow \mathbf{y}\bullet$ — by the Yoneda lemma determined by the image of the identity $1_\bullet \in G$ — is precisely *left-multiplication* by that image, and that naturality is exactly $G$-equivariance with respect to the *right* action. The interplay of left (the transformation) and right (the action) is the crux; getting the sides straight is what makes the proof click.

---

# Legal Operations Used

1. **Operation 8 from the topic page (translate between a group and its one-object category).** We pass back and forth between $G$ and $BG$, and between right $G$-sets and presheaves on $BG$.

2. **Operation 9 from the topic page (apply Yoneda full faithfulness to compute an endomorphism set).** Full faithfulness identifies $\mathrm{End}_{G\text{-Set}}(G)$ with $G$ itself.

---

# Hints

> [!note]- Hint 1
> In $BG$ there is one object, and $\mathbf{y}(\bullet) = BG(-, \bullet)$ evaluated at $\bullet$ is $BG(\bullet, \bullet) = G$. The presheaf structure (precomposition) is right multiplication, so $\mathbf{y}(\bullet)$ is the right regular $G$-set.

> [!note]- Hint 2
> Full faithfulness gives $G = BG(\bullet, \bullet) \cong \mathrm{Nat}(\mathbf{y}\bullet, \mathbf{y}\bullet)$. A natural transformation here is a $G$-equivariant map $G \to G$.

> [!note]- Hint 3
> By the Yoneda lemma a $G$-equivariant endomorphism is determined by the image of the identity $e$, and equivariance forces it to be $g \mapsto a \cdot g$ for that image $a$ — left multiplication. Left and right multiplication commute, which is why left-mult is right-equivariant.

> [!note]- Hint 4
> Every left-multiplication is a bijection (inverse is left-mult by $a^{-1}$), so $\mathrm{End} = \mathrm{Aut}$ and $G \cong \mathrm{Aut}_{G\text{-Set}}(G)$. Forgetting equivariance lands $G$ inside $\mathrm{Sym}(G)$.

---

# Solution

The plan: translate $G$ into $BG$, compute the representable presheaf as the right regular $G$-set, apply full faithfulness to identify $G$ with the equivariant endomorphisms of that set, recognize those as left-multiplications (hence automorphisms), and forget down to permutations.

**Step 1: The representable presheaf is the right regular $G$-set.**

> [!note]- Derivation
> The category $BG$ has one object $\bullet$ with $BG(\bullet, \bullet) = G$. A presheaf $BG^{op} \to \mathbf{Set}$ assigns to $\bullet$ a set $X$ with, for each morphism $g \in G$, a function $X \to X$, contravariantly — i.e. a *right* [[Def - Group Action|group action]]. The representable presheaf $\mathbf{y}(\bullet) = BG(-, \bullet)$ assigns $BG(\bullet, \bullet) = G$ to $\bullet$, and a morphism $g \in G$ acts by *pre*composition $h \mapsto h \cdot g$ — right multiplication. So $\mathbf{y}(\bullet)$ is the **right regular $G$-set** $G$.

**Step 2: Equivariant endomorphisms are left-multiplications, and $G \cong \mathrm{Aut}(G)$.**

> [!note]- Derivation
> By [[Thm - The Yoneda Embedding is Fully Faithful|full faithfulness]], $G = BG(\bullet, \bullet) \cong \mathrm{Nat}(\mathbf{y}\bullet, \mathbf{y}\bullet) = \mathrm{End}_{G\text{-Set}}(G)$, the right-$G$-equivariant endomorphisms of the right regular $G$-set. Concretely, by the [[Thm - The Yoneda Lemma|Yoneda lemma]] such an endomorphism $\alpha$ is determined by $\alpha(e) =: a \in G$, and equivariance ($\alpha(h g) = \alpha(h) g$) forces $\alpha(g) = \alpha(e \cdot g) = \alpha(e) g = a g$ — left multiplication $L_a$. This is right-equivariant precisely because left and right multiplication commute: $L_a(h g) = a h g = (a h) g = L_a(h) g$. Each $L_a$ is a bijection with inverse $L_{a^{-1}}$, so $\mathrm{End}_{G\text{-Set}}(G) = \mathrm{Aut}_{G\text{-Set}}(G)$, and the map $a \mapsto L_a$ is a group isomorphism $G \cong \mathrm{Aut}_{G\text{-Set}}(G)$ (it is a homomorphism: $L_{ab} = L_a L_b$, injective since $L_a(e) = a$, surjective by the above).

**Step 3: Embed into the symmetric group.**

> [!note]- Derivation
> The forgetful functor $G\text{-Set} \to \mathbf{Set}$ is faithful, so it embeds $\mathrm{Aut}_{G\text{-Set}}(G)$ into $\mathrm{Aut}_{\mathbf{Set}}(G) = \mathrm{Sym}(G)$, the symmetric group on the underlying set of $G$. Composing with $G \cong \mathrm{Aut}_{G\text{-Set}}(G)$ gives an injective homomorphism $G \hookrightarrow \mathrm{Sym}(G)$, $a \mapsto L_a$ — exactly the left regular representation. This is **Cayley's theorem**.

> [!note]- Complete formal solution
> Regard $G$ as the one-object category $BG$. The representable presheaf $\mathbf{y}(\bullet) = BG(-, \bullet)$ is the underlying set $G$ with right-multiplication action (precomposition), i.e. the right regular $G$-set. By [[Thm - The Yoneda Embedding is Fully Faithful|full faithfulness]] of Yoneda, $G = BG(\bullet, \bullet) \cong \mathrm{End}_{G\text{-Set}}(G)$, and by the [[Thm - The Yoneda Lemma|Yoneda lemma]] each such endomorphism is left-multiplication $L_a$ (determined by $a = \alpha(e)$, with equivariance forcing $\alpha(g) = ag$). Since each $L_a$ is invertible, $G \cong \mathrm{Aut}_{G\text{-Set}}(G)$ via $a \mapsto L_a$. The faithful forgetful functor embeds this into $\mathrm{Sym}(G)$, yielding the injective homomorphism $G \hookrightarrow \mathrm{Sym}(G)$ — Cayley's theorem. $\blacksquare$

> [!warning] Why the action must be the *right* regular action
> One might try to use the *left* regular action and natural transformations as *left*-equivariant maps. But the representable presheaf on $BG$ is contravariant, giving the *right* action, and the equivariant endomorphisms are then *left*-multiplications — the variances must be opposite for left-multiplication to be equivariant, because $L_a$ commutes with right-multiplication but not with left-multiplication. Mixing the sides makes naturality fail and the isomorphism $G \cong \mathrm{Aut}$ collapses. The opposite-handedness of "the transformation" and "the action" is essential, not cosmetic.

---

# Key Takeaways

**Cayley's theorem is the Yoneda embedding restricted to a one-object category — the abstract theorem contains the classical one as a special case.** The deep content is that "every group embeds in a symmetric group" is not a fact about groups specifically but a shadow of "every category embeds in its presheaves". A group is a category with one object, its presheaves are $G$-sets, the representable one is the regular representation, and full faithfulness says the group equals the automorphisms of that representation. The trigger to deploy this pattern is "I have an algebraic structure I want to represent concretely"; the reaction is "regard it as a one-object (or few-object) category and apply Yoneda" — this is how the regular representation of monoids, the Cayley–Dickson embedding, and faithful representations in general are seen as one phenomenon.

**The left/right handedness is the whole subtlety, and it comes from the contravariance of the embedding.** The single thing that can go wrong is mixing up which side multiplies. The representable presheaf carries the *right* action (precomposition is contravariant), and the natural endomorphisms are *left*-multiplications, because $L_a$ is exactly the map that commutes with the right action. This is a general lesson about Yoneda: the morphisms of the original category become natural transformations acting on the *opposite* side from the presheaf structure, and keeping the two sides straight is essential whenever you compute an endomorphism object via full faithfulness.

**"Determined by the image of the identity" is the engine, here and everywhere Yoneda is used.** The reason an equivariant endomorphism of $G$ is forced to be left-multiplication is the same reason a natural transformation out of a representable is pinned down by one element: the value on the identity propagates to everything by naturality/equivariance. Recognizing that the identity element $e \in G$ plays the role of the universal element $1_A$ unifies this computation with every other Yoneda application — the natural-transformations-via-Yoneda computation of [[Ex - Computing a natural transformation set via Yoneda]], the monoid case of [[Ex - The Yoneda lemma for posets and monoids]], and the scheme case of [[Ex - A scheme is determined by its functor of points]] are all "the identity determines the map".
