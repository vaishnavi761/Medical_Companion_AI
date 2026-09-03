# 🏥 Medical Companion AI

An AI-powered medical report analysis application built using **Python, Streamlit, LangChain, Groq LLM, HuggingFace Embeddings, and ChromaDB**. The application helps users understand complex medical reports, ask questions about their reports, compare reports over time, and generate AI-powered health summaries.

---

## 📌 Problem Statement

Medical reports often contain complex medical terminology that is difficult for patients to understand. Comparing multiple reports manually is time-consuming, and many users are unsure which changes are important or what questions to ask during a doctor's appointment.

Medical Companion AI simplifies medical reports using Generative AI and Retrieval-Augmented Generation (RAG), making healthcare information easier to understand.

---

## 🎯 Objective

- Simplify medical reports using AI
- Answer questions based on uploaded reports
- Compare previous and current medical reports
- Track health changes over time
- Generate doctor discussion questions
- Create downloadable AI-generated health summaries

---

# ✨ Features

- 📄 Upload Medical Reports (PDF)
- 🤖 AI-Powered Medical Report Summarization
- 💊 Medicine Explanation
- 🩺 Diagnosis Explanation
- 🧪 Lab Test Interpretation
- 🌱 Lifestyle Recommendations
- 💬 Chat with Your Medical Report (RAG)
- 📊 Compare Two Medical Reports
- 📈 Health Timeline Generation
- ❓ AI-Generated Doctor Questions
- 📥 Download AI Health Report as PDF

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Frontend | Streamlit |
| LLM | Groq (Llama) |
| Framework | LangChain |
| Embeddings | HuggingFace Embeddings |
| Vector Database | ChromaDB |
| PDF Processing | PyMuPDF |
| Database | MySQL |
| Environment Variables | python-dotenv |

---

# 🏗 Project Architecture

```text
                User Uploads Report
                        │
                        ▼
               PDF Text Extraction
                        │
                        ▼
                Text Preprocessing
                        │
                        ▼
                   Text Chunking
                        │
                        ▼
          HuggingFace Embeddings
                        │
                        ▼
                 Chroma Vector DB
                        │
                        ▼
              LangChain Retriever
                        │
                        ▼
             Prompt + Retrieved Context
                        │
                        ▼
                 Groq Llama LLM
                        │
                        ▼
        AI Summary • Chat • Comparison
      Timeline • Doctor Questions • PDF
```

---

# ⚙ Workflow

1. Upload medical report
2. Extract text from PDF
3. Clean and preprocess extracted text
4. Split report into chunks
5. Generate embeddings
6. Store embeddings in ChromaDB
7. Retrieve relevant chunks using LangChain Retriever
8. Generate AI response using Groq LLM
9. Display report summary and explanations
10. Compare previous and current reports
11. Generate health timeline
12. Suggest doctor questions
13. Export AI-generated report as PDF

---

# 📂 Project Structure

```text
Medical_Companion_AI/
│
├── app.py
│
├── ocr/
│   ├── pdf_reader.py
│   ├── image_reader.py
│   └── text_cleaner.py
│
├── rag/
│   ├── chunking.py
│   ├── embeddings.py
│   ├── retriever.py
│   ├── vector_store.py
│   └── qa_chain.py
│
├── llm/
│   └── summarizer.py
│
├── comparison/
│   ├── compare_report.py
│   ├── timeline.py
│   └── doctor_ques.py
│
├── report/
│   └── pdf_generator.py
│
├── utils/
│
├── data/
│
├── requirements.txt
│
└── README.md
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_api_key
```

---

# 📚 Key Concepts Used

- Generative AI
- Retrieval-Augmented Generation (RAG)
- LangChain
- Prompt Engineering
- Embeddings
- Semantic Search
- Vector Databases
- Large Language Models (LLMs)
- Medical Document Processing

---

# 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Building end-to-end RAG applications
- Integrating LLMs with LangChain
- Working with vector databases
- Semantic document retrieval
- Prompt engineering
- Streamlit application development
- Medical document analysis using AI

---

