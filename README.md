
# AI-CHAT BOT

## Overview 
* It is Flask Based RAG Chat bot which can provide ansewers to questions of Artificial Intelligence and Machine Learning
* **RAG** or r Retrieval-Augmented Generation, a Generative AI (GenAI) framework that augments Large Language Models (LLMs) with internal data to help AI-powered software to communicate more effectively with people.


## Key Points

* **RAG** : Retrieval-Augmented Generation System is used to create to get better accuracy of answer
* **LLM** : langchain based bigscience/bloom-7b1 model is used
* **Flask** flask is used to create web app

## Dependencies
* tiktoken
* pypdf
* faiss-gpu
* InstructorEmbedding
* transformers
*  langchain==0.1.2
*  sentence_transformers==2.2.2
*  FLask

## Organisation of files
```
/project-root
||--KowledgeBase
 ||-- .pdf files
||--_pycache_
||--static
  ||--css
    ||--style.css
||--templates
  ||--index.html
||--NoteBook.ipynb
||--ReadME.md
||--Backend.py

```
* **knowledge base** : consist of pdf files which are books of ml
* **Notebook.ipynb** : NoteBook which consist of details regarding model preperation
* **Backend.py** : Backend of Flask APP
* **Style.css** : CSS used
* **Index.html** : Html file


  
