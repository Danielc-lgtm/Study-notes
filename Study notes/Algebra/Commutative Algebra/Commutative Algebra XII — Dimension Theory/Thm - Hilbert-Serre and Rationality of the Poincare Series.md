---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - The Hilbert Function and Hilbert Polynomial"
  - "Def - Graded Ring and Graded Module"
  - "Def - Composition Series and Length"
  - "Def - Noetherian Ring"
  - "Def - Exact Sequence and Short Exact Sequence"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $A = \bigoplus_{n \geq 0} A_n$ be a Noetherian [[Def - Graded Ring and Graded Module|graded ring]], generated as an $A_0$-algebra by homogeneous $x_1, \dots, x_s$ with $x_i \in A_{k_i}$, $k_i > 0$, and with $A_0$ **Artinian**. Let $M = \bigoplus_{n} M_n \neq 0$ be a finitely generated graded $A$-module; each $M_n$ has finite [[Def - Composition Series and Length|length]] $\ell(M_n)$ over $A_0$. The [[Def - The Hilbert Function and Hilbert Polynomial|Poincaré series]] is $P(M, T) = \sum_{n \geq 0} \ell(M_n) T^n \in \mathbb{Z}[[T]]$. The full registry is on [[Commutative Algebra XII — Dimension Theory]].

---

# Statement

> **Theorem (Hilbert–Serre).** Let $A = \bigoplus_{n\geq 0} A_n$ be a Noetherian graded ring with $A_0$ Artinian, generated as an $A_0$-algebra by homogeneous elements $x_1,\dots,x_s$ of positive degrees $k_1,\dots,k_s$. For every finitely generated graded $A$-module $M$, the Poincaré series is a rational function:
> $$P(M, T) = \sum_{n \geq 0} \ell(M_n)\, T^n = \frac{f(T)}{\prod_{i=1}^{s}(1 - T^{k_i})}, \qquad f(T) \in \mathbb{Z}[T].$$
>
> In particular, all but finitely many coefficients $\ell(M_n)$ are determined by the finitely many coefficients of $f$, and the order $d(M)$ of the pole of $P(M,T)$ at $T = 1$ satisfies $0 \leq d(M) \leq s$.

When all $k_i = 1$ the denominator is $(1-T)^s$ and the pole order $d(M)$ controls the eventual polynomial growth of $\ell(M_n)$ — this is the bridge to the [[Thm - The Hilbert Polynomial|Hilbert polynomial]].

---

# Motivation

The Hilbert function $n \mapsto \ell(M_n)$ is an infinite sequence of integers, and on its face there is no reason it should be tame. This theorem says it is as tame as possible: the whole sequence is packaged in a rational function with a completely explicit denominator, depending only on the *degrees of the generators of the ring*, not on $M$. The numerator $f(T)$ carries all the module-specific information, and it is a polynomial — finite data. So the theorem is a finiteness statement: the infinitely many values of the Hilbert function are encoded in finitely many integers.

Why should one expect this? Because a finitely generated graded module is built from the ring by finitely many generators and relations, and the ring is built from $A_0$ by adjoining the $x_i$. Each $x_i$ acts on $M$ by raising degree by $k_i$, and on the generating-function side raising degree by $k_i$ is multiplication by $T^{k_i}$. So the algebraic relations that finitely present $M$ become relations among power series, forcing rationality with denominator $\prod(1 - T^{k_i})$ — one factor per generator, each factor recording "this generator shifts degree by $k_i$". The theorem is the precise form of the slogan *finite generation of the module is rationality of its generating function*.

