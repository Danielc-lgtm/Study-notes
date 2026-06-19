---
type: exercise
subject: category-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Monad and Comonad"
  - "Def - Algebra for a Monad"
  - "Def - Kleisli Category"
  - "Thm - Eilenberg-Moore and Kleisli Realize a Monad"
tags: [category-theory, foundations]
---

# Problem Statement

**(a)** Exhibit two genuinely different [[Def - Adjunction|adjunctions]] $F_1 \dashv U_1$ and $F_2 \dashv U_2$, with the *same* base category $\mathcal{C}$, that induce the *same* [[Def - Monad and Comonad|monad]] $T$ on $\mathcal{C}$.

**(b)** Show that the [[Def - Kleisli Category|Kleisli]] adjunction $F_T \dashv U_T$ and the [[Def - Algebra for a Monad|Eilenberg–Moore]] adjunction $F^T \dashv U^T$ both induce $T$, and that for *any* adjunction inducing $T$ there are unique comparison functors $\mathcal{C}_T \to \mathcal{D} \to \mathcal{C}^T$. Conclude that Kleisli is initial and Eilenberg–Moore is terminal among all such adjunctions.

**Recall:**

![[Thm - Eilenberg-Moore and Kleisli Realize a Monad#Statement]]

The [[Def - Kleisli Category|Kleisli category]] $\mathcal{C}_T$ has the objects of $\mathcal{C}$ and morphisms $\mathcal{C}_T(A,B) = \mathcal{C}(A,TB)$; it is the free algebras inside $\mathcal{C}^T$. The [[Def - Algebra for a Monad|Eilenberg–Moore category]] $\mathcal{C}^T$ is all $T$-algebras.

---

# Convergent Strategy

**Problem class:** A "compare two resolutions of a monad" problem — the comparison-functor situation from the topic page. Part (a) demonstrates non-uniqueness of resolutions; part (b) organizes all resolutions into a category with initial and terminal objects.

**Assumption pattern:** The data is "a monad presented two ways." The assumption to leverage is that both presentations have the *same* $T = UF$, $\eta$, $\mu$, so both factor through the universal resolutions (legal operation 9). Recognizing "same monad, different adjunction" as the trigger for [[Thm - Eilenberg-Moore and Kleisli Realize a Monad]] is the key.

**Theorem routing:** Route directly through [[Thm - Eilenberg-Moore and Kleisli Realize a Monad]]: it provides the comparison functors and their universal properties. For (a), use the free-monoid monad, which is induced both by $\mathbf{Set}\rightleftarrows\mathbf{Mon}$ and by its Kleisli adjunction.

**Key decision point:** The non-obvious point is that "genuinely different" adjunctions can still induce the same monad — the monad sees only $UF$, $\eta$, and $U\varepsilon F$, not the categories $\mathcal{D}_1, \mathcal{D}_2$ themselves. The cleanest witness is to take $\mathcal{D}_1 = \mathbf{Mon}$ (Eilenberg–Moore-equivalent) and $\mathcal{D}_2 = \mathcal{C}_T$ (Kleisli), which are non-equivalent categories inducing the identical monad.

---

# Legal Operations Used

1. **Operation 9 from the topic page (recognize the free algebra / free–Kleisli embedding).** Both resolutions are compared by routing through the Kleisli embedding into Eilenberg–Moore and the initiality/terminality statements.

2. **Operation 1 from the topic page (read a monad off an adjunction).** Each adjunction in (a) yields its monad by [[Thm - Every Adjunction Gives a Monad]]; we check the two yield the same one.

3. **Operation 3 from the topic page (build the structure map of an algebra).** The comparison $\mathcal{D} \to \mathcal{C}^T$ sends $D$ to the algebra $(UD, U\varepsilon_D)$, the whiskered-counit structure map.

---

# Hints

> [!note]- Hint 1
> A monad determines $T$, $\eta$, $\mu$ — and nothing about the resolving category $\mathcal{D}$ beyond those. So any two adjunctions with the same $UF$, $\eta$, $U\varepsilon F$ induce the same monad, even if $\mathcal{D}_1 \not\simeq \mathcal{D}_2$.

> [!note]- Hint 2
> Take $T$ = the [[Ex - The free monoid monad|free-monoid monad]]. One resolution is $\mathbf{Set}\rightleftarrows\mathbf{Mon}$ (whose comparison to $\mathcal{C}^T$ is an equivalence, since the forgetful functor is monadic). Another is the *Kleisli* adjunction $\mathbf{Set}\rightleftarrows\mathbf{Set}_T$. These two have non-equivalent middle categories.

> [!note]- Hint 3
> For (b), the comparison *into* Eilenberg–Moore is $K(D) = (UD, U\varepsilon_D)$; it commutes with the forgetful functors. The comparison *out of* Kleisli sends the free Kleisli object on $X$ to $FX$. Uniqueness comes from commuting with the structure functors.

> [!note]- Hint 4
> Initiality of Kleisli = "unique functor *from* $\mathcal{C}_T$"; terminality of Eilenberg–Moore = "unique functor *to* $\mathcal{C}^T$". Any resolution $\mathcal{D}$ sits in between: $\mathcal{C}_T \to \mathcal{D} \to \mathcal{C}^T$.

---

# Solution

The plan: (a) present the free-monoid monad two ways — via $\mathbf{Mon}$ and via its Kleisli category — and check both induce the same $(T,\eta,\mu)$; (b) construct the comparison functors and verify their universal properties using [[Thm - Eilenberg-Moore and Kleisli Realize a Monad]]. The crux is that the monad is a *projection* of an adjunction, forgetting the resolving category.

**Step 1 (a): Two resolutions of the free-monoid monad.**

> [!note]- Derivation
> Let $T$ be the [[Ex - The free monoid monad|free-monoid monad]] on $\mathbf{Set}$, $TA = A^*$, $\eta$ = singleton, $\mu$ = concatenation.
>
> *Resolution 1:* the free–forgetful adjunction $F_1 \dashv U_1$ with $\mathcal{D}_1 = \mathbf{Mon}$, $U_1$ forgetful, $F_1 A = A^*$. By [[Ex - The free monoid monad|the free-monoid computation]], $U_1 F_1 = T$, with the given $\eta, \mu$.
>
> *Resolution 2:* the Kleisli adjunction $F_T \dashv U_T$ with $\mathcal{D}_2 = \mathbf{Set}_T$, the [[Def - Kleisli Category|Kleisli category]] (objects = sets, morphisms $A \to B$ = functions $A \to B^*$). By construction $U_T F_T = T$ with the same $\eta, \mu$.
>
> The middle categories differ: $\mathbf{Mon}$ has all monoids and all homomorphisms, while $\mathbf{Set}_T$ has only sets as objects (its objects are *free* monoids, with morphisms the Kleisli arrows). They are not equivalent — $\mathbf{Set}_T$ has a proper class fewer objects up to iso. Yet both induce the identical monad $T$, demonstrating non-uniqueness.

**Step 2 (b): Both canonical resolutions induce $T$.**

> [!note]- Derivation
> By [[Thm - Eilenberg-Moore and Kleisli Realize a Monad]] (Lemma 1 there), $F^T \dashv U^T$ induces $T$: the comparison $\mathbf{Mon} \to \mathbf{Set}^T$ is in fact an equivalence (the forgetful functor is monadic), and $U^T F^T = T$. By construction the Kleisli adjunction $F_T \dashv U_T$ has $U_T F_T = T$ with the same unit and multiplication. So both are objects of the category $\mathbf{Adj}(T)$ of adjunctions inducing $T$.

**Step 3 (b): The comparison functors and their universal properties.**

> [!note]- Derivation
> For any adjunction $F \dashv U$ inducing $T$ ($U : \mathcal{D} \to \mathcal{C}$):
>
> *Into Eilenberg–Moore:* $K : \mathcal{D} \to \mathcal{C}^T$, $K(D) = (UD, U\varepsilon_D)$, is a $T$-algebra by the whiskered-counit computation, and satisfies $U^T K = U$, $KF = F^T$. It is the *unique* such functor (commuting with $U$ forces the underlying object $UD$; commuting with $F$ and the counit forces the structure map $U\varepsilon_D$). So $\mathcal{C}^T$ is **terminal**: every resolution maps uniquely *to* it.
>
> *Out of Kleisli:* $L : \mathcal{C}_T \to \mathcal{D}$, $L(A) = FA$ on objects and $L(f : A \to TB) = \varepsilon_{FB}\circ Ff$ on Kleisli arrows, satisfies $UL = U_T$, $LF_T = F$, and is unique. So $\mathcal{C}_T$ is **initial**: it maps uniquely *from* itself into every resolution.
>
> Composing, every $\mathcal{D}$ sits in the chain $\mathcal{C}_T \xrightarrow{L} \mathcal{D} \xrightarrow{K} \mathcal{C}^T$, with the composite $\mathcal{C}_T \to \mathcal{C}^T$ the inclusion of free algebras.

**Step 4 (b): Conclusion.**

> [!note]- Derivation
> The adjunctions inducing $T$ form a category $\mathbf{Adj}(T)$ with the Kleisli adjunction initial and the Eilenberg–Moore adjunction terminal. The two resolutions of part (a) — $\mathbf{Mon}$ (terminal, up to equivalence) and $\mathbf{Set}_T$ (initial) — are precisely the two ends of this interval, which is why they differ yet induce the same monad: every other resolution lives between them.

> [!note]- Complete formal solution
> **(a)** Let $T$ be the free-monoid monad. The free–forgetful adjunction $\mathbf{Set}\rightleftarrows\mathbf{Mon}$ and the Kleisli adjunction $\mathbf{Set}\rightleftarrows\mathbf{Set}_T$ both have $U F = T$ with $\eta$ = singleton, $\mu$ = concatenation, so both induce $T$; but $\mathbf{Mon}\not\simeq\mathbf{Set}_T$ (the latter's objects are only the free monoids).
>
> **(b)** By [[Thm - Eilenberg-Moore and Kleisli Realize a Monad]], $F^T\dashv U^T$ and $F_T\dashv U_T$ induce $T$. For any adjunction $F\dashv U$ inducing $T$, $K(D) = (UD, U\varepsilon_D)$ is the unique functor $\mathcal{D}\to\mathcal{C}^T$ with $U^T K = U$, $KF = F^T$ (terminality), and $L(A) = FA$, $L(f) = \varepsilon_{FB}\circ Tf$ is the unique functor $\mathcal{C}_T\to\mathcal{D}$ with $UL = U_T$, $LF_T = F$ (initiality). Hence in $\mathbf{Adj}(T)$ Kleisli is initial and Eilenberg–Moore terminal, and every resolution factors $\mathcal{C}_T\to\mathcal{D}\to\mathcal{C}^T$. $\blacksquare$

> [!warning] Illegal but tempting: concluding the two resolutions are equivalent
> It is tempting to think "same monad ⟹ same category," i.e. $\mathcal{D}_1 \simeq \mathcal{D}_2$. This is false: $\mathbf{Mon}$ and $\mathbf{Set}_T$ induce the same monad but are not equivalent. The monad only records $UF, \eta, \mu$; it forgets the resolving category. Two resolutions coincide *only* in the idempotent case (when Kleisli $\simeq$ Eilenberg–Moore). The repair is to remember that the monad determines the *interval* $[\mathcal{C}_T, \mathcal{C}^T]$, not a single category.

---

# Key Takeaways

**A monad is a projection that forgets the resolving category.** The deepest lesson is that the monad $(T, \eta, \mu)$ retains only the data visible from the base: the endofunctor $UF$, the unit, and the whiskered counit. Everything about $\mathcal{D}$ beyond this — how many objects it has, whether they are "free" or not — is invisible. This is why non-equivalent categories can induce the same monad: they agree on what the forgetful functor remembers and differ on everything the projection discards. The trigger for recognizing this situation is "two free–forgetful setups with the same composite," and the reaction is to compare them through the universal resolutions rather than directly.

**Initial and terminal resolutions bracket every other one.** The organizing principle is that the resolutions of a fixed monad form a category with a smallest (Kleisli, the free algebras only) and a largest (Eilenberg–Moore, all algebras) element, and every concrete category of structured objects inducing the monad sits in between. This is enormously useful: to test whether a category $\mathcal{D}$ "is the algebras," you only ever examine the *single* canonical comparison $K : \mathcal{D} \to \mathcal{C}^T$ to the terminal object — there is no search over adjunctions. The diagnostic is that recognizing $\mathcal{D}$ as $\mathcal{C}^T$ is exactly recognizing $K$ as an equivalence, which is the content of the [[Thm - The Barr-Beck Monadicity Theorem|monadicity theorem]].

**Initiality and terminality point in opposite directions — track the arrows.** A recurring source of error is the direction of the comparison functors: Kleisli is *initial*, so there is a unique functor *out of* it into any resolution, while Eilenberg–Moore is *terminal*, so there is a unique functor *into* it from any resolution. The mnemonic is that the free algebras (Kleisli) are the "least committed" objects, so they map forward into everything, while all algebras (Eilenberg–Moore) are the "most committed," so everything maps backward into them. Keeping the arrows straight is what makes the universal-property statements usable, and it generalizes: whenever you meet "the free version" and "the complete version" of a structure, the free version is initial and the complete version is terminal in the appropriate category of intermediaries. See [[Ex - Which forgetful functors are monadic]] for the payoff when the terminal comparison turns out to be an equivalence.
