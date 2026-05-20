---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐"
prereqs:
  - "Thm - Properties of Conditional Expectation"
  - "Def - Independence"
tags: [probability, advanced-probability]
---

# Problem Statement

**(a)** Show that if $X$ is independent of $\mathcal{G}$, then $\mathbb{E}[X\mid\mathcal{G}]=\mathbb{E}[X]$ — conditioning on irrelevant information collapses to the unconditional mean.

**(b)** Show the *role-reversal* fact: if $X$ is $\mathcal{G}$-measurable and $Y$ is independent of $\mathcal{G}$, then for Borel $h$,
$$\mathbb{E}[h(X,Y)\mid\mathcal{G}]=g(X),\qquad g(x)=\mathbb{E}[h(x,Y)].$$

**(c)** Show that adding *independent* information does not change a conditional expectation: if $\sigma(X,\mathcal{G})$ is independent of $\mathcal{H}$, then $\mathbb{E}[X\mid\sigma(\mathcal{G},\mathcal{H})]=\mathbb{E}[X\mid\mathcal{G}]$.

**Recall:**

[[Def - Independence|Independence]]; [[Thm - Properties of Conditional Expectation|properties of conditional expectation]] — characterise by $\mathcal{G}$-measurability + the averaging identity.

---

# Convergent Strategy

**Problem class:** computing conditional expectations when independence is present — independence makes the conditioning *partly inert*.

**Assumption pattern:** independence lets a factor be replaced by its mean. Each part is proved by the *propose-and-verify* method: write down the candidate, check it is measurable for the relevant $\sigma$-algebra and has the right integrals.

---

# Legal Operations Used

1. **Propose a candidate, verify the two characterising properties.**
2. **Independence $\Rightarrow$ factorisation of expectations**; check the averaging identity on a $\pi$-system.

---

# Hints

> [!note]- Hint 1
> (a): the constant $\mathbb{E}[X]$ is $\mathcal{G}$-measurable; check $\mathbb{E}[\mathbb{E}[X]\mathbf{1}_A]=\mathbb{E}[X\mathbf{1}_A]$ using independence.

> [!note]- Hint 2
> (b): "freeze" the $\mathcal{G}$-measurable $X$ at a value $x$ and average only the independent $Y$ — verify $g(X)$ has the right $\mathcal{G}$-integrals.

> [!note]- Hint 3
> (c): check that $\mathbb{E}[X\mid\mathcal{G}]$ — already $\sigma(\mathcal{G},\mathcal{H})$-measurable — satisfies the averaging identity over the generating $\pi$-system $\{A\cap B:A\in\mathcal{G},B\in\mathcal{H}\}$.

---

# Solution

The proof breaks into three steps, one per sub-part, each a propose-and-verify against the conditional-expectation characterisation. Step 1 (part a) proposes the constant $\mathbb{E}[X]$ and verifies the averaging identity using $X \perp \mathcal{G}$; Step 2 (part b) proposes $g(X) = \mathbb{E}[h(x, Y)]|_{x = X}$ and verifies the identity via Fubini against the product law of $((X, \mathbf{1}_A), Y)$; Step 3 (part c) shows $\mathbb{E}[X\mid\mathcal{G}]$ already satisfies the averaging identity for the larger $\sigma$-algebra by checking on the $\pi$-system $\{A \cap B\}$ and extending via Dynkin. The non-obvious move is "freeze what is known, average what is independent" (Step 2) — this is the conditional analogue of Fubini and the engine of all Markov-property calculations.

**Step 1 — (a).** The constant $\mathbb{E}[X]$ is $\mathcal{G}$-measurable. For $A\in\mathcal{G}$, $X$ and $\mathbf{1}_A$ are independent, so $\mathbb{E}[X\mathbf{1}_A]=\mathbb{E}[X]\mathbb{E}[\mathbf{1}_A]=\mathbb{E}[\mathbb{E}[X]\mathbf{1}_A]$ — the averaging identity. By [[Thm - Existence and Uniqueness of Conditional Expectation|uniqueness]], $\mathbb{E}[X\mid\mathcal{G}]=\mathbb{E}[X]$.

