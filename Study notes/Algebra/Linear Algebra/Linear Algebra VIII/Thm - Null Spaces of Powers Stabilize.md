---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Null Space and Range"
  - "Def - Dimension"
  - "Thm - Fundamental Theorem of Linear Maps"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional nonzero vector space over $\mathbf{F}$ and $T \in \mathcal{L}(V)$. $T^k$ is the $k$-fold composition of $T$ with itself, with $T^0 = I$. $\operatorname{null} S$ denotes the kernel of an operator and $\operatorname{range} S$ denotes its image. Full registry on [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces]].

---

# Statement

> **Theorem (null spaces of powers stabilize).** Suppose $T \in \mathcal{L}(V)$.
>
> 1. (Increasing chain.) The null spaces $\operatorname{null} T^0 \subseteq \operatorname{null} T^1 \subseteq \operatorname{null} T^2 \subseteq \cdots$ form a non-decreasing sequence of subspaces of $V$.
>
> 2. (Stabilisation propagates.) If $\operatorname{null} T^m = \operatorname{null} T^{m+1}$ for some non-negative integer $m$, then $\operatorname{null} T^m = \operatorname{null} T^{m+k}$ for every $k \geq 0$.
>
> 3. (Stabilisation by dimension.) $\operatorname{null} T^{\dim V} = \operatorname{null} T^{\dim V + 1} = \operatorname{null} T^{\dim V + 2} = \cdots$.

> **Corollary.** $V = \operatorname{null} T^{\dim V} \oplus \operatorname{range} T^{\dim V}$.

---

# Motivation

We have an operator $T$ on $V$ and we are interested in studying its iterates $T^k$ for various $k$. Two natural sequences attach to this iteration: the null spaces $\operatorname{null} T^k$ (vectors that $T^k$ destroys) and the ranges $\operatorname{range} T^k$ (vectors that some $T^k v$ can produce). As we apply $T$ more and more times, the null spaces *grow* — vectors that survive $T^k$ may not survive $T^{k+1}$ — and the ranges *shrink* — only what was produced by $T^{k-1}$ can become a $T^k$-image after another application of $T$.

The natural question: do these chains *go on forever*? If $T$ is nilpotent, then $\operatorname{null} T^k$ keeps growing until it fills $V$, after which it stays at $V$. If $T$ is invertible, then $\operatorname{null} T^k = \{0\}$ for every $k$. In general one expects the chain to grow for a while and then stop, but it is not a priori clear *when* it stops, or that it stops at all.

The theorem says: (i) once two consecutive null spaces agree, they all agree from there on; and (ii) the chain must stabilise by the index $\dim V$ at the latest. The first statement is the *qualitative* content — "once stuck, always stuck" — and the second is the *quantitative* bound — the dimension of the ambient space caps the length of growth.

The result is the workhorse for all of chapter 8. Every appearance of "generalized eigenspace" involves a power of $T - \lambda I$, and the chain-stabilisation result is what licenses the use of the *fixed* power $(T - \lambda I)^{\dim V}$ in the definition of $G(\lambda, T)$ as $\operatorname{null}(T - \lambda I)^{\dim V}$. Without stabilisation we would have to write $G(\lambda, T) = \bigcup_k \operatorname{null}(T - \lambda I)^k$, an infinite union, and proofs would be more awkward.

The corollary — that $V$ splits as $\operatorname{null} T^{\dim V} \oplus \operatorname{range} T^{\dim V}$ — is what makes the inductive proof of the [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]] work. We peel off a generalized eigenspace and a $T$-invariant complement, and apply induction on dimension.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's literal precondition is mild — *any* operator $T$ on any finite-dimensional space — so the source question is when *recognizing the relevance* of the theorem is non-obvious.

The first disguised source is **a problem about generalized eigenvectors**. The definition of a generalized eigenvector uses an *existential* power: $(T - \lambda I)^k v = 0$ for some $k$. Whenever the problem asks about generalized eigenvectors or generalized eigenspaces, the chain-stabilisation theorem is the bridge that converts the existential "some $k$" into the explicit "$k = \dim V$". *Example problem:* prove that if $(T - \lambda I)^k v = 0$ for some $k$, then $(T - \lambda I)^{\dim V} v = 0$ — direct invocation of stabilisation applied to $T - \lambda I$.

