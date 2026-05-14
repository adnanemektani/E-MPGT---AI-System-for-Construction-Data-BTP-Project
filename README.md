E-MPGT: Intelligent Construction Data Management System
An AI-driven framework for automated extraction, structuring, and analysis of BTP project documentation.

Project Overview
E-MPGT is a specialized AI solution designed to handle the high volume of unstructured data in the construction industry. The system processes technical sheets, project emails, and onsite imagery to provide a centralized, searchable knowledge base for project managers and engineers.

System Architecture
The platform is built on a modular three-layer architecture to ensure scalability and precise data retrieval:

1. Data Processing Layer
Multi-Source Ingestion: Supports PDF documents, Excel spreadsheets, Word files, and images (JPEG/PNG).

Automated OCR & Extraction: Utilizes Vision models to extract text and metadata from technical drawings and onsite photos.

Vectorization: Converts unstructured text into high-dimensional vectors using sentence-transformers.

Storage: Implements Pinecone as a vector database, utilizing Namespaces to ensure strict data isolation between different construction projects (Chantiers).

2. Artificial Intelligence Layer
Contextual Analysis: Leverages Gemini 1.5 Flash for visual document understanding and Llama 3.1 for complex reasoning.

Retrieval-Augmented Generation (RAG): Anchors AI responses in the specific uploaded documents to prevent hallucinations and provide site-specific answers.

Semantic Search: Enables natural language queries to find technical specifications across thousands of project pages.

3. Execution & Workflow Layer
Interactive Dashboard: A Streamlit-based interface for real-time document querying and manual file uploads.

Email Synchronization: Integrated IMAP protocol to automatically sync project updates and attachments directly from Gmail.

History Management: Maintains a consistent conversation state using LangChain's memory components to handle multi-turn technical inquiries.

Technical Stack
Backend: Python

Web Interface: Streamlit

AI Orchestration: LangChain

Vector Database: Pinecone

LLMs: Google Gemini (Vision), Groq/Llama 3.1 (Inference)

Infrastructure: Git

Setup and Installation
Clone the repository:

Bash
git clone https://github.com/adnanemektani/E-MPGT---AI-System-for-Construction-Data-BTP-Project.git
Create and activate a virtual environment:

Bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install dependencies:

Bash
pip install -r requirements.txt
Configure environment variables in a .env file (API keys for Pinecone, Google, and Groq).

Kifach t-puchi l-README m-ba3d ma t-cree-ih:
Melli t-salli l-kteba f l-fichier, rje3 l-terminal w dir:

PowerShell
git add README.md
git commit -m "Add detailed system architecture to README"
git push origin main
