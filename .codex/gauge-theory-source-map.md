# Gauge theory source-coverage map

This is the durable coverage ledger for the Gauge Theory series under `Study notes/Geometry/Gauge Theory/` (thirteen chapters `Gauge Theory I`–`Gauge Theory XIII` plus the front door `Gauge Theory — Series Map`), a standalone peer of `Differential Geometry/`. The series replaced the earlier `Geometry of Physics/Gauge Theory/` notes, which were deleted and whose incoming links were repointed to the new chapter titles.

A section is checked only after every one of its definitions, theorems, proofs, examples, exercises, and load-bearing remarks has a destination page in the vault and that page passes review under the vault-wide prose and proof standard (`.claude/skills/polymath-notes/references/prose-and-proof-standard.md`: thesis register, every theorem mentioned proved in full, imports only from the pre-approved list). Page numbers are PDF page numbers, not printed-page numbers.

## Source A — Haydys, *Introduction to Gauge Theory* (`sources/`, 73 PDF pages)

| Source section | PDF pages | Destination chapter | Status |
|---|---:|---|---|
| §1, moduli-space blueprint and purpose of gauge theory | 2–4 | XI (motivation), Series Map | in progress |
| §2.1, vector bundles, operations, sections, covariant derivatives, curvature, gauge group | 4–10 | II (gauge group of a vector bundle: V) | in progress |
| §2.2.1–2.2.2, frame bundles, structure groups, associated bundles | 11–15 | III | in progress |
| §2.2.3–2.2.4, principal connections and curvature | 16–21 | IV | in progress |
| §2.2.5, gauge group of a principal bundle | 21 | V | in progress |
| §2.3, Levi–Civita connection as a connection on $TM$ | 22–23 | II | in progress |
| §2.4, classification of $U(1)$ and $SU(2)$ bundles; complex and quaternionic lines | 23–25 | III | in progress |
| §3.1, invariant polynomials, Chern–Weil theory, Chern classes | 26–29 | VI | in progress |
| §3.2, Chern–Simons functional | 30–31 | VI | in progress |
| §3.3, flat connections, parallel transport, holonomy, monodromy | 32–33 | V | in progress |
| §4.1, spin groups and Clifford algebras | 34–35 | VIII | in progress |
| §4.2, Dirac operators | 36–37 | VIII | in progress |
| §4.3, spin and $\operatorname{Spin}^c$ structures and their classification | 37–41 | VIII | in progress |
| §4.4, Weitzenböck formula | 41–42 | VIII | in progress |
| §5.1, Sobolev spaces | 43–46 | IX | in progress |
| §5.2, elliptic operators | 46–49 | IX | in progress |
| §5.3, elliptic complexes, gauge interpretation, de Rham complex | 49–51 | IX | in progress |
| §6.1, Kuranishi model and Sard–Smale theorem | 52–53 | X | in progress |
| §6.2, $\mathbb Z/2\mathbb Z$ degree | 53–55 | X | in progress |
| §6.3, parametric transversality | 55–56 | X | in progress |
| §6.4, determinant line bundle | 56–58 | X | in progress |
| §6.5, orientations and integer-valued degree | 58–59 | X | in progress |
| §6.6, equivariant setup | 59–60 | X | in progress |
| §7.1, Seiberg–Witten equations, gauge action, deformation complex, Sobolev completion, compactness, slices, perturbations, reducibles, orientability | 61–70 | XI | in progress |
| §7.2, Seiberg–Witten invariant and its applications | 71–73 | XI | in progress |
| Appendix B of the content map: source typos | — | corrected on the destination pages, each with a `(source typo: …)` note | in progress |

## Source B — Bär, *Gauge Theory* (Potsdam lecture notes, 2011; file `sources/mathematical_gauge_theory.pdf`, 155 PDF pages)

The file is misnamed: its author is Christian Bär, not Wernli, and every page of the series attributes it to Bär.

