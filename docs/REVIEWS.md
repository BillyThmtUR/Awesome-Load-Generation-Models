# Reviews, surveys and evaluation literature

**11 curated review or comparative-guide records**, newest first. These are **separate** from original load generation studies in [papers.csv](../catalogue/papers.csv): a literature survey is not a load generator. Date = first established online month unless otherwise specified; where the issue month differs it is explicitly noted. No claim of completeness.

| Date | Article | Coverage / reason to read | Link |
|---|---|---|---|
| September 2026 | **Synthetic data generation: A tertiary study** | Across 17 evaluated reviews, reports gaps in evaluation protocols, privacy, diversity, reproducibility<br><sub>general synthetic data; not load-specific</sub> | [Paper](https://doi.org/10.1016/j.ipm.2026.104715) |
| June 2026 | **A comprehensive survey on generative AI for power systems: Methods, applications, and emerging trends** | GAN, VAE, diffusion, LLMs; transfer / physical constraints<br><sub>broader power systems; accepted online 02 June 2026</sub> | [Paper](https://doi.org/10.26599/CAI.2026.9390018) |
| April 2026 | **Generative AI and LLM applications in renewable energy and smart grids: a systematic review for the sustainable energy transition** | 106 GenAI/LLM studies across energy application clusters<br><sub>broad energy, includes forecasting and data generation</sub> | [Paper](https://doi.org/10.1007/s10462-026-11545-2) |
| February 2025 | **Deep generative models in energy system applications: Review, challenges, and future directions** | 228 works; data generation, forecasting, awareness, modelling and decision support<br><sub>broader energy systems</sub> | [Paper](https://doi.org/10.1016/j.apenergy.2024.125059) |
| September 2024 | **A Comprehensive guide to Generative Adversarial Networks (GANs) and application to individual electricity demand** | Compares GAN variants and proposes average coverage error (ACE) for individual load sequences<br><sub>direct load; includes evaluation criteria</sub> | [Paper](https://doi.org/10.1016/j.eswa.2024.123851) |
| August 2024 | **Generating synthetic energy time series: A review** | 169 papers; generation method / characteristics / use case / evaluation; calls for standardization<br><sub>online 30 August 2024; issue December 2024</sub> | [Paper](https://doi.org/10.1016/j.rser.2024.114842) |
| June 2024 | **Privacy Mechanisms and Evaluation Metrics for Synthetic Data Generation: A Systematic Review** | 105 studies, mechanisms and privacy metrics<br><sub>general synthetic data; June 2024</sub> | [Paper](https://doi.org/10.1109/ACCESS.2024.3417608) |
| May 2024 | **Evaluation is key: a survey on evaluation measures for synthetic time series** | 83 measures from 56 works; fidelity, coherence, diversity, utility, privacy; no universal protocol<br><sub>general time series; evaluation-centered</sub> | [Paper](https://doi.org/10.1186/s40537-024-00924-7) |
| April 2024 | **A Survey on Diffusion Models for Time Series and Spatio-Temporal Data** | Conditioned/unconditioned and generation vs forecasting; model taxonomy<br><sub>preprint April 2024; ACM journal version 2026 DOI 10.1145/3783986</sub> | [Paper](https://arxiv.org/abs/2404.18886) |
| February 2023 | **Generative Adversarial Networks in Time Series: A Systematic Literature Review** | GAN architectures, evaluation and privacy<br><sub>online February 2023; accepted-manuscript 2022; issue October 2023</sub> | [Paper](https://doi.org/10.1145/3559540) |
| January 2021 | **A Comprehensive Review of Residential Electricity Load Profile Models** | 32 residential load-profile models; privacy, data access and modelling taxonomy<br><sub>many non-generative models; useful background</sub> | [Paper](https://doi.org/10.1109/ACCESS.2021.3050074) |

## How to use this for an academic novelty claim

- **Domain-specific**: Turowski et al. (169 works) and Zhang et al. (228 energy works) document the large prior body; do a systematic backward and forward citation search instead of relying on the 35 curated original-study records alone.
- **Evaluation**: Stenger et al. catalogue 83 measures and explicitly find no universal procedure. Yilmaz & Korn propose the *average coverage error* (ACE) for GAN selection on individual electricity demand. Missing a single metric ≠ evidence no one evaluated load generation.
- **Diffusion / DiT**: Yang et al. map methods by conditioning, generation vs forecasting and temporal vs spatio-temporal data. The April 2024 arXiv and 2026 journal version represent **one work**.
- **Privacy / utility**: report separately from fidelity; a synthetic series can be realistic yet leak household-specific information.
