import os
from openai import OpenAI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from output_structure import ComplianceAssessment
from prompts import SYSTEM_PROMPT_SUMMARY, SYSTEM_PROMPT_POLICY_TYPE


load_dotenv()
client = OpenAI()


def remove_nonrelevant_text(text: str) -> str:
    response = client.chat.completions.create(model="gpt-4.1",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT_SUMMARY},
        {"role": "user", "content": "Remove all non-relevant text from the following text: \n\n" + text}
    ])
    return response.choices[0].message.content


def predict_compliance_status(requirement: str, policy_text: str) -> dict:
    llm = ChatOpenAI(model="gpt-4.1", temperature=0).with_structured_output(ComplianceAssessment)
    messages = [
        ("system", SYSTEM_PROMPT_POLICY_TYPE.format(requirement=requirement, policy=policy_text)),
    ]
    try:
        response = llm.invoke(messages)
        try:
            response_dict = {
                "requirement_id": hash(requirement),
                "requirement_description": requirement,
                "compliance_status": response.compliance_status,
                "evidence": response.evidence,
                "missing_elements": response.missing_elements,
                "amendments": response.amendments,
            }
            return response_dict
        except Exception as e:
            return {
                "requirement_id": hash(requirement),
                "requirement_description": requirement,
                "error": f"Output structure error: {e}"
            }
    except Exception as api_err:
        return {
            "requirement_id": hash(requirement),
            "requirement_description": requirement,
            "error": f"OpenAI API error: {api_err}"
        }


if __name__ == "__main__":

    # load policy text
    from document_loader import extract_text_from_pdf, load_requirements
    policy_text = extract_text_from_pdf("fake_policy.pdf")

    requirements = load_requirements("requirements_assignment.json")
    requirement = requirements[0]["requirement_description"]


    # remove non-relevant text
    print("Removing non-relevant text...")
    policy_text = remove_nonrelevant_text(policy_text)

    with open(os.path.join("outputs","policy_text.txt"), "w") as f:
        f.write(policy_text)


    # predict compliance status
    print("Predicting compliance status...")
    compliance_status = predict_compliance_status(requirement, policy_text)
    print(compliance_status)
