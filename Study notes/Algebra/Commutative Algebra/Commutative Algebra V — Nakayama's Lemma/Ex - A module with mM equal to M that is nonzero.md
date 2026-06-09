---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Finitely Generated Module"
  - "Def - Local Ring and Residue Field"
  - "Thm - Nakayama's Lemma"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $p$ be a prime number and consider the [[Def - Local Ring and Residue Field|local ring]]
$$\mathbb Z_{(p)} = \left\{ \tfrac{a}{b} : a, b \in \mathbb Z,\ p \nmid b \right\} \subseteq \mathbb Q,$$
with maximal ideal $\mathfrak m = (p)\mathbb Z_{(p)}$. Find a $\mathbb Z_{(p)}$-module $M$ with
$$(p)\mathbb Z_{(p)} \cdot M = M \qquad\text{but}\qquad M \neq 0.$$
Explain why this does **not** contradict [[Thm - Nakayama's Lemma|Nakayama's lemma]].

(This is Becker Example Sheet 3, Q1(c).)

**Recall:**

The objects in play are the local ring $\mathbb Z_{(p)}$, its maximal ideal, a nonzero module on which the maximal ideal acts surjectively, and the finite-generation hypothesis of Nakayama.

The ring $\mathbb Z_{(p)} = (\mathbb Z \setminus (p))^{-1}\mathbb Z$ is the [[Def - Local Ring and Residue Field|localization]] of $\mathbb Z$ at the prime $(p)$: a local ring with unique maximal ideal $\mathfrak m = (p)\mathbb Z_{(p)} = \{\tfrac ab : p \mid a,\ p \nmid b\}$ and residue field $\mathbb Z_{(p)}/\mathfrak m \cong \mathbb F_p$. Its units are the fractions $\tfrac ab$ with $p \nmid a$ and $p \nmid b$.

The statement under test — Nakayama's lemma — requires **finite generation**:

