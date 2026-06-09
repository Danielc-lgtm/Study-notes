---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - The I-adic Completion"
  - "Def - Noetherian Ring"
  - "Def - Finitely Generated Module"
  - "Def - Module"
  - "Def - Ideal"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $R$ be a [[Def - Noetherian Ring|Noetherian]] ring, $\mathfrak{a}\trianglelefteq R$ an [[Def - Ideal|ideal]], $M$ an [[Def - Module|R-module]]. Write $\widehat{R}=\varprojlim_n R/\mathfrak{a}^n$ for the [[Def - The I-adic Completion|\mathfrak{a}-adic completion]] of $R$ and $\widehat{M}=\varprojlim_n M/\mathfrak{a}^n M$ for that of $M$; both are taken with respect to the *same* ideal $\mathfrak{a}$. We write $\otimes_R$ for the tensor product over $R$ and call a functor **exact** if it preserves short exact sequences. The full registry is on [[Commutative Algebra X — Completions and Limits]].

---

# Statement

> **Theorem (completion of a Noetherian ring; Atiyah–Macdonald Ch.10).** Let $R$ be a Noetherian ring and $\widehat{R}$ its $\mathfrak{a}$-adic completion. Then:
>
> 1. $\widehat{R}$ is **Noetherian**.
> 2. The functor $\widehat{R}\otimes_R(-)$ is **exact** (equivalently, $\widehat{R}$ is a **flat** $R$-module).
> 3. For every finitely generated $R$-module $M$, the natural map
> $$\widehat{R}\otimes_R M\;\longrightarrow\;\widehat{M},\qquad x\otimes m\mapsto xm,$$
> is an isomorphism of $\widehat{R}$-modules.
>
> Consequently, for a Noetherian $R$ the completion functor $M\mapsto\widehat{M}$, restricted to finitely generated modules, is exact (parts 2 and 3 combined).

The three parts are the precise analogues, for completion, of the three standard facts about [[Commutative Algebra IV — Localization|localization]]: $S^{-1}R$ is Noetherian when $R$ is, $S^{-1}R\otimes_R(-)$ is exact, and $S^{-1}M\cong S^{-1}R\otimes_R M$.

---

# Motivation

Completion is only useful if the ring it produces is as manageable as the one it came from. The danger is real: an inverse limit is an infinite construction, and infinite constructions routinely destroy finiteness — an infinite product of fields is not Noetherian, an infinite-dimensional space has no finite basis. If $\widehat{R}$ were not Noetherian, every theorem of dimension theory, every primary decomposition, every use of Hilbert's basis theorem would be unavailable on the formal disk, and completion would be a dead end. This theorem is the guarantee that the danger does not materialise: passing to the formal neighbourhood preserves Noetherianity, so the entire apparatus of commutative algebra transfers wholesale to $\widehat{R}$.

Parts 2 and 3 are the working form of "completion behaves like localization". Part 3 identifies the completion of a finitely generated module with a *base change* — tensoring up to $\widehat{R}$ — which means that to compute $\widehat{M}$ you never have to take an inverse limit by hand; you tensor, an algebraic operation with known rules. Part 2 says this base change is exact, so completing an exact sequence of finitely generated modules keeps it exact: kernels, cokernels and quotients all commute with completion. Together they make $\widehat{R}$-module theory a faithful mirror of $R$-module theory, reached by the single functor $\widehat{R}\otimes_R(-)$. The lecture notes flag, correctly, that *every part assumes $R$ Noetherian* — this is not decoration. The proof runs through the associated graded ring and the Artin–Rees lemma, both of which are false without Noetherianity, and the conclusions fail too: outside the Noetherian world completion can be inexact and $\widehat{R}$ can be badly behaved. We follow Atiyah–Macdonald in quoting the result and using it; the [[Commutative Algebra XI — Graded Rings and the Artin-Rees Lemma|next chapter]] develops the graded-ring tools the proof rests on.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition $A$ is "$R$ is Noetherian". The disguised sources are the many ways a ring acquires Noetherianity before completion.

