---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Subspace"
  - "Def - Linear Independence"
  - "Def - Linear Combination and Span"
  - "Def - Finite-Dimensional Vector Space"
  - "Thm - Length of Linearly Independent List Bounded by Length of Spanning List"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a finite-dimensional vector space over $F$, $U \subseteq V$ is a subspace. See the parent topic page [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]] for the full notation registry.

---

# Statement

> **Theorem (LADR 2.25).** Every [[Def - Subspace|subspace]] of a [[Def - Finite-Dimensional Vector Space|finite-dimensional]] vector space is itself finite-dimensional.

**Corollary.** Every subspace $U$ of a finite-dimensional $V$ has a [[Def - Basis|basis]], and $\dim U \leq \dim V$.

---

# Motivation

The theorem closes a basic structural gap. Finite-dimensionality is defined as the existence of a *finite spanning list*. A priori a subspace $U$ of a finite-dimensional $V$ might lack a finite spanning list — it could be spanned by something inside $V$, but the spanning list of $V$ uses vectors outside $U$, and they cannot be used to span $U$. So the question "is every subspace finite-dimensional?" is genuine.

The theorem says yes, and the proof is a *constructive greedy procedure*. Build a list inside $U$ by adding any vector of $U$ not in the current span; the list remains linearly independent (since each added vector is outside the previous span); by the [[Thm - Length of Linearly Independent List Bounded by Length of Spanning List|length inequality]] applied in $V$, an independent list in $V$ has length at most $\dim V$, so the procedure terminates. At termination, no vector of $U$ is outside the span, so the span is $U$, and we have a finite spanning list.

The result also gives $\dim U \leq \dim V$ as a direct corollary. The corollary in turn powers the dimension-comparison arguments of §2C — *equality* $\dim U = \dim V$ forces $U = V$ ([[Ex - Dimension of a subspace equals dimension only if equal]]), and inequalities allow us to bound the dimension of an unknown subspace from below or above.

The theorem is a clean illustration of **inheritance**: a property of $V$ (finite-dimensionality) propagates to all of its subspaces. Not every property does — for example, a basis of $V$ does not in general restrict to a basis of $U$. The properties that *do* propagate to subspaces are exactly those defined by independent-list bounds, and finite-dimensionality is the cleanest example.

---

# Sources and Targets

**Sources (Input Broadening).**

The hypothesis is sparse: a subspace of a finite-dimensional space. The skill is recognising that any subspace, however described, has finite dimension.

A first source is **a subspace defined by linear equations**. Property $B$: "$U = \{v \in V : L_i(v) = 0 \text{ for all } i\}$ for some linear conditions $L_i$." The bridge: $U$ is a subspace of finite-dimensional $V$, so finite-dimensional by 2.25. The non-obvious payoff: $\dim U$ is then a well-defined integer, which can be computed by parametric solution.

A second source is **a span of given vectors in $V$**. Property $B$: "$U = \operatorname{span}(v_1, \ldots, v_k)$ for some $v_i \in V$." The bridge: $U$ is a subspace, finite-dimensional, with $\dim U \leq k$ (the spanning list bounds the dimension). The actual dimension can be computed by reducing the spanning list.

A third source is **an intersection or sum of subspaces**. Property $B$: "you have $V_1 \cap V_2$ or $V_1 + V_2$ for two given subspaces." The bridge: both are subspaces, both finite-dimensional. This is what licenses the dimension formula [[Thm - Dimension of a Sum of Subspaces|2.43]] to manipulate $\dim$ of these objects as a well-defined integer.

A fourth source is **a kernel or image of a linear map**. Property $B$: "$T : V \to W$ is a linear map." The bridge: $\ker T \subseteq V$ is a subspace of finite-dimensional $V$, hence finite-dimensional. $\operatorname{range} T \subseteq W$ is a subspace of finite-dimensional $W$ (if $W$ is finite-dimensional), hence finite-dimensional. This pre-figures [[Linear Algebra III — §3A–D Linear Maps|the rank-nullity theorem]], where $\dim \ker T$ and $\dim \operatorname{range} T$ are the two halves of the dimension equation.

**Targets (Output Amplification).**

