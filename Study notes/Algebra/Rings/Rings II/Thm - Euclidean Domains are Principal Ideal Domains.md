---
type: theorem
subject: ring-theory
prereqs:
  - "Def - Ring"
  - "Def - Ideal"
  - "Def - Integral Domain"
  - "Def - Euclidean Domain"
  - "Def - Principal Ideal Domain"
tags: [algebra, ring-theory]
---

# Notation

Throughout, $R$ is an [[Def - Integral Domain|integral domain]] — a nonzero commutative [[Def - Ring|ring]] with $1_R \neq 0_R$ and no zero divisors. An [[Def - Ideal|ideal]] $I \trianglelefteq R$ is **principal** if $I = (b) = \{rb : r \in R\}$ for some single element $b$; $R$ is a [[Def - Principal Ideal Domain|principal ideal domain]] (PID) if it is a domain and *every* ideal is principal. $R$ is a [[Def - Euclidean Domain|Euclidean domain]] (ED) if it is a domain carrying a **Euclidean function** $\varphi : R \setminus \{0\} \to \mathbb{Z}_{\geq 0}$ such that (i) $\varphi(ab) \geq \varphi(b)$ for all nonzero $a, b$, and (ii) **division with remainder** holds: for all $a, b \in R$ with $b \neq 0$ there exist $q, r \in R$ with $a = bq + r$ and either $r = 0$ or $\varphi(r) < \varphi(b)$. The symbol $\trianglelefteq$ means "is an ideal of"; $\mathbb{Z}_{\geq 0}$ is the non-negative integers. The full symbol registry is on the parent page [[Rings II — §2.3–2.4]].

---

# Statement

> **Euclidean domains are principal ideal domains.** Let $R$ be a [[Def - Euclidean Domain|Euclidean domain]], with Euclidean function $\varphi : R \setminus \{0\} \to \mathbb{Z}_{\geq 0}$. Then $R$ is a [[Def - Principal Ideal Domain|principal ideal domain]]: every [[Def - Ideal|ideal]] $I \trianglelefteq R$ is principal.
>
> Explicitly, if $I = \{0\}$ then $I = (0)$; and if $I \neq \{0\}$, then choosing $b \in I \setminus \{0\}$ with $\varphi(b)$ minimal gives $I = (b)$.

---

# Motivation

Every integer ideal you have ever met is of the form $n\mathbb{Z}$ — the multiples of a single integer. There is no ideal of $\mathbb{Z}$ that needs *two* generators; "$(6, 10)$" is just a long-winded name for $(2)$. This is not an accident, and the reason it is true is that $\mathbb{Z}$ has the *Euclidean algorithm*: given any two integers you can do long division, and the remainder is genuinely smaller. The question this theorem answers is: **was the Euclidean algorithm the real reason all [[Def - Ideal|ideals]] of $\mathbb{Z}$ are principal?** If so, then *any* ring with a working division-with-remainder should have the same property.

The answer is yes, and the value of the theorem is that it isolates the *exact* feature of $\mathbb{Z}$ responsible for the one-generator phenomenon. The feature is the Euclidean function: a size measure $\varphi$ for which you can always divide and get a strictly smaller remainder. That is a modest, checkable hypothesis — and the polynomial ring $F[X]$ has it (with $\varphi = \deg$), and the Gaussian integers $\mathbb{Z}[i]$ have it (with $\varphi =$ norm). So the moment you verify division-with-remainder in some ring, you get for *free* that all of its ideals are principal — a strong structural conclusion bought with a single, concrete check.

