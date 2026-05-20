---
type: theorem
subject: measure-theory
prereqs:
  - "Def - Algebra and σ-Algebra"
  - "Def - Generated σ-Algebra"
tags: [analysis, measure-theory, probability]
---

# Notation

$X$ a set. A **$\pi$-system** $\mathcal{P}$ is a family closed under finite intersections (and containing $\emptyset$). A **$\lambda$-system** (or **d-system**) $\mathcal{L}$ contains $X$, is closed under proper differences ($A\subseteq B\Rightarrow B\setminus A\in\mathcal{L}$), and under increasing countable unions.

---

# Motivation

A recurring obstacle: one wants to prove a property holds for *all* sets in a $\sigma$-algebra $\mathcal{A}=\sigma(\mathcal{P})$, but can only verify it directly on the simple generators $\mathcal{P}$. The generated $\sigma$-algebra is [[Def - Generated σ-Algebra|non-constructive]] — there is no induction up to it. Dynkin's $\pi$–$\lambda$ theorem is the induction principle that fills the gap: **if a property survives finite intersections (so it can start on a $\pi$-system) and forms a $\lambda$-system, it propagates to the whole generated $\sigma$-algebra.** It is the workhorse behind every "two measures agreeing on a generating $\pi$-system agree everywhere" argument — uniqueness of [[Thm - Product Measure|product measures]], uniqueness of laws from [[Def - Distribution Function|distribution functions]], the [[Thm - Fubini-Tonelli Theorem|measurability of slices]], and the very definition of [[Def - Independence|independence]].

---

# Sources and Targets

**Sources.** The theorem applies whenever the family of "good sets" $\mathcal{L}$ can be shown to be a $\lambda$-system and to contain a $\pi$-system $\mathcal{P}$ generating the target $\sigma$-algebra. The non-obvious recognitions: the family $\{A:\mu_1(A)=\mu_2(A)\}$ is a $\lambda$-system (for finite measures); the family of sets on which a Fubini-type identity holds is a $\lambda$-system; the rectangles, the rays $(-\infty,t]$, the cylinder sets are $\pi$-systems.

**Targets.** "$\sigma(\mathcal{P})\subseteq\mathcal{L}$" yields: **measure uniqueness** — two (σ-)finite measures equal on a generating $\pi$-system are equal; **independence criteria** — independence need only be checked on generating $\pi$-systems; the **slice and product-measure lemmas** of [[Thm - Fubini-Tonelli Theorem|Fubini]].

---

# Statement

