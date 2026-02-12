# RAG Q&A System - Streamlit Frontend

A modern web interface for querying your documents using Retrieval-Augmented Generation (RAG).

## Features

✨ **Key Features:**
- 📄 Upload and process PDF documents
- 🔍 Semantic search using FAISS vectors
- 🤖 LLM-powered question answering
- 💬 Interactive chat interface
- 📚 View source documents referenced in responses
- ⚙️ Configurable LLM models and parameters

## Prerequisites

Make sure you have installed:
- Python 3.8+
- Ollama (for local LLM inference) - [Download here](https://ollama.ai)

## Installation

1. **Install required Python dependencies:**

```bash
pip install streamlit langchain langchain-community faiss-cpu sentence-transformers pypdf ollama
```

2. **Install and start Ollama:**
   - Download Ollama from https://ollama.ai
   - Start the Ollama service
   - Pull a model (runs automatically on first use):
   
```bash
ollama pull mistral
# or
ollama pull llama2
# or
ollama pull neural-chat
```

## Usage

1. **Start the Streamlit app:**

```bash
streamlit run streamlit_rag_app.py
```

2. **Open your browser:**
   Navigate to `http://localhost:8501`

3. **Upload a document:**
   - Click on the file uploader in the sidebar
   - Select a PDF file
   - Click "Load/Reinitialize" to process the document

4. **Ask questions:**
   - Type your question in the input field
   - The system will retrieve relevant document chunks
   - An LLM-powered response will be generated
   - View source documents by clicking the expand button

## Configuration Options

**Sidebar Settings:**

- **Model Selection**: Choose between Mistral, Llama2, or Neural Chat
- **Temperature** (0.0-1.0): Controls response creativity
  - Lower values (0.0) = More deterministic
  - Higher values (1.0) = More creative
- **Top K**: Number of document chunks to retrieve (1-20)

## File Structure

```
streamilit_rag_app.py     # Main Streamlit application
README.md                 # This file
```

## How It Works

1. **Document Loading**: The PDF is loaded and split into 512-character chunks with 20-character overlap
2. **Embedding**: Chunks are embedded using sentence-transformers/all-MiniLM-L6-v2
3. **Vectorstore**: Embeddings are stored in FAISS for fast retrieval
4. **Retrieval**: User queries are embedded and matched against the vectorstore
5. **Generation**: Retrieved context + user query is sent to the local LLM for answering

## Troubleshooting

**Issue: "Connection refused" or "Cannot connect to Ollama"**
- Solution: Make sure Ollama is running: `ollama serve`

**Issue: Model not found**
- Solution: Pull the model first: `ollama pull mistral`

**Issue: Slow performance on first load**
- Solution: This is normal. Embedding generation takes time on first run. Subsequent queries will be faster.

**Issue: Out of memory errors**
- Solution: Use a smaller model like `neural-chat` or reduce chunk size in the code

## Model Recommendations

- **Fast & Small**: neural-chat (7B) - Best for low-end machines
- **Balanced**: mistral (7B) - Good quality, decent speed
- **High Quality**: llama2 (7B/13B) - Better responses, slower

## Tips for Best Results

1. **Document Quality**: Ensure PDFs have extractable text (not scanned images)
2. **Chunk Size**: Current setting (512 chars) works well for most documents
3. **Top K**: Use 5-10 for balanced results; higher values = slower but more comprehensive
4. **Temperature**: Start at 0.1 for factual answers, increase for creative responses

## Known Limitations

- Requires local Ollama installation and running service
- Processing time depends on document size and model choice
- Scanned PDFs without OCR won't be processed correctly
- Very large documents may require more memory

## Future Enhancements

- [ ] Support for multiple document formats (DOCX, TXT, etc.)
- [ ] Cloud LLM API integration (OpenAI, HuggingFace)
- [ ] Document persistence and management
- [ ] Advanced retrieval techniques (BM25, hybrid search)
- [ ] Response quality metrics
- [ ] Export chat history
- [ ] Multi-document cross-referencing

## License

MIT License - Feel free to modify and use!

---

**Need Help?** Check the logs in the terminal running `streamlit run streamlit_rag_app.py`
