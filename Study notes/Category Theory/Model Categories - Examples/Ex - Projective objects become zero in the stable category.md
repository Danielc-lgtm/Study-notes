---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Stable Module Category over a Frobenius Ring"
  - "Def - Projective Module"
  - "Def - Module"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $R$ be a Frobenius ring. Prove that a [[Def - Module|module]] $P$ is isomorphic to the zero object $0$ in the [[Def - Stable Module Category over a Frobenius Ring|stable module category]] $\underline{\mathbf{Mod}}_R$ **if and only if** $P$ is [[Def - Projective Module|projective]]. Conclude that the stable category collapses exactly the projective ("free") part of representation theory while retaining everything else.

**Recall:**

In $\underline{\mathbf{Mod}}_R$, the morphisms are $\underline{\operatorname{Hom}}(M, N) = \operatorname{Hom}(M, N)/\operatorname{PHom}(M, N)$, where $\operatorname{PHom}$ is the maps factoring through a [[Def - Projective Module|projective]]. An object $X$ is **isomorphic to $0$** in a category iff $\mathrm{id}_X = 0$ in $\operatorname{End}(X)$ (equivalently $\underline{\operatorname{Hom}}(X, X) = 0$, equivalently $X$ is a zero object). A module $P$ is projective iff $\mathrm{Hom}(P, -)$ is exact, iff every surjection onto $P$ splits, iff $P$ is a direct summand of a free module. See [[Def - Stable Module Category over a Frobenius Ring]].

---

# Convergent Strategy

**Problem class:** This is a "characterise the zero objects of a quotient category" problem. The routine is to translate "$P \cong 0$ in $\underline{\mathbf{Mod}}_R$" into "$\mathrm{id}_P \in \operatorname{PHom}(P,P)$" and recognise the latter as a characterisation of projectivity.

**Assumption pattern:** The recognisable structure is "object is zero in a morphism-ideal quotient", which always means "the identity lies in the ideal". The assumption that unlocks the result is the characterisation of projectives by the splitting / lifting property: $\mathrm{id}_P$ factors through a projective exactly when $P$ is a retract of a projective, which (projectives being closed under retracts) means $P$ is projective.

**Theorem routing:** The route is the chain of equivalences: $P \cong 0$ in $\underline{\mathbf{Mod}}_R$ $\iff$ $\mathrm{id}_P \in \operatorname{PHom}(P,P)$ $\iff$ $\mathrm{id}_P$ factors through a projective $\iff$ $P$ is a retract of a projective $\iff$ $P$ is projective (retracts of projectives are projective).

**Key decision point:** The non-obvious step is recognising that "$\mathrm{id}_P$ factors through a projective $Q$" means "$P$ is a *retract* of $Q$" — the factorization $P \xrightarrow{\alpha} Q \xrightarrow{\beta} P$ with $\beta\alpha = \mathrm{id}_P$ is exactly a retract diagram. Then one uses that a retract (direct summand) of a projective is projective. Seeing the factorization-of-the-identity as a retract is the move that converts the categorical condition into the module-theoretic one.

---

# Legal Operations Used

1. **Operation 7 from the topic page (quotient out maps through projectives).** Used to translate "$P \cong 0$" into "$\mathrm{id}_P$ factors through a projective".

---

# Hints

> [!note]- Hint 1
> When is an object $X$ a zero object in *any* category? Translate this to a condition on $\mathrm{id}_X$ in the endomorphism group, then apply it in $\underline{\mathbf{Mod}}_R$ where $\underline{\operatorname{Hom}}(P,P) = \operatorname{Hom}(P,P)/\operatorname{PHom}(P,P)$.

> [!note]- Hint 2
> "$\mathrm{id}_P$ factors through a projective $Q$" means there are $\alpha : P \to Q$, $\beta : Q \to P$ with $\beta\alpha = \mathrm{id}_P$. What does such a pair say about the relationship between $P$ and $Q$?

> [!note]- Hint 3
> $\beta\alpha = \mathrm{id}_P$ exhibits $P$ as a *retract* (direct summand) of $Q$. Use that a direct summand of a projective module is projective for the forward direction; for the converse, $P$ projective factors $\mathrm{id}_P$ through $P$ itself.

---

# Solution

The argument is a chain of equivalences. "$P$ is zero in $\underline{\mathbf{Mod}}_R$" unwinds to "$\mathrm{id}_P$ factors through a projective", which exhibits $P$ as a retract of a projective, which (projectives being retract-closed) means $P$ is projective. The converse is immediate.

**Step 1: $P \cong 0$ in $\underline{\mathbf{Mod}}_R$ $\iff$ $\mathrm{id}_P \in \operatorname{PHom}(P,P)$.**

> [!note]- Derivation
> In any additive category, an object $P$ is isomorphic to the zero object if and only if its identity morphism is the zero morphism, $\mathrm{id}_P = 0$ in $\operatorname{End}(P)$. (If $\mathrm{id}_P = 0$ then for any $f : X \to P$, $f = \mathrm{id}_P \circ f = 0$, and dually, so $P$ is both initial and terminal, a zero object; conversely a zero object has $\mathrm{id} = 0$.)
>
> In $\underline{\mathbf{Mod}}_R$, the identity of $P$ is the class $[\mathrm{id}_P] \in \underline{\operatorname{Hom}}(P,P) = \operatorname{Hom}(P,P)/\operatorname{PHom}(P,P)$. So $[\mathrm{id}_P] = 0$ if and only if $\mathrm{id}_P \in \operatorname{PHom}(P,P)$, i.e. $\mathrm{id}_P$ factors through a [[Def - Projective Module|projective]] module. Thus $P \cong 0$ in $\underline{\mathbf{Mod}}_R$ $\iff$ $\mathrm{id}_P$ factors through a projective.