The second disguised source is **a problem about the partial dimensions of null spaces**. Whenever you know $\dim \operatorname{null} T^j$ for a few values of $j$ — typically as part of computing the Jordan structure — stabilisation tells you that once you see two consecutive equal dimensions, all later dimensions agree, and the chain has therefore reached its limit. *Example problem:* if $\dim \operatorname{null} T^4 = 8$ and $\dim \operatorname{null} T^6 = 9$, what is $\dim \operatorname{null} T^m$ for $m \geq 5$? The answer is $9$: since the chain is increasing and $\dim \operatorname{null} T^4 = 8 < 9 = \dim \operatorname{null} T^6$, there must be an increment at some $j \in \{5, 6\}$, but it cannot be both (since then $\dim$ would exceed $9$ at $T^6$) and... actually the chain must satisfy $\dim \operatorname{null} T^4 \leq \dim \operatorname{null} T^5 \leq \dim \operatorname{null} T^6 = 9$ with the leftmost equal to $8$. Then both intermediate values must equal one of $\{8, 9\}$. If $\dim \operatorname{null} T^5 = 8$, then $\operatorname{null} T^4 = \operatorname{null} T^5$, and by stabilisation $\dim \operatorname{null} T^m = 8$ for all $m \geq 4$ — contradicting $\dim \operatorname{null} T^6 = 9$. So $\dim \operatorname{null} T^5 = 9$, and by stabilisation $\dim \operatorname{null} T^m = 9$ for all $m \geq 5$. This is exercise 1 of §8A in LADR.

The third disguised source is **a problem requiring $V = \operatorname{null} T^k \oplus \operatorname{range} T^k$** for some $k$. The decomposition holds at $k = \dim V$ by the corollary, but it may also hold for smaller $k$ — in fact, it holds at the *smallest* $k$ where the chain stabilises. *Example problem:* prove $V = \operatorname{null} T \oplus \operatorname{range} T$ iff $\operatorname{null} T^2 = \operatorname{null} T$. The bridge here is the equivalence "(stabilisation at $k$) $\iff$ ($V = \operatorname{null} T^k \oplus \operatorname{range} T^k$)", which can be extracted from the proof of the corollary.

**Targets (Output Amplification)**

The bare conclusion is "null spaces stabilise". Combined with other facts it does much more.

Combine with **the [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem of linear maps]]** (rank-nullity). At each step, $\dim \operatorname{range} T^k = \dim V - \dim \operatorname{null} T^k$, so the ranges shrink in lockstep with the null spaces growing. Stabilisation of null spaces is thus equivalent to stabilisation of ranges, and the chain of ranges $\operatorname{range} T^0 \supseteq \operatorname{range} T^1 \supseteq \cdots$ also stabilises by $\dim V$. The further result is that $\operatorname{range} T^{\dim V}$ is the largest $T$-invariant subspace on which $T$ is *surjective*; this dovetails with $\operatorname{null} T^{\dim V}$ being the largest $T$-invariant subspace on which $T$ is *eventually zero*.

Combine with **invariance under $T$**. Both $\operatorname{null} T^k$ and $\operatorname{range} T^k$ are $T$-invariant subspaces — the first because $T$ commutes with $T^k$, the second because $\operatorname{range} T^{k+1} = T(\operatorname{range} T^k) \subseteq \operatorname{range} T^k$ (well, here we need a slight argument; let us just take it as evident). At the stabilised level $k = \dim V$, both subspaces are $T$-invariant, and their direct sum is $V$. This is exactly the Fitting decomposition: every operator splits $V$ into a part where it is eventually zero (a generalized 0-eigenspace) and a part where it is invertible. The further result is the foundation of the [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]] — apply the Fitting decomposition not to $T$ but to $T - \lambda I$ for each eigenvalue $\lambda$, and assemble.

