---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Direct and Inverse Limits"
  - "Def - The I-adic Completion"
  - "Def - Integral Domain"
  - "Def - Local Ring and Residue Field"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Fix a prime $p$ and define the ring of **$p$-adic integers** as the inverse limit
$$\mathbb{Z}_p=\varprojlim_n\mathbb{Z}/p^n\mathbb{Z}$$
along the natural projections $h_{mn}:\mathbb{Z}/p^n\mathbb{Z}\twoheadrightarrow\mathbb{Z}/p^m\mathbb{Z}$ ($m\leq n$). Prove the following.

1. **(Digit expansion.)** Every element of $\mathbb{Z}_p$ is represented uniquely by a sequence of digits $(d_0,d_1,d_2,\dots)$ with $0\leq d_i<p$, via $x=\big(\sum_{k=0}^{n-1}d_k p^k+p^n\mathbb{Z}\big)_{n\geq1}$ — a "base-$p$ number with digits running to the left". Compute the digit expansions of $0$, $1$, and $-1$ in $\mathbb{Z}_5$.
2. **(Domain.)** $\mathbb{Z}_p$ is an integral domain, and the completion map $\mathbb{Z}\to\mathbb{Z}_p$ is injective.
3. **(Local ring and units.)** $\mathbb{Z}_p$ is a [[Def - Local Ring and Residue Field|local ring]] with maximal ideal $p\mathbb{Z}_p$ and residue field $\mathbb{Z}_p/p\mathbb{Z}_p\cong\mathbb{F}_p$; an element is a unit iff its first digit $d_0\neq0$.

**Recall:**

The objects in play are the inverse limit, the $\mathfrak{a}$-adic completion at $\mathfrak{a}=(p)$, integral domains, and local rings.

