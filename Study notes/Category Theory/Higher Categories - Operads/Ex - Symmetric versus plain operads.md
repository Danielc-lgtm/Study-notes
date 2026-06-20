---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Operad"
  - "Def - Algebra for an Operad"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

A **plain (non-symmetric) operad** is the data of an [[Def - Operad|operad]] *minus* the $S_n$-action and the equivariance axiom. There is a forgetful functor $U$ from symmetric operads to plain operads (forget the action) and a free functor $\mathrm{Sym}$ in the other direction.

(a) Describe $\mathrm{Sym}$ explicitly: given a plain operad $Q$, build the symmetric operad $\mathrm{Sym}(Q)$ with $\mathrm{Sym}(Q)(n) = Q(n) \times S_n$, and verify it is a symmetric operad. (This is the "$S_n$-induction" or "symmetrisation".)

(b) Prove that an algebra over the plain operad $Q$ is the same as an algebra over the symmetric operad $\mathrm{Sym}(Q)$ — that is, plain-operad algebras and their symmetrisation's algebras coincide. Conclude that the non-symmetric associative operad $\mathrm{Assoc}^{\mathrm{ns}}$ (with $\mathrm{Assoc}^{\mathrm{ns}}(n) = \{*\}$) symmetrises to the symmetric associative operad $\mathrm{Assoc}$ (with $\mathrm{Assoc}(n) = S_n$).

(c) Give an example showing that the symmetric commutative operad $\mathrm{Comm}$ ($\mathrm{Comm}(n) = \{*\}$) is **not** $\mathrm{Sym}(Q)$ for any plain operad $Q$, i.e. not every symmetric operad is a symmetrised plain one.

**Recall:**

