---
type: exercise
subject: commutative-algebra
difficulty: "⭐"
prereqs:
  - "Def - Module"
  - "Def - Quotient Module"
  - "Def - Multiplicative Set and Localization"
  - "Def - Local Ring and Residue Field"
  - "Thm - Localization is Exact and the Localization is Flat"
  - "Thm - Localization Commutes with Quotients and Finite Operations"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $S\subseteq R$ be a [[Def - Multiplicative Set and Localization|multiplicative subset]], $M$ an [[Def - Module|$R$-module]], and $N\subseteq M$ a [[Def - Submodule|submodule]]. Prove that localization commutes with the quotient:
$$S^{-1}(M/N) \;\cong\; S^{-1}M / S^{-1}N \quad\text{as } S^{-1}R\text{-modules}, \qquad \tfrac{m+N}{s}\mapsfrom\tfrac ms + S^{-1}N.$$
Deduce the ring statement: for an ideal $\mathfrak{a}\trianglelefteq R$, $S^{-1}(R/\mathfrak{a})\cong S^{-1}R/\mathfrak{a}^e$. Then deduce the residue-field identity: for a prime $\mathfrak{p}$,
$$\kappa(\mathfrak{p}) := R_{\mathfrak{p}}/\mathfrak{p}R_{\mathfrak{p}} \;\cong\; (R/\mathfrak{p})_{\mathfrak{p}} = \operatorname{Frac}(R/\mathfrak{p}),$$
so "localize then quotient" equals "quotient then take fractions". (Becker uses this in Remark 4.21 to define $\kappa(\mathfrak{p})$.)

**Recall:**

