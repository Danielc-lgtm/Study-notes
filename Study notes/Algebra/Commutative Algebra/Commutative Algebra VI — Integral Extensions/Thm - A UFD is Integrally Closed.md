---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Unique Factorization Domain"
  - "Def - Integral Domain"
  - "Def - Field of Fractions"
  - "Def - Integral Closure and Normal Domain"
  - "Def - Integral Element and Integral Extension"
  - "Def - Irreducible and Prime Elements"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $A$ be a [[Def - Unique Factorization Domain|unique factorization domain]] (UFD), $\operatorname{Frac}(A)$ its [[Def - Field of Fractions|field of fractions]]. For $x \in \operatorname{Frac}(A)$, "lowest terms" $x = a/b$ means $a, b \in A$, $b \neq 0$, and no [[Def - Irreducible and Prime Elements|prime element]] $p$ of $A$ divides both $a$ and $b$ (equivalently $\gcd(a, b)$ is a unit). Recall that in a UFD, irreducible $=$ prime, and every nonzero non-unit factors uniquely into primes. "[[Def - Integral Closure and Normal Domain|Integrally closed]]" (normal) means $\overline A = A$ inside $\operatorname{Frac}(A)$. The full registry is on [[Commutative Algebra VI — Integral Extensions]].

---

# Statement

> **Theorem (a UFD is integrally closed).** Every unique factorization domain is integrally closed in its field of fractions: if $A$ is a UFD and $x \in \operatorname{Frac}(A)$ is integral over $A$, then $x \in A$. Equivalently, the integral closure $\overline A$ of a UFD $A$ equals $A$ — every UFD is **normal**.

> **Corollary.** $\mathbb{Z}$, every [[Def - Principal Ideal Domain|principal ideal domain]], and every polynomial ring $k[T_1, \dots, T_n]$ over a field is integrally closed; so the only rational/polynomial functions integral over these rings are their own elements.

---

# Motivation

This theorem is the supply line of "normal" rings, and it is what lets you *disprove* integrality in one line. The structural theorems of the chapter tell you the integral closure $\overline A$ is a ring sitting between $A$ and $\operatorname{Frac}(A)$; this theorem tells you *when that ring is $A$ itself*, so that there is nothing in the fraction field to be integral beyond the obvious. The class it certifies is exactly the rings you most often work in — $\mathbb{Z}$, polynomial rings, PIDs — so in practice "is $x$ integral over $A$?" reduces, whenever $A$ is a UFD, to the trivial "is $x \in A$?".

The result generalises a fact you already trust. Over $\mathbb{Z}$ it says: the only rationals that are algebraic integers are the ordinary integers — [[Thm - Rational Algebraic Integers are Integers|a rational algebraic integer is an integer]]. The proof of that special case is the *rational root theorem*: a monic integer polynomial's rational roots are integers, because clearing denominators forces the denominator to divide the leading coefficient $1$. This theorem is that argument run in any UFD, with "the denominator divides the leading coefficient" replaced by "any prime dividing the denominator divides the numerator, contradicting lowest terms". The role of unique factorization is precisely to make "lowest terms" meaningful and stable: in a UFD you can write any fraction with coprime numerator and denominator, and coprimality is exactly the lever the proof pulls.

Geometrically the theorem is why **smooth varieties are normal**. A regular local ring is a UFD (the Auslander–Buchsbaum theorem), so a smooth variety's local rings are UFDs, hence normal — normality is "smoothness in codimension one", the part of smoothness that pure integral closure can detect. The contrapositive is just as useful: a *non-normal* ring cannot be a UFD, so the cusp ring $k[t^2, t^3]$ and $\mathbb{Z}[\sqrt5]$ — both non-normal — are immediately known not to be UFDs without exhibiting a failure of factorization. The theorem thus both *certifies* good rings (UFD $\Rightarrow$ normal) and *diagnoses* bad ones (non-normal $\Rightarrow$ not a UFD).

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$A$ is a UFD", but it is reached through several recognisable situations.

