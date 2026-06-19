---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Universal Element"
  - "Def - Hom-Functor and Representable Functor"
  - "Def - Category of Elements"
tags: [category-theory, foundations]
---

# Problem Statement

Let $\mathcal{P} : \mathbf{Set}^{op} \to \mathbf{Set}$ be the **contravariant power-set functor**, sending a set $X$ to $\mathcal{P}(X)$ and a function $f : X \to Y$ to the *preimage* map $\mathcal{P}(f)(T) = f^{-1}(T)$.

1. Show $\mathcal{P}$ is representable by the two-element set $\Omega = \{0, 1\}$, with the natural isomorphism $\mathbf{Set}(X, \Omega) \cong \mathcal{P}(X)$ given by characteristic functions.
2. Show the [[Def - Universal Element|universal element]] is the subset $\{1\} \in \mathcal{P}(\Omega)$ — *not* the element $1 \in \Omega$ — and verify the universal property directly.
3. Explain how this is the **subobject classifier** in the topos $\mathbf{Set}$, with $\{1\}$ the "true" element.

**Recall:**

![[Def - Universal Element#The Definition]]

A [[Def - Universal Element|universal element]] of a presheaf $F : \mathbf{Set}^{op} \to \mathbf{Set}$ is a pair $(\Omega, u)$ with $u \in F(\Omega)$ such that for every $B$ and $x \in F(B)$ there is a unique $f : B \to \Omega$ with $F(f)(u) = x$. The characteristic function $\chi_S : X \to \{0,1\}$ of $S \subseteq X$ sends $S$ to $1$ and its complement to $0$.

---

# Convergent Strategy

**Problem class:** This is an "identify and verify the universal element" exercise, with the twist that the universal element is a subtly-chosen element (a subset, not a point). The routine is to guess the representing object, then locate the *specific* element of the functor's value at that object which generates all others by restriction.

**Assumption pattern:** The decisive structure is that $\mathcal{P}$ acts by *preimage* (pullback), which is exactly the flexible action that makes the functor representable (contrast the rigid pushforward in [[Ex - A non-representable functor]]). The assumption "subsets are classified by maps to a truth-value object" is what produces the bijection.

**Theorem routing:** The route is: (i) define the bijection $\mathbf{Set}(X, \Omega) \cong \mathcal{P}(X)$ by $f \mapsto f^{-1}(\{1\})$ with inverse $S \mapsto \chi_S$; (ii) identify the universal element as $u = \{1\} \in \mathcal{P}(\Omega)$ by tracing $\eta_\Omega(1_\Omega)$; (iii) verify the universal property: every subset $S \subseteq B$ is $\mathcal{P}(\chi_S)(\{1\}) = \chi_S^{-1}(\{1\})$ for the unique classifying map $\chi_S$.

**Key decision point:** The crux — and the common error — is the universal element being $\{1\}$ *the subset*, living in $\mathcal{P}(\Omega)$, not $1$ *the element*, living in $\Omega$. The universal element must be an element of $F(\Omega) = \mathcal{P}(\Omega)$, i.e. a subset of $\Omega$, and the one that generates all subsets by preimage is $\{1\}$. Getting the type right ($\{1\} \in \mathcal{P}(\Omega)$ versus $1 \in \Omega$) is the whole subtlety.

---

# Legal Operations Used

1. **Operation 3 from the topic page (build the representation via the universal element).** We take $u = \{1\} \in \mathcal{P}(\Omega)$ and define the bijection by $f \mapsto \mathcal{P}(f)(u) = f^{-1}(\{1\})$.

2. **Operation 1 from the topic page (translate universality into a unique-factorization condition).** The universal property is "every subset is the preimage of $\{1\}$ under a unique classifying map".

---

# Hints

> [!note]- Hint 1
> A subset $S \subseteq X$ is the same as a function $\chi_S : X \to \{0, 1\}$ via $\chi_S^{-1}(\{1\}) = S$. This is the bijection $\mathcal{P}(X) \cong \mathbf{Set}(X, \Omega)$.

> [!note]- Hint 2
> The universal element lives in $F(\Omega) = \mathcal{P}(\Omega)$, so it is a *subset* of $\Omega = \{0,1\}$, not an element of $\Omega$. Which subset, when pulled back along $\chi_S$, gives $S$?

> [!note]- Hint 3
> $\chi_S^{-1}(\{1\}) = S$. So the universal element is the subset $\{1\} \in \mathcal{P}(\Omega)$. Verify: for any $S \subseteq B$, the unique $f : B \to \Omega$ with $f^{-1}(\{1\}) = S$ is $\chi_S$.

> [!note]- Hint 4
> This is the subobject classifier: $\Omega$ is the object of truth values, $\{1\}$ corresponds to the map $\top : * \to \Omega$ (pick out $1$), and every subobject is classified by pullback of $\top$.

---

# Solution

The plan is to set up the characteristic-function bijection, trace the universal element to the subset $\{1\}$, verify its universal property by the preimage formula, and recognize the structure as the subobject classifier of $\mathbf{Set}$.

**Step 1: $\mathcal{P}$ is representable by $\Omega = \{0, 1\}$.**

> [!note]- Derivation
> Define $\eta_X : \mathbf{Set}(X, \Omega) \to \mathcal{P}(X)$ by $\eta_X(f) = f^{-1}(\{1\})$, with inverse $S \mapsto \chi_S$ where $\chi_S(x) = 1$ if $x \in S$ and $0$ otherwise. These are mutually inverse: $\chi_S^{-1}(\{1\}) = S$, and a function $f$ is recovered from $f^{-1}(\{1\})$ as its own characteristic function. Naturality: for $g : X \to Y$, $\eta_X(\mathbf{Set}(g, \Omega)(f)) = \eta_X(f \circ g) = (f \circ g)^{-1}(\{1\}) = g^{-1}(f^{-1}(\{1\})) = \mathcal{P}(g)(\eta_Y(f))$, using $\mathcal{P}(g) = g^{-1}$. So $\mathbf{Set}(-, \Omega) \cong \mathcal{P}$.

**Step 2: The universal element is the subset $\{1\}$.**

> [!note]- Derivation
> The universal element is $u = \eta_\Omega(1_\Omega) = 1_\Omega^{-1}(\{1\}) = \{1\} \in \mathcal{P}(\Omega)$. Note carefully: $u$ is the *subset* $\{1\} \subseteq \Omega$, an element of $\mathcal{P}(\Omega)$ — not the *point* $1 \in \Omega$. Verify the universal property directly: given any set $B$ and subset $S \in \mathcal{P}(B)$, we need a unique $f : B \to \Omega$ with $\mathcal{P}(f)(u) = f^{-1}(\{1\}) = S$. The characteristic function $\chi_S$ satisfies $\chi_S^{-1}(\{1\}) = S$, and it is unique: any $f$ with $f^{-1}(\{1\}) = S$ must send exactly the elements of $S$ to $1$ and the rest to $0$, which is $\chi_S$. So $(\Omega, \{1\})$ is the universal element.

**Step 3: The subobject classifier interpretation.**

> [!note]- Derivation
> In topos-theoretic language, $\Omega = \{0, 1\}$ is the **subobject classifier** of $\mathbf{Set}$: the object of truth values. The universal element $\{1\}$ corresponds to the morphism $\top : * \to \Omega$ from the terminal object picking out $1$ (the "true" value). The universal property says: every subobject (subset) $S \hookrightarrow B$ arises as the pullback of $\top$ along a unique characteristic map $\chi_S : B \to \Omega$. So "subsets of $B$" $=$ "maps $B \to \Omega$" is the statement that $\Omega$ classifies subobjects — the defining feature of a topos, here for $\mathbf{Set}$, generalizing to any elementary **topos**.

> [!note]- Complete formal solution
> Define $\eta_X : \mathbf{Set}(X, \Omega) \to \mathcal{P}(X)$, $f \mapsto f^{-1}(\{1\})$, with inverse $S \mapsto \chi_S$; naturality holds because $(f \circ g)^{-1} = g^{-1} \circ f^{-1}$. So $\mathcal{P} \cong \mathbf{Set}(-, \Omega)$. The universal element is $\eta_\Omega(1_\Omega) = \{1\} \in \mathcal{P}(\Omega)$ — the subset $\{1\}$, not the point $1$. Its universal property: for every $S \subseteq B$ the unique $f : B \to \Omega$ with $f^{-1}(\{1\}) = S$ is $\chi_S$. This exhibits $\Omega$ as the subobject classifier of $\mathbf{Set}$, with $\{1\}$ (equivalently $\top : * \to \Omega$) the truth value classifying every subobject by pullback. $\blacksquare$

---

# Key Takeaways

**The universal element of the power-set functor is a subset, not a point — type discipline is the lesson.** The single most instructive trap here is that the universal element must live in $F(\Omega) = \mathcal{P}(\Omega)$, so it is a *subset* of the two-element set, and the correct one is $\{1\}$, not the element $1 \in \Omega$. This is a general discipline: a universal element of $F$ is an element of $F(A)$ for the representing object $A$, and you must respect that type. When $F$ is itself a "set of structures" functor (power set, set of bilinear maps, set of solutions), the universal element is a *structure on $A$*, often one level up from where intuition first points. Checking "what set does the universal element live in?" before guessing it prevents the most common error.

**Preimage is flexible enough to classify every subset, which is precisely why the contravariant power set is representable.** The contrast with [[Ex - A non-representable functor]] is sharp and worth holding onto: the *covariant* power set (direct image) is not representable, while the *contravariant* one (preimage) is. The reason is that $f^{-1}(\{1\})$ can be made any subset by choosing $f = \chi_S$, so the single universal element $\{1\}$ generates everything by pullback. Whenever a functor acts by pulling back along maps (preimage, restriction, substitution), representability is plausible and the universal element is "the generic instance you pull back"; when it pushes forward, expect non-representability.

**This is the toy model of the subobject classifier, the gateway to topos theory.** The fact that subsets of $B$ are the same as maps $B \to \Omega$ is the defining property of the subobject classifier, and $\mathbf{Set}$ is the simplest **topos**. In a general topos the subobject classifier $\Omega$ is the internal object of truth values, and the universal element $\{1\}$ becomes the truth morphism $\top : 1 \to \Omega$; classifying a subobject by pullback of $\top$ is how a topos internalizes logic and supports higher-order reasoning. Recognizing this exercise as the $\mathbf{Set}$-level shadow of that structure is the bridge from representability to the logical side of category theory, and to the **internal logic** that makes a topos a universe for mathematics.