![[Thm - Localization Commutes with Quotients and Finite Operations#Statement]]

The engine is the [[Thm - Localization is Exact and the Localization is Flat|exactness of localization]]: applying the exact functor $S^{-1}(-)$ to a short exact sequence keeps it exact. The [[Def - Local Ring and Residue Field|residue field]] is $\kappa(\mathfrak{p}) = R_{\mathfrak{p}}/\mathfrak{p}R_{\mathfrak{p}}$.

---

# Convergent Strategy

**Problem class.** This is a *localize-a-construction* problem: show that $S^{-1}(-)$ passes through a quotient. Per the [[Commutative Algebra IV — Localization#Legal Operations|topic legal operations]], the universal move for any built-up module is "localize the exact sequence that defines it" — here the defining sequence is $0\to N\to M\to M/N\to 0$.

**Assumption pattern.** No special hypotheses; the recognisable feature is simply that a *quotient* appears and one wants to localize it. The trigger is "$M/N$ is the cokernel of an inclusion", which means it sits at the end of a short exact sequence, which means exactness of localization applies directly.

**Theorem routing.** Apply the exact functor $S^{-1}(-)$ ([[Thm - Localization is Exact and the Localization is Flat]]) to $0\to N\to M\xrightarrow{\pi}M/N\to 0$; exactness gives $0\to S^{-1}N\to S^{-1}M\xrightarrow{S^{-1}\pi}S^{-1}(M/N)\to 0$, so $S^{-1}(M/N)$ is the cokernel of $S^{-1}N\hookrightarrow S^{-1}M$, i.e. $S^{-1}M/S^{-1}N$. The ring and residue-field statements are specialisations ($M = R$, $N = \mathfrak{a}$; then $\mathfrak{a} = \mathfrak{p}$ with $S = R\setminus\mathfrak{p}$).

**Key decision point.** The one decision is to *prove it via the exact sequence rather than by hand*. One could try to build the isomorphism $\tfrac ms + S^{-1}N\mapsto\tfrac{m+N}{s}$ directly and check well-definedness and bijectivity through fraction arithmetic — tedious and error-prone. The clean path observes that this map is exactly $S^{-1}\pi$ followed by the first isomorphism theorem, so exactness does all the work. The residue-field deduction then requires noticing that $(R/\mathfrak{p})_{\mathfrak{p}}$ is the localization of a *domain* at its zero ideal, i.e. its fraction field.

---

# Legal Operations Used

This solution deploys the following [[Commutative Algebra IV — Localization#Legal Operations|legal operations from the topic page]]:

1. **Operation 3 (localize an exact sequence).** The entire proof: apply $S^{-1}(-)$ to $0\to N\to M\to M/N\to 0$ and keep exactness.

2. **Operation 8 (pass between $R_{\mathfrak{p}}$, $R/\mathfrak{p}$, and $\kappa(\mathfrak{p})$).** The residue-field deduction reconciles localize-then-quotient with quotient-then-fractions.

3. **Operation 9 (localization commutes with finite operations).** The result *is* the quotient case of this operation; the deduction uses it for ideals.

---

# Hints

> [!note]- Hint 1
> $M/N$ is the cokernel of the inclusion $N\hookrightarrow M$ — it sits at the right end of the short exact sequence $0\to N\to M\to M/N\to 0$. You have a powerful theorem about what localization does to exact sequences. Apply it.

> [!note]- Hint 2
> Localization is an [[Thm - Localization is Exact and the Localization is Flat|exact functor]], so $0\to S^{-1}N\to S^{-1}M\xrightarrow{S^{-1}\pi}S^{-1}(M/N)\to 0$ is exact. Read off: $S^{-1}\pi$ is surjective with kernel $S^{-1}N$. What does the first isomorphism theorem give?

> [!note]- Hint 3
> For the residue field: take $M = R$, $N = \mathfrak{p}$, $S = R\setminus\mathfrak{p}$. Then $S^{-1}(R/\mathfrak{p}) = (R/\mathfrak{p})_{\mathfrak{p}}$ — but $R/\mathfrak{p}$ is a *domain*, and the image of $S = R\setminus\mathfrak{p}$ in $R/\mathfrak{p}$ is exactly the *nonzero* elements. Localizing a domain at all its nonzero elements gives what?

---

# Solution

Localize the defining short exact sequence $0\to N\to M\to M/N\to 0$; exactness makes $S^{-1}(M/N)$ the cokernel of $S^{-1}N\hookrightarrow S^{-1}M$, which is $S^{-1}M/S^{-1}N$. Specialising to $M = R$, $N = \mathfrak{a}$ gives the ring statement, and to $\mathfrak{a} = \mathfrak{p}$ gives the residue field as the fraction field of the domain $R/\mathfrak{p}$.

**Step 1: Localize the defining short exact sequence.**

Applying the exact functor to $0\to N\to M\to M/N\to 0$ keeps it exact.

> [!note]- Derivation
> The inclusion $\iota : N\hookrightarrow M$ and quotient $\pi : M\twoheadrightarrow M/N$ form the short exact sequence
> $$0\to N\xrightarrow{\iota}M\xrightarrow{\pi}M/N\to 0.$$
> By [[Thm - Localization is Exact and the Localization is Flat|exactness of $S^{-1}(-)$]], applying it preserves exactness:
> $$0\to S^{-1}N\xrightarrow{S^{-1}\iota}S^{-1}M\xrightarrow{S^{-1}\pi}S^{-1}(M/N)\to 0$$
> is exact. Here $S^{-1}\iota$ embeds $S^{-1}N$ as a submodule of $S^{-1}M$, and $S^{-1}\pi$ acts by $\tfrac ms\mapsto\tfrac{\pi(m)}{s} = \tfrac{m+N}{s}$.

**Step 2: Read off the isomorphism via the first isomorphism theorem.**

Exactness says $S^{-1}\pi$ is surjective with kernel $S^{-1}N$, giving $S^{-1}M/S^{-1}N\cong S^{-1}(M/N)$.

> [!note]- Derivation
> From the exact sequence, $S^{-1}\pi$ is surjective (the map onto $S^{-1}(M/N)$ is onto), and $\ker(S^{-1}\pi) = \operatorname{im}(S^{-1}\iota) = S^{-1}N$. By the first isomorphism theorem for $S^{-1}R$-modules,
> $$S^{-1}M/S^{-1}N = S^{-1}M/\ker(S^{-1}\pi)\;\cong\;\operatorname{im}(S^{-1}\pi) = S^{-1}(M/N),$$
> via $\tfrac ms + S^{-1}N\mapsto\tfrac{m+N}{s}$. This is the desired isomorphism, well-defined and bijective automatically — exactness supplied everything, with no fraction bookkeeping.

**Step 3: The ring statement.**

Take $M = R$, $N = \mathfrak{a}$: $S^{-1}(R/\mathfrak{a})\cong S^{-1}R/\mathfrak{a}^e$.

> [!note]- Derivation
> With $M = R$ and $N = \mathfrak{a}\trianglelefteq R$, Step 2 gives $S^{-1}(R/\mathfrak{a})\cong S^{-1}R/S^{-1}\mathfrak{a} = S^{-1}R/\mathfrak{a}^e$ (recall $\mathfrak{a}^e = S^{-1}\mathfrak{a}$ for the localization map). The isomorphism is one of $S^{-1}R$-algebras: it sends $\tfrac{r+\mathfrak{a}}{s}\mapsto\tfrac rs + \mathfrak{a}^e$ and respects multiplication, since both $\pi$ and $S^{-1}(-)$ are ring/algebra maps.

**Step 4: The residue field.**

Take $\mathfrak{a} = \mathfrak{p}$, $S = R\setminus\mathfrak{p}$: $\kappa(\mathfrak{p}) = R_{\mathfrak{p}}/\mathfrak{p}R_{\mathfrak{p}}\cong(R/\mathfrak{p})_{\mathfrak{p}} = \operatorname{Frac}(R/\mathfrak{p})$.

> [!note]- Derivation
> Let $\mathfrak{p}$ be prime and $S = R\setminus\mathfrak{p}$. By Step 3, $R_{\mathfrak{p}}/\mathfrak{p}R_{\mathfrak{p}} = S^{-1}R/\mathfrak{p}^e\cong S^{-1}(R/\mathfrak{p}) = (R/\mathfrak{p})_{\mathfrak{p}}$, where $(R/\mathfrak{p})_{\mathfrak{p}}$ denotes localizing the domain $R/\mathfrak{p}$ at the image $\bar S$ of $S$. Now $\bar S = $ image of $R\setminus\mathfrak{p}$ in $R/\mathfrak{p}$ is exactly $(R/\mathfrak{p})\setminus\{0\}$ (an element maps to $0$ iff it lies in $\mathfrak{p}$). So $(R/\mathfrak{p})_{\mathfrak{p}}$ is the localization of the domain $R/\mathfrak{p}$ at *all its nonzero elements*, which is by definition its [[Def - Field of Fractions|fraction field]] $\operatorname{Frac}(R/\mathfrak{p})$. Hence
> $$\kappa(\mathfrak{p}) = R_{\mathfrak{p}}/\mathfrak{p}R_{\mathfrak{p}}\cong\operatorname{Frac}(R/\mathfrak{p}),$$
> a field — confirming that "localize at $\mathfrak{p}$ then quotient by the maximal ideal" equals "quotient by $\mathfrak{p}$ then take fractions".

> [!note]- Complete formal solution
> Apply the exact functor $S^{-1}(-)$ to $0\to N\to M\xrightarrow{\pi}M/N\to 0$ to get the exact sequence $0\to S^{-1}N\to S^{-1}M\xrightarrow{S^{-1}\pi}S^{-1}(M/N)\to 0$. Thus $S^{-1}\pi$ is surjective with kernel $S^{-1}N$, and the first isomorphism theorem gives $S^{-1}(M/N)\cong S^{-1}M/S^{-1}N$ via $\tfrac{m+N}{s}\mapsfrom\tfrac ms + S^{-1}N$.
>
> Taking $M = R$, $N = \mathfrak{a}$: $S^{-1}(R/\mathfrak{a})\cong S^{-1}R/\mathfrak{a}^e$.
>
> Taking $\mathfrak{a} = \mathfrak{p}$, $S = R\setminus\mathfrak{p}$: $R_{\mathfrak{p}}/\mathfrak{p}R_{\mathfrak{p}}\cong(R/\mathfrak{p})_{\mathfrak{p}}$; since the image of $R\setminus\mathfrak{p}$ in the domain $R/\mathfrak{p}$ is its set of nonzero elements, $(R/\mathfrak{p})_{\mathfrak{p}} = \operatorname{Frac}(R/\mathfrak{p}) = \kappa(\mathfrak{p})$. $\blacksquare$

---

# Key Takeaways

**Localize a construction by localizing the exact sequence that defines it.** Every basic module construction — quotient, kernel, image, cokernel — is the (co)kernel of a map, hence sits in a short exact sequence, and because localization is exact, $S^{-1}(-)$ commutes with all of them. The recipe is mechanical and universal: write the defining sequence, apply $S^{-1}(-)$, read off the (co)kernel. This spares you every well-definedness check that a hands-on fraction construction would demand — the isomorphism $\tfrac ms + S^{-1}N\mapsto\tfrac{m+N}{s}$ is handed to you by exactness plus the first isomorphism theorem. Internalise this as the default response to "localize this quotient/kernel/image": never compute, always localize the sequence.

**The residue field is a theorem, not two definitions, and the proof is "the image of $R\setminus\mathfrak{p}$ is the nonzero elements of $R/\mathfrak{p}$".** Students often see $\kappa(\mathfrak{p}) = R_{\mathfrak{p}}/\mathfrak{p}R_{\mathfrak{p}}$ and $\kappa(\mathfrak{p}) = \operatorname{Frac}(R/\mathfrak{p})$ as two unrelated formulas to memorise. This exercise shows they are *equal*, and the bridge is quotient–localization commutation plus the observation that localizing the domain $R/\mathfrak{p}$ at $\bar S = (R/\mathfrak{p})\setminus\{0\}$ is precisely forming its fraction field. The transferable point: "localize then quotient" and "quotient then localize" commute (for compatible data), so the value field of a point can be computed by whichever order is convenient — localize first to get a local ring and kill its maximal ideal, or quotient first to get the function ring of the subvariety and take its fractions. Recognising this symmetry resolves the perennial confusion between $R_{\mathfrak{p}}$ and $R/\mathfrak{p}$: they are the two halves that meet in $\kappa(\mathfrak{p})$.

**Commutation of localization and quotient is the algebraic form of "restriction to an open set commutes with restriction to a closed subscheme".** Geometrically, $R/\mathfrak{a}$ is the functions on the closed subvariety $V(\mathfrak{a})$, and $S^{-1}(-)$ is restriction to an open set; the identity $S^{-1}(R/\mathfrak{a})\cong S^{-1}R/\mathfrak{a}^e$ says it does not matter whether you first cut out the subvariety and then restrict to the open set, or first restrict and then cut — the two operations commute. This is the compatibility that makes the structure sheaf well-defined on intersections of opens and closed subschemes, and it is why "the local ring of a point on a subvariety" $R_{\mathfrak{p}}/\mathfrak{q}R_{\mathfrak{p}}\cong(R/\mathfrak{q})_{\mathfrak{p}}$ is unambiguous — see [[Thm - Localization Commutes with Quotients and Finite Operations]] for the general statement underlying all of this.