The first disguised source is **$A$ is a PID** (in particular $\mathbb{Z}$, $k[T]$, a DVR). The property $B$ is "every ideal is principal", which gives unique factorization ([[Thm - Principal Ideal Domains are Unique Factorization Domains|PID ⇒ UFD]]), hence normality. Nonobvious because principal-ideal-ness is an ideal-theoretic condition that secretly yields the element-theoretic lowest-terms argument. *Example problem:* show $\mathbb{Z}_{(p)}$ (a DVR, hence PID) is integrally closed — used in localizing normality.

The second disguised source is **$A$ is a polynomial ring over a UFD/field**. The property $B$ is "$A = R[T_1, \dots, T_n]$ with $R$ a UFD"; by [[Thm - Polynomial Rings over a UFD|polynomial rings over a UFD are UFDs]] (Gauss), $A$ is a UFD, hence normal. Nonobvious because it certifies *all* coordinate rings of affine space as normal in one stroke. *Example problem:* show $k[x, y]$ is integrally closed — affine plane is normal.

The third disguised source is **$A$ is regular local** (smooth point). The property $B$ is "the local ring at a smooth point is regular", which by Auslander–Buchsbaum is a UFD, hence normal. Nonobvious because it routes a *geometric* smoothness hypothesis through deep homological algebra to normality. *Example problem:* a smooth variety is normal, so its function theory is well-behaved in codimension one.

**Targets (Output Amplification)**

The conclusion is "$A$ is integrally closed".

Combine "$A$ normal" with **the sandwich for computing closures**. To find $\overline B$ for a non-normal $B$, propose a candidate $A$ with $B \subseteq A \subseteq \operatorname{Frac}(B)$, show $A$ is integral over $B$ and $A$ is a UFD (hence normal). Then $\overline B \subseteq \overline A = A$, so $\overline B = A$. The further result $E$ is an *actual computed normalization* — $\overline{k[t^2,t^3]} = k[t]$, $\overline{\mathbb{Z}[\sqrt5]} = \mathbb{Z}[\tfrac{1+\sqrt5}2]$. Nonobvious because normality of the candidate is what *caps* the closure from above.

Combine "$A$ normal" with **localization**. Normality localizes: $A$ normal $\Rightarrow A_{\mathfrak p}$ normal, and conversely normality is local. The further result $E$ is the local criterion "$A$ normal iff every $A_{\mathfrak m}$ normal" (Example Sheet 3 Q7), reducing global normality to local rings, often DVRs. Nonobvious because it lets a global property be checked one prime at a time.

Combine "non-normal $\Rightarrow$ not UFD" with **a singularity**. If a coordinate ring is non-normal (its variety is singular in codimension one), it cannot be a UFD; so its class group / divisor theory is nontrivial. The further result $E$ links failure of unique factorization to geometric singularity and to the **class group** measuring it. Nonobvious because it turns an algebraic non-factorization into a geometric singularity statement.

---

# Why Is It True

**A monic equation says the leading coefficient is $1$, so when you clear denominators the only prime that could appear in the denominator must already divide the numerator — and in lowest terms it cannot.** That is the whole proof, and unique factorization is what makes "lowest terms" and "prime divides" precise.

Take $x \in \operatorname{Frac}(A)$ integral, and write it in *lowest terms* $x = a/b$ — possible because $A$ is a UFD, so we can cancel common prime factors until $a, b$ share none. Suppose $x \notin A$; then $b$ is a non-unit, so some prime $p$ divides $b$, and (lowest terms) $p \nmid a$. Plug $x = a/b$ into the monic equation $x^n + a_1 x^{n-1} + \cdots + a_n = 0$ and multiply through by $b^n$:
$$a^n + a_1 a^{n-1} b + a_2 a^{n-2} b^2 + \cdots + a_n b^n = 0,$$
so
$$a^n = -b\,(a_1 a^{n-1} + a_2 a^{n-2} b + \cdots + a_n b^{n-1}).$$
The right-hand side is divisible by $b$, hence by the prime $p$. So $p \mid a^n$. But $p$ is prime, so $p \mid a$ — contradicting $p \nmid a$. The contradiction came *only* from assuming $x \notin A$; therefore $x \in A$.

