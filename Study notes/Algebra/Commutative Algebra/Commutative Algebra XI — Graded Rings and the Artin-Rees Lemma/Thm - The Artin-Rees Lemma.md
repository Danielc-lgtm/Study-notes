---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Noetherian Ring"
  - "Def - Ideal"
  - "Def - Module"
  - "Def - Submodule"
  - "Def - Finitely Generated Module"
  - "Def - Filtration and Stable Filtration"
  - "Def - The Associated Graded Ring and the Rees Algebra"
  - "Thm - A Graded Ring is Noetherian iff Finitely Generated in Degree One"
  - "Thm - Hilbert's Basis Theorem"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $R$ be a [[Def - Noetherian Ring|Noetherian ring]], $\mathfrak{a} \trianglelefteq R$ an [[Def - Ideal|ideal]], $M$ a [[Def - Finitely Generated Module|finitely generated]] $R$-module, $(M_n)_{n \geq 0}$ a [[Def - Filtration and Stable Filtration|filtration]] of $M$, and $N \subseteq M$ a [[Def - Submodule|submodule]]. The **Rees algebra** is $R^* = \bigoplus_{n \geq 0} \mathfrak{a}^n$ and the **Rees module** of the filtration is $M^* = \bigoplus_{n \geq 0} M_n$, a graded $R^*$-module (see [[Def - The Associated Graded Ring and the Rees Algebra]]). A filtration is **$\mathfrak{a}$-stable** if $\mathfrak{a} M_n = M_{n+1}$ for all large $n$. The full registry is on [[Commutative Algebra XI — Graded Rings and the Artin-Rees Lemma]].

---

# Statement

> **Theorem (Artin–Rees Lemma).** Let $R$ be a Noetherian ring, $\mathfrak{a} \trianglelefteq R$ an ideal, $M$ a finitely generated $R$-module, $(M_n)_{n \geq 0}$ a *stable* $\mathfrak{a}$-filtration of $M$, and $N \subseteq M$ a submodule. Then $(N \cap M_n)_{n \geq 0}$ is a stable $\mathfrak{a}$-filtration of $N$.

The standard special case — and the form most often quoted — takes the $\mathfrak{a}$-adic filtration $M_n = \mathfrak{a}^n M$:

> **Corollary (Artin–Rees, classical form).** Under the same hypotheses, there is an integer $c \geq 0$ such that for all $n \geq c$,
> $$\mathfrak{a}^n M \cap N = \mathfrak{a}^{n - c}\big(\mathfrak{a}^c M \cap N\big).$$
> In particular $\mathfrak{a}^n M \cap N \subseteq \mathfrak{a}^{n-c} N$ for all $n \geq c$: the trace on $N$ of the $\mathfrak{a}$-adic filtration of $M$ is, up to a bounded shift $c$, the $\mathfrak{a}$-adic filtration of $N$.

The two are equivalent: the theorem says $(N \cap M_n)$ is stable, and "stable" unwound for the $\mathfrak{a}$-adic case is exactly the displayed equation with $c$ the stabilization index. The one-line summary: **over a Noetherian ring, a stable filtration cuts a stable filtration on every submodule.**

---

# Motivation

The lemma answers a question that looks innocent and turns out to control the whole local theory: *how does the $\mathfrak{a}$-adic filtration of a module interact with a submodule?* You have $M$ with its tower $M \supseteq \mathfrak{a}M \supseteq \mathfrak{a}^2 M \supseteq \cdots$, and a submodule $N$. The submodule inherits a filtration by intersection, $N \supseteq N \cap \mathfrak{a}M \supseteq N \cap \mathfrak{a}^2 M \supseteq \cdots$, and the question is whether this *induced* filtration is the same — up to a harmless shift — as $N$'s *own* $\mathfrak{a}$-adic filtration $N \supseteq \mathfrak{a}N \supseteq \mathfrak{a}^2 N \supseteq \cdots$.

A priori these can differ. The element of $N$ might sit deep in the filtration of $M$ — be in $\mathfrak{a}^n M$ for large $n$ — without being correspondingly deep in $N$, i.e. without being in $\mathfrak{a}^{n} N$, because the witnesses $\sum a_i m_i$ to its $\mathfrak{a}^n M$-membership might use $m_i \in M$ that lie outside $N$. The naive expectation $\mathfrak{a}^n M \cap N = \mathfrak{a}^n N$ is *false* in general. What Artin–Rees rescues is that the discrepancy is *bounded*: there is one universal constant $c$ such that $\mathfrak{a}^n M \cap N \subseteq \mathfrak{a}^{n-c} N$ for all large $n$. The two filtrations on $N$ are not equal but *equivalent* — each contains a shift of the other — and equivalence is all you ever need, because equivalent filtrations define the same topology.

Why does this matter? Because it is the missing technical input for three of the most important facts in commutative algebra. The **Krull intersection theorem** ($\bigcap_n \mathfrak{a}^n M = 0$ in a Noetherian local ring) needs exactly this bounded-discrepancy statement to run a Nakayama argument. The exactness of completion on Noetherian modules — that $\hat{(\cdot)}$ preserves short exact sequences of finitely generated modules — needs Artin–Rees to compare the completion of $N$ computed inside $M$ with its intrinsic completion. And the comparison of the $\mathfrak{a}$-adic topology on a submodule with the induced topology — the subspace-topology question — is *literally* Artin–Rees. The lemma is the rule that says "the $\mathfrak{a}$-adic topology behaves well under taking submodules", and that good behaviour is what makes the entire $\mathfrak{a}$-adic / completion machinery work.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition $A$ is "$R$ Noetherian, $M$ finitely generated, and an $\mathfrak{a}$-stable filtration in hand". Recognising it:

The first disguised source is **any submodule of a finitely generated module over a Noetherian ring, with the $\mathfrak{a}$-adic filtration**. This is the default setting: $M_n = \mathfrak{a}^n M$ is automatically stable, so all the hypotheses are present the moment you have $N \subseteq M$ with $M$ finitely generated over Noetherian $R$. The bridge $B \to A$ is trivial but worth stating: "$\mathfrak{a}$-adic filtration" is *always* stable, so you never need to check stability in the classical form. *Example problem:* compare the $\mathfrak{a}$-adic topology on a submodule with the subspace topology (see [[Ex - The Artin-Rees lemma and the subspace topology]]).

The second disguised source is **$M = R$ itself, $N = \mathfrak{b}$ another ideal**. Then Artin–Rees compares $\mathfrak{a}^n \cap \mathfrak{b}$ with $\mathfrak{a}^{n-c}\mathfrak{b}$: there is $c$ with $\mathfrak{a}^n \cap \mathfrak{b} = \mathfrak{a}^{n-c}(\mathfrak{a}^c \cap \mathfrak{b})$ for $n \geq c$. The bridge: ideals are submodules of the free module $R$, which is finitely generated. *Example problem:* show that in a Noetherian local ring, $\bigcap_n \mathfrak{a}^n = 0$ by taking $\mathfrak{b} = \bigcap_n \mathfrak{a}^n$ (this routes into [[Thm - The Krull Intersection Theorem|Krull intersection]]).

The third disguised source is **a need to control completion of a submodule**. When you want the $\mathfrak{a}$-adic completion $\hat{N}$ computed inside $M$ to agree with $N$'s own completion, the hidden hypothesis is precisely that the induced filtration $N \cap \mathfrak{a}^n M$ is equivalent to $\mathfrak{a}^n N$ — which is Artin–Rees. The bridge: "completion is exact on f.g. modules over Noetherian rings" *is* Artin–Rees in disguise. *Example problem:* prove the completion functor is exact on short exact sequences of finitely generated modules (a key result of the completions chapter).

**Targets (Output Amplification)**

The conclusion $C$ is "$(N \cap \mathfrak{a}^n M)$ is a stable $\mathfrak{a}$-filtration of $N$", equivalently "$\exists c:\ \mathfrak{a}^n M \cap N \subseteq \mathfrak{a}^{n-c} N$ for $n \geq c$".

