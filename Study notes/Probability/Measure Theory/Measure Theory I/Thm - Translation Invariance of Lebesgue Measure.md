---
type: theorem
subject: measure-theory
prereqs:
  - "Def - Lebesgue Measure"
  - "Thm - Regularity of Lebesgue Measure"
tags: [analysis, measure-theory]
---

# Notation

$\lambda$ is [[Def - Lebesgue Measure|Lebesgue measure]] on $\mathbb{R}^n$. For $x_0\in\mathbb{R}^n$, $\Phi_{x_0}(x)=x_0+x$ is translation by $x_0$, and $x_0+A=\Phi_{x_0}(A)=\{x_0+x:x\in A\}$.

---

# Motivation

"Volume" must not depend on *where* a region sits — a unit cube has volume $1$ at the origin and volume $1$ anywhere else. Translation invariance is the precise statement of this homogeneity of space. It is also the property that *singles Lebesgue measure out*: among all Borel measures on $\mathbb{R}^n$, $\lambda$ is the unique translation-invariant one normalised by $\lambda([0,1]^n)=1$. So translation invariance is simultaneously a sanity check (volume behaves as it should) and a characterisation (it pins down $\lambda$).

It is also the hinge of the [[Thm - Existence of a Non-Measurable Set|Vitali argument]]: a non-measurable set is produced precisely by exhibiting countably many *translates* whose total measure cannot simultaneously be finite and consistent — a contradiction that *uses* translation invariance.

---

# Sources and Targets

**Sources.** The hypothesis "$A$ Borel" is broadened by the proof's own method: the result is first shown for *boxes* (where it is the definition of [[Def - Interval and Elementary Figure|elementary volume]]), then for *open sets* (countable disjoint unions of boxes), then for *all Borel sets* via [[Thm - Regularity of Lebesgue Measure|outer regularity]]. So the genuine source structure is the three-tier ladder boxes $\to$ open $\to$ Borel — the standard ladder for any statement about $\lambda$.

**Targets.** Translation invariance combines with: (i) *uniqueness of the extension* to give the **characterisation** — $\lambda$ is the only translation-invariant normalised Borel measure (any such agrees with $\lambda$ on dyadic boxes, which generate); (ii) *the existence of a [[Thm - Existence of a Non-Measurable Set|Vitali set]]* — translation invariance is the property that makes the Vitali contradiction bite; (iii) *linear changes of variable* — the broader fact $\lambda(gA)=|\det g|\,\lambda(A)$, of which translation invariance is the $g=\mathrm{id}$, shift-only case.

---

# Statement

For every $x_0\in\mathbb{R}^n$ and every $A\in\mathcal{B}(\mathbb{R}^n)$,
$$\lambda(x_0+A)=\lambda(A).$$
Moreover $x_0+A$ is Borel whenever $A$ is (translation is a [[Def - Homeomorphism|homeomorphism]]). Consequently $\lambda$ is **the** unique translation-invariant measure on $\mathcal{B}(\mathbb{R}^n)$ with $\lambda([0,1]^n)=1$.

---

# Why Is It True

The result is *true on boxes by sheer definition*: translating a box $(a,b)$ to $(a+x_0,b+x_0)$ leaves every side length $b_k-a_k$ unchanged, so the elementary volume $\prod(b_k-a_k)$ is unchanged. Translation invariance is *built into the seed*.

The only question is whether it *survives the extension* from boxes to all Borel sets. It does, and the reason is that the extension was performed by *covering with boxes*, an operation that itself commutes with translation. Concretely: an open set is a countable disjoint union of boxes, and translating it translates each box; by $\sigma$-additivity, $\lambda$ of the translated open set is the sum of the (unchanged) box volumes — invariance for open sets. Then a general Borel $A$ is, by [[Thm - Regularity of Lebesgue Measure|outer regularity]], approximated from outside by open sets, and the approximation *also commutes with translation* ("$A\subseteq G$, $G$ open" is equivalent to "$x_0+A\subseteq x_0+G$, $x_0+G$ open"). So the infimum defining $\lambda(x_0+A)$ is over the *translated* family of open supersets, which has the *same* infimum.

The slogan: invariance holds for boxes by definition, and *every step of the construction — covering, countable union, infimum over open supersets — commutes with translation*, so invariance is carried, untouched, all the way up to the Borel sets.

---

# What Makes This Hard

