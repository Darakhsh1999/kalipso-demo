# Kalipso Case Study Solution

## How to run

### Install dependencies

To install dependencies, navigate to the root directory and run:
```bash
uv sync
```

### Run

To run the backend application, run:
```bash
uvicorn src.fastapi_server:app --reload
```

To run the frontend application, run:
```bash
streamlit run src/frontend.py
```


## Reflection


### What you would do differently with more time


### Any improvements you'd make to your approach


### Lessons learned from the assignment


## Personal notes

- Givet ett policy dokument, skulle det vara bra att ha ground truth data för att kunna jämföra mot compliance status. Svårt att säga hur bra vår prestanda är nu utan någon domänexpert att jämföra mot.
- implementera caching för att inte behöva köra samma LLM-analys flera gånger med samma input (policy)
- Skapa flera DB för att separera olika krav (investment firms, bank, insurance etc.)
- Frontend och backend kan kommunicera via % complete
- värt att leka runt med olika PDF readers (pdfplumber, pdfminer, PyPDF2) och see vilken som är bäst
- sektionera PDF indata i olika delar för att kunna köra LLM-analys på mindre delar.
    - behöver dock veta vilka delar som är relevant för vilket krav
- skicka alla krav genom en cross-encoder för att beräkna ett relevance score. Konstruera en graf där liknande krav har hög relevance score mellan sig
- investigera om policy dokument finns i en viss struktur, där vi kan sektionera indatan på ett mer strukturerat sätt.
- om vi antar att vi har väldigt många användare, så kan vi implementera LLM invokationen via async där vi skickar ut flera API calls samtidigt. Detta minimerar thread blocking och vi kan eventuellt hantera flera användare samtidigt.