Combine $C$ with **Nakayama's lemma** in a Noetherian local ring $(R, \mathfrak{m})$. Take $N = \bigcap_n \mathfrak{m}^n M$ and $\mathfrak{a} = \mathfrak{m}$. Then $N \subseteq \mathfrak{m}^n M$ for all $n$, so $N = N \cap \mathfrak{m}^{c+1} M = \mathfrak{m}(N \cap \mathfrak{m}^c M) \subseteq \mathfrak{m}N$, giving $\mathfrak{m}N = N$, and Nakayama forces $N = 0$. The further result $E$ is the **Krull intersection theorem** $\bigcap_n \mathfrak{m}^n M = 0$. The combination is non-obvious because Artin–Rees provides the *single* equation $N = \mathfrak{m}N$ that Nakayama needs, out of an infinite intersection.

Combine $C$ with **the induced versus subspace topology**. The bounded discrepancy $\mathfrak{a}^n M \cap N \subseteq \mathfrak{a}^{n-c} N \subseteq \mathfrak{a}^n M \cap N$ (the last by $\mathfrak{a}^{n-c}N \subseteq \mathfrak{a}^{n-c}M$ and $N$) sandwiches the two filtrations of $N$ between shifts of each other. The further result $E$: the $\mathfrak{a}$-adic topology on $N$ *equals* the topology induced from the $\mathfrak{a}$-adic topology on $M$. The combination is non-obvious because topological equality follows from filtration equivalence, not equality, and Artin–Rees gives exactly equivalence.

Combine $C$ with **the snake/completion machinery**. Tensoring or completing a short exact sequence $0 \to N \to M \to M/N \to 0$ and tracking filtrations, Artin–Rees guarantees the filtration on $N$ from $M$ is cofinal with $N$'s own, so $\varprojlim$ over the two filtrations agree. The further result $E$ is **exactness of $\mathfrak{a}$-adic completion** on finitely generated modules over a Noetherian ring. This is non-obvious because completion is only left-exact in general; Artin–Rees is precisely what upgrades it to exact in the Noetherian f.g. case.

---

# Why Is It True

The lemma feels like it should be hard — it is an infinite family of statements (one per degree $n$, comparing $N \cap \mathfrak{a}^n M$ with $\mathfrak{a}^{n}N$) with a uniform bound $c$, and uniform bounds over infinitely many degrees usually require real work. The insight is that *all infinitely many statements are packaged into a single finite-generation statement* about one module over one ring, and that ring is Noetherian.

Here is the package. Form the Rees algebra $R^* = \bigoplus_n \mathfrak{a}^n$ — the graded ring that stacks the powers of $\mathfrak{a}$ into degree slots. The filtration $(\mathfrak{a}^n M)$ becomes the Rees module $M^* = \bigoplus_n \mathfrak{a}^n M$, a graded $R^*$-module, and the induced filtration on $N$ becomes the *submodule* $N^* = \bigoplus_n (N \cap \mathfrak{a}^n M) \subseteq M^*$. The whole question "is the induced filtration stable?" is, by a clean lemma, exactly the question "is $N^*$ finitely generated over $R^*$?"

Now run the Noetherian machine. Because $R$ is Noetherian, the Rees algebra $R^* = \bigoplus \mathfrak{a}^n$ is generated over $R$ in degree one by generators of $\mathfrak{a}$, so it is itself Noetherian by [[Thm - A Graded Ring is Noetherian iff Finitely Generated in Degree One|the graded Noetherian criterion]]. The Rees module $M^*$ of the *stable* filtration $(\mathfrak{a}^n M)$ is finitely generated over $R^*$ (this is the other half of the same lemma: stable $\iff$ finitely generated). A finitely generated module over a Noetherian ring is a Noetherian module — its submodules are all finitely generated. In particular the submodule $N^*$ is finitely generated. Translating back: $N^*$ finitely generated means the induced filtration $(N \cap \mathfrak{a}^n M)$ is stable. Done.

**The whole proof is: package the infinitely many comparisons into one Rees module, observe the Rees algebra is Noetherian, and let "submodules of Noetherian modules are finitely generated" do everything.** The genius is the *change of category* — from "infinitely many filtration comparisons over $R$" to "one finiteness statement over $R^*$" — after which the Noetherian property of $R^*$ supplies the uniform bound $c$ for free, because finite generation of $N^*$ means it is generated in degrees $\leq c$, and that $c$ is the stabilization index.

The reason the bound is uniform: a finitely generated graded module is generated by elements in finitely many degrees, so there is a *largest* generating degree $c$, and beyond it everything is obtained by multiplying up — which is exactly "$N \cap \mathfrak{a}^{n+1}M = \mathfrak{a}(N \cap \mathfrak{a}^n M)$ for $n \geq c$". Noetherian-ness manufactures the single $c$ out of the infinitude.

