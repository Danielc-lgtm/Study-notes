# Selecting exercises and research topics

Paths are relative to the repository root. Use `Study notes/Prerequisite DAG.md` as the subject map. A displayed numeric pair means **(familiarity, interest)**, in that order. Missing values are unknown, not zero; do not fabricate scores or infer mastery from the presence of notes. Explicit user requests and recent direct feedback take precedence over default selection.

## Priority order

1. **Self-containedness is a gate.** Reject or narrow a candidate that cannot be made solvable and intelligible from mathematical maturity, basic undergraduate notation, and the context supplied. Specialized subject mastery must not be silently assumed.
2. **Prefer instrumental reuse.** Prioritize definitions, concepts, lemmas, theorems, and algorithms used across many DAG nodes. Inspect prerequisite edges and downstream uses to identify broadly enabling tools, then verify the actual operation each candidate teaches. A node's out-degree is evidence of prerequisite reach, not proof that every theorem in that subject is broadly useful; do not invent graph counts. Judge the concrete operation enabled, not the prestige of a name or an unverified claim that everything is connected. A focused exercise can teach a reusable tool without becoming a multifield exercise.
3. **Advance the learning frontier.** Use the user's familiarity scores, stated gaps, and exercise feedback to aim just beyond current familiarity and toward deeper DAG nodes. Any node is eligible when its prerequisites can be supplied. Do not permanently restrict selection to roots, or jump to a deep topic merely because it sounds advanced. Unknown familiarity remains an uncertainty; provide its prerequisites and use subsequent feedback to calibrate.
4. **Prefer underrepresented subjects over interest.** Among candidates passing the earlier criteria, prioritize less-covered nodes. Use interest to choose among comparably suitable, comparably covered candidates; high interest must not continually crowd out neglected fields.

This is a qualitative priority order, not a fabricated numerical score. Keep the selection rationale in working reasoning or a requested planning response, not as extra exercise sections. Selecting broadly reusable tools is compatible with forbidding visible convergent-strategy classifications, sources/targets apparatus, and bridges.

## Measure actual coverage

Before an unprompted topic choice within an authorized exercise task, inventory existing exercise notes under `Study notes/exercises/`, using the shared exercise metadata and each note's problem and solution. Read `dag_nodes` as a list of exact canonical node names from the DAG; resolve obvious shorthand deliberately rather than creating new nodes. An algorithmic or competitive programming exercise need not claim a DAG node that it does not genuinely exercise.

- Count exercise notes, not category indexes, overview pages, context/concept subpages, research roadmaps, blank `type: format-preview` pages, or links to exercises. Coverage is availability of meaningful practice, not evidence that the user has completed or mastered it.
- Count a node only if solving the exercise requires using its ideas. Mere mention in background, a prerequisite recalled for notation, or a decorative application does not earn coverage. Inspect questionable metadata before relying on it.
- Deduplicate by the underlying problem and intended learning task. Renamed or copied notes and multiple index entries count once. For competitive programming, compare source problem identifier/URL and specification; a distinct, substantive variation may count separately, with the variation identified.
- For a genuine multifield exercise, count one exercise toward each node actually exercised. Do not inflate coverage by listing incidental fields. Compare counts only among eligible candidates; the figures are a guide to balance, not a demand to equalize the entire DAG.
- If older exercise notes lack metadata, inspect them and infer only what their content supports for the current inventory. Record uncertainty; do not treat missing metadata as proof of zero coverage or rewrite unrelated notes merely to make counting easy.

At initial setup the exercise categories may be empty. Verify that condition when selecting rather than treating it as permanent. When coverage is tied, use reuse value, familiarity/gaps, and then interest. Do not generate filler to satisfy a quota.

## Apply selection to the requested workflow

For algorithm reconstruction, choose useful conventional algorithms and advanced data structures within the requested scope, favouring new mechanisms over superficial variants. For competitive programming, choose actual accessible source problems that meet the desired challenge and verify that the supplied context and solution are sufficient.

For interdisciplinary and frontier rediscovery exercises, use the DAG priorities directly. Genuine cross-field composition is welcome but optional. For active research, use the same pedagogical priorities together with the research skill's evidence and tractability requirements; a neglected node alone does not justify an unsupported research direction. Do not count research roadmaps as solved-result exercises.

Before writing a batch, check whether existing exercises already serve the proposed purpose. A user-requested revisit is valid; do not silently create another copy. After writing, maintain `dag_nodes` and the category indexes so the next selection can rely on the actual collection. Preserve user-authored insight and feedback, and use feedback to adjust future difficulty and context rather than guessing how far the user has progressed.