**The one-line mechanism: monic-ness puts $a^n$ (a pure power of the numerator) alone on one side, and every other term carries a factor of $b$; so any prime in $b$ must divide $a^n$, hence $a$ — impossible in lowest terms.** The single place monic-ness is used is in isolating $a^n$ with coefficient $1$: if the leading coefficient were a non-unit $a_0$, you would only get $a_0 a^n$ divisible by $p$, and $p$ might divide $a_0$ rather than $a$ — which is exactly why $\tfrac12$ (with $a_0 = 2$, $p = 2 \mid a_0$) *is* algebraic but not integral. Unique factorization enters in three places: to write lowest terms, to know $p \mid b$ exists when $b$ is a non-unit, and to pass from $p \mid a^n$ to $p \mid a$ (primality).

---

# What Makes This Hard

The proof is short, so the difficulty is *remembering that lowest terms is the entire engine* and that it requires unique factorization to even formulate. The non-obvious step is isolating $a^n$ on one side — multiplying by $b^n$ and moving every $b$-containing term across — so that monic-ness shows up as "$a^n$ has coefficient $1$". The most common error is to forget *why* unique factorization is needed and try to run the same argument in a general domain, where "lowest terms" may not exist and "$p \mid a^n \Rightarrow p \mid a$" can fail (this is exactly where $\mathbb{Z}[\sqrt5]$, not a UFD, slips through and admits the integral element $\tfrac{1+\sqrt5}2 \notin \mathbb{Z}[\sqrt5]$).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Write the integral element in lowest terms $x = a/b$ using unique factorization. Assume $x \notin A$, so a prime $p$ divides $b$ but not $a$. Clear denominators in the monic equation to isolate $a^n$; the rest is divisible by $b$ hence $p$, forcing $p \mid a$, a contradiction. Hence $x \in A$.

**Subgoal decomposition:**

1. **Lowest terms.** Write $x = a/b$ with $a, b$ coprime (no common prime).
   - *Hint:* In a UFD, cancel shared prime factors from numerator and denominator until none remain.
   - *Why needed:* Coprimality is the lever; "$p \nmid a$" is what the final contradiction uses.

2. **Clear denominators, isolate $a^n$.** From the monic equation, derive $a^n = -b(\cdots)$.
   - *Hint:* Substitute $x = a/b$, multiply by $b^n$, move all terms but $a^n$ to the other side; monic-ness leaves $a^n$ with coefficient $1$.
   - *Why needed:* It exhibits $a^n$ as a multiple of $b$, hence of any prime $p \mid b$.

3. **Primality contradiction.** Conclude $p \mid a$, contradicting lowest terms.
   - *Hint:* $p \mid a^n$ and $p$ prime give $p \mid a$; but $p \nmid a$. So $b$ has no prime factor — $b$ is a unit — and $x = a/b \in A$.
   - *Why needed:* It is the conclusion.

---

# Lemma Decomposition

> [!note]- Lemma 1: Lowest-terms representation in a UFD
> **Statement:** In a UFD $A$, every $x \in \operatorname{Frac}(A)$ can be written $x = a/b$ with $a, b \in A$, $b \neq 0$, and no prime of $A$ dividing both $a$ and $b$.
>
> **Hint:** Start from any representation and cancel common prime factors.
>
> **Why needed:** It supplies the coprimality used in the final contradiction; it is also where unique factorization is essential.
>
> > [!note]- Full proof
> > Write $x = a_0 / b_0$ with $a_0, b_0 \in A$, $b_0 \neq 0$. Factor $a_0$ and $b_0$ into primes (possible and unique in a UFD). Cancel each prime appearing in both factorizations — i.e. divide $a_0$ and $b_0$ by their gcd $d = \gcd(a_0, b_0)$ (well-defined up to units in a UFD), obtaining $a = a_0/d$, $b = b_0/d$. Then $x = a/b$ and no prime divides both $a$ and $b$, for such a prime would have survived the cancellation. (If $b$ is a unit, $x = a b^{-1} \in A$ already.)

> [!note]- Lemma 2: Clearing denominators isolates the numerator power
> **Statement:** If $x = a/b$ satisfies the monic $x^n + a_1 x^{n-1} + \cdots + a_n = 0$ with $a_i \in A$, then $a^n = -b\,(a_1 a^{n-1} + a_2 a^{n-2} b + \cdots + a_n b^{n-1})$ in $A$.
>
> **Hint:** Substitute and multiply through by $b^n$; gather all terms but the leading one.
>
> **Why needed:** It exhibits $a^n$ as divisible by $b$, the crux that monic-ness makes possible.
>
> > [!note]- Full proof
> > Substituting $x = a/b$ into the monic equation and multiplying by $b^n$:
> > $$a^n + a_1 a^{n-1} b + a_2 a^{n-2} b^2 + \cdots + a_n b^n = 0.$$
> > (The leading term $x^n \cdot b^n = a^n$ has coefficient $1$ — this is where monic-ness is used.) Every term except $a^n$ contains a factor of $b$, so moving them across,
> > $$a^n = -\big(a_1 a^{n-1} b + a_2 a^{n-2} b^2 + \cdots + a_n b^n\big) = -b\,\big(a_1 a^{n-1} + a_2 a^{n-2} b + \cdots + a_n b^{n-1}\big),$$
> > an element of $A$ divisible by $b$.

> [!note]- Lemma 3: A prime in the denominator divides the numerator
> **Statement:** With $x = a/b$ in lowest terms and $a^n$ divisible by $b$, if $b$ is a non-unit then a contradiction follows.
>
> **Hint:** A non-unit $b$ has a prime factor $p$; $p \mid a^n$ and primality give $p \mid a$, against lowest terms.
>
> **Why needed:** It forces $b$ to be a unit, i.e. $x \in A$.
>
> > [!note]- Full proof
> > Suppose $b$ is a non-unit. In a UFD, a nonzero non-unit has a prime factor; let $p \mid b$ be prime. By Lemma 2, $b \mid a^n$, so $p \mid a^n$. Since $p$ is prime, $p \mid a$. But lowest terms (Lemma 1) says no prime divides both $a$ and $b$, while $p$ divides both — contradiction. Hence $b$ is a unit, and $x = a b^{-1} \in A$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $A$ be a UFD and $x \in \operatorname{Frac}(A)$ integral over $A$, say
> $$x^n + a_1 x^{n-1} + \cdots + a_n = 0, \qquad a_i \in A,\ n \geq 1.$$
> By Lemma 1 write $x = a/b$ in lowest terms ($a, b \in A$, $b \neq 0$, no prime divides both). By Lemma 2, clearing denominators gives
> $$a^n = -b\,(a_1 a^{n-1} + a_2 a^{n-2} b + \cdots + a_n b^{n-1}),$$
> so $b \mid a^n$. By Lemma 3, if $b$ were a non-unit, a prime $p \mid b$ would satisfy $p \mid a^n$, hence $p \mid a$ (primality), contradicting lowest terms. So $b$ is a unit and $x = a b^{-1} \in A$.
>
> Therefore every $x \in \operatorname{Frac}(A)$ integral over $A$ lies in $A$: the UFD $A$ is integrally closed. $\blacksquare$
>
> ---
> **Corollary.** $\mathbb{Z}$ and every PID are UFDs ([[Thm - Principal Ideal Domains are Unique Factorization Domains]]), and $k[T_1, \dots, T_n]$ is a UFD ([[Thm - Polynomial Rings over a UFD]], by induction from $k$ a field); all are therefore integrally closed. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The rational root theorem.** Specialising to $A = \mathbb{Z}$: a monic integer polynomial's rational roots are integers, and more generally a root $p/q$ (lowest terms) of $c_0 T^n + \cdots + c_n$ has $q \mid c_0$, $p \mid c_n$. This theorem *is* the rational root theorem freed of $\mathbb{Z}$, with "lowest terms" and "prime divides" supplied by unique factorization. The application is nonobvious because the elementary rational root theorem is revealed as a special case of normality of a UFD.

