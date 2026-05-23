---
type: theorem
subject: ring-theory
prereqs:
  - "Def - Ring"
  - "Def - Subring"
  - "Def - Ring Homomorphism"
  - "Def - Ideal"
  - "Def - Quotient Ring"
  - "Thm - First Isomorphism Theorem for Rings"
tags: [algebra, ring-theory]
---

# Notation

Throughout, $S$ is a [[Def - Ring|ring]], $R \leq S$ is a [[Def - Subring|subring]] (a subset containing $0_S$ and $1_S$, closed under $+$, $-$, and $\times$), and $J \trianglelefteq S$ is an [[Def - Ideal|ideal]] of $S$ (an additive subgroup with the strong-closure property $a \in J,\ s \in S \implies as, sa \in J$). We write
$$R + J = \{r + j : r \in R,\ j \in J\}, \qquad R \cap J = \{x : x \in R \text{ and } x \in J\}.$$
The [[Def - Quotient Ring|quotient ring]] $S/J$ has elements the cosets $s + J$; inside it,
$$(R + J)/J = \{r + J : r \in R\}$$
is the set of cosets with a representative in $R$. The symbol $\trianglelefteq$ means "is an ideal of", $\leq$ means "is a subring of", $\hookrightarrow$ denotes an inclusion, $\twoheadrightarrow$ a surjection, and $\cong$ a ring isomorphism. The full symbol registry is on the parent page [[Rings I — §2.1–2.2]].

---

# Statement

> **[[Thm - Second Isomorphism Theorem|Second Isomorphism Theorem]] for [[Def - Ring|Rings]].** Let $S$ be a ring, $R \leq S$ a [[Def - Subring|subring]], and $J \trianglelefteq S$ an ideal. Then:
> - $R \cap J$ is an ideal of $R$;
> - $(R + J)/J$ is a subring of $S/J$;
> - there is a ring isomorphism
> $$\frac{R}{R \cap J} \;\cong\; \frac{R + J}{J}.$$

---

# Motivation

The first isomorphism theorem tells you that *if* you have a homomorphism, you can read off a quotient. But many situations do not hand you a homomorphism — they hand you two *substructures* of a ring: a subring $R$ and an ideal $J$, sitting side by side inside $S$. The natural question is how they interact. Can you build a new ring from $R$ and $J$ together? How does $R$ see the quotient $S/J$? The second isomorphism theorem is the systematic answer.

Concretely, picture the quotient $S/J$ and ask: what does the subring $R$ look like *after* you pass to the quotient — that is, what is the image of $R$ in $S/J$? Some elements of $R$ may already lie in $J$, so they collapse to zero; the rest survive. The theorem says the surviving image is the subring $(R + J)/J$, and — this is the content — it is isomorphic to $R$ with its own collapse divided out, namely $R/(R \cap J)$. The intersection $R \cap J$ is exactly "the part of $R$ that dies in $S/J$", and the theorem says: *the image of $R$ in the quotient is $R$ modulo the part of $R$ that dies.* That is intuitively obvious, and the theorem makes it precise and proves it.

There is also a purely structural payoff. The second isomorphism theorem lets you compute a quotient $(R+J)/J$ — which lives inside the possibly large and unfamiliar ring $S/J$ — by instead computing $R/(R \cap J)$, which lives entirely inside the subring $R$ you presumably understand better. It trades a quotient in a big ambient ring for a quotient in a small familiar one. A standard instance: in $\mathbb{Z}$, take $R = m\mathbb{Z}$ and $J = n\mathbb{Z}$. Then $R \cap J = \operatorname{lcm}(m,n)\mathbb{Z}$ and $R + J = \gcd(m,n)\mathbb{Z}$, and the theorem produces an isomorphism relating these — number-theoretic identities falling out of pure ring theory.

But the deepest thing about the second isomorphism theorem is *how it is proved*: it is not proved from scratch at all. It is the [[Thm - First Isomorphism Theorem for Rings|first isomorphism theorem]] applied to one specific, cleverly chosen homomorphism — the restriction to $R$ of the quotient map $S \to S/J$. Every clause of the statement is just the kernel, the image, or the conclusion of that single map. Recognising the second isomorphism theorem as "the first theorem in disguise" is the real lesson, and it is the template for the third theorem too.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "a subring $R$ and an ideal $J$ inside a common ring $S$". The source question is: when does a problem present this configuration, perhaps without naming it?

