---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - The I-adic Completion"
  - "Def - Direct and Inverse Limits"
  - "Def - Local Ring and Residue Field"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $p$ be a prime and $\mathbb{Z}_p=\varprojlim\mathbb{Z}/p^n\mathbb{Z}$ the [[Def - The I-adic Completion|p-adic integers]]. Prove **Hensel's lemma** and apply it.

1. **(Hensel's lemma.)** Let $f\in\mathbb{Z}_p[X]$ and $a_0\in\mathbb{Z}_p$ with
$$f(a_0)\equiv0\pmod{p}\qquad\text{and}\qquad f'(a_0)\not\equiv0\pmod{p}$$
(a *simple* root mod $p$). Then there is a unique $a\in\mathbb{Z}_p$ with $f(a)=0$ and $a\equiv a_0\pmod{p}$. (More generally the same holds with $p$ replaced by the maximal ideal of any complete local ring.)
2. **(Roots of unity.)** Deduce that $\mathbb{Z}_p$ contains a full set of $(p-1)$-th roots of unity — the Teichmüller representatives — so $\mu_{p-1}\subseteq\mathbb{Z}_p^\times$.
3. **(A square root.)** Show $\sqrt{-1}\in\mathbb{Z}_5$ exists (solve $X^2+1=0$), and more generally that a unit $u\in\mathbb{Z}_p^\times$ ($p$ odd) has a square root iff $u\bmod p$ is a quadratic residue.

**Recall:**

![[Def - The I-adic Completion#The Definition]]

The [[Def - The I-adic Completion|p-adic integers]] $\mathbb{Z}_p=\varprojlim\mathbb{Z}/p^n\mathbb{Z}$ are complete: every $p$-adically Cauchy sequence (one whose differences sink into ever-higher $p^n\mathbb{Z}_p$) has a limit. An element is a unit iff its residue mod $p$ is non-zero.

For $f=\sum c_i X^i\in\mathbb{Z}_p[X]$, the **formal derivative** is $f'=\sum i c_i X^{i-1}$, and the first-order Taylor expansion $f(a+h)=f(a)+f'(a)h+h^2 g(a,h)$ holds with $g\in\mathbb{Z}_p[X,Y]$ (a purely algebraic identity, no analysis).

---

# Convergent Strategy

**Problem class.** This is a *lift-a-solution-by-successive-approximation* problem — the hardest target type of the chapter and the algebraic form of Newton's method. As the [[Commutative Algebra X — Completions and Limits#Problem-Solving Strategy|topic strategy]] records, given an approximate root mod $\mathfrak{a}$ with non-degenerate derivative, you improve it one power of $\mathfrak{a}$ at a time, and completeness assembles the corrections into an exact root.

**Assumption pattern.** The trigger is the pair *root mod $p$* plus *unit derivative mod $p$* — the simple-root condition. The first gives a starting approximation; the second is the non-degeneracy that makes the Newton correction $h=-f(a)/f'(a)$ legal (you may divide by $f'(a)$ because it is a unit) and quadratically convergent. The whole difficulty is that this single hypothesis $f'(a_0)\in\mathbb{Z}_p^\times$ is what separates "lifts uniquely" from "may not lift at all".

**Theorem routing.** The route is: (1) prove Hensel by the inductive correction $a_{n+1}=a_n-f(a_n)/f'(a_n)$, showing $f(a_{n+1})\equiv0\pmod{p^{n+1}}$ (in fact mod $p^{2^n}$, quadratic) via the Taylor identity, and that $(a_n)$ is Cauchy with [[Def - The I-adic Completion|complete]] limit $a$; uniqueness from the derivative being a unit; (2) for roots of unity, apply Hensel to $f=X^{p-1}-1$ over $\mathbb{F}_p$, where every non-zero residue is a simple root (the polynomial is separable); (3) for square roots, apply Hensel to $X^2-u$, simple root condition $2X\not\equiv0$ needing $p$ odd and $u$ a QR.

**Key decision point.** The non-obvious heart is the *quadratic* convergence and why the unit-derivative hypothesis is indispensable. The Newton step gains *order* because the Taylor remainder is $O(h^2)$: correcting an order-$p^n$ error produces an order-$p^{2n}$ error, but only if you can divide by $f'(a_n)$ — and that requires $f'(a_n)$ to be a unit, which holds throughout because $f'(a_0)\not\equiv0\bmod p$ and the $a_n$ stay congruent to $a_0$. Without it (a *multiple* root mod $p$, $f'(a_0)\equiv0$), the correction is undefined and lifting genuinely fails — e.g. $X^2-p$ has a root mod $p$ ($X\equiv0$) but no root in $\mathbb{Z}_p$ because $\sqrt{p}\notin\mathbb{Z}_p$.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra X — Completions and Limits#Legal Operations|the topic page's Legal Operations]]:

1. **Lift a root by successive approximation (operation 4).** The core Newton iteration $a_{n+1}=a_n-f(a_n)/f'(a_n)$, made exact by completeness.

2. **Represent the limit as a compatible thread (operation 2).** The corrections $(a_n)$ form a Cauchy thread; its limit is the $p$-adic root.

3. **Recognise units by their residue (operation 9).** $f'(a_n)\in\mathbb{Z}_p^\times$ because $f'(a_n)\equiv f'(a_0)\not\equiv0\bmod p$; this is what licenses the division.

4. **Reduce mod $p^n$ and take the limit (operation 3).** Each correction is a congruence mod a power of $p$; the exact root is the limit.

---

# Hints

> [!note]- Hint 1
> Newton's method: from an approximate root $a_n$, the correction $h=-f(a_n)/f'(a_n)$ should improve it. The Taylor identity $f(a_n+h)=f(a_n)+f'(a_n)h+h^2(\cdots)$ shows the linear term cancels $f(a_n)$, leaving an error of order $h^2$.

> [!note]- Hint 2
> Quantify: if $f(a_n)\equiv0\pmod{p^n}$ then $h=-f(a_n)/f'(a_n)\in p^n\mathbb{Z}_p$ (legal because $f'(a_n)$ is a unit), so $h^2\in p^{2n}\mathbb{Z}_p$ and $f(a_{n+1})=f(a_n+h)\equiv0\pmod{p^{2n}}$. The order at least doubles — quadratic convergence.

> [!note]- Hint 3
> The $a_n$ satisfy $a_{n+1}\equiv a_n\pmod{p^n}$, so they form a Cauchy thread; let $a=\lim a_n\in\mathbb{Z}_p$ (completeness). Then $f(a)=\lim f(a_n)=0$. Uniqueness: two roots $\equiv a_0\bmod p$ would differ by $h$ with $0=f(a+h)-f(a)=f'(a)h+O(h^2)$, forcing $h=0$ since $f'(a)$ is a unit.

> [!note]- Hint 4
> Roots of unity: $f=X^{p-1}-1$ has $f'=(p-1)X^{p-2}$, and for any $a_0\in\{1,\dots,p-1\}$, $f(a_0)\equiv0\pmod p$ (Fermat) and $f'(a_0)=(p-1)a_0^{p-2}\not\equiv0\pmod p$. So each of the $p-1$ residues lifts to a distinct root of $X^{p-1}=1$ in $\mathbb{Z}_p$.

> [!note]- Hint 5
> $\sqrt{-1}\in\mathbb{Z}_5$: solve $X^2+1=0$. Mod $5$, $2^2=4\equiv-1$, so $a_0=2$ is a root with $f'(2)=4\not\equiv0\pmod5$. Hensel lifts it: $a=2+5+2\cdot5^2+\cdots$, a $5$-adic square root of $-1$.

---

# Solution

The proof is Newton's iteration with $p$-adic bookkeeping: the simple-root hypothesis makes $f'$ a unit, the correction $-f(a_n)/f'(a_n)$ is legal and gains order quadratically, and completeness turns the Cauchy sequence of approximations into an exact root. The applications instantiate $f=X^{p-1}-1$ and $f=X^2-u$.

**Step 1: Hensel's lemma by Newton iteration.**

Starting from $a_0$ with $f(a_0)\equiv0\pmod p$ and $f'(a_0)$ a unit, the iteration $a_{n+1}=a_n-f(a_n)f'(a_n)^{-1}$ produces a Cauchy sequence converging to the unique root $a\equiv a_0\pmod p$.

> [!note]- Derivation
> *Taylor identity.* For any $a,h\in\mathbb{Z}_p$, the algebraic identity
> $$f(a+h)=f(a)+f'(a)\,h+h^2\,g(a,h),\qquad g\in\mathbb{Z}_p[X,Y],$$
> holds (it is the finite Taylor expansion of a polynomial; no analysis needed).
>
> *The iteration improves the approximation.* Claim: if $f(a_n)\equiv0\pmod{p^{m}}$ with $m\geq1$ and $f'(a_n)$ a unit, then $a_{n+1}=a_n-f(a_n)f'(a_n)^{-1}$ satisfies $a_{n+1}\equiv a_n\pmod{p^m}$ and $f(a_{n+1})\equiv0\pmod{p^{2m}}$. Indeed set $h=-f(a_n)f'(a_n)^{-1}$. Since $f(a_n)\in p^m\mathbb{Z}_p$ and $f'(a_n)^{-1}\in\mathbb{Z}_p$, we have $h\in p^m\mathbb{Z}_p$, so $a_{n+1}\equiv a_n\pmod{p^m}$. By the Taylor identity,
> $$f(a_{n+1})=f(a_n)+f'(a_n)h+h^2 g=f(a_n)-f(a_n)+h^2 g=h^2 g(a_n,h).$$
> As $h\in p^m\mathbb{Z}_p$, $h^2\in p^{2m}\mathbb{Z}_p$, so $f(a_{n+1})\equiv0\pmod{p^{2m}}$. (The error order at least doubles — quadratic convergence.)
>
> *$f'$ stays a unit.* Since $a_{n+1}\equiv a_n\pmod{p^m}$ and all $a_n\equiv a_0\pmod p$, we have $f'(a_n)\equiv f'(a_0)\not\equiv0\pmod p$, so $f'(a_n)\in\mathbb{Z}_p^\times$ throughout; the division is always legal.
>
> *Convergence.* Starting from $f(a_0)\equiv0\pmod p$ ($m=1$), the orders are $1,2,4,8,\dots$, so $f(a_n)\to0$ and $a_{n+1}-a_n\in p^{2^n}\mathbb{Z}_p\to0$. Hence $(a_n)$ is $p$-adically Cauchy; by [[Def - The I-adic Completion|completeness]] of $\mathbb{Z}_p$ it has a limit $a=\lim a_n\in\mathbb{Z}_p$ with $a\equiv a_0\pmod p$. Continuity of the polynomial $f$ (it is $p$-adically continuous, being a polynomial) gives $f(a)=\lim f(a_n)=0$.
>
> *Uniqueness.* If $a,a'$ are roots with $a\equiv a'\equiv a_0\pmod p$, write $a'=a+h$, $h\in p\mathbb{Z}_p$. Then $0=f(a')-f(a)=f'(a)h+h^2 g(a,h)=h\big(f'(a)+h\,g\big)$. The factor $f'(a)+hg$ is a unit (its residue is $f'(a_0)\neq0$), so $h=0$, i.e. $a=a'$.

**Step 2: $(p-1)$-th roots of unity (Teichmüller lifts).**

Each non-zero residue mod $p$ lifts to a distinct root of $X^{p-1}-1$ in $\mathbb{Z}_p$, so $\mu_{p-1}\subseteq\mathbb{Z}_p^\times$.

> [!note]- Derivation
> Apply Hensel to $f=X^{p-1}-1$, $f'=(p-1)X^{p-2}$. For each $a_0\in\{1,2,\dots,p-1\}$ (a non-zero residue mod $p$):
> - $f(a_0)=a_0^{p-1}-1\equiv0\pmod p$ by Fermat's little theorem;
> - $f'(a_0)=(p-1)a_0^{p-2}\equiv-a_0^{p-2}\not\equiv0\pmod p$ since $a_0\not\equiv0$ and $p-1\equiv-1$.
>
> So each of the $p-1$ residues is a simple root, and Hensel lifts it to a unique $\omega_{a_0}\in\mathbb{Z}_p$ with $\omega_{a_0}^{p-1}=1$ and $\omega_{a_0}\equiv a_0\pmod p$. The $\omega_{a_0}$ are distinct (distinct residues), giving exactly $p-1$ roots of $X^{p-1}=1$ — the full group $\mu_{p-1}$ of $(p-1)$-th roots of unity, the **Teichmüller representatives**. They form a cyclic subgroup of $\mathbb{Z}_p^\times$ mapping isomorphically onto $\mathbb{F}_p^\times$ under reduction mod $p$, splitting the residue map $\mathbb{Z}_p^\times\to\mathbb{F}_p^\times$.

**Step 3: Square roots — $\sqrt{-1}\in\mathbb{Z}_5$ and the QR criterion.**

For $p$ odd, a unit $u$ has a square root in $\mathbb{Z}_p$ iff $u\bmod p$ is a quadratic residue; in particular $\sqrt{-1}\in\mathbb{Z}_5$.

> [!note]- Derivation
> Apply Hensel to $f=X^2-u$, $f'=2X$. A root $a_0$ mod $p$ needs $a_0^2\equiv u\pmod p$, i.e. $u\bmod p$ must be a quadratic residue. The simple-root condition is $f'(a_0)=2a_0\not\equiv0\pmod p$, which holds because $p$ is odd ($2\not\equiv0$) and $a_0\not\equiv0$ (as $u$ is a unit, $a_0^2\equiv u\neq0$). So:
> - if $u\bmod p$ is a QR, Hensel lifts $a_0$ to $a\in\mathbb{Z}_p$ with $a^2=u$;
> - if $u\bmod p$ is a non-residue, there is no root even mod $p$, hence none in $\mathbb{Z}_p$ (reduce mod $p$).
>
> *Example $\sqrt{-1}\in\mathbb{Z}_5$:* $u=-1$, and $-1\equiv4=2^2\pmod5$ is a QR, with $a_0=2$ (or $3$). Then $f'(2)=4\not\equiv0\pmod5$, so Hensel lifts: the iteration $a_{n+1}=a_n-\frac{a_n^2+1}{2a_n}$ gives $a_1=2-\frac{5}{4}=\frac{3}{4}$; reducing, $a\equiv2\pmod5$, $a\equiv7\pmod{25}$ (since $7^2=49\equiv-1\pmod{25}$), so
> $$\sqrt{-1}=2+1\cdot5+2\cdot5^2+\cdots\in\mathbb{Z}_5,\qquad a\equiv7\pmod{25}.$$
> The other root is $-a\equiv3\pmod5$. (Note $-1$ is a non-residue mod $3$, so $\sqrt{-1}\notin\mathbb{Z}_3$, consistent with $-1$ being a QR mod $p$ iff $p\equiv1\pmod4$.)

> [!note]- Complete formal solution
> **(1)** Use the Taylor identity $f(a+h)=f(a)+f'(a)h+h^2g(a,h)$. Given $f(a_n)\in p^m\mathbb{Z}_p$ and $f'(a_n)\in\mathbb{Z}_p^\times$, set $a_{n+1}=a_n-f(a_n)f'(a_n)^{-1}$; then $a_{n+1}\equiv a_n\pmod{p^m}$ and $f(a_{n+1})=h^2g\in p^{2m}\mathbb{Z}_p$. Since all $a_n\equiv a_0\pmod p$, $f'(a_n)$ stays a unit. From $m=1$ the orders double, so $(a_n)$ is Cauchy with limit $a\in\mathbb{Z}_p$ (completeness), $f(a)=0$, $a\equiv a_0\pmod p$. Uniqueness: a second root $a+h$ gives $0=h(f'(a)+hg)$ with $f'(a)+hg$ a unit, so $h=0$.
>
> **(2)** $f=X^{p-1}-1$: each $a_0\in\{1,\dots,p-1\}$ has $a_0^{p-1}\equiv1$ (Fermat) and $f'(a_0)=(p-1)a_0^{p-2}\not\equiv0\pmod p$, a simple root; Hensel lifts all $p-1$ to distinct roots, giving $\mu_{p-1}\subseteq\mathbb{Z}_p^\times$ (Teichmüller lifts).
>
> **(3)** $f=X^2-u$, $f'=2X$: for $p$ odd and $u$ a unit, the simple-root condition $2a_0\not\equiv0$ holds whenever $a_0^2\equiv u\pmod p$ has a solution, i.e. iff $u$ is a QR mod $p$; then Hensel lifts to $\sqrt{u}\in\mathbb{Z}_p$, else no root exists mod $p$. For $\mathbb{Z}_5$, $-1\equiv2^2$ is a QR, so $\sqrt{-1}\in\mathbb{Z}_5$ with $a\equiv7\pmod{25}$. $\blacksquare$

> [!warning] Illegal but tempting: applying Hensel at a multiple root
> The temptation is to drop the condition $f'(a_0)\not\equiv0\pmod p$ and lift *any* root mod $p$. This fails catastrophically at a multiple root. Take $f=X^2-p$ over $\mathbb{Z}_p$: it has the root $a_0=0$ mod $p$, but $f'(0)=0\equiv0\pmod p$, so the Newton correction $-f(a_n)/f'(a_n)$ divides by a non-unit and is undefined. And indeed $f$ has *no* root in $\mathbb{Z}_p$: $\sqrt{p}\notin\mathbb{Z}_p$ because the valuation of $p$ is $1$, which is odd, so $p$ is not a square. The simple-root condition is exactly the non-degeneracy that the implicit function theorem also requires; at a multiple root the linearisation is singular and the iteration has no foothold. *Never* invoke Hensel without checking $f'(a_0)$ is a unit.

> [!note]- Sanity check via the formal power series analogue
> The same lifting works in $k[[T]]$ with $T$ in place of $p$: a root of $f\in k[[T]][X]$ mod $T$ with $f'$ a unit lifts to a root in $k[[T]]$. For instance $\sqrt{1+T}=1+\tfrac12 T-\tfrac18 T^2+\cdots\in k[[T]]$ (char $k\neq2$) is the Hensel lift of the root $X\equiv1$ of $X^2-(1+T)$, with $f'(1)=2$ a unit. That this matches the binomial series is the confidence check: Hensel's lemma is the algebraic shadow of the convergent inverse/implicit function theorem.

---

# Key Takeaways

**Hensel's lemma is Newton's method made exact by completeness, and the simple-root condition is the non-degeneracy of the linearisation.** The entire mechanism is: linearise $f$ at the approximate root, solve the linear equation (legal because $f'$ is a unit), and iterate; the quadratic Taylor remainder makes the error order double each step, and completeness — every $p$-adic Cauchy sequence converges — turns the limit of approximations into an honest root. The trigger to burn in: a polynomial equation over a complete local ring, plus a root mod $\mathfrak{m}$ with *unit derivative*, means a unique exact root. The one hypothesis to check is always $f'(a_0)\in\mathbb{Z}_p^\times$; it is the algebraic implicit-function-theorem condition, and at a multiple root (singular linearisation) lifting genuinely fails, as $X^2-p$ shows. This is the single most useful solving tool in $p$-adic and formal-power-series computation.

**Quadratic convergence is why $p$-adic Newton is so much cleaner than real Newton.** Over $\mathbb{R}$, Newton's method converges quadratically only near the root and with analytic caveats; over $\mathbb{Z}_p$, the ultrametric makes "order at least doubles" an exact, unconditional statement — $f(a_n)\in p^{2^n}\mathbb{Z}_p$ — with no convergence radius to worry about. The transferable insight: in a complete *non-archimedean* setting, approximation schemes that are delicate over $\mathbb{R}$ become clean, because "small" is measured by membership in $\mathfrak{m}^n$ and products of small things are *exactly* as small as the sum of their orders. This is why $p$-adic and formal methods are a computational gift: the bookkeeping is integer valuations, not epsilon estimates. The same cleanliness underlies the unit-inversion geometric series of [[Ex - The p-adic integers as an inverse limit]] and [[Ex - The formal power series ring as a completion]].

**Hensel lifting splits the residue map, producing canonical lifts (Teichmüller, square roots) of residue-field data.** The roots-of-unity application shows something structural: Hensel's lemma lifts the *entire* multiplicative group $\mathbb{F}_p^\times$ to a canonical copy $\mu_{p-1}\subseteq\mathbb{Z}_p^\times$, splitting the reduction map. This "canonical lift of separable residue data" is a recurring theme — Teichmüller representatives, Witt vectors, the Cohen structure theorem's coefficient field — all rest on Hensel lifting idempotents and roots of separable polynomials. The trigger: whenever you want to lift a piece of residue-field structure (a root of unity, an idempotent, a factorisation) to the complete ring, check that it is *separable* (simple roots / unit derivative) and Hensel will lift it uniquely. This is how the residue field's algebra is recovered inside the complete local ring, and it is the bridge from this chapter to the structure theory of complete local rings.
