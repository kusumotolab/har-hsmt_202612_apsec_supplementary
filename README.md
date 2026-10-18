# Supplementary Material: LLM-Assisted Completeness Review of SRS Using Related Artifacts

This repository provides supplementary material for the following paper:

> H. Hashimoto, S. Kusumoto, S. Matsumoto, Y. Saito, Y. Kita, and K. Takeda. "An LLM-Assisted Method for Completeness Review of Software Requirements Specifications Using Related Artifacts." In *Proceedings of the 33rd Asia-Pacific Software Engineering Conference (APSEC 2026)*, SEIP Track, 2026.

It contains the LLM prompts used in the paper (in Japanese and English) and the source code used to send them to the LLM.

---

## Overview

The method supports the completeness review of a Software Requirements Specification (SRS) by checking its consistency with related artifacts (in this study, meeting minutes). It consists of three steps:

| Step | Description | Executed by |
|---|---|---|
| STEP 1 | Build an Integrated Reference Model (IRM) by incrementally summarizing and integrating the related artifacts | LLM |
| STEP 2 | Establish bidirectional correspondences between IRM requirements and SRS requirements, and derive *candidate missing requirements* and *candidate unsubstantiated requirements* | LLM |
| STEP 3 | Verify the candidates against the original artifacts | Human reviewer |

This repository covers STEP 1 and STEP 2.

---

## Repository Structure

```
.
├── README.md
├── prompts/
│   ├── prompts_ja.md   # Japanese prompts used in the paper
│   └── prompts_en.md   # English translation, execution order, and terminology
└── src/
    └── comp_review.py  # Source code used to send the prompts to the LLM (prompt contents removed)
```

---

## Prompts

The method is executed as a single multi-turn conversation consisting of a system prompt and 14 prompts (Turns 1–10: STEP 1, Turns 11–14: STEP 2).

- [`prompts/prompts_ja.md`](prompts/prompts_ja.md): **Japanese prompts** used in the paper. For publication, the wording and notation have been edited for readability and consistency without changing the content of the instructions.
- [`prompts/prompts_en.md`](prompts/prompts_en.md): **English translation** for reference, together with the execution order of the turns and the mapping between the terms used in the prompts and those used in the paper.

The paper reports results obtained with the Japanese prompts. Outputs obtained with the English translation may differ from those reported in the paper.

Project-specific content (the meeting minutes, the SRS, and the names of the function categories) has been replaced with placeholders.

---

## Source Code

[`src/comp_review.py`](src/comp_review.py) is the Python script used for the evaluation in the paper. It sends the system prompt and the 14 prompts to the LLM in order as a single multi-turn conversation via the OpenAI Responses API, accumulating the conversation history, and saves the output of each turn together with the total execution time.

The contents of the prompt variables (`prompt1` to `prompt14`) have been removed from the script because they contained confidential project data. Their contents correspond to Turns 1–14 in [`prompts/prompts_ja.md`](prompts/prompts_ja.md). The script is provided for reference and is not intended to be run as is.

### Model Settings

| Item | Value |
|---|---|
| Model | `gpt-5`  |
| API | OpenAI Responses API |
| Reasoning effort | `high` |
| Other parameters | API defaults |

LLM behavior may change across model updates. Using a different model or version may produce different outputs.

---

## Data

The project data used in the paper (meeting minutes and SRS) was provided by an industrial partner and is not included in this repository due to confidentiality.

---

## Citation

If you use this material, please cite the paper above.

## License

No license is granted for the contents of this repository. All rights are reserved by the authors. For any use beyond viewing, please contact the authors.

## Contact

Haruki Hashimoto, Graduate School of Information Science and Technology, The University of Osaka — har-hsmt@ist.osaka-u.ac.jp