Combine with **knowledge of the minimal polynomial $m_T$**. If $m_T(z) = z^k q(z)$ with $q(0) \neq 0$, then the smallest power of $T$ that is constant on $\operatorname{null} T^{\text{anything}}$ is $k$, so the stabilisation index of the null-space chain (for $T$, with $\lambda = 0$) is exactly the exponent of $z$ in $m_T$. The further result is that the stabilisation index at $\lambda$ — for the chain $\operatorname{null}(T - \lambda I)^j$ — equals the exponent of $(z - \lambda)$ in the minimal polynomial. This is exercise 18(c) of §8B in LADR.

---

# Why Is It True

The argument has two pieces. The first is **propagation**: once two consecutive null spaces agree, the chain stays put. The argument is purely formal. Suppose $\operatorname{null} T^m = \operatorname{null} T^{m+1}$. Then any $v$ with $T^{m+2} v = 0$ satisfies $T^{m+1}(T v) = 0$, so $T v \in \operatorname{null} T^{m+1} = \operatorname{null} T^m$, so $T^{m+1} v = T^m(T v) = 0$, so $v \in \operatorname{null} T^{m+1}$, so the next null space is contained in (hence equal to) the current one. Induction propagates this forward.

The second piece is the **dimensional bound**: the chain cannot strictly increase past $\dim V$ steps. The argument is dimensional: at each strict inclusion the dimension must increase by at least $1$, but $\dim \operatorname{null} T^k \leq \dim V$, so the chain can strictly increase at most $\dim V$ times. After $\dim V$ steps the chain must have stopped strictly increasing — that is, *two consecutive terms must agree by index $\dim V$* — and the propagation result then takes over.

**Mechanism summary: a strictly increasing chain of subspaces of $V$ adds at least one dimension per step, and $V$ has only $\dim V$ dimensions to give.**

This argument is *not* spectral, polynomial, or basis-dependent. It is the purest dimension-counting argument in chapter 8, and it is precisely the strength of finite-dimensionality: in infinite dimensions the chain can strictly increase forever, and the result fails. (For instance, on the space of polynomials $\mathcal{P}(\mathbb{R})$ — infinite-dimensional — the differentiation operator $D$ has $\operatorname{null} D^k = \mathcal{P}_{k-1}(\mathbb{R})$, a strictly increasing chain that never stabilises.)

The corollary $V = \operatorname{null} T^{\dim V} \oplus \operatorname{range} T^{\dim V}$ takes a little more work but is short. Suppose $v \in \operatorname{null} T^{\dim V} \cap \operatorname{range} T^{\dim V}$. Then $v = T^{\dim V} u$ for some $u$ and $T^{\dim V} v = 0$. So $T^{2 \dim V} u = 0$, hence $u \in \operatorname{null} T^{2 \dim V} = \operatorname{null} T^{\dim V}$ by stabilisation, hence $v = T^{\dim V} u = 0$. The intersection is zero. Then by rank-nullity, $\dim \operatorname{null} T^{\dim V} + \dim \operatorname{range} T^{\dim V} = \dim V$, so the sum is all of $V$ — direct.

---

# What Makes This Hard

The conceptual content is easy — a strictly increasing chain in a finite-dimensional space must stop — but the *propagation* step is the subtle part. Students often try to argue "the chain stops when it stabilises", which is circular: stabilisation is the conclusion, not a hypothesis. The actual argument is the manipulation $T^{m+1}(T v) = 0 \implies T v \in \operatorname{null} T^{m+1} = \operatorname{null} T^m$, where the equality is the *hypothesis* "two consecutive null spaces agree at index $m$", and the deduction $\operatorname{null} T^{m+1} \subseteq \operatorname{null} T^{m+2}$... wait, we want the reverse, that $\operatorname{null} T^{m+2} \subseteq \operatorname{null} T^{m+1}$. Let me re-examine: if $v \in \operatorname{null} T^{m+2}$, that is $T^{m+2} v = 0$, then $T^{m+1}(T v) = 0$, so $Tv \in \operatorname{null} T^{m+1}$, and by the *hypothesis* equal to $\operatorname{null} T^m$, so $T^m (T v) = 0$, that is $T^{m+1} v = 0$, that is $v \in \operatorname{null} T^{m+1}$. So $\operatorname{null} T^{m+2} \subseteq \operatorname{null} T^{m+1}$, combined with the always-true reverse inclusion, $\operatorname{null} T^{m+1} = \operatorname{null} T^{m+2}$. The propagation step is one of those argument structures where every line is short but they have to be assembled exactly right.

