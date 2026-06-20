---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Algebra for a Generalized Operad"
  - "Def - Generalized Operad"
  - "Def - Monoid in a Monoidal Category"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $T = (-)^{*}$ on $\mathbf{Set}$ and let $\mathrm{Assoc}$ be the associative $T$-[[Def - Generalized Operad|operad]]: the operad with exactly one operation of each arity, $\mathrm{Assoc}(n) = \{\nu_n\}$ for all $n \geq 0$, with $\nu_1$ the unit and substitution forced. Show that an [[Def - Algebra for a Generalized Operad|algebra]] for $\mathrm{Assoc}$ is exactly a [[Def - Monoid in a Monoidal Category|monoid]]: a set $X$ with an associative binary operation and a unit. Identify which operation gives the monoid multiplication, which gives the unit, and how the operad axioms force associativity and unitality.

**Recall:**

![[Def - Algebra for a Generalized Operad#The Definition]]

A [[Def - Monoid in a Monoidal Category|monoid]] is a set $X$ with a multiplication $m : X \times X \to X$ and a unit $u : 1 \to X$ such that $m$ is associative ($m(m \times 1) = m(1 \times m)$) and unital ($m(u, x) = x = m(x, u)$).

---

# Convergent Strategy

**Problem class:** A *construct-the-algebras* problem (the fourth target): identify the category of algebras of a given operad with a known algebraic category. The routine is to write the action maps, see what the operad forces, and recognize the result.

**Assumption pattern:** The decisive feature of $\mathrm{Assoc}$ is that it has *exactly one operation per arity*. This rigidity means the action of $\mathrm{Assoc}$ on a set $X$ is just a single map $X^n \to X$ for each $n$, and the operad's (forced) composition then forces all of these to be iterates of the binary one. The assumption to exploit is "one operation per arity $\Rightarrow$ no choice, everything is determined by $\nu_2$".

**Theorem routing:** From the [[Def - Algebra for a Generalized Operad|definition of an algebra]] for a $(-)^{*}$-operad: an action is a family of maps $\mathrm{Assoc}(n) \times X^n \to X$, i.e. (since $\mathrm{Assoc}(n)$ is a point) maps $\nu_n : X^n \to X$. The associativity and unit *of the operad* then route to the associativity and unit *of the monoid* via [[Thm - Generalized Operads Recover Classical Structures]].

**Key decision point:** The non-obvious move is to show that the binary operation $\nu_2$ *determines* all the higher $\nu_n$, so that an $\mathrm{Assoc}$-algebra is no more data than a monoid. One must verify $\nu_3 = \nu_2(\nu_2 \times 1) = \nu_2(1 \times \nu_2)$ (well-defined because the operad's two ways of building the ternary operation coincide), and inductively $\nu_n$ is an iterate of $\nu_2$. The tempting error is to treat the $\nu_n$ as independent data, which would make an algebra richer than a monoid.

---

# Legal Operations Used

1. **Operation 7 from the topic page (turn an operad into a monad and read its algebras).** An $\mathrm{Assoc}$-algebra is an algebra for the induced monad $T_{\mathrm{Assoc}} X = \coprod_n X^n = X^{*}$, the free-monoid monad, whose algebras are monoids.
2. **Operation 1 from the topic page (specialize the monad).** Working with $T = (-)^{*}$ to write the action maps concretely.
3. **Operation 6 from the topic page (one-object case).** $\mathrm{Assoc}$ is a $T$-operad, the single-sorted case.

---

# Hints

> [!note]- Hint 1
> Since $\mathrm{Assoc}(n)$ is a one-point set, the action $\mathrm{Assoc}(n) \times X^n \to X$ is just a map $\nu_n : X^n \to X$. So an $\mathrm{Assoc}$-algebra is a set with one $n$-ary operation for each $n$. The question is how these relate.

> [!note]- Hint 2
> The operad's substitution forces relations. Building the ternary operation two ways — $\nu_2 \circ (\nu_2, \nu_1)$ and $\nu_2 \circ (\nu_1, \nu_2)$ — both equal $\nu_3$ in $\mathrm{Assoc}$ (one operation per arity), so the algebra axiom forces $\nu_2(\nu_2(x,y), z) = \nu_2(x, \nu_2(y,z))$: associativity.

> [!note]- Hint 3
> The nullary operation $\nu_0 : X^0 = 1 \to X$ is the unit element. The unary $\nu_1 : X \to X$ is forced to be the identity by the operad unit law. Set $m = \nu_2$, $u = \nu_0$; then $\nu_n$ is the $n$-fold product, and $(X, m, u)$ is a monoid. Conversely every monoid gives an $\mathrm{Assoc}$-algebra by taking $\nu_n$ to be iterated multiplication.

---

# Solution

The plan: write an $\mathrm{Assoc}$-algebra as a family of operations $\nu_n : X^n \to X$ (Step 1); use the operad's forced substitution to show $\nu_2$ determines all $\nu_n$ and is associative, with $\nu_0$ the unit (Step 2); conclude the equivalence with monoids, both directions (Step 3).

**Step 1: An $\mathrm{Assoc}$-algebra is a set with one operation per arity.**

> [!note]- Derivation
> An [[Def - Algebra for a Generalized Operad|algebra]] for a $(-)^{*}$-operad $P$ is a set $X$ with an action $h : P \times_{\mathbb{N}} X^{*} \to X$, which decomposes over arities into maps $P(n) \times X^n \to X$. For $P = \mathrm{Assoc}$, each $\mathrm{Assoc}(n) = \{\nu_n\}$ is a one-point set, so the action at arity $n$ is a map
> $$\nu_n^X : X^n \to X$$
> (one $n$-ary operation on $X$, the action of the unique abstract operation $\nu_n$). We write $\nu_n$ for $\nu_n^X$. So an $\mathrm{Assoc}$-algebra is a set $X$ together with, for each $n \geq 0$, a map $\nu_n : X^n \to X$ — but these are constrained by the operad axioms, as we now see.

**Step 2: The binary operation determines and forces everything.**

> [!note]- Derivation
> *Unit law forces $\nu_1 = \mathrm{id}$.* The operad's unit is $\nu_1 \in \mathrm{Assoc}(1)$, and the algebra unit axiom says acting by the unit operation is the identity: $\nu_1 : X \to X$ equals $1_X$.
>
> *Associativity.* In $\mathrm{Assoc}$ there is exactly one ternary operation $\nu_3$, and it equals both substituted composites $\nu_2 \circ (\nu_2, \nu_1)$ and $\nu_2 \circ (\nu_1, \nu_2)$ (both are operations of arity $3$, and there is only one). The algebra associativity axiom transports this equality to $X$:
> $$\nu_2(\nu_2(x, y), z) = \nu_3(x, y, z) = \nu_2(x, \nu_2(y, z)) \quad \text{for all } x, y, z \in X.$$
> So $\nu_2$ is associative.
>
> *Higher operations are iterates.* Inductively, $\nu_n = \nu_2 \circ (\nu_{n-1}, \nu_1)$, the $n$-fold product built from $\nu_2$, because in $\mathrm{Assoc}$ every $\nu_n$ is the unique arity-$n$ operation, obtained by substituting binaries, and the algebra axioms make $\nu_n$ on $X$ the corresponding iterate. Thus all $\nu_n$ are determined by $\nu_2$.
>
> *Unit element.* The nullary operation $\nu_0 : X^0 = 1 \to X$ picks an element $e \in X$, and the unit/associativity laws give $\nu_2(e, x) = x = \nu_2(x, e)$ (the arity-bookkeeping: substituting $\nu_0$ into one slot of $\nu_2$ yields $\nu_1 = \mathrm{id}$). So $e$ is a two-sided unit for $\nu_2$.

**Step 3: The equivalence with monoids.**

> [!note]- Derivation
> Set $m = \nu_2 : X \times X \to X$ and $u = \nu_0 : 1 \to X$. By Step 2, $m$ is associative and $u$ is a two-sided unit, so $(X, m, u)$ is a [[Def - Monoid in a Monoidal Category|monoid]]. Conversely, given a monoid $(X, m, u)$, define $\nu_0 = u$, $\nu_1 = 1_X$, and let $\nu_n$ be the $n$-fold iterate of $m$ (unambiguous by associativity); these satisfy the operad action axioms, giving an $\mathrm{Assoc}$-algebra. The two constructions are mutually inverse and respect morphisms (a map preserving all $\nu_n$ is exactly a monoid homomorphism, since it preserves $m$ and $u$). Hence $\mathrm{Assoc}\text{-}\mathbf{Alg} \cong \mathbf{Mon}$.
>
> *Structural cross-check.* The induced monad is $T_{\mathrm{Assoc}} X = \coprod_n \mathrm{Assoc}(n) \times X^n = \coprod_n X^n = X^{*}$, the free-monoid monad, whose [[Def - Algebra for a Monad|Eilenberg–Moore algebras]] are exactly monoids — confirming the result by the [[Def - Algebra for a Generalized Operad#Categorical / Structural Definition|operad-induces-a-monad]] perspective.

> [!note]- Complete formal solution
> An $\mathrm{Assoc}$-algebra is a set $X$ with maps $\nu_n : X^n \to X$ (one per arity, since $\mathrm{Assoc}(n)$ is a point). The unit law forces $\nu_1 = 1_X$; the equality of the two ternary substitutes in $\mathrm{Assoc}$ forces $\nu_2(\nu_2(x,y),z) = \nu_2(x,\nu_2(y,z))$ (associativity of $\nu_2$); $\nu_0 : 1 \to X$ is a two-sided unit for $\nu_2$; and all higher $\nu_n$ are iterates of $\nu_2$. So $(X, \nu_2, \nu_0)$ is a monoid, and conversely every monoid yields an $\mathrm{Assoc}$-algebra via iterated multiplication; the correspondence is an isomorphism of categories $\mathrm{Assoc}\text{-}\mathbf{Alg} \cong \mathbf{Mon}$. Equivalently, the induced monad $T_{\mathrm{Assoc}} = (-)^{*}$ is the free-monoid monad, whose algebras are monoids. $\blacksquare$

---

# Key Takeaways

**"One operation per arity" is the operadic signature of an associative structure with no extra symmetry.** The reason $\mathrm{Assoc}$-algebras are monoids and nothing more is that $\mathrm{Assoc}$ offers no choices: a single $n$-ary operation, all of them forced to be iterates of the binary one. The reusable diagnostic is to read an operad's algebras off its *operation-counts and symmetries*: one operation per arity, no symmetric-group action, gives monoids; one operation per arity *with* trivial $S_n$-action gives commutative monoids; Catalan-many operations (free on a binary operation) gives "magmas" with no associativity. The operad is the theory, the operation-counts are its signature, and the algebras are its models — this is the cleanest instance of that slogan.

**A higher operation that is forced to equal both of its substitutes *is* an associativity law.** The crux of the proof is that $\mathrm{Assoc}$ has exactly one ternary operation, so the two ways of building it from binaries must coincide, and this coincidence transports to the algebra as $x(yz) = (xy)z$. This is the operadic mechanism behind every associativity statement: associativity is not an extra equation imposed by hand but the *uniqueness* of a higher operation in the operad. The trigger to carry forward is that whenever you want to know whether an operadic structure is associative, ask how many operations of arity $3$ the operad has — one means strictly associative, a contractible space of them means associative up to coherent homotopy (the $A_\infty$ case), more than one with no relation means non-associative.

**Converting an operad to its induced monad is the fastest route to its algebras.** Rather than chase the operad axioms by hand, one can compute $T_P X = \coprod_n P(n) \times X^n$ and recognize $T_P$-algebras as a known [[Def - Algebra for a Monad|Eilenberg–Moore]] category — here $T_{\mathrm{Assoc}} = (-)^{*}$, the free-monoid monad, whose algebras are monoids by the standard monad-algebra theory. The transferable technique is "operad $\to$ monad $\to$ recognize the algebras", and it pays off precisely because the entire well-developed theory of monad-algebras (limits, free–forgetful adjunctions, monadicity) becomes available. See [[Ex - The induced monad of a generalized operad]] for the general construction and [[Ex - Reading the unifying table across three monads]] for how this algebra sits in the chapter's table.
