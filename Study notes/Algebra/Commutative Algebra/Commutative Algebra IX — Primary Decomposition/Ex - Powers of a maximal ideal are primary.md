---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Primary Ideal"
  - "Def - Prime and Maximal Ideal"
  - "Def - Radical of an Ideal and the Nilradical"
  - "Def - Local Ring and Residue Field"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $R$ be a ring and $\mathfrak{q} \subsetneq R$ an ideal whose [[Def - Radical of an Ideal and the Nilradical|radical]] $\sqrt{\mathfrak{q}} = \mathfrak{m}$ is a [[Def - Prime and Maximal Ideal|maximal]] ideal. Prove that $\mathfrak{q}$ is [[Def - Primary Ideal|primary]] (hence $\mathfrak{m}$-primary). Deduce that **every power $\mathfrak{m}^n$ ($n \geq 1$) of a maximal ideal is $\mathfrak{m}$-primary** (this is ES3.9(b)).

Contrast with the false converse: $\sqrt{\mathfrak{q}}$ being merely *prime* (not maximal) does **not** force $\mathfrak{q}$ primary — exhibit the standard counterexample $\mathfrak{p}^2$ in $k[X,Y,Z]/(XY - Z^2)$ where $\mathfrak{p} = (\bar X, \bar Z)$.

**Recall:**

The objects in play are primary ideals, maximal ideals, the radical, and the structure of $R/\mathfrak{q}$ as a local ring.

