---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Strong Nullstellensatz"
  - "Thm - The Weak Nullstellensatz"
  - "Def - Radical of an Ideal and the Nilradical"
  - "Def - Prime and Maximal Ideal"
  - "Def - Finitely Generated Algebra"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $A$ be a finitely generated $k$-algebra and $I$ an ideal of $A$. Prove that the radical of $I$ equals the intersection of all maximal ideals of $A$ containing $I$:
$$\sqrt{I} = \bigcap_{\substack{\mathfrak m \in \operatorname{mSpec} A \\ I \subseteq \mathfrak m}} \mathfrak m.$$
(This is Example Sheet 3, Question 5; the hint is to use the strong Nullstellensatz.) In particular, taking $I = (0)$, the **nilradical** of a finitely generated $k$-algebra is the intersection of its maximal ideals — i.e. such rings are **Jacobson**: nilradical $=$ Jacobson radical.

**Recall:**

The objects in play are the radical, maximal ideals, finitely generated algebras, and the strong Nullstellensatz.

![[Def - Radical of an Ideal and the Nilradical#The Definition]]

![[Thm - The Strong Nullstellensatz#Statement]]

A $k$-algebra $A$ is **finitely generated** if $A = k[a_1, \dots, a_n]$ for finitely many $a_i$, equivalently $A \cong k[T_1, \dots, T_n]/J$ for an ideal $J$ ([[Def - Finitely Generated Algebra|finitely generated algebra]]). The **Jacobson radical** $J(A)$ is the intersection of all maximal ideals of $A$. In general $\sqrt{(0)} = \operatorname{nil}(A) \subseteq J(A)$ for any ring; the content here is that *equality* holds — and persists for every $I$ — when $A$ is finitely generated over a field.

---

# Convergent Strategy

**Problem class.** This is a *radical-equals-intersection* problem, establishing that finitely generated $k$-algebras are **Jacobson rings**. It is the bridge between two descriptions of the radical: the algebraic one ($\sqrt I = $ functions some power of which lands in $I$) and the geometric/spectral one ($\sqrt I = $ functions vanishing at every point of $V(I)$). The topic page's strategy files it under "compute a radical by translating to vanishing via the strong Nullstellensatz".

**Assumption pattern.** The decisive assumption is that $A$ is *finitely generated over a field* — this is exactly the hypothesis under which the strong Nullstellensatz, and its corollary "maximal ideals are points", hold. The general inclusion $\sqrt I = \bigcap_{I \subseteq \mathfrak p}\mathfrak p$ (intersection of *primes*, from [[Commutative Algebra IV — Localization|localization]]) holds in any ring; the strengthening to *maximal* ideals is special to finitely generated algebras and is the whole point.

**Theorem routing.** Reduce to the polynomial ring: write $A = k[T_1, \dots, T_n]/J$ and pull back to ideals of $k[T_1, \dots, T_n]$ containing $J$, so it suffices to prove the statement for a polynomial ring and an ideal $\mathfrak a \supseteq$ nothing extra. There, the route is: $\sqrt{\mathfrak a} = I(V(\mathfrak a))$ ([[Thm - The Strong Nullstellensatz|strong Nullstellensatz]]); the maximal ideals containing $\mathfrak a$ are exactly the $\mathfrak m_x$ for $x \in V(\mathfrak a)$ ([[Thm - The Weak Nullstellensatz|weak Nullstellensatz]], point form); and $I(V(\mathfrak a)) = \bigcap_{x \in V(\mathfrak a)} \mathfrak m_x$ because $f$ vanishes on $V(\mathfrak a)$ iff $f \in \mathfrak m_x$ for every $x \in V(\mathfrak a)$. Chaining gives $\sqrt{\mathfrak a} = \bigcap_{\mathfrak a \subseteq \mathfrak m}\mathfrak m$.

**Key decision point.** The non-obvious recognition is that **"$f$ vanishes on the whole variety" is the same as "$f$ lies in every maximal ideal $\mathfrak m_x$ of a point $x$ of the variety"** — the identity $I(V(\mathfrak a)) = \bigcap_{x \in V(\mathfrak a)} I(\{x\}) = \bigcap_{x \in V(\mathfrak a)}\mathfrak m_x$. This converts the strong Nullstellensatz (about vanishing) into a statement about maximal ideals (about containment). A reader who tries to prove "$\sqrt I = \bigcap \mathfrak m$" by pure ideal theory, without the geometric detour through points, is fighting the general (false-for-primes-only) inclusion and will not get *maximal*.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz#Legal Operations|the topic page's Legal Operations]]:

1. **Reduce a finitely generated algebra to a polynomial ring quotient.** Write $A = k[T_1, \dots, T_n]/J$ and lift the statement to ideals containing $J$.

2. **Replace the radical by the ideal of the vanishing set.** $\sqrt{\mathfrak a} = I(V(\mathfrak a))$ via the strong Nullstellensatz.

3. **Identify maximal ideals containing $\mathfrak a$ with points of $V(\mathfrak a)$.** Via the weak Nullstellensatz point form, $\mathfrak m \supseteq \mathfrak a \iff \mathfrak m = \mathfrak m_x$ with $x \in V(\mathfrak a)$.

4. **Express the ideal of a set as an intersection of point-ideals.** $I(X) = \bigcap_{x \in X}\mathfrak m_x$, since vanishing on $X$ is vanishing at each point.

---

# Hints

> [!note]- Hint 1
> One inclusion is general: $\sqrt I \subseteq \mathfrak m$ for any maximal (indeed prime) $\mathfrak m \supseteq I$, because primes are radical and swallow radicals. So the work is the reverse inclusion — showing anything in *every* maximal ideal above $I$ already lies in $\sqrt I$. What special feature of finitely generated $k$-algebras lets maximal ideals "see" the radical?

> [!note]- Hint 2
> Reduce to $A = k[T_1, \dots, T_n]$ (quotients are handled by lifting). The hint on the sheet is the **strong Nullstellensatz**: $\sqrt{\mathfrak a} = I(V(\mathfrak a))$. So $\sqrt{\mathfrak a}$ is the set of polynomials vanishing on the *variety* $V(\mathfrak a)$. Now you need to express "vanishing on $V(\mathfrak a)$" in terms of maximal ideals.

> [!note]- Hint 3
> By the weak Nullstellensatz, the points of $V(\mathfrak a)$ are exactly the maximal ideals $\mathfrak m_x$ containing $\mathfrak a$. And $f$ vanishes at $x$ iff $f \in \mathfrak m_x = I(\{x\})$. So $I(V(\mathfrak a)) = \bigcap_{x \in V(\mathfrak a)} \mathfrak m_x$. Combine with $\sqrt{\mathfrak a} = I(V(\mathfrak a))$.

> [!note]- Hint 4
> Putting it together: $\sqrt{\mathfrak a} = I(V(\mathfrak a)) = \bigcap_{x \in V(\mathfrak a)} \mathfrak m_x = \bigcap_{\mathfrak a \subseteq \mathfrak m}\mathfrak m$, the last equality because maximal ideals containing $\mathfrak a$ are precisely the $\mathfrak m_x$ with $x \in V(\mathfrak a)$. For a general finitely generated $A = k[T]/J$, a maximal ideal of $A$ is $\bar{\mathfrak m}$ for a maximal $\mathfrak m \supseteq J$ of $k[T]$, and the bijection of ideals containing $J$ carries the whole argument over.

---

# Solution

The proof reduces to a polynomial ring, where the strong Nullstellensatz rewrites the radical as "functions vanishing on the variety", and the weak Nullstellensatz identifies the points of the variety with the maximal ideals above the ideal. The two together turn $\sqrt{\mathfrak a}$ into the intersection of those maximal ideals. The easy inclusion is general ring theory; the substance is the reverse inclusion, supplied by the Nullstellensatz.

**Step 1: The easy inclusion $\sqrt I \subseteq \bigcap_{I \subseteq \mathfrak m}\mathfrak m$ holds in any ring.**

A maximal ideal is prime, hence radical, so it contains $\sqrt I$ whenever it contains $I$.

> [!note]- Derivation
> Let $\mathfrak m$ be maximal with $I \subseteq \mathfrak m$. Maximal ideals are [[Def - Prime and Maximal Ideal|prime]], and prime ideals are radical ($\sqrt{\mathfrak m} = \mathfrak m$). If $f \in \sqrt I$ then $f^r \in I \subseteq \mathfrak m$ for some $r$; since $\mathfrak m$ is prime, $f \in \mathfrak m$. So $\sqrt I \subseteq \mathfrak m$ for every such $\mathfrak m$, hence $\sqrt I \subseteq \bigcap_{I \subseteq \mathfrak m}\mathfrak m$. This direction uses nothing about finite generation.

**Step 2: Reduce to a polynomial ring.**

It suffices to prove the reverse inclusion for $A = k[T_1, \dots, T_n]$; the general case follows by lifting along $A = k[T]/J$.

> [!note]- Derivation
> Write $A = k[T_1, \dots, T_n]/J$ and let $\pi : k[T] \to A$ be the quotient. The ideal $I \trianglelefteq A$ is $\pi(\mathfrak a)$ for $\mathfrak a := \pi^{-1}(I) \supseteq J$. The correspondence theorem gives an inclusion-preserving bijection between ideals of $A$ and ideals of $k[T]$ containing $J$, under which maximal ideals correspond to maximal ideals and radicals to radicals: $\pi^{-1}(\sqrt I) = \sqrt{\mathfrak a}$ and $\pi^{-1}(\bigcap_{I \subseteq \bar{\mathfrak m}}\bar{\mathfrak m}) = \bigcap_{\mathfrak a \subseteq \mathfrak m}\mathfrak m$ (intersection over maximal ideals of $k[T]$ containing $\mathfrak a$, equivalently containing $J$). So the identity for $A$ follows from the identity $\sqrt{\mathfrak a} = \bigcap_{\mathfrak a \subseteq \mathfrak m}\mathfrak m$ in $k[T]$. We prove that. (For the bijection of maximal ideals over $\Omega \supseteq k$, work in $\Omega[T]$; the statement over $k$ follows since maximal ideals of $k[T]/J$ correspond to Galois orbits, which does not affect the *intersection*.)

**Step 3: Strong Nullstellensatz rewrites the radical.**

In $\Omega[T_1, \dots, T_n]$, $\sqrt{\mathfrak a} = I(V(\mathfrak a))$ — the polynomials vanishing on the variety.

> [!note]- Derivation
> By the [[Thm - The Strong Nullstellensatz|strong Nullstellensatz]] (over the algebraically closed $\Omega \supseteq k$),
> $$\sqrt{\mathfrak a} = I(V(\mathfrak a)) = \{f : f(x) = 0 \text{ for all } x \in V(\mathfrak a)\}.$$
> This is the crucial input: it converts the *algebraic* radical into a *geometric* vanishing condition.

**Step 4: Vanishing on $V(\mathfrak a)$ = lying in every maximal ideal above $\mathfrak a$.**

$I(V(\mathfrak a)) = \bigcap_{x \in V(\mathfrak a)}\mathfrak m_x = \bigcap_{\mathfrak a \subseteq \mathfrak m}\mathfrak m$.

> [!note]- Derivation
> For a point $x$, $I(\{x\}) = \mathfrak m_x$ (functions vanishing at $x$ are exactly those in the maximal ideal of $x$). A polynomial vanishes on all of $V(\mathfrak a)$ iff it vanishes at each $x \in V(\mathfrak a)$ iff it lies in every $\mathfrak m_x$:
> $$I(V(\mathfrak a)) = \bigcap_{x \in V(\mathfrak a)} I(\{x\}) = \bigcap_{x \in V(\mathfrak a)} \mathfrak m_x.$$
> By the [[Thm - The Weak Nullstellensatz|weak Nullstellensatz]] (point form), the maximal ideals containing $\mathfrak a$ are *exactly* the $\mathfrak m_x$ with $x \in V(\mathfrak a)$: indeed $\mathfrak m_x \supseteq \mathfrak a \iff$ every $f \in \mathfrak a$ vanishes at $x \iff x \in V(\mathfrak a)$. Hence
> $$\bigcap_{x \in V(\mathfrak a)} \mathfrak m_x = \bigcap_{\mathfrak a \subseteq \mathfrak m}\mathfrak m.$$
> Chaining Steps 3–4: $\sqrt{\mathfrak a} = I(V(\mathfrak a)) = \bigcap_{\mathfrak a \subseteq \mathfrak m}\mathfrak m$, the reverse (and hence, with Step 1, full) inclusion.

> [!note]- Complete formal solution
> **Claim.** For $A$ a finitely generated $k$-algebra and $I \trianglelefteq A$, $\sqrt I = \bigcap_{I \subseteq \mathfrak m \in \operatorname{mSpec} A} \mathfrak m$.
>
> *Easy inclusion.* Each maximal $\mathfrak m \supseteq I$ is prime, hence radical, so $\sqrt I \subseteq \mathfrak m$; thus $\sqrt I \subseteq \bigcap \mathfrak m$.
>
> *Reverse inclusion.* Reduce to $A = k[T_1, \dots, T_n]$ via $A = k[T]/J$ and the correspondence of ideals containing $J$. Over $\Omega \supseteq k$ algebraically closed, the [[Thm - The Strong Nullstellensatz|strong Nullstellensatz]] gives $\sqrt{\mathfrak a} = I(V(\mathfrak a))$. A polynomial vanishes on $V(\mathfrak a)$ iff it lies in $\mathfrak m_x = I(\{x\})$ for every $x \in V(\mathfrak a)$, so $I(V(\mathfrak a)) = \bigcap_{x \in V(\mathfrak a)}\mathfrak m_x$. By the [[Thm - The Weak Nullstellensatz|weak Nullstellensatz]], $\{\mathfrak m_x : x \in V(\mathfrak a)\}$ is exactly the set of maximal ideals containing $\mathfrak a$. Hence $\sqrt{\mathfrak a} = \bigcap_{\mathfrak a \subseteq \mathfrak m}\mathfrak m$, and lifting back, $\sqrt I = \bigcap_{I \subseteq \mathfrak m}\mathfrak m$.
>
> In particular, with $I = (0)$: $\operatorname{nil}(A) = \sqrt{(0)} = \bigcap_{\mathfrak m \in \operatorname{mSpec} A}\mathfrak m = J(A)$, so finitely generated $k$-algebras are **Jacobson**. $\blacksquare$

> [!warning] Illegal but tempting: claiming $\sqrt I = \bigcap_{I \subseteq \mathfrak m}\mathfrak m$ in an arbitrary ring
> The identity with *maximal* ideals is **false** in general rings — it holds only for Jacobson rings (of which finitely generated $k$-algebras are the prototype). The always-true statement is $\sqrt I = \bigcap_{I \subseteq \mathfrak p}\mathfrak p$, the intersection of *primes*. The gap is real: in a [[Commutative Algebra IV — Localization|local ring]] $(R, \mathfrak m)$ like $\mathbb{Z}_{(p)}$, the intersection of *maximal* ideals is just $\mathfrak m = p\mathbb{Z}_{(p)}$, whereas $\sqrt{(0)} = (0)$ — so nilradical $\neq$ Jacobson radical there. What rescues finitely generated algebras is precisely the weak Nullstellensatz: enough maximal ideals (one per point) to detect every prime. The repair condition is "the ring is Jacobson", i.e. every prime is an intersection of maximals.

---

# Key Takeaways

**The strong Nullstellensatz is the converter between "radical" and "vanishing"; use it whenever a radical needs to be computed geometrically.** The single most reusable idea here is the rewrite $\sqrt I = I(V(I))$: the radical of an ideal *is* the set of functions vanishing on its variety. This turns an algebraic question (membership in $\sqrt I$) into a geometric one (vanishing on a point set), and conversely lets geometric facts about the variety be read as algebraic facts about the radical. The trigger is "I need to understand $\sqrt I$" in a finitely generated $k$-algebra; the reaction is "look at $V(I)$ and ask what vanishes on it". This is how radical-membership algorithms work, and it is why the radical — not the ideal — is the geometrically meaningful object.

**Maximal ideals see the radical exactly when there are enough of them — the Jacobson property.** In a general ring, primes detect the radical but maximals may miss it (local rings are the extreme: one maximal ideal, blind to most of the nilradical structure). Finitely generated $k$-algebras are special because the weak Nullstellensatz manufactures a maximal ideal at *every point* of every variety, so the maximal ideals are dense enough to recover $\sqrt I$. The diagnostic to carry: before writing "$\sqrt I = \bigcap_{\text{maximal}} \mathfrak m$", check you are in a Jacobson ring; otherwise only "$\sqrt I = \bigcap_{\text{prime}}\mathfrak p$" is safe. This distinction — primes always, maximals only when Jacobson — separates the geometry of varieties (Jacobson) from the geometry of general schemes and local rings (not Jacobson).

**Reduction to the polynomial ring via $A = k[T]/J$ is the universal first move for finitely generated algebras.** Almost every statement about a finitely generated $k$-algebra is proved by presenting it as a quotient of a polynomial ring and using the ideal correspondence to transport the statement to ideals containing $J$. Radicals pull back to radicals, maximal ideals to maximal ideals, varieties to subvarieties of $\mathbb{A}^n$. The trigger is "$A$ is a finitely generated $k$-algebra and I have a Nullstellensatz-type tool stated for polynomial rings"; the reaction is "present $A = k[T]/J$, lift to $k[T]$, apply the tool, push back down". This is the same reflex used in [[Ex - The ideal-variety correspondence and unions and intersections]] and throughout the chapter, and it is what makes the Nullstellensatz — stated for $k[T_1, \dots, T_n]$ — apply to every affine variety.
