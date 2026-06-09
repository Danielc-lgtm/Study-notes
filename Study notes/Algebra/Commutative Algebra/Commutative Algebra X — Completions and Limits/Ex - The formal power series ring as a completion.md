---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Direct and Inverse Limits"
  - "Def - The I-adic Completion"
  - "Def - Polynomial Ring"
  - "Def - Local Ring and Residue Field"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $k$ be a field. Prove the following.

1. **(Power series = completion.)** $\varprojlim_n k[T]/(T^n)\cong k[[T]]$, the ring of formal power series, by matching a compatible family of polynomial truncations to a single power series. Conclude $k[[T]]=\widehat{k[T]}^{(T)}$.
2. **(Local ring and units.)** $k[[T]]$ is a [[Def - Local Ring and Residue Field|local ring]] with maximal ideal $(T)$ and residue field $k$; a power series $f=\sum_{m\geq0}a_m T^m$ is a unit iff $a_0=f(0)\neq0$. Exhibit the inverse of $1-T$.
3. **(Several variables.)** $\varprojlim_i k[T_1,\dots,T_n]/\mathfrak{a}^i\cong k[[T_1,\dots,T_n]]$ where $\mathfrak{a}=(T_1,\dots,T_n)$, using that $\mathfrak{a}^i=\mathrm{span}_k\{T_1^{e_1}\cdots T_n^{e_n}:e_1+\cdots+e_n\geq i\}$.

**Recall:**

The objects in play are the inverse limit, the $(T)$-adic completion, the polynomial ring, and local rings.

![[Def - Direct and Inverse Limits#The Definition]]

A [[Def - Direct and Inverse Limits|inverse limit]] $\varprojlim Y_i$ is the set of compatible threads. Here $Y_n=k[T]/(T^n)$, the polynomials of degree $<n$, and the transition map $k[T]/(T^{n+1})\to k[T]/(T^n)$ drops the degree-$n$ term.

![[Def - The I-adic Completion#The Definition]]

The [[Def - The I-adic Completion|$(T)$-adic completion]] of $k[T]$ is $\widehat{k[T]}^{(T)}=\varprojlim k[T]/(T)^n$; the claim is that it equals the formal power series ring.

![[Def - Polynomial Ring#The Definition]]

The **formal power series ring** $k[[T]]$ is the set of formal sums $\sum_{m\geq0}a_m T^m$ ($a_m\in k$), with addition coefficientwise and multiplication by the Cauchy product $\big(\sum a_m T^m\big)\big(\sum b_m T^m\big)=\sum_m\big(\sum_{i+j=m}a_i b_j\big)T^m$.

![[Def - Local Ring and Residue Field#The Definition]]

---

# Convergent Strategy

**Problem class.** This is an *identify-the-completion-via-the-universal-property* problem — the polynomial-ring twin of the $p$-adic exercise. As the [[Commutative Algebra X — Completions and Limits#Problem-Solving Strategy|topic strategy]] records, to prove $\varprojlim Y_i\cong A$ you either exhibit $A$ with the same universal property or, as here, give an explicit bijection respecting the operations, then read off locality from the unit criterion.

**Assumption pattern.** The trigger is *degree-truncation maps* $k[T]/(T^{n+1})\twoheadrightarrow k[T]/(T^n)$. A thread is then a coherent family of polynomial truncations agreeing on low-degree terms — exactly the data of a single power series, since each coefficient $a_m$ is determined once and stays fixed. The analogy with the $p$-adic digits is exact: "coefficient $a_m$" plays the role of "digit $d_m$", and $T$ plays the role of $p$.

**Theorem routing.** The route is: (1) map a thread $(p_n)$ to the power series whose degree-$m$ coefficient is the (stable) degree-$m$ coefficient of $p_n$ for any $n>m$ — well-defined by compatibility — and check this is a ring isomorphism (the Cauchy product is compatible with truncation because each output coefficient uses only finitely many inputs); (2) the unit criterion is [[Def - The I-adic Completion|"units detected mod $\mathfrak{a}$"]]: $f$ is a unit iff $f\bmod(T)=a_0$ is a unit in $k$, i.e. $a_0\neq0$, with the inverse a geometric series; (3) the several-variable case is identical once one identifies $\mathfrak{a}^i$ with "total degree $\geq i$".

**Key decision point.** The non-obvious point is that *multiplication survives the limit*: a priori the Cauchy product is an infinite sum, but its degree-$m$ coefficient $\sum_{i+j=m}a_i b_j$ is a *finite* sum, so it is computed correctly inside any truncation $k[T]/(T^{n})$ with $n>m$. This finiteness-per-coefficient is what makes $\varprojlim$ a ring isomorphism and not merely an additive one — the same reason the Cauchy product is well-defined in $k[[T]]$ at all.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra X — Completions and Limits#Legal Operations|the topic page's Legal Operations]]:

1. **Invoke the universal property / explicit bijection (operation 1).** Identify $\varprojlim k[T]/(T^n)$ with $k[[T]]$ by the coefficient-extraction map, the inverse-limit incarnation of "compatible families in, unique object out".

2. **Represent an element as a Taylor series (operation 2).** A thread is a power series; equality and operations are checked coefficient by coefficient.

3. **Present a completion as a power-series ring (operation 8).** This is the defining instance: $\widehat{k[T]}^{(T)}=k[[T]]$, the template for recognising other completions as power-series quotients.

4. **Recognise units by their residue (operation 9).** $f$ a unit iff $f(0)\neq0$, inverse built by geometric series.

---

# Hints

> [!note]- Hint 1
> A thread $(p_n)$ has $p_n\in k[T]/(T^n)$, a polynomial of degree $<n$, with $p_{n+1}$ reducing to $p_n$ mod $T^n$ — i.e. $p_{n+1}$ and $p_n$ agree on all terms of degree $<n$. So the degree-$m$ coefficient is the same in every $p_n$ with $n>m$. Define $a_m$ to be that common value.

> [!note]- Hint 2
> The map $(p_n)\mapsto\sum_m a_m T^m$ is a bijection onto $k[[T]]$. To see it is a *ring* map, check that multiplication of threads (coordinatewise in each $k[T]/(T^n)$) matches the Cauchy product — the degree-$m$ coefficient of a product uses only $a_0,\dots,a_m$ and $b_0,\dots,b_m$, all visible in $k[T]/(T^{m+1})$.

> [!note]- Hint 3
> For units: $f$ is a unit iff $f$ is a unit mod $T$, i.e. $a_0\neq0$. Given $a_0\neq0$, solve $fg=1$ for $g=\sum b_m T^m$ recursively: $b_0=a_0^{-1}$, and $b_m$ is determined by $\sum_{i+j=m}a_i b_j=0$, i.e. $a_0 b_m=-\sum_{i=1}^m a_i b_{m-i}$.

> [!note]- Hint 4
> For $1-T$: solve $(1-T)\sum b_m T^m=1$. You get $b_0=1$ and $b_m=b_{m-1}$, so all $b_m=1$: $(1-T)^{-1}=1+T+T^2+\cdots=\sum_{m\geq0}T^m$. (This is the geometric series, now an exact identity in $k[[T]]$.)

---

# Solution

The proof is the coefficient-extraction bijection, the observation that the Cauchy product is computed correctly per coefficient inside finite truncations, and the geometric-series unit criterion. The several-variable case is the same with "total degree" replacing "degree".

**Step 1: A thread is a power series, and the bijection is a ring isomorphism.**

The map $\Phi:\varprojlim k[T]/(T^n)\to k[[T]]$, $(p_n)\mapsto\sum_m a_m T^m$ with $a_m=[\text{deg-}m\text{ coeff of }p_n]$ for any $n>m$, is a ring isomorphism.

> [!note]- Derivation
> Let $(p_n)\in\varprojlim k[T]/(T^n)$, so $p_n$ is a polynomial of degree $<n$ and $p_{n+1}\equiv p_n\pmod{T^n}$, meaning $p_{n+1}$ and $p_n$ share every coefficient of degree $<n$. Hence for each $m$, the degree-$m$ coefficient is the same in $p_{m+1},p_{m+2},\dots$; call it $a_m$. Define $\Phi((p_n))=\sum_{m\geq0}a_m T^m\in k[[T]]$.
>
> *Bijection.* Injectivity: if all $a_m=0$ then every $p_n=0$, so the thread is $0$. Surjectivity: given $\sum a_m T^m$, the truncations $p_n=\sum_{m<n}a_m T^m$ form a compatible thread with $\Phi$-image the given series.
>
> *Additivity* is clear (coefficients add). *Multiplicativity*: in $\varprojlim$, the product $(p_n)(q_n)=(p_n q_n)$, and the degree-$m$ coefficient of $p_n q_n$ (for $n>m$) is $\sum_{i+j=m}a_i b_j$ — a finite sum using only $a_0,\dots,a_m,b_0,\dots,b_m$, hence stable in $n$. This is exactly the Cauchy-product coefficient of $\Phi((p_n))\Phi((q_n))$. So $\Phi$ is multiplicative, sends $1\mapsto1$, and is a ring isomorphism. By definition $\varprojlim k[T]/(T)^n=\widehat{k[T]}^{(T)}$, so $\widehat{k[T]}^{(T)}\cong k[[T]]$.

**Step 2: $k[[T]]$ is local with maximal ideal $(T)$, residue field $k$, units $\{a_0\neq0\}$.**

$f=\sum a_m T^m$ is a unit iff $a_0\neq0$; the non-units form $(T)$, and $k[[T]]/(T)\cong k$.

> [!note]- Derivation
> The map $k[[T]]\to k$, $f\mapsto f(0)=a_0$, is a surjective ring homomorphism (it is reduction mod $(T)$) with kernel $(T)=\{f:a_0=0\}$, so $k[[T]]/(T)\cong k$, a field.
>
> Suppose $a_0\neq0$. Solve $fg=1$ for $g=\sum b_m T^m$ by matching coefficients: degree $0$ gives $a_0 b_0=1$, so $b_0=a_0^{-1}$; degree $m\geq1$ gives $\sum_{i+j=m}a_i b_j=0$, i.e.
> $$a_0 b_m=-\sum_{i=1}^m a_i b_{m-i},\qquad b_m=-a_0^{-1}\sum_{i=1}^m a_i b_{m-i}.$$
> This recursion determines every $b_m$ uniquely from earlier ones, so $g\in k[[T]]$ exists with $fg=1$: $f$ is a unit. Conversely if $a_0=0$ then $f\in(T)$, and a unit cannot lie in the proper ideal $(T)$ (its image in $k$ would be a unit and $0$). Hence $k[[T]]^\times=\{a_0\neq0\}=k[[T]]\setminus(T)$, the ring is local with maximal ideal $(T)$, and residue field $k$.
>
> *Inverse of $1-T$:* here $a_0=1,a_1=-1$, rest $0$. The recursion gives $b_0=1$, $b_m=b_{m-1}$, so $b_m=1$ for all $m$:
> $$(1-T)^{-1}=\sum_{m\geq0}T^m=1+T+T^2+\cdots.$$

**Step 3: Several variables.**

$\varprojlim k[T_1,\dots,T_n]/\mathfrak{a}^i\cong k[[T_1,\dots,T_n]]$ for $\mathfrak{a}=(T_1,\dots,T_n)$.

> [!note]- Derivation
> The ideal $\mathfrak{a}^i$ is spanned over $k$ by all monomials $T_1^{e_1}\cdots T_n^{e_n}$ of total degree $e_1+\cdots+e_n\geq i$ (a product of $i$ generators $T_j$ has total degree $i$, and conversely). So $k[T_1,\dots,T_n]/\mathfrak{a}^i$ has as $k$-basis the monomials of total degree $<i$ — it is the polynomials truncated at total degree $i-1$, and the transition maps drop the top total-degree terms.
>
> Repeating Step 1 with "degree" replaced by "total degree": a thread assigns, compatibly, a coefficient $c_\alpha$ to every monomial $T^\alpha$ (the coefficient stabilises once $i>|\alpha|$), which is exactly a formal power series $\sum_\alpha c_\alpha T^\alpha\in k[[T_1,\dots,T_n]]$. The Cauchy product again uses only finitely many lower-degree coefficients per output, so multiplication is compatible with truncation. Hence $\varprojlim k[T_1,\dots,T_n]/\mathfrak{a}^i\cong k[[T_1,\dots,T_n]]$, i.e. $\widehat{k[T_1,\dots,T_n]}^{\mathfrak{a}}=k[[T_1,\dots,T_n]]$.

> [!note]- Complete formal solution
> **(1)** A thread $(p_n)\in\varprojlim k[T]/(T^n)$ has $p_{n+1}\equiv p_n\pmod{T^n}$, so the degree-$m$ coefficient $a_m$ is independent of $n>m$. The map $\Phi:(p_n)\mapsto\sum_m a_m T^m$ is a bijection onto $k[[T]]$ (inverse: $\sum a_m T^m\mapsto(\sum_{m<n}a_m T^m)_n$). It is additive, and multiplicative because the Cauchy coefficient $\sum_{i+j=m}a_i b_j$ is a finite sum visible in $k[T]/(T^{m+1})$. So $\widehat{k[T]}^{(T)}=\varprojlim k[T]/(T^n)\cong k[[T]]$.
>
> **(2)** Reduction mod $(T)$ gives $k[[T]]\to k$, $f\mapsto a_0$, surjective with kernel $(T)$, so $k[[T]]/(T)\cong k$. If $a_0\neq0$, the recursion $b_0=a_0^{-1}$, $b_m=-a_0^{-1}\sum_{i=1}^m a_i b_{m-i}$ produces $f^{-1}=\sum b_m T^m$; if $a_0=0$, $f\in(T)$ is a non-unit. Thus units $=\{a_0\neq0\}=k[[T]]\setminus(T)$, $k[[T]]$ is local with maximal ideal $(T)$ and residue field $k$, and $(1-T)^{-1}=\sum_{m\geq0}T^m$.
>
> **(3)** $\mathfrak{a}^i$ is spanned by monomials of total degree $\geq i$, so $k[T_1,\dots,T_n]/\mathfrak{a}^i$ keeps total degree $<i$; the Step-1 argument with total degree gives $\varprojlim k[T_1,\dots,T_n]/\mathfrak{a}^i\cong k[[T_1,\dots,T_n]]$. $\blacksquare$

> [!warning] Illegal but tempting: treating $\sum T^m$ as requiring convergence
> The identity $(1-T)^{-1}=\sum_{m\geq0}T^m$ in $k[[T]]$ does *not* depend on any notion of convergence — $k$ carries no metric and $T$ is an indeterminate. The "convergence" is $\mathfrak{a}$-adic: the partial sums $\sum_{m<n}T^m$ form a Cauchy thread in $\varprojlim k[T]/(T^n)$, and their limit is the power series. Trying to "evaluate at $T=2$" (so the sum diverges) is the error: the only legal substitution is $T\mapsto$ an element of the maximal ideal of a complete ring, where the geometric series converges $\mathfrak{a}$-adically. The identity is purely formal and exact.

---

# Key Takeaways

**A formal power series is the canonical example of a completion: a compatible thread of truncations, with each coefficient permanent once it appears.** The isomorphism $\widehat{k[T]}^{(T)}=k[[T]]$ is the cleanest illustration of the chapter's central object, and it installs the dictionary "coefficient $\leftrightarrow$ digit, $T\leftrightarrow p$, degree $\leftrightarrow$ valuation". The trigger to carry: whenever a ring is built from a tower of degree-truncations, its completion is a power-series ring, and recognising this lets you import Noetherianity ([[Thm - Formal Power Series over a Noetherian Ring are Noetherian]]) and exactness for free. The several-variable version, with "total degree" replacing "degree", is the local model of the formal disk in $n$ dimensions and the same recognition applies — $\widehat{R}$ for a completed local ring of a smooth point is exactly a power-series ring.

**Multiplication survives the inverse limit because each output coefficient is a finite sum.** The subtle point that makes $k[[T]]$ a *ring* and not just a group is that the Cauchy product's degree-$m$ coefficient $\sum_{i+j=m}a_i b_j$ uses only finitely many inputs, so it is computed correctly inside the finite truncation $k[T]/(T^{m+1})$ and is therefore compatible with the limit. This "finiteness per coefficient" is the general reason inverse limits of rings are rings, and it is what fails for ill-behaved infinite products. The transferable diagnostic: when checking that an inverse limit inherits a ring structure, verify that each structural output is determined by finitely many coordinates — if so, the operation passes to the limit; the Cauchy product is the prototype.

**Units in a complete local ring are exactly the elements with invertible residue, inverted by a coefficient recursion.** The criterion "$f$ a unit iff $f(0)\neq0$" makes $k[[T]]$ local, and its proof — solve $fg=1$ coefficient by coefficient, each $b_m$ forced by the lower ones — is the geometric-series/Newton mechanism shared with the $p$-adic units of [[Ex - The p-adic integers as an inverse limit]] and with Hensel lifting in [[Ex - Hensel-style lifting in the p-adics]]. The trigger: in any complete local ring, reduce "is this a unit?" to "is its residue a unit?", and build the inverse as a convergent recursion even when no closed form exists. This is why complete local rings have so many more units than their uncompleted versions — every element congruent to a unit mod $\mathfrak{m}$ becomes invertible — and it is the engine behind the locality of all the rings in this chapter.
