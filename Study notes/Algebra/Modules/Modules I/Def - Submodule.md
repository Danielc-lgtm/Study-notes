---
type: definition
subject: module-theory
prereqs:
  - "Def - Module"
  - "Def - Ring"
  - "Def - Ideal"
  - "Def - Abelian Group"
  - "Def - Unit and Field"
tags: [algebra, module-theory]
---

# Notation

$R$ is a commutative ring with $1_R$, and $M = (M, +, 0_M, \cdot)$ is an [[Def - Module|R-module]]. A submodule $N$ of $M$ is written $N \leq M$, the same symbol used for "subgroup" and "subspace" — deliberately, since a submodule is both at once. Elements of $M$ are $m, n$; scalars are $r, s$. The action is written by juxtaposition, $rn$. See [[Modules I — §3.1–3.2]] for the full notation registry.

---

# Axiom Motivation

Every algebraic structure comes with a notion of *substructure*: a subset that is closed under all the operations and is therefore a structure of the same kind in its own right. For [[Def - Group|groups]] it is the subgroup, for [[Def - Ring|rings]] the [[Def - Subring|subring]], for vector spaces the subspace. A **submodule** is simply the substructure notion for [[Def - Module|modules]], and the way to invent it is mechanical: list the operations of a [[Def - Module|module]], and demand a subset be closed under each one.

A module has exactly two pieces of operational data: the abelian group structure $(M, +, 0_M)$, and the action $\cdot : R \times M \to M$. So a submodule must be closed under both. Closure under the group structure means the subset $N$ must be a **subgroup** of $(M, +, 0_M)$ — non-empty, closed under $+$, and closed under additive inverses (equivalently, by the subgroup criterion, closed under $n_1 - n_2$). Closure under the action means: whenever $n \in N$ and $r \in R$, the element $rn$ must again lie in $N$. That is the entire definition. There is nothing to invent beyond "be closed under everything a module can do".

Watch what each clause buys you, and what is lost if it is dropped. If you keep only the subgroup condition and forget action-closure, you have specified a subset that is fine under addition but on which scalar multiplication may *leave* the subset — and then $N$ is not a module at all, because the action $R \times N \to N$ does not even land in $N$. Concretely, inside the $\mathbb{Z}[X]$-module $\mathbb{Z}[X]$, the subgroup $\mathbb{Z}$ of constant polynomials is closed under addition, but the scalar $X$ sends the element $1 \in \mathbb{Z}$ to $X \notin \mathbb{Z}$; so $\mathbb{Z}$ is a subgroup but not a submodule. Conversely, if you somehow demanded action-closure but forgot the subgroup condition, $N$ might not contain $0_M$ or might not be closed under addition, and again would fail to be a module. Both clauses are needed, and together they are not just necessary but *sufficient*: a subset closed under $+$, inverses, and the action, equipped with the restricted operations, satisfies every module axiom automatically — axioms (a)–(d) are universally quantified identities, so if they hold for all elements of $M$ they certainly hold for all elements of $N$. This is the recurring miracle of substructure definitions: closure is the only thing to check, because the *axioms come for free by restriction*.

There is one more thing the definition should make you anticipate: a submodule is *both* a subgroup *and* — when $M = R$ — an [[Def - Ideal|ideal]]. The reason is that the action-closure clause "$r \in R, n \in N \implies rn \in N$" is *verbatim* the absorption clause in the definition of an ideal. So the submodule concept is engineered to make "subgroup", "subspace", and "ideal" instances of one idea, depending on what the ambient module $M$ is. That is the payoff of getting the definition right: a single closure condition specialises correctly in every case.

---

# The Definition

Let $M$ be an [[Def - Module|R-module]]. A subset $N \subseteq M$ is an **$R$-submodule of $M$**, written $N \leq M$, if:

1. **[[Def - Subgroup|Subgroup]].** $N$ is a subgroup of the abelian group $(M, +, 0_M)$ — equivalently, $N$ is non-empty and $n_1 - n_2 \in N$ whenever $n_1, n_2 \in N$ (this single condition gives closure under addition, inverses, and membership of $0_M$).

2. **Closure under the action.** For every $r \in R$ and every $n \in N$, the element $r \cdot n$ lies in $N$.

