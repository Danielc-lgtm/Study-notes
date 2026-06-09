---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Integral Element and Integral Extension"
  - "Def - Finite and Finite-Type Algebra"
  - "Def - Noetherian Ring"
  - "Thm - Characterizations of Integrality (Module-Finite Criterion)"
  - "Thm - Transitivity of Integrality and Finiteness"
  - "Thm - Hilbert's Basis Theorem"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $A \subseteq B \subseteq C$ be rings such that

1. $A$ is [[Def - Noetherian Ring|Noetherian]];
2. $C$ is [[Def - Finite and Finite-Type Algebra|finitely generated as an A-algebra]] (finite-type);
3. $C$ is [[Def - Finite and Finite-Type Algebra|finite over B]] (finitely generated as a $B$-module).

Prove that $B$ is finitely generated as an $A$-algebra. (Example Sheet 3 Q4; this is the **Artin–Tate lemma**.)

**Recall:**

The objects in play are Noetherian rings, finite and finite-type algebras, the module-finite criterion, transitivity, and Hilbert's basis theorem.

![[Def - Finite and Finite-Type Algebra#The Definition]]

![[Def - Noetherian Ring#The Definition]]

A ring is [[Def - Noetherian Ring|Noetherian]] if every ideal is finitely generated, equivalently every ascending chain of ideals stabilises; a key consequence ([[Thm - Hilbert's Basis Theorem|Hilbert's basis theorem]]) is that a finite-type algebra over a Noetherian ring is Noetherian, and a submodule of a finite module over a Noetherian ring is finite.

![[Thm - Characterizations of Integrality (Module-Finite Criterion)#Statement]]

The subtlety: a *sub*algebra of a finitely generated algebra need *not* be finitely generated in general — so condition (3), finiteness of $C$ over $B$, is doing essential work.

---

# Convergent Strategy

**Problem class.** This is a *finiteness-descent* problem of the most delicate kind: deducing finite generation of an *intermediate* ring $B$ from finiteness data above ($C$ finite over $B$) and a Noetherian hypothesis below ($A$ Noetherian). It is genuinely ⭐⭐⭐ because subalgebras of finitely generated algebras are *not* generally finitely generated — the standard caution being $k[xy, xy^2, xy^3, \dots] \subseteq k[x, y]$ — so the proof must use *all three* hypotheses, and the trick (manufacturing a Noetherian intermediate ring $A'$) is non-obvious.

**Assumption pattern.** Three hypotheses, each indispensable. *$C$ finite-type over $A$* gives finitely many algebra generators $x_1, \dots, x_m$ of $C$. *$C$ finite over $B$* gives finitely many module generators $y_1, \dots, y_n$ of $C$ over $B$. *$A$ Noetherian* will, via Hilbert's basis theorem, make a cleverly chosen intermediate ring Noetherian, so that a submodule (which will turn out to contain $B$) is finite. The trigger is "descend finite generation through a tower with a Noetherian base".

**Theorem routing.** The route: express each generator $x_i$ and each product $y_i y_j$ in terms of the $y$'s with coefficients in $B$; collect *all* those finitely many $B$-coefficients into $A' = A[\text{coefficients}]$, a *finite-type $A$-algebra*, hence Noetherian by [[Thm - Hilbert's Basis Theorem|Hilbert's basis theorem]]. Show $C$ is *finite as an $A'$-module* (the $y$'s span it over $A'$). Then $B$, sandwiched as $A' \subseteq B \subseteq C$, is an $A'$-submodule of the finite $A'$-module $C$ over the Noetherian ring $A'$, hence *finite over $A'$* ([[Thm - Characterizations of Integrality (Module-Finite Criterion)|submodule of finite module over Noetherian is finite]]). Finally $B$ finite over $A'$ and $A'$ finite-type over $A$ make $B$ finite-type over $A$.

**Key decision point.** The crux — and the reason this is hard — is *constructing $A'$*. You must realise that the $B$-coefficients appearing in (a) the expression of the *algebra* generators $x_i$ in terms of the *module* generators $y_j$, and (b) the multiplication table $y_i y_j = \sum b_{ijk} y_k$, are *finitely many* elements of $B$, and that adjoining exactly these to $A$ produces a Noetherian ring $A'$ over which $C$ is *finite* (not merely finite-type). This is the inspired move; everything else is bookkeeping. The danger is to try to prove $B$ finite-type directly, which fails because subalgebras need not be finitely generated.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra VI — Integral Extensions#Legal Operations|the topic page's Legal Operations]]:

1. **Stack finiteness through a tower (operation 3).** Combine "$B$ finite over $A'$" with "$A'$ finite-type over $A$" to get "$B$ finite-type over $A$".

2. **Collect finitely many coefficients into an intermediate ring.** Form $A' = A[\text{the } B\text{-coefficients}]$ — the same finite-coefficient device as in [[Thm - Transitivity of Integrality and Finiteness|transitivity]], used here to manufacture a Noetherian ring.

3. **Invoke Hilbert's basis theorem.** $A$ Noetherian $+$ $A'$ finite-type over $A$ $\Rightarrow A'$ Noetherian ([[Thm - Hilbert's Basis Theorem]]).

4. **Use that a submodule of a finite module over a Noetherian ring is finite.** $B \subseteq C$, with $C$ finite over the Noetherian $A'$, forces $B$ finite over $A'$.

---

# Hints

> [!note]- Hint 1
> Be warned: a *subalgebra* of a finitely generated algebra need not be finitely generated (e.g. $k[xy, xy^2, xy^3, \dots] \subseteq k[x, y]$). So you cannot deduce $B$ finite-type from $C$ finite-type alone — condition (3), $C$ finite over $B$, must be used. The strategy is to find a *Noetherian* ring sitting between $A$ and $B$ over which everything becomes finite.

> [!note]- Hint 2
> Write the data explicitly. Let $x_1, \dots, x_m$ generate $C$ as an $A$-algebra, and $y_1, \dots, y_n$ generate $C$ as a $B$-module (say $y_1 = 1$). Two sets of equations:
> $$x_i = \sum_j b_{ij}\, y_j, \qquad y_i y_j = \sum_k b_{ijk}\, y_k,$$
> with all $b_{ij}, b_{ijk} \in B$. How many such coefficients are there? Finitely many. What ring should you build from them?

> [!note]- Hint 3
> Let $A' = A[\,b_{ij}, b_{ijk}\,] \subseteq B$, the $A$-subalgebra generated by those finitely many coefficients. Then $A'$ is *finite-type over $A$*, hence **Noetherian** by Hilbert's basis theorem. Claim: $C$ is a *finite $A'$-module*, spanned by $y_1, \dots, y_n$. Prove this using the two sets of equations (every element of $C$ is an $A$-polynomial in the $x_i$, which you rewrite in the $y_j$ with coefficients in $A'$).

> [!note]- Hint 4
> Now $A' \subseteq B \subseteq C$ with $C$ a finite $A'$-module and $A'$ Noetherian. A submodule of a finite module over a Noetherian ring is finite — so $B$ is a *finite $A'$-module*. Finally, $B$ finite over $A'$ and $A'$ finite-type over $A$ give $B$ finite-type over $A$ (a module-finite extension of a finite-type algebra is finite-type).

---

# Solution

The plan: the naive hope "subalgebra of finite-type is finite-type" is false, so condition (3) must be used to manufacture a *Noetherian* intermediate ring $A'$ — generated over $A$ by the finitely many $B$-coefficients in the expressions for the algebra generators and the module multiplication table. Over $A'$, the ring $C$ becomes a *finite module*; then $B$, trapped between $A'$ and $C$, is a submodule of a finite module over a Noetherian ring, hence finite over $A'$; and finite-over-$A'$ plus $A'$-finite-type-over-$A$ gives $B$ finite-type over $A$.

**Step 1: Set up the generators and the two coefficient systems.**

Let $C = A[x_1, \dots, x_m]$ (algebra generators) and $C = By_1 + \cdots + By_n$ (module generators, $y_1 = 1$). Write each $x_i$ and each product $y_i y_j$ in terms of the $y$'s with $B$-coefficients.

> [!note]- Derivation
> By hypothesis (2), $C$ is generated as an $A$-algebra by finitely many elements $x_1, \dots, x_m$. By hypothesis (3), $C$ is generated as a $B$-module by finitely many elements $y_1, \dots, y_n$; we may take $y_1 = 1$ (adjoin $1$ to the generating set).
>
> Since the $x_i \in C = \sum_j B y_j$, there are $b_{ij} \in B$ with
> $$x_i = \sum_{j=1}^n b_{ij}\, y_j \qquad (1 \leq i \leq m).$$
> Since each product $y_i y_j \in C = \sum_k B y_k$, there are $b_{ijk} \in B$ with
> $$y_i y_j = \sum_{k=1}^n b_{ijk}\, y_k \qquad (1 \leq i, j \leq n).$$
> These are *finitely many* coefficients in $B$: $mn$ of the $b_{ij}$ and $n^3$ of the $b_{ijk}$.

**Step 2: Build the Noetherian intermediate ring $A'$.**

Let $A' = A[\,\{b_{ij}\}, \{b_{ijk}\}\,] \subseteq B$. Then $A'$ is finite-type over $A$, hence Noetherian.

> [!note]- Derivation
> Define $A'$ to be the $A$-subalgebra of $B$ generated by the finitely many coefficients $b_{ij}, b_{ijk}$:
> $$A' = A[\,b_{ij}\ (1 \leq i \leq m, 1 \leq j \leq n),\ \ b_{ijk}\ (1 \leq i, j, k \leq n)\,].$$
> Being generated over $A$ by finitely many elements, $A'$ is a [[Def - Finite and Finite-Type Algebra|finite-type]] $A$-algebra. Since $A$ is [[Def - Noetherian Ring|Noetherian]], [[Thm - Hilbert's Basis Theorem|Hilbert's basis theorem]] gives that $A'$ — a quotient of a polynomial ring $A[T_1, \dots, T_N]$ over the Noetherian $A$ — is itself **Noetherian**. Note $A \subseteq A' \subseteq B$.

**Step 3: $C$ is a finite $A'$-module, spanned by $y_1, \dots, y_n$.**

Every element of $C$ is an $A'$-linear combination of the $y_j$, because the multiplication table has coefficients in $A'$ and the $x_i$ expand into the $y_j$ over $A'$.

> [!note]- Derivation
> Let $M = A' y_1 + \cdots + A' y_n \subseteq C$. We show $M = C$.
>
> First, $M$ is closed under multiplication: $y_i y_j = \sum_k b_{ijk} y_k$ with $b_{ijk} \in A'$, so a product of two $y$'s lies in $M$; by bilinearity any product of two elements of $M$ lies in $M$, so $M$ is a subring of $C$. It contains $A'$ (as $y_1 = 1$, so $A' = A' y_1 \subseteq M$) and contains each $x_i = \sum_j b_{ij} y_j$ with $b_{ij} \in A'$, so $x_i \in M$.
>
> Therefore $M$ is a subring of $C$ containing $A'$ and all the $x_i$. But $C = A[x_1, \dots, x_m] \subseteq A'[x_1, \dots, x_m] \subseteq M$ (the last inclusion because $M$ is a ring containing $A'$ and the $x_i$, hence all $A'$-polynomials in them). So $C \subseteq M \subseteq C$, giving $M = C$. Thus $C = \sum_j A' y_j$ is a **finite $A'$-module**.

**Step 4: $B$ is finite over $A'$, hence finite-type over $A$.**

$B$ is an $A'$-submodule of the finite $A'$-module $C$ over the Noetherian $A'$, hence finite over $A'$; then $B$ finite over $A'$ and $A'$ finite-type over $A$ give $B$ finite-type over $A$.

> [!note]- Derivation
> We have $A' \subseteq B \subseteq C$. By Step 3, $C$ is a finite $A'$-module, and by Step 2, $A'$ is Noetherian. A submodule of a finitely generated module over a Noetherian ring is finitely generated ([[Thm - Characterizations of Integrality (Module-Finite Criterion)|standard Noetherian module fact]] — over a Noetherian ring, finitely generated modules are Noetherian, so their submodules are finitely generated). The subset $B$ is an $A'$-submodule of $C$ (it is closed under $A'$-scaling since $A' \subseteq B$, and under addition). Hence $B$ is a **finite $A'$-module**, say $B = A' z_1 + \cdots + A' z_r$.
>
> Finally, assemble: $A'$ is generated as an $A$-algebra by the coefficients $\{b_{ij}, b_{ijk}\}$, and $B$ is generated as an $A'$-*module* (hence a fortiori as an $A'$-algebra) by $z_1, \dots, z_r$. So $B$ is generated as an $A$-algebra by the *finite* set $\{b_{ij}\} \cup \{b_{ijk}\} \cup \{z_1, \dots, z_r\}$:
> $$B = A[\,b_{ij},\, b_{ijk},\, z_1, \dots, z_r\,].$$
> Therefore $B$ is finitely generated as an $A$-algebra. $\blacksquare$

> [!note]- Complete formal solution
> **Claim (Artin–Tate).** With $A$ Noetherian, $C$ finite-type over $A$, and $C$ finite over $B$, the ring $B$ is finite-type over $A$.
>
> Write $C = A[x_1, \dots, x_m]$ and $C = \sum_{j=1}^n B y_j$ with $y_1 = 1$. There are $b_{ij}, b_{ijk} \in B$ with
> $$x_i = \sum_j b_{ij} y_j, \qquad y_i y_j = \sum_k b_{ijk} y_k.$$
> Let $A' = A[\{b_{ij}\}, \{b_{ijk}\}] \subseteq B$. Then $A'$ is finite-type over $A$, hence Noetherian by [[Thm - Hilbert's Basis Theorem|Hilbert's basis theorem]].
>
> The $A'$-module $M = \sum_j A' y_j$ is a subring of $C$ (closed under multiplication by the $y_i y_j$ relations, with coefficients now in $A'$), contains $A'$ and the $x_i$, hence contains $A[x_1, \dots, x_m] = C$; so $C = M$ is finite over $A'$.
>
> Then $B$, an $A'$-submodule of the finite $A'$-module $C$ over the Noetherian ring $A'$, is finite over $A'$: $B = \sum_l A' z_l$. Combining, $B = A[\{b_{ij}\}, \{b_{ijk}\}, \{z_l\}]$ is finitely generated as an $A$-algebra. $\blacksquare$

---

# Key Takeaways

**To descend finite generation through a tower, manufacture a Noetherian intermediate ring from the structure constants.** The signature technique here — and the reason the lemma is non-trivial — is building $A' = A[\text{the finitely many } B\text{-coefficients}]$ that appear in the expressions for the algebra generators *and* in the module multiplication table. This $A'$ is finite-type over the Noetherian $A$, hence Noetherian (Hilbert), and — crucially — $C$ becomes a *finite module* over it, even though $C$ was only finite-type over $A$. The intermediate ring "absorbs just enough of $B$" to make the higher data finite while staying small enough to be Noetherian. This pattern — *collect the structure constants of a presentation into a finitely generated subring to gain Noetherianity* — recurs whenever one needs to descend a finiteness property, and it is the same finite-coefficient device that drives [[Thm - Transitivity of Integrality and Finiteness|transitivity of integrality]], here upgraded with a Noetherian hypothesis.

**Subalgebras of finitely generated algebras are NOT generally finitely generated — which is why all three hypotheses are load-bearing.** The trap this exercise teaches you to respect: from "$C$ is finite-type over $A$" alone you cannot conclude "$B$ is finite-type over $A$", because subalgebras can be wild. The standard witness is $k[xy, xy^2, xy^3, \dots] \subseteq k[x, y]$: the subalgebra needs infinitely many generators (each $xy^n$ is a new generator, since no finite subset's products reach all of them). The Artin–Tate lemma rescues finite generation of $B$ *only* because of the extra hypothesis that $C$ is *finite* (module-finite) over $B$ — this is what lets you trap $B$ as a submodule of a finite module. Track where each of the three hypotheses is used: finite-type-of-$C$ gives the $x_i$; finite-of-$C$-over-$B$ gives the $y_j$ and the multiplication table; Noetherian-$A$ makes $A'$ Noetherian so the submodule $B$ is finite. Drop any one and the conclusion fails.

**Module-finite is the strong, descendable notion; finite-type is the weak, non-descendable one — and Noetherianity bridges them.** The deep structural lesson is the asymmetry between the two finiteness conditions of [[Def - Finite and Finite-Type Algebra]]. *Finite-type* (algebra-finite) does not descend to subalgebras. *Finite* (module-finite) *does* descend to submodules — but only over a Noetherian ring, where finitely generated modules are Noetherian. The whole proof is a relay that converts the non-descendable finite-type data into descendable module-finite data (by passing to $A'$, over which $C$ is module-finite), descends it to $B$ (submodule of a finite module over Noetherian $A'$), and then converts back (module-finite over $A'$ plus finite-type $A'$-over-$A$ gives finite-type $B$-over-$A$). Recognising which finiteness you have and which you need — and that Noetherianity is the bridge that lets module-finiteness be inherited by submodules — is the transferable insight, central to the finiteness theorems of [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz|Noether normalization]] and the finiteness of integral closure.
