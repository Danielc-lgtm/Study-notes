---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Noetherian Ring"
  - "Def - Ideal"
  - "Def - Module"
  - "Def - Finitely Generated Module"
  - "Def - Prime and Maximal Ideal"
  - "Thm - The Artin-Rees Lemma"
  - "Thm - Nakayama's Lemma"
  - "Def - The Jacobson Radical"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $R$ be a [[Def - Noetherian Ring|Noetherian ring]], $\mathfrak{a} \trianglelefteq R$ an [[Def - Ideal|ideal]], and $M$ a [[Def - Finitely Generated Module|finitely generated]] $R$-module. We write $\bigcap_n \mathfrak{a}^n M = \bigcap_{n \geq 0} \mathfrak{a}^n M$ for the **stable submodule** (the elements infinitely divisible by $\mathfrak{a}$). A local ring $(R, \mathfrak{m})$ is one with a unique [[Def - Prime and Maximal Ideal|maximal ideal]] $\mathfrak{m}$; its [[Def - The Jacobson Radical|Jacobson radical]] $\operatorname{Jac}(R)$ is the intersection of all maximal ideals, equal to $\mathfrak{m}$ in the local case. The full registry is on [[Commutative Algebra XI — Graded Rings and the Artin-Rees Lemma]].

---

# Statement

> **Theorem (Krull Intersection Theorem).** Let $R$ be a Noetherian ring, $\mathfrak{a} \trianglelefteq R$ an ideal, and $M$ a finitely generated $R$-module. Set $N = \bigcap_{n \geq 0} \mathfrak{a}^n M$. Then
> $$\mathfrak{a}N = N,$$
> and consequently there exists $a \in \mathfrak{a}$ with $(1 + a)N = 0$. In particular:
>
> 1. If $\mathfrak{a} \subseteq \operatorname{Jac}(R)$ (for instance if $(R, \mathfrak{m})$ is local and $\mathfrak{a} \subseteq \mathfrak{m}$), then $\bigcap_{n} \mathfrak{a}^n M = 0$.
> 2. If $R$ is a Noetherian integral domain and $\mathfrak{a} \neq R$ a proper ideal, then $\bigcap_n \mathfrak{a}^n = 0$.

The two headline cases are worth stating separately:

> **Corollary (local case).** In a Noetherian local ring $(R, \mathfrak{m})$, $\bigcap_n \mathfrak{m}^n = 0$, and more generally $\bigcap_n \mathfrak{m}^n M = 0$ for every finitely generated $M$.

The general statement gives $\mathfrak{a}N = N$; the corollaries are what you get by feeding that to Nakayama under the extra hypothesis $\mathfrak{a} \subseteq \operatorname{Jac}(R)$.

---

# Motivation

The theorem answers the question "are there elements infinitely divisible by an ideal?" In $\mathbb{Z}$, no nonzero integer is divisible by $p^n$ for all $n$ — the powers $p^n\mathbb{Z}$ shrink down to $\{0\}$, because $|x| \geq p^n$ would have to hold for all $n$. Krull's theorem is the vast generalization: in any Noetherian local ring, the powers of the maximal ideal also shrink to zero, $\bigcap_n \mathfrak{m}^n = 0$. There is no "infinitely small but nonzero" element. Equivalently, every nonzero element has a *finite* order of vanishing: there is a largest $n$ with $x \in \mathfrak{m}^n$.

This is exactly the statement that makes the $\mathfrak{a}$-adic topology *separated* (Hausdorff). Recall the $\mathfrak{a}$-adic filtration gives $M$ a topology with the $\mathfrak{a}^n M$ as neighbourhoods of $0$; a sequence converges to $0$ iff it eventually enters every $\mathfrak{a}^n M$. The intersection $\bigcap_n \mathfrak{a}^n M$ is precisely the set of points that are "topologically indistinguishable from $0$" — points the topology cannot separate from $0$. The theorem says (under $\mathfrak{a} \subseteq \operatorname{Jac}(R)$) this set is just $\{0\}$, so the topology is Hausdorff and the completion map $M \to \hat{M} = \varprojlim M/\mathfrak{a}^n M$ is *injective*. Without Krull intersection, completion could lose information — distinct elements could complete to the same thing. The theorem is the guarantee that completion is faithful: you can recover $M$'s elements from their sequences of approximations.

