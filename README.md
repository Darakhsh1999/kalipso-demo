# Policy Compliance Assessment

## Overview

This take-home assignment involves analyzing a PDF policy document to determine whether it satisfies a set of regulatory requirements for investment firms. You will be provided with a PDF containing a company's policy document, and your task is to assess whether this policy meets all the requirements specified in the `requirements_assignment.json` file.

## Time Expectations

- **Estimated Duration**: 1-5 hours
- **Time Limit**: None - work at your own pace
- **Submission**: Submit to github and add @GMarkfjard to the repo

## Assignment Details

### Your Task

You need to:
1. Review the provided PDF policy document
2. Check if the policy satisfies each requirement listed in `requirements_assignment.json`
3. Create a systematic assessment showing which requirements are met, partially met, or not met
4. Provide clear reasoning for your determinations
5. Any other fun side deliverables


### Deliverables

Your submission should include:

1. **Compliance Assessment Tool**: A script, API endpoint, or executable program that:
   - Takes a PDF file as input
   - Analyzes it against the requirements in `requirements_assignment.json`
   - Outputs a structured assessment showing:
     - Each requirement ID/description
     - Compliance status (Met/Partially Met/Not Met)
     - (Optional) Evidence from the PDF supporting your determination
     - Any gaps or missing elements
     - Suggestions for amendments
   
   Examples of acceptable implementations:
   - Python script: `python assess_compliance.py policy.pdf`
   - REST API: `POST /assess` with PDF upload
   - CLI tool: `./compliance-checker --pdf policy.pdf`
   - Web interface with PDF upload functionality

2. **Output Format**: Your tool should produce a clear, structured output such as:
   - JSON report with compliance results
   - Markdown formatted assessment
   - HTML report
   - CSV with requirement mappings

## Technical Guidelines

### API Usage
- An API key is provided for making necessary API calls within the assignment
- **Important**: The API key is restricted and rate-limited
- The key will expire in 7 days
- Use the key only for the analysis, it is not intended to be used as a API key for any dev tooling.
- API key is found in .env
- You may use any gpt-4.1* model from OpenAI

### AI Assistance
- You are welcome to use AI tools to assist with this assignment
- Be transparent about which tools you used and how
- The focus is on your analytical approach and reasoning

## Submission Instructions

Please submit:
1. All source code with clear documentation
2. The `assignment.md` file (see below)
3. Any additional documentation you feel is relevant

### Required: assignment.md

You must include an `assignment.md` file in your submission that contains:

1. **How to Run Your Project**:
   - Step-by-step instructions to run any code you've written
   - Required dependencies and how to install them
   - Environment setup instructions
   - Example commands to execute your solution

2. **Reflection**:
   - What you would do differently with more time
   - Any improvements you'd make to your approach
   - Lessons learned from the assignment
   - Keep it brief, we will dive deeper in our call

This file is intended to help us prepare for the technical followup call.

## Questions?

If you have questions about the assignment requirements or technical issues, please reach out to gabriel@kalipso.ai.

Good luck with your assessment!