![[Thm - Nakayama's Lemma#Statement]]

A module is [[Def - Finitely Generated Module|finitely generated]] if it has a finite generating set; the counterexample will be a module that is *not* finitely generated.

---

# Convergent Strategy

**Problem class.** This is a *construct-a-counterexample* problem: produce a witness showing that a hypothesis of a theorem cannot be dropped. The [[Commutative Algebra V — Nakayama's Lemma#Problem-Solving Strategy|topic strategy]] flags the instinct: when a module is not finitely generated, *look for a counterexample, not a proof* — the determinant trick has no finite matrix to build.

**Assumption pattern.** Nakayama has two hypotheses — finite generation and $\mathfrak a \subseteq J(R)$. Here $\mathfrak a = \mathfrak m = J(\mathbb Z_{(p)})$, so the *Jacobson* hypothesis holds; the only hypothesis available to violate is *finite generation*. The trigger is therefore "build a non-finitely-generated module on which $p$ acts surjectively (invertibly)".

**Theorem routing.** The cleanest witness is $M = \mathbb Q$, viewed as a $\mathbb Z_{(p)}$-module. Multiplication by $p$ on $\mathbb Q$ is a bijection (every rational is $p$ times a rational), so $pM = M$, i.e. $\mathfrak m M = M$; and $\mathbb Q \neq 0$. The non-contradiction is then immediate: $\mathbb Q$ is *not finitely generated* over $\mathbb Z_{(p)}$ (denominators are unbounded), so Nakayama does not apply.

**Key decision point.** The non-obvious move is realising that the *only* escape route is infinite generation, and then choosing a module where multiplication by $p$ is actually a *bijection* — making $pM = M$ obvious. $\mathbb Q$ is the canonical choice: inverting $p$ is built into it. The alternative witness $\mathbb Z[\tfrac1p]/\mathbb Z$ (the Prüfer $p$-group) works equally — there $p$ is surjective because every element is a $p$-power-torsion fraction — but $\mathbb Q$ is conceptually cleaner because $p$ is genuinely invertible, not merely surjective. The point to nail is *why* infinite generation lets $pM = M$ persist: there is no finite generating set to which the determinant trick could attach a characteristic polynomial.

---

# Legal Operations Used

This solution uses the topic page's [[Commutative Algebra V — Nakayama's Lemma#Legal Operations|Legal Operations]] mostly in the negative — by exhibiting where they fail:

1. **Recognise the failure of operation 3 (specialise Cayley–Hamilton).** The determinant trick requires a *finite* generating set to form the matrix $P$; with $M = \mathbb Q$ infinitely generated, no such matrix exists, so the trick — and hence Nakayama — cannot run.

2. **Check the Jacobson hypothesis is satisfied** (operation 4 in reverse). $\mathfrak m = J(\mathbb Z_{(p)})$, so $1 - a$ would be a unit for $a \in \mathfrak m$; this confirms the *only* failing hypothesis is finite generation, isolating it cleanly.

3. **Verify surjectivity of multiplication by $p$.** On $\mathbb Q$, $x \mapsto px$ is a bijection, giving $pM = M$ directly.

---

# Hints

> [!note]- Hint 1
> Nakayama has two hypotheses: finite generation, and $\mathfrak a \subseteq J(R)$. Here $\mathfrak a = \mathfrak m$, and for a local ring $\mathfrak m = J(R)$ — so the Jacobson hypothesis holds. Which hypothesis is left for your counterexample to violate?

> [!note]- Hint 2
> You need a nonzero $\mathbb Z_{(p)}$-module $M$ that is *not* finitely generated, on which multiplication by $p$ is surjective. Where have you seen $p$ become invertible? A module where you can already divide by $p$.

> [!note]- Hint 3
> Take $M = \mathbb Q$. Multiplication by $p$ is a bijection $\mathbb Q \to \mathbb Q$ (inverse: multiply by $\tfrac1p$), so $p\mathbb Q = \mathbb Q$, i.e. $\mathfrak m M = M$, and $\mathbb Q \neq 0$. Why is $\mathbb Q$ not finitely generated over $\mathbb Z_{(p)}$? Bound the denominators of any finite list.

---

# Solution

The counterexample is $M = \mathbb Q$. We verify $\mathfrak m M = M$, that $M \neq 0$, and that $M$ is not finitely generated — the last being exactly the hypothesis of Nakayama that fails.

**Step 1: $\mathbb Q$ is a $\mathbb Z_{(p)}$-module with $\mathfrak m \mathbb Q = \mathbb Q$.**

Multiplication by $p$ is a bijection of $\mathbb Q$, so $(p)\mathbb Z_{(p)} \cdot \mathbb Q = \mathbb Q$.

> [!note]- Derivation
> $\mathbb Q$ is a $\mathbb Z_{(p)}$-module ($\mathbb Z_{(p)} \subseteq \mathbb Q$ acts by multiplication). The maximal ideal $\mathfrak m = (p)\mathbb Z_{(p)}$ acts, and
> $$\mathfrak m \mathbb Q = (p)\mathbb Z_{(p)} \cdot \mathbb Q \supseteq p \cdot \mathbb Q.$$
> Multiplication by $p$ is a bijection $\mathbb Q \to \mathbb Q$: for any $q \in \mathbb Q$, $q = p \cdot (\tfrac1p q)$ with $\tfrac1p q \in \mathbb Q$. Hence $p\mathbb Q = \mathbb Q$, and therefore
> $$\mathfrak m \mathbb Q = \mathbb Q.$$
> (Indeed $p$ is a unit in $\mathbb Q$, so multiplying the module by $(p)$ recovers all of it.)

**Step 2: $\mathbb Q \neq 0$.**

Trivially, $\mathbb Q$ contains $1 \neq 0$.

> [!note]- Derivation
> $1 \in \mathbb Q$ and $1 \neq 0$, so $M = \mathbb Q \neq 0$. Thus we have a nonzero module with $\mathfrak m M = M$ — precisely the configuration Nakayama would forbid for a *finitely generated* module.

**Step 3: $\mathbb Q$ is not finitely generated over $\mathbb Z_{(p)}$, so Nakayama does not apply.**

Any finite list of rationals generates a $\mathbb Z_{(p)}$-submodule with bounded denominators, missing most of $\mathbb Q$.

> [!note]- Derivation
> Suppose, for contradiction, $\mathbb Q = \mathbb Z_{(p)} q_1 + \dots + \mathbb Z_{(p)} q_r$ for finitely many $q_i = \tfrac{a_i}{b_i} \in \mathbb Q$. Let $D = b_1 \cdots b_r$ (a common denominator of the $q_i$). Every element of $\mathbb Z_{(p)} q_1 + \dots + \mathbb Z_{(p)} q_r$ is a $\mathbb Z_{(p)}$-combination $\sum_i \tfrac{c_i}{d_i} q_i$ with $p \nmid d_i$; writing over a common denominator, every such element has the form $\tfrac{n}{D \cdot d}$ with $p \nmid d$ — that is, its denominator divides $D$ times a $p$-free integer. So in lowest terms, the denominator of any element is a divisor of $D$ multiplied by a power... more precisely, the prime $\ell$-adic valuation is bounded below by $-v_\ell(D)$ for every prime $\ell \neq p$. But $\mathbb Q$ contains rationals with arbitrarily large denominators at primes $\ell \neq p$ (e.g. $\tfrac{1}{\ell^k}$ for a prime $\ell \neq p$ and large $k$, which is not even in $\mathbb Z_{(p)}$ but is in $\mathbb Q$), contradicting the bound. Hence no finite generating set exists: $\mathbb Q$ is **not finitely generated** as a $\mathbb Z_{(p)}$-module.
>
> Therefore the hypothesis of [[Thm - Nakayama's Lemma|Nakayama's lemma]] — that $M$ be finitely generated — fails. The lemma's conclusion "$\mathfrak m M = M \Rightarrow M = 0$" simply does not apply, so $\mathfrak m \mathbb Q = \mathbb Q$ with $\mathbb Q \neq 0$ is no contradiction. $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** $M = \mathbb Q$ is a nonzero $\mathbb Z_{(p)}$-module with $\mathfrak m M = M$, not contradicting Nakayama because $\mathbb Q$ is not finitely generated.
>
> Multiplication by $p$ is invertible on $\mathbb Q$, so $p\mathbb Q = \mathbb Q$, giving $\mathfrak m \mathbb Q = (p)\mathbb Z_{(p)} \cdot \mathbb Q = \mathbb Q$. Clearly $\mathbb Q \neq 0$. If $\mathbb Q$ were finitely generated over $\mathbb Z_{(p)}$ by $q_1,\dots,q_r$, all elements would have denominators (at primes $\neq p$) bounded by a common $D$, but $\mathbb Q$ has elements with unbounded such denominators — contradiction. So $\mathbb Q$ is not finitely generated, the finite-generation hypothesis of Nakayama fails, and there is no contradiction. (The Prüfer module $\mathbb Z[\tfrac1p]/\mathbb Z$ over $\mathbb Z$ is an alternative witness.) $\blacksquare$

---

# Key Takeaways

**When a module is not finitely generated, expect Nakayama to fail — and build the counterexample by inverting the ideal.** The instinct this exercise drills: the moment you see "$\mathfrak m M = M$ with $M \neq 0$", check finite generation, because that is the only hypothesis the configuration can be violating (assuming the ring is local, so $\mathfrak m = J$). To *construct* such a module, make multiplication by the relevant element surjective — easiest by making it *invertible*, i.e. by taking a module where you can already divide. $\mathbb Q$ over $\mathbb Z_{(p)}$, $\mathbb Z[\tfrac1p]/\mathbb Z$ over $\mathbb Z$, and any divisible module over a domain are the stock witnesses. The general principle: divisible modules are the obstruction to Nakayama, and finite generation is exactly the condition that excludes divisibility.

**Finite generation is what makes the determinant trick — and hence Nakayama — run; without it, there is no characteristic polynomial.** The deep reason the counterexample exists is mechanical: the proof of Nakayama builds a finite matrix $P$ from the action of the identity on a finite generating set, and takes its characteristic polynomial. With $M = \mathbb Q$ infinitely generated, there is no finite generating set, no matrix, no polynomial — the engine has nothing to grip. This is the recurring lesson of the chapter's counterexamples: every failure of a Nakayama-type theorem traces to the absence of a finite generating set, and the standard witnesses are infinitely generated modules where an element acts invertibly (here $p$) or shifts coordinates (the left shift in the surjective-endomorphism exercise). Compare [[Ex - A surjective endomorphism of a finitely generated module is injective]], where infinite generation breaks "surjective $\Rightarrow$ injective" by exactly the same loss of the finite matrix.

**The two hypotheses of Nakayama fail in different rings, and isolating which one fails is the diagnostic.** It is worth distinguishing the two ways Nakayama can be inapplicable. Here, over the *local* ring $\mathbb Z_{(p)}$, the Jacobson hypothesis $\mathfrak m \subseteq J$ holds (it is an equality), so the failure is *finite generation*. Contrast the other standard non-example: over $\mathbb Z$, the module $\mathbb Z/q$ ($q \neq p$ prime) has $p \cdot (\mathbb Z/q) = \mathbb Z/q$ and is *finitely generated*, but Nakayama still does not apply because $(p) \not\subseteq J(\mathbb Z) = (0)$ — the *Jacobson* hypothesis fails. When you meet "$\mathfrak a M = M$ with $M \neq 0$", the diagnostic is to ask which hypothesis is missing: is $M$ infinitely generated, or is $\mathfrak a$ too big for the Jacobson radical? Localizing fixes the second; nothing fixes the first.
