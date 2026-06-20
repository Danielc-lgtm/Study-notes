---
type: exercise
subject: model-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Pre-Triangulated Category"
  - "Def - Cofiber and Fiber Sequence"
  - "Def - Pointed Model Category Suspension and Loop"
  - "Def - Opposite Category and Duality"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $\mathcal{T}$ be a [[Def - Pre-Triangulated Category|pre-triangulated category]].

1. Show that the [[Def - Opposite Category and Duality|opposite category]] $\mathcal{T}^{\mathrm{op}}$ is again pre-triangulated, with suspension and loop **swapped**: $\Sigma_{\mathcal{T}^{\mathrm{op}}} = \Omega_{\mathcal{T}}$ and $\Omega_{\mathcal{T}^{\mathrm{op}}} = \Sigma_{\mathcal{T}}$.
2. Show that the cofiber sequences of $\mathcal{T}^{\mathrm{op}}$ are exactly the fiber sequences of $\mathcal{T}$ (read backwards), and vice versa.
3. Explain how this single observation *is* the source of the cofiber/fiber duality used throughout the chapter, and why a pointed model category $\mathcal{C}$ has $\mathrm{Ho}(\mathcal{C}^{\mathrm{op}}) = \mathrm{Ho}(\mathcal{C})^{\mathrm{op}}$ with this swap.

**Recall:**

