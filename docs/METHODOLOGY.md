# Literature collection methodology · 2026-09-19

This is a **curated and non-exhaustive snapshot, not PRISMA-compliant systematic screening**. Literature search used publisher/DOI pages, preprints, university records, reference lists and code repositories, in English and French queries (with international research regardless of source language). Elicit API access was unavailable. A publisher DOI or original preprint is preferred; **do not copy copyrighted PDFs into this repository**.

## Scope and deduplication

**Core:** papers empirically generating electricity consumption/load or explicit net-load sequences, or direct benchmark comparisons. **Adjacent:** probabilistic forecast residuals, joint source-load, appliance/NILM, super-resolution and related flow methods — all labelled, not treated as direct substitutes. **Exclude:** pure point forecasting without sampling, solar/wind-only generation and generic method papers. Reviews are separate in [reviews.csv](../catalogue/reviews.csv).

Each intellectual work has one record. Prefer a confirmed journal version while recording earlier preprint date in the notes. **Date fields:** year, month (01–12), publication_date (YYYY-MM), date_precision (online versus issue/claimed date). If only year is verified, month and publication_date are blank; order unknown months last within that year. Journal issue month does not establish online-first month automatically. Cite original title in its published language, optionally followed by translation.

## Quality and novelty evidence

Source-verified identifiers do **not automatically verify** every metric, resolution, code artefact, or exact model loss. Explicit “à vérifier” remains where evidence is insufficient. A conditional WGAN with gradient penalty should be tagged cWGAN-GP only when the source establishes both conditions and GP; cluster-specific standalone WGAN-GPs should not be automatically reclassified. Likewise a Transformer generator is not a DiT unless reverse diffusion is implemented.

Track dataset geography, physical target, units, sampling granularity, horizon, conditioning features, evaluation definitions, code/data access and scope. Distinguish *loss Wasserstein used during training* from *Wasserstein evaluated on generated samples*. The 2025 Conv1D-WGAN-GP paper’s quality thresholds are empirical heuristics, not universal normalised standards.

Relevant comparison starting points: [Turowski et al. 2024](https://doi.org/10.1016/j.rser.2024.114842) (169 energy synthesis papers), [Zhang et al. 2025](https://doi.org/10.1016/j.apenergy.2024.125059) (228 deep generative energy applications), [Stenger et al. 2024](https://doi.org/10.1186/s40537-024-00924-7) (83 evaluation measures). Read full texts and use forward/backward citation tracking before any novelty assertion. The catalogue is **not an accuracy ranking**.

## Current state and reproducibility

The catalogue counts 35 original studies (including labelled adjacent examples), plus 11 reviews. The [quality-control comparison](QUALITY_CONTROL_LITERATURE.md) and [GATE-LOCO](GATE_LOCO.md) distinguish published facts from proposed experiments and previously reported notebook observations. GATE-LOCO numerical notes have **not been independently validated against the working notebooks** here.

When contributing a paper: provide stable DOI/preprint, original title, month source and precision, target variable, exact training objective and GP, benchmark, resolution, horizon, conditioning and metrics **with units/definitions**, code/data and direct/adjacent tag. Treat dates of preprints and journal publications separately.
