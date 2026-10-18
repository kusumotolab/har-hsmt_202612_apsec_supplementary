# Prompts (English Translation)

> **Note:** The evaluation in the paper was conducted using the **Japanese prompts** ([prompts_ja.md](prompts_ja.md)). This file is an English translation provided for reference. Outputs obtained with the English prompts may differ from those reported in the paper.

- Text in square brackets (e.g., `[Contents of the minutes of the first meeting]`) is a placeholder. The actual project data was inserted at these positions.
- Category names have been replaced with `Category 1` to `Category 10` for confidentiality.
- The system prompt is set at the beginning of the conversation, and the prompts are then input sequentially (Turn 1 → Turn 14) as a multi-turn conversation.

---

## Execution Order

| Turn | Step in the paper | Purpose |
|---|---|---|
| System | — | Set the role of the LLM and instruct it to respond consistently across the 14 prompts |
| 1 | STEP 1 | Explain the overall task, analysis procedure, conditions, and output format |
| 2 | STEP 1 | Input and analyze the minutes of the 1st meeting |
| 3 | STEP 1 | Input and analyze the minutes of the 2nd meeting |
| 4 | STEP 1 | Organize the results so far |
| 5 | STEP 1 | Input and analyze the minutes of the 3rd meeting |
| 6 | STEP 1 | Organize the results so far |
| 7 | STEP 1 | Input and analyze the minutes of the 4th meeting |
| 8 | STEP 1 | Organize the results so far |
| 9 | STEP 1 | Input and analyze the minutes of the 5th meeting |
| 10 | STEP 1 | Output the IRM (referred to in the prompts as the "GPT version of the requirements specification") |
| 11 | STEP 2 | Explain the review procedure and evaluation criteria |
| 12 | STEP 2 | Input the actual SRS |
| 13 | STEP 2 | Review: IRM → SRS |
| 14 | STEP 2 | Review: SRS → IRM |

## Terminology

| Term in the prompts | Term in the paper |
|---|---|
| GPT version of the requirements specification | Integrated Reference Model (IRM) |
| actual requirements specification | Software Requirements Specification (SRS) |
| minutes | meeting minutes (related artifacts) |

---

## System Prompt

```text
You are an expert in software requirements definition and review.
You will now receive 14 prompts in sequence.
Taking into account each prompt and all of your own previous responses, provide consistent responses.
```

## Turn 1

```text
We will now ask you to perform a task: reviewing whether a requirements specification contains all the necessary requirements and does not contain any unnecessary ones.
The overall flow of this task is as follows.
1. I will input the minutes of all five meetings on which the requirements specification was based.
   Then, based solely on the contents of the minutes as a whole, output a list of the requirements that should be included in the requirements specification, without omission.
   Hereafter, this output list of requirements is referred to as the "GPT version of the requirements specification."
2. After the GPT version of the requirements specification has been output, I will input the actual requirements specification.
   After that input, perform the following two reviews.
   In the first review, output which requirement in the actual requirements specification each requirement in the GPT version of the requirements specification corresponds to.
   In the second review, output which requirement in the GPT version of the requirements specification each requirement in the actual requirements specification is included in.

Next, I will explain how the minutes are analyzed to output the GPT version of the requirements specification in step 1 of the task above.
The flow is as follows.
1. I will input the minutes of the first meeting.
   Analyze the contents of these minutes, and extract and output all items that correspond to requirements.
2. I will input the minutes of the second meeting.
   Analyze the contents of these minutes, and extract and output all items that correspond to requirements.
3. I will input "Please organize the contents, taking into account everything up to the previous input."
   Organize the contents of the requirement-related items extracted from the minutes of the first and second meetings.
4. I will input the minutes of the third meeting.
   Analyze the contents of these minutes, and extract and output all items that correspond to requirements.
5. I will input "Please organize the contents, taking into account everything up to the previous input."
   Organize the contents of the requirement-related items extracted from the minutes of the first, second, and third meetings.
6. I will input the minutes of the fourth meeting.
   Analyze the contents of these minutes, and extract and output all items that correspond to requirements.
7. I will input "Please organize the contents, taking into account everything up to the previous input."
   Organize the contents of the requirement-related items extracted from the minutes of the first, second, third, and fourth meetings.
8. I will input the minutes of the fifth meeting.
   Analyze the contents of these minutes, and extract and output all items that correspond to requirements.
9. I will instruct you to output the requirements specification based on the contents of the minutes of all five meetings.
   Based solely on the results of analyzing the minutes of all five meetings, list and output only the necessary requirements.

The conditions for analyzing the minutes are as follows.
・Extract from the minutes only the items that are likely to be treated as a single requirement in the requirements specification, and analyze and classify each item by function in the form "Function name / Function category / Description / Function status (Decided / Under consideration)."
・Regarding the function status, if there is wording such as "under consideration" or an equivalent expression, judge that function to be under consideration.
・Never refer to any information other than the minutes input so far (do not add anything on your own that is not written in the minutes).
・The function categories are as follows:
    ・Category 1
    ・Category 2
    ・Category 3
    ・Category 4
    ・Category 5
    ・Category 6
    ・Category 7
    ・Category 8
    ・Category 9
    ・Category 10

A simple example of analyzing minutes is also provided below.
The input will not necessarily take this form, but be sure to follow the output format of this example.
Input---------------------------------
# Category 1
    ・Requirement A
    ・Requirement B

Output---------------------------------
**Function name**: Requirement A
   - **Function category**: Category 1
   - **Description**: xxxxx
   - **Function status**: Decided

**Function name**: Requirement B
   - **Function category**: Category 1
   - **Description**: xxxx
   - **Function status**: Decided

For minutes like these, "Requirement A" and "Requirement B" are each treated as an independent requirement belonging to Function Category 1.

We will now begin inputting the minutes.
The minutes will be input in Markdown notation.
For this input, reply with just "Yes."
```

