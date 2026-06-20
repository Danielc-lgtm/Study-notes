---
type: exercise
subject: higher-categories
difficulty: "⭐"
prereqs:
  - "Def - Generalized Operad"
  - "Def - Cartesian Monad"
  - "Def - Initial and Terminal Object"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

For each of the following [[Def - Cartesian Monad|cartesian monads]], compute the **arity object** $T1$ (where $1$ is the terminal object) and state what a $T$-[[Def - Generalized Operad|operad]]'s operations look like as a result:

(a) the identity monad $T = \mathrm{id}$ on $\mathbf{Set}$;
(b) the free-monoid (list) monad $T = (-)^{*}$ on $\mathbf{Set}$;
(c) the free-category monad $T = fc$ on directed graphs $\mathbf{Gph}$ (whose terminal object is the graph with one vertex and one loop);
(d) the free-strict-$\omega$-category monad $T = \mathbb{T}$ on globular sets (state the answer; full computation is HC7).

**Recall:**

A $T$-[[Def - Generalized Operad|operad]] has an operation-object $P$ and an arity map $\mathrm{ar} : P \to T1$; the fibre $\mathrm{ar}^{-1}(s)$ over a point $s \in T1$ is the object of operations of arity-shape $s$. The terminal object $1$ is the [[Def - Initial and Terminal Object|object with exactly one map from every other object]].

