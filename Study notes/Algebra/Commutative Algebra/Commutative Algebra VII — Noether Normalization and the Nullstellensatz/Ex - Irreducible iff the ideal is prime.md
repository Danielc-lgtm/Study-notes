---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Irreducible Algebraic Set"
  - "Thm - The Strong Nullstellensatz"
  - "Thm - The Weak Nullstellensatz"
  - "Def - Prime and Maximal Ideal"
  - "Def - The Coordinate Ring and the Ideal of a Set"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $\Omega$ be an algebraically closed field and $X \subseteq \Omega^n$ an algebraic set. Prove that
$$X \text{ is irreducible} \quad \Longleftrightarrow \quad I(X) \text{ is a prime ideal of } \Omega[T_1, \dots, T_n] \quad \Longleftrightarrow \quad \Omega[X] \text{ is an integral domain.}$$
You may use the fact (Example Sheet 2, Q2(a)) that in any ring, if a **prime** ideal $\mathfrak p$ equals a finite intersection $\mathfrak a_1 \cap \dots \cap \mathfrak a_\ell$ of ideals, then $\mathfrak p = \mathfrak a_i$ for some $i$.

**Recall:**

The objects in play are irreducibility, prime ideals, the strong and weak Nullstellensatz, and the coordinate ring.

