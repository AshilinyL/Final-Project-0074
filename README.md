RECIPE FINDER APP - FINAL PROJECT
==================================

A Dockerized ML application that finds recipes based on ingredients.

HOW TO RUN:
-----------
1. Make sure Docker Desktop is running
2. Open terminal in project folder
3. Run: python init_database.py
4. Run: docker-compose up --build
5. Open: http://localhost:7860

FIRST TIME NOTES:
-----------------
- Will download ML models (~300MB) - be patient
- Might take 2-3 minutes to start
- Ignore some warnings if things still work

TROUBLESHOOTING:
----------------
If docker-compose fails:
1. Check Docker Desktop is running
2. Make sure files are in correct folders
3. Try: docker-compose down (then up again)

If no recipes found:
1. Check data/recipes.json exists
2. Try different ingredients

TEST WITH:
----------
Ingredients: chicken, rice, vegetables
Preference: savory
Appliance: pan

PROJECT STRUCTURE:
------------------
recipe_project/
├── docker-compose.yml    # Docker config
├── init_database.py     # Setup script (this)
├── backend/            # ML API
├── frontend/           # Web interface
└── data/              # Recipe data

TECH STACK:
-----------
- FastAPI (backend)
- Gradio (frontend)
- Sentence-BERT (ML)
- ChromaDB (vector database)
- Docker (containerization)

Made for Professional Training PT2 course.
Student project - not production ready.