---
type: theorem
subject: ring-theory
prereqs:
  - "Def - Gaussian Integers"
  - "Def - Unique Factorization Domain"
  - "Def - Irreducible and Prime Elements"
  - "Thm - Classification of Gaussian Primes"
tags: [algebra, ring-theory]
---

# Notation

Throughout, $n$ is a non-negative integer and "$n$ is a **sum of two squares**" means $n = x^2 + y^2$ for some integers $x, y$ (zero allowed: $0$, $1$, $4$ are sums of two squares). The ring $\mathbb{Z}[i] = \{a + bi : a, b \in \mathbb{Z}\}$ is the [[Def - Gaussian Integers|Gaussian integers]], with multiplicative **norm** $N(a + bi) = a^2 + b^2 = (a+bi)(a-bi)$; note $N(x + iy) = x^2 + y^2$, so *$n$ is a sum of two squares exactly when $n$ is the norm of some Gaussian integer*. A **rational prime** is an ordinary prime $p \in \mathbb{Z}$. We write $n = p_1^{n_1} p_2^{n_2} \cdots p_k^{n_k}$ for the prime factorization of $n$ into distinct rational primes $p_j$ with exponents $n_j \geq 1$. The congruence $p \equiv 3 \pmod 4$ means $p$ leaves remainder $3$ on division by $4$. Since $\mathbb{Z}[i]$ is a [[Def - Unique Factorization Domain|UFD]], every non-zero Gaussian integer factors into [[Def - Irreducible and Prime Elements|irreducibles]], uniquely up to order and units. The full registry is on [[Rings III — §2.5–2.6]].

---

# Statement

> **Sum of Two Squares Theorem (Fermat).** A non-negative integer $n$ is a sum of two squares,
> $$n = x^2 + y^2 \qquad\text{for some } x, y \in \mathbb{Z},$$
> if and only if every rational prime $p \equiv 3 \pmod 4$ occurs to an **even power** in the prime factorization of $n$.
>
> Equivalently: write $n = p_1^{n_1} \cdots p_k^{n_k}$ with the $p_j$ distinct primes; then $n$ is a sum of two squares if and only if, for each $j$ with $p_j \equiv 3 \pmod 4$, the exponent $n_j$ is even.

---

# Motivation

Which whole numbers are sums of two squares? $1 = 1^2 + 0^2$, $2 = 1^2 + 1^2$, $5 = 2^2 + 1^2$, $13 = 3^2 + 2^2$ — but $3$ is not, $7$ is not, $21$ is not. Stare at a list of which integers *are* expressible and which are not, and a pattern refuses to be obvious: the answer is not about size, not about parity, not visibly about the number itself. This is one of the oldest questions in number theory, going back to Diophantus and answered by Fermat, and the striking thing is that the answer turns out to be a clean statement about the *prime factorization* — specifically about the primes $\equiv 3 \pmod 4$ and the parity of their exponents.

Why should the question have anything to do with primes mod $4$? Because $x^2 + y^2$ is *not* just a number — it factors. In the Gaussian integers,
$$x^2 + y^2 = (x + iy)(x - iy) = N(x + iy).$$
So "$n$ is a sum of two squares" is *identically* the statement "$n$ is the norm of a Gaussian integer". This single reinterpretation moves the problem from $\mathbb{Z}$, where $x^2 + y^2$ is opaque, into $\mathbb{Z}[i]$, where it is a factorization. And in $\mathbb{Z}[i]$ we already know everything: it is a [[Def - Unique Factorization Domain|unique factorization domain]], and the [[Thm - Classification of Gaussian Primes|classification of Gaussian primes]] tells us exactly which rational primes are norms ($2$ and the $p \equiv 1 \pmod 4$) and which are not (the $p \equiv 3 \pmod 4$).

From there the answer is forced, and one should *expect* it. The norm is multiplicative, so a norm times a norm is a norm: the set of integers expressible as $x^2 + y^2$ is closed under multiplication. So to build a sum-of-two-squares it is enough to build each prime-power factor as a norm. The split primes $p$ (those $\equiv 1 \pmod 4$, and $2$) are norms — $p = \pi\bar\pi$ — so any power of them is a norm. The inert primes $p \equiv 3 \pmod 4$ are *not* norms — but $p^2 = N(p)$ certainly is, since $p$ itself is a Gaussian integer. So an inert prime contributes a norm exactly when it appears to an *even* power, packaged as $(p^2)^{n_j/2}$. That is the whole theorem: split primes are free, inert primes must come in pairs. The motivation for the result is that it is the inevitable shadow, on the integers, of the classification of primes in $\mathbb{Z}[i]$.

