---
type: exercise
subject: group-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Group"
  - "Def - Order of a Group and of an Element"
  - "Def - Abelian Group"
  - "Thm - Lagrange's Theorem"
tags: [algebra, group-theory]
---

# Problem Statement

Let $G$ be a finite [[Def - Group|group]], and suppose $G$ has **exactly one** element $x$ of order $2$. Show that $x$ commutes with every element of $G$ — that is, $gx = xg$ for all $g \in G$.

**Recall:**

In a [[Def - Group|group]] $G$ with identity $e$, the **order** of an element $y$ is the least positive integer $n$ with $y^n = e$. An element $y$ has **order $2$** precisely when $y \neq e$ and $y^2 = e$ — equivalently, $y$ is its own inverse but is not the identity. See [[Def - Order of a Group and of an Element]].

For any $g \in G$, **conjugation by $g$** sends an element $y$ to $gyg^{-1}$. The reader should keep one fact about conjugation at hand: it preserves the order of an element. Concretely, $(gyg^{-1})^n = g y^n g^{-1}$, because the inner factors telescope —
$$(gyg^{-1})(gyg^{-1}) = gy(g^{-1}g)yg^{-1} = gy^2g^{-1},$$
and inductively $(gyg^{-1})^n = gy^ng^{-1}$. Hence $gyg^{-1}$ and $y$ raise to the identity at exactly the same powers, so they have the same order.

An element $x$ **commutes** with $g$ when $gx = xg$, equivalently when $gxg^{-1} = x$ (conjugating $x$ by $g$ leaves it fixed). An element commuting with *every* element of $G$ is called central.

---

# Convergent Strategy

**Problem class.** This is a *structural problem* of the "uniqueness forces rigidity" type: a counting hypothesis (there is exactly one element of a certain order) is leveraged into a structural conclusion (that element is central). The mechanism is a recurring one — when an object is the *unique* thing with some property, any operation that preserves that property must fix the object.

**Assumption pattern.** Two features of the hypothesis do the work. First, *order $2$* is a property invariant under conjugation: conjugating an element never changes its order, as recalled above. Second, *uniqueness*: there is only one element of order $2$. The combination is the whole engine — conjugation moves $x$ to another element of order $2$, and uniqueness says there is nowhere else for it to go.

**Theorem routing.** This problem does not route through a named theorem so much as through the *conjugation-preserves-order* fact: for any $g$, the element $gxg^{-1}$ has the same order as $x$, namely $2$; by uniqueness $gxg^{-1} = x$; rearranging gives $gx = xg$. [[Thm - Lagrange's Theorem|Lagrange's theorem]] does not enter the main argument, but it underlies the optional remark below — that a group of even order *has* an element of order $2$ to begin with — and it is what makes the hypothesis non-vacuous.

**Key decision point.** The non-obvious move is to conjugate $x$ by an *arbitrary* $g$ and recognize $gxg^{-1}$ as again an element of order $2$. Beginners try to compute with $x$ directly, or attempt to show $G$ is abelian (it need not be). The insight is to stop treating $x$ as a fixed element and instead watch what conjugation does to it: the orbit of $x$ under conjugation consists entirely of order-$2$ elements, and there is only one of those.

---

# Legal Operations Used

1. **Conjugate to test or exploit a property** — for an arbitrary $g \in G$, form $gxg^{-1}$. Conjugation is the operation that "views $x$ from the standpoint of $g$"; here it is used to generate another candidate element of order $2$.

2. **Use an order-preserving invariant to constrain the result** — conjugation preserves order, so $gxg^{-1}$ has order $2$. This is the step that pins $gxg^{-1}$ down to the set of order-$2$ elements.

3. **Invoke uniqueness to collapse the candidates** — there is exactly one element of order $2$, so $gxg^{-1} = x$. Rearranging this equation yields commutativity.

---

# Hints

> [!note]- Hint 1
> Do not try to compute with $x$ alone. Instead, take an arbitrary $g \in G$ and apply some structure-preserving operation to $x$. Which operation, built from $g$, produces another element you can say something about?

> [!note]- Hint 2
> Consider the conjugate $gxg^{-1}$. What is its order? Use the fact that conjugation preserves the order of an element.

> [!note]- Hint 3
> The conjugate $gxg^{-1}$ has order $2$. But $G$ has only *one* element of order $2$. So $gxg^{-1} = x$. Now multiply both sides on the right by $g$.

---

# Solution

**Step 1: For any $g$, the conjugate $gxg^{-1}$ has order $2$.**

Conjugation preserves order, and $x$ has order $2$, so $gxg^{-1}$ also has order $2$.

> [!note]- Derivation
> Fix an arbitrary $g \in G$ and set $y = gxg^{-1}$. As recalled in the problem statement, $(gxg^{-1})^n = g x^n g^{-1}$ for every $n \geq 1$, because consecutive factors $g^{-1}g$ cancel.
>
> Therefore $y^2 = (gxg^{-1})^2 = g x^2 g^{-1} = g e g^{-1} = e$, using $x^2 = e$. And $y \neq e$: if $gxg^{-1} = e$ then $x = g^{-1}eg = e$, contradicting that $x$ has order $2$. An element that is not the identity and squares to the identity has order exactly $2$. Hence $\operatorname{ord}(gxg^{-1}) = 2$.