Geometrically, in the coordinate ring of a variety localized at a point, $\bigcap_n \mathfrak{m}^n = 0$ says that a function vanishing to infinite order at a point (vanishing in $\mathfrak{m}^n$ for all $n$) must be the zero function — there are no nonzero "flat" functions in the algebraic category, in sharp contrast to the $C^\infty$ world where $e^{-1/x^2}$ vanishes to infinite order without being zero. Algebraic functions are rigid: their Taylor series determines them. Krull's theorem is the algebraic incarnation of that rigidity.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$R$ Noetherian, $M$ finitely generated, and $\mathfrak{a} \subseteq \operatorname{Jac}(R)$ for the vanishing conclusion".

The first disguised source is **a Noetherian local ring $(R, \mathfrak{m})$**. Here $\operatorname{Jac}(R) = \mathfrak{m}$, so *any* ideal $\mathfrak{a} \subseteq \mathfrak{m}$ — that is, any proper ideal — satisfies the hypothesis automatically. The bridge $B \to A$: "local" is the cleanest way to guarantee $\mathfrak{a} \subseteq \operatorname{Jac}(R)$, because in a local ring the Jacobson radical *is* the maximal ideal and contains every proper ideal. *Example problem:* show that in a Noetherian local ring, the completion map is injective (see [[Ex - Krull intersection for a Noetherian local ring]]).

The second disguised source is **a Noetherian integral domain with a proper ideal**. The Jacobson radical may not contain $\mathfrak{a}$, so the local argument does not apply directly; instead use $\mathfrak{a}N = N$ to get $(1+a)N = 0$ with $a \in \mathfrak{a}$, then note $1 + a \neq 0$ (else $-1 = a \in \mathfrak{a}$, contradicting $\mathfrak{a}$ proper), so in a domain $1 + a$ is a nonzerodivisor and $N = 0$. The bridge: "domain + proper ideal" lets you cancel $1 + a$ even without the local hypothesis. *Example problem:* show $\bigcap_n \mathfrak{a}^n = 0$ in $\mathbb{Z}$ or $k[x_1, \dots, x_d]$ for any proper $\mathfrak{a}$.

The third disguised source is **the kernel of a completion map**. Whenever you must show a completion map $M \to \hat{M}$ is injective, the kernel is $\bigcap_n \mathfrak{a}^n M$ by definition of the inverse limit, so the hidden hypothesis is precisely Krull intersection. The bridge: "completion is injective" *is* "$\bigcap_n \mathfrak{a}^n M = 0$" verbatim. *Example problem:* prove the $\mathfrak{a}$-adic completion is separated (injective on f.g. modules over Noetherian local rings).

**Targets (Output Amplification)**

The conclusion $C$ is $\mathfrak{a}N = N$ (general) or $\bigcap_n \mathfrak{a}^n M = 0$ (with $\mathfrak{a} \subseteq \operatorname{Jac}(R)$).

Combine $C$ with **the inverse-limit description of completion**. The kernel of $M \to \hat{M} = \varprojlim M/\mathfrak{a}^n M$ is $\bigcap_n \mathfrak{a}^n M = 0$. The further result $E$: the completion map is **injective**, so $M$ embeds in its completion, and the $\mathfrak{a}$-adic topology is Hausdorff. This is non-obvious because separatedness of a topology is being deduced from a finiteness theorem about powers of an ideal.

Combine $C$ with **regularity / order functions**. If $\bigcap_n \mathfrak{m}^n = 0$, then every nonzero $x \in R$ has a well-defined finite **order** $\nu(x) = \max\{n : x \in \mathfrak{m}^n\}$, and the leading form of $x$ in $\operatorname{gr}_{\mathfrak{m}}(R)$ is nonzero. The further result $E$: the map $R \setminus \{0\} \to \operatorname{gr}_{\mathfrak{m}}(R)$, $x \mapsto$ its leading form, is well-defined and injective on initial forms — the foundation of the theory of standard bases / Gröbner bases in local rings. Non-obvious because it turns a vanishing theorem into a *positivity* (nonzero leading form) statement.