There is also a constructive payoff. The proof does not merely decide *whether* $n$ is a sum of two squares — it *finds* the representation, by factoring each prime in $\mathbb{Z}[i]$ and multiplying the Gaussian factors back together. And because there are choices in that multiplication (which conjugate to take), it explains why a number can have *several* representations.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem decides membership in the set $S = \{x^2 + y^2 : x, y \in \mathbb{Z}\}$, and recognising its applicability is recognising when a problem is secretly asking about $S$.

The first disguised source is **a quadratic form $x^2 + y^2$, however dressed up**. Any expression that *is* a sum of two squares — the squared modulus $|z|^2$ of a complex number $z = x + iy$ with integer parts, the squared length $\|v\|^2$ of an integer vector $v \in \mathbb{Z}^2$, the norm $N(\alpha)$ of a Gaussian integer — is governed by this theorem. The bridge is the identity $x^2 + y^2 = N(x + iy)$, turning the geometric or analytic object into a Gaussian norm. The non-obvious part is noticing that "integer point on a circle of radius $\sqrt n$" and "$n$ is a sum of two squares" are the same question. *Example problem:* decide whether the circle $x^2 + y^2 = 2024$ contains an integer point.

The second disguised source is **a number presented through its prime factorization, or through enough of it**. The theorem's hypothesis is entirely about exponents of primes $\equiv 3 \pmod 4$. So whenever a problem hands you $n$ already factored, or hands you divisibility information pinning down those exponents, you have the input directly. The non-obviousness is that you need *only* the $3 \bmod 4$ primes' parities — primes $\equiv 1 \pmod 4$ and the prime $2$ may appear to any power and are irrelevant to the decision. *Example problem:* is $3^4 \cdot 5 \cdot 7^2$ a sum of two squares? Yes — both $3$ and $7$ appear to even powers.

The third, subtler source is **a multiplicative closure question**. Because $S$ is closed under multiplication (the norm is multiplicative), any problem of the form "if $m$ and $n$ are sums of two squares, is $mn$?" or "is the product of these expressible numbers expressible?" routes through this theorem and the two-square identity $(a^2+b^2)(c^2+d^2) = (ac-bd)^2 + (ad+bc)^2$. The non-obvious bridge is that multiplicativity of $S$ is *the same fact* as multiplicativity of the Gaussian norm.

**Targets (Output Amplification)**

The bare conclusion is a yes/no membership test. Combined with other facts it does more.

Combine the theorem with **the constructive content of its proof** to *produce* a representation. The proof factors each prime of $n$ in $\mathbb{Z}[i]$ and multiplies the Gaussian factors; reading off real and imaginary parts of the product $z = x + iy$ gives explicit $x, y$ with $x^2 + y^2 = n$. The non-obvious target: the theorem is not only a decision procedure but an *algorithm*, reducing "write $n$ as a sum of squares" to "factor $n$ and factor its split primes in $\mathbb{Z}[i]$".

Combine the theorem with **the freedom in choosing conjugates** to *count* representations. When $n$ has split prime $p^k$ in its factorization, distributing the $k$ Gaussian factors between $\pi$ and $\bar\pi$ is a free choice, and different choices generally give genuinely different $(x, y)$. This is why $65 = 5 \cdot 13$ has two essentially different representations, $1^2 + 8^2$ and $4^2 + 7^2$. The non-obvious target is the exact formula for the number of representations $r_2(n)$.

Combine the theorem with **its negative direction** to prove non-representability and to obstruct equations. "Some prime $\equiv 3 \pmod 4$ appears to an odd power" certifies that $n$ is *not* a sum of two squares — a clean, checkable obstruction. This is used to show certain Diophantine equations have no solutions and to prove integers are not norms from $\mathbb{Z}[i]$. *Example:* $x^2 + y^2 = 21$ is unsolvable because $21 = 3 \cdot 7$ has $3$ (and $7$) to the first power.