There is no hard step — only a discipline: one must verify invariance *separately at each rung of the ladder* (box, open, Borel) and resist the temptation to assert it directly for Borel sets. The single point worth stating explicitly is *why* the Borel rung works: it is not that "Borel sets are translation-invariant" but that the **outer-regularity infimum** is taken over a family (open supersets) that translation maps bijectively to itself. The deeper conceptual content — that this argument can fail — surfaces in [[Thm - Existence of a Non-Measurable Set|Vitali's theorem]]: invariance is *so* rigid that, combined with countable additivity, it forbids $\lambda$ from being defined on all of $2^{\mathbb{R}}$.

---

# Rederivation Scaffold

**High-level strategy.** Climb the ladder boxes $\to$ open $\to$ Borel; at each rung use that the previous rung's result plus $\sigma$-additivity (or the regularity infimum) commutes with translation.

**Subgoal decomposition.**

1. **Boxes.** $\Phi_{x_0}((a,b))=(a+x_0,b+x_0)$; side lengths unchanged; $\widetilde\lambda$ unchanged.
2. **Open sets.** Write $G=\bigsqcup_k I_k$ (disjoint boxes); $\Phi_{x_0}(G)=\bigsqcup_k\Phi_{x_0}(I_k)$; $\sigma$-additivity + step 1.
3. **Borel sets.** $\lambda(\Phi_{x_0}(A))=\inf\{\lambda(G'):G'\supseteq\Phi_{x_0}(A)\text{ open}\}$; substitute $G'=\Phi_{x_0}(G)$, use step 2 and that $G\mapsto\Phi_{x_0}(G)$ is a bijection of open supersets.
4. **Characterisation.** Any translation-invariant normalised $\mu$ agrees with $\lambda$ on dyadic boxes (subdivide $[0,1]^n$ into $2^{nk}$ congruent translates), which generate $\mathcal{B}(\mathbb{R}^n)$; apply [[Thm - Uniqueness of the Hahn-Carathéodory Extension|uniqueness]].

---

# Lemma Decomposition

> [!note]- Lemma 1: Invariance on boxes and open sets
> **Statement:** $\widetilde\lambda(x_0+I)=\widetilde\lambda(I)$ for boxes $I$; $\lambda(x_0+G)=\lambda(G)$ for open $G$.
>
> > [!note]- Full proof
> > For a box, $\Phi_{x_0}\big(\prod(a_k,b_k)\big)=\prod(a_k+x_0,k,\,b_k+x_0,k)$ has the same side lengths $b_k-a_k$, so the same elementary volume. An open $G\subseteq\mathbb{R}^n$ is a countable disjoint union of (half-open) boxes $G=\bigsqcup_k I_k$; $\Phi_{x_0}(G)=\bigsqcup_k\Phi_{x_0}(I_k)$ is open, the union still disjoint, so by $\sigma$-additivity $\lambda(\Phi_{x_0}(G))=\sum_k\lambda(\Phi_{x_0}(I_k))=\sum_k\lambda(I_k)=\lambda(G)$. $\square$

> [!note]- Lemma 2: Invariance on Borel sets
> **Statement:** $\lambda(x_0+A)=\lambda(A)$ for all $A\in\mathcal{B}(\mathbb{R}^n)$.
>
> **Hint:** The outer-regularity infimum is over a translation-invariant family.
>
> > [!note]- Full proof
> > $A\subseteq G$ with $G$ open iff $\Phi_{x_0}(A)\subseteq\Phi_{x_0}(G)$ with $\Phi_{x_0}(G)$ open, and $G\mapsto\Phi_{x_0}(G)$ is a bijection of the open supersets of $A$ onto those of $\Phi_{x_0}(A)$. Hence by [[Thm - Regularity of Lebesgue Measure|outer regularity]] and Lemma 1,
> > $$\lambda(\Phi_{x_0}(A))=\inf_{\Phi_{x_0}(A)\subseteq G'\text{ open}}\lambda(G')=\inf_{A\subseteq G\text{ open}}\lambda(\Phi_{x_0}(G))=\inf_{A\subseteq G\text{ open}}\lambda(G)=\lambda(A).$$
> > $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Lemma 1 (boxes, open sets) and Lemma 2 (Borel sets) give $\lambda(x_0+A)=\lambda(A)$. For the characterisation: if $\mu$ is translation-invariant on $\mathcal{B}(\mathbb{R}^n)$ with $\mu([0,1]^n)=1$, then $[0,1]^n$ is a disjoint union (up to measure-zero boundaries) of $2^{nk}$ translates of $[0,2^{-k}]^n$, so $\mu([0,2^{-k}]^n)=2^{-nk}=\lambda([0,2^{-k}]^n)$, and $\mu=\lambda$ on all dyadic boxes; these form a generating $\pi$-system, so $\mu=\lambda$ by [[Thm - Uniqueness of the Hahn-Carathéodory Extension|uniqueness]]. $\blacksquare$

---

# Cross-Field Exercise Suggestions

Translation invariance is the prototype of *symmetry forcing a measure*: on any locally compact [[Def - Group|group]] it becomes the existence and uniqueness of **Haar measure**, the canonical invariant measure underlying representation theory and ergodic theory. The generalisation $\lambda(gA)=|\det g|\lambda(A)$ for linear $g$ is the **change-of-variables Jacobian**. In probability, invariance of a law under a group action is *exchangeability* / stationarity, the entry point to [[Thm - Birkhoff's Ergodic Theorem|ergodic theory]] and de Finetti's theorem.

---

# Bridges

- **[[Thm - Existence of a Non-Measurable Set]]** — Vitali's contradiction is built from countably many translates of one set; translation invariance is the property being exploited.
- **[[Thm - Uniqueness of the Hahn-Carathéodory Extension]]** — turns invariance-on-dyadic-boxes into the global characterisation of $\lambda$.
- **[[Thm - Regularity of Lebesgue Measure]]** — supplies the open-set approximation that carries invariance to all Borel sets.