The role this plays in the larger story is foundational. The pole order $d(M)$ at $T = 1$ — how badly the rational function blows up as $T \to 1^-$ — is the measure of dimension. A bigger pole means the partial sums $\sum_{n \leq N} \ell(M_n)$ grow faster, which means the module is "bigger" in the dimensional sense. The [[Thm - The Dimension Theorem for Noetherian Local Rings|dimension theorem]] will identify $d(G_{\mathfrak{m}}(A))$ with the Krull dimension; Hilbert–Serre is what makes $d$ well-defined in the first place, by guaranteeing $P$ is rational so that "pole order at $T=1$" even makes sense.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "$M$ is a finitely generated graded module over a Noetherian graded ring with Artinian degree-zero part". Several common situations are secretly instances.

The first disguised source is **the coordinate ring of a projective variety**. The property $B$ is "$A = k[X_0,\dots,X_n]/I$ for a homogeneous ideal $I$, with $M = A$". Here $A_0 = k$ is a field (the simplest Artinian ring, length $= \dim_k$), and $A$ is standard graded ($k_i = 1$), so $B \Rightarrow A$ immediately and Hilbert–Serre applies with denominator $(1-T)^{n+1}$ before cancellation. *Example problem:* compute the Poincaré series of a hypersurface $k[X_0,\dots,X_n]/(f)$ and read its dimension off the pole order — the answer is $\frac{1 - T^{\deg f}}{(1-T)^{n+1}} = \frac{1 + T + \cdots + T^{\deg f - 1}}{(1-T)^n}$, pole order $n$, dimension $n$.

The second disguised source is **the associated graded ring of a local ring**, $G_{\mathfrak{m}}(A) = \bigoplus_n \mathfrak{m}^n/\mathfrak{m}^{n+1}$. The property $B$ is "$(A,\mathfrak{m})$ is Noetherian local". Then $G_{\mathfrak{m}}(A)_0 = A/\mathfrak{m}$ is a field (Artinian), and $G_{\mathfrak{m}}(A)$ is generated in degree $1$ by the images of generators of $\mathfrak{m}$, so $B$ implies the hypothesis. The non-obviousness: a *non-graded* local ring produces a graded ring to which Hilbert–Serre applies, and this is the route by which the theorem feeds dimension theory. *Example problem:* this is exactly the setup of the dimension theorem.

The third disguised source is **any finitely generated graded module over $k[x_1,\dots,x_s]$ with assigned weights**. The property $B$ is "$M$ is presented by a finite graded free resolution". Since $A_0 = k$ and the $x_i$ have positive degrees $k_i$, Hilbert–Serre applies; the resolution even computes the numerator $f(T) = \sum_j (-1)^j \sum_p T^{(\text{degree of } p\text{-th generator of } j\text{-th syzygy module})}$ as an alternating sum, the **K-polynomial**. The non-obvious bridge: rationality is visibly inherited from the additivity of $\ell$ along the resolution. *Example problem:* compute the Hilbert series of $k[x,y]/(x^2, xy, y^2)$ from its resolution.

**Targets (Output Amplification)**

The conclusion is "$P(M,T)$ is rational with denominator $\prod(1-T^{k_i})$".

Combine the rational form with **partial fractions at $T = 1$** to get the Hilbert polynomial. The additional input $D$ is "all $k_i = 1$", so the denominator is $(1-T)^s$; writing $P(M,T) = f(T)(1-T)^{-d}$ with $f(1) \neq 0$ and expanding $(1-T)^{-d} = \sum_j \binom{j+d-1}{j}T^j$ yields that $\ell(M_n)$ is eventually a polynomial of degree $d - 1$. The further result $E$ is the [[Thm - The Hilbert Polynomial|Hilbert polynomial]], and the combination is non-obvious because rationality alone does not give a polynomial — you need the denominator to be a pure power of $(1-T)$.

Combine the pole order with **cancellation of $(1-T)$ against $f$** to compute dimension drops. The additional input $D$ is "a non-zero-divisor $x \in A_k$ acts on $M$", giving the exact sequence $0 \to M(-k) \xrightarrow{x} M \to M/xM \to 0$ and hence $P(M/xM, T) = (1 - T^k)P(M, T)$. The further result $E$ is $d(M/xM) = d(M) - 1$: multiplying the denominator by another $(1 - T^k)$, or equivalently killing a non-zero-divisor, drops the pole order by one. This is the engine of "one equation drops dimension by one".

