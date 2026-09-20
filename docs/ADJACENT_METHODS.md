# Adjacent generative approaches — different tasks or model classes

These works add useful comparisons but should not be confused with a native GAN/DDPM load generator. **Dates are journal or preprint months as indicated**, and same-paper arXiv/journal versions are not counted twice in the main catalogue.

| Date | Work | Method and relevance | Article |
|---|---|---|---|
| January 2026 (arXiv) | SmartMeterFM: Unifying Smart Meter Data Generative Tasks Using Flow Matching Models | Flow matching for smart-meter data; **not a DDPM**; multi-task imputation, super-resolution, synthesis | [arXiv](https://arxiv.org/abs/2601.21706) |
| 2026 (month unverified) | Month-long conditioned synthesis of half-hourly household gas and electricity data with an autoregressive transformer (Synthetic-SERL) | Conditioned autoregressive Transformer; **not diffusion Transformer** | [UCL](https://discovery.ucl.ac.uk/id/eprint/10228107/) |
| September 2025 (journal; preprint May 2024) | A flow-based model for conditional and probabilistic electricity consumption profile generation | FCPFlow **normalizing flow**; includes **cWGAN-GP as a benchmark** under continuous conditions including temperature/irradiation; do not count the flow model as a new GAN | [DOI](https://doi.org/10.1016/j.egyai.2025.100586) |
| May 2025 (journal) | Data efficiency assessment of generative adversarial networks in energy applications | Data-size and feature-exclusion sensitivity for cGAN and WGAN in energy; includes load forecasting, not exclusively synthetic load sampling | [DOI](https://doi.org/10.1016/j.egyai.2025.100501) |
| July 2024 (journal issue; preprint August 2023) | DiffCharge: Generating EV Charging Scenarios via a Denoising Diffusion Model | Conditional denoising diffusion for EV battery- and station-level charging profiles; related to electrical load but **not generic residential or grid load synthesis** | [DOI](https://doi.org/10.1109/TSG.2024.3360874) · [Code](https://github.com/LSY-Cython/DiffCharge) |
| 2023 (month unverified) | Generating realistic load profiles in smart grids: An approach based on nonlinear independent component estimation (NICE) and convolutional layers | Invertible flow, not GAN | [DOI](https://doi.org/10.1016/j.apenergy.2023.121902) |
| April 2024 preprint (ACM version 2026) | A Survey on Diffusion Models for Time Series and Spatio-Temporal Data | General review; foundational diffusion taxonomy, **not evidence that electrical-load DiT is new** | [arXiv](https://arxiv.org/abs/2404.18886) |

**Cross-scope prior art:** [Wang et al. 2020](https://doi.org/10.1016/j.epsr.2020.106732) applies **CWGAN-GP** to probabilistic load-forecast residual scenarios (not unconstrained load synthesis); [Sun et al. 2024](https://doi.org/10.1109/EI264398.2024.10991846) uses **cWGAN-GP** for joint source-load scenarios. Both appear in the main list with explicit *adjacent* scope because they are critical to novelty assessment.