This matters because being a PID is a powerful property and being principal is awkward to verify ideal-by-ideal. There are infinitely many ideals; you cannot inspect them one at a time. The theorem replaces "check every ideal is principal" — an infinite task — with "exhibit one Euclidean function" — a single task. And it sits at the top of a chain of implications, Euclidean domain $\Rightarrow$ PID $\Rightarrow$ [[Thm - Principal Ideal Domains are Unique Factorization Domains|unique factorisation domain]], so a Euclidean function ultimately certifies *unique factorisation* as well. The whole edifice of "$\mathbb{Z}$-like" arithmetic — principal ideals, greatest common divisors, unique factorisation — rests on the single foundation of division with remainder, and this theorem is the first girder.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$R$ is a Euclidean domain". The skill is recognising a Euclidean function where the problem names none.

The first disguised source is **a ring of polynomials over a field**. The property $B$ is "$R = F[X]$ with $F$ a field". The bridge is that $\varphi(f) = \deg f$ is a Euclidean function: polynomial long division over a field always terminates with a remainder of strictly smaller degree, because the leading coefficient of the divisor is invertible. The non-obvious part is that degree, an entirely combinatorial gadget, satisfies the Euclidean axioms. *Example problem:* show every ideal of $\mathbb{Q}[X]$ is principal — apply the theorem with $\varphi = \deg$.

The second disguised source is **a subring of $\mathbb{C}$ on which a norm controls geometry**. The property $B$ is "$R \leq \mathbb{C}$ and every complex number lies within distance $1$ of a point of $R$". The bridge is that the norm $\varphi(z) = |z|^2$ is then Euclidean: to divide $a$ by $b$, look at $a/b \in \mathbb{C}$, round it to a nearby point $q \in R$ at distance $< 1$, and the remainder $r = a - bq$ has $\varphi(r) = |b|^2|a/b - q|^2 < |b|^2 = \varphi(b)$. The non-obviousness: a *geometric* covering condition on the ring becomes the *algebraic* division axiom. *Example problem:* show $\mathbb{Z}[i]$ is a PID — it is Euclidean because the unit lattice covers $\mathbb{C}$ within distance $1$.

The third disguised source is **a ring known to have a working "greatest common divisor by repeated reduction" algorithm**. The property $B$ is "the classical Euclidean algorithm runs in $R$ and terminates". Wherever a course has said "Euclidean algorithm", there is a Euclidean function, and the theorem applies. The non-obvious step is recognising that the *termination* of the gcd algorithm is exactly the strict-decrease axiom (ii) in disguise. *Example problem:* any ring in which you can compute gcds by iterated remainders is a PID.

**Targets (Output Amplification)**

The conclusion is "$R$ is a PID — every ideal is $(b)$ for one element $b$".

Combine the conclusion with **the PID $\Rightarrow$ UFD theorem**. By [[Thm - Principal Ideal Domains are Unique Factorization Domains|principal ideal domains are unique factorisation domains]], a PID has unique factorisation into irreducibles. The further result $E$: a Euclidean domain is a UFD — so verifying one Euclidean function delivers the *entire* unique-factorisation theory. This is non-obvious because division with remainder says nothing overtly about factorisation, yet it implies it through the principal-ideal property.

Combine "every ideal is principal" with **a finitely generated ideal you wish to collapse**. Given an ideal $(a_1,\dots,a_n)$, the theorem says it equals $(d)$ for a single $d$, and $d$ is then a greatest common divisor of the $a_i$. The further result $E$ is the existence of gcds *and* Bézout's identity: $d = (d) = (a_1,\dots,a_n)$ means $d = \sum r_i a_i$ for some $r_i$. The non-obvious payoff: the abstract statement "$I$ is principal" secretly contains the concrete, computational Bézout relation.

Combine the conclusion with **the ascending chain condition**. A PID satisfies the ACC on ideals (any increasing chain stabilises), since the union of a chain is a principal ideal $(a)$ and $a$ already lives at a finite stage. The further result $E$ is that a Euclidean domain is *Noetherian*, which is the engine behind the *existence* half of factorisation into irreducibles. Recognising that "Euclidean" silently implies "Noetherian" is the non-obvious link.

---

# Why Is It True

