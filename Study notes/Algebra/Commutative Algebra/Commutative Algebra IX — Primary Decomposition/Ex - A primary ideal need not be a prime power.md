---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Primary Ideal"
  - "Def - Prime and Maximal Ideal"
  - "Def - Radical of an Ideal and the Nilradical"
  - "Def - Quotient Ring"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Sever the naive identification "primary $=$ prime power" in *both* directions, using $k$ a field throughout.

**Part (a) — a primary ideal that is not a prime power.** Let $R = k[X,Y]$ and $\mathfrak{q} = (X, Y^2)$. Show $\mathfrak{q}$ is [[Def - Primary Ideal|primary]] (indeed $(X,Y)$-primary), but $\mathfrak{q}$ is *not* a power $\mathfrak{p}^n$ of any prime ideal.

**Part (b) — a prime power that is not primary.** Let $R = k[X,Y,Z]/(XY - Z^2)$ with $\bar X, \bar Y, \bar Z$ the images of $X, Y, Z$, and let $\mathfrak{p} = (\bar X, \bar Z)$. Show $\mathfrak{p}$ is prime but $\mathfrak{p}^2 = (\bar X^2, \bar X\bar Z, \bar Z^2)$ is *not* primary, even though $\sqrt{\mathfrak{p}^2} = \mathfrak{p}$ is prime.

**Recall:**

The objects in play are primary ideals, the radical, prime versus maximal ideals, and the quotient criterion for primeness.