---

# Why Is It True

Drop the integers entirely and think inside $\mathbb{Z}[i]$. The equation $n = x^2 + y^2$ is the equation $n = N(z)$ for $z = x + iy$: *$n$ is a sum of two squares precisely when $n$ is a norm.* Once the problem is "which integers are Gaussian norms?", the answer is dictated by two facts you already have — the norm is multiplicative, and the [[Thm - Classification of Gaussian Primes|Gaussian primes are classified]] — and the theorem becomes almost inevitable. Here is the reasoning, in the direction that builds intuition.

**The set of norms is closed under multiplication.** If $m = N(z)$ and $n = N(w)$, then $mn = N(z)N(w) = N(zw)$ is again a norm. So the integers that are sums of two squares form a multiplicatively closed set. This means: to understand which $n$ are norms, it suffices to understand which *prime powers* $p^k$ are norms — because $n$ is the product of its prime powers, and a product of norms is a norm. The problem decomposes prime by prime.

**Now ask, for each rational prime $p$: which powers $p^k$ are norms?** The classification of Gaussian primes sorts the primes into exactly two behaviours.

- If $p = 2$ or $p \equiv 1 \pmod 4$ — the **split** primes — then $p$ *itself* is a norm: $p = \pi\bar\pi = N(\pi)$ for a Gaussian prime $\pi$. Then *every* power is a norm: $p^k = N(\pi)^k = N(\pi^k)$. Split primes are completely free — to any power, they are sums of two squares.

- If $p \equiv 3 \pmod 4$ — the **inert** primes — then $p$ is *not* a norm: by the classification it stays prime in $\mathbb{Z}[i]$, and a prime $p \equiv 3 \pmod 4$ is not a sum of two squares (a square is $0$ or $1$ mod $4$, so a sum of two squares is never $3$ mod $4$). So $p^1$ is not a norm. But $p^2$ *is* a norm — trivially, because $p$ is a Gaussian integer and $p^2 = p \cdot \bar p = N(p)$ (here $\bar p = p$). More generally $p^{2j} = N(p^j)$ is a norm, while the odd powers $p^{2j+1}$ are not. The reason an *odd* power fails is the heart of it: in $\mathbb{Z}[i]$ the prime $p$ is itself irreducible, so the only Gaussian primes dividing $p^k$ are associates of $p$, each contributing $p^2$ to the norm; a norm built from copies of $p$ is therefore always an *even* power of $p$. To get $p^k$ as a norm you must have $k$ even.

**Assemble.** An integer $n = \prod p_j^{n_j}$ is a norm if and only if each factor $p_j^{n_j}$ is a norm — because norms multiply, and conversely a norm's prime factorization inherits the parity constraint. Split primes impose no condition. Each inert prime $p_j \equiv 3 \pmod 4$ imposes exactly one condition: its exponent $n_j$ must be even. That is the theorem. The slogan: *split primes are free, inert primes come in pairs* — and the only reason inert primes come in pairs is that, staying prime in $\mathbb{Z}[i]$, they can only enter a norm two at a time.

One more remark on why the converse direction (building $n$ when the parity condition holds) works so cleanly: it is **constructive**. Given the factorization of $n$, factor each split prime $p_j$ as $\pi_j\bar\pi_j$ in $\mathbb{Z}[i]$, write each inert prime power $p_j^{n_j} = (p_j^{n_j/2})^2 = N(p_j^{n_j/2})$, multiply all the Gaussian pieces into a single $z = x + iy$, and then $n = N(z) = x^2 + y^2$ outright. The proof hands you the $x$ and $y$.

---

# What Makes This Hard

The conceptual leap is the reinterpretation $x^2 + y^2 = N(x+iy)$ — recognising that the problem lives in $\mathbb{Z}[i]$, not $\mathbb{Z}$; without it there is no traction. After that, the step people stumble on is the inert-prime parity: one must see that a prime $p \equiv 3 \pmod 4$, staying *prime* in $\mathbb{Z}[i]$, can only enter a norm as $p^2$ at a time, so an odd power of $p$ can never be a norm — this needs the [[Thm - Classification of Gaussian Primes|classification of Gaussian primes]] and unique factorization, not just the multiplicativity of the norm. The most common error is to prove only one direction and forget the other: the easy direction is "parity holds $\Rightarrow$ $n$ is a sum of squares" (build it up), and the genuinely-using-UFD direction is "$n$ a sum of squares $\Rightarrow$ parity holds" (a norm forces even exponents on inert primes).

