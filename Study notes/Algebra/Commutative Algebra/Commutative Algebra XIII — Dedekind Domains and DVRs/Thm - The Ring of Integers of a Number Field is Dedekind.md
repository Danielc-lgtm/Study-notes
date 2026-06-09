---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Dedekind Domain"
  - "Def - Integral Closure and Normal Domain"
  - "Def - Noetherian Ring"
  - "Def - Algebraic Integer and Minimal Polynomial"
  - "Def - Free Module"
  - "Def - Krull Dimension and Height"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. A **number field** $K$ is a finite extension of $\mathbb{Q}$, i.e. $[K : \mathbb{Q}] < \infty$. Its **ring of integers** is $\mathcal{O}_K = \{x \in K : x \text{ is integral over } \mathbb{Z}\}$, the [[Def - Integral Closure and Normal Domain|integral closure]] of $\mathbb{Z}$ in $K$ — equivalently the set of [[Def - Algebraic Integer and Minimal Polynomial|algebraic integers]] lying in $K$. We write $\operatorname{Frac}(\mathcal{O}_K) = K$, $\dim$ for [[Def - Krull Dimension and Height|Krull dimension]], and $\mathbb{Z}^n$ for the [[Def - Free Module|free $\mathbb{Z}$-module]] of rank $n$. The full registry is on [[Commutative Algebra XIII — Dedekind Domains and DVRs]].

---

# Statement

> **Theorem (rings of integers are Dedekind).** Let $K$ be a number field and $\mathcal{O}_K$ its ring of integers. Then $\mathcal{O}_K$ is a [[Def - Dedekind Domain|Dedekind domain]].

> **Supporting fact (non-examinable).** As a $\mathbb{Z}$-module, $\mathcal{O}_K$ is free of rank $[K : \mathbb{Q}]$: $\mathcal{O}_K \cong \mathbb{Z}^{[K:\mathbb{Q}]}$. This is the deepest input — it supplies the Noetherian property — and rests on the nondegeneracy of the trace form.

---

# Motivation

This is the theorem that puts number theory inside commutative algebra. The arithmetic of a number field $K$ — how primes factor, how units behave, how close the field is to having unique factorization — all takes place in its ring of integers $\mathcal{O}_K$, the natural generalization of $\mathbb{Z} \subseteq \mathbb{Q}$. But $\mathcal{O}_K$ can be a badly-behaved ring as far as element factorization goes: in $\mathbb{Z}[\sqrt{-5}] = \mathcal{O}_{\mathbb{Q}(\sqrt{-5})}$, numbers factor non-uniquely. The salvation, and the reason number theory works at all, is that $\mathcal{O}_K$ is always a *Dedekind domain*, so its *ideals* factor uniquely. This theorem is what guarantees that — it is the bridge that lets the entire machinery of the chapter (DVRs, unique factorization of ideals, the class group) be applied to every number field.

The content is a verification: $\mathcal{O}_K$ satisfies the three defining conditions of a Dedekind domain — Noetherian, integrally closed, dimension $1$. Each is established by a clean structural argument, and the three together are why $\mathcal{O}_K$ deserves to be called a "ring of integers": it is the unique maximal order, the integral closure of $\mathbb{Z}$ in $K$, behaving in every structural respect like $\mathbb{Z}$ does in $\mathbb{Q}$. The historical significance is hard to overstate — this is the theorem that vindicated Kummer's "ideal numbers" and turned them into Dedekind's ideals, founding algebraic number theory.

The proof also showcases the toolkit assembled over the previous chapters. Integral-closedness is automatic because an integral closure is, by transitivity of integrality, integrally closed. Dimension $1$ follows because $\mathbb{Z} \subseteq \mathcal{O}_K$ is an integral extension and integral extensions preserve dimension, so $\dim \mathcal{O}_K = \dim \mathbb{Z} = 1$. Noetherianity is the one nontrivial input: it comes from $\mathcal{O}_K$ being a finitely generated $\mathbb{Z}$-module (in fact free of rank $[K:\mathbb{Q}]$), hence a Noetherian $\mathbb{Z}$-module, hence — since its ideals are $\mathbb{Z}$-submodules — a Noetherian ring. Three earlier theorems, each doing one job.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$K$ is a number field and $A = \mathcal{O}_K$". The disguises are about recognizing rings that *are* (or contain) rings of integers.

