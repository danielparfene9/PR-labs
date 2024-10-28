## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)


## 🧐 About <a name = "about"></a>

This FastAPI application provides endpoints for managing PDF files using MongoDB for storage. It supports uploading, retrieving, deleting PDF documents, and performing operations like extracting pages, converting them to images, and updating PDFs.

  ### Features

    - **Upload PDF**: Upload PDF files to the database.
    - **Get All PDFs**: Retrieve a list of all uploaded PDFs.
    - **Update PDF**: Extract pages, process them (deskew functionality not fully implemented), and update the PDF in the database.
    - **Delete PDF**: Remove a specific PDF from the database.
    - **Download PDF**: Download a specific PDF file.


## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

  ### Prerequisites

    What things you need to install the software and how to install them.

    ```
    - Python 3.8+
    - FastAPI
    - PyMongo
    - MongoEngine
    - PyMuPDF
    - Pillow
    - OpenCV
    - numpy
    - python-dotenv
    ```

  ## Repository Structure

  ### app:

	  routes.py              # Defines the API endpoints and their respective request handlers.
	  schemas.py             # Contains Pydantic models for request and response validation.
	  services.py            # Implements the logic and interaction with other components.
 
  ### components:

	  __init__.py
	  gcv_ocr.py             # Handles OCR processing using Google Cloud Vision API.
	  pdf_processing.py      # Manages PDF processing tasks, such as conversion and manipulation.
	  utils.py
 
  ### database:

	  __init__.py
	  db.py                  # Sets up the database connection and configuration.
	  operations.py          # Defines CRUD operations and database-related logic.

  ### libs:

	  standard_lib.py
	  third_party_lib.py
 
  ### main.py -> The entry point for the FastAPI application.

  ### requirements.txt -> Lists Python dependencies required for the project.

  ### settings:

	  __init__.py
	  mongo_settings.py      # Configures MongoDB-related settings.

  ### Installing

    A step by step series of examples that tell you how to get a development env running.

    1. Clone the repository:

        ```bash
        git clone https://github.com/danielparfene9/FastAPI-MongoDB
        cd your-repo
        ```

    2. Create a virtual environment and activate it:

        ```bash
        python -m venv venv
        source venv/bin/activate  # On Windows use `venv\Scripts\activate`
        ```

    3. Install dependencies:

        ```bash
        pip install -r requirements.txt
        ```