Combine $C$ with **the structure of the associated graded ring**. $\bigcap_n \mathfrak{m}^n = 0$ implies $\operatorname{gr}_{\mathfrak{m}}(R)$ "sees" all of $R$ — no nonzero element is invisible to the layers. The further result $E$: dimension and multiplicity computed from $\operatorname{gr}_{\mathfrak{m}}(R)$ genuinely reflect $R$; in particular $\dim R = \dim \operatorname{gr}_{\mathfrak{m}}(R)$. Non-obvious because it licenses transferring dimension from $R$ to the simpler graded ring — the strategy of all of dimension theory.

---

# Why Is It True

The shape of the argument is "Artin–Rees converts an infinite intersection into a single equation, then Nakayama finishes". Strip away the technology and the idea is this: the intersection $N = \bigcap_n \mathfrak{a}^n M$ is, by definition, *as deep as you like* in the $\mathfrak{a}$-adic filtration of $M$ — it lies in every $\mathfrak{a}^n M$. So when you intersect $N$ with the filtration of $M$, nothing is lost: $N \cap \mathfrak{a}^n M = N$ for every $n$. Artin–Rees says the induced filtration $(N \cap \mathfrak{a}^n M)$ is *stable*, which in particular means $N \cap \mathfrak{a}^{n+1}M = \mathfrak{a}(N \cap \mathfrak{a}^n M)$ for $n$ large. Substituting $N \cap \mathfrak{a}^k M = N$ on both sides gives the punchline equation
$$N = \mathfrak{a}N.$$
That is the whole structural content: **a submodule that is infinitely $\mathfrak{a}$-divisible must equal $\mathfrak{a}$ times itself, because Artin–Rees forbids the filtration on it from being strictly finer than the $\mathfrak{a}$-adic one.**

Now Nakayama. The equation $N = \mathfrak{a}N$ says $N$ is "all multiples of $\mathfrak{a}$" — a finitely generated module equal to $\mathfrak{a}$ times itself. [[Thm - Nakayama's Lemma|Nakayama's lemma]] is precisely the statement that this is impossible unless $N = 0$, *provided* $\mathfrak{a}$ lies in the Jacobson radical (so that $1 + a$ is a unit for $a \in \mathfrak{a}$). The determinant trick gives an element $a \in \mathfrak{a}$ with $(1 + a)N = 0$; if $\mathfrak{a} \subseteq \operatorname{Jac}(R)$ then $1 + a$ is a unit, so $N = 0$. In a domain you do not even need the radical hypothesis: $1 + a \neq 0$ (else $\mathfrak{a} \ni a = -1$ would be improper) is automatically a nonzerodivisor, so $N = 0$ again.

The reason it is unsurprising in hindsight: "infinitely divisible by $\mathfrak{a}$" forces "fixed by multiplication by $\mathfrak{a}$" (that is Artin–Rees), and "fixed by multiplication by an ideal in the radical" forces "zero" (that is Nakayama). The two lemmas are exactly the two halves of the implication, and each is doing the minimum.

**The one-line mechanism: Artin–Rees gives $N = \mathfrak{a}N$, Nakayama gives $N = 0$.**

---

# What Makes This Hard

The non-obvious step is the *first* one: recognising that $N \cap \mathfrak{a}^n M = N$ (because $N$ is contained in every $\mathfrak{a}^n M$ by definition), so that Artin–Rees's stability statement collapses to $N = \mathfrak{a}N$. People expect to need a hands-on argument and miss that Artin–Rees does it in one substitution. The most common error is to forget the hypothesis $\mathfrak{a} \subseteq \operatorname{Jac}(R)$ and claim $\bigcap_n \mathfrak{a}^n M = 0$ unconditionally — it is false: in $R = \mathbb{Z}$ with $\mathfrak{a} = R$, or in a non-local ring where $\mathfrak{a}$ contains a unit's complement, the intersection need not vanish (e.g. $\mathfrak{a} = (e)$ for an idempotent $e \neq 0, 1$ has $\mathfrak{a}^n = \mathfrak{a}$ for all $n$, so $\bigcap_n \mathfrak{a}^n = (e) \neq 0$). The Jacobson-radical (or domain) hypothesis is exactly what Nakayama needs, and dropping it breaks the theorem.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Let $N = \bigcap_n \mathfrak{a}^n M$. Observe $N \subseteq \mathfrak{a}^n M$ for all $n$, so the induced filtration on $N$ is constant: $N \cap \mathfrak{a}^n M = N$. Apply Artin–Rees to learn the induced filtration is stable, hence $N = \mathfrak{a}N$ for large indices. Apply Nakayama (using $\mathfrak{a} \subseteq \operatorname{Jac}(R)$, or domain) to conclude $N = 0$.

