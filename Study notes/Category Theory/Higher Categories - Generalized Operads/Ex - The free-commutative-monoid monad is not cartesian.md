---
type: exercise
subject: higher-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Cartesian Monad"
  - "Def - Monad and Comonad"
  - "Def - Pullback and Pushout"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $M$ be the free-commutative-monoid (finite-multiset) monad on $\mathbf{Set}$: $MX = \coprod_{n \geq 0} X^n / S_n$, the set of finite multisets (unordered lists) of elements of $X$, with unit $\eta_X(x) = \{x\}$ the singleton multiset and multiplication $\mu_X$ the union (concatenation, forgetting order) of a multiset of multisets. Show that $M$ is **not** a [[Def - Cartesian Monad|cartesian monad]] by exhibiting a naturality square of the multiplication $\mu$ that fails to be a [[Def - Pullback and Pushout|pullback]].

**Recall:**

![[Def - Cartesian Monad#The Definition]]

A multiplication naturality square for $f : A \to B$ has corners $M^2 A, M^2 B, MA, MB$, with $\mu$ on the vertical legs and $Mf, M^2 f$ on the horizontal. It is a pullback iff the comparison $M^2 A \to MA \times_{MB} M^2 B$ is a bijection — equivalently, iff every multiset-of-multisets in $M^2 A$ is uniquely determined by its flattening in $MA$ together with its abstract shape in $M^2 B$.

---

# Convergent Strategy

**Problem class:** This is a *refutation of cartesianness* (the most instructive case of the chapter's first target). The routine is not to check all squares but to construct a *single* explicit square whose comparison map fails to be injective, exhibiting two distinct elements of the apex with the same image on both legs.

**Assumption pattern:** The decisive feature is the *symmetric quotient* $(-)^n / S_n$: multisets forget the order of their elements. This forgetting is exactly the mechanism that destroys the pullback, because a flattened multiset can arise from genuinely different partitions and the union $\mu$ cannot tell them apart. The assumption to exploit is "union forgets the partition".

**Theorem routing:** No external theorem; the route is straight from the [[Def - Cartesian Monad|definition]], used negatively. Pick a map $f$ (collapsing onto one point is enough), write the multiplication square, and find two multisets-of-multisets that flatten to the same multiset and have the same shape but are not equal — then the comparison map is not injective, so the square is not a pullback.

**Key decision point:** The non-obvious choice is *which two partitions to use*. The cleanest witness uses a flattened multiset with a repeated element, so that "which copies were grouped together" is exactly the lost information. Choosing $\{a, a, b\}$ partitioned as $\{a\} \sqcup \{a, b\}$ versus $\{a, a\} \sqcup \{b\}$ gives the same union and the same shape (two blocks, sizes $1$ and $2$), but distinct elements of $M^2 A$. The natural alternative — a flattened multiset with all distinct elements — fails to be a witness, because then the partition *is* recoverable and the square looks like a pullback on that fibre.

---

# Legal Operations Used

1. **Operation 3 from the topic page (check cartesianness as a checklist — used to refute).** We exhibit one multiplication square that is not a pullback, which suffices to refute cartesianness.
2. **Operation 1 from the topic page (specialize the monad).** Working with the concrete multiset description makes the failure visible.
3. **Illegal-but-tempting #1 from the topic page (treating the multiset monad as cartesian).** This exercise *is* the counterexample that the warning points to; the repair is to use the list monad instead.

---

# Hints

> [!note]- Hint 1
> Compare with the list monad, where the analogous square *is* a pullback because a flat list cuts uniquely into consecutive blocks of given lengths. Ask: for multisets, can you always recover the partition from the union and the block-sizes?

> [!note]- Hint 2
> Take $A = \{a, b\}$, and let $f : A \to 1 = \{*\}$ be the unique map. Consider multisets-of-multisets in $M^2 A$ that flatten to $\{a, a, b\}$. The shape (recorded in $M^2 B = M^2 1$) is just the *sizes* of the blocks, since $f$ collapses everything to $*$.

> [!note]- Hint 3
> The two elements $\{\{a\}, \{a, b\}\}$ and $\{\{a, a\}, \{b\}\}$ of $M^2 A$ both have union $\{a, a, b\}$ and both have block-size-multiset $\{1, 2\}$ (their common image in $M^2 1$). They are not equal in $M^2 A$. So the comparison map sends two distinct points to one — not injective, hence not a pullback.

---

# Solution

The plan is to build one explicit multiplication square that is not a pullback. Step 1 sets up the square for the collapse map $f : \{a,b\} \to 1$. Step 2 exhibits two distinct multisets-of-multisets with the same flattening and the same shape. Step 3 concludes that the comparison map is not injective, so the square is not a pullback and $M$ is not cartesian — and identifies the symmetric quotient as the precise culprit.

**Step 1: Set up the multiplication square for $f : \{a, b\} \to 1$.**

> [!note]- Derivation
> Let $A = \{a, b\}$, $B = 1 = \{*\}$, and $f : A \to B$ the unique map. The multiplication naturality square is
> $$\begin{array}{ccc}
> M^2 A & \xrightarrow{\;M^2 f\;} & M^2 1 \\
> {\scriptstyle \mu_A}\big\downarrow & & \big\downarrow{\scriptstyle \mu_1} \\
> M A & \xrightarrow{\;Mf\;} & M 1
> \end{array}$$
> Here $M1$ is the set of multisets of $*$, i.e. $M1 \cong \mathbb{N}$ (a multiset of $*$ is determined by its cardinality). Likewise $M^2 1 \cong M\mathbb{N}$ is the set of finite multisets of natural numbers — an element records the *multiset of block-sizes*. The map $M^2 f$ sends a multiset-of-multisets over $A$ to the multiset of its block-sizes (collapsing all elements to $*$ records only how big each block is). The comparison map for the pullback is
> $$\Phi : M^2 A \longrightarrow MA \times_{M1} M^2 1, \qquad \Gamma \longmapsto \big(\mu_A(\Gamma),\, M^2 f(\Gamma)\big).$$
> The square is a pullback iff $\Phi$ is a bijection.

**Step 2: Two distinct elements with the same image.**

> [!note]- Derivation
> Consider the two elements of $M^2 A$:
> $$\Gamma_1 = \{\, \{a\},\ \{a, b\} \,\}, \qquad \Gamma_2 = \{\, \{a, a\},\ \{b\} \,\}.$$
> These are distinct multisets-of-multisets: $\Gamma_1$ contains a singleton $\{a\}$ and a pair $\{a,b\}$, while $\Gamma_2$ contains a pair $\{a,a\}$ and a singleton $\{b\}$; no relabelling of blocks turns one into the other.
> Now compute their images:
> - **Flattening (union):** $\mu_A(\Gamma_1) = \{a\} \cup \{a, b\} = \{a, a, b\}$ and $\mu_A(\Gamma_2) = \{a, a\} \cup \{b\} = \{a, a, b\}$. Equal.
> - **Shape (block-sizes):** $\Gamma_1$ has blocks of sizes $1$ and $2$, so $M^2 f(\Gamma_1) = \{1, 2\}$; $\Gamma_2$ has blocks of sizes $2$ and $1$, so $M^2 f(\Gamma_2) = \{2, 1\} = \{1, 2\}$. Equal (multisets ignore order).
>
> So $\Phi(\Gamma_1) = (\{a,a,b\}, \{1,2\}) = \Phi(\Gamma_2)$, yet $\Gamma_1 \neq \Gamma_2$.

**Step 3: Conclude the square is not a pullback.**

> [!note]- Derivation
> The comparison map $\Phi$ sends the two distinct elements $\Gamma_1, \Gamma_2 \in M^2 A$ to the same element of the pullback $MA \times_{M1} M^2 1$. Hence $\Phi$ is not injective, so it is not a bijection, so the multiplication naturality square for $f : \{a,b\} \to 1$ is **not** a pullback. By the definition of a cartesian monad (which requires *every* naturality square of $\mu$ to be a pullback), $M$ is not cartesian.
>
> The precise culprit is the symmetric quotient. The data lost is *which copies of $a$ were grouped together*: in $\Gamma_1$ one $a$ sits alone and one $a$ sits with $b$; in $\Gamma_2$ both $a$'s sit together. The union $\mu_A$ forgets this grouping (it just pools all elements), and the block-sizes record only $\{1,2\}$, which does not pin down the grouping when an element is repeated. In the *list* monad this information is preserved — the order of the flat list, cut at the prescribed lengths, recovers the grouping uniquely — which is exactly why $(-)^{*}$ is cartesian and $M$ is not. Symmetry is the obstruction.

> [!note]- Complete formal solution
> Take $A = \{a,b\}$ and $f : A \to 1$ the unique map. In the multiplication square for $f$, the comparison map is $\Phi : M^2 A \to MA \times_{M1} M^2 1$, $\Gamma \mapsto (\mu_A \Gamma, M^2 f\, \Gamma)$, where $\mu_A$ is union and $M^2 f$ records the multiset of block-sizes. The elements
> $$\Gamma_1 = \{\{a\}, \{a,b\}\}, \qquad \Gamma_2 = \{\{a,a\}, \{b\}\}$$
> are distinct in $M^2 A$ but satisfy $\mu_A(\Gamma_1) = \{a,a,b\} = \mu_A(\Gamma_2)$ and $M^2 f(\Gamma_1) = \{1,2\} = M^2 f(\Gamma_2)$. Thus $\Phi(\Gamma_1) = \Phi(\Gamma_2)$ with $\Gamma_1 \neq \Gamma_2$, so $\Phi$ is not injective and the square is not a pullback. Therefore $M$ is not a cartesian monad. The lost information is the partition of the repeated element $a$, forgotten by the symmetric quotient $(-)^n/S_n$; the list monad preserves it via ordering, which is why $(-)^{*}$ is cartesian. $\blacksquare$

---

# Key Takeaways

**To refute a universal property, build one explicit witness — do not survey.** The entire proof is a single counterexample: two distinct points of the apex with the same image on both legs. This is the canonical shape of every "not a pullback / not a limit / not cartesian" argument, and it is far cheaper than checking the condition fails "in general". The reusable trigger is: when asked whether some comparison map is a bijection (and you suspect not), hunt for *two elements that the legs cannot distinguish*. The productive place to hunt is wherever a quotient or a forgetful operation throws information away, because that lost information is exactly what lets two apex elements collapse.

**Symmetry destroys cartesianness, and a repeated element is the cleanest detector.** The witness works precisely because $a$ appears twice in the flattening: with all-distinct elements, the partition would be recoverable and this particular square would look fine. The lesson is a fast diagnostic — *to test whether a "free symmetric structure" monad is cartesian, flatten a configuration with a repeated element and ask whether the partition survives*. It never does, because the symmetric quotient is exactly the act of forgetting order, and order is what makes partitions reconstructible. This single test instantly disqualifies the multiset, free-commutative-monoid, free-abelian-group, and symmetric-algebra monads from the framework.

**This is *why* the chapter delivers non-symmetric operads, not symmetric ones.** The failure here is not a defect to be patched but a structural fact that carves higher category theory in two. Because the multiset monad is not cartesian, symmetric operads cannot be obtained as $M$-operads, and the cartesian-monad framework yields only *non-symmetric* (plain) operads — see [[Thm - Generalized Operads Recover Classical Structures]]. Symmetric operads require the genuinely different symmetric-sequences technology (HC3). The trigger to carry forward is: the moment a structure involves "unordered inputs" or "inputs up to permutation", it lives *outside* this chapter's framework, and you should reach for symmetric sequences instead. The contrast with [[Ex - The list monad is cartesian]] — same computation, opposite outcome, with ordering the only difference — is the sharpest way to remember where the boundary lies.
