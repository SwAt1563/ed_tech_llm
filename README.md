# SEL Assistant Chatbot Backend

Welcome to the backend repository for the SEL Assistant Chatbot! This repository houses the core functionalities that power our chatbot, designed to support students by managing their emotions and providing social-emotional guidance outside school hours. Developed with Django REST framework, this backend integrates with Azure services, including Azure VM and Azure OpenAI, utilizing ChatGPT for natural language processing and LangChain for managing chat interactions and history.

## Features

- **API Integration**: RESTful API built with Django REST Framework to serve the frontend application.
- **CORS Handling**: Configured to handle Cross-Origin Resource Sharing (CORS) for secure access between different domains.
- **Azure VM Hosting**: Hosted on an Azure Virtual Machine for scalable, reliable performance.
- **Azure OpenAI Integration**: Incorporates Azure OpenAI's pretrained models to enhance chatbot responses.
- **LangChain**: Manages prompt templates and chat history effectively, ensuring a contextual and coherent interaction history.

## Built With

- **[Django REST Framework](https://www.django-rest-framework.org/)** - A powerful and flexible toolkit for building Web APIs in Django.
- **[Azure VM](https://azure.microsoft.com/en-us/services/virtual-machines/)** - For hosting the application.
- **[Azure OpenAI](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/)** - For utilizing AI models.
- **[LangChain](https://www.langchain.com/)** - For managing conversation logic and state.

## Getting Started

Follow these instructions to get your backend server up and running.

### Prerequisites

- Python 3.8 or [newer]((https://www.python.org/downloads/))


## Setup Instructions

Follow these steps to get your development environment set up:

### 1. Clone the Repository

First, you need to clone the repository from GitHub to your local machine.

```bash
git clone https://github.com/SwAt1563/ed_tech_llm.git
cd ed_tech_llm
```

### 2. Create a Virtual Environment

Creating a virtual environment is highly recommended to manage dependencies.

#### For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### For Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Requirements

With your virtual environment active, install the project dependencies using:

```bash
pip install -r requirements.txt
```

### 4. Database Setup

Before running the application, you need to make migrations and migrate the database schemas.

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server

Finally, start the Django development server:

```bash
python manage.py runserver
```

By default, the server will start on `http://127.0.0.1:8000/`. You can open this address in a web browser to view the application.


## Usage

This backend serves as the processing and data management layer for the SEL Assistant Chatbot, handling requests from the [frontend application](https://github.com/SwAt1563/chatbot-reactjs). It processes these requests to deliver appropriate responses based on the student's emotional state and queries.



