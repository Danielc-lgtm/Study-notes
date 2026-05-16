---
type: exercise
subject: ring-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Gaussian Integers"
  - "Def - Irreducible and Prime Elements"
  - "Thm - The Unit Group of a Finite Field is Cyclic"
  - "Thm - Classification of Gaussian Primes"
tags: [algebra, ring-theory]
---

# Problem Statement

Let $p$ be a rational prime, regarded as an element of the Gaussian integers $\mathbb{Z}[i]$. Prove the **splitting trichotomy**:

1. If $p\equiv 3\pmod 4$, then $p$ **remains prime** in $\mathbb{Z}[i]$ (it is **inert**).
2. If $p\equiv 1\pmod 4$, then $p$ is **not prime** in $\mathbb{Z}[i]$: it **splits** as $p=\pi\bar\pi$ with $\pi,\bar\pi$ non-associate Gaussian primes of norm $p$.
3. The prime $p=2$ is **not prime** in $\mathbb{Z}[i]$: it **ramifies**, $2=-i(1+i)^2$.

Show, as the heart of the argument, that for an odd prime $p$ the dichotomy is governed by whether $-1$ is a square modulo $p$: $p$ splits when $-1$ is a square mod $p$ and is inert when it is not, and that $-1$ is a square mod $p$ precisely when $p\equiv 1\pmod 4$.

**Recall:**

The objects in play are the Gaussian integers and their norm, the notion of a prime element, the structure of the unit group of $\mathbb{F}_p$, and the resulting classification of Gaussian primes.

