---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Casimir Invariants of the Poincaré Group"
  - "Thm - The Poincaré Group as a Lie Group"
  - "Def - Angular Momentum Four-Tensor"
tags: [physics, special-relativity]
---

# Problem Statement

To qualify as a Casimir, an operator must commute with *every* generator of the Poincaré algebra. Verify this for both Casimirs. Working with $c = 1$ and the Poincaré algebra in covariant form, with translation generators $P^\mu$ and Lorentz generators $J^{\mu\nu} = -J^{\nu\mu}$ obeying
$$[P^\mu, P^\nu] = 0, \qquad [J^{\mu\nu}, P^\rho] = i(\eta^{\nu\rho}P^\mu - \eta^{\mu\rho}P^\nu), \qquad [J^{\mu\nu}, J^{\rho\sigma}] = i(\eta^{\nu\rho}J^{\mu\sigma} - \eta^{\mu\rho}J^{\nu\sigma} - \eta^{\nu\sigma}J^{\mu\rho} + \eta^{\mu\sigma}J^{\nu\rho}),$$

1. Show $[P^2, P^\rho] = 0$ and $[P^2, J^{\rho\sigma}] = 0$, where $P^2 = P_\mu P^\mu$. Conclude $P^2$ is a Casimir.
2. Show that the Pauli–Lubanski vector $W^\mu = -\tfrac{1}{2}\varepsilon^{\mu\nu\rho\sigma}J_{\nu\rho}P_\sigma$ commutes with the translations, $[W^\mu, P^\nu] = 0$.
3. Show $W^\mu$ transforms as a four-vector under Lorentz transformations: $[J^{\mu\nu}, W^\rho] = i(\eta^{\nu\rho}W^\mu - \eta^{\mu\rho}W^\nu)$.
4. Conclude $W^2 = W_\mu W^\mu$ commutes with all generators, hence is a Casimir, and that $(P^2, W^2)$ are the two labels of an irreducible representation.

**Recall:**