The first disguised source is **a ring presented as $\mathbb{Z}[\alpha]$ for an algebraic integer $\alpha$**. The property $B$ is "$A = \mathbb{Z}[\alpha]$ with $\alpha$ an algebraic integer generating $K = \mathbb{Q}(\alpha)$". When $\mathbb{Z}[\alpha]$ happens to be integrally closed (e.g. $\alpha = i$, $\alpha = \sqrt{-5}$), it *equals* $\mathcal{O}_K$ and the theorem applies directly. The non-obvious caveat: $\mathbb{Z}[\alpha]$ is not always all of $\mathcal{O}_K$ — for $\alpha = \sqrt{-3}$ one must enlarge to $\mathbb{Z}[\tfrac{1+\sqrt{-3}}2]$ — so the bridge requires checking integral-closedness. *Example problem:* identify $\mathcal{O}_{\mathbb{Q}(i)} = \mathbb{Z}[i]$ and conclude it is Dedekind.

The second disguised source is **a quadratic or cyclotomic field**. The property $B$ is "$K = \mathbb{Q}(\sqrt{d})$ or $K = \mathbb{Q}(\zeta_n)$". For these, $\mathcal{O}_K$ has a known explicit form ($\mathbb{Z}[\sqrt{d}]$ or $\mathbb{Z}[\tfrac{1+\sqrt d}2]$ depending on $d \bmod 4$; $\mathbb{Z}[\zeta_n]$), and the theorem certifies it is Dedekind, switching on factorization. *Example problem:* factor $(2)$ in $\mathbb{Z}[\sqrt{-5}]$, which presupposes the ring is Dedekind.

The third disguised source is **the integral closure of a Dedekind domain in a finite extension**. The property $B$ is "$A$ is the integral closure of a Dedekind domain $R$ in a finite separable extension $L$ of $\operatorname{Frac}(R)$". By the same argument structure, $A$ is Dedekind (Remark 14.14 in the source). The non-obviousness: the theorem generalizes from $\mathbb{Z}$ to any Dedekind base, founding the theory of extensions of number fields and function fields. *Example problem:* the integral closure of $k[T]$ in a finite extension of $k(T)$ is Dedekind — a smooth affine curve.

**Targets (Output Amplification)**

The conclusion is "$\mathcal{O}_K$ is Dedekind".

Combine "Dedekind" with **[[Thm - A Dedekind Domain has Unique Factorization of Ideals|unique factorization of ideals]]**. The instant $\mathcal{O}_K$ is known Dedekind, every nonzero ideal factors uniquely into primes. The further result $E$: the entire arithmetic of $K$ — splitting of primes, ramification — becomes available. Nonobvious because a single structural theorem unlocks all of explicit number theory.

