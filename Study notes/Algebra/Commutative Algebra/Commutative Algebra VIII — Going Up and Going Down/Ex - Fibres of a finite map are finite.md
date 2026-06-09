---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Thm - Incomparability"
  - "Def - The Induced Map on Spectra"
  - "Def - Local Ring and Residue Field"
  - "Def - Finitely Generated Module"
  - "Thm - Lying Over"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $A \subseteq B$ be a **finite** extension — that is, $B$ is a finitely generated $A$-module (equivalently, module-finite; this implies integral). Prove that every fibre of the contraction map $\iota^* : \operatorname{Spec} B \to \operatorname{Spec} A$ is a **finite set**: for each $\mathfrak{p} \in \operatorname{Spec} A$,
$$\#\{\mathfrak{q} \in \operatorname{Spec} B : \mathfrak{q} \cap A = \mathfrak{p}\} < \infty.$$

The intended route: identify the fibre with $\operatorname{Spec}$ of the **fibre ring** $\bar B := B \otimes_A \kappa(\mathfrak{p}) \cong (B/\mathfrak{p}B)_{\mathfrak{p}}$; show $\bar B$ is a *finite-dimensional algebra over the field* $\kappa(\mathfrak{p})$; conclude $\bar B$ is Artinian, hence has only finitely many primes — all maximal by [[Thm - Incomparability|incomparability]].

**Recall:**

The objects in play are finite (module-finite) extensions, the fibre and the fibre ring, the residue field, incomparability, and Artinian rings.