![[Def - Primary Ideal#The Definition]]

![[Def - Prime and Maximal Ideal#The Definition]]

A [[Def - Prime and Maximal Ideal|maximal]] ideal $\mathfrak{m}$ is one with $R/\mathfrak{m}$ a [[Def - Unit and Field|field]]. The radical satisfies $\sqrt{\mathfrak{m}^n} = \mathfrak{m}$ for all $n \geq 1$, since $\sqrt{I^n} = \sqrt{I}$. A ring is [[Def - Local Ring and Residue Field|local]] if it has a unique maximal ideal; in a local ring every non-unit lies in the maximal ideal.

The key structural fact: $\sqrt{\mathfrak{q}} = \mathfrak{m}$ maximal means $R/\mathfrak{q}$ has a unique prime ideal $\mathfrak{m}/\mathfrak{q}$, which is therefore both maximal and the nilradical — so $R/\mathfrak{q}$ is a local ring whose maximal ideal is nilpotent.

---

# Convergent Strategy

**Problem class.** This is a *certify-primariness* problem solved by the cheapest available route — the maximal-radical shortcut. As the [[Commutative Algebra IX — Primary Decomposition#Problem-Solving Strategy|topic page strategy]] records, the first thing to try when asked "is $\mathfrak{q}$ primary?" is "is $\sqrt{\mathfrak{q}}$ maximal?", because a maximal radical removes the zero-divisor check entirely.

**Assumption pattern.** The single hypothesis "$\sqrt{\mathfrak{q}} = \mathfrak{m}$ maximal" is doing all the work. It forces $R/\mathfrak{q}$ to be a [[Def - Local Ring and Residue Field|local ring]] with a *nilpotent* maximal ideal — because the unique prime of $R/\mathfrak{q}$ is simultaneously its maximal ideal and its nilradical. The recognisable trigger is "the radical is a maximal ideal", which should immediately suggest "the quotient is local with nilpotent maximal ideal, so every non-unit is nilpotent".

**Theorem routing.** The route is: from $\sqrt{\mathfrak{q}} = \mathfrak{m}$ maximal, show the *only* prime of $R/\mathfrak{q}$ is $\bar{\mathfrak{m}} = \mathfrak{m}/\mathfrak{q}$; deduce $R/\mathfrak{q}$ is local with maximal ideal $\bar{\mathfrak{m}}$, and that $\bar{\mathfrak{m}} = \operatorname{nil}(R/\mathfrak{q})$ (the nilradical is the intersection of all primes, here just $\bar{\mathfrak{m}}$); conclude every non-unit of $R/\mathfrak{q}$ is nilpotent; since every zero-divisor is a non-unit, every zero-divisor is nilpotent — which is exactly primariness. The deduction for $\mathfrak{m}^n$ is immediate from $\sqrt{\mathfrak{m}^n} = \mathfrak{m}$.

**Key decision point.** The non-obvious step is recognising that *non-unit equals nilpotent* in $R/\mathfrak{q}$ — this is what collapses the primary condition. The genuine insight is that "$\sqrt{\mathfrak{q}}$ maximal" forces the nilradical and the maximal ideal of $R/\mathfrak{q}$ to *coincide*, so the (always true) "nilpotents are non-units" reverses to "non-units are nilpotents". The natural alternative — checking the primary condition $xy \in \mathfrak{q} \Rightarrow x \in \mathfrak{q}$ or $y \in \sqrt{\mathfrak{q}}$ directly — works but is more laborious; the structural shortcut is the point.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra IX — Primary Decomposition#Legal Operations|the topic page's Legal Operations]]:

1. **Pass to the quotient and read off the definition (operation 1).** Translate "is $\mathfrak{q}$ primary?" into "are all zero-divisors of $R/\mathfrak{q}$ nilpotent?", then study the ring $R/\mathfrak{q}$.

2. **Upgrade to primary via a maximal radical (operation 4).** This *is* the operation being justified: $\sqrt{\mathfrak{q}}$ maximal $\Rightarrow$ $\mathfrak{q}$ primary. The exercise proves the operation.

3. **Take radicals to find the attached prime (operation 2).** Compute $\sqrt{\mathfrak{m}^n} = \mathfrak{m}$ to conclude $\mathfrak{m}^n$ is $\mathfrak{m}$-primary.

4. **Pass between $R/\mathfrak{q}$ and its nilradical.** Identify $\operatorname{nil}(R/\mathfrak{q})$ as the intersection of all primes, which here is the single prime $\bar{\mathfrak{m}}$.

---

# Hints

> [!note]- Hint 1
> Work in $R/\mathfrak{q}$. You want every zero-divisor there to be nilpotent. A zero-divisor is in particular a non-unit. So it would suffice to show: *every non-unit of $R/\mathfrak{q}$ is nilpotent.* When is that true? When the maximal ideal and the nilradical coincide.

> [!note]- Hint 2
> The radical $\sqrt{\mathfrak{q}} = \mathfrak{m}$ corresponds, in $R/\mathfrak{q}$, to the nilradical $\operatorname{nil}(R/\mathfrak{q}) = \mathfrak{m}/\mathfrak{q}$ (the radical of $(0)$ in the quotient). And $\mathfrak{m}$ is maximal, so $\mathfrak{m}/\mathfrak{q}$ is a maximal ideal of $R/\mathfrak{q}$. Now use: the primes of $R/\mathfrak{q}$ are the primes of $R$ containing $\mathfrak{q}$, all of which contain $\sqrt{\mathfrak{q}} = \mathfrak{m}$, hence equal $\mathfrak{m}$. So $R/\mathfrak{q}$ has a *unique* prime.

> [!note]- Hint 3
> A ring with a unique prime ideal $\bar{\mathfrak{m}}$ is local, and that prime is both its maximal ideal *and* its nilradical (the nilradical is the intersection of all primes $= \bar{\mathfrak{m}}$). So every element of $\bar{\mathfrak{m}}$ is nilpotent, and every element outside $\bar{\mathfrak{m}}$ is a unit. Every non-unit is therefore nilpotent — and every zero-divisor is a non-unit.

> [!note]- Hint 4
> For the powers: $\sqrt{\mathfrak{m}^n} = \mathfrak{m}$ because $\sqrt{I^n} = \sqrt{I}$ in general, and $\mathfrak{m}$ is maximal, so the first part applies directly to $\mathfrak{q} = \mathfrak{m}^n$. For the counterexample, note the cone relation $\bar X \bar Y = \bar Z^2 \in \mathfrak{p}^2$ gives a zero-divisor $\bar Y$ of $R/\mathfrak{p}^2$ that is not nilpotent (its radical $\sqrt{\mathfrak{p}^2} = \mathfrak{p}$ is only *prime*, not maximal — so the shortcut does not apply).

---

# Solution

The proof is one structural observation: when $\sqrt{\mathfrak{q}} = \mathfrak{m}$ is maximal, the quotient $R/\mathfrak{q}$ is a local ring whose maximal ideal equals its nilradical, so every non-unit is nilpotent — and since every zero-divisor is a non-unit, every zero-divisor is nilpotent, which is primariness. The deduction for $\mathfrak{m}^n$ is then a one-liner via $\sqrt{\mathfrak{m}^n} = \mathfrak{m}$. The counterexample shows the hypothesis "maximal" cannot be weakened to "prime".

**Step 1: $R/\mathfrak{q}$ has a unique prime ideal, namely $\bar{\mathfrak{m}} = \mathfrak{m}/\mathfrak{q}$.**

Every prime of $R/\mathfrak{q}$ pulls back to a prime of $R$ containing $\mathfrak{q}$, hence containing $\sqrt{\mathfrak{q}} = \mathfrak{m}$, hence equal to $\mathfrak{m}$.

> [!note]- Derivation
> Primes of $R/\mathfrak{q}$ correspond to primes $\mathfrak{P}$ of $R$ with $\mathfrak{q} \subseteq \mathfrak{P}$. Any such $\mathfrak{P}$ is in particular a radical ideal containing $\mathfrak{q}$, so $\mathfrak{P} = \sqrt{\mathfrak{P}} \supseteq \sqrt{\mathfrak{q}} = \mathfrak{m}$. But $\mathfrak{m}$ is [[Def - Prime and Maximal Ideal|maximal]] and $\mathfrak{P} \neq R$ (it is prime), so $\mathfrak{m} \subseteq \mathfrak{P} \subsetneq R$ forces $\mathfrak{P} = \mathfrak{m}$. Hence the only prime of $R$ containing $\mathfrak{q}$ is $\mathfrak{m}$, so $R/\mathfrak{q}$ has the unique prime $\bar{\mathfrak{m}} = \mathfrak{m}/\mathfrak{q}$.

**Step 2: In $R/\mathfrak{q}$, every non-unit is nilpotent.**

The unique prime $\bar{\mathfrak{m}}$ is simultaneously the maximal ideal and the nilradical of $R/\mathfrak{q}$; so non-units (which lie in $\bar{\mathfrak{m}}$) are nilpotent.

> [!note]- Derivation
> A ring with a unique prime ideal is [[Def - Local Ring and Residue Field|local]]: $\bar{\mathfrak{m}}$ is the unique prime, hence the unique maximal ideal, and every non-unit lies in some maximal ideal, hence in $\bar{\mathfrak{m}}$. The nilradical of any ring is the intersection of all its prime ideals; here that intersection is the single prime $\bar{\mathfrak{m}}$, so $\operatorname{nil}(R/\mathfrak{q}) = \bar{\mathfrak{m}}$. Therefore every element of $\bar{\mathfrak{m}}$ is nilpotent. Since every non-unit of $R/\mathfrak{q}$ lies in $\bar{\mathfrak{m}}$, every non-unit is nilpotent.

**Step 3: $\mathfrak{q}$ is $\mathfrak{m}$-primary.**

Every zero-divisor of $R/\mathfrak{q}$ is a non-unit, hence nilpotent; that is the definition of primary, and $\sqrt{\mathfrak{q}} = \mathfrak{m}$ gives $\mathfrak{m}$-primary.

> [!note]- Derivation
> Let $\bar a \in R/\mathfrak{q}$ be a zero-divisor: $\bar a \neq 0$ and $\bar a \bar b = 0$ for some $\bar b \neq 0$. Then $\bar a$ is not a unit (a unit times a nonzero element is nonzero). By Step 2, $\bar a$ is nilpotent. So every zero-divisor of $R/\mathfrak{q}$ is nilpotent, which is exactly the definition of $\mathfrak{q}$ being [[Def - Primary Ideal|primary]]. Its radical is $\sqrt{\mathfrak{q}} = \mathfrak{m}$, so $\mathfrak{q}$ is $\mathfrak{m}$-primary. (Also $R/\mathfrak{q} \neq 0$ since $\mathfrak{q} \subsetneq R$.)

**Step 4: Every power $\mathfrak{m}^n$ is $\mathfrak{m}$-primary.**

Since $\sqrt{\mathfrak{m}^n} = \mathfrak{m}$ is maximal, Steps 1–3 apply to $\mathfrak{q} = \mathfrak{m}^n$.

> [!note]- Derivation
> For any ideal $I$ and $n \geq 1$, $\sqrt{I^n} = \sqrt{I}$ (if $x^k \in I^n$ then $x^k \in I$ so $x \in \sqrt I$; conversely $x \in \sqrt I \Rightarrow x^k \in I \Rightarrow x^{kn} \in I^n$). Applying this to $I = \mathfrak{m}$: $\sqrt{\mathfrak{m}^n} = \mathfrak{m}$, which is maximal. By the result just proved, $\mathfrak{m}^n$ is $\mathfrak{m}$-primary, for every $n \geq 1$. In particular $(p^n) \subseteq \mathbb{Z}$ is $(p)$-primary, recovering the prime-power ideals of $\mathbb{Z}$.

**Step 5: The converse fails — $\sqrt{\mathfrak{q}}$ prime is not enough.**

In $R = k[X,Y,Z]/(XY - Z^2)$, $\mathfrak{p} = (\bar X, \bar Z)$ is prime but $\mathfrak{p}^2$ is not primary.

> [!note]- Derivation
> $\mathfrak{p} = (\bar X, \bar Z)$ is prime since $R/\mathfrak{p} \cong k[Y]$ is a domain; so $\sqrt{\mathfrak{p}^2} = \mathfrak{p}$ is *prime but not maximal* (it is properly contained in $(\bar X, \bar Y, \bar Z)$). The shortcut does not apply, and indeed $\mathfrak{p}^2$ fails to be primary: the cone relation gives $\bar X \bar Y = \bar Z^2 \in \mathfrak{p}^2$, yet $\bar X \notin \mathfrak{p}^2$ (it has degree $1$, while $\mathfrak{p}^2 = (\bar X^2, \bar X \bar Z, \bar Z^2)$ is generated in degree $2$) and $\bar Y \notin \sqrt{\mathfrak{p}^2} = \mathfrak{p}$ (since $\bar Y$ does not vanish in $R/\mathfrak{p} \cong k[Y]$). So $\bar Y$ is a non-nilpotent zero-divisor of $R/\mathfrak{p}^2$, breaking primariness. (Full treatment in [[Ex - A primary ideal need not be a prime power]].) The lesson: "$\sqrt{\mathfrak{q}}$ maximal" is genuinely stronger than "$\sqrt{\mathfrak{q}}$ prime", and only the former forces primariness.

> [!note]- Complete formal solution
> **Claim.** If $\sqrt{\mathfrak{q}} = \mathfrak{m}$ is maximal then $\mathfrak{q}$ is $\mathfrak{m}$-primary; in particular each $\mathfrak{m}^n$ is $\mathfrak{m}$-primary.
>
> Every prime of $R$ containing $\mathfrak{q}$ contains $\sqrt{\mathfrak{q}} = \mathfrak{m}$, hence equals $\mathfrak{m}$ (maximality). So $R/\mathfrak{q}$ has a unique prime $\bar{\mathfrak{m}} = \mathfrak{m}/\mathfrak{q}$, which is therefore both its maximal ideal and its nilradical (the latter being the intersection of all primes). Thus every non-unit of $R/\mathfrak{q}$ lies in $\bar{\mathfrak{m}}$ and is nilpotent. Any zero-divisor is a non-unit, hence nilpotent; so $\mathfrak{q}$ is primary, and $\sqrt{\mathfrak{q}} = \mathfrak{m}$ makes it $\mathfrak{m}$-primary.
>
> Since $\sqrt{\mathfrak{m}^n} = \sqrt{\mathfrak{m}} = \mathfrak{m}$ is maximal, the above applies to $\mathfrak{q} = \mathfrak{m}^n$, so every power of a maximal ideal is $\mathfrak{m}$-primary.
>
> *The hypothesis is sharp.* In $k[X,Y,Z]/(XY-Z^2)$ with $\mathfrak{p} = (\bar X, \bar Z)$ prime, $\sqrt{\mathfrak{p}^2} = \mathfrak{p}$ is prime but not maximal, and $\mathfrak{p}^2$ is not primary: $\bar X \bar Y = \bar Z^2 \in \mathfrak{p}^2$ with $\bar X \notin \mathfrak{p}^2$ and $\bar Y \notin \mathfrak{p}$. $\blacksquare$

---

# Key Takeaways

**The maximal-radical shortcut is the cheapest test for primariness, and you should reach for it first.** Whenever a problem asks whether an ideal $\mathfrak{q}$ is primary, the very first thing to compute is $\sqrt{\mathfrak{q}}$; if it turns out to be a *maximal* ideal, you are done — no zero-divisor analysis required. The reason is structural and worth internalising as a unit: a maximal radical forces $R/\mathfrak{q}$ to be a local ring whose maximal ideal *is* its nilradical, collapsing "non-unit" and "nilpotent" into the same thing. The trigger to recognise: the radical is a maximal ideal (equivalently, $R/\mathfrak{q}$ has a single prime, equivalently $R/\mathfrak{q}$ is local Artinian, equivalently $\dim R/\mathfrak{q} = 0$ at that point). This covers the most common primary ideals in practice — every $\mathfrak{m}^n$, every $\mathbb{Z}/(p^n)$, every ideal supported at a single closed point — so it is the workhorse of decomposition computations, where the embedded components are almost always supported at maximal ideals.

**"Non-unit equals nilpotent" is the signature of a local Artinian ring, and it is what makes primariness automatic.** The collapse at the heart of this proof — every non-unit of $R/\mathfrak{q}$ is nilpotent — happens exactly when the nilradical and the maximal ideal coincide, i.e. when the ring has a single prime. This is the defining feature of a zero-dimensional local ring (local Artinian ring), and it is worth recognising in its own right: in such a ring, the only obstruction to being a field is nilpotents, and every proper ideal is primary. The transferable diagnostic: if you can show a quotient ring has a unique prime, you have shown the original ideal is primary, and more — you have shown the quotient is a "fat point", a single point with nilpotent thickening. This recurs in dimension theory (Artinian $\iff$ Noetherian of dimension zero) and in deformation theory (the local Artinian rings are the test objects).

**The hypothesis "maximal" cannot be weakened to "prime", and the cone is the canonical witness.** It is tempting to hope that $\sqrt{\mathfrak{q}}$ prime already forces $\mathfrak{q}$ primary — after all, $\sqrt{\mathfrak{q}}$ prime is what we expect of a primary ideal. But primariness is genuinely stronger than "prime radical", and the gap is exactly the difference between maximal and merely-prime radicals. When $\sqrt{\mathfrak{q}} = \mathfrak{p}$ is prime but not maximal, $R/\mathfrak{q}$ has dimension $\geq 1$, so it has non-units that are not nilpotent (the non-zero-divisors that survive into the higher-dimensional quotient), and these can be zero-divisors when the geometry is singular. The cone $XY = Z^2$ is the standard counterexample because its singularity at the origin is precisely what injects the extra zero-divisor $\bar Y$. The lesson for spaced practice: the shortcut applies *only* at maximal radicals; at prime-but-not-maximal radicals you must check primariness honestly, and it often fails — which is exactly why symbolic powers $\mathfrak{p}^{(n)}$ (the primary part of $\mathfrak{p}^n$) are needed in higher dimension. See [[Ex - A primary ideal need not be a prime power]] for the full counterexample, and [[Def - Primary Ideal]] for the prime-vs-maximal distinction.