The corollary $V = \operatorname{null} T^{\dim V} \oplus \operatorname{range} T^{\dim V}$ has its own subtle point: the *intersection* argument requires stabilisation at $2 \dim V$ (which holds by stabilisation at $\dim V$), and pinning down which version of the theorem one needs is the technical bit.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Two parts. First, prove that if two consecutive null spaces agree at index $m$, then every later pair agrees — this is the propagation step, by showing $\operatorname{null} T^{m+k+1} \subseteq \operatorname{null} T^{m+k}$ by an algebraic manipulation. Second, observe that a strictly increasing chain in $V$ can have at most $\dim V$ strict inclusions, so two consecutive terms must agree by index $\dim V$ — this is the dimensional bound. Combine.

**Subgoal decomposition:**

1. **Increasing chain.** Show $\operatorname{null} T^k \subseteq \operatorname{null} T^{k+1}$ for every $k \geq 0$.
   - *Hint:* If $T^k v = 0$ then $T^{k+1} v = T (T^k v) = T(0) = 0$.
   - *Why needed:* This is the chain that we will then show stabilises.

2. **Propagation.** Show that if $\operatorname{null} T^m = \operatorname{null} T^{m+1}$, then $\operatorname{null} T^{m+1} = \operatorname{null} T^{m+2}$ (and inductively, $\operatorname{null} T^{m+k} = \operatorname{null} T^{m+k+1}$ for every $k$).
   - *Hint:* For $v \in \operatorname{null} T^{m+2}$, compute $T^{m+1}(T v) = 0$, conclude $T v \in \operatorname{null} T^{m+1} = \operatorname{null} T^m$, deduce $v \in \operatorname{null} T^{m+1}$.
   - *Why needed:* This is the "once stuck, always stuck" property.

3. **Dimensional bound.** Show that by index $\dim V$ at the latest, the chain must stabilise (i.e. two consecutive terms must agree).
   - *Hint:* A strictly increasing chain of subspaces of $V$ adds at least one dimension at each step, and the chain is capped by $\dim V$.
   - *Why needed:* This is the quantitative version of the theorem.

4. **Corollary — direct-sum decomposition at index $\dim V$.** Show $V = \operatorname{null} T^{\dim V} \oplus \operatorname{range} T^{\dim V}$.
   - *Hint:* The intersection is zero (by stabilisation applied at $2 \dim V$), and dimensions add to $\dim V$ by rank-nullity.
   - *Why needed:* This is the form used in the inductive proof of the generalized eigenspace decomposition.

---

# Lemma Decomposition

> [!note]- Lemma 1: The chain $\operatorname{null} T^k$ is non-decreasing
> **Statement:** $\operatorname{null} T^k \subseteq \operatorname{null} T^{k+1}$ for every $k \geq 0$.
>
> **Hint:** If $T^k v = 0$, apply $T$ to both sides.
>
> **Why needed:** We need the chain to be increasing in order for "stabilisation" to even be a question.
>
> > [!note]- Full proof
> > Suppose $v \in \operatorname{null} T^k$, that is, $T^k v = 0$. Then
> > $$T^{k+1} v = T(T^k v) = T(0) = 0,$$
> > so $v \in \operatorname{null} T^{k+1}$. Hence $\operatorname{null} T^k \subseteq \operatorname{null} T^{k+1}$.

