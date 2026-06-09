---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Prime and Maximal Ideal"
  - "Def - Associated and Minimal Primes"
  - "Def - Noetherian Ring"
  - "Def - Radical of an Ideal and the Nilradical"
  - "Def - Irreducible Algebraic Set"
tags: [algebra, commutative-algebra]
---

# Problem Statement

This exercise proves the prime-avoidance lemma underlying minimal primes (ES2.2(a)) and the finiteness of minimal primes for radical ideals (ES2.2(c)–(d)), then translates both into geometry.

**Part (a) — primes swallow intersections (ES2.2a).** Let $\mathfrak{a}_1, \dots, \mathfrak{a}_n$ be ideals of $R$ and $\mathfrak{p}$ a [[Def - Prime and Maximal Ideal|prime]]. Prove: if $\bigcap_i \mathfrak{a}_i \subseteq \mathfrak{p}$ then $\mathfrak{a}_i \subseteq \mathfrak{p}$ for some $i$; and if $\bigcap_i \mathfrak{a}_i = \mathfrak{p}$ then $\mathfrak{a}_i = \mathfrak{p}$ for some $i$.

**Part (b) — finitely many minimal primes (ES2.2c–d).** Let $I$ be a radical ideal in a [[Def - Noetherian Ring|Noetherian ring]] $R$. Prove $I$ is a finite intersection of prime ideals, and deduce $I$ has finitely many minimal primes $\mathfrak{p}_1, \dots, \mathfrak{p}_t$ with $I = \mathfrak{p}_1 \cap \cdots \cap \mathfrak{p}_t$ and the $\mathfrak{p}_i$ pairwise incomparable.

**Part (c) — geometry.** With $R = k[X_1, \dots, X_n]$, $k$ algebraically closed, translate: the [[Def - Irreducible Algebraic Set|irreducible components]] of $V(I)$ are exactly the $V(\mathfrak{p}_i)$ for $\mathfrak{p}_i$ the minimal primes over $I$, there are finitely many, and none is contained in another. Illustrate with $I = (XY, XZ) \subseteq k[X,Y,Z]$.

**Recall:**

The objects in play are prime ideals, minimal primes, radical ideals in Noetherian rings, and irreducible algebraic sets.

