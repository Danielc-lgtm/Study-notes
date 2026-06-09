---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Noetherian Ring"
  - "Def - Prime and Maximal Ideal"
  - "Def - Finitely Generated Module"
  - "Thm - The Krull Intersection Theorem"
  - "Thm - The Artin-Rees Lemma"
  - "Thm - Nakayama's Lemma"
  - "Def - The Jacobson Radical"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $(R, \mathfrak{m})$ be a Noetherian local ring and $M$ a [[Def - Finitely Generated Module|finitely generated]] $R$-module. Prove:
$$\bigcap_{n \geq 0} \mathfrak{m}^n M = 0.$$
Deduce that $\bigcap_n \mathfrak{m}^n = 0$ in $R$ (no nonzero element of $R$ is divisible by every power of $\mathfrak{m}$), and conclude that the $\mathfrak{m}$-adic completion map
$$\varphi : M \to \hat{M} = \varprojlim_n M/\mathfrak{m}^n M, \qquad \ker\varphi = \bigcap_n \mathfrak{m}^n M,$$
is **injective**. Then show by example that the local (or Jacobson-radical) hypothesis is essential: exhibit a Noetherian ring $R$ and an ideal $\mathfrak{a}$ with $\bigcap_n \mathfrak{a}^n \neq 0$.

**Recall:**

