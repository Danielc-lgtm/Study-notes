---
type: definition
subject: category-theory
prereqs:
  - "Def - Monad and Comonad"
  - "Def - Functor"
  - "Def - Natural Transformation"
  - "Def - Adjunction"
tags: [category-theory, foundations]
---

# Notation

Throughout, $(T, \eta, \mu)$ is a [[Def - Monad and Comonad|monad]] on a [[Def - Category|category]] $\mathcal{C}$, with $T : \mathcal{C} \to \mathcal{C}$ the endofunctor, $\eta : 1_{\mathcal{C}} \Rightarrow T$ the unit (component $\eta_A : A \to TA$), and $\mu : T^2 \Rightarrow T$ the multiplication (component $\mu_A : T^2A \to TA$). A $T$-algebra is written $(A, a)$ with $A$ an object and $a : TA \to A$ its **structure map**. The Eilenberg–Moore category is $\mathcal{C}^T$; its forgetful functor is $U^T : \mathcal{C}^T \to \mathcal{C}$, $(A,a) \mapsto A$, and its free functor is $F^T : \mathcal{C} \to \mathcal{C}^T$. The full symbol registry is on [[Category Theory V — Monads, Algebras, and Monoidal Categories]].

---

# Axiom Motivation

A [[Def - Monad and Comonad|monad]] $T$ on $\mathbf{Set}$ is a syntax: it tells you how to form *formal* expressions out of the elements of a set, and how to flatten nested formal expressions. For the list monad, $TA$ is formal words in $A$; for the free-group monad, formal reduced words in $A \cup A^{-1}$; for the free-module monad, formal linear combinations. But a syntax with no semantics is inert. An **algebra** is the missing semantics: a rule that takes a formal expression and *actually evaluates it* to a genuine element. If $TA$ is "formal words in $A$" then a structure map $a : TA \to A$ is a rule that takes a formal word and multiplies it out to an element of $A$. The question is which rules deserve to be called evaluations, and the answer forces the two algebra axioms.

The first demand is that **evaluation must be trivial on generators**. A single generator $x \in A$, viewed as the formal expression $\eta_A(x)$ (the one-letter word $(x)$, or the singleton sum $1\cdot x$), should evaluate back to $x$ itself. There is no other sensible value: a length-one expression has no operations to perform. So we require
$$a \circ \eta_A = 1_A.$$
Drop this and "evaluation" could send the generator $x$ to some unrelated element; the map $a$ would not be evaluating the formal expression at all, just permuting elements. With it, the inclusion of generators is a section of $a$, so every element of $A$ is the value of at least the trivial expression naming it.

The second demand is that **evaluation must be consistent with flattening**. Take a *nested* expression $w \in T^2 A$ — a word of words, a sum of sums. There are two ways to evaluate it to an element of $A$. You can flatten first and then evaluate: apply $\mu_A$ to collapse the nesting into a single expression in $TA$, then apply $a$. Or you can evaluate the inner expressions first and then evaluate the outer one: apply $Ta$ (evaluate each inner word, producing a word of elements still in $TA$), then apply $a$. For "evaluate the formal expression" to be a coherent operation, these must agree:
$$a \circ \mu_A = a \circ Ta \qquad (\text{as maps } T^2A \to A).$$
This is the heart of the definition. It says the monad's own flattening $\mu$ and the algebra's evaluation $a$ are compatible — evaluation does not care whether you collapse the syntax all at once or stage by stage. Drop it and "the value of a nested expression" is ambiguous, exactly the pathology the monad's associativity axiom was designed to forbid at the syntactic level, now demanded at the semantic level.

Why exactly these two and no third? Because together they say precisely "$a$ is an action of the monad $T$ on the object $A$," in the same way that a [[Def - Group|group]] action $G \times X \to X$ satisfies $e \cdot x = x$ and $(gh)\cdot x = g \cdot (h \cdot x)$. The unit law is "the identity acts trivially"; the associativity law is "multiplying then acting equals acting then acting." The monad replaces the group $G$, the endofunctor $T(-)$ replaces $G \times (-)$, and the algebra is the action. Could a reader invent the definition? Yes — demand that a structure map "evaluate formal expressions" coherently, and you are forced to a unit law (trivial on generators) and an associativity law (compatible with flattening), which are exactly the two axioms.

A morphism of algebras must then be a map that **commutes with evaluation**: $f : (A,a) \to (B,b)$ should satisfy $f \circ a = b \circ Tf$, i.e. "evaluate then transport" equals "transport then evaluate." For the list monad this is exactly the homomorphism condition $f(x_1 \cdots x_n) = f(x_1)\cdots f(x_n)$. The square is forced by demanding that $f$ respect the algebraic structure encoded by the monad.