**(Dynkin's $\pi$–$\lambda$ theorem.)** Let $\mathcal{P}$ be a $\pi$-system and $\mathcal{L}$ a $\lambda$-system on $X$ with $\mathcal{P}\subseteq\mathcal{L}$. Then $\sigma(\mathcal{P})\subseteq\mathcal{L}$.

**(Measure uniqueness, the standard corollary.)** If $\mu_1,\mu_2$ are measures on $\sigma(\mathcal{P})$ with $\mu_1=\mu_2$ on a generating $\pi$-system $\mathcal{P}$, and either both are finite with $\mu_1(X)=\mu_2(X)$, or $X=\bigcup_n P_n$ for $P_n\in\mathcal{P}$ of finite measure, then $\mu_1=\mu_2$ on all of $\sigma(\mathcal{P})$.

---

# Why Is It True

A $\sigma$-algebra is exactly "a $\pi$-system that is also a $\lambda$-system": closed under intersection *and* under complement-and-countable-union. The theorem's content is that *if you already have a $\lambda$-system, you only need to add $\pi$-closure to upgrade it to a $\sigma$-algebra* — and a $\lambda$-system containing a $\pi$-system can be shrunk to one that has $\pi$-closure.

The proof is a *two-step minimality argument*. Let $\mathcal{L}_0$ be the smallest $\lambda$-system containing $\mathcal{P}$ (intersection of all such — $\lambda$-systems are closed under intersection). Goal: $\mathcal{L}_0$ is a $\sigma$-algebra; then $\sigma(\mathcal{P})\subseteq\mathcal{L}_0\subseteq\mathcal{L}$.

It suffices to show $\mathcal{L}_0$ is $\pi$-closed (a $\lambda$-system with $\pi$-closure is a $\sigma$-algebra). Fix the auxiliary family $\mathcal{L}_1=\{A\in\mathcal{L}_0:A\cap P\in\mathcal{L}_0\ \forall P\in\mathcal{P}\}$ — sets that intersect everything in $\mathcal{P}$ correctly. One checks $\mathcal{L}_1$ is a $\lambda$-system, and it contains $\mathcal{P}$ (because $\mathcal{P}$ is $\pi$-closed). By *minimality* of $\mathcal{L}_0$, $\mathcal{L}_1=\mathcal{L}_0$ — so every $A\in\mathcal{L}_0$ intersects every $P\in\mathcal{P}$ correctly. Now repeat: $\mathcal{L}_2=\{A\in\mathcal{L}_0:A\cap B\in\mathcal{L}_0\ \forall B\in\mathcal{L}_0\}$ is a $\lambda$-system, and the *first* step shows it contains $\mathcal{P}$; minimality again gives $\mathcal{L}_2=\mathcal{L}_0$ — $\mathcal{L}_0$ is $\pi$-closed.

The slogan: **bootstrap $\pi$-closure by the minimality of the generated $\lambda$-system, applied twice** — first to get "$\mathcal{L}_0$ closes under intersection with $\mathcal{P}$," then to upgrade to "with all of $\mathcal{L}_0$."

For uniqueness: $\mathcal{L}=\{A:\mu_1(A)=\mu_2(A)\}$ is a $\lambda$-system (proper differences and increasing unions respect equality, using finiteness to subtract), contains the $\pi$-system $\mathcal{P}$, hence contains $\sigma(\mathcal{P})$.

---

# What Makes This Hard

The proof's one genuine idea is the **double application of minimality** to the auxiliary families $\mathcal{L}_1,\mathcal{L}_2$ — a bootstrap that most people do not invent unaided. The conceptual hurdle is *why* one introduces $\lambda$-systems at all: they are precisely the closure properties of "the set of $A$ where a finitely-additive identity persists" (differences and increasing limits respect such identities; *arbitrary* unions do not), so they are the natural home of "the good sets," while the *hypothesis* one can check is $\pi$-closure. The theorem mediates between the checkable hypothesis and the desired conclusion.

---

# Rederivation Scaffold

**High-level strategy.** Let $\mathcal{L}_0$ = smallest $\lambda$-system $\supseteq\mathcal{P}$. Show $\mathcal{L}_0$ is $\pi$-closed (hence a $\sigma$-algebra) by applying minimality twice to auxiliary families.

**Subgoal decomposition.**

1. **A $\lambda$-system with $\pi$-closure is a $\sigma$-algebra.** Check the $\sigma$-algebra axioms from the $\lambda$/$\pi$ axioms.
2. **$\mathcal{L}_1=\{A\in\mathcal{L}_0:A\cap P\in\mathcal{L}_0\,\forall P\in\mathcal{P}\}$ is a $\lambda$-system containing $\mathcal{P}$.** Minimality $\Rightarrow\mathcal{L}_1=\mathcal{L}_0$.
3. **$\mathcal{L}_2=\{A\in\mathcal{L}_0:A\cap B\in\mathcal{L}_0\,\forall B\in\mathcal{L}_0\}$ is a $\lambda$-system; step 2 $\Rightarrow\mathcal{P}\subseteq\mathcal{L}_2$.** Minimality $\Rightarrow\mathcal{L}_2=\mathcal{L}_0$ — $\pi$-closure.
4. **Conclude** $\mathcal{L}_0$ is a $\sigma$-algebra, $\sigma(\mathcal{P})\subseteq\mathcal{L}_0\subseteq\mathcal{L}$.

---

# Lemma Decomposition

> [!note]- Lemma 1: λ-system + π-closure ⇒ σ-algebra
> **Statement:** A $\lambda$-system closed under finite intersections is a $\sigma$-algebra.
>
> > [!note]- Full proof
> > It contains $X$; $A^c=X\setminus A$ by proper-difference closure. For $A,B$: $A\cup B=(A^c\cap B^c)^c$, so finite unions, hence (combining with disjointification and increasing-union closure) countable unions, lie in it. $\square$

> [!note]- Lemma 2: The bootstrap
> **Statement:** The smallest $\lambda$-system $\mathcal{L}_0\supseteq\mathcal{P}$ is $\pi$-closed.
>
> > [!note]- Full proof
> > $\mathcal{L}_1=\{A\in\mathcal{L}_0:A\cap P\in\mathcal{L}_0\ \forall P\in\mathcal{P}\}$ is a $\lambda$-system (the $\lambda$-axioms pass through intersection with a fixed $P$) and contains $\mathcal{P}$ (as $\mathcal{P}$ is $\pi$-closed). By minimality of $\mathcal{L}_0$, $\mathcal{L}_1=\mathcal{L}_0$: every $A\in\mathcal{L}_0$ meets every $P\in\mathcal{P}$ correctly. Then $\mathcal{L}_2=\{A\in\mathcal{L}_0:A\cap B\in\mathcal{L}_0\ \forall B\in\mathcal{L}_0\}$ is a $\lambda$-system, and by the previous sentence $\mathcal{P}\subseteq\mathcal{L}_2$; minimality gives $\mathcal{L}_2=\mathcal{L}_0$. So $\mathcal{L}_0$ is $\pi$-closed. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> By Lemma 2, $\mathcal{L}_0$ (smallest $\lambda$-system $\supseteq\mathcal{P}$) is $\pi$-closed; by Lemma 1 it is a $\sigma$-algebra. Hence $\sigma(\mathcal{P})\subseteq\mathcal{L}_0$. Since $\mathcal{P}\subseteq\mathcal{L}$ and $\mathcal{L}$ is a $\lambda$-system, $\mathcal{L}_0\subseteq\mathcal{L}$, so $\sigma(\mathcal{P})\subseteq\mathcal{L}$. Uniqueness corollary: $\{A:\mu_1(A)=\mu_2(A)\}$ is a $\lambda$-system containing $\mathcal{P}$ (finiteness licenses the subtraction in the proper-difference axiom; the $\sigma$-finite case splits $X$ along the $P_n$), hence contains $\sigma(\mathcal{P})$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

In probability the $\pi$–$\lambda$ theorem is *ubiquitous*: a law on $\mathbb{R}$ is determined by its values on the rays $(-\infty,t]$ (a $\pi$-system) — i.e. by its [[Def - Distribution Function|distribution function]]; [[Def - Independence|independence]] of $\sigma$-algebras need only be checked on generating $\pi$-systems; two processes with the same finite-dimensional distributions (cylinder sets, a $\pi$-system) have the same law. Each is "agree on a $\pi$-system $\Rightarrow$ agree on the $\sigma$-algebra."

---

# Bridges

- **[[Thm - Uniqueness of the Hahn-Carathéodory Extension]]** — the $\pi$–$\lambda$ uniqueness corollary is the clean, $\sigma$-finite restatement of extension-uniqueness, in the form used throughout probability.
- **[[Thm - Product Measure]]**, **[[Thm - Fubini-Tonelli Theorem]]** — both use $\pi$–$\lambda$ to push facts from rectangles to all product-measurable sets.
- **[[Def - Independence]]** *(Advanced Probability)* — independence is checked on $\pi$-systems and extended by this theorem.