---

# Rederivation Scaffold

**High-level strategy:**
Translate $x^2 + y^2 = N(x + iy)$, so the question is "which $n$ are Gaussian norms?". Use that norms are closed under multiplication and that the [[Thm - Classification of Gaussian Primes|Gaussian primes]] are known. Forward direction: a norm, factored in $\mathbb{Z}[i]$, forces inert primes to even exponents. Converse: given the parity condition, build $z$ with $N(z) = n$ prime-power by prime-power.

**Subgoal decomposition:**

1. **Reformulate.** Show $n$ is a sum of two squares $\iff$ $n = N(z)$ for some $z \in \mathbb{Z}[i]$.
   - *Hint:* $N(x + iy) = x^2 + y^2$; this is a definitional identity.
   - *Why needed:* It moves the entire problem into $\mathbb{Z}[i]$, where factorization tools apply.

2. **Norms multiply.** Show that if $m$ and $n$ are norms then $mn$ is a norm.
   - *Hint:* $N(z)N(w) = N(zw)$.
   - *Why needed:* It lets the problem be solved one prime power at a time, then reassembled.

3. **(Converse) Each allowed prime power is a norm.** Show: for $p$ split, $p^k = N(\pi^k)$; for $p \equiv 3 \pmod 4$ and $k$ even, $p^k = N(p^{k/2})$.
   - *Hint:* By the classification, split $p = \pi\bar\pi = N(\pi)$; inert $p$ has $p^2 = p\bar p = N(p)$.
   - *Why needed:* With Subgoal 2, multiplying these gives $n = N(z)$ when the parity condition holds.

4. **(Forward) A norm forces even exponents on inert primes.** Show: if $n = N(z)$, factor $z$ into Gaussian primes; each Gaussian prime contributes a rational prime power to $N(z)$, and an inert prime $p \equiv 3 \pmod 4$ can only contribute $p^2$ at a time.
   - *Hint:* By the classification, a Gaussian prime $\alpha$ has $N(\alpha) = p$ (split) or $N(\alpha) = p^2$ (inert $p$, with $\alpha \sim p$); take $N$ of $z = \prod \alpha_i$.
   - *Why needed:* It is the only-if direction — without it the theorem is half-proved.

5. **Assemble.** Combine Subgoals 3 and 4 into the biconditional, and note the construction yields explicit $x, y$.
   - *Hint:* Forward = Subgoal 4; converse = Subgoals 2 + 3; reading off $z = x + iy$ gives the representation.
   - *Why needed:* States the full theorem and its constructive corollary.

---

# Lemma Decomposition

> [!note]- Lemma 1: Sum of two squares = Gaussian norm
> **Statement:** A non-negative integer $n$ is a sum of two squares if and only if $n = N(z)$ for some $z \in \mathbb{Z}[i]$.
>
> **Hint:** Use the definition of the norm directly.
>
> **Why needed:** It is the translation that moves the problem into $\mathbb{Z}[i]$; the rest of the proof is factorization there.
>
> > [!note]- Full proof
> > If $n = x^2 + y^2$ with $x, y \in \mathbb{Z}$, set $z = x + iy \in \mathbb{Z}[i]$; then $N(z) = x^2 + y^2 = n$. Conversely, if $n = N(z)$ for some $z = x + iy \in \mathbb{Z}[i]$, then $n = N(x + iy) = x^2 + y^2$ is a sum of two squares. $\blacksquare$