---

# What Makes This Hard

The non-obvious move is the *reformulation*: recognising that "the induced filtration is stable" is the same statement as "$N^* = \bigoplus(N \cap \mathfrak{a}^n M)$ is a finitely generated $R^*$-module", which converts an infinite family of comparisons into one finiteness assertion. Most people get stuck trying to find the bound $c$ by hand, degree by degree, and never see that the Rees algebra packages it. The two facts that must be in place — *the Rees algebra is Noetherian* and *stable filtration $\iff$ finitely generated Rees module* — are the load-bearing lemmas, and the common error is to try to prove Artin–Rees directly without the Rees-algebra detour, which is possible but obscures why the uniform $c$ exists at all.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Translate the filtration question into a finite-generation question over the Rees algebra $R^* = \bigoplus \mathfrak{a}^n$. Show $R^*$ is Noetherian (it is generated in degree one over Noetherian $R$). Show the Rees module of a *stable* filtration is finitely generated, hence Noetherian, so its submodules — in particular the Rees module of the induced filtration on $N$ — are finitely generated. Translate finite generation back into stability.

**Subgoal decomposition:**

1. **The Rees algebra is Noetherian.** Show $R^* = \bigoplus_n \mathfrak{a}^n$ is Noetherian when $R$ is.
   - *Hint:* $\mathfrak{a} = (x_1, \dots, x_r)$ puts $R^* = R[x_1, \dots, x_r]$ generated in degree one; apply [[Thm - A Graded Ring is Noetherian iff Finitely Generated in Degree One|the graded criterion]] / [[Thm - Hilbert's Basis Theorem|Hilbert's basis theorem]].
   - *Why needed:* It makes $R^*$-modules Noetherian, the source of the uniform bound.

2. **Stable $\iff$ finitely generated Rees module.** Show: for finitely generated $M$ over Noetherian $R$, the $\mathfrak{a}$-filtration $(M_n)$ is stable $\iff$ $M^* = \bigoplus M_n$ is a finitely generated $R^*$-module.
   - *Hint:* Track the ascending chain of $R^*$-submodules $M_n^* = M_0 \oplus \cdots \oplus M_n \oplus \bigoplus_{i \geq 1}\mathfrak{a}^i M_n$; it stabilizes $\iff$ the filtration is stable, and $M^* = \bigcup M_n^*$.
   - *Why needed:* It is the dictionary between the analytic word "stable" and the algebraic word "finitely generated".

3. **The induced filtration on $N$ is an $\mathfrak{a}$-filtration, and its Rees module is a submodule.** Show $\mathfrak{a}(N \cap M_n) \subseteq N \cap M_{n+1}$, so $N^* = \bigoplus(N \cap M_n) \subseteq M^*$ is a graded $R^*$-submodule.
   - *Hint:* $\mathfrak{a}(N \cap M_n) \subseteq N$ and $\subseteq \mathfrak{a}M_n \subseteq M_{n+1}$.
   - *Why needed:* It places the object of interest inside the Noetherian module $M^*$.

4. **Conclude stability of the induced filtration.** Show $(N \cap M_n)$ is stable.
   - *Hint:* $M^*$ is finitely generated (step 2) over Noetherian $R^*$ (step 1), hence Noetherian; its submodule $N^*$ (step 3) is finitely generated; apply step 2 backwards to $N$.
   - *Why needed:* It is the theorem.

---

# Lemma Decomposition