![[Thm - The Krull Intersection Theorem#Statement]]

A **local ring** $(R, \mathfrak{m})$ has a unique [[Def - Prime and Maximal Ideal|maximal ideal]] $\mathfrak{m}$, so the [[Def - The Jacobson Radical|Jacobson radical]] $\operatorname{Jac}(R) = \mathfrak{m}$ and *every* proper ideal lies in $\mathfrak{m}$. The set $N = \bigcap_n \mathfrak{m}^n M$ is the submodule of elements "infinitely deep" in the $\mathfrak{m}$-adic filtration. The **$\mathfrak{m}$-adic completion** is $\hat{M} = \varprojlim M/\mathfrak{m}^n M$, and the completion map $\varphi(x) = (x + \mathfrak{m}^n M)_n$ has kernel exactly the elements that are $0$ in every quotient $M/\mathfrak{m}^n M$, i.e. $\bigcap_n \mathfrak{m}^n M$. So "$\varphi$ injective" and "$\bigcap_n \mathfrak{m}^n M = 0$" are the same statement.

The two tools are [[Thm - The Artin-Rees Lemma|Artin–Rees]] and [[Thm - Nakayama's Lemma|Nakayama's lemma]]:

![[Thm - Nakayama's Lemma#Statement]]

---

# Convergent Strategy

**Problem class.** This is a *prove-a-submodule-vanishes* problem, attacked by the chapter's signature two-stroke engine: use Artin–Rees to convert an infinite intersection into a single fixed-point equation $\mathfrak{m}N = N$, then use Nakayama to force $N = 0$. As the [[Commutative Algebra XI — Graded Rings and the Artin-Rees Lemma#Problem-Solving Strategy|topic-page strategy]] records, "show a deep submodule is zero" routes through exactly this pairing.

**Assumption pattern.** Three assumptions are doing distinct jobs and recognising each is the key. *Noetherian + finitely generated* is the Artin–Rees input. *Local* (equivalently $\mathfrak{m} = \operatorname{Jac}(R)$) is the Nakayama input — it is what guarantees $1 + a$ is a unit for $a \in \mathfrak{m}$. The intersection $N = \bigcap_n \mathfrak{m}^n M$ being *infinitely $\mathfrak{m}$-divisible* is the trigger: $N \subseteq \mathfrak{m}^n M$ for every $n$ means the induced filtration on $N$ is constant, which is what collapses Artin–Rees's stability statement to $\mathfrak{m}N = N$.

**Theorem routing.** The route is: set $N = \bigcap_n \mathfrak{m}^n M$; note $N \cap \mathfrak{m}^n M = N$ for all $n$ (since $N \subseteq \mathfrak{m}^n M$); apply [[Thm - The Artin-Rees Lemma|Artin–Rees]] to the $\mathfrak{m}$-adic filtration to get $N \cap \mathfrak{m}^{n+1}M = \mathfrak{m}(N \cap \mathfrak{m}^n M)$ for large $n$, which becomes $N = \mathfrak{m}N$; apply [[Thm - Nakayama's Lemma|Nakayama]] (legal because $\mathfrak{m} = \operatorname{Jac}(R)$) to conclude $N = 0$. The deduction $\bigcap_n \mathfrak{m}^n = 0$ is the case $M = R$; the completion-map injectivity is reading off $\ker\varphi = N = 0$. The counterexample uses a *non-local* ring where $\mathfrak{m} \not\subseteq \operatorname{Jac}$ fails, e.g. an idempotent-generated ideal.

**Key decision point.** The non-obvious move is the substitution $N \cap \mathfrak{m}^n M = N$. It looks like nothing, but it is the entire reason Artin–Rees applies: the lemma's conclusion is about the *induced* filtration $(N \cap \mathfrak{m}^n M)$, and only because $N$ lies inside every $\mathfrak{m}^n M$ does that induced filtration collapse to the constant filtration $N, N, N, \dots$, turning the stability equation into the Nakayama-ready $N = \mathfrak{m}N$. The second decision is to recognise that the local hypothesis is *not optional* — and the discipline of constructing a counterexample (an idempotent ideal $\mathfrak{a} = (e)$ with $\mathfrak{a}^n = \mathfrak{a}$) pins down exactly what goes wrong without it: $1 + a$ need not be a unit, so Nakayama fails.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra XI — Graded Rings and the Artin-Rees Lemma#Legal Operations|the topic page's Legal Operations]]:

1. **Collapse an infinite intersection into a fixed-point equation via Artin–Rees (operation 4).** Use $N \cap \mathfrak{m}^n M = N$ to turn the stability conclusion into $\mathfrak{m}N = N$.

2. **Close a fixed-point equation with Nakayama (operation 10).** From $\mathfrak{m}N = N$ with $\mathfrak{m} = \operatorname{Jac}(R)$ and $N$ finitely generated, conclude $N = 0$.

3. **Read a completion kernel off an intersection (operation 9).** Identify $\ker\varphi = \bigcap_n \mathfrak{m}^n M$ and convert vanishing into injectivity.

4. **Test necessity of a hypothesis with an idempotent counterexample.** Exhibit a non-local ring where $\mathfrak{a}^n = \mathfrak{a} \neq 0$ to show the local hypothesis cannot be dropped.

---

# Hints

> [!note]- Hint 1
> Let $N = \bigcap_n \mathfrak{m}^n M$. You want to show $N = 0$. The chapter's engine for "a submodule is zero" is Artin–Rees followed by Nakayama. To use Artin–Rees, look at how $N$ sits inside the $\mathfrak{m}$-adic filtration of $M$: what is $N \cap \mathfrak{m}^n M$?

> [!note]- Hint 2
> Since $N \subseteq \mathfrak{m}^n M$ for every $n$ (it is the intersection of them all), $N \cap \mathfrak{m}^n M = N$. Now apply [[Thm - The Artin-Rees Lemma|Artin–Rees]] to the stable $\mathfrak{m}$-adic filtration $(\mathfrak{m}^n M)$ and the submodule $N$: the induced filtration $(N \cap \mathfrak{m}^n M)$ is stable, so $N \cap \mathfrak{m}^{n+1}M = \mathfrak{m}(N \cap \mathfrak{m}^n M)$ for large $n$. Substitute $N \cap \mathfrak{m}^k M = N$.

> [!note]- Hint 3
> The substitution gives $N = \mathfrak{m}N$. Now $N$ is finitely generated (submodule of finitely generated over Noetherian), and $\mathfrak{m} = \operatorname{Jac}(R)$ because $R$ is local. What does [[Thm - Nakayama's Lemma|Nakayama]] say about a finitely generated module $N$ with $\mathfrak{m}N = N$?

> [!note]- Hint 4
> Nakayama forces $N = 0$. For the completion map: $\ker\varphi = \{x : x \in \mathfrak{m}^n M \text{ for all } n\} = \bigcap_n \mathfrak{m}^n M = N = 0$, so $\varphi$ is injective. For the counterexample, you need a ring where $\bigcap_n \mathfrak{a}^n \neq 0$ — try an *idempotent* generator: if $e^2 = e$, what is $(e)^n$?

---

# Solution

The proof is the Artin–Rees / Nakayama two-stroke. Step 1 records that $N = \bigcap_n \mathfrak{m}^n M$ meets the filtration trivially, $N \cap \mathfrak{m}^n M = N$. Step 2 runs Artin–Rees to get $N = \mathfrak{m}N$. Step 3 runs Nakayama to get $N = 0$, then reads off the corollaries ($\bigcap \mathfrak{m}^n = 0$, $\varphi$ injective). Step 4 builds the counterexample showing the local hypothesis is essential.

**Step 1: The stable submodule meets every filtration level fully, $N \cap \mathfrak{m}^n M = N$.**

By definition $N = \bigcap_n \mathfrak{m}^n M \subseteq \mathfrak{m}^n M$ for each $n$, so intersecting with $\mathfrak{m}^n M$ returns $N$.

> [!note]- Derivation
> Set $N = \bigcap_{k \geq 0}\mathfrak{m}^k M$. For any fixed $n$, $N \subseteq \mathfrak{m}^n M$ (the intersection is contained in each member). Hence $N \cap \mathfrak{m}^n M = N$ for every $n$: the induced filtration $(N \cap \mathfrak{m}^n M)_n$ on $N$ is the *constant* filtration $N, N, N, \dots$. Also $N$ is finitely generated: it is a submodule of $M$, which is a Noetherian module (finitely generated over the Noetherian ring $R$), so all its submodules are finitely generated.

**Step 2: Artin–Rees gives $N = \mathfrak{m}N$.**

The $\mathfrak{m}$-adic filtration is stable, so by Artin–Rees the induced filtration on $N$ is stable; substituting $N \cap \mathfrak{m}^k M = N$ collapses the stability equation to $N = \mathfrak{m}N$.

> [!note]- Derivation
> The $\mathfrak{m}$-adic filtration $M_n = \mathfrak{m}^n M$ is a stable $\mathfrak{m}$-filtration of $M$ (indeed $\mathfrak{m}\cdot\mathfrak{m}^n M = \mathfrak{m}^{n+1}M$ for all $n$). By the [[Thm - The Artin-Rees Lemma|Artin–Rees Lemma]] (with $R$ Noetherian, $M$ finitely generated, $N \subseteq M$), the induced filtration $(N \cap \mathfrak{m}^n M)$ is a stable $\mathfrak{m}$-filtration of $N$. Stability gives an integer $c$ with
> $$N \cap \mathfrak{m}^{n+1}M = \mathfrak{m}\,(N \cap \mathfrak{m}^n M) \qquad (n \geq c).$$
> By Step 1, the left side equals $N$ and $N \cap \mathfrak{m}^n M = N$, so the right side equals $\mathfrak{m}N$. Therefore
> $$N = \mathfrak{m}N.$$
> (The inclusion $\mathfrak{m}N \subseteq N$ is automatic; Artin–Rees supplies the reverse.)

**Step 3: Nakayama gives $N = 0$; deduce the corollaries.**

Since $N$ is finitely generated with $\mathfrak{m}N = N$ and $\mathfrak{m} = \operatorname{Jac}(R)$, Nakayama forces $N = 0$. Taking $M = R$ gives $\bigcap_n \mathfrak{m}^n = 0$, and $\ker\varphi = N = 0$ gives injectivity of the completion map.

> [!note]- Derivation
> $N$ is finitely generated (Step 1) and satisfies $\mathfrak{m}N = N$ (Step 2). Because $R$ is local, $\operatorname{Jac}(R) = \mathfrak{m}$, so $\mathfrak{m} \subseteq \operatorname{Jac}(R)$ — the hypothesis of [[Thm - Nakayama's Lemma|Nakayama's lemma]]. Nakayama then forces $N = 0$:
> $$\bigcap_{n \geq 0}\mathfrak{m}^n M = 0.$$
> *(Equivalently, the determinant trick gives $a \in \mathfrak{m}$ with $(1+a)N = 0$; since $a \in \mathfrak{m} = \operatorname{Jac}(R)$, $1 + a$ is a unit, so $N = 0$.)*
>
> **Deduction $\bigcap_n \mathfrak{m}^n = 0$.** Apply the result to $M = R$, the free rank-one module: $\bigcap_n \mathfrak{m}^n R = \bigcap_n \mathfrak{m}^n = 0$. So no nonzero element of $R$ lies in every power of $\mathfrak{m}$ — every nonzero element has a finite $\mathfrak{m}$-order.
>
> **Injectivity of $\varphi$.** The completion map $\varphi : M \to \hat{M} = \varprojlim M/\mathfrak{m}^n M$ sends $x \mapsto (x + \mathfrak{m}^n M)_n$. Its kernel is $\{x : x \in \mathfrak{m}^n M \text{ for all } n\} = \bigcap_n \mathfrak{m}^n M = N = 0$. Hence $\varphi$ is injective: $M$ embeds in its $\mathfrak{m}$-adic completion, and the $\mathfrak{m}$-adic topology on $M$ is Hausdorff (separated).

**Step 4: The local hypothesis is essential — a counterexample.**

In a non-local ring, $\bigcap_n \mathfrak{a}^n$ can be nonzero; an idempotent generator gives $\mathfrak{a}^n = \mathfrak{a}$ for all $n$.

> [!note]- Derivation
> Let $R = k \times k$ (or any product of two nonzero rings), and $e = (1, 0)$, an idempotent: $e^2 = e$. Take $\mathfrak{a} = (e) = k \times 0$. Then $\mathfrak{a}^n = (e^n) = (e) = \mathfrak{a}$ for all $n \geq 1$, since $e^n = e$. Hence
> $$\bigcap_{n \geq 1}\mathfrak{a}^n = \mathfrak{a} = k \times 0 \neq 0.$$
> $R = k \times k$ is Noetherian (a finite product of fields), $\mathfrak{a}$ is a proper ideal, yet the intersection is nonzero. What fails? $R$ is *not local* — it has two maximal ideals $k \times 0$ and $0 \times k$ — so $\operatorname{Jac}(R) = (k\times 0)\cap(0 \times k) = 0$, and $\mathfrak{a} = k \times 0 \not\subseteq \operatorname{Jac}(R) = 0$. The Nakayama step is unavailable: from $\mathfrak{a}N = N$ one extracts $a \in \mathfrak{a}$ with $(1 + a)N = 0$, but with $a = -e$ (i.e. $a = (-1, 0) \in \mathfrak{a}$), $1 + a = (0, 1)$ is *not* a unit and indeed annihilates $\mathfrak{a} = k \times 0$. The local hypothesis is exactly what rules this out: in a local ring $1 + a$ is always a unit for $a \in \mathfrak{m}$.

> [!note]- Complete formal solution
> Let $(R, \mathfrak{m})$ be Noetherian local, $M$ finitely generated, $N = \bigcap_n \mathfrak{m}^n M$.
>
> Since $N \subseteq \mathfrak{m}^n M$ for all $n$, $N \cap \mathfrak{m}^n M = N$. The $\mathfrak{m}$-adic filtration $(\mathfrak{m}^n M)$ is stable, so by the [[Thm - The Artin-Rees Lemma|Artin–Rees Lemma]] the induced filtration $(N \cap \mathfrak{m}^n M)$ on $N$ is stable: $N \cap \mathfrak{m}^{n+1}M = \mathfrak{m}(N \cap \mathfrak{m}^n M)$ for large $n$. Substituting $N \cap \mathfrak{m}^k M = N$ gives $N = \mathfrak{m}N$.
>
> $N$ is finitely generated (submodule of $M$, Noetherian over $R$) and $\mathfrak{m} = \operatorname{Jac}(R)$ ($R$ local), so [[Thm - Nakayama's Lemma|Nakayama]] gives $N = 0$. Thus $\bigcap_n \mathfrak{m}^n M = 0$; with $M = R$, $\bigcap_n \mathfrak{m}^n = 0$. The completion map $\varphi : M \to \varprojlim M/\mathfrak{m}^n M$ has $\ker\varphi = \bigcap_n \mathfrak{m}^n M = 0$, so $\varphi$ is injective.
>
> *Necessity of locality:* in $R = k \times k$ with $\mathfrak{a} = (e)$, $e = (1,0)$ idempotent, $\mathfrak{a}^n = \mathfrak{a}$ for all $n$, so $\bigcap_n \mathfrak{a}^n = \mathfrak{a} \neq 0$. Here $\mathfrak{a} \not\subseteq \operatorname{Jac}(R) = 0$, so Nakayama does not apply. $\blacksquare$

---

# Key Takeaways

**"Show a submodule is zero" over a Noetherian local ring = Artin–Rees to get $N = \mathfrak{m}N$, then Nakayama to get $N = 0$.** This two-stroke is the single most important problem-solving reflex of the chapter, and it generalizes far beyond the Krull intersection. Whenever you face a submodule $N$ that is "infinitely deep" — defined as an intersection $\bigcap_n \mathfrak{m}^n M$, or as a stable submodule, or as the kernel of a completion — the move is: (1) observe $N$ sits inside every filtration level so the induced filtration collapses, (2) Artin–Rees converts the infinite condition into the *finite* equation $N = \mathfrak{m}N$, (3) Nakayama (needing $\mathfrak{m} \subseteq \operatorname{Jac}$) finishes. The trigger to recognise the pattern: an infinite intersection of ideal-powers times a module, over a Noetherian local (or Jacobson-radical) ring. The reason it works is that Artin–Rees is exactly the device that produces, out of infinitely many containments, the one algebraic equation Nakayama can consume.

**The local hypothesis is load-bearing, and its job is precisely to make $1 + a$ a unit.** The counterexample $R = k \times k$, $\mathfrak{a} = (e)$ is worth internalizing because it isolates *what* goes wrong without locality: Artin–Rees still gives $\mathfrak{a}N = N$, but the final Nakayama step extracts only $(1 + a)N = 0$ with $a \in \mathfrak{a}$, and $1 + a$ need not be a unit when $\mathfrak{a} \not\subseteq \operatorname{Jac}(R)$. In the idempotent example $1 + a = 1 - e$ is itself a nontrivial idempotent annihilating $\mathfrak{a}$. The transferable diagnostic: any theorem that ends "...therefore $N = 0$ by Nakayama" secretly requires the acting ideal to lie in the Jacobson radical, and the way to test whether a hypothesis is essential is to manufacture a ring where $1 + a$ fails to be a unit — idempotents and zero-divisors are the standard wreckers. This is the same hypothesis-necessity discipline used in [[Ex - A nonstandard grading and its Hilbert function]] to locate which Hilbert–Serre assumption fails.

**Krull intersection is the separatedness of the adic topology: it makes the completion faithful.** The corollary "$\varphi : M \to \hat{M}$ is injective" is the conceptual payoff, and it is worth seeing as a statement about *information*: completing a module replaces it by the system of its approximations $M/\mathfrak{m}^n M$, and injectivity says no information is lost — distinct elements have distinct sequences of approximations. Equivalently, the $\mathfrak{m}$-adic topology is Hausdorff: $0$ is a closed point. The trigger for recognising when this matters: any argument of the form "complete, solve in $\hat{R}$ where the structure theorems and Hensel's lemma live, then descend to $R$" *requires* $R \hookrightarrow \hat{R}$ to be injective, which is Krull intersection. Without it, descent could fail because the completion forgot something. This is the bridge to the **completions** chapter, where faithfulness of completion underwrites the entire technique; compare [[Ex - The Artin-Rees lemma and the subspace topology]], which uses the same Artin–Rees input to get exactness of completion rather than separatedness.