Start with the picture in $\mathbb{Z}$, because the general proof is that picture with the word "size" left abstract. Take an ideal $I$ of $\mathbb{Z}$, not the zero ideal. It contains some nonzero numbers; among those, look at the one *closest to zero* — the smallest in absolute value. Call it $b$. The claim is that $b$ single-handedly generates $I$: every element of $I$ is a multiple of $b$. Why? Because if some $a \in I$ were *not* a multiple of $b$, you could divide $a$ by $b$ and get a nonzero remainder $r$, and that remainder would be *smaller than $b$*. But $r = a - (\text{multiple of } b)$, and both $a$ and the multiple of $b$ live in $I$, so $r$ lives in $I$ too. Now you have an element of $I$ — namely $r$ — that is nonzero and smaller than $b$. That contradicts the choice of $b$ as the *smallest* nonzero element. The only way out is that there is no such $a$: every element of $I$ *is* a multiple of $b$.

That is the entire argument, and every step generalises. The notion of "size" was the absolute value; in a general Euclidean domain it is the Euclidean function $\varphi$. The fact that you can "divide and get a smaller remainder" was the division algorithm for integers; in a Euclidean domain it is, by definition, axiom (ii). The fact that "smallest" makes sense — that a non-empty set of sizes has a least element — used that the sizes are non-negative integers, and $\varphi$ also lands in $\mathbb{Z}_{\geq 0}$, where the well-ordering principle guarantees a minimum. So the proof rests on a tripod:

1. *There is a smallest element to pick.* The sizes $\varphi(x)$ of nonzero elements of $I$ form a non-empty subset of $\mathbb{Z}_{\geq 0}$, which therefore has a least element; pick $b$ achieving it. This is why $\varphi$ must take values in the *well-ordered* set $\mathbb{Z}_{\geq 0}$ — well-ordering is exactly what makes "minimise $\varphi$" a legal move.

2. *Dividing keeps you inside $I$.* The remainder $r = a - bq$ is a difference of two members of $I$ (recall $a \in I$, and $bq \in I$ because ideals absorb multiplication), so $r \in I$. The ideal axioms are precisely engineered so that division does not eject you from the ideal.

3. *A nonzero remainder would be too small.* Division with remainder gives $r = 0$ or $\varphi(r) < \varphi(b)$. The second option produces a nonzero element of $I$ with size below the minimum — impossible. So $r = 0$, meaning $b \mid a$.

The deep point: $b$ is the element of $I$ "of minimal size", and minimal size is exactly the obstruction to being further reducible. The Euclidean function turns the qualitative idea "$b$ is as simple as possible" into a quantitative, minimisable number, and the division axiom guarantees that anything not yet a multiple of $b$ can be made *strictly simpler* — which, against a true minimum, cannot happen. One should *expect* every ideal to be principal in any ring where "keep dividing, the remainder shrinks" is a legal procedure, because that procedure cannot run forever, and where it stops is exactly a single generator.

---

# What Makes This Hard

The proof is short, and the difficulty is entirely in *believing the minimum exists and is the right thing to pick*: the non-obvious move is to extremise — to choose $b\in I\setminus\{0\}$ with $\varphi(b)$ minimal — and this is legal only because $\varphi$ takes values in the well-ordered set $\mathbb{Z}_{\geq 0}$. The most common error is to forget *why* the remainder $r = a - bq$ lies back in $I$ (it is the ideal-absorption axiom: $bq \in I$ since $b \in I$, and $a - bq \in I$ since $I$ is closed under subtraction), and a second frequent slip is to omit the $I = \{0\}$ case, where there is no nonzero element to minimise over and one writes $I = (0)$ directly.

---

# Rederivation Scaffold

**High-level strategy:**
Take an arbitrary ideal $I$; dispose of $I = \{0\}$ separately. For $I \neq \{0\}$, pick the nonzero element $b \in I$ of minimal Euclidean value. Show $I = (b)$ by proving both inclusions: $(b) \subseteq I$ is immediate, and $I \subseteq (b)$ comes from dividing an arbitrary $a \in I$ by $b$ and forcing the remainder to be $0$.

