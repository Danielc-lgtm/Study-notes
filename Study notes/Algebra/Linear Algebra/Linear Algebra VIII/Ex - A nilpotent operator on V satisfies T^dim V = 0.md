---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Nilpotent Operator"
  - "Thm - Null Spaces of Powers Stabilize"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $V$ be a finite-dimensional nonzero vector space over $\mathbf{F}$ and $T \in \mathcal{L}(V)$. Prove that if $T^k = 0$ for some positive integer $k$, then $T^{\dim V} = 0$.

**Recall:**

The objects involved are an operator on a finite-dimensional space, its iterates, and the kernel of those iterates.

![[Def - Nilpotent Operator#The Definition]]

The key tool is the *stabilisation* of the null-space chain:

![[Thm - Null Spaces of Powers Stabilize#Statement]]

Specifically, the null spaces $\operatorname{null} T^k$ form an increasing sequence, and once two consecutive terms coincide, all later terms coincide. The chain must stabilise by index $\dim V$ at the latest, because a strictly increasing chain of subspaces in $V$ adds at least one dimension at each step, and $V$ has only $\dim V$ dimensions.

---

# Convergent Strategy

**Problem class.** This is a *bound the power needed for nilpotence* problem — given that *some* power of $T$ vanishes, conclude that a *specific universal* power vanishes. The problem class is the one drilled by results that convert existential into universal: "given some $k$ with property $P(k)$, find an explicit, universal $k_0$ with $P(k_0)$". See the chapter's [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces#Problem-Solving Strategy|problem-solving strategy]] — the general meta-strategy here is to reach for [[Thm - Null Spaces of Powers Stabilize]] whenever powers of $T$ appear in a problem.

**Assumption pattern.** The hypothesis is the existential "$T^k = 0$ for some $k$" — equivalently, $\operatorname{null} T^k = V$ for some $k$. This single assumption has dramatic implications: it says the null-space chain $\operatorname{null} T^0 \subseteq \operatorname{null} T^1 \subseteq \cdots$ eventually saturates at all of $V$. The assumption gives us *some* index of saturation, and the stabilisation theorem promises this index is at most $\dim V$.

**Theorem routing.** The route runs through one theorem only: [[Thm - Null Spaces of Powers Stabilize]]. The chain $\operatorname{null} T^k$ stabilises by index $\dim V$, so once it reaches $V$ at some index $k$, it must have reached $V$ by index $\dim V$ — there is no room to grow further once the chain saturates at $V$ since $V$ is the largest possible subspace. The hypothesis "$T^k = 0$" feeds into the stabilisation theorem to give "$T^{\dim V} = 0$".

**Key decision point.** The non-obvious move is to *use the inclusion direction of the stabilisation theorem correctly*. The stabilisation says "the chain stops increasing by index $\dim V$"; we need to deduce "the chain reaches $V$ by index $\dim V$". These two are equivalent when the chain is already known to reach $V$: if $\operatorname{null} T^k = V$ for *any* $k$, then by stabilisation $\operatorname{null} T^{\dim V} = V$ (since the chain is non-decreasing, capped at $V$, and stabilises). The decision is to recognise that the stabilisation theorem is *both* a statement about increasing chains *and* a statement about chains reaching their cap — and to use the cap-reaching form.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces#Legal Operations|the topic page's Legal Operations]]:

1. **Use the null-space-stabilisation chain** (operation 3). This is the operation the entire exercise is an instance of — indeed, this exercise is essentially the *content* of stabilisation, applied to the specific case of "$T^k$ is the zero operator". The trigger is the appearance of powers of $T$ and a claim about a specific power; the move is to invoke stabilisation directly.

2. **Read polynomial constraints** (operation 5). The hypothesis $T^k = 0$ is exactly the statement that $z^k$ annihilates $T$ — a polynomial constraint. The minimal polynomial of $T$ then divides $z^k$, so the minimal polynomial is $z^m$ for some $m \leq k$, and by [[Thm - Null Spaces of Powers Stabilize]] applied to the minimal polynomial argument, $m \leq \dim V$. (This is an alternative route, used in the polynomial-constraint formulation. The direct route via stabilisation is shorter.)

---

# Hints

> [!note]- Hint 1
> Stabilisation. The null-space chain $\operatorname{null} T^0 \subseteq \operatorname{null} T^1 \subseteq \cdots$ stops growing by index $\dim V$ at the latest. If the chain reaches all of $V$ at *some* index $k$, what does stabilisation tell you about $\operatorname{null} T^{\dim V}$?

> [!note]- Hint 2
> The chain is non-decreasing and bounded above by $V$. If it reaches $V$ at index $k$, it stays at $V$ for every index $\geq k$ — there is nothing larger than $V$ to grow to. So if $k \leq \dim V$, then $\operatorname{null} T^{\dim V} = V$, that is, $T^{\dim V} = 0$. The only worry is if $k > \dim V$ — but stabilisation already rules this out, because the chain stops increasing by index $\dim V$.

> [!note]- Hint 3
> Case 1: $k \leq \dim V$. The chain $\operatorname{null} T^k \subseteq \operatorname{null} T^{\dim V}$ (non-decreasing), so $V = \operatorname{null} T^k \subseteq \operatorname{null} T^{\dim V} \subseteq V$, giving $\operatorname{null} T^{\dim V} = V$, i.e. $T^{\dim V} = 0$.
>
> Case 2: $k > \dim V$. By stabilisation, $\operatorname{null} T^{\dim V} = \operatorname{null} T^{\dim V + 1} = \cdots = \operatorname{null} T^k = V$. So $T^{\dim V} = 0$.
>
> In both cases the conclusion follows.

---

# Solution

The strategy is to use the stabilisation of the null-space chain to bridge from the existential hypothesis "$T^k = 0$ for some $k$" to the universal conclusion "$T^{\dim V} = 0$". The proof breaks into two steps: first establish that the chain reaches $V$ at the hypothesised index, then use stabilisation to push the saturation back to index $\dim V$.

**Step 1: The hypothesis $T^k = 0$ is equivalent to $\operatorname{null} T^k = V$.**

The hypothesis says some power of $T$ is the zero operator. Equivalently, every vector in $V$ is in the kernel of $T^k$, which is $\operatorname{null} T^k = V$.

> [!note]- Derivation
> $T^k = 0$ means $T^k v = 0$ for every $v \in V$, that is, $v \in \operatorname{null} T^k$ for every $v$. So $V \subseteq \operatorname{null} T^k$. The reverse inclusion is automatic ($\operatorname{null} T^k$ is by definition a subspace of $V$), so $\operatorname{null} T^k = V$.
>
> Conversely, $\operatorname{null} T^k = V$ means every $v$ is killed by $T^k$, that is, $T^k = 0$. So the two conditions are equivalent.

**Step 2: $\operatorname{null} T^{\dim V} = V$.**

By [[Thm - Null Spaces of Powers Stabilize]], the chain $\operatorname{null} T^j$ is non-decreasing in $j$ and stabilises by index $\dim V$. Combined with $\operatorname{null} T^k = V$, this forces $\operatorname{null} T^{\dim V} = V$ as well.

> [!note]- Derivation
> Let $n = \dim V$. We split into two cases based on whether $k \leq n$ or $k > n$.
>
> *Case 1: $k \leq n$.* The chain $\operatorname{null} T^j$ is non-decreasing in $j$ (Lemma 1 of [[Thm - Null Spaces of Powers Stabilize]]). So $\operatorname{null} T^k \subseteq \operatorname{null} T^n$. We are given $\operatorname{null} T^k = V$, so $V \subseteq \operatorname{null} T^n$. Combined with $\operatorname{null} T^n \subseteq V$ (trivially), $\operatorname{null} T^n = V$.
>
> *Case 2: $k > n$.* By [[Thm - Null Spaces of Powers Stabilize]] part (3), $\operatorname{null} T^n = \operatorname{null} T^{n+1} = \operatorname{null} T^{n+2} = \cdots$. In particular $\operatorname{null} T^n = \operatorname{null} T^k = V$.
>
> In either case, $\operatorname{null} T^n = V$.

**Step 3: Conclude $T^{\dim V} = 0$.**

The equivalence in Step 1 (with $k$ replaced by $\dim V$) gives the desired conclusion.

> [!note]- Derivation
> By Step 2, $\operatorname{null} T^n = V$ where $n = \dim V$. By Step 1 (applied in reverse with $k$ replaced by $n$), this means $T^n = 0$, that is, $T^{\dim V} = 0$.

> [!note]- Complete formal solution
> Let $V$ be a finite-dimensional vector space and $T \in \mathcal{L}(V)$ with $T^k = 0$ for some positive integer $k$. Let $n = \dim V$.
>
> We show $T^n = 0$.
>
> Since $T^k = 0$, every $v \in V$ satisfies $T^k v = 0$, so $v \in \operatorname{null} T^k$. Hence $\operatorname{null} T^k = V$.
>
> Now we consider two cases.
>
> *Case 1: $k \leq n$.* The chain $\operatorname{null} T^j$ is non-decreasing in $j$, so $\operatorname{null} T^k \subseteq \operatorname{null} T^n$. Combined with $\operatorname{null} T^k = V$, we have $V \subseteq \operatorname{null} T^n$, and since $\operatorname{null} T^n \subseteq V$ trivially, $\operatorname{null} T^n = V$.
>
> *Case 2: $k > n$.* By the null-space-stabilisation theorem ([[Thm - Null Spaces of Powers Stabilize]]), the chain stabilises by index $n$: $\operatorname{null} T^n = \operatorname{null} T^{n+1} = \cdots$. In particular $\operatorname{null} T^n = \operatorname{null} T^k = V$.
>
> In either case, $\operatorname{null} T^n = V$, which means $T^n v = 0$ for every $v \in V$, that is, $T^n = 0$, i.e. $T^{\dim V} = 0$. $\blacksquare$

> [!note]- Sanity check via the minimal polynomial
> An alternative route: the hypothesis $T^k = 0$ means $z^k$ annihilates $T$, so the minimal polynomial of $T$ divides $z^k$. The minimal polynomial has the form $z^m$ for some $1 \leq m \leq k$, and the standard fact that the minimal polynomial has degree at most $\dim V$ gives $m \leq \dim V$. Hence $T^{\dim V} = T^m \cdot T^{\dim V - m} = 0 \cdot T^{\dim V - m} = 0$. This route uses the polynomial-arithmetic of $\mathbb{F}[x]$ rather than the null-space-stabilisation theorem, but the underlying content is the same — the minimal polynomial having degree at most $\dim V$ is, ultimately, also a null-space-stabilisation fact.

---

# Key Takeaways

**Stabilisation converts existential into universal power statements.** The hypothesis "$T^k = 0$ for some $k$" is existential — we know *some* power kills $T$ but not which. The conclusion "$T^{\dim V} = 0$" is universal — a specific, explicit power kills $T$. The bridge between them is [[Thm - Null Spaces of Powers Stabilize]]. The pattern is reusable: whenever you have an existential hypothesis about powers and want a universal conclusion, look for a stabilisation-type theorem. Cases include "$T^k v = 0$ for some $k$" $\to$ "$T^{\dim V} v = 0$" (the definition of generalized eigenvector for $\lambda = 0$ in [[Def - Generalized Eigenvector]]), and the analogous statements for $\operatorname{range}$ instead of $\operatorname{null}$. The reusable diagnostic is: when an existential power appears, ask whether the universal power $\dim V$ works, and reach for stabilisation to bridge.

**The dimension of the space caps the depth of nilpotence.** No nilpotent operator on $V$ needs more than $\dim V$ applications to be zero — even if the operator looks deeply nested, the chain of null spaces cannot grow past $\dim V$ dimensions. The transferable lesson is that *in finite dimensions, no infinite-iteration phenomenon truly happens*: every "eventually zero" or "eventually stationary" statement comes with an explicit step count bounded by the dimension. This is the reason finite-dimensional linear algebra is so much cleaner than its infinite-dimensional counterpart: there, the differentiation operator $D$ on $\mathcal{P}(\mathbb{R})$ shows that "eventually zero" can require *every* finite step but no specific bounded one. The dimension bound is the precious lubricant of finite dimensions, and recognising when problems implicitly need it is a key skill.

**The minimal polynomial and stabilisation are dual viewpoints.** The same statement — "$T^{\dim V} = 0$ when $T$ is nilpotent" — admits two proofs: one via null-space stabilisation, one via the minimal polynomial dividing $z^k$ and having degree at most $\dim V$. Both routes are valid; they reflect that the same content (the structure of $T$-invariant subspaces) is encoded in two algebraic objects — the chain of null spaces $\operatorname{null} T^k$ and the minimal polynomial $m_T$. Whenever a problem hinges on the structure of $T^k$, ask whether the polynomial picture or the kernel-chain picture is more convenient. The polynomial picture is good for division-algebraic manipulations; the kernel-chain picture is good for dimensional arguments. Knowing both routes gives you a backup whenever one is harder than the other.
