SUMMARY_PROMPT = """
You are an experienced medical assistant.

Summarize the following medical report in simple language.

Medical Report:
{text}

Instructions:
- Explain in simple English.
- Highlight important findings.
- Mention abnormal values if available.
- Do not invent information.
- Mention if the report is incomplete.
- End by reminding the user to consult a healthcare professional.
"""

MEDICINE_PROMPT = """
From the medical report below:

{text}

Identify all medicines mentioned.

For each medicine explain:
- Purpose
- How it generally works
- Common precautions

Do not invent medicines.
"""

DIAGNOSIS_PROMPT = """
Explain every diagnosis mentioned in this report.

{text}

For each diagnosis include:
- Simple explanation
- Possible symptoms
- General treatment approach

Do not add information not present in the report.
"""

LAB_PROMPT = """
Explain every laboratory test in this report.

{text}

For every test explain:
- What it measures
- Why doctors order it
- Whether it appears normal or abnormal based only on the report

If no reference range is provided, avoid making definitive claims.
"""

LIFESTYLE_PROMPT = """
Based only on this medical report,

{text}

Suggest general lifestyle recommendations.

Include:
- Diet
- Exercise
- Sleep
- Hydration
- Follow-up advice

Do not prescribe medicines.
"""

COMPARE_REPORTS_PROMPT = """
You are an experienced medical AI assistant.

Compare the two medical reports below.

Previous Report:
{old_report}

Current Report:
{new_report}

Analyze and organize your response into the following sections:

## Overall Summary

Provide a brief overview of the patient's health progression.

## Improved Parameters

Mention values or conditions that have improved.

## Worsened Parameters

Mention values or conditions that have become worse.

## Newly Observed Findings

Mention findings that appear only in the current report.

## Stable Findings

Mention findings that remained similar.

Do not invent any information.

Base every statement only on the uploaded reports.

End with:

"This comparison is for informational purposes only and should not replace professional medical advice."
"""

TIMELINE_PROMPT = """
You are an experienced medical AI assistant.

Using the two medical reports below, create a chronological health timeline.

Previous Report:
{old_report}

Current Report:
{new_report}

Organize the response using these sections:

## Timeline

Show how important findings changed from the previous report to the current report.

## Key Changes

Highlight significant improvements or deteriorations.

## Overall Trend

Summarize the patient's overall health progression in a few sentences.

Only use information available in the reports.

Do not invent values or dates.

End with:

"This timeline is for informational purposes only and should not replace professional medical advice."
"""

DOCTOR_QUESTIONS_PROMPT = """
You are an experienced medical AI assistant.

Based ONLY on the medical report(s) below, generate questions that the patient may ask during their doctor's appointment.

Current Report:
{current_report}

Previous Report:
{previous_report}

Instructions:

- Generate between 4 and 5 questions.
- Questions should be personalized to the uploaded report(s).
- Focus on:
  - Abnormal laboratory values
  - Diagnoses
  - Medicines
  - Follow-up tests
  - Lifestyle changes
  - Monitoring progress
- Do NOT answer the questions.
- Do NOT diagnose.
- Do NOT recommend treatment.
- If only one report is available, ignore the previous report section.
- Use simple language.

Return the questions as a numbered list.
"""