**Eisenstein and irreducibility.** The lowest-terms/clearing-denominators technique here is a cousin of the manipulations in [[Thm - Eisenstein's Criterion|Eisenstein's criterion]] and Gauss's lemma, where divisibility of coefficients by a prime forces conclusions about factorization. Recognising the shared mechanism — track a single prime through a cleared-denominator equation — transfers between proving integrality facts and proving irreducibility. The application is nonobvious because the two appear in different parts of the syllabus.

**Class groups and the failure of normality.** A non-normal domain is not a UFD, so its **divisor class group** is nontrivial; conversely, a normal Noetherian domain is a UFD iff its class group vanishes. Using "non-normal $\Rightarrow$ not UFD" to detect non-trivial class groups (e.g. for $\mathbb{Z}[\sqrt{-5}]$, $k[x,y,z]/(xy-z^2)$) is a standard diagnostic. The application is nonobvious because it links the *element*-level integral closure to the *ideal*-level class group.

**Smoothness implies normality in geometry.** Via Auslander–Buchsbaum (regular local $\Rightarrow$ UFD) and this theorem, smooth points are normal points — so the function theory of a smooth variety has no "missing" integral functions. The application is nonobvious because it bridges a homological fact (regular $\Rightarrow$ UFD) to a geometric one (smooth $\Rightarrow$ normal) through this theorem.

---

# Bridges

- **[[Thm - Rational Algebraic Integers are Integers|A rational algebraic integer is an integer]]** — the special case $A = \mathbb{Z}$. That theorem's proof *is* this theorem's proof with the rational root theorem in place of the general lowest-terms argument; this page generalises it from $\mathbb{Z}$ to every UFD by replacing "denominator divides leading coefficient $1$" with "prime in denominator divides numerator".

- **[[Thm - Principal Ideal Domains are Unique Factorization Domains|PID ⇒ UFD]]** and **[[Thm - Polynomial Rings over a UFD|polynomial rings over a UFD are UFDs]]** — the two supply lines that turn this theorem into the corollary. They are what certify $\mathbb{Z}$, PIDs, DVRs, and all polynomial rings as normal, populating the world with normal rings.

- **[[Def - Integral Closure and Normal Domain|Integral closure and normal domain]]** — this theorem is the primary *source* of normal rings, and its contrapositive (non-normal $\Rightarrow$ not UFD) the primary *diagnostic* of non-normal ones. The sandwich method for computing $\overline A$ relies on capping with a known-normal (UFD) candidate.

- **[[Thm - The Integral Closure is a Subring|The integral closure is a subring]]** — the complementary statement: that theorem builds $\overline A$ as a ring between $A$ and $\operatorname{Frac}(A)$; this one says $\overline A = A$ exactly when $A$ is "UFD-good". Used together to compute normalizations: build the candidate as a ring, cap it by its UFD-normality.

---

# Unlocked by This

> [!tip] Smooth implies normal; Serre's criterion *(from Algebraic Geometry)*
> Via Auslander–Buchsbaum (regular local rings are UFDs), this theorem gives **smooth $\Rightarrow$ normal**, and normality is precisely "smooth in codimension one" by **Serre's criterion** ($R_1 + S_2$). So normalization resolves exactly the codimension-one singularities, and the discrepancy between normal and smooth is the higher-codimension singular locus. This is the geometric meaning of normality, developed alongside the singularity theory of varieties.

> [!tip] Dedekind domains and unique factorization of ideals *(from Algebraic Number Theory)*
> A Noetherian normal domain of dimension one is a **Dedekind domain**, where ideals factor uniquely into primes even though elements need not. Since rings of integers $\mathcal{O}_K$ are normal (integral closures) and one-dimensional Noetherian, this theorem (via normality) is one of the three pillars making $\mathcal{O}_K$ Dedekind; see [[Commutative Algebra XIII — Dedekind Domains and DVRs]].
