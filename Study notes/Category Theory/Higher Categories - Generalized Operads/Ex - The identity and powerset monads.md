---
type: exercise
subject: higher-categories
difficulty: "⭐"
prereqs:
  - "Def - Cartesian Monad"
  - "Def - Monad and Comonad"
  - "Def - Pullback and Pushout"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

(a) Show that the **identity monad** $T = 1_{\mathcal{E}}$ on any category $\mathcal{E}$ with [[Def - Pullback and Pushout|pullbacks]] is a [[Def - Cartesian Monad|cartesian monad]].

(b) Show that the **powerset monad** $P$ on $\mathbf{Set}$ — $PX = \{S : S \subseteq X\}$, with unit $\eta_X(x) = \{x\}$ and multiplication $\mu_X(\mathcal{S}) = \bigcup \mathcal{S}$ (union of a set of subsets) — is **not** cartesian, by showing its unit $\eta$ is not a cartesian natural transformation.

**Recall:**

![[Def - Cartesian Monad#The Definition]]

A natural transformation $\alpha : F \Rightarrow G$ is cartesian when each naturality square (for $f : A \to B$, corners $FA, FB, GA, GB$) is a [[Def - Pullback and Pushout|pullback]]. In $\mathbf{Set}$, $A \times_C B = \{(a,b) : f(a) = g(b)\}$.

---

# Convergent Strategy

**Problem class:** A pair of *cartesianness checks* — one positive (the trivial base case), one negative (a quick refutation). Part (a) is the floor of the framework; part (b) is a one-square counterexample, the same shape as the multiset refutation but even shorter.

**Assumption pattern:** For (a) the assumption is that the identity functor and identity transformations are as well-behaved as possible — they preserve everything and their naturality squares are degenerate. For (b) the assumption to exploit is that $\eta_X(x) = \{x\}$ is a singleton but $\mu$ and the subsets allow *non-singleton* sets to interfere, breaking the singleton sub-family condition.

**Theorem routing:** Straight from the [[Def - Cartesian Monad|definition]]. For (a), observe identity functors preserve pullbacks and identity-transformation squares have parallel identity edges. For (b), write the unit square for a suitable $f$ and find two elements of the apex with the same image, or show the comparison map is not a bijection.

**Key decision point:** In (b), the choice is which map $f$ exposes the failure fastest. Collapsing a two-element set to a point, $f : \{a, b\} \to 1$, makes the unit square's pullback contain *every* subset of the fibre, not just singletons — so the comparison from $\{a,b\}$ to the pullback is far from surjective. The natural alternative of using an injective $f$ hides the failure, since injections behave better.

---

# Legal Operations Used

1. **Operation 3 from the topic page (check cartesianness as a checklist).** Used positively in (a) and negatively in (b).
2. **Operation 1 from the topic page (specialize the monad).** Working with the concrete identity and powerset descriptions.

---

# Hints

> [!note]- Hint 1
> For (a): the identity functor preserves all limits, and the naturality square of the identity transformation $1 : \mathrm{id} \Rightarrow \mathrm{id}$ for a map $f$ has $f$ on top, $f$ on the bottom, and identities on the sides — a square with two parallel identity edges is always a pullback.

> [!note]- Hint 2
> For (b): the unit square for $f : A \to B$ should make $A$ the pullback $PA \times_{PB} B = \{(S, b) : Pf(S) = \{b\}\}$. Ask whether *only singletons* $S$ satisfy $Pf(S) = \{b\}$.

> [!note]- Hint 3
> For (b), take $A = \{a_1, a_2\}$, $B = 1$, $f$ the unique map. Then $Pf(S) = \{*\}$ for *every* non-empty subset $S \subseteq A$, including $S = \{a_1, a_2\}$. So the pullback contains $(\{a_1,a_2\}, *)$, which is not in the image of $\eta_A$ (whose image is only singletons). The square is not a pullback.

---

# Solution

The plan is two short checks. Step 1 verifies the identity monad is cartesian by noting identity functors and transformations are maximally degenerate. Step 2 refutes cartesianness of the powerset monad by exhibiting a non-singleton subset that lands in a unit-square pullback, breaking the singleton sub-family condition.

**Step 1: The identity monad is cartesian.**

> [!note]- Derivation
> Let $T = 1_{\mathcal{E}}$ with $\eta = \mu = 1$ (the identity natural transformation). (i) *Preserves pullbacks:* the identity functor sends every pullback square to itself, so it preserves all pullbacks. (ii) *$\eta$ cartesian:* the naturality square of $\eta = 1$ for a map $f : A \to B$ is
> $$\begin{array}{ccc}
> A & \xrightarrow{\;f\;} & B \\
> {\scriptstyle 1_A}\big\downarrow & & \big\downarrow{\scriptstyle 1_B} \\
> A & \xrightarrow{\;f\;} & B
> \end{array}$$
> which has identity vertical edges; such a square is always a pullback (the apex $A$ is canonically $A \times_B B$ via $1_A$). (iii) *$\mu$ cartesian:* identical, since $\mu = 1$ as well. Hence $T = 1_{\mathcal{E}}$ is cartesian. This is the framework's floor: with the identity monad, $T$-multicategories are ordinary internal categories.

**Step 2: The powerset monad is not cartesian.**

> [!note]- Derivation
> Take $A = \{a_1, a_2\}$, $B = 1 = \{*\}$, and $f : A \to B$ the unique map. The unit naturality square is
> $$\begin{array}{ccc}
> A & \xrightarrow{\;f\;} & B \\
> {\scriptstyle \eta_A}\big\downarrow & & \big\downarrow{\scriptstyle \eta_B} \\
> PA & \xrightarrow{\;Pf\;} & PB
> \end{array}$$
> with $\eta_A(a) = \{a\}$ and $Pf(S) = \{f(s) : s \in S\}$. For the square to be a pullback we would need $A \cong PA \times_{PB} B = \{(S, b) : Pf(S) = \eta_B(b)\}$. Here $\eta_B(*) = \{*\}$, and $Pf(S) = \{*\}$ holds for *every non-empty* subset $S \subseteq A$, not only singletons. So the pullback contains $(\{a_1, a_2\}, *)$, since $Pf(\{a_1, a_2\}) = \{*\} = \eta_B(*)$. But $(\{a_1, a_2\}, *)$ is not in the image of the comparison $\eta_A : A \to PA \times_{PB} B$, whose image consists only of pairs $(\{a\}, *)$ with $a \in A$ (singletons). Thus the comparison map is not surjective, the square is not a pullback, and $P$ is not cartesian. *(Equivalently: $P$ also fails to preserve pullbacks, but the unit failure already suffices.)*

> [!note]- Complete formal solution
> **(a)** For $T = 1_{\mathcal{E}}$: the identity functor preserves all pullbacks, and the naturality squares of $\eta = \mu = 1$ have identity vertical edges, hence are pullbacks. So $T$ is cartesian.
>
> **(b)** For the powerset monad $P$, take $f : \{a_1, a_2\} \to 1$. In the unit square, the pullback $PA \times_{PB} B = \{(S, b) : Pf(S) = \{b\}\}$ contains $(\{a_1, a_2\}, *)$ because $Pf(\{a_1,a_2\}) = \{*\}$, yet the comparison map $\eta_A$ has image only the singletons $(\{a\}, *)$. So the comparison is not surjective, the square is not a pullback, and $P$ is not cartesian. $\blacksquare$

---

# Key Takeaways

**The identity monad is the framework's calibration point, and its cartesianness is automatic.** Whenever a definition in this chapter feels opaque, the first move is to set $T = \mathrm{id}$ and watch the structure collapse to something familiar — categories, monoids, ordinary composition. This exercise confirms the identity monad is cartesian for the most degenerate possible reason (everything in sight is an identity), which is why $T = \mathrm{id}$ is always a safe sanity check: any general theorem about cartesian monads must, in particular, hold for the identity, and reading it there tells you what the theorem "really says" about ordinary category theory before any arities enter.

**The singleton sub-family condition is what the unit's cartesianness encodes, and the powerset monad violates it loudly.** The unit $\eta$ being cartesian says that the "bare objects" sit inside $T$ along an exact pullback — that the only $T$-elements mapping to a singleton are themselves singletons. The powerset monad fails this maximally: *every* non-empty subset maps to a singleton under a collapse, so the singletons are nowhere near the whole fibre. The reusable diagnostic is to test the unit square against a collapse map $f : A \to 1$ and ask "do non-singleton elements sneak into the pullback?" — if they do, the unit is not cartesian. This is a one-line refutation and the fastest of all cartesianness tests.

**Good Eilenberg–Moore behaviour does not imply cartesianness.** The powerset monad has a perfectly nice category of algebras (complete sup-lattices) and is one of the most-used monads in mathematics, yet it sits *outside* this chapter's framework. The lesson is that "cartesian" is a genuinely restrictive, geometric condition about pullbacks and arities, not a measure of how useful a monad is. The trigger to remember: being a monad with good algebras is necessary for the Eilenberg–Moore story but irrelevant to whether $T$-multicategories make sense; for that, the pullback conditions must hold, and many excellent monads (powerset, multiset, free commutative monoid) simply do not satisfy them. Compare [[Ex - The list monad is cartesian]] (passes) and [[Ex - The free-commutative-monoid monad is not cartesian]] (fails) to see the boundary from both sides.
