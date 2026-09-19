# Awesome Load Generation Models ⚡

A curated literature list for **synthetic electricity load / consumption data generation**, including GAN, WGAN, WGAN-GP, conditional WGAN-GP, diffusion and diffusion Transformer. / Bibliographie de recherche sur la génération synthétique de charge électrique.

**Last checked: 2026-09-19 · 32 distinct studies** (including explicitly marked adjacent work). This collection is **not exhaustive or a systematic review**. Unverified details say « à vérifier » rather than being invented. Papers are sorted newest → oldest; journal and arXiv versions are deduplicated. Listed model types follow actual methods where identifiable, not title keywords alone.

## Navigation

- [All papers: newest → oldest](#all-papers-newest--oldest)
- [Browse by model family](#browse-by-model-family)
- [Datasets and evaluation](#datasets-and-evaluation)
- [Research and novelty cautions](#research-and-novelty-cautions)

## All papers: newest → oldest

| Year | Model / paper | Family | Dataset / benchmark | Resolution; horizon | Links |
|---:|---|---|---|---|---|
| 2026 | **LoaDiff** — LoaDiff: Conditional Generation of Electricity Consumption Time Series for Energy Analytics<br><sub>Direct; arXiv Sep 2026</sub> | Diffusion conditionnelle | 3 jeux résidentiels | infra-horaire; annuel | [Paper](https://arxiv.org/abs/2609.11639) |
| 2026 | **Temporally-Conditioned DiT** — Temporally-Conditioned Diffusion Transformer for Appliance-Level Load Synthesis in Non-Intrusive Load Monitoring<br><sub>Adjacent appareil/NILM; SSRN Jul 2026</sub> | Diffusion Transformer | Appliances; à vérifier | à vérifier; séquences appareils | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7124192) |
| 2026 | **Seasonal weekly WGAN-GP** — Synthetic Seasonal Weekly Load Profile Generation Based on Advanced Wasserstein-Distance Generative Adversarial Networks<br><sub>Direct; Energies Aug 2026</sub> | WGAN-GP | Irish residential | à vérifier; semaine saisonnière | [Paper](https://doi.org/10.3390/en19153651) |
| 2026 | **AC-WTGAN+** — AC-WTGAN+: A conditional Wasserstein temporal generator for high-quality residential load synthesis<br><sub>Direct; Electric Power Systems Research Jun 2026</sub> | cWGAN-GP | Irish CER | 30 min; 336 pas / semaine | [Paper](https://doi.org/10.1016/j.epsr.2026.113338) |
| 2026 | **LV conditional diffusion** — Coherent load profile synthesis with conditional diffusion for LV distribution network scenario generation<br><sub>Direct; Sustainable Energy Grids and Networks Jun 2026</sub> | Diffusion conditionnelle | Réseau LV | à vérifier; journée | [Paper](https://doi.org/10.1016/j.segan.2026.102264) · [Code/data](https://github.com/strath-ai/lv-synthesis-diffusion) |
| 2026 | **Annual convolutional WGAN** — From Data Scarcity to Scalability: Generating Realistic Building Energy Profiles with GANs<br><sub>Direct; SSRN Jan 2026; version 2025 remplacée</sub> | WGAN (GP à vérifier) | 1300 foyers; PV; PAC; EV | 1 h; annuel 24 × 368 | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6135520) · [Code/data](https://github.com/MODERATE-Project/Synthetic-Load-Profiles) |
| 2026 | **Interpretable diffusion + Transformer** — Long-term scenario generation for distribution network loads based on interpretable diffusion models<br><sub>Direct/scénarios; IJEPES Jan 2026</sub> | Diffusion + Transformer | Réseau distribution | multi-échelle; long terme / annuel | [Paper](https://doi.org/10.1016/j.ijepes.2025.111491) |
| 2026 | **DGAN** — Residential electrical demand data synthesis using the DGAN model: performance evaluation for diverse dwellings<br><sub>Direct; Energy and Buildings Jan 2026</sub> | GAN | Habitations diverses | à vérifier; à vérifier | [Paper](https://doi.org/10.1016/j.enbuild.2025.116722) |
| 2025 | **EnergyDiff** — EnergyDiff: Universal Time-Series Energy Data Generation Using Diffusion Models<br><sub>Direct; IEEE TSG Jun 2025; arXiv 2024</sub> | Diffusion DDPM | Électricité; PAC; PV; consommateur et transformateur | 1; 15; 30; 60 min; à vérifier | [Paper](https://doi.org/10.1109/TSG.2025.3581472) |
| 2025 | **Conv1D-WGAN-GP** — A Data-Driven Approach for Generating Synthetic Load Profiles with GANs<br><sub>Direct; Applied Sciences Jul 2025</sub> | WGAN-GP | 4 datasets industriels; agricoles; résidentiels | à vérifier; 24 h | [Paper](https://doi.org/10.3390/app15147835) |
| 2025 | **SocioDiff** — SocioDiff: A Socio-Aware Diffusion Model for Residential Electricity Consumption Data Generation<br><sub>Direct; IEEE TSG 2025</sub> | Diffusion conditionnelle | Irish CER | 30 min; 336 pas / semaine | [Paper](https://doi.org/10.1109/TSG.2025.3575819) · [Code/data](https://github.com/Intelligame/SocialDiff) |
| 2025 | **PV/EV building cGAN** — Conditional generative adversarial network (cGAN) for generating building load profiles with photovoltaics and electric vehicles<br><sub>Direct; Energy and Buildings 2025</sub> | cGAN | Bâtiments PV/EV | à vérifier; à vérifier | [Paper](https://doi.org/10.1016/j.enbuild.2025.115584) |
| 2025 | **RLP-GAN** — Learning and Generating Diverse Residential Load Patterns Using GAN with Weakly-Supervised Training and Weight Selection<br><sub>Direct; IEEE TCE May 2025</sub> | GAN | 417 foyers | à vérifier; patterns résidentiels | [Paper](https://doi.org/10.1109/TCE.2025.3563272) |
| 2025 | **Activity-based GAN** — Residential Load Modeling With Generative Adversarial Networks<br><sub>Direct/hybride activités vers charge; 2025</sub> | cGAN hybride | Emploi du temps Italie | appareils; journée | [Paper](https://doi.org/10.1109/TSUSC.2025.3605668) |
| 2025 | **Physics-informed diffusion** — Generating Synthetic Net Load Data for Residential Customers With Physics-Informed Diffusion Models<br><sub>Direct/net-load; online 2025; volume 2026</sub> | Diffusion conditionnelle | Pecan Street | à vérifier; à vérifier | [Paper](https://doi.org/10.1109/TSG.2025.3625925) |
| 2024 | **Building metadata diffusion** — Creating synthetic energy meter data using conditional diffusion and building metadata<br><sub>Direct; Energy and Buildings Jun 2024</sub> | Diffusion conditionnelle | 1828 compteurs multi-pays | à vérifier; annuel | [Paper](https://doi.org/10.1016/j.enbuild.2024.114216) |
| 2024 | **Customized load diffusion** — Customized Load Profiles Synthesis for Electricity Customers Based on Conditional Diffusion Models<br><sub>Direct; IEEE TSG Feb 2024; arXiv 2023</sub> | Diffusion conditionnelle | Dataset public à vérifier | à vérifier; à vérifier | [Paper](https://doi.org/10.1109/TSG.2024.3366212) |
| 2024 | **GAN/WGAN/WGAN-GP benchmark** — Comparative assessment of generative models for transformer- and consumer-level load profiles generation<br><sub>Direct benchmark; SEGAN Jun 2024</sub> | Benchmark | Client et transformateur | 15; 30; 60 min; à vérifier | [Paper](https://doi.org/10.1016/j.segan.2024.101338) |
| 2024 | **DGAN + wavelets** — Capturing multiscale temporal dynamics in synthetic residential load profiles through Generative Adversarial Networks (GANs)<br><sub>Direct; Applied Energy Apr 2024</sub> | GAN | Résidentiel (confidentiel) | haute fréquence; annuel puis intrajournalier | [Paper](https://doi.org/10.1016/j.apenergy.2024.122831) |
| 2024 | **ERGAN** — Synthetic Data Generation for Residential Load Patterns via Recurrent GAN and Ensemble Method<br><sub>Direct; IEEE TIM Oct 2024; données synthétiques</sub> | GAN récurrent | Pecan Street 417 foyers | 1 h; journée | [Paper](https://doi.org/10.1109/TIM.2024.3480225) · [Code/data](https://github.com/AdamLiang42/ERGAN-Dataset) |
| 2023 | **MultiLoad-GAN** — MultiLoad-GAN: A GAN-Based Synthetic Load Group Generation Method Considering Spatial-Temporal Correlations<br><sub>Direct; IEEE TSG 2023; données réelles restreintes</sub> | GAN | Groupe de charges / transformateur | à vérifier; à vérifier | [Paper](https://doi.org/10.1109/TSG.2023.3302192) · [Code/data](https://github.com/hughwln/MultiLoad-GAN_public) |
| 2022 | **WDCGAN (GP in loss)** — Energy data generation with Wasserstein Deep Convolutional Generative Adversarial Networks<br><sub>Direct; Energy Oct 2022</sub> | WGAN-GP | Irish residential | 30 min; 7 × 48 pas / semaine | [Paper](https://doi.org/10.1016/j.energy.2022.124694) |
| 2022 | **RCGAN / TimeGAN / CWGAN / RCWGAN** — Synthetic demand data generation for individual electricity consumers: Generative Adversarial Networks (GANs)<br><sub>Direct benchmark; Energy and AI Aug 2022</sub> | GAN / cWGAN | Clients individuels | à vérifier; à vérifier | [Paper](https://doi.org/10.1016/j.egyai.2022.100161) |
| 2022 | **DPWGAN** — DPWGAN: High-Quality Load Profiles Synthesis With Differential Privacy Guarantees<br><sub>Direct; online 2022 / journal 2023</sub> | WGAN + DP | Smart meters | à vérifier; à vérifier | [Paper](https://doi.org/10.1109/TSG.2022.3230671) |
| 2022 | **ProfileSR-GAN** — ProfileSR-GAN: A GAN Based Super-Resolution Method for Generating High-Resolution Load Profiles<br><sub>Direct super-résolution; IEEE TSG 2022</sub> | GAN / super-résolution | Smart-meter LR/HR | haute fréquence; à vérifier | [Paper](https://doi.org/10.1109/TSG.2022.3158235) |
| 2022 | **Time-Variant GAN** — Synthetic Energy Data Generation Using Time Variant Generative Adversarial Network<br><sub>Direct; Electronics Jan 2022</sub> | GAN | Consommation énergétique | à vérifier; à vérifier | [Paper](https://doi.org/10.3390/electronics11030355) |
| 2022 | **Grid stress-testing GAN** — Stress testing electrical grids: Generative Adversarial Networks for load scenario generation<br><sub>Adjacent / scope mix electric inland generation et consumption; Energy and AI Aug 2022</sub> | GAN | Pays européens / variable mixte | 1 h; scénarios multivariés | [Paper](https://doi.org/10.1016/j.egyai.2022.100177) · [Code/data](https://github.com/Advestis/els_paper) |
| 2021 | **Transmission cGAN** — Synthetic Time-Series Load Data via Conditional Generative Adversarial Networks<br><sub>Direct; arXiv 2021</sub> | cGAN | Réseau de transport | 1 h; 1 semaine | [Paper](https://arxiv.org/abs/2107.03545) |
| 2020 | **Clustered GAN** — Generating realistic building electrical load profiles through the Generative Adversarial Network (GAN)<br><sub>Direct; Energy and Buildings Oct 2020</sub> | GAN | Building Data Genome | 1 h; 24 h | [Paper](https://doi.org/10.1016/j.enbuild.2020.110299) |
| 2019 | **R-GAN / WGAN / MH-GAN** — Generating Energy Data for Machine Learning with Recurrent Generative Adversarial Networks<br><sub>Direct; online Dec 2019; Energies vol. 2020</sub> | GAN / WGAN | Consommation énergétique | à vérifier; à vérifier | [Paper](https://doi.org/10.3390/en13010130) |
| 2019 | **ACGAN / Conv GAN** — GAN-based Model for Residential Load Generation Considering Typical Consumption Patterns<br><sub>Direct; ISGT 2019</sub> | cGAN | Irish smart meters | à vérifier; hebdomadaire | [Paper](https://doi.org/10.1109/ISGT.2019.8791575) |
| 2018 | **Demand-side cGAN** — Demand Side Data Generating Based on Conditional Generative Adversarial Networks<br><sub>Direct; Energy Procedia Oct 2018</sub> | cGAN | Compteurs + enquêtes | à vérifier; à vérifier | [Paper](https://doi.org/10.1016/j.egypro.2018.09.157) |

Complete metadata (conditioning, metrics, DOI, scope and code): [catalogue/papers.csv](catalogue/papers.csv). **Do not compare raw metric values across incompatible datasets, scales or evaluation protocols.**

## Browse by model family

### cWGAN-GP / WGAN-GP

- **2026 · Seasonal weekly WGAN-GP** — [Synthetic Seasonal Weekly Load Profile Generation Based on Advanced Wasserstein-Distance Generative Adversarial Networks](https://doi.org/10.3390/en19153651).
- **2026 · AC-WTGAN+** — [AC-WTGAN+: A conditional Wasserstein temporal generator for high-quality residential load synthesis](https://doi.org/10.1016/j.epsr.2026.113338).
- **2025 · Conv1D-WGAN-GP** — [A Data-Driven Approach for Generating Synthetic Load Profiles with GANs](https://doi.org/10.3390/app15147835).
- **2022 · WDCGAN (GP in loss)** — [Energy data generation with Wasserstein Deep Convolutional Generative Adversarial Networks](https://doi.org/10.1016/j.energy.2022.124694).

### GAN, WGAN and other adversarial models

- **2026 · Annual convolutional WGAN** — [From Data Scarcity to Scalability: Generating Realistic Building Energy Profiles with GANs](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6135520).
- **2026 · DGAN** — [Residential electrical demand data synthesis using the DGAN model: performance evaluation for diverse dwellings](https://doi.org/10.1016/j.enbuild.2025.116722).
- **2025 · PV/EV building cGAN** — [Conditional generative adversarial network (cGAN) for generating building load profiles with photovoltaics and electric vehicles](https://doi.org/10.1016/j.enbuild.2025.115584).
- **2025 · RLP-GAN** — [Learning and Generating Diverse Residential Load Patterns Using GAN with Weakly-Supervised Training and Weight Selection](https://doi.org/10.1109/TCE.2025.3563272).
- **2025 · Activity-based GAN** — [Residential Load Modeling With Generative Adversarial Networks](https://doi.org/10.1109/TSUSC.2025.3605668).
- **2024 · DGAN + wavelets** — [Capturing multiscale temporal dynamics in synthetic residential load profiles through Generative Adversarial Networks (GANs)](https://doi.org/10.1016/j.apenergy.2024.122831).
- **2024 · ERGAN** — [Synthetic Data Generation for Residential Load Patterns via Recurrent GAN and Ensemble Method](https://doi.org/10.1109/TIM.2024.3480225).
- **2023 · MultiLoad-GAN** — [MultiLoad-GAN: A GAN-Based Synthetic Load Group Generation Method Considering Spatial-Temporal Correlations](https://doi.org/10.1109/TSG.2023.3302192).
- **2022 · RCGAN / TimeGAN / CWGAN / RCWGAN** — [Synthetic demand data generation for individual electricity consumers: Generative Adversarial Networks (GANs)](https://doi.org/10.1016/j.egyai.2022.100161).
- **2022 · DPWGAN** — [DPWGAN: High-Quality Load Profiles Synthesis With Differential Privacy Guarantees](https://doi.org/10.1109/TSG.2022.3230671).
- **2022 · ProfileSR-GAN** — [ProfileSR-GAN: A GAN Based Super-Resolution Method for Generating High-Resolution Load Profiles](https://doi.org/10.1109/TSG.2022.3158235).
- **2022 · Time-Variant GAN** — [Synthetic Energy Data Generation Using Time Variant Generative Adversarial Network](https://doi.org/10.3390/electronics11030355).
- **2022 · Grid stress-testing GAN** — [Stress testing electrical grids: Generative Adversarial Networks for load scenario generation](https://doi.org/10.1016/j.egyai.2022.100177).
- **2021 · Transmission cGAN** — [Synthetic Time-Series Load Data via Conditional Generative Adversarial Networks](https://arxiv.org/abs/2107.03545).
- **2020 · Clustered GAN** — [Generating realistic building electrical load profiles through the Generative Adversarial Network (GAN)](https://doi.org/10.1016/j.enbuild.2020.110299).
- **2019 · R-GAN / WGAN / MH-GAN** — [Generating Energy Data for Machine Learning with Recurrent Generative Adversarial Networks](https://doi.org/10.3390/en13010130).
- **2019 · ACGAN / Conv GAN** — [GAN-based Model for Residential Load Generation Considering Typical Consumption Patterns](https://doi.org/10.1109/ISGT.2019.8791575).
- **2018 · Demand-side cGAN** — [Demand Side Data Generating Based on Conditional Generative Adversarial Networks](https://doi.org/10.1016/j.egypro.2018.09.157).

### Diffusion and diffusion Transformers

- **2026 · LoaDiff** — [LoaDiff: Conditional Generation of Electricity Consumption Time Series for Energy Analytics](https://arxiv.org/abs/2609.11639).
- **2026 · Temporally-Conditioned DiT** — [Temporally-Conditioned Diffusion Transformer for Appliance-Level Load Synthesis in Non-Intrusive Load Monitoring](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7124192).
- **2026 · LV conditional diffusion** — [Coherent load profile synthesis with conditional diffusion for LV distribution network scenario generation](https://doi.org/10.1016/j.segan.2026.102264).
- **2026 · Interpretable diffusion + Transformer** — [Long-term scenario generation for distribution network loads based on interpretable diffusion models](https://doi.org/10.1016/j.ijepes.2025.111491).
- **2025 · EnergyDiff** — [EnergyDiff: Universal Time-Series Energy Data Generation Using Diffusion Models](https://doi.org/10.1109/TSG.2025.3581472).
- **2025 · SocioDiff** — [SocioDiff: A Socio-Aware Diffusion Model for Residential Electricity Consumption Data Generation](https://doi.org/10.1109/TSG.2025.3575819).
- **2025 · Physics-informed diffusion** — [Generating Synthetic Net Load Data for Residential Customers With Physics-Informed Diffusion Models](https://doi.org/10.1109/TSG.2025.3625925).
- **2024 · Building metadata diffusion** — [Creating synthetic energy meter data using conditional diffusion and building metadata](https://doi.org/10.1016/j.enbuild.2024.114216).
- **2024 · Customized load diffusion** — [Customized Load Profiles Synthesis for Electricity Customers Based on Conditional Diffusion Models](https://doi.org/10.1109/TSG.2024.3366212).

### Benchmark comparisons

- **2024 · GAN/WGAN/WGAN-GP benchmark** — [Comparative assessment of generative models for transformer- and consumer-level load profiles generation](https://doi.org/10.1016/j.segan.2024.101338).

## Datasets and evaluation

| Dataset / artifact | Examples / usage | Resource |
|---|---|---|
| Irish CER smart metering | 30-min residential load; conditional attributes | [ISSDA](https://www.ucd.ie/issda/data/commissionforenergyregulationcer/) |
| Pecan Street | Residential smart-meter / net load | [Pecan Street](https://www.pecanstreet.org/) |
| Building Data Genome | Building load synthesis | [Building Data Genome 2](https://github.com/buds-lab/building-data-genome-project-2) |
| ERGAN-Dataset | One million generated hourly 24-point profiles | [Synthetic data](https://github.com/AdamLiang42/ERGAN-Dataset) |
| MODERATE | Annual hourly residential WGAN generator | [Code](https://github.com/MODERATE-Project/Synthetic-Load-Profiles) |
| LV conditional diffusion | Substation synthesis and power-flow context | [Code](https://github.com/strath-ai/lv-synthesis-diffusion) |

See [evaluation protocol](docs/EVALUATION_PROTOCOL.md) and [selection methodology](docs/METHODOLOGY.md).

## Research and novelty cautions

- **A conditional Wasserstein GAN with gradient penalty for electricity load already exists:** see AC-WTGAN+ (2026), and examine WDCGAN (2022) for its gradient-penalty formulation. Do not claim a bare cWGAN-GP is unprecedented.
- **Conditioning and seasonality:** inspect SocioDiff, LoaDiff, Fu et al., Gu et al., and weekly seasonal WGAN-GP; validate new conditioning-variable selection with held-out ablations and strict no-leakage splits.
- **Multi-resolution:** EnergyDiff explicitly covers 1/15/30/60 min; ProfileSR-GAN studies super-resolution; DGAN+wavelets and annual WGAN cover multi-scale structure. Aggregating 30-min **power** to hourly/daily/monthly is not equivalent to independently modelling each scale; check energy-conservation constraints.
- **Multi-locality:** MultiLoad-GAN captures cross-consumer structure; conditional LV diffusion addresses inter-substation coherence; annual building diffusion uses location metadata. Country-to-country transfer is a separately testable claim.
- **Quality-control protocol:** report stratified Wasserstein, MMD, DTW, ACF and peak behaviour, downstream TSTR/TRTR, multiple pre-registered seeds and privacy tests where relevant. EMA alone is not a novel architecture; test its contribution with an ablation.

## Scope and contributing

Core entries synthesize *electrical demand / load* or explicitly identified *net load*. Closely related appliance generation, grid-variable synthesis and super-resolution are labelled. Forecast-only papers without synthetic sampling, wind/PV-only generation and generic method papers are excluded from the primary list. [Adjacent methods](docs/ADJACENT_METHODS.md) are kept separately. Researchers from every country and source language are eligible; original-language titles and translated titles can be submitted in [CONTRIBUTING.md](CONTRIBUTING.md).

Inspired by [Awesome-TimeSeries-SpatioTemporal-Diffusion-Model](https://github.com/yyysjz1997/Awesome-TimeSeries-SpatioTemporal-Diffusion-Model); independent, electricity-load-specific project.
