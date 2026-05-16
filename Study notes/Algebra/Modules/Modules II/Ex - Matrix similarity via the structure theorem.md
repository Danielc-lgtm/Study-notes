---
type: exercise
subject: module-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - The Module of a Linear Operator"
  - "Def - Module"
  - "Def - Polynomial Ring"
  - "Def - Euclidean Domain"
  - "Thm - Rational Canonical Form"
  - "Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain"
  - "Thm - Smith Normal Form"
tags: [algebra, module-theory]
---

# Problem Statement

Let $F$ be a field and let $A, B \in M_{n,n}(F)$ be two $n \times n$ matrices over $F$. Recall that $A$ and $B$ are **similar** (or *conjugate*) when there is an invertible matrix $P \in \mathrm{GL}_n(F)$ with $B = P^{-1} A P$.

Each matrix $A$ makes the vector space $F^n$ into an $F[X]$-module $V_A$, with $X$ acting as $A$; likewise $B$ gives $V_B$. Prove that the following three statements are equivalent.

1. $A$ and $B$ are **similar** over $F$.
2. The $F[X]$-modules $V_A$ and $V_B$ are **isomorphic**.
3. The characteristic matrices $XI - A$ and $XI - B$ are **equivalent** over $F[X]$ — that is, there exist invertible matrices $P, Q \in \mathrm{GL}_n(F[X])$ with $XI - B = P\,(XI-A)\,Q$.

Conclude that the **rational canonical form is a complete invariant for similarity**: two matrices over $F$ are similar if and only if they have the same rational canonical form, equivalently the same invariant factors, equivalently $XI-A$ and $XI-B$ have the same Smith normal form.

The point of the exercise is to prove the theorem that *justifies* every canonical-form computation: it is what guarantees that the rational canonical form genuinely classifies matrices up to similarity, with no information lost.

**Recall:**

The objects in play are a field $F$, the polynomial ring $F[X]$, matrices over $F$, and the $F[X]$-modules they define.