**Step 2: $\mathrm{id}_P$ factors through a projective $\iff$ $P$ is projective.**

> [!note]- Derivation
> ($\Rightarrow$) Suppose $\mathrm{id}_P = \beta\alpha$ with $\alpha : P \to Q$, $\beta : Q \to P$, $Q$ projective. Then $\beta\alpha = \mathrm{id}_P$ exhibits $P$ as a **retract** of $Q$: the map $e = \alpha\beta : Q \to Q$ is an idempotent ($e^2 = \alpha(\beta\alpha)\beta = \alpha\beta = e$) whose image is a direct summand of $Q$ isomorphic to $P$. So $P$ is a direct summand of the projective $Q$. A direct summand of a projective module is projective (if $Q = P \oplus P'$ is a summand of a free module, so is $P$). Hence $P$ is projective.
>
> ($\Leftarrow$) Conversely, if $P$ is projective, then $\mathrm{id}_P$ factors as $P \xrightarrow{\mathrm{id}} P \xrightarrow{\mathrm{id}} P$ through the projective $P$ itself, so $\mathrm{id}_P \in \operatorname{PHom}(P,P)$, and by Step 1 $P \cong 0$ in $\underline{\mathbf{Mod}}_R$.

**Step 3: interpretation.**

> [!note]- Derivation
> Combining: $P \cong 0$ in $\underline{\mathbf{Mod}}_R$ exactly when $P$ is projective. So the stable category sends every projective module to zero and is *insensitive* to projective summands: $M \cong M \oplus P$ in $\underline{\mathbf{Mod}}_R$ for any projective $P$ (since $P \cong 0$). In modular representation theory the projective (= injective) modules are the "free part" carrying no cohomological information; the stable category discards precisely this part and retains the genuinely modular structure. This is why Tate cohomology and support-variety theory live in $\underline{\mathbf{Mod}}_R$ — they are the invariants that survive the collapse.

> [!note]- Complete formal solution
> In an additive category $P \cong 0$ iff $\mathrm{id}_P = 0$. In $\underline{\mathbf{Mod}}_R$ this means $\mathrm{id}_P \in \operatorname{PHom}(P,P)$, i.e. $\mathrm{id}_P = \beta\alpha$ through a projective $Q$. Such a factorization makes $P$ a retract (direct summand) of $Q$ via the idempotent $\alpha\beta$, and a direct summand of a projective is projective; so $P$ is projective. Conversely a projective $P$ has $\mathrm{id}_P$ factoring through $P$ itself, so $\mathrm{id}_P \in \operatorname{PHom}$ and $P \cong 0$. Hence $P \cong 0$ in $\underline{\mathbf{Mod}}_R$ iff $P$ is projective; the stable category collapses exactly the projective modules. $\blacksquare$

---

# Key Takeaways

**An object is zero in a morphism-ideal quotient exactly when its identity lies in the ideal — this is the universal test.** The single reusable fact is that "$X \cong 0$ in $\mathcal{C}/\mathcal{I}$" unwinds to "$\mathrm{id}_X \in \mathcal{I}(X,X)$". This holds in every quotient by a two-sided ideal of morphisms: in the homotopy category an object is zero iff its identity is null-homotopic (iff the object is weakly contractible), in the Calkin algebra an operator's image is zero iff the identity is compact (iff the space is finite-dimensional). The trigger is "which objects become zero in this quotient?"; the reaction is "those whose identity lies in the killed ideal". Applying it here turns the question into "when does $\mathrm{id}_P$ factor through a projective?", which is a concrete module computation.

**Factoring the identity through an object means being a retract of it.** The pivotal recognition — $\mathrm{id}_P = \beta\alpha$ exhibits $P$ as a direct summand of $Q$ via the idempotent $\alpha\beta$ — is a tool that recurs throughout algebra and category theory. Whenever you see a factorization of an identity morphism, read "retract": the source is a retract of the intermediate object. Combined with a closure property of the intermediate class (here, retracts of projectives are projective), this converts "identity factors through class $\mathcal{T}$" into "object lies in $\mathcal{T}$". The diagnostic: identity-factorizations are retract witnesses, and idempotents are the algebraic shadow of retracts (the Karoubi/idempotent-completion machinery formalises this).

**The stable category is "representation theory modulo the free part", and knowing what becomes zero tells you what the theory sees.** The conceptual payoff is that $\underline{\mathbf{Mod}}_R$ is engineered to forget exactly the projective (= injective, by Frobenius) modules, which carry no modular information, and to retain everything else. This is why the stable category is the right home for Tate cohomology and support varieties: those invariants are precisely the ones invisible to projective summands. The transferable principle: when a quotient category is built to study some phenomenon, identifying its zero objects tells you what the construction deliberately ignores, and hence what the surviving invariants can and cannot detect. Here the zero objects are the projectives, so the stable category is blind to the free part and sharp on the rest — the design intent made precise.