> [!note]- Lemma 1: The Rees algebra is Noetherian
> **Statement:** If $R$ is Noetherian and $\mathfrak{a} \trianglelefteq R$, then the Rees algebra $R^* = \bigoplus_{n \geq 0} \mathfrak{a}^n$ is a Noetherian graded ring.
>
> **Hint:** Generators of $\mathfrak{a}$, placed in degree one, generate $R^*$ as an $R$-algebra; use the graded Noetherian criterion / Hilbert's basis theorem.
>
> **Why needed:** Noetherian-ness of $R^*$ is what makes finitely generated $R^*$-modules Noetherian, which is the source of the uniform stabilization bound $c$.
>
> > [!note]- Full proof
> > Since $R$ is Noetherian, $\mathfrak{a} = (x_1, \dots, x_r)$ is finitely generated. Place $x_i$ in the degree-one slot of $R^*$ (i.e. $x_i \in \mathfrak{a} = (R^*)_1$). Any element of $\mathfrak{a}^n$ is a sum of products $a_{i_1} \cdots a_{i_n}$ of $n$ elements of $\mathfrak{a}$, each a combination of the $x_j$; hence every degree-$n$ component of $R^*$ is an $R$-polynomial in $x_1, \dots, x_r$, so $R^* = R[x_1, \dots, x_r]$ is generated in degree one over $R^*_0 = R$. By [[Thm - A Graded Ring is Noetherian iff Finitely Generated in Degree One|the graded Noetherian criterion]] (equivalently, $R^*$ is a quotient of $R[T_1, \dots, T_r]$, Noetherian by [[Thm - Hilbert's Basis Theorem|Hilbert's basis theorem]]), $R^*$ is Noetherian.

> [!note]- Lemma 2: Stable filtration if and only if finitely generated Rees module
> **Statement:** Let $R$ be Noetherian, $M$ finitely generated, $(M_n)$ an $\mathfrak{a}$-filtration. Then $(M_n)$ is stable $\iff$ $M^* = \bigoplus_n M_n$ is a finitely generated $R^*$-module.
>
> **Hint:** Define $M_n^* = M_0 \oplus \cdots \oplus M_n \oplus \bigoplus_{i \geq 1}\mathfrak{a}^i M_n \subseteq M^*$; this ascending chain stabilizes iff the filtration is stable, and $M^* = \bigcup_n M_n^*$.
>
> **Why needed:** It is the dictionary translating "stable" $\leftrightarrow$ "finitely generated", used in both directions: forward to get $M^*$ finitely generated, backward to read stability off $N^*$.
>
> > [!note]- Full proof
> > Each $M_n$ is a finitely generated $R$-module ($M$ is Noetherian, being finitely generated over Noetherian $R$, so its submodules $M_n$ are finitely generated). Define the $R^*$-submodule
> > $$M_n^* = M_0 \oplus M_1 \oplus \cdots \oplus M_n \oplus \mathfrak{a}M_n \oplus \mathfrak{a}^2 M_n \oplus \cdots \subseteq M^*,$$
> > i.e. $M_n^*$ agrees with $M^*$ up to degree $n$ and is generated from $M_n$ above degree $n$. It is genuinely an $R^*$-submodule because $\mathfrak{a}^i \cdot \mathfrak{a}^j M_n = \mathfrak{a}^{i+j}M_n$. The chain $M_0^* \subseteq M_1^* \subseteq \cdots$ is ascending with union $\bigcup_n M_n^* = M^*$ (every $M_m$ appears in $M_m^*$).
> >
> > *Stable $\Rightarrow$ finitely generated.* If $\mathfrak{a}M_n = M_{n+1}$ for $n \geq n_0$, then $M_{n_0}^* = M^*$ (above degree $n_0$ both equal $\mathfrak{a}^{i}M_{n_0}$), so $M^* = M_{n_0}^*$ is generated as an $R^*$-module by $M_0 \oplus \cdots \oplus M_{n_0}$, a finitely generated $R$-module, hence finitely many elements generate $M^*$ over $R^*$.
> >
> > *Finitely generated $\Rightarrow$ stable.* If $M^*$ is finitely generated over $R^*$, then since $R^*$ is Noetherian (Lemma 1), $M^*$ is a Noetherian $R^*$-module, so the ascending chain $(M_n^*)$ stabilizes: $M_{n_0}^* = M_{n_0 + 1}^* = \cdots$. Comparing in degree $n_0 + 1$, $M_{n_0}^*$ has $\mathfrak{a}M_{n_0}$ while $M_{n_0+1}^*$ has $M_{n_0+1}$, and equality forces $\mathfrak{a}M_{n} = M_{n+1}$ for $n \geq n_0$; that is, $(M_n)$ is stable.