**Subgoal decomposition:**

1. **Handle the zero ideal.** If $I = \{0\}$, observe $I = (0)$, principal.
   - *Hint:* $(0) = \{r\cdot 0 : r\in R\} = \{0\}$.
   - *Why needed:* The minimisation step needs a nonzero element to operate on; the zero ideal has none.

2. **Pick a minimal generator.** For $I \neq \{0\}$, choose $b \in I \setminus \{0\}$ with $\varphi(b)$ minimal.
   - *Hint:* $\{\varphi(x) : x \in I, x \neq 0\}$ is a non-empty subset of $\mathbb{Z}_{\geq 0}$, which has a least element by well-ordering; let $b$ realise it.
   - *Why needed:* Minimality of $\varphi(b)$ is the contradiction lever in step 4.

3. **Show $(b) \subseteq I$.** Every multiple of $b$ lies in $I$.
   - *Hint:* $b \in I$ and $I$ is an ideal, so $rb \in I$ for all $r \in R$.
   - *Why needed:* It is the easy inclusion; half of $I = (b)$.

4. **Show $I \subseteq (b)$.** Every $a \in I$ is a multiple of $b$.
   - *Hint:* Divide: $a = bq + r$ with $r = 0$ or $\varphi(r) < \varphi(b)$. Note $r = a - bq \in I$. If $r \neq 0$, then $\varphi(r) < \varphi(b)$ contradicts minimality. So $r = 0$ and $a = bq \in (b)$.
   - *Why needed:* It is the hard inclusion; combined with step 3 it yields $I = (b)$, principal.

---

# Lemma Decomposition

> [!note]- Lemma 1: A non-empty set of non-negative integers has a least element
> **Statement:** Every non-empty subset $A \subseteq \mathbb{Z}_{\geq 0}$ has a minimum element.
>
> **Hint:** This is the well-ordering principle of $\mathbb{Z}_{\geq 0}$.
>
> **Why needed:** It licenses the central move of the proof — choosing an element of $I$ with *minimal* Euclidean value. Without well-ordering, "minimise $\varphi$" would be illegal.
>
> > [!note]- Full proof
> > This is the well-ordering principle for the non-negative integers, a defining property of $\mathbb{Z}_{\geq 0}$ (equivalent to the principle of mathematical induction). Given a non-empty $A \subseteq \mathbb{Z}_{\geq 0}$, pick any $n \in A$. The set $A \cap \{0, 1, \dots, n\}$ is non-empty (it contains $n$) and finite, so it has a least element $m$. Any element of $A$ is either $\leq n$, hence $\geq m$ by choice of $m$, or $> n \geq m$; so $m \leq a$ for all $a \in A$, and $m$ is the minimum of $A$. It is essential that the Euclidean function $\varphi$ takes values in $\mathbb{Z}_{\geq 0}$ precisely so this lemma applies to the set of values $\{\varphi(x) : x \in I \setminus \{0\}\}$.