A first combination is **plus a dimension bound to control element counts**. Knowing $\dim U \leq \dim V = n$ means $U$ has a basis of at most $n$ elements, hence $|U|$ is at most $|F|^n$ if $F$ is finite. This is used in algebraic combinatorics and coding theory: bounds on subspaces of $\mathbb{F}_q^n$ via dimension.

A second combination is **plus inheritance of bases**. Once $U$ is known finite-dimensional, every linearly independent list in $U$ extends to a basis of $U$ ([[Thm - Every Linearly Independent List Extends to a Basis|2.32]] applied within $U$). Without 2.25 this extension would not be guaranteed.

A third combination is **plus the dimension formula 2.43**. The intersection $V_1 \cap V_2$ being finite-dimensional is what licenses the integer $\dim(V_1 \cap V_2)$ appearing in 2.43.

A fourth combination is **plus the lattice of subspaces is finite-dimensional**. The subspace lattice of a finite-dimensional space is a *modular* lattice, and 2.25 is the local content guaranteeing each element of the lattice has a well-defined dimension. The modular law is then proved by combining 2.25 with 2.43.

---

# Why Is It True

The intuition is **greedy construction with a hard cap**: keep adding vectors to a list in $U$ as long as they extend the span, and the process must stop because the resulting list remains linearly independent in $V$ and so is bounded in length by $\dim V$.

Start with the empty list (trivially independent in $U$, spanning $\{0\}$). At each step, if the current list does not span $U$, pick any vector $u \in U$ outside the current span and add it. By the "adding an outside vector preserves independence" property of independence (see [[Def - Linear Independence]] corollary), the new list is still linearly independent.

The current list is, at every step, linearly independent in $U$ — and *hence* in $V$ (independence is a property of the list, not of the ambient). By [[Thm - Length of Linearly Independent List Bounded by Length of Spanning List|2.22]] applied in $V$, the list has length at most $\dim V$. So the procedure cannot run more than $\dim V$ times.

When the procedure stops (after at most $\dim V$ steps), the current list spans $U$ — by construction, there is no vector of $U$ outside the current span at the stopping point. So we have a finite spanning list of $U$, and $U$ is finite-dimensional.

The bolded one-liner: **a greedy linearly-independent list in $U$ cannot exceed length $\dim V$, so the greedy span-extending procedure must terminate, producing a finite spanning list of $U$**.

The corollary $\dim U \leq \dim V$ falls out by counting: any basis of $U$ is an independent list of $U$, hence of $V$, hence has length at most $\dim V$ by 2.22. The basis length is exactly $\dim U$, so $\dim U \leq \dim V$.

---

# What Makes This Hard

The proof is not hard, but it has a slightly unusual flavour for §2: most theorems in §2 take a finite spanning or independent list as input, whereas here the input is a subspace and the work is to *produce* the spanning list. The greedy construction is the right idea, and the termination argument is the bite.

A subtle point is the use of the **axiom of choice** at each step of the greedy construction: we are picking "any" vector of $U$ outside the current span. For finite-dimensional spaces this is essentially trivial (in fact, the choice can usually be made constructively, by parametrising $U$ via linear equations), but in infinite-dimensional spaces the analogous "every subspace is spanned by some Hamel basis" requires Zorn's lemma. The finite-dimensional case is choice-free in practice.

A second potential confusion is the role of *independence-in-the-ambient* vs *independence-in-the-subspace*. Linear independence is a property of the list and the field, *not* of the ambient space. The same list is independent (or dependent) in any space containing all its vectors. The proof uses this fact when it appeals to 2.22 in $V$: the greedy list, independent in $U$, is also independent in $V$.

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.

**High-level strategy:** Run a greedy procedure inside $U$: at each step, either the current list spans $U$ (stop) or there is a vector of $U$ outside the span (add it). The added vector is outside the previous span, hence the extended list remains linearly independent. The length is bounded by $\dim V$ via 2.22, so the procedure terminates.

**Subgoal decomposition:**

1. **Define the greedy procedure.** Start with the empty list. At step $k$, if the current list $L_{k-1} = (u_1, \ldots, u_{k-1})$ spans $U$, stop. Otherwise pick any $u_k \in U \setminus \operatorname{span}(L_{k-1})$ and set $L_k = (u_1, \ldots, u_k)$.
   - *Hint:* The choice of $u_k$ at each step is arbitrary; any vector outside the span works.