---

# The Definition

Let $(T, \eta, \mu)$ be a monad on $\mathcal{C}$. A **$T$-algebra** (or **Eilenberg–Moore algebra**) is a pair $(A, a)$ where $A$ is an object of $\mathcal{C}$ and $a : TA \to A$ is a morphism, the **structure map**, such that the following commute:

**Unit law** ($A \to A$):
$$a \circ \eta_A = 1_A.$$

**Associativity law** ($T^2A \to A$):
$$a \circ \mu_A = a \circ Ta.$$

In diagram form:
$$\begin{array}{ccc}
A & \xrightarrow{\;\eta_A\;} & TA \\
& {\scriptstyle 1_A}\searrow & \big\downarrow{\scriptstyle a} \\
& & A
\end{array}
\qquad\qquad
\begin{array}{ccc}
T^2A & \xrightarrow{\;T a\;} & TA \\
{\scriptstyle \mu_A}\big\downarrow & & \big\downarrow{\scriptstyle a} \\
TA & \xrightarrow{\;\;a\;\;} & A
\end{array}$$

A **morphism of $T$-algebras** $f : (A,a) \to (B,b)$ is a morphism $f : A \to B$ in $\mathcal{C}$ such that $f \circ a = b \circ Tf$. These objects and morphisms form the **Eilenberg–Moore category** $\mathcal{C}^T$, with composition and identities inherited from $\mathcal{C}$.

There are two canonical functors. The **forgetful functor** $U^T : \mathcal{C}^T \to \mathcal{C}$ sends $(A,a) \mapsto A$ and $f \mapsto f$. The **free functor** $F^T : \mathcal{C} \to \mathcal{C}^T$ sends an object $X$ to the **free algebra** $(TX, \mu_X)$ — the structure map being the monad's own multiplication — and a morphism $g : X \to Y$ to $Tg$. One has $F^T \dashv U^T$, an adjunction inducing $T$; its unit is $\eta$ and the structure map of every algebra is the counit's component.

---

# Categorical / Structural Definition

The structural reading is that **a $T$-algebra is an action of the monoid $T$ on an object, exactly as a [[Def - Group|group]] action is an action of a group on a set.** Recall (from [[Def - Monad and Comonad]]) that $T$ is a [[Def - Monoid in a Monoidal Category|monoid]] in the monoidal category $([\mathcal{C},\mathcal{C}], \circ, 1)$. A module over a monoid $M$ in a monoidal category is an object $A$ with an action $M \otimes A \to A$ satisfying unit and associativity laws; here $\otimes = \circ$ acts on objects of $\mathcal{C}$ via evaluation $T \otimes A = TA$, and the action $a : TA \to A$ with its two laws is precisely a module over the monoid $T$. So:

$$\text{$T$-algebra} \;=\; \text{module over the monoid } T \text{ in } ([\mathcal{C},\mathcal{C}], \circ, 1).$$

This identifies the Eilenberg–Moore category $\mathcal{C}^T$ as the category of $T$-modules, and it is the abstract reason the algebra laws look like an action: they *are* one. The forgetful functor $U^T$ is then "forget the action," and the free functor $F^T$ is "act freely," $X \mapsto (TX, \mu_X)$ — the regular action of $T$ on itself.

---

# Relate to Other Fields / Compression

The Eilenberg–Moore construction is the categorical formalization of **universal algebra**: a monad on $\mathbf{Set}$ is a (possibly infinitary) algebraic theory, and its algebras are the models. Groups, [[Def - Ring|rings]], [[Def - Module|modules]], lattices, and Boolean algebras are each $\mathcal{C}^T$ for the appropriate $T$, which is why they all share a free functor, a forgetful functor, free objects, and presentations by generators and relations. The slogan "$T$-algebras for the free-group monad are groups" is the assertion that the *formal* operations packaged by the monad, once you demand they be coherently evaluable, reconstruct *exactly* the group axioms.

**True name:** a $T$-algebra is **an action of the monad** — a coherent rule for evaluating the formal expressions $T$ builds. The structure map $a : TA \to A$ is best read as "perform the formal operation": it multiplies a formal word, sums a formal linear combination, unions a family of subsets. The two axioms are "trivial expressions evaluate to themselves" and "nested expressions evaluate consistently."