> [!note]- Lemma 2: The integers expressible as sums of two squares are closed under multiplication
> **Statement:** If $m$ and $n$ are each sums of two squares, then so is $mn$. Concretely, $(a^2 + b^2)(c^2 + d^2) = (ac - bd)^2 + (ad + bc)^2$.
>
> **Hint:** Multiplicativity of the Gaussian norm; or expand the two-square identity directly.
>
> **Why needed:** It reduces the theorem to a statement about prime powers — a product of norms is a norm, so $n$ is handled one prime power at a time.
>
> > [!note]- Full proof
> > Write $m = N(z)$ and $n = N(w)$ for Gaussian integers $z, w$ (Lemma 1). Since the norm is multiplicative,
> > $$mn = N(z)\,N(w) = N(zw),$$
> > so $mn$ is a norm, hence a sum of two squares (Lemma 1 again). Writing $z = a + bi$, $w = c + di$, the product is $zw = (ac - bd) + (ad + bc)i$, and taking norms gives the explicit identity
> > $$(a^2 + b^2)(c^2 + d^2) = (ac - bd)^2 + (ad + bc)^2. \qquad \blacksquare$$

> [!note]- Lemma 3: Each permitted prime power is a sum of two squares
> **Statement:** Let $p$ be a rational prime. (a) If $p = 2$ or $p \equiv 1 \pmod 4$, then $p^k$ is a sum of two squares for *every* $k \geq 0$. (b) If $p \equiv 3 \pmod 4$, then $p^k$ is a sum of two squares for every *even* $k \geq 0$.
>
> **Hint:** Use the [[Thm - Classification of Gaussian Primes|classification]]: split $p = \pi\bar\pi$; for inert $p$, note $p^2 = N(p)$.
>
> **Why needed:** It supplies the building blocks for the converse direction: multiply these together (Lemma 2) to realise any $n$ satisfying the parity condition.
>
> > [!note]- Full proof
> > **(a)** Let $p = 2$ or $p \equiv 1 \pmod 4$. By the [[Thm - Classification of Gaussian Primes|classification of Gaussian primes]], such $p$ is the norm of a Gaussian prime: $p = \pi\bar\pi = N(\pi)$ for some $\pi \in \mathbb{Z}[i]$ (for $p = 2$, $\pi = 1 + i$). Then for any $k \geq 0$,
> > $$p^k = N(\pi)^k = N(\pi^k),$$
> > a norm, hence a sum of two squares by Lemma 1.
> >
> > **(b)** Let $p \equiv 3 \pmod 4$ and $k = 2j$ even. Since $p \in \mathbb{Z} \subseteq \mathbb{Z}[i]$ and $\bar p = p$, we have $p^2 = p\cdot\bar p = N(p)$. Then
> > $$p^k = p^{2j} = (p^2)^j = N(p)^j = N(p^j),$$
> > a norm, hence a sum of two squares. (Explicitly, $p^{2j} = (p^j)^2 + 0^2$.) $\blacksquare$

