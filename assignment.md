# Kalipso Case Study Solution

## How to run

### Install dependencies

To install dependencies, navigate to the project root directory and run:
```bash
uv sync
```

Activate the virtual environment:
```bash
source .venv/bin/activate
```

### Run (in separate terminal windows)

To run the backend application, navigate to /src and run:
```bash
uvicorn fastapi_server:app --reload
```

To run the frontend application, navigate to /src and run:
```bash
streamlit run frontend.py
```
Open up in browser at localhost


## Reflection


### What you would do differently with more time / Any improvements you'd make to your approach
- Kolla igenom fler policy dokument och se om vi kan identifiera en gemensam struktur. Detta kan användas för att identifiera delar av dokumentet som är relevant för vilket krav, vilket ger oss möjligheten att inte behöva skicka hela dokumentet till LLM (sparar tokens).
- För några dokument & krav, skapa ett validerings dataset för att kunna få någon estimering av prestanda (F1, accuracy, recall etc.)
- Eftersom fokus inte var på frontend, gjorde jag den väldigt minimal. Utvecklings områden för kommunikation mellan frontend och backend kan vara att skicka "update" omkring progress och status. Just nu sker allt i ett enda API call.
- Om vi antar att vi har många användare, så kan vi implementera en job queue för att hantera flera användare samtidigt. Samt göra asynkroniserade calls till OpenAI LLM, vilket minimerar thread blocking i vår backend.
- Implementera en caching lager för att inte behöva köra samma LLM-analys flera gånger med samma input (policy). Detta hanteras på OpenAI's sida (finns prompt-struktur som tillåter detta)
- Denna demo fokuserade enbart på "investment firms" krav, men vi kan implementera en DB för att separera olika krav (investment firms, bank, insurance etc.). Men kanske vill vi ha support för "banks" och "insurance" också. Då kan vi antingen skapa en "tag" i vår frontend som säger vilken DB vi ska använda för att läsa in våra krav, eller så kan vi försöka estimera tag utifrån klassifikation av policy dokumentet (document classifier).
- Testade olika PDF readers, alla vara inte perfekta men pdfminer var den bästa. Kan lägga ner lite tid för att se om man kan få en bättre text extractor, så att vi kan undvika att göra en API call för summering.
- Just nu är lösningen lite "brute force" där vi för varje krav skickar en API call till OpenAI LLM. Värt att investigera smarta lösningar på att matcha krav mot sektioner i policy dokumentet. Vi kommer inte undvika API calls till OpenAI, men vi kan försöka att göra detta mer effektivt genom att endast filtrera ut delar av dokumentet som är relevant för vilket krav vi vill analysera. Metoder för att kunna etablera detta:
    1. Kör en parvis cross-encoder för att beräkna ett relevance score mellan våra krav. Konstruera en graf där liknande krav har hög relevance score mellan sig. Detta kan tillåta oss att skicka flera liknande krav samtidigt istället för ett krav i taget. 
    2. Kombinera ovan lösning med similarity search.
        2.1 sektionera policy dokumentet
        2.2 för varje krav kör en similarity search mot sektionerna i dokumentet och assign kravet till sektionen med högst relevance score.
        2.3 Om ett krav har grannar (hög edge weight i grafen) som ligger i andra sektioner av dokumentet, mata in dem delarna också I LLM vid analys. 
    
     
Excalidraw doodle: https://excalidraw.com/#json=bTXEFq-NOTjBF7L4EfeIc,ApGVPGe0qSBxYXgx8hau1w


### Lessons learned from the assignment
- Har personligen mest implementerat lösningar som kör allt lokalt, alltså `python assess_compliance.py policy.pdf` implementatoiner. Så att bygga upp en faktiskt backend som kommunicerar med en frontend är något relativt nytt för mig.