Equipped with the restricted addition, the element $0_M$, and the restricted action $R \times N \to N$, a submodule $N$ is itself an $R$-module: the four module axioms are universally quantified identities, so they continue to hold on the subset $N$ with no further verification. Every module $M$ has two **trivial submodules**, the zero submodule $\{0_M\}$ and $M$ itself; a submodule different from $M$ is called **proper**.

A compact equivalent of the two conditions: $N$ is a submodule if and only if $N \neq \emptyset$ and $rn_1 + n_2 \in N$ for all $r \in R$ and all $n_1, n_2 \in N$ — a single closure check folding the subgroup criterion and the action together.

---

# Relate to Other Fields / Compression

A submodule is **the simultaneous generalisation of "subspace" and "ideal", and a specialisation of "subgroup"**. Run the dial on the ambient module $M$. When $M$ is a vector space over a field $F$, an $F$-submodule is exactly a vector **subspace** — the two conditions become "closed under addition and under scalar multiplication", the textbook subspace test. When $M$ is the ring $R$ regarded as a module over itself, an $R$-submodule is exactly an [[Def - Ideal|ideal]] of $R$ — the action-closure clause "$rn \in N$" is precisely ideal absorption. And in every case, forgetting the action, a submodule is in particular a **subgroup** of the underlying abelian group.

So the inclusion-of-concepts reads: subgroup $\supseteq$ submodule, and submodule is a single notion that, depending on $M$, *is* a subspace or *is* an ideal. This is why one symbol $N \leq M$ serves all three. The compression is genuine: a theorem about submodules (the [[Thm - Isomorphism Theorems for Modules|isomorphism theorems]], say) instantly yields a theorem about subspaces, a theorem about ideals, and a theorem about subgroups of abelian groups.

---

# Examples / Corollaries

**Is an instance: the trivial submodules.** In any [[Def - Module|R-module]] $M$, both $\{0_M\}$ and $M$ are submodules. The set $\{0_M\}$ is a subgroup and $r \cdot 0_M = 0_M \in \{0_M\}$ for every $r$; the set $M$ is closed under everything by definition. A module whose *only* submodules are these two (and $M \neq \{0_M\}$) is called **simple** — the module-theoretic analogue of a simple group or a field.

**Is an instance: submodules of $R$ are exactly the [[Def - Ideal|ideals]].** Regard $R$ as a module over itself. A subset $N \subseteq R$ is an $R$-submodule precisely when it is an additive subgroup of $R$ and $rn \in N$ for all $r \in R, n \in N$ — and that is *word for word* the definition of an [[Def - Ideal|ideal]] $N \trianglelefteq R$. So the lattice of submodules of $R$ and the lattice of ideals of $R$ are the same object. For example, in $\mathbb{Z}$ the submodules of $\mathbb{Z}$ (as a $\mathbb{Z}$-module) are exactly the subsets $n\mathbb{Z}$, the ideals of $\mathbb{Z}$.

**Is an instance: $F$-submodules are exactly [[Def - Subspace|subspaces]].** If $F$ is a [[Def - Unit and Field|field]] and $V$ is an $F$-module — that is, a vector space over $F$ — then a subset $W \subseteq V$ is an $F$-submodule if and only if $W$ is a vector subspace of $V$. The submodule conditions are the subspace test verbatim. For instance, any line through the origin in $\mathbb{R}^2$ is an $\mathbb{R}$-submodule of $\mathbb{R}^2$.

**Is an instance: $nM$ and the $n$-torsion, inside a $\mathbb{Z}$-module.** Let $M$ be a $\mathbb{Z}$-module — an abelian group — and fix $n \in \mathbb{Z}$. The set $nM = \{nm : m \in M\}$ is a submodule (it is closed under addition since $nm_1 + nm_2 = n(m_1 + m_2)$, and under the $\mathbb{Z}$-action since $k(nm) = n(km)$). So is the **$n$-torsion** $M[n] = \{m \in M : nm = 0\}$. These are genuine submodules manufactured purely from the action, with no analogue available for a bare set; they are the typical *players* in torsion arguments.