The first disguised source is **two ideals of the same ring**. If $I$ and $J$ are both ideals of $S$, then in particular $I$ is a *subring's worth of additive structure* — more usefully, the theorem applies with $R$ taken to be a subring containing $I$, but the cleanest instance is this: when $R$ is itself a subring and $J$ an ideal, $R + J$ is a subring and $R \cap J$ an ideal of $R$. The bridge to the theorem's hypotheses is recognising which of your two objects is the *ideal* (it must absorb multiplication by all of $S$) and which is merely the *subring*. The non-obvious part is that the roles are not symmetric: $R \cap J$ is an ideal of $R$ but generally not of $S$, and $R+J$ is a subring but $J$ alone need not sit inside $R$. *Example problem:* with $R = m\mathbb{Z}$ a subring-like additive object and $J = n\mathbb{Z}$ an ideal of $\mathbb{Z}$, identify $R/(R \cap J)$.

The second disguised source is **a subring together with a surjection of the ambient ring**. If you are given $R \leq S$ and *any* surjective homomorphism $\psi : S \twoheadrightarrow T$, then $J = \ker\psi$ is an ideal of $S$ and the theorem applies. So whenever a problem provides "a subring and a quotient of the big ring", the second isomorphism theorem computes how the subring fares under that quotient. The non-obvious step is to see the kernel of the given surjection *as* the ideal $J$ the theorem wants. *Example problem:* given a surjection $S \to T$ and a subring $R$ of $S$, describe the image of $R$ in $T$ as $R/(R \cap \ker\psi)$.

The third disguised source is **the desire to compute an awkward quotient $(R+J)/J$ in a large ring**. If a problem asks you to understand a subring of a quotient ring $S/J$ — specifically the subring generated by the image of some $R$ — the theorem says that subring *is* $(R+J)/J$ and is isomorphic to the friendlier $R/(R\cap J)$. The non-obviousness is that the awkward object $(R+J)/J$ is not approached directly; you instead recognise it as the conclusion of the theorem and replace it. *Example problem:* show that the image of $\mathbb{Z}[X]$ inside $\mathbb{Z}[X]/(X^2+1)$ under some specified inclusion is $\mathbb{Z}[X]/(\text{something})$.

**Targets (Output Amplification)**

The bare conclusion is $R/(R \cap J) \cong (R+J)/J$. Combined with other facts it does more.

Combine the conclusion with **finiteness and counting**. If $R$ is finite, then $|R/(R \cap J)| = |R|/|R \cap J|$, and the isomorphism forces $|(R+J)/J| = |R|/|R \cap J|$. The further result $E$ is an order formula: $|R + J| = |R| \cdot |J| / |R \cap J|$ when everything is finite — the ring-theoretic analogue of the inclusion–exclusion / product formula for subgroups. This is non-obvious because $R + J$ is not a direct product, yet its size factors as if it were, with $R \cap J$ as the correction.

Combine the conclusion with **a structural property of $R/(R \cap J)$**. Because the two sides are isomorphic, any property of $R/(R\cap J)$ transfers to $(R+J)/J$ and conversely. If $R \cap J$ is a maximal ideal of $R$, then $R/(R\cap J)$ is a field, so $(R+J)/J$ is a field — even though it sits inside the possibly complicated ring $S/J$. The further result is that you can certify a subring of a quotient as a field, or a domain, by checking a condition entirely within $R$. This is non-obvious because the field property is verified on the *small* side and exported to the *large* side.