Combine the explicit numerator with **the value $f(1)$** to read off multiplicity. The additional input $D$ is "$d(M) = d$ and $k_i = 1$"; then the leading coefficient of $\mathrm{HP}_M$ is $f(1)/(d-1)!$, so $f(1)$ — the numerator evaluated at $1$ — is the **degree** (multiplicity) of the module. The result $E$ is that the single number $f(1)$ controls the geometric degree, non-obvious because $f(1)$ is just an alternating sum of binomial coefficients from a resolution.

---

# Why Is It True

The mechanism is an **induction on the number of generators $s$, using one generator at a time to splice the Hilbert function into a short exact sequence and translate that sequence into a relation between Poincaré series.**

Start with the base case $s = 0$: then $A = A_0$ is Artinian and $M$ is a finitely generated $A_0$-module, so $M$ is concentrated in finitely many degrees (a finite set of homogeneous generators lives in bounded degree, and $A_0$ does not raise degree). Hence $\ell(M_n) = 0$ for large $n$, $P(M,T)$ is a *polynomial*, and the empty product in the denominator is $1$ — rationality is trivial.

Now the inductive step, which is the whole idea. Suppose the result holds with $s - 1$ generators, and consider $A$ with generators $x_1,\dots,x_s$. Single out the last generator $x_s \in A_{k_s}$ and look at what *multiplication by $x_s$* does. It is an $A_0$-linear map $M_n \xrightarrow{x_s} M_{n+k_s}$ in each degree, and it fits into a four-term exact sequence
$$0 \to K_n \to M_n \xrightarrow{x_s} M_{n+k_s} \to L_{n+k_s} \to 0,$$
where $K_n = \ker(x_s)$ in degree $n$ and $L = M/x_s M$ is the cokernel. The kernel $K$ and cokernel $L$ are both finitely generated graded modules, and — crucially — they are both **annihilated by $x_s$** (the kernel because $x_s$ kills it by definition; the cokernel because $x_s M$ is divided out). A module annihilated by $x_s$ is really a module over the smaller ring $A_0[x_1,\dots,x_{s-1}]$, with only $s-1$ generators. So the induction hypothesis applies to $K$ and $L$.

The bridge from the exact sequence to the series is **additivity of length**: in any exact sequence the alternating sum of lengths is zero, so $\ell(K_n) - \ell(M_n) + \ell(M_{n+k_s}) - \ell(L_{n+k_s}) = 0$. Multiply by $T^{n+k_s}$ and sum over $n$; the two "shifted" terms assemble into $T^{k_s}$ times series and the unshifted terms into plain series, giving the clean identity
$$(1 - T^{k_s})\, P(M, T) = P(L, T) - T^{k_s} P(K, T).$$
The right-hand side is rational with denominator $\prod_{i<s}(1 - T^{k_i})$ by induction; dividing by $(1 - T^{k_s})$ gives $P(M,T)$ the denominator $\prod_{i \leq s}(1-T^{k_i})$. That is the theorem.

**The one-line mechanism: multiplication by the last generator $x_s$ turns the Hilbert function into a four-term exact sequence whose kernel and cokernel are killed by $x_s$ (so live over fewer generators), and additivity of length converts that sequence into "$(1 - T^{k_s})P(M) = P(L) - T^{k_s}P(K)$" — one factor of the denominator per generator.**

---

# What Makes This Hard