This compresses the relationship between a structure and its free version. A group is not "a set plus opaque group-ness"; it is a set $A$ together with a chosen way $a : TA \to A$ to multiply out any formal word — and the group axioms are forced once you require $a$ to be a coherent action. The forgetful functor $\mathbf{Grp} \to \mathbf{Set}$ forgets the action, not some inscrutable extra data.

---

# Examples / Corollaries

**Is an instance — algebras for the list monad are monoids.** For $T A = A^*$, a structure map $a : A^* \to A$ assigns to each word $(x_1, \dots, x_n)$ an element of $A$. The unit law forces $a(x) = x$ on length-one words; the associativity law forces $a$ to respect concatenation, so $a(w_1 \frown w_2) = a(w_1) \cdot a(w_2)$ where $\cdot$ is the binary operation $a(x,y)$. Setting $1 = a()$ (the empty word) and $x \cdot y = a(x,y)$ yields exactly a [[Def - Monoid in a Monoidal Category|monoid]], and the axioms come out of associativity of $a$. Hence $\mathbf{Set}^T \simeq \mathbf{Mon}$.

**Is an instance — algebras for the free-group monad are groups.** For $T = UF$ the free-group monad, a structure map evaluates a reduced word in $A \cup A^{-1}$ to an element of $A$; the laws force this to be a group multiplication with inverses, so $\mathbf{Set}^T \simeq \mathbf{Grp}$ (full proof in [[Ex - Algebras for the free-group monad are groups]]).

**Is an instance — algebras for the free-module monad are modules.** For $T A = R[A]$, the free $R$-module on $A$, a structure map evaluates a formal $R$-linear combination $\sum r_i a_i$ to an actual element; the laws force $A$ to be an [[Def - Module|module]] over $R$ and $a$ its linear-combination operation. Hence $\mathbf{Set}^{R[-]} \simeq \mathbf{Mod}_R$ (see [[Ex - Algebras for the free-vector-space monad]] for $R = k$ a field).

**Is an instance — algebras for the power-set monad are complete lattices.** For $T = P$, a structure map $a : P(A) \to A$ assigns to each subset a "supremum"; the unit law gives $a(\{x\}) = x$ and the associativity law gives compatibility of nested unions with the assignment, which is exactly the data of arbitrary joins. So $\mathbf{Set}^P \simeq$ complete (sup-)lattices, with algebra morphisms the sup-preserving maps.

**Is NOT an instance — a structure map violating the unit law.** Take the list monad and define $a : A^* \to A$ by sending *every* word, including singletons, to a fixed element $a_0 \in A$. This respects concatenation in a degenerate sense but fails $a(x) = x$, so it is not a $T$-algebra. The failure shows the unit law is doing real work: it forbids "evaluations" that ignore their generators.

**Corollary — free algebras.** For any object $X$, the pair $(TX, \mu_X)$ is a $T$-algebra: the unit law is the monad's right unit axiom $\mu_X \circ \eta_{TX} = 1$ and the associativity law is the monad's associativity $\mu_X \circ \mu_{TX} = \mu_X \circ T\mu_X$. These free algebras form the image of $F^T$ and constitute the [[Def - Kleisli Category|Kleisli category]] inside $\mathcal{C}^T$.

**Calibration check.** Verify that for the list monad the empty-word value $a()$ is forced to be a two-sided unit for $x\cdot y = a(x,y)$; verify that the free algebra $(TX, \mu_X)$ satisfies both axioms using only the monad laws; and confirm that an algebra morphism for the list monad is exactly a [[Def - Monoid in a Monoidal Category|monoid]] homomorphism.

---

# Unlocked by This

> [!tip] The Kleisli Category and Monadicity *(from this chapter)*
> The free algebras $(TX, \mu_X)$ form the [[Def - Kleisli Category|Kleisli category]], and the question of whether a given concrete category *equals* $\mathcal{C}^T$ is answered by the [[Thm - The Barr-Beck Monadicity Theorem|Barr–Beck theorem]].

> [!tip] Universal Algebra and Lawvere Theories *(from Algebra)*
> Eilenberg–Moore categories of finitary monads on $\mathbf{Set}$ are exactly the categories of models of **Lawvere theories**. This is the categorical formulation of **universal algebra**, unifying groups, rings, modules, and lattices as algebras for a monad.

> [!tip] Modules over a Ring as Eilenberg–Moore Algebras *(from Algebraic Geometry)*
> For a commutative [[Def - Ring|ring]] $R$, the monad $R \otimes_R (-)$ (and base-change monads $S \otimes_R (-)$) have modules as algebras; the comonadic dual organizes **faithfully flat descent** of quasi-coherent sheaves on a **scheme**.