Combine the conclusion with **the case $J \subseteq R$**. If the ideal $J$ happens to lie inside the subring $R$, then $R \cap J = J$ and $R + J = R$, so the theorem degenerates to $R/J \cong R/J$ — a tautology — but the *useful* reading is the converse: when you see $R/J$ with $J$ an ideal of a larger ring, you may freely re-express it as $(R+J')/J'$ for a larger ideal $J' \supseteq J$ in $S$, or shrink the ambient ring. The further result is a flexibility principle for rewriting quotients, and it is the bookkeeping that makes chained applications of the isomorphism theorems work.

---

# Why Is It True

Do not think about [[Def - Coset|cosets]] at first. Think about the quotient map $\pi : S \to S/J$, the homomorphism that crushes $J$ to zero and leaves everything else as a coset. Now restrict your attention to the subring $R$. The map $\pi$, looked at only on $R$, is a homomorphism $R \to S/J$ — call it $\theta$. The entire second isomorphism theorem is the first isomorphism theorem applied to this $\theta$, and "why is it true" is just "what are the kernel and image of $\theta$".

What does $\theta$ do? It takes $r \in R$ and returns the coset $r + J$. When is that the zero coset? Exactly when $r \in J$. But $r$ was already in $R$, so $r$ must be in *both* $R$ and $J$ — that is, $r \in R \cap J$. So the kernel of $\theta$ is $R \cap J$. This is the whole reason $R \cap J$ turns out to be an ideal of $R$: it is a *kernel*, and kernels are [[Def - Ideal|ideals]]. You did not have to check the ideal axioms by hand; they are automatic.

What is the image of $\theta$? It is the set of cosets $r + J$ as $r$ ranges over $R$ — which is precisely $(R+J)/J$. (A coset $r + J$ with $r \in R$ is the same as a coset $(r + j) + J$ for any $j \in J$, so "cosets with a representative in $R$" and "cosets with a representative in $R + J$" are the same set; that is why the image is written $(R+J)/J$ rather than $R/J$ — $R$ alone need not be a union of $J$-cosets, but $R + J$ is.) The image of a homomorphism is always a subring of the target, so $(R+J)/J$ is automatically a subring of $S/J$ — again, no axiom-checking.

Now the first isomorphism theorem says $\theta$ induces an isomorphism from $R$ modulo its kernel onto its image. Substituting what we found:
$$R/(R \cap J) \;\cong\; (R+J)/J.$$
Every clause of the theorem — "$R \cap J$ is an ideal", "$(R+J)/J$ is a subring", and the isomorphism itself — is one of the three outputs (kernel, image, induced map) of the *single* homomorphism $\theta = \pi|_R$. The intuition for the isomorphism is then the intuition for the first theorem: $\theta$ identifies two elements of $R$ exactly when they differ by something in $R \cap J$, so collapsing $R \cap J$ makes $\theta$ a perfect bijection onto what it can reach. The only genuinely new idea in the second isomorphism theorem is *which homomorphism to look at* — and that idea is "restrict the quotient map to the subring".

---

# What Makes This Hard

The proof is effortless once you see the trick — restrict the quotient map $\pi : S \to S/J$ to the subring $R$ — so the difficulty is entirely in *finding* that map rather than proving anything; students freeze because the theorem names no homomorphism and they do not realise they must build one. The non-obvious step is recognising that the awkward objects $R \cap J$ and $(R+J)/J$ are not things to verify from axioms but are simply the kernel and image of the restricted map, so their ideal/subring status is free. The most common error is asymmetry confusion: writing $R/J$ instead of $(R+J)/J$ for the image (wrong, because $R$ is generally not a union of $J$-cosets), or claiming $R \cap J$ is an ideal of $S$ rather than only of $R$.

---

# Rederivation Scaffold

**High-level strategy:**
Do not prove the three clauses separately and do not touch a coset by hand. Build one homomorphism — the quotient map $S \to S/J$ restricted to $R$ — and let the [[Thm - First Isomorphism Theorem for Rings|first isomorphism theorem]] produce all three clauses as its kernel, its image, and its induced isomorphism.

**Subgoal decomposition:**

1. **Build the map.** Define $\varphi : R \to S/J$ by $\varphi(r) = r + J$.
   - *Hint:* This is the composite $R \hookrightarrow S \twoheadrightarrow S/J$ — the inclusion followed by the canonical quotient map. A composite of ring [[Def - Homomorphism|homomorphisms]] is a ring homomorphism.
   - *Why needed:* This single map carries all the information; everything below is reading it off.

2. **Compute the kernel.** Show $\ker\varphi = R \cap J$.
   - *Hint:* $\varphi(r) = 0$ in $S/J$ means $r + J = J$, i.e. $r \in J$; combined with $r \in R$ this is $r \in R \cap J$.
   - *Why needed:* The first isomorphism theorem will then declare $R \cap J$ an ideal of $R$ for free.

3. **Compute the image.** Show $\operatorname{im}\varphi = (R+J)/J$.
   - *Hint:* The image is $\{r + J : r \in R\}$; since $r + J = (r+j) + J$ for any $j \in J$, this equals $\{x + J : x \in R + J\} = (R+J)/J$.
   - *Why needed:* The first isomorphism theorem will then declare $(R+J)/J$ a subring of $S/J$ for free.

4. **Apply the first isomorphism theorem.** Conclude $R/(R \cap J) \cong (R+J)/J$.
   - *Hint:* Substitute $\ker\varphi = R \cap J$ and $\operatorname{im}\varphi = (R+J)/J$ into $R/\ker\varphi \cong \operatorname{im}\varphi$.
   - *Why needed:* This is the isomorphism the theorem asserts; all three clauses are now established.

---

# Lemma Decomposition

> [!note]- Lemma 1: The restricted quotient map is a ring homomorphism
> **Statement:** Let $R \leq S$ be a subring and $J \trianglelefteq S$ an ideal. The map $\varphi : R \to S/J$, $\varphi(r) = r + J$, is a ring homomorphism.
>
> **Hint:** It is the composite of the inclusion $R \hookrightarrow S$ and the canonical quotient map $S \twoheadrightarrow S/J$; both are ring homomorphisms.
>
> **Why needed:** It is the one map the entire proof is built on; the kernel and image of this map are the theorem.
>
> > [!note]- Full proof
> > The inclusion $\iota : R \hookrightarrow S$, $\iota(r) = r$, is a ring homomorphism: it respects $+$ and $\times$ because $R$ is a subring with the operations inherited from $S$, and it sends $0_R \mapsto 0_S$, $1_R \mapsto 1_S$ because a subring shares the ambient zero and one. The canonical quotient map $\pi : S \to S/J$, $\pi(s) = s + J$, is a ring homomorphism by the construction of the [[Def - Quotient Ring|quotient ring]] (the quotient operations are defined precisely so that $\pi$ respects them, and $\pi(0_S) = 0_S + J$, $\pi(1_S) = 1_S + J$ are the zero and one of $S/J$). The composite $\varphi = \pi \circ \iota : R \to S/J$ is therefore a ring homomorphism, and explicitly $\varphi(r) = \pi(\iota(r)) = \pi(r) = r + J$.

> [!note]- Lemma 2: The kernel of the restricted map is $R \cap J$
> **Statement:** For $\varphi : R \to S/J$, $\varphi(r) = r + J$, the kernel is $\ker\varphi = R \cap J$.
>
> **Hint:** A coset $r + J$ is the zero of $S/J$ exactly when $r$ lies in $J$.
>
> **Why needed:** Feeding this into the first isomorphism theorem makes $R \cap J$ an ideal of $R$ automatically and supplies the denominator of the conclusion.
>
> > [!note]- Full proof
> > By definition, $\ker\varphi = \{r \in R : \varphi(r) = 0_{S/J}\}$. The zero of $S/J$ is the coset $0_S + J = J$. So $\varphi(r) = r + J$ equals the zero coset if and only if $r + J = J$, which holds if and only if $r \in J$. Hence
> > $$\ker\varphi = \{r \in R : r \in J\} = R \cap J.$$
> > In particular, since the kernel of a ring homomorphism is always an ideal of its domain (by Lemma 1 of [[Thm - First Isomorphism Theorem for Rings]]), $R \cap J$ is an ideal of $R$.

> [!note]- Lemma 3: The image of the restricted map is $(R+J)/J$
> **Statement:** For $\varphi : R \to S/J$, $\varphi(r) = r + J$, the image is $\operatorname{im}\varphi = (R+J)/J = \{x + J : x \in R + J\}$.
>
> **Hint:** The image is literally $\{r + J : r \in R\}$; show this set of cosets equals the set of cosets with a representative in $R + J$.
>
> **Why needed:** Feeding this into the first isomorphism theorem makes $(R+J)/J$ a subring of $S/J$ automatically and supplies the right-hand side of the conclusion.
>
> > [!note]- Full proof
> > By definition $\operatorname{im}\varphi = \{\varphi(r) : r \in R\} = \{r + J : r \in R\}$.
> >
> > ($\subseteq$) Each $r \in R$ also lies in $R + J$ (take $j = 0$), so every coset $r + J$ with $r \in R$ is a coset $x + J$ with $x = r \in R + J$. Hence $\operatorname{im}\varphi \subseteq (R+J)/J$.
> >
> > ($\supseteq$) Take a coset $x + J$ with $x \in R + J$, say $x = r + j$ for $r \in R$, $j \in J$. Then $x + J = (r + j) + J = r + J$, because $j \in J$. So $x + J = \varphi(r) \in \operatorname{im}\varphi$. Hence $(R+J)/J \subseteq \operatorname{im}\varphi$.
> >
> > Therefore $\operatorname{im}\varphi = (R+J)/J$. Since the image of a ring homomorphism is always a subring of its codomain, $(R+J)/J$ is a subring of $S/J$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $S$ be a ring, $R \leq S$ a subring, and $J \trianglelefteq S$ an ideal.
>
> **Step 1 — define the homomorphism.** Define
> $$\varphi : R \longrightarrow S/J, \qquad \varphi(r) = r + J.$$
> This is the composite $R \xhookrightarrow{\ \iota\ } S \xtwoheadrightarrow{\ \pi\ } S/J$ of the subring inclusion and the canonical quotient map. By Lemma 1 it is a ring homomorphism.
>
> **Step 2 — compute the kernel.** By Lemma 2, the zero of $S/J$ is the coset $J$, and $\varphi(r) = r + J = J$ holds exactly when $r \in J$; since $r \in R$ as well, this is $r \in R \cap J$. Hence
> $$\ker\varphi = R \cap J.$$
> Because the kernel of any ring homomorphism is an ideal of its domain, $R \cap J$ is an ideal of $R$. *(First clause proved.)*
>
> **Step 3 — compute the image.** By Lemma 3, $\operatorname{im}\varphi = \{r + J : r \in R\}$, and since $r + J = (r + j) + J$ for every $j \in J$, this set of cosets is exactly $\{x + J : x \in R + J\}$. Hence
> $$\operatorname{im}\varphi = (R + J)/J.$$
> Because the image of any ring homomorphism is a subring of its codomain, $(R+J)/J$ is a subring of $S/J$. *(Second clause proved.)*
>
> **Step 4 — apply the first isomorphism theorem.** By the [[Thm - First Isomorphism Theorem for Rings|first isomorphism theorem for rings]] applied to $\varphi$,
> $$R/\ker\varphi \;\cong\; \operatorname{im}\varphi.$$
> Substituting $\ker\varphi = R \cap J$ from Step 2 and $\operatorname{im}\varphi = (R+J)/J$ from Step 3,
> $$\frac{R}{R \cap J} \;\cong\; \frac{R + J}{J}. \qquad \blacksquare$$
> *(Third clause proved; all three clauses established.)*

---

# Cross-Field Exercise Suggestions

**The gcd–lcm identity in number theory.** Take $S = \mathbb{Z}$, the subring-style additive object $R = m\mathbb{Z}$, and the ideal $J = n\mathbb{Z}$. Then $R \cap J = \operatorname{lcm}(m,n)\mathbb{Z}$ (common multiples) and $R + J = \gcd(m,n)\mathbb{Z}$ (the ideal generated by $m$ and $n$). The second isomorphism theorem produces an isomorphism between $m\mathbb{Z}/\operatorname{lcm}(m,n)\mathbb{Z}$ and $\gcd(m,n)\mathbb{Z}/n\mathbb{Z}$; comparing cardinalities recovers $\gcd(m,n)\cdot\operatorname{lcm}(m,n) = mn$. This is non-obvious because a purely arithmetic identity is being produced by a structural ring theorem — the source property $B$ is "two ideals of $\mathbb{Z}$", and the recognition that $R + J$ is the gcd-ideal and $R \cap J$ the lcm-ideal is the whole step.

**Restriction of functions to a [[Def - Subspace|subspace]].** Let $S = C(X)$ be continuous real functions on a space $X$, let $J$ be the ideal of functions vanishing on a closed subset $Y \subseteq X$, and let $R$ be the subring of functions that are constant on each connected component (or any subring of interest). The image of $R$ in $S/J \cong C(Y)$ — the restrictions to $Y$ of functions in $R$ — is $(R+J)/J$, and the theorem identifies it with $R/(R \cap J)$, where $R \cap J$ is the functions in $R$ that already vanish on $Y$. The application is non-obvious because $S/J$ is an analytically defined function ring, yet the algebraic theorem still computes how a subring restricts.

**Comparing two extensions of a base ring.** Let $S$ contain a base ring $k$ and two further pieces: a subring $R$ generated by $k$ and one new element, and an ideal $J$. The theorem describes how $R$ projects into $S/J$ — useful when $S = k[X,Y]$, $R = k[X]$, and $J = (Y - X^2)$, where it shows the copy of $k[X]$ inside the coordinate ring of the parabola $Y = X^2$ is the *whole* coordinate ring, because $R + J = S$. The non-obvious recognition is that "is the image of $R$ all of $S/J$?" is the question "$R + J = S$?", which the second isomorphism theorem turns into an isomorphism statement about $R/(R \cap J)$.

**Image of a matrix subring under reduction.** Let $S = M_2(\mathbb{Z})$, let $J$ be the ideal of matrices with all entries divisible by $n$ (so $S/J \cong M_2(\mathbb{Z}/n\mathbb{Z})$), and let $R$ be the subring of upper-triangular integer matrices. The image of $R$ in $M_2(\mathbb{Z}/n\mathbb{Z})$ is $(R+J)/J$ — the upper-triangular matrices mod $n$ — and the theorem identifies it with $R/(R \cap J)$, where $R \cap J$ is upper-triangular matrices with entries divisible by $n$. The application is out-of-distribution because the ambient ring is noncommutative, yet the second isomorphism theorem applies unchanged — it never used commutativity.

---

# Bridges

- **[[Thm - First Isomorphism Theorem for Rings|First Isomorphism Theorem for Rings]]** — the parent. The second isomorphism theorem is not an independent result; it is the first theorem applied to the single homomorphism $R \hookrightarrow S \twoheadrightarrow S/J$. Its three clauses are exactly the kernel, the image, and the induced isomorphism of that map.

- **[[Thm - Third Isomorphism Theorem for Rings|Third Isomorphism Theorem for Rings]]** — the sibling. Both are corollaries of the first theorem obtained by choosing a clever homomorphism: the second restricts a quotient map to a *subring*, the third composes *two* quotient maps. Together with the second they exhaust the standard quotient manipulations.

- **[[Thm - Second Isomorphism Theorem|Second Isomorphism Theorem for Groups]]** — the prototype in another category. The group statement $H/(H \cap N) \cong HN/N$ for $H \leq G$ and $N \trianglelefteq G$ becomes the ring statement by replacing "subgroup" with "subring", "normal subgroup" with "ideal", and "$HN$" with "$R + J$" (the group product becomes the ring sum because the ambient operation in play is addition). The proof — restrict the quotient map to the substructure — is identical.

- **[[Thm - Ideal Correspondence|Ideal Correspondence]]** — a bookkeeping companion. When chaining isomorphism theorems, the ideal correspondence keeps track of which subsets of $S/J$ are ideals or subrings; the second theorem then identifies the quotient ring structure on those pieces.

---

# Unlocked by This

> [!tip] Order Formula for Finite Rings *(from Finite Ring Theory)*
> Taking cardinalities in $R/(R\cap J) \cong (R+J)/J$ yields $|R + J| = |R|\,|J|/|R \cap J|$ for finite rings — the additive-counting identity that underlies counting arguments for finite rings and modules.