| Source section | PDF pages | Destination chapter | Status |
|---|---:|---|---|
| Preface | 5–6 | Series Map | in progress |
| §1.1–1.5, Lie groups, Lie algebras, representations, exponential map, group actions | 7–36 | I | in progress |
| §2.1–2.2, fibre and principal bundles | 37–49 | III | in progress |
| §2.3–2.4, connections and curvature | 50–58 | IV | in progress |
| §2.5, characteristic classes | 59–64 | VI | in progress |
| §2.6, parallel transport and holonomy | 65–74 | V | in progress |
| §2.7, automorphisms and gauge transformations | 75–78 | V | in progress |
| §3.1, Hodge-star operator in arbitrary signature | 79–83 | VII | in progress |
| §3.2, electrodynamics, Maxwell equations, action, energy-momentum tensor | 84–96 | VII | in progress |
| §3.3, Yang–Mills fields, variation, characteristic number, instantons | 97–106 | VII | in progress |
| §4.1, homotopy theory | 107–115 | XII | in progress |
| §4.2, homology theory | 116–125 | XII | in progress |
| §4.3, orientations and fundamental class | 126–130 | XII | in progress |
| §5.1, intersection form | 131–137 | XIII | in progress |
| §5.2, four-manifold classification results | 138–143 | XIII | in progress |
| §5.3, Donaldson's theorem and gauge-theoretic context | 144–155 | XIII (deduction of the diagonalisation; the analytic package is imported) | in progress |
| Appendix B of the content map: source typos | — | corrected on the destination pages, each with a `(source typo: …)` note | in progress |

## Architecture and convention decisions

1. The two sources are merged concept by concept: where Haydys and Bär define or prove the same thing there is one page, with both formulations recorded and any difference of convention explained in a `> [!warning] Convention:` callout.
2. Lie groups act on principal bundles on the right; representations and group actions on manifolds are left actions. The Lie algebra is $T_eG$ with the bracket of left-invariant vector fields.
3. Curvature is $F_A = dA + \tfrac12[A \wedge A]$ for a local connection form, which equals $dA + A \wedge A$ for matrix groups; the structure equation is $\Omega = d\omega + \tfrac12[\omega \wedge \omega]$ with $R_g^*\omega = \operatorname{Ad}_{g^{-1}}\omega$.
4. Characteristic classes are normalised by $c(E) = \det(1 + \tfrac{i}{2\pi}F)$, so that $c_2(P) = [\tfrac{1}{8\pi^2}\operatorname{tr}(F \wedge F)]$ for an $SU(2)$-bundle; complex manifolds carry the complex orientation and $S^3 = \partial B^4 \subset \mathbb H$ the boundary orientation. The sign-sensitive pages (the Hopf bundle, the classification of $SU(2)$-bundles over four-manifolds, the second Chern number as a clutching degree, the gauge variation of the Chern–Simons functional) share one sign ledger recorded on `Def - The Hopf Bundle`.
5. The Hodge star follows Bär, $\omega \wedge \eta = \langle \star\omega, \eta\rangle\,\mathrm{vol}$, in every signature; Lorentzian signature is $(-,+,+,+)$ with $c = 1$; the Clifford relation is $v \cdot v = -q(v)\,1$. Every page that uses one of these states it and compares it with the other common convention.
6. Sobolev and elliptic theory are developed in $L^2$-Sobolev spaces; the intersection form is defined by transverse intersection of oriented surfaces, and its identifications with the cup-product form and the de Rham pairing are theorems.
7. The only results allowed inside an `Imported without proof` callout are the eight on the pre-approved list of the series conventions (Freedman's classification, the analytic package behind Donaldson's diagonalisation theorem, the Atiyah–Singer index theorem, Hasse–Minkowski and Meyer, the Lefschetz hyperplane theorem, Casson's theory, the Minkowski–Siegel mass formula, and Whitehead's topological-manifold input). Each is registered under `# Imported Results` on its chapter's topic page and on the Series Map. Everything else the sources cite without proof is proved in full in the series.