> [!note]- Lemma 3: The induced filtration sits inside the Rees module
> **Statement:** With $N \subseteq M$ a submodule and $(M_n)$ an $\mathfrak{a}$-filtration, $(N \cap M_n)$ is an $\mathfrak{a}$-filtration of $N$, and $N^* = \bigoplus_n (N \cap M_n)$ is a graded $R^*$-submodule of $M^* = \bigoplus_n M_n$.
>
> **Hint:** $\mathfrak{a}(N \cap M_n) \subseteq N \cap \mathfrak{a}M_n \subseteq N \cap M_{n+1}$.
>
> **Why needed:** It exhibits the object whose stability we want as a *submodule* of the Noetherian module $M^*$, so Noetherian-ness applies to it.
>
> > [!note]- Full proof
> > Each $N \cap M_n$ is a submodule of $N$, and $N \cap M_{n+1} \subseteq N \cap M_n$, so $(N \cap M_n)$ is a filtration of $N$ (with $N \cap M_0 = N \cap M = N$). It is an $\mathfrak{a}$-filtration: for $x \in N \cap M_n$ and $a \in \mathfrak{a}$, $ax \in N$ (as $N$ is a submodule) and $ax \in \mathfrak{a}M_n \subseteq M_{n+1}$, so $ax \in N \cap M_{n+1}$; hence $\mathfrak{a}(N \cap M_n) \subseteq N \cap M_{n+1}$. Therefore $N^* = \bigoplus_n (N \cap M_n)$ is closed under the $R^*$-action ($\mathfrak{a}^i \cdot (N \cap M_n) \subseteq N \cap M_{i+n}$ by iterating) and is a graded subgroup of $M^*$ with $N^* \subseteq M^*$ — a graded $R^*$-submodule.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $R$ be Noetherian, $\mathfrak{a} \trianglelefteq R$, $M$ finitely generated, $(M_n)$ a stable $\mathfrak{a}$-filtration, $N \subseteq M$.
>
> **Step 0 — the ambient graded ring is Noetherian.** By Lemma 1, the Rees algebra $R^* = \bigoplus_n \mathfrak{a}^n$ is a Noetherian graded ring.
>
> **Step 1 — the Rees module of $M$ is finitely generated.** The filtration $(M_n)$ is stable by hypothesis, so by Lemma 2 the Rees module $M^* = \bigoplus_n M_n$ is a finitely generated $R^*$-module. Since $R^*$ is Noetherian (Step 0), a finitely generated $R^*$-module is a Noetherian $R^*$-module; hence $M^*$ is Noetherian.
>
> **Step 2 — the induced filtration sits inside as a submodule.** By Lemma 3, $(N \cap M_n)$ is an $\mathfrak{a}$-filtration of $N$, and $N^* = \bigoplus_n (N \cap M_n)$ is an $R^*$-submodule of $M^*$.
>
> **Step 3 — finite generation of the submodule.** Because $M^*$ is a Noetherian $R^*$-module (Step 1), every submodule of $M^*$ is finitely generated; in particular $N^*$ is a finitely generated $R^*$-module.
>
> **Step 4 — translate back to stability.** By Lemma 2 applied to $N$ and its $\mathfrak{a}$-filtration $(N \cap M_n)$ (valid since $N$ is finitely generated over Noetherian $R$): $N^*$ finitely generated $\Rightarrow$ $(N \cap M_n)$ is a stable $\mathfrak{a}$-filtration of $N$.
>
> This proves the theorem.
>
> **Classical form.** Take $M_n = \mathfrak{a}^n M$ (stable with $n_0 = 0$). Stability of $(N \cap \mathfrak{a}^n M)$ gives $c \geq 0$ with $\mathfrak{a}(N \cap \mathfrak{a}^n M) = N \cap \mathfrak{a}^{n+1}M$ for $n \geq c$; iterating, $N \cap \mathfrak{a}^n M = \mathfrak{a}^{n-c}(N \cap \mathfrak{a}^c M)$ for $n \geq c$. Since $\mathfrak{a}^{n-c}(N \cap \mathfrak{a}^c M) \subseteq \mathfrak{a}^{n-c}N$, we get $\mathfrak{a}^n M \cap N \subseteq \mathfrak{a}^{n-c}N$ for $n \geq c$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Power-series and analytic germs.** In the ring $\mathcal{O}_{\mathbb{C}^n, 0}$ of convergent power series, with $\mathfrak{m}$ the maximal ideal of functions vanishing at $0$, Artin–Rees says the order of vanishing of a germ restricted to a subvariety is comparable (up to a bounded shift) to its intrinsic order. This is the algebraic backbone of why analytic continuation and Weierstrass-division estimates have uniform bounds on subvarieties. The application is non-obvious because it imports a purely algebraic finiteness into the analytic estimate.

