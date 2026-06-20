---
type: exercise
subject: model-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Stable Model Category"
  - "Def - Adjunction"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $\mathcal{M}$ be a pointed model category with suspension–loop adjunction $\Sigma \dashv \Omega$ on $\mathrm{Ho}(\mathcal{M})$, unit $\eta \colon \mathrm{id} \to \Omega\Sigma$ and counit $\varepsilon \colon \Sigma\Omega \to \mathrm{id}$. Prove the equivalence of the following, thereby justifying the multiple formulations of stability:

(a) $\Sigma$ is an equivalence of categories ($\mathcal{M}$ is [[Def - Stable Model Category|stable]]).

(b) $\eta$ and $\varepsilon$ are both natural isomorphisms (the adjunction is an **adjoint equivalence**).

(c) $\Omega$ is an equivalence of categories.

Show in particular that if $\Sigma$ is an equivalence then its quasi-inverse is *necessarily* $\Omega$ (you do not get to choose a different inverse), so "$\Sigma$ invertible" and "$\Sigma \dashv \Omega$ an adjoint equivalence" are the same statement.

**Recall:**

![[Def - Stable Model Category#The Definition]]

An [[Def - Adjunction|adjunction]] $F \dashv G$ has unit $\eta \colon \mathrm{id} \to GF$ and counit $\varepsilon \colon FG \to \mathrm{id}$ satisfying the triangle identities $\varepsilon F \circ F\eta = \mathrm{id}_F$ and $G\varepsilon \circ \eta G = \mathrm{id}_G$. A functor is an **equivalence** iff it is fully faithful and essentially surjective, iff it has a quasi-inverse.

---

# Convergent Strategy

**Problem class:** This is a pure "adjoint-equivalence formalism" problem — the topic page notes that the multiple formulations of stability are equivalent by abstract nonsense, and this exercise carries out that nonsense. No homotopy theory is needed beyond the existence of the adjunction.

**Assumption pattern:** The only resource is the adjunction $\Sigma \dashv \Omega$ with its triangle identities. The key leverage is that a *right adjoint is unique up to natural isomorphism* — this is what forces the quasi-inverse of $\Sigma$ to be $\Omega$ rather than some unrelated functor.

**Theorem routing:** Prove (b) $\Rightarrow$ (a) (iso unit/counit make $\Omega$ a two-sided inverse via the triangle identities); (a) $\Rightarrow$ (b) (an equivalence's quasi-inverse is its adjoint by uniqueness of adjoints, forcing $\eta, \varepsilon$ to be isos); (a) $\Leftrightarrow$ (c) (a right adjoint of an equivalence is an equivalence). This is exactly Lemma 1 of [[Thm - Characterization of Stable Model Categories]], here proved in full.

**Key decision point:** The crux is the direction (a) $\Rightarrow$ (b): one must argue that the quasi-inverse of $\Sigma$ *is* $\Omega$. The natural alternative — "$\Sigma$ has some quasi-inverse $\Sigma'$, and separately $\Omega$ is the right adjoint" — fails to connect the two unless you invoke uniqueness of adjoints, which is the non-obvious lever.

---

# Legal Operations Used

1. **Operation 4 from the topic page (suspend or desuspend).** This exercise establishes the precise sense in which desuspension ($\Omega = \Sigma^{-1}$) becomes available exactly in the stable case.

2. **Operation 9 from the topic page (identify cofiber and fiber).** The conclusion $\Omega = \Sigma^{-1}$ is what makes fiber and cofiber sequences agree, which is operation 9.

---

# Hints

> [!note]- Hint 1
> Start with (b) $\Rightarrow$ (a). The triangle identities say $\varepsilon\Sigma \circ \Sigma\eta = \mathrm{id}_\Sigma$ and $\Omega\varepsilon \circ \eta\Omega = \mathrm{id}_\Omega$. If $\eta$ and $\varepsilon$ are isomorphisms, these exhibit $\Omega\Sigma \cong \mathrm{id}$ (via $\eta^{-1}$) and $\Sigma\Omega \cong \mathrm{id}$ (via $\varepsilon$), so $\Omega$ is a two-sided inverse of $\Sigma$.

> [!note]- Hint 2
> For (a) $\Rightarrow$ (b): an equivalence $\Sigma$ has *some* quasi-inverse $\Sigma'$ with $\Sigma'\Sigma \cong \mathrm{id} \cong \Sigma\Sigma'$. A quasi-inverse of an equivalence is automatically both a left and a right adjoint to it. But right adjoints are unique up to natural isomorphism, and $\Omega$ is a right adjoint to $\Sigma$; hence $\Sigma' \cong \Omega$.

> [!note]- Hint 3
> Once $\Sigma' \cong \Omega$, transport the natural isomorphisms $\Sigma'\Sigma \cong \mathrm{id}$ and $\Sigma\Sigma' \cong \mathrm{id}$ through this identification. The triangle identities then force the unit $\eta$ and counit $\varepsilon$ of the *original* adjunction to be those isomorphisms, hence isomorphisms.

---

# Solution

The plan: prove the cycle (b) $\Rightarrow$ (a) $\Rightarrow$ (b) and the side equivalence (a) $\Leftrightarrow$ (c), the engine throughout being the triangle identities and the uniqueness of adjoints.

**Step 1: (b) $\Rightarrow$ (a).**

> [!note]- Derivation
> Assume $\eta \colon \mathrm{id} \to \Omega\Sigma$ and $\varepsilon \colon \Sigma\Omega \to \mathrm{id}$ are natural isomorphisms. Then $\eta$ exhibits $\Omega\Sigma \cong \mathrm{id}$ and $\varepsilon$ exhibits $\Sigma\Omega \cong \mathrm{id}$. So $\Omega$ is a two-sided inverse of $\Sigma$ up to natural isomorphism, i.e. $\Sigma$ is an equivalence with quasi-inverse $\Omega$. Hence $\mathcal{M}$ is stable.

**Step 2: (a) $\Rightarrow$ (b).**

> [!note]- Derivation
> Assume $\Sigma$ is an equivalence, so it has a quasi-inverse $\Sigma'$ with natural isomorphisms $\Sigma'\Sigma \cong \mathrm{id}$ and $\Sigma\Sigma' \cong \mathrm{id}$. A quasi-inverse of an equivalence is both left and right adjoint to it (an equivalence and its quasi-inverse form an adjoint equivalence on each side). In particular $\Sigma'$ is a *right* adjoint of $\Sigma$. But $\Omega$ is also a right adjoint of $\Sigma$ (given). Since right adjoints are unique up to natural isomorphism, $\Sigma' \cong \Omega$. Transporting the natural isomorphisms through this identification gives $\Omega\Sigma \cong \mathrm{id}$ and $\Sigma\Omega \cong \mathrm{id}$, and the comparison isomorphisms are, by the triangle identities, exactly the unit $\eta$ and counit $\varepsilon$ of the original adjunction. Therefore $\eta$ and $\varepsilon$ are isomorphisms. In particular the quasi-inverse of $\Sigma$ is *forced* to be $\Omega$ — you cannot choose a different inverse.

**Step 3: (a) $\Leftrightarrow$ (c).**

> [!note]- Derivation
> If $\Sigma$ is an equivalence then by Step 2 its quasi-inverse is $\Omega$, and a quasi-inverse of an equivalence is itself an equivalence, so $\Omega$ is an equivalence — (a) $\Rightarrow$ (c). Conversely, if $\Omega$ is an equivalence, its quasi-inverse is its left adjoint $\Sigma$ (same uniqueness-of-adjoints argument, applied to left adjoints), so $\Sigma$ is an equivalence — (c) $\Rightarrow$ (a). Hence (a) $\Leftrightarrow$ (c).

> [!note]- Complete formal solution
> *(b) $\Rightarrow$ (a).* If $\eta, \varepsilon$ are isomorphisms, then $\Omega\Sigma \cong \mathrm{id}$ (via $\eta$) and $\Sigma\Omega \cong \mathrm{id}$ (via $\varepsilon$), so $\Omega$ is a two-sided inverse of $\Sigma$ and $\Sigma$ is an equivalence.
>
> *(a) $\Rightarrow$ (b).* If $\Sigma$ is an equivalence with quasi-inverse $\Sigma'$, then $\Sigma'$ is in particular a right adjoint of $\Sigma$. Right adjoints are unique up to isomorphism and $\Omega$ is a right adjoint of $\Sigma$, so $\Sigma' \cong \Omega$. Transporting $\Sigma'\Sigma \cong \mathrm{id} \cong \Sigma\Sigma'$ along this isomorphism and matching against the triangle identities shows $\eta, \varepsilon$ are isomorphisms; in particular $\Sigma^{-1} \cong \Omega$ necessarily.
>
> *(a) $\Leftrightarrow$ (c).* An equivalence's quasi-inverse is an equivalence; by Step 2 the quasi-inverse of $\Sigma$ is $\Omega$, so $\Sigma$ equivalence $\Leftrightarrow$ $\Omega$ equivalence.
>
> Thus (a), (b), (c) are equivalent. $\blacksquare$

---

# Key Takeaways

**Uniqueness of adjoints is the lever that turns "$\Sigma$ invertible" into "$\Omega = \Sigma^{-1}$."** The subtle and reusable point is that one cannot separately have "$\Sigma$ has some inverse" and "$\Omega$ is the right adjoint" — uniqueness of adjoints *welds* them together, forcing the inverse to be $\Omega$. The trigger to remember: whenever a functor is both an equivalence and part of an adjunction, its quasi-inverse must be the adjoint, by uniqueness. This is why stability has a *canonical* desuspension ($\Omega$), not just some abstract inverse, and it is what makes the formula "$\Sigma^{-1} = \Omega$" legitimate.

**The multiple formulations of stability are connected by formalism, not homotopy theory, which is why they are all genuinely equivalent.** This exercise shows that "definition page lists four equivalent conditions" is not loose talk — the equivalence is a theorem of pure category theory (adjoint-equivalence yoga). The transferable diagnostic: when a definition offers several characterizations of the same property, check whether they are linked by adjunction formalism (cheap, always valid) or by substantive content (needs proof in each case); stability is the former, which is why one is free to use whichever formulation is most convenient in a given problem.

**Adjoint equivalences are the right notion of "inverse" in category theory, and they package invertibility with its compatibility data.** A bare equivalence remembers only that an inverse exists; an adjoint equivalence remembers the inverse *together with the coherent unit and counit*, which is what downstream constructions actually need. The conceptual upgrade to carry forward: whenever you invert a functor, upgrade to an adjoint equivalence so the unit and counit are available — this is the same reason one prefers an adjoint equivalence of model categories (a Quillen equivalence with controlled unit/counit) over a bare equivalence of homotopy categories, and it is the form in which stability feeds the rest of the chapter.