The non-obvious step is realizing that the kernel and cokernel of multiplication-by-$x_s$ are modules over the *smaller* ring (because $x_s$ annihilates them), which is what makes the induction on $s$ go through — without this observation you cannot apply the inductive hypothesis. The most common error is sign/index bookkeeping when summing $\ell(M_{n+k_s})T^{n+k_s}$: one must shift the summation index correctly so the term reassembles as $T^{k_s}P(M,T)$ minus the missing low-degree terms, and the missing terms are exactly absorbed into the polynomial numerator. A second subtlety is remembering that $P(K,T)$ and $P(L,T)$ are rational by induction with $s-1$ factors, so the final denominator is $\prod_{i \leq s}$, not $\prod_{i < s}$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Induct on the number $s$ of algebra generators. The base case $s=0$ makes $P$ a polynomial. For the step, single out the last generator $x_s$, use multiplication by $x_s$ to build a degree-$n$ four-term exact sequence with kernel $K$ and cokernel $L = M/x_sM$, note both are killed by $x_s$ hence are $(s-1)$-generator modules, apply additivity of length, and sum into the recursion $(1-T^{k_s})P(M) = P(L) - T^{k_s}P(K)$.

**Subgoal decomposition:**

1. **Base case.** Show $P(M,T) \in \mathbb{Z}[T]$ when $s = 0$.
   - *Hint:* $A = A_0$ Artinian and $M$ finitely generated means $M$ lives in finitely many degrees.
   - *Why needed:* It anchors the induction; the empty denominator is $1$.

2. **The four-term sequence.** From $x_s : M_n \to M_{n+k_s}$, extract $0 \to K_n \to M_n \to M_{n+k_s} \to L_{n+k_s} \to 0$.
   - *Hint:* $K = \ker$, $L = \operatorname{coker} = M/x_sM$; exactness is the definition of kernel and cokernel.
   - *Why needed:* It is the object additivity of length will be applied to.

3. **$K$ and $L$ live over fewer generators.** Show $x_s K = 0$ and $x_s L = 0$, so both are finitely generated $A_0[x_1,\dots,x_{s-1}]$-modules.
   - *Hint:* $x_s$ kills the kernel by definition and kills the cokernel because $x_sM$ is divided out.
   - *Why needed:* This is what licenses the inductive hypothesis on $K, L$.

4. **Additivity and summation.** From $\ell(K_n) - \ell(M_n) + \ell(M_{n+k_s}) - \ell(L_{n+k_s}) = 0$, derive $(1-T^{k_s})P(M) = P(L) - T^{k_s}P(K)$.
   - *Hint:* Multiply by $T^{n+k_s}$, sum over $n$, and track the index shift.
   - *Why needed:* It is the recursion; dividing by $(1-T^{k_s})$ and applying induction finishes the proof.

---

# Lemma Decomposition

