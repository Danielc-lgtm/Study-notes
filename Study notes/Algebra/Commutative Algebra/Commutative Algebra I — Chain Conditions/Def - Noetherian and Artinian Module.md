---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Module"
  - "Def - Submodule"
  - "Def - Noetherian Ring"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$, and all modules are unital. Let $R$ be a ring and $M$ an [[Def - Module|R-module]]. We write $N \subseteq M$ for "$N$ is a [[Def - Submodule|submodule]] of $M$", and an *ascending chain* of submodules is a sequence $M_1 \subseteq M_2 \subseteq M_3 \subseteq \cdots$; a *descending chain* is $M_1 \supseteq M_2 \supseteq M_3 \supseteq \cdots$. A chain **stabilises** if it is eventually constant: there is $n$ with $M_{n'} = M_n$ for all $n' \geq n$. For a non-empty set $\Sigma$ of submodules, a **maximal element** is an $M_0 \in \Sigma$ contained in no other member of $\Sigma$, and a **minimal element** is one containing no other member. The full registry is on [[Commutative Algebra I — Chain Conditions]].

This is a compound page: it defines two interlocking notions — the **Noetherian module** (a chain condition that bounds growth) and the **Artinian module** (the dual condition bounding shrinkage) — because they are introduced together, are formally dual, and the entire point of the pair is that they are *independent*, so neither is fully understood without the other beside it.

---

# Axiom Motivation

The goal is to write down the *right* finiteness condition on a module — one strong enough to support induction, but not so strong as to exclude the modules we care about. The obvious candidate, "$M$ is [[Def - Finitely Generated Module|finitely generated]]", is the one you would try first, and it is *almost* right; the chain condition is the small but decisive correction that makes it usable. Watching exactly what goes wrong with finite generation is the way to invent the Noetherian axiom rather than memorise it.

**Why finite generation alone fails, and what the chain condition adds.** Finite generation says $M = \langle m_1, \dots, m_k \rangle$ for some finite list. The defect is that this property is not inherited by submodules: a submodule $N \subseteq M$ of a finitely generated module need not itself be finitely generated. The standard witness is $R = \mathbb{Z}[T_1, T_2, \dots]$, finitely generated as a module over itself by the single element $1$, whose submodule of constant-term-zero polynomials needs the infinitely many generators $T_1, T_2, \dots$. An inductive argument that peels off a submodule and recurses therefore *cannot* assume the submodule is still finitely generated — the hypothesis evaporates after one step. The fix is to demand finite generation of *every* submodule at once, and the miracle is that this demand has a purely chain-theoretic reformulation: every ascending chain of submodules stabilises. So the Noetherian axiom is exactly "finite generation made hereditary", and the ascending chain condition is its self-contained, induction-friendly form.

**Why the maximal-element form is equivalent, and why it is wanted.** The ascending chain condition has a logically equivalent contrapositive: every non-empty set $\Sigma$ of submodules has a maximal element. To see the equivalence intuitively, suppose $\Sigma$ had *no* maximal element; then starting from any $N_1 \in \Sigma$ we could always find a strictly larger $N_2 \in \Sigma$, and again a strictly larger $N_3$, building an infinite strictly ascending chain — violating ACC. (The honest proof of the reverse direction needs the axiom of choice, to make the infinitely many "find a strictly larger one" selections.) We *want* this form because it is what powers existence arguments: "choose a maximal counterexample" is the single most common Noetherian proof technique, and it is available precisely because every non-empty family has a maximal member. The two formulations are the same condition wearing different clothes — one good for refuting (build a non-stabilising chain), one good for proving (extract a maximal element).

**Why a dual condition, and why "ascending" and "descending" are not interchangeable.** Having isolated the ascending chain condition, symmetry demands we ask about the *descending* one: every chain $M_1 \supseteq M_2 \supseteq \cdots$ stabilises. This defines the **Artinian** module, and one might expect — wrongly — that it is equivalent to Noetherian or follows from it. It does not. The asymmetry is real and it traces to the asymmetry between $\mathbb{Z}$ and a divisible group. In $\mathbb{Z}$, multiplication by $2$ strictly shrinks an ideal, so $(1) \supsetneq (2) \supsetneq (4) \supsetneq \cdots$ descends forever — $\mathbb{Z}$ is Noetherian (all ideals principal, ACC holds) but *not* Artinian. Dually, in the divisible group $\mathbb{Z}[\tfrac12]/\mathbb{Z}$, the submodules form a single ascending chain $\tfrac12\mathbb{Z}/\mathbb{Z} \subsetneq \tfrac14\mathbb{Z}/\mathbb{Z} \subsetneq \cdots$ with no top — Artinian (no infinite descending chain) but not Noetherian. Keeping both definitions in view, side by side, is the only way to remember they measure independent things: Noetherian bounds how far submodules can *grow*, Artinian bounds how far they can *shrink*, and a module can fail either while satisfying the other.

**What the definition should capture, and what it should exclude.** It must capture finite-dimensional vector spaces (both conditions hold, and length equals dimension), finitely generated modules over $\mathbb{Z}$ and over polynomial rings (Noetherian, by Hilbert), and the ring $R$ as a module over itself whenever $R$ is a [[Def - Noetherian Ring|Noetherian ring]] — indeed the ring definition is recovered as the special case $M = R$, where submodules are exactly ideals. It must *exclude* pathologies like $\mathbb{Z}[T_1, T_2, \dots]$'s constant-term-zero submodule (rightly not Noetherian) while still admitting $\mathbb{Z}$ itself (rightly Noetherian though not Artinian). The chain condition threads this needle precisely because it is a statement about *all* submodules, not about the module's generators in isolation.

---

# The Definition

Let $R$ be a ring and $M$ an [[Def - Module|R-module]].

## Noetherian module

$M$ is **Noetherian** if one — hence both — of the following equivalent conditions holds:

1. **(Ascending chain condition.)** Every ascending chain of [[Def - Submodule|submodules]] $M_1 \subseteq M_2 \subseteq M_3 \subseteq \cdots$ stabilises: there is $n \geq 1$ with $M_{n'} = M_n$ for all $n' \geq n$.
2. **(Maximal condition.)** Every non-empty set $\Sigma$ of submodules of $M$ has a maximal element.

A third equivalent condition — *every submodule of $M$ is finitely generated* — is [[Thm - Noetherian iff Every Submodule is Finitely Generated|the central characterisation]] and the one most used in practice.

## Artinian module

$M$ is **Artinian** if one — hence both — of the following equivalent conditions holds:

1. **(Descending chain condition.)** Every descending chain of submodules $M_1 \supseteq M_2 \supseteq M_3 \supseteq \cdots$ stabilises.
2. **(Minimal condition.)** Every non-empty set $\Sigma$ of submodules of $M$ has a minimal element.

The equivalence of the two conditions in each definition uses the axiom of choice (or a weak form of it).

## The ring case

A ring $R$ is **Noetherian** (resp. **Artinian**) if it is Noetherian (resp. Artinian) as a module over itself; since submodules of $R$ are exactly its [[Def - Ideal|ideals]], this is the chain condition on ideals and recovers [[Def - Noetherian Ring|the Rings IV definition]].

---

# Categorical / Structural Definition

The two conditions are the two well-foundedness conditions on the **poset of submodules** $\operatorname{Sub}(M)$, ordered by inclusion. A partially ordered set satisfies the *ascending chain condition* exactly when it contains no infinite strictly ascending sequence, equivalently when every non-empty subset has a maximal element; dually for the descending chain condition. So:

- $M$ is **Noetherian** $\iff$ $\operatorname{Sub}(M)$ satisfies ACC $\iff$ $\operatorname{Sub}(M)$ is *well-founded under $\supseteq$* (no infinite strictly increasing sequence).
- $M$ is **Artinian** $\iff$ $\operatorname{Sub}(M)$ satisfies DCC $\iff$ $\operatorname{Sub}(M)$ is *well-founded under $\subseteq$*.

This is the same well-foundedness that makes induction work in set theory: ACC is precisely the condition under which "Noetherian induction" — proving a statement about all submodules by assuming it for all strictly larger ones — is valid, exactly as the descending chain condition on $\mathbb{N}$ validates ordinary induction. The maximal/minimal-element formulations are the order-theoretic statements of well-foundedness, and the chain formulations are their negation-of-an-infinite-descent statements; their equivalence is the order-theoretic fact that well-foundedness and "every non-empty subset has a minimal element" coincide (using choice).

---

# Relate to Other Fields / Compression

The cleanest compression is that **Noetherian and Artinian are the two well-foundedness conditions on submodules, and they are independent because a poset can be well-founded in one direction without the other.** The integers under divisibility illustrate the asymmetry in miniature: you cannot ascend forever (every integer has finitely many divisors above it in the order... ) — the genuine clean model is that $\mathbb{Z}$'s ideals descend forever ($n\mathbb{Z} \supsetneq 2n\mathbb{Z} \supsetneq \cdots$) but ascend only finitely.

**True name:** for problem-solving, the operational name of *Noetherian* is **"every submodule is finitely generated, and every non-empty family of submodules has a maximal element"** — you *spend* the hypothesis by grabbing finitely many generators or by choosing a maximal counterexample, never by reasoning about literal chains. The operational name of *Artinian* is **"every non-empty family of submodules has a minimal element"** — you spend it by choosing a minimal nonzero submodule (which is necessarily simple) to start a length argument.

In analysis and set theory this is the well-foundedness underlying induction; in algebraic geometry the Noetherian condition on a ring becomes the descending chain condition on closed subsets of $\operatorname{Spec} R$, the statement that a **Noetherian space** cannot be subdivided into closed pieces forever. In order theory the pair is exactly "ACC poset" and "DCC poset". A finite-dimensional vector space is the place where the two conditions, finite generation, finite length, and finite dimension all coincide — the degenerate case where the ring is a field and no asymmetry can arise.

---

# Examples / Corollaries

**Is an instance (Noetherian, not Artinian) — $\mathbb{Z}$ as a $\mathbb{Z}$-module.** Every submodule of $\mathbb{Z}$ is an ideal $n\mathbb{Z}$, hence principal, hence finitely generated, so $\mathbb{Z}$ is Noetherian by the finite-generation criterion; concretely any ascending chain $n_1\mathbb{Z} \subseteq n_2\mathbb{Z} \subseteq \cdots$ has the $n_i$ dividing down, which can only happen finitely often, so it stabilises. But $\mathbb{Z}$ is *not* Artinian: the chain $(2) \supsetneq (4) \supsetneq (8) \supsetneq \cdots$, i.e. $2\mathbb{Z} \supsetneq 4\mathbb{Z} \supsetneq 8\mathbb{Z} \supsetneq \cdots$, descends strictly forever. This is the canonical separating example showing Noetherian does not imply Artinian.

**Is an instance (Artinian, not Noetherian) — $\mathbb{Z}[\tfrac12]/\mathbb{Z}$ as a $\mathbb{Z}$-module.** Its submodules are exactly $\tfrac{1}{2^n}\mathbb{Z}/\mathbb{Z}$, the cyclic group of order $2^n$, for $n = 0, 1, 2, \dots$ together with the whole module. These form a *single* ascending chain $0 \subsetneq \tfrac12\mathbb{Z}/\mathbb{Z} \subsetneq \tfrac14\mathbb{Z}/\mathbb{Z} \subsetneq \cdots$ with no maximal proper member, so Noetherian fails. But any *descending* chain among these submodules is finite — each $\tfrac{1}{2^n}\mathbb{Z}/\mathbb{Z}$ has only finitely many submodules below it — so DCC holds and the module is Artinian. (See [[Ex - The dyadic rationals mod Z are Artinian but not Noetherian]] for the full submodule analysis.) This is the dual canonical separating example.

**Is an instance (both) — a finite-dimensional vector space.** A $k$-vector space $V$ with $\dim_k V = d < \infty$ satisfies both conditions: any strictly ascending or strictly descending chain of subspaces changes dimension by at least $1$ at each step, so it can have at most $d+1$ terms and must stabilise. Here Noetherian, Artinian, finite length, and finite-dimensional are all the same condition (see [[Ex - A vector space is Noetherian iff Artinian iff finite-dimensional]]).

**Is NOT an instance (neither) — $\mathbb{Z}[T_1, T_2, \dots]$ as a module over itself, restricted to the relevant submodule; and $k[T_1, T_2, \dots]$ as a $k$-vector space.** The polynomial ring $A = k[T_1, T_2, \dots]$ in infinitely many variables, viewed as a $k$-vector space, is neither Noetherian nor Artinian: the chain $\langle T_1 \rangle \subsetneq \langle T_1, T_2 \rangle \subsetneq \cdots$ ascends forever (no Noetherian) and the chain $\langle T_1, T_2, \dots \rangle \supsetneq \langle T_2, T_3, \dots \rangle \supsetneq \cdots$ descends forever (no Artinian). Infinite-dimensional vector spaces always fail both. This probes that the conditions are genuine restrictions, not automatic.

**Corollary — the ring definition is the case $M = R$.** Submodules of $R$ are exactly its ideals, so "$R$ is a Noetherian module over itself" is "every ascending chain of ideals stabilises", the [[Def - Noetherian Ring|definition of a Noetherian ring]]. This is the calibration check that the module notion genuinely generalises the ring notion.

**Calibration check.** Verify directly that $\mathbb{Z}$ is Noetherian but not Artinian by exhibiting the chain $2\mathbb{Z} \supsetneq 4\mathbb{Z} \supsetneq \cdots$. Verify that a field, as a module over itself, is both (its only submodules are $0$ and itself). Confirm that a $\mathbb{Z}$-module that is *not* finitely generated cannot be Noetherian (the module itself is a submodule that is not finitely generated), but *can* be Artinian (take $\mathbb{Z}[\tfrac12]/\mathbb{Z}$). If you can produce, from memory, one Noetherian-not-Artinian and one Artinian-not-Noetherian module, you have understood that the two conditions are independent.

---

# Unlocked by This

> [!tip] Spec as a Noetherian topological space *(from Algebraic Geometry)*
> When $R$ is a Noetherian ring, the ascending chain condition on ideals translates — via the order-reversing correspondence between radical ideals and closed sets — into the *descending* chain condition on closed subsets of **Spec $R$**. A topological space with this property is a **Noetherian space**, and its defining feature is that it has only finitely many irreducible components. This is the structural reason classical varieties decompose into finitely many irreducible pieces.

> [!tip] Artinian rings are zero-dimensional *(from Commutative Algebra)*
> A ring $R$ is **Artinian** if and only if it is Noetherian of Krull dimension zero — equivalently, Noetherian with every prime ideal maximal. So although Noetherian and Artinian are independent for modules, for *rings* Artinian is the much stronger condition "Noetherian and finite", and an Artinian ring is a finite product of Artinian local rings, each of finite length. This is developed in **dimension theory** (Commutative Algebra XII).

> [!tip] Noetherian induction *(from Commutative Algebra)*
> The ascending chain condition validates **Noetherian induction**: to prove a statement holds for all submodules (or all closed subschemes), it suffices to prove it for a submodule assuming it for all strictly larger ones, because a minimal counterexample to "all larger ones satisfy it $\Rightarrow$ this one does" would generate an infinite ascending chain. This is the proof engine behind primary decomposition and the finiteness of associated primes.
