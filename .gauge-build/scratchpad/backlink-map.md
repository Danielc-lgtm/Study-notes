# Old → new wikilink targets (for repairing the 141 links from 72 files outside the deleted folder)

Topic pages (the display text after `|` is kept; only the target changes). Where an old chapter's content is split across two new chapters, the rule for choosing is given.

| Old target | New target | Rule |
|---|---|---|
| Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection | Gauge Theory II — Vector Bundles, Covariant Derivatives, and Curvature | default |
| (same) | Gauge Theory VII — The Hodge Star, Electrodynamics, and Yang–Mills Theory | if the display text or the surrounding line mentions electromagnet-, Maxwell, U(1) gauge field, four-potential, monopole, Aharonov, minimal coupling, gauge potential $A_\mu$ |
| Gauge Theory II — Principal Bundles, Representations, and Bundle Classification | Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles | default |
| (same) | Gauge Theory VI — Chern–Weil Theory, Characteristic Classes, and the Chern–Simons Functional | if the display text mentions Gauss–Bonnet–Chern, Chern–Gauss–Bonnet, characteristic class, Euler class, Chern class |
| Gauge Theory III — Principal Connections, Curvature, Holonomy, and Gauge Symmetry | Gauge Theory IV — Connections and Curvature on Principal Bundles | default |
| (same) | Gauge Theory V — Parallel Transport, Holonomy, Gauge Transformations, and Flat Connections | if the display text mentions holonomy, parallel transport, horizontal lift, gauge transformation, flat, monodromy |
| Gauge Theory IV — Chern–Weil Theory, Characteristic Classes, Chern–Simons, and Flat Moduli | Gauge Theory VI — … | always |
| Gauge Theory V — Hodge Theory, Maxwell, Yang–Mills, and Instantons | Gauge Theory VII — … | always |
| Gauge Theory VI — Clifford Algebras, Spin Geometry, and Dirac Operators | Gauge Theory VIII — Clifford Algebras, Spin Structures, and Dirac Operators | always |
| Gauge Theory VII — Sobolev Spaces, Elliptic Operators, and Gauge-Fixing Complexes | Gauge Theory IX — Sobolev Spaces, Elliptic Operators, and Elliptic Complexes | always |
| Gauge Theory VIII — Fredholm Maps, Transversality, Determinant Lines, and Degree | Gauge Theory X — Fredholm Maps, Transversality, and Degree | always |
| Gauge Theory IX — Seiberg–Witten Equations, Compactness, and Moduli Spaces | Gauge Theory XI — Seiberg–Witten Theory | always |
| Gauge Theory X — Seiberg–Witten Invariants and Four-Manifold Applications | Gauge Theory XI — Seiberg–Witten Theory | always |
| Gauge Theory XI — Topology, Intersection Forms, and Donaldson Theory | Gauge Theory XIII — Intersection Forms, Four-Manifold Classification, and Donaldson's Theorem | always |

Definition pages linked from outside — the new series keeps these exact filenames so the links resolve unchanged:

| Old page (links) | New home | Note |
|---|---|---|
| Def - Instanton (11) | VII | (anti-)self-dual connection on a 4-manifold; B §3.3 |
| Def - Pfaffian (7) | VI | B §2.5 Euler class via the Pfaffian |
| Def - Fibre Bundle (4) | III | B §2.1 (British spelling kept for the link) |
| Def - U(1) Gauge Field and Electromagnetic Connection (3) | VII | B §3.2 |
| Def - Connection on a Vector Bundle (2) | II | A §2.1.4 (Haydys says "covariant derivative"; the page states both names) |
| Def - The Yang-Mills Field Strength (1) | VII | B §3.3 |
| Def - Gauge Transformation (1) | V | B §2.7 (principal-bundle gauge transformations; the vector-bundle gauge group is `Def - Gauge Group of a Vector Bundle` in II) |

After the series is written: run the repair script over `Study notes/` (excluding the new folder), then the vault-wide link audit; any old target not covered above becomes **bold plain text** with the display text.
