---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Ring"
  - "Def - Ideal"
  - "Def - Noetherian Ring"
  - "Def - Polynomial Ring"
  - "Def - Algebra over a Ring (R-algebra)"
  - "Def - Finitely Generated Algebra"
  - "Thm - Hilbert's Basis Theorem"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $R$ be a ring; $R[T]$ is the [[Def - Polynomial Ring|polynomial ring]] in one variable, $R[T_1, \dots, T_n]$ in $n$ variables. For an [[Def - Ideal|ideal]] $\mathfrak{a} \trianglelefteq R[T]$ and $i \geq 0$, write
$$\mathfrak{a}(i) = \{\,c \in R : c T^i + (\text{lower-degree terms}) \in \mathfrak{a}\,\} \cup \{0\}$$
for the set of **leading coefficients** of the degree-$i$ elements of $\mathfrak{a}$ (together with $0$); each $\mathfrak{a}(i)$ is an ideal of $R$. A ring is **[[Def - Noetherian Ring|Noetherian]]** if it satisfies the ascending chain condition on ideals; an algebra is Noetherian if it is so as a ring. A **[[Def - Finitely Generated Algebra|finitely generated R-algebra]]** is a quotient of some $R[T_1, \dots, T_n]$. The full registry is on [[Commutative Algebra I — Chain Conditions]].

---

# Statement