**Numerical: $p$-adic congruences on a sublattice.** Take $R = \mathbb{Z}_p$, $\mathfrak{a} = (p)$, $M = \mathbb{Z}_p^k$, and $N$ a sublattice. Artin–Rees says: if a vector of $N$ is divisible by $p^n$ as an element of $M$, then it is divisible by $p^{n-c}$ as an element of $N$, for one fixed $c$. This is exactly the statement that a sublattice's $p$-adic topology is the subspace topology — used implicitly whenever one solves congruences on sublattices. The application is non-obvious because the "obvious" bound $c = 0$ is false, and Artin–Rees provides the correct uniform $c$.

**Symbolic powers and the uniform Artin–Rees property.** For an ideal $\mathfrak{a}$ and a prime $\mathfrak{p}$ in a Noetherian ring, comparing $\mathfrak{a}^n \cap \mathfrak{p}^{(m)}$ (symbolic powers) leads to *uniform* Artin–Rees theorems (Huneke), which control how badly symbolic and ordinary powers differ — the engine behind results like Ein–Lazarsfeld–Smith on symbolic-power containments. The application is non-obvious because it iterates Artin–Rees to get bounds independent of the ideals involved, a topic of active research in commutative algebra.

---

# Bridges

- **[[Thm - The Krull Intersection Theorem|The Krull Intersection Theorem]]** — the headline corollary. Applying Artin–Rees with $N = \bigcap_n \mathfrak{a}^n M$ inside a Noetherian local ring produces the single equation $N = \mathfrak{a}N$ that Nakayama needs; Nakayama then forces $N = 0$, i.e. $\bigcap_n \mathfrak{a}^n M = 0$. Artin–Rees is what turns an infinite intersection into a finite, Nakayama-ready statement.

- **[[Def - The Associated Graded Ring and the Rees Algebra|The Rees algebra]]** — the machine the proof runs on. The entire argument is "package the filtration into the Rees module over the Rees algebra, and use that the Rees algebra is Noetherian". The lemma is, in a sense, just the observation that submodules of Noetherian modules are finitely generated, transported through the Rees construction.

- **[[Thm - Stable Filtrations Induce the Same Topology|Stable filtrations induce the same topology]]** — the topological consequence. Artin–Rees says the induced filtration $(N \cap \mathfrak{a}^n M)$ is stable; that theorem says all stable $\mathfrak{a}$-filtrations of $N$ induce the *same* topology as the $\mathfrak{a}$-adic one. Composing the two gives that the subspace topology on $N$ (from $M$'s $\mathfrak{a}$-adic topology) equals $N$'s own $\mathfrak{a}$-adic topology — the [[Ex - The Artin-Rees lemma and the subspace topology|subspace-topology theorem]].

- **Exactness of completion** — the homological consequence. Completion $\hat{(\cdot)}$ is only left-exact in general; Artin–Rees is exactly the input that upgrades it to *exact* on short exact sequences of finitely generated modules over a Noetherian ring, by ensuring the filtration induced on a submodule is cofinal with its own. The link to the prior chapter on **the $\mathfrak{a}$-adic completion** runs through this.

# Unlocked by This

> [!tip] Faithful flatness of completion and the local criterion *(from Commutative Algebra X)*
> Artin–Rees is the technical heart behind two pillars of the completions chapter: that the $\mathfrak{a}$-adic **completion** $\hat{R}$ is **flat** over a Noetherian $R$, and that completion is **exact** on finitely generated modules. Both reduce to the statement that, for $N \subseteq M$ finitely generated, the completion $\hat{N}$ injects into $\hat{M}$ with the right image — which is guaranteed by the induced filtration on $N$ being cofinal with $N$'s $\mathfrak{a}$-adic filtration. Through this, Artin–Rees underwrites the comparison of a ring with its completion ($\hat{\mathbb{Z}_p}$, $k[[x]]$), the foundation of formal and rigid geometry.