## Turn 2

```text
The following are the minutes of the first meeting.
Analyze them based on the conditions input earlier.

[Contents of the minutes of the first meeting]

Now analyze the requirement-related items in these minutes and output the results.
```

## Turn 3

```text
The following are the minutes of the second meeting.
Analyze them based on the conditions input earlier.

[Contents of the minutes of the second meeting]

Now analyze the requirement-related items in these minutes and output the results.
```

## Turn 4

```text
Please organize the contents, taking into account everything up to the previous input.
```

## Turn 5

```text
The following are the minutes of the third meeting.
Analyze them based on the conditions input earlier.

[Contents of the minutes of the third meeting]

Now analyze the requirement-related items in these minutes and output the results.
```

## Turn 6

```text
Please organize the contents, taking into account everything up to the previous input.
```

## Turn 7

```text
The following are the minutes of the fourth meeting.
Analyze them based on the conditions input earlier.

[Contents of the minutes of the fourth meeting]

Now analyze the requirement-related items in these minutes and output the results.
```

## Turn 8

```text
Please organize the contents, taking into account everything up to the previous input.
```

## Turn 9

```text
The following are the minutes of the fifth meeting.
Analyze them based on the conditions input earlier.

[Contents of the minutes of the fifth meeting]

Now analyze the requirement-related items in these minutes and output the results.
```

## Turn 10

```text
Based on all the inputs so far, extract only the requirements you have judged to be necessary, completely and without omission, and output the requirements specification.
Also output the items that are under consideration.
Include only functional requirements in the requirements specification you output.
Also, describe the requirements grouped by function category.

Output the requirements specification in the following output format.
Output---------------------------------
# Requirements Specification
## Functional Requirements
### Function Category A
- Requirement A-1
    - Description of Requirement A-1
- Requirement A-2
    - Description of Requirement A-2
- Requirement A-3
    - Description of Requirement A-3
### Function Category B
- Requirement B-1
    - Description of Requirement B-1
- Requirement B-2
    - Description of Requirement B-2
- Requirement B-3
    - Description of Requirement B-3
- Requirement B-4
    - Description of Requirement B-4
- Requirement B-5
    - Description of Requirement B-5
```

## Turn 11

```text
Next, using the GPT version of the requirements specification, review whether the actual requirements specification that I will now input properly contains the necessary information.
Specifically, compare the correspondence between the descriptions in the two documents.

~Review procedure~
1. Review whether the descriptions in the GPT version of the requirements specification are included in the actual requirements specification.
2. Review whether the descriptions in the actual requirements specification are included in the GPT version of the requirements specification.

~Evaluation criteria~
When checking whether the contents of Requirements Specification A are included in Requirements Specification B:
・If the item in A is definitely included as an item in B: ○
・If it cannot be stated with certainty that the item in A is included as an item in B, but it can be inferred to be a similar item: △
・If the item in A is definitely not included as an item in B: ×

For this input, reply with just "Yes."
```

> ○, △, and × are marks commonly used in Japan, meaning "included," "possibly included (similar item)," and "not included," respectively.

## Turn 12

```text
I will now input the actual requirements specification. Note that the requirements specification has been converted into Markdown format.
A concrete example is shown below.
# Function category name
- Requirement A
    - Requirement A1 (this is a smaller requirement included in Requirement A)
- Requirement B

The following is the actual requirements specification.

[Contents of the requirements specification]

Do not perform the review yet in your output for this input.
```

## Turn 13

```text
Now, perform the task corresponding to step 1 of the review procedure: checking whether the requirements in the GPT version of the requirements specification are described in the actual requirements specification.
Be sure to review every functional requirement in the GPT version of the requirements specification that you generated earlier.
Never review items that were not extracted as necessary requirements.
```

## Turn 14

```text
Now, perform the task corresponding to step 2 of the review procedure: checking whether the requirements in the actual requirements specification are described in the GPT version of the requirements specification.
This time as well, be sure to review every functional requirement in the actual requirements specification.
```