The first disguised source is **"$R$ is a finitely generated algebra over a field or over $\mathbb{Z}$"**. The property $B$ is "finite type over a Noetherian base". The bridge is [[Thm - Hilbert's Basis Theorem|Hilbert's basis theorem]]: $k[T_1,\dots,T_n]$ and $\mathbb{Z}[T_1,\dots,T_n]$ are Noetherian, and quotients of Noetherian rings are Noetherian, so any finitely generated algebra qualifies and its completions are Noetherian. The non-obviousness is that the coordinate ring of *any* affine variety — however singular — has a Noetherian formal completion. *Example problem:* the complete local ring of a plane curve at a singular point, $k[[x,y]]/(f)$, is Noetherian.

The second disguised source is **"$R$ is a localization of a Noetherian ring"**. The property $B$ is "$R=S^{-1}R_0$ with $R_0$ Noetherian". The bridge is that [[Commutative Algebra IV — Localization|localizations of Noetherian rings are Noetherian]], so the local rings $\mathcal{O}_{X,x}=R_{\mathfrak{p}}$ of a variety are Noetherian and their completions are too. The non-obviousness: completion is usually applied to a *local* ring, which is itself a localization, and the Noetherian hypothesis is inherited two steps back. *Example problem:* $\widehat{k[x,y]_{(x,y)}}=k[[x,y]]$ is Noetherian.

The third disguised source is **"$R$ is itself already a completion or a power series ring"**. The property $B$ is "$R=k[[T_1,\dots,T_n]]$ or $R=\mathbb{Z}_p$". The bridge is part 1 applied once: these are completions of Noetherian rings, hence Noetherian, hence *their* further quotients and completions are Noetherian. The non-obviousness is that Noetherianity is stable under iterating the construction. *Example problem:* $\mathbb{Z}_p[[T]]$ and $k[[x,y,z]]/I$ are Noetherian.

**Targets (Output Amplification)**

The conclusions are "$\widehat{R}$ Noetherian", "$\widehat{R}$ flat / $\otimes\widehat{R}$ exact", and "$\widehat{M}=\widehat{R}\otimes_R M$".

Combine **part 1 with Hilbert's basis theorem** to get [[Thm - Formal Power Series over a Noetherian Ring are Noetherian|that the formal power series ring R⟦T₁,…,Tₙ⟧ is Noetherian]]. The additional fact $D$ is that $R[[T_1,\dots,T_n]]$ *is* the $(T_1,\dots,T_n)$-adic completion of the Noetherian ring $R[T_1,\dots,T_n]$. The result $E$ is the power-series analogue of Hilbert's theorem, in one line. Nonobvious because the power-series ring is *not* finitely generated over $R$ as a ring, so Hilbert does not apply directly — completion is the bridge.

Combine **part 3 with a presentation $M=R^n/K$** to compute $\widehat{M}$ concretely. The additional data $D$ is a finite presentation of $M$ (available since $R$ is Noetherian). The result $E$ is $\widehat{M}=\widehat{R}^n/\widehat{K}$: completion commutes with cokernels of maps of free modules, so $\widehat{M}$ is computed by completing a presentation. Nonobvious because it converts an inverse limit into linear algebra over $\widehat{R}$.

Combine **part 2 with a regular sequence** to deduce $\widehat{R}$ inherits depth/regularity. The additional structure $D$ is a regular sequence $x_1,\dots,x_d$ in $\mathfrak{m}$. The result $E$ is that its image in $\widehat{R}$ is again regular (flatness preserves regular sequences), so completion preserves the Cohen–Macaulay and regular properties. Nonobvious because it lets one check these subtle local conditions after completing, where the ring is simpler.

---

# Why Is It True

Part 3 is the conceptual heart, and the other two follow from it. Why should $\widehat{R}\otimes_R M$ equal $\widehat{M}$? Tensoring with $\widehat{R}$ is base change; completing is taking the inverse limit of truncations. They agree because, for a *finitely generated* module over a *Noetherian* ring, the two operations commute with the finite-generation data: $M$ has a finite presentation $R^p\to R^q\to M\to0$, both functors are right exact, and they agree on the free modules $R^p,R^q$ (trivially $\widehat{R}\otimes R^q=\widehat{R}^q=\widehat{R^q}$), so by the five-lemma they agree on $M$. The finiteness is essential at exactly one point: the comparison of the kernels uses Artin–Rees to control how the $\mathfrak{a}$-adic filtration interacts with the submodule, and Artin–Rees needs Noetherian.

**Completion and base-change-to-$\widehat{R}$ are the same operation on finitely generated modules, because both are right-exact functors that agree on free modules and Artin–Rees makes them agree on kernels.**

Part 2, flatness, then drops out: an inverse limit of the *exact* truncation functors $M\mapsto M/\mathfrak{a}^n M$ is exact provided the system satisfies the Mittag-Leffler condition, and for finitely generated modules over a Noetherian ring Artin–Rees guarantees exactly this — the relevant $\varprojlim^1$ vanishes. So completing a short exact sequence of f.g. modules keeps it exact, which is the statement that $\widehat{R}$ is flat. (The geometric slogan: passing to the formal disk does not create or destroy linear relations, just as restricting to an open set does not.)

Part 1, Noetherianity, is the subtlest, and the honest answer is that it is a theorem about the *associated graded ring*. One shows $\widehat{R}$ Noetherian by showing its associated graded ring $\mathrm{gr}_{\mathfrak{a}}\widehat{R}=\bigoplus\mathfrak{a}^n/\mathfrak{a}^{n+1}$ is Noetherian — which it is, being a quotient of a polynomial ring over the Noetherian $R/\mathfrak{a}$ — and then lifting Noetherianity from the graded ring to the filtered ring by an induction on degrees that the completeness of $\widehat{R}$ makes converge. The intuition: an ideal of $\widehat{R}$ is detected by its "leading forms" in $\mathrm{gr}$, finitely many leading forms generate (since $\mathrm{gr}$ is Noetherian), and completeness lets you assemble a finite generating set of the ideal itself from finitely many leading forms by successive approximation — the same Hensel-style convergence that pervades the chapter. This is why the proof belongs with the graded-ring material of the next chapter, and why we quote it here.

---

# What Makes This Hard

The difficulty is that part 1 cannot be proved by the easy method one hopes for: $\widehat{R}$ is *not* finitely generated over $R$ (it is genuinely bigger, full of limiting elements), so [[Thm - Hilbert's Basis Theorem|Hilbert's basis theorem]] does *not* apply directly — the standard route to Noetherianity is blocked. The real proof must instead pass to the **associated graded ring** $\mathrm{gr}_{\mathfrak{a}}\widehat{R}$, prove *it* Noetherian (where Hilbert does apply, since it is a quotient of a polynomial ring), and then lift the property back up the filtration using completeness. The non-obvious step is this lifting — assembling a finite generating set of an ideal of $\widehat{R}$ from finitely many leading forms by successive approximation. The most common error is to assume $\widehat{R}$ is module-finite or algebra-finite over $R$ and quote Hilbert; it is neither.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof (modulo the imported graded-ring lemma).**

**High-level strategy:**
Prove part 3 first by completing a finite presentation and comparing via the five-lemma, using Artin–Rees for the kernel. Deduce part 2 (flatness) from part 3 plus exactness of $\varprojlim$ under Mittag-Leffler (Artin–Rees again). Prove part 1 by reducing Noetherianity of $\widehat{R}$ to Noetherianity of $\mathrm{gr}_{\mathfrak{a}}\widehat{R}$, the latter via Hilbert, and lifting through the filtration by completeness.

**Subgoal decomposition:**

1. **Base-change on free modules.** Show $\widehat{R}\otimes_R R^q\cong\widehat{R^q}=\widehat{R}^q$.
   - *Hint:* Tensor and completion both commute with finite direct sums.
   - *Why needed:* It is the trivial base case for the five-lemma comparison.

2. **Comparison on f.g. modules.** From a finite presentation $R^p\to R^q\to M\to0$, conclude $\widehat{R}\otimes_R M\cong\widehat{M}$ (part 3).
   - *Hint:* Apply $\widehat{R}\otimes_R(-)$ and $\widehat{(-)}$ to the presentation; both are right exact and agree on the free terms; use Artin–Rees to match the images, then the five-lemma.
   - *Why needed:* It is part 3 and the source of parts 1 and 2.

3. **Flatness.** Deduce $\widehat{R}\otimes_R(-)$ exact (part 2).
   - *Hint:* Completion of f.g. modules over Noetherian $R$ is exact because Artin–Rees gives Mittag-Leffler, killing $\varprojlim^1$; transport via part 3.
   - *Why needed:* It is part 2.

4. **Noetherianity.** Show $\widehat{R}$ Noetherian (part 1).
   - *Hint:* $\mathrm{gr}_{\mathfrak{a}}\widehat{R}=\bigoplus\mathfrak{a}^n/\mathfrak{a}^{n+1}$ is a quotient of $(R/\mathfrak{a})[T_1,\dots,T_r]$, hence Noetherian by Hilbert; lift to $\widehat{R}$ via completeness (leading-form argument).
   - *Why needed:* It is part 1, the safety theorem.

---

# Lemma Decomposition

> [!note]- Lemma 1: Completion commutes with finite direct sums
> **Statement:** $\widehat{M\oplus N}\cong\widehat{M}\oplus\widehat{N}$, and $\widehat{R^q}\cong\widehat{R}^q$.
>
> **Hint:** $\mathfrak{a}^n(M\oplus N)=\mathfrak{a}^n M\oplus\mathfrak{a}^n N$, and inverse limits commute with finite products.
>
> **Why needed:** It is the base case for identifying $\widehat{R}\otimes_R(-)$ with $\widehat{(-)}$ on free modules.
>
> > [!note]- Full proof
> > Since $\mathfrak{a}^n(M\oplus N)=\mathfrak{a}^n M\oplus\mathfrak{a}^n N$, we have $(M\oplus N)/\mathfrak{a}^n(M\oplus N)\cong M/\mathfrak{a}^n M\oplus N/\mathfrak{a}^n N$, compatibly with the projections. An inverse limit commutes with finite direct sums (a thread in a direct sum is a pair of threads), so $\widehat{M\oplus N}\cong\widehat{M}\oplus\widehat{N}$. Iterating, $\widehat{R^q}\cong\widehat{R}^q$. Also $\widehat{R}\otimes_R R^q\cong\widehat{R}^q$, so the natural map $\widehat{R}\otimes_R R^q\to\widehat{R^q}$ is an isomorphism on free modules.