![[Def - Gaussian Integers#The Definition]]

The [[Def - Gaussian Integers|Gaussian integers]] $\mathbb{Z}[i]=\{a+bi:a,b\in\mathbb{Z}\}$ form a subring of $\mathbb{C}$, with multiplicative **norm** $N(a+bi)=a^2+b^2=(a+bi)(a-bi)$ and units $\{\pm1,\pm i\}$ (the four elements of norm $1$). Since the norm is a Euclidean function, $\mathbb{Z}[i]$ is a Euclidean domain, hence a [[Def - Principal Ideal Domain|principal ideal domain]], hence a [[Def - Unique Factorization Domain|unique factorization domain]].

![[Def - Irreducible and Prime Elements#The Definition]]

Because $\mathbb{Z}[i]$ is a unique factorization domain, [[Def - Irreducible and Prime Elements|irreducible and prime coincide]] in it. So "$p$ is prime in $\mathbb{Z}[i]$" may be checked either as "$p$ has no non-trivial factorisation" (irreducibility) or as "$p\mid zw\Rightarrow p\mid z$ or $p\mid w$" (primality). We will move freely between the two.

![[Thm - The Unit Group of a Finite Field is Cyclic#Statement]]

For a prime $p$, write $\mathbb{F}_p=\mathbb{Z}/p\mathbb{Z}$ for the field with $p$ elements and $\mathbb{F}_p^\times$ for its multiplicative group of $p-1$ non-zero elements. The [[Thm - The Unit Group of a Finite Field is Cyclic|unit group of a finite field is cyclic]]: $\mathbb{F}_p^\times\cong C_{p-1}$. In a cyclic group of even order there is a **unique** element of order $2$.

![[Thm - Classification of Gaussian Primes#Statement]]

The conclusion of this exercise, packaged as a theorem, is the [[Thm - Classification of Gaussian Primes|classification of Gaussian primes]]: every Gaussian prime is, up to associates, either a rational prime $p\equiv 3\pmod 4$, or a Gaussian integer of norm equal to a prime $p=2$ or $p\equiv 1\pmod 4$.

---

# Convergent Strategy

**Problem class.** This is a *structural classification* problem from [[Rings III — §2.5–2.6]]: determine, as a function of $p$, whether a given element stays prime in a larger ring. The target is a clean trichotomy keyed to $p\bmod 4$, and the proof has two distinct flavours — a one-line *congruence obstruction* for inertness, and a genuine *existence argument* for splitting.

**Assumption pattern.** The input is a single rational prime $p$. Two facts make $p\bmod 4$ the deciding invariant. First, the norm form is $a^2+b^2$, and a square is $0$ or $1$ mod $4$, so the norm form *misses* every residue $3\bmod 4$ — this instantly blocks any Gaussian integer of norm $p$ when $p\equiv 3\pmod 4$. Second, $p$ splits exactly when $p=N(\pi)=a^2+b^2$ is solvable, and $a^2+b^2\equiv 0\pmod p$ with $b$ invertible rearranges to $(a/b)^2\equiv -1\pmod p$ — so splitting is equivalent to $-1$ being a **quadratic residue** mod $p$.

**Theorem routing.** Inertness ($p\equiv 3$): the congruence obstruction. If $p=N(z)$ then $p$ is a sum of two squares, impossible mod $4$; and the only way $p$ could be non-prime in the unique factorization domain $\mathbb{Z}[i]$ is $p=uv$ with $N(u)=N(v)=p$, so no such factorisation exists and $p$ stays prime. Splitting ($p\equiv 1$): route through the unit group. The [[Thm - The Unit Group of a Finite Field is Cyclic|cyclicity of $\mathbb{F}_p^\times\cong C_{p-1}$]] guarantees, when $4\mid p-1$, an element $a$ of order $4$; then $a^2$ has order $2$, so $a^2\equiv -1\pmod p$, i.e. $p\mid a^2+1=(a+i)(a-i)$. Since $p$ divides a product but divides neither factor (the quotients $(a\pm i)/p$ have non-integer imaginary part), $p$ is not prime.

**Key decision point.** The non-obvious move is to manufacture a square root of $-1$ mod $p$ *abstractly*, from cyclicity, rather than exhibiting one. The proof never names the element $a$; it only knows $C_{p-1}$ with $4\mid p-1$ contains an order-$4$ element, whose square is the unique order-$2$ element $[-1]$. This is the same "funny" non-constructive step that powers the classification theorem, and recognising that *existence of a square root of $-1$* — not its value — is all the splitting argument needs is the crux.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Rings III — §2.5–2.6#Legal Operations|the topic page's Legal Operations]]:

1. **Block a factorisation with a congruence obstruction on the norm.** Show no Gaussian integer has norm $p$ by observing $a^2+b^2$ is never $\equiv 3\pmod 4$; this forbids any non-trivial factorisation of $p$.

2. **Reduce non-primality of $p$ to solvability of $p=N(\pi)$.** In the unique factorization domain $\mathbb{Z}[i]$, taking norms of $p=uv$ forces $N(u)=N(v)=p$, so $p$ is non-prime if and only if $p$ is a value of the norm form.

3. **Translate "$p$ splits" into "$-1$ is a square mod $p$".** Rearrange $a^2+b^2\equiv 0\pmod p$ into $(ab^{-1})^2\equiv -1$, identifying the splitting condition with a quadratic-residue condition.

4. **Manufacture a root of $-1$ from cyclicity of $\mathbb{F}_p^\times$.** Use $\mathbb{F}_p^\times\cong C_{p-1}$: when $4\mid p-1$ pick an order-$4$ element $a$; its square $a^2$ is the unique order-$2$ element $[-1]$.

5. **Detect non-primality by a divides-the-product-not-the-factors witness.** From $p\mid a^2+1=(a+i)(a-i)$ with $p\nmid a\pm i$, conclude $p$ violates the prime property directly.

6. **Identify ramification by a direct factorisation.** For $p=2$, exhibit $2=-i(1+i)^2$ and note $N(1+i)=2$ is prime, so $1+i$ is a Gaussian prime and $2$ is a unit times its square.

---

# Hints

> [!note]- Hint 1
> $\mathbb{Z}[i]$ is a unique factorization domain, so "prime" and "irreducible" agree. Ask first: *when can $p$ factor non-trivially at all?* If $p=uv$ with $u,v$ non-units, take norms — $p^2=N(u)N(v)$ — and conclude $N(u)=N(v)=p$. So $p$ is non-prime in $\mathbb{Z}[i]$ exactly when some Gaussian integer has norm $p$, i.e. exactly when $p=a^2+b^2$.

> [!note]- Hint 2
> For $p\equiv 3\pmod 4$, that can never happen: a perfect square is $0$ or $1$ modulo $4$, so $a^2+b^2$ is $0,1$ or $2$ mod $4$ — never $3$. Hence no Gaussian integer has norm $p$, $p$ admits no non-trivial factorisation, and $p$ stays prime.

> [!note]- Hint 3
> For odd $p$, splitting needs $p=a^2+b^2$. Mod $p$ this reads $a^2\equiv -b^2$; with $b$ invertible, $(ab^{-1})^2\equiv -1\pmod p$. So $p$ splits if and only if $-1$ is a square mod $p$. To produce a square root of $-1$: $\mathbb{F}_p^\times\cong C_{p-1}$ is cyclic. If $p\equiv 1\pmod 4$ then $4\mid p-1$, so $C_{p-1}$ has an element $a$ of order $4$.

> [!note]- Hint 4
> If $a$ has order $4$ in $\mathbb{F}_p^\times$, then $a^2$ has order $2$. A cyclic group of even order has exactly one element of order $2$, and $[-1]$ is one — so $a^2\equiv -1\pmod p$. Thus $p\mid a^2+1=(a+i)(a-i)$. But $p$ divides neither $a+i$ nor $a-i$ (their imaginary parts $\pm 1$ are not multiples of $p$). A prime dividing a product but neither factor is not prime — so $p$ splits. For $p\equiv 3$, no order-$4$ element exists since $4\nmid p-1$, matching part 1.

---

# Solution

The argument splits cleanly by the value of $p\bmod 4$. Inertness is a congruence obstruction read off the norm form; splitting is an existence argument routed through the cyclic group $\mathbb{F}_p^\times$; ramification of $2$ is a direct factorisation.

**Step 1: Reduce non-primality of $p$ to "$p$ is a sum of two squares".**

In $\mathbb{Z}[i]$, the prime $p$ is non-prime if and only if $p=a^2+b^2$ for some integers $a,b$.

> [!note]- Derivation
> $\mathbb{Z}[i]$ is a unique factorization domain, so $p$ is prime there exactly when it is irreducible. Suppose $p=uv$ with $u,v$ both non-units. Applying the multiplicative norm,
> $$p^2=N(p)=N(u)N(v),$$
> an equation in positive integers. Since $u,v$ are non-units, $N(u),N(v)>1$, and the only factorisation of $p^2$ into two integers each $>1$ is $p\cdot p$. Hence $N(u)=N(v)=p$. Writing $u=a+bi$, this says $a^2+b^2=p$.
>
> Conversely, if $p=a^2+b^2$ then $p=(a+bi)(a-bi)$ with $N(a\pm bi)=p>1$, so neither factor is a unit — a genuine factorisation, and $p$ is reducible, hence non-prime.
>
> So the entire trichotomy reduces to a single number-theoretic question: **for which $p$ is $p$ a sum of two squares?**

**Step 2: If $p\equiv 3\pmod 4$, then $p$ stays prime (inert).**

A prime $p\equiv 3\pmod 4$ is not a sum of two squares, so by Step 1 it remains prime in $\mathbb{Z}[i]$.

> [!note]- Derivation
> A perfect square is congruent to $0$ or $1$ modulo $4$: if $n$ is even, $n^2\equiv 0$; if $n$ is odd, $n^2\equiv 1\pmod 4$. Therefore a sum of two squares $a^2+b^2$ is congruent to one of $0+0,\;0+1,\;1+1$, that is, to $0,1$ or $2\pmod 4$ — **never $3$**.
>
> Hence if $p\equiv 3\pmod 4$, the equation $p=a^2+b^2$ has no integer solution. By Step 1, $p$ admits no non-trivial factorisation in $\mathbb{Z}[i]$, so $p$ is irreducible, hence prime. Its norm is $N(p)=p^2$.

**Step 3: For odd $p$, splitting is equivalent to $-1$ being a square modulo $p$.**

For an odd prime $p$, the prime $p$ splits in $\mathbb{Z}[i]$ if and only if the congruence $x^2\equiv -1\pmod p$ has a solution.

> [!note]- Derivation
> By Step 1, $p$ splits exactly when $p=a^2+b^2$ for some integers $a,b$.
>
> ($\Rightarrow$) Suppose $p=a^2+b^2$. Reducing modulo $p$, $a^2+b^2\equiv 0$, so $a^2\equiv -b^2\pmod p$. Neither $a$ nor $b$ is divisible by $p$: if $p\mid b$ then $p\mid a^2$, so $p\mid a$, and then $p^2\mid a^2+b^2=p$, absurd for $p>1$. So $b$ is invertible mod $p$; set $x\equiv a\,b^{-1}\pmod p$. Then $x^2\equiv a^2 b^{-2}\equiv -b^2 b^{-2}\equiv -1\pmod p$. So $-1$ is a square mod $p$.
>
> ($\Leftarrow$) Suppose $x^2\equiv -1\pmod p$. Then $p\mid x^2+1=(x+i)(x-i)$ in $\mathbb{Z}[i]$. If $p$ were prime in $\mathbb{Z}[i]$ it would divide $x+i$ or $x-i$; but $(x\pm i)/p=(x/p)\pm(1/p)i$ has imaginary part $\pm 1/p\notin\mathbb{Z}$, so $p$ divides neither factor. A prime dividing a product but neither factor is impossible — so $p$ is **not** prime in $\mathbb{Z}[i]$, i.e. $p$ splits. (Concretely, $p=\gcd_{\mathbb{Z}[i]}(p,\,x+i)\cdot\overline{(\,\cdot\,)}$ is a product of two non-associate primes of norm $p$; the existence of the factorisation is all we need here.)

**Step 4: $-1$ is a square modulo $p$ if and only if $p\equiv 1\pmod 4$.**

For an odd prime $p$, the congruence $x^2\equiv -1\pmod p$ is solvable precisely when $p\equiv 1\pmod 4$.

> [!note]- Derivation
> By the [[Thm - The Unit Group of a Finite Field is Cyclic|cyclicity of the unit group]], $\mathbb{F}_p^\times\cong C_{p-1}$, a cyclic group of order $p-1$.
>
> *A square root of $-1$ is exactly an element of order $4$.* The class $[-1]\in\mathbb{F}_p^\times$ has order $2$ (it is not $[1]$ since $p$ is odd, and $(-1)^2=1$). An element $x$ satisfies $x^2=[-1]$ if and only if $x^2$ has order $2$ if and only if $x$ has order $4$. (If $x^2=[-1]$ then $x^4=[1]$ and $x^2\ne[1]$, so $\operatorname{ord}(x)=4$; conversely if $\operatorname{ord}(x)=4$ then $x^2$ has order $2$, and a cyclic group has a *unique* element of order $2$, which must be $[-1]$.)
>
> *When does $C_{p-1}$ contain an order-$4$ element?* A cyclic group of order $n$ has an element of order $d$ if and only if $d\mid n$. So $C_{p-1}$ has an element of order $4$ if and only if $4\mid p-1$, i.e. if and only if $p\equiv 1\pmod 4$.
>
> Combining: $x^2\equiv -1\pmod p$ is solvable $\iff$ $\mathbb{F}_p^\times$ has an order-$4$ element $\iff$ $p\equiv 1\pmod 4$. Note this is *non-constructive*: it produces the existence of a square root of $-1$ without exhibiting one — exactly the "funny" step flagged in the source.

**Step 5: Assemble the trichotomy; treat $p=2$ separately.**

For odd $p$: $p\equiv 1\pmod 4$ splits, $p\equiv 3\pmod 4$ is inert. For $p=2$: $2$ ramifies, $2=-i(1+i)^2$.

> [!note]- Derivation
> *Odd primes.* Chain Steps 3 and 4: $p$ splits $\iff$ $-1$ is a square mod $p$ $\iff$ $p\equiv 1\pmod 4$. The complementary odd case $p\equiv 3\pmod 4$ is therefore non-splitting, and Step 2 already showed it is inert (stays prime) — the two descriptions agree.
>
> When $p\equiv 1\pmod 4$ splits, $p=(a+bi)(a-bi)$ with $N(a\pm bi)=p$ prime, so $\pi=a+bi$ and $\bar\pi=a-bi$ are Gaussian primes. They are **non-associate**: an associate of $\pi$ is one of $\pi,-\pi,i\pi,-i\pi$, namely $a+bi,\,-a-bi,\,-b+ai,\,b-ai$; for $\bar\pi=a-bi$ to be among these would force $b=0$ or $a=0$, making $p=a^2$ or $p=b^2$ a perfect square — impossible for a prime. So $p$ genuinely splits into *two distinct* primes.
>
> *The prime $2$.* Directly, $2=(1+i)(1-i)$. Since $-i(1+i)=-i+1=1-i$, the factors are associates and
> $$2=(1+i)\cdot(-i)(1+i)=-i\,(1+i)^2.$$
> Here $N(1+i)=1^2+1^2=2$ is a rational prime, so $1+i$ is a Gaussian prime. Thus $2$ is a unit times the *square* of a single prime — it does not split into two distinct primes, nor stay inert; this intermediate behaviour is **ramification**.

> [!note]- Complete formal solution
> **Claim.** A rational prime $p$ in $\mathbb{Z}[i]$ is inert if $p\equiv 3\pmod 4$, splits into two non-associate primes of norm $p$ if $p\equiv 1\pmod 4$, and ramifies as $2=-i(1+i)^2$ if $p=2$.
>
> $\mathbb{Z}[i]$ is a unique factorization domain with multiplicative norm $N(a+bi)=a^2+b^2$ and units $\pm1,\pm i$.
>
> *Reduction.* If $p=uv$ with $u,v$ non-units, then $p^2=N(u)N(v)$ forces $N(u)=N(v)=p$; writing $u=a+bi$ gives $p=a^2+b^2$. Conversely $p=a^2+b^2$ gives $p=(a+bi)(a-bi)$, a non-trivial factorisation. So $p$ is non-prime in $\mathbb{Z}[i]$ if and only if $p$ is a sum of two squares.
>
> *Inert case.* Squares are $0,1\pmod 4$, so $a^2+b^2\not\equiv 3\pmod 4$. If $p\equiv 3\pmod 4$, then $p\ne a^2+b^2$, so $p$ has no non-trivial factorisation and stays prime; $N(p)=p^2$.
>
> *Square-root reformulation.* For odd $p$: if $p=a^2+b^2$, then mod $p$, $b$ is invertible and $(ab^{-1})^2\equiv -1$. Conversely if $x^2\equiv -1\pmod p$, then $p\mid (x+i)(x-i)$ while $p\nmid x\pm i$, so $p$ is non-prime. Hence $p$ splits if and only if $x^2\equiv -1\pmod p$ is solvable.
>
> *Quadratic residue.* $\mathbb{F}_p^\times\cong C_{p-1}$. A square root of $-1$ is an element of order $4$, and $C_{p-1}$ has one if and only if $4\mid p-1$, i.e. $p\equiv 1\pmod 4$.
>
> *Conclusion.* Odd $p$: splits if and only if $p\equiv1\pmod4$, inert if and only if $p\equiv3\pmod4$; in the split case $p=\pi\bar\pi$ with $\pi,\bar\pi$ non-associate (else $p$ is a perfect square). For $p=2$: $2=(1+i)(1-i)=-i(1+i)^2$ with $1+i$ prime of norm $2$ — ramified. $\blacksquare$

---

# Key Takeaways

**Whether a prime survives in a larger ring is decided by a sum-of-norms equation, which a congruence often kills outright.** The reduction in Step 1 is the reusable skeleton: in a unique factorization domain with a multiplicative norm, $p=uv$ forces $N(u)N(v)=N(p)$, and because $p$ is rational-prime the only way the norm can split is $N(u)=N(v)=p$. So the abstract question "does $p$ stay prime?" collapses to the concrete question "is $p$ a value of the norm form?". Once there, a congruence obstruction can settle it in one line — here $a^2+b^2\not\equiv 3\pmod 4$ kills every $p\equiv 3\pmod 4$. This pattern recurs throughout algebraic number theory: in $\mathbb{Z}[\omega]$ (Eisenstein integers) the norm form is $a^2-ab+b^2$ and a mod-$3$ congruence governs which primes split; in any imaginary quadratic ring the splitting of $p$ is decided by whether the discriminant is a square mod $p$. The trigger is "does element $x$ stay prime/irreducible upstairs" — reach for the norm and look for a congruence obstruction first.

**Splitting of $p$ is the same fact as $-1$ being a quadratic residue mod $p$ — an arithmetic statement in disguise.** Step 3 performs a translation that is worth internalising: $p=a^2+b^2$, read modulo $p$, becomes $(ab^{-1})^2\equiv -1$. So the ring-theoretic event "$p$ factors in $\mathbb{Z}[i]$" *is* the number-theoretic event "$-1\in(\mathbb{F}_p^\times)^2$". The element $i\in\mathbb{Z}[i]$ is a square root of $-1$; reducing $\mathbb{Z}[i]$ mod $p$ gives $\mathbb{Z}[i]/(p)\cong\mathbb{F}_p[x]/(x^2+1)$, which is a field (so $p$ inert) exactly when $x^2+1$ is irreducible mod $p$, i.e. when $-1$ has *no* square root, and is a product of two fields (so $p$ splits) exactly when $x^2+1$ factors. This "factor the minimal polynomial mod $p$" criterion is the general law for splitting of primes in $\mathbb{Z}[\alpha]$: a prime splits according to how the minimal polynomial of $\alpha$ factors modulo $p$. Sums of two squares are simply the case $\alpha=i$.

**Cyclicity of $\mathbb{F}_p^\times$ converts a counting question on $p$ into an order-divisibility question.** The deciding step (Step 4) needs only one structural fact: $\mathbb{F}_p^\times$ is cyclic, and a cyclic group of order $n$ has an element of order $d$ if and only if $d\mid n$. A square root of $-1$ is precisely an element of order $4$ — because $-1$ is the unique order-$2$ element — so its existence is the divisibility $4\mid p-1$, which is the congruence $p\equiv 1\pmod 4$. The pattern "a special element exists if and only if its order divides the group order" is the workhorse for every quadratic-residue and primitive-root question: $-1$ is a square if and only if $4\mid p-1$; more generally a primitive $m$-th root of unity exists mod $p$ if and only if $m\mid p-1$. Whenever you must decide whether some root or character exists modulo $p$, translate it to the order of an element of the cyclic group $\mathbb{F}_p^\times$.

**The argument proves a square root of $-1$ exists without ever producing one — and that suffices.** A striking feature of Step 4 is its non-constructiveness: it asserts an order-$4$ element of $\mathbb{F}_p^\times$ exists, hence $-1$ has a square root, without naming it. For the splitting conclusion this is *enough* — Step 3 needs only the *existence* of $x$ with $x^2\equiv -1$ to produce the witness $p\mid(x+i)(x-i)$. Separating "this object exists" from "here is the object" is a recurring efficiency in algebra: existence often follows from a structural theorem (here cyclicity) far more cheaply than any construction. The contrast is instructive — actually *finding* the square root of $-1$, or *finding* the representation $p=a^2+b^2$, is a real computational task (solved by, e.g., the Euclidean algorithm on $p$ and $x+i$ in $\mathbb{Z}[i]$, as in [[Ex - Writing an integer as a sum of two squares]]), whereas knowing the representation *exists* is immediate. Recognising which half of a problem you actually need — existence or construction — keeps proofs short.

**Inert, split, ramified is a genuine trichotomy, and $2$ is the lone exceptional prime.** The three behaviours are not arbitrary labels: inert means $p$ stays a single prime of norm $p^2$; split means $p$ becomes two distinct primes of norm $p$; ramified means $p$ becomes a unit times the *square* of one prime. Exactly one prime, $p=2$, ramifies in $\mathbb{Z}[i]$, and it does so because $2$ is the prime dividing the discriminant of $\mathbb{Z}[i]$ — equivalently, because $x^2+1\equiv(x+1)^2\pmod 2$ has a repeated root. This trichotomy is the prototype for how every prime behaves in every ring of integers of a number field: finitely many primes ramify (those dividing the discriminant), and the rest split or stay inert according to the factorisation of a polynomial mod $p$. Carrying the picture "primes either stay whole, break into distinct pieces, or break into a repeated piece" into any quadratic or higher extension is the single most reusable idea here.
