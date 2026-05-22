---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Eigenvalue and Eigenvector"
  - "Def - Invariant Subspace"
  - "Thm - Existence of Eigenvalues on Complex Vector Spaces"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $V$ be a finite-dimensional nonzero complex vector space, and let $S, T \in \mathcal{L}(V)$ be **commuting** operators: $ST = TS$. Prove that $S$ and $T$ share a common eigenvector — i.e., there exists $v \in V$ with $v \neq 0$ such that $Sv = \mu v$ and $Tv = \lambda v$ for some scalars $\mu, \lambda \in \mathbb{C}$.

**Recall:**

![[Def - Eigenvalue and Eigenvector#The Definition]]

A subspace $U \leq V$ is **invariant under $T$** if $T(U) \subseteq U$. See [[Def - Invariant Subspace]].

**Key lemma about commuting operators**: if $S$ and $T$ commute and $\mu \in \mathbb{C}$, then the eigenspace $E(\mu, S) = \ker(S - \mu I)$ is **$T$-invariant**. Reason: for $v \in E(\mu, S)$, $(S - \mu I)(Tv) = STv - \mu Tv = T(Sv) - \mu Tv = T(\mu v) - \mu Tv = \mu Tv - \mu Tv = 0$, so $Tv \in E(\mu, S)$.

![[Thm - Existence of Eigenvalues on Complex Vector Spaces#Statement]]

---

# Convergent Strategy

**Problem class.** This is the **simultaneous eigenvalue problem** — a structural existence result combining the chapter's existence-of-eigenvalues theorem with the commutativity hypothesis. The result is the key step in the inductive proof of [[Thm - Upper-Triangular Form on Complex Vector Spaces|simultaneous upper-triangularisation of commuting operators]].

**Assumption pattern.** Two ingredients:
1. **$V$ is finite-dimensional, nonzero, complex** — the hypothesis for [[Thm - Existence of Eigenvalues on Complex Vector Spaces|the existence-of-eigenvalues theorem]].
2. **$S, T$ commute** — converts eigenspaces of $S$ into $T$-invariant subspaces (the key lemma above).

The two ingredients combine: an eigenspace of $S$ is $T$-invariant; on this $T$-invariant subspace (which is itself a nonzero finite-dimensional complex vector space), $T$ has an eigenvector by the existence theorem; this eigenvector is simultaneously an eigenvector of $S$ (it lies in $E(\mu, S)$) and of $T$.

**Theorem routing.** The route is:
1. **$S$ has an eigenvector $v_0$** on $V$ (by [[Thm - Existence of Eigenvalues on Complex Vector Spaces]] applied to $S$). So $E(\mu, S) \neq 0$ for some $\mu \in \mathbb{C}$.
2. **$E(\mu, S)$ is $T$-invariant** (by the key lemma — uses commutativity).
3. **$T|_{E(\mu, S)}$ has an eigenvector $v$** (by [[Thm - Existence of Eigenvalues on Complex Vector Spaces]] applied to $T|_{E(\mu, S)}$, since $E(\mu, S)$ is nonzero finite-dimensional complex).
4. **$v$ is a common eigenvector**: $v \in E(\mu, S)$ gives $Sv = \mu v$, and $v$ being a $T|_{E(\mu, S)}$-eigenvector gives $Tv = \lambda v$ for some $\lambda \in \mathbb{C}$.

**Key decision point.** The non-obvious move is **converting the eigenspace of $S$ into a $T$-invariant subspace via commutativity**. Without commutativity, $T$ acts on $E(\mu, S)$ in some unconstrained way — it could even leave $E(\mu, S)$ entirely. With commutativity, $T$ maps $E(\mu, S)$ into itself, opening the door to applying the existence theorem to the restriction $T|_{E(\mu, S)}$. The eigenvector produced by this restriction lives in $E(\mu, S)$ — which is exactly the invariance of the $\mu$-eigenspace of $S$ — so it is automatically an eigenvector of $S$ too, with eigenvalue $\mu$.

---

# Legal Operations Used

1. **Find a common eigenvector for commuting operators** (operation 8 from the topic page). This exercise IS the operation; the construction is the proof.

2. **Restrict to an invariant subspace** (operation 9). The crucial restriction is $T|_{E(\mu, S)}$ on the $T$-invariant subspace $E(\mu, S)$, where the existence-of-eigenvalues theorem applies.

3. **Find an eigenvector via the existence-of-eigenvalues theorem on $\mathbb{C}$** (a particular instance of operation 2). Used twice: once on $S$ acting on $V$, once on $T|_{E(\mu, S)}$ acting on $E(\mu, S)$.

---

# Hints

> [!note]- Hint 1
> The existence-of-eigenvalues theorem gives $S$ an eigenvalue $\mu \in \mathbb{C}$ with eigenspace $E(\mu, S) \neq 0$. Now ask: how does $T$ interact with this eigenspace?

> [!note]- Hint 2
> If $v \in E(\mu, S)$ (so $Sv = \mu v$) and $S, T$ commute, then $S(Tv) = ?$ Expand using commutativity.

> [!note]- Hint 3
> Compute: $S(Tv) = T(Sv) = T(\mu v) = \mu Tv$. So $Tv$ is also a $\mu$-eigenvector of $S$, i.e. $Tv \in E(\mu, S)$. So $T(E(\mu, S)) \subseteq E(\mu, S)$ — the eigenspace is $T$-invariant.

> [!note]- Hint 4
> Apply the existence-of-eigenvalues theorem to $T|_{E(\mu, S)}$ — an operator on the nonzero finite-dimensional complex vector space $E(\mu, S)$. It has an eigenvector $v$ with $Tv = \lambda v$ for some $\lambda$. And $v \in E(\mu, S)$ gives $Sv = \mu v$ for free.

---

# Solution

The plan is to apply the existence-of-eigenvalues theorem twice: once to $S$ on $V$ to find an eigenspace $E(\mu, S)$, and once to $T$ restricted to $E(\mu, S)$ to find a common eigenvector. The bridge between the two applications is the commutativity of $S$ and $T$, which makes $E(\mu, S)$ $T$-invariant.

**Step 1: $S$ has an eigenspace $E(\mu, S) \neq 0$ for some $\mu \in \mathbb{C}$.**

> [!note]- Derivation
> By the hypotheses, $V$ is a nonzero finite-dimensional complex vector space and $S \in \mathcal{L}(V)$. By [[Thm - Existence of Eigenvalues on Complex Vector Spaces]], $S$ has an eigenvalue $\mu \in \mathbb{C}$. So the eigenspace $E(\mu, S) = \ker(S - \mu I)$ is nonzero.

**Step 2: $E(\mu, S)$ is $T$-invariant.**

> [!note]- Derivation
> Take any $v \in E(\mu, S)$, so $Sv = \mu v$. Apply $T$ and use commutativity:
> $$S(Tv) = (ST) v = (TS) v = T(Sv) = T(\mu v) = \mu (Tv).$$
> So $Tv$ satisfies $S(Tv) = \mu (Tv)$, i.e. $Tv \in \ker(S - \mu I) = E(\mu, S)$. Hence $T(E(\mu, S)) \subseteq E(\mu, S)$, i.e. $E(\mu, S)$ is $T$-invariant.

**Step 3: $T|_{E(\mu, S)}$ has an eigenvector $v$ in $E(\mu, S)$.**

> [!note]- Derivation
> By Step 1, $E(\mu, S)$ is nonzero. By Step 2, $E(\mu, S)$ is $T$-invariant, so the restriction $T|_{E(\mu, S)} : E(\mu, S) \to E(\mu, S)$ is a well-defined operator. $E(\mu, S)$ is a finite-dimensional complex vector space (as a subspace of $V$, which is itself finite-dimensional complex). By [[Thm - Existence of Eigenvalues on Complex Vector Spaces]] applied to $T|_{E(\mu, S)}$ on $E(\mu, S)$, there exists $v \in E(\mu, S)$ with $v \neq 0$ and $(T|_{E(\mu, S)})(v) = \lambda v$ for some $\lambda \in \mathbb{C}$.
>
> Since $(T|_{E(\mu, S)})(v) = T(v)$ (the restriction agrees with $T$ on its domain), we have $Tv = \lambda v$.

**Step 4: $v$ is a common eigenvector of $S$ and $T$.**

> [!note]- Derivation
> We have $v \in E(\mu, S)$ (from Step 3, where the eigenvector is found inside $E(\mu, S)$). So $Sv = \mu v$. Combined with $Tv = \lambda v$ from Step 3, $v$ is simultaneously an eigenvector of $S$ (with eigenvalue $\mu$) and of $T$ (with eigenvalue $\lambda$). $\blacksquare$

> [!note]- Complete formal solution
> Let $V$ be a nonzero finite-dimensional complex vector space and $S, T \in \mathcal{L}(V)$ commuting operators.
>
> By [[Thm - Existence of Eigenvalues on Complex Vector Spaces]] applied to $S$ on $V$, $S$ has an eigenvalue $\mu \in \mathbb{C}$; let $U = E(\mu, S) = \ker(S - \mu I)$, which is a nonzero subspace of $V$.
>
> *$U$ is $T$-invariant.* Take $v \in U$. Then $Sv = \mu v$ and, using $ST = TS$:
> $$S(Tv) = (ST) v = (TS) v = T(\mu v) = \mu (Tv).$$
> So $Tv \in U$. Hence $T(U) \subseteq U$.
>
> *Find a common eigenvector.* Since $U$ is a nonzero finite-dimensional complex vector space (subspace of $V$) and $T|_U : U \to U$ is well-defined, [[Thm - Existence of Eigenvalues on Complex Vector Spaces]] applied to $T|_U$ gives an eigenvector $v \in U$ with $Tv = \lambda v$ for some $\lambda \in \mathbb{C}$.
>
> Now $v \in U = E(\mu, S)$ gives $Sv = \mu v$, and $Tv = \lambda v$. So $v$ is a nonzero vector that is simultaneously an eigenvector of $S$ (for $\mu$) and of $T$ (for $\lambda$). $\blacksquare$

---

# Key Takeaways

**Commutativity makes one operator's eigenspaces invariant under the other.** This is the structural meaning of $ST = TS$: $T$ "respects" $S$'s eigenspace decomposition (and vice versa). The trigger-reaction is "$ST = TS$, want a common $X$" → "restrict to an $S$-eigenspace, which is $T$-invariant by commutativity, and find $X$ there". This is the canonical move for problems combining commutativity and eigenstructure. It appears throughout linear algebra: simultaneous diagonalization, the spectral theorem for commuting normal operators, common decompositions of representations of abelian groups.

**The existence theorem is applied iteratively along nested invariant subspaces.** This exercise is the **inductive step** in the proof of [[Thm - Upper-Triangular Form on Complex Vector Spaces|simultaneous upper-triangularization of commuting operators]] — Axler's theorem 5.80, in fact. The pattern: at each step of the induction, pick a common eigenvector (this exercise) for the family of commuting operators on the current space, set up a quotient or complementary subspace, and induct. The whole family can be simultaneously upper-triangularized by iterating this exercise.

**The pattern extends to any commuting family.** The exercise as stated is for two operators, but the same argument extends to any commuting family $\{T_\alpha\}_{\alpha \in A}$: pick an eigenspace of $T_{\alpha_1}$, restrict $T_{\alpha_2}$ to it (which is invariant by commutativity), find a common eigenspace, restrict $T_{\alpha_3}$, and so on. The final intersection of eigenspaces is nonempty as long as the family is finite (or, with care, even infinite). This is the **common eigenvector for commuting families** — Exercise 9(a) in LADR §5E — and the foundation of the **simultaneous diagonalisation theorem**: a commuting family of diagonalisable operators can be simultaneously diagonalised. Decomposition of representations of abelian groups (always commuting) into one-dimensional pieces is the standard application.

**Trigger-reaction: "find a common X for commuting Y" → restrict to an eigenspace of one, induct on the other.** This pattern appears throughout linear algebra and operator theory. The two key ingredients are: (i) eigenspaces of an operator are invariant under any commuting operator; (ii) a smaller-dimensional invariant subspace gives an inductive descent. Together they reduce many problems about commuting families to problems about a single operator on a smaller space.

**Connection to representation theory.** The structural pattern of this exercise — "commuting operators have a common eigenvector" — is the same as **Schur's lemma** in disguise: in an irreducible representation of a group, any operator commuting with the whole group action must be a scalar. The connection: if $\rho : G \to \mathrm{GL}(V)$ is irreducible and $T$ commutes with every $\rho(g)$, then the eigenspaces of $T$ are $G$-invariant subspaces of $V$; by irreducibility, each is $\{0\}$ or $V$; so $T$ has only one eigenvalue (the only nonzero eigenspace is $V$), making $T = \lambda I$ for some scalar. This generalises the present exercise to commuting families parametrised by groups.