> [!note]- Lemma 2: The associated graded ring is Noetherian
> **Statement:** For Noetherian $R$, $\mathrm{gr}_{\mathfrak{a}}R=\bigoplus_{n\geq0}\mathfrak{a}^n/\mathfrak{a}^{n+1}$ is a Noetherian ring, and $\mathrm{gr}_{\mathfrak{a}}\widehat{R}\cong\mathrm{gr}_{\mathfrak{a}}R$.
>
> **Hint:** $\mathfrak{a}$ is finitely generated (Noetherian), say by $x_1,\dots,x_r$; their images in degree $1$ generate $\mathrm{gr}_{\mathfrak{a}}R$ as an algebra over $R/\mathfrak{a}$, so it is a quotient of $(R/\mathfrak{a})[T_1,\dots,T_r]$.
>
> **Why needed:** It is the Noetherian object from which part 1 is lifted; completion does not change it.
>
> > [!note]- Full proof
> > Since $R$ is Noetherian, $\mathfrak{a}=(x_1,\dots,x_r)$ is finitely generated, and $R/\mathfrak{a}$ is Noetherian. The graded ring $\mathrm{gr}_{\mathfrak{a}}R=\bigoplus_n\mathfrak{a}^n/\mathfrak{a}^{n+1}$ is generated in degree $1$ by the images $\bar{x}_i\in\mathfrak{a}/\mathfrak{a}^2$ over the degree-$0$ part $R/\mathfrak{a}$, because $\mathfrak{a}^n$ is generated by degree-$n$ monomials in the $x_i$. Hence there is a surjection of graded rings $(R/\mathfrak{a})[T_1,\dots,T_r]\twoheadrightarrow\mathrm{gr}_{\mathfrak{a}}R$, $T_i\mapsto\bar{x}_i$. By [[Thm - Hilbert's Basis Theorem|Hilbert's basis theorem]] the polynomial ring is Noetherian, and a quotient of a Noetherian ring is Noetherian, so $\mathrm{gr}_{\mathfrak{a}}R$ is Noetherian. Finally $\mathfrak{a}^n/\mathfrak{a}^{n+1}\cong\widehat{\mathfrak{a}}^n/\widehat{\mathfrak{a}}^{n+1}$ (truncation is unchanged by completion), so $\mathrm{gr}_{\mathfrak{a}}\widehat{R}\cong\mathrm{gr}_{\mathfrak{a}}R$ is Noetherian.