![[Def - Prime and Maximal Ideal#The Definition]]

![[Def - Associated and Minimal Primes#Minimal prime over an ideal]]

A **minimal prime over $I$** is a prime $\mathfrak{p} \supseteq I$ with no prime strictly between. By the [[Thm - Minimal Primes are Finite in a Noetherian Ring|finiteness theorem]], a radical ideal in a Noetherian ring is a finite intersection of its minimal primes. An algebraic set is [[Def - Irreducible Algebraic Set|irreducible]] if it is not the union of two proper closed subsets; $V(\mathfrak{p})$ is irreducible exactly when $\mathfrak{p}$ is prime.

---

# Convergent Strategy

**Problem class.** This is a *foundational-lemma-plus-translation* problem: parts (a) and (b) are the algebraic engine (prime avoidance and Noetherian finiteness), and part (c) cashes them out as the finiteness and uniqueness of irreducible components. As the [[Commutative Algebra IX — Primary Decomposition#Problem-Solving Strategy|topic page strategy]] records, "components are finite" routes through Noetherian induction, and "minimal primes are the components" routes through prime avoidance.

**Assumption pattern.** Part (a) uses primeness in its multiplicative form: a prime not containing each $\mathfrak{a}_i$ has, for each, an escapee $a_i \notin \mathfrak{p}$, whose product $\prod a_i$ then escapes $\mathfrak{p}$ but lies in $\bigcap \mathfrak{a}_i$. Part (b) uses the Noetherian condition through a maximal-counterexample argument. The recognisable trigger in (a) is "a prime sits over an intersection" $\Rightarrow$ "build the product of escapees".

**Theorem routing.** Part (a): assume no $\mathfrak{a}_i \subseteq \mathfrak{p}$, pick escapees $a_i \in \mathfrak{a}_i \setminus \mathfrak{p}$, form $\prod a_i \in \bigcap \mathfrak{a}_i \subseteq \mathfrak{p}$, contradict primeness. Part (b): this is the [[Thm - Minimal Primes are Finite in a Noetherian Ring|finiteness theorem]] — maximal-counterexample induction with the splitting $\sqrt{I+(x)} \cap \sqrt{I+(y)} = I$; then use (a) to identify the surviving primes as the minimal ones. Part (c): apply the order-reversing dictionary $\mathfrak{p} \leftrightarrow V(\mathfrak{p})$ and $V(\bigcap \mathfrak{p}_i) = \bigcup V(\mathfrak{p}_i)$, with irreducibility of $V(\mathfrak{p}_i)$ from primeness of $\mathfrak{p}_i$.

**Key decision point.** The non-obvious move in (a) is *forming the product* $\prod a_i$ of escapees rather than reasoning about the intersection directly — the product lands in the intersection (each $a_i \in \mathfrak{a}_i$, and a product of things from different ideals lies in every $\mathfrak{a}_j$? no — careful: $\prod a_i$ lies in *each* $\mathfrak{a}_j$ because $a_j$ is a factor and $\mathfrak{a}_j$ absorbs the rest). In (c) the non-obvious move is that the *minimal* primes, not all primes over $I$, give the components — a non-minimal prime $\mathfrak{p}' \supsetneq \mathfrak{p}_i$ has $V(\mathfrak{p}') \subsetneq V(\mathfrak{p}_i)$, so it is contained in a component and not itself one.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra IX — Primary Decomposition#Legal Operations|the topic page's Legal Operations]]:

1. **Use $\bigcap \mathfrak{a}_i \subseteq \mathfrak{p} \Rightarrow$ some $\mathfrak{a}_i \subseteq \mathfrak{p}$ (operation 8).** This is part (a), the lemma being proved and then used.

2. **Decompose by Noetherian induction (operation 6).** Part (b) is the maximal-counterexample argument for radical ideals.

3. **Take radicals (operation 2).** Use $\sqrt{I + (x)}$ in the splitting and $\sqrt I = \bigcap \mathfrak{p}_i$.

4. **Translate to geometry via $V(-)$ (operation 9).** Part (c) applies $V(\bigcap \mathfrak{p}_i) = \bigcup V(\mathfrak{p}_i)$ and irreducibility.

---

# Hints

> [!note]- Hint 1 (part a)
> Contrapositive: suppose $\mathfrak{a}_i \not\subseteq \mathfrak{p}$ for *every* $i$. Then for each $i$ pick $a_i \in \mathfrak{a}_i \setminus \mathfrak{p}$. Consider the product $a_1 a_2 \cdots a_n$. Where does it live? It is in each $\mathfrak{a}_j$ (because $a_j$ is a factor and $\mathfrak{a}_j$ absorbs the other factors), hence in $\bigcap_i \mathfrak{a}_i$. Is it in $\mathfrak{p}$?

> [!note]- Hint 2 (part a)
> Since $\mathfrak{p}$ is prime and no $a_i \in \mathfrak{p}$, the product $a_1 \cdots a_n \notin \mathfrak{p}$. But $a_1 \cdots a_n \in \bigcap_i \mathfrak{a}_i \subseteq \mathfrak{p}$ — contradiction. So some $\mathfrak{a}_i \subseteq \mathfrak{p}$. For the "$=$" version: if $\bigcap \mathfrak{a}_i = \mathfrak{p}$ then some $\mathfrak{a}_i \subseteq \mathfrak{p} = \bigcap \mathfrak{a}_j \subseteq \mathfrak{a}_i$, forcing $\mathfrak{a}_i = \mathfrak{p}$.

> [!note]- Hint 3 (part b)
> This is the finiteness theorem. Maximal-counterexample: if some radical ideal is not a finite intersection of primes, take a maximal such $I$ (Noetherian). It is not prime, so $xy \in I$, $x, y \notin I$. Show $I = \sqrt{I+(x)} \cap \sqrt{I+(y)}$, both strictly larger and radical, hence (by maximality) finite intersections of primes — contradiction.

> [!note]- Hint 4 (part c)
> Use $V(\mathfrak{a} \cap \mathfrak{b}) = V(\mathfrak{a}) \cup V(\mathfrak{b})$ and $V(I) = V(\sqrt I)$. So $V(I) = V(\bigcap \mathfrak{p}_i) = \bigcup V(\mathfrak{p}_i)$, each $V(\mathfrak{p}_i)$ irreducible (prime $\Rightarrow$ irreducible). Incomparability of the $\mathfrak{p}_i$ gives no containments $V(\mathfrak{p}_i) \subseteq V(\mathfrak{p}_j)$. For $(XY, XZ)$: $\sqrt{(XY,XZ)} = (X) \cap (Y,Z)$, so the components are the plane $V(X)$ and the line $V(Y,Z)$.

---

# Solution

Part (a) is the product-of-escapees argument: if a prime contained none of the $\mathfrak{a}_i$, the product of one escapee from each would land in the intersection but escape the prime. Part (b) is the Noetherian maximal-counterexample, splitting a non-prime radical ideal as $\sqrt{I+(x)} \cap \sqrt{I+(y)}$. Part (c) translates: the minimal primes are the irreducible components, finitely many and incomparable. The non-obvious move is forming the product in (a) and recognising it sits in the intersection.

**Step 1 (a): a prime over an intersection contains a factor.**

> [!note]- Derivation
> Suppose $\bigcap_{i=1}^n \mathfrak{a}_i \subseteq \mathfrak{p}$ but $\mathfrak{a}_i \not\subseteq \mathfrak{p}$ for every $i$. For each $i$ choose $a_i \in \mathfrak{a}_i \setminus \mathfrak{p}$. Consider $a = a_1 a_2 \cdots a_n$. For each fixed $j$, $a_j \in \mathfrak{a}_j$ and $\mathfrak{a}_j$ absorbs the product of the other factors, so $a = a_j \cdot \prod_{i \neq j}a_i \in \mathfrak{a}_j$. As this holds for all $j$, $a \in \bigcap_i \mathfrak{a}_i \subseteq \mathfrak{p}$.
>
> But $\mathfrak{p}$ is [[Def - Prime and Maximal Ideal|prime]] and none of the factors $a_i$ lies in $\mathfrak{p}$, so by induction on the prime property ($\mathfrak{p}$ prime $\Rightarrow$ a product lies in $\mathfrak{p}$ only if a factor does), $a = a_1 \cdots a_n \notin \mathfrak{p}$. This contradicts $a \in \mathfrak{p}$. Hence some $\mathfrak{a}_i \subseteq \mathfrak{p}$.
>
> *The "$=$" case.* If $\bigcap_i \mathfrak{a}_i = \mathfrak{p}$, then $\bigcap_i \mathfrak{a}_i \subseteq \mathfrak{p}$ gives $\mathfrak{a}_i \subseteq \mathfrak{p}$ for some $i$; and $\mathfrak{p} = \bigcap_j \mathfrak{a}_j \subseteq \mathfrak{a}_i$, so $\mathfrak{a}_i = \mathfrak{p}$.

**Step 2 (b): a radical ideal in a Noetherian ring is a finite intersection of primes.**

The maximal-counterexample argument; identical to the [[Thm - Minimal Primes are Finite in a Noetherian Ring|finiteness theorem]].

> [!note]- Derivation
> Let $\Sigma$ be the set of radical ideals that are *not* finite intersections of primes. If $\Sigma \neq \varnothing$, then by [[Def - Noetherian Ring|Noetherianity]] $\Sigma$ has a maximal element $I$. $I$ is not prime (a prime is its own one-term intersection), so there are $x, y \notin I$ with $xy \in I$. Then
> $$\sqrt{I+(x)} \cap \sqrt{I+(y)} = I,$$
> since "$\supseteq$" is clear and, for "$\subseteq$", $z \in$ both gives $z^a \in I+(x)$, $z^b \in I+(y)$, so $z^{a+b} \in (I+(x))(I+(y)) \subseteq I + (xy) = I$, whence $z \in \sqrt I = I$. Both $\sqrt{I+(x)}$ and $\sqrt{I+(y)}$ strictly contain $I$ (they contain $x$ resp. $y \notin I$), so by maximality each is a finite intersection of primes; hence so is $I$, contradicting $I \in \Sigma$. So $\Sigma = \varnothing$: every radical ideal is $\mathfrak{p}_1 \cap \cdots \cap \mathfrak{p}_m$ for finitely many primes.
>
> *Minimal primes.* Discard any $\mathfrak{p}_j$ containing another (does not change the intersection), leaving incomparable $\mathfrak{p}_1, \dots, \mathfrak{p}_t$ with $I = \bigcap \mathfrak{p}_i$. By part (a), any prime $\mathfrak{q} \supseteq I = \bigcap \mathfrak{p}_i$ contains some $\mathfrak{p}_i$; so the minimal primes over $I$ are exactly the incomparable $\mathfrak{p}_i$ — finitely many.

**Step 3 (c): minimal primes are the irreducible components.**

> [!note]- Derivation
> Let $R = k[X_1, \dots, X_n]$, $k$ algebraically closed, $I$ radical with $I = \mathfrak{p}_1 \cap \cdots \cap \mathfrak{p}_t$ (minimal primes). Using $V(\mathfrak{a} \cap \mathfrak{b}) = V(\mathfrak{a}) \cup V(\mathfrak{b})$,
> $$V(I) = V(\mathfrak{p}_1 \cap \cdots \cap \mathfrak{p}_t) = V(\mathfrak{p}_1) \cup \cdots \cup V(\mathfrak{p}_t).$$
> Each $V(\mathfrak{p}_i)$ is [[Def - Irreducible Algebraic Set|irreducible]] because $\mathfrak{p}_i$ is prime (a closed set $V(\mathfrak{p})$ is irreducible iff $\mathfrak{p}$ is prime). Incomparability of the $\mathfrak{p}_i$ gives, via the order-reversing $\mathfrak{p} \mapsto V(\mathfrak{p})$, that no $V(\mathfrak{p}_i) \subseteq V(\mathfrak{p}_j)$ for $i \neq j$. So the $V(\mathfrak{p}_i)$ are the **irreducible components** of $V(I)$: finitely many, pairwise non-contained, maximal irreducible closed subsets.
>
> *Example.* $I = (XY, XZ) \subseteq k[X,Y,Z]$. Then $XY, XZ$ both have the factor $X$, and $\sqrt{(XY, XZ)} = (X) \cap (Y, Z)$: indeed $(XY, XZ) = (X) \cap (Y,Z)$ already (check: $f \in (X) \cap (Y,Z)$ means $f = aX$ and $f \in (Y,Z)$, forcing $a \in (Y,Z)$, so $f \in X(Y,Z) = (XY, XZ)$). Both $(X)$ and $(Y,Z)$ are prime ($R/(X) \cong k[Y,Z]$, $R/(Y,Z) \cong k[X]$, both domains) and incomparable. So $V(I) = V(X) \cup V(Y,Z)$: the *plane* $\{X = 0\}$ union the *line* $\{Y = Z = 0\}$ (the $X$-axis) — two irreducible components, of dimensions $2$ and $1$, neither containing the other.

> [!note]- Complete formal solution
> **(a)** If $\bigcap_i \mathfrak{a}_i \subseteq \mathfrak{p}$ and no $\mathfrak{a}_i \subseteq \mathfrak{p}$, pick $a_i \in \mathfrak{a}_i \setminus \mathfrak{p}$; then $a_1 \cdots a_n \in \bigcap_i \mathfrak{a}_i \subseteq \mathfrak{p}$, but $\mathfrak{p}$ prime and $a_i \notin \mathfrak{p}$ give $a_1 \cdots a_n \notin \mathfrak{p}$ — contradiction. So some $\mathfrak{a}_i \subseteq \mathfrak{p}$; if $\bigcap \mathfrak{a}_i = \mathfrak{p}$ then that $\mathfrak{a}_i = \mathfrak{p}$.
>
> **(b)** A maximal radical ideal $I$ that is not a finite intersection of primes is not prime, so $xy \in I$, $x,y \notin I$, and $I = \sqrt{I+(x)} \cap \sqrt{I+(y)}$ splits it into two strictly larger radical ideals, both finite intersections of primes by maximality — contradiction. So every radical ideal is $\bigcap_{i=1}^t \mathfrak{p}_i$ over its incomparable minimal primes, finitely many.
>
> **(c)** $V(I) = \bigcup_i V(\mathfrak{p}_i)$ with each $V(\mathfrak{p}_i)$ irreducible (prime) and pairwise non-contained (incomparable) — the irreducible components. For $I = (XY, XZ) = (X) \cap (Y,Z)$, the components are the plane $V(X)$ and the line $V(Y,Z)$. $\blacksquare$

---

# Key Takeaways

**When a prime sits over an intersection, build the product of escapees.** Part (a) is one of the most-used micro-lemmas in commutative algebra, and its proof is a fixed reflex: to show $\bigcap \mathfrak{a}_i \subseteq \mathfrak{p}$ forces some $\mathfrak{a}_i \subseteq \mathfrak{p}$, assume not, pick one escapee $a_i \in \mathfrak{a}_i \setminus \mathfrak{p}$ from each, and form their product. The product lands in *every* $\mathfrak{a}_j$ (each $a_j$ is a factor, and the ideal absorbs the rest), hence in the intersection, hence in $\mathfrak{p}$ — but a prime cannot contain a product of non-members. The trigger is literally "a prime contains an intersection of ideals", and the reaction is "product of escapees". This is the dual of the more famous *prime avoidance* lemma (an ideal contained in a union of primes is contained in one of them), and the two together handle almost every interaction between a single prime and a finite family of ideals. It is what identifies the minimal primes over $I$ as exactly the incomparable primes appearing in $\sqrt I$.

**Finiteness of components is a maximal-counterexample induction on radical ideals, and the splitting is the engine.** Part (b) showcases the single most reusable proof technique in the subject: to prove "every [radical ideal] has property $P$", consider the set of counterexamples, use Noetherianity to extract a *maximal* one, and derive a contradiction by *splitting* it into strictly larger pieces that, by maximality, have $P$. Here the splitting $\sqrt{I+(x)} \cap \sqrt{I+(y)} = I$ (available because $I$ is not prime) is the crux, and it works precisely on radical ideals — the radical closure is what lets $z^{a+b} \in I$ conclude $z \in I$. The transferable diagnostic: whenever finiteness or existence is claimed for ideals in a Noetherian ring, reach for the maximal counterexample, and look for a way to split it; the chain condition guarantees the maximal element exists, and a structural failure (here, non-primality) usually supplies the split. This same template proves [[Thm - Primary Decomposition Exists in a Noetherian Ring (Lasker-Noether)|Lasker–Noether existence]] and the finiteness of irreducible decompositions.

**Minimal primes are the components; non-minimal primes are sub-components.** The geometric payoff is that the irreducible components of $V(I)$ are the $V(\mathfrak{p})$ for $\mathfrak{p}$ *minimal* over $I$ — not all primes over $I$. A non-minimal prime $\mathfrak{p}' \supsetneq \mathfrak{p}_i$ gives a *smaller* closed set $V(\mathfrak{p}') \subsetneq V(\mathfrak{p}_i)$ sitting inside a component, so it is not itself a component. The order-reversing dictionary $\mathfrak{p} \mapsto V(\mathfrak{p})$ turns "minimal prime" into "maximal irreducible closed set", which is the definition of a component. The example $(XY, XZ) = (X) \cap (Y,Z)$ makes this vivid: a plane and a line, of different dimensions, meeting along the origin — and crucially the line is *not* contained in the plane, so both are genuine components. For spaced practice, hold the dictionary: minimal primes $\leftrightarrow$ irreducible components, finitely many (this theorem), pairwise incomparable, and $\sqrt I = \bigcap(\text{minimal primes})$ is the ideal of the figure-as-a-set. See [[Thm - Minimal Primes are Finite in a Noetherian Ring]] for the abstract finiteness and [[Ex - A primary decomposition in k[X,Y]]] for how embedded primes add structure beyond the components.