**Step 2: By uniqueness, $gxg^{-1} = x$.**

Since $gxg^{-1}$ has order $2$ and $x$ is the *only* element of order $2$ in $G$, the two must be equal.

> [!note]- Derivation
> The hypothesis is that $G$ contains exactly one element of order $2$, and that element is $x$. Step 1 produced an element $gxg^{-1}$ of order $2$. "Exactly one" means every element of order $2$ equals $x$, so in particular $gxg^{-1} = x$.

**Step 3: Rearrange to get $gx = xg$.**

From $gxg^{-1} = x$, right-multiplying by $g$ gives $gx = xg$. As $g$ was arbitrary, $x$ commutes with every element of $G$.

> [!note]- Derivation
> Take the equation $gxg^{-1} = x$ from Step 2 and multiply both sides on the right by $g$:
> $$gxg^{-1}g = xg \quad\Longrightarrow\quad gxe = xg \quad\Longrightarrow\quad gx = xg.$$
> Since $g$ was an arbitrary element of $G$, this holds for all $g \in G$. That is precisely the statement that $x$ commutes with every element of $G$ (equivalently, $x$ is central). $\qquad\blacksquare$

> [!note]- Complete formal solution
> Let $g \in G$ be arbitrary, and put $y = gxg^{-1}$.
>
> By telescoping, $(gxg^{-1})^n = g x^n g^{-1}$ for all $n \ge 1$. Hence $y^2 = g x^2 g^{-1} = g e g^{-1} = e$, and $y \ne e$ (since $y = e$ would force $x = e$). An element that squares to $e$ but is not $e$ has order exactly $2$, so $y$ has order $2$.
>
> By hypothesis $x$ is the unique element of order $2$ in $G$, so $y = x$, i.e. $gxg^{-1} = x$.
>
> Right-multiplying by $g$ yields $gx = xg$. As $g$ was arbitrary, $x$ commutes with every element of $G$. $\qquad\blacksquare$

> [!example] Optional remark: a group of even order always has an element of order $2$
> The hypothesis "$G$ has an element of order $2$" is not vacuous when $|G|$ is even. Pair off the elements of $G$: put $y$ together with $y^{-1}$. An element is paired *with itself* exactly when $y = y^{-1}$, i.e. $y^2 = e$ — that is, $y$ is either the identity or has order $2$. The elements with $y \ne y^{-1}$ split into genuine pairs of size $2$, contributing an even count. So the number of self-paired elements has the same parity as $|G|$. When $|G|$ is even, the count of self-paired elements is even; it is at least $1$ (the identity is self-paired); hence it is at least $2$, and the extra self-paired element is a non-identity element with $y^2 = e$ — an element of order $2$. This is a "pairing" or "involution-counting" argument, and it is the seed of more powerful results such as Cauchy's theorem.

---

# Key Takeaways

**Uniqueness plus an invariance-preserving operation forces a fixed point.** The shape of this argument is worth extracting in full generality, because it recurs constantly. You have an object $x$ that is the *unique* element with some property $P$. You have an operation — here conjugation by $g$ — that *preserves* property $P$: it sends things-with-$P$ to things-with-$P$. Then the operation must send $x$ to something with property $P$, and since $x$ is the only such thing, the operation fixes $x$. The conclusion "$gxg^{-1} = x$ for all $g$" *is* the statement that $x$ is central. Watch for this pattern whenever a problem says "the unique element such that...": the next question to ask is "what operations preserve that defining property?", because each such operation must leave the unique element alone. The same reasoning shows a unique [[Def - Subgroup|subgroup]] of a given order is normal (conjugation preserves [[Def - Subgroup|subgroup]] order), and a unique Sylow $p$-subgroup is normal — these are the workhorse normality arguments of [[Group Theory III — §1.5–1.7]].

**Conjugation is the canonical order-preserving operation; reach for it when "order" is in the hypothesis.** The single fact that makes this problem dissolve is that $gxg^{-1}$ has the same order as $x$. Conjugation never changes an element's order, because $(gxg^{-1})^n = g x^n g^{-1}$, so the two elements hit the identity at exactly the same exponents. Whenever a problem's hypothesis is phrased in terms of *how many elements of order $d$ there are*, conjugation is the natural operation to apply, since it permutes the set of order-$d$ elements among themselves. More broadly, conjugate elements share every "intrinsic" property — order, being a power of a given element, generating an isomorphic subgroup — so conjugation is the move that exploits or tests any conjugation-invariant property. The illegal-operations warning on the parent page about treating normality as transitive is the flip side of this same idea: conjugation behaves well, but only relative to one fixed overgroup.

**Do not over-reach for "abelian" — the conclusion is centrality of one element, not of the whole group.** A natural false start is to try to prove $G$ is abelian; it need not be. The dihedral group $D_8$ of order $8$ has exactly one element of order $2$ in its centre (the half-turn), yet $D_8$ is non-abelian. What the hypothesis buys is centrality of the *single* element $x$, and the solution is careful to conclude only that. The general discipline: when a hypothesis concerns one distinguished element, the conclusion you can hope for is a statement about that element (it is central, it is fixed, it is normal-as-a-subgroup), not a global statement about $G$. Matching the strength of the conclusion to the strength of the hypothesis is what keeps the argument honest and is often the difference between a proof that works and one that stalls trying to prove too much.