> [!note]- Lemma 3: A complete filtered ring is Noetherian if its associated graded ring is
> **Statement:** If $\widehat{R}$ is complete for the $\widehat{\mathfrak{a}}$-adic filtration and $\mathrm{gr}_{\mathfrak{a}}\widehat{R}$ is Noetherian, then $\widehat{R}$ is Noetherian.
>
> **Hint:** Given an ideal $I\subseteq\widehat{R}$, its leading forms generate a finitely generated ideal of $\mathrm{gr}$; lift finitely many leading forms to elements of $I$ and show they generate $I$ by successive approximation.
>
> **Why needed:** It is the lifting step that turns Noetherianity of the graded ring into Noetherianity of the completion (part 1).
>
> > [!note]- Full proof
> > Let $I\subseteq\widehat{R}$ be an ideal. For $f\in I$ non-zero, its **leading form** $\mathrm{in}(f)$ is the image of $f$ in $\widehat{\mathfrak{a}}^d/\widehat{\mathfrak{a}}^{d+1}$ where $d$ is largest with $f\in\widehat{\mathfrak{a}}^d$. The leading forms of elements of $I$ generate a homogeneous ideal $\mathrm{in}(I)\subseteq\mathrm{gr}$, which is finitely generated since $\mathrm{gr}$ is Noetherian (Lemma 2): say by $\mathrm{in}(f_1),\dots,\mathrm{in}(f_s)$ with $f_j\in I$. Claim: $f_1,\dots,f_s$ generate $I$. Given $g\in I$, match its leading form by a combination of the $\mathrm{in}(f_j)$, subtract to raise the order of $g$, and repeat; the corrections form a $\widehat{\mathfrak{a}}$-adic Cauchy sequence whose limit (existing because $\widehat{R}$ is complete) expresses $g$ as an $\widehat{R}$-combination of the $f_j$. Hence $I=(f_1,\dots,f_s)$ is finitely generated, and $\widehat{R}$ is Noetherian.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $R$ be Noetherian, $\mathfrak{a}\trianglelefteq R$, $\widehat{R}=\varprojlim R/\mathfrak{a}^n$.
>
> ---
> **Part 3 — $\widehat{R}\otimes_R M\cong\widehat{M}$ for f.g. $M$.** Since $R$ is Noetherian, $M$ has a finite presentation $R^p\xrightarrow{\;A\;}R^q\to M\to0$. Apply the two right-exact functors $T_1=\widehat{R}\otimes_R(-)$ and $T_2=\widehat{(-)}$:
> $$\widehat{R}\otimes R^p\to\widehat{R}\otimes R^q\to\widehat{R}\otimes M\to0,\qquad \widehat{R^p}\to\widehat{R^q}\to\widehat{M}\to0.$$
> By Lemma 1 the natural maps $\widehat{R}\otimes R^p\to\widehat{R^p}$ and $\widehat{R}\otimes R^q\to\widehat{R^q}$ are isomorphisms, and they intertwine the two left maps (both are $A$ completed). By the five-lemma the induced map $\widehat{R}\otimes M\to\widehat{M}$ is an isomorphism. (The verification that the rows are exact at the middle term — i.e. that completion of the image of $A$ is the image of $\widehat{A}$ — is where [[Thm - The Artin-Rees Lemma|Artin–Rees]] is used, to compare the $\mathfrak{a}$-adic filtration on $\mathrm{im}\,A$ with its intrinsic one.)
>
> ---
> **Part 2 — $\widehat{R}$ flat.** Let $0\to M'\to M\to M''\to0$ be a short exact sequence of finitely generated $R$-modules. Completing termwise gives $0\to\widehat{M'}\to\widehat{M}\to\widehat{M''}\to0$, exact: left-exactness is general for $\varprojlim$, and surjectivity on the right holds because the inverse system $(M'/\mathfrak{a}^n M')$ satisfies the Mittag-Leffler condition — its transition maps are surjective and, by [[Thm - The Artin-Rees Lemma|Artin–Rees]], the induced filtration stabilises, so $\varprojlim^1=0$. By Part 3, this is $0\to\widehat{R}\otimes M'\to\widehat{R}\otimes M\to\widehat{R}\otimes M''\to0$, so $\widehat{R}\otimes_R(-)$ is exact on f.g. modules; flatness over a Noetherian ring is detected on f.g. modules, so $\widehat{R}$ is flat.
>
> ---
> **Part 1 — $\widehat{R}$ Noetherian.** By Lemma 2, $\mathrm{gr}_{\mathfrak{a}}\widehat{R}\cong\mathrm{gr}_{\mathfrak{a}}R$ is Noetherian. By [[Thm - The Inverse Limit and Completeness|completeness]] of $\widehat{R}$ and Lemma 3, Noetherianity lifts from the associated graded ring to $\widehat{R}$ itself. Hence $\widehat{R}$ is Noetherian.
>
> Combining Parts 2 and 3, the functor $M\mapsto\widehat{M}$ is exact on finitely generated modules over the Noetherian ring $R$. $\blacksquare$
>
> *(For the full graded-ring details of Parts 1 and the Artin–Rees comparisons in Parts 2–3, see Atiyah–Macdonald, Commutative Algebra, Chapter 10, and the [[Commutative Algebra XI — Graded Rings and the Artin-Rees Lemma|next chapter]].)*

---

# Cross-Field Exercise Suggestions

**Convergent power series and Noetherianity in analysis.** The ring $\mathbb{C}\{T_1,\dots,T_n\}$ of *convergent* power series at the origin is Noetherian, proved by the same Weierstrass-preparation/leading-form method used here for $\mathbb{C}[[T_1,\dots,T_n]]$. Recognising that the algebraic completion theorem and the analytic Noetherianity theorem share the associated-graded argument is the bridge; nonobvious because one is "formal" and one is "convergent", yet the finiteness mechanism is identical.

