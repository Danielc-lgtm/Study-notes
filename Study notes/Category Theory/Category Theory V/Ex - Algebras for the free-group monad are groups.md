---
type: exercise
subject: category-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Algebra for a Monad"
  - "Def - Monad and Comonad"
  - "Def - Group"
  - "Def - Free Group and Free Product"
tags: [category-theory, foundations]
---

# Problem Statement

Let $F : \mathbf{Set} \to \mathbf{Grp}$ be the [[Def - Free Group and Free Product|free group]] functor and $U : \mathbf{Grp} \to \mathbf{Set}$ the forgetful functor, with induced [[Def - Monad and Comonad|monad]] $T = UF$ on $\mathbf{Set}$: $TA$ is the set of reduced words in the alphabet $A \cup A^{-1}$, $\eta_A$ includes generators, and $\mu_A$ multiplies a word of words and re-reduces.

Prove that the [[Def - Algebra for a Monad|Eilenberg–Moore category]] $\mathbf{Set}^T$ is equivalent to the category of [[Def - Group|groups]] $\mathbf{Grp}$. Concretely: a $T$-algebra structure $a : TA \to A$ is exactly the data of a group structure on $A$, and $T$-algebra morphisms are exactly group homomorphisms.

**Recall:**

![[Def - Algebra for a Monad#The Definition]]

![[Def - Group#The Definition]]

The [[Def - Free Group and Free Product|free group]] $F(A)$ on a set $A$ has elements the reduced words in $A \cup A^{-1}$, with concatenation-and-reduction as multiplication; it satisfies the universal property that any function $A \to UG$ extends uniquely to a homomorphism $F(A) \to G$.

---

# Convergent Strategy

**Problem class:** An "identify the category of algebras" problem — the most important target of §5.2. The goal is to recognize $\mathbf{Set}^T$ as a familiar algebraic category by reading the structure map as "evaluate the formal expression."

**Assumption pattern:** The data is the free-group monad and an abstract algebra structure map $a : TA \to A$. The assumption to leverage is that $TA$ is "formal reduced words," so $a$ is "multiply out a word" (legal operation 3); the algebra laws then force exactly the group operations.

**Theorem routing:** Route through [[Def - Algebra for a Monad]]: extract a binary operation, identity, and inverse from $a$ via the words of length 2, 0, and the inverse-letter; use the unit law to fix their behaviour on generators and the associativity law to force the group axioms. Then build the inverse functor $\mathbf{Grp} \to \mathbf{Set}^T$ and check the two functors are mutually inverse up to natural iso.

**Key decision point:** The crux is that the structure map $a$ must be *consistent with reduction*: $a(x x^{-1})$ must equal $a$ of the empty word, which forces $x \cdot x^{-1} = e$. The non-obvious step is realizing that the *reduction* built into the free group (not just concatenation) is what supplies inverses — the list monad gives only monoids; the extra $A^{-1}$ letters and reduction give groups.

---

# Legal Operations Used

1. **Operation 3 from the topic page (build the structure map of an algebra).** We read $a : TA \to A$ as "multiply out a reduced word," extracting $\cdot$, $e$, and $(-)^{-1}$ from the values of $a$ on short words.

2. **Operation 1 from the topic page (read a monad off an adjunction).** The monad $T = UF$ is given as the shadow of the free-group adjunction.

3. **Operation 5 from the topic page (Barr–Beck recognition), in spirit.** The equivalence $\mathbf{Set}^T \simeq \mathbf{Grp}$ is the conclusion that the comparison functor $\mathbf{Grp} \to \mathbf{Set}^T$ is an equivalence — the monadicity of $\mathbf{Grp} \to \mathbf{Set}$ specialized.

---

# Hints

> [!note]- Hint 1
> A $T$-algebra structure map $a : TA \to A$ takes a reduced word in $A \cup A^{-1}$ and returns an element of $A$. Read it as "multiply out the word." Extract operations: $x \cdot y := a(xy)$ (word of length 2), $e := a(\varnothing)$ (empty word), $x^{-1}_{\text{op}} := a(x^{-1})$ (the inverse-letter).

> [!note]- Hint 2
> The unit law $a \circ \eta_A = 1$ forces $a(x) = x$ on single generators. The associativity law $a\circ\mu_A = a\circ Ta$ forces $a$ to respect multiplication-of-words: evaluating a word-of-words equals evaluating each piece and multiplying.

> [!note]- Hint 3
> Crucially, $a$ is defined on *reduced* words, and $\mu$ re-reduces. So $a(x\,x^{-1}) = a(\varnothing) = e$ because $x x^{-1}$ reduces to the empty word. This is what gives $x \cdot x^{-1}_{\text{op}} = e$ — the inverse axiom — and it is exactly what the list monad lacks.

> [!note]- Hint 4
> For the equivalence: the forgetful functor $\mathbf{Grp}\to\mathbf{Set}^T$ sends a group $G$ to $(UG, a_G)$ where $a_G$ multiplies out a reduced word in $G$. Check this is inverse (up to natural iso) to the functor extracting a group from an algebra.

---

# Solution

The plan: (1) from an algebra $(A,a)$ extract a binary operation, identity, and inverse; (2) use the algebra laws to verify the [[Def - Group|group axioms]], with the reduction in $T$ supplying inverses; (3) build the comparison functor from groups and show the two assignments are mutually inverse, giving the equivalence. The crux is that "evaluate a reduced word" already obeys associativity (from the algebra law) and inverses (from reduction).

**Step 1: Extract the group operations from $a$.**

> [!note]- Derivation
> Let $(A, a)$ be a $T$-algebra, $a : TA \to A$. Recall $TA$ = reduced words in $A \cup A^{-1}$. Define
> $$x \cdot y := a(xy), \qquad e := a(\varnothing), \qquad \bar{x} := a(x^{-1}),$$
> where $xy$ is the length-two word (reduced unless $y = x^{-1}$, in which case it reduces to $\varnothing$), $\varnothing$ is the empty word, and $x^{-1}$ is the single inverse-letter. The unit law $a\circ\eta_A = 1_A$ gives $a(x) = x$ for every generator $x \in A$. These are the candidate group operations on $A$.

**Step 2: The associativity law forces "evaluate = multiply out."**

> [!note]- Derivation
> The algebra associativity law $a \circ \mu_A = a \circ Ta$ says: for a word-of-words $W \in T^2A$, evaluating the flattened word equals applying $a$ to each inner word and then evaluating the resulting word. In particular, for the word-of-words $((x_1\cdots x_m),(y_1\cdots y_n))$,
> $$a\big((x_1\cdots x_m)(y_1\cdots y_n)\big) = a\big(\,a(x_1\cdots x_m)\ a(y_1\cdots y_n)\,\big),$$
> i.e. $a$ of a concatenation equals the product (via $\cdot$) of the two evaluations. Inductively, $a(z_1 z_2 \cdots z_k) = a(z_1)\cdot a(z_2) \cdots a(z_k)$ (with $a(z_i) = z_i$ or $\bar z_i$ for generators or inverse-letters). So $a$ is "multiply out the word using $\cdot$, $e$, $\bar{(-)}$."

**Step 3: Verify the group axioms.**

> [!note]- Derivation
> *Associativity of $\cdot$.* Using Step 2, $(x\cdot y)\cdot z = a(a(xy)\,z) = a(xyz) = a(x\,a(yz)) = x\cdot(y\cdot z)$, since both equal $a$ of the length-three word $xyz$.
>
> *Identity.* $e\cdot x = a(\varnothing\, x) = a(x) = x$ (the empty word concatenated with $x$ reduces to $x$), and similarly $x \cdot e = x$. So $e$ is a two-sided unit.
>
> *Inverses.* Here is where reduction matters. The length-two word $x\, x^{-1}$ **reduces to the empty word** $\varnothing$ in the free group. Since $a$ is defined on reduced words and $\mu$ re-reduces, $a(x\,x^{-1}) = a(\varnothing) = e$. But by Step 2, $a(x\, x^{-1}) = a(x)\cdot a(x^{-1}) = x \cdot \bar x$. Hence $x \cdot \bar x = e$, and symmetrically $\bar x \cdot x = e$. So $\bar x = a(x^{-1})$ is a two-sided inverse for $x$.
>
> Therefore $(A, \cdot, e, \bar{(-)})$ is a [[Def - Group|group]].

**Step 4: The equivalence $\mathbf{Set}^T \simeq \mathbf{Grp}$.**

> [!note]- Derivation
> Define $\Phi : \mathbf{Set}^T \to \mathbf{Grp}$ by $\Phi(A,a) = (A,\cdot,e,\bar{(-)})$ as above, and on morphisms identically. A $T$-algebra morphism $f : (A,a) \to (B,b)$ satisfies $f\circ a = b\circ Tf$; evaluating on length-two words gives $f(x\cdot_A y) = f(a(xy)) = b(Tf(xy)) = b(f(x)f(y)) = f(x)\cdot_B f(y)$, so $f$ is a group homomorphism. Thus $\Phi$ is a functor.
>
> Define $\Psi : \mathbf{Grp} \to \mathbf{Set}^T$ by $\Psi(G) = (UG, a_G)$ where $a_G : TUG \to UG$ multiplies out a reduced word in $G$ (well-defined by the universal property of the free group: $a_G$ is the underlying function of the counit $\varepsilon_G : FUG \to G$). The algebra laws for $a_G$ hold because $\varepsilon$ is a group homomorphism satisfying the triangle identities. On a homomorphism $\phi$, $\Psi(\phi) = U\phi$.
>
> $\Phi\Psi = 1_{\mathbf{Grp}}$: starting from $G$, extracting $\cdot$ from $a_G$ recovers the multiplication of $G$. $\Psi\Phi \cong 1$: starting from $(A,a)$, the multiply-out map of the extracted group equals $a$ by Step 2. So $\Phi, \Psi$ are mutually inverse: $\mathbf{Set}^T \simeq \mathbf{Grp}$.

> [!note]- Complete formal solution
> Given a $T$-algebra $(A,a)$ with $TA$ = reduced words in $A\cup A^{-1}$, define $x\cdot y = a(xy)$, $e = a(\varnothing)$, $\bar x = a(x^{-1})$. The unit law gives $a(x) = x$; the associativity law gives $a(z_1\cdots z_k) = a(z_1)\cdots a(z_k)$ (multiply out). Then: associativity of $\cdot$ holds since $(x\cdot y)\cdot z = a(xyz) = x\cdot(y\cdot z)$; $e$ is a unit since $a(\varnothing x) = a(x) = x$; and $x\cdot\bar x = a(xx^{-1}) = a(\varnothing) = e$ because $xx^{-1}$ reduces to the empty word. So $(A,\cdot,e,\bar{(-)})$ is a group. The functors $\Phi(A,a) = (A,\cdot,e,\bar{(-)})$ and $\Psi(G) = (UG, \varepsilon_G)$ are mutually inverse (the multiply-out map equals $a$, and extracting $\cdot$ recovers $G$), and morphisms match (the algebra-morphism square is the homomorphism condition). Hence $\mathbf{Set}^T \simeq \mathbf{Grp}$. $\blacksquare$

> [!warning] Illegal but tempting: forgetting reduction and getting only monoids
> If one used the *free monoid* functor (words, no inverses, no reduction) the same argument would produce only a [[Def - Monoid in a Monoidal Category|monoid]] — there would be no inverse-letters and no reduction $xx^{-1}\to\varnothing$, so the inverse axiom would never appear. The reduction in the free group is doing essential work: it is precisely the syntactic relation $xx^{-1} = e$ that the algebra law converts into the group inverse axiom. Skipping it silently downgrades groups to monoids.

---

# Key Takeaways

**Reading the structure map as "multiply out the formal expression" is the universal technique.** For any free-algebra monad, the structure map $a : TA \to A$ should be read as a rule that evaluates the formal expressions $T$ builds, and the algebra associativity law $a\circ\mu = a\circ Ta$ is exactly the statement that this evaluation is a homomorphism on concatenation — so $a(z_1\cdots z_k) = a(z_1)\cdots a(z_k)$. Once you have this, the algebra axioms reproduce the defining axioms of whatever structure the monad is free for. The trigger is "identify $\mathbf{Set}^T$"; the reaction is "extract the operations from $a$ on short words and check the axioms fall out of the two algebra laws."

**Syntactic relations in the monad become algebraic axioms in the algebra.** The single most instructive point of this exercise is that the *reduction* $xx^{-1} \to \varnothing$ built into the free group is what produces the inverse axiom. The free-monoid monad has no such relation and yields only monoids; adding inverse-letters and the reduction relation to the syntax adds the inverse axiom to the semantics. This is the general phenomenon that a monad on $\mathbf{Set}$ is an *algebraic theory* — a signature of operations *and equations* — and the equations (here, reduction) are exactly the axioms its algebras satisfy. When you want algebras with a certain axiom, you build that axiom into the monad as a syntactic identity.

**Monadicity of an algebraic forgetful functor is a single clean equivalence.** This exercise is the hands-on version of the [[Thm - The Barr-Beck Monadicity Theorem|Barr–Beck theorem]] for groups: it shows directly that the comparison $\mathbf{Grp} \to \mathbf{Set}^T$ is an equivalence, which is the assertion that $\mathbf{Grp} \to \mathbf{Set}$ is monadic. The transferable diagnostic is that for any *algebraic* category — one defined by operations and equations — the forgetful functor to $\mathbf{Set}$ is monadic, so the category is recovered as the algebras of its free monad. Groups, [[Def - Ring|rings]], modules ([[Ex - Algebras for the free-vector-space monad]]), and lattices all work this way; the contrast is with [[Ex - Which forgetful functors are monadic|topological spaces and fields]], which are not algebraic and not monadic.