> **Theorem (Hilbert's basis theorem, algebra form).** Every finitely generated algebra over a Noetherian ring is Noetherian. Explicitly: if $R$ is a Noetherian ring then every finitely generated $R$-algebra $A$ is a Noetherian ring.

> **Lemma (one-variable form).** If $R$ is Noetherian, then $R[T]$ is Noetherian. (This is the [[Thm - Hilbert's Basis Theorem|ring-level Hilbert basis theorem]] from Rings IV; the algebra form is its iteration plus passage to quotients.)

The reduction is two steps: by induction $R[T_1, \dots, T_n] \cong R[T_1, \dots, T_{n-1}][T_n]$ is Noetherian using the one-variable lemma $n$ times, and any finitely generated algebra $A \cong R[T_1, \dots, T_n]/I$ is a quotient of a Noetherian ring, hence Noetherian.

---

# Motivation

This is the deep finiteness theorem of commutative algebra, and the word "deep" is earned: the conclusion is *much* stronger than the module-level results that precede it. [[Thm - Finitely Generated Modules over a Noetherian Ring are Noetherian|Finitely generated modules over a Noetherian ring are Noetherian]] is, in the end, bookkeeping with exact sequences. Hilbert's theorem is not — it says a finitely generated *algebra* is Noetherian, and a finitely generated algebra is emphatically *not* a finitely generated module. The polynomial ring $k[T]$ is generated as an algebra by one element but as a module needs the infinite basis $1, T, T^2, \dots$; the module results say nothing about it, yet Hilbert says it is Noetherian. The theorem reaches across the gap between linear and polynomial generation that the rest of the chapter could not cross.

Why does this matter so much? Because the rings that actually arise in algebra and geometry are finitely generated algebras, not finitely generated modules. Coordinate rings of affine varieties $k[T_1, \dots, T_n]/I$, finitely generated $\mathbb{Z}$-algebras of arithmetic geometry, polynomial and power-series rings — all are finitely generated algebras over a field or over $\mathbb{Z}$, and Hilbert is the single theorem that certifies *all of them* Noetherian. Without it, one could not even assert that the ideal defining a variety is finitely generated, and the entire edifice of "varieties are cut out by finitely many equations" would have no foundation.

The structure of the proof is worth absorbing before the details, because it is a model of how Noetherian arguments go. The conclusion for an arbitrary finitely generated algebra is reduced, by the universal property of polynomial rings, to the single case $R[T]$ — every finitely generated algebra is a quotient of a polynomial ring, and quotients of Noetherian rings are Noetherian. The case $R[T]$ is then handled by *degree-tracking*: an ideal of $R[T]$ is controlled by its leading coefficients in each degree, those leading coefficients form an ascending chain of ideals in $R$, and the ACC in $R$ forces that chain to stabilise, which caps how much "new" leading behaviour the ideal can have and lets finitely many polynomials generate it. The motivating slogan is that **a polynomial ideal is finite because its leading coefficients stabilise and the remaining low-degree information is itself finite by induction**.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$A$ is a finitely generated algebra over a Noetherian ring". The disguised sources are the ways this hypothesis appears.

The first disguised source is **$A$ is presented by finitely many generators and (any number of) relations over a field**. The property $B$ is "$A = k[T_1, \dots, T_n]/I$ for some field $k$ and ideal $I$". Since $k$ is Noetherian (a field has only two ideals), $A$ is a finitely generated algebra over a Noetherian ring, so the theorem applies and $A$ is Noetherian. The non-obvious value is that $I$ need not be given by finitely many relations — the theorem retroactively guarantees it is. *Example problem:* the coordinate ring of any affine variety is Noetherian.

The second disguised source is **$A$ is module-finite over a Noetherian ring, or is a localisation/completion of a Noetherian ring**. The property $B$ is "$A$ is built from a Noetherian ring by a finiteness-preserving operation". Module-finite extensions, localisations, and completions of Noetherian rings are Noetherian, often proved via or alongside Hilbert. The non-obviousness is that Noetherianity propagates through the standard constructions. *Example problem:* $\mathbb{Z}_p$ (the $p$-adic integers) is Noetherian as a completion of the Noetherian $\mathbb{Z}$.

The third disguised source is **$A$ is a finitely generated $\mathbb{Z}$-algebra**. The property $B$ is "$A = \mathbb{Z}[T_1, \dots, T_n]/I$". Since $\mathbb{Z}$ is Noetherian (a PID), $A$ is Noetherian. The non-obviousness is that arithmetic schemes of finite type are Noetherian, the foundation of arithmetic geometry. *Example problem:* rings of integers $\mathcal{O}_K$ and their finitely generated extensions are Noetherian.

**Targets (Output Amplification)**

The conclusion is "$A$ is a Noetherian ring", hence every ideal of $A$ is finitely generated and ACC holds.

Combine the conclusion with **the zero-locus argument**. For $S \subseteq k[T_1, \dots, T_n]$ generating an ideal $I$, the simultaneous zero set $V(S) = V(I)$ (the vanishing locus does not change when passing from $S$ to the ideal it generates), and $I$ is finitely generated by Hilbert, so $V(S) = V(S_0)$ for a finite subset $S_0 \subseteq S$. The further result $E$ is that **every algebraic set is cut out by finitely many polynomials** — an infinite system of polynomial equations is equivalent to a finite subsystem. This is non-obvious because the system $S$ may be genuinely infinite.

Combine the conclusion with **the descending chain of closed sets**. ACC on ideals of $A$ becomes DCC on closed subsets of $\operatorname{Spec} A$ (closed sets reverse-correspond to radical ideals). The further result $E$ is that **$\operatorname{Spec} A$ is a Noetherian topological space, so $V(I)$ has finitely many irreducible components**. This is non-obvious because it converts an algebraic chain condition into a topological finiteness of geometric components.

Combine the conclusion with **finite generation of modules over $A$**. Since $A$ is Noetherian, [[Thm - Finitely Generated Modules over a Noetherian Ring are Noetherian|every finitely generated A-module is Noetherian]]. The further result $E$ is that the whole module theory over coordinate rings is finite: submodules, syzygies, and resolutions are all finitely generated. This is the combination that makes computational algebraic geometry possible.

---

# Why Is It True

The algebra form is true because of two clean reductions and one genuine idea. The reductions: every finitely generated algebra is a quotient of a polynomial ring, and quotients of Noetherian rings are Noetherian; and the multivariable polynomial ring is built one variable at a time, $R[T_1, \dots, T_n] = R[T_1, \dots, T_{n-1}][T_n]$, so the whole theorem rests on the single statement "$R$ Noetherian $\Rightarrow$ $R[T]$ Noetherian". The genuine idea lives there.

**The bolded mechanism: an ideal of $R[T]$ is pinned down by its leading coefficients degree-by-degree; those leading-coefficient ideals ascend, so ACC in $R$ stops them, and once the leading behaviour is fixed only finitely many low-degree polynomials remain to generate.**

Here is the idea in full. Let $\mathfrak{a} \trianglelefteq R[T]$. For each degree $i$, collect the leading coefficients of the degree-$i$ polynomials in $\mathfrak{a}$; these form an ideal $\mathfrak{a}(i)$ of $R$ (closed under addition because you can add two degree-$i$ polynomials, and under $R$-multiplication because you can scale). Multiplying a polynomial by $T$ raises its degree by one without changing the leading coefficient, so $\mathfrak{a}(i) \subseteq \mathfrak{a}(i+1)$ — the leading-coefficient ideals form an *ascending chain* in $R$. Now ACC in $R$ bites: this chain stabilises, say $\mathfrak{a}(m) = \mathfrak{a}(m+1) = \cdots$. So beyond degree $m$ no genuinely new leading coefficient appears — anything achievable in high degree was already achievable at degree $m$ by multiplying through by powers of $T$.

The finiteness now follows. Each $\mathfrak{a}(i)$ (for $0 \leq i \leq m$) is finitely generated in $R$ (because $R$ is Noetherian), so pick finitely many polynomials in $\mathfrak{a}$ whose degree-$i$ leading coefficients generate $\mathfrak{a}(i)$, for each $i \leq m$. This is a *finite* collection of polynomials. Let $\mathfrak{b}$ be the ideal they generate. Then $\mathfrak{b}$ and $\mathfrak{a}$ have the same leading-coefficient ideals in every degree (equal for $i \leq m$ by construction, equal for $i > m$ because both stabilised). The claim is $\mathfrak{a} = \mathfrak{b}$: if not, take $f \in \mathfrak{a} \setminus \mathfrak{b}$ of *least* degree $i$; since $\mathfrak{b}(i) = \mathfrak{a}(i)$, there is $g \in \mathfrak{b}$ with the same degree-$i$ leading coefficient, so $f - g$ has degree $< i$ and lies in $\mathfrak{a}$; by minimality $f - g \in \mathfrak{b}$, whence $f = (f - g) + g \in \mathfrak{b}$, a contradiction. So $\mathfrak{a} = \mathfrak{b}$ is finitely generated, and $R[T]$ is Noetherian.

The reason this is *deep* rather than bookkeeping: it manufactures finite generation in $R[T]$ from finite generation in $R$, across the unbounded-degree gap, by recognising that *degree is the only place infinitude can hide*, and that the leading-coefficient chain captures all of it in a single ascending sequence that ACC kills. No exact-sequence argument can do this, because $R[T]$ is not a finitely generated $R$-module — the finiteness is not module-theoretic, it is the subtle interplay of degree filtration with ACC.

---

# What Makes This Hard

The hard step is the **leading-coefficient construction** in the one-variable lemma: realising that an ideal of $R[T]$ should be probed *by degree*, that the leading coefficients in each degree form an ideal $\mathfrak{a}(i)$ of $R$, and that multiplication by $T$ makes these ascend so ACC applies. People get stuck trying to bound the *number* of generators or the degree directly, instead of letting the ascending chain $\mathfrak{a}(0) \subseteq \mathfrak{a}(1) \subseteq \cdots$ do the work. The second subtle point is the *minimal-degree* argument $f = (f-g) + g$: one must take a counterexample of least degree and cancel the top term, and the common error is to forget that $g$ exists precisely because $\mathfrak{b}(i) = \mathfrak{a}(i)$. The reduction from the algebra form to the one-variable case is easy but is sometimes overlooked — one must remember that quotients and finite iterations preserve Noetherianity.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Reduce the algebra form to "$R$ Noetherian $\Rightarrow R[T]$ Noetherian" by iterating one variable at a time and passing to quotients. Prove the one-variable case by tracking leading coefficients: their degree-wise ideals ascend, ACC in $R$ stabilises them, and finitely many witnessing polynomials generate the ideal via a minimal-degree cancellation.

**Subgoal decomposition:**

1. **Reduce the algebra form to one variable.** Show it suffices to prove $R[T]$ Noetherian.
   - *Hint:* $A \cong R[T_1, \dots, T_n]/I$ is a quotient of a Noetherian ring (quotients preserve ACC), and $R[T_1, \dots, T_n] = R[T_1, \dots, T_{n-1}][T_n]$ lets you induct.
   - *Why needed:* It concentrates all difficulty in the single-variable lemma.

2. **Leading-coefficient ideals ascend.** Show $\mathfrak{a}(i)$ is an ideal of $R$ and $\mathfrak{a}(0) \subseteq \mathfrak{a}(1) \subseteq \cdots$.
   - *Hint:* Multiplying a degree-$i$ element by $T$ gives a degree-$(i{+}1)$ element with the same leading coefficient.
   - *Why needed:* It is the chain ACC will stabilise.

3. **Stabilise and pick witnesses.** Use ACC in $R$ to stabilise the chain at degree $m$, and pick finitely many polynomials whose leading coefficients generate each $\mathfrak{a}(i)$, $i \leq m$.
   - *Hint:* $R$ Noetherian gives finite generation of each $\mathfrak{a}(i)$; only $i \leq m$ matter.
   - *Why needed:* It produces a finite candidate generating set $\mathfrak{b}$.

4. **Minimal-degree cancellation shows $\mathfrak{a} = \mathfrak{b}$.** Show the finite set generates the whole ideal.
   - *Hint:* A least-degree element of $\mathfrak{a} \setminus \mathfrak{b}$ can have its top term cancelled by some $g \in \mathfrak{b}$ with the same leading coefficient, contradicting minimality.
   - *Why needed:* It completes finite generation, hence Noetherianity of $R[T]$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Reduction of the algebra form to one variable
> **Statement:** If $R[T]$ is Noetherian whenever $R$ is, then every finitely generated algebra over a Noetherian ring is Noetherian.
>
> **Hint:** Iterate $R[T_1, \dots, T_n] = R[T_1, \dots, T_{n-1}][T_n]$; a finitely generated algebra is a quotient $R[T_1, \dots, T_n]/I$, and quotients of Noetherian rings are Noetherian.
>
> **Why needed:** It concentrates the entire theorem into the single-variable case.
>
> > [!note]- Full proof
> > Let $R$ be Noetherian. By induction on $n$: $R[T_1] = R[T_1]$ is Noetherian by hypothesis; assuming $R[T_1, \dots, T_{n-1}]$ Noetherian, the ring $R[T_1, \dots, T_n] \cong (R[T_1, \dots, T_{n-1}])[T_n]$ is Noetherian by the one-variable hypothesis applied to the Noetherian base $R[T_1, \dots, T_{n-1}]$. Now let $A$ be a finitely generated $R$-algebra, say generated by $x_1, \dots, x_n$. By the universal property of the polynomial algebra there is a surjective $R$-algebra homomorphism $R[T_1, \dots, T_n] \twoheadrightarrow A$, $T_i \mapsto x_i$, so $A \cong R[T_1, \dots, T_n]/I$. A quotient of a Noetherian ring is Noetherian (its ideals correspond to ideals of $R[T_1, \dots, T_n]$ containing $I$, and ACC is inherited). Hence $A$ is Noetherian.

> [!note]- Lemma 2: Leading coefficients form an ascending chain of ideals
> **Statement:** For an ideal $\mathfrak{a} \trianglelefteq R[T]$, each $\mathfrak{a}(i)$ is an ideal of $R$, and $\mathfrak{a}(0) \subseteq \mathfrak{a}(1) \subseteq \mathfrak{a}(2) \subseteq \cdots$.
>
> **Hint:** Closure under $R$-multiplication and addition is inherited from $\mathfrak{a}$; for the inclusion, multiply a degree-$i$ polynomial by $T$.
>
> **Why needed:** It is the ascending chain that ACC in $R$ will stabilise.
>
> > [!note]- Full proof
> > *$\mathfrak{a}(i)$ is an ideal.* Let $c, c' \in \mathfrak{a}(i)$ be leading coefficients of $f, f' \in \mathfrak{a}$ of degree $i$. Then $f + f'$ has degree $\leq i$ with degree-$i$ coefficient $c + c'$; if $c + c' \neq 0$ it lies in $\mathfrak{a}(i)$, and $0 \in \mathfrak{a}(i)$ by convention. For $r \in R$, $rf \in \mathfrak{a}$ has degree-$i$ coefficient $rc$, so $rc \in \mathfrak{a}(i)$. Hence $\mathfrak{a}(i)$ is an ideal.
> >
> > *Ascending.* If $c \in \mathfrak{a}(i)$ is the leading coefficient of $f \in \mathfrak{a}$ with $\deg f = i$, then $Tf \in \mathfrak{a}$ has degree $i+1$ with the same leading coefficient $c$, so $c \in \mathfrak{a}(i+1)$. Thus $\mathfrak{a}(i) \subseteq \mathfrak{a}(i+1)$.

> [!note]- Lemma 3: A finite set of witnesses generates the ideal
> **Statement:** Let $\mathfrak{a}(m) = \mathfrak{a}(m+1) = \cdots$ (stabilisation point), and for each $0 \leq i \leq m$ let $f_{i,1}, \dots, f_{i,n_i} \in \mathfrak{a}$ be degree-$i$ polynomials whose leading coefficients generate $\mathfrak{a}(i)$. Then the ideal $\mathfrak{b} = (\,f_{i,j} : 0 \leq i \leq m,\ 1 \leq j \leq n_i\,)$ equals $\mathfrak{a}$.
>
> **Hint:** $\mathfrak{b} \subseteq \mathfrak{a}$ is clear; for the reverse take a least-degree element of $\mathfrak{a} \setminus \mathfrak{b}$ and cancel its leading term using an element of $\mathfrak{b}$ with the same leading coefficient.
>
> **Why needed:** It produces finite generation of $\mathfrak{a}$, hence Noetherianity of $R[T]$.
>
> > [!note]- Full proof
> > By construction $\mathfrak{b} \subseteq \mathfrak{a}$, and $\mathfrak{b}(i) = \mathfrak{a}(i)$ for all $i$ (for $i \leq m$ by the choice of witnesses; for $i > m$ because $\mathfrak{a}(i) = \mathfrak{a}(m) = \mathfrak{b}(m) \subseteq \mathfrak{b}(i) \subseteq \mathfrak{a}(i)$, using that multiplying the degree-$m$ witnesses by $T^{i-m}$ realises every element of $\mathfrak{a}(m)$ as a degree-$i$ leading coefficient in $\mathfrak{b}$).
> >
> > Suppose $\mathfrak{a} \neq \mathfrak{b}$ and pick $f \in \mathfrak{a} \setminus \mathfrak{b}$ of least degree $i$, with leading coefficient $c \in \mathfrak{a}(i) = \mathfrak{b}(i)$. So there is $g \in \mathfrak{b}$ of degree $i$ with the same leading coefficient $c$ (a suitable $R$-combination of the witnesses, multiplied up to degree $i$ if $i > m$). Then $f - g \in \mathfrak{a}$ has degree $< i$. By minimality of $i$, $f - g \in \mathfrak{b}$. Hence $f = (f - g) + g \in \mathfrak{b}$, contradicting $f \notin \mathfrak{b}$. Therefore $\mathfrak{a} = \mathfrak{b}$, which is finitely generated.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — reduction (Lemma 1).** It suffices to prove: $R$ Noetherian $\Rightarrow R[T]$ Noetherian. Granting this, $R[T_1, \dots, T_n]$ is Noetherian by induction (each adjunction of a variable preserves Noetherianity), and any finitely generated $R$-algebra $A \cong R[T_1, \dots, T_n]/I$ is a quotient of a Noetherian ring, hence Noetherian.
>
> ---
> **The one-variable case.** Let $R$ be Noetherian and $\mathfrak{a} \trianglelefteq R[T]$ an ideal; we show $\mathfrak{a}$ is finitely generated.
>
> By Lemma 2, the leading-coefficient sets $\mathfrak{a}(i) = \{c \in R : cT^i + \cdots \in \mathfrak{a}\} \cup \{0\}$ are ideals of $R$ with $\mathfrak{a}(0) \subseteq \mathfrak{a}(1) \subseteq \cdots$. Since $R$ is Noetherian, this ascending chain stabilises: there is $m \geq 0$ with $\mathfrak{a}(i) = \mathfrak{a}(m)$ for all $i \geq m$. Also, each $\mathfrak{a}(i)$ is finitely generated (as an ideal of the Noetherian $R$): for $0 \leq i \leq m$ choose generators $r_{i,1}, \dots, r_{i,n_i}$ of $\mathfrak{a}(i)$, and pick $f_{i,j} \in \mathfrak{a}$ of degree $i$ with leading coefficient $r_{i,j}$.
>
> Let $\mathfrak{b}$ be the ideal of $R[T]$ generated by the finite set $\{f_{i,j} : 0 \leq i \leq m,\ 1 \leq j \leq n_i\}$. By Lemma 3, $\mathfrak{b} = \mathfrak{a}$. Hence $\mathfrak{a}$ is finitely generated by this finite set.
>
> Since every ideal of $R[T]$ is finitely generated, $R[T]$ is Noetherian. Combined with Step 0, every finitely generated algebra over a Noetherian ring is Noetherian. $\blacksquare$
>
> *(This one-variable case is exactly the [[Thm - Hilbert's Basis Theorem|ring-level Hilbert basis theorem]]; the algebra form is its iteration and quotient.)*

---

# Cross-Field Exercise Suggestions

**Every system of polynomial equations is finite.** Given any (possibly infinite) set $S \subseteq k[T_1, \dots, T_n]$, the solution set $V(S)$ in $k^n$ equals $V(I)$ for $I = (S)$, and Hilbert makes $I$ finitely generated, so $V(S) = V(S_0)$ for a finite $S_0 \subseteq S$. The application is non-obvious because it converts an infinite simultaneous system into a finite equivalent one — the *finiteness theorem* underlying all of polynomial elimination and computational algebra.

**Noetherianity of rings of invariants (Hilbert's original motivation).** For a finite group $G$ acting linearly on $k[T_1, \dots, T_n]$, the ring of invariants $k[T_1, \dots, T_n]^G$ is a finitely generated $k$-algebra (Noether's bound), hence Noetherian; Hilbert proved finite generation of invariants for the general linear and special linear groups, and the basis theorem was the tool. The application is non-obvious because it was the historical problem that *motivated* the theorem — Hilbert's "Gordan's problem".

**Termination of Gröbner basis computation.** The ascending chain of leading-term ideals in Buchberger's algorithm stabilises by Noetherianity of $k[T_1, \dots, T_n]$ (a consequence of Hilbert), which is exactly why the algorithm terminates. The application is non-obvious because it ties a computational halting guarantee to the abstract chain condition; the leading-monomial ideals are a concrete instance of the leading-coefficient ideals in the proof.

---

# Bridges

- **[[Thm - Hilbert's Basis Theorem|Hilbert's basis theorem (ring form, Rings IV)]]** — the one-variable engine. The ring-level theorem proves "$R$ Noetherian $\Rightarrow R[T]$ Noetherian" by the leading-coefficient argument; this algebra-form page is that result *iterated over several variables and pushed through quotients* to reach all finitely generated algebras. The two are the same mathematics at two levels of generality, and the algebra form is the one that interfaces with geometry.

- **[[Thm - Finitely Generated Modules over a Noetherian Ring are Noetherian|Finitely generated modules over a Noetherian ring]]** — the complementary finiteness. Hilbert produces Noetherian *rings*; that theorem then certifies all finitely generated *modules* over them Noetherian. Together they guarantee that, over any finitely generated algebra (a coordinate ring, say), every finitely generated module and all its submodules are finite — the working environment of the whole subject.

- **[[Def - Finitely Generated Algebra|Finitely generated algebra]]** — the hypothesis class. The theorem applies exactly to quotients of polynomial rings, which is why the presentation $A \cong R[T_1, \dots, T_n]/I$ is the form to put any concrete ring into before invoking Noetherianity. The contrast with finitely generated modules (which Hilbert is far stronger than) is the conceptual content of this chapter.

- **Noether normalization and the Nullstellensatz** — the downstream structure theory. Hilbert guarantees finitely generated $k$-algebras are Noetherian; **Noether normalization** then shows each is module-finite over a polynomial subring, and the **Nullstellensatz** turns the maximal ideals into points. These build on Hilbert to give the full algebra–geometry dictionary in [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz]].

---

# Unlocked by This

> [!tip] Coordinate rings and the Nullstellensatz *(from Algebraic Geometry)*
> Hilbert's basis theorem is the prerequisite for the **algebra–geometry dictionary**: finitely generated $k$-algebras (now known Noetherian) are the coordinate rings of affine varieties, ideals are finitely generated so varieties are finite-equation, and the descending chain condition on closed sets gives finitely many irreducible components. The Nullstellensatz then identifies maximal ideals with points. This entire program, developed in [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz]], rests on this theorem.

> [!tip] Noetherianity of power series and completions *(from Commutative Algebra)*
> A close variant of the leading-coefficient argument (now tracking *lowest*-degree terms) shows that the **formal power series ring** $R[[T]]$ is Noetherian when $R$ is, and hence that **completions** of Noetherian rings are Noetherian. This extends the reach of Noetherianity from finite-type algebras to the analytic and adic local rings of Commutative Algebra X, where the $p$-adic integers and formal neighbourhoods live.

> [!tip] Hilbert's finiteness theorem for invariants *(from Invariant Theory)*
> The historical application: for a reductive group $G$ acting on $k[T_1, \dots, T_n]$, the **ring of invariants** $k[T_1, \dots, T_n]^G$ is a finitely generated $k$-algebra, hence Noetherian. Hilbert's proof of finite generation of invariants — which introduced the basis theorem — settled Gordan's problem and is the founding result of modern invariant theory and geometric invariant theory.
