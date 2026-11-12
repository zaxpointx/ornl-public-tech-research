# Grid resilience and wildfire detection

## Plain-language summary

ORNL is building tools that look for small, dangerous changes in electrical signals before they become equipment failures, outages, or wildfires.

## What the public record shows

The AWARE work analyzes power-grid waveforms. ORNL says its methods can detect and classify seven kinds of faults, including low-current arcing that traditional systems may miss. In one test using utility data, the method increased the visible signal strength from 6% to 72%. [S26]

The project used more than 5,700 waveform signatures in the Grid Event Signature Library. ORNL says the work was tested on a small utility dataset and was being checked against five years of field data from Southern California Edison. [S26]

ORNL describes a planned open-source data-analytics toolbox for researchers and utilities. The project team named in the article includes Ali Ekti, Ozgur Alaca, Ali Boyaci, Aaron Wilson, and Omer Aziz. [S26]

## Why it connects to the atlas

The workflow is:

```text
waveform data -> signal cleanup -> event detection -> classification -> utility alert -> human response
```

That connects public data, machine learning, utility operations, safety, and technology transfer. The system is not just a prediction model. It is meant to turn a hard-to-see signal into an action that a person can review.

## Unknowns

- The public evidence does not establish the final deployment status of AWARE.
- It does not show the complete training dataset or utility integration design.
- A research result is not proof that every wildfire can be predicted or prevented.

## Safe study path

Use synthetic waveforms with labeled anomalies. Add a review step before any alert is treated as real. Measure false alarms, missed events, confidence, and what happens when the data format changes.