**Subgoal decomposition:**

1. **The induced filtration on $N$ is constant.** Show $N \cap \mathfrak{a}^n M = N$ for all $n$.
   - *Hint:* $N = \bigcap_k \mathfrak{a}^k M \subseteq \mathfrak{a}^n M$ for each fixed $n$.
   - *Why needed:* It is what makes the stability equation collapse to $N = \mathfrak{a}N$.

2. **$N = \mathfrak{a}N$.** Show the stable submodule is fixed by $\mathfrak{a}$.
   - *Hint:* [[Thm - The Artin-Rees Lemma|Artin–Rees]]: $(N \cap \mathfrak{a}^n M)$ is stable, so $N \cap \mathfrak{a}^{n+1}M = \mathfrak{a}(N \cap \mathfrak{a}^n M)$ for $n \gg 0$; substitute step 1.
   - *Why needed:* It is the single equation Nakayama consumes.

3. **$N = 0$ under the radical/domain hypothesis.** Conclude.
   - *Hint:* [[Thm - Nakayama's Lemma|Nakayama]] gives $a \in \mathfrak{a}$ with $(1+a)N = 0$; if $\mathfrak{a} \subseteq \operatorname{Jac}(R)$ then $1+a$ is a unit; if $R$ is a domain and $\mathfrak{a}$ proper then $1 + a \neq 0$ is a nonzerodivisor.
   - *Why needed:* It is the conclusion $\bigcap_n \mathfrak{a}^n M = 0$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The stable submodule is constant under the induced filtration
> **Statement:** Let $N = \bigcap_{k \geq 0} \mathfrak{a}^k M$. Then $N \cap \mathfrak{a}^n M = N$ for every $n \geq 0$.
>
> **Hint:** $N$ is contained in each individual $\mathfrak{a}^n M$ by definition of the intersection.
>
> **Why needed:** It is the substitution that turns the stability equation of Artin–Rees into $N = \mathfrak{a}N$.
>
> > [!note]- Full proof
> > By definition $N = \bigcap_{k \geq 0} \mathfrak{a}^k M$, so for any fixed $n$, $N \subseteq \mathfrak{a}^n M$. Hence $N \cap \mathfrak{a}^n M = N$ (intersecting a set with a superset of it returns the set). The induced filtration $(N \cap \mathfrak{a}^n M)_n$ is therefore the constant filtration $N, N, N, \dots$.

> [!note]- Lemma 2: Artin–Rees forces $N = \mathfrak{a}N$
> **Statement:** With $N = \bigcap_n \mathfrak{a}^n M$, $R$ Noetherian, $M$ finitely generated, one has $\mathfrak{a}N = N$.
>
> **Hint:** Apply [[Thm - The Artin-Rees Lemma|Artin–Rees]] to the $\mathfrak{a}$-adic filtration of $M$ and the submodule $N$, then use Lemma 1.
>
> **Why needed:** It produces the one equation Nakayama needs, out of the infinite intersection.
>
> > [!note]- Full proof
> > The $\mathfrak{a}$-adic filtration $M_n = \mathfrak{a}^n M$ is a stable $\mathfrak{a}$-filtration of the finitely generated module $M$ over the Noetherian ring $R$. By the [[Thm - The Artin-Rees Lemma|Artin–Rees Lemma]], the induced filtration $(N \cap \mathfrak{a}^n M)_n$ on $N$ is stable, so there is $c$ with
> > $$N \cap \mathfrak{a}^{n+1}M = \mathfrak{a}\,(N \cap \mathfrak{a}^n M) \qquad (n \geq c).$$
> > By Lemma 1 both intersections equal $N$: the left side is $N \cap \mathfrak{a}^{n+1}M = N$ and the right side is $\mathfrak{a}(N \cap \mathfrak{a}^n M) = \mathfrak{a}N$. Hence $N = \mathfrak{a}N$. (One inclusion $\mathfrak{a}N \subseteq N$ is automatic; Artin–Rees supplies the reverse.)

> [!note]- Lemma 3: Nakayama closes the argument
> **Statement:** If $N$ is a finitely generated $R$-module with $\mathfrak{a}N = N$, then there is $a \in \mathfrak{a}$ with $(1 + a)N = 0$. Consequently $N = 0$ if either $\mathfrak{a} \subseteq \operatorname{Jac}(R)$ or ($R$ a domain and $\mathfrak{a} \neq R$).
>
> **Hint:** The determinant trick / [[Thm - Nakayama's Lemma|Nakayama]] gives $(1+a)N = 0$; then make $1 + a$ a unit or a nonzerodivisor.
>
> **Why needed:** It converts the fixed-point equation $\mathfrak{a}N = N$ into vanishing — the conclusion of the theorem.
>
> > [!note]- Full proof
> > $N$ is finitely generated ($N \subseteq M$, $M$ finitely generated over Noetherian $R$, so $N$ is too). Since $\mathfrak{a}N = N$, the [[Thm - Nakayama's Lemma|determinant trick]] gives an element $a \in \mathfrak{a}$ with $(1 + a)x = 0$ for all $x \in N$, i.e. $(1+a)N = 0$.
> >
> > *If $\mathfrak{a} \subseteq \operatorname{Jac}(R)$:* then $a \in \operatorname{Jac}(R)$, so $1 + a$ is a unit (a defining property of the Jacobson radical: $1 + r$ is a unit for every $r \in \operatorname{Jac}(R)$). Multiplying $(1+a)N = 0$ by $(1+a)^{-1}$ gives $N = 0$.
> >
> > *If $R$ is a domain and $\mathfrak{a} \neq R$:* then $1 + a \neq 0$ — otherwise $a = -1 \in \mathfrak{a}$ would make $\mathfrak{a} = R$. In a domain a nonzero element is a nonzerodivisor, so $(1+a)x = 0$ forces $x = 0$ for each $x \in N$; hence $N = 0$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $R$ be Noetherian, $\mathfrak{a} \trianglelefteq R$, $M$ finitely generated, and $N = \bigcap_{n \geq 0} \mathfrak{a}^n M$.
>
> **Step 0 — $N$ is finitely generated.** $N$ is a submodule of $M$, and $M$ is a Noetherian $R$-module (finitely generated over the Noetherian ring $R$), so $N$ is finitely generated. This is what licenses Nakayama below.
>
> **Step 1 — the induced filtration on $N$ is constant.** For each $n$, $N \subseteq \mathfrak{a}^n M$, so $N \cap \mathfrak{a}^n M = N$ (Lemma 1).
>
> **Step 2 — $\mathfrak{a}N = N$.** The $\mathfrak{a}$-adic filtration $(\mathfrak{a}^n M)$ is a stable $\mathfrak{a}$-filtration of $M$. By the [[Thm - The Artin-Rees Lemma|Artin–Rees Lemma]], the induced filtration $(N \cap \mathfrak{a}^n M)$ is stable: there is $c$ with $N \cap \mathfrak{a}^{n+1}M = \mathfrak{a}(N \cap \mathfrak{a}^n M)$ for all $n \geq c$. Using Step 1, the left side is $N$ and the right side is $\mathfrak{a}N$, so $\mathfrak{a}N = N$ (Lemma 2).
>
> **Step 3 — conclude.** By [[Thm - Nakayama's Lemma|Nakayama's lemma]] applied to the finitely generated module $N$ with $\mathfrak{a}N = N$, there is $a \in \mathfrak{a}$ with $(1 + a)N = 0$ (Lemma 3). This is the general statement.
> - If $\mathfrak{a} \subseteq \operatorname{Jac}(R)$ — in particular if $(R, \mathfrak{m})$ is local and $\mathfrak{a} \subseteq \mathfrak{m}$ — then $1 + a$ is a unit, so $N = 0$, i.e. $\bigcap_n \mathfrak{a}^n M = 0$.
> - If $R$ is a Noetherian domain and $\mathfrak{a} \neq R$, then $1 + a \neq 0$ is a nonzerodivisor, so $N = 0$, i.e. $\bigcap_n \mathfrak{a}^n = 0$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**$p$-adic and power-series rigidity.** In $\mathbb{Z}_p$ (or $k[[x]]$) the theorem reads $\bigcap_n p^n\mathbb{Z}_p = 0$ ($\bigcap_n x^n k[[x]] = 0$): a $p$-adic integer (power series) divisible by every power of $p$ ($x$) is zero. This is what makes the $p$-adic valuation finite on nonzero elements and is the bedrock of $p$-adic analysis. The application is non-obvious because it certifies that the completed objects, where one most fears "infinitely small" elements, are nonetheless separated.

**No flat functions in the algebraic category.** For $R = k[x_1, \dots, x_d]$ localized at the origin $\mathfrak{m}$, $\bigcap_n \mathfrak{m}^n = 0$ says no nonzero polynomial vanishes to infinite order at $0$ — sharply unlike the smooth category, where $e^{-1/x^2}$ does. The application is non-obvious because it isolates a structural difference between algebraic and $C^\infty$ geometry: algebraic functions are determined by their (finite-data) jets, smooth ones are not.

**Stabilization of descending chains of "deep" submodules.** Given a Noetherian local ring and a finitely generated module, the descending chain $M \supseteq \mathfrak{m}M \supseteq \mathfrak{m}^2 M \supseteq \cdots$ has trivial intersection, so for any nonzero $x \in M$ there is a *finite* depth $\nu(x) = \max\{n : x \in \mathfrak{m}^n M\}$, making $\nu$ a well-defined order function. The application is non-obvious because this finiteness is what allows induction "on the order of vanishing", a workhorse in local algebra and singularity theory.

---

# Bridges

- **[[Thm - The Artin-Rees Lemma|The Artin–Rees Lemma]]** — the first half of the proof. Artin–Rees, applied to the $\mathfrak{a}$-adic filtration and the submodule $N = \bigcap_n \mathfrak{a}^n M$, yields the single equation $\mathfrak{a}N = N$ by collapsing the stability statement using $N \cap \mathfrak{a}^n M = N$. Without Artin–Rees one has no way to convert "infinitely divisible" into a finite, Nakayama-ready equation.

- **[[Thm - Nakayama's Lemma|Nakayama's Lemma]]** — the second half. Nakayama says a finitely generated module fixed by an ideal in the Jacobson radical is zero. The hypothesis $\mathfrak{a} \subseteq \operatorname{Jac}(R)$ in Krull's theorem is exactly Nakayama's hypothesis, and the conclusion $N = 0$ is Nakayama's conclusion; Krull intersection is the composite of Artin–Rees and Nakayama.

- **The $\mathfrak{a}$-adic completion** — the consequence. The kernel of the completion map $M \to \hat{M} = \varprojlim M/\mathfrak{a}^n M$ is exactly $\bigcap_n \mathfrak{a}^n M$, so Krull intersection is the statement that completion is *injective* on finitely generated modules over Noetherian local rings — the separatedness that makes the completion faithful. This is the through-line to the prior chapter on **completions and limits**.

- **[[Def - The Associated Graded Ring and the Rees Algebra|The associated graded ring]]** — the structural beneficiary. $\bigcap_n \mathfrak{m}^n = 0$ means every nonzero element has a nonzero leading form in $\operatorname{gr}_{\mathfrak{m}}(R)$, so the passage $R \rightsquigarrow \operatorname{gr}_{\mathfrak{m}}(R)$ loses no element — the basis for transferring dimension and multiplicity from $R$ to its tangent cone.

# Unlocked by This

> [!tip] Separatedness and the faithfulness of completion *(from Commutative Algebra X)*
> Krull intersection is the theorem that makes the **$\mathfrak{a}$-adic topology** Hausdorff and the **completion** $M \to \hat{M}$ injective on finitely generated modules over a Noetherian local ring. Concretely it says the kernel $\bigcap_n \mathfrak{a}^n M$ of the completion map vanishes, so no information is lost in passing to the completion: $\mathbb{Z}$ embeds in $\hat{\mathbb{Z}}_p$, $k[x]_{(x)}$ embeds in $k[[x]]$, and a function is determined by its formal Taylor series. This faithfulness is the licence for the entire technique of "complete, solve in the completion (where Hensel's lemma and the structure theorems live), and descend" — the engine of the Cohen structure theorem and of much of modern local algebra and arithmetic geometry.
