---
type: exercise-index
subject: commutative-algebra
section: "11.2"
tags: [algebra, commutative-algebra]
---

## §11.2 Completions — Exercises

The exercises of §11.2 drill the [[Def - The I-adic Completion|\mathfrak{a}-adic completion]] and the four things one does with it: *identify* it as a familiar ring (power series, $p$-adics), *compare* it with the original ring and its localization (same residue field, finer than $R_{\mathfrak{p}}$), *certify its faithfulness* by proving the completion map injective (the kernel formula plus [[Thm - The Krull Intersection Theorem|Krull intersection]]), and *solve equations in it* by Hensel-style successive approximation. The recurring lever is "units are detected mod $\mathfrak{a}$", proved by geometric-series inversion, which gives locality, the unit group, and the foothold for Hensel. Together these exercises install the slogan that completion passes to the **formal disk** — the analytic-local neighbourhood resolving infinitesimal structure while leaving the residue field untouched.

- [[Ex - The formal power series ring as a completion]] (⭐⭐) — realise $k[[T]]=\widehat{k[T]}^{(T)}$ via the coefficient bijection, prove $k[[T]]$ is local with units $\{f(0)\neq0\}$, and extend to $k[[T_1,\dots,T_n]]$ using $\mathfrak{a}^i=$ (total degree $\geq i$) — the local model of the formal disk in $n$ variables ([[Def - Direct and Inverse Limits]], [[Def - The I-adic Completion]], [[Def - Polynomial Ring]], [[Def - Local Ring and Residue Field]]).

- [[Ex - Completion of a local ring at its maximal ideal]] (⭐⭐) — show $\widehat{R}^{\,\mathfrak{m}}$ is local with maximal ideal $\mathfrak{m}\widehat{R}$ and the *same* residue field $\widehat{R}/\widehat{\mathfrak{m}}\cong R/\mathfrak{m}$, by the residue-detects-units criterion and the order-$1$ truncation, with $\widehat{\mathbb{Z}_{(p)}}=\mathbb{Z}_p$ and $\widehat{k[x,y]_{(x,y)}}=k[[x,y]]$ as the models — completion is invisible at the point but resolves the neighbourhood ([[Def - The I-adic Completion]], [[Def - Local Ring and Residue Field]], [[Def - Noetherian Ring]], [[Thm - The Inverse Limit and Completeness]]).

- [[Ex - The completion map and the Krull intersection]] (⭐⭐) — *(ES4 Q15)* prove $\ker\varphi=\bigcap_n\mathfrak{a}^n M$ from the inverse-limit definition, then injectivity for $R$ Noetherian local (or a domain) by deriving $\mathfrak{a}I=I$ from [[Thm - The Artin-Rees Lemma|Artin–Rees]] and killing $I$ with the determinant trick — the proof of [[Thm - The Krull Intersection Theorem|Krull intersection]] and the certificate that $R\hookrightarrow\widehat{R}$ ([[Def - The I-adic Completion]], [[Def - Noetherian Ring]], [[Def - Local Ring and Residue Field]], [[Def - Finitely Generated Module]], [[Thm - The Inverse Limit and Completeness]], [[Thm - The Artin-Rees Lemma]], [[Thm - The Krull Intersection Theorem]]).

- [[Ex - Hensel-style lifting in the p-adics]] (⭐⭐⭐) — prove Hensel's lemma by Newton iteration $a_{n+1}=a_n-f(a_n)/f'(a_n)$ (quadratic convergence from the Taylor remainder, completeness supplying the limit), then lift the $(p-1)$-th roots of unity (Teichmüller representatives) and $\sqrt{-1}\in\mathbb{Z}_5$, with the simple-root condition $f'(a_0)\in\mathbb{Z}_p^\times$ as the indispensable non-degeneracy ([[Def - The I-adic Completion]], [[Def - Direct and Inverse Limits]], [[Def - Local Ring and Residue Field]]).