2. **Show $L_k$ is linearly independent for every $k$.** By induction: $L_0$ is trivially independent. If $L_{k-1}$ is independent and $u_k \notin \operatorname{span}(L_{k-1})$, then by the iterative-extension corollary of [[Def - Linear Independence|linear independence]], $L_k$ is independent.
   - *Hint:* Adjoining an outside vector preserves independence.

3. **Show the procedure terminates.** $L_k$ is linearly independent in $U$, hence in $V$. By [[Thm - Length of Linearly Independent List Bounded by Length of Spanning List|2.22]] applied in $V$ with $L_k$ as the independent list and any spanning list of $V$ (length $\dim V$), we have $k \leq \dim V$. So the procedure runs for at most $\dim V$ steps before having to stop.
   - *Hint:* The cap is $\dim V$.

4. **At termination, the list spans $U$.** The stopping criterion was "the current list spans $U$", so by construction this holds at termination.
   - *Hint:* This is the stopping criterion itself.

5. **Conclude $U$ is finite-dimensional.** $U$ has a finite spanning list (of length at most $\dim V$), so is finite-dimensional by definition.

---

# Lemma Decomposition

> [!note]- Lemma 1: Adding a vector outside the span preserves independence
> **Statement:** If $u_1, \ldots, u_{k-1}$ is linearly independent and $u_k \notin \operatorname{span}(u_1, \ldots, u_{k-1})$, then $u_1, \ldots, u_k$ is linearly independent.
>
> **Hint:** If $u_k$ had a non-trivial coefficient in a vanishing combination, it would land in the span of the predecessors; if the coefficient is zero, independence of $u_1, \ldots, u_{k-1}$ forces the rest to vanish.
>
> **Why needed:** This is what keeps the greedy procedure producing independent lists.
>
> > [!note]- Full proof
> > Suppose $a_1 u_1 + \cdots + a_{k-1} u_{k-1} + a_k u_k = 0$. If $a_k \neq 0$, then $u_k = -a_k^{-1} (a_1 u_1 + \cdots + a_{k-1} u_{k-1}) \in \operatorname{span}(u_1, \ldots, u_{k-1})$, contradicting the hypothesis. So $a_k = 0$. The remaining equation $a_1 u_1 + \cdots + a_{k-1} u_{k-1} = 0$, by linear independence of $u_1, \ldots, u_{k-1}$, forces $a_1 = \cdots = a_{k-1} = 0$. So all $a_i = 0$, and the list $u_1, \ldots, u_k$ is linearly independent.