Combine "Dedekind" with **the class group machinery**. $\operatorname{Cl}(\mathcal{O}_K)$ is defined, and (by Minkowski's bound, beyond this chapter) finite. The further result $E$: the **class number** $h_K$ is a well-defined finite invariant, and $\mathcal{O}_K$ is a PID iff $h_K = 1$. Nonobvious because finiteness of the class group — a deep theorem — needs the Dedekind structure as its starting point.

Combine "Dedekind" with **the free-module structure $\mathcal{O}_K \cong \mathbb{Z}^n$**. An **integral basis** $\{\omega_1, \dots, \omega_n\}$ exists, and the **discriminant** $\operatorname{disc}(K)$ is computed from it. The further result $E$: the discriminant detects exactly which primes ramify, connecting the algebra to the geometry of the branched cover $\operatorname{Spec}\mathcal{O}_K \to \operatorname{Spec}\mathbb{Z}$. Nonobvious because a module-theoretic invariant controls ramification.

---

# Why Is It True

The intuition is that **$\mathcal{O}_K$ is built to be the maximal ring of "whole numbers" in $K$, and the three Dedekind axioms are each a different way of saying it has been built correctly — closed under the operations that should keep you integral, no bigger than $\mathbb{Z}$ in dimension, no holes left to fill.**

**The bolded mechanism:** **integral-closedness is free because an integral closure is closed (you cannot become integral over $\mathcal{O}_K$ without already being integral over $\mathbb{Z}$, by transitivity); dimension $1$ is free because being integral over $\mathbb{Z}$ cannot create new chains of primes (integrality preserves dimension); and the only real work is Noetherianity, which comes from $\mathcal{O}_K$ being squeezed inside a free $\mathbb{Z}$-module of finite rank.**

Take each axiom. *Integrally closed:* $\mathcal{O}_K$ is by definition the set of elements of $K$ integral over $\mathbb{Z}$. If $x \in K$ is integral over $\mathcal{O}_K$, then $x$ is integral over $\mathbb{Z}$ (an element integral over an integral extension is integral over the base — transitivity of integrality), so $x \in \mathcal{O}_K$. There is nothing to fill in: an integral closure is always integrally closed, by construction. This is the cleanest of the three.

*Dimension $1$:* the inclusion $\mathbb{Z} \subseteq \mathcal{O}_K$ is an integral extension (every element of $\mathcal{O}_K$ is integral over $\mathbb{Z}$ by definition). Integral extensions preserve Krull dimension — they cannot lengthen or shorten chains of primes, because lying-over and incomparability force the prime chains on both sides to have the same length. Since $\dim\mathbb{Z} = 1$, we get $\dim\mathcal{O}_K = 1$. Intuitively, $\mathcal{O}_K$ sits "directly above" $\mathbb{Z}$ with finite fibers, so it has the same number of "layers" of primes.

*Noetherian:* this is where the finiteness lives. The key input is that $\mathcal{O}_K$, as a $\mathbb{Z}$-module, is free of rank $n = [K:\mathbb{Q}]$ — it has an integral basis $\omega_1, \dots, \omega_n$ so that $\mathcal{O}_K = \mathbb{Z}\omega_1 \oplus \cdots \oplus \mathbb{Z}\omega_n \cong \mathbb{Z}^n$. A finitely generated module over the Noetherian ring $\mathbb{Z}$ is a Noetherian $\mathbb{Z}$-module, so every $\mathbb{Z}$-submodule of $\mathcal{O}_K$ is finitely generated. But the *ideals* of $\mathcal{O}_K$ are in particular $\mathbb{Z}$-submodules, hence finitely generated as $\mathbb{Z}$-modules, a fortiori finitely generated as $\mathcal{O}_K$-modules — so $\mathcal{O}_K$ is a Noetherian ring. The whole Noetherian property is inherited from $\mathbb{Z}$ through the finite free-module structure; this is "where the property comes from".

The three together are exactly the definition of a Dedekind domain, so $\mathcal{O}_K$ is one. The only genuinely deep ingredient is $\mathcal{O}_K \cong \mathbb{Z}^n$ — that the ring of integers is *finitely generated* over $\mathbb{Z}$ — and that rests on the trace form $K \times K \to \mathbb{Q}$ being nondegenerate, sandwiching $\mathcal{O}_K$ between two free modules of rank $n$.

---

# What Makes This Hard

The structural argument is short — three axioms, three earlier theorems — so the only real difficulty is the **non-examinable supporting fact $\mathcal{O}_K \cong \mathbb{Z}^{[K:\mathbb{Q}]}$**, i.e. that $\mathcal{O}_K$ is finitely generated as a $\mathbb{Z}$-module. This is where people get stuck, because it requires the trace pairing and the discriminant, not just integrality formalism. The non-obvious step is sandwiching $\mathcal{O}_K$ between two free $\mathbb{Z}$-modules of rank $n$ (one from a $\mathbb{Q}$-basis of $K$ inside $\mathcal{O}_K$, one from its trace-dual), using nondegeneracy of the trace form; then $\mathcal{O}_K$ is a submodule of a finitely generated free module over the PID $\mathbb{Z}$, hence free of the same rank. The common error is to assume $\mathcal{O}_K = \mathbb{Z}[\alpha]$ for a single $\alpha$ (true for $\mathbb{Q}(i)$ but false for $\mathbb{Q}(\sqrt{-3})$ and many others) — the integral basis need not be powers of one element.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Verify the three Dedekind axioms separately. Integral-closedness is automatic (an integral closure is integrally closed, by transitivity). Dimension $1$ follows from $\mathbb{Z} \subseteq \mathcal{O}_K$ integral plus "integrality preserves dimension". Noetherianity follows from $\mathcal{O}_K$ being a finitely generated (free) $\mathbb{Z}$-module, so its ideals are finitely generated $\mathbb{Z}$-submodules.

**Subgoal decomposition:**

1. **$\mathcal{O}_K$ is a domain with $\operatorname{Frac}(\mathcal{O}_K) = K$.**
   - *Hint:* It is a subring of the field $K$, hence a domain; and every $x \in K$ is $\tfrac{a_0 x}{a_0}$ with $a_0 x$ integral for a suitable $a_0 \in \mathbb{Z}$, so $K = \operatorname{Frac}(\mathcal{O}_K)$.
   - *Why needed:* It sets up the integral-closure and dimension arguments.

2. **$\mathcal{O}_K$ is integrally closed.**
   - *Hint:* If $x \in K$ is integral over $\mathcal{O}_K$, then by transitivity of integrality $x$ is integral over $\mathbb{Z}$, so $x \in \mathcal{O}_K$.
   - *Why needed:* It is Dedekind axiom (1).

3. **$\dim \mathcal{O}_K = 1$.**
   - *Hint:* $\mathbb{Z} \subseteq \mathcal{O}_K$ is integral; integral extensions preserve dimension; $\dim\mathbb{Z} = 1$.
   - *Why needed:* It is the dimension axiom.

4. **$\mathcal{O}_K$ is Noetherian.**
   - *Hint:* $\mathcal{O}_K \cong \mathbb{Z}^n$ (free of rank $n = [K:\mathbb{Q}]$), so it is a finitely generated, hence Noetherian, $\mathbb{Z}$-module; its ideals are $\mathbb{Z}$-submodules, hence finitely generated.
   - *Why needed:* It is the Noetherian axiom, the one nontrivial input.

---

# Lemma Decomposition

> [!note]- Lemma 1: $\mathcal{O}_K$ is a domain with fraction field $K$
> **Statement:** $\mathcal{O}_K$ is an integral domain and $\operatorname{Frac}(\mathcal{O}_K) = K$.
>
> **Hint:** Subring of a field is a domain; clear denominators to write any $x \in K$ as a ratio of integers.
>
> **Why needed:** It establishes the ambient field for integral-closedness and dimension.
>
> > [!note]- Full proof
> > $\mathcal{O}_K \subseteq K$ is a subring (sums and products of algebraic integers are algebraic integers), and $K$ is a field, so $\mathcal{O}_K$ is a domain. Clearly $\operatorname{Frac}(\mathcal{O}_K) \subseteq K$. Conversely, let $x \in K$. Since $[K:\mathbb{Q}] < \infty$, $x$ is algebraic over $\mathbb{Q}$, satisfying $a_0 x^n + a_1 x^{n-1} + \cdots + a_n = 0$ with $a_i \in \mathbb{Z}$, $a_0 \neq 0$. Multiplying by $a_0^{n-1}$ gives $(a_0 x)^n + a_1(a_0 x)^{n-1} + \cdots + a_n a_0^{n-1} = 0$, a monic equation for $a_0 x$ over $\mathbb{Z}$, so $a_0 x \in \mathcal{O}_K$. Then $x = \tfrac{a_0 x}{a_0} \in \operatorname{Frac}(\mathcal{O}_K)$ since $a_0 \in \mathbb{Z} \subseteq \mathcal{O}_K$. Hence $K = \operatorname{Frac}(\mathcal{O}_K)$.

> [!note]- Lemma 2: $\mathcal{O}_K$ is integrally closed
> **Statement:** $\mathcal{O}_K$ is integrally closed in $K = \operatorname{Frac}(\mathcal{O}_K)$.
>
> **Hint:** Transitivity of integrality: integral over an integral extension is integral over the base.
>
> **Why needed:** It is Dedekind axiom (1), free from the closure construction.
>
> > [!note]- Full proof
> > Let $x \in K$ be integral over $\mathcal{O}_K$. Every element of $\mathcal{O}_K$ is integral over $\mathbb{Z}$ by definition, so $\mathcal{O}_K$ is integral over $\mathbb{Z}$. By [[Thm - Characterizations of Integrality (Module-Finite Criterion)|transitivity of integrality]] (an element integral over a ring integral over $\mathbb{Z}$ is integral over $\mathbb{Z}$), $x$ is integral over $\mathbb{Z}$. Hence $x \in \mathcal{O}_K$ by definition of the integral closure. So $\mathcal{O}_K$ equals its integral closure in $K$.

> [!note]- Lemma 3: $\dim \mathcal{O}_K = 1$
> **Statement:** The Krull dimension of $\mathcal{O}_K$ is $1$.
>
> **Hint:** $\mathbb{Z} \subseteq \mathcal{O}_K$ is integral, and integral extensions preserve dimension.
>
> **Why needed:** It is the dimension axiom of a Dedekind domain.
>
> > [!note]- Full proof
> > The extension $\mathbb{Z} \subseteq \mathcal{O}_K$ is integral (every element of $\mathcal{O}_K$ is an algebraic integer, i.e. integral over $\mathbb{Z}$). For an integral extension, lying-over and incomparability give $\dim \mathcal{O}_K = \dim \mathbb{Z}$: a chain of primes in $\mathcal{O}_K$ contracts to a chain of the same length in $\mathbb{Z}$ (incomparability prevents collapse), and any chain in $\mathbb{Z}$ lifts (lying-over and going-up) to one of the same length in $\mathcal{O}_K$. Since $\dim\mathbb{Z} = 1$, we get $\dim\mathcal{O}_K = 1$. (Also $\mathcal{O}_K$ is not a field, since $\mathbb{Z}$ is not and integral extensions of non-fields by domains are non-fields here.)

> [!note]- Lemma 4: $\mathcal{O}_K$ is Noetherian
> **Statement:** $\mathcal{O}_K$ is a Noetherian ring.
>
> **Hint:** $\mathcal{O}_K \cong \mathbb{Z}^n$ as $\mathbb{Z}$-modules; ideals are $\mathbb{Z}$-submodules of a Noetherian $\mathbb{Z}$-module.
>
> **Why needed:** It is the Noetherian axiom, supplying the finiteness that makes factorization terminate.
>
> > [!note]- Full proof
> > By the supporting fact (non-examinable), $\mathcal{O}_K$ is a free $\mathbb{Z}$-module of rank $n = [K:\mathbb{Q}]$: $\mathcal{O}_K \cong \mathbb{Z}^n$. In particular $\mathcal{O}_K$ is a *finitely generated* $\mathbb{Z}$-module. Since $\mathbb{Z}$ is Noetherian, every finitely generated $\mathbb{Z}$-module is a Noetherian module — its $\mathbb{Z}$-submodules satisfy the ascending chain condition. Now let $\mathfrak{a}$ be an ideal of $\mathcal{O}_K$. It is in particular a $\mathbb{Z}$-submodule of $\mathcal{O}_K$, hence finitely generated as a $\mathbb{Z}$-module, a fortiori finitely generated as an $\mathcal{O}_K$-module. Since every ideal of $\mathcal{O}_K$ is finitely generated, $\mathcal{O}_K$ is a Noetherian ring.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $K$ be a number field, $n = [K:\mathbb{Q}]$, and $\mathcal{O}_K$ its ring of integers.
>
> ---
> **Step 0 — $\mathcal{O}_K$ is a domain with $\operatorname{Frac}(\mathcal{O}_K) = K$.** By Lemma 1, $\mathcal{O}_K$ is a subring of the field $K$, hence an integral domain, and clearing denominators shows $K = \operatorname{Frac}(\mathcal{O}_K)$.
>
> ---
> **Integrally closed.** By Lemma 2, any $x \in K$ integral over $\mathcal{O}_K$ is integral over $\mathbb{Z}$ (transitivity), hence in $\mathcal{O}_K$. So $\mathcal{O}_K$ is integrally closed in its fraction field — Dedekind condition (1).
>
> ---
> **Dimension $1$.** By Lemma 3, $\mathbb{Z} \subseteq \mathcal{O}_K$ is integral, integral extensions preserve dimension, and $\dim\mathbb{Z} = 1$, so $\dim\mathcal{O}_K = 1$.
>
> ---
> **Noetherian.** By Lemma 4, $\mathcal{O}_K \cong \mathbb{Z}^n$ is a finitely generated $\mathbb{Z}$-module, hence Noetherian as a $\mathbb{Z}$-module; every ideal of $\mathcal{O}_K$ is a $\mathbb{Z}$-submodule, hence finitely generated, so $\mathcal{O}_K$ is a Noetherian ring.
>
> ---
> $\mathcal{O}_K$ is a Noetherian, integrally closed domain of dimension $1$ — a Dedekind domain. $\blacksquare$
>
> *(The free-module fact $\mathcal{O}_K \cong \mathbb{Z}^n$ is proved via the nondegeneracy of the trace form: a $\mathbb{Q}$-basis of $K$ scaled into $\mathcal{O}_K$ gives a free submodule $M \subseteq \mathcal{O}_K$ of rank $n$, and the trace-dual $M^* \supseteq \mathcal{O}_K$ is also free of rank $n$; $\mathcal{O}_K$ is sandwiched between two rank-$n$ free $\mathbb{Z}$-modules, hence free of rank $n$ over the PID $\mathbb{Z}$.)*

---

# Cross-Field Exercise Suggestions

**The Gaussian integers (number theory).** $\mathcal{O}_{\mathbb{Q}(i)} = \mathbb{Z}[i]$, the [[Def - Gaussian Integers|Gaussian integers]], is Dedekind by this theorem — and in fact a PID. The application: the factorization of a rational prime $p$ in $\mathbb{Z}[i]$ (split if $p \equiv 1 \bmod 4$, ramified if $p = 2$, inert if $p \equiv 3 \bmod 4$) is the ideal-theoretic content of Fermat's two-squares theorem. The nonobvious link: a classical Diophantine result is a statement about prime splitting in a Dedekind domain.

**Cyclotomic fields and Fermat's Last Theorem (number theory).** $\mathcal{O}_{\mathbb{Q}(\zeta_p)} = \mathbb{Z}[\zeta_p]$ is Dedekind, the setting of Kummer's attack on Fermat's Last Theorem. The application: Kummer proved FLT for **regular primes** $p$ (those with $p \nmid h_{\mathbb{Q}(\zeta_p)}$) precisely by exploiting unique factorization of *ideals* in this Dedekind domain, sidestepping the failure of element factorization. This theorem is what makes the ideal arithmetic legitimate.

**Function fields and curves (algebraic geometry).** The analogue replaces $\mathbb{Z}$ by $k[T]$: the integral closure of $k[T]$ in a finite extension of $k(T)$ is a Dedekind domain, the coordinate ring of a **smooth affine curve** covering the line. The application: the geometry of branched covers of curves — ramification, the Riemann–Hurwitz formula — is the exact analogue of prime splitting in number fields, and both are governed by the Dedekind structure this theorem provides.

---

# Bridges

- **[[Def - Dedekind Domain|Dedekind domain]]** — this theorem is the principal *source of examples* of Dedekind domains, and the reason the abstract definition matters. Without it, Dedekind domains might seem an arbitrary axiomatic class; with it, every number field supplies one, and the whole chapter's machinery descends on number theory.

- **[[Thm - Characterizations of Integrality (Module-Finite Criterion)|Transitivity and finiteness of integrality]]** — two of the three axioms run on integrality formalism: integral-closedness is "integral over an integral extension is integral over the base", and dimension $1$ uses "integral extensions preserve dimension". The finiteness side (module-finite criterion) underlies the free-module fact that gives Noetherianity.

- **[[Thm - Rational Algebraic Integers are Integers|Rational algebraic integers are integers]]** — the special case $K = \mathbb{Q}$, where $\mathcal{O}_{\mathbb{Q}} = \mathbb{Z}$: a rational number integral over $\mathbb{Z}$ is in $\mathbb{Z}$. This is integral-closedness of $\mathbb{Z}$, the base case from which the general theorem ascends, and the reason $\mathbb{Z}$ itself is the prototype Dedekind domain.

- **[[Thm - A Dedekind Domain has Unique Factorization of Ideals|Unique factorization of ideals]]** — this theorem is the *hypothesis* that lets unique factorization apply to $\mathcal{O}_K$. Together they are the foundation of algebraic number theory: $\mathcal{O}_K$ is Dedekind (here), so its ideals factor uniquely (there), so the arithmetic of $K$ is governed by prime ideals.

---

# Unlocked by This

> [!tip] Splitting of primes, the decomposition group, and Frobenius *(from Algebraic Number Theory)*
> Once $\mathcal{O}_K$ is Dedekind, a rational prime extends as $(p)\mathcal{O}_K = \prod \mathfrak{p}_i^{e_i}$, and the study of how this factorization depends on $K$ is the core of algebraic number theory: the **decomposition** and **inertia groups**, the **Frobenius element**, and ultimately **class field theory**, which describes abelian extensions of $K$ in terms of the arithmetic of $\mathcal{O}_K$. The discriminant of $K$ pinpoints the ramified primes. All of this presupposes the Dedekind structure established here.

> [!tip] The Minkowski bound and finiteness of the class group *(from Algebraic Number Theory)*
> The free-module structure $\mathcal{O}_K \cong \mathbb{Z}^n$ embeds $\mathcal{O}_K$ as a **lattice** in $\mathbb{R}^{r_1}\times\mathbb{C}^{r_2}$, and Minkowski's geometry of numbers then bounds the norms of ideal-class representatives, proving the **class group is finite**. The **class number** $h_K$, the **regulator**, and the **class number formula** (relating them to the Dedekind zeta function) are the deep invariants this finiteness opens up — and the lattice structure is exactly the $\mathbb{Z}^n$ from this theorem's supporting fact.
