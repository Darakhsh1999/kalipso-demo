from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from output_structure import ComplianceAssessment
from document_loader import load_requirements, extract_text_from_pdf
from llm_calls import remove_nonrelevant_text, predict_compliance_status

app = FastAPI(
    title="Policy Compliance Assessment API",
    description="API for assessing compliance of policy PDFs against regulatory requirements using LLMs.",
    version="0.1.0"
)

DEBUG = False # Set to False when deploying, DEBUG=True will only process 4 requirements

# CORS settings (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/assess")
async def assess_policy(file: UploadFile = File(...)):
    """
    Receives a policy PDF, processes it, and returns compliance assessment.
    (Business logic to be implemented)
    """
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are accepted.")
    else:
        print("Received PDF file: ", file.filename)
    

    # Extract policy text from PDF
    policy_text = extract_text_from_pdf(file.file)

    # (Optional) Preprocess policy text by removing non-relevant text
    policy_text = remove_nonrelevant_text(policy_text)

    # Load requirements
    requirements = load_requirements("requirements_assignment.json")
    
    # Assess each requirement (brute force)
    requirement_status: list[ComplianceAssessment] = []
    for idx, requirement in enumerate(requirements):

        print("Processing requirement idx", idx)

        if DEBUG and (idx > 3):
            print("Finished processing requirements")
            break

        # Call LLM to assess requirement
        requirement_assessment = predict_compliance_status(requirement["requirement_description"], policy_text)
        requirement_status.append(requirement_assessment)

    return JSONResponse(content={"requirement_status": requirement_status})
