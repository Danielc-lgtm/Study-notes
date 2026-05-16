---
type: exercise
subject: ring-theory
difficulty: "⭐"
prereqs:
  - "Def - Gaussian Integers"
  - "Thm - Classification of Gaussian Primes"
  - "Def - Irreducible and Prime Elements"
tags: [algebra, ring-theory]
---

# Problem Statement

Working in the Gaussian integers $\mathbb{Z}[i]$:

1. Factor the rational integer $30$ into a product of **Gaussian primes**.
2. Factor the Gaussian integer $4+7i$ into a product of Gaussian primes.

In each case the method should be: compute the **norm**, factor the norm into rational primes, and use the **classification of Gaussian primes** to determine the Gaussian prime factors of each piece, checking the answer by multiplying back. State the factorisation up to units and reordering, and identify the units involved.

**Recall:**

The objects in play are the Gaussian integers, their multiplicative norm, the notion of irreducible/prime element, and the classification theorem that lists all Gaussian primes.

![[Def - Gaussian Integers#The Definition]]

The [[Def - Gaussian Integers|Gaussian integers]] $\mathbb{Z}[i]=\{a+bi:a,b\in\mathbb{Z}\}$ are a subring of $\mathbb{C}$, with **norm** $N(a+bi)=a^2+b^2=(a+bi)(a-bi)$. The norm is **multiplicative**, $N(zw)=N(z)N(w)$, and its **units** are exactly the four elements of norm $1$:
$$\mathbb{Z}[i]^\times=\{1,-1,i,-i\}.$$
Because the norm is a Euclidean function, $\mathbb{Z}[i]$ is a Euclidean domain, hence a [[Def - Principal Ideal Domain|principal ideal domain]], hence a [[Def - Unique Factorization Domain|unique factorization domain]]. So every non-zero non-unit factors into Gaussian primes, **uniquely up to order and units**.

![[Def - Irreducible and Prime Elements#The Definition]]

In a unique factorization domain [[Def - Irreducible and Prime Elements|irreducible and prime coincide]]; in $\mathbb{Z}[i]$ we simply say **Gaussian prime**. A useful sufficient test: if $N(z)$ is a rational prime, then $z$ is a Gaussian prime, because a non-trivial factorisation $z=uv$ would give $N(z)=N(u)N(v)$ with both factors $>1$, contradicting primality of $N(z)$.

![[Thm - Classification of Gaussian Primes#Formal Statement]]

**Classification of Gaussian primes.** Every Gaussian prime is an associate of exactly one of:
- $1+i$, the unique prime above $2$, with $N(1+i)=2$ (and $2$ **ramifies**: $2=-i(1+i)^2$);
- $\pi$ and its conjugate $\bar\pi$, of norm $p$, for each rational prime $p\equiv 1\pmod 4$ (such $p$ **splits**: $p=\pi\bar\pi$, with $\pi,\bar\pi$ non-associate);
- the rational primes $p\equiv 3\pmod 4$ themselves, of norm $p^2$ (such $p$ stays **inert**).

---

# Convergent Strategy

**Problem class.** This is a *direct computation* problem from [[Rings III — §2.5–2.6]]: factor a given element of $\mathbb{Z}[i]$ into primes. It is the Gaussian-integer analogue of factoring an ordinary integer, and like that task it is routine once the right invariant — the norm — is in hand. The difficulty rating is one star precisely because no decision or obstruction is involved: the classification theorem hands you the answer prime by prime.

**Assumption pattern.** The only given data is an element of $\mathbb{Z}[i]$ (a rational integer in part 1, a genuinely complex one in part 2). The signal that the norm is the route is that $\mathbb{Z}[i]$ is a unique factorization domain whose primes are *classified by their norms* — so factoring an element reduces to factoring the single rational integer $N(z)$ and then matching Gaussian primes to its prime factors.

**Theorem routing.** The norm converts the problem to ordinary integer factorisation: $N(z)=\prod p_i^{m_i}$. The [[Thm - Classification of Gaussian Primes|classification of Gaussian primes]] then tells you what sits over each $p_i$: over $2$, the prime $1+i$; over $p\equiv1\pmod4$, a conjugate pair $\pi,\bar\pi$; over $p\equiv3\pmod4$, the prime $p$ itself. Multiplicativity $N(zw)=N(z)N(w)$ guarantees the Gaussian factors you pick multiply (up to a unit) back to $z$, and dividing $z$ by the factors found so far pins down which conjugate to take and which unit to absorb.

**Key decision point.** The one non-mechanical step occurs at a *split* prime $p\equiv 1\pmod 4$: the classification gives a conjugate pair $\pi,\bar\pi$ of norm $p$, and you must decide which one actually divides $z$. You decide by **trial division in $\mathbb{Z}[i]$** — compute $z/\pi$ and see whether it lands in $\mathbb{Z}[i]$. The leftover unit (one of $\pm1,\pm i$) is then fixed by comparing the product of chosen primes against $z$.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Rings III — §2.5–2.6#Legal Operations|the topic page's Legal Operations]]:

1. **Reduce to integer factorisation via the norm.** Compute $N(z)$ and factor it into rational primes; the Gaussian prime factorisation of $z$ must have norms multiplying to $N(z)$.

2. **Read off Gaussian primes from the classification.** For each rational prime $p\mid N(z)$, use the [[Thm - Classification of Gaussian Primes|classification]] to list the Gaussian prime(s) lying over $p$: $1+i$ over $2$, a conjugate pair over $p\equiv1\pmod4$, and $p$ itself over $p\equiv3\pmod4$.

3. **Certify a factor is prime by prime norm.** If $N(z)$ is a rational prime, conclude $z$ is a Gaussian prime immediately, with no further factoring.

4. **Select the correct conjugate by trial division.** At a split prime, divide $z$ by a candidate $\pi$; if the quotient is a Gaussian integer, $\pi\mid z$; otherwise $\bar\pi\mid z$.

5. **Absorb the leftover unit.** After collecting all prime factors, divide $z$ by their product; the quotient is a unit in $\{1,-1,i,-i\}$, which is recorded as the unit factor of the factorisation.

---

# Hints

> [!note]- Hint 1
> Factoring in $\mathbb{Z}[i]$ is controlled by the *norm*. Compute $N(z)$ first — it is an ordinary positive integer — and factor *that* into rational primes. Whatever the Gaussian prime factorisation of $z$ is, the norms of its factors must multiply to $N(z)$. So $N(30)=900$ and $N(4+7i)=16+49=65$ tell you exactly which rational primes to look at.

> [!note]- Hint 2
> For each rational prime $p$ dividing $N(z)$, the classification of Gaussian primes says what sits over it. $p=2$: the single prime $1+i$ (and $2=-i(1+i)^2$). $p\equiv 1\pmod 4$: a conjugate pair $\pi,\bar\pi$ with $N(\pi)=p$ — find $\pi$ by solving $p=x^2+y^2$. $p\equiv 3\pmod 4$: the prime $p$ stays prime, contributing $p$ itself.

> [!note]- Hint 3
> For $30=2\cdot 3\cdot 5$: $2$ contributes $1+i$ (up to a unit), $3\equiv 3\pmod4$ stays prime, and $5\equiv1\pmod4$ splits as $5=(2+i)(2-i)$. For $4+7i$: $N=65=5\cdot 13$, both $\equiv 1\pmod 4$, so $4+7i$ is a product of *two* Gaussian primes, one of norm $5$ and one of norm $13$.

> [!note]- Hint 4
> To find which Gaussian prime of norm $5$ divides $4+7i$, just divide: $\dfrac{4+7i}{2+i}=\dfrac{(4+7i)(2-i)}{5}=\dfrac{15+10i}{5}=3+2i$. The quotient $3+2i$ is a Gaussian integer (so $2+i$ works), and $N(3+2i)=13$, so $3+2i$ is itself the norm-$13$ prime. Hence $4+7i=(2+i)(3+2i)$ — no leftover unit.

---

# Solution

Both factorisations follow the same routine: compute the norm, factor it over $\mathbb{Z}$, lay down one Gaussian prime per rational prime factor using the classification, fix conjugates and the leftover unit by division.

**Step 1: Factor $30$ in $\mathbb{Z}[i]$.**
$$30=-i\,(1+i)\cdot 3\cdot (2+i)(2-i),$$
a product of the Gaussian primes $1+i,\;3,\;2+i,\;2-i$ together with the unit $-i$.

> [!note]- Derivation
> *Norm.* $N(30)=30^2=900=2^2\cdot 3^2\cdot 5^2$. So $30$ involves the rational primes $2,3,5$.
>
> *Factor each rational prime in $\mathbb{Z}[i]$, using the classification.*
> - $2$ **ramifies**: $2=(1+i)(1-i)$. Note $1-i=-i(1+i)$ since $-i(1+i)=-i+1=1-i$, so the two factors are associates and $2=-i(1+i)^2$. The Gaussian prime over $2$ is $1+i$.
> - $3\equiv 3\pmod 4$ stays **inert**: $3$ is itself a Gaussian prime. (Indeed $3=a^2+b^2$ has no integer solution, so $N$ takes no value $3$, and $N(3)=9$ admits no balanced split $3\cdot 3$ — $3$ cannot factor.)
> - $5\equiv 1\pmod 4$ **splits**: $5=2^2+1^2=(2+i)(2-i)$, with $N(2\pm i)=5$ prime, so $2+i$ and $2-i$ are non-associate Gaussian primes.
>
> *Assemble.* Multiply the pieces:
> $$2\cdot 3\cdot 5=(1+i)(1-i)\cdot 3\cdot (2+i)(2-i).$$
> Replacing $1-i$ by $-i(1+i)$ collects the unit:
> $$30=-i\,(1+i)^2\cdot 3\cdot (2+i)(2-i).$$
> *Check.* $(1+i)^2=2i$, so $-i\cdot 2i\cdot 3\cdot 5=-i\cdot 2i\cdot 15=2\cdot 15=30$. ✓ Up to units, $30$ has Gaussian prime factorisation $(1+i)^2\cdot 3\cdot(2+i)\cdot(2-i)$.

**Step 2: Factor $4+7i$ in $\mathbb{Z}[i]$.**
$$4+7i=(2+i)(3+2i),$$
a product of two Gaussian primes, with no unit factor.

> [!note]- Derivation
> *Norm.* $N(4+7i)=4^2+7^2=16+49=65=5\cdot 13$. Both $5$ and $13$ are rational primes $\equiv 1\pmod 4$, hence **split**, and each contributes one Gaussian prime factor of $4+7i$. So $4+7i$ is a product of exactly two Gaussian primes, of norms $5$ and $13$.
>
> *The norm-$5$ prime.* The two Gaussian primes of norm $5$ are $2+i$ and $2-i$. Test which divides $4+7i$:
> $$\frac{4+7i}{2+i}=\frac{(4+7i)(2-i)}{(2+i)(2-i)}=\frac{8-4i+14i-7i^2}{5}=\frac{8+10i+7}{5}=\frac{15+10i}{5}=3+2i.$$
> The quotient $3+2i$ is a genuine Gaussian integer, so $2+i\mid 4+7i$ and the norm-$5$ factor is $2+i$.
>
> *The remaining factor.* The cofactor is $3+2i$, with $N(3+2i)=3^2+2^2=13$, a rational prime. By the prime-norm test, $3+2i$ is itself a Gaussian prime — no further factoring is possible.
>
> *Assemble and check.* Hence $4+7i=(2+i)(3+2i)$. Verify directly:
> $$(2+i)(3+2i)=6+4i+3i+2i^2=6+7i-2=4+7i. ✓$$
> The product of the chosen primes equals $4+7i$ exactly, so the **unit factor is $1$**: no leftover unit is needed.

> [!note]- Complete formal solution
> **Claim.** $30=-i\,(1+i)^2\cdot 3\cdot(2+i)(2-i)$ and $4+7i=(2+i)(3+2i)$, as products of Gaussian primes in $\mathbb{Z}[i]$.
>
> $\mathbb{Z}[i]$ is a unique factorization domain; $N(a+bi)=a^2+b^2$ is multiplicative; the units are $\pm1,\pm i$; an element of prime norm is a Gaussian prime.
>
> *Factoring $30$.* $N(30)=900=2^2 3^2 5^2$. By the classification of Gaussian primes: $2=(1+i)(1-i)$ with $1-i=-i(1+i)$, so $2=-i(1+i)^2$; $3\equiv 3\pmod 4$ is inert, hence prime; $5\equiv 1\pmod 4$ splits, $5=(2+i)(2-i)$ with $2\pm i$ prime of norm $5$. Therefore $30=2\cdot 3\cdot 5=-i\,(1+i)^2\cdot 3\cdot(2+i)(2-i)$; check $-i(1+i)^2\cdot 3\cdot 5=-i(2i)(15)=30$.
>
> *Factoring $4+7i$.* $N(4+7i)=65=5\cdot 13$, both $\equiv 1\pmod 4$, so $4+7i$ is a product of two Gaussian primes of norms $5,13$. Trial division: $(4+7i)/(2+i)=(4+7i)(2-i)/5=(15+10i)/5=3+2i\in\mathbb{Z}[i]$, so $2+i\mid 4+7i$. The cofactor $3+2i$ has prime norm $13$, hence is a Gaussian prime. So $4+7i=(2+i)(3+2i)$; check $(2+i)(3+2i)=4+7i$. $\blacksquare$

---

# Key Takeaways

**Factoring in $\mathbb{Z}[i]$ is factoring the norm in $\mathbb{Z}$, plus a lookup table.** The whole procedure rests on one observation: a Gaussian prime is recognised by its norm, and the norm of a product is the product of the norms. So to factor $z$ you factor the *single ordinary integer* $N(z)$, and then the classification of Gaussian primes acts as a deterministic lookup — over $2$ put $1+i$, over a split prime put a conjugate pair, over an inert prime put the prime itself. There is no search over the two-dimensional lattice $\mathbb{Z}[i]$. This is the general shape of factorisation in a ring of integers: the norm pushes the problem down to $\mathbb{Z}$, where factorisation is understood, and a splitting law (here the $\pmod 4$ trichotomy) reconstructs the upstairs factors. The same template factors elements of the Eisenstein integers $\mathbb{Z}[\omega]$ (splitting governed by residues mod $3$) or any imaginary quadratic ring with unique factorisation.

**The number of prime factors and the presence of conjugate pairs are visible in the norm before any computation.** Once $N(4+7i)=65=5\cdot 13$ is in hand, you already know $4+7i$ is a product of exactly two Gaussian primes, one of norm $5$ and one of norm $13$, with no unit subtleties — because both $5,13$ are split primes contributing one prime each. Reading the *shape* of the answer off the norm's factorisation is the first thing to do: a square factor $p^2$ with $p\equiv 3\pmod 4$ signals one inert prime $p$; a factor $2^k$ signals $k$ copies of $1+i$ and a unit (since $2$ ramifies); a factor $p^k$ with $p\equiv 1\pmod 4$ signals $k$ split primes whose conjugate types are still to be determined. This pre-reading turns the factorisation from open-ended search into filling in a template of known length.

**Trial division in $\mathbb{Z}[i]$ resolves the only genuine ambiguity — which conjugate divides.** At a split prime the classification offers a conjugate pair $\pi,\bar\pi$ and is silent on which one divides $z$; you settle it by dividing. Division in $\mathbb{Z}[i]$ is mechanical: $z/\pi=z\bar\pi/N(\pi)$, and $\pi\mid z$ exactly when this lands in $\mathbb{Z}[i]$, i.e. when $N(\pi)$ divides both coordinates of $z\bar\pi$. This rationalise-and-test step is the Gaussian analogue of checking divisibility of integers, and it is the one place creativity might seem required but is not — both candidates are explicit, and one division decides. The leftover unit is then forced by comparing the product of chosen primes to $z$, since $\mathbb{Z}[i]^\times=\{\pm1,\pm i\}$ is a finite, fully known group.

**Inert primes contribute themselves; ramified primes hide a unit.** Two of the three prime types need care beyond "pick a factor". An inert prime $p\equiv 3\pmod 4$ is *already* a Gaussian prime: do not try to break it, and note its norm is $p^2$, not $p$. A ramified prime $2$ factors as $(1+i)(1-i)$, but $1-i$ and $1+i$ are associates ($1-i=-i(1+i)$), so writing $2$ in terms of a single prime $1+i$ extrudes a unit: $2=-i(1+i)^2$. Tracking that unit is why the factorisation of $30$ carries a $-i$. The general principle — ramification concentrates a prime into a repeated factor times a unit, inertness leaves it whole, splitting breaks it into a conjugate pair — is exactly the trichotomy of how primes behave in quadratic extensions, and recognising which case you are in is what makes the factorisation correct rather than merely plausible.
