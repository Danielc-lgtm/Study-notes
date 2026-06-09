---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Going Down for Integrally Closed Domains"
  - "Def - Integral Closure and Normal Domain"
  - "Def - Lying Over, Going Up, Going Down"
  - "Def - The Induced Map on Spectra"
  - "Def - Prime and Maximal Ideal"
tags: [algebra, commutative-algebra]
---

# Problem Statement

The [[Thm - Going Down for Integrally Closed Domains|going-down theorem]] requires the base ring $A$ to be an integrally closed domain. **Show this hypothesis is essential** by exhibiting an integral extension $A \subseteq B$, with $A$ *not* integrally closed, for which going down *fails*: there are primes $\mathfrak{p}_2 \subsetneq \mathfrak{p}_1$ in $A$ and a prime $\mathfrak{q}_1 \in \operatorname{Spec} B$ over $\mathfrak{p}_1$ such that **no** prime $\mathfrak{q}_2 \in \operatorname{Spec} B$ satisfies $\mathfrak{q}_2 \subseteq \mathfrak{q}_1$ and $\mathfrak{q}_2 \cap A = \mathfrak{p}_2$.

Use the "**two lines glued at a point**":
$$B = k[u] \times k[v], \qquad A = \{(f, g) \in B : f(0) = g(0)\},$$
the subring of pairs of polynomials agreeing at the origin. ($k$ is a field.) Show:

1. $A \subseteq B$ is an integral extension, and $A$ is *not* an integrally closed domain (indeed $A$ is not even a domain);
2. the spectra are "two lines meeting at a point" downstairs and "two disjoint lines" upstairs, with the map $\iota^*$ gluing the two origins;
3. with $\mathfrak{p}_1$ the glue point and $\mathfrak{p}_2$ the generic point of one component, and $\mathfrak{q}_1$ the origin of the *other* component upstairs, going down fails.

**Recall:**

The objects in play are the going-down property, integrally closed (normal) domains, the induced map on spectra, and the prime ideals of a product ring.

![[Def - Lying Over, Going Up, Going Down#Going down]]

A domain $A$ is **[[Def - Integral Closure and Normal Domain|integrally closed]]** (normal) if every element of $\operatorname{Frac} A$ integral over $A$ already lies in $A$; more generally, a reduced ring is integrally closed in its total quotient ring if every integral element of that ring already lies in it. The going-down theorem needs $A$ to be a normal *domain*. The example below is non-normal because its integral closure (in its total quotient ring) is strictly larger — the idempotent $(1,0)$ is integral over $A$ but not in $A$.

**Primes of a product.** For $B = R_1 \times R_2$, every ideal is $I_1 \times I_2$, and $\operatorname{Spec} B = \operatorname{Spec} R_1 \sqcup \operatorname{Spec} R_2$: a prime is either $\mathfrak{p}_1 \times R_2$ ($\mathfrak{p}_1 \in \operatorname{Spec} R_1$) or $R_1 \times \mathfrak{p}_2$ ($\mathfrak{p}_2 \in \operatorname{Spec} R_2$). (Because $e = (1,0)$ is idempotent, every prime contains exactly one of $e$, $1-e$.) For $B = k[u]\times k[v]$, $\operatorname{Spec} B$ is two disjoint copies of $\operatorname{Spec} k[t]$ = the affine line.

---

# Convergent Strategy

**Problem class.** This is a *construct-a-counterexample* problem — disprove a universal statement by building one instance where it breaks. As the [[Commutative Algebra VIII — Going Up and Going Down#Problem-Solving Strategy|topic-page strategy]] records, when asked to *disprove* going down, look for a "gluing" of the base that creates two branches over one point with no shared specialisation downstairs — exactly the non-normality the hypothesis rules out.

**Assumption pattern.** The construction is engineered so that $A$ fails the *one* hypothesis going down needs: normality. By gluing two lines at a point, $A$ acquires a singular point (the glue), and its normalization is precisely $B$ = the two separated lines. The recognisable pattern: a non-normal ring is one whose normalization $B$ "pulls apart" a singularity into several branches, and going down fails exactly at the singular point because a preimage on *one* branch cannot specialise to a point on *another* branch.

**Theorem routing.** The route is: verify $A \subseteq B$ integral (the idempotent $e = (1,0)$ satisfies $e^2 = e$, so $B = A + Ae$ is module-finite); identify $\operatorname{Spec} A$ (two lines meeting at the glue point $P$) and $\operatorname{Spec} B$ (two disjoint lines); compute the contraction map $\iota^*$ (it glues the two origins to $P$, is a bijection elsewhere); choose the failing data $\mathfrak{p}_2 \subsetneq \mathfrak{p}_1 = P$ on the $u$-component and $\mathfrak{q}_1$ the origin of the $v$-component; observe that the only prime $\subseteq \mathfrak{q}_1$ is the generic point of the $v$-component, which contracts to the *$v$*-component prime, not $\mathfrak{p}_2$.

**Key decision point.** The non-obvious construction is the *glued* ring $A = \{(f,g) : f(0) = g(0)\}$ — neither $k[u]\times k[v]$ nor a polynomial ring, but the "node" obtained by identifying the two origins. The genuine insight is choosing $\mathfrak{q}_1$ on the *opposite* branch from $\mathfrak{p}_2$: $\mathfrak{p}_2$ is the generic point of the $u$-line, but $\mathfrak{q}_1$ is the origin of the $v$-line, and below $\mathfrak{q}_1$ there is *only* the $v$-line's generic point — which sits over the $v$-line downstairs, not the $u$-line. The branches do not communicate below the glue point. (A reader who picks $\mathfrak{q}_1$ on the *same* branch as $\mathfrak{p}_2$ will find going down *succeeds* there, missing the failure.)

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra VIII — Going Up and Going Down#Legal Operations|the topic page's Legal Operations]]:

1. **Verify integrality via module-finiteness (operation 9, integrality form).** $B = A + Ae$ with $e = (1,0)$ idempotent, so $B$ is a finite $A$-module, hence integral.

2. **Read primes of $B$ off the product decomposition.** $\operatorname{Spec}(k[u]\times k[v]) = \operatorname{Spec} k[u] \sqcup \operatorname{Spec} k[v]$, two disjoint lines.

3. **Compute the contraction map explicitly.** Determine $\iota^*(\mathfrak{q}) = \mathfrak{q} \cap A$ for each prime $\mathfrak{q}$ of $B$, finding that the two origins glue to $P$.

4. **Exhibit the failure by exhausting the candidates.** List every prime $\subseteq \mathfrak{q}_1$ and check none contracts to $\mathfrak{p}_2$ — a finite check because $\mathfrak{q}_1$ has height $1$.

---

# Hints

> [!note]- Hint 1
> Going down needs $A$ *normal*. So pick a *non-normal* $A$ — and the canonical way to make one is to *glue*: take two lines $\operatorname{Spec} k[u]$ and $\operatorname{Spec} k[v]$ and identify their origins. Algebraically, the functions on the glued space are the pairs $(f,g)$ with $f(0) = g(0)$. Its normalization is the ungLued $B = k[u]\times k[v]$.

> [!note]- Hint 2
> First get the geometry. $\operatorname{Spec} B = \operatorname{Spec} k[u] \sqcup \operatorname{Spec} k[v]$ is *two disjoint lines*. $\operatorname{Spec} A$ is *two lines meeting at one point* $P$ (the glue). The map $\iota^* : \operatorname{Spec} B \to \operatorname{Spec} A$ is a bijection away from the origins, but sends *both* origins $(u) \times k[v]$ and $k[u] \times (v)$ to the single point $P$.

> [!note]- Hint 3
> Now set up the failing chain. Downstairs, take $\mathfrak{p}_1 = P$ (the glue point, a maximal ideal) and let $\mathfrak{p}_2$ be the generic point of the $u$-line (the prime of functions vanishing on the $u$-component). So $\mathfrak{p}_2 \subsetneq \mathfrak{p}_1$. Upstairs, let $\mathfrak{q}_1$ be the origin of the $v$-line — note: the *other* branch. Check $\mathfrak{q}_1$ lies over $\mathfrak{p}_1 = P$.

> [!note]- Hint 4
> Going down asks for $\mathfrak{q}_2 \subseteq \mathfrak{q}_1$ over $\mathfrak{p}_2$. The only primes $\subseteq \mathfrak{q}_1$ (the $v$-origin) are $\mathfrak{q}_1$ itself and the generic point of the $v$-line. The $v$-line's generic point contracts to the $v$-component prime in $A$ — *not* to $\mathfrak{p}_2$, which is the $u$-component prime. So no $\mathfrak{q}_2$ works: going down fails. The branches do not talk below the glue.

---

# Solution

The proof builds the non-normal ring $A$ by gluing two lines at the origin, computes its spectrum as a node, and exhibits the failure on the branch *opposite* to a chosen base specialisation. The mechanism: a preimage point sitting on the $v$-branch can only specialise *within* the $v$-branch, but the base prime $\mathfrak{p}_2$ lives on the $u$-branch, so there is nothing below $\mathfrak{q}_1$ to lie over it.

**Step 1: $A \subseteq B$ is an integral extension, and $A$ is non-normal (not even a domain).**

$B = A[e]$ with $e = (1,0)$ idempotent ($e^2 = e$), so $B = A + Ae$ is module-finite over $A$, hence integral. And $A$ is non-normal: the idempotent $e$ is integral over $A$ and lies in the total quotient ring of $A$, yet $e \notin A$, so $A$ is strictly smaller than its integral closure $B$.

> [!note]- Derivation
> First, $A$ is a subring of $B = k[u]\times k[v]$: it contains $(1,1) = 1_B$, and is closed under sums and products because "$f(0) = g(0)$" is preserved (if $(f,g), (f',g') \in A$ then $(f+f')(0) = f(0)+f'(0) = g(0)+g'(0) = (g+g')(0)$, similarly for products). So $A \subseteq B$.
>
> *Integrality.* The idempotent $e = (1,0)$ satisfies $e^2 - e = (1,0) - (1,0) = 0$, a monic relation over $A$ (indeed over the prime subring), so $e$ is integral over $A$. Likewise $u' := (u, 0)$ and $v' := (0, v)$: note $(u,0) = (u,u)\cdot(1,0)$ where $(u,u) \in A$ (it has $u(0) = 0 = u(0)$) and $(1,0) = e$; and $B$ is generated as a ring over $A$ by $e$ (since $(0,v) = (v,v)(0,1) = (v,v)(1-e)$ with $(v,v) \in A$, and $(u,0) = (u,u)e$). So $B = A[e] = A + Ae$ (as $e^2 = e$ collapses higher powers), a finitely generated $A$-module. By the module-finite criterion for integrality, $A \subseteq B$ is integral.
>
> *Non-normality.* $A$ is not normal because it is not a domain in the way required — more precisely, $A$ is reduced but its normalization in its total ring of fractions is $B \neq A$. The element $e = (1,0) \in B$ is integral over $A$ (root of $X^2 - X$) and lies in the total quotient ring of $A$, but $e \notin A$ (its components $1, 0$ disagree at the origin: $1 \neq 0$). So $A$ is strictly smaller than its integral closure $B$ — $A$ fails to be integrally closed. (This is exactly the obstruction: $B$ is the normalization of $A$, separating the glued branches.)

**Step 2: $\operatorname{Spec} B$ is two disjoint lines; $\operatorname{Spec} A$ is two lines glued at a point $P$.**

The primes of $B = k[u]\times k[v]$ are the two families $\mathfrak{a}\times k[v]$ and $k[u]\times\mathfrak{b}$; downstairs, the only identification $A$ makes is to fuse the two origins into one maximal ideal $P$.

> [!note]- Derivation
> *Upstairs.* By the product description, $\operatorname{Spec} B = \operatorname{Spec} k[u] \sqcup \operatorname{Spec} k[v]$. The relevant primes:
> - $\eta_u = (0)\times k[v]$ — the generic point of the $u$-line (functions vanishing on the whole $u$-component);
> - $O_u = (u)\times k[v]$ — the origin of the $u$-line;
> - $\eta_v = k[u]\times(0)$ — the generic point of the $v$-line;
> - $O_v = k[u]\times(v)$ — the origin of the $v$-line.
>
> These satisfy $\eta_u \subsetneq O_u$ and $\eta_v \subsetneq O_v$, and there are no inclusions between a $u$-prime and a $v$-prime (the two lines are disjoint).
>
> *Downstairs.* Contracting to $A$:
> - $O_u \cap A = \{(f,g) \in A : f \in (u)\} = \{(f,g) : f(0) = 0,\ f(0)=g(0)\} = \{(f,g) : f(0) = g(0) = 0\} =: P$.
> - $O_v \cap A = \{(f,g) \in A : g(0) = 0\} = \{(f,g) : f(0) = g(0) = 0\} = P$ — the **same** maximal ideal.
>
> So both origins contract to the single maximal ideal $P = \{(f,g) \in A : f(0) = g(0) = 0\}$. This is the *glue point*: the two lines of $\operatorname{Spec} B$ are sewn together at their origins to form the node $\operatorname{Spec} A$.
> - $\eta_u \cap A = \{(f,g) \in A : f = 0\} = \{(0, g) : g \in k[v],\ g(0) = 0\} =: \mathfrak{p}_u$ — the prime of the $u$-component.
> - $\eta_v \cap A = \{(f,g) \in A : g = 0\} = \{(f, 0) : f(0) = 0\} =: \mathfrak{p}_v$ — the prime of the $v$-component.
>
> Note $\mathfrak{p}_u \subsetneq P$ and $\mathfrak{p}_v \subsetneq P$ (each component prime is contained in the glue maximal ideal), and $\mathfrak{p}_u \neq \mathfrak{p}_v$.

**Step 3: The failing data — $\mathfrak{p}_2 = \mathfrak{p}_u \subsetneq P = \mathfrak{p}_1$ and $\mathfrak{q}_1 = O_v$ over $P$.**

Choose $\mathfrak{p}_1 = P$, $\mathfrak{p}_2 = \mathfrak{p}_u$ (so $\mathfrak{p}_2 \subsetneq \mathfrak{p}_1$), and $\mathfrak{q}_1 = O_v$ — the origin of the $v$-line, which lies over $P$.

> [!note]- Derivation
> From Step 2, $\mathfrak{p}_u \subsetneq P$ is a strict inclusion of primes of $A$, so it is a valid descending pair $\mathfrak{p}_1 = P \supsetneq \mathfrak{p}_2 = \mathfrak{p}_u$. The prime $\mathfrak{q}_1 = O_v = k[u]\times(v)$ of $B$ contracts to $P$ (computed in Step 2), so $\mathfrak{q}_1$ lies over $\mathfrak{p}_1 = P$. This is exactly the input to going down: a descending pair downstairs and a prime over the top, $\mathfrak{q}_1$. The crucial — and deliberate — choice is that $\mathfrak{q}_1$ sits on the *$v$*-branch, while $\mathfrak{p}_2 = \mathfrak{p}_u$ is the *$u$*-branch prime.

**Step 4: No $\mathfrak{q}_2 \subseteq \mathfrak{q}_1$ contracts to $\mathfrak{p}_2$ — going down fails.**

The only primes contained in $\mathfrak{q}_1 = O_v$ are $O_v$ itself and $\eta_v$; the former contracts to $P \neq \mathfrak{p}_2$, the latter to $\mathfrak{p}_v \neq \mathfrak{p}_2$. So no $\mathfrak{q}_2$ works.

> [!note]- Derivation
> The primes of $B$ contained in $\mathfrak{q}_1 = O_v = k[u]\times(v)$ are exactly the primes $\subseteq O_v$. Since $O_v$ is a $v$-line prime of height $1$ (the chain $\eta_v \subsetneq O_v$), the only primes below it are:
> - $O_v$ itself, with $O_v \cap A = P \neq \mathfrak{p}_u = \mathfrak{p}_2$;
> - $\eta_v = k[u]\times(0)$, with $\eta_v \cap A = \mathfrak{p}_v \neq \mathfrak{p}_u = \mathfrak{p}_2$.
>
> (No $u$-line prime is contained in $O_v$, because the two lines are disjoint in $\operatorname{Spec} B$: a $u$-prime $\mathfrak{a}\times k[v]$ contains $(0,1) = 1 - e$, while $O_v = k[u]\times(v)$ does not contain $(0,1)$ since $1 \notin (v)$ — so a $u$-prime is never $\subseteq O_v$.)
>
> Neither candidate contracts to $\mathfrak{p}_2 = \mathfrak{p}_u$. Therefore **there is no prime $\mathfrak{q}_2 \in \operatorname{Spec} B$ with $\mathfrak{q}_2 \subseteq \mathfrak{q}_1$ and $\mathfrak{q}_2 \cap A = \mathfrak{p}_2$**. Going down fails for the integral extension $A \subseteq B$. The obstruction is geometric: $\mathfrak{q}_1$ lives on the $v$-branch, and everything below it stays on the $v$-branch, but $\mathfrak{p}_2$ demands a point on the $u$-branch — the two branches do not communicate below the glue point, which is precisely the non-normality of $A$. $\blacksquare$

> [!note]- Complete formal solution
> Let $k$ be a field, $B = k[u] \times k[v]$, and $A = \{(f,g) \in B : f(0) = g(0)\}$.
>
> **$A \subseteq B$ is integral, $A$ non-normal.** $A$ is a subring of $B$ ($1_B \in A$; the condition $f(0)=g(0)$ is closed under $+, \times$). The idempotent $e = (1,0)$ satisfies $e^2 = e$, and $B = A + Ae$ is a finite $A$-module (as $(u,0) = (u,u)e$, $(0,v) = (v,v)(1-e)$, with $(u,u), (v,v) \in A$), so $A \subseteq B$ is integral. But $e \in B$ is integral over $A$ (root of $X^2 - X$), lies in the total quotient ring of $A$, and $e \notin A$ (since $1 \neq 0$); so $A$ is not integrally closed — $B$ is its normalization.
>
> **Spectra.** $\operatorname{Spec} B = \operatorname{Spec} k[u] \sqcup \operatorname{Spec} k[v]$. Writing $\eta_u = (0)\times k[v]$, $O_u = (u)\times k[v]$, $\eta_v = k[u]\times(0)$, $O_v = k[u]\times(v)$, contraction to $A$ gives $O_u \cap A = O_v \cap A = P := \{(f,g)\in A : f(0)=g(0)=0\}$ (a maximal ideal, the glue point), $\eta_u\cap A = \mathfrak{p}_u := \{(0,g)\in A\}$, $\eta_v\cap A = \mathfrak{p}_v := \{(f,0)\in A\}$, with $\mathfrak{p}_u, \mathfrak{p}_v \subsetneq P$ and $\mathfrak{p}_u \neq \mathfrak{p}_v$.
>
> **Failure.** Take $\mathfrak{p}_1 = P \supsetneq \mathfrak{p}_2 = \mathfrak{p}_u$ in $\operatorname{Spec} A$, and $\mathfrak{q}_1 = O_v$ over $P$. Going down would require $\mathfrak{q}_2 \subseteq O_v$ with $\mathfrak{q}_2 \cap A = \mathfrak{p}_u$. The only primes $\subseteq O_v$ are $O_v$ (contracting to $P$) and $\eta_v$ (contracting to $\mathfrak{p}_v$); neither contracts to $\mathfrak{p}_u$. Hence no such $\mathfrak{q}_2$ exists, and going down fails. $\blacksquare$

> [!warning] Why $\mathfrak{q}_1$ must be on the opposite branch
> Had we chosen $\mathfrak{q}_1 = O_u$ (the origin of the *same* branch as $\mathfrak{p}_2 = \mathfrak{p}_u$), going down would *succeed*: $\eta_u \subseteq O_u$ contracts to $\mathfrak{p}_u = \mathfrak{p}_2$, so $\mathfrak{q}_2 = \eta_u$ works. The failure is visible *only* by choosing $\mathfrak{q}_1$ over $P$ on the branch *not* containing $\mathfrak{p}_2$. This is the whole point: at the glue point $P$, the fibre $\{O_u, O_v\}$ has two points on two different branches, and a chosen preimage $O_v$ on one branch cannot specialise downward into the other branch. Normality would forbid this two-branch structure over $P$ — a normal point has a single branch.

---

# Key Takeaways

**Non-normality is the failure of going down, and its geometric face is "multiple branches at a point".** The reusable principle: a non-normal ring is one whose normalization *pulls apart* a singular point into several branches, and going down fails precisely because a preimage on one branch cannot specialise into another. The trigger to recognise a potential going-down failure: the base has a singular point whose fibre (in an integral extension) has several points on geometrically separated branches. The glued lines are the simplest instance, but the same mechanism breaks going down at the node $y^2 = x^2(x+1)$, the cusp $y^2 = x^3$, and any non-normal variety — normalization exists precisely to repair it. When a problem hands you a non-normal base, do not assume any downward chain-lifting.

**To disprove a universal statement, engineer the *one* hypothesis it depends on to fail — and locate the failure precisely.** Going down holds for *every* integral extension *except* when $A$ is non-normal, so a counterexample must be non-normal, and the cleanest non-normal rings are built by gluing (a subring of a product, identifying values at a point). But constructing a non-normal ring is not enough: you must find *where* going down breaks, and here the subtlety is that it breaks only for $\mathfrak{q}_1$ on the *opposite* branch from $\mathfrak{p}_2$. The diagnostic for spaced practice: when disproving a chain-lifting property, identify the *fibre with multiple components* and choose the preimage point on the "wrong" component — the one whose specialisations cannot reach the target base prime. Picking the preimage on the same component would make the property hold and hide the counterexample.

**The "two lines glued at a point" is the universal local model of going-down failure — keep it in working memory.** This single example, $A = \{(f,g) : f(0)=g(0)\} \subseteq k[u]\times k[v] = B$, is worth memorising as a unit: $B$ is the normalization (two separated lines), $A$ the node (lines glued), $\iota^*$ glues the origins, and going down fails at the glue point across branches. It is the going-down analogue of "$\mathbb{Z} \hookrightarrow \mathbb{Q}$ shows lying over needs integrality" — a one-line picture that instantly recalls *why* the hypothesis is there. Whenever you doubt whether normality is genuinely needed for a downward statement, recall this node and check whether the statement survives it. The companion theorem [[Thm - Going Down for Integrally Closed Domains]] shows the positive side: normality forces the minimal polynomial of an element of $\sqrt{\mathfrak{p}_2 B}$ to have coefficients in $\mathfrak{p}_2$, the control that the glued ring $A$ lacks.