**Flatness of completion as a flat family in deformation theory.** A flat family of varieties over a base is one whose total space is flat over the base; completing the base ring along a point gives the *formal deformation*, and part 2 (flatness of $\widehat{R}$) is exactly what guarantees the formal deformation is again flat, so fibres deform without jumping in dimension. The application is nonobvious because "flatness of $\widehat{R}$ over $R$" is the abstract shadow of "the formal family has constant fibre dimension".

**Iwasawa theory and completed group rings.** The Iwasawa algebra $\Lambda=\mathbb{Z}_p[[T]]=\varprojlim\mathbb{Z}_p[\mathbb{Z}/p^n]$ is Noetherian by iterating this theorem ($\mathbb{Z}_p$ Noetherian, then power series over it), and its module theory controls the growth of class groups in $\mathbb{Z}_p$-extensions. The application is nonobvious because the Noetherianity that makes Iwasawa modules manageable is exactly this completion theorem applied twice.

---

# Bridges

- **[[Thm - Formal Power Series over a Noetherian Ring are Noetherian|Formal Power Series over a Noetherian Ring are Noetherian]]** — the immediate corollary. Since $R[[T_1,\dots,T_n]]$ is the $(T_1,\dots,T_n)$-adic completion of the Noetherian (by Hilbert) ring $R[T_1,\dots,T_n]$, part 1 makes it Noetherian. This is the power-series analogue of Hilbert's basis theorem, and it cannot be proved by Hilbert directly because the power-series ring is not finitely generated over $R$.

- **[[Thm - Hilbert's Basis Theorem|Hilbert's Basis Theorem]]** — used twice and contrasted. It is *used* to make $\mathrm{gr}_{\mathfrak{a}}R$ Noetherian (a quotient of a polynomial ring) inside the proof, and it is *contrasted* with this theorem because Hilbert handles finitely generated algebras while completion handles the non-finitely-generated power-series rings — the two together give Noetherianity for all the rings of commutative algebra.

- **[[Thm - The Artin-Rees Lemma|Artin–Rees Lemma]]** — the hidden engine of parts 2 and 3. It controls how the $\mathfrak{a}$-adic filtration restricts to a submodule, which is exactly what is needed to match completion with base change (part 3) and to verify Mittag-Leffler so that completion is exact (part 2). Noetherianity enters the whole theorem through Artin–Rees.

- **[[Commutative Algebra IV — Localization|Localization]]** — the parallel construction. Parts 1–3 are the verbatim analogues of "$S^{-1}R$ Noetherian", "$S^{-1}R$ flat", "$S^{-1}M=S^{-1}R\otimes M$". Both localization and completion are exact base changes to a more local ring; the proofs that they preserve Noetherianity differ (localization is elementary, completion needs graded rings) because completion is the finer, infinite construction.

---

# Unlocked by This

> [!tip] Cohen's structure theorem for complete local rings *(from Commutative Algebra / Algebraic Geometry)*
> Once $\widehat{R}$ is known to be Noetherian, **Cohen's structure theorem** classifies complete Noetherian local rings: an equicharacteristic complete regular local ring of dimension $d$ is isomorphic to a power series ring $k[[T_1,\dots,T_d]]$, and in general $\widehat{R}$ is a quotient of such a power series ring. This is the theorem that makes the formal disk *computable* — every complete local ring has an explicit power-series presentation — and it is the algebraic backbone of the local classification of singularities. It depends entirely on this theorem to guarantee the power-series ring it produces is Noetherian.

> [!tip] Faithfully flat descent along completion *(from Algebraic Geometry)*
> Flatness (part 2), upgraded to **faithful flatness** for the completion of a Noetherian local ring at its maximal ideal, lets properties be checked after completing and then descended back to $R$: a sequence is exact, a module is zero, an ideal is radical, iff the same holds after $\otimes\widehat{R}$. This **faithfully flat descent** is why one may prove statements about a variety by passing to the much simpler formal disk and then descending — a workhorse of modern algebraic geometry made available by this theorem.
