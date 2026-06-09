---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Krull Dimension and Height"
  - "Def - System of Parameters"
  - "Def - The Hilbert Function and Hilbert Polynomial"
  - "Def - Local Ring and Residue Field"
  - "Def - Noetherian Ring"
  - "Thm - Hilbert-Serre and Rationality of the Poincare Series"
  - "Thm - The Hilbert Polynomial"
  - "Thm - The Artin-Rees Lemma"
  - "Def - Primary Ideal"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $(A, \mathfrak{m})$ be a Noetherian [[Def - Local Ring and Residue Field|local ring]] with maximal ideal $\mathfrak{m}$ and residue field $\kappa = A/\mathfrak{m}$. We write $\dim A$ for the [[Def - Krull Dimension and Height|Krull dimension]]. An ideal $\mathfrak{q}$ is **$\mathfrak{m}$-primary** if $\sqrt{\mathfrak{q}} = \mathfrak{m}$; equivalently $\mathfrak{m}^t \subseteq \mathfrak{q} \subseteq \mathfrak{m}$ for some $t \geq 1$, and then $A/\mathfrak{q}$ is Artinian. We write $\delta(\mathfrak{q})$ for the minimal number of generators of $\mathfrak{q}$, and
$$\delta(A) = \min\{\delta(\mathfrak{q}) : \mathfrak{q} \text{ is } \mathfrak{m}\text{-primary}\}.$$
We write $G_{\mathfrak{m}}(A) = \bigoplus_{n \geq 0} \mathfrak{m}^n/\mathfrak{m}^{n+1}$ for the [[Def - Graded Ring and Graded Module|associated graded ring]], a standard graded $\kappa$-algebra, and $d(G_{\mathfrak{m}}(A))$ for the order of the pole at $T = 1$ of its [[Def - The Hilbert Function and Hilbert Polynomial|Poincaré series]] — equivalently $1 + \deg$ of the **Hilbert–Samuel polynomial** $n \mapsto \ell(A/\mathfrak{m}^n)$. The full registry is on [[Commutative Algebra XII — Dimension Theory]].

---

# Statement

> **Theorem (Dimension theorem).** For a Noetherian local ring $(A, \mathfrak{m})$, the three integers
> $$\dim A = d(G_{\mathfrak{m}}(A)) = \delta(A)$$
> all coincide:
> - $\dim A$ — the **Krull dimension**, the length of the longest chain of prime ideals;
> - $d(G_{\mathfrak{m}}(A))$ — the **Hilbert–Samuel degree**, the growth rate of $\ell(A/\mathfrak{m}^n)$ as a polynomial in $n$;
> - $\delta(A)$ — the **least number of generators** of an $\mathfrak{m}$-primary ideal.
>
> In particular $\dim A < \infty$, and there exists a [[Def - System of Parameters|system of parameters]]: $d = \dim A$ elements $x_1, \dots, x_d \in \mathfrak{m}$ generating an $\mathfrak{m}$-primary ideal, and no fewer suffice.

The proof establishes the cycle of inequalities $\delta(A) \geq d(G_{\mathfrak{m}}(A)) \geq \dim A \geq \delta(A)$, each a separate proposition, which forces all three to be equal.

---

# Motivation

Three completely different ideas each try to capture what "dimension" should mean for a local ring, and the miracle is that they agree. The first is *combinatorial*: how long a chain of irreducible subvarieties can you stack inside the space? That is the Krull dimension, $\dim A$ — honest, geometric, but almost impossible to compute directly because enumerating all chains of primes is hopeless. The second is *analytic*: how fast does the ring grow as you look at higher and higher infinitesimal neighbourhoods of the point? Measure $\ell(A/\mathfrak{m}^n)$, the "number of functions modulo order-$n$ vanishing", and read off its polynomial growth rate $d(G_{\mathfrak{m}}(A))$. The third is *constructive*: how few equations does it take to cut the point out — to find functions whose only common zero is the point itself? That is $\delta(A)$, the minimal size of a generating set of an $\mathfrak{m}$-primary ideal.

Each is natural, and each is useless without the others. The Krull dimension is the *definition* you want but cannot compute. The Hilbert–Samuel degree is *computable* — you count lengths and interpolate a polynomial — but on its face has nothing to do with chains of primes. And $\delta(A)$ is the one you can *bound from above by exhibiting a single ideal*: produce any $\mathfrak{m}$-primary ideal with $r$ generators and you have proved $\delta(A) \leq r$. The dimension theorem welds these three into one number, so that the geometric notion you care about can be computed by the analytic recipe and bounded by the constructive trick. This is the theorem that makes dimension theory *work*: every later result — Krull's height theorem, the dimension of a polynomial ring, the theory of multiplicity — is downstream of the freedom to switch between these three faces of one integer.

The route the proof takes is a closed loop of three inequalities. Generators bound growth ($\delta(A) \geq d(G_{\mathfrak{m}}(A))$, because $\delta(\mathfrak{q})$ generators give a Poincaré series with denominator $(1-T)^{\delta(\mathfrak{q})}$, capping the pole order). Growth bounds chains ($d(G_{\mathfrak{m}}(A)) \geq \dim A$, the hard analytic induction: killing one element drops the growth degree by one, so chains cannot outrun the degree). And chains bound generators ($\dim A \geq \delta(A)$, the constructive prime-avoidance induction: build the parameters one at a time, each cutting height by exactly one). Three inequalities around a triangle force equality everywhere.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "$(A, \mathfrak{m})$ Noetherian local". Several setups reduce to it.

The first disguised source is **a height computation at a prime**, $\operatorname{ht}\mathfrak{p}$ for $\mathfrak{p} \in \operatorname{Spec} R$ in any Noetherian ring $R$. The property $B$ is "$\mathfrak{p}$ is a prime of a Noetherian ring". The bridge is $\operatorname{ht}\mathfrak{p} = \dim R_{\mathfrak{p}}$, and $R_{\mathfrak{p}}$ is Noetherian local, so the dimension theorem applies to it. The non-obviousness: a *global* invariant (height in $R$) becomes a *local* one (dimension of $R_{\mathfrak{p}}$) to which the three-way equality applies. *Example problem:* bound $\operatorname{ht}\mathfrak{p}$ by the number of generators of $\mathfrak{p}$ — this is [[Thm - Krull's Height Theorem (Principal Ideal Theorem)|Krull's height theorem]].

The second disguised source is **a graded $k$-algebra**, $A = k[X_0, \dots, X_n]/I$ standard graded. The property $B$ is "$A$ is a finitely generated graded algebra over a field". Localizing at the irrelevant maximal ideal $\mathfrak{m}_+ = \bigoplus_{n>0}A_n$ gives a Noetherian local ring whose dimension is computed by the graded Hilbert polynomial of $A$ itself (no passage to the associated graded is needed — $A$ is already graded). The non-obvious bridge: for a graded ring the Hilbert polynomial and the Hilbert–Samuel polynomial carry the same dimension information. *Example problem:* read $\dim A$ off $\deg \mathrm{HP}_A$.

The third disguised source is **the quotient by one element**, $A/(x)$ for $x \in \mathfrak{m}$. The property $B$ is "I have a Noetherian local ring and want to understand a hypersurface section". Then $A/(x)$ is again Noetherian local, and the theorem applies to it with $\dim A/(x) \geq \dim A - 1$ (equality when $x$ avoids the minimal primes). The non-obviousness: cutting by one equation is governed by the same growth-degree bookkeeping that defines $d(G_{\mathfrak{m}})$. *Example problem:* the inductive step in the dimension of a polynomial ring.

**Targets (Output Amplification)**

The conclusion is "$\dim A = d(G_{\mathfrak{m}}(A)) = \delta(A) < \infty$, and parameters exist".

Combine $\dim A = \delta(A)$ with **a single explicit $\mathfrak{m}$-primary ideal** to bound dimension from above. The additional input $D$ is "I can exhibit $\mathfrak{m}$-primary $\mathfrak{q} = (x_1, \dots, x_r)$". Then $\dim A = \delta(A) \leq r$. The result $E$ is **Krull's height theorem**: a minimal prime of an $r$-generated ideal has height $\leq r$. Non-obvious because bounding a chain-length by exhibiting an ideal is a complete change of category.

Combine $\dim A = d(G_{\mathfrak{m}}(A))$ with **the Hilbert–Samuel polynomial** to compute Krull dimension by interpolation. The additional input $D$ is "I can count $\ell(A/\mathfrak{m}^n)$ for several $n$". Then $\dim A = \deg$ of the interpolating polynomial — a finite, mechanical computation. The result $E$ is an *algorithm* for dimension, replacing the search over chains of primes. Non-obvious because dimension is *defined* by chains but *computed* by counting lengths.

Combine the existence of a system of parameters with **a regular-sequence hypothesis** to access depth and Cohen–Macaulayness. The additional input $D$ is "the parameters form a regular sequence (each a non-zero-divisor mod the previous)". Then $A$ is **Cohen–Macaulay**, $\ell(A/\mathfrak{q})$ equals the multiplicity, and intersection theory is well-behaved. The result $E$ is the bridge from the chain-invariant $\dim$ to the homological invariant $\operatorname{depth}$. Non-obvious because it upgrades a *counting* statement to a *homological* one.

---

# Why Is It True

The theorem is true because the three numbers are linked by a *triangle of inequalities*, each proved by an idea you can grasp on its own; once the triangle closes, equality is forced with no further work.

**$\delta(A) \geq d(G_{\mathfrak{m}}(A))$: generators cap the growth rate.** If an $\mathfrak{m}$-primary ideal $\mathfrak{q}$ has $r$ generators, then its associated graded ring $G_{\mathfrak{q}}(A)$ is generated in degree one by $r$ elements over the Artinian ring $A/\mathfrak{q}$, so by [[Thm - Hilbert-Serre and Rationality of the Poincare Series|Hilbert–Serre]] its Poincaré series has denominator $(1-T)^r$ — the pole order at $T=1$ is at most $r$. And the $\mathfrak{q}$-adic and $\mathfrak{m}$-adic filtrations have the same growth degree (because $\mathfrak{m}^t \subseteq \mathfrak{q} \subseteq \mathfrak{m}$ squeezes $\ell(A/\mathfrak{m}^n) \leq \ell(A/\mathfrak{q}^n) \leq \ell(A/\mathfrak{m}^{tn})$, and a polynomial and its $t$-fold dilate have equal degree). So $d(G_{\mathfrak{m}}(A)) = d(G_{\mathfrak{q}}(A)) \leq r$; minimizing over $\mathfrak{q}$ gives $d(G_{\mathfrak{m}}(A)) \leq \delta(A)$.

**$d(G_{\mathfrak{m}}(A)) \geq \dim A$: growth caps chain length.** This is the analytic heart, an induction on $d := d(G_{\mathfrak{m}}(A))$. The base case $d = 0$ means $\ell(\mathfrak{m}^n/\mathfrak{m}^{n+1}) = 0$ for large $n$, so $\mathfrak{m}^{n+1} = \mathfrak{m}^n$, and [[Thm - Cayley-Hamilton for Modules (Determinant Trick)|Nakayama]] forces $\mathfrak{m}^n = 0$, making $A$ Artinian, so $\dim A = 0$. For the step, take any chain of primes $\mathfrak{p}_0 \subsetneq \cdots \subsetneq \mathfrak{p}_r$; pass to the domain $A/\mathfrak{p}_0$ and pick $x \in \mathfrak{p}_1 \setminus \mathfrak{p}_0$. The crucial lemma — proved with [[Thm - The Artin-Rees Lemma|Artin–Rees]] — is that **killing a non-zero-divisor drops the growth degree by at least one**: $d(G(A/(p_0 + (x)))) \leq d(G(A/\mathfrak{p}_0)) - 1 \leq d - 1$. By induction the smaller ring has $\dim \geq r - 1$ (the images of $\mathfrak{p}_1 \subsetneq \cdots \subsetneq \mathfrak{p}_r$ form a chain there), so $d \geq (r-1) + 1 = r$. Hence $d \geq \dim A$.

**$\dim A \geq \delta(A)$: chains let you build parameters.** This is the constructive half, an induction that *manufactures* $d = \dim A$ elements $x_1, \dots, x_d$ with $\operatorname{ht}(x_1, \dots, x_i) \geq i$ at each stage. Having built $x_1, \dots, x_{i-1}$ with $\operatorname{ht}(x_1, \dots, x_{i-1}) \geq i-1$, the finitely many height-$(i-1)$ primes containing $(x_1, \dots, x_{i-1})$ are all proper sub-ideals of $\mathfrak{m}$ (since $i - 1 < d = \operatorname{ht}\mathfrak{m}$), so by **prime avoidance** $\mathfrak{m} \not\subseteq$ their union; pick $x_i$ in $\mathfrak{m}$ outside all of them, forcing the height up to $i$. After $d$ steps, $(x_1, \dots, x_d)$ has every prime above it of height $\geq d$, hence equal to $\mathfrak{m}$, so it is $\mathfrak{m}$-primary with $d$ generators: $\delta(A) \leq d = \dim A$.

**The one-line mechanism: three faces of dimension are chained — $\delta$ caps growth via Hilbert–Serre, growth caps chains because killing an element drops the growth degree by one (Artin–Rees), and chains build parameters by prime avoidance — and the loop $\delta \geq d \geq \dim \geq \delta$ forces all three equal.**

---

# What Makes This Hard

The genuine difficulty is the middle inequality $d(G_{\mathfrak{m}}(A)) \geq \dim A$, and specifically the lemma that killing a non-zero-divisor $x$ drops the Hilbert–Samuel growth degree by exactly one: the obvious short exact sequence $0 \to A/(\mathfrak{m}^n : x) \xrightarrow{x} A/\mathfrak{m}^n \to A/(\mathfrak{m}^n + (x)) \to 0$ only gives the inequality after one knows that the filtration $(\mathfrak{m}^n \cap (x))_n$ is equivalent to $(\mathfrak{m}^n (x))_n$, which is precisely where [[Thm - The Artin-Rees Lemma|Artin–Rees]] enters and where most people get stuck. The second subtlety is purely organizational: it is easy to lose track of which of the three inequalities is being proved and to circularly invoke the conclusion. The most common error is to try to prove $\dim A = \delta(A)$ directly without the analytic middle term — but there is no known direct route; the Hilbert function is not a detour, it is the bridge.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove three inequalities forming a cycle $\delta(A) \geq d(G_{\mathfrak{m}}(A)) \geq \dim A \geq \delta(A)$; equality of all three follows. The first is Hilbert–Serre (an $r$-generated ideal gives pole order $\leq r$). The second is an induction on $d$ using "killing a non-zero-divisor drops the growth degree by one" (Artin–Rees). The third is an induction building parameters by prime avoidance.

**Subgoal decomposition:**

1. **$\delta(A) \geq d(G_{\mathfrak{m}}(A))$.** Show an $\mathfrak{m}$-primary $\mathfrak{q}$ with $r$ generators gives $d(G_{\mathfrak{m}}(A)) \leq r$.
   - *Hint:* $G_{\mathfrak{q}}(A)$ is degree-one generated by $r$ elements, so Hilbert–Serre gives denominator $(1-T)^r$; and $d(G_{\mathfrak{q}}) = d(G_{\mathfrak{m}})$ by the squeeze $\mathfrak{m}^t \subseteq \mathfrak{q} \subseteq \mathfrak{m}$.
   - *Why needed:* It is the easy cap that closes the loop at the top.

2. **Reduction lemma.** Show that if $x \in \mathfrak{m}$ is a non-zero-divisor then $d(G_{\mathfrak{m}/(x)}(A/(x))) \leq d(G_{\mathfrak{m}}(A)) - 1$.
   - *Hint:* Compare $\ell(A/(\mathfrak{m}^n + (x)))$ with $\ell(A/\mathfrak{m}^n)$; use $A \cong (x)$ via $a \mapsto ax$ and Artin–Rees to match leading terms of $\ell((x)/\mathfrak{m}^n(x))$ and $\ell((x)/(\mathfrak{m}^n \cap (x)))$.
   - *Why needed:* It is the engine of the analytic induction.

3. **$d(G_{\mathfrak{m}}(A)) \geq \dim A$.** Induct on $d = d(G_{\mathfrak{m}}(A))$; base $d=0$ via Nakayama gives $A$ Artinian; step uses the reduction lemma on $A/\mathfrak{p}_0$ and $x \in \mathfrak{p}_1 \setminus \mathfrak{p}_0$.
   - *Hint:* $\dim A/(\mathfrak{p}_0 + (x)) \geq r - 1$ from the images of the chain, and the reduction lemma drops $d$ by one.
   - *Why needed:* It is the hard inequality, the only place chains and growth meet.

4. **$\dim A \geq \delta(A)$.** Build $x_1, \dots, x_d \in \mathfrak{m}$ with $\operatorname{ht}(x_1, \dots, x_i) \geq i$ by prime avoidance; the final ideal is $\mathfrak{m}$-primary.
   - *Hint:* Finitely many minimal primes (Noetherian), none equal to $\mathfrak{m}$ while $i - 1 < d$, so $\mathfrak{m}$ avoids their union; pick $x_i$ outside.
   - *Why needed:* It closes the loop at the bottom; the resulting ideal is a system of parameters.

---

# Lemma Decomposition

> [!note]- Lemma 1: $\mathfrak{m}$-primary characterization and finite length
> **Statement:** In a Noetherian local ring $(A, \mathfrak{m})$, an ideal $\mathfrak{q}$ is $\mathfrak{m}$-primary iff $\mathfrak{m}^t \subseteq \mathfrak{q} \subseteq \mathfrak{m}$ for some $t \geq 1$, and then $A/\mathfrak{q}$ is Artinian (finite length).
>
> **Hint:** $\sqrt{\mathfrak{q}} = \mathfrak{m}$ in a Noetherian ring means $\mathfrak{m}^t \subseteq \mathfrak{q}$ for some $t$ (every ideal contains a power of its radical); conversely $\sqrt{\mathfrak{m}^t} = \mathfrak{m}$ squeezes $\sqrt{\mathfrak{q}} = \mathfrak{m}$.
>
> **Why needed:** It is what makes $\ell(A/\mathfrak{q}^n)$ finite and what licenses comparing the $\mathfrak{q}$-adic and $\mathfrak{m}$-adic growth rates.
>
> > [!note]- Full proof
> > ($\Leftarrow$) If $\mathfrak{m}^t \subseteq \mathfrak{q} \subseteq \mathfrak{m}$ then $\mathfrak{m} = \sqrt{\mathfrak{m}^t} \subseteq \sqrt{\mathfrak{q}} \subseteq \sqrt{\mathfrak{m}} = \mathfrak{m}$, so $\sqrt{\mathfrak{q}} = \mathfrak{m}$, i.e. $\mathfrak{q}$ is $\mathfrak{m}$-primary. ($\Rightarrow$) If $\sqrt{\mathfrak{q}} = \mathfrak{m}$ then in the Noetherian ring $A$, $\mathfrak{m} = \sqrt{\mathfrak{q}}$ is finitely generated and each generator has a power in $\mathfrak{q}$, so $\mathfrak{m}^t \subseteq \mathfrak{q}$ for some $t$; and $\mathfrak{q} \subseteq \sqrt{\mathfrak{q}} = \mathfrak{m}$. For finite length: $(A/\mathfrak{q}, \mathfrak{m}/\mathfrak{q})$ is Noetherian local, and if $\mathfrak{q} \subseteq \mathfrak{p} \in \operatorname{Spec} A$ then $\mathfrak{m} = \sqrt{\mathfrak{q}} \subseteq \mathfrak{p}$, forcing $\mathfrak{p} = \mathfrak{m}$. So $A/\mathfrak{q}$ has a unique prime, $\dim A/\mathfrak{q} = 0$; a Noetherian ring of dimension $0$ is Artinian, hence of finite length.

> [!note]- Lemma 2: Generators cap the pole order ($\delta(A) \geq d(G_{\mathfrak{m}}(A))$)
> **Statement:** If $\mathfrak{q}$ is $\mathfrak{m}$-primary with $\delta(\mathfrak{q}) = r$ generators, then $d(G_{\mathfrak{m}}(A)) = d(G_{\mathfrak{q}}(A)) \leq r$.
>
> **Hint:** $G_{\mathfrak{q}}(A)$ is generated in degree one by the $r$ images of generators of $\mathfrak{q}$ over $A/\mathfrak{q}$ (Artinian); apply Hilbert–Serre. Equate $d(G_{\mathfrak{q}})$ and $d(G_{\mathfrak{m}})$ by squeezing the length functions.
>
> **Why needed:** It is the first inequality of the cycle and supplies the upper bound on the growth degree.
>
> > [!note]- Full proof
> > By Lemma 1, $\mathfrak{m}^t \subseteq \mathfrak{q} \subseteq \mathfrak{m}$, so $\mathfrak{q}^n \subseteq \mathfrak{m}^n$ and $\mathfrak{m}^{tn} \subseteq \mathfrak{q}^n$, giving $\ell(A/\mathfrak{m}^n) \leq \ell(A/\mathfrak{q}^n) \leq \ell(A/\mathfrak{m}^{tn})$ for all $n$. The outer functions are (eventually) polynomials in $n$ of the same degree $d(G_{\mathfrak{m}}(A))$ (a polynomial $p(n)$ and its dilate $p(tn)$ have equal degree), so the squeezed middle is eventually a polynomial of that same degree, i.e. $d(G_{\mathfrak{q}}(A)) = d(G_{\mathfrak{m}}(A))$. Now $G_{\mathfrak{q}}(A) = \bigoplus_n \mathfrak{q}^n/\mathfrak{q}^{n+1}$ is generated as an $(A/\mathfrak{q})$-algebra by the $r = \delta(\mathfrak{q})$ images in $\mathfrak{q}/\mathfrak{q}^2$ of the generators of $\mathfrak{q}$, all in degree one, with $A/\mathfrak{q}$ Artinian. By [[Thm - Hilbert-Serre and Rationality of the Poincare Series|Hilbert–Serre]], $P(G_{\mathfrak{q}}(A), T) = f(T)/(1-T)^r$, so the pole order $d(G_{\mathfrak{q}}(A)) \leq r$. Hence $d(G_{\mathfrak{m}}(A)) \leq r$; minimizing over $\mathfrak{q}$ gives $d(G_{\mathfrak{m}}(A)) \leq \delta(A)$.

> [!note]- Lemma 3: Killing a non-zero-divisor drops the growth degree ($d \mapsto \leq d - 1$)
> **Statement:** If $x \in \mathfrak{m}$ is a non-zero-divisor, then $d\big(G_{\mathfrak{m}/(x)}(A/(x))\big) \leq d(G_{\mathfrak{m}}(A)) - 1$.
>
> **Hint:** Show $\deg \ell(A/(\mathfrak{m}^n + (x))) \leq \deg \ell(A/\mathfrak{m}^n) - 1$ by comparing leading terms of $\ell(A/\mathfrak{m}^n)$ and $\ell((x)/(\mathfrak{m}^n \cap (x)))$, using the isomorphism $A \cong (x)$, $a \mapsto ax$, and Artin–Rees to replace $\mathfrak{m}^n \cap (x)$ by $\mathfrak{m}^n(x)$ up to a degree shift.
>
> **Why needed:** It is the engine of the analytic induction in Lemma 4 — the precise form of "one equation drops dimension by one".
>
> > [!note]- Full proof
> > Write $\bar A = A/(x)$, $\bar{\mathfrak{m}} = \mathfrak{m}/(x)$. Then $\bar{\mathfrak{m}}^n = (\mathfrak{m}^n + (x))/(x)$, so $d(G_{\bar{\mathfrak{m}}}(\bar A)) = \deg \ell(\bar A/\bar{\mathfrak{m}}^n) = \deg \ell(A/(\mathfrak{m}^n + (x)))$, while $d(G_{\mathfrak{m}}(A)) = \deg \ell(A/\mathfrak{m}^n)$. We must show $\deg \ell(A/(\mathfrak{m}^n + (x))) \leq \deg \ell(A/\mathfrak{m}^n) - 1$.
> >
> > The short exact sequence $0 \to (\mathfrak{m}^n + (x))/\mathfrak{m}^n \to A/\mathfrak{m}^n \to A/(\mathfrak{m}^n + (x)) \to 0$ gives
> > $$\ell(A/(\mathfrak{m}^n + (x))) = \ell(A/\mathfrak{m}^n) - \ell\big((x)/(\mathfrak{m}^n \cap (x))\big),$$
> > using $(\mathfrak{m}^n + (x))/\mathfrak{m}^n \cong (x)/(\mathfrak{m}^n \cap (x))$. It therefore suffices to show $\ell(A/\mathfrak{m}^n)$ and $\ell((x)/(\mathfrak{m}^n \cap (x)))$ have the *same leading term* (then their difference has strictly smaller degree). Since $x$ is a non-zero-divisor, $a \mapsto ax$ is an $A$-isomorphism $A \xrightarrow{\sim} (x)$, inducing $A/\mathfrak{m}^n \xrightarrow{\sim} (x)/\mathfrak{m}^n(x)$, so $\ell(A/\mathfrak{m}^n) = \ell((x)/\mathfrak{m}^n(x))$. It remains to compare $\ell((x)/\mathfrak{m}^n(x))$ with $\ell((x)/(\mathfrak{m}^n \cap (x)))$. By [[Thm - The Artin-Rees Lemma|Artin–Rees]], the filtration $(\mathfrak{m}^n \cap (x))_n$ of the submodule $(x)$ is $\mathfrak{m}$-stable, hence equivalent to $(\mathfrak{m}^n(x))_n$: there is $n_0$ with $\mathfrak{m}^{n+n_0} \cap (x) \subseteq \mathfrak{m}^n(x)$ and $\mathfrak{m}^{n+n_0}(x) \subseteq \mathfrak{m}^n \cap (x)$ for all $n$. The squeeze $\ell((x)/(\mathfrak{m}^{n - n_0} \cap (x))) \leq \ell((x)/\mathfrak{m}^n(x)) \leq \ell((x)/(\mathfrak{m}^{n + n_0} \cap (x)))$ then forces equal leading terms. Hence $\ell(A/\mathfrak{m}^n)$ and $\ell((x)/(\mathfrak{m}^n \cap (x)))$ share a leading term, and their difference $\ell(A/(\mathfrak{m}^n + (x)))$ has degree $\leq \deg \ell(A/\mathfrak{m}^n) - 1$.

> [!note]- Lemma 4: Growth caps chains ($d(G_{\mathfrak{m}}(A)) \geq \dim A$)
> **Statement:** $\dim A \leq d := d(G_{\mathfrak{m}}(A))$.
>
> **Hint:** Induct on $d$. Base $d = 0$: $\mathfrak{m}^n = \mathfrak{m}^{n+1}$ for large $n$, Nakayama gives $\mathfrak{m}^n = 0$, $A$ Artinian, $\dim A = 0$. Step: for a chain of length $r$, pass to $A/\mathfrak{p}_0$, kill $x \in \mathfrak{p}_1 \setminus \mathfrak{p}_0$, apply Lemma 3 and induction.
>
> **Why needed:** It is the hard middle inequality — the only bridge from analytic growth to combinatorial chains.
>
> > [!note]- Full proof
> > Induct on $d$. If $d = 0$, then $\deg \ell(\mathfrak{m}^n/\mathfrak{m}^{n+1}) = -1$, so $\ell(\mathfrak{m}^n/\mathfrak{m}^{n+1}) = 0$ for large $n$, i.e. $\mathfrak{m}^{n+1} = \mathfrak{m} \cdot \mathfrak{m}^n = \mathfrak{m}^n$; by [[Thm - Cayley-Hamilton for Modules (Determinant Trick)|Nakayama's lemma]] applied to the finitely generated module $\mathfrak{m}^n$, $\mathfrak{m}^n = 0$. A Noetherian ring with $\mathfrak{m}^n = 0$ is Artinian, so $\dim A = 0$. Now assume $d \geq 1$ and the result for smaller values. If $\dim A = 0$ we are done; otherwise take a chain $\mathfrak{p}_0 \subsetneq \cdots \subsetneq \mathfrak{p}_r$ with $r \geq 1$; it suffices to show $d \geq r$. Pass to the Noetherian local domain $(A/\mathfrak{p}_0, \mathfrak{m}/\mathfrak{p}_0)$ and choose $x \in \mathfrak{p}_1 \setminus \mathfrak{p}_0$. Since $(A/\mathfrak{p}_0)/(\mathfrak{m}/\mathfrak{p}_0)^n \cong A/(\mathfrak{m}^n + \mathfrak{p}_0)$ is a quotient of $A/\mathfrak{m}^n$, we have $d(G_{\mathfrak{m}/\mathfrak{p}_0}(A/\mathfrak{p}_0)) \leq d$. The image $\bar x$ of $x$ is a non-zero-divisor in the domain $A/\mathfrak{p}_0$, so by Lemma 3, $d\big(G(A/(\mathfrak{p}_0 + (x)))\big) \leq d(G(A/\mathfrak{p}_0)) - 1 \leq d - 1$. The inductive hypothesis applied to the ring $A/(\mathfrak{p}_0 + (x))$ gives $\dim A/(\mathfrak{p}_0 + (x)) \leq d(G(A/(\mathfrak{p}_0 + (x)))) \leq d - 1$. On the other hand, the images of $\mathfrak{p}_1 \subsetneq \cdots \subsetneq \mathfrak{p}_r$ in $A/(\mathfrak{p}_0 + (x))$ form a strictly increasing chain of primes (they all contain $\mathfrak{p}_0 + (x)$, since $x \in \mathfrak{p}_1$), so $\dim A/(\mathfrak{p}_0 + (x)) \geq r - 1$. Combining, $r - 1 \leq d - 1$, i.e. $r \leq d$. Hence $\dim A \leq d$.

> [!note]- Lemma 5: Chains build parameters ($\dim A \geq \delta(A)$)
> **Statement:** There is an $\mathfrak{m}$-primary ideal generated by $d := \dim A$ elements; hence $\delta(A) \leq \dim A$.
>
> **Hint:** Construct $x_1, \dots, x_d \in \mathfrak{m}$ inductively with $\operatorname{ht}(x_1, \dots, x_i) \geq i$, choosing $x_i$ outside the finitely many height-$(i-1)$ primes over $(x_1, \dots, x_{i-1})$ by prime avoidance.
>
> **Why needed:** It closes the cycle at the bottom and exhibits a system of parameters.
>
> > [!note]- Full proof
> > Build $x_1, \dots, x_d \in \mathfrak{m}$ with $\operatorname{ht} q_i \geq i$ where $q_i = (x_1, \dots, x_i)$. Base: $q_0 = (0)$ lies in a minimal prime, of height $0$, so $\operatorname{ht} q_0 \geq 0$. Suppose $q_{i-1}$ is built with $\operatorname{ht} q_{i-1} \geq i-1$, where $i - 1 < d$. The primes $\mathfrak{p}_1, \dots, \mathfrak{p}_t$ of height exactly $i-1$ containing $q_{i-1}$ are minimal over $q_{i-1}$ (since $\operatorname{ht} q_{i-1} \geq i-1$), and there are only finitely many minimal primes over any ideal in a Noetherian ring. Because $i - 1 < d = \operatorname{ht}\mathfrak{m}$, none of these $\mathfrak{p}_j$ equals $\mathfrak{m}$, so $\mathfrak{m} \not\subseteq \mathfrak{p}_j$ for each $j$; by **prime avoidance**, $\mathfrak{m} \not\subseteq \bigcup_j \mathfrak{p}_j$. Pick $x_i \in \mathfrak{m} \setminus \bigcup_j \mathfrak{p}_j$ and set $q_i = (x_1, \dots, x_i)$. Any prime $\mathfrak{p} \supseteq q_i$ contains $q_{i-1}$ and is not among the $\mathfrak{p}_j$ (it contains $x_i$), so $\operatorname{ht}\mathfrak{p} \geq i$; thus $\operatorname{ht} q_i \geq i$. After $d$ steps, every prime over $q_d$ has height $\geq d = \operatorname{ht}\mathfrak{m}$, hence equals $\mathfrak{m}$, so $\sqrt{q_d} = \mathfrak{m}$ and $q_d$ is $\mathfrak{m}$-primary with $d$ generators. Hence $\delta(A) \leq d = \dim A$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — finiteness of the lengths.** By Lemma 1, for $\mathfrak{m}$-primary $\mathfrak{q}$ the rings $A/\mathfrak{q}^n$ are Artinian, so $\ell(A/\mathfrak{q}^n) < \infty$ and the Poincaré series of $G_{\mathfrak{q}}(A)$ is well-defined. In particular $d(G_{\mathfrak{m}}(A))$ is defined.
>
> We prove the cycle of inequalities; equality of all three integers follows immediately.
>
> **(i) $\delta(A) \geq d(G_{\mathfrak{m}}(A))$.** This is Lemma 2.
>
> **(ii) $d(G_{\mathfrak{m}}(A)) \geq \dim A$.** This is Lemma 4 (whose inductive step uses Lemma 3).
>
> **(iii) $\dim A \geq \delta(A)$.** This is Lemma 5.
>
> Chaining, $\delta(A) \geq d(G_{\mathfrak{m}}(A)) \geq \dim A \geq \delta(A)$, so all three are equal. In particular each is finite (it equals $\delta(A)$, which is finite because $A$ is Noetherian, so $\mathfrak{m}$ itself is a finitely generated $\mathfrak{m}$-primary ideal). The ideal $q_d$ constructed in Lemma 5 is an $\mathfrak{m}$-primary ideal generated by exactly $d = \dim A$ elements — a [[Def - System of Parameters|system of parameters]] — and by (iii) combined with $\dim A = \delta(A)$, no $\mathfrak{m}$-primary ideal has fewer than $d$ generators. $\blacksquare$
>
> **Remark (post-completion).** Once the theorem is proved, $\delta(A) = \dim A$ gives the converse direction in Lemma 5: each $q_i$ in that construction also satisfies $\operatorname{ht} q_i \leq i$ (it is $i$-generated, so a minimal prime over it has height $\leq i$ by Krull's height theorem, itself now a corollary), so in fact $\operatorname{ht} q_i = i$ exactly.

---

# Cross-Field Exercise Suggestions

**Smoothness and the Jacobian criterion (differential geometry / singularity theory).** The dimension theorem underlies the algebraic test for smoothness: a point of a variety is nonsingular iff its local ring is regular, $\dim_\kappa \mathfrak{m}/\mathfrak{m}^2 = \dim A$, where the right side is the Krull dimension supplied by this theorem and the left is the embedding dimension. Comparing the two is the algebraic Jacobian criterion. The application is non-obvious because the *analytic* face $d(G_{\mathfrak{m}})$ is what makes the dimension on the right computable, tying smoothness to a length-growth count.

**Intersection multiplicity and Bézout (enumerative geometry).** For a system of parameters generating an $\mathfrak{m}$-primary $\mathfrak{q}$, the multiplicity $e(\mathfrak{q}, A) = \lim d!\,\ell(A/\mathfrak{q}^n)/n^d$ — a quantity that *only makes sense* because the dimension theorem guarantees $\deg \ell(A/\mathfrak{q}^n) = d = \dim A$ — is the local intersection number. Bézout's theorem is the global sum of these. The non-obvious bridge: counting intersection points "with multiplicity" is reading the leading coefficient of a Hilbert–Samuel polynomial whose *degree* is pinned by this theorem.

**Dimension of fibres of a morphism (algebraic geometry).** For a finite-type morphism, the dimension of the fibre over a point is governed by the local rings, and the semicontinuity of fibre dimension rests on the three-way equality: one bounds fibre dimension by the number of equations cutting out the fibre ($\delta$) and computes it by Hilbert functions ($d(G_{\mathfrak{m}})$). The application is non-obvious because a global property of a map (fibre dimension) is controlled by the local invariant this theorem makes computable.

---

# Bridges

- **[[Thm - Krull's Height Theorem (Principal Ideal Theorem)|Krull's height theorem]]** — the immediate corollary. The inequality $\dim A = \delta(A) \leq$ (number of generators of an $\mathfrak{m}$-primary ideal), applied to $A = R_{\mathfrak{p}}$ where $\mathfrak{p}$ is minimal over an $r$-generated ideal $(x_1, \dots, x_r)$, gives $\operatorname{ht}\mathfrak{p} = \dim R_{\mathfrak{p}} \leq r$. So Krull's theorem is the statement $\dim \geq \delta$ read at a localization. The principal-ideal case ($r = 1$) says one non-unit cuts height at most one.

- **[[Thm - The Hilbert Polynomial|The Hilbert polynomial]]** — the supplier of $d(G_{\mathfrak{m}}(A))$. The Hilbert–Samuel polynomial $\ell(A/\mathfrak{m}^n)$ is, by that theorem applied to $G_{\mathfrak{m}}(A)$, eventually a polynomial of degree $d(G_{\mathfrak{m}}(A))$. This theorem then *names that degree the Krull dimension*. The two are a matched pair: one produces the polynomial, the other interprets its degree geometrically.

- **[[Thm - The Artin-Rees Lemma|Artin–Rees]]** — the technical lever inside Lemma 3. Comparing the $\mathfrak{m}$-adic filtration of a submodule $(x)$ with the induced filtration is exactly an Artin–Rees stability question; without it, "killing a non-zero-divisor drops the growth degree by one" could not be proved, and the hard middle inequality would collapse.

- **[[Thm - Integral Extensions Preserve Dimension|Integral extensions preserve dimension]]** — the complementary route to dimension. Where this theorem computes $\dim$ of a *local* ring by its Hilbert function, integral-extension invariance computes $\dim$ of a finitely generated algebra by transporting it to a polynomial subring via [[Thm - Noether Normalization|Noether normalization]]. Both feed [[Thm - Dimension of a Polynomial Ring|the dimension of a polynomial ring]]: the local theorem handles the inductive hypersurface step, the integral-extension theorem handles the global reduction.

- **[[Def - System of Parameters|System of parameters]]** — the object whose existence the theorem certifies. A system of parameters is a length-$\dim A$ generating set of an $\mathfrak{m}$-primary ideal; the theorem says such a thing exists and that $\dim A$ is the minimal length. In the regular case it generates $\mathfrak{m}$ itself and is a coordinate system.

---

# Unlocked by This

> [!tip] Regular local rings and the local theory of smoothness *(from Algebraic Geometry)*
> Once $\dim A$ is identified with $\delta(A)$, one can ask when $\mathfrak{m}$ *itself* is generated by exactly $\dim A$ elements — the minimum allowed, since $\delta(A) \leq \dim_\kappa \mathfrak{m}/\mathfrak{m}^2$ always. When equality holds, $(A, \mathfrak{m})$ is a **regular local ring** and the point is **smooth**: $\dim_\kappa \mathfrak{m}/\mathfrak{m}^2 = \dim A$. The gap $\dim_\kappa \mathfrak{m}/\mathfrak{m}^2 - \dim A$ measures singularity, and regular local rings are integral domains, integrally closed, and (by a theorem of Serre) characterized by finite global homological dimension. The dimension theorem is the load-bearing input: it is what makes "$\dim A$" a number you can compare against the embedding dimension.

> [!tip] Cohen–Macaulay rings and depth *(from Commutative Algebra / Homological Algebra)*
> A system of parameters is in general just a set of elements whose common zero locus is the point; when it can be chosen to be a **regular sequence** (each a non-zero-divisor modulo the previous), the ring is **Cohen–Macaulay** and dimension theory becomes maximally well-behaved. The maximal length of a regular sequence in $\mathfrak{m}$ is the **depth**, and $\operatorname{depth} A \leq \dim A$ always — the dimension theorem supplies the right-hand side. Cohen–Macaulay rings ($\operatorname{depth} = \dim$) are exactly the rings where the Hilbert–Samuel multiplicity equals the colength $\ell(A/\mathfrak{q})$ of any parameter ideal, making intersection theory exact and unmixedness theorems hold.

> [!tip] The dimension of a scheme and the fibre-dimension theorem *(from Algebraic Geometry)*
> For a **scheme**, dimension is the Krull dimension of the local rings of the structure sheaf, and this theorem is what makes those dimensions finite and computable on a Noetherian scheme. The deepest payoff is the **fibre-dimension theorem**: for a dominant morphism $f : X \to Y$ of irreducible varieties, the generic fibre has dimension $\dim X - \dim Y$, and *every* fibre has dimension $\geq \dim X - \dim Y$, with the inequality governed by exactly the "one equation drops dimension by at most one" mechanism (Lemma 3) iterated $\dim Y$ times. This is the algebraic backbone of the theory of families.
