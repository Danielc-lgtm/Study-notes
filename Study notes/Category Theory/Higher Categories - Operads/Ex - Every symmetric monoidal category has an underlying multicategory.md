---
type: exercise
subject: higher-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Multicategory"
  - "Def - Monoidal Category"
  - "Def - Monad and Comonad"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $(\mathcal{V}, \otimes, I)$ be a symmetric [[Def - Monoidal Category|monoidal category]]. Define its **underlying multicategory** $\mathcal{V}^{\otimes}$ by taking the same objects and setting
$$\mathcal{V}^{\otimes}(a_1, \dots, a_n; b) = \mathcal{V}(a_1 \otimes \dots \otimes a_n,\ b),$$
with the convention that the empty tensor is $I$. Prove that $\mathcal{V}^{\otimes}$ is a symmetric [[Def - Multicategory|multicategory]]: define identities, substitution, and the symmetric action, and verify the axioms (you may suppress the associator and unitors by [[Thm - Mac Lane Coherence Theorem|coherence]], working as if $\otimes$ is strict). Then prove the converse-flavoured fact: a multicategory $\mathcal{M}$ arises as $\mathcal{V}^{\otimes}$ for some monoidal $\mathcal{V}$ — equivalently $\mathcal{M}$ is **representable** — if and only if every tuple of objects has a universal multimap out of it. Conclude that "monoidal category" and "representable multicategory" are interchangeable.

**Recall:**