![[Def - Direct and Inverse Limits#The Definition]]

A [[Def - Direct and Inverse Limits|inverse limit]] $\varprojlim Y_i$ is the set of compatible threads $(y_i)$ with $y_i=h_{ij}(y_j)$, made a ring by coordinatewise operations. Here $Y_n=\mathbb{Z}/p^n\mathbb{Z}$ and $h_{mn}$ reduces mod $p^m$, so a thread is a sequence $(x_n)$ with $x_n\in\mathbb{Z}/p^n\mathbb{Z}$ and $x_{n+1}\equiv x_n\pmod{p^n}$.

![[Def - The I-adic Completion#The Definition]]

This $\mathbb{Z}_p$ is precisely the [[Def - The I-adic Completion|(p)-adic completion]] $\widehat{\mathbb{Z}}^{(p)}$ of $\mathbb{Z}$, with completion map $\varphi:\mathbb{Z}\to\mathbb{Z}_p$, $m\mapsto(m+p^n\mathbb{Z})_n$.

![[Def - Local Ring and Residue Field#The Definition]]

A [[Def - Local Ring and Residue Field|local ring]] has a unique maximal ideal $\mathfrak{m}$, and then $R\setminus\mathfrak{m}=R^\times$ (every non-unit lies in $\mathfrak{m}$); the residue field is $R/\mathfrak{m}$.

---

# Convergent Strategy

**Problem class.** This is an *identify-the-limit-and-read-off-its-structure* problem, the foundational worked example of the chapter's first target type. As the [[Commutative Algebra X — Completions and Limits#Problem-Solving Strategy|topic strategy]] records, the move for an inverse limit is to represent elements as compatible threads and check claims level by level; everything here is an instance of that single technique applied to the most important inverse system there is.

**Assumption pattern.** The recognisable trigger is *projections down a tower of finite quotients of $\mathbb{Z}$*: $\mathbb{Z}/p^{n+1}\twoheadrightarrow\mathbb{Z}/p^n$. This says "completion at $(p)$", so the snapshots are residues mod $p^n$ and a thread is a coherent system of residues — which, by the division algorithm, is exactly a left-infinite base-$p$ expansion. The finiteness of each $\mathbb{Z}/p^n$ is what makes the digit extraction terminate at each level.

**Theorem routing.** The route is: (1) for each thread, peel off digits by the division algorithm at each level, using compatibility to show the lower digits never change — this gives the unique expansion; (2) injectivity of $\mathbb{Z}\to\mathbb{Z}_p$ is the kernel formula $\ker\varphi=\bigcap_n p^n\mathbb{Z}=0$ in the domain $\mathbb{Z}$ ([[Thm - The Inverse Limit and Completeness]]); (3) the domain property and locality follow from the unit criterion, proved by inverting any $d_0\neq0$ digit-by-digit (a geometric-series construction). The unit criterion is the [[Def - The I-adic Completion|"units detected mod \mathfrak{a}"]] corollary specialised to $p$.

**Key decision point.** The non-obvious move is realising that *compatibility forces the low-order digits to be permanent*: when you write $x_{n+1}=x_n+d_n p^n$, the digit $d_n$ is *new* and $x_n$ is *unchanged*, so the expansion grows only at the high end. This is why a thread is a single well-defined infinite digit string rather than a sequence of unrelated base-$p$ numbers. The alternative — treating each $x_n$ independently — misses that the thread condition is exactly "agree on all previous digits", and is the source of every confusion about $p$-adics.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra X — Completions and Limits#Legal Operations|the topic page's Legal Operations]]:

1. **Represent an element as a compatible thread (operation 2).** Treat $x\in\mathbb{Z}_p$ as the sequence $(x_n)$ with $x_{n+1}\equiv x_n\pmod{p^n}$, and work level by level.

2. **Reduce modulo $p^n$ to a finite problem (operation 3).** At each level the ring $\mathbb{Z}/p^n$ is finite, so digit extraction by the division algorithm terminates; the global statement is the limit of these finite ones.

3. **Compute the kernel of completion as $\bigcap_n p^n\mathbb{Z}$ (operation 5).** Injectivity of $\mathbb{Z}\to\mathbb{Z}_p$ is exactly $\bigcap_n p^n\mathbb{Z}=0$, true because a non-zero integer has finite $p$-adic valuation.

4. **Recognise units by their residue (operation 9).** $x$ is a unit iff $x\bmod p\neq0$ iff $d_0\neq0$; the inverse is built by a geometric-series correction digit by digit.

---

# Hints

> [!note]- Hint 1
> An element of $\mathbb{Z}_p$ is a sequence $(x_n)$, $x_n\in\mathbb{Z}/p^n$, with $x_{n+1}$ reducing to $x_n$ mod $p^n$. Try to extract a "next digit" at each step: given $x_n$, lift it to $0\leq\tilde{x}_n<p^n$ and ask how $x_{n+1}$ extends it.

> [!note]- Hint 2
> Write $\tilde{x}_{n+1}=\tilde{x}_n+d_n p^n$ with $0\leq d_n<p$ (this is forced by $\tilde{x}_{n+1}\equiv\tilde{x}_n\bmod p^n$ and $0\leq\tilde{x}_{n+1}<p^{n+1}$). The digits $d_0,d_1,\dots$ are uniquely determined and never change once set — that is the whole content of part 1.

> [!note]- Hint 3
> For $-1$ in $\mathbb{Z}_5$: you need $x_n\equiv-1\pmod{5^n}$, i.e. $x_n=5^n-1$. In base $5$, $5^n-1=\underbrace{44\cdots4}_{n}{}_5$. So the digit string is all $4$s.

> [!note]- Hint 4
> For locality: show $x$ is a unit iff $d_0\neq0$. If $d_0\neq0$, then $x$ is a unit mod $p$, and you can invert it mod $p^n$ for every $n$ by Hensel-style correction, getting a thread that is the inverse. If $d_0=0$ then $x\in p\mathbb{Z}_p$ and $x$ is not a unit. So the non-units are exactly $p\mathbb{Z}_p$ — a single maximal ideal.

---

# Solution

The proof has three movements. First we turn a compatible thread into a unique infinite digit string by the division algorithm, the key point being that compatibility freezes the low digits. Then injectivity of $\mathbb{Z}\to\mathbb{Z}_p$ is the kernel formula $\bigcap_n p^n\mathbb{Z}=0$. Finally locality comes from the unit criterion "$d_0\neq0$", proved by inverting digit-by-digit, which also gives the domain property.

**Step 1: Each thread is a unique left-infinite base-$p$ expansion.**

Every $x=(x_n)\in\mathbb{Z}_p$ corresponds bijectively to a digit sequence $(d_0,d_1,\dots)$, $0\leq d_i<p$, with $x_n=\sum_{k=0}^{n-1}d_k p^k\bmod p^n$.

> [!note]- Derivation
> Let $x=(x_n)_{n\geq1}\in\mathbb{Z}_p$, so $x_n\in\mathbb{Z}/p^n\mathbb{Z}$ and $x_{n+1}\equiv x_n\pmod{p^n}$. Represent each $x_n$ by its unique integer lift $\tilde{x}_n$ with $0\leq\tilde{x}_n<p^n$. The compatibility $x_{n+1}\equiv x_n\pmod{p^n}$ means $\tilde{x}_{n+1}\equiv\tilde{x}_n\pmod{p^n}$, and since $0\leq\tilde{x}_{n+1}<p^{n+1}$ we may write
> $$\tilde{x}_{n+1}=\tilde{x}_n+d_n p^n,\qquad 0\leq d_n<p,$$
> with $d_n$ uniquely determined (it is the $\lfloor\cdot/p^n\rfloor$ of $\tilde{x}_{n+1}$ after subtracting $\tilde{x}_n$). Setting $\tilde{x}_1=d_0$ ($0\leq d_0<p$), induction gives $\tilde{x}_n=\sum_{k=0}^{n-1}d_k p^k$. The digits $d_0,d_1,\dots$ are determined by $x$ and, crucially, *the digit $d_k$ is fixed once and for all at stage $k+1$ and never altered* — adding $d_n p^n$ changes only the new high-order place. Conversely any digit string $(d_k)$ yields a thread by $x_n=\sum_{k<n}d_k p^k\bmod p^n$, and these reduce compatibly. So $\mathbb{Z}_p\leftrightarrow\{(d_k):0\leq d_k<p\}$ bijectively, and the elements are "base-$p$ numbers with digits running infinitely to the left".

**Step 2: The digit expansions of $0$, $1$, $-1$ in $\mathbb{Z}_5$.**

$0=(\dots000)_5$, $1=(\dots001)_5$, and $-1=(\dots444)_5$.

> [!note]- Derivation
> $0$ is the thread $(0,0,0,\dots)$, all digits $0$. The integer $1$ gives the thread $(1+5^n\mathbb{Z})_n$, with $\tilde{x}_n=1$ for all $n$, so $d_0=1$ and all higher digits $0$: $1=(\dots0001)_5$.
>
> For $-1$: we need $x_n\equiv-1\pmod{5^n}$, i.e. $\tilde{x}_n=5^n-1$. Then
> $$\tilde{x}_1=4,\ \tilde{x}_2=24,\ \tilde{x}_3=124,\ \tilde{x}_4=624,\dots,\qquad 5^n-1=\underbrace{44\cdots4}_{n}{}_{(5)}.$$
> So $d_k=4$ for all $k$, and $-1=(\dots4444)_5$. As a check, $(\dots4444)_5+1$ carries infinitely: $4+1=10_5$ carries a $1$, turning every digit to $0$, giving $(\dots000)_5=0$. So indeed $(\dots4444)_5=-1$.

**Step 3: $\mathbb{Z}\to\mathbb{Z}_p$ is injective and $\mathbb{Z}_p$ is a domain.**

The completion map has kernel $\bigcap_n p^n\mathbb{Z}=0$, so it is injective; and the unit criterion of Step 4 shows $\mathbb{Z}_p$ has no zero-divisors.

> [!note]- Derivation
> By the kernel formula ([[Thm - The Inverse Limit and Completeness]]), $\ker(\varphi:\mathbb{Z}\to\mathbb{Z}_p)=\bigcap_{n\geq0}p^n\mathbb{Z}$. A non-zero integer $m$ has a finite $p$-adic valuation $v_p(m)<\infty$, so $m\notin p^{v_p(m)+1}\mathbb{Z}$; hence the only integer in *every* $p^n\mathbb{Z}$ is $0$, i.e. $\bigcap_n p^n\mathbb{Z}=0$ and $\varphi$ is injective. (This is the Noetherian-domain case of [[Thm - The Krull Intersection Theorem|Krull intersection]] done by hand.)
>
> For the domain property: suppose $xy=0$ with $x,y\neq0$ in $\mathbb{Z}_p$. Let $v_p(x)$ be the index of the first non-zero digit of $x$ (so $x=p^{v_p(x)}u$ with $u$ a unit by Step 4), similarly $v_p(y)$. Then $xy=p^{v_p(x)+v_p(y)}uw$ with $uw$ a unit, so $xy$ has first non-zero digit at place $v_p(x)+v_p(y)<\infty$, hence $xy\neq0$ — contradiction. So $\mathbb{Z}_p$ is a domain.

**Step 4: $\mathbb{Z}_p$ is local with maximal ideal $p\mathbb{Z}_p$ and residue field $\mathbb{F}_p$.**

$x\in\mathbb{Z}_p$ is a unit iff $d_0\neq0$; the non-units are exactly $p\mathbb{Z}_p$, the unique maximal ideal, with quotient $\mathbb{F}_p$.

> [!note]- Derivation
> First, $x=(x_n)$ lies in $p\mathbb{Z}_p$ iff $x_1=d_0=0$ in $\mathbb{Z}/p$: indeed $p\mathbb{Z}_p$ is the kernel of the level-$1$ projection $\pi_1:\mathbb{Z}_p\to\mathbb{Z}/p\mathbb{Z}$, $x\mapsto d_0$, and $\pi_1$ is surjective with $\ker\pi_1=p\mathbb{Z}_p$, so $\mathbb{Z}_p/p\mathbb{Z}_p\cong\mathbb{F}_p$.
>
> Now suppose $d_0\neq0$, i.e. $x_1\in(\mathbb{Z}/p)^\times$. We build $y=(y_n)\in\mathbb{Z}_p$ with $xy=1$ by inverting level by level. At level $1$, $y_1=x_1^{-1}$ exists since $\mathbb{Z}/p$ is a field. Inductively, given $y_n$ with $x_n y_n\equiv1\pmod{p^n}$, write $x_n y_n=1+p^n c$; since $x$ is a unit mod $p$ it is a unit mod $p^{n+1}$, and setting $y_{n+1}=y_n(1-p^n c)\bmod p^{n+1}$ gives $x_{n+1}y_{n+1}\equiv1\pmod{p^{n+1}}$ (the correction kills the order-$p^n$ error — this is the geometric-series/Newton step). The $y_n$ are compatible, so $y\in\mathbb{Z}_p$ and $xy=1$. Hence every $x$ with $d_0\neq0$ is a unit.
>
> Conversely if $d_0=0$ then $x\in p\mathbb{Z}_p$, and a unit cannot lie in the proper ideal $p\mathbb{Z}_p$ (its image mod $p$ would be both $0$ and a unit). So units $=\{d_0\neq0\}=\mathbb{Z}_p\setminus p\mathbb{Z}_p$, the non-units form the single ideal $p\mathbb{Z}_p$, and $\mathbb{Z}_p$ is local with maximal ideal $p\mathbb{Z}_p$ and residue field $\mathbb{F}_p$.

> [!note]- Complete formal solution
> **Setup.** $\mathbb{Z}_p=\varprojlim\mathbb{Z}/p^n\mathbb{Z}$; an element is a thread $(x_n)$, $x_n\in\mathbb{Z}/p^n$, with $x_{n+1}\equiv x_n\pmod{p^n}$.
>
> **(1) Digit expansion.** Lift $x_n$ to $0\leq\tilde{x}_n<p^n$. Compatibility gives $\tilde{x}_{n+1}=\tilde{x}_n+d_n p^n$ with unique $0\leq d_n<p$, and $\tilde{x}_n=\sum_{k<n}d_k p^k$. The map $x\mapsto(d_k)$ is a bijection $\mathbb{Z}_p\to\prod_{k}\{0,\dots,p-1\}$, since any digit string defines a compatible thread. Thus every $p$-adic integer is a unique left-infinite base-$p$ expansion.
>
> **Digits in $\mathbb{Z}_5$:** $0=(\dots000)_5$; $1=(\dots001)_5$; and since $-1$ requires $\tilde{x}_n=5^n-1=\underbrace{4\cdots4}_n{}_5$, we get $-1=(\dots4444)_5$ (verified by $(\dots4444)_5+1=0$ via infinite carry).
>
> **(2) Injective and domain.** $\ker(\mathbb{Z}\to\mathbb{Z}_p)=\bigcap_n p^n\mathbb{Z}=0$ because a non-zero integer has finite $v_p$; so $\mathbb{Z}\hookrightarrow\mathbb{Z}_p$. Writing each non-zero element as $p^v\cdot(\text{unit})$ (part 3), products of non-zero elements are non-zero, so $\mathbb{Z}_p$ is a domain.
>
> **(3) Local ring.** The level-$1$ projection $\pi_1:\mathbb{Z}_p\to\mathbb{F}_p$, $x\mapsto d_0$, is a surjective ring map with kernel $p\mathbb{Z}_p$, so $\mathbb{Z}_p/p\mathbb{Z}_p\cong\mathbb{F}_p$. If $d_0\neq0$, invert $x$ level by level (Newton correction $y_{n+1}=y_n(1-p^n c)$ where $x_n y_n=1+p^n c$), producing $y\in\mathbb{Z}_p$ with $xy=1$. If $d_0=0$, $x\in p\mathbb{Z}_p$ is a non-unit. Hence $\mathbb{Z}_p^\times=\{d_0\neq0\}=\mathbb{Z}_p\setminus p\mathbb{Z}_p$, so $\mathbb{Z}_p$ is local with maximal ideal $p\mathbb{Z}_p$ and residue field $\mathbb{F}_p$. $\blacksquare$

> [!warning] Illegal but tempting: reading $-1$ as a finite base-$p$ number
> It is tempting to say "$-1$ has no base-$p$ expansion" because negative numbers do not in ordinary base-$p$. The point of $\mathbb{Z}_p$ is that the digits run *to the left infinitely*, and the infinite carry $(\dots4444)_5+1=(\dots0000)_5$ is legal precisely because there is no leftmost digit to overflow. Treating the expansion as terminating (e.g. stopping at $4_5=4\neq-1$) is the error; only the full infinite thread equals $-1$, and it equals $-1$ because *every* truncation $5^n-1\equiv-1\pmod{5^n}$.

---

# Key Takeaways

**A compatible thread freezes its low-order data, which is why an inverse limit of truncations is a single infinite expansion.** The structural heart of the $p$-adics — and of every completion — is that the thread condition $x_{n+1}\equiv x_n\pmod{p^n}$ says the new stage *refines* the old without disturbing it. So an element is not a sequence of independent approximations but a single object being progressively revealed, digit by digit, each digit permanent once written. The trigger to recognise: whenever you meet $\varprojlim$ of a tower whose transition maps are surjective truncations, expect the elements to be "infinite expansions" with a well-defined notion of "the first $n$ digits". This is the same phenomenon as a power series being determined by its truncations in $k[[T]]$, and as a real number being determined by its decimal truncations; the digit-permanence is what makes all three constructions a genuine completion rather than a shapeless sequence space.

**Injectivity of completion is finite valuation: $\bigcap_n p^n\mathbb{Z}=0$ because non-zero integers are not infinitely divisible.** The clean way to see $\mathbb{Z}\hookrightarrow\mathbb{Z}_p$ is to notice that the kernel is exactly the integers divisible by every power of $p$, and the only such integer is $0$. This is the [[Thm - The Krull Intersection Theorem|Krull intersection theorem]] in its most transparent case, done by an elementary valuation argument, and it is the template for the general statement: completion loses information *only* along infinitely-divisible elements, and in a Noetherian domain there are none. The transferable diagnostic: to decide whether $R\hookrightarrow\widehat{R}$, ask "is anything non-zero infinitely divisible by $\mathfrak{a}$?" — if the ring is a Noetherian domain or local, the answer is no, and the embedding is honest.

**Locality of a complete ring comes from the unit criterion "non-zero residue mod $\mathfrak{m}$", proved by digit-by-digit inversion.** The reason $\mathbb{Z}_p$ is local — and the reason every complete local ring is local — is that you can invert anything not in the maximal ideal by successive approximation: if $x$ is a unit modulo $p$, correct its approximate inverse one power of $p$ at a time, and completeness assembles the corrections into a true inverse. This is the geometric-series/Newton mechanism, and it is the same computation that proves $f\in k[[T]]$ is a unit iff $f(0)\neq0$, and that drives Hensel's lemma. The trigger: in any complete local setting, "is this a unit?" reduces to "is its residue a unit?", and the inverse, however inexpressible in closed form, is built as a convergent thread of corrections. Recognising this collapses unit questions in $\mathbb{Z}_p$, $k[[T]]$, and complete local rings to a one-line residue check — see the companion exercises [[Ex - The formal power series ring as a completion]] and [[Ex - Hensel-style lifting in the p-adics]].
