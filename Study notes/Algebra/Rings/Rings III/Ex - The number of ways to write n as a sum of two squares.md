---
type: exercise
subject: ring-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Gaussian Integers"
  - "Def - Unique Factorization Domain"
  - "Thm - Classification of Gaussian Primes"
  - "Thm - Sum of Two Squares"
tags: [algebra, ring-theory]
---

# Problem Statement

Work in the Gaussian integers $\mathbb{Z}[i]$, a unique factorization domain.

1. Show that $65$ has two **essentially different** representations as a sum of two squares,
$$65=1^2+8^2=4^2+7^2,$$
and explain how the two arise from the freedom to choose, independently, a conjugate factor in each of the splittings
$$5=(2+i)(2-i),\qquad 13=(3+2i)(3-2i).$$
2. Account precisely for the number of representations: starting from a Gaussian integer $z$ with $N(z)=65$, show that **unique factorization** in $\mathbb{Z}[i]$ forces $z$ to be (a unit times) a product of one chosen Gaussian prime over $5$ and one over $13$, so there are $2\times 2=4$ such $z$ up to units — collapsing to **two** representations once conjugation $z\mapsto\bar z$ and sign/order symmetries are quotiented out.
3. Explain the general principle: for a positive integer $n$, the count of representations as an ordered/unordered sum of two squares is governed by the **exponents of the primes $p\equiv 1\pmod 4$** dividing $n$ (with primes $\equiv 3\pmod 4$, which must occur to even powers, and the prime $2$, contributing no extra multiplicity).

**Recall:**

The objects in play are the Gaussian integers, their norm, unique factorization in $\mathbb{Z}[i]$, and the classification of Gaussian primes.

