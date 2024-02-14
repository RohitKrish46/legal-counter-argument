# legal-counter-argument

This project delves into the comprehensive legal counter-argument response generation employing LLM.

The primary objective of this initiative is to facilitate individuals crafting counterarguments against legal accusations. It accomplishes this by summarizing legal documents and generating corresponding counters from these summaries. Moreover, to enhance the end-user's understanding of the document and enable queries, a question-answering module has been seamlessly integrated.

## Document Summarization and Counterargument Generation
Document summarization and counterargument generation architecture

![image](https://github.com/RohitKrish46/legal-counter-argument/assets/25106707/cf70f0f1-35dc-4fb4-a8b9-ff45324b09f8)

Document Summarization workflow:

1. we begin by comprehensively parsing a legal document to initiate the document summarization process. It's strategically divided into smaller, fixed-sized sections of approximately 2000 tokens. This segmentation with a slight overlap ensures document continuity and facilitates the Language Model's (LLM) comprehension.
2. Following segmentation, a tailor-made prompt is meticulously crafted using a PromptTemplate. This prompt forms the foundation for summarizing any given legal document.
3. Leveraging langchain's specialized function, load_summarize_chain, we systematically generate summaries for each segmented portion of the document. These individual chunk summaries are then skillfully woven together to form a coherent final summary, presenting a comprehensive view of the document's essence.
4. With the summary in hand, we further employ OpenAI's text completion models via API calls. Custom prompts guide the creation of a robust set of counterarguments, intelligently derived from the key points highlighted in the summary.


## Document Question Answering

Document question-answering architecture
![image](https://github.com/RohitKrish46/legal-counter-argument/assets/25106707/05ef5e19-4e5d-4942-a824-8a1c9d4754c3)

Document Question Answering Workflow:

1. Commencing the process, we provide a directory containing diverse unstructured data formats such as PDFs, text files, and HTML files. Our system thoroughly reads and processes each document.
2. To ensure an organized approach, the RecursiveCharacterTextSplitter comes into play, segmenting the documents into equal-sized chunks of around 1000 tokens. Overlapping portions are thoughtfully included to maintain document coherence and fluidity.
3. The chunked text undergoes meticulous embedding through OpenAIEmbeddings, identifying the exact dimensionality of the embeddings.
4. Transitioning seamlessly, we establish a Pinecone Database index, leveraging the determined embedding dimensionality for efficient data management.
5. With the index operational, we systematically store the embedded text chunks within the Pinecone index, facilitating swift and precise retrieval.
6. Utilizing Langchain's prowess, we seamlessly chain the LLM (get-3.5-turbo) with a specialized function equipped to locate similar documents based on a given query, employing the load_qa_chain module.
7. Concluding the workflow, our integrated system adeptly responds to user questions. It initially identifies analogous documents relevant to the query, then feeds both the question and retrieved information into the LLM. This orchestrates a precise answer generation process, ensuring targeted and insightful responses to specific questions extracted from the documents.