**Is NOT an instance: a non-empty subset closed under addition but not the action.** Inside the $\mathbb{Z}[X]$-module $M = \mathbb{Z}[X]$, take $N = \mathbb{Z}$, the constant polynomials. $N$ is a subgroup of $(\mathbb{Z}[X], +)$ — sums and differences of constants are constants. But it fails action-closure: the scalar $X \in \mathbb{Z}[X]$ sends the element $1 \in N$ to $X \cdot 1 = X \notin N$. So $N$ is a subgroup that is **not** a submodule. This non-example isolates condition (2): a subset can satisfy the entire group-theoretic half and still fail to be a submodule, because scalar multiplication escapes it.

**Is NOT an instance: a subset closed under the action but not under addition.** In the $\mathbb{Z}$-module $M = \mathbb{Z}$, take $N = \{0\} \cup \{\pm 2^k : k \geq 0\} = \{\ldots, -4, -2, -1, 0, 1, 2, 4, \ldots\}$, the integers that are $0$ or $\pm$ a power of $2$. This set is closed under the $\mathbb{Z}$-action *only* in the loose sense that it contains $0$; in fact even action-closure fails ($3 \cdot 2 = 6 \notin N$). The cleaner illustration of "fails addition": the subset $\{0, 1\} \subseteq \mathbb{Z}$ contains $0$ and is fixed under no nontrivial scalar, and $1 + 1 = 2 \notin \{0,1\}$, so it is not even a subgroup, hence not a submodule. The point: dropping the subgroup condition (1) also destroys submodule-hood, so both conditions are independently necessary.

**Corollary (intersections of submodules are submodules).** If $\{N_i\}_{i \in I}$ is any family of submodules of $M$, then $\bigcap_{i} N_i$ is a submodule. *Calibration check:* if $x, y \in \bigcap N_i$ then $x, y$ lie in each $N_i$, so $rx + y \in N_i$ for each $i$ (each $N_i$ is a submodule), hence $rx + y \in \bigcap N_i$; and the intersection is non-empty as every $N_i$ contains $0_M$. This is what licenses the definition of the submodule *generated* by a set as the intersection of all submodules containing it.

**Corollary (sums of submodules are submodules).** If $A, B \leq M$ then $A + B = \{a + b : a \in A, b \in B\}$ is a submodule, and it is the smallest submodule containing both $A$ and $B$. *Calibration check:* given $a + b$ and $a' + b'$ in $A + B$ and a scalar $r$, the combination $r(a+b) + (a'+b') = (ra + a') + (rb + b')$ lies in $A + B$ because $ra + a' \in A$ and $rb + b' \in B$. Intersection and sum make the submodules of $M$ into a lattice — the setting for the [[Thm - Isomorphism Theorems for Modules|second isomorphism theorem]].

**Corollary (a submodule is closed under finite $R$-linear combinations).** If $N \leq M$, then for any $n_1, \ldots, n_k \in N$ and any scalars $r_1, \ldots, r_k \in R$, the element $r_1 n_1 + \cdots + r_k n_k$ lies in $N$. *Calibration check:* this is conditions (1) and (2) applied repeatedly. It is the reason the [[Def - Finitely Generated Module|submodule generated]] by a set $S$ is exactly the set of finite $R$-linear combinations of elements of $S$.

---

# Unlocked by This

> [!tip] Quotient module *(from this chapter)*
> Once you have a submodule $N \leq M$, you can form the [[Def - Quotient Module|quotient module]] $M/N$ — and remarkably this works for *any* submodule, with no normality or ideal-type restriction, unlike the situation for groups and rings.

> [!tip] Kernel and image *(from this chapter)*
> The kernel and image of a [[Def - Module Homomorphism|module homomorphism]] are submodules — of the source and target respectively — which is exactly what makes the [[Thm - Isomorphism Theorems for Modules|isomorphism theorems]] for modules go through.

> [!tip] Generated submodules and finite generation *(from Commutative Algebra)*
> The intersection of all submodules containing a set $S$ is the **submodule generated by $S$**; when a finite $S$ generates the whole module, $M$ is [[Def - Finitely Generated Module|finitely generated]]. This is the substructure language in which the structure theorem for modules over a principal ideal domain is stated.
