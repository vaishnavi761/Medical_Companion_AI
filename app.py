import streamlit as st

# OCR
from ocr.pdf_reader import extract_text_from_pdf
from ocr.image_reader import extract_text_from_image
from ocr.text_cleaner import clean_text

# LLM
from llm.summarizer import (
    summarize_report,
    explain_medicines,
    explain_diagnosis,
    explain_lab_tests,
    lifestyle_tips,
)

# RAG
from rag.chunking import create_chunks
from rag.embeddings import load_embeddings
from rag.vector_store import create_vector_store
from rag.retriever import get_retriever
from rag.qa_chain import ask_question

# Comparison
from comparison.compare_report import compare_reports
from comparison.timeline import generate_timeline
from comparison.doctor_ques import generate_doctor_questions

# PDF Report
from report.pdf_generator import generate_pdf


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Medical Companion AI",
    page_icon="🏥",
    layout="wide",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ======================================================
       MAIN APPLICATION
       ====================================================== */

    .stApp {
        background-color: #f8fafc;
        color: #111827;
    }

    /* Main content text */
    .main {
        color: #111827;
    }

    /* All normal paragraphs */
    p {
        color: #111827 !important;
    }

    /* Markdown text */
    .stMarkdown {
        color: #111827 !important;
    }

    .stMarkdown p {
        color: #111827 !important;
    }

    /* ======================================================
       HEADINGS
       ====================================================== */

    h1 {
        color: #2563eb !important;
    }

    h2 {
        color: #1e3a8a !important;
    }

    h3 {
        color: #1e40af !important;
    }

    h4 {
        color: #1f2937 !important;
    }

    /* Streamlit headers */
    [data-testid="stHeader"] {
        color: #111827;
    }

    /* ======================================================
       STREAMLIT TEXT
       ====================================================== */

    label {
        color: #111827 !important;
    }

    [data-testid="stWidgetLabel"] {
        color: #111827 !important;
    }

    [data-testid="stWidgetLabel"] p {
        color: #111827 !important;
    }

    /* ======================================================
       BUTTONS
       ====================================================== */

    .stButton > button {
        width: 100%;
        background-color: #2563eb;
        color: white !important;
        border-radius: 10px;
        border: none;
        padding: 0.6rem;
        font-weight: bold;
    }

    .stButton > button:hover {
        background-color: #1d4ed8;
        color: white !important;
    }

    /* ======================================================
       TEXT INPUT
       ====================================================== */

    .stTextInput input {
        border-radius: 10px;
        color: #111827 !important;
        background-color: white !important;
    }

    .stTextInput input::placeholder {
        color: #6b7280 !important;
    }

    /* ======================================================
       FILE UPLOADER
       ====================================================== */

    [data-testid="stFileUploader"] {
        border: 2px dashed #2563eb;
        border-radius: 12px;
        padding: 15px;
        background-color: white;
    }

    /* Dropzone area (the box you drag files into) */
    [data-testid="stFileUploaderDropzone"] {
        background-color: white !important;
    }

    /* "Drag and drop file here" + size-limit hint text */
    [data-testid="stFileUploaderDropzone"] span,
    [data-testid="stFileUploaderDropzone"] small,
    [data-testid="stFileUploaderDropzoneInstructions"] * {
        color: #111827 !important;
    }

    [data-testid="stFileUploaderDropzoneInstructions"] small {
        color: #6b7280 !important;
    }

    /* Label above the uploader ("Upload Medical Report") */
    [data-testid="stFileUploader"] label {
        color: #111827 !important;
    }

    /* "Browse files" button — give it its own explicit background +
       text color instead of inheriting dark text, otherwise dark text
       on Streamlit's default dark button becomes unreadable */
    [data-testid="stFileUploader"] button {
        background-color: #2563eb !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }

    [data-testid="stFileUploader"] button:hover {
        background-color: #1d4ed8 !important;
        color: #ffffff !important;
    }

    /* Row that appears after a file is uploaded (filename + size + X) */
    [data-testid="stFileUploaderFile"] {
        background-color: #f1f5f9 !important;
        border-radius: 8px !important;
    }

    [data-testid="stFileUploaderFile"] * {
        color: #111827 !important;
    }

    /* ======================================================
       TABS
       ====================================================== */

    button[data-baseweb="tab"] {
        font-weight: 600;
        border-radius: 8px;
        color: #374151 !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        color: #2563eb !important;
    }

    /* ======================================================
       TABS CONTENT
       ====================================================== */

    [data-baseweb="tab-panel"] {
        color: #111827 !important;
    }

    [data-baseweb="tab-panel"] p {
        color: #111827 !important;
    }

    [data-baseweb="tab-panel"] li {
        color: #111827 !important;
    }

    [data-baseweb="tab-panel"] strong {
        color: #111827 !important;
    }

    /* ======================================================
       SUCCESS MESSAGE
       ====================================================== */

    [data-testid="stAlert"] {
        color: #111827 !important;
    }

    [data-testid="stAlert"] p {
        color: #111827 !important;
    }

    /* ======================================================
       DIVIDER
       ====================================================== */

    hr {
        border-color: #d1d5db;
    }

    /* ======================================================
       DOWNLOAD BUTTON
       ====================================================== */

    .stDownloadButton > button {
        width: 100%;
        background-color: #16a34a;
        color: white !important;
        border-radius: 10px;
        border: none;
        padding: 0.6rem;
        font-weight: bold;
    }

    .stDownloadButton > button:hover {
        background-color: #15803d;
        color: white !important;
    }

    /* ======================================================
       EXPANDERS
       ====================================================== */

    [data-testid="stExpander"] {
        background-color: white;
        border-radius: 10px;
    }

    [data-testid="stExpander"] * {
        color: #111827;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# TITLE
# ============================================================

st.markdown(
    """
    <h1 style="
        text-align:center;
        color:#2563eb !important;
        margin-bottom:5px;
    ">
        🏥 Medical Companion AI
    </h1>

    <p style="
        text-align:center;
        font-size:18px;
        color:#4b5563 !important;
        margin-top:0px;
    ">
        Understand • Compare • Track Your Medical Reports with AI
    </p>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# MEDICAL REPORT ANALYSIS
# ============================================================

st.header("📄 Medical Report Analysis")

uploaded_file = st.file_uploader(
    "Upload Medical Report",
    type=["pdf", "png", "jpg", "jpeg"],
)


summary = None
medicine = None
diagnosis = None
lab = None
tips = None
retriever = None


# ============================================================
# PROCESS UPLOADED REPORT
# ============================================================

if uploaded_file:

    # --------------------------------------------------------
    # Extract Text
    # --------------------------------------------------------

    if uploaded_file.type == "application/pdf":

        extracted_text = extract_text_from_pdf(uploaded_file)

    else:

        extracted_text = extract_text_from_image(uploaded_file)

    extracted_text = clean_text(extracted_text)

    # Check if text was extracted
    if not extracted_text.strip():

        st.error(
            "Unable to extract text from this report. "
            "Please upload a text-based PDF or a clear image."
        )

    else:

        # ----------------------------------------------------
        # LLM ANALYSIS
        # ----------------------------------------------------

        with st.spinner("Analyzing your medical report..."):

            summary = summarize_report(extracted_text)

            medicine = explain_medicines(extracted_text)

            diagnosis = explain_diagnosis(extracted_text)

            lab = explain_lab_tests(extracted_text)

            tips = lifestyle_tips(extracted_text)

        # ----------------------------------------------------
        # TABS
        # ----------------------------------------------------

        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            [
                "Summary",
                "Medicines",
                "Diagnosis",
                "Lab Tests",
                "Lifestyle Tips",
            ]
        )

        with tab1:

            st.subheader("📋 Report Summary")

            st.markdown(
                f"""
                <div style="
                    background-color:white;
                    padding:20px;
                    border-radius:12px;
                    border:1px solid #e5e7eb;
                    color:#111827;
                    line-height:1.7;
                ">
                    {summary}
                </div>
                """,
                unsafe_allow_html=True,
            )

        with tab2:

            st.subheader("💊 Medicines")

            st.markdown(
                f"""
                <div style="
                    background-color:white;
                    padding:20px;
                    border-radius:12px;
                    border:1px solid #e5e7eb;
                    color:#111827;
                    line-height:1.7;
                ">
                    {medicine}
                </div>
                """,
                unsafe_allow_html=True,
            )

        with tab3:

            st.subheader("🩺 Diagnosis Explanation")

            st.markdown(
                f"""
                <div style="
                    background-color:white;
                    padding:20px;
                    border-radius:12px;
                    border:1px solid #e5e7eb;
                    color:#111827;
                    line-height:1.7;
                ">
                    {diagnosis}
                </div>
                """,
                unsafe_allow_html=True,
            )

        with tab4:

            st.subheader("🧪 Lab Tests")

            st.markdown(
                f"""
                <div style="
                    background-color:white;
                    padding:20px;
                    border-radius:12px;
                    border:1px solid #e5e7eb;
                    color:#111827;
                    line-height:1.7;
                ">
                    {lab}
                </div>
                """,
                unsafe_allow_html=True,
            )

        with tab5:

            st.subheader("🌿 Lifestyle Tips")

            st.markdown(
                f"""
                <div style="
                    background-color:white;
                    padding:20px;
                    border-radius:12px;
                    border:1px solid #e5e7eb;
                    color:#111827;
                    line-height:1.7;
                ">
                    {tips}
                </div>
                """,
                unsafe_allow_html=True,
            )

        # ====================================================
        # RAG
        # ====================================================

        chunks = create_chunks(extracted_text)

        embeddings = load_embeddings()

        vector_db = create_vector_store(
            chunks,
            embeddings,
        )

        retriever = get_retriever(vector_db)

        # ----------------------------------------------------
        # CHAT WITH MEDICAL REPORT
        # ----------------------------------------------------

        st.divider()

        st.header("💬 Chat with Your Medical Report")

        question = st.text_input(
            "Do you have any doubts?",
            placeholder="Example: What does my blood sugar result mean?",
        )

        if st.button("Ask AI"):

            if question.strip():

                with st.spinner("Finding the answer..."):

                    answer = ask_question(
                        question,
                        retriever,
                    )

                st.markdown(
                    f"""
                    <div style="
                        background-color:#ffffff;
                        padding:20px;
                        border-radius:12px;
                        border-left:5px solid #2563eb;
                        color:#111827;
                        line-height:1.7;
                    ">
                        <strong>AI Answer</strong><br><br>
                        {answer}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            else:

                st.warning("Please enter a question.")


# ============================================================
# COMPARE REPORTS
# ============================================================

st.divider()

st.header("📊 Compare Two Medical Reports")

old_file = st.file_uploader(
    "Upload Previous Report",
    type=["pdf"],
    key="old",
)

new_file = st.file_uploader(
    "Upload Current Report",
    type=["pdf"],
    key="new",
)


if old_file and new_file:

    with st.spinner("Comparing medical reports..."):

        previous_text = clean_text(
            extract_text_from_pdf(old_file)
        )

        current_text = clean_text(
            extract_text_from_pdf(new_file)
        )

        comparison = compare_reports(
            previous_text,
            current_text,
        )

        timeline = generate_timeline(
            previous_text,
            current_text,
        )

        doctor_questions = generate_doctor_questions(
            current_text,
            previous_text,
        )

    # --------------------------------------------------------
    # COMPARISON
    # --------------------------------------------------------

    st.subheader("📊 Comparison Result")

    st.markdown(
        f"""
        <div style="
            background-color:white;
            padding:20px;
            border-radius:12px;
            border:1px solid #e5e7eb;
            color:#111827;
            line-height:1.7;
        ">
            {comparison}
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # TIMELINE
    # --------------------------------------------------------

    st.subheader("📈 Health Timeline")

    st.markdown(
        f"""
        <div style="
            background-color:white;
            padding:20px;
            border-radius:12px;
            border:1px solid #e5e7eb;
            color:#111827;
            line-height:1.7;
        ">
            {timeline}
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # DOCTOR QUESTIONS
    # --------------------------------------------------------

    st.subheader("❓ Questions to Ask Your Doctor")

    st.markdown(
        f"""
        <div style="
            background-color:white;
            padding:20px;
            border-radius:12px;
            border:1px solid #e5e7eb;
            color:#111827;
            line-height:1.7;
        ">
            {doctor_questions}
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # PDF DOWNLOAD
    # --------------------------------------------------------
    #
    # FIX: previously this block was gated on `if summary:`, which is
    # only ever set inside the "Medical Report Analysis" section above.
    # A user who goes straight to "Compare Two Medical Reports" (a
    # separate, valid workflow) would generate a comparison, timeline,
    # and doctor questions on screen — but never see a download button,
    # because `summary` was still None.
    #
    # Gating on `comparison` instead (which IS always set inside this
    # `if old_file and new_file:` block) fixes that. Missing single-report
    # sections (summary/medicine/diagnosis/lab/tips) are filled with a
    # placeholder string so generate_pdf() never receives None and the
    # PDF still builds cleanly.

    if comparison:

        pdf_file = generate_pdf(
            summary or "Not generated in this session.",
            medicine or "Not generated in this session.",
            diagnosis or "Not generated in this session.",
            lab or "Not generated in this session.",
            tips or "Not generated in this session.",
            comparison,
            timeline,
            doctor_questions,
        )

        with open(pdf_file, "rb") as pdf:

            st.download_button(
                label="⬇ Download AI Health Report",
                data=pdf,
                file_name="AI_Health_Report.pdf",
                mime="application/pdf",
            )