![[Def - Monoidal Category#The Definition]]

A [[Def - Multicategory|multicategory]] $\mathcal{M}$ is **representable** if for every tuple $(a_1, \dots, a_n)$ there is an object $t$ and a universal multimap $u \in \mathcal{M}(a_1, \dots, a_n; t)$, meaning $(- \circ u) : \mathcal{M}(t; b) \to \mathcal{M}(a_1, \dots, a_n; b)$ is a bijection for all $b$.

---

# Convergent Strategy

**Problem class:** This is a *change-of-presentation* problem: show that two ways of recording the same mathematics (a monoidal structure versus a representable system of multimaps) carry the same information. The forward direction builds a multicategory from a monoidal category; the backward direction reconstructs the monoidal structure from a representability hypothesis.

**Assumption pattern:** The signal is a *tensor product packaging multi-input maps into single-object maps*. In a monoidal category, an $n$-input map is forced to be a single morphism out of the tensor $a_1 \otimes \dots \otimes a_n$; this is precisely what "representable multicategory" means. The symmetric braiding $\beta$ is the assumption that supplies the $S_n$-action on multimaps.

**Theorem routing:** Substitution in $\mathcal{V}^{\otimes}$ routes through the monoidal product of morphisms: given $f : b_1 \otimes \dots \otimes b_k \to c$ and $g_i : a_{i,\bullet}^{\otimes} \to b_i$, the composite is $f \circ (g_1 \otimes \dots \otimes g_k)$. Associativity and unit follow from [[Thm - Mac Lane Coherence Theorem|Mac Lane coherence]] (so the associators do not obstruct), and the $S_n$-action uses the symmetric braiding. The backward direction routes through the universal property: representing objects, being unique up to canonical isomorphism, assemble into a tensor with associator and unitors.

**Key decision point:** The crux is the *coherence suppression*. Without invoking Mac Lane's coherence theorem, the associativity axiom of the multicategory would require chasing a forest of associator and unitor isomorphisms, and it is easy to either over- or under-insert them. The decision to work in the strictified (equivalent strict monoidal) category, justified by coherence, is what makes the verification tractable — and one must remember to note that this is *legitimate* precisely because coherence guarantees a unique coherence isomorphism between any two bracketings.

---

# Legal Operations Used

1. **Build a multimap as a single morphism out of a tensor (operation 6 from the topic page).** We represent each $n$-input multimap as one morphism out of $a_1 \otimes \dots \otimes a_n$, which is the entire definition of $\mathcal{V}^{\otimes}$.

2. **Suppress coherence isomorphisms by Mac Lane's theorem (operation 7 from the topic page).** We replace $\mathcal{V}$ by an equivalent strict monoidal category so that associativity of substitution is on the nose.

3. **Use the braiding for the symmetric action (operation 5 from the topic page).** We define the $S_n$-action via the symmetry $\beta$ permuting tensor factors and verify equivariance from the symmetric coherence (hexagon).

4. **Recover a tensor from representing objects (operation 6 from the topic page).** In the backward direction, we define $a \otimes b$ as the representing object of $(a, b)$ and obtain coherence isomorphisms from uniqueness.

---

# Hints

> [!note]- Hint 1
> A multimap $a_1, \dots, a_n \to b$ is, by definition, a single morphism $a_1 \otimes \dots \otimes a_n \to b$. So substitution should be: tensor the inner morphisms, then compose with the outer. Write it out: $f \circ (g_1 \otimes \dots \otimes g_k)$.

> [!note]- Hint 2
> The identity multimap $1_a \in \mathcal{V}^{\otimes}(a;a) = \mathcal{V}(a, a)$ is the identity morphism. The unit laws use that $g \otimes (\dots)$ with identities is $g$ (after unitors).

> [!note]- Hint 3
> For the $S_n$-action, $\sigma \in S_n$ acts on $f : a_1 \otimes \dots \otimes a_n \to b$ by precomposing with the symmetry $\beta_\sigma : a_{\sigma^{-1}(1)} \otimes \dots \otimes a_{\sigma^{-1}(n)} \to a_1 \otimes \dots \otimes a_n$. Equivariance with substitution is the hexagon coherence for the braiding.

> [!note]- Hint 4
> Backward direction: define $a \otimes b$ to be the representing object of the pair $(a,b)$, with universal multimap $u_{a,b} : a, b \to a \otimes b$. The associator comes from the fact that both $(a \otimes b) \otimes c$ and $a \otimes (b \otimes c)$ represent the triple $(a,b,c)$ — and a triple's representing object is unique up to unique isomorphism.

---

# Solution

The plan: in the forward direction, define the multicategory data and verify the axioms after strictifying by coherence (Steps 1–3); in the backward direction, build a tensor from representing objects and obtain the coherence isomorphisms from their uniqueness (Steps 4–5); then state the equivalence (Step 6).

**Step 1: $\mathcal{V}^{\otimes}$ data, and strictification.**

> [!note]- Derivation
> By [[Thm - Mac Lane Coherence Theorem|Mac Lane's coherence theorem]], $\mathcal{V}$ is monoidally equivalent to a strict monoidal category, so we may assume $\otimes$ is strictly associative and unital and the associator/unitors are identities; the underlying multicategory is unchanged up to isomorphism. Now set $\mathcal{V}^{\otimes}(a_1, \dots, a_n; b) = \mathcal{V}(a_1 \otimes \dots \otimes a_n, b)$, with $1_a = \mathrm{id}_a \in \mathcal{V}(a,a) = \mathcal{V}^{\otimes}(a;a)$, empty tensor $= I$ so $\mathcal{V}^{\otimes}(\,; b) = \mathcal{V}(I, b)$.

**Step 2: Substitution and its associativity and unit laws.**

> [!note]- Derivation
> Given $f \in \mathcal{V}^{\otimes}(b_1, \dots, b_k; c) = \mathcal{V}(b_1 \otimes \dots \otimes b_k, c)$ and $g_i \in \mathcal{V}^{\otimes}(a_{i,1}, \dots, a_{i,n_i}; b_i) = \mathcal{V}(a_{i,1} \otimes \dots, b_i)$, define
> $$f \circ (g_1, \dots, g_k) = f \circ (g_1 \otimes \dots \otimes g_k) \in \mathcal{V}\big((a_{1,1} \otimes \dots \otimes a_{k,n_k}), c\big),$$
> using that $\otimes$ of the sources $b_i$ is $b_1 \otimes \dots \otimes b_k$ (strictly). Associativity: for a third layer $h_{i,j}$, both grafting orders equal $f \circ (g_1 \otimes \dots) \circ (h_{\bullet})$ by functoriality and associativity of $\otimes$ on morphisms and associativity of $\circ$ in $\mathcal{V}$. Unit: $f \circ (1_{a_1} \otimes \dots \otimes 1_{a_n}) = f \circ \mathrm{id} = f$, and $1_c \circ (f) = f$.

**Step 3: Symmetric action and equivariance.**

> [!note]- Derivation
> For $\sigma \in S_n$ and $f : a_1 \otimes \dots \otimes a_n \to b$, set $f \cdot \sigma = f \circ \beta_\sigma$, where $\beta_\sigma : a_{\sigma^{-1}(1)} \otimes \dots \otimes a_{\sigma^{-1}(n)} \to a_1 \otimes \dots \otimes a_n$ is the canonical symmetry built from the braiding $\beta$. That $\sigma \mapsto (-\cdot\sigma)$ is an action uses the coherence of the symmetry ($\beta_{\sigma\tau} = \beta_\sigma \circ \beta_\tau$ up to the canonical identification), which is the symmetric-monoidal coherence theorem. Equivariance with substitution — that permuting the blocks of a composite by $\sigma \in S_k$ matches permuting inputs by the block permutation $\sigma\langle n_\bullet\rangle$ — is precisely the naturality of $\beta$ and the hexagon axiom applied to $g_1 \otimes \dots \otimes g_k$. Hence $\mathcal{V}^{\otimes}$ is a symmetric multicategory.

**Step 4: Backward direction — a tensor from representing objects.**

> [!note]- Derivation
> Suppose $\mathcal{M}$ is a representable multicategory. For each pair $(a,b)$ choose a representing object $a \otimes b$ with universal multimap $u_{a,b} \in \mathcal{M}(a, b; a \otimes b)$; for the empty tuple choose a representing object $I$ with universal $u_\varnothing \in \mathcal{M}(\,; I)$. Functoriality of $\otimes$ on morphisms: given $f \in \mathcal{M}(a; a')$ and $g \in \mathcal{M}(b; b')$, the multimap $u_{a',b'} \circ (f, g) \in \mathcal{M}(a, b; a' \otimes b')$ factors uniquely through $u_{a,b}$ as a unary $f \otimes g : a \otimes b \to a' \otimes b'$. This makes $\otimes$ a [[Def - Functor|functor]] on the underlying category $\mathcal{M}_1$.

**Step 5: Coherence isomorphisms from uniqueness.**

> [!note]- Derivation
> Both $(a \otimes b) \otimes c$ and $a \otimes (b \otimes c)$ are representing objects for the triple $(a, b, c)$: composing the universal multimaps exhibits each as universal among multimaps $a, b, c \to (-)$. By uniqueness of representing objects up to unique isomorphism, there is a canonical iso $\alpha_{a,b,c} : (a \otimes b) \otimes c \xrightarrow{\cong} a \otimes (b \otimes c)$, natural in all three. Similarly $I \otimes a$ and $a \otimes I$ both represent $(a)$, giving unitors $\lambda, \rho$. The pentagon and triangle follow because all the maps in question are the unique isomorphisms between representing objects of the same (regrouped) tuple, and uniqueness forces every coherence diagram to commute. The braiding comes from the symmetric action: $a \otimes b$ and $b \otimes a$ both represent $(a,b)$ up to the swap, giving $\beta_{a,b}$.

**Step 6: The equivalence.**

> [!note]- Derivation
> Therefore $(\mathcal{M}_1, \otimes, I, \alpha, \lambda, \rho, \beta)$ is a symmetric monoidal category, and unwinding shows $\mathcal{M} \cong (\mathcal{M}_1)^{\otimes}$: an $n$-input multimap of $\mathcal{M}$ corresponds, via the iterated universal multimaps, to a morphism out of $a_1 \otimes \dots \otimes a_n$. Conversely $\mathcal{V}^{\otimes}$ is representable with representing objects the tensors. So symmetric monoidal categories and representable symmetric multicategories are the same notion, mutually inverse up to equivalence.

> [!note]- Complete formal solution
> *Forward.* Strictify $\mathcal{V}$ by [[Thm - Mac Lane Coherence Theorem|coherence]]. Define $\mathcal{V}^{\otimes}(a_1, \dots, a_n; b) = \mathcal{V}(a_1 \otimes \dots \otimes a_n, b)$, identities $= \mathrm{id}$, substitution $f \circ (g_\bullet) = f \circ (g_1 \otimes \dots \otimes g_k)$, and $S_n$-action $f \cdot \sigma = f \circ \beta_\sigma$. Associativity and unit follow from associativity/unit of $\circ$ and $\otimes$ in $\mathcal{V}$; equivariance from naturality of $\beta$ and the hexagon. Hence $\mathcal{V}^{\otimes}$ is a symmetric multicategory, and it is representable with representing objects the tensors.
>
> *Backward.* If $\mathcal{M}$ is representable, choose representing objects $a \otimes b$ (and $I$ for the empty tuple) with universal multimaps; make $\otimes$ functorial via the universal property; obtain associator/unitors/braiding as the unique isomorphisms between representing objects of regrouped tuples; pentagon, triangle, and hexagon hold by uniqueness. This makes $\mathcal{M}_1$ symmetric monoidal with $\mathcal{M} \cong (\mathcal{M}_1)^{\otimes}$.
>
> Hence symmetric monoidal categories $\simeq$ representable symmetric multicategories. $\blacksquare$

---

# Key Takeaways

**A monoidal category is a multicategory whose multimaps are all represented.** This is the structural punchline of the whole §1, and it reframes the tensor product as a *representability* phenomenon rather than a primitive operation. The operational consequence is a recognition heuristic: whenever you have a notion of multi-input morphism and you want to know whether it comes from a monoidal structure, the question is exactly "is each tuple's multimap functor representable?". If yes, you have $\otimes$; if no, the multicategory is the honest home of the multi-input maps and there is no tensor to be had. This dichotomy — representable versus not — is the single most useful lens for deciding whether a multilinear-type situation can be linearised.

**Coherence is what lets you suppress associators and actually compute.** The verification would be a nightmare of associator-chasing without Mac Lane's coherence theorem; invoking it to strictify is not a shortcut but the standard and rigorous move. The transferable lesson is that whenever a proof in a (braided/symmetric) monoidal setting threatens to drown in coherence isomorphisms, the first step is to cite coherence and work strictly, *then* check at the end that the construction was coherence-natural so the strictification was legitimate. This pattern recurs constantly in the operad chapter, where the composition product and the bar construction are defined "as if strict".

**Uniqueness of representing objects manufactures all the coherence for free.** In the backward direction, the associator, unitors, braiding, and *all* their coherence axioms (pentagon, triangle, hexagon) drop out of a single fact: representing objects are unique up to unique isomorphism. This is a profound economy — you do not verify the pentagon by hand; it holds because every map in it is the unique iso between two representing objects of the same tuple, and two such maps must coincide. The general principle, worth internalising for any universal-property argument, is that *coherence is automatic whenever your structure is assembled from universal objects*, because uniqueness collapses any diagram of canonical maps. This is why universal-property definitions are so much cleaner than equational ones, and it is the reason the [[Def - Operad|operad]]-as-monoid and free-operad constructions in this chapter are stated via universal properties rather than explicit coherence data.
