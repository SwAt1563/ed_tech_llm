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

- Python 3.8 or newer
- Pipenv for dependency management

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SwAt1563/ed_tech_llm.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ed_tech_llm
   ```
3. Install dependencies using Pipenv:
   ```bash
   pipenv install
   ```
4. Activate the virtual environment:
   ```bash
   pipenv shell
   ```
5. Migrate the database:
   ```bash
   python manage.py migrate
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

The server will start running on `http://localhost:8000`.

## Usage

This backend serves as the processing and data management layer for the SEL Assistant Chatbot, handling requests from the [frontend application](https://github.com/SwAt1563/chatbot-reactjs). It processes these requests to deliver appropriate responses based on the student's emotional state and queries.