![[Def - Irreducible Algebraic Set#The Definition]]

![[Def - Prime and Maximal Ideal#Prime ideal]]

For $X \subseteq \Omega^n$, $I(X)$ is the [[Def - The Coordinate Ring and the Ideal of a Set|ideal]] of polynomials vanishing on $X$, and $\Omega[X] = \Omega[T_1, \dots, T_n]/I(X)$ is the coordinate ring. We write $V(f) = V(\{f\})$. The [[Thm - The Strong Nullstellensatz|strong Nullstellensatz]] gives $I(V(\mathfrak a)) = \sqrt{\mathfrak a}$; the [[Thm - The Weak Nullstellensatz|weak Nullstellensatz]] gives $V(\mathfrak a) = \varnothing \iff 1 \in \mathfrak a$. An algebraic set is **irreducible** if nonempty and not a union of two proper algebraic subsets.

**Recall (prime quotient criterion):**

![[Thm - Maximal and Prime Ideals via Quotients#Statement]]

---

# Convergent Strategy

**Problem class.** This is an *equivalence-of-characterisations* problem establishing the central entry of the [[Thm - The Nullstellensatz Correspondence (radical ideals and varieties)|Nullstellensatz dictionary]]: geometric irreducibility $\iff$ algebraic primality. It is the proof that the geometric atoms (irreducible varieties) are exactly the prime ideals.

**Assumption pattern.** $X$ is an *algebraic set* over an *algebraically closed* $\Omega$, so $V(I(X)) = X$ and the strong/weak Nullstellensatz apply. The equivalence "$I(X)$ prime $\iff \Omega[X]$ a domain" is pure [[Thm - Maximal and Prime Ideals via Quotients|ring theory]] (prime $\iff$ domain quotient), needing no closure; the equivalence with *irreducibility* needs the Nullstellensatz to connect ideals to point sets.

**Theorem routing.** Two directions. *(Irreducible $\Rightarrow$ prime):* given $fg \in I(X)$, the product vanishes on $X$, so $X \subseteq V(f) \cup V(g)$, decomposing $X$; irreducibility forces $X \subseteq V(f)$ (say), giving $f \in I(X)$. *(Prime $\Rightarrow$ irreducible):* given $X = X_1 \cup X_2$, $I(X) = I(X_1) \cap I(X_2)$ ([[Ex - The ideal-variety correspondence and unions and intersections|union-to-intersection]]); since $I(X)$ is prime and equals a finite intersection, $I(X) = I(X_i)$ for some $i$ (ES2 Q2a), so $X = V(I(X)) = V(I(X_i)) = X_i$; nonemptiness from $1 \notin I(X)$ via the weak Nullstellensatz.

**Key decision point.** The non-obvious move in the forward direction is *translating $fg \in I(X)$ into the geometric covering $X \subseteq V(f) \cup V(g)$* — recognising that "$fg$ vanishes on $X$" means "at each point of $X$, $f$ or $g$ vanishes", which is a *union* of two closed sets. The non-obvious move in the reverse direction is *using ES2 Q2(a)* — that a prime equal to a finite intersection of ideals equals one of them — to convert the geometric decomposition $X = X_1 \cup X_2$ (an intersection of ideals) into "$I(X)$ is one of the $I(X_i)$". Both directions are the same fact ("vanishing of a product = union of vanishing loci") read in opposite directions.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz#Legal Operations|the topic page's Legal Operations]]:

1. **Translate a product vanishing into a union of zero loci.** $fg \in I(X) \Rightarrow X \subseteq V(f) \cup V(g)$.

2. **Decompose $X$ using a covering and invoke irreducibility.** $X = (X \cap V(f)) \cup (X \cap V(g))$ forces $X$ into one piece.

3. **Convert a union of varieties to an intersection of ideals.** $I(X_1 \cup X_2) = I(X_1) \cap I(X_2)$.

4. **Use that a prime equal to a finite intersection equals a factor (ES2 Q2a).** $I(X)$ prime $= I(X_1) \cap I(X_2) \Rightarrow I(X) = I(X_i)$.

5. **Recover nonemptiness from properness via the weak Nullstellensatz.** $1 \notin I(X) \Rightarrow V(I(X)) = X \neq \varnothing$.

---

# Hints

> [!note]- Hint 1
> For irreducible $\Rightarrow$ prime: take $fg \in I(X)$, so $fg$ vanishes on all of $X$. At each point of $X$, what does "$f(x)g(x) = 0$" say about $f(x)$ and $g(x)$ (remember $\Omega$ is a field)? Phrase the result as a *covering* of $X$ by two closed sets.

> [!note]- Hint 2
> $X \subseteq V(f) \cup V(g)$, so $X = (X \cap V(f)) \cup (X \cap V(g))$, a union of two algebraic subsets. Now use irreducibility: one of these must be all of $X$. If $X \subseteq V(f)$, what does that say about $f$ and $I(X)$?

> [!note]- Hint 3
> If $X \subseteq V(f)$ then $f$ vanishes on $X$, so $f \in I(X)$ — giving the prime condition "$fg \in I(X) \Rightarrow f \in I(X)$ or $g \in I(X)$". For the converse (prime $\Rightarrow$ irreducible), suppose $X = X_1 \cup X_2$. Apply $I(\cdot)$: what is $I(X_1 \cup X_2)$ in terms of $I(X_1), I(X_2)$?

> [!note]- Hint 4
> $I(X) = I(X_1) \cap I(X_2)$. Since $I(X)$ is *prime* and equals a finite intersection of ideals, ES2 Q2(a) gives $I(X) = I(X_i)$ for some $i$; apply $V$ to get $X = X_i$. Finally, $I(X)$ prime means $1 \notin I(X)$, so by the weak Nullstellensatz $V(I(X)) = X \neq \varnothing$ — irreducibility requires nonemptiness.

---

# Solution

The two directions are mirror images of the single fact "a product vanishes exactly where one factor does", which translates "$fg \in I(X)$" into "$X$ is covered by $V(f) \cup V(g)$". Forward, irreducibility forbids the covering from being proper, forcing $f$ or $g$ into $I(X)$ — primality. Backward, primality plus the union-to-intersection identity and ES2 Q2(a) forbids $X$ from splitting — irreducibility. The "$I(X)$ prime $\iff \Omega[X]$ a domain" equivalence is the standard quotient criterion.

**Step 1: $I(X)$ prime $\iff \Omega[X]$ is a domain.**

This is the quotient criterion, independent of geometry.

> [!note]- Derivation
> By [[Thm - Maximal and Prime Ideals via Quotients|prime ⟺ domain quotient]], $I(X)$ is prime if and only if $\Omega[T_1, \dots, T_n]/I(X) = \Omega[X]$ is an integral domain. This holds in any ring and needs no algebraic closure. So the third characterisation is automatic; the substance is connecting these to *irreducibility*.

**Step 2: Irreducible $\Rightarrow$ $I(X)$ prime.**

A product in $I(X)$ covers $X$ by two zero loci; irreducibility forces one factor to vanish on all of $X$.

> [!note]- Derivation
> First, $I(X) \neq \Omega[T]$ because $X \neq \varnothing$ (irreducible sets are nonempty), so $1 \notin I(X)$ — the ideal is proper. Now take $f, g$ with $fg \in I(X)$. Then $fg$ vanishes on $X$: for every $x \in X$, $f(x)g(x) = 0$, and since $\Omega$ is a field (no zero divisors), $f(x) = 0$ or $g(x) = 0$. Hence
> $$X \subseteq V(f) \cup V(g), \quad\text{so}\quad X = \big(X \cap V(f)\big) \cup \big(X \cap V(g)\big),$$
> a union of two algebraic subsets of $X$. By **irreducibility**, one of them is all of $X$; say $X = X \cap V(f)$, i.e. $X \subseteq V(f)$. Then $f$ vanishes on $X$, so $f \in I(X)$. (If instead $X \subseteq V(g)$, then $g \in I(X)$.) Thus $fg \in I(X) \Rightarrow f \in I(X)$ or $g \in I(X)$: $I(X)$ is prime.

**Step 3: $I(X)$ prime $\Rightarrow$ Irreducible.**

A decomposition of $X$ gives an intersection equal to the prime $I(X)$; ES2 Q2(a) collapses it.

> [!note]- Derivation
> Suppose $X = X_1 \cup X_2$ with $X_1, X_2$ algebraic subsets. By the [[Ex - The ideal-variety correspondence and unions and intersections|union-to-intersection identity]],
> $$I(X) = I(X_1 \cup X_2) = I(X_1) \cap I(X_2).$$
> Since $I(X)$ is **prime** and equals a finite intersection of ideals, ES2 Q2(a) gives $I(X) = I(X_i)$ for some $i$ (say $i = 1$). Applying $V$ and using $V(I(Y)) = Y$ for algebraic $Y$:
> $$X = V(I(X)) = V(I(X_1)) = X_1.$$
> So $X = X_1$, i.e. the decomposition was trivial — no proper splitting exists. Finally, $I(X)$ prime means $I(X) \neq \Omega[T]$, so $1 \notin I(X)$, and by the [[Thm - The Weak Nullstellensatz|weak Nullstellensatz]] $V(I(X)) = X \neq \varnothing$. A nonempty algebraic set with no proper decomposition is **irreducible**.

> [!note]- Complete formal solution
> **Claim.** For $X \subseteq \Omega^n$ algebraic ($\Omega$ algebraically closed): $X$ irreducible $\iff I(X)$ prime $\iff \Omega[X]$ a domain.
>
> *Prime $\iff$ domain:* the [[Thm - Maximal and Prime Ideals via Quotients|quotient criterion]], $I(X)$ prime $\iff \Omega[T]/I(X) = \Omega[X]$ a domain.
>
> *Irreducible $\Rightarrow$ prime:* $X \neq \varnothing$ gives $I(X)$ proper. If $fg \in I(X)$, then for all $x \in X$, $f(x)g(x) = 0$, so $f(x) = 0$ or $g(x) = 0$ ($\Omega$ a field); thus $X = (X \cap V(f)) \cup (X \cap V(g))$. Irreducibility forces $X \subseteq V(f)$ or $X \subseteq V(g)$, i.e. $f \in I(X)$ or $g \in I(X)$. So $I(X)$ is prime.
>
> *Prime $\Rightarrow$ irreducible:* if $X = X_1 \cup X_2$ then $I(X) = I(X_1) \cap I(X_2)$; $I(X)$ prime and equal to a finite intersection gives $I(X) = I(X_i)$ (ES2 Q2a), so $X = V(I(X)) = X_i$. And $1 \notin I(X)$ gives $X \neq \varnothing$ (weak Nullstellensatz). So $X$ is irreducible. $\blacksquare$

> [!warning] Illegal but tempting: using $X \subseteq V(f) \cup V(g) \Rightarrow X \subseteq V(f)$ or $X \subseteq V(g)$ without irreducibility
> The covering $X \subseteq V(f) \cup V(g)$ does *not* by itself force $X$ into one piece — that step *is* the irreducibility hypothesis, and it fails for reducible $X$. Concretely, for $X = V(T_1 T_2)$ (the two axes), take $f = T_1$, $g = T_2$: $fg = T_1 T_2 \in I(X)$, and $X \subseteq V(T_1) \cup V(T_2)$, but neither $T_1$ nor $T_2$ is in $I(X) = (T_1 T_2)$ (each axis contains points where the other coordinate is nonzero). The reducibility is exactly why $I(X) = (T_1 T_2)$ is *not* prime. The repair is precisely irreducibility: it is the condition that makes the covering-implies-containment step legal, which is why the equivalence holds.

---

# Key Takeaways

**"Vanishing of a product = union of zero loci" is the single mechanism behind irreducible $\iff$ prime.** Both directions of the equivalence run on the identity: $fg$ vanishes on $X$ iff $X \subseteq V(f) \cup V(g)$. The prime condition "$fg \in I(X) \Rightarrow f \in I(X)$ or $g \in I(X)$" is *literally* "the covering $X \subseteq V(f) \cup V(g)$ implies $X \subseteq V(f)$ or $X \subseteq V(g)$" — which is irreducibility. The trigger to internalise: a prime ideal is the algebra of an indecomposable shape, because the prime axiom is the impossibility of writing the shape as a union via a product relation. This is the geometric *meaning* of primality, and it generalises verbatim to schemes (integral $=$ reduced $+$ irreducible $=$ domain coordinate ring).

**ES2 Q2(a) — a prime equal to a finite intersection equals a factor — is the algebraic engine of "components".** The reverse direction needs that a prime ideal cannot be a *nontrivial* finite intersection: $\mathfrak p = \mathfrak a_1 \cap \dots \cap \mathfrak a_\ell \Rightarrow \mathfrak p = \mathfrak a_i$. Geometrically this says an irreducible variety cannot be properly covered by finitely many subvarieties — the defining property of irreducibility. This same lemma drives the decomposition of any algebraic set into finitely many irreducible *components* (the minimal primes of $I(X)$), and it is the reason "irreducible components" are well-defined and finite in number (Noetherian-ness). The diagnostic: whenever you must rule out a decomposition of an irreducible object, reach for "prime = intersection $\Rightarrow$ prime = a factor".

**The quotient criterion makes the third characterisation free, and the geometry is the bonus.** Half of the theorem — "$I(X)$ prime $\iff \Omega[X]$ a domain" — is pure ring theory ([[Thm - Maximal and Prime Ideals via Quotients|prime ⟺ domain quotient]]) and needs no Nullstellensatz; it is the *geometric* equivalence with irreducibility that requires algebraic closure (through $V(I(X)) = X$ and the weak Nullstellensatz for nonemptiness). The transferable lesson: when proving a geometric notion equals an algebraic one, separate the *ring-theoretic* core (often a quotient criterion, free) from the *geometric* bridge (needs the Nullstellensatz / closure). Here, "$\Omega[X]$ a domain" is the true name of "X irreducible" — operationally, to prove a variety irreducible, exhibit its coordinate ring as a domain (e.g. a subring of a field, or a polynomial ring), bypassing the covering argument entirely. This is exactly how one proves $V(f)$ irreducible for irreducible $f$: $\Omega[T]/(f)$ is a domain because $(f)$ is prime in the UFD $\Omega[T_1, \dots, T_n]$.
