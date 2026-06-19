---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Cartesian Closed Category"
  - "Def - Adjunction"
  - "Def - Product and Coproduct"
tags: [category-theory, foundations]
---

# Problem Statement

**(a)** In $\mathbf{Set}$, verify the currying isomorphism $\mathbf{Set}(A\times B, C)\cong\mathbf{Set}(A, C^B)$ explicitly, where $C^B$ is the set of functions $B\to C$, and show it is natural in $A$.

**(b)** Identify the evaluation map $\mathrm{ev} : C^B\times B\to C$ as the **counit** of the adjunction $(-\times B)\dashv(-)^B$, and the map $A\to(A\times B)^B$ as the unit.

**(c)** Derive the exponential law $C^{B\times B'}\cong(C^B)^{B'}$ from iterating the adjunction, and explain why $(C\times D)^B\cong C^B\times D^B$ follows from [[Thm - Right Adjoints Preserve Limits|RAPL]].

**Recall:**

![[Def - Cartesian Closed Category#The Definition]]

The [[Def - Adjunction|adjunction]] $(-\times B)\dashv(-)^B$ has counit the evaluation $\mathrm{ev}$ and unit the "name of the pairing". A [[Def - Product and Coproduct|product]] is a limit.

---

# Convergent Strategy

**Problem class:** This is a "verify the cartesian closed structure and harvest its exponential laws" problem. The currying isomorphism is the adjunction $(-\times B)\dashv(-)^B$; the exponential laws are formal consequences of iterating and of [[Thm - Right Adjoints Preserve Limits|RAPL]].

**Assumption pattern:** The key fact is the universal property of the exponential: a map $A\times B\to C$ is the same as a map $A\to C^B$, via $\widehat{f}(a) = f(a, -)$. This is currying; everything else follows formally.

**Theorem routing:** Verify the bijection and naturality (a) $\Rightarrow$ identify $\mathrm{ev}$ as counit, the pairing-name as unit (b) $\Rightarrow$ iterate the adjunction for $C^{B\times B'}\cong(C^B)^{B'}$ and apply [[Thm - Right Adjoints Preserve Limits|RAPL]] (right adjoint $(-)^B$ preserves products) for $(C\times D)^B\cong C^B\times D^B$ (c).

**Key decision point:** The exponential laws should be derived *abstractly* — $C^{B\times B'}\cong(C^B)^{B'}$ by composing two adjunctions, and $(C\times D)^B\cong C^B\times D^B$ because the right adjoint $(-)^B$ preserves the limit $C\times D$ — rather than by element computations. The abstract derivation works in any CCC (e.g. $\mathbf{Cat}$, presheaves), not just $\mathbf{Set}$.

---

# Legal Operations Used

1. **Operation 10 from the topic page (curry in a cartesian closed category).** The whole exercise is the currying adjunction.

2. **Operation 1 from the topic page (transpose across the adjunction).** Currying is the transpose; evaluation is the counit.

3. **Operation 4 from the topic page (apply RAPL).** Part (c) uses that the right adjoint $(-)^B$ preserves products.

---

# Hints

> [!note]- Hint 1
> Currying: a function $f : A\times B\to C$ gives, for each $a$, a function $f(a,-) : B\to C$, i.e. an element of $C^B$. So $\widehat{f} : A\to C^B$, $a\mapsto f(a,-)$. Check this is a bijection with inverse uncurrying $g\mapsto((a,b)\mapsto g(a)(b))$.

> [!note]- Hint 2
> Evaluation $\mathrm{ev} : C^B\times B\to C$, $(\phi, b)\mapsto\phi(b)$, is $\Phi^{-1}(1_{C^B})$ — the counit. The unit $\eta_A : A\to(A\times B)^B$ is $a\mapsto(b\mapsto(a,b))$, the transpose of $1_{A\times B}$.

> [!note]- Hint 3
> For $C^{B\times B'}\cong(C^B)^{B'}$: a map into $C^{B\times B'}$ from $A$ is a map $A\times(B\times B')\to C$; reassociate to $(A\times B')\times B\to C$, which is a map $A\times B'\to C^B$, i.e. a map $A\to(C^B)^{B'}$. For $(C\times D)^B$: $(-)^B$ is a right adjoint, so it preserves the product $C\times D$.

---

# Solution

Currying is the adjunction $(-\times B)\dashv(-)^B$. Evaluation is its counit. The exponential laws are formal: one from iterating the adjunction, one from RAPL.

**Step 1: The currying bijection (part a).**

$\mathbf{Set}(A\times B, C)\cong\mathbf{Set}(A, C^B)$, natural in $A$.

> [!note]- Derivation
> Define $\Lambda : \mathbf{Set}(A\times B, C)\to\mathbf{Set}(A, C^B)$ by $\Lambda(f)(a) = f(a, -)$, the function $b\mapsto f(a,b)$. Its inverse is uncurrying $\Lambda^{-1}(g)(a, b) = g(a)(b)$. Check:
> - $\Lambda^{-1}(\Lambda(f))(a,b) = \Lambda(f)(a)(b) = f(a,b)$, so $\Lambda^{-1}\Lambda = \mathrm{id}$.
> - $\Lambda(\Lambda^{-1}(g))(a) = \Lambda^{-1}(g)(a,-) = (b\mapsto g(a)(b)) = g(a)$, so $\Lambda\Lambda^{-1} = \mathrm{id}$.
>
> **Naturality in $A$.** For $h : A'\to A$, $\Lambda(f\circ(h\times 1_B))(a') = f(h(a'), -) = \Lambda(f)(h(a')) = (\Lambda(f)\circ h)(a')$. So $\Lambda(f\circ(h\times 1_B)) = \Lambda(f)\circ h$, the naturality square. Hence $(-\times B)\dashv(-)^B$.

**Step 2: Evaluation as counit, pairing as unit (part b).**

> [!note]- Derivation
> The counit is $\varepsilon_C = \Lambda^{-1}(1_{C^B}) : C^B\times B\to C$. Computing: $\Lambda^{-1}(1_{C^B})(\phi, b) = 1_{C^B}(\phi)(b) = \phi(b)$. So $\varepsilon_C = \mathrm{ev}$, evaluation $(\phi, b)\mapsto\phi(b)$ — application of a function to its argument.
>
> The unit is $\eta_A = \Lambda(1_{A\times B}) : A\to(A\times B)^B$. Computing: $\Lambda(1_{A\times B})(a) = 1_{A\times B}(a, -) = (b\mapsto(a, b))$. So $\eta_A(a)$ is the function $b\mapsto(a, b)$ — "pair $a$ with $-$". This is the name of the pairing.
>
> The first triangle identity $\mathrm{ev}\circ(\widehat{f}\times 1_B) = f$ is the basic computation rule: curry $f$, then evaluate, and you recover $f$.

**Step 3: Exponential laws (part c).**

$C^{B\times B'}\cong(C^B)^{B'}$ and $(C\times D)^B\cong C^B\times D^B$.

> [!note]- Derivation
> **Iterated currying.** For any $A$, natural in $A$:
> $$\mathbf{Set}(A, C^{B\times B'})\cong\mathbf{Set}(A\times(B\times B'), C)\cong\mathbf{Set}((A\times B')\times B, C)\cong\mathbf{Set}(A\times B', C^B)\cong\mathbf{Set}(A, (C^B)^{B'}),$$
> using currying twice and associativity/commutativity of the product. By [[Thm - The Yoneda Lemma|Yoneda]], $C^{B\times B'}\cong(C^B)^{B'}$. (This is the categorical "$c^{bb'} = (c^b)^{b'}$".)
>
> **Right adjoint preserves products.** The functor $(-)^B$ is a *right* adjoint (to $(-)\times B$). By [[Thm - Right Adjoints Preserve Limits|RAPL]], it preserves limits, in particular products: $(C\times D)^B\cong C^B\times D^B$. (Categorical "$(cd)^b = c^b d^b$".) Likewise $1^B\cong 1$ (the right adjoint preserves the terminal object/empty product), and $C^1\cong C$ (currying over the terminal object: $\mathbf{Set}(A\times 1, C)\cong\mathbf{Set}(A, C)$).

> [!note]- Complete formal solution
> **(a)** $\Lambda(f)(a) = f(a,-)$ and $\Lambda^{-1}(g)(a,b) = g(a)(b)$ are mutually inverse, and $\Lambda$ is natural in $A$ ($\Lambda(f\circ(h\times 1)) = \Lambda(f)\circ h$). So $(-\times B)\dashv(-)^B$ with $\mathbf{Set}(A\times B, C)\cong\mathbf{Set}(A, C^B)$.
>
> **(b)** Counit $\varepsilon_C = \Lambda^{-1}(1_{C^B}) = \mathrm{ev} : (\phi, b)\mapsto\phi(b)$. Unit $\eta_A = \Lambda(1_{A\times B}) : a\mapsto(b\mapsto(a,b))$.
>
> **(c)** $C^{B\times B'}\cong(C^B)^{B'}$ by currying twice (Yoneda); $(C\times D)^B\cong C^B\times D^B$ because the right adjoint $(-)^B$ preserves products (RAPL), and $C^1\cong C$, $1^B\cong 1$. $\blacksquare$

---

# Key Takeaways

**Currying is an adjunction, and the exponential laws are its formal consequences — they hold in every CCC, not just $\mathbf{Set}$.** The familiar bijection "a function of two arguments is a function of one argument valued in functions" is precisely the adjunction $(-\times B)\dashv(-)^B$. Once you see currying this way, the laws of exponents ($c^{bb'} = (c^b)^{b'}$, $(cd)^b = c^b d^b$, $c^1 = c$, $1^b = 1$) are not arithmetic facts to memorize but categorical theorems: the first from iterating the adjunction, the rest from the right adjoint $(-)^B$ preserving limits ([[Thm - Right Adjoints Preserve Limits|RAPL]]). Because the derivations are abstract, the same laws hold in $\mathbf{Cat}$ (functor categories), in presheaf categories, and in any Heyting algebra — the exponential laws of intuitionistic logic. The trigger to deploy this is any "internal hom" or "object of maps": it is a right adjoint to a product, and it obeys the exponential laws automatically.

**Evaluation is the counit; the counit is "apply".** The map $\mathrm{ev} : C^B\times B\to C$, $(\phi, b)\mapsto\phi(b)$, is the counit of the currying adjunction, and the first triangle identity $\mathrm{ev}\circ(\widehat{f}\times 1) = f$ is the computation rule "curry then evaluate is the identity" — the $\beta$-reduction rule of the lambda calculus. This identifies the abstract counit with a concrete, familiar operation, which is the pattern across all adjunctions: the counit *evaluates* (multiply a word out, sum a combination, apply a function). Recognising evaluation as a counit is what connects the cartesian closed structure to computation: function application *is* the counit, and the whole operational semantics of typed lambda calculus is the unit-counit calculus of a CCC.

**Right adjoint preservation gives the "distributive" exponential laws for free.** That $(C\times D)^B\cong C^B\times D^B$ and $1^B\cong 1$ follow from a single observation — $(-)^B$ is a right adjoint, hence preserves limits — is the cleanest illustration of harvesting RAPL. You do not verify these laws by hand in each CCC; you note the functor's handedness and apply the theorem. Dually, the left adjoint $(-)\times B$ preserves colimits, giving the *distributive law* $A\times(X\sqcup Y)\cong(A\times X)\sqcup(A\times Y)$ in any CCC with coproducts — which is why CCCs with coproducts are distributive categories, the categorical home of "if-then-else" and sum types. This exercise is the computational core; the companion [[Ex - Curry-Howard-Lambek correspondence|Curry-Howard-Lambek correspondence]] reads the same structure as logic and type theory.
