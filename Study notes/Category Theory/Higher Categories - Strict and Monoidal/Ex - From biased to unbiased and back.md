---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Unbiased Monoidal Category"
  - "Def - Monoidal Category"
  - "Thm - Biased and Unbiased Monoidal Categories Coincide"
  - "Thm - Mac Lane Coherence Theorem"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

(a) Starting from an [[Def - Unbiased Monoidal Category|unbiased monoidal category]] $(\mathcal{C},(\otimes_n),\gamma,\iota)$, construct the associator of the underlying [[Def - Monoidal Category|biased]] structure $(\mathcal{C},\otimes_2,\otimes_0())$ purely from the composition [[Def - Isomorphism|isomorphisms]] $\gamma$, and show it satisfies the **pentagon**.

(b) Starting from a biased monoidal category, define $\otimes_3(A,B,C)$ by left-bracketing and write down the composition isomorphism $\gamma_{2,1}$ comparing $\otimes_2(\otimes_2(A,B),C)$ with $\otimes_3(A,B,C)$. Show that defining $\gamma$ on a longer list requires choosing a bracketing, and that well-definedness is exactly [[Thm - Mac Lane Coherence Theorem|Mac Lane's coherence theorem]].

(c) Conclude that the pentagon is *not* an arbitrary axiom but the length-four instance of the single unbiased associativity coherence axiom.

**Recall:**

An [[Def - Unbiased Monoidal Category|unbiased monoidal category]] has $\otimes_n:\mathcal{C}^n\to\mathcal{C}$ for all $n$, with composition isomorphisms $\gamma_{k_1,\dots,k_n}:\otimes_n(\otimes_{k_1}(-),\dots,\otimes_{k_n}(-))\cong\otimes_{\sum k_i}(-)$ and unit iso $\iota:\otimes_1\cong\mathrm{id}$, subject to associativity and unit coherence:

![[Def - Unbiased Monoidal Category#The Definition]]

The [[Def - Monoidal Category|biased]] pentagon for the associator $\alpha$ is
$$\alpha_{A,B,C\otimes D}\circ\alpha_{A\otimes B,C,D} = (1_A\otimes\alpha_{B,C,D})\circ\alpha_{A,B\otimes C,D}\circ(\alpha_{A,B,C}\otimes 1_D).$$
[[Thm - Mac Lane Coherence Theorem|Mac Lane's coherence theorem]]: in the free monoidal category, any two composites of $\alpha,\lambda,\rho$ with equal source and target are equal.

---

# Convergent Strategy

**Problem class:** This is an *equivalence-of-presentations* problem — the concrete, hands-on core of [[Thm - Biased and Unbiased Monoidal Categories Coincide]]. The two directions (unbiased $\to$ biased, biased $\to$ unbiased) are asymmetric: one is free, the other needs coherence, and seeing exactly where the asymmetry bites is the goal.

**Assumption pattern:** In (a) we are handed the all-arity $\gamma$'s and want to extract the binary associator; the unlock is that $(A\otimes_2 B)\otimes_2 C$ and $A\otimes_2(B\otimes_2 C)$ are both $\gamma$-comparable to the *same* flat $\otimes_3(A,B,C)$, so the associator is the composite "down to $\otimes_3$ and back up." In (b) we go the other way and discover the cost: building $\gamma$ from $\alpha$ requires *choosing* a re-bracketing route, and the choice must not matter — which is precisely coherence.

**Theorem routing:** Part (a) routes through the unbiased associativity axiom (applied to a length-four list) to verify the pentagon. Part (b) routes through [[Thm - Mac Lane Coherence Theorem|Mac Lane's coherence theorem]], which guarantees the re-bracketing composite defining $\gamma$ is independent of the chosen route. Part (c) reads off the logical relationship: pentagon $=$ length-four associativity coherence.

**Key decision point:** The non-obvious realization is that the asymmetry is *essential*, not an artefact of the construction. Extracting the binary part from the unbiased data is free because the data is already there ($\gamma_{2,1}$, $\gamma_{1,2}$ are given); building the unbiased data from the binary part is not free because bracketing requires a *choice*, and only coherence makes the choice irrelevant. The trap is to think both directions are equally trivial; the entire weight of [[Thm - Mac Lane Coherence Theorem|Mac Lane]] sits in direction (b).

---

# Legal Operations Used

1. **Operation 4 from the topic page (pass from biased to unbiased and back).** This exercise is the explicit computation behind operation 4: assembling the associator from $\gamma$ (forward) and defining $\gamma$ from the associator (backward).

2. **Operation 5 from the topic page (cite coherence).** Part (b) invokes [[Thm - Mac Lane Coherence Theorem|coherence]] to certify that the re-bracketing definition of $\gamma$ is well-defined, the single nontrivial step.

---

# Hints

> [!note]- Hint 1
> In the unbiased structure, both $(A\otimes_2 B)\otimes_2 C = \otimes_2(\otimes_2(A,B),\otimes_1(C))$ and $A\otimes_2(B\otimes_2 C) = \otimes_2(\otimes_1(A),\otimes_2(B,C))$ are comparable by a $\gamma$ to the *flat* $\otimes_3(A,B,C)$. Compose the two comparisons to get $\alpha$.

> [!note]- Hint 2
> For the pentagon, do not compute associator strings. Instead note that both sides of the pentagon are canonical maps from $((A\otimes B)\otimes C)\otimes D$ to $A\otimes(B\otimes(C\otimes D))$, and both factor through $\otimes_4(A,B,C,D)$; the unbiased associativity axiom says the factorizations agree.

> [!note]- Hint 3
> For (b), $\otimes_3(A,B,C)$ is *defined* as $(A\otimes B)\otimes C$ (left-bracketing), so $\gamma_{2,1}$ is the identity in that convention — but to compare with the *other* bracketing $A\otimes(B\otimes C)$ you need the associator $\alpha$. For a length-four list there are five bracketings (Catalan number $C_3=5$) connected by associators.

> [!note]- Hint 4
> The map $\gamma$ for a long list is "re-bracket from the chosen normal form to the target bracketing," a composite of associators. Two such composites with the same endpoints are equal *only because* of [[Thm - Mac Lane Coherence Theorem|Mac Lane's coherence theorem]] — that is the precise content needed, and the pentagon is its first non-trivial case.

---

# Solution

The plan: (a) build $\alpha = \gamma_{1,2}\circ\gamma_{2,1}^{-1}$ and prove the pentagon by factoring through $\otimes_4$ and applying the unbiased associativity axiom; (b) write $\gamma_{2,1}$ in the left-bracketing convention, then show defining $\gamma$ on longer lists needs a bracketing choice whose irrelevance is coherence; (c) state the logical equivalence pentagon $\Leftrightarrow$ length-four associativity. The single insight is that the flat tensor $\otimes_n$ is a common refinement through which all bracketings factor.

**Step 1: The associator from $\gamma$, and the pentagon.**

Define $\alpha_{A,B,C} := \gamma_{1,2;A,B,C}\circ\gamma_{2,1;A,B,C}^{-1} : (A\otimes_2 B)\otimes_2 C\to A\otimes_2(B\otimes_2 C)$. It satisfies the pentagon.

> [!note]- Derivation
> Write $\otimes := \otimes_2$. In the unbiased structure:
> $$(A\otimes B)\otimes C = \otimes_2\big(\otimes_2(A,B),\,\otimes_1(C)\big) \xrightarrow{\ \gamma_{2,1}\ } \otimes_3(A,B,C) \xleftarrow{\ \gamma_{1,2}\ } \otimes_2\big(\otimes_1(A),\,\otimes_2(B,C)\big) = A\otimes(B\otimes C).$$
> (We suppress $\iota$ identifying $\otimes_1(X)$ with $X$.) Define $\alpha_{A,B,C} := \gamma_{1,2}\circ\gamma_{2,1}^{-1}$; it is an isomorphism since both $\gamma$'s are, and natural since $\gamma$ is.
>
> *Pentagon.* Consider a length-four list $(A,B,C,D)$. Each of the five bracketings is $\gamma$-comparable to the flat $\otimes_4(A,B,C,D)$. The two sides of the pentagon are composites of $\alpha$'s, hence of $\gamma^{\pm}$'s, from $((A\otimes B)\otimes C)\otimes D$ to $A\otimes(B\otimes(C\otimes D))$. Write each side as: (compare source bracketing with $\otimes_4$) then (compare $\otimes_4$ with target bracketing). The first leg is the same for both sides ($\gamma$ to $\otimes_4$ from the common source), the last leg is the same ($\gamma^{-1}$ from $\otimes_4$ to the common target); the *unbiased associativity coherence axiom* says that the two intermediate ways of reaching $\otimes_4$ (contracting the nested $\gamma$'s in the two pentagon orders) coincide. Hence the two pentagon composites are equal. No associator string was computed — the flat tensor $\otimes_4$ is the common refinement and the axiom does the rest.

**Step 2: Defining $\gamma$ from a biased structure needs coherence.**

> [!note]- Derivation
> Now start from a biased $(\mathcal{C},\otimes,I,\alpha,\lambda,\rho)$ and *define* $\otimes_n$ by left-bracketing: $\otimes_0()=I$, $\otimes_1(A)=A$, $\otimes_2=\otimes$, $\otimes_3(A,B,C)=(A\otimes B)\otimes C$, and in general $\otimes_n(A_1,\dots,A_n)=((\cdots(A_1\otimes A_2)\otimes\cdots)\otimes A_n)$.
>
> The composition isomorphism $\gamma_{k_1,\dots,k_n}$ must compare $\otimes_n(\otimes_{k_1}(-),\dots)$ — a nested left-bracketed expression — with the flat left-bracketing $\otimes_{\sum k_i}(-)$. For $\gamma_{2,1;A,B,C}$: the source is $\otimes_2(\otimes_2(A,B),\otimes_1(C)) = (A\otimes B)\otimes C$ and the target is $\otimes_3(A,B,C)=(A\otimes B)\otimes C$ — *identical* in the left-bracketing convention, so $\gamma_{2,1}=\mathrm{id}$. But $\gamma_{1,2;A,B,C}$ compares $\otimes_2(\otimes_1(A),\otimes_2(B,C)) = A\otimes(B\otimes C)$ with $\otimes_3(A,B,C)=(A\otimes B)\otimes C$, and these *differ* by the associator: $\gamma_{1,2} = \alpha_{A,B,C}^{-1}$.
>
> For a longer list, say $\gamma$ comparing $\otimes_2(\otimes_2(A,B),\otimes_2(C,D))=(A\otimes B)\otimes(C\otimes D)$ with $\otimes_4(A,B,C,D)=((A\otimes B)\otimes C)\otimes D$, the comparison is a composite of associators — and there is more than one such composite (one can re-bracket via different intermediate forms, exactly the two routes of the pentagon). For $\gamma$ to be *well-defined*, these composites must agree. This is precisely [[Thm - Mac Lane Coherence Theorem|Mac Lane's coherence theorem]]: any two morphisms in the free monoidal category built from $\alpha,\lambda,\rho$ with the same source and target are equal. Without coherence, $\gamma$ would depend on the chosen re-bracketing and the unbiased structure would be ill-defined.

**Step 3: The pentagon is the length-four associativity axiom.**

> [!note]- Derivation
> Combine the two directions. In Step 1 the pentagon for $\alpha = \gamma_{1,2}\gamma_{2,1}^{-1}$ followed from the *length-four* case of the unbiased associativity axiom. In Step 2 the well-definedness of $\gamma$ on a length-four list — the equality of the two re-bracketing routes — is exactly the pentagon for $\alpha$. So the two statements are the same equation read in opposite directions: **the pentagon is the length-four instance of the single unbiased associativity coherence axiom**, no more and no less. The reason there is a pentagon (and not a hexagon or an infinite family) is that length four is the first length at which two distinct re-bracketing routes exist; longer lists give larger coherence diagrams (the associahedra $K_n$), but all of them follow from the pentagon by [[Thm - Mac Lane Coherence Theorem|coherence]], which is itself the unbiased associativity axiom transported across [[Thm - Biased and Unbiased Monoidal Categories Coincide|the equivalence]].

> [!note]- Complete formal solution
> **(a)** Set $\alpha_{A,B,C}:=\gamma_{1,2}\circ\gamma_{2,1}^{-1}:(A\otimes_2 B)\otimes_2 C\to A\otimes_2(B\otimes_2 C)$, an isomorphism, natural since $\gamma$ is. For the pentagon, both sides are composites of $\gamma^{\pm}$ from $((A\otimes B)\otimes C)\otimes D$ to $A\otimes(B\otimes(C\otimes D))$, each factoring through $\otimes_4(A,B,C,D)$; the unbiased associativity axiom equates the two routes to $\otimes_4$, so the pentagon holds.
>
> **(b)** With $\otimes_n$ left-bracketed: $\gamma_{2,1;A,B,C}=\mathrm{id}$ (both source and target are $(A\otimes B)\otimes C$), while $\gamma_{1,2;A,B,C}=\alpha_{A,B,C}^{-1}$ (comparing $A\otimes(B\otimes C)$ with $(A\otimes B)\otimes C$). On a length-four list, $\gamma$ is a composite of associators, and there are several such composites; their equality is exactly [[Thm - Mac Lane Coherence Theorem|Mac Lane's coherence theorem]], which is therefore what makes $\gamma$ well-defined.
>
> **(c)** The pentagon (Step 1) is the length-four unbiased associativity axiom, and well-definedness of $\gamma$ on a length-four list (Step 2) is the pentagon; so the pentagon *is* the length-four associativity coherence axiom. It is necessary and sufficient, the first length at which two re-bracketing routes exist, and all higher coherences follow from it. $\qquad\blacksquare$

---

# Key Takeaways

**The flat tensor is the common refinement through which all bracketings factor — that is why coherence proofs never compute associator strings.** The recurring trick in part (a) is to route every comparison through the single flat object $\otimes_n(A_1,\dots,A_n)$ rather than navigating between bracketings directly. Once you do this, a coherence diagram becomes "two ways of contracting to a common refinement," which the associativity axiom resolves in one stroke. This is the same move that powers the full [[Thm - Coherence for Unbiased Monoidal Categories|coherence theorem]] (every tree contracts to the corolla) and the strict-pasting argument (every diagram contracts uniquely). Whenever you face "do these two composites of structural isomorphisms agree?", look for the common refinement they both reduce to; the answer is almost always yes for a structural reason, not a computational one.

**The asymmetry between the two directions is the location of all the mathematical content.** Extracting the binary structure from the unbiased one is free — the data is already present as the $\gamma$'s. Building the unbiased structure from the binary one is *not* free — it requires choosing a bracketing route, and only [[Thm - Mac Lane Coherence Theorem|coherence]] makes the choice irrelevant. This asymmetry is the precise reason coherence is a theorem at all: the binary presentation under-determines the comparison maps (many routes), and coherence is the statement that the over-determination is consistent. The diagnostic to carry away: when one direction of an equivalence is obvious and the other needs a theorem, the theorem is exactly the statement that a *choice* made in the hard direction does not matter.

**The pentagon is necessary and sufficient because length four is the first place two re-bracketing routes diverge.** Part (c) demystifies the pentagon entirely: it is not a magic five-sided diagram but the smallest non-trivial instance of "re-bracketing is coherent." Lengths one, two, and three admit a unique route between any two bracketings, so no axiom is needed; length four is the first with genuinely distinct routes, and demanding they agree is the pentagon. Higher lengths give bigger diagrams (the associahedra), but all follow from the pentagon. This is the model for understanding *every* coherence axiom in higher category theory: find the lowest [[Def - Dimension|dimension]] at which ambiguity first appears, and the coherence law there generates all the rest.