> [!note]- Lemma 1: Length is additive on exact sequences
> **Statement:** For an exact sequence $0 \to P_1 \to P_2 \to \cdots \to P_r \to 0$ of finite-length $A_0$-modules, $\sum_{i=1}^r (-1)^i \ell(P_i) = 0$.
>
> **Hint:** Reduce to the short-exact case $\ell(P) = \ell(P') + \ell(P'')$ and splice; for a four-term sequence insert the image of the middle map.
>
> **Why needed:** It is the bridge from the exact sequence of graded pieces to the numerical identity among lengths, which is then summed into the Poincaré-series recursion.
>
> > [!note]- Full proof
> > For a short exact sequence $0 \to P' \to P \to P'' \to 0$, a composition series of $P'$ followed by the preimage of a composition series of $P''$ is a composition series of $P$, so $\ell(P) = \ell(P') + \ell(P'')$. For a general exact sequence $0 \to P_1 \to \cdots \to P_r \to 0$, let $Z_i = \operatorname{im}(P_i \to P_{i+1}) = \ker(P_{i+1}\to P_{i+2})$. Each $Z_i$ has finite length (submodule of a finite-length module), and exactness gives short exact sequences $0 \to Z_{i-1} \to P_i \to Z_i \to 0$, so $\ell(P_i) = \ell(Z_{i-1}) + \ell(Z_i)$ with $Z_0 = Z_r = 0$. The alternating sum $\sum (-1)^i \ell(P_i)$ telescopes to $0$. For the four-term sequence $0 \to K_n \to M_n \to M_{n+k_s} \to L_{n+k_s} \to 0$ this reads $\ell(K_n) - \ell(M_n) + \ell(M_{n+k_s}) - \ell(L_{n+k_s}) = 0$.

> [!note]- Lemma 2: Kernel and cokernel of $x_s$ are modules over fewer generators
> **Statement:** $K = \ker(x_s : M \to M)$ and $L = M/x_sM$ are finitely generated graded modules, both annihilated by $x_s$, hence finitely generated graded $A_0[x_1,\dots,x_{s-1}]$-modules.
>
> **Hint:** $x_s$ kills $K$ by definition of kernel; $x_s$ kills $L$ because $x_s L = (x_s M + x_s M)/x_s M = 0$. Finite generation is from Noetherianity of $A$.
>
> **Why needed:** Being modules over the $(s-1)$-generator ring is exactly the hypothesis needed to apply the inductive step to $K$ and $L$.
>
> > [!note]- Full proof
> > $K$ is a graded submodule of the finitely generated module $M$ over the Noetherian ring $A$, hence finitely generated; $L$ is a quotient of $M$, hence finitely generated. For $m \in K$, $x_s m = 0$ by definition, so $x_s K = 0$. For $\bar m \in L = M/x_sM$, $x_s \bar m = \overline{x_s m} \in \overline{x_s M} = 0$, so $x_s L = 0$. A graded module annihilated by $x_s$ is naturally a graded module over $A/(x_s)$, and since $A = A_0[x_1,\dots,x_s]$, the quotient $A/(x_s)$ is generated over $A_0$ by the images of $x_1,\dots,x_{s-1}$ — that is, $K$ and $L$ are finitely generated graded modules over a ring with $s-1$ algebra generators.

> [!note]- Lemma 3: The Poincaré-series recursion
> **Statement:** $(1 - T^{k_s})\, P(M, T) = P(L, T) - T^{k_s} P(K, T)$.
>
> **Hint:** Multiply the length identity of Lemma 1 by $T^{n+k_s}$ and sum over $n \in \mathbb{Z}$ (with $M_n = 0$ for $n < 0$).
>
> **Why needed:** It is the recursion that, combined with the inductive hypothesis on $K$ and $L$, yields rationality of $P(M,T)$ with the predicted denominator.
>
> > [!note]- Full proof
> > By Lemma 1, $\ell(M_{n+k_s}) - T^0\ell(M_n)$ rearranges with the kernel/cokernel terms. Write the identity as $\ell(M_{n+k_s}) - \ell(M_n) = \ell(L_{n+k_s}) - \ell(K_n)$. Multiply by $T^{n+k_s}$:
> > $$\ell(M_{n+k_s})T^{n+k_s} - T^{k_s}\ell(M_n)T^n = \ell(L_{n+k_s})T^{n+k_s} - T^{k_s}\ell(K_n)T^n.$$
> > Sum over all $n \in \mathbb{Z}$ (modules vanish in negative degrees, so the sums are over $n \geq 0$ up to finitely many boundary terms that are absorbed into the polynomial numerator). The left side telescopes to $(1 - T^{k_s})P(M,T)$; the right side is $P(L,T) - T^{k_s}P(K,T)$. Hence $(1-T^{k_s})P(M,T) = P(L,T) - T^{k_s}P(K,T)$.

---

# Formal Proof

> [!note]- Complete formal proof
> We induct on the number $s$ of homogeneous algebra generators of $A$ over $A_0$.
>
> **Step 0 — well-definedness of $\ell(M_n)$.** Since $M$ is a finitely generated module over the Noetherian ring $A$, each graded piece $M_n$ is a finitely generated $A_0$-module; since $A_0$ is Artinian, every finitely generated $A_0$-module has finite length, so $\ell(M_n) < \infty$ and $P(M,T) \in \mathbb{Z}[[T]]$ is well-defined.
>
> **Base case $s = 0$.** Then $A = A_0$. A finite homogeneous generating set of $M$ lies in degrees $\leq n_0$ for some $n_0$, and $A_0$ raises no degree, so $M_n = 0$ for $n > n_0$. Hence $P(M,T) = \sum_{n=0}^{n_0}\ell(M_n)T^n \in \mathbb{Z}[T]$, which is $f(T)/1$, the empty product. Rationality holds.
>
> **Inductive step.** Assume the theorem for graded rings with $s-1$ generators. Let $A = A_0[x_1,\dots,x_s]$, $x_i \in A_{k_i}$. Multiplication by $x_s$ gives, in each degree $n$, the four-term exact sequence of $A_0$-modules
> $$0 \to K_n \to M_n \xrightarrow{\;x_s\;} M_{n+k_s} \to L_{n+k_s} \to 0,$$
> with $K = \ker(x_s)$ and $L = M/x_s M$. By **Lemma 2**, $K$ and $L$ are finitely generated graded modules over $A_0[x_1,\dots,x_{s-1}]$, so by the inductive hypothesis $P(K,T)$ and $P(L,T)$ are rational with denominator $\prod_{i<s}(1 - T^{k_i})$. By **Lemma 1** (additivity of length) and **Lemma 3**,
> $$(1 - T^{k_s})\,P(M,T) = P(L,T) - T^{k_s}P(K,T).$$
> The right side is rational with denominator $\prod_{i<s}(1-T^{k_i})$, so
> $$P(M,T) = \frac{P(L,T) - T^{k_s}P(K,T)}{1 - T^{k_s}} = \frac{f(T)}{\prod_{i=1}^{s}(1 - T^{k_i})}$$
> for some $f \in \mathbb{Z}[T]$ (clear denominators; the numerator is an integer polynomial because all the $\ell(\cdot)$ are integers). This completes the induction.
>
> **Pole order.** Cancelling common factors of $(1-T)$, the pole order $d(M)$ of $P(M,T)$ at $T=1$ satisfies $0 \leq d(M) \leq s$. The non-negativity $d(M) \geq 0$ holds because if $P(M,T)$ vanished at $T=1$, then $\lim_{T\to1^-}P(M,T) = 0 \geq \lim_{T\to1^-}\ell(M_k)T^k = \ell(M_k)$ forces $\ell(M_k) = 0$ for all $k$, so $M = 0$, contradicting $M \neq 0$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Generating functions in combinatorics.** The Poincaré series of $k[x_1,\dots,x_s]$ is $(1-T)^{-s} = \sum_n \binom{n+s-1}{s-1}T^n$, which is the generating function for the number of monomials of degree $n$ — equivalently the number of ways to write $n$ as an ordered sum of $s$ non-negative integers (stars and bars). Hilbert–Serre with general $k_i$ is the statement that the generating function for **partitions into parts of sizes $k_1,\dots,k_s$** is rational with denominator $\prod(1-T^{k_i})$ — the classical theory of restricted partitions, here recovered as the Hilbert series of a weighted polynomial ring. The non-obvious bridge: a partition-counting problem is a Hilbert-function problem for a graded ring.

**Ehrhart polynomials of lattice polytopes.** For a lattice polytope $P$, the number of lattice points in the dilate $nP$ is the Ehrhart quasi-polynomial, and its generating function $\sum_n |nP \cap \mathbb{Z}^d| T^n$ is rational. This is Hilbert–Serre applied to the semigroup ring of the cone over $P$ (a graded ring, generally with nonstandard grading), and the pole order at $T=1$ is $\dim P + 1$. The application is non-obvious because polytope point-counting is geometric, yet it is governed by the same rationality theorem.

**Graded representation theory and characters.** For a finite group $G$ acting on a polynomial ring $S = k[V]$, the graded character $\sum_n (\text{character of } S_n) T^n$ is rational by Molien's theorem, $\frac{1}{|G|}\sum_{g}\frac{1}{\det(1 - Tg)}$. This is Hilbert–Serre refined to track $G$-isotypic pieces, and the invariant ring $S^G$ has rational Hilbert series with poles encoding $\dim V$. The bridge: Molien's formula is the equivariant Hilbert series, rational for exactly the Hilbert–Serre reason.

---

# Bridges

- **[[Thm - The Hilbert Polynomial|The Hilbert polynomial]]** — the immediate downstream consequence. Once $P(M,T) = f(T)/(1-T)^d$ (standard grading, pole order $d$), expanding $(1-T)^{-d}$ as a binomial series shows $\ell(M_n)$ is eventually a polynomial of degree $d-1$. Hilbert–Serre supplies the rational form; the Hilbert polynomial extracts the eventual polynomial from it. The two together are the analytic content of "$\ell(M_n)$ grows like $n^{d-1}$".

- **[[Thm - The Dimension Theorem for Noetherian Local Rings|The dimension theorem]]** — the ultimate target. Applied to $G_{\mathfrak{m}}(A) = \bigoplus \mathfrak{m}^n/\mathfrak{m}^{n+1}$, Hilbert–Serre makes the pole order $d(G_{\mathfrak{m}}(A))$ well-defined, and the dimension theorem proves it equals $\dim A$. So Hilbert–Serre is the technical foundation on which the equality of the three dimension-invariants rests.

- **[[Def - The Associated Graded Ring and the Rees Algebra|The associated graded ring]]** — the construction that turns a local ring into a graded one to which Hilbert–Serre applies. Filtering $A$ by powers of $\mathfrak{m}$ and taking the associated graded ring linearizes the local structure into a standard graded $k$-algebra, exactly the input Hilbert–Serre wants. The Rees algebra is the parallel construction for a general $\mathfrak{m}$-primary ideal.

- **[[Thm - The Artin-Rees Lemma|Artin–Rees]]** — used in the dimension-theory proofs to compare the Hilbert functions of $\mathfrak{m}$-primary ideals: it guarantees that the $\mathfrak{m}$-adic and $\mathfrak{q}$-adic filtrations are equivalent, so their Hilbert–Serre pole orders agree. This is what lets one replace $\mathfrak{m}$ by any $\mathfrak{m}$-primary ideal without changing $d$.

---

# Unlocked by This

> [!tip] Hilbert series and free resolutions *(from Homological Algebra)*
> The numerator $f(T)$ is computed from any finite graded free resolution of $M$ as an alternating sum: $f(T) = \sum_j (-1)^j \sum_p T^{a_{j,p}}$ where $a_{j,p}$ are the degrees of the free generators at homological stage $j$. This is the **K-polynomial**, and its rationality is the generating-function shadow of the **Hilbert syzygy theorem** (every finitely generated graded $k[x_1,\dots,x_s]$-module has a finite free resolution of length $\leq s$). Hilbert–Serre is thus the numerical face of finite projective dimension.

> [!tip] Serre's coherent sheaf cohomology *(from Algebraic Geometry)*
> Serre's GAGA-era insight is that the Poincaré series of a projective coordinate ring equals $\sum_n \chi(\mathcal{F}(n))T^n$ for the associated coherent sheaf $\mathcal{F}$, with the Euler characteristic $\chi$ replacing $\dim_k$ once higher cohomology is accounted for. The rationality of $P$ then reflects the finiteness of sheaf cohomology on projective space, and the pole at $T=1$ is the dimension of the support of $\mathcal{F}$. This is the route from elementary length-counting to the cohomological theory of dimension.
