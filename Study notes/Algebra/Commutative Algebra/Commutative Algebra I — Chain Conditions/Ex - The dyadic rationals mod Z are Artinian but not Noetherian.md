---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Noetherian and Artinian Module"
  - "Def - Submodule"
  - "Def - Module"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Consider the $\mathbb{Z}$-module
$$M = \mathbb{Z}[\tfrac12]/\mathbb{Z}, \qquad \text{where } \mathbb{Z}[\tfrac12] = \left\{\tfrac{a}{2^m} : a, m \in \mathbb{Z}\right\}$$
is the ring of **dyadic rationals**. Prove that $M$ is **Artinian but not Noetherian** as a $\mathbb{Z}$-module.

The intended route: classify all submodules of $M$. Show they are exactly
$$0 = M_0 \subsetneq M_1 \subsetneq M_2 \subsetneq \cdots, \qquad M_n = \tfrac{1}{2^n}\mathbb{Z}/\mathbb{Z} = \left\{\tfrac{a}{2^n} + \mathbb{Z} : a \in \mathbb{Z}\right\} \cong \mathbb{Z}/2^n,$$
together with $M$ itself. These form a single ascending chain with no top (so Noetherian fails) and admit no infinite strictly descending chain (so Artinian holds).

**Recall:**

![[Def - Noetherian and Artinian Module#Noetherian module]]

![[Def - Noetherian and Artinian Module#Artinian module]]

A [[Def - Submodule|submodule]] of a $\mathbb{Z}$-module is a subgroup closed under integer scalars (automatic for abelian groups, so a $\mathbb{Z}$-submodule is just a subgroup). The module $M = \mathbb{Z}[\tfrac12]/\mathbb{Z}$ consists of cosets $\tfrac{a}{2^m} + \mathbb{Z}$; every element has order a power of $2$ (it is a **$2$-group**), and $M$ is the **Prüfer $2$-group** $\mathbb{Z}(2^\infty)$. Its element $\tfrac{a}{2^m} + \mathbb{Z}$ may be taken with $0 \leq a < 2^m$ and, after cancelling, with $a$ odd (or the element is $0$).

---

# Convergent Strategy

**Problem class.** This is a *refute-a-chain-condition* problem combined with a *verify-the-dual-chain-condition* problem — the two halves of [[Commutative Algebra I — Chain Conditions#Problem-Solving Strategy|the chapter's central dichotomy]]. To disprove Noetherian you exhibit one strictly ascending chain that never stabilises; to prove Artinian you must show *no* strictly descending chain is infinite, which requires understanding *all* submodules, not just one chain. The decisive observation is that the submodules of $M$ are **totally ordered** by inclusion — a single chain — which makes both halves transparent at once.

**Assumption pattern.** The structure to exploit is that $M$ is a divisible $2$-group whose submodules are forced to be the finite cyclic pieces $M_n = \tfrac{1}{2^n}\mathbb{Z}/\mathbb{Z}$. The recognisable trigger is "divisible torsion group with a single generator at each level": every element is killed by some $2^n$, and the elements killed by $2^n$ form exactly $M_n$. So a submodule is determined by *how high it reaches* — the largest $n$ for which it contains an element of order $2^n$ — and either it reaches a finite maximum (giving $M_n$) or it reaches all levels (giving $M$).

**Theorem routing.** The route is: (1) compute, for each $n$, the submodule $M_n = \{x \in M : 2^n x = 0\}$ of elements killed by $2^n$, and show $M_n \cong \mathbb{Z}/2^n$; (2) prove *every* proper submodule is some $M_n$, by showing a submodule containing an element of order $2^n$ contains all of $M_n$, and a proper submodule has a finite maximal level; (3) read off the chain condition directly from the classification $0 \subsetneq M_1 \subsetneq M_2 \subsetneq \cdots \subsetneq M$. Step (3) needs no theorem — once the submodule lattice is the chain $0 \subsetneq M_1 \subsetneq \cdots$, ascending-non-stabilising is visible (no Noetherian) and descending-always-finite is visible (Artinian).

**Key decision point.** The non-obvious move is to *classify all submodules* rather than fish for one ascending and one descending chain. One could try to disprove Noetherian with the chain $M_1 \subsetneq M_2 \subsetneq \cdots$ directly (easy), but *proving* Artinian cannot be done by inspecting a single descending chain — you must rule out *all* infinite descending chains, and the only way to do that cleanly is to know the entire submodule lattice is well-ordered downward. The genuine insight is that the submodules are **totally ordered**: any two are comparable, so any descending chain is a descending chain in $\{M, M_n, 0\}$ indexed by decreasing $n$, which is finite because the $n$ are non-negative integers. The total order is what makes the Prüfer group the canonical Artinian-not-Noetherian example.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra I — Chain Conditions#Legal Operations|the topic page's Legal Operations]]:

1. **Operation 4 (refute a chain condition with one explicit chain).** To disprove Noetherian, exhibit the single strictly ascending chain $M_1 \subsetneq M_2 \subsetneq M_3 \subsetneq \cdots$ and verify each inclusion is strict (each $M_{n+1}$ contains an element of order $2^{n+1}$ not in $M_n$).

2. **Classification of submodules (a structural prerequisite to operation 4 in the Artinian direction).** Determine *all* submodules of $M$ — they are $0$, the $M_n$, and $M$ — so that the descending chain condition can be checked against the complete lattice, not a single chain.

3. **Operation 5 / the maximal-and-minimal conditions.** Read off ACC and DCC from the classified lattice: the family $\{M_n\}$ has no maximal element (no Noetherian) but every non-empty subfamily of submodules has a minimal element (Artinian), because the indices are well-ordered.

---

# Hints

> [!note]- Hint 1
> Both chain conditions are about *submodules*. Before testing either, ask: what are all the submodules of $M = \mathbb{Z}[\tfrac12]/\mathbb{Z}$? Every element of $M$ has order a power of $2$. For a fixed $n$, what is the set of elements $x$ with $2^n x = 0$?

> [!note]- Hint 2
> Let $M_n = \{x \in M : 2^n x = 0\}$. Show $M_n = \tfrac{1}{2^n}\mathbb{Z}/\mathbb{Z}$, a cyclic group of order $2^n$ generated by $\tfrac{1}{2^n} + \mathbb{Z}$. These are submodules and they are nested: $M_0 = 0 \subsetneq M_1 \subsetneq M_2 \subsetneq \cdots$.

> [!note]- Hint 3
> Show these are *all* the proper submodules. If a submodule $N$ contains an element of order $2^n$ (i.e. some $\tfrac{a}{2^n} + \mathbb{Z}$ with $a$ odd), then it contains a generator of $M_n$, hence all of $M_n$. So $N$ is determined by the set of orders it contains. If that set is bounded by $2^n$, then $N = M_n$; if unbounded, $N = M$.

> [!note]- Hint 4
> Now the chain conditions are immediate from the lattice $0 \subsetneq M_1 \subsetneq M_2 \subsetneq \cdots \subsetneq M$. The ascending chain $M_1 \subsetneq M_2 \subsetneq \cdots$ never stabilises — *not Noetherian*. For Artinian: any descending chain of submodules is a descending chain among $\{M, M_n, 0\}$, indexed by *decreasing* $n$; since the indices are non-negative integers, the chain is finite — *Artinian*.

---

# Solution

The proof is in three steps. Step 1 identifies the submodules $M_n = \tfrac{1}{2^n}\mathbb{Z}/\mathbb{Z}$ of elements killed by $2^n$. Step 2 proves these and $M$ are the *only* submodules, by showing each proper submodule reaches a finite maximal order-level. Step 3 reads both chain conditions off the resulting totally-ordered lattice. The non-obvious move is the full classification in Step 2 — without it, Artinian cannot be verified.

**Step 1: For each $n \geq 0$, the set $M_n = \{x \in M : 2^n x = 0\}$ equals $\tfrac{1}{2^n}\mathbb{Z}/\mathbb{Z}$, a cyclic submodule of order $2^n$, and $M_0 = 0 \subsetneq M_1 \subsetneq M_2 \subsetneq \cdots$.**

> [!note]- Derivation
> An element of $M = \mathbb{Z}[\tfrac12]/\mathbb{Z}$ is a coset $x = \tfrac{a}{2^m} + \mathbb{Z}$; we may take $0 \leq a < 2^m$. Then $2^n x = \tfrac{2^n a}{2^m} + \mathbb{Z}$, which is $0$ in $M$ (i.e. an integer) exactly when $2^m \mid 2^n a$, i.e. when $\tfrac{a}{2^m}$ has denominator dividing $2^n$ after reduction — equivalently $x \in \tfrac{1}{2^n}\mathbb{Z}/\mathbb{Z}$. Hence
> $$M_n = \{x \in M : 2^n x = 0\} = \tfrac{1}{2^n}\mathbb{Z}/\mathbb{Z} = \left\{\tfrac{a}{2^n} + \mathbb{Z} : a \in \mathbb{Z}\right\}.$$
> This is the image of the cyclic group $\langle \tfrac{1}{2^n}\rangle$ under the quotient map; it is generated by $g_n = \tfrac{1}{2^n} + \mathbb{Z}$, and $g_n$ has order exactly $2^n$ (the least $k$ with $\tfrac{k}{2^n} \in \mathbb{Z}$ is $k = 2^n$). So $M_n \cong \mathbb{Z}/2^n$. Each $M_n$ is a submodule (kernel of multiplication by $2^n$). Since $g_n = 2 g_{n+1}$, we have $M_n \subseteq M_{n+1}$, and the inclusion is strict because $g_{n+1} \in M_{n+1} \setminus M_n$ (it has order $2^{n+1} > 2^n$). Thus $0 = M_0 \subsetneq M_1 \subsetneq M_2 \subsetneq \cdots$.

**Step 2: Every proper submodule of $M$ equals some $M_n$; the only other submodule is $M$ itself.**

> [!note]- Derivation
> Let $N \subseteq M$ be a submodule. Define its *level set* $S = \{n \geq 0 : N \text{ contains an element of order } 2^n\}$. Note $0 \in S$ (the zero element).
>
> *Claim: if $n \in S$ then $M_n \subseteq N$.* If $N$ contains an element $x$ of order $2^n$, write $x = \tfrac{a}{2^n} + \mathbb{Z}$ with $a$ odd (order $2^n$ forces the reduced denominator to be exactly $2^n$, i.e. $a$ odd). Since $a$ is odd, it is invertible mod $2^n$: choose $b$ with $ab \equiv 1 \pmod{2^n}$. Then $b x = \tfrac{ab}{2^n} + \mathbb{Z} = \tfrac{1}{2^n} + \mathbb{Z} = g_n$, so $g_n \in N$ (submodules are closed under $\mathbb{Z}$-scalars). Hence $M_n = \langle g_n \rangle \subseteq N$, proving the claim.
>
> *Consequence.* $S$ is "downward closed" in the sense that $n \in S \Rightarrow \{0, 1, \dots, n\} \subseteq S$ (since $M_n \supseteq M_k$ for $k \leq n$, all those levels appear). Two cases:
> - **$S$ is bounded**, with maximum $n$. Then $N$ contains no element of order $> 2^n$, so $N \subseteq M_n$ (every element of $N$ is killed by $2^n$); and $N \supseteq M_n$ by the claim. Hence $N = M_n$.
> - **$S$ is unbounded.** Then $M_n \subseteq N$ for all $n$, so $N \supseteq \bigcup_n M_n = M$ (every element of $M$ lies in some $M_n$). Hence $N = M$.
>
> So the submodules of $M$ are exactly $\{M_n : n \geq 0\} \cup \{M\}$, totally ordered by inclusion.

**Step 3: $M$ is not Noetherian (ascending chain $M_1 \subsetneq M_2 \subsetneq \cdots$) but is Artinian (every descending chain is finite).**

> [!note]- Derivation
> *Not Noetherian.* The chain $M_1 \subsetneq M_2 \subsetneq M_3 \subsetneq \cdots$ from Step 1 is strictly ascending and never stabilises, so the ascending chain condition fails. (Equivalently, the family $\{M_n\}$ has no maximal element.)
>
> *Artinian.* Let $N_1 \supseteq N_2 \supseteq \cdots$ be any descending chain of submodules. By Step 2 each $N_i$ is either $M$ or some $M_{n_i}$ or $0$. Discarding leading copies of $M$, from some point on each $N_i = M_{n_i}$ (or $0 = M_0$), and $N_i \supseteq N_{i+1}$ forces $n_i \geq n_{i+1}$. So $(n_i)$ is a non-increasing sequence of non-negative integers, which is eventually constant. Hence the chain stabilises, and the descending chain condition holds: $M$ is Artinian.

> [!note]- Complete formal solution
> **Claim.** $M = \mathbb{Z}[\tfrac12]/\mathbb{Z}$ is Artinian but not Noetherian as a $\mathbb{Z}$-module.
>
> For $n \geq 0$ let $M_n = \{x \in M : 2^n x = 0\}$. Then $M_n = \tfrac{1}{2^n}\mathbb{Z}/\mathbb{Z}$ is cyclic of order $2^n$, generated by $g_n = \tfrac{1}{2^n} + \mathbb{Z}$, with $g_n = 2g_{n+1}$, so $0 = M_0 \subsetneq M_1 \subsetneq M_2 \subsetneq \cdots$.
>
> *Classification.* Let $N \subseteq M$ be a submodule. If $N$ contains an element $x = \tfrac{a}{2^n}+\mathbb{Z}$ of order $2^n$ (so $a$ odd), pick $b$ with $ab \equiv 1 \pmod{2^n}$; then $bx = g_n \in N$, so $M_n \subseteq N$. Thus if the orders of elements of $N$ are bounded by $2^n$, then $N = M_n$; if unbounded, $N \supseteq \bigcup_n M_n = M$, so $N = M$. Hence the submodules are exactly $\{M_n\}_{n \geq 0}$ and $M$, totally ordered by inclusion.
>
> *Not Noetherian.* $M_1 \subsetneq M_2 \subsetneq \cdots$ is a non-stabilising ascending chain.
>
> *Artinian.* Any descending chain of submodules is, after discarding initial copies of $M$, a chain $M_{n_1} \supseteq M_{n_2} \supseteq \cdots$ with $n_1 \geq n_2 \geq \cdots \geq 0$; a non-increasing sequence of non-negative integers is eventually constant, so the chain stabilises. $\blacksquare$

---

# Key Takeaways

**To prove Artinian you must control *all* submodules, not just one chain — and a totally-ordered submodule lattice makes this automatic.** Disproving a chain condition needs a single witnessing chain (operation 4), but *proving* one is a universal statement over every chain, which you cannot establish by examples. The clean way to prove DCC (or ACC) is to classify the submodule lattice and show its order type forbids infinite descent (or ascent). Here the lattice is a single chain $0 \subsetneq M_1 \subsetneq \cdots \subsetneq M$ indexed by $\mathbb{N} \cup \{\infty\}$, so DCC reduces to "$\mathbb{N}$ is well-ordered" — there is no infinite strictly decreasing sequence of natural numbers. Whenever you face an Artinian (or Noetherian) claim about a specific module, the first move should be "what is the submodule lattice, and what is its order type?", because the chain conditions are *purely* order-theoretic facts about that lattice.

**The Prüfer group is the canonical Artinian-not-Noetherian module, and its mechanism is "divisible torsion with one new generator per level".** The reason $\mathbb{Z}(2^\infty) = \mathbb{Z}[\tfrac12]/\mathbb{Z}$ separates the two conditions is structural: it is built by *adding* a generator $g_{n+1}$ at each level with $2g_{n+1} = g_n$, so it grows upward forever (no top, hence no Noetherian) but each level is finite and the levels are well-ordered downward (hence Artinian). This is the exact mirror of $\mathbb{Z}$, which shrinks downward forever ($n\mathbb{Z} \supsetneq 2n\mathbb{Z} \supsetneq \cdots$, no Artinian) but is Noetherian. Recognising "divisible torsion $p$-group" should immediately trigger "Artinian, not Noetherian", just as "free of infinite rank" triggers "neither". The dual pair $\mathbb{Z}$ / $\mathbb{Z}(2^\infty)$ is worth memorising as the two witnesses that the chain conditions are independent.

**Odd numerators are units mod $2^n$ — this is why one element of order $2^n$ drags in the whole cyclic piece $M_n$.** The crux of the classification (Step 2) is that an element of order $2^n$ is $\tfrac{a}{2^n}$ with $a$ *odd*, and odd $a$ is invertible modulo $2^n$, so scaling recovers the generator $\tfrac{1}{2^n}$. This "a single element of full order generates its level" phenomenon is general for cyclic modules over a local ring or a $\mathbb{Z}/p^k$: the elements of maximal order are exactly the generators, because the non-units are precisely the elements of lower order. The transferable diagnostic: in a $p$-group or a cyclic $p^k$-module, *order equals generating power* — finding one element of a given order pins down the entire subgroup it generates, which is what collapses the classification of submodules to a single chain.