![[Def - Pre-Triangulated Category#The Definition]]

The [[Def - Opposite Category and Duality|opposite category]] $\mathcal{T}^{\mathrm{op}}$ has the same objects and reversed morphisms: $\mathcal{T}^{\mathrm{op}}(X, Y) = \mathcal{T}(Y, X)$. A [[Def - Pointed Model Category Suspension and Loop|pointed]] structure dualizes (the zero object is self-dual). An [[Def - Adjunction|adjunction]] $F \dashv G$ in $\mathcal{T}$ becomes $G^{\mathrm{op}} \dashv F^{\mathrm{op}}$ in $\mathcal{T}^{\mathrm{op}}$ (the opposite reverses the direction of adjunction). [[Def - Cofiber and Fiber Sequence|Cofiber sequences]] are built from homotopy pushouts, fiber sequences from homotopy pullbacks; pushouts and pullbacks are interchanged by passing to the opposite.

---

# Convergent Strategy

**Problem class:** This is a "duality / opposite-category" exercise, the most structural kind in the chapter. The route is to track how each ingredient of the pre-triangulated definition transforms under $(-)^{\mathrm{op}}$ and observe that the cofiber and fiber data swap.

**Assumption pattern:** The load-bearing facts are that the opposite reverses the direction of every adjunction (so $\Sigma \dashv \Omega$ becomes $\Omega^{\mathrm{op}} \dashv \Sigma^{\mathrm{op}}$, i.e. $\Sigma_{\mathcal{T}^{\mathrm{op}}} = \Omega_{\mathcal{T}}$) and that the opposite interchanges pushouts with pullbacks (so cofiber squares become fiber squares). Once these two dualizations are in hand, the result is forced.

**Theorem routing:** Part (1) routes through the opposite of an [[Def - Adjunction|adjunction]] and the self-duality of the zero object. Part (2) routes through the interchange of homotopy [[Def - Pullback and Pushout|pushouts and pullbacks]] under $(-)^{\mathrm{op}}$. Part (3) routes through the principle of [[Def - Opposite Category and Duality|duality]]: a theorem about cofiber sequences becomes a theorem about fiber sequences in the opposite.

**Key decision point:** The crucial — and easy to mishandle — step is the direction of the adjunction under the opposite. A left adjoint becomes a right adjoint in $\mathcal{T}^{\mathrm{op}}$, so the *left* adjoint $\Sigma$ of $\mathcal{T}$ becomes the *right* adjoint of $\mathcal{T}^{\mathrm{op}}$, which means the *suspension of the opposite* (the left adjoint there) is $\Omega$. Getting this swap right is the whole exercise; reversing it gives the wrong (non-adjoint) pairing.

---

# Legal Operations Used

1. **Operation 3 from the topic page (recognize a homotopy pushout/pullback square with a corner at $*$).** The swap of cofiber and fiber sequences is the swap of pushout and pullback squares under the opposite.

2. **Operation 6 from the topic page (use the suspension–loop adjunction).** Part (1) dualizes the adjunction $\Sigma \dashv \Omega$.

3. **Operation 4 from the topic page (paste (co)cartesian squares).** The Puppe sequences dualize because pasting pushout squares becomes pasting pullback squares in the opposite.

---

# Hints

> [!note]- Hint 1
> A pushout in $\mathcal{T}$ is a pullback in $\mathcal{T}^{\mathrm{op}}$, because reversing all arrows turns a colimit into the corresponding limit. So the cofiber square of $f$ (a pushout with a corner at $*$) becomes a pullback square with a corner at $*$ — a fiber square — in the opposite.

> [!note]- Hint 2
> An adjunction $\Sigma \dashv \Omega$ in $\mathcal{T}$ means $\mathcal{T}(\Sigma X, Y) \cong \mathcal{T}(X, \Omega Y)$. In $\mathcal{T}^{\mathrm{op}}$ hom-sets reverse: $\mathcal{T}^{\mathrm{op}}(A, B) = \mathcal{T}(B, A)$. Rewrite the adjunction with reversed homs and read off which functor is the left adjoint in $\mathcal{T}^{\mathrm{op}}$.

> [!note]- Hint 3
> The reversal gives $\mathcal{T}^{\mathrm{op}}(\Omega Y, X) \cong \mathcal{T}^{\mathrm{op}}(Y, \Sigma X)$, i.e. $\Omega \dashv \Sigma$ in $\mathcal{T}^{\mathrm{op}}$. So the left adjoint (= "suspension") of $\mathcal{T}^{\mathrm{op}}$ is $\Omega$, and its right adjoint (= "loop") is $\Sigma$.

---

# Solution

The solution dualizes each pre-triangulated ingredient: the adjunction reverses (swapping $\Sigma$ and $\Omega$), pushouts become pullbacks (swapping cofiber and fiber sequences), and the long-exact-sequence axioms dualize. This swap is the source of the chapter's cofiber/fiber duality.

**Step 1: $\Sigma$ and $\Omega$ swap under the opposite.**

> [!note]- Derivation
> The [[Def - Opposite Category and Duality|opposite]] $\mathcal{T}^{\mathrm{op}}$ is pointed: the zero object $*$ is both initial and terminal, and reversing arrows swaps "initial" with "terminal," so $*$ remains a zero object (self-dual). The zero maps are preserved.
>
> Dualize the [[Def - Pointed Model Category Suspension and Loop|adjunction]] $\Sigma \dashv \Omega$, which is the natural isomorphism $\mathcal{T}(\Sigma X, Y) \cong \mathcal{T}(X, \Omega Y)$. In the opposite, $\mathcal{T}^{\mathrm{op}}(A, B) = \mathcal{T}(B, A)$, so reversing both sides:
> $$\mathcal{T}^{\mathrm{op}}(Y, \Sigma X) = \mathcal{T}(\Sigma X, Y) \cong \mathcal{T}(X, \Omega Y) = \mathcal{T}^{\mathrm{op}}(\Omega Y, X).$$
> Reading this as an adjunction in $\mathcal{T}^{\mathrm{op}}$: it says $\mathcal{T}^{\mathrm{op}}(\Omega Y, X) \cong \mathcal{T}^{\mathrm{op}}(Y, \Sigma X)$, i.e. $\Omega \dashv \Sigma$ **in $\mathcal{T}^{\mathrm{op}}$**. Therefore the left adjoint in $\mathcal{T}^{\mathrm{op}}$ — which plays the role of *suspension* — is $\Omega$, and the right adjoint — the *loop* — is $\Sigma$:
> $$\Sigma_{\mathcal{T}^{\mathrm{op}}} = \Omega_{\mathcal{T}}, \qquad \Omega_{\mathcal{T}^{\mathrm{op}}} = \Sigma_{\mathcal{T}}.$$
> The opposite of an adjunction reverses the direction of adjunction, so the left/right roles — and hence the names suspension/loop — swap.

**Step 2: Cofiber and fiber sequences swap.**

> [!note]- Derivation
> A [[Def - Cofiber and Fiber Sequence|cofiber sequence]] in $\mathcal{T}$ is built from a homotopy [[Def - Pullback and Pushout|pushout]] square with a corner at $*$. Passing to $\mathcal{T}^{\mathrm{op}}$ reverses every arrow, turning a colimit (pushout) into the corresponding limit (pullback): the cofiber square of $f : X \to Y$ in $\mathcal{T}$ becomes, in $\mathcal{T}^{\mathrm{op}}$, a pullback square with a corner at $*$ — a **fiber square** — for the reversed map $f^{\mathrm{op}} : Y \to X$. Concretely, the cofiber sequence $X \to Y \to C_f \to \Sigma X$ in $\mathcal{T}$, read in $\mathcal{T}^{\mathrm{op}}$ with arrows reversed, is
> $$\Omega_{\mathcal{T}}\, X \to C_f \to Y \to X,$$
> which (using $\Sigma_{\mathcal{T}^{\mathrm{op}}} = \Omega_{\mathcal{T}}$, so the leading term is $\Sigma_{\mathcal{T}^{\mathrm{op}}} X$... read in the fiber-sequence template) is a **fiber sequence** of $\mathcal{T}^{\mathrm{op}}$. Symmetrically, the fiber sequences of $\mathcal{T}$ become the cofiber sequences of $\mathcal{T}^{\mathrm{op}}$. So:
> $$\{\text{cofiber sequences of } \mathcal{T}^{\mathrm{op}}\} = \{\text{fiber sequences of } \mathcal{T} \text{, reversed}\}, \quad \{\text{fiber sequences of } \mathcal{T}^{\mathrm{op}}\} = \{\text{cofiber sequences of } \mathcal{T}\text{, reversed}\}.$$
> The existence, rotation, and long-exact-sequence axioms transfer because each is self-dual: the long exact sequence of $\mathcal{T}(-, W)$ on a cofiber sequence becomes the long exact sequence of $\mathcal{T}^{\mathrm{op}}(W, -)$ on the corresponding fiber sequence (the contravariant $\mathcal{T}(-, W)$ becomes the covariant $\mathcal{T}^{\mathrm{op}}(W, -)$). Hence $\mathcal{T}^{\mathrm{op}}$ satisfies all pre-triangulated axioms.

**Step 3: This is the source of cofiber/fiber duality.**

> [!note]- Derivation
> The entire "and dually..." structure of the chapter is this opposite-category symmetry. Because $\mathcal{T}^{\mathrm{op}}$ is pre-triangulated with $\Sigma$ and $\Omega$ swapped and cofiber and fiber sequences swapped, every theorem proved about cofiber sequences in $\mathcal{T}$ becomes, applied to $\mathcal{T}^{\mathrm{op}}$, a theorem about fiber sequences in $\mathcal{T}$. This is the formal content of the [[Def - Opposite Category and Duality|principle of duality]]: one proves the cofiber statement once and obtains the fiber statement by reading it in the opposite. At the model-category level, a pointed model category $\mathcal{C}$ has an opposite model structure $\mathcal{C}^{\mathrm{op}}$ (cofibrations and fibrations swap, weak equivalences are self-dual), and $\mathrm{Ho}(\mathcal{C}^{\mathrm{op}}) = \mathrm{Ho}(\mathcal{C})^{\mathrm{op}}$. Under this identification suspension in $\mathcal{C}^{\mathrm{op}}$ (homotopy pushout of $* \leftarrow X \rightarrow *$ in $\mathcal{C}^{\mathrm{op}}$ = homotopy pullback in $\mathcal{C}$) is the loop of $\mathcal{C}$, exactly as in Step 1. So the cofiber/fiber duality is not a coincidence of parallel constructions — it is a single self-duality of the pre-triangulated structure under $(-)^{\mathrm{op}}$.

> [!note]- Complete formal solution
> **(1)** $\mathcal{T}^{\mathrm{op}}$ is pointed (zero object self-dual). The adjunction $\mathcal{T}(\Sigma X, Y) \cong \mathcal{T}(X, \Omega Y)$, reversed, reads $\mathcal{T}^{\mathrm{op}}(\Omega Y, X) \cong \mathcal{T}^{\mathrm{op}}(Y, \Sigma X)$, i.e. $\Omega \dashv \Sigma$ in $\mathcal{T}^{\mathrm{op}}$. So $\Sigma_{\mathcal{T}^{\mathrm{op}}} = \Omega_{\mathcal{T}}$, $\Omega_{\mathcal{T}^{\mathrm{op}}} = \Sigma_{\mathcal{T}}$.
>
> **(2)** Reversing arrows turns pushouts into pullbacks, so cofiber squares of $\mathcal{T}$ become fiber squares of $\mathcal{T}^{\mathrm{op}}$ and vice versa; the cofiber sequences of $\mathcal{T}^{\mathrm{op}}$ are the (reversed) fiber sequences of $\mathcal{T}$. The existence/rotation/long-exact-sequence axioms are self-dual ($\mathcal{T}(-, W) \rightsquigarrow \mathcal{T}^{\mathrm{op}}(W, -)$), so $\mathcal{T}^{\mathrm{op}}$ is pre-triangulated.
>
> **(3)** This self-duality is the principle of duality for the chapter: cofiber statements yield fiber statements in the opposite. At the model level $\mathrm{Ho}(\mathcal{C}^{\mathrm{op}}) = \mathrm{Ho}(\mathcal{C})^{\mathrm{op}}$ with $\Sigma$ and $\Omega$ swapped, so the cofiber/fiber duality is one structural symmetry. $\blacksquare$

---

# Key Takeaways

**The opposite reverses the direction of adjunction, which is why $\Sigma$ and $\Omega$ swap — and getting this swap right is the whole subtlety of dualization.** The most error-prone step in any opposite-category argument is the adjunction: a left adjoint in $\mathcal{T}$ is a *right* adjoint in $\mathcal{T}^{\mathrm{op}}$. So the suspension (left adjoint) of $\mathcal{T}$ becomes the loop (right adjoint) of $\mathcal{T}^{\mathrm{op}}$, and the suspension of the opposite is the original loop. The reusable rule is: under $(-)^{\mathrm{op}}$, left and right adjoints trade places, colimits and limits trade places, and any "left/colimit" construction becomes the corresponding "right/limit" one. Mechanically rewriting hom-sets with reversed arrows, as in the solution, is the safe way to determine the swap rather than guessing.

**Cofiber/fiber duality is a single self-duality, not two parallel theories.** The chapter is full of "and dually" remarks — cofiber and fiber sequences, suspension and loop, pushout-collapse and pullback-restriction — and this exercise reveals them all as one symmetry: $\mathcal{T}$ pre-triangulated implies $\mathcal{T}^{\mathrm{op}}$ pre-triangulated with everything swapped. The transferable payoff is enormous economy: you prove every cofiber statement once, and the fiber statement is the same statement read in the opposite category. This is the [[Def - Opposite Category and Duality|principle of duality]] in action, and recognizing it lets you halve the work in any (co)limit-based subject — derived categories, abelian categories, and topos theory all exploit the same self-duality.

**Opposite model structures are real, and they implement the duality at the source.** That a pointed model category $\mathcal{C}$ has an opposite $\mathcal{C}^{\mathrm{op}}$ (cofibrations and fibrations swapped, weak equivalences self-dual) with $\mathrm{Ho}(\mathcal{C}^{\mathrm{op}}) = \mathrm{Ho}(\mathcal{C})^{\mathrm{op}}$ is the model-category fact underwriting all the homotopy-categorical duality. The diagnostic to carry is that whenever you want the dual of a homotopy-theoretic statement, you can often realize it by passing to the opposite model category, where pushouts become pullbacks and cones become cocones. This is why suspension and loop, cofiber and fiber, are genuinely dual rather than merely analogous: they are literally the same constructions performed in $\mathcal{C}$ and in $\mathcal{C}^{\mathrm{op}}$.
