---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Endomorphism Operad"
  - "Def - Operad"
  - "Def - Algebra for an Operad"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $X$ be a set. Define $\mathrm{End}_X(n) = \mathrm{Hom}(X^n, X)$, the set of $n$-ary functions on $X$. 

(a) Equip this sequence with a unit, an $S_n$-action, and a composition, and verify in full that $(\mathrm{End}_X, \gamma, \mathrm{id})$ is a symmetric [[Def - Operad|operad]] — checking associativity, the unit law, and equivariance from first principles (no appeal to a general theorem).

(b) Prove that a [[Def - Algebra for an Operad|$P$-algebra]] structure on $X$, for any operad $P$, is the same as an operad morphism $\rho : P \to \mathrm{End}_X$. 

(c) Identify $\mathrm{End}_X(1)$ as a monoid and $\mathrm{End}_X(0)$ as a set, and interpret what an operad map $P \to \mathrm{End}_X$ does to the unit and nullary operations.

**Recall:**

![[Def - Endomorphism Operad#The Definition]]

An [[Def - Operad|operad]] in $\mathbf{Set}$ is a sequence $P(n)$ with $\mathrm{id} \in P(1)$, an $S_n$-action, and composition $\gamma : P(k) \times P(n_1) \times \dots \times P(n_k) \to P(\sum n_i)$, satisfying associativity, unit, and equivariance. A morphism of operads preserves all three.

---

# Convergent Strategy

**Problem class:** This is a *foundational axiom-checking* problem: verify that a concrete, important object satisfies an axiom scheme, then use it to ground a definition (here, "algebra over an operad"). The method is to write each operad axiom as an equation of functions and check it holds because the analogous equation holds for ordinary function composition.

**Assumption pattern:** The signal is "operations on a fixed object, composing by substitution". The endomorphism operad's axioms are *not* extra hypotheses; they are inherited from properties of function composition (associativity, identity, argument-permutation). Recognising "I am checking the operad axioms for genuine functions" tells you the proof is a translation, not a construction.

**Theorem routing:** Part (a) routes through the elementary identities for function composition: $f \circ (g \circ h) = (f\circ g)\circ h$ becomes operad associativity, $f \circ \mathrm{id} = f = \mathrm{id}\circ f$ becomes the unit law, and "relabel arguments" becomes equivariance. Part (b) routes through unwinding the definition of operad morphism and the definition of [[Def - Algebra for an Operad|algebra]]: both are families $P(n) \times X^n \to X$ compatible with composition, unit, and action. Part (c) routes through reading the low-arity pieces: $\mathrm{End}_X(1) = \mathrm{Hom}(X,X)$ is the endomorphism monoid, $\mathrm{End}_X(0) = \mathrm{Hom}(X^0, X) = X$.

**Key decision point:** The non-obvious care needed is in equivariance: one must distinguish the action of $S_n$ on an operation (relabelling its inputs) from the action on the *elements* fed to it, and check the two match. The temptation is to wave at "permutations obviously commute with everything"; the actual content is the precise statement $\gamma(\theta\cdot\sigma; \varphi_\bullet) = \gamma(\theta; \varphi_{\sigma^{-1}(\bullet)})\cdot\sigma\langle n_\bullet\rangle$, and verifying it for functions requires tracking which arguments go where.

---

# Legal Operations Used

1. **Translate operad axioms into equations of functions (operation 2 from the topic page).** Each axiom is checked by evaluating both sides on a general tuple of elements of $X$.

2. **Substitute functions into the slots of a function (operation 1 from the topic page).** The composition $\gamma$ is nested function application.

3. **Recognise an algebra as a map into the endomorphism operad (operation 4 from the topic page).** We identify the two definitions of "algebra structure".

---

# Hints

> [!note]- Hint 1
> The composition is $\gamma(f; g_1, \dots, g_k)(x_1, \dots, x_N) = f\big(g_1(x_1, \dots, x_{n_1}), g_2(x_{n_1+1}, \dots), \dots\big)$, partitioning the $N = \sum n_i$ inputs into consecutive blocks fed to the $g_i$. The unit is $\mathrm{id} = \mathrm{id}_X \in \mathrm{Hom}(X, X)$.

> [!note]- Hint 2
> Associativity: evaluate both $\gamma(\gamma(f; g_\bullet); h_\bullet)$ and $\gamma(f; \gamma(g_i; h_\bullet))$ on a tuple and watch both become the same nested expression $f(g_1(h_{1,\bullet}), \dots)$.

> [!note]- Hint 3
> The $S_n$-action: $(f \cdot \sigma)(x_1, \dots, x_n) = f(x_{\sigma(1)}, \dots, x_{\sigma(n)})$. Check this is a right action and that it satisfies equivariance with $\gamma$ by tracking how arguments are relabelled.

> [!note]- Hint 4
> For (b): an operad map $\rho : P \to \mathrm{End}_X$ is a family $\rho_n : P(n) \to \mathrm{Hom}(X^n, X)$. Curry it to $P(n) \times X^n \to X$ — that is exactly the structure maps of a $P$-algebra, and the operad-map conditions are exactly the algebra axioms.

---

# Solution

The plan: define the data and verify the three axioms by reducing each to an identity for function composition (Steps 1–3); then prove the algebra/morphism equivalence by currying (Step 4); finally read off the low arities (Step 5).

**Step 1: Data and the unit law.**

> [!note]- Derivation
> Set $\mathrm{End}_X(n) = \mathrm{Hom}(X^n, X)$, unit $\mathrm{id} = \mathrm{id}_X \in \mathrm{End}_X(1)$, action $(f\cdot\sigma)(x_\bullet) = f(x_{\sigma(1)}, \dots, x_{\sigma(n)})$, composition
> $$\gamma(f; g_1, \dots, g_k)(x_1, \dots, x_N) = f\big(g_1(x_1, \dots, x_{n_1}),\ \dots,\ g_k(x_{N - n_k + 1}, \dots, x_N)\big),$$
> with $N = \sum n_i$. Unit law: $\gamma(\mathrm{id}_X; g) = \mathrm{id}_X \circ g = g$, and $\gamma(f; \mathrm{id}_X, \dots, \mathrm{id}_X)(x_\bullet) = f(\mathrm{id}_X(x_1), \dots, \mathrm{id}_X(x_n)) = f(x_\bullet) = f$. So the unit law holds.

**Step 2: Associativity.**

> [!note]- Derivation
> Take $f \in \mathrm{End}_X(k)$, $g_i \in \mathrm{End}_X(n_i)$, $h_{i,j} \in \mathrm{End}_X(m_{i,j})$. Evaluate $\gamma(\gamma(f; g_\bullet); h_\bullet)$ on a tuple $\mathbf{x}$: first $\gamma(f; g_\bullet)$ is the function $\mathbf{y} \mapsto f(g_1(y_\bullet), \dots)$, then substituting the $h$'s gives $f\big(g_1(h_{1,1}(\mathbf{x}_{1,1}), \dots), \dots\big)$. Evaluate $\gamma(f; \gamma(g_i; h_{i,\bullet}))$: each $\gamma(g_i; h_{i,\bullet})$ is $\mathbf{z} \mapsto g_i(h_{i,1}(\mathbf{z}_{\bullet}), \dots)$, and substituting into $f$ gives $f\big(g_1(h_{1,1}(\mathbf{x}_{1,1}), \dots), \dots\big)$ — the *same* nested expression. The two sides agree on every tuple because function application is associative. Hence operad associativity holds.

**Step 3: Equivariance.**

> [!note]- Derivation
> First, $(f\cdot\sigma)\cdot\tau (x_\bullet) = (f\cdot\sigma)(x_{\tau(\bullet)}) = f(x_{\tau(\sigma(\bullet))}) = f(x_{(\tau\sigma)(\bullet)}) = (f\cdot(\sigma\tau))(x_\bullet)$... careful: with the convention $(f\cdot\sigma)(x_\bullet) = f(x_{\sigma(\bullet)})$ this is a right action $f\cdot(\sigma\tau)$. Equivariance with $\gamma$: permuting the $k$ blocks of the composite by $\sigma \in S_k$ moves block $i$ to position $\sigma(i)$; on the function $\gamma(f\cdot\sigma; g_\bullet)$ evaluated at $\mathbf{x}$, this feeds the blocks of $\mathbf{x}$ to $f$ in the order $\sigma$, which equals $\gamma(f; g_{\sigma^{-1}(\bullet)})$ evaluated at $\mathbf{x}$ reindexed by the block permutation $\sigma\langle n_\bullet\rangle$. Tracking the indices: both sides compute $f$ applied to $g_{\sigma^{-1}(1)}, \dots, g_{\sigma^{-1}(k)}$ on the correspondingly permuted blocks of $\mathbf{x}$. The within-block law $\gamma(f; g_i\cdot\tau_i) = \gamma(f; g_i)\cdot(\tau_1\oplus\dots)$ holds because permuting $g_i$'s arguments permutes the corresponding input block. So equivariance holds and $\mathrm{End}_X$ is a symmetric operad.

**Step 4: Algebras = operad morphisms into $\mathrm{End}_X$.**

> [!note]- Derivation
> An operad morphism $\rho : P \to \mathrm{End}_X$ is a family $\rho_n : P(n) \to \mathrm{Hom}(X^n, X)$ preserving unit, composition, and action. Currying $\rho_n$ gives $\hat\rho_n : P(n) \times X^n \to X$, $\hat\rho_n(\theta, x_\bullet) = \rho_n(\theta)(x_\bullet)$. The operad-map conditions become exactly the [[Def - Algebra for an Operad|algebra axioms]]: $\rho$ preserving $\gamma$ is the algebra associativity $\hat\rho(\gamma(\theta; \varphi_\bullet)) = \hat\rho(\theta)(\hat\rho(\varphi_1), \dots)$; $\rho(\mathrm{id}) = \mathrm{id}_X$ is the unit law; $\rho$ preserving the action is the equivariance $\hat\rho(\theta\cdot\sigma; x_\bullet) = \hat\rho(\theta; x_{\sigma(\bullet)})$. Conversely a $P$-algebra structure uncurries to such a $\rho$. So $P$-algebra structures on $X$ are exactly operad morphisms $P \to \mathrm{End}_X$.

**Step 5: Low arities.**

> [!note]- Derivation
> $\mathrm{End}_X(1) = \mathrm{Hom}(X, X)$ with operadic composition $=$ ordinary function composition, and unit $\mathrm{id}_X$: this is the endomorphism *monoid* of $X$. An operad map $\rho$ restricted to arity $1$ is a monoid map $P(1) \to \mathrm{Hom}(X,X)$, an action of the monoid $P(1)$ on $X$. $\mathrm{End}_X(0) = \mathrm{Hom}(X^0, X) = \mathrm{Hom}(\{*\}, X) = X$: the nullary operations are the *elements* of $X$. An operad map sends $P(0) \to X$, i.e. picks out a chosen element (a "constant") for each nullary operation of $P$ — for instance the unit element of a monoid is the image of the nullary operation of $\mathrm{Assoc}$.

> [!note]- Complete formal solution
> *(a)* With $\mathrm{End}_X(n)=\mathrm{Hom}(X^n,X)$, unit $\mathrm{id}_X$, action $(f\cdot\sigma)(x_\bullet)=f(x_{\sigma(\bullet)})$, and $\gamma(f;g_\bullet)(\mathbf{x})=f(g_1(\mathbf{x}_1),\dots)$ partitioning inputs into consecutive blocks: the unit law is $f\circ(\mathrm{id}_X,\dots)=f$; associativity holds because both bracketings evaluate to the same nested application; equivariance holds by tracking how block and within-block permutations relabel inputs. Hence $\mathrm{End}_X$ is a symmetric operad.
>
> *(b)* Currying identifies operad morphisms $P\to\mathrm{End}_X$ with families $P(n)\times X^n\to X$ satisfying the algebra axioms; so $P$-algebra structures = operad maps $P\to\mathrm{End}_X$.
>
> *(c)* $\mathrm{End}_X(1)=\mathrm{Hom}(X,X)$ is the endomorphism monoid; $\mathrm{End}_X(0)=X$ is the set of nullary operations (elements). An operad map sends the operad's unit to $\mathrm{id}_X$ and its nullary operations to chosen elements of $X$. $\blacksquare$

---

# Key Takeaways

**The endomorphism operad inherits its axioms from function composition — that is the whole reason operads have the axioms they do.** The single most important realisation is that checking $\mathrm{End}_X$ is an operad is a *translation exercise*: every operad axiom is the abstract shadow of a property of genuine function composition (associativity, identity, argument-permutation). This is not a coincidence — the operad axioms were reverse-engineered to be exactly "whatever $\mathrm{End}_X$ satisfies", so that an algebra could be defined as a map into $\mathrm{End}_X$. The transferable insight: whenever you meet an axiom system that seems arbitrary, look for the *one example it was designed to capture* — here, the operations on a set — and the axioms will reveal themselves as that example's inherited properties.

**To act is to map into the gadget of all actions.** Part (b) is an instance of a universal pattern that recurs across mathematics: a group acts on $X$ via a homomorphism $G \to \mathrm{Sym}(X)$; a monoid acts via $M \to \mathrm{End}(X)$; an operad acts via $P \to \mathrm{End}_X$; a Lie algebra acts via a map to $\mathfrak{gl}(X)$. In every case "the operations on $X$" assemble into a universal target, and "an action" is a structure-preserving map into it. Recognising this pattern means that whenever you want to define "$Y$ acts on $X$", the correct move is to identify the object of all $X$-operations of the relevant kind and ask for a morphism into it — the axioms of the action are then automatically the morphism conditions.

**Nullary operations are elements, and arity-one operations are a monoid.** The low-arity reading in (c) is a reusable orientation tool for any operad: $P(0)$ supplies *constants* (the chosen elements an algebra must have, like a unit or a zero), and $P(1)$ is always a *monoid* acting on the algebra (unary operations like scalar multiplications or the identity). When you encounter a new operad, reading $P(0)$ and $P(1)$ first tells you which constants its algebras carry and which unary symmetries act — for the associative operad, $P(0)$ is the unit element and $P(1) = S_1$ is trivial; for an operad over $\mathbf{Vect}_k$, $P(1)$ often contains the scalars. This bottom-up reading is the fastest way to get a feel for an unfamiliar operad's algebras.