![[Def - The Induced Map on Spectra#The fibre over a prime]]

A **finite** extension $A \subseteq B$ has $B$ a [[Def - Finitely Generated Module|finitely generated]] $A$-module; this forces $B$ integral over $A$ (each $b$ satisfies the characteristic polynomial of multiplication-by-$b$). The **fibre ring** over $\mathfrak{p}$ is $B \otimes_A \kappa(\mathfrak{p})$, where $\kappa(\mathfrak{p}) = A_{\mathfrak{p}}/\mathfrak{p}A_{\mathfrak{p}}$ is the [[Def - Local Ring and Residue Field|residue field]]; its prime spectrum is the fibre.

![[Thm - Incomparability#Statement]]

An **Artinian ring** (descending chain condition on ideals) has Krull dimension $0$ and only finitely many prime ideals, all maximal — in particular a finite-dimensional algebra over a field is Artinian.

---

# Convergent Strategy

**Problem class.** This is a *bound-the-fibre-size* problem — the finiteness refinement of incomparability. As the [[Commutative Algebra VIII — Going Up and Going Down#Problem-Solving Strategy|topic-page strategy]] records, finiteness of a fibre is established by demanding module-finiteness and recognising the fibre ring as a finite-dimensional algebra over the residue field, hence Artinian.

**Assumption pattern.** Two hypotheses do distinct jobs. "$B$ module-finite over $A$" makes the fibre ring $B \otimes_A \kappa(\mathfrak{p})$ *finite-dimensional* over $\kappa(\mathfrak{p})$ (tensoring a finite module by a field gives a finite-dimensional vector space). "$A \subseteq B$ integral" (implied) gives [[Thm - Incomparability|incomparability]], so the fibre is zero-dimensional. The recognisable trigger is "how many primes over $\mathfrak{p}$?" with a *finite* extension — which always routes through "fibre ring is Artinian".

**Theorem routing.** The route is: the fibre is $\operatorname{Spec}(B \otimes_A \kappa(\mathfrak{p}))$ (fibre dictionary); $B$ finite over $A$ $\Rightarrow$ $B \otimes_A \kappa(\mathfrak{p})$ finite-dimensional over the field $\kappa(\mathfrak{p})$ (base change of a finite module); a finite-dimensional algebra over a field is *Artinian*; an Artinian ring has finitely many primes, all maximal. So the fibre is a finite set of (maximal) primes. Incomparability re-certifies that they are maximal/incomparable, consistent with $\dim = 0$.

**Key decision point.** The non-obvious move is to pass to the *fibre ring over the residue field*, $B \otimes_A \kappa(\mathfrak{p})$, rather than work in $B$ or even $B_{\mathfrak{p}}$. The fibre ring kills $\mathfrak{p}$ *and* inverts $A \setminus \mathfrak{p}$, leaving an algebra over the *field* $\kappa(\mathfrak{p})$ — and "finite-dimensional over a field" is exactly the hypothesis that triggers Artinian-ness. The temptation is to count primes of $B_{\mathfrak{p}}$ directly, but $B_{\mathfrak{p}}$ is not finite-dimensional over anything; the residue-field reduction is what makes finiteness visible. The second decision is realising that *finite-dimensional algebra over a field $\Rightarrow$ Artinian* is the bridge from linear algebra (finite dimension) to commutative algebra (finitely many primes).

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra VIII — Going Up and Going Down#Legal Operations|the topic page's Legal Operations]]:

1. **Recognise a finite fibre via the fibre ring (operation 9).** The fibre is $\operatorname{Spec}(B \otimes_A \kappa(\mathfrak{p}))$, a finite-$\kappa(\mathfrak{p})$-dimensional algebra, hence Artinian, hence finite spectrum.

2. **Translate the fibre into the fibre ring (operation 1).** Identify primes over $\mathfrak{p}$ with $\operatorname{Spec}$ of one ring over a field.

3. **Use incomparability to certify zero-dimensionality (operation 5).** The fibre primes are maximal and pairwise incomparable, consistent with the Artinian fibre ring having $\dim = 0$.

---

# Hints

> [!note]- Hint 1
> "How many primes over $\mathfrak{p}$?" is a question about the *fibre ring*. Which ring's spectrum is the fibre over $\mathfrak{p}$? (Reduce to an algebra over a *field*.)

> [!note]- Hint 2
> The fibre is $\operatorname{Spec}(B \otimes_A \kappa(\mathfrak{p}))$, where $\kappa(\mathfrak{p})$ is the residue field. Since $B$ is a *finite* $A$-module — say generated by $b_1, \dots, b_m$ — what does $B \otimes_A \kappa(\mathfrak{p})$ look like as a $\kappa(\mathfrak{p})$-vector space?

> [!note]- Hint 3
> $B \otimes_A \kappa(\mathfrak{p})$ is spanned over $\kappa(\mathfrak{p})$ by $b_1 \otimes 1, \dots, b_m \otimes 1$, so it is *finite-dimensional* (dimension $\leq m$) over the field $\kappa(\mathfrak{p})$. A finite-dimensional algebra over a field is Artinian. What does Artinian say about primes?

> [!note]- Hint 4
> An Artinian ring has only finitely many prime ideals, and they are all maximal (Artinian $\Rightarrow$ Krull dimension $0$, and there are finitely many maximal ideals). So the fibre is finite. Incomparability independently confirms the fibre primes are maximal and incomparable.

---

# Solution

The proof reduces a counting question to linear algebra. The fibre over $\mathfrak{p}$ is the spectrum of the fibre ring $B \otimes_A \kappa(\mathfrak{p})$; module-finiteness makes this a finite-dimensional algebra over the field $\kappa(\mathfrak{p})$; a finite-dimensional algebra over a field is Artinian; and an Artinian ring has finitely many primes. Incomparability confirms they are all maximal.

**Step 1: The fibre is $\operatorname{Spec}$ of the fibre ring $\bar B = B \otimes_A \kappa(\mathfrak{p})$.**

The primes of $B$ over $\mathfrak{p}$ correspond bijectively to the primes of $\bar B = B \otimes_A \kappa(\mathfrak{p}) \cong (B/\mathfrak{p}B)_{\mathfrak{p}}$.

> [!note]- Derivation
> By the [[Def - The Induced Map on Spectra|fibre dictionary]], the fibre $(\iota^*)^{-1}(\mathfrak{p})$ is in bijection with $\operatorname{Spec}(B \otimes_A \kappa(\mathfrak{p}))$. Concretely, $B \otimes_A \kappa(\mathfrak{p}) \cong (B/\mathfrak{p}B)_{\mathfrak{p}}$: tensoring $B$ with $\kappa(\mathfrak{p}) = A_{\mathfrak{p}}/\mathfrak{p}A_{\mathfrak{p}}$ first reduces mod $\mathfrak{p}$ (giving $B/\mathfrak{p}B$) then localizes at the image of $A \setminus \mathfrak{p}$. The primes of this ring are exactly those primes $\mathfrak{q}$ of $B$ containing $\mathfrak{p}B$ (so $\mathfrak{q} \cap A \supseteq \mathfrak{p}$) and disjoint from $A \setminus \mathfrak{p}$ (so $\mathfrak{q} \cap A \subseteq \mathfrak{p}$), i.e. with $\mathfrak{q} \cap A = \mathfrak{p}$ — the fibre.

**Step 2: $\bar B$ is finite-dimensional over the field $\kappa(\mathfrak{p})$.**

If $B$ is generated by $b_1, \dots, b_m$ as an $A$-module, then $\bar B$ is spanned by $b_1 \otimes 1, \dots, b_m \otimes 1$ over $\kappa(\mathfrak{p})$, so $\dim_{\kappa(\mathfrak{p})} \bar B \leq m < \infty$.

> [!note]- Derivation
> $B$ is a [[Def - Finitely Generated Module|finitely generated]] $A$-module: $B = A b_1 + \cdots + A b_m$. Tensoring the surjection $A^m \twoheadrightarrow B$ (sending the standard basis to the $b_i$) with $\kappa(\mathfrak{p})$ over $A$ — and using that tensoring is right-exact, so it preserves surjections — gives a surjection of $\kappa(\mathfrak{p})$-vector spaces
> $$\kappa(\mathfrak{p})^m = A^m \otimes_A \kappa(\mathfrak{p}) \;\twoheadrightarrow\; B \otimes_A \kappa(\mathfrak{p}) = \bar B.$$
> Hence $\bar B$ is spanned over $\kappa(\mathfrak{p})$ by the images $b_1 \otimes 1, \dots, b_m \otimes 1$, so $\dim_{\kappa(\mathfrak{p})}\bar B \leq m$. In particular $\bar B$ is a *finite-dimensional algebra over the field* $\kappa(\mathfrak{p})$.

**Step 3: $\bar B$ is Artinian, so has finitely many primes — all maximal.**

A finite-dimensional algebra over a field is Artinian; an Artinian ring has finitely many primes, all maximal. Hence the fibre is finite.

> [!note]- Derivation
> A $\kappa(\mathfrak{p})$-algebra $\bar B$ of finite dimension $d$ satisfies the descending chain condition on ideals: any strictly descending chain of ideals is a strictly descending chain of $\kappa(\mathfrak{p})$-subspaces, and dimensions strictly decrease, so the chain has length $\leq d$. Thus $\bar B$ is **Artinian**. An Artinian ring has Krull dimension $0$ (every prime is maximal) and only finitely many maximal ideals (its quotient by the nilradical is a finite product of fields, by the structure theory of Artinian rings). Therefore $\operatorname{Spec}\bar B$ is a finite set of maximal ideals, and by Step 1 the fibre $(\iota^*)^{-1}(\mathfrak{p})$ is finite.
>
> Consistency with [[Thm - Incomparability|incomparability]]: incomparability already told us the fibre is an antichain (the fibre ring has $\dim = 0$); the new content of *module-finiteness* is that the antichain is *finite*. The two combine to "non-empty finite fibre" (non-emptiness from [[Thm - Lying Over|lying over]]).

> [!note]- Complete formal solution
> Let $A \subseteq B$ be finite, $\mathfrak{p} \in \operatorname{Spec} A$.
>
> The fibre over $\mathfrak{p}$ is in bijection with $\operatorname{Spec}(\bar B)$, $\bar B = B \otimes_A \kappa(\mathfrak{p}) \cong (B/\mathfrak{p}B)_{\mathfrak{p}}$.
>
> If $B = Ab_1 + \cdots + Ab_m$, tensoring $A^m \twoheadrightarrow B$ with $\kappa(\mathfrak{p})$ gives $\kappa(\mathfrak{p})^m \twoheadrightarrow \bar B$, so $\dim_{\kappa(\mathfrak{p})}\bar B \leq m < \infty$.
>
> A finite-dimensional algebra over a field is Artinian (descending chains of ideals are descending chains of subspaces, with strictly decreasing dimension). An Artinian ring has finitely many primes, all maximal. Hence $\operatorname{Spec}\bar B$ — the fibre — is finite. $\blacksquare$

---

# Key Takeaways

**Finiteness of a fibre is finite-dimensionality of the fibre ring over the residue field.** The reusable principle: the size of a fibre is controlled by the fibre ring $B \otimes_A \kappa(\mathfrak{p})$, and "finite fibre" is the linear-algebra statement "this ring is finite-dimensional over the field $\kappa(\mathfrak{p})$", which holds exactly when $B$ is module-finite over $A$. The trigger is any "count the points in the fibre" question for a finite map; the move is to base-change to the residue field and count maximal ideals of the resulting finite-dimensional algebra. This is why *finite* maps (module-finite) have finite fibres while merely *integral* maps need not — integrality gives zero-dimensional fibres, but only module-finiteness bounds their cardinality. The same reduction computes the number of points in the fibre of a finite map of varieties and the number of primes over $p$ in a number ring (where $\dim_{\mathbb{F}_p}\mathcal{O}_K/p\mathcal{O}_K = [K:\mathbb{Q}]$ bounds the count).

**"Finite-dimensional over a field $\Rightarrow$ Artinian $\Rightarrow$ finite spectrum" is a high-value bridge.** This chain of implications converts a *dimension* (linear algebra) into a *finiteness of primes* (commutative algebra), and it recurs constantly: it is why a finite field extension is zero-dimensional, why the fibre ring of a finite map has finitely many points, why a finitely generated algebra over a field that is also integral over the field is Artinian. Internalise it as a unit — whenever a ring is finite-dimensional over a field, immediately conclude it is Artinian, has finitely many primes, all maximal, and is a finite product of local Artinian rings. The descending-chain-condition argument (descending ideals are descending subspaces, dimension strictly drops) is the one-line proof worth remembering.

**Incomparability and module-finiteness split the labour: zero-dimensional versus finite.** It is worth separating what each hypothesis buys. [[Thm - Incomparability|Incomparability]] (pure integrality) makes the fibre an *antichain* — zero-dimensional, no nesting. Module-finiteness makes that antichain *finite*. Neither alone gives "finite fibre": an integral extension that is not module-finite (e.g. the integral closure of a non-Japanese ring, or $\bar{\mathbb{Q}}$ over $\mathbb{Q}$) can have a fibre that is zero-dimensional but infinite. The diagnostic for spaced practice: when you need *finiteness* of a fibre, check for *module-finiteness*, not just integrality; when you need only *zero-dimensionality* (incomparability), integrality suffices. The companion [[Ex - Primes of Z[i] over a rational prime]] computes a fibre explicitly and sees both — one or two points, always finite, always incomparable.
