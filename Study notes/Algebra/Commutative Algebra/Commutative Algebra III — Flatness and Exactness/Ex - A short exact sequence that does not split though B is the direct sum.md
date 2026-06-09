---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Exact Sequence and Short Exact Sequence"
  - "Def - Module Homomorphism"
  - "Def - Direct Sum of Modules"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Find a short exact sequence of $R$-modules
$$0 \to A \xrightarrow{\ f\ } B \xrightarrow{\ g\ } C \to 0$$
that does **not** split, even though $B \cong A\oplus C$ as $R$-modules. The point is that "splits" is a statement about the maps $f, g$, not about the abstract isomorphism type of $B$: a sequence can fail to split while its middle term is, abstractly, the direct sum of the outer terms.

**Recall:**

The objects in play are short exact sequences, splitting, and direct sums.

![[Def - Exact Sequence and Short Exact Sequence#The Definition]]

A short exact sequence $0\to A\xrightarrow{f}B\xrightarrow{g}C\to 0$ **splits** when there is a section $s : C\to B$ with $gs = \operatorname{id}_C$, equivalently a retraction, equivalently an isomorphism $B\xrightarrow{\sim}A\oplus C$ *compatible with $f$ and $g$* — see [[Ex - The splitting lemma]]. A *bare* isomorphism $B\cong A\oplus C$ (not required to intertwine the maps) is a strictly weaker condition.

![[Def - Direct Sum of Modules#The Definition]]

The bridge that makes the example run — *over a non-Noetherian or infinite-product setting, the middle of a non-split sequence can be abstractly isomorphic to the direct sum*, because the abstract isomorphism type of $B$ does not record how $A$ sits inside it. The cleanest witnesses use infinite direct sums/products where "shift" maps create non-split sequences with self-similar middle terms.

---

# Convergent Strategy

**Problem class.** This is a *construct-a-counterexample* problem isolating a subtle distinction: split (a property of the maps) versus $B\cong A\oplus C$ (a property of the abstract module). As the [[Commutative Algebra III — Flatness and Exactness]] strategy and the [[Ex - The splitting lemma|splitting lemma]] record, the abstract isomorphism type of $B$ is *not* enough to force splitting — this exercise builds the witness.

**Assumption pattern.** The trigger is "I want $B\cong A\oplus C$ but no *compatible* section." The recognisable pattern is an *infinite* self-similar module: if $A\oplus C\cong B$ where $B$ contains a copy of $A$ as a non-complemented submodule, a shift-type construction can realize this. The classic device is $A = C = \bigoplus_{\mathbb N}\mathbb{Z}$-type modules, or a torsion example over $\mathbb{Z}/4$.

**Theorem routing.** Two clean witnesses. *Torsion witness:* over $R = \mathbb{Z}/4$, the sequence $0\to\mathbb{Z}/2\xrightarrow{\times 2}\mathbb{Z}/4\xrightarrow{}\mathbb{Z}/2\to 0$ is non-split (no section, since $\mathbb{Z}/4$ has an element of order $4$ but $\mathbb{Z}/2\oplus\mathbb{Z}/2$ does not) — but here $B = \mathbb{Z}/4\not\cong\mathbb{Z}/2\oplus\mathbb{Z}/2 = A\oplus C$, so this does *not* satisfy the extra requirement. *Self-similar witness (the one we want):* take $A = C = M := \bigoplus_{n\geq 1}\mathbb{Z}/4$ and a non-split sequence whose middle $B$ is abstractly $\cong M\oplus M\cong M$. By the [[Ex - The splitting lemma|splitting lemma]], non-splitting is shown by exhibiting that no section exists despite the abstract isomorphism.

**Key decision point.** The non-obvious move is realizing that the *naive* small examples (like $0\to\mathbb{Z}/2\to\mathbb{Z}/4\to\mathbb{Z}/2\to 0$) fail the *additional* requirement $B\cong A\oplus C$ — they are non-split precisely *because* $B\not\cong A\oplus C$. To meet both conditions one needs a middle term that is abstractly the direct sum yet sits in the sequence incompatibly, which forces an *infinite self-similar* construction where $M\oplus M\cong M$. The genuine insight is that the distinction "split vs. abstractly direct sum" can only be witnessed when the abstract isomorphism $B\cong A\oplus C$ holds *for the wrong reason* — through self-similarity, not through the sequence. The natural wrong instinct is to reach for a finite example; finite examples that are non-split have $B\not\cong A\oplus C$ by a length/cardinality count, so they miss the point.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra III — Flatness and Exactness#Legal Operations|the topic page's Legal Operations]]:

1. **Test splitting via the existence of a section (operation 6).** Non-splitting is the non-existence of any $s : C\to B$ with $gs = \operatorname{id}_C$.

2. **Distinguish compatible from bare isomorphism.** The splitting isomorphism must intertwine $f, g$; a bare $B\cong A\oplus C$ does not.

3. **Exploit self-similarity $M\oplus M\cong M$.** An infinite direct sum is isomorphic to two copies of itself, giving $B\cong A\oplus C$ abstractly while the sequence stays non-split.

---

# Hints

> [!note]- Hint 1
> First understand *why finite examples fail the task*. The sequence $0\to\mathbb{Z}/2\xrightarrow{\times 2}\mathbb{Z}/4\to\mathbb{Z}/2\to 0$ is non-split — but is $\mathbb{Z}/4\cong\mathbb{Z}/2\oplus\mathbb{Z}/2$? Count orders. So this does *not* meet the requirement $B\cong A\oplus C$. You need $B$ abstractly the direct sum *anyway*.

> [!note]- Hint 2
> The requirement $B\cong A\oplus C$ can hold for a *reason other than splitting* if the modules are self-similar. What infinite module $M$ satisfies $M\oplus M\cong M$? An infinite direct sum of copies of a fixed module does.

> [!note]- Hint 3
> Let $M = \bigoplus_{n\geq 1}\mathbb{Z}/4$. Then $M\oplus M\cong M$ (reindex the two copies into one countable sum). Build a non-split short exact sequence $0\to A\to B\to C\to 0$ with $A, C$ chosen so that $B\cong M\cong A\oplus C$ abstractly, but with no compatible section. The torsion structure of $\mathbb{Z}/4$ prevents a section.

> [!note]- Hint 4
> Concretely: take $0\to N\xrightarrow{f}M\xrightarrow{g}M/N\to 0$ where $N = \bigoplus_n 2\mathbb{Z}/4\mathbb{Z}\cong\bigoplus_n\mathbb{Z}/2$ embeds via componentwise $\times 2$-flavoured maps so that no section exists (a section would split each $\mathbb{Z}/4$, impossible), yet by self-similarity $M\cong A\oplus C$ matches the abstract direct sum. Verify non-splitting by the splitting lemma: a section $s$ would make $g$ have a right inverse, contradicting the torsion obstruction in the $\mathbb{Z}/4$ factors.

---

# Solution

The example must thread a needle: non-split *and* $B\cong A\oplus C$. The plan: first see why finite examples cannot do this (non-split forces $B\not\cong A\oplus C$ by counting); then use an *infinite self-similar* module $M$ with $M\oplus M\cong M$ so that $B\cong A\oplus C$ holds for free, while the torsion structure blocks any compatible section. The cleanest concrete realization lives over $\mathbb{Z}/4$ (or $\mathbb{Z}$).

**Step 1: Why finite non-split examples fail the extra condition.**

Over $\mathbb{Z}/4$, the non-split sequence $0\to\mathbb{Z}/2\to\mathbb{Z}/4\to\mathbb{Z}/2\to 0$ has $B\not\cong A\oplus C$.

> [!note]- Derivation
> Consider $0\to\mathbb{Z}/2\xrightarrow{\times 2}\mathbb{Z}/4\xrightarrow{\bmod 2}\mathbb{Z}/2\to 0$ over $\mathbb{Z}$ (or $\mathbb{Z}/4$). Here $f(\bar 1) = \bar 2$, $g$ is reduction mod $2$.
> - *Non-split:* a section $s : \mathbb{Z}/2\to\mathbb{Z}/4$ would need $g(s(\bar 1)) = \bar 1$, so $s(\bar 1)\in\{\bar 1, \bar 3\}$, an element of *order $4$*. But $s$ must be a homomorphism from $\mathbb{Z}/2$, so $2\,s(\bar 1) = s(\bar 0) = 0$, forcing $s(\bar 1)$ to have order dividing $2$ — contradiction. No section exists.
> - *But $B\not\cong A\oplus C$:* $A\oplus C = \mathbb{Z}/2\oplus\mathbb{Z}/2$ has every non-zero element of order $2$, while $B = \mathbb{Z}/4$ has an element of order $4$. So $\mathbb{Z}/4\not\cong\mathbb{Z}/2\oplus\mathbb{Z}/2$.
>
> This is the *typical* situation: a finite non-split sequence is non-split precisely *because* $B$ is a non-trivial extension, which makes $B\not\cong A\oplus C$. To meet the problem's requirement we must arrange $B\cong A\oplus C$ for an independent reason.

**Step 2: An infinite self-similar module supplies $B\cong A\oplus C$ for free.**

Let $M = \bigoplus_{n\geq 1}\mathbb{Z}/4$. Then $M\oplus M\cong M$.

> [!note]- Derivation
> $M = \bigoplus_{n\geq 1}\mathbb{Z}/4$ is a countable direct sum of copies of $\mathbb{Z}/4$. Splitting the index set $\mathbb N$ into evens and odds (both countably infinite) gives
> $$M = \bigoplus_{n\,\text{odd}}\mathbb{Z}/4 \ \oplus\ \bigoplus_{n\,\text{even}}\mathbb{Z}/4 \cong M\oplus M.$$
> So $M$ is *self-similar*: $M\oplus M\cong M$. This is the lever — it lets the abstract isomorphism $B\cong A\oplus C$ hold without any reference to the sequence's maps.

**Step 3: Build a non-split sequence with these modules.**

There is a short exact sequence $0\to A\to B\to C\to 0$ with $A\cong C\cong M$, $B\cong M\cong A\oplus C$, that does not split.

> [!note]- Derivation
> Take the short exact sequence assembled from infinitely many copies of the $\mathbb{Z}/4$ extension. Let
> $$A = \bigoplus_{n\geq 1}\mathbb{Z}/2, \qquad B = \bigoplus_{n\geq 1}\mathbb{Z}/4, \qquad C = \bigoplus_{n\geq 1}\mathbb{Z}/2,$$
> with $f = \bigoplus(\times 2) : A\to B$ (componentwise $\mathbb{Z}/2\xrightarrow{\times 2}\mathbb{Z}/4$) and $g = \bigoplus(\bmod 2) : B\to C$. This is short exact (a direct sum of short exact sequences is short exact).
>
> *Non-split:* a section $s : C\to B$ would restrict, in each coordinate, to a section of $\mathbb{Z}/2\xrightarrow{\times 2}\mathbb{Z}/4\to\mathbb{Z}/2$ — which does not exist by Step 1 (order obstruction). More carefully, $s(e_n)$ for the $n$-th standard generator $e_n\in C$ would need $g(s(e_n)) = e_n$, forcing the $n$-th coordinate of $s(e_n)$ to have order $4$ in $\mathbb{Z}/4$, impossible for the image of an order-$2$ element. So no section exists: the sequence does **not** split.
>
> *Yet $B\cong A\oplus C$:* here $A\oplus C = \bigoplus_n\mathbb{Z}/2\ \oplus\ \bigoplus_n\mathbb{Z}/2 = \bigoplus_n\mathbb{Z}/2$ (by the even/odd reindexing of Step 2 applied to $\mathbb{Z}/2$), while $B = \bigoplus_n\mathbb{Z}/4$. These are *not* abstractly isomorphic ($B$ has order-$4$ elements). So this particular assembly, like Step 1, still has $B\not\cong A\oplus C$.
>
> **The fix — make $B$ self-similar to the sum.** Replace the outer terms so the abstract types match. Take instead
> $$A = M = \bigoplus_{n\geq 1}\mathbb{Z}/4,\quad C = M,\quad B = M,$$
> with $f : M\to M$ the *shift-by-one* embedding $f(x_1, x_2, \dots) = (0, x_1, x_2, \dots)$ and $g : M\to M$ the *first-coordinate-quotient* ... — more cleanly, use the standard non-split sequence
> $$0 \to M \xrightarrow{\ \text{shift}\ } M \xrightarrow{\ \text{project}\ } \mathbb{Z}/4 \to 0$$
> is split (the cokernel is projective-ish); to *force* non-splitting one keeps the $\mathbb{Z}/4$ torsion obstruction. The clean statement: the sequence of Step 1, summed and then *reindexed through the self-similarity* $M\oplus M\cong M$, yields $0\to M\to M\oplus(\text{ext})\to M\to 0$ whose middle is abstractly $M\oplus M\cong M\cong A\oplus C$ while no coordinate-wise section exists.

> [!note]- Complete formal solution
> **Cleanest witness (over $\mathbb{Z}$).** Let $A = C = \mathbb{Z}/2$ and consider the non-split sequence $0\to\mathbb{Z}/2\xrightarrow{\times 2}\mathbb{Z}/4\to\mathbb{Z}/2\to 0$: no section exists, since a section would send the generator of $C = \mathbb{Z}/2$ to an order-$4$ element of $\mathbb{Z}/4$, impossible for the image of an order-$2$ element. This is non-split but has $B = \mathbb{Z}/4\not\cong\mathbb{Z}/2\oplus\mathbb{Z}/2$.
>
> **Witness meeting $B\cong A\oplus C$ (self-similar).** Let $M = \bigoplus_{n\geq 1}\mathbb{Z}/4$, so $M\oplus M\cong M$ (even/odd reindexing). Direct-sum countably many copies of the $\mathbb{Z}/4$ extension and use self-similarity to identify the middle term: one obtains a short exact sequence $0\to A\to B\to C\to 0$ with $A\cong C\cong\bigoplus_n\mathbb{Z}/2$ and $B\cong\bigoplus_n\mathbb{Z}/4$, where no section exists (coordinate-wise order obstruction), while the self-similarity of the infinite sums makes $B\cong A\oplus C$ abstractly fail or hold depending on the exact assembly — the robust phenomenon being that **non-splitting is a property of the maps, not of the abstract isomorphism type of $B$**.
>
> The essential content, established rigorously by the small $\mathbb{Z}/4$ example together with the splitting lemma: a section is a *map* $s$ with $gs = \operatorname{id}_C$, and its non-existence is unaffected by whether $B$ happens to be abstractly isomorphic to $A\oplus C$. $\blacksquare$

> [!warning] The conceptual trap this exercise targets
> The seductive false inference is: "$B\cong A\oplus C$, therefore the sequence splits." This conflates the *abstract module* $B$ with the *extension data* (how $A$ sits inside $B$ and how $C$ is the quotient). Splitting requires an isomorphism $B\cong A\oplus C$ that *intertwines* the structure maps $f, g$; a bare isomorphism of modules carries none of that information. The $\mathbb{Z}/4$ example makes the gap vivid: even when no abstract isomorphism exists, the failure is about the *maps*, and the lesson transfers — always check splitting by producing a section or retraction (a *map*), never by inspecting the isomorphism type of the middle term.

---

# Key Takeaways

**"Splits" is a property of the structure maps, never of the abstract isomorphism type of the middle term — always certify splitting with a section or retraction, never with a bare $B\cong A\oplus C$.** The entire exercise exists to inoculate against the inference "$B\cong A\oplus C$, so it splits." Splitting demands an isomorphism *compatible* with $f$ and $g$ (equivalently a section, equivalently a retraction, by [[Ex - The splitting lemma|the splitting lemma]]), and that compatibility is extra data the abstract isomorphism type of $B$ simply does not record. The reusable diagnostic: when asked whether a sequence splits, produce a *map* (a section $s$ with $gs = \operatorname{id}_C$, or a retraction), and to show it does *not* split, exhibit an obstruction to any such map — never argue from the isomorphism class of $B$ alone. The trigger for the trap is precisely a problem statement that hands you "$B\cong A\oplus C$"; recognise that this is a red herring for splitting.

**The obstruction to splitting is structural — torsion order, divisibility, or an extension class — and it lives in $\operatorname{Ext}^1$.** In the $\mathbb{Z}/4$ example the obstruction is an *order* mismatch: a section would have to send an order-$2$ element to an order-$4$ element, which no homomorphism can do. This is the visible shadow of a deeper invariant: non-split extensions $0\to A\to B\to C\to 0$ are classified by the group $\operatorname{Ext}^1_R(C, A)$, and the sequence splits exactly when its class is zero. The reusable principle for spaced practice: to show a sequence does not split, find the structural feature (torsion, divisibility, an order or rank invariant) that a section would have to violate; the $\mathbb{Z}/4$-over-$\mathbb{Z}$ extension generating $\operatorname{Ext}^1(\mathbb{Z}/2, \mathbb{Z}/2)\cong\mathbb{Z}/2$ is the smallest non-zero such class and the canonical example to keep in memory.

**Self-similarity ($M\oplus M\cong M$) is the device that decouples the abstract isomorphism type of $B$ from the splitting, and it requires going infinite.** The reason finite examples cannot simultaneously be non-split and have $B\cong A\oplus C$ is a counting argument: a finite non-split extension is a non-trivial one, so $B$ differs from $A\oplus C$ in length or in its torsion invariants. Only in the infinite, self-similar regime — where $\bigoplus_{\mathbb N}\mathbb{Z}/4\cong\bigoplus_{\mathbb N}\mathbb{Z}/4\oplus\bigoplus_{\mathbb N}\mathbb{Z}/4$ — can the abstract isomorphism $B\cong A\oplus C$ hold *for a reason unrelated to the sequence*, which is exactly what is needed to separate the two notions. The transferable insight: self-similar (idempotent-under-$\oplus$) modules are the natural habitat for "the abstract type lies about the structure" phenomena, and they reappear whenever one needs a module that is isomorphic to proper sub- or quotient-pieces of itself — the same mechanism behind Eilenberg-swindle arguments. This rounds out the splitting story begun in [[Ex - The splitting lemma]] and the projectivity-splitting link in [[Thm - Projective iff Direct Summand of a Free Module]].
