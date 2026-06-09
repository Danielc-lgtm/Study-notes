---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Finitely Generated Module"
  - "Def - Module Homomorphism"
  - "Def - Polynomial Ring"
  - "Thm - Cayley-Hamilton for Modules (Determinant Trick)"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $R$ be a ring, $M$ a [[Def - Finitely Generated Module|finitely generated]] $R$-module, and $\varphi : M \to M$ an $R$-module endomorphism. Prove:

(i) If $\varphi$ is **surjective**, then $\varphi$ is **injective** (hence an isomorphism).

(ii) The reverse implication fails: an injective endomorphism of a finitely generated module need not be surjective.

(iii) The finite-generation hypothesis in (i) is necessary: there is a non-finitely-generated module with a surjective non-injective endomorphism.

*Hint (Becker).* For (i), make $M$ into an $R[T]$-module by letting $T$ act as $\varphi$.

(This is Becker Example Sheet 3, Q1(e).)

**Recall:**

The objects in play are a finitely generated module, an endomorphism, the polynomial-ring action, and the determinant trick (Cayley–Hamilton for modules).

![[Def - Finitely Generated Module#The Definition]]

A [[Def - Module Homomorphism|module endomorphism]] $\varphi : M \to M$ is $R$-linear; *surjective* means $\varphi(M) = M$, *injective* means $\ker\varphi = 0$.

To let $T$ act as $\varphi$ is to make $M$ a module over the [[Def - Polynomial Ring|polynomial ring]] $R[T]$ via $p(T)\cdot m = p(\varphi)(m)$; this is well-defined because $R[T]$ is free on one generator, so any choice of image for $T$ extends to an $R$-algebra map $R[T] \to \operatorname{End}_R(M)$.

The key tool — the determinant trick:

![[Thm - Cayley-Hamilton for Modules (Determinant Trick)#Statement]]

---

# Convergent Strategy

**Problem class.** This is a *promote-surjectivity-to-injectivity* problem — the chapter's most surprising application, proving something that looks like it needs finite *dimension* using only finite *generation*. The [[Commutative Algebra V — Nakayama's Lemma#Problem-Solving Strategy|topic strategy]] flags the route: an endomorphism or self-surjection feeds into the determinant trick via the $R[T]$-module construction.

**Assumption pattern.** The recognisable trigger is "$\varphi : M \to M$ surjective endomorphism of a finitely generated module". This is the disguised source for [[Thm - Cayley-Hamilton for Modules (Determinant Trick)|Cayley–Hamilton]]: letting $T$ act as $\varphi$ turns surjectivity into the ideal condition $(T)M = M$, i.e. $\varphi(M) = M = (T)M \subseteq (T)M$, so the trick applies over $R[T]$ with $\mathfrak a = (T)$.

**Theorem routing.** Make $M$ an $R[T]$-module with $T \cdot m = \varphi(m)$. Surjectivity gives $\varphi(M) = M$, i.e. $T M = M$, so $(T)M = M$. By the determinant trick (over $R[T]$, with $f = \operatorname{id}_M$ and $\mathfrak a = (T)$), there is $g(T) \in (T)$ with $(1 - g(T))\operatorname{id}_M = 0$, i.e. $g(\varphi) = \operatorname{id}_M$ with $g(T) = T h(T)$. Then $\varphi \circ h(\varphi) = \operatorname{id}_M$, exhibiting a two-sided inverse, so $\varphi$ is injective.

**Key decision point.** The non-obvious move is **letting $T$ act as $\varphi$**, manufacturing an ideal $(T)$ out of a bare endomorphism that mentions no ideal. The natural alternative — trying to prove $\ker\varphi = 0$ directly by chasing elements — fails because there is no traction without a relation satisfied by $\varphi$. The $R[T]$ trick produces exactly such a relation (a polynomial in $\varphi$ equalling the identity), from which the inverse is read off. The factored form $g(T) = T h(T)$ is the punchline: every coefficient of $g$ lies in $(T)$, so $g(T) = T \cdot h(T)$, and $g(\varphi) = \varphi h(\varphi) = \operatorname{id}$.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra V — Nakayama's Lemma#Legal Operations|the topic page's Legal Operations]]:

1. **Make $M$ into an $R[T]$-module by letting $T$ act as $\varphi$** (operation 3'). This is the manoeuvre that creates the ideal $(T)$ from the endomorphism.

2. **Write the action as a matrix over the ideal** (operation 1) and **specialise Cayley–Hamilton** (operation 3): with $f = \operatorname{id}$ and $\mathfrak a = (T)$, the trick yields $(1 - g(T))\operatorname{id} = 0$ with $g(T) \in (T)$.

3. **Read off the inverse from the factored relation.** Since $g(T) = T h(T)$, the relation $g(\varphi) = \operatorname{id}$ becomes $\varphi h(\varphi) = \operatorname{id}$ — a two-sided inverse.

---

# Hints

> [!note]- Hint 1
> A bare endomorphism $\varphi$ satisfies no obvious algebraic relation. To get one, give yourself an indeterminate: make $M$ a module over $R[T]$ by letting $T$ act as $\varphi$. Surjectivity of $\varphi$ now says $T M = M$. What ideal $\mathfrak a$ of $R[T]$ has $\mathfrak a M = M$?

> [!note]- Hint 2
> $(T)M = M$. Apply the determinant trick over $R[T]$ with the ideal $\mathfrak a = (T)$ to the identity map (or to $\varphi$). You get a relation $(1 - g(T))\operatorname{id}_M = 0$ where every coefficient of $g(T)$ lies in $(T)$ — so $g(T) = T h(T)$ for some $h(T) \in R[T]$.

> [!note]- Hint 3
> Translate $(1 - g(T))\operatorname{id}_M = 0$ back to endomorphisms: $g(\varphi) = \operatorname{id}_M$. Since $g(T) = T h(T)$, this is $\varphi \circ h(\varphi) = \operatorname{id}_M$. An endomorphism with a right inverse on a module... and the inverse commutes with it, so it is also a left inverse. Conclude $\varphi$ is injective.

> [!note]- Hint 4
> For (ii), look at $\varphi$, multiplication by $2$, on $M = \mathbb Z$: injective, not surjective. For (iii), drop finite generation: the left shift on $M = \bigoplus_{n \geq 0} k$ (or $k[T]$, shifting coefficients down) is surjective but kills the bottom coordinate, so it is not injective.

---

# Solution

The proof of (i) is the determinant trick in its sharpest form. Make $M$ an $R[T]$-module with $T$ acting as $\varphi$; surjectivity becomes $(T)M = M$; Cayley–Hamilton produces a polynomial relation that factors to exhibit an explicit inverse of $\varphi$. Parts (ii) and (iii) are one-line counterexamples isolating the two ways the statement is sharp.

**Step 1: Make $M$ an $R[T]$-module and rewrite surjectivity as $(T)M = M$.**

Letting $T$ act as $\varphi$, surjectivity of $\varphi$ is the statement $(T)\cdot M = M$ over $R[T]$.

> [!note]- Derivation
> Define an $R[T]$-module structure on $M$ by $T \cdot m := \varphi(m)$, extended to $p(T) \cdot m := p(\varphi)(m)$ for $p(T) \in R[T]$. This is well-defined: $R[T]$ is the free $R$-algebra on one generator, so the assignment $T \mapsto \varphi \in \operatorname{End}_R(M)$ extends uniquely to an $R$-algebra homomorphism $R[T] \to \operatorname{End}_R(M)$, making $M$ an $R[T]$-module.
>
> $M$ is finitely generated over $R$, hence over $R[T]$ (the same generators work). Now $\varphi$ surjective means $\varphi(M) = M$, i.e. $T M = M$. The ideal $(T) \trianglelefteq R[T]$ satisfies $(T) M = T M = M$, so
> $$(T)\, M = M.$$

**Step 2: Apply the determinant trick with $\mathfrak a = (T)$ to get $g(\varphi) = \operatorname{id}_M$ with $g(T) \in (T)$.**

Cayley–Hamilton (applied to $\operatorname{id}_M$, with $(T) M = M \supseteq \operatorname{id}_M(M)$) gives $(1 - g(T))\operatorname{id}_M = 0$, i.e. $g(\varphi) = \operatorname{id}_M$, with $g(T) \in (T)$.

> [!note]- Derivation
> Apply [[Thm - Cayley-Hamilton for Modules (Determinant Trick)|the determinant trick]] over the ring $R[T]$, to the endomorphism $f = \operatorname{id}_M$ and the ideal $\mathfrak a = (T)$. The hypothesis is met: $\operatorname{id}_M(M) = M = (T)M \subseteq (T)M$. The trick yields $a_1,\dots,a_n \in (T)$ with
> $$\operatorname{id}_M^{\,n} + a_1 \operatorname{id}_M^{\,n-1} + \dots + a_n \operatorname{id}_M = 0 \quad\text{in } \operatorname{End}_{R[T]}(M),$$
> i.e. $(1 + a_1 + \dots + a_n)\operatorname{id}_M = 0$. Set $g(T) = -(a_1 + \dots + a_n) \in (T)$; then $(1 - g(T))\operatorname{id}_M = 0$, meaning $1 - g(T)$ acts as the zero endomorphism, i.e. $g(T)$ acts as the identity:
> $$g(\varphi) = \operatorname{id}_M.$$
> Since every $a_i \in (T)$ and $(T)$ is an ideal, $g(T) \in (T)$, so $g(T) = T\, h(T)$ for some $h(T) \in R[T]$.

**Step 3: Read off the inverse and conclude $\varphi$ is injective.**

From $g(T) = T h(T)$, the relation $g(\varphi) = \operatorname{id}_M$ is $\varphi \circ h(\varphi) = \operatorname{id}_M$; since $h(\varphi)$ commutes with $\varphi$, it is a two-sided inverse, so $\varphi$ is bijective.

> [!note]- Derivation
> Write $g(T) = T h(T)$. Acting on $M$, $g(\varphi) = \varphi \circ h(\varphi) = h(\varphi) \circ \varphi$ (powers of $\varphi$ commute with $\varphi$, and $h(\varphi)$ is a polynomial in $\varphi$). The relation $g(\varphi) = \operatorname{id}_M$ becomes
> $$\varphi \circ h(\varphi) = h(\varphi) \circ \varphi = \operatorname{id}_M.$$
> Thus $h(\varphi)$ is a two-sided inverse of $\varphi$, so $\varphi$ is an isomorphism; in particular it is injective. $\blacksquare$

**Step 4: Counterexamples for (ii) and (iii).**

Injective need not imply surjective; and dropping finite generation breaks (i).

> [!note]- Derivation
> *(ii) Injective $\not\Rightarrow$ surjective.* Take $R = \mathbb Z$, $M = \mathbb Z$, and $\varphi(x) = 2x$. This is an injective $\mathbb Z$-module endomorphism ($2x = 0 \Rightarrow x = 0$), but it is not surjective ($1$ is not in the image, since $\tfrac12 \notin \mathbb Z$). $M = \mathbb Z$ is finitely generated, so the failure of the converse is genuine, not an artefact of infinite generation.
>
> *(iii) Finite generation is necessary in (i).* Take $R = k$ a field and $M = \bigoplus_{n \geq 0} k = k^{(\mathbb N)}$, an infinite-rank free module (not finitely generated). Let $\varphi$ be the *left shift* $\varphi(a_0, a_1, a_2, \dots) = (a_1, a_2, a_3, \dots)$. Then $\varphi$ is surjective (every sequence is the shift of one with an arbitrary new first coordinate), but $\varphi(1,0,0,\dots) = 0$, so $\varphi$ is not injective. Equivalently, on $M = k[T]$, the map "differentiate-and-drop" or "divide by $T$ and discard the constant term" is surjective but not injective. This shows (i) genuinely requires finite generation.

> [!note]- Complete formal solution
> **Claim.** A surjective endomorphism $\varphi$ of a finitely generated $R$-module $M$ is injective; the converse fails; and finite generation is necessary.
>
> *(i)* Make $M$ an $R[T]$-module via $T \cdot m = \varphi(m)$. Surjectivity gives $T M = M$, so $(T) M = M$. By the determinant trick (with $f = \operatorname{id}_M$, $\mathfrak a = (T)$, over $R[T]$), $(1 - g(T))\operatorname{id}_M = 0$ for some $g(T) \in (T)$, i.e. $g(\varphi) = \operatorname{id}_M$. Writing $g(T) = T h(T)$, this is $\varphi h(\varphi) = h(\varphi)\varphi = \operatorname{id}_M$, so $\varphi$ is invertible, hence injective.
>
> *(ii)* $\varphi(x) = 2x$ on $M = \mathbb Z$ is injective but not surjective.
>
> *(iii)* The left shift on $M = \bigoplus_{n\geq 0} k$ is surjective but not injective; $M$ is not finitely generated. $\blacksquare$

---

# Key Takeaways

**"Surjective endomorphism of a finitely generated module" should fire "let $T$ act as $\varphi$, then Cayley–Hamilton".** This is the chapter's signature trigger-reaction, and its surprise is that it proves a finite-*dimensional*-feeling fact (a surjective linear self-map is injective) using only finite *generation*. The mechanism: the bare endomorphism has no ideal to grip, so you *manufacture* one by letting an indeterminate $T$ act as $\varphi$; surjectivity becomes $(T)M = M$; the determinant trick spits out a polynomial relation $g(\varphi) = \operatorname{id}$; and because $g(T)$ is divisible by $T$, factoring out the $T$ exhibits $\varphi$'s inverse explicitly. Internalise the whole arc as one move. It generalises far beyond modules — the same "act by $T$, then find a monic relation" idea proves that integral elements satisfy monic equations and underlies the entire theory of integral extensions.

**The inverse is explicit, not abstract: it is a polynomial in $\varphi$.** A subtle but reusable point is that the proof does not merely assert an inverse exists — it constructs $\varphi^{-1} = h(\varphi)$ as a polynomial in $\varphi$ itself. This is why the inverse automatically commutes with $\varphi$ (so a right inverse is also a left inverse) and why the argument works over a noncommutative endomorphism ring with no division. The diagnostic for spaced practice: when the determinant trick gives a relation $g(\varphi) = \operatorname{id}$ with $g(0) = 0$, the inverse is $h(\varphi)$ where $g(T) = T h(T)$. Watch for the constant term: it is the divisibility by $T$ (equivalently, $g$ has no constant term) that makes the factorisation possible, and it comes precisely from the coefficients lying in $(T)$.

**The two sharpness counterexamples isolate the two hypotheses, and both are necessary.** The statement "surjective $\Rightarrow$ injective" is sharp in exactly two ways, and a complete answer must exhibit both. *Injective $\Rightarrow$ surjective is false* even with finite generation — multiplication by $2$ on $\mathbb Z$ — because the determinant trick only sees surjectivity as the input $(T)M = M$; there is no symmetric statement. *Finite generation cannot be dropped* — the left shift on an infinite-rank free module is surjective but not injective — because without a finite generating set there is no finite matrix to take a determinant of, and the module can absorb the kernel into its infinitely many coordinates. The general lesson: an asymmetry in a theorem ("surjective gives injective but not conversely") usually traces to an asymmetry in the proof mechanism, and the standard way to break a finiteness-dependent result is to exhibit an infinite-rank module where the relevant operator shifts coordinates. Compare [[Ex - A module with mM equal to M that is nonzero]], the analogous counterexample isolating finite generation in Nakayama itself.