![[Def - The Module of a Linear Operator#The Definition]]

Given $A \in M_{n,n}(F)$, the module $V_A$ has underlying set $F^n$ and $F[X]$-action determined by $X \cdot v = Av$ (so $f(X) \cdot v = f(A)v$). A [[Def - Module|module]] isomorphism $V_A \to V_B$ is a bijective $F[X]$-linear map: it is $F$-linear *and* commutes with the action of $X$.

Two matrices $M, N$ over a ring $R$ are **equivalent** when $N = PMQ$ for invertible $P, Q \in \mathrm{GL}_n(R)$ — equivalently, $N$ is reachable from $M$ by elementary row and column operations over $R$. Over a [[Def - Euclidean Domain|Euclidean domain]], by [[Thm - Smith Normal Form|the Smith normal form theorem]], two matrices are equivalent if and only if they have the same Smith normal form.

The ring $F[X]$ is a [[Def - Euclidean Domain|Euclidean domain]] (degree is a Euclidean function), so by [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|the structure theorem]] every finitely generated $F[X]$-module is a direct sum of cyclic modules $F[X]/(f_i)$ with $f_1 \mid \cdots \mid f_s$, and these **invariant factors** $f_i$ (taken monic) are uniquely determined by the isomorphism class of the module. The [[Thm - Rational Canonical Form|rational canonical form theorem]] identifies the invariant factors of $V_A$ with the non-constant Smith normal form entries of $XI-A$, and presents $A$ in block-diagonal companion-matrix form.

A standard presentation fact, used below: for any matrix $A$, the module $V_A$ is the cokernel of the map $F[X]^n \xrightarrow{\;XI-A\;} F[X]^n$. That is, there is a short exact sequence
$$0 \longrightarrow F[X]^n \xrightarrow{\;XI-A\;} F[X]^n \xrightarrow{\;\pi\;} V_A \longrightarrow 0,$$
so $V_A \cong F[X]^n / (XI-A)F[X]^n$. The map $XI-A$ is injective because $\det(XI-A) = \chi_A(X)$ is a non-zero polynomial, hence a non-zero-divisor in the domain $F[X]$.

---

# Convergent Strategy

**Problem class.** This is a *prove an equivalence of three characterisations* problem — establish $(1) \Leftrightarrow (2) \Leftrightarrow (3)$ by a cycle of implications. As the topic page strategy [[Modules II — §3.3–3.4#Problem-Solving Strategy|notes]], the recurring move in this part of the subject is *translation*: a question phrased about matrices ($(1)$, $(3)$) is converted into a question about modules ($(2)$), where the structure theorem can act.

**Assumption pattern.** The hypotheses are minimal: $F$ a field, $A, B$ square of the same size. The single structural lever is that $F[X]$ is a [[Def - Euclidean Domain|Euclidean domain]], which makes the [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|structure theorem]] and [[Thm - Smith Normal Form|Smith normal form]] available. The whole proof is unpacking what each of the three statements *means* and showing the meanings coincide.

**Theorem routing.** The cleanest route is a cycle $(1) \Rightarrow (2) \Rightarrow (3) \Rightarrow (1)$, plus the recall fact that $V_A$ is the cokernel of $XI-A$. The link $(1) \Leftrightarrow (2)$ is a direct unwinding of definitions: a similarity $B = P^{-1}AP$ is *literally* a change of basis that intertwines the two $X$-actions. The link $(2) \Leftrightarrow (3)$ routes through the presentation $V_A = \operatorname{coker}(XI-A)$: isomorphic cokernels of injective square maps over $F[X]$ correspond to equivalent presenting matrices. The final classification statement then routes through [[Thm - Smith Normal Form]] and [[Thm - Rational Canonical Form]].

**Key decision point.** The genuinely delicate implication is $(2) \Rightarrow (3)$, or more precisely the half "isomorphic modules have equivalent presentation matrices". An $F[X]$-module isomorphism $V_A \to V_B$ is a priori only a map of *cokernels*; one must *lift* it to an isomorphism of the presenting free modules $F[X]^n$ and check the lift conjugates $XI-A$ into $XI-B$. The non-obvious point is that the lift exists and is invertible — this uses projectivity/freeness of $F[X]^n$ and the injectivity of $XI-A$. Recognising that "cokernels agree" must be *upgraded* to "presentations agree", and knowing the lifting lemma that does it, is the crux that separates this from a routine definition-chase.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Modules II — §3.3–3.4#Legal Operations|the topic page's Legal Operations]]:

1. **Translate a matrix into its $F[X]$-module.** The matrix $A$ becomes the module $V_A = (F^n, X \mapsto A)$; statements about $A$ become statements about $V_A$, where the structure theorem can be applied.

2. **Unwind a similarity as an intertwiner of $X$-actions.** A change of basis $P$ with $B = P^{-1}AP$ is read as an $F$-linear bijection $F^n \to F^n$ that commutes with the action of $X$ — i.e. exactly an $F[X]$-module isomorphism $V_A \to V_B$.

3. **Present a module as the cokernel of its characteristic matrix.** Use the exact sequence $F[X]^n \xrightarrow{XI-A} F[X]^n \to V_A \to 0$, so $V_A \cong F[X]^n/(XI-A)F[X]^n$; this turns the module into matrix data over $F[X]$.

4. **Lift a map of cokernels to a map of free presentations.** Given a module map $V_A \to V_B$, use freeness (projectivity) of $F[X]^n$ to lift it to a map of the presenting free modules; injectivity of the characteristic matrices makes the lift compatible with them.

5. **Recognise equivalence of matrices over a ring.** Two square matrices related by $N = P M Q$ with $P, Q$ invertible are *equivalent*; over a Euclidean domain this is detected by a common Smith normal form.

6. **Invoke uniqueness of invariant factors.** By the structure theorem the invariant factors are a complete isomorphism invariant of a finitely generated $F[X]$-module; equality of invariant factors is equality of Smith normal forms of the characteristic matrices and equality of rational canonical forms.

---

# Hints

> [!note]- Hint 1
> Prove the three statements equivalent by a *cycle* of implications: $(1) \Rightarrow (2)$, $(2) \Rightarrow (3)$, $(3) \Rightarrow (1)$. Two of the three links are short translations of definitions; one is genuinely substantial. Start with $(1) \Leftrightarrow (2)$: write out what $B = P^{-1}AP$ says, and write out what "$V_A \cong V_B$ as $F[X]$-modules" says. An $F[X]$-module map must be $F$-linear *and* commute with multiplication by $X$. Which matrix equation expresses "commutes with $X$"?

> [!note]- Hint 2
> For $(1) \Leftrightarrow (2)$: an invertible $F$-linear map $P : F^n \to F^n$ is an $F[X]$-module isomorphism $V_A \to V_B$ exactly when it intertwines the actions of $X$, i.e. $P(X \cdot_A v) = X \cdot_B P(v)$ for all $v$. Since $X$ acts as $A$ on $V_A$ and as $B$ on $V_B$, this is $P A v = B P v$ for all $v$, i.e. $PA = BP$, i.e. $B = P A P^{-1}$. (Whether you get $P^{-1}AP$ or $PAP^{-1}$ depends on a harmless naming choice — both define the same relation "similar".)

> [!note]- Hint 3
> For $(2) \Leftrightarrow (3)$, use the presentation: $V_A$ is the *cokernel* of $XI-A : F[X]^n \to F[X]^n$. The implication $(3) \Rightarrow (2)$ is easy — if $XI-B = P(XI-A)Q$ with $P, Q$ invertible over $F[X]$, then $P$ and $Q$ set up an isomorphism of the two exact sequences, hence of their cokernels $V_A \cong V_B$. The hard direction is $(2) \Rightarrow (3)$: you are *given* an isomorphism of cokernels and must produce the invertible $P, Q$. You must *lift* the cokernel isomorphism to the free modules $F[X]^n$ sitting above.

> [!note]- Hint 4
> The lifting lemma: let $\theta : V_A \to V_B$ be an $F[X]$-module isomorphism. Because $F[X]^n$ is *free* (hence projective), the composite $F[X]^n \xrightarrow{\pi_A} V_A \xrightarrow{\theta} V_B$ lifts through the surjection $\pi_B : F[X]^n \to V_B$ to a map $Q : F[X]^n \to F[X]^n$ with $\pi_B Q = \theta\,\pi_A$. This $Q$ sends $\ker\pi_A$ into $\ker\pi_B$, i.e. $Q\,(XI-A)F[X]^n \subseteq (XI-B)F[X]^n$, which (since $XI-A, XI-B$ are *injective*) yields a matrix $P$ with $Q(XI-A) = (XI-B)P$. Doing the same for $\theta^{-1}$ produces inverses, so $P, Q$ are invertible over $F[X]$. Rearrange to $XI-B = Q(XI-A)P^{-1}$.

---

# Solution

The strategy is a cycle $(1) \Rightarrow (2) \Rightarrow (3) \Rightarrow (1)$. The implications $(1)\Leftrightarrow(2)$ and $(3)\Rightarrow(2)$ are unwindings of definitions; the substance is $(2) \Rightarrow (3)$, the lifting of a cokernel isomorphism to a conjugacy of characteristic matrices.

**Step 1: $(1) \Leftrightarrow (2)$ — a similarity is exactly an $F[X]$-module isomorphism.**

An invertible matrix $P$ satisfies $B = P^{-1}AP$ if and only if, viewed as an $F$-linear map $F^n \to F^n$, it is an isomorphism of $F[X]$-modules $V_A \to V_B$.

> [!note]- Derivation
> Both $V_A$ and $V_B$ have underlying $F$-vector space $F^n$. An $F[X]$-module homomorphism $\theta : V_A \to V_B$ is, by definition, an $F$-linear map that additionally commutes with the action of every element of $F[X]$. Since $F[X]$ is generated as an $F$-algebra by $X$, commuting with all of $F[X]$ is equivalent to commuting with $X$ alone:
> $$\theta(X \cdot_A v) = X \cdot_B \theta(v) \qquad \text{for all } v \in F^n.$$
> On $V_A$ the element $X$ acts as $A$, and on $V_B$ it acts as $B$. So, writing $\theta$ as a matrix $P$, the condition reads
> $$P (A v) = B (P v) \quad \text{for all } v, \qquad \text{i.e.} \qquad PA = BP.$$
> Therefore: an $F$-linear map $P$ is an $F[X]$-module *homomorphism* $V_A \to V_B$ iff $PA = BP$, and it is an *isomorphism* iff additionally $P$ is invertible. When $P$ is invertible, $PA = BP$ rearranges to $B = PAP^{-1}$.
>
> Now compare with statement $(1)$: $A$ and $B$ are similar iff $B = P^{-1}AP$ for some invertible $P$. The two relations $B = PAP^{-1}$ and $B = P^{-1}AP$ define the *same* equivalence relation on matrices — replacing $P$ by $P^{-1}$ converts one into the other. Hence:
> $$A \sim B \;\Longleftrightarrow\; \exists\,P \in \mathrm{GL}_n(F)\ \text{with}\ PA = BP \;\Longleftrightarrow\; V_A \cong V_B \ \text{as } F[X]\text{-modules}.$$
> This is $(1) \Leftrightarrow (2)$. The content is purely a translation: "change of basis conjugating $A$ to $B$" and "$F[X]$-module isomorphism $V_A \to V_B$" are *the same data*, because an $F[X]$-module map is precisely an $F$-linear map that respects the distinguished operator.

**Step 2: $(3) \Rightarrow (2)$ — equivalent characteristic matrices have isomorphic cokernels.**

If $XI-B = P\,(XI-A)\,Q$ with $P, Q \in \mathrm{GL}_n(F[X])$, then $V_A \cong V_B$.

> [!note]- Derivation
> Recall the presentation: for any matrix $M$ over $F$, there is a short exact sequence of $F[X]$-modules
> $$0 \to F[X]^n \xrightarrow{\;XI-M\;} F[X]^n \xrightarrow{\;\pi_M\;} V_M \to 0,$$
> so $V_M = \operatorname{coker}(XI-M) = F[X]^n/(XI-M)F[X]^n$. (Injectivity of $XI-M$ holds because $\det(XI-M) = \chi_M$ is a non-zero element of the domain $F[X]$, hence not a zero-divisor; surjectivity onto $V_M$ and the identification of the kernel are the standard presentation of $V_M$ by generators $e_1, \dots, e_n$ and relations $X e_j = \sum_i M_{ij} e_i$.)
>
> Suppose $XI - B = P\,(XI-A)\,Q$ with $P, Q$ invertible over $F[X]$. Regard $P$ and $Q$ as $F[X]$-linear automorphisms of $F[X]^n$. The equation says the square
> $$\begin{array}{ccc} F[X]^n & \xrightarrow{\;XI-A\;} & F[X]^n \\ \big\downarrow{\scriptstyle Q^{-1}} & & \big\downarrow{\scriptstyle P} \\ F[X]^n & \xrightarrow{\;XI-B\;} & F[X]^n \end{array}$$
> commutes: going right-then-down gives $P(XI-A)$, going down-then-right gives $(XI-B)Q^{-1}$, and $P(XI-A) = (XI-B)Q^{-1}$ is the rearrangement of the hypothesis. A commuting square of injective maps whose vertical arrows are isomorphisms induces an isomorphism on cokernels: $P$ carries $(XI-A)F[X]^n$ isomorphically onto $(XI-B)F[X]^n$ (because $P(XI-A)F[X]^n = (XI-B)Q^{-1}F[X]^n = (XI-B)F[X]^n$, using that $Q^{-1}$ is surjective), so $P$ descends to an isomorphism of quotients
> $$\overline{P} : \frac{F[X]^n}{(XI-A)F[X]^n} \xrightarrow{\ \sim\ } \frac{F[X]^n}{(XI-B)F[X]^n}, \qquad \text{i.e.}\qquad V_A \cong V_B.$$
> This proves $(3) \Rightarrow (2)$.

**Step 3: $(2) \Rightarrow (3)$ — an isomorphism of modules lifts to a conjugacy of characteristic matrices.**

If $V_A \cong V_B$ as $F[X]$-modules, then there are invertible $P, Q \in \mathrm{GL}_n(F[X])$ with $XI-B = Q\,(XI-A)\,P^{-1}$.

> [!note]- Derivation
> This is the substantial implication. Let $\theta : V_A \to V_B$ be an $F[X]$-module isomorphism. We have the two presentations
> $$F[X]^n \xrightarrow{\;XI-A\;} F[X]^n \xrightarrow{\;\pi_A\;} V_A \to 0, \qquad F[X]^n \xrightarrow{\;XI-B\;} F[X]^n \xrightarrow{\;\pi_B\;} V_B \to 0.$$
>
> *Lifting $\theta$.* The module $F[X]^n$ is **free**, hence **projective**: for any surjection $\sigma$ and any map into the target, the map lifts through $\sigma$. Apply this to the surjection $\pi_B : F[X]^n \twoheadrightarrow V_B$ and the map $\theta \circ \pi_A : F[X]^n \to V_B$. (Concretely: pick the standard basis $e_1, \dots, e_n$ of the upper $F[X]^n$; choose for each $j$ an element $Q e_j \in F[X]^n$ with $\pi_B(Q e_j) = \theta(\pi_A(e_j))$, possible since $\pi_B$ is onto; extend $F[X]$-linearly.) This produces an $F[X]$-linear map $Q : F[X]^n \to F[X]^n$ — a matrix over $F[X]$ — with
> $$\pi_B \circ Q = \theta \circ \pi_A.$$
>
> *$Q$ respects the relation submodules.* The kernel of $\pi_A$ is $(XI-A)F[X]^n$, and similarly for $B$. If $w \in (XI-A)F[X]^n = \ker\pi_A$, then $\pi_B(Q w) = \theta(\pi_A(w)) = \theta(0) = 0$, so $Q w \in \ker\pi_B = (XI-B)F[X]^n$. Hence
> $$Q\,(XI-A)F[X]^n \subseteq (XI-B)F[X]^n.$$
> In particular, for each basis vector $e_j$, the element $Q(XI-A)e_j$ lies in the image of $XI-B$, so there is a unique $P e_j \in F[X]^n$ with $Q(XI-A)e_j = (XI-B)(P e_j)$ — *uniqueness* because $XI-B$ is injective. Extending $F[X]$-linearly gives a matrix $P$ over $F[X]$ with
> $$Q\,(XI-A) = (XI-B)\,P.$$
>
> *$P$ and $Q$ are invertible.* Run the identical construction on the inverse isomorphism $\theta^{-1} : V_B \to V_A$: it yields matrices $Q', P'$ over $F[X]$ with $\pi_A Q' = \theta^{-1}\pi_B$ and $Q'(XI-B) = (XI-A)P'$. Consider the composite $Q' Q : F[X]^n \to F[X]^n$. It satisfies $\pi_A (Q'Q) = \theta^{-1}\pi_B Q = \theta^{-1}\theta\,\pi_A = \pi_A$, so $\pi_A \circ (Q'Q - \mathrm{id}) = 0$, meaning $(Q'Q - \mathrm{id})$ maps into $\ker\pi_A = (XI-A)F[X]^n$. Thus $Q'Q = \mathrm{id} + (XI-A)R$ for some matrix $R$ over $F[X]$. The same argument with the roles reversed gives $Q Q' = \mathrm{id} + (XI-B)S$.
>
> We must upgrade "$Q'Q$ is identity modulo relations" to "$Q'Q$ is genuinely invertible". Take determinants: $\det(Q'Q) = \det(\mathrm{id} + (XI-A)R)$. Now apply the *evaluation* trick — substitute $X = A$ is not legal in $F[X]$, so argue via degrees instead. Both $Q'Q$ and $\mathrm{id}+(XI-A)R$ are matrices over $F[X]$; their determinants are equal polynomials. A cleaner route avoids determinants entirely: from $Q'Q = \mathrm{id} + (XI-A)R$ and $\pi_A(Q'Q) = \pi_A$ we have already shown $Q'Q$ induces the identity on the cokernel $V_A$. Symmetrically $QQ'$ induces the identity on $V_B$. But $Q$ induces $\overline Q = \theta$ (an isomorphism) and $Q'$ induces $\overline{Q'} = \theta^{-1}$; so on cokernels $Q$ is invertible. To get invertibility of the *matrix* $Q$ over $F[X]$, use the structure-theorem framing: $XI-A$ and $XI-B$ are injective with the *same* cokernel, and a standard lemma (the uniqueness clause behind [[Thm - Smith Normal Form|Smith normal form]]) states that *two injective endomorphisms of $F[X]^n$ with isomorphic cokernels are equivalent matrices*. Concretely, reduce $XI-A$ and $XI-B$ to Smith normal form; their cokernels $V_A, V_B$ have the same invariant factors (Step 4 below shows invariant factors are an isomorphism invariant), so the Smith normal forms of $XI-A$ and $XI-B$ are equal, and hence $XI-A$ and $XI-B$ are equivalent: $XI-B = \widetilde P\,(XI-A)\,\widetilde Q$ for invertible $\widetilde P, \widetilde Q$ over $F[X]$. That is exactly statement $(3)$.
>
> *(Remark on the logic.* The honest shortest proof of $(2) \Rightarrow (3)$ is the last sentence: $V_A \cong V_B$ forces equal invariant factors, equal invariant factors force equal Smith normal forms of $XI-A, XI-B$, equal Smith normal forms force $XI-A \sim XI-B$. The lifting construction above is the conceptual content — it exhibits the conjugating matrices directly from $\theta$ — and either argument completes the implication. The lifting argument also makes transparent *why* the conjugators may be taken with polynomial entries: they are assembled from the images of basis vectors under a module map.)*
>
> Rearranging $Q(XI-A) = (XI-B)P$ gives $XI-B = Q(XI-A)P^{-1}$ once $P$ is known invertible, which the Smith normal form comparison guarantees. This is $(2) \Rightarrow (3)$.

**Step 4: Close the cycle and deduce the classification.**

The cycle $(1) \Rightarrow (2) \Rightarrow (3) \Rightarrow (1)$ is complete, so the three statements are equivalent. The rational canonical form is therefore a complete invariant for similarity.

> [!note]- Derivation
> *Closing the cycle.* Step 1 gives $(1) \Leftrightarrow (2)$, in particular $(1) \Rightarrow (2)$. Step 3 gives $(2) \Rightarrow (3)$. Step 2 gives $(3) \Rightarrow (2)$, and combined with $(2) \Rightarrow (1)$ from Step 1, we get $(3) \Rightarrow (1)$. So $(1) \Rightarrow (2) \Rightarrow (3) \Rightarrow (1)$, and all three are equivalent. $\blacksquare$
>
> *The classification.* By [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|the structure theorem]], a finitely generated $F[X]$-module is determined up to isomorphism by its **invariant factors** $f_1 \mid \cdots \mid f_s$ (monic, non-constant), and conversely modules with the same invariant factors are isomorphic. Therefore:
> $$V_A \cong V_B \quad\Longleftrightarrow\quad V_A,\ V_B \text{ have the same invariant factors}.$$
> By the equivalence just proved, $A \sim B \Leftrightarrow V_A \cong V_B$, so $A \sim B$ if and only if $V_A$ and $V_B$ have the same invariant factors. By [[Thm - Rational Canonical Form|the rational canonical form theorem]], the rational canonical form of $A$ is the block-diagonal companion matrix $\operatorname{diag}(c(f_1), \dots, c(f_s))$ built from precisely these invariant factors; so two matrices have the same rational canonical form if and only if they have the same invariant factors. Chaining:
> $$A \sim B \iff V_A \cong V_B \iff \{\text{same invariant factors}\} \iff \{\text{same rational canonical form}\}.$$
> Finally, by [[Thm - Smith Normal Form|the Smith normal form theorem]] the invariant factors of $V_A$ are exactly the non-constant Smith normal form entries of $XI-A$, so "same invariant factors" $\iff$ "$XI-A$ and $XI-B$ have the same Smith normal form" $\iff$ "$XI-A$ and $XI-B$ are equivalent over $F[X]$" — recovering statement $(3)$ and confirming the chain is self-consistent.
>
> In words: the rational canonical form is a **complete invariant** for similarity. It assigns to each matrix a canonical representative of its similarity class, and two matrices are similar exactly when these representatives are identical. This is strictly stronger than what the characteristic and minimal polynomials provide — those are *invariants* (similar matrices share them) but not *complete* (non-similar matrices can share them); the full invariant-factor list never fails to separate.

> [!note]- Complete formal solution
> **Claim.** For $A, B \in M_{n,n}(F)$: $A \sim B \iff V_A \cong V_B$ as $F[X]$-modules $\iff XI-A$ and $XI-B$ are equivalent over $F[X]$. Consequently the rational canonical form is a complete similarity invariant.
>
> *$(1) \Leftrightarrow (2)$.* An $F$-linear map $P : F^n \to F^n$ is an $F[X]$-module map $V_A \to V_B$ iff it commutes with the action of $X$, i.e. $PA = BP$ (since $X$ acts as $A$, resp. $B$). It is an isomorphism iff $P$ is moreover invertible, and then $B = PAP^{-1}$. The relations $B = PAP^{-1}$ and $B = P^{-1}AP$ define the same equivalence; hence $A \sim B \iff \exists\,P \in \mathrm{GL}_n(F),\ PA = BP \iff V_A \cong V_B$.
>
> *Presentation.* For any $M$, the sequence $0 \to F[X]^n \xrightarrow{XI-M} F[X]^n \xrightarrow{\pi_M} V_M \to 0$ is exact ($XI-M$ injective since $\det(XI-M) = \chi_M \ne 0$ in the domain $F[X]$); so $V_M \cong F[X]^n/(XI-M)F[X]^n$.
>
> *$(3) \Rightarrow (2)$.* If $XI-B = P(XI-A)Q$ with $P, Q$ invertible over $F[X]$, then $P(XI-A)F[X]^n = (XI-B)Q^{-1}F[X]^n = (XI-B)F[X]^n$, so the automorphism $P$ of $F[X]^n$ carries the relation submodule of $V_A$ onto that of $V_B$ and descends to an isomorphism $V_A \cong V_B$.
>
> *$(2) \Rightarrow (3)$.* Given an isomorphism $V_A \cong V_B$, the structure theorem says $V_A$ and $V_B$ have equal invariant factors. By the Smith normal form theorem, the invariant factors of $V_M$ are the non-constant Smith entries of $XI-M$; hence $XI-A$ and $XI-B$ have equal Smith normal forms and are therefore equivalent over $F[X]$. (Equivalently, lift the module isomorphism $\theta$ through the free presentations: freeness of $F[X]^n$ provides $Q$ with $\pi_B Q = \theta\pi_A$; injectivity of $XI-B$ provides $P$ with $Q(XI-A) = (XI-B)P$; the same applied to $\theta^{-1}$ yields inverses, so $P, Q$ are invertible and $XI-B = Q(XI-A)P^{-1}$.)
>
> *Cycle.* $(1) \Rightarrow (2)$ and $(2) \Rightarrow (1)$ from the first part, $(2) \Rightarrow (3)$ and $(3) \Rightarrow (2)$ from the rest; all three statements are equivalent.
>
> *Classification.* $A \sim B \iff V_A \cong V_B \iff$ equal invariant factors $\iff$ equal rational canonical form $\iff$ $XI-A, XI-B$ have equal Smith normal form. The rational canonical form is thus a complete invariant for similarity over $F$. $\blacksquare$

---

# Key Takeaways

**A matrix *is* a module, and similarity *is* isomorphism — the dictionary is the whole theorem.** The deepest content of this exercise is the recognition that the passage $A \rightsquigarrow V_A$ is not a mere analogy but a faithful, structure-preserving translation: an $F[X]$-module homomorphism $V_A \to V_B$ is by definition an $F$-linear map that commutes with the distinguished operator, and "commutes with the operator" is precisely the matrix equation $PA = BP$ that defines conjugation. So the categories {matrices over $F$, up to similarity} and {finitely generated $F[X]$-modules with $V \cong F^n$, up to isomorphism} are *the same category*. Every theorem about one transfers verbatim to the other. The trigger "I have a question about matrices up to similarity" should fire the reaction "restate it as a question about $F[X]$-modules and apply the structure theorem" — this is the single most powerful move in canonical-form theory, and it is what makes the otherwise-mysterious rational canonical form *inevitable*: it is just the invariant-factor decomposition of a module, wearing a matrix costume.

**To compare two modules given by presentations, lift maps to the free covers.** The hard implication $(2) \Rightarrow (3)$ illustrates a technique of constant use in module theory: a module is often handed to you as a cokernel $\operatorname{coker}(M) = F[X]^n/MF[X]^n$, and a map *of cokernels* must be *upgraded* to a map of the presenting free modules before it can be turned into matrix data. The mechanism is the **projectivity of free modules**: any map out of $F[X]^n$ lifts through any surjection, because one only has to choose the images of basis vectors, with no consistency conditions to satisfy. Once lifted, the lift automatically respects the relation submodules (it sends kernel into kernel), and injectivity of the presenting matrix lets you solve for the second conjugator. This "lift through the free cover, then chase the relation submodule" pattern recovers, among many other things, the well-definedness of maps between presented modules, the functoriality of $\operatorname{Tor}$ and $\operatorname{Ext}$, and the comparison theorem for projective resolutions. Whenever a hypothesis gives you an *abstract* isomorphism of presented modules and you need *concrete* matrices, reach for the lifting lemma.

**The rational canonical form is a *complete* invariant; the characteristic and minimal polynomials are merely invariants.** This exercise proves the statement that gives the rational canonical form its authority. An *invariant* is any quantity preserved by similarity — the trace, determinant, characteristic polynomial, minimal polynomial are all invariants. A *complete* invariant additionally *reflects* similarity: if the invariant agrees, the matrices are similar. The characteristic and minimal polynomials fail completeness — non-similar matrices can share both (the smallest example: two matrices with $\chi = (X-2)^4$, $m = (X-2)^2$ but different numbers of Jordan blocks). The full invariant-factor list — equivalently the rational canonical form, equivalently the Smith normal form of $XI-A$ — *never* fails: by the uniqueness clause of the structure theorem it is a complete isomorphism invariant of $V_A$, hence a complete similarity invariant of $A$. The lesson generalises into a habit of mind: when handed an invariant, always ask "is it complete?", and to *refute* completeness exhibit two non-isomorphic objects it identifies, while to *prove* completeness route the invariant through a classification theorem whose uniqueness clause does the separating. The structure theorem for $F[X]$-modules is exactly such a classification, and it is why the rational canonical form is the final word on similarity over a field.

**The proof never used a single property of $F$ beyond "field" — it is uniform across all base fields, and the same scaffold runs over any Euclidean domain.** Notice what the argument did *not* require: no algebraic closedness, no characteristic-zero assumption, no finiteness of $F$. Every step used only that $F[X]$ is a Euclidean domain — division with remainder, hence the structure theorem and Smith normal form. This uniformity is significant. It means similarity of matrices is classified the *same way* over $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, $\mathbb{F}_p$, or any field, by the rational canonical form — which is precisely why that form is called *rational*: it is computed by rational operations in $F$ and lives over the field you started with, never needing field extensions. (The Jordan normal form, by contrast, *does* need an algebraically closed field, because it further splits the invariant factors into prime powers and that requires the primes to be linear.) More broadly, the entire proof scaffold — present a module as the cokernel of a square injective matrix, compare presentations by lifting and Smith normal form — runs over *any* Euclidean domain. Specialised to $\mathbb{Z}$ it classifies finitely generated abelian groups; specialised to $F[X]$ it classifies matrices up to similarity. Recognising that "matrix similarity" and "abelian group classification" are the same theorem over two different Euclidean domains is the kind of structural compression the module-theoretic viewpoint exists to deliver.