![[Def - Operad#The Definition]]

A plain operad $Q$ has operation sets $Q(n)$, a unit $\mathrm{id} \in Q(1)$, and composition $\gamma$, satisfying associativity and unit laws but *no* symmetric structure. Its algebras have structure maps $Q(n) \times X^n \to X$ with *no* equivariance condition. The inputs are genuinely ordered.

---

# Convergent Strategy

**Problem class:** This is an *adjunction-between-two-flavours* problem: compare plain and symmetric operads through a free–forgetful adjunction and track what it does to algebras. The recurring method is to construct the free functor explicitly and verify it computes the right thing on algebras by chasing the structure maps.

**Assumption pattern:** The signal is "operations with ordered inputs versus operations with permutable inputs". A plain operad's operations come in a fixed order; symmetrising freely *adds* a copy of each operation for every reordering, which is exactly $Q(n) \times S_n$. The recognisable pattern in (c) is "an operad whose $S_n$-action is non-free" — symmetrised operads always have free $S_n$-action (the action is on the $S_n$-factor by right multiplication), so any operad with a fixed point under the action cannot be a symmetrisation.

**Theorem routing:** Part (a) routes through direct verification of the operad axioms for $Q(n) \times S_n$ with the regular $S_n$-action. Part (b) routes through the adjunction $\mathrm{Sym} \dashv U$ and the observation that an algebra is a map to the endomorphism operad: $\mathrm{Sym}(Q) \to \mathrm{End}_X$ corresponds to $Q \to U(\mathrm{End}_X)$, and $U(\mathrm{End}_X)$ is the plain endomorphism operad, so $\mathrm{Sym}(Q)$-algebras = $Q$-algebras. Part (c) routes through the *freeness of the action* on any symmetrisation versus the *triviality* of $\mathrm{Comm}$'s action.

**Key decision point:** The crux of (c) is recognising the invariant that distinguishes symmetrised operads: their $S_n$-action is *free*. The temptation is to try to construct a $Q$ by setting $Q(n) = \mathrm{Comm}(n)/S_n = \{*\}$ and hope $\mathrm{Sym}(\{*\}_n) = \mathrm{Comm}$ — but $\mathrm{Sym}(\{*\})(n) = \{*\} \times S_n = S_n = \mathrm{Assoc}(n) \neq \mathrm{Comm}(n)$. The decision is to test against the free-action invariant rather than to guess a preimage.

---

# Legal Operations Used

1. **Build the free symmetric operad on a plain one (operation 6 from the topic page).** We form $\mathrm{Sym}(Q)(n) = Q(n) \times S_n$ with the regular action.

2. **Pass algebra structures across an adjunction (operation 4 from the topic page).** We use $\mathrm{Sym} \dashv U$ to transport algebra structures between plain and symmetric operads.

3. **Detect non-representability via an invariant (operation 6, contrapositive, from the topic page).** We use freeness of the $S_n$-action as an invariant ruling out a preimage under $\mathrm{Sym}$.

---

# Hints

> [!note]- Hint 1
> $\mathrm{Sym}(Q)(n) = Q(n) \times S_n$. Let $S_n$ act by right multiplication on the second factor: $(q, \pi) \cdot \sigma = (q, \pi\sigma)$. The composition combines $Q$'s composition with the block-permutation calculus of the symmetric groups (as in the associative operad).

> [!note]- Hint 2
> For (b): an algebra over $\mathrm{Sym}(Q)$ assigns to $(q, \pi) \in Q(n) \times S_n$ an operation; equivariance forces the value on $(q, \pi)$ to be determined by the value on $(q, e)$ permuted by $\pi$. So the algebra is determined by the maps $Q(n) \times X^n \to X$, $q \mapsto \rho(q, e)$ — exactly a $Q$-algebra structure.

> [!note]- Hint 3
> For (c): what is the $S_n$-action on $\mathrm{Sym}(Q)(n) = Q(n) \times S_n$? Right multiplication on $S_n$ is *free*. Is the $S_n$-action on $\mathrm{Comm}(n) = \{*\}$ free for $n \geq 2$?

> [!note]- Hint 4
> A free $S_n$-action on a finite set forces the set to have size divisible by $n!$. $\mathrm{Comm}(n) = \{*\}$ has size $1$, not divisible by $n!$ for $n \geq 2$. Hence $\mathrm{Comm}(n)$ cannot be $Q(n) \times S_n$ for any $Q$.

---

# Solution

The plan: construct and verify $\mathrm{Sym}(Q)$ (Step 1); prove the algebra-equivalence via the adjunction and equivariance (Step 2); identify $\mathrm{Sym}(\mathrm{Assoc}^{\mathrm{ns}}) = \mathrm{Assoc}$ (Step 3); and rule out $\mathrm{Comm}$ as a symmetrisation by the free-action invariant (Step 4).

**Step 1: $\mathrm{Sym}(Q)$ is a symmetric operad.**

> [!note]- Derivation
> Set $\mathrm{Sym}(Q)(n) = Q(n) \times S_n$ with right $S_n$-action $(q, \pi)\cdot\sigma = (q, \pi\sigma)$, unit $(\mathrm{id}_Q, e) \in Q(1) \times S_1$. Composition: for $(q, \pi) \in Q(k)\times S_k$ and $(q_i, \pi_i) \in Q(n_i) \times S_{n_i}$, set
> $$\gamma\big((q,\pi); (q_1,\pi_1), \dots, (q_k,\pi_k)\big) = \big(\gamma_Q(q; q_{\pi^{-1}(1)}, \dots, q_{\pi^{-1}(k)}),\ \pi\langle n_\bullet\rangle \cdot (\pi_1 \oplus \dots \oplus \pi_k)\big),$$
> combining $Q$'s composition on the first factor (with blocks reordered by $\pi$) and the block-permutation calculus on the second. Associativity and unit follow from those of $Q$ and of the symmetric-group composition (as for $\mathrm{Assoc}$); equivariance holds because the second factor carries the regular action by construction. So $\mathrm{Sym}(Q)$ is a symmetric operad, and $\mathrm{Sym} \dashv U$ (a symmetric operad map $\mathrm{Sym}(Q) \to P$ is a plain operad map $Q \to U(P)$, extending by equivariance).

**Step 2: Algebras coincide.**

> [!note]- Derivation
> A $\mathrm{Sym}(Q)$-algebra on $X$ is a symmetric operad map $\mathrm{Sym}(Q) \to \mathrm{End}_X$. By the adjunction $\mathrm{Sym} \dashv U$, this is the same as a plain operad map $Q \to U(\mathrm{End}_X)$, where $U(\mathrm{End}_X)$ is the plain endomorphism operad (forget the $S_n$-action). A plain operad map $Q \to U(\mathrm{End}_X)$ is exactly a $Q$-algebra structure on $X$. Hence $\mathrm{Alg}_{\mathrm{Sym}(Q)} \cong \mathrm{Alg}_Q$. Concretely: a $\mathrm{Sym}(Q)$-algebra map $\rho$ is determined by $\rho(q, e)$ for $q \in Q(n)$, since equivariance forces $\rho(q, \pi)(x_\bullet) = \rho(q, e)(x_{\pi(\bullet)})$; and the family $q \mapsto \rho(q, e)$ is precisely a $Q$-algebra structure.

**Step 3: $\mathrm{Sym}(\mathrm{Assoc}^{\mathrm{ns}}) = \mathrm{Assoc}$.**

> [!note]- Derivation
> The non-symmetric associative operad has $\mathrm{Assoc}^{\mathrm{ns}}(n) = \{*\}$ (one ordered $n$-ary product). Then $\mathrm{Sym}(\mathrm{Assoc}^{\mathrm{ns}})(n) = \{*\} \times S_n \cong S_n = \mathrm{Assoc}(n)$, with the regular action — exactly the symmetric associative operad. By Step 2, $\mathrm{Assoc}$-algebras = $\mathrm{Assoc}^{\mathrm{ns}}$-algebras = [[Def - Monoid in a Monoidal Category|monoids]], consistent with the previous exercise: monoids can be described either by the plain operad (one $n$-ary product, inputs in their given order) or by its symmetrisation (an ordering of the inputs in each arity).

**Step 4: $\mathrm{Comm}$ is not a symmetrisation.**

> [!note]- Derivation
> For any plain operad $Q$, the $S_n$-action on $\mathrm{Sym}(Q)(n) = Q(n) \times S_n$ is right multiplication on the $S_n$-factor, which is **free**: $(q,\pi)\cdot\sigma = (q,\pi)$ forces $\pi\sigma = \pi$, hence $\sigma = e$. A free action of a group $G$ on a set partitions it into orbits each of size $|G|$, so $|\mathrm{Sym}(Q)(n)|$ is a multiple of $|S_n| = n!$ (when $Q(n)$ is finite; more generally $\mathrm{Sym}(Q)(n)$ is a free $S_n$-set). But $\mathrm{Comm}(n) = \{*\}$ has the *trivial* $S_n$-action, which for $n \geq 2$ is not free ($* \cdot \sigma = *$ for all $\sigma$). A single point cannot be a free $S_n$-set for $n \geq 2$ (its size $1$ is not a multiple of $n! \geq 2$). Therefore $\mathrm{Comm}(n) \not\cong Q(n) \times S_n$ for any $Q$, and $\mathrm{Comm}$ is not the symmetrisation of any plain operad. Operadically: commutativity is a genuinely symmetric phenomenon, invisible to plain operads, because forgetting the order destroys exactly the structure that distinguishes $\mathrm{Comm}$ from $\mathrm{Assoc}$.

> [!note]- Complete formal solution
> *(a)* $\mathrm{Sym}(Q)(n) = Q(n)\times S_n$, regular action $(q,\pi)\cdot\sigma=(q,\pi\sigma)$, unit $(\mathrm{id},e)$, composition combining $\gamma_Q$ with block permutations. Axioms inherited from $Q$ and the symmetric groups; equivariance from the regular action. This is left adjoint to $U$.
>
> *(b)* By $\mathrm{Sym}\dashv U$ and the endomorphism-operad description of algebras, $\mathrm{Alg}_{\mathrm{Sym}(Q)} \cong \mathrm{Alg}_Q$; explicitly a $\mathrm{Sym}(Q)$-algebra is determined by $q\mapsto\rho(q,e)$, a $Q$-algebra. In particular $\mathrm{Sym}(\mathrm{Assoc}^{\mathrm{ns}}) = \mathrm{Assoc}$ and both have monoids as algebras.
>
> *(c)* Any $\mathrm{Sym}(Q)(n)$ is a free $S_n$-set; $\mathrm{Comm}(n) = \{*\}$ is not free for $n\ge 2$. Hence $\mathrm{Comm} \neq \mathrm{Sym}(Q)$ for any plain $Q$. $\blacksquare$

---

# Key Takeaways

**Plain operads order their inputs; symmetric operads permute them, and symmetrisation freely adds the permutations.** The structural lesson is that the symmetrisation $\mathrm{Sym}(Q)(n) = Q(n) \times S_n$ does exactly one thing: it attaches a free copy of $S_n$ so the inputs become permutable. This is why $\mathrm{Sym}$ is *free* — it imposes no relations, just adds the orderings. The diagnostic to carry: when you see an operad-like structure on ordered data (lists, sequences, planar trees, words), it is probably a plain operad, and its symmetrisation governs the same algebras but now with permutable inputs. Plain operads are the right tool whenever order is intrinsic — non-commutative power series, planar algebras, the $A_\infty$ structure on a single ordered sequence of operations.

**Free actions are an invariant; use them to detect non-freeness.** The slick part of (c) is recognising that "is a symmetrisation" is detected by "the $S_n$-action is free", and that freeness is a checkable invariant (orbit sizes divide $n!$). This is a widely reusable move: to show an object is *not* free/induced/representable, find an invariant that all free objects share and that the target violates. Here a single fixed point under the action is the obstruction. The same reasoning shows the commutative operad cannot be cofibrant in the naive (non-equivariant) sense, which is precisely why the homotopy theory of commutative versus $E_\infty$ algebras is subtle — the trivial $S_n$-action on $\mathrm{Comm}(n)$ is the source of all the difficulty.

**Symmetric structure is where commutativity is born and cannot be faked.** The deepest takeaway is that commutativity is irreducibly a symmetric-operad phenomenon: there is no plain operad whose symmetrisation is $\mathrm{Comm}$, because plain operads have no notion of "input order does not matter" — they only have "input order is fixed". This is the operadic explanation of why commutative algebra behaves so differently from associative algebra, and why the little-disks operads $E_n$ (which interpolate toward $\mathrm{Comm}$ as $n \to \infty$) require genuinely symmetric — and increasingly highly-connected — spaces of operations. Forgetting symmetry collapses the entire spectrum from associative to commutative down to the single associative point.