> [!note]- Lemma 2: An independent list in a subspace is independent in the ambient
> **Statement:** If $W \subseteq V$ are vector spaces and $v_1, \ldots, v_m \in W$ is a linearly independent list in $W$, then it is also linearly independent in $V$.
>
> **Hint:** Independence is a property of the list and the field, not of the ambient space.
>
> **Why needed:** The greedy list, independent in $U$, must be independent in $V$ to apply 2.22.
>
> > [!note]- Full proof
> > A vanishing combination $a_1 v_1 + \cdots + a_m v_m = 0$ in $V$ is the same equation as $a_1 v_1 + \cdots + a_m v_m = 0$ in $W$ (since $W$ shares the zero vector with $V$, and inherits the addition and scalar multiplication). So the set of vanishing combinations is the same in both, and the trivial-only condition is preserved.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Every subspace $U$ of a finite-dimensional vector space $V$ is finite-dimensional.
>
> *Proof.* We run a greedy construction.
>
> **Step 0** (initialisation). Set $L_0 = ()$, the empty list. By convention, $L_0$ is linearly independent.
>
> **Step $k$** (for $k \geq 1$). If $\operatorname{span}(L_{k-1}) = U$, halt and return $L_{k-1}$. Otherwise, pick any $u_k \in U \setminus \operatorname{span}(L_{k-1})$ and set $L_k = (u_1, \ldots, u_k)$ where the first $k-1$ entries are those of $L_{k-1}$.
>
> *Claim 1: $L_k$ is linearly independent for every $k$ for which it is defined.*
>
> By induction on $k$. Base case: $L_0$ is linearly independent. Inductive step: if $L_{k-1}$ is independent and the procedure does not halt at step $k$, then $u_k \notin \operatorname{span}(L_{k-1})$, and by Lemma 1, $L_k$ is independent.
>
> *Claim 2: The procedure halts within $\dim V$ steps.*
>
> By Claim 1, $L_k$ is linearly independent in $U$. By Lemma 2, $L_k$ is also linearly independent in $V$. By [[Thm - Length of Linearly Independent List Bounded by Length of Spanning List|LADR 2.22]] applied to $L_k$ and any basis of $V$ (which has length $\dim V$, by [[Def - Dimension|definition of dimension]]), we have $|L_k| \leq \dim V$, i.e. $k \leq \dim V$. So the procedure must halt at some step $\leq \dim V$.
>
> *Claim 3: At halt, the returned list spans $U$.*
>
> The procedure halts at step $k$ exactly when $\operatorname{span}(L_{k-1}) = U$. So the returned list $L_{k-1}$ spans $U$.
>
> Hence $U$ has a finite spanning list (of length at most $\dim V$), so $U$ is finite-dimensional by definition. $\qquad\blacksquare$
>
> **Corollary.** $\dim U \leq \dim V$. *Proof:* By the theorem, $U$ has a basis $u_1, \ldots, u_m$ of length $m = \dim U$. This basis is a linearly independent list in $U$, hence in $V$ by Lemma 2. By [[Thm - Length of Linearly Independent List Bounded by Length of Spanning List|2.22]], $m \leq \dim V$, so $\dim U \leq \dim V$. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Module theory: Noetherian rings and finitely generated submodules.** A ring $R$ is **Noetherian** if every submodule of a finitely generated $R$-module is itself finitely generated. This is the module-theoretic analogue of 2.25: finite-generation propagates to submodules. Over fields, every module is finitely generated iff it has a finite basis; Noetherian-ness of fields is trivial (every ideal is principal — either $0$ or the whole field). Over $\mathbb{Z}$, Noetherian-ness gives "every subgroup of a finitely generated abelian group is finitely generated", which is the structure theorem for finitely generated abelian groups.

**Algebraic topology: subcomplexes of finite CW complexes have finitely many cells.** A CW complex with finitely many cells is "finite-dimensional" in a topological sense; its subcomplexes have only finitely many cells too. The analogue of 2.25 here is that the cellular structure is inherited by subcomplexes, with at most the cell count of the ambient.

**Functional analysis: subspaces of finite-dimensional normed spaces are closed.** In a finite-dimensional normed vector space, every subspace is automatically closed (Heine-Borel argument: finite-dimensional subspaces are complete, hence closed in any normed superspace). The closedness is *automatic* in finite dimensions, but in infinite-dimensional Banach spaces, subspaces can be dense (the polynomial subspace of $C[0,1]$ is dense by Weierstrass) — and densely included subspaces fail to be closed. So 2.25, in its full generality, is a uniquely finite-dimensional phenomenon when one tries to lift it to topological vector spaces.

---

# Bridges

- **[[Thm - Length of Linearly Independent List Bounded by Length of Spanning List]]** — the proof of 2.25 is essentially the application of 2.22 to control the greedy list. Without the length inequality the procedure could in principle run forever; with it, the procedure terminates after at most $\dim V$ steps.

- **[[Thm - Every Linearly Independent List Extends to a Basis]]** — once $U$ is known finite-dimensional, every linearly independent list in $U$ extends to a basis of $U$ by 2.32 *applied within $U$*. The two theorems combine: 2.25 says $U$ is finite-dimensional, so 2.32 in $U$ is meaningful. Without 2.25 the latter would not be available.

- **Inheritance — finite-dimensional spaces inherit their structure** — 2.25 is one of the cleanest "inheritance" results in linear algebra. The property "is finite-dimensional" propagates to every subspace. The analogous question for other properties is interesting: "having a particular basis" does not propagate (a basis of $V$ does not in general restrict to a basis of $U$), but "having a basis" (i.e. being a vector space at all) does. Properties that are downstream invariants of dimension all propagate to subspaces.

- **Noetherian property (commutative algebra)** — the module-theoretic generalisation, requiring the ring to be Noetherian. Over a field this is automatic; over $\mathbb{Z}$ it gives the structure theorem for finitely generated abelian groups; over polynomial rings it gives Hilbert basis theorem.
