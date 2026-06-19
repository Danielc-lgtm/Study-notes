---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Kleisli Category"
  - "Def - Monad and Comonad"
  - "Def - Category"
tags: [category-theory, foundations]
---

# Problem Statement

Let $P$ be the [[Ex - The power-set monad|power-set monad]] on $\mathbf{Set}$: $P(A)$ = subsets of $A$, $\eta_A(a) = \{a\}$, $\mu_A(\mathcal{S}) = \bigcup\mathcal{S}$. Let $\mathbf{Rel}$ be the category whose objects are sets and whose morphisms $A \to B$ are **relations** $R \subseteq A \times B$, with composition $S \circ R = \{(a,c) : \exists b,\ (a,b)\in R \wedge (b,c)\in S\}$ and identities the diagonal relations $\Delta_A = \{(a,a)\}$.

Prove that the [[Def - Kleisli Category|Kleisli category]] $\mathbf{Set}_P$ is isomorphic to $\mathbf{Rel}$.

**Recall:**

![[Def - Kleisli Category#The Definition]]

A morphism $A \to B$ in $\mathbf{Set}_P$ is a function $f : A \to P(B)$, i.e. an assignment of a subset of $B$ to each element of $A$. Kleisli composition is $g \diamond f = \mu_C \circ Pg \circ f$.

---

# Convergent Strategy

**Problem class:** A "compute a Kleisli category concretely" problem — recognizing that effectful maps for a specific monad form a familiar category. Here the effect is nondeterminism and the familiar category is $\mathbf{Rel}$.

**Assumption pattern:** A Kleisli arrow $A \to P(B)$ assigns a *subset* of $B$ to each $a \in A$ — which is exactly the data of a relation (legal operation 4). The assumption to leverage is the bijection "function into the power set $\leftrightarrow$ relation," the curry/uncurry of the membership predicate.

**Theorem routing:** Route through [[Def - Kleisli Category]]: identify objects (same sets), morphisms (functions $A \to P(B)$ $\cong$ relations $A \times B$), and verify that Kleisli composition $\mu_C \circ Pg \circ f$ unwinds to relational composition, and that the Kleisli identity $\eta_A$ is the diagonal.

**Key decision point:** The one computation that carries the proof is showing Kleisli composition equals relational composition. The decision is to expand $\mu_C \circ Pg \circ f$ pointwise: for $a \in A$, $f(a)$ is a subset of $B$, $Pg$ sends it to a set of subsets of $C$, and $\mu_C$ unions them — yielding exactly $\{c : \exists b \in f(a),\ c \in g(b)\}$, the relational composite.

---

# Legal Operations Used

1. **Operation 4 from the topic page (pass to the Kleisli category to model effectful maps).** A nondeterministic map "$a$ may go to any of a set of $b$'s" is a Kleisli arrow $A \to P(B)$, recognized as a relation.

2. **Operation 9 from the topic page (recognize the free algebra / free–Kleisli structure), in spirit.** We exhibit the isomorphism of categories $\mathbf{Set}_P \cong \mathbf{Rel}$ by matching objects, morphisms, composition, and identities.

---

# Hints

> [!note]- Hint 1
> A function $f : A \to P(B)$ is the same data as a relation $R_f \subseteq A \times B$: declare $(a,b) \in R_f$ iff $b \in f(a)$. This is a bijection between $\mathbf{Set}_P(A,B)$ and relations $A \to B$.

> [!note]- Hint 2
> Unwind Kleisli composition pointwise. For $f : A \to P(B)$ and $g : B \to P(C)$, compute $(g\diamond f)(a) = \mu_C(Pg(f(a)))$. Here $Pg(f(a)) = \{g(b) : b \in f(a)\}$ (a set of subsets of $C$), and $\mu_C$ unions: $\bigcup_{b\in f(a)} g(b)$.

> [!note]- Hint 3
> Translate to relations: $c \in (g\diamond f)(a)$ iff $\exists b\in f(a)$ with $c\in g(b)$, iff $\exists b$ with $(a,b)\in R_f$ and $(b,c)\in R_g$ — exactly $(a,c) \in R_g \circ R_f$.

> [!note]- Hint 4
> The Kleisli identity is $\eta_A(a) = \{a\}$, whose relation is $\{(a,a')\colon a' \in \{a\}\} = \Delta_A$, the diagonal — the identity in $\mathbf{Rel}$.

---

# Solution

The plan: build the identity-on-objects functor sending a Kleisli arrow to its relation, show it is a bijection on morphisms, and verify it preserves composition and identities. The whole proof rests on the single pointwise computation that Kleisli composition is relational composition.

**Step 1: The object and morphism correspondence.**

> [!note]- Derivation
> Define $\Phi : \mathbf{Set}_P \to \mathbf{Rel}$ to be the identity on objects (both have all sets). On morphisms, send a Kleisli arrow $f : A \to P(B)$ to the relation
> $$\Phi(f) = R_f := \{(a,b) \in A\times B : b \in f(a)\}.$$
> This is a bijection $\mathbf{Set}_P(A,B) = \mathbf{Set}(A, P(B)) \xrightarrow{\sim} \{\text{relations } A\to B\}$: given a relation $R$, recover $f_R(a) = \{b : (a,b)\in R\}$, and $\Phi(f_{R}) = R$, $f_{\Phi(f)} = f$. (This is the curry/uncurry bijection $\mathbf{Set}(A, P(B)) \cong \mathbf{Set}(A\times B, 2) \cong \mathcal{P}(A\times B)$.)

**Step 2: Kleisli composition equals relational composition.**

> [!note]- Derivation
> Let $f : A \to P(B)$ and $g : B \to P(C)$. By the [[Def - Kleisli Category|Kleisli composition]] formula, $g \diamond f = \mu_C \circ Pg \circ f$. Pointwise, for $a \in A$:
> $$f(a) \in P(B); \quad Pg(f(a)) = \{g(b) : b \in f(a)\} \in P(P(C)); \quad \mu_C(\dots) = \bigcup_{b\in f(a)} g(b).$$
> So $(g\diamond f)(a) = \bigcup_{b\in f(a)} g(b)$, and therefore
> $$c \in (g\diamond f)(a) \iff \exists b\ \big(b \in f(a) \wedge c \in g(b)\big) \iff \exists b\ \big((a,b)\in R_f \wedge (b,c)\in R_g\big).$$
> The right side is exactly $(a,c) \in R_g \circ R_f$, the relational composite. Hence $\Phi(g\diamond f) = R_g \circ R_f = \Phi(g)\circ\Phi(f)$.

**Step 3: Identities and conclusion.**

> [!note]- Derivation
> The Kleisli identity on $A$ is $\eta_A : a \mapsto \{a\}$, whose relation is $R_{\eta_A} = \{(a,a') : a' \in \{a\}\} = \{(a,a)\} = \Delta_A$, the identity of $\mathbf{Rel}$. So $\Phi$ preserves identities. Being identity-on-objects, bijective on morphisms (Step 1), and composition- and identity-preserving (Steps 2–3), $\Phi$ is an isomorphism of categories: $\mathbf{Set}_P \cong \mathbf{Rel}$.

> [!note]- Complete formal solution
> Define $\Phi : \mathbf{Set}_P \to \mathbf{Rel}$ to be the identity on objects and to send a Kleisli arrow $f : A \to P(B)$ to $R_f = \{(a,b) : b \in f(a)\}$. This is a bijection on hom-sets (inverse $R \mapsto (a\mapsto\{b:(a,b)\in R\})$). It preserves composition: $(g\diamond f)(a) = \mu_C(Pg(f(a))) = \bigcup_{b\in f(a)}g(b)$, so $c\in(g\diamond f)(a)$ iff $\exists b\,(a,b)\in R_f,(b,c)\in R_g$, i.e. $R_g\circ R_f$. It preserves identities: $R_{\eta_A} = \Delta_A$. Hence $\Phi$ is an isomorphism $\mathbf{Set}_P \cong \mathbf{Rel}$. $\blacksquare$

> [!tip] Sanity check via the maybe monad
> The same recipe with the maybe monad $(-)+1$ gives the category of sets and *partial* functions: a Kleisli arrow $A \to B+1$ is a partial function, and Kleisli composition is composition of partial functions. The pattern "Kleisli of a monad = a category of generalized maps" is robust; $\mathbf{Rel}$ (nondeterministic) and partial functions (possibly-undefined) are two instances differing only in the monad.

---

# Key Takeaways

**A Kleisli arrow is a generalized map, and the monad names the generalization.** The reusable principle is that "function into $T$ of the target" packages a specific flavour of non-functional map: into $P(B)$ it is a relation (nondeterministic), into $B+1$ a partial function, into $D(B)$ a stochastic map. Recognizing this lets you import the entire categorical apparatus — composition, identities, limits — to settings that look like they have "maps that misbehave." The trigger is a class of maps that "produce more than a single output element," and the reaction is to identify the monad $T$ whose Kleisli category they form, after which relational, partial, and probabilistic composition are all the *same* formula $\mu \circ Tg \circ f$.

**Kleisli composition is "flatten after mapping," and it is always the natural composition law.** The pointwise computation $\mu_C \circ Pg \circ f = \bigcup_{b\in f(a)}g(b)$ is the template: apply the second map under $T$, producing a nested effect, then flatten with $\mu$. For relations this is "chase through an intermediate point"; for probability it is the law of total probability; for partial functions it is "defined where both stages are." Internalizing that these are one operation, instantiated by the monad's multiplication, means you never re-derive relational or probabilistic composition from scratch — you read it off the Kleisli formula. This is the diagnostic that turns a zoo of composition rules into a single mechanism.

**Identity-on-objects functors that are bijective on hom-sets are isomorphisms — a clean recognition pattern.** The cleanest way to prove two categories are *the same* (not merely equivalent) is to exhibit an identity-on-objects, hom-set-bijective, composition-preserving functor, exactly as here. This is stronger than equivalence and is the right notion when, as for $\mathbf{Set}_P$ and $\mathbf{Rel}$, the two descriptions have literally the same objects and a tautological matching of morphisms. The transferable move is: when two categories have the same objects and you suspect they coincide, set up the identity-on-objects functor and reduce everything to a single composition-law computation. See [[Ex - Algebras for the free-vector-space monad]] and [[Ex - Algebras for the free-group monad are groups]] for the contrasting situation where the comparison is an *equivalence* rather than an isomorphism, because the algebra side has genuinely different objects.