> [!note]- Lemma 4: A Gaussian norm has every inert prime to an even power
> **Statement:** Let $z \in \mathbb{Z}[i]$ be non-zero and $n = N(z)$. Then in the prime factorization of $n$, every rational prime $p \equiv 3 \pmod 4$ occurs to an even power.
>
> **Hint:** Factor $z$ into Gaussian primes and take the norm; each Gaussian prime contributes either a split prime $p$ or an inert prime *squared*, $p^2$.
>
> **Why needed:** It is the forward direction — the only-if half — and the one place unique factorization in $\mathbb{Z}[i]$ is essential.
>
> > [!note]- Full proof
> > If $z$ is a unit, $N(z) = 1$ and the claim is vacuous. Otherwise, since $\mathbb{Z}[i]$ is a [[Def - Unique Factorization Domain|UFD]], factor $z = \alpha_1 \alpha_2 \cdots \alpha_q$ into Gaussian primes. Taking norms and using multiplicativity,
> > $$n = N(z) = N(\alpha_1)\,N(\alpha_2)\cdots N(\alpha_q).$$
> > By the [[Thm - Classification of Gaussian Primes|classification of Gaussian primes]], each Gaussian prime $\alpha_i$ is, up to associates, of one of two types, and its norm is correspondingly:
> > - a **split** prime: $N(\alpha_i) = p$ for $p = 2$ or $p \equiv 1 \pmod 4$;
> > - an **inert** prime: $\alpha_i$ is an associate of a rational prime $p \equiv 3 \pmod 4$, and $N(\alpha_i) = N(p) = p^2$.
> >
> > So $n$ is a product of factors each of which is either a split prime $p$, or the *square* $p^2$ of an inert prime. A given inert prime $p \equiv 3 \pmod 4$ therefore enters $n$ only through factors of $p^2$ — that is, two at a time. Hence the total exponent of $p$ in $n$ is $2 \cdot (\#\{i : \alpha_i \text{ is an associate of } p\})$, an **even** number. (Split primes $\equiv 1 \pmod 4$, and $2$, are unconstrained.) $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
>
> Let $n$ be a non-negative integer with prime factorization $n = p_1^{n_1} \cdots p_k^{n_k}$ ($p_j$ distinct rational primes). We prove: $n$ is a sum of two squares $\iff$ every $p_j \equiv 3 \pmod 4$ has $n_j$ even. The cases $n = 0$ ($= 0^2 + 0^2$) and $n = 1$ ($= 1^2 + 0^2$) are immediate, so take $n \geq 2$.
>
> **($\Leftarrow$) Parity condition holds $\Rightarrow$ $n$ is a sum of two squares.**
>
> Assume every prime $p_j \equiv 3 \pmod 4$ occurs in $n$ to an even power. Consider each prime power $p_j^{n_j}$ separately.
> - If $p_j = 2$ or $p_j \equiv 1 \pmod 4$: by Lemma 3(a), $p_j^{n_j}$ is a sum of two squares.
> - If $p_j \equiv 3 \pmod 4$: by hypothesis $n_j$ is even, so by Lemma 3(b), $p_j^{n_j}$ is a sum of two squares.
>
> Thus every factor $p_j^{n_j}$ is a sum of two squares. By Lemma 2 (closure under multiplication), applied repeatedly, the product
> $$n = p_1^{n_1} \cdot p_2^{n_2} \cdots p_k^{n_k}$$
> is a sum of two squares. Concretely, by Lemma 1 each $p_j^{n_j} = N(z_j)$ for some $z_j \in \mathbb{Z}[i]$, and then $n = N(z_1 z_2 \cdots z_k)$; writing $z_1 \cdots z_k = x + iy$ gives the explicit representation $n = x^2 + y^2$.
>
> **($\Rightarrow$) $n$ is a sum of two squares $\Rightarrow$ parity condition holds.**
>
> Assume $n = x^2 + y^2$. By Lemma 1, $n = N(z)$ where $z = x + iy \in \mathbb{Z}[i]$, and $z \neq 0$ since $n \geq 2$. By Lemma 4, every rational prime $p \equiv 3 \pmod 4$ occurs in the factorization of $n = N(z)$ to an even power. This is exactly the parity condition.
>
> Both directions hold, so $n$ is a sum of two squares if and only if every prime $\equiv 3 \pmod 4$ occurs to an even power in $n$. $\blacksquare$
>
> ---
>
> **Worked example — $65 = 5 \times 13$.** Both $5 \equiv 1$ and $13 \equiv 1 \pmod 4$, so the parity condition holds (no inert primes at all) and $65$ is a sum of two squares. The proof *constructs* the representation: factor each prime in $\mathbb{Z}[i]$,
> $$5 = (2 + i)(2 - i), \qquad 13 = (2 + 3i)(2 - 3i).$$
> Multiplying one Gaussian factor of each, $z = (2 + i)(2 + 3i) = 4 + 6i + 2i + 3i^2 = 1 + 8i$, so $65 = N(1 + 8i) = 1^2 + 8^2$. The other choice of conjugate, $z' = (2 + i)(2 - 3i) = 4 - 6i + 2i - 3i^2 = 7 - 4i$, gives $65 = N(7 - 4i) = 7^2 + 4^2$. The freedom in pairing conjugates is exactly why $65$ has two distinct representations as a sum of two squares.

---

# Cross-Field Exercise Suggestions

**Integer points on circles — geometry of numbers.** The circle $x^2 + y^2 = n$ in the plane contains a lattice point if and only if $n$ is a sum of two squares. So the theorem decides, for each radius $\sqrt n$, whether the circle "sees" the integer lattice — and the constructive proof locates the points. The non-obvious recognition is that a question of plane geometry (does this circle pass through a lattice point?) is settled by the [[Def - Residue|residues]] mod $4$ of the prime factors of $n$.

**Counting representations and the function $r_2(n)$.** Refining the theorem with the *choices* in the proof (which conjugate of each split prime to take) yields the exact count of representations $r_2(n) = 4\bigl(d_1(n) - d_3(n)\bigr)$, where $d_j(n)$ counts divisors of $n$ congruent to $j \pmod 4$. The non-obvious step is that the *multiplicity* of solutions, not just their existence, is governed by the Gaussian factorization — split primes generate the choices, inert primes generate none.

**Non-existence of solutions to Diophantine equations.** The negative direction is a sharp obstruction: $x^2 + y^2 = n$ has *no* integer solution whenever some prime $\equiv 3 \pmod 4$ divides $n$ to an odd power. This rules out solutions to families of equations at a glance — e.g. $x^2 + y^2 = 3m$ with $3 \nmid m$ is always unsolvable. The non-obvious use is as a *local obstruction*, the two-squares analogue of arguments that show an equation has no solution by working modulo a well-chosen number.

**Pythagorean-type and norm-form problems.** Because the theorem is really "which integers are norms from $\mathbb{Z}[i]$", it generalises: the analogous question for the Eisenstein integers $\mathbb{Z}[\omega]$ asks which $n$ have the form $x^2 + xy + y^2$, answered by the *same* method (classify the primes of $\mathbb{Z}[\omega]$, use multiplicativity of its norm). Recognising the two-squares theorem as the prototype of a *norm-form representation theorem* is the non-obvious cross-field step, connecting §2.6 to the theory of binary quadratic forms.

---

# Bridges

- **[[Thm - Classification of Gaussian Primes|Classification of Gaussian Primes]]** — the engine. The two-squares theorem is the classification "multiplied up": the classification says which *primes* are Gaussian norms, and multiplicativity of the norm propagates this to all integers. Every clause of the two-squares theorem — split primes free, inert primes paired — is a direct image of a clause of the classification.

- **[[Def - Gaussian Integers|Multiplicativity of the Gaussian norm]]** — the structural fact powering Lemma 2. That $N(zw) = N(z)N(w)$ is *the same statement* as the two-square identity $(a^2+b^2)(c^2+d^2) = (ac-bd)^2 + (ad+bc)^2$; closure of "sums of two squares" under multiplication is closure of "norms" under multiplication.

- **[[Def - Unique Factorization Domain|Unique factorization in $\mathbb{Z}[i]$]]** — what makes Lemma 4 valid. The forward direction needs to factor an arbitrary Gaussian integer into primes and read off the contribution of each rational prime; without unique factorization the parity bookkeeping would not be well-defined.

- **First supplement to quadratic reciprocity** — a sub-result in disguise. The fact that an odd prime $p$ is a sum of two squares if and only if $p \equiv 1 \pmod 4$ is equivalent to "$-1$ is a quadratic residue mod $p$ exactly when $p \equiv 1 \pmod 4$", the first supplement. The two-squares theorem packages this supplement together with multiplicativity into a statement about all integers.

- **Norm-form representation theorems** — the generalisation. "Which $n$ are $x^2 + y^2$?" is the prototype; replacing $\mathbb{Z}[i]$ by another quadratic ring asks which $n$ are represented by another binary quadratic form (e.g. $x^2 + xy + y^2$ for $\mathbb{Z}[\omega]$). The method — classify primes in the ring, use the multiplicative norm — is the model for the general theory of representation by quadratic forms.

---

# Unlocked by This

> [!tip] Counting Sums of Two Squares — the function $r_2(n)$ *(from Analytic Number Theory)*
> Refining "is $n$ a sum of two squares?" to "*how many ways*?" gives $r_2(n) = 4(d_1(n) - d_3(n))$, and summing $r_2(n)$ over $n \leq X$ is the Gauss circle problem — counting lattice points in a disc. The two-squares theorem is the exact, pointwise input to this average.

> [!tip] Representation by Binary Quadratic Forms *(from Algebraic Number Theory)*
> Reading the theorem as "which integers are norms from $\mathbb{Z}[i]$" opens the general question of which integers a given binary quadratic form represents — answered, form by form, through the arithmetic of the corresponding quadratic ring and its class group.