> [!note]- Lemma 2: Propagation — equality at one step propagates forward
> **Statement:** If $\operatorname{null} T^m = \operatorname{null} T^{m+1}$ for some $m \geq 0$, then $\operatorname{null} T^{m+k} = \operatorname{null} T^{m+k+1}$ for every $k \geq 0$.
>
> **Hint:** Induction on $k$. For the induction step, use $T^{m+k+1}(T v) = 0$ and the previous equality.
>
> **Why needed:** This says the chain *stays* stable once it becomes stable. Without this, "stabilises at some point" would not mean "stabilises forever after".
>
> > [!note]- Full proof
> > We argue by induction on $k$. The base case $k = 0$ is the hypothesis.
> >
> > For the induction step, suppose $\operatorname{null} T^{m+k} = \operatorname{null} T^{m+k+1}$. We show $\operatorname{null} T^{m+k+1} = \operatorname{null} T^{m+k+2}$.
> >
> > The inclusion $\operatorname{null} T^{m+k+1} \subseteq \operatorname{null} T^{m+k+2}$ is Lemma 1.
> >
> > For the reverse inclusion, suppose $v \in \operatorname{null} T^{m+k+2}$. Then
> > $$T^{m+k+1}(T v) = T^{m+k+2} v = 0,$$
> > so $T v \in \operatorname{null} T^{m+k+1}$. By the induction hypothesis $\operatorname{null} T^{m+k+1} = \operatorname{null} T^{m+k}$, so $T v \in \operatorname{null} T^{m+k}$. That is,
> > $$T^{m+k}(T v) = 0, \qquad \text{i.e.}, \qquad T^{m+k+1} v = 0,$$
> > so $v \in \operatorname{null} T^{m+k+1}$. This shows $\operatorname{null} T^{m+k+2} \subseteq \operatorname{null} T^{m+k+1}$.
> >
> > Combining the two inclusions, $\operatorname{null} T^{m+k+1} = \operatorname{null} T^{m+k+2}$, completing the induction.

> [!note]- Lemma 3: Dimensional bound — stabilisation by $\dim V$
> **Statement:** $\operatorname{null} T^{\dim V} = \operatorname{null} T^{\dim V + 1}$.
>
> **Hint:** Suppose not. Then $\operatorname{null} T^0 \subsetneq \operatorname{null} T^1 \subsetneq \cdots \subsetneq \operatorname{null} T^{\dim V} \subsetneq \operatorname{null} T^{\dim V + 1}$ — a strictly increasing chain of $\dim V + 2$ subspaces. The dimensions are forced to be at least $0, 1, 2, \dots, \dim V + 1$, contradicting that all are subspaces of $V$.
>
> **Why needed:** The quantitative bound — without it we would not know *when* the chain stabilises, only that it must.
>
> > [!note]- Full proof
> > Suppose for contradiction that $\operatorname{null} T^{\dim V} \neq \operatorname{null} T^{\dim V + 1}$. By Lemma 2 (propagating *backward*: the contrapositive says if equality fails at index $\dim V$, then equality fails at every earlier index too), all the inclusions $\operatorname{null} T^k \subseteq \operatorname{null} T^{k+1}$ for $k = 0, 1, \dots, \dim V$ are *strict*.
> >
> > Wait — we need to be careful. The propagation lemma says "if equality at $m$, then equality at $m + 1, m + 2, \dots$". The *contrapositive* is "if inequality at $m + 1$, then inequality at $m$" — and inductively, if inequality holds at $\dim V + 1$ (i.e. at index $m = \dim V$ in the sense "$\operatorname{null} T^{\dim V} \neq \operatorname{null} T^{\dim V + 1}$"), then inequality holds at every earlier $m$. So all of $\operatorname{null} T^0 \subsetneq \operatorname{null} T^1 \subsetneq \cdots \subsetneq \operatorname{null} T^{\dim V + 1}$ are strict inclusions.
> >
> > Since each strict inclusion increases dimension by at least $1$, and the chain starts at $\dim \operatorname{null} T^0 = \dim\{0\} = 0$, we get $\dim \operatorname{null} T^{\dim V + 1} \geq \dim V + 1$. But $\operatorname{null} T^{\dim V + 1} \subseteq V$, so $\dim \operatorname{null} T^{\dim V + 1} \leq \dim V$. Contradiction.
> >
> > Hence $\operatorname{null} T^{\dim V} = \operatorname{null} T^{\dim V + 1}$, and by Lemma 2 all later null spaces coincide with these.