![[Def - Gaussian Integers#The Definition]]

The [[Def - Gaussian Integers|Gaussian integers]] $\mathbb{Z}[i]=\{a+bi:a,b\in\mathbb{Z}\}$ carry the multiplicative **norm** $N(a+bi)=a^2+b^2=(a+bi)(a-bi)=z\bar z$, with units $\mathbb{Z}[i]^\times=\{1,-1,i,-i\}$ — the four elements of norm $1$.

![[Def - Unique Factorization Domain#The Definition]]

$\mathbb{Z}[i]$ is a Euclidean domain, hence a [[Def - Unique Factorization Domain|unique factorization domain]]: every non-zero non-unit factors into Gaussian primes, **uniquely up to reordering and replacing factors by associates**. Two elements are **associates** if they differ by a unit factor; an associate class in $\mathbb{Z}[i]$ has four members, $\{z,-z,iz,-iz\}$.

![[Thm - Classification of Gaussian Primes#Statement]]

By the [[Thm - Classification of Gaussian Primes|classification of Gaussian primes]], a rational prime $p\equiv 1\pmod 4$ **splits**, $p=\pi\bar\pi$, into two **non-associate** Gaussian primes of norm $p$; a prime $p\equiv 3\pmod 4$ stays **inert**, of norm $p^2$; and $2$ **ramifies**, $2=-i(1+i)^2$.

The [[Thm - Sum of Two Squares|sum of two squares theorem]] decides *whether* $n$ is a sum of two squares (every prime $\equiv 3\pmod 4$ to an even power); the present exercise refines it to count *how many ways*. Throughout, a representation $n=a^2+b^2$ is the same data as a Gaussian integer $z=a+bi$ with $N(z)=n$.

---

# Convergent Strategy

**Problem class.** This is a *counting via unique factorization* problem from [[Rings III — §2.5–2.6]]: not "does a decomposition exist?" but "exactly how many are there?". The right move is to set up a bijection between the objects being counted (representations $n=a^2+b^2$) and the factorisations of a single element in a unique factorization domain, then count factorisations — which unique factorization makes a finite, fully determined bookkeeping task.

**Assumption pattern.** A representation $n=a^2+b^2$ is *literally* a Gaussian integer $z=a+bi$ of norm $n$. The decisive structural input is that $\mathbb{Z}[i]$ is a unique factorization domain: this means every $z$ with $N(z)=n$ is, up to a unit, a product of Gaussian primes whose norms multiply to $n$ — and the *only* freedom is which Gaussian prime to take over each rational prime factor of $n$. At a split prime $p\equiv 1\pmod 4$ there are two choices ($\pi$ or $\bar\pi$); at an inert or ramified prime there is essentially one. The count of representations is therefore a product of small per-prime counts.

**Theorem routing.** The route is: representation $\leftrightarrow$ Gaussian integer of norm $n$ (definition of norm) $\to$ factor $z$ into Gaussian primes (unique factorization) $\to$ enumerate the choices using the [[Thm - Classification of Gaussian Primes|classification of Gaussian primes]] $\to$ quotient by the symmetries that produce the *same* unordered representation, namely the unit group $\{\pm1,\pm i\}$ and conjugation $z\mapsto\bar z$ (since $a^2+b^2$ is insensitive to signs, order, and complex conjugation).

**Key decision point.** The subtle part is the *quotient*. Raw choices of conjugate over the split primes give $2^k$ Gaussian integers $z$ (for $k$ distinct split primes), but many of these yield the *same* sum of two squares. The symmetries collapsing them are exactly: multiplication by a unit (4-fold) and conjugation (2-fold) — together an $8$-element symmetry group acting on the $z$'s — under which a representation $\{a^2,b^2\}$ is an orbit. Getting the count right means correctly identifying that conjugating *all* split factors simultaneously is the same as $z\mapsto\bar z$, so it does **not** produce a new representation. For $65$, the $2^2=4$ choices fall into $4/2=2$ conjugation-orbits, giving two representations.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Rings III — §2.5–2.6#Legal Operations|the topic page's Legal Operations]]:

1. **Identify a representation with a Gaussian integer of given norm.** Encode $n=a^2+b^2$ as $z=a+bi$ with $N(z)=n$, turning a counting problem about integers into a counting problem about ring elements.

2. **Enumerate factorisations using unique factorization.** In the unique factorization domain $\mathbb{Z}[i]$, list every $z$ of norm $n$ as a unit times a product of Gaussian primes whose norms multiply to $n$ — the factorisation is unique, so the list is complete and non-redundant.

3. **Apply the classification to count per-prime choices.** For each rational prime $p\mid n$, the [[Thm - Classification of Gaussian Primes|classification]] gives the available Gaussian primes of the right norm: two conjugates over a split $p$, one over an inert or ramified $p$.

4. **Quotient by units to pass from $z$ to its associate class.** Since $a^2+b^2=N(z)$ is unit-invariant, group the $z$'s into associate classes of size $4$.

5. **Quotient by conjugation to pass from associate classes to unordered representations.** Since $\overline{a+bi}=a-bi$ gives the same pair $\{a^2,b^2\}$, identify $z$ with $\bar z$; the surviving orbits are the essentially different representations.

6. **Multiply per-prime counts.** Because choices at distinct primes are independent, the total count of $z$'s is the product of the per-prime choice-counts, and the representation count is that product divided by the order of the collapsing symmetry.

---

# Hints

> [!note]- Hint 1
> A representation $65=a^2+b^2$ is exactly a Gaussian integer $z=a+bi$ with $N(z)=65$. So instead of hunting for pairs $(a,b)$, ask: what are the Gaussian integers of norm $65$? Since $65=5\cdot 13$ and the norm is multiplicative, $z$ must be a product of a Gaussian integer of norm $5$ and one of norm $13$.

> [!note]- Hint 2
> $\mathbb{Z}[i]$ is a unique factorization domain. Factor $5$ and $13$ into Gaussian primes: $5=(2+i)(2-i)$ and $13=(3+2i)(3-2i)$. A Gaussian integer of norm $65$ is — up to a unit — *one* prime from $\{2+i,2-i\}$ times *one* prime from $\{3+2i,3-2i\}$. That is $2\times 2=4$ products.

> [!note]- Hint 3
> Compute the four products. $(2+i)(3+2i)=4+7i$; $(2+i)(3-2i)=8-i$; $(2-i)(3+2i)=8+i$; $(2-i)(3-2i)=4-7i$. Their norms are all $65$. But $4+7i$ and $4-7i$ are complex conjugates, and $8-i,8+i$ are conjugates — and conjugation does not change $a^2+b^2$. So the four products give only **two** representations: $4^2+7^2$ and $8^2+1^2$.

> [!note]- Hint 4
> The collapse is structural: conjugating *both* chosen factors at once sends $z\mapsto\bar z$, which leaves $a^2+b^2$ unchanged. So the $2^k$ choices of conjugate (here $k=2$ split primes, $2^2=4$) fall into orbits of size $2$ under $z\mapsto\bar z$, giving $2^k/2=2^{k-1}$ essentially different representations. For general $n$, replace $k$ by a count built from the *exponents* of the primes $\equiv 1\pmod 4$: a split prime to the power $e$ offers $e+1$ choices (how many of the $e$ copies are $\pi$ versus $\bar\pi$).

---

# Solution

A representation of $n$ as a sum of two squares is a Gaussian integer of norm $n$. Unique factorization in $\mathbb{Z}[i]$ pins every such Gaussian integer down to a choice of conjugate over each split prime; counting those choices, then quotienting by the unit and conjugation symmetries that preserve $a^2+b^2$, counts the representations.

**Step 1: Representations of $65$ are Gaussian integers of norm $65$.**

The pairs $(a,b)$ with $a^2+b^2=65$ correspond bijectively to Gaussian integers $z=a+bi$ with $N(z)=65$.

> [!note]- Derivation
> By definition $N(a+bi)=a^2+b^2$. So $a^2+b^2=65$ holds if and only if $z=a+bi$ satisfies $N(z)=65$. A *representation* in the sense of the problem — an unordered pair $\{a^2,b^2\}$ of squares, with $a,b\ge 0$ say — corresponds to a Gaussian integer of norm $65$ taken up to the symmetries that do not change $\{a^2,b^2\}$: changing the sign of $a$ or $b$, swapping $a\leftrightarrow b$, and (as we will use) complex conjugation. We first enumerate *all* $z$ with $N(z)=65$, then quotient.

**Step 2: Unique factorization forces $z$ to be a unit times one prime over $5$ and one over $13$.**

Every Gaussian integer of norm $65$ has the form $u\cdot\pi_5\cdot\pi_{13}$ with $u$ a unit, $\pi_5\in\{2+i,2-i\}$, $\pi_{13}\in\{3+2i,3-2i\}$ — giving $4$ such $z$ up to units.

> [!note]- Derivation
> Factor the rational primes. Both $5,13\equiv 1\pmod 4$ split:
> $$5=(2+i)(2-i),\qquad 13=(3+2i)(3-2i),$$
> with $N(2\pm i)=5$ and $N(3\pm 2i)=13$ rational primes, so all four factors $2+i,2-i,3+2i,3-2i$ are **Gaussian primes** (prime norm $\Rightarrow$ prime), and within each conjugate pair the two primes are **non-associate** (an associate of $2+i$ is one of $\pm(2+i),\pm i(2+i)=\pm(2+i),\,\mp1\pm2i$, none equal to $2-i$).
>
> Now suppose $N(z)=65$. Then $z\bar z=65=5\cdot 13$. Factor $z$ into Gaussian primes: $z=u\,\rho_1\cdots\rho_m$ with $u$ a unit and each $\rho_j$ a Gaussian prime. Taking norms, $N(z)=\prod N(\rho_j)=65=5\cdot 13$. Each $N(\rho_j)>1$, and $65$ is a product of two rational primes, so **exactly two** prime factors occur, with $\{N(\rho_1),N(\rho_2)\}=\{5,13\}$. A Gaussian prime of norm $5$ is, by **unique factorization**, an associate of $2+i$ or of $2-i$ — the only Gaussian primes dividing $5$; similarly a Gaussian prime of norm $13$ is an associate of $3+2i$ or $3-2i$. Absorbing all the unit ambiguity into a single front unit $u$,
> $$z=u\cdot\pi_5\cdot\pi_{13},\qquad \pi_5\in\{2+i,2-i\},\quad\pi_{13}\in\{3+2i,3-2i\},\quad u\in\{\pm1,\pm i\}.$$
> Unique factorization guarantees this representation is *unambiguous*: distinct triples $(u,\pi_5,\pi_{13})$ give distinct $z$. So there are $4\times 2=8$... but the $4$ units only rotate $z$ within its associate class; **up to units there are exactly $2\times 2=4$ Gaussian integers of norm $65$**, indexed by the two independent conjugate-choices.

**Step 3: Compute the four products and collapse by conjugation.**

The four products are $4+7i,\;8-i,\;8+i,\;4-7i$; under $z\mapsto\bar z$ they pair up, leaving the **two** representations $65=4^2+7^2=1^2+8^2$.

> [!note]- Derivation
> Take $u=1$ and multiply out the four choices:
> $$\begin{aligned}
> (2+i)(3+2i)&=6+4i+3i+2i^2=4+7i, &N&=4^2+7^2=65,\\
> (2+i)(3-2i)&=6-4i+3i-2i^2=8-i, &N&=8^2+1^2=65,\\
> (2-i)(3+2i)&=6+4i-3i-2i^2=8+i, &N&=8^2+1^2=65,\\
> (2-i)(3-2i)&=6-4i-3i+2i^2=4-7i, &N&=4^2+7^2=65.
> \end{aligned}$$
> Now observe the **conjugation symmetry**. Complex conjugation $z\mapsto\bar z$ sends $a+bi\mapsto a-bi$, which leaves $a^2+b^2$ unchanged — so $z$ and $\bar z$ encode the *same* representation. And conjugating a product conjugates each factor: $\overline{(2+i)(3+2i)}=(2-i)(3-2i)$. Hence the four products split into two conjugate pairs:
> $$\{4+7i,\;4-7i\}\quad\text{and}\quad\{8-i,\;8+i\}.$$
> The first pair gives $65=4^2+7^2$; the second gives $65=8^2+1^2$. These are the **two essentially different representations**. (Together with sign and order changes the full symmetry group is larger, but it does not merge $4^2+7^2$ with $8^2+1^2$ — the unordered pairs $\{16,49\}$ and $\{1,64\}$ are different.)
>
> *Where the two come from.* Each split prime contributes one **binary** choice — conjugate or not. Two split primes give $2^2=4$ choices of $z$. Conjugating *both* factors simultaneously is exactly $z\mapsto\bar z$, an involution with no fixed points here, so it pairs the $4$ choices into $4/2=\mathbf{2}$ orbits. One conjugation choice is "absolute" (it is $z\mapsto\bar z$ and produces nothing new); the *relative* choice between the two split primes — same conjugate type or opposite — is the genuine degree of freedom, and with two split primes there are exactly $2$ relative configurations.

**Step 4: The general counting principle.**

For $n=2^{a}\prod_j p_j^{e_j}\prod_k q_k^{2f_k}$ with $p_j\equiv 1\pmod 4$ and $q_k\equiv 3\pmod 4$, the count of representations is governed entirely by the exponents $e_j$ of the split primes; the inert primes (forced to even power $2f_k$) and the ramified prime $2$ contribute no multiplicity.

> [!note]- Derivation
> Take $z$ with $N(z)=n$ and factor into Gaussian primes. [[Def - Group|Group]] the rational primes of $n$ by type, using the classification:
> - **Ramified, $p=2$.** Over $2$ sits the single prime $1+i$ (with $2=-i(1+i)^2$). A factor $2^a$ of $n$ forces *exactly* $(1+i)^a$ into $z$ (up to a unit) — there is **no choice**: $1+i$ and $1-i$ are associates, so picking "which conjugate" is picking a unit, already absorbed. Multiplicity contributed: $1$.
> - **Inert, $q\equiv 3\pmod 4$.** Here $q$ is itself a Gaussian prime, of norm $q^2$. For $N(z)=n$ to have the factor $q^{2f}$, $z$ must contain *exactly* $q^{f}$ (since each $q$ contributes $q^2$ to the norm, and $q^{2f}$ needs $f$ copies). Again **no choice**, and this is *why* $q$ must occur to an even power $2f$ — an odd power could not be a norm. Multiplicity contributed: $1$.
> - **Split, $p\equiv 1\pmod 4$.** Here $p=\pi\bar\pi$ with $\pi\not\sim\bar\pi$. A factor $p^{e}$ of $n$ means $z$ contains $\pi^{s}\bar\pi^{\,e-s}$ for some $0\le s\le e$ — the norm of $\pi^s\bar\pi^{e-s}$ is $p^s p^{e-s}=p^e$ regardless of $s$. So the split prime $p^e$ offers exactly $e+1$ choices (the value of $s$). Multiplicity contributed: $e+1$.
>
> Choices at distinct primes are independent, so the number of Gaussian integers of norm $n$ **up to units** is the product
> $$\#\{z:N(z)=n\}/\text{units}=\prod_j (e_j+1)=:D(n),$$
> the number of divisors of the "odd-split part" $\prod_j p_j^{e_j}$. (If any $q_k$ has odd exponent, $D(n)=0$: $n$ is not a sum of two squares — recovering the [[Thm - Sum of Two Squares|sum of two squares theorem]].)
>
> Finally pass from $z$'s to **representations**. Conjugation $z\mapsto\bar z$ sends the choice-vector $(s_j)_j$ to $(e_j-s_j)_j$, an involution on the $D(n)$ classes. The number of *unordered* representations $n=a^2+b^2$ is the number of orbits: $\lceil D(n)/2\rceil$ — half of $D(n)$, rounded up to account for the (rare) self-conjugate $z$ with every $s_j=e_j/2$. Equivalently, the classical formula counts *ordered* representations with signs: $r_2(n)=4\sum_{d\mid n}\chi(d)$ where $\chi$ is the non-trivial character mod $4$, the factor $4$ being the unit group $\{\pm1,\pm i\}$. For $n=65$: split primes $5,13$ each to exponent $1$, so $D(65)=(1+1)(1+1)=4$, and $\lceil 4/2\rceil=\mathbf 2$ representations — exactly $4^2+7^2$ and $1^2+8^2$.

> [!note]- Complete formal solution
> **Claim.** $65=1^2+8^2=4^2+7^2$ are its only two representations as a sum of two squares; the count is governed by the exponents of primes $\equiv 1\pmod 4$.
>
> A representation $n=a^2+b^2$ is a Gaussian integer $z=a+bi$ with $N(z)=n$, where $N$ is the multiplicative norm of the unique factorization domain $\mathbb{Z}[i]$, units $\{\pm1,\pm i\}$.
>
> *Factor $65$.* $5,13\equiv 1\pmod 4$ split: $5=(2+i)(2-i)$, $13=(3+2i)(3-2i)$, all four factors Gaussian primes of prime norm, conjugates non-associate.
>
> *Enumerate $z$ with $N(z)=65$.* By unique factorization, $z\bar z=5\cdot 13$ forces $z=u\,\pi_5\,\pi_{13}$, $u$ a unit, $\pi_5\in\{2+i,2-i\}$, $\pi_{13}\in\{3+2i,3-2i\}$: four classes up to units. Products (with $u=1$): $(2+i)(3+2i)=4+7i$, $(2+i)(3-2i)=8-i$, $(2-i)(3+2i)=8+i$, $(2-i)(3-2i)=4-7i$.
>
> *Collapse.* Conjugation $z\mapsto\bar z$ preserves $a^2+b^2$ and conjugates each factor, pairing $\{4\pm7i\}$ and $\{8\mp i\}$. The two orbits give $65=4^2+7^2$ and $65=8^2+1^2$; these are distinct since $\{16,49\}\ne\{1,64\}$. So exactly two representations.
>
> *General principle.* For $n=2^a\prod p_j^{e_j}\prod q_k^{2f_k}$ ($p_j\equiv1$, $q_k\equiv3\pmod4$), the ramified prime $2$ and each inert $q_k$ force unique factors $(1+i)^a$, $q_k^{f_k}$ into $z$ (no choice; odd exponent of a $q_k$ would make $n$ no sum of two squares). A split prime $p^e$ allows $z$ to contain $\pi^s\bar\pi^{e-s}$, $0\le s\le e$: $e+1$ choices. So $\#\{z:N(z)=n\}/\text{units}=\prod_j(e_j+1)$, and the number of unordered representations is $\lceil\tfrac12\prod_j(e_j+1)\rceil$. For $65$: $(1+1)(1+1)=4$, $\lceil 4/2\rceil=2$. $\blacksquare$

---

# Key Takeaways

**Counting decompositions becomes tractable the moment they are identified with factorisations in a unique factorization domain.** The exercise asks "how many ways" — a counting question — and the winning move is to realise that each way is an object in a ring: a representation $n=a^2+b^2$ *is* a Gaussian integer $z$ of norm $n$. Unique factorization then makes the set of such $z$ explicitly enumerable: $z$ is a unit times a product of Gaussian primes whose norms multiply to $n$, and uniqueness guarantees the enumeration has no repeats and no omissions. This "count by setting up a bijection with factorisations, then use unique factorization to list them" template is pervasive: it counts the divisors of an integer (a divisor is a sub-multiset of prime factors), counts representations by other quadratic forms via the relevant ring of integers, and underlies multiplicative number theory generally. The trigger is any "in how many ways can $n$ be written as ..." question where the "ways" can be encoded as elements or factorisations in a ring with unique factorization.

**The multiplicity lives entirely in the split primes, and each contributes its exponent plus one.** The decisive structural insight is that the three prime types behave completely differently as sources of choice. A ramified prime ($2$) and an inert prime ($q\equiv 3\pmod 4$) are *rigid*: the classification leaves no genuine choice of Gaussian factor, so they contribute a multiplicity of $1$ and do not affect the count. A split prime $p\equiv 1\pmod 4$ to the power $e$ is *flexible*: $z$ may contain $\pi^s\bar\pi^{e-s}$ for any $0\le s\le e$, giving $e+1$ options, because conjugate primes have equal norm so swapping them is invisible to $N(z)$. Hence the raw count of norm-$n$ Gaussian integers (up to units) is $\prod_{p\equiv 1}(e_p+1)$ — exactly the divisor count of the "$1\bmod 4$ part" of $n$. This is why a number like $5^4=625$ has many representations (one split prime, high exponent: $5$ choices) while $3\cdot 5=15$ has none ($3$ to an odd power kills it) and $9\cdot 5=45$ has few ($9=3^2$ rigid, $5$ to exponent $1$). Recognising "which primes are flexible and which are rigid" is the whole of the count.

**Conjugation is a symmetry of the problem, not a new solution — and quotienting by it is where the count is finally right.** The four products for $65$ look like four answers but are two, because $z$ and $\bar z$ describe the same unordered sum of squares: $\overline{a+bi}=a-bi$ leaves $\{a^2,b^2\}$ fixed. Crucially, conjugating a product conjugates every factor, so $z\mapsto\bar z$ corresponds to flipping *all* split-prime choices $s_j\mapsto e_j-s_j$ simultaneously. The genuine degrees of freedom are therefore the *relative* configurations of the conjugate-choices, not the absolute ones — and the representation count is the number of orbits of the choice-set under this involution, $\lceil D(n)/2\rceil$. The general lesson: when you count objects up to a symmetry, first count objects ignoring the symmetry, then identify the symmetry group precisely and divide (Burnside/orbit-counting), being careful about fixed points. Here the symmetry group acting on Gaussian integers is the $8$-element group generated by the four units and conjugation; the representation is the orbit, and miscounting comes from forgetting that conjugation is *not* independent of the per-prime choices but is their simultaneous flip.

**This exercise upgrades the sum-of-two-squares theorem from a yes/no test to an exact count, and exposes its mechanism.** The [[Thm - Sum of Two Squares|sum of two squares theorem]] says $n$ is representable if and only if every prime $\equiv 3\pmod 4$ occurs to an even power — a *decision*. The counting refinement shows *why*: an inert prime $q$ contributes $q^2$ to any norm, so $q$ must appear to an even power for $n$ to be a norm at all ($D(n)=0$ otherwise); and when representation is possible, the *number* of representations is $\lceil\tfrac12\prod_{p\equiv1}(e_p+1)\rceil$. The classical statement $r_2(n)=4\sum_{d\mid n}\chi_4(d)$ (with $\chi_4$ the non-trivial Dirichlet character mod $4$, the $4$ being the units $\pm1,\pm i$) is the same fact in analytic dress, and its appearance as a coefficient of the theta function $\theta(q)^2$ ties this ring-theoretic count to modular forms. The reusable principle is that an existence theorem proved via a ring with unique factorization almost always carries a *counting* refinement for free: the same factorisation that witnesses existence, enumerated, counts the witnesses — exhibited here, and equally for representations by $x^2+xy+y^2$ via the Eisenstein integers, or by other norm forms via their [[Def - Ring|rings]] of integers.
