---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Cartesian Monad"
  - "Def - Monad and Comonad"
  - "Def - Pullback and Pushout"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $T = (-)^{*}$ be the free-monoid (list) monad on $\mathbf{Set}$: $TX = X^{*} = \coprod_{n \geq 0} X^n$, the set of finite lists of elements of $X$, with unit $\eta_X(x) = (x)$ (the singleton list) and multiplication $\mu_X$ given by concatenating a list of lists. Show that $T$ is a [[Def - Cartesian Monad|cartesian monad]]: that is, prove that

(a) $T$ preserves pullbacks;
(b) the unit $\eta$ is a cartesian natural transformation; and
(c) the multiplication $\mu$ is a cartesian natural transformation.

**Recall:**

A [[Def - Monad and Comonad|monad]] $(T, \eta, \mu)$ on a category $\mathcal{E}$ with [[Def - Pullback and Pushout|pullbacks]] is **cartesian** when $T$ preserves pullbacks and the naturality squares of $\eta$ and $\mu$ are all pullbacks.

![[Def - Cartesian Monad#The Definition]]

A natural transformation $\alpha : F \Rightarrow G$ is **cartesian** if for every $f : A \to B$ the naturality square with corners $FA, FB, GA, GB$ is a [[Def - Pullback and Pushout|pullback]] — equivalently, $FA \cong GA \times_{GB} FB$ via the canonical map.

---

# Convergent Strategy

**Problem class:** This is a *cartesianness verification* problem (the first target of the [[Higher Categories — Generalized Operads via Cartesian Monads#Sources and Targets|chapter]]). The routine is the two-item checklist of the definition — preservation of pullbacks, plus the cartesian condition on $\eta$ and $\mu$ — carried out by direct element-chasing in $\mathbf{Set}$, where pullbacks are concrete fibre products.

**Assumption pattern:** The decisive assumption is the *explicit description of $T$ on objects*: $TX$ is the set of finite lists. This makes every relevant object — $TX$, $T(A \times_C B)$, the naturality squares — computable element by element. The list structure is *ordered and rigid* (no symmetry is quotiented), which is precisely the feature that will make each square a pullback; recognizing that rigidity is the assumption to lean on.

**Theorem routing:** No external theorem is needed; the route is straight from the [[Def - Cartesian Monad|definition of a cartesian monad]]. For (a), compute $T(A \times_C B)$ and compare it to $TA \times_{TC} TB$. For (b) and (c), write the naturality square of $\eta$ (respectively $\mu$) for a map $f$ and check the universal property of the pullback directly.

**Key decision point:** The non-obvious choice is *how to match a list in the apex to the data on the legs*. For (a), the crux is that a list of pairs $((a_1,b_1), \dots, (a_n,b_n))$ in $T(A \times_C B)$ corresponds to a pair of *equal-length* lists in $TA \times_{TC} TB$ — the equal-length condition is forced by the matching over $TC$, and getting that condition right is the whole problem. The natural alternative, ignoring length-matching, fails because lists of different lengths cannot be paired componentwise.

---

# Legal Operations Used

1. **Operation 3 from the topic page (check cartesianness as a two-item checklist).** We verify preservation of pullbacks and the cartesian condition on $\eta, \mu$ separately, exactly as the operation prescribes.
2. **Operation 9 from the topic page (recognize a pullback as a fibre of $T$).** In each part we identify the relevant object as a fibre product and check the universal property by exhibiting the unique mediating map.
3. **Operation 1 from the topic page (specialize the monad).** Working with the concrete list description of $T$ is the specialization that makes the abstract conditions computable.

---

# Hints

> [!note]- Hint 1
> Pullbacks in $\mathbf{Set}$ are concrete: $A \times_C B = \{(a,b) : f(a) = g(b)\}$. Write down what $T(A \times_C B)$ is as a set of lists, and what $TA \times_{TC} TB$ is, and compare.

> [!note]- Hint 2
> A list of pairs is the same as a pair of lists *of the same length*. The condition $\mu, \eta, Tf$ impose is exactly that lengths match and components agree. For (a), the map $T(A \times_C B) \to TA \times_{TC} TB$ sending a list of pairs to (list of first coordinates, list of second coordinates) is a bijection — that bijection *is* the pullback condition.

> [!note]- Hint 3
> For (c), the multiplication square for $f : A \to B$ relates $T^2 A, T^2 B, TA, TB$. The pullback says: a list-of-lists in $T^2 A$ is determined by its concatenation in $TA$ together with the abstract list-of-lists shape in $T^2 B$ (i.e. the lengths of the sublists). Reconstruct the partition of a concatenated list from the sublist-lengths — this is possible *because lists are ordered*, and it is exactly where a symmetric monad would fail.

---

# Solution

The proof is three direct computations in $\mathbf{Set}$, all instances of one idea: a list of structured things is the same as a structure of lists *of matching length*, and the length data is exactly what the pullback remembers. Step 1 does preservation of pullbacks; Step 2 does the unit; Step 3 does the multiplication, where the ordered (symmetry-free) nature of lists is decisive.

**Step 1: $T$ preserves pullbacks.**

> [!note]- Derivation
> Let $A \xrightarrow{f} C \xleftarrow{g} B$ be a cospan, with pullback $A \times_C B = \{(a,b) : f(a) = g(b)\}$. Then
> $$T(A \times_C B) = (A \times_C B)^{*} = \{((a_1,b_1), \dots, (a_n,b_n)) : f(a_i) = g(b_i) \text{ for all } i\}.$$
> On the other side, $TA \times_{TC} TB$ consists of pairs of lists $(\alpha, \beta)$ with $\alpha \in A^{*}$, $\beta \in B^{*}$, and $T f(\alpha) = T g(\beta)$ in $C^{*}$. Now $Tf(\alpha) = (f(a_1), \dots, f(a_m))$ and $Tg(\beta) = (g(b_1), \dots, g(b_k))$, and two lists in $C^{*}$ are equal iff they have the same length and equal entries. So $Tf(\alpha) = Tg(\beta)$ forces $m = k$ and $f(a_i) = g(b_i)$ for all $i$. Therefore the map
> $$T(A \times_C B) \longrightarrow TA \times_{TC} TB, \qquad ((a_i,b_i))_i \longmapsto \big((a_i)_i, (b_i)_i\big)$$
> is a bijection: its inverse zips two equal-length compatible lists back into a list of pairs. A bijection onto the pullback realizes $T(A \times_C B)$ *as* the pullback $TA \times_{TC} TB$, so $T$ preserves this pullback. Since the cospan was arbitrary, $T$ preserves all pullbacks.

**Step 2: $\eta$ is cartesian.**

> [!note]- Derivation
> Fix $f : A \to B$. The naturality square of $\eta$ is
> $$\begin{array}{ccc}
> A & \xrightarrow{\;f\;} & B \\
> {\scriptstyle \eta_A}\big\downarrow & & \big\downarrow{\scriptstyle \eta_B} \\
> TA & \xrightarrow{\;Tf\;} & TB
> \end{array}$$
> We must show $A$ is the pullback $TA \times_{TB} B = \{(\alpha, b) : Tf(\alpha) = \eta_B(b)\}$. Now $\eta_B(b) = (b)$ is the singleton list, and $Tf(\alpha) = (b)$ forces $\alpha$ to be a singleton list $(a)$ with $f(a) = b$. So the pullback is $\{((a), b) : f(a) = b\} \cong \{a \in A\} = A$, via $a \mapsto ((a), f(a))$ and $\eta_A : a \mapsto (a)$ as the comparison. Hence the square is a pullback: the only lists mapping to a singleton are singletons, and they are exactly the elements of $A$. So $\eta$ is cartesian. *(This is the precise statement that the singleton lists form a clean sub-family, with no extra identifications — the picture from the [[Def - Cartesian Monad#Axiom Motivation|axiom motivation]].)*

**Step 3: $\mu$ is cartesian.**

> [!note]- Derivation
> Fix $f : A \to B$. The naturality square of $\mu$ is
> $$\begin{array}{ccc}
> T^2 A & \xrightarrow{\;T^2 f\;} & T^2 B \\
> {\scriptstyle \mu_A}\big\downarrow & & \big\downarrow{\scriptstyle \mu_B} \\
> TA & \xrightarrow{\;Tf\;} & TB
> \end{array}$$
> We show $T^2 A \cong TA \times_{TB} T^2 B$, i.e. $T^2 A = \{(\gamma, \Delta) : Tf(\gamma) = \mu_B(\Delta)\}$. An element of $T^2 A$ is a list of lists $\Gamma = ((a_{11}, \dots, a_{1 k_1}), \dots, (a_{m1}, \dots, a_{m k_m}))$. Its image under $\mu_A$ is the concatenation $\gamma = (a_{11}, \dots, a_{m k_m})$, a flat list of length $\sum k_i$. Its image under $T^2 f$ is the list-of-lists of the $f(a_{ij})$, with the *same shape* (the same $m$ and same $k_i$). The claim is that $\Gamma$ is recoverable from the pair $(\gamma, \Delta)$ where $\Delta = T^2 f(\Gamma)$: indeed $\Delta$ records the shape — the number $m$ of sublists and their lengths $k_1, \dots, k_m$ — and $\gamma$ records the flat sequence of entries; cutting $\gamma$ into consecutive blocks of lengths $k_1, \dots, k_m$ reconstructs $\Gamma$ uniquely, and the entries match because $Tf(\gamma) = \mu_B(\Delta)$ ensures the $f$-values agree. This reconstruction is *unambiguous precisely because the list is ordered*: there is exactly one way to cut a sequence into consecutive blocks of given lengths. Hence the comparison map $T^2 A \to TA \times_{TB} T^2 B$ is a bijection, and $\mu$ is cartesian.

> [!note]- Complete formal solution
> Let $T = (-)^{*}$ on $\mathbf{Set}$, with $\eta_X(x) = (x)$ and $\mu_X$ = concatenation.
>
> **(a) Preservation of pullbacks.** For a cospan $A \xrightarrow{f} C \xleftarrow{g} B$, an element of $T(A \times_C B)$ is a list $((a_i, b_i))_{i=1}^n$ with $f(a_i) = g(b_i)$ for all $i$. The assignment $((a_i,b_i))_i \mapsto ((a_i)_i, (b_i)_i)$ is a bijection onto $TA \times_{TC} TB = \{(\alpha,\beta) : Tf(\alpha) = Tg(\beta)\}$, because $Tf(\alpha) = Tg(\beta)$ holds iff $\alpha, \beta$ have equal length with $f(\alpha_i) = g(\beta_i)$. Thus $T$ preserves the pullback.
>
> **(b) $\eta$ cartesian.** For $f : A \to B$, the pullback $TA \times_{TB} B = \{(\alpha, b) : Tf(\alpha) = (b)\}$ equals $\{((a), b) : f(a) = b\}$ since only singleton lists map to a singleton, and this is in bijection with $A$ via $a \mapsto ((a), f(a))$, with $\eta_A$ the comparison. The naturality square is a pullback.
>
> **(c) $\mu$ cartesian.** For $f : A \to B$, the comparison $T^2 A \to TA \times_{TB} T^2 B$, $\Gamma \mapsto (\mu_A \Gamma, T^2 f\,\Gamma)$, is a bijection: from the flat concatenation $\mu_A\Gamma$ and the shape recorded by $T^2 f\,\Gamma$ (number and lengths of sublists), one reconstructs $\Gamma$ by cutting the concatenation into consecutive blocks of the prescribed lengths — uniquely, because lists are ordered. The naturality square is a pullback.
>
> All three conditions hold, so $T = (-)^{*}$ is a cartesian monad. $\blacksquare$

---

# Key Takeaways

**A list of structured things is a structure of equal-length lists, and the length data is what the pullback remembers.** Every part of this proof is the same observation in three costumes: $T$ of a fibre product, the singleton sub-family, and the flatten-and-recut bijection all reduce to "lists pair up componentwise when their lengths match". The reusable diagnostic is that whenever you must check a list-monad square is a pullback, the right thing to track is *length/shape data*, because that is the information that distinguishes elements of the apex; once you can recover each apex element from its image on the two legs, you have the pullback for free. This pattern recurs for every "free, ordered structure" monad — trees, forests, planar operations — and the recovery-by-shape argument is identical.

**The ordering is load-bearing, and seeing exactly where shows why symmetric monads fail.** The crucial line in Step 3 is "there is exactly one way to cut a sequence into consecutive blocks of given lengths". This uniqueness is what makes $\mu$ cartesian, and it is the single point that would collapse if lists were replaced by *multisets*: cutting an unordered collection into blocks of given sizes is genuinely ambiguous, so the reconstruction fails and the multiplication square is not a pullback. Internalizing this gives a fast diagnostic for cartesianness — *is there an ordering that makes shape-reconstruction unique, or is a symmetry quotiented away that destroys it?* — which is far quicker than re-deriving pullback squares for each new monad (see the companion exercise on the multiset monad).

**Cartesianness is "no information is lost in flattening", and that is why operadic composition is well-defined.** The deeper reason this computation matters is that the cartesian $\mu$ is exactly what makes the composition law of a [[Def - Generalized Multicategory|$T$-multicategory]] associative: grafting a configuration-of-configurations and flattening must be reconstructible, or the composition is ambiguous. This exercise is therefore not a self-contained curiosity but the verification that the *list* monad — the one whose multicategories are classical multicategories — earns its place in the framework. The trigger to carry forward is: when a generalized composition needs to be associative, the obligation is precisely cartesianness of the multiplication, and this exercise is the template for discharging it. See [[Ex - The free-commutative-monoid monad is not cartesian]] for the contrasting failure and [[Thm - Generalized Operads Recover Classical Structures]] for what the cartesianness buys.
