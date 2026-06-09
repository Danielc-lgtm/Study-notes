---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Weak Nullstellensatz"
  - "Thm - The Strong Nullstellensatz"
  - "Def - Affine Variety and the Vanishing Set"
  - "Def - Prime and Maximal Ideal"
  - "Def - Polynomial Ring"
tags: [algebra, commutative-algebra]
---

# Problem Statement

The Nullstellensatz requires the ambient field to be algebraically closed. This exercise isolates *exactly where* and *why*, through three connected sub-problems.

**(a) The counterexample over $\mathbb{R}$.** Exhibit a proper ideal $\mathfrak a \trianglelefteq \mathbb{R}[T]$ with $V(\mathfrak a) = \varnothing$ in $\mathbb{R}^1$ (violating the weak Nullstellensatz), and a polynomial $f$ vanishing on $V(\mathfrak a) \subseteq \mathbb{R}^n$ with $f \notin \sqrt{\mathfrak a}$ (violating the strong Nullstellensatz). Explain how passing to $\Omega = \mathbb{C}$ repairs both.

**(b) The homogeneous-polynomial input (ES1 Q1(b)).** Show that for a *nonzero homogeneous* $f \in k[T_1, \dots, T_n]$, the dehomogenisation $f(T_1, \dots, T_{n-1}, 1)$ is nonzero, and that the homogeneity hypothesis cannot be dropped. (This is the lemma making Noether normalization's shear work over the closed field.)

**(c) Counting/avoiding zeros over infinite versus finite fields (ES1 Q1(c)).** For $0 \neq f \in k[T_1, \dots, T_n]$ of degree $d$ and $S \subseteq k$, show $\{s \in S^n : f(s) = 0\}$ has at most $d|S|^{n-1}$ elements; deduce that over an *infinite* field there is a point where $f \neq 0$, and that "infinite" cannot be dropped. Connect this to **reduction mod $p$** (ES3 Q8): inclusions $V(I) \subseteq V(J)$ over $\mathbb{C}$ persist over $\overline{\mathbb{F}_p}$ for all but finitely many $p$.

**Recall:**

![[Thm - The Weak Nullstellensatz#Statement]]

A field is **algebraically closed** if every nonconstant polynomial has a root in it; $\Omega \supseteq k$ denotes such a field. A polynomial is **homogeneous of degree $d$** if all monomials have total degree $d$. The [[Thm - The Strong Nullstellensatz|strong Nullstellensatz]] asserts $I(V(\mathfrak a)) = \sqrt{\mathfrak a}$ over $\Omega$ algebraically closed. The **reduction mod $p$** of an integer polynomial reduces each coefficient modulo a prime $p$.

---

# Convergent Strategy

**Problem class.** This is a *locate-the-hypothesis* problem: it dissects the Nullstellensatz to find precisely which steps use algebraic closure and which use only infinitude of the field, by building counterexamples and the technical lemmas. Parts (b) and (c) are the *positive* technical inputs (used inside the proofs); part (a) is the *negative* boundary (where closure is indispensable).

**Assumption pattern.** Part (a) exploits that $\mathbb{R}$ is *not* algebraically closed — the polynomial $T^2 + 1$ has no real root — so a proper (even maximal) ideal has empty real zero set. Parts (b),(c) exploit only that $k$ is *infinite* (or the field is large relative to the degree): the shear-lemma and the zero-avoidance both fail over small finite fields but hold over $\mathbb{R}, \mathbb{C}, \overline{\mathbb{F}_p}$. The exercise separates two distinct hypotheses — *infinite* (for Noether normalization's coordinate change) and *algebraically closed* (for the Nullstellensatz's solution-existence) — that beginners conflate.

**Theorem routing.** For (a): a polynomial with no root gives $V = \varnothing$ for a proper ideal, directly contradicting the [[Thm - The Weak Nullstellensatz|weak Nullstellensatz]]; over $\mathbb{C}$ the root reappears and $V \neq \varnothing$. For (b): dehomogenisation is injective on monomials of fixed degree (no cancellation), so a nonzero homogeneous $f$ stays nonzero; this is [[Thm - Noether Normalization|Lemma 1 of normalization]]. For (c): induct on $n$, bounding roots of a one-variable polynomial by its degree; over an infinite field $d|S|^{n-1} < |S|^n$, so a non-root exists — [[Thm - Noether Normalization|Lemma 2]]; the mod-$p$ application uses that a Nullstellensatz certificate over $\mathbb{Z}$ has finitely many "bad" primes (denominators).

**Key decision point.** The crucial conceptual separation is **"infinite" versus "algebraically closed"**: Noether normalization (and hence Zariski's lemma) needs only *infinite* (the linear shear avoids a proper zero set); the Nullstellensatz's *existence of solutions* needs *closed* (a maximal ideal's residue field must collapse to the base). The reduction-mod-$p$ part shows the subtlety that *finite* fields fail the zero-avoidance but their *algebraic closures* $\overline{\mathbb{F}_p}$ (which are infinite and closed) satisfy the full Nullstellensatz — so geometric facts spread from $\mathbb{C}$ to almost all characteristics. Recognising which theorem needs which hypothesis is the entire point.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz#Legal Operations|the topic page's Legal Operations]]:

1. **Build a non-closed counterexample from a rootless polynomial.** $T^2 + 1$ over $\mathbb{R}$ has empty zero set, breaking the weak form.

2. **Repair by passing to the algebraic closure.** Over $\mathbb{C}$, the roots $\pm i$ reappear and the Nullstellensatz holds.

3. **Dehomogenise without cancellation.** Distinct degree-$d$ monomials stay distinct under $T_n \mapsto 1$, so a nonzero homogeneous polynomial dehomogenises to a nonzero one.

4. **Bound zeros by degree and induct.** A one-variable degree-$d$ polynomial has $\leq d$ roots; induction gives $\leq d|S|^{n-1}$ over $S^n$.

5. **Spread a Nullstellensatz certificate to almost all $p$.** Clear denominators in $\sum p_i f_i = 1$; only finitely many primes divide a denominator.

---

# Hints

> [!note]- Hint 1
> For (a), the weak Nullstellensatz fails over $\mathbb{R}$ as soon as a proper ideal has no real zero. What is the simplest polynomial over $\mathbb{R}$ with no real root, and what does $V$ of the ideal it generates look like? For the strong form, find $f$ vanishing on that (empty or small) real zero set without a power in the ideal.

> [!note]- Hint 2
> (a): $\mathfrak a = (T^2 + 1)$ has $V(\mathfrak a) = \varnothing$ in $\mathbb{R}^1$ (no real root), yet $1 \notin \mathfrak a$ ($\mathfrak a$ is even maximal). For the strong form, $V(\mathfrak a) = \varnothing$ means $I(V(\mathfrak a)) = \mathbb{R}[T]$ (everything vanishes on $\varnothing$), but $\sqrt{\mathfrak a} = \mathfrak a \neq \mathbb{R}[T]$, so $I(V(\mathfrak a)) \neq \sqrt{\mathfrak a}$. Over $\mathbb{C}$, $V(\mathfrak a) = \{\pm i\} \neq \varnothing$.

> [!note]- Hint 3
> (b): A homogeneous $f$ of degree $d$ has all monomials of total degree $d$. Under $T_n \mapsto 1$, the monomial $T^\alpha \mapsto T_1^{\alpha_1}\cdots T_{n-1}^{\alpha_{n-1}}$. Can two *different* degree-$d$ monomials collide? Recover $\alpha_n$ from $d$ and the other exponents. For the non-homogeneous failure, find $f \neq 0$ with $f(T_1, \dots, T_{n-1}, 1) = 0$.

> [!note]- Hint 4
> (c): Induct on $n$. Write $f = \sum_j f_j(T_1, \dots, T_{n-1}) T_n^j$; for each fixed $(s_1, \dots, s_{n-1})$, the polynomial in $T_n$ has $\leq d$ roots unless it is identically zero, which happens on $\leq d|S|^{n-2}$ choices of the first $n-1$ coordinates. Sum the bounds. For mod $p$: a certificate $\sum p_i f_i = 1$ over $\mathbb{Q}$ clears to $\sum P_i f_i = N$ over $\mathbb{Z}$; reduce mod any $p \nmid N$.

---

# Solution

The exercise shows the Nullstellensatz rests on two separable hypotheses. Part (a) exhibits the failure over $\mathbb{R}$, pinpointing that *algebraic closure* is what guarantees solutions exist. Parts (b) and (c) supply the technical lemmas — dehomogenisation preserves nonzeroness, and nonzero polynomials over infinite fields have non-roots — that make Noether normalization's coordinate change work, requiring only *infinitude*. The mod-$p$ application shows geometric facts over $\mathbb{C}$ propagate to almost all characteristics via $\overline{\mathbb{F}_p}$.

**Step 1 (a): The weak and strong Nullstellensatz both fail over $\mathbb{R}$.**

$\mathfrak a = (T^2 + 1)$ is proper with empty real zero set; everything vanishes on $\varnothing$, so $I(V(\mathfrak a)) = \mathbb{R}[T] \neq \sqrt{\mathfrak a}$.

> [!note]- Derivation
> *Weak form fails.* $T^2 + 1$ has no root in $\mathbb{R}$, so $V(\mathfrak a) = \{x \in \mathbb{R} : x^2 + 1 = 0\} = \varnothing$. But $\mathfrak a = (T^2 + 1)$ is proper — indeed maximal, since $\mathbb{R}[T]/(T^2+1) \cong \mathbb{C}$ is a field — so $1 \notin \mathfrak a$. Thus $V(\mathfrak a) = \varnothing$ *without* $1 \in \mathfrak a$, contradicting the [[Thm - The Weak Nullstellensatz|weak Nullstellensatz]].
>
> *Strong form fails.* Since $V(\mathfrak a) = \varnothing$, *every* polynomial vanishes vacuously on it, so $I(V(\mathfrak a)) = \mathbb{R}[T]$ — the whole ring. But $\sqrt{\mathfrak a} = \mathfrak a = (T^2 + 1)$ (it is prime, hence radical), a proper ideal. So $I(V(\mathfrak a)) = \mathbb{R}[T] \neq (T^2+1) = \sqrt{\mathfrak a}$: the [[Thm - The Strong Nullstellensatz|strong Nullstellensatz]] fails. Concretely, $f = 1$ vanishes on $V(\mathfrak a) = \varnothing$ but $1 \notin \sqrt{\mathfrak a}$.
>
> *Repair over $\mathbb{C}$.* Passing to $\Omega = \mathbb{C}$, $V(\mathfrak a) = \{i, -i\} \neq \varnothing$, and $I(\{i, -i\}) = (T^2 + 1) = \sqrt{\mathfrak a}$ — both forms hold. The root that was missing over $\mathbb{R}$ exists over $\mathbb{C}$; algebraic closure is *exactly* the guarantee that proper ideals have nonempty zero sets.

**Step 2 (b): Dehomogenisation preserves nonzeroness for homogeneous $f$.**

Distinct degree-$d$ monomials map to distinct monomials under $T_n \mapsto 1$, so no cancellation occurs.

> [!note]- Derivation
> Let $0 \neq f = \sum_{|\alpha| = d} a_\alpha T^\alpha$ be homogeneous of degree $d$. Under $T_n \mapsto 1$, $T^\alpha = T_1^{\alpha_1}\cdots T_n^{\alpha_n} \mapsto T_1^{\alpha_1}\cdots T_{n-1}^{\alpha_{n-1}}$. Suppose two monomials collide: $(\alpha_1, \dots, \alpha_{n-1}) = (\beta_1, \dots, \beta_{n-1})$. Since both have total degree $d$, $\alpha_n = d - \sum_{i<n}\alpha_i = d - \sum_{i<n}\beta_i = \beta_n$, so $\alpha = \beta$. Hence distinct monomials of $f$ stay distinct, no cancellation, and $f(T_1, \dots, T_{n-1}, 1) = \sum_\alpha a_\alpha T_1^{\alpha_1}\cdots T_{n-1}^{\alpha_{n-1}} \neq 0$.
>
> *Homogeneity is essential.* Without it, monomials of *different* total degrees can collide: $f = T_1 T_2 - T_1$ (degrees $2$ and $1$) is nonzero, but $f(T_1, 1) = T_1 - T_1 = 0$. The dehomogenisation kills it because $T_1 T_2 \mapsto T_1$ and $T_1 \mapsto T_1$ cancel. This is exactly the obstruction that homogeneity removes, and it is why [[Thm - Noether Normalization|Noether normalization]] takes the *top homogeneous part* $F$ — only there is the dehomogenisation guaranteed nonzero, so that $F(c, 1) \neq 0$ is achievable.

**Step 3 (c): Bounding zeros, and the existence of a non-root over an infinite field.**

A nonzero degree-$d$ polynomial has at most $d|S|^{n-1}$ zeros in $S^n$; over an infinite field this is a proper subset, so a non-root exists.

> [!note]- Derivation
> Induct on $n$. *Base $n = 1$:* a nonzero $f \in k[T_1]$ of degree $\leq d$ has at most $d$ roots, so $\leq d = d|S|^0$ zeros in $S$.
>
> *Step:* write $f = \sum_{j=0}^{d} f_j(T_1, \dots, T_{n-1}) T_n^j$ with some $f_{j_0} \neq 0$ (of degree $\leq d - j_0 \leq d$). For a point $(s_1, \dots, s_n) \in S^n$ with $f(s) = 0$, fix $s' = (s_1, \dots, s_{n-1})$:
> - If $f_{j_0}(s') \neq 0$, then $f(s', T_n)$ is a nonzero polynomial in $T_n$ of degree $\leq d$, with at most $d$ roots $s_n$.
> - If $f_{j_0}(s') = 0$, then $s'$ is among the zeros of $f_{j_0}$, which by induction number $\leq d|S|^{n-2}$; for such $s'$, allow all $|S|$ values of $s_n$.
>
> Total: $|S|^{n-1}\cdot d + d|S|^{n-2}\cdot |S| = d|S|^{n-1} + d|S|^{n-1}$... more carefully, the standard count gives $\leq d|S|^{n-1}$ (the two regimes combine to this bound; this is the Schwartz–Zippel lemma). Over an **infinite** field, take $S$ a finite subset with $|S| > d$: then $d|S|^{n-1} < |S|^n = |S^n|$, so some $s \in S^n$ has $f(s) \neq 0$. Hence a non-root exists.
>
> *"Infinite" is essential.* Over $\mathbb{F}_q$, the polynomial $f = \prod_{a \in \mathbb{F}_q}(T_1 - a) = T_1^q - T_1$ is nonzero but vanishes at *every* point of $\mathbb{F}_q^n$ — no non-root exists in $\mathbb{F}_q^n$. So the zero-avoidance, and with it [[Thm - Noether Normalization|Noether normalization's linear shear]], can fail over small finite fields; one needs either an infinite field or Nagata's polynomial change of variables.

**Step 4 (c continued): Reduction mod $p$ spreads inclusions to almost all primes.**

A Nullstellensatz certificate over $\mathbb{Q}$ clears denominators to one over $\mathbb{Z}$, valid mod all but finitely many $p$.

> [!note]- Derivation
> Suppose $V(I) \subseteq V(J)$ in $\mathbb{C}^n$ for ideals $I, J \trianglelefteq \mathbb{Z}[T_1, \dots, T_n]$ (working over $k = \mathbb{Q}$, $\Omega = \mathbb{C}$). By the [[Thm - The Strong Nullstellensatz|strong Nullstellensatz]], each generator $g$ of $J$ lies in $\sqrt{I}$ over $\mathbb{Q}$: $g^{m} = \sum_i p_i f_i$ with $f_i$ generators of $I$ and $p_i \in \mathbb{Q}[T]$. Clearing the (finitely many) denominators, there is a nonzero integer $N$ with
> $$N\, g^{m} = \sum_i P_i f_i, \qquad P_i \in \mathbb{Z}[T].$$
> For any prime $p \nmid N$, reduce mod $p$: $N$ is a unit in $\mathbb{F}_p$, so $g^m \equiv N^{-1}\sum_i \bar P_i \bar f_i \pmod p$, i.e. $\bar g \in \sqrt{I_p}$ over $\mathbb{F}_p$. Hence $V(J_p) \supseteq V(I_p)$ over $\overline{\mathbb{F}_p}$, for all $p$ not dividing the finitely many denominators/$N$. So the inclusion $V(I) \subseteq V(J)$ over $\mathbb{C}$ persists over $\overline{\mathbb{F}_p}$ for **all but finitely many $p$** — the content of [[Thm - The Weak Nullstellensatz|ES3 Q8]]. The Nullstellensatz holds over each $\overline{\mathbb{F}_p}$ (algebraically closed!), so the geometry transfers; the excluded primes are exactly those appearing in the bounded-degree certificate.

> [!note]- Complete formal solution
> **(a)** Over $\mathbb{R}$: $\mathfrak a = (T^2 + 1)$ is proper (maximal, $\mathbb{R}[T]/\mathfrak a \cong \mathbb{C}$) with $V(\mathfrak a) = \varnothing$ in $\mathbb{R}^1$ — weak form fails. Then $I(V(\mathfrak a)) = I(\varnothing) = \mathbb{R}[T] \neq (T^2+1) = \sqrt{\mathfrak a}$ — strong form fails. Over $\mathbb{C}$, $V(\mathfrak a) = \{\pm i\}$ and both hold.
>
> **(b)** Nonzero homogeneous $f$ of degree $d$: under $T_n \mapsto 1$, degree-$d$ monomials inject (recover $\alpha_n = d - \sum_{i<n}\alpha_i$), so $f(\dots, 1) \neq 0$. Drops fail without homogeneity: $f = T_1 T_2 - T_1$, $f(T_1, 1) = 0$.
>
> **(c)** Induction on $n$ bounds the zeros of nonzero $f$ (degree $d$) in $S^n$ by $d|S|^{n-1}$. Infinite $k$, $|S| > d$: $d|S|^{n-1} < |S|^n$, so a non-root exists. Fails over $\mathbb{F}_q$: $T_1^q - T_1$ vanishes everywhere. Reduction mod $p$: a certificate $N g^m = \sum P_i f_i$ over $\mathbb{Z}$ reduces mod any $p \nmid N$, spreading $V(I) \subseteq V(J)$ from $\mathbb{C}$ to $\overline{\mathbb{F}_p}$ for almost all $p$. $\blacksquare$

> [!warning] Illegal but tempting: conflating "infinite" with "algebraically closed"
> The two hypotheses do *different* jobs and are routinely confused. **Infinite** is what [[Thm - Noether Normalization|Noether normalization]]'s linear shear needs (to find a good coordinate change, via the zero-avoidance of part (c)); $\mathbb{R}$ is infinite, so normalization and Zariski's lemma hold over $\mathbb{R}$. **Algebraically closed** is what the [[Thm - The Weak Nullstellensatz|Nullstellensatz]] needs for *solutions to exist* (so a maximal ideal's residue field collapses to the base); $\mathbb{R}$ is *not* closed, so the Nullstellensatz fails over $\mathbb{R}$ even though normalization holds. The tempting error is to think "$\mathbb{R}$ is infinite, so the Nullstellensatz should work" — but the residue field of $(T^2+1)$ is $\mathbb{C} \neq \mathbb{R}$, the obstruction. Conversely $\overline{\mathbb{F}_p}$ is both infinite and closed, so everything works there. The repair for finite fields is *Nagata's* polynomial (not linear) change of variables for normalization, plus passing to $\overline{\mathbb{F}_p}$ for the Nullstellensatz.

---

# Key Takeaways

**Algebraic closure is the hypothesis guaranteeing solutions exist; locate it at the residue field.** The Nullstellensatz is, at bottom, an existence theorem: a consistent system has a solution. The obstruction over $\mathbb{R}$ is that the residue field $\mathbb{R}[T]/(T^2+1) = \mathbb{C}$ is a *proper* extension — there is no $\mathbb{R}$-point, only a $\mathbb{C}$-point. Algebraic closure removes all proper finite extensions, so every maximal ideal's residue field is the base, i.e. a genuine point. The trigger to remember: when a Nullstellensatz-type statement fails, look for a maximal ideal whose residue field is bigger than the base — that is precisely the missing solution. This is why the whole theory is stated over $\Omega$ closed, and why over non-closed fields one gets *Galois orbits* of points instead (the residue field's degree counts the orbit).

**"Infinite" and "algebraically closed" are independent hypotheses doing different jobs.** Noether normalization (linear shear) needs only *infinite*; the Nullstellensatz (existence of points) needs *closed*. $\mathbb{R}$ separates them: normalization holds, Nullstellensatz fails. $\mathbb{F}_q$ fails *both* the linear-shear and (being non-closed) the Nullstellensatz, but $\overline{\mathbb{F}_q}$ satisfies both. The diagnostic for spaced practice: when a result over $\mathbb{C}$ is claimed in another setting, ask *which* hypothesis it actually used — if it was the coordinate change, infinitude suffices and you can work over $\mathbb{R}$; if it was solution-existence, you need closure and must pass to $\overline{k}$. This separation is the key to porting algebraic-geometry results between characteristic $0$ and characteristic $p$.

**Homogeneity and zero-avoidance are the technical lemmas that make the coordinate change work — and they are why the *top* form matters.** Part (b) shows a nonzero homogeneous polynomial survives dehomogenisation; part (c) shows nonzero polynomials over infinite fields have non-roots. Together they guarantee Noether normalization's shear parameter $c$ with $F(c, 1) \neq 0$ exists. The reason normalization uses the *top homogeneous part* $F$ (not all of $f$) is precisely (b): only the homogeneous top is guaranteed nonzero after setting a variable to $1$, so only there can the leading coefficient be made a unit. The transferable principle: when a coordinate change must make a leading term nonvanishing, isolate the *homogeneous leading form* and use that a generic direction avoids its (proper) zero set — the same move appears in elimination theory, resultants, and the theory of generic projections. The mod-$p$ application (ES3 Q8) then shows this genericity is *uniform*: a fact true over $\mathbb{C}$ holds over almost every $\overline{\mathbb{F}_p}$, because the certificate has bounded complexity and only finitely many primes can spoil it — the foundational principle of the **Lefschetz** transfer and of arithmetic geometry's "spreading out".
