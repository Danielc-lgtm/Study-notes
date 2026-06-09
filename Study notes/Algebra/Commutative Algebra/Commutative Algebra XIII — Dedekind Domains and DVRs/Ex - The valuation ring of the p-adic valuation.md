---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Discrete Valuation and Valuation Ring"
  - "Def - Local Ring and Residue Field"
  - "Def - Prime and Maximal Ideal"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Investigate how much a discrete valuation is determined by its valuation ring. Specifically (ES4 Q17(b)):

1. **The valuation ring determines the valuation.** If $v_1$ and $v_2$ are [[Def - Discrete Valuation and Valuation Ring|discrete valuations]] on a single field $K$ whose valuation rings are *equal*, $A_{v_1} = A_{v_2}$, prove that $v_1 = v_2$.
2. **Isomorphic valuation rings need not give isomorphic fields.** Decide whether the following is true: if $v_1, v_2$ are discrete valuations on fields $K_1, K_2$ with $A_{v_1} \cong A_{v_2}$ as rings, then $K_1 \cong K_2$. Prove or give a counterexample.

Use the $p$-adic valuation $v_p$ on $\mathbb{Q}$, with valuation ring $\mathbb{Z}_{(p)}$, as the running example.

**Recall:**

![[Def - Discrete Valuation and Valuation Ring#The Definition]]

For a discrete valuation $v$ on $K$ with valuation ring $A = A_v$ and uniformizer $\pi$ (an element with $v(\pi) = 1$), every nonzero $x \in K$ is uniquely $u\pi^{v(x)}$ with $u \in A^\times$, and the nonzero ideals of $A$ are $(\pi^n) = \{x \in A : v(x) \geq n\}$. The units are $A^\times = \{x : v(x) = 0\}$, the maximal ideal is $\mathfrak{m} = \{x : v(x) \geq 1\}$.

The model is $v_p$ on $\mathbb{Q}$ with $A_{v_p} = \mathbb{Z}_{(p)}$, uniformizer $p$, and residue field $\mathbb{F}_p$ (see [[Ex - Z localized at p is a DVR]]).

---

# Convergent Strategy

**Problem class.** This is a pair of *is-the-data-redundant* questions: part 1 asks whether the valuation $v$ is extra data beyond the ring $A_v$ (it is not), and part 2 asks whether the ring remembers the field (it does not). As the [[Commutative Algebra XIII — Dedekind Domains and DVRs#Legal Operations|topic's illegal-operation 4]] flags, treating the valuation as extra data is a tempting error — this exercise proves it is recoverable from the ideal structure alone.

**Assumption pattern.** For part 1 the key fact is that the valuation is *read off the ideals*: $v(x) = n \iff (x) = \mathfrak{m}^n$, and $\mathfrak{m}$ is determined by $A$ (its unique maximal ideal). So equal rings have equal maximal ideals, equal powers, hence equal valuations. For part 2 the relevant fact is that $\operatorname{Frac}(A_v) = K$, so the field is recovered as the fraction field of the ring — *but only as the fraction field of that specific ring*, and an abstract ring isomorphism $A_{v_1} \cong A_{v_2}$ induces $\operatorname{Frac}(A_{v_1}) \cong \operatorname{Frac}(A_{v_2})$, which would seem to force $K_1 \cong K_2$. The trap is that this *does* hold — so part 2 must be answered by recognizing the statement is actually **true**, not by hunting a counterexample.

**Theorem routing.** Part 1 routes through "$v$ is intrinsic to $A_v$": the units are $\{v = 0\}$, the maximal ideal is $\{v \geq 1\}$, and $v(x) = $ the unique $n$ with $(x) = \mathfrak{m}^n$ — all phrased in $A_v$ without mentioning $v$. Part 2 routes through "$K = \operatorname{Frac}(A_v)$" and functoriality of the fraction field under ring isomorphism.

**Key decision point.** The genuine subtlety is in part 2: one is *invited* to find a counterexample, and the discipline is to first check whether the statement might be true. It is: $A_{v_1} \cong A_{v_2}$ as rings forces $\operatorname{Frac}(A_{v_1}) \cong \operatorname{Frac}(A_{v_2})$ (the fraction field is a functor of the domain), and since $K_i = \operatorname{Frac}(A_{v_i})$, we get $K_1 \cong K_2$. The non-obvious decision is to resist the framing's bait and prove the implication rather than search for a (nonexistent) counterexample. (The contrast with part 1 is instructive: the *field* is determined, even though distinct valuations on the *same* field can have different — but never equal — valuation rings.)

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra XIII — Dedekind Domains and DVRs#Legal Operations|the topic page's Legal Operations]]:

1. **Read off valuation arithmetic (operation 1).** The valuation is recovered from the ideal structure: $v(x) = n \iff (x) = \mathfrak{m}^n$, with $\mathfrak{m}$ the maximal ideal of $A_v$.

2. **Recognize the valuation is intrinsic (illegal-but-tempting 4).** The exercise turns the warning "the valuation is not extra data" into a proof: $v$ is a function of $A_v$ alone.

---

# Hints

> [!note]- Hint 1
> For part 1, the valuation ring $A_v$ knows its own maximal ideal $\mathfrak{m}$ (it is local). And every nonzero element $x$ generates an ideal $(x)$ that is some power $\mathfrak{m}^n$. Can you read $v(x)$ off the equation $(x) = \mathfrak{m}^n$?

> [!note]- Hint 2
> $v(x) = n$ exactly when $(x) = \mathfrak{m}^n$ as ideals of $A_v$. Since $A_{v_1} = A_{v_2}$ as rings, they have the *same* maximal ideal $\mathfrak{m}$ and the same powers $\mathfrak{m}^n$, so the same value of $n$ for each $x$. Hence $v_1(x) = v_2(x)$ for all $x \in A_v$; extend to $K$ multiplicatively.

> [!note]- Hint 3
> For part 2, do not rush to find a counterexample. Note $K_i = \operatorname{Frac}(A_{v_i})$. What does a ring isomorphism $A_{v_1} \cong A_{v_2}$ do to fraction fields?

> [!note]- Hint 4
> A ring isomorphism of domains induces an isomorphism of their fraction fields (the fraction field is functorial). So $A_{v_1} \cong A_{v_2}$ forces $\operatorname{Frac}(A_{v_1}) \cong \operatorname{Frac}(A_{v_2})$, i.e. $K_1 \cong K_2$. The statement in part 2 is **true**; the framing's invitation to disprove it is a red herring.

---

# Solution

Part 1 shows the valuation is intrinsic: it is read off the ideal structure of $A_v$, which equal rings share. Part 2 shows the field is intrinsic too: it is the fraction field of $A_v$, and ring isomorphisms carry fraction fields along — so the statement is true, despite the framing inviting a counterexample.

**Step 1 (Part 1): the valuation is determined by the ring.**

If $A_{v_1} = A_{v_2}$ (equal as subrings of $K$), then $v_1 = v_2$.

> [!note]- Derivation
> Write $A = A_{v_1} = A_{v_2}$. As a valuation ring, $A$ is local with a unique maximal ideal $\mathfrak{m}$; since $\mathfrak{m}$ is the set of non-units of $A$, it is determined by $A$ alone, so $v_1$ and $v_2$ have the *same* maximal ideal $\mathfrak{m}$.
>
> Now recover the valuation from the ideals. For $v = v_i$ with uniformizer $\pi_i$, every nonzero $x \in A$ satisfies $(x) = (\pi_i^{\,v_i(x)}) = \mathfrak{m}^{v_i(x)}$ — the principal ideal generated by $x$ is the power of $\mathfrak{m}$ matching the valuation. So
> $$v_i(x) = \text{the unique } n \geq 0 \text{ with } (x) = \mathfrak{m}^n,$$
> a description using only $A$ and $\mathfrak{m}$, *not* the valuation. Since $A$ and $\mathfrak{m}$ are the same for $i = 1, 2$, and the powers $\mathfrak{m}^n$ form one strictly descending chain (uniquely indexed), the integer $n$ with $(x) = \mathfrak{m}^n$ is the same for both. Hence $v_1(x) = v_2(x)$ for all $x \in A\setminus\{0\}$.
>
> Extend to all of $K^\times$: any $x \in K^\times$ is $a/b$ with $a, b \in A$, and $v_i(x) = v_i(a) - v_i(b)$, equal for $i = 1, 2$ by the above. Therefore $v_1 = v_2$ on $K^\times$, and both send $0 \mapsto \infty$. So $v_1 = v_2$.

**Step 2 (Part 2): isomorphic valuation rings force isomorphic fields — the statement is true.**

If $A_{v_1} \cong A_{v_2}$ as rings, then $K_1 \cong K_2$.

> [!note]- Derivation
> Let $\varphi : A_{v_1} \xrightarrow{\sim} A_{v_2}$ be a ring isomorphism of these two domains. The fraction field is *functorial in injective ring maps of domains*: $\varphi$ extends uniquely to $\operatorname{Frac}(\varphi) : \operatorname{Frac}(A_{v_1}) \to \operatorname{Frac}(A_{v_2})$, $\tfrac ab \mapsto \tfrac{\varphi(a)}{\varphi(b)}$, which is a field isomorphism (its inverse is $\operatorname{Frac}(\varphi^{-1})$).
>
> Now use $K_i = \operatorname{Frac}(A_{v_i})$, which holds because a valuation ring has fraction field equal to the field it lives in. Therefore
> $$K_1 = \operatorname{Frac}(A_{v_1}) \cong \operatorname{Frac}(A_{v_2}) = K_2.$$
> So the implication holds: **isomorphic valuation rings have isomorphic fraction fields, hence isomorphic ambient fields.** The statement in part 2 is *true*, and the invitation to disprove it is a deliberate red herring — the valuation ring remembers the field, even though (as part 1's contrast shows) it also remembers its own valuation.

> [!note]- Sanity check via the $p$-adic example
> Take $v_1 = v_p$ on $K_1 = \mathbb{Q}$ and $v_2 = v_q$ on $K_2 = \mathbb{Q}$ for primes $p \neq q$. The rings $\mathbb{Z}_{(p)}$ and $\mathbb{Z}_{(q)}$ are *isomorphic* (both are DVRs with residue field of different size — actually residue fields $\mathbb{F}_p$, $\mathbb{F}_q$ — so they are NOT isomorphic when $p \neq q$). This is consistent: distinct residue fields obstruct an isomorphism, and indeed the fields $\mathbb{Q} \cong \mathbb{Q}$ are (trivially) isomorphic. For a cleaner illustration of part 1: on $\mathbb{Q}$ the valuations $v_p$ for different $p$ have *different* valuation rings $\mathbb{Z}_{(p)}$, never equal — consistent with "equal rings force equal valuations".

> [!note]- Complete formal solution
> **Part 1.** Let $A = A_{v_1} = A_{v_2}$, a valuation ring, local with unique maximal ideal $\mathfrak{m}$ (the non-units), determined by $A$ alone. For each $i$ and each nonzero $x \in A$, $(x) = \mathfrak{m}^{v_i(x)}$, so $v_i(x)$ is the unique $n$ with $(x) = \mathfrak{m}^n$ — a quantity depending only on $A$ and $\mathfrak{m}$, the same for $i = 1, 2$. Hence $v_1 = v_2$ on $A\setminus\{0\}$, and extending by $v_i(a/b) = v_i(a) - v_i(b)$ gives $v_1 = v_2$ on $K^\times$. So $v_1 = v_2$.
>
> **Part 2.** The statement is **true**. A ring isomorphism $\varphi : A_{v_1} \xrightarrow{\sim} A_{v_2}$ of domains extends to a field isomorphism $\operatorname{Frac}(A_{v_1}) \xrightarrow{\sim} \operatorname{Frac}(A_{v_2})$. Since $K_i = \operatorname{Frac}(A_{v_i})$, we conclude $K_1 \cong K_2$. $\blacksquare$

---

# Key Takeaways

**A discrete valuation is intrinsic to its valuation ring: there is nothing to choose.** The defining-by-a-valuation presentation of a DVR makes it look as if the valuation $v$ is extra structure attached to the ring. Part 1 dispels this once and for all: $v(x)$ is the unique exponent $n$ with $(x) = \mathfrak{m}^n$, a quantity computed from the ideal structure of $A_v$ alone. So two valuations on the same field with the same valuation ring are literally the same function. The transferable principle: **whenever an object is "defined with auxiliary data", check whether the data is recoverable from the object** — for DVRs it always is, which is why one speaks of *the* valuation of a DVR. This is the same phenomenon as a metric being recoverable from its induced topology only sometimes; here the recovery always succeeds because the ideal lattice is totally ordered.

**The fraction field is a functor, so ring isomorphisms transport the ambient field.** Part 2's resolution turns on a structural reflex: $\operatorname{Frac}(-)$ takes isomorphisms of domains to isomorphisms of fields, because the fraction field is the universal field receiving the domain. So any time you know two domains are abstractly isomorphic, their fraction fields are isomorphic for free — there is no need to track the fields separately. The trigger to recognize: when a problem asks whether some derived field is determined, ask whether that field is the fraction field (or another functorial construction) of a ring you already control. Here the field is $\operatorname{Frac}(A_v)$, so it comes along automatically.

**Beware framings that invite a counterexample to a true statement.** This is a meta-lesson about problem-solving discipline. Part 2 is phrased "prove or disprove", and the natural instinct after part 1 (where the data *was* redundant in a surprising way) is to expect a surprising *failure* in part 2 and to hunt for a counterexample. Resisting that pull — pausing to ask "is this maybe just true?" — saves a long fruitless search. The general diagnostic: before searching for a counterexample, spend one line checking whether the obvious structural argument already proves the statement. Here, "$K = \operatorname{Frac}(A_v)$ and Frac is a functor" settles it in a sentence. The residue field $A_v/\mathfrak{m}$, by contrast, is a genuinely finer invariant — $\mathbb{Z}_{(p)}$ and $\mathbb{Z}_{(q)}$ have residue fields $\mathbb{F}_p \not\cong \mathbb{F}_q$ — and it is the obstruction one *would* use to distinguish non-isomorphic valuation rings, a useful companion fact to carry.
