# Python Documentation with FastAPI 🚀

This repository is a **learning and practice space** where I will be
developing different test services using **FastAPI** and related
technologies.

## Purpose 📘

-   Get familiar with the **FastAPI** framework to build modern, fast,
    and secure APIs.\
-   Practice concepts such as:
    -   Creating REST endpoints.
    -   Handling models with **Pydantic**.
    -   Database integration using **SQLAlchemy**.
    -   Automatic documentation with **Swagger** and **ReDoc**.

## Project Structure 📂

-   `app/` → Main application code (models, schemas, services, routes).\
-   `requirements.txt` → Project dependencies.\
-   `.env` → Environment variables (ignored in the repository).\
-   `.venv/` → Virtual environment (also ignored in the repository).

## Usage ▶️

1.  Clone the repository:

    ``` bash
    git clone https://github.com/obonelli/Python_documentation.git
    cd Python_documentation
    ```

2.  Create and activate a virtual environment:

    ``` bash
    python -m venv .venv
    source .venv/bin/activate   # Linux/Mac
    .venv\Scripts\activate    # Windows
    ```

3.  Install dependencies:

    ``` bash
    pip install -r requirements.txt
    ```

4.  Run the FastAPI server:

    ``` bash
    uvicorn app.main:app --reload
    ```

5.  Open in the browser:

    -   API Docs (Swagger): `http://127.0.0.1:8000/docs`\
    -   ReDoc: `http://127.0.0.1:8000/redoc`

## Notes 📝

This repository is **not intended for production**, but for personal
practice and documentation.\
Examples and improvements will be added progressively.

------------------------------------------------------------------------

💡 *Learning FastAPI step by step.*
