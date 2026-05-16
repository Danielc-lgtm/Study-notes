---
type: exercise
subject: ring-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Gauss's Lemma"
  - "Def - Content and Primitive Polynomial"
  - "Def - Irreducible and Prime Elements"
  - "Def - Polynomial Ring"
  - "Def - Field of Fractions"
tags: [algebra, ring-theory]
---

# Problem Statement

1. Show that $X^4 + X + 1$ is **irreducible over $\mathbb{Q}$** by reducing its coefficients modulo $2$ and analysing the resulting polynomial in $\mathbb{F}_2[X]$ — verify that it has no root in $\mathbb{F}_2$, and that it is not the square of the unique irreducible quadratic over $\mathbb{F}_2$.
2. Explain the limitation of the method: exhibit that $X^4 + 1$ is reducible modulo *every* prime $p$, even though $X^4 + 1$ is irreducible over $\mathbb{Q}$. Conclude that reduction mod $p$ is a *sufficient but not necessary* irreducibility test, and that a single prime failing to certify irreducibility proves nothing.

**Recall:**

The setting is the [[Def - Polynomial Ring|polynomial ring]] $\mathbb{Z}[X]$, the finite field $\mathbb{F}_p = \mathbb{Z}/p\mathbb{Z}$, the notion of a [[Def - Content and Primitive Polynomial|primitive polynomial]], and [[Def - Irreducible and Prime Elements|irreducibility]].

For a prime $p$, **reduction mod $p$** is the map $\mathbb{Z}[X] \to \mathbb{F}_p[X]$ that replaces each integer coefficient by its residue class modulo $p$. Write $\overline{f}$ for the reduction of $f$. This map is a **ring homomorphism**: $\overline{gh} = \overline{g}\,\overline{h}$ and $\overline{g + h} = \overline{g} + \overline{h}$. Crucially it *preserves degree* whenever $p$ does not divide the leading coefficient of $f$ — and for monic $f$ this always holds, since the leading coefficient $1$ reduces to $1 \neq 0$ in $\mathbb{F}_p$.

A polynomial of positive degree is [[Def - Irreducible and Prime Elements|irreducible]] over a field if it is not a product of two positive-degree factors. Over $\mathbb{F}_2$ there are exactly four monic linear polynomials and quadratics to keep track of: the linear ones are $X$ and $X + 1$; the monic quadratics are $X^2, X^2 + 1, X^2 + X, X^2 + X + 1$, of which only $X^2 + X + 1$ is **irreducible** (the other three have a root in $\mathbb{F}_2$).

![[Thm - Gauss's Lemma#The Statement]]

Gauss's lemma underwrites the reduction test: it lets a $\mathbb{Q}[X]$-factorisation of a primitive polynomial be replaced by a $\mathbb{Z}[X]$-factorisation, whose factors can then be reduced mod $p$.

The **reduction-mod-$p$ irreducibility criterion** (the theorem this exercise applies): *if $f \in \mathbb{Z}[X]$ is monic and the reduction $\overline{f} \in \mathbb{F}_p[X]$ is irreducible for some prime $p$, then $f$ is irreducible over $\mathbb{Q}$.*

---

# Convergent Strategy

**Problem class.** Part 1 is *irreducibility certification by passing to a quotient* — projecting the problem into a finite field where irreducibility can be checked by a finite search. Part 2 is a *limitation/counterexample* problem: demonstrate that the technique of part 1 is one-directional, by exhibiting a polynomial it fails to certify. Together they belong to the [[Rings III — §2.5–2.6]] strategy's catalogue of irreducibility tests, alongside Eisenstein and the root search.

**Assumption pattern.** The signal to try reduction mod $p$ is a polynomial over $\mathbb{Z}$ — ideally monic, so degree is preserved — for which Eisenstein finds no prime and a root search is inconclusive (degree $\geq 4$, so "no root" is insufficient). The freedom in the method is the *choice of prime*: small primes give small finite fields where the irreducible polynomials are few and fully enumerable. For $X^4 + X + 1$ the prime $2$ is the natural first try, because $\mathbb{F}_2[X]$ has the shortest list of irreducibles.

**Theorem routing.** Part 1: the contrapositive of the criterion. A $\mathbb{Q}[X]$-factorisation of the monic, primitive $X^4 + X + 1$ descends by [[Thm - Gauss's Lemma|Gauss's lemma]] to a $\mathbb{Z}[X]$-factorisation; reduction mod $2$ is a degree-preserving ring homomorphism, so it carries that factorisation to a non-trivial factorisation of $\overline{f}$ in $\mathbb{F}_2[X]$. Showing $\overline{f}$ admits *no* such factorisation — no linear factor (no root), and not a product of two quadratics (not the square of $X^2+X+1$) — refutes the existence of the original $\mathbb{Q}[X]$-factorisation. Part 2 routes through a counting/structure fact about finite fields: every element of $\mathbb{F}_{p^2}$ satisfies a degree-$\leq 2$ equation, which forces $X^4 + 1$ to lose irreducibility mod every $p$.

**Key decision point.** In part 1, the non-obvious move is recognising that for a *degree-$4$* polynomial, ruling out a *root* (linear factor) is not enough — one must also rule out a *quadratic times quadratic* split. Over $\mathbb{F}_2$ this second possibility is tightly constrained: a degree-$4$ polynomial with no linear factor that splits into two quadratics must split into two *irreducible* quadratics, and there is only *one* irreducible quadratic over $\mathbb{F}_2$, namely $X^2 + X + 1$; so the only possible such factorisation is $(X^2 + X + 1)^2$. Checking $\overline{f} \neq (X^2+X+1)^2$ is therefore the entire second half of the argument. In part 2, the key realisation is that "$X^4 + 1$ factors mod $p$" is a *uniform* phenomenon, provable for all $p$ at once by a structural argument, not a prime-by-prime check.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Rings III — §2.5–2.6#Legal Operations|the topic page's Legal Operations]]:

1. **Reduce coefficients modulo a prime.** Apply the ring homomorphism $\mathbb{Z}[X] \to \mathbb{F}_p[X]$; for monic $f$ this preserves degree.

2. **Push a factorisation through a ring homomorphism.** A factorisation $f = gh$ reduces to $\overline f = \overline g\,\overline h$; degree preservation keeps both reduced factors non-constant.

3. **Search for roots in a finite field by exhaustion.** Evaluate $\overline f$ at every element of $\mathbb{F}_p$ — a finite list — to detect or exclude linear factors.

4. **Enumerate the irreducible polynomials of low degree over a small finite field.** Over $\mathbb{F}_2$, list the irreducible quadratics ($X^2+X+1$ only) to constrain a possible quadratic factorisation.

5. **Use Gauss's lemma to descend a $\mathbb{Q}[X]$-factorisation to $\mathbb{Z}[X]$** before reducing — reduction mod $p$ acts on integer coefficients, not rational ones.

6. **Exhibit a counterexample to test the converse.** Construct a polynomial ($X^4 + 1$) on which the test fails at every prime, certifying that the criterion is sufficient only.

---

# Hints

> [!note]- Hint 1
> $X^4 + X + 1$ is monic, hence primitive, and reduction mod $p$ preserves its degree. If it factored over $\mathbb{Q}$, it would factor over $\mathbb{Z}$ (Gauss's lemma), and reducing mod $2$ would give a non-trivial factorisation in $\mathbb{F}_2[X]$ with the *same degrees*. So: show $\overline{f} = X^4 + X + 1 \in \mathbb{F}_2[X]$ cannot be factored non-trivially.

> [!note]- Hint 2
> A non-trivial factorisation of a degree-$4$ polynomial over a field has degree pattern $1 + 3$ or $2 + 2$ (a $1+3$ split contains a linear factor too). So first check for roots: evaluate $\overline f$ at $X = 0$ and $X = 1$ in $\mathbb{F}_2$. If there is no root, the only remaining possibility is a product of two quadratics.

> [!note]- Hint 3
> With no linear factor, a $2 + 2$ split must be into two *irreducible* quadratics. Over $\mathbb{F}_2$ the only irreducible quadratic is $X^2 + X + 1$ (check: $X^2, X^2+1, X^2+X$ all have a root). So the *only* possible factorisation of $\overline f$ into quadratics is $(X^2 + X + 1)^2$. Compute $(X^2 + X + 1)^2$ in $\mathbb{F}_2[X]$ and compare it with $X^4 + X + 1$.

> [!note]- Hint 4
> For part 2: over the field $\mathbb{F}_{p^2}$, *every* element $\alpha$ satisfies a polynomial equation of degree $\leq 2$ over $\mathbb{F}_p$ (its minimal polynomial divides $X^{p^2} - X$ and has degree $1$ or $2$). The roots of $X^4 + 1$ — the primitive $8$th roots of unity — all live in $\mathbb{F}_{p^2}$ for *every* odd $p$ (since $8 \mid p^2 - 1$ for all odd $p$). So every irreducible factor of $X^4 + 1$ mod $p$ has degree $\leq 2$, forcing a non-trivial factorisation. Handle $p = 2$ separately: $X^4 + 1 = (X+1)^4$ in $\mathbb{F}_2[X]$.

---

# Solution

For part 1, reducing mod $2$ sends a hypothetical factorisation into $\mathbb{F}_2[X]$, where a degree-$4$ polynomial can only split as a linear factor (a root) or as two irreducible quadratics — and over $\mathbb{F}_2$ there is just one irreducible quadratic, so both possibilities are checked in a few lines. Part 2 shows the test is one-directional: $X^4 + 1$ defeats it at every prime.

**Step 1: Reduce $X^4 + X + 1$ modulo $2$ and check for roots.**

The reduction $\overline f = X^4 + X + 1 \in \mathbb{F}_2[X]$ has no root in $\mathbb{F}_2$, so it has no linear factor.

> [!note]- Derivation
> $f = X^4 + X + 1$ is monic; its coefficients $1, 1, 0, 0, 1$ reduce mod $2$ to $1, 1, 0, 0, 1$, so $\overline f = X^4 + X + 1$ in $\mathbb{F}_2[X]$, still of degree $4$ — reduction preserves degree because the leading coefficient $1$ does not reduce to $0$.
>
> Evaluate at every element of $\mathbb{F}_2 = \{0, 1\}$:
> $$\overline f(0) = 0 + 0 + 1 = 1 \neq 0, \qquad \overline f(1) = 1 + 1 + 1 = 1 \neq 0 \quad (\text{in } \mathbb{F}_2).$$
> ($1 + 1 + 1 = 3 \equiv 1 \pmod 2$.) Neither element is a root. By the **factor theorem**, a degree-$1$ factor $X - a$ of $\overline f$ would correspond to a root $a \in \mathbb{F}_2$; since there is none, $\overline f$ has no linear factor in $\mathbb{F}_2[X]$.

**Step 2: Rule out a factorisation into two quadratics.**

The only monic irreducible quadratic over $\mathbb{F}_2$ is $X^2 + X + 1$, so the only possible quadratic-times-quadratic factorisation of $\overline f$ is $(X^2+X+1)^2$. Computing $(X^2+X+1)^2 = X^4 + X^2 + 1 \neq X^4 + X + 1$, no such factorisation exists.

> [!note]- Derivation
> A non-trivial factorisation of the degree-$4$ polynomial $\overline f$ over the field $\mathbb{F}_2$ has degree pattern $1+3$ or $2+2$. The pattern $1 + 3$ includes a degree-$1$ factor, hence a root — excluded by Step 1. So the only possibility is $2 + 2$: $\overline f = q_1 q_2$ with $\deg q_1 = \deg q_2 = 2$.
>
> If either $q_i$ were *reducible*, it would have a linear factor, hence $\overline f$ would have a linear factor — again excluded. So $q_1, q_2$ must both be **irreducible** monic quadratics over $\mathbb{F}_2$ (monic because $\overline f$ is monic).
>
> Enumerate the monic quadratics over $\mathbb{F}_2$:
> $$X^2,\qquad X^2 + 1,\qquad X^2 + X,\qquad X^2 + X + 1.$$
> Test each for a root: $X^2$ has root $0$; $X^2 + 1 = (X+1)^2$ has root $1$ (since $1 + 1 = 0$); $X^2 + X = X(X+1)$ has roots $0, 1$; $X^2 + X + 1$ evaluates to $1$ at both $0$ and $1$, so it has *no* root and is **irreducible**. Hence $X^2 + X + 1$ is the unique monic irreducible quadratic over $\mathbb{F}_2$.
>
> Therefore the only candidate $2+2$ factorisation is $q_1 = q_2 = X^2 + X + 1$, i.e. $\overline f = (X^2 + X + 1)^2$. Compute the square in $\mathbb{F}_2[X]$ (all arithmetic mod $2$; note the cross terms $2(\cdot)$ vanish):
> $$(X^2 + X + 1)^2 = X^4 + X^2 + 1 + \underbrace{2X^3 + 2X^2 + 2X}_{\equiv\, 0} = X^4 + X^2 + 1.$$
> But $\overline f = X^4 + X + 1 \neq X^4 + X^2 + 1$ — they differ in the $X$ and $X^2$ coefficients. So $\overline f \neq (X^2+X+1)^2$, and no $2 + 2$ factorisation exists.

**Step 3: Conclude $X^4 + X + 1$ is irreducible over $\mathbb{Q}$.**

$\overline f$ is irreducible in $\mathbb{F}_2[X]$, and therefore $f = X^4 + X + 1$ is irreducible over $\mathbb{Q}$.

> [!note]- Derivation
> Steps 1 and 2 together show $\overline f$ admits **no** non-trivial factorisation in $\mathbb{F}_2[X]$ — neither a linear factor nor a $2+2$ split — so $\overline f$ is irreducible in $\mathbb{F}_2[X]$.
>
> Now run the criterion by contraposition. Suppose $f = X^4 + X + 1$ were *reducible* over $\mathbb{Q}$. The polynomial is monic, hence primitive, so by [[Thm - Gauss's Lemma|Gauss's lemma]] it is reducible over $\mathbb{Z}$:
> $$f = g\,h, \qquad g, h \in \mathbb{Z}[X], \quad \deg g, \deg h \geq 1, \quad \deg g + \deg h = 4.$$
> Apply the reduction-mod-$2$ homomorphism, which respects products: $\overline f = \overline g\,\overline h$. Because $f$ is monic, its leading coefficient is $1$; the leading coefficients of $g$ and $h$ multiply to $1$, so each is $\pm 1$, which is non-zero mod $2$. Hence reduction preserves the degrees of $g$ and $h$: $\deg \overline g = \deg g \geq 1$ and $\deg \overline h = \deg h \geq 1$. So $\overline f = \overline g\,\overline h$ is a non-trivial factorisation of $\overline f$ in $\mathbb{F}_2[X]$ — contradicting the irreducibility of $\overline f$ just established.
>
> Therefore $f = X^4 + X + 1$ is irreducible over $\mathbb{Q}$. $\blacksquare$

**Step 4: The limitation — $X^4 + 1$ is reducible mod every prime, yet irreducible over $\mathbb{Q}$.**

$X^4 + 1$ is irreducible over $\mathbb{Q}$, but $\overline{X^4 + 1}$ is reducible in $\mathbb{F}_p[X]$ for *every* prime $p$. So reduction mod $p$ can fail to certify a genuinely irreducible polynomial.

> [!note]- Derivation
> *$X^4 + 1$ is irreducible over $\mathbb{Q}$.* Substitute $X \mapsto X + 1$: by the binomial theorem
> $$(X+1)^4 + 1 = X^4 + 4X^3 + 6X^2 + 4X + 1 + 1 = X^4 + 4X^3 + 6X^2 + 4X + 2.$$
> Apply [[Thm - Eisenstein's Criterion|Eisenstein's criterion]] at $p = 2$: the leading coefficient $1$ is not divisible by $2$; the coefficients $4, 6, 4, 2$ are all divisible by $2$; the constant term $2$ is not divisible by $2^2 = 4$. So $(X+1)^4 + 1$ is irreducible, and since $X \mapsto X + 1$ is an automorphism of $\mathbb{Q}[X]$ (preserving irreducibility — see [[Ex - Irreducibility of the cyclotomic polynomial]]), $X^4 + 1$ is irreducible over $\mathbb{Q}$.
>
> *$X^4 + 1$ is reducible mod every prime.* Handle the primes in cases.
>
> - **$p = 2$:** in $\mathbb{F}_2[X]$, since $2 \equiv 0$ and the cross terms vanish, $(X+1)^4 = X^4 + 1$. So $X^4 + 1 = (X+1)^4$ — reducible.
> - **$p$ odd:** the roots of $X^4 + 1$ are the primitive $8$th roots of unity, the elements of order $8$ in the multiplicative group of an algebraic closure. We claim they all lie in the field $\mathbb{F}_{p^2}$ with $p^2$ elements. The multiplicative group $\mathbb{F}_{p^2}^\times$ is cyclic of order $p^2 - 1$. For any odd prime $p$, $p$ is odd so $p^2 \equiv 1 \pmod 8$ (the square of any odd number is $1$ mod $8$), hence $8 \mid p^2 - 1$. A cyclic group whose order is divisible by $8$ contains an element of order $8$, indeed all four elements of order $8$. So every root of $X^4 + 1$ lies in $\mathbb{F}_{p^2}$.
>
>   Now, every element $\alpha \in \mathbb{F}_{p^2}$ has a minimal polynomial over $\mathbb{F}_p$ of degree $1$ or $2$ (its degree divides $[\mathbb{F}_{p^2} : \mathbb{F}_p] = 2$). Therefore *every irreducible factor* of $X^4 + 1$ in $\mathbb{F}_p[X]$ has degree $\leq 2$. A degree-$4$ polynomial all of whose irreducible factors have degree $\leq 2$ cannot itself be irreducible — it must split (into $2+2$, or $2+1+1$, or $1+1+1+1$). So $\overline{X^4 + 1}$ is reducible in $\mathbb{F}_p[X]$ for every odd $p$ as well.
>
> *Conclusion.* $X^4 + 1$ is irreducible over $\mathbb{Q}$, yet its reduction is reducible modulo *every* prime. The reduction-mod-$p$ criterion is therefore **sufficient but not necessary**: $\overline f$ irreducible $\Rightarrow$ $f$ irreducible, but the converse fails. In particular, finding that $\overline f$ is *reducible* for some prime $p$ — or even for many primes — proves nothing about $f$; only an *irreducible* reduction is informative. $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** (1) $X^4 + X + 1$ is irreducible over $\mathbb{Q}$, shown via reduction mod $2$. (2) $X^4 + 1$ is irreducible over $\mathbb{Q}$ but reducible mod every prime, so the test is sufficient only.
>
> *Part 1.* $f = X^4 + X + 1$ is monic, hence primitive; reduction mod $2$ preserves degree, giving $\overline f = X^4 + X + 1 \in \mathbb{F}_2[X]$. Roots: $\overline f(0) = 1$, $\overline f(1) = 1$, so no linear factor. A non-trivial factorisation must then be $2 + 2$ into two irreducible monic quadratics; the only monic irreducible quadratic over $\mathbb{F}_2$ is $X^2 + X + 1$, so the only candidate is $(X^2+X+1)^2 = X^4 + X^2 + 1 \neq X^4 + X + 1$. Hence $\overline f$ is irreducible in $\mathbb{F}_2[X]$. If $f$ were reducible over $\mathbb{Q}$, by [[Thm - Gauss's Lemma|Gauss's lemma]] it would be reducible over $\mathbb{Z}$, and reduction mod $2$ (a degree-preserving homomorphism, $f$ monic) would yield a non-trivial factorisation of $\overline f$ — contradiction. So $f$ is irreducible over $\mathbb{Q}$.
>
> *Part 2.* $(X+1)^4 + 1 = X^4 + 4X^3 + 6X^2 + 4X + 2$ is Eisenstein at $2$, so irreducible; since $X \mapsto X+1$ is an automorphism of $\mathbb{Q}[X]$, $X^4 + 1$ is irreducible over $\mathbb{Q}$. Modulo $2$: $X^4 + 1 = (X+1)^4$. Modulo an odd prime $p$: $p^2 \equiv 1 \pmod 8$, so $8 \mid p^2 - 1 = |\mathbb{F}_{p^2}^\times|$, so the cyclic group $\mathbb{F}_{p^2}^\times$ contains the elements of order $8$ — the roots of $X^4 + 1$ — hence all roots lie in $\mathbb{F}_{p^2}$, and each has minimal polynomial of degree $\leq 2$ over $\mathbb{F}_p$. A degree-$4$ polynomial with all irreducible factors of degree $\leq 2$ is reducible. So $X^4 + 1$ is reducible mod every prime. The criterion "$\overline f$ irreducible $\Rightarrow$ $f$ irreducible" is therefore not reversible. $\blacksquare$

---

# Key Takeaways

**Reduction mod $p$ is "push the problem through a ring homomorphism into a finite field where irreducibility is decidable by exhaustion."** The technique exploits one structural fact: reduction $\mathbb{Z}[X] \to \mathbb{F}_p[X]$ is a *ring homomorphism*, so it carries any factorisation $f = gh$ to a factorisation $\overline f = \overline g\,\overline h$. Provided it also preserves degree — which it does for monic $f$, since the leading $1$ survives — a non-trivial factorisation upstairs becomes a non-trivial factorisation downstairs. Contrapositively, *if the reduction is irreducible, so was the original*. The payoff is that $\mathbb{F}_p[X]$ is a setting where irreducibility is genuinely *checkable*: $\mathbb{F}_p$ is finite, so root searches terminate, and the irreducible polynomials of each low degree can be listed outright. The trigger to reach for this test: a polynomial over $\mathbb{Z}$, monic, that resists Eisenstein (no prime fits the coefficient pattern) and resists the root search (degree $\geq 4$, so "no rational root" is insufficient). The general principle — *map a hard problem into a finite quotient where it becomes a finite computation* — is one of the most reusable moves in algebra, the same idea behind using congruences to prove a Diophantine equation has no solutions.

**For a degree-$4$ polynomial, excluding roots excludes only *half* the factorisations — the quadratic-times-quadratic split must be killed separately.** This is the central subtlety of part 1 and the recurring trap with quartics. A degree-$4$ polynomial factors non-trivially in exactly two shapes: $1 + 3$ and $2 + 2$. The $1 + 3$ shape contains a linear factor, so a root search detects it. But the $2 + 2$ shape has *no linear factor and no root* — it is invisible to a root search. So "no root" is **not** sufficient for irreducibility from degree $4$ onward; one must additionally exclude a split into two quadratics. Over a small field this second exclusion is cheap: over $\mathbb{F}_2$ there is exactly *one* irreducible quadratic, $X^2 + X + 1$, so a rootless quartic that factors must equal $(X^2+X+1)^2$, and a single polynomial multiplication settles it. The general lesson for spaced practice: when testing a quartic for irreducibility, *always* do two things — search for roots, *and* compare against the (finite, enumerable) list of products of two irreducible quadratics. For higher degrees the bookkeeping grows but the principle is identical: exclude every degree pattern, not just the ones with a linear piece. This is precisely the gap that the degree-$2$/degree-$3$ root test of [[Ex - Gauss's lemma and factorization over the integers]] does *not* have.

**The test is one-directional: an irreducible reduction certifies, a reducible reduction certifies nothing.** Reduction mod $p$ is a *sufficient* condition for irreducibility, never a necessary one. The implication runs only "$\overline f$ irreducible $\Rightarrow$ $f$ irreducible". The converse is false, and $X^4 + 1$ is the canonical witness: it is irreducible over $\mathbb{Q}$ (Eisenstein after a shift), yet it is reducible modulo *every single prime*. The structural reason is illuminating — its roots are $8$th roots of unity, which live in $\mathbb{F}_{p^2}$ for every prime $p$ (because $8 \mid p^2 - 1$ for odd $p$, and $X^4+1 = (X+1)^4$ for $p=2$), so every irreducible factor mod $p$ has degree $\leq 2$ and the quartic always splits. The practical consequence is a discipline of interpretation: if you reduce mod $2$, mod $3$, mod $5$ and each reduction factors, you have learned *nothing* — the polynomial may still be irreducible. Only a prime at which the reduction comes out *irreducible* is informative. When every small prime gives a reducible reduction, the correct response is not "the polynomial is reducible" but "this test is inconclusive; switch to Eisenstein-after-substitution or another method." This asymmetry is shared by Eisenstein's criterion (also sufficient-only — see [[Ex - Irreducibility by Eisenstein's criterion]]): both tests can certify irreducibility but neither can certify reducibility, and silence from either is not a verdict.

**Different primes see different factorisations, and the *factorisation type* mod $p$ is a genuine invariant carrying arithmetic information.** Even though $X^4 + 1$ is reducible mod every prime, *how* it factors varies with $p$ — into two quadratics for some primes, into four linear factors for others, into $(X+1)^4$ at $p = 2$. This is not noise: the way a fixed polynomial decomposes modulo varying primes is one of the central objects of algebraic number theory, encoding how the prime $p$ behaves in the number field generated by a root (splitting, remaining inert, or ramifying). For the practical business of irreducibility testing, the operational takeaway is to *try several primes*: since the test only ever succeeds when a reduction is irreducible, and different primes yield different factorisation patterns, scanning $p = 2, 3, 5, 7, \dots$ maximises the chance that *some* prime delivers an irreducible reduction. If a polynomial is irreducible over $\mathbb{Q}$ and is not of the special "reducible mod every prime" type (like $X^4 + 1$), then some prime will certify it. The art of the method is the search over primes, exactly as the art of Eisenstein is the search over primes for the coefficient pattern.