![[Def - Casimir Invariants of the Poincaré Group#The Definition]]

The covariant commutation relations above are the [[Thm - The Poincaré Group as a Lie Group|Poincaré algebra]] in the standard physics normalisation (generators Hermitian, factors of $i$). $P^2 = P_\mu P^\mu$ is translation-invariant since translations commute, and is a Lorentz scalar; the [[Def - Angular Momentum Four-Tensor|angular-momentum tensor]] $J^{\mu\nu}$ generates Lorentz transformations. A Lorentz *scalar* operator $S$ (one with $[J^{\mu\nu}, S] = 0$) that also commutes with $P^\rho$ is a Casimir.

---

# Convergent Strategy

**Problem class.** A *verify-a-Casimir* problem: prove two operators commute with all generators of a Lie algebra. The [[Special Relativity XII — Inertial Observers and the Poincaré Group#Problem-Solving Strategy|topic strategy]] for representation problems says to check commutation with translations and with Lorentz generators separately.

**Assumption pattern.** The tools are the three covariant commutation relations and the Leibniz rule for commutators, $[A, BC] = [A, B]C + B[A, C]$. The signpost is "is this a Casimir?": compute $[\text{operator}, P^\rho]$ and $[\text{operator}, J^{\rho\sigma}]$ and show both vanish. For a *scalar* built from four-vectors, the Lorentz commutator vanishes automatically once each building block transforms covariantly.

**Theorem routing.** The route: (i) $P^2$ commutes with $P^\rho$ trivially ($[P,P]=0$) and with $J^{\rho\sigma}$ because it is a scalar (the index contraction makes the vector-transformation terms cancel); (ii) $[W^\mu, P^\nu] = 0$ because $W$ is built from $P$ and a $P$-commuting combination of $J$; (iii) $[J^{\mu\nu}, W^\rho]$ is the four-vector rule, shown by treating $W^\rho$ as a contraction of tensors each transforming covariantly; (iv) $W^2$, being the square of a four-vector, is a scalar, hence commutes with $J$, and commutes with $P$ since $W$ does — Casimir.

**Key decision point.** The crux is the principle that *a fully-contracted scalar built from Lorentz-covariant tensors automatically commutes with the Lorentz generators* — one need not grind out the commutator, only verify each building block is covariant. The work is in (ii) and (iii): showing $W^\mu$ commutes with $P$ (so $W^2$ does) and transforms as a four-vector (so $W^2$ is a scalar). The non-obvious step is using the Leibniz rule and the antisymmetry/contraction structure to collapse the many terms.

---

# Legal Operations Used

1. **Identify a Casimir by checking it commutes with all generators** (operation 8 from the topic page). Both $P^2$ and $W^2$ are verified against the full generator set.

2. **Read structure constants from the bracket** (operation 7 from the topic page, in covariant form): the three commutation relations are the structure constants used throughout, applied via the Leibniz rule.

---

# Hints

> [!note]- Hint 1
> Use the Leibniz rule $[A, BC] = [A,B]C + B[A,C]$. For $[P^2, J^{\rho\sigma}] = [P_\mu P^\mu, J^{\rho\sigma}]$, push $J^{\rho\sigma}$ through both factors of $P$ using $[J^{\rho\sigma}, P^\mu] = i(\eta^{\sigma\mu}P^\rho - \eta^{\rho\mu}P^\sigma)$. The two contributions combine into a contraction of an antisymmetric (in $\rho\sigma$) object with $P_\mu P^\mu$ — symmetric — and vanish.

> [!note]- Hint 2
> $[W^\mu, P^\nu] = -\tfrac{1}{2}\varepsilon^{\mu\alpha\beta\gamma}[J_{\alpha\beta}P_\gamma, P^\nu]$. By Leibniz, $[J_{\alpha\beta}P_\gamma, P^\nu] = [J_{\alpha\beta}, P^\nu]P_\gamma + J_{\alpha\beta}[P_\gamma, P^\nu] = [J_{\alpha\beta}, P^\nu]P_\gamma$ (the second term vanishes). Then $[J_{\alpha\beta}, P^\nu] \sim (\eta^\nu_\beta P_\alpha - \eta^\nu_\alpha P_\beta)$, and contracting with $\varepsilon^{\mu\alpha\beta\gamma}P_\gamma$ gives $\varepsilon^{\mu\alpha\beta\gamma}P_\alpha P_\gamma$-type terms — antisymmetric $\varepsilon$ against symmetric $PP$ — which vanish.

> [!note]- Hint 3
> $W^\rho = -\tfrac{1}{2}\varepsilon^{\rho\alpha\beta\gamma}J_{\alpha\beta}P_\gamma$ is a contraction of the invariant tensor $\varepsilon$ with the tensors $J$ and $P$, leaving one free index $\rho$. Any such object transforms as a four-vector under Lorentz, because $\varepsilon$ is Lorentz-invariant (its components are the same in every frame, up to the $\det\Lambda = 1$ for proper transformations) and $J$, $P$ transform covariantly. Concretely, applying $[J^{\mu\nu}, \cdot]$ via Leibniz to each of $J_{\alpha\beta}$ and $P_\gamma$ reproduces the vector rule on the free index $\rho$.

> [!note]- Hint 4
> $W^2 = W_\rho W^\rho$ is the square of a four-vector, hence a Lorentz scalar: $[J^{\mu\nu}, W^2] = 0$ (the two vector-transformation terms cancel on contraction, exactly as for $P^2$). And $[W^2, P^\nu] = [W_\rho, P^\nu]W^\rho + W_\rho[W^\rho, P^\nu] = 0$ since $[W^\rho, P^\nu] = 0$ from part 2. So $W^2$ commutes with all generators.

---

# Solution

Both Casimirs are verified against every generator. Step 1 handles $P^2$. Step 2 shows $W$ commutes with translations. Step 3 shows $W$ is a four-vector. Step 4 assembles: $W^2$ is a scalar (commutes with $J$) and commutes with $P$, hence Casimir.

**Step 1: $P^2$ is a Casimir.**

> [!note]- Derivation
> *Commutes with translations.* $[P^2, P^\rho] = [P_\mu P^\mu, P^\rho]$. By Leibniz, $= [P_\mu, P^\rho]P^\mu + P_\mu[P^\mu, P^\rho] = 0$, since $[P^\mu, P^\nu] = 0$ (translations commute). So $[P^2, P^\rho] = 0$.
>
> *Commutes with Lorentz generators.* $[P^2, J^{\rho\sigma}] = [P_\mu P^\mu, J^{\rho\sigma}]$. By Leibniz,
> $$[P_\mu P^\mu, J^{\rho\sigma}] = [P_\mu, J^{\rho\sigma}]P^\mu + P_\mu[P^\mu, J^{\rho\sigma}].$$
> Use $[P^\mu, J^{\rho\sigma}] = -[J^{\rho\sigma}, P^\mu] = -i(\eta^{\sigma\mu}P^\rho - \eta^{\rho\mu}P^\sigma) = i(\eta^{\rho\mu}P^\sigma - \eta^{\sigma\mu}P^\rho)$. Lowering appropriately, the first term is $[P_\mu, J^{\rho\sigma}]P^\mu = i(\delta^\rho_\mu P^\sigma - \delta^\sigma_\mu P^\rho)P^\mu = i(P^\sigma P^\rho - P^\rho P^\sigma) = 0$ (the $P$'s commute). The second term $P_\mu[P^\mu, J^{\rho\sigma}] = i\,P_\mu(\eta^{\rho\mu}P^\sigma - \eta^{\sigma\mu}P^\rho) = i(P^\rho P^\sigma - P^\sigma P^\rho) = 0$. Both vanish, so $[P^2, J^{\rho\sigma}] = 0$.
>
> Since $P^2$ commutes with both translations and Lorentz generators, it is a **Casimir**. Its eigenvalue is the squared mass $m^2$.

**Step 2: $W^\mu$ commutes with translations.**

> [!note]- Derivation
> $$[W^\mu, P^\nu] = -\tfrac{1}{2}\varepsilon^{\mu\alpha\beta\gamma}[J_{\alpha\beta}P_\gamma,\, P^\nu].$$
> By Leibniz, $[J_{\alpha\beta}P_\gamma, P^\nu] = [J_{\alpha\beta}, P^\nu]P_\gamma + J_{\alpha\beta}[P_\gamma, P^\nu]$. The second commutator vanishes ($[P_\gamma, P^\nu] = 0$), leaving
> $$[W^\mu, P^\nu] = -\tfrac{1}{2}\varepsilon^{\mu\alpha\beta\gamma}[J_{\alpha\beta}, P^\nu]P_\gamma.$$
> Now $[J_{\alpha\beta}, P^\nu] = i(\delta^\nu_\beta P_\alpha - \delta^\nu_\alpha P_\beta)$ (the covariant relation, indices lowered). Substituting,
> $$[W^\mu, P^\nu] = -\tfrac{i}{2}\varepsilon^{\mu\alpha\beta\gamma}(\delta^\nu_\beta P_\alpha - \delta^\nu_\alpha P_\beta)P_\gamma = -\tfrac{i}{2}\big(\varepsilon^{\mu\alpha\nu\gamma}P_\alpha P_\gamma - \varepsilon^{\mu\nu\beta\gamma}P_\beta P_\gamma\big).$$
> In each term the Levi-Civita symbol is antisymmetric in the two indices carried by the $P$'s ($\alpha\gamma$ in the first, $\beta\gamma$ in the second), while $P_\alpha P_\gamma$ (resp. $P_\beta P_\gamma$) is symmetric. Antisymmetric contracted with symmetric vanishes. Hence
> $$[W^\mu, P^\nu] = 0.$$
> The Pauli–Lubanski vector commutes with the translations — it is translation-invariant, which (unlike $J^{\mu\nu}$ itself) makes it a viable Casimir building block.

**Step 3: $W^\mu$ is a four-vector.**

> [!note]- Derivation
> We must show $[J^{\mu\nu}, W^\rho] = i(\eta^{\nu\rho}W^\mu - \eta^{\mu\rho}W^\nu)$, the four-vector transformation rule. Write $W^\rho = -\tfrac{1}{2}\varepsilon^{\rho\alpha\beta\gamma}J_{\alpha\beta}P_\gamma$ and apply $[J^{\mu\nu}, \cdot]$ by Leibniz to the two operator factors $J_{\alpha\beta}$ and $P_\gamma$ (the symbol $\varepsilon$ is a constant numerical tensor, so it passes through):
> $$[J^{\mu\nu}, W^\rho] = -\tfrac{1}{2}\varepsilon^{\rho\alpha\beta\gamma}\big([J^{\mu\nu}, J_{\alpha\beta}]P_\gamma + J_{\alpha\beta}[J^{\mu\nu}, P_\gamma]\big).$$
> Each commutator is a covariant transformation: $[J^{\mu\nu}, P_\gamma]$ rotates the index $\gamma$, and $[J^{\mu\nu}, J_{\alpha\beta}]$ rotates the indices $\alpha, \beta$. The key structural fact is that $\varepsilon^{\rho\alpha\beta\gamma}$ is a Lorentz-*invariant* tensor (for proper Lorentz transformations, $\Lambda^\rho{}_{\rho'}\Lambda^\alpha{}_{\alpha'}\Lambda^\beta{}_{\beta'}\Lambda^\gamma{}_{\gamma'}\varepsilon^{\rho'\alpha'\beta'\gamma'} = (\det\Lambda)\varepsilon^{\rho\alpha\beta\gamma} = \varepsilon^{\rho\alpha\beta\gamma}$). Therefore the contraction of $\varepsilon$ with the covariantly-transforming $J$ and $P$ on the indices $\alpha, \beta, \gamma$ produces, on the single remaining free index $\rho$, exactly the four-vector transformation: the rotations of $\alpha, \beta, \gamma$ "pass through" the invariant $\varepsilon$ and re-emerge as a rotation of $\rho$. Carrying out the index algebra (substitute the two commutators, relabel dummy indices, use the antisymmetry of $\varepsilon$ to combine terms), all the $\alpha\beta\gamma$-rotations collapse and what survives is
> $$[J^{\mu\nu}, W^\rho] = i\big(\eta^{\nu\rho}W^\mu - \eta^{\mu\rho}W^\nu\big),$$
> the four-vector rule. (This is the general principle: any tensor formed by contracting the invariant $\varepsilon$ with covariant tensors transforms covariantly on its free indices — a fully-contracted object is a scalar, an object with one free index a vector, etc.)

**Step 4: $W^2$ is a Casimir.**

> [!note]- Derivation
> *Commutes with Lorentz generators.* Since $W^\rho$ is a four-vector (Step 3), its square $W^2 = W_\rho W^\rho$ is a Lorentz scalar. Explicitly,
> $$[J^{\mu\nu}, W^2] = [J^{\mu\nu}, W_\rho]W^\rho + W_\rho[J^{\mu\nu}, W^\rho] = i(\delta^\nu_\rho W^\mu - \delta^\mu_\rho W^\nu)W^\rho + W_\rho\,i(\eta^{\nu\rho}W^\mu - \eta^{\mu\rho}W^\nu).$$
> The first bracket gives $i(W^\mu W^\nu - W^\nu W^\mu)$-type terms and the second $i(W^\nu W^\mu - W^\mu W^\nu)$-type; carefully tracking the contractions, the two cancel exactly (as for $P^2$ in Step 1), giving $[J^{\mu\nu}, W^2] = 0$.
>
> *Commutes with translations.* By Leibniz and Step 2,
> $$[W^2, P^\nu] = [W_\rho, P^\nu]W^\rho + W_\rho[W^\rho, P^\nu] = 0 + 0 = 0.$$
>
> So $W^2$ commutes with both the translations and the Lorentz generators: it is a **Casimir**. Its eigenvalue on a massive spin-$s$ representation is $-m^2 s(s+1)$ (see [[Ex - Computing the Pauli-Lubanski vector]]).
>
> *Conclusion.* The Poincaré algebra has exactly two independent Casimirs, $P^2$ and $W^2$. By Schur's lemma, each is a scalar on an irreducible representation, so the pair $(P^2, W^2) = (m^2, -m^2 s(s+1))$ — equivalently $(m, s)$ — completely labels the irreducible representation. This is the algebraic underpinning of the [[Def - Casimir Invariants of the Poincaré Group|Wigner classification]]: mass and spin are the two Casimir eigenvalues.

> [!note]- Complete formal solution
> *$P^2$:* $[P^2, P^\rho] = 0$ since $[P^\mu, P^\nu] = 0$; $[P^2, J^{\rho\sigma}] = 0$ because each Leibniz term gives $\pm i(P^\rho P^\sigma - P^\sigma P^\rho) = 0$. So $P^2$ is Casimir, eigenvalue $m^2$.
> *$W$ commutes with $P$:* $[W^\mu, P^\nu] = -\tfrac{i}{2}\varepsilon^{\mu\alpha\beta\gamma}(\delta^\nu_\beta P_\alpha - \delta^\nu_\alpha P_\beta)P_\gamma$, and each term contracts the antisymmetric $\varepsilon$ against a symmetric $P_\alpha P_\gamma$, vanishing. So $[W^\mu, P^\nu] = 0$.
> *$W$ is a four-vector:* $W^\rho = -\tfrac12\varepsilon^{\rho\alpha\beta\gamma}J_{\alpha\beta}P_\gamma$ contracts the Lorentz-invariant $\varepsilon$ with covariant $J, P$, so it transforms covariantly on the free index: $[J^{\mu\nu}, W^\rho] = i(\eta^{\nu\rho}W^\mu - \eta^{\mu\rho}W^\nu)$.
> *$W^2$ is Casimir:* being the square of a four-vector it is a scalar, $[J^{\mu\nu}, W^2] = 0$; and $[W^2, P^\nu] = 0$ since $[W^\rho, P^\nu] = 0$. So both $P^2$ and $W^2$ commute with all ten generators; by Schur they are scalars on an irreducible representation, and $(m^2, -m^2 s(s+1))$ labels it by mass and spin. $\blacksquare$

---

# Key Takeaways

**A fully-contracted scalar built from Lorentz-covariant tensors commutes with the Lorentz generators automatically — you need only check the building blocks.** The recurring labour-saver in this exercise is the principle that an operator formed by contracting all indices of covariant tensors is a Lorentz scalar, hence commutes with $J^{\mu\nu}$, without grinding out the commutator. $P^2 = P_\mu P^\mu$ and $W^2 = W_\rho W^\rho$ are scalars because they are squares of four-vectors; the two vector-transformation terms in $[J, V^2]$ always cancel on contraction. The transferable diagnostic: to test whether a quadratic operator is a Lorentz scalar, check that each factor transforms as a tensor and that all indices are contracted; if so, it commutes with the Lorentz generators by construction. The real work is never the Lorentz commutator of the scalar — it is verifying that the building blocks (here $W^\mu$) are genuinely covariant, which is Steps 2–3.

**The antisymmetric-against-symmetric vanishing is the workhorse of the whole computation.** Three times — in $W\cdot P = 0$ (previous exercise), in $[W^\mu, P^\nu] = 0$, and implicitly in the four-vector rule — the key cancellation is "an $\varepsilon$ (antisymmetric in two indices) contracted with a product $P P$ (symmetric in those indices) vanishes". This single identity, $A_{[\mu\nu]}S^{(\mu\nu)} = 0$, drives the Casimir structure. The reusable pattern: whenever the Levi-Civita symbol meets a repeated momentum (or any symmetric pair), expect that contraction to vanish, and use it to collapse expressions. It is why the Pauli–Lubanski vector is translation-invariant (the obstruction would be a $\varepsilon P P$ term) and why it is orthogonal to the momentum. Mastering this one move makes the Poincaré Casimir algebra tractable; missing it leaves a thicket of terms.

**Why $W^\mu$, not $J^{\mu\nu}$ — translation-invariance is the missing ingredient that the Pauli–Lubanski construction supplies.** The deepest lesson is *why* the spin Casimir requires the Pauli–Lubanski vector at all. The naive scalar $J_{\mu\nu}J^{\mu\nu}$ is a Lorentz scalar, but it is *not* a Casimir, because $J^{\mu\nu}$ does not commute with the translations $P^\rho$ — angular momentum depends on the choice of origin, so it is not translation-invariant. The Pauli–Lubanski vector $W^\mu = -\tfrac{1}{2}\varepsilon^{\mu\nu\rho\sigma}J_{\nu\rho}P_\sigma$ repairs this: by contracting $J$ with $P$ it produces a combination that *does* commute with translations (Step 2), discarding the origin-dependent orbital part and keeping only the intrinsic spin. So $W^2$ is the spin Casimir precisely because the contraction with $P$ buys translation-invariance that $J$ alone lacks. The transferable insight: when a candidate invariant fails to be Casimir because it is not translation-invariant, look for a way to contract it with the momentum to project onto the translation-invariant (intrinsic) part. This is exactly how spin is separated from orbital angular momentum, both here and in the classical [[Def - Spin Four-Vector|spin four-vector]].