> [!note]- Lemma 2: The remainder of an ideal element by an ideal element stays in the ideal
> **Statement:** Let $I \trianglelefteq R$, let $a, b \in I$, and let $q \in R$. Then $a - bq \in I$.
>
> **Hint:** Use the two ideal axioms: absorption of multiplication, and closure under subtraction.
>
> **Why needed:** It is what guarantees the remainder $r = a - bq$ produced by division lands back inside $I$, so that a small nonzero remainder would genuinely contradict the minimality of $b$.
>
> > [!note]- Full proof
> > Since $b \in I$ and $I$ is an ideal, $I$ absorbs multiplication by arbitrary ring elements, so $bq \in I$ for every $q \in R$. Since $a \in I$ and $bq \in I$, and $I$ is an additive [[Def - Subgroup|subgroup]] of $R$ (hence closed under subtraction), $a - bq \in I$. So the remainder $r := a - bq$ in any division $a = bq + r$ with $a, b \in I$ satisfies $r \in I$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $R$ be a Euclidean domain with Euclidean function $\varphi : R \setminus \{0\} \to \mathbb{Z}_{\geq 0}$, and let $I \trianglelefteq R$ be an arbitrary ideal. We show $I$ is principal.
>
> **Case 1 — $I = \{0\}$.** Then $I = (0) = \{r \cdot 0 : r \in R\}$, which is principal, generated by $0$.
>
> **Case 2 — $I \neq \{0\}$.** Then $I$ contains a nonzero element, so the set of values
> $$V = \{\varphi(x) : x \in I,\ x \neq 0\} \subseteq \mathbb{Z}_{\geq 0}$$
> is non-empty. By Lemma 1 (well-ordering of $\mathbb{Z}_{\geq 0}$), $V$ has a least element. Choose $b \in I \setminus \{0\}$ with $\varphi(b)$ equal to this minimum, so
> $$\varphi(b) \leq \varphi(x) \quad\text{for every } x \in I \setminus \{0\}. \tag{$\star$}$$
> We claim $I = (b)$.
>
> **$(b) \subseteq I$.** Since $b \in I$ and $I$ is an ideal, $rb \in I$ for every $r \in R$. Hence $(b) = \{rb : r \in R\} \subseteq I$.
>
> **$I \subseteq (b)$.** Let $a \in I$ be arbitrary. Since $b \neq 0$, division with remainder (Euclidean axiom (ii)) supplies $q, r \in R$ with
> $$a = bq + r, \qquad \text{where } r = 0 \ \text{ or } \ \varphi(r) < \varphi(b).$$
> By Lemma 2, $r = a - bq \in I$ (as $a, b \in I$). Suppose, for contradiction, that $r \neq 0$. Then $r$ is a nonzero element of $I$, so by $(\star)$ we must have $\varphi(b) \leq \varphi(r)$. But division gave $\varphi(r) < \varphi(b)$ — a contradiction. Therefore $r = 0$, and
> $$a = bq \in (b).$$
> As $a \in I$ was arbitrary, $I \subseteq (b)$.
>
> **Conclusion.** Both inclusions hold, so $I = (b)$ is principal. In Case 1 the ideal was also principal. Since $I$ was an arbitrary ideal and $R$ is an integral domain, $R$ is a principal ideal domain. $\blacksquare$
>
> *(Remark: this is verbatim the classical proof that every ideal of $\mathbb{Z}$ is principal, with the absolute value $|\cdot|$ replaced by the Euclidean function $\varphi$. Euclidean axiom (i), $\varphi(ab) \geq \varphi(b)$, is not needed for this proof — only the division axiom (ii) and the integer-valuedness of $\varphi$.)*

---

# Cross-Field Exercise Suggestions

**Gaussian integers and sums of two squares.** The ring $\mathbb{Z}[i]$ is Euclidean with $\varphi(z) = |z|^2$ (geometrically: every point of $\mathbb{C}$ lies within distance $1$ of a lattice point). The theorem makes $\mathbb{Z}[i]$ a PID, and PIDs are UFDs, which is the structural backbone of the classification of which integers are sums of two squares. The application is nonobvious because a *number-theoretic* question ("is $n$ a sum of two squares?") is answered by the *ideal-theoretic* fact that $\mathbb{Z}[i]$ has all ideals principal, traced back to a geometric covering property.

**Minimal polynomials of matrices.** For a field $F$, the ring $F[X]$ is Euclidean (with $\varphi = \deg$), hence a PID. Given a square matrix $A$, the set $I = \{f \in F[X] : f(A) = 0\}$ is an ideal of $F[X]$; the theorem says $I = (m)$ for a single polynomial $m$, the *minimal polynomial* of $A$. The application is nonobvious because the very *existence* of a minimal polynomial — and the fact that it divides every polynomial annihilating $A$ — is a corollary of "every ideal of $F[X]$ is principal", which is a corollary of $F[X]$ being Euclidean.

**Bézout's identity in disguise.** In any Euclidean domain, the ideal $(a, b)$ generated by two elements equals $(d)$ for a single $d$, and $d = ra + sb$ for some ring elements $r, s$ — Bézout's identity. The application is nonobvious because Bézout's identity is normally derived by *running* the Euclidean algorithm, whereas here it falls out *structurally*: the theorem says the two-generated ideal is principal, and a generator of $(a,b)$ is automatically an $R$-linear combination of $a$ and $b$.

**Power series [[Def - Ring|rings]] and a degree-of-vanishing function.** The ring $F[[X]]$ of formal power series over a field is Euclidean with $\varphi(f) =$ the order of vanishing of $f$ (the index of the lowest nonzero coefficient). The theorem then makes $F[[X]]$ a PID — indeed its only ideals are $(X^n)$. The application is out-of-distribution because $F[[X]]$ is an infinite, completed object, yet the same minimise-the-Euclidean-function argument pins down every ideal; the disguised Euclidean function is an order of vanishing rather than a degree or a norm.

---

# Bridges

- **[[Def - Euclidean Domain|Euclidean Domain]]** and **[[Def - Principal Ideal Domain|Principal Ideal Domain]]** — this theorem is the bridge ED $\Rightarrow$ PID. The implication is strict: there exist principal ideal domains that carry no Euclidean function at all (e.g. $\mathbb{Z}[\tfrac{1+\sqrt{-19}}{2}]$), so "Euclidean" is genuinely stronger than "PID". The value of "Euclidean" is that it is *constructively checkable* — exhibit one function — whereas "PID" quantifies over all ideals.

- **[[Thm - Principal Ideal Domains are Unique Factorization Domains|Principal Ideal Domains are Unique Factorization Domains]]** — the next link in the chain. Composing the two gives Euclidean domain $\Rightarrow$ PID $\Rightarrow$ UFD, so a single Euclidean function ultimately certifies unique factorisation into irreducibles.

- **The classical proof that every ideal of $\mathbb{Z}$ is principal** — the special case from which this theorem is abstracted. That proof minimises the absolute value of a nonzero ideal element; this theorem replaces $|\cdot|$ with an abstract Euclidean function $\varphi$, changing nothing else.

- **The Euclidean algorithm for $\gcd$** — the same hypothesis, used algorithmically rather than structurally. Division with remainder, axiom (ii), is exactly what makes the iterative gcd algorithm terminate; here the same axiom is used in a single non-iterative step to locate a generator.

- **Noetherian rings and the ascending chain condition** — a PID satisfies the ACC on ideals, so a Euclidean domain is Noetherian. This is the link by which "Euclidean" feeds into the *existence* half of factorisation in [[Thm - Principal Ideal Domains are Unique Factorization Domains|the PID Rightarrow UFD theorem]].

---

# Unlocked by This

> [!tip] Smith Normal Form and Modules over a PID *(from Module Theory)*
> Because Euclidean domains are PIDs, the structure theorem for finitely generated modules over a PID applies to $\mathbb{Z}$ and to $F[X]$. Over $\mathbb{Z}$ this is the classification of finitely generated abelian groups; over $F[X]$ it yields the rational and Jordan canonical forms of a linear operator.

> [!tip] Dedekind Domains and Ideal Factorisation *(from Algebraic Number Theory)*
> Rings of integers in number fields are usually *not* PIDs, and the failure is measured by the class group. The PID case — reached via a Euclidean function — is the well-behaved extreme, and contrasting it with the general case motivates the theory of unique factorisation of *ideals* in Dedekind domains.
