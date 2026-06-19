---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Unit and Counit of an Adjunction"
  - "Thm - Equivalence of the Definitions of Adjunction"
  - "Def - Free-Forgetful Adjunction"
tags: [category-theory, foundations]
---

# Problem Statement

Let $F\dashv G$ be an adjunction with hom-set bijection $\Phi_{A,B} : \mathcal{D}(FA, B)\cong\mathcal{C}(A, GB)$, unit $\eta_A = \Phi(1_{FA})$, and counit $\varepsilon_B = \Phi^{-1}(1_{GB})$.

**(a)** Prove the two **triangle identities** directly from the hom-set definition:
$$\varepsilon_{FA}\circ F(\eta_A) = 1_{FA} \quad\text{and}\quad G(\varepsilon_B)\circ\eta_{GB} = 1_{GB}.$$

**(b)** Verify both identities concretely on the [[Def - Free-Forgetful Adjunction|free-forgetful adjunction]] for groups, where $\eta_S$ is insertion of generators and $\varepsilon_H$ multiplies a word out.

**Recall:**

![[Def - Unit and Counit of an Adjunction#The Definition]]

The [[Thm - Equivalence of the Definitions of Adjunction|equivalence-of-definitions theorem]] gives the transpose formulas $\Phi(f) = Gf\circ\eta_A$ and $\Phi^{-1}(g) = \varepsilon_B\circ Fg$, which we use to translate the identities into computations with $\Phi$.

---

# Convergent Strategy

**Problem class:** This is a "verify the defining axioms" problem — establishing that the unit and counit (transposes of identities) satisfy the triangle identities, both abstractly (a) and on a concrete model (b). It is the computation underlying [[Thm - Equivalence of the Definitions of Adjunction|the equivalence of the three definitions]].

**Assumption pattern:** The decisive assumptions are the transpose formulas $\Phi(f) = Gf\circ\eta_A$ and $\Phi^{-1}(g) = \varepsilon_B\circ Fg$, together with $\Phi$ being a bijection. The triangle identities are exactly "$\Phi^{-1}\Phi = \mathrm{id}$ and $\Phi\Phi^{-1} = \mathrm{id}$ evaluated at the identity".

**Theorem routing:** Apply the transpose formula to a cleverly chosen morphism (the unit or counit itself), then use bijectivity of $\Phi$ to collapse to the identity. For (b), substitute the explicit insertion/evaluation maps and chase a generator.

**Key decision point:** The non-obvious move in (a) is to compute $\Phi^{-1}(\eta_A)$ or $\Phi(\varepsilon_B)$ — feeding a unit/counit *back into the transpose machinery* — and recognise the result is an identity by bijectivity. The natural but wrong instinct is to try to manipulate $\varepsilon_{FA}\circ F\eta_A$ directly without re-expressing it through $\Phi$.

---

# Legal Operations Used

1. **Operation 1 from the topic page (transpose a morphism across the adjunction).** The proof of (a) repeatedly transposes morphisms and uses that transposition is a bijection.

2. **Operation 3 from the topic page (build the unit and counit).** We use $\eta_A = \Phi(1_{FA})$ and $\varepsilon_B = \Phi^{-1}(1_{GB})$ as the definitions to be fed into the transpose formulas.

---

# Hints

> [!note]- Hint 1
> Both triangle identities are bijectivity of $\Phi$ in disguise. The first identity is "$\Phi^{-1}(\Phi(1_{FA})) = 1_{FA}$" once you express things correctly.

> [!note]- Hint 2
> Use $\Phi^{-1}(g) = \varepsilon_B\circ Fg$ with $g = \eta_A : A\to GFA$ (so $B = FA$): $\Phi^{-1}(\eta_A) = \varepsilon_{FA}\circ F\eta_A$. But $\eta_A = \Phi(1_{FA})$, so $\Phi^{-1}(\eta_A) = \Phi^{-1}(\Phi(1_{FA})) = 1_{FA}$. That *is* the first triangle identity.

> [!note]- Hint 3
> For (b): the first identity at a generator $s\in S$ reads — insert $s$ as a generator ($\eta_S$), apply $F$ to get the one-letter word $s$ in $FUFS$ ... then multiply it out ($\varepsilon_{FS}$) to recover $s\in FS$. Track a single generator through $\varepsilon_{FS}\circ F\eta_S$ and check it returns.

---

# Solution

Each triangle identity is a single application of the transpose formula followed by bijectivity. Part (b) checks the abstract identities survive on the concrete model by chasing a generator.

**Step 1: First triangle identity (part a).**

$\varepsilon_{FA}\circ F\eta_A = 1_{FA}$.

> [!note]- Derivation
> By the transpose formula $\Phi^{-1}(g) = \varepsilon_B\circ Fg$, apply it with $g = \eta_A : A\to GFA$ and target object $B = FA$:
> $$\Phi^{-1}_{A, FA}(\eta_A) = \varepsilon_{FA}\circ F(\eta_A).$$
> But $\eta_A = \Phi_{A, FA}(1_{FA})$ by definition of the unit. Substituting,
> $$\varepsilon_{FA}\circ F\eta_A = \Phi^{-1}(\eta_A) = \Phi^{-1}(\Phi(1_{FA})) = 1_{FA},$$
> using that $\Phi^{-1}$ and $\Phi$ are mutually inverse. This is the first triangle identity.

**Step 2: Second triangle identity (part a).**

$G\varepsilon_B\circ\eta_{GB} = 1_{GB}$.

> [!note]- Derivation
> By the transpose formula $\Phi(f) = Gf\circ\eta_A$, apply it with $f = \varepsilon_B : FGB\to B$ and source object $A = GB$:
> $$\Phi_{GB, B}(\varepsilon_B) = G(\varepsilon_B)\circ\eta_{GB}.$$
> But $\varepsilon_B = \Phi^{-1}_{GB, B}(1_{GB})$ by definition of the counit. Substituting,
> $$G\varepsilon_B\circ\eta_{GB} = \Phi(\varepsilon_B) = \Phi(\Phi^{-1}(1_{GB})) = 1_{GB}.$$
> This is the second triangle identity.

**Step 3: Concrete verification on the free group (part b).**

Both identities hold for $F\dashv U$ on groups: insertion-then-evaluation recovers the identity.

> [!note]- Derivation
> Here $\eta_S(s) = s$ (one-letter word) and $\varepsilon_H$ multiplies a word out.
>
> **First identity** $\varepsilon_{FS}\circ F\eta_S = 1_{FS}$, evaluated on a generator $s\in S\subseteq UFS$. Apply $F\eta_S : F S \to FUFS$: since $F\eta_S$ is the homomorphism induced by the function $\eta_S$, it sends the generator $s\in FS$ to the generator $\eta_S(s) = s$ of $FUFS$ (the one-letter word whose single letter is the element $s\in UFS$). Then $\varepsilon_{FS} : FUFS\to FS$ multiplies that one-letter word out, returning the element $s\in FS$. So $\varepsilon_{FS}\circ F\eta_S$ fixes every generator $s$, and since homomorphisms agreeing on generators are equal, $\varepsilon_{FS}\circ F\eta_S = 1_{FS}$.
>
> **Second identity** $U\varepsilon_H\circ\eta_{UH} = 1_{UH}$, evaluated on an element $h\in UH$. $\eta_{UH}(h) = h$ is the one-letter word $h\in UFUH$. Then $U\varepsilon_H$ multiplies it out, giving $h\in UH$. So the composite is the identity function on $UH$.
>
> Both identities reduce to: *insert as a one-letter word, then multiply that single letter out, and you get back what you started with.* This is the concrete shadow of the abstract bijectivity argument.

> [!note]- Complete formal solution
> **(a)** Using $\Phi^{-1}(g) = \varepsilon\circ Fg$ at $g = \eta_A$: $\varepsilon_{FA}\circ F\eta_A = \Phi^{-1}(\eta_A) = \Phi^{-1}\Phi(1_{FA}) = 1_{FA}$. Using $\Phi(f) = Gf\circ\eta$ at $f = \varepsilon_B$: $G\varepsilon_B\circ\eta_{GB} = \Phi(\varepsilon_B) = \Phi\Phi^{-1}(1_{GB}) = 1_{GB}$. Both triangle identities hold.
>
> **(b)** With $\eta_S(s)=s$ and $\varepsilon_H$ = "multiply out": $\varepsilon_{FS}(F\eta_S(s)) = \varepsilon_{FS}(\text{one-letter word } s) = s$, so the first identity holds on generators, hence as homomorphisms. $U\varepsilon_H(\eta_{UH}(h)) = U\varepsilon_H(\text{one-letter word } h) = h$, so the second holds on elements. $\blacksquare$

---

# Key Takeaways

**The triangle identities ARE the bijectivity of the transpose, evaluated at identities.** The cleanest way to see why the triangle identities hold — and why there are exactly two of them — is that $\Phi^{-1}\Phi = \mathrm{id}$ and $\Phi\Phi^{-1} = \mathrm{id}$, evaluated at the identity morphisms, *are* the two triangle identities once the transpose formulas $\Phi(f) = Gf\circ\eta$ and $\Phi^{-1}(g) = \varepsilon\circ Fg$ are substituted. This is the content of [[Thm - Equivalence of the Definitions of Adjunction|the equivalence-of-definitions theorem]] made computational: naturality of the bijection, which looks like infinitely many squares, is repackaged as two equations. The two identities are not interchangeable — one guards $\Phi^{-1}\Phi$, the other $\Phi\Phi^{-1}$ — so verifying only one and citing "symmetry" is a real gap.

**Feed the unit/counit back into the transpose to collapse a triangle.** The proof technique worth keeping is: to verify $\varepsilon_{FA}\circ F\eta_A = 1$, recognise the left side as $\Phi^{-1}(\eta_A)$ and then use $\eta_A = \Phi(1)$ to get $\Phi^{-1}\Phi(1) = 1$. The trick is to *re-express a composite of whiskered unit/counit maps as a single transpose*, after which bijectivity finishes immediately. This pattern recurs throughout the "calculus of adjunctions" — mate calculations, composition of adjunctions, and uniqueness proofs all reduce composites to single transposes and exploit bijectivity. Direct manipulation of $\varepsilon_{FA}\circ F\eta_A$ without this re-expression is the hard way and usually stalls.

**On any concrete adjunction, the triangle identities say "insert then evaluate is the identity".** For free-forgetful adjunctions both identities reduce to chasing a single generator/element: insert it as a one-letter word, multiply it out, recover it. This concrete reading is a fast sanity check whenever you meet a new adjunction — verify that "insertion followed by evaluation" (suitably whiskered) returns the original on generators, and you have checked the triangle identity on the part of the object where homomorphisms are determined. It also makes vivid *why* the whiskerings are present: $F\eta_S$ builds the free group on the inserted generators before $\varepsilon_{FS}$ evaluates, so the two maps live in compatible categories only after the $F$ is applied. The companion exercise [[Ex - Unit and counit of the free-forgetful adjunction|Unit and counit of the free-forgetful adjunction]] computes the very $\eta, \varepsilon$ that this exercise verifies, and [[Ex - An adjunction from a Galois connection|An adjunction from a Galois connection]] shows the triangle identities become automatic in the poset case.