**Step 2 — (b).** Define $g(x)=\mathbb{E}[h(x,Y)]$ — average out $Y$ with $x$ frozen. Then $g(X)$ is $\mathcal{G}$-measurable ($X$ is, $g$ Borel). For $A\in\mathcal{G}$: since $X,\mathbf{1}_A$ are $\mathcal{G}$-measurable and $Y$ is independent of $\mathcal{G}$, [[Thm - Fubini-Tonelli Theorem|Fubini]] against the product law of $((X,\mathbf{1}_A),Y)$ gives
$$\mathbb{E}[h(X,Y)\mathbf{1}_A]=\mathbb{E}\big[\mathbb{E}[h(x,Y)]\big|_{x=X}\mathbf{1}_A\big]=\mathbb{E}[g(X)\mathbf{1}_A].$$
So $g(X)$ satisfies the characterisation: $\mathbb{E}[h(X,Y)\mid\mathcal{G}]=g(X)$. *Known information is frozen, independent information is averaged.*

**Step 3 — (c).** $\mathbb{E}[X\mid\mathcal{G}]$ is $\mathcal{G}$-measurable, hence $\sigma(\mathcal{G},\mathcal{H})$-measurable. The sets $A\cap B$ ($A\in\mathcal{G}$, $B\in\mathcal{H}$) form a [[Thm - Dynkin's π-λ Theorem|π-system]] generating $\sigma(\mathcal{G},\mathcal{H})$; it suffices to verify the averaging identity there. Since $\sigma(X,\mathcal{G})$ is independent of $\mathcal{H}$, both $X\mathbf{1}_A$ and $\mathbb{E}[X\mid\mathcal{G}]\mathbf{1}_A$ are independent of $\mathbf{1}_B$, so
$$\mathbb{E}[X\mathbf{1}_{A\cap B}]=\mathbb{E}[X\mathbf{1}_A]\mathbb{P}(B)=\mathbb{E}[\mathbb{E}[X\mid\mathcal{G}]\mathbf{1}_A]\mathbb{P}(B)=\mathbb{E}[\mathbb{E}[X\mid\mathcal{G}]\mathbf{1}_{A\cap B}].$$
By [[Thm - Dynkin's π-λ Theorem|Dynkin]] the identity extends to all of $\sigma(\mathcal{G},\mathcal{H})$; uniqueness gives $\mathbb{E}[X\mid\sigma(\mathcal{G},\mathcal{H})]=\mathbb{E}[X\mid\mathcal{G}]$.

> [!note]- Complete formal solution
> (a) $\mathbb{E}[X]$ is $\mathcal{G}$-measurable; independence gives $\mathbb{E}[X\mathbf{1}_A]=\mathbb{E}[X]\mathbb{P}(A)$ for $A\in\mathcal{G}$; uniqueness. (b) $g(X)$, $g(x)=\mathbb{E}[h(x,Y)]$, is $\mathcal{G}$-measurable and (Fubini, $Y\perp\mathcal{G}$) has the right $\mathcal{G}$-integrals. (c) $\mathbb{E}[X\mid\mathcal{G}]$ satisfies the averaging identity on the $\pi$-system $\{A\cap B\}$ by independence; Dynkin extends it. $\blacksquare$

---

# Key Takeaways

**Independence makes conditioning partly inert: information independent of $X$ contributes nothing, and adding independent information to a conditioning $\sigma$-algebra changes nothing.** $\mathbb{E}[X\mid\mathcal{G}]=\mathbb{E}[X]$ when $X\perp\mathcal{G}$ — conditioning on the irrelevant collapses to the global mean. And $\mathbb{E}[X\mid\sigma(\mathcal{G},\mathcal{H}))=\mathbb{E}[X\mid\mathcal{G}]$ when $\mathcal{H}$ is independent of everything relevant — extra noise is invisible. These are the rules that let one *discard* irrelevant $\sigma$-algebras in a computation, and they are essential to the [[Thm - Strong Law of Large Numbers|backward-martingale proof of the SLLN]] ("adding the independent tail does not change the conditional expectation").

**The "freeze the known, average the independent" rule is the master recipe for $\mathbb{E}[h(X,Y)\mid\mathcal{G}]$ when $X$ is known and $Y$ is independent.** Treat the $\mathcal{G}$-measurable $X$ as a fixed parameter, average out the independent $Y$, and substitute $X$ back: $\mathbb{E}[h(X,Y)\mid\mathcal{G}]=g(X)$ with $g(x)=\mathbb{E}[h(x,Y)]$. This is the [[Thm - Fubini-Tonelli Theorem|Fubini]]-on-a-product-law computation in conditional form, and it is exactly how Markov-property and strong-Markov calculations are carried out — the future depends on an independent increment with the present "frozen."