![[Def - Primary Ideal#The Definition]]

An ideal $\mathfrak{q}$ is [[Def - Primary Ideal|primary]] iff every zero-divisor of $R/\mathfrak{q}$ is nilpotent, iff $xy \in \mathfrak{q} \Rightarrow x \in \mathfrak{q}$ or $y \in \sqrt{\mathfrak{q}}$. A [[Def - Prime and Maximal Ideal|prime]] ideal $\mathfrak{p}$ has $R/\mathfrak{p}$ an [[Def - Integral Domain|integral domain]]; a maximal one has $R/\mathfrak{m}$ a field.

![[Def - Radical of an Ideal and the Nilradical#The Definition]]

To show $\mathfrak{q}$ is **not** a prime power, it suffices to identify the only candidate prime $\mathfrak{p} = \sqrt{\mathfrak{q}}$ and show $\mathfrak{q}$ falls strictly between consecutive powers: $\mathfrak{p}^{n+1} \subsetneq \mathfrak{q} \subsetneq \mathfrak{p}^n$ for some $n$, since any prime power $\mathfrak{p}^m$ equalling $\mathfrak{q}$ would have to use $\mathfrak{p} = \sqrt{\mathfrak{q}}$.

---

# Convergent Strategy

**Problem class.** This is a pair of *construct-a-counterexample* problems, the kind the [[Commutative Algebra IX — Primary Decomposition#Problem-Solving Strategy|topic page strategy]] flags as the natural use of primary decomposition ("good for explicit computations and counterexamples"). Each part demolishes one half of a tempting-but-false equivalence.

**Assumption pattern.** Part (a) leverages that $(X, Y^2)$ has a *maximal* radical $(X,Y)$ — making it primary for free — while its position strictly between $(X,Y)^2$ and $(X,Y)$ rules out being a prime power. Part (b) leverages the *singularity* of the cone $XY = Z^2$: the defining relation $\bar X \bar Y = \bar Z^2$ is exactly the witness $xy \in \mathfrak{p}^2$ that breaks primariness. The recognisable trigger in (b) is "a prime that is not maximal" — the maximal-radical shortcut fails, opening the door to non-primariness.

**Theorem routing.** Part (a): certify primariness via the maximal-radical shortcut (operation 4, justified in [[Ex - Powers of a maximal ideal are primary]]); rule out prime-power by squeezing $\mathfrak{q}$ between $(X,Y)^2$ and $(X,Y)$. Part (b): certify $\mathfrak{p}$ prime via $R/\mathfrak{p} \cong k[Y]$ a domain; break primariness of $\mathfrak{p}^2$ by exhibiting the witness $\bar X \bar Y = \bar Z^2 \in \mathfrak{p}^2$ with $\bar X \notin \mathfrak{p}^2$ and $\bar Y \notin \sqrt{\mathfrak{p}^2} = \mathfrak{p}$.

**Key decision point.** In (a) the non-obvious move is realising the *only* candidate prime is the radical $(X,Y)$, so checking $\mathfrak{q}$ is squeezed between two powers of $(X,Y)$ is *sufficient* to rule out all prime powers — you do not need to check other primes. In (b) the non-obvious move is finding the witness: the cone relation $\bar X \bar Y = \bar Z^2$ is handed to you by the ring's defining equation, and recognising that $\bar Y \notin \mathfrak{p}$ (it survives in $R/\mathfrak{p} \cong k[Y]$) is what makes it a *non-nilpotent* zero-divisor. The natural error is to expect $\mathfrak{p}^2$ primary because $\mathfrak{p}$ is prime; the insight is that primeness of $\mathfrak{p}$ controls $\mathfrak{p}$, not $\mathfrak{p}^2$.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra IX — Primary Decomposition#Legal Operations|the topic page's Legal Operations]]:

1. **Pass to the quotient and read off the definition (operation 1).** Compute $R/\mathfrak{q} \cong k[Y]/(Y^2)$ in (a) and inspect $R/\mathfrak{p}^2$ in (b) to test primariness.

2. **Take radicals to find the attached prime (operation 2).** Compute $\sqrt{(X,Y^2)} = (X,Y)$ and $\sqrt{\mathfrak{p}^2} = \mathfrak{p}$ to identify the candidate primes.

3. **Upgrade to primary via a maximal radical (operation 4).** Use $(X,Y)$ maximal to certify $(X,Y^2)$ primary in (a).

4. **Produce a witness to break primariness.** In (b), exhibit $xy \in \mathfrak{p}^2$ with $x \notin \mathfrak{p}^2$, $y \notin \sqrt{\mathfrak{p}^2}$ — the negation of the primary condition.

---

# Hints

> [!note]- Hint 1 (part a)
> Compute $R/(X, Y^2)$. Setting $X = 0$ leaves $k[Y]/(Y^2)$ — the dual numbers. Its elements are $a + b\bar Y$; which are the zero-divisors, and are they nilpotent? If every zero-divisor is nilpotent, $(X, Y^2)$ is primary.

> [!note]- Hint 2 (part a)
> The radical is $\sqrt{(X, Y^2)} = (X, Y)$, a maximal ideal — so primariness is automatic. To rule out prime-power: the only prime whose power could equal $(X,Y^2)$ is its radical $(X,Y)$. Compute $(X,Y)^1 = (X,Y)$ and $(X,Y)^2 = (X^2, XY, Y^2)$ and check $(X,Y)^2 \subsetneq (X,Y^2) \subsetneq (X,Y)$.

> [!note]- Hint 3 (part b)
> First show $\mathfrak{p} = (\bar X, \bar Z)$ is prime: compute $R/\mathfrak{p}$. Killing $\bar X$ and $\bar Z$ in $k[X,Y,Z]/(XY-Z^2)$ leaves $k[Y]$ (the relation $XY = Z^2$ becomes $0 = 0$). A domain quotient means $\mathfrak{p}$ is prime, so $\sqrt{\mathfrak{p}^2} = \mathfrak{p}$ is prime — but is it maximal? No: $\mathfrak{p} \subsetneq (\bar X, \bar Y, \bar Z)$.

> [!note]- Hint 4 (part b)
> The defining relation gives you the witness for free: $\bar X \bar Y = \bar Z^2$. Is $\bar Z^2 \in \mathfrak{p}^2 = (\bar X^2, \bar X\bar Z, \bar Z^2)$? Yes. Is $\bar X \in \mathfrak{p}^2$? No (degree reasons). Is $\bar Y \in \sqrt{\mathfrak{p}^2} = \mathfrak{p}$? No ($\bar Y \neq 0$ in $R/\mathfrak{p} \cong k[Y]$). So $\bar X \bar Y \in \mathfrak{p}^2$ with $\bar X \notin \mathfrak{p}^2$ and $\bar Y \notin \sqrt{\mathfrak{p}^2}$ — primariness fails.

---

# Solution

Part (a) shows $(X, Y^2)$ is $(X,Y)$-primary (maximal radical) but sits strictly between $(X,Y)^2$ and $(X,Y)$, so it is no prime power. Part (b) shows $\mathfrak{p} = (\bar X, \bar Z)$ is prime (domain quotient) yet $\mathfrak{p}^2$ fails primariness because the cone relation $\bar X \bar Y = \bar Z^2$ furnishes a non-nilpotent zero-divisor $\bar Y$ in $R/\mathfrak{p}^2$. The non-obvious content is that primeness of $\mathfrak{p}$ does not propagate to $\mathfrak{p}^2$ once $\mathfrak{p}$ is non-maximal and the ring is singular.

**Step 1 (a): $(X, Y^2)$ is $(X,Y)$-primary.**

$R/(X,Y^2) \cong k[Y]/(Y^2)$, whose zero-divisors are exactly the multiples of $\bar Y$, all nilpotent; the radical is the maximal ideal $(X,Y)$.

> [!note]- Derivation
> The map $k[X,Y] \to k[Y]/(Y^2)$, $X \mapsto 0$, $Y \mapsto \bar Y$, is surjective with kernel $(X, Y^2)$, so $R/(X,Y^2) \cong k[Y]/(Y^2)$. An element $a + b\bar Y$ ($a, b \in k$) is a unit iff $a \neq 0$, and a zero-divisor iff $a = 0$ and $b \neq 0$ (then $(b\bar Y)(\bar Y) = b\bar Y^2 = 0$). Every such zero-divisor $b\bar Y$ is nilpotent: $(b\bar Y)^2 = 0$. So every zero-divisor is nilpotent, and $(X, Y^2)$ is [[Def - Primary Ideal|primary]]. Its radical: $\sqrt{(X,Y^2)} = (X,Y)$ since $X \in$ and $Y^2 \in \Rightarrow Y \in$ the radical, and $(X,Y)$ is maximal. So $(X,Y^2)$ is $(X,Y)$-primary. (Alternatively, the maximal radical $(X,Y)$ makes primariness automatic by [[Ex - Powers of a maximal ideal are primary]].)

**Step 2 (a): $(X, Y^2)$ is not a power of any prime.**

Any prime power equal to $(X,Y^2)$ would have base prime $\sqrt{(X,Y^2)} = (X,Y)$; but $(X,Y)^2 \subsetneq (X,Y^2) \subsetneq (X,Y)$, so $(X,Y^2)$ is strictly between consecutive powers and equals none.

> [!note]- Derivation
> Suppose $(X, Y^2) = \mathfrak{p}^n$ for some prime $\mathfrak{p}$ and $n \geq 1$. Taking radicals, $\mathfrak{p} = \sqrt{\mathfrak{p}^n} = \sqrt{(X,Y^2)} = (X,Y)$. So the only possibility is $(X,Y^2) = (X,Y)^n$. Compute the powers:
> $$(X,Y)^1 = (X,Y), \qquad (X,Y)^2 = (X^2, XY, Y^2).$$
> Now $(X,Y)^2 \subsetneq (X, Y^2)$: every generator $X^2 = X\cdot X, XY = X \cdot Y, Y^2$ lies in $(X, Y^2)$, and the containment is strict because $X \in (X, Y^2) \setminus (X,Y)^2$ (an element of $(X,Y)^2$ has all terms of total degree $\geq 2$). Also $(X, Y^2) \subsetneq (X,Y)$: clearly $X, Y^2 \in (X,Y)$, and the containment is strict because $Y \in (X,Y) \setminus (X, Y^2)$ (an element of $(X,Y^2)$ has no pure $Y$-term of degree $1$). So
> $$(X,Y)^2 \subsetneq (X, Y^2) \subsetneq (X,Y)^1.$$
> Thus $(X, Y^2)$ is strictly between $(X,Y)^2$ and $(X,Y)^1$, so it equals neither, and (the powers being decreasing) it equals no $(X,Y)^n$. Hence $(X, Y^2)$ is not a prime power. $\square$

**Step 3 (b): $\mathfrak{p} = (\bar X, \bar Z)$ is prime, with non-maximal radical.**

$R/\mathfrak{p} \cong k[Y]$ is a domain, so $\mathfrak{p}$ is prime; $\sqrt{\mathfrak{p}^2} = \mathfrak{p}$ is prime but not maximal.

> [!note]- Derivation
> In $R = k[X,Y,Z]/(XY - Z^2)$, quotient further by $\mathfrak{p} = (\bar X, \bar Z)$: this sets $\bar X = \bar Z = 0$, and the defining relation $\bar X \bar Y = \bar Z^2$ becomes $0 = 0$, automatically satisfied. So $R/\mathfrak{p} \cong k[Y]$, an [[Def - Integral Domain|integral domain]]; hence $\mathfrak{p}$ is [[Def - Prime and Maximal Ideal|prime]] ([[Thm - Maximal and Prime Ideals via Quotients|prime ⟺ domain quotient]]). Then $\sqrt{\mathfrak{p}^2} = \mathfrak{p}$ (as $\sqrt{I^2} = \sqrt I$ and $\mathfrak{p}$ is radical, being prime), which is prime. But $\mathfrak{p}$ is *not maximal*: $\mathfrak{p} = (\bar X, \bar Z) \subsetneq (\bar X, \bar Y, \bar Z) \subsetneq R$, and $(\bar X, \bar Y, \bar Z)$ is a proper ideal (the origin), so $\mathfrak{p}$ is properly contained in a larger proper ideal. The maximal-radical shortcut therefore does *not* apply to $\mathfrak{p}^2$.

**Step 4 (b): $\mathfrak{p}^2$ is not primary.**

The cone relation gives $\bar X \bar Y = \bar Z^2 \in \mathfrak{p}^2$ with $\bar X \notin \mathfrak{p}^2$ and $\bar Y \notin \sqrt{\mathfrak{p}^2} = \mathfrak{p}$ — the negation of the primary condition.

> [!note]- Derivation
> Compute $\mathfrak{p}^2 = (\bar X, \bar Z)^2 = (\bar X^2, \bar X \bar Z, \bar Z^2)$. The defining relation of $R$ is $\bar X \bar Y = \bar Z^2$, and $\bar Z^2 \in \mathfrak{p}^2$, so
> $$\bar X \bar Y = \bar Z^2 \in \mathfrak{p}^2.$$
> Now check the two failures of the primary condition for the product $\bar X \cdot \bar Y$:
> - $\bar X \notin \mathfrak{p}^2$. The ideal $\mathfrak{p}^2 = (\bar X^2, \bar X \bar Z, \bar Z^2)$ is generated by elements of degree $2$ (in $\bar X, \bar Z$); $\bar X$ has degree $1$. More carefully, in the graded ring $R$ (graded by total degree, well-defined since $XY - Z^2$ is homogeneous of degree $2$), $\mathfrak{p}^2$ lies in degrees $\geq 2$, while $\bar X$ is in degree $1$ and nonzero, so $\bar X \notin \mathfrak{p}^2$.
> - $\bar Y \notin \sqrt{\mathfrak{p}^2} = \mathfrak{p}$. In $R/\mathfrak{p} \cong k[Y]$, the image of $\bar Y$ is the variable $Y \neq 0$, so $\bar Y \notin \mathfrak{p}$, hence $\bar Y \notin \sqrt{\mathfrak{p}^2}$.
>
> So $\bar X \bar Y \in \mathfrak{p}^2$ while $\bar X \notin \mathfrak{p}^2$ and $\bar Y \notin \sqrt{\mathfrak{p}^2}$, which directly violates the definition of [[Def - Primary Ideal|primary]] ($xy \in \mathfrak{q} \Rightarrow x \in \mathfrak{q}$ or $y \in \sqrt{\mathfrak{q}}$). Equivalently, $\bar Y$ is a zero-divisor of $R/\mathfrak{p}^2$ (it kills the nonzero class of $\bar X$, since $\bar X \bar Y = \bar Z^2 \equiv 0$ but $\bar X \not\equiv 0$ mod $\mathfrak{p}^2$) that is not nilpotent. Hence $\mathfrak{p}^2$ is not primary. $\square$

> [!note]- Complete formal solution
> **Part (a).** $R/(X,Y^2) \cong k[Y]/(Y^2)$, whose zero-divisors $b\bar Y$ are all nilpotent, so $(X, Y^2)$ is primary, with radical the maximal ideal $(X,Y)$. If $(X,Y^2) = \mathfrak{p}^n$ then $\mathfrak{p} = \sqrt{(X,Y^2)} = (X,Y)$, but $(X,Y)^2 = (X^2,XY,Y^2) \subsetneq (X,Y^2) \subsetneq (X,Y)$ (witnesses: $X \in (X,Y^2)\setminus(X,Y)^2$, $Y \in (X,Y)\setminus(X,Y^2)$), so $(X,Y^2)$ is no power of $(X,Y)$, hence no prime power.
>
> **Part (b).** In $R = k[X,Y,Z]/(XY-Z^2)$, $\mathfrak{p} = (\bar X,\bar Z)$ has $R/\mathfrak{p} \cong k[Y]$ a domain, so $\mathfrak{p}$ is prime and $\sqrt{\mathfrak{p}^2} = \mathfrak{p}$ — prime but not maximal. The relation $\bar X\bar Y = \bar Z^2 \in \mathfrak{p}^2$, together with $\bar X \notin \mathfrak{p}^2$ (degree $1$ vs. degree-$2$ generators) and $\bar Y \notin \mathfrak{p} = \sqrt{\mathfrak{p}^2}$ ($\bar Y \neq 0$ in $k[Y]$), violates the primary condition. So $\mathfrak{p}^2$ is not primary. $\blacksquare$

---

# Key Takeaways

**To rule out "prime power", identify the unique candidate base prime via the radical, then squeeze between consecutive powers.** The decisive simplification in part (a) is that a prime power $\mathfrak{p}^n$ has $\sqrt{\mathfrak{p}^n} = \mathfrak{p}$, so if $\mathfrak{q}$ is a prime power *at all*, its base must be $\sqrt{\mathfrak{q}}$ — there is only one candidate. This collapses an a-priori infinite search ("is $\mathfrak{q}$ a power of *some* prime?") into a finite check ("is $\mathfrak{q} = (\sqrt{\mathfrak{q}})^n$ for some $n$?"), settled by computing the powers of $\sqrt{\mathfrak{q}}$ and showing $\mathfrak{q}$ lands strictly between two consecutive ones. The transferable diagnostic: whenever you must show an ideal is not a prime power, take its radical to pin the base, then exhibit $\mathfrak{p}^{n+1} \subsetneq \mathfrak{q} \subsetneq \mathfrak{p}^n$ using a single generator of $\mathfrak{q}$ that sits between the degree filtrations. This is the standard refutation, and it explains *why* primary is the right primitive: it does not depend on the accidental coincidence "primary $=$ prime power" that holds only in PIDs.

**Primeness of $\mathfrak{p}$ says nothing about $\mathfrak{p}^2$ once $\mathfrak{p}$ is non-maximal and the ring is singular — the defining relation is the witness.** Part (b) is the canonical demonstration that the prime-power $\mathfrak{p}^2$ can fail to be primary even when $\mathfrak{p}$ is impeccably prime. The mechanism is geometric: the cone $XY = Z^2$ is singular at the origin, and the singularity injects an extra zero-divisor into $R/\mathfrak{p}^2$ that the smooth picture would not have. The trigger to find the witness is *the defining relation of the ring itself*: $\bar X \bar Y = \bar Z^2$ is exactly a product $xy$ landing in $\mathfrak{p}^2$ (because $\bar Z^2 \in \mathfrak{p}^2$) with $\bar X$ outside $\mathfrak{p}^2$ and $\bar Y$ outside $\mathfrak{p}$. The general lesson: in a singular ring, look at the relations among generators to find products that land in $\mathfrak{p}^2$ unexpectedly — these are precisely the witnesses to non-primariness, and they are why one needs *symbolic powers* $\mathfrak{p}^{(2)}$ (the $\mathfrak{p}$-primary component of $\mathfrak{p}^2$) in dimension $\geq 2$ rather than ordinary powers.

**Both failures together justify "primary" as the correct primitive notion.** The two parts are dual, and seen together they make the conceptual point of the chapter: "primary" and "prime power" are *incomparable* classes, agreeing only in special rings (PIDs, Dedekind domains). Part (a) gives a primary ideal outside the prime powers; part (b) gives a prime power outside the primary ideals. Neither contains the other. This is why the definition of primary is stated via zero-divisors-are-nilpotent rather than as "power of a prime" — the latter is a low-dimensional accident. For spaced retrieval, hold the pair as a unit: $(X, Y^2)$ is "primary but not a prime power" (smooth, but between powers), and $\mathfrak{p}^2$ on the cone is "prime power but not primary" (singular, with an injected zero-divisor). Together they delimit exactly where the integer intuition breaks down. See [[Def - Primary Ideal]] for the trichotomy prime $=$ radical $\cap$ primary, and [[Ex - Powers of a maximal ideal are primary]] for the maximal-radical case where the pathology cannot occur.