> [!note]- Lemma 4: Direct-sum decomposition at index $\dim V$
> **Statement:** $V = \operatorname{null} T^{\dim V} \oplus \operatorname{range} T^{\dim V}$.
>
> **Hint:** Show the intersection is zero by using stabilisation at $2 \dim V$. Then use rank-nullity to get the dimensions add up.
>
> **Why needed:** This is the form used in the inductive proof of the [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]] — it is what lets us peel off a generalized eigenspace at $\lambda$ and a $T$-invariant complement.
>
> > [!note]- Full proof
> > Let $n = \dim V$. We first show $\operatorname{null} T^n \cap \operatorname{range} T^n = \{0\}$.
> >
> > Suppose $v \in \operatorname{null} T^n \cap \operatorname{range} T^n$. Then $T^n v = 0$ and $v = T^n u$ for some $u \in V$. Substituting,
> > $$0 = T^n v = T^n (T^n u) = T^{2n} u.$$
> > So $u \in \operatorname{null} T^{2n}$. By stabilisation (Lemma 3 applied at $2n \geq n$), $\operatorname{null} T^{2n} = \operatorname{null} T^n$, so $u \in \operatorname{null} T^n$, that is, $T^n u = 0$. Thus $v = T^n u = 0$. So the intersection is zero.
> >
> > By [[Thm - Fundamental Theorem of Linear Maps|rank-nullity]] applied to the operator $T^n$,
> > $$\dim \operatorname{null} T^n + \dim \operatorname{range} T^n = \dim V.$$
> > Combined with the intersection being trivial, the sum $\operatorname{null} T^n + \operatorname{range} T^n$ has dimension equal to $\dim V$, hence equals $V$, hence the sum is direct: $V = \operatorname{null} T^n \oplus \operatorname{range} T^n$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $n = \dim V$.
>
> **Part 1 — Increasing chain.** By Lemma 1, $\operatorname{null} T^k \subseteq \operatorname{null} T^{k+1}$ for every $k \geq 0$.
>
> **Part 2 — Propagation.** By Lemma 2, if $\operatorname{null} T^m = \operatorname{null} T^{m+1}$ for some $m$, then $\operatorname{null} T^{m+k} = \operatorname{null} T^{m+k+1}$ for every $k \geq 0$. In particular all later null spaces equal $\operatorname{null} T^m$.
>
> **Part 3 — Stabilisation by $n$.** By Lemma 3, $\operatorname{null} T^n = \operatorname{null} T^{n+1}$. By Part 2 applied at $m = n$, $\operatorname{null} T^n = \operatorname{null} T^{n+1} = \operatorname{null} T^{n+2} = \cdots$.
>
> **Corollary — direct-sum decomposition.** By Lemma 4, $V = \operatorname{null} T^n \oplus \operatorname{range} T^n$.
>
> $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Markov chains and absorbing states.** Let $P$ be the transition matrix of a finite Markov chain. The kernel of $P - I$ is the space of *stationary distributions*; the kernel of $(P - I)^k$ for higher $k$ includes vectors that are *eventually stationary*, that is, distributions that converge to a stationary distribution under iteration. The null-space stabilisation says: there is a finite step $k$ (at most $\dim V$) after which "eventually-stationary" no longer grows — exactly the absorbing classes of the Markov chain are detected by this stabilisation. The number of independent stationary distributions equals the geometric multiplicity of $1$ as an eigenvalue, and the algebraic multiplicity counts a more refined "size" of the absorbing structure.

**Bounded linear operators on Banach spaces.** In infinite dimensions the theorem *fails*: the differentiation operator $D$ on $\mathcal{P}(\mathbb{R})$ has $\operatorname{null} D^k = \mathcal{P}_{k-1}(\mathbb{R})$, strictly increasing forever. But for **compact** operators on a Banach space the analogous statement *does* hold by the Riesz–Schauder theory: the chain $\operatorname{null}(T - \lambda I)^k$ for $\lambda \neq 0$ stabilises in finitely many steps. The proof is more intricate but uses compactness in place of finite-dimensionality. This is the source of the *spectral theory of compact operators*, which extends Jordan-form-style results to infinite dimensions for sufficiently nice operators.

**Algebraic geometry — flag varieties.** The chain of nested subspaces $\operatorname{null} T^0 \subsetneq \operatorname{null} T^1 \subsetneq \cdots \subsetneq \operatorname{null} T^k = V$ for a nilpotent $T$ of index $k$ is a **complete flag** in $V$ (if the inclusions are all strict). The space of all complete flags in $V$ is the **flag variety** $\mathrm{Fl}(V)$, a smooth projective variety of central importance in algebraic geometry and representation theory. Nilpotent operators correspond to points in the flag variety with extra structure (and the moduli space of nilpotent operators modulo conjugation is the **nilpotent cone**), connecting linear algebra to geometric representation theory.

---

# Bridges

- **[[Thm - Generalized Eigenspace Decomposition|Generalized Eigenspace Decomposition]]** — direct consequence applied to $T - \lambda I$ for each eigenvalue $\lambda$. The chain $\operatorname{null}(T - \lambda I)^k$ stabilises at $\operatorname{null}(T - \lambda I)^{\dim V} = G(\lambda, T)$, the generalized eigenspace; the corollary gives the Fitting decomposition $V = G(\lambda, T) \oplus \operatorname{range}(T - \lambda I)^{\dim V}$ used in the inductive proof.

- **[[Def - Generalized Eigenspace|Generalized Eigenspace]]** — provides the equivalence between the "existential" definition (some $k$ with $(T - \lambda I)^k v = 0$) and the "universal" definition ($k = \dim V$). The two definitions agree because of this theorem.

- **[[Def - Nilpotent Operator|Nilpotent Operators]]** — provides the equivalence "$N^k = 0$ for some $k$" $\iff$ "$N^{\dim V} = 0$". A nilpotent operator is one for which $\operatorname{null} N^k = V$ for some $k$; by stabilisation, $\operatorname{null} N^{\dim V} = V$, that is, $N^{\dim V} = 0$.

- **Range version** — the analogous statement for ranges: $\operatorname{range} T^k$ is a *decreasing* chain that also stabilises by index $\dim V$. The proofs are identical with arrows reversed, and the two stabilisation results are equivalent via the Fundamental Theorem of Linear Maps ([[Thm - Fundamental Theorem of Linear Maps]]): $\dim \operatorname{range} T^k = \dim V - \dim \operatorname{null} T^k$, so growth of nulls equals shrinkage of ranges.

- **Fitting decomposition** — the corollary $V = \operatorname{null} T^{\dim V} \oplus \operatorname{range} T^{\dim V}$ is the **Fitting decomposition** for $T$ at the eigenvalue $0$. It splits $V$ into a "nilpotent part" (where $T$ is eventually zero) and an "invertible part" (where $T$ is invertible). Applied to $T - \lambda I$ for various $\lambda$, this is the engine of the [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]].

---

# Unlocked by This

> [!tip] Generalized Eigenspace as $\operatorname{null}(T - \lambda I)^{\dim V}$
> The stabilisation result is what justifies the "uniform power" definition of the generalized eigenspace: $G(\lambda, T) = \operatorname{null}(T - \lambda I)^{\dim V}$, regardless of how quickly the chain actually stabilises (which depends on $T$).

> [!tip] Jordan Block Sizes from Null-Space Dimensions
> The increments $\dim \operatorname{null}(T - \lambda I)^k - \dim \operatorname{null}(T - \lambda I)^{k-1}$ give the number of Jordan blocks of size $\geq k$ at $\lambda$. Stabilisation says these increments become zero by $k = \dim V$, so the partition has finitely many parts; the largest part is the smallest $k$ at which stabilisation occurs.

> [!tip] Spectral Theory of Compact Operators
> The infinite-dimensional analogue of this theorem holds for **compact operators** on a Banach space (the Riesz–Schauder theorem): the chain $\operatorname{null}(T - \lambda I)^k$ stabilises in finitely many steps for nonzero $\lambda$, giving a generalized eigenspace structure analogous to the Jordan form. The proof uses compactness in place of finite-dimensionality.