![[Def - Generalized Operad#Notation]]

---

# Convergent Strategy

**Problem class:** A *compute-the-arity-object* drill (the third target). The routine is mechanical: apply each monad to the terminal object and describe the result, then read off the operad shape.

**Assumption pattern:** Each part supplies an *explicit description of $T$ on objects*, which is exactly what makes $T1$ computable by hand. The assumption to lean on is "I know what $TX$ is as a set/graph/globular set, so I substitute $X = 1$".

**Theorem routing:** No theorem needed; the route is the definition of $T1$ as the arity object plus the explicit monad descriptions. The downstream identification (monoid / operad / linear-graph-operad / globular-operad) follows from [[Thm - Generalized Operads Recover Classical Structures]].

**Key decision point:** The only subtlety is identifying the *terminal object* correctly in each ambient category — it is the one-point set in $\mathbf{Set}$, but in $\mathbf{Gph}$ it is the one-vertex one-loop graph (not the single vertex with no edges), and in $\mathbf{GSet}$ it is the terminal globular set. Using the wrong terminal object gives the wrong $T1$. The tempting error is to use the "empty" or "discrete" object as terminal.

---

# Legal Operations Used

1. **Operation 2 from the topic page (compute $T1$ to find the arity object).** This exercise is operation 2 applied four times.
2. **Operation 1 from the topic page (specialize the monad to read off a classical structure).** Each $T1$ is read off to say what the operads look like.

---

# Hints

> [!note]- Hint 1
> The terminal object in $\mathbf{Set}$ is the one-point set $1 = \{*\}$. In $\mathbf{Gph}$, the terminal object is the graph $\mathbf{1}_{\mathbf{Gph}}$ with one vertex and exactly one edge (a loop), since every graph has a unique map to it. In $\mathbf{GSet}$, the terminal globular set has one cell in each dimension.

> [!note]- Hint 2
> (a) The identity functor fixes $1$, so $T1 = 1$. (b) A list of points of $1$ is determined by its length: $T1 = 1^{*} \cong \mathbb{N}$. (c) The free category on the one-loop graph has paths = powers of the loop, so the arity-shapes are the natural numbers again, but realized as *linear graphs* (paths) $\bullet \to \bullet \to \cdots \to \bullet$.

> [!note]- Hint 3
> Read off the operad: $T1 = 1$ means one arity, so a $T$-operad is a [[Def - Monoid in a Monoidal Category|monoid]]. $T1 = \mathbb{N}$ means one arity per natural number, so a $T$-operad is a classical operad with sets $P(n)$. For (d), $\mathbb{T}1$ is the set of globular pasting diagrams, so a $\mathbb{T}$-operad is a globular operad.

---

# Solution

The plan is four substitutions $X = 1$ into the known descriptions of $T$, each followed by reading off what the operad looks like. The only care needed is identifying the correct terminal object in each ambient category.

**Step 1: Identity monad — $T1 = 1$, operad = monoid.**

> [!note]- Derivation
> The identity functor fixes every object, so $T1 = 1$, the one-point set. There is a single arity-shape, so the arity map $\mathrm{ar} : P \to 1$ carries no information and $P$ is a single set with a unit and an associative, unital composition $P \times_1 P = P \times P \to P$ — a [[Def - Monoid in a Monoidal Category|monoid]]. *(This matches: a one-object category is a monoid.)*

**Step 2: List monad — $T1 = \mathbb{N}$, operad = classical operad.**

> [!note]- Derivation
> $T1 = 1^{*} = \coprod_{n \geq 0} 1^n$. A length-$n$ list of copies of the unique point $* \in 1$ is determined by $n$, so $T1 \cong \mathbb{N}$. The arity map $\mathrm{ar} : P \to \mathbb{N}$ partitions $P$ into sets $P(n) = \mathrm{ar}^{-1}(n)$ of $n$-ary operations, so a $T$-operad is a classical non-symmetric operad with substitution $P(k) \times \prod_i P(n_i) \to P(\sum_i n_i)$.

**Step 3: Free-category monad on graphs — $T1$ is the set of paths, $T1 \cong \mathbb{N}$, operad over linear graphs.**

> [!note]- Derivation
> The terminal graph $\mathbf{1}_{\mathbf{Gph}}$ has one vertex $v$ and one loop $\ell : v \to v$ (this is terminal because every graph maps to it uniquely: all vertices to $v$, all edges to $\ell$). The free category $fc(\mathbf{1}_{\mathbf{Gph}})$ has objects $= \{v\}$ and arrows $=$ paths from $v$ to $v$, i.e. the powers $\ell^0, \ell^1, \ell^2, \dots$ of the loop. So as a graph (one vertex, edges $= \mathbb{N}$), $T1$ has arity-shapes indexed by $\mathbb{N}$, realized as the *linear graphs* (paths) of each length. A $T$-operad here is thus an operad whose arities are linear graphs — the seed of the $fc$-multicategory story (HC5).

**Step 4: Free-strict-$\omega$-category monad — $T1$ is the set of globular pasting diagrams.**

> [!note]- Derivation
> Over globular sets, $\mathbb{T}1$ is the set of **globular pasting diagrams** — the formal shapes in which higher cells paste together (a point in dimension $0$, an arrow in dimension $1$, composable strings and whiskerings in higher dimensions). The arity map $\mathrm{ar} : P \to \mathbb{T}1$ assigns each operation its pasting shape, so a $\mathbb{T}$-operad is a **[[Def - Globular Operad|globular operad]]**: an operation of a given arity is "a way to compose that pasting diagram into a single cell" (full development in HC7).

> [!note]- Complete formal solution
> (a) $T = \mathrm{id}$: $T1 = 1$, one arity-shape, so a $T$-operad is a [[Def - Monoid in a Monoidal Category|monoid]].
> (b) $T = (-)^{*}$: $T1 = 1^{*} \cong \mathbb{N}$, arities indexed by $n \in \mathbb{N}$, so a $T$-operad is a classical non-symmetric operad with sets $P(n)$.
> (c) $T = fc$ on $\mathbf{Gph}$: the terminal graph is one vertex with one loop $\ell$; $fc$ of it has arrows the powers of $\ell$, so $T1 \cong \mathbb{N}$ realized as linear graphs (paths), and a $T$-operad has arities the linear graphs.
> (d) $T = \mathbb{T}$ on $\mathbf{GSet}$: $\mathbb{T}1$ is the globular pasting diagrams, so a $\mathbb{T}$-operad is a globular operad. $\blacksquare$

---

# Key Takeaways

**$T1$ is the single object that tells you what kind of operad you have, so compute it before anything else.** This drill exists to install one reflex: when handed a cartesian monad and asked about its operads, evaluate $T$ at the terminal object first. The answer is a complete classifier — a one-point answer ($T1 = 1$) means monoids, a copy of $\mathbb{N}$ means classical operads, a set of pasting diagrams means globular operads. The reusable trigger is "new cartesian monad $\rightsquigarrow$ compute $T1$", and it short-circuits a great deal of unwinding, because the structure of the operad is determined by the structure of $T1$.

**Identify the terminal object correctly — it is not always the "smallest" or "emptiest" object.** The one genuine pitfall here is part (c): the terminal object of $\mathbf{Gph}$ is the one-vertex *one-loop* graph, not the bare vertex, because terminality means "unique map *in* from everything", which forces an edge to absorb all edges. Getting this wrong gives $T1$ wrong and hence the wrong operad. The transferable diagnostic is to characterize the terminal object by its universal property (unique incoming map) in each ambient category, rather than guessing by size; this matters whenever the ambient category is not $\mathbf{Set}$.

**Different monads can share an arity *count* yet differ in arity *shape*.** Parts (b) and (c) both give $T1 \cong \mathbb{N}$ as a counting set, yet they are different framings: lists versus linear graphs. The richer information is not the cardinality of $T1$ but its internal structure as an object of the ambient category, because that structure governs how arities compose. The insight to carry forward is that $T1$ should be read as an *object*, with its own morphisms and composition, not merely as an index set — this is precisely why the $fc$ case (HC5) and the globular case (HC7), though their arity-counts look familiar, support genuinely two-dimensional and higher-dimensional structures. See [[Ex - A classical operad is a free-monoid-operad]] for the full unwinding of the $\mathbb{N}$ case.
