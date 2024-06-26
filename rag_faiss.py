import os
import openai
import argparse
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI

load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']

FAISS_PATH = "faiss_index"

PROMPT_TEMPLATE = """
Answer the question based only on the following context: {context}

---

Answer the question based on the above context: {question}
"""

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, help="Input query (textual content).")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()    
    query = args.query

    # db preparation
    embedding_function = OpenAIEmbeddings()
    db = FAISS.load_local(FAISS_PATH, embedding_function, allow_dangerous_deserialization=True)

    # db searching
    results = db.similarity_search_with_relevance_scores(query, k=3)
    if len(results) == 0 or results[0][1] < 0.7: # early stopping
        print("Unable to find matching results.")
        return

    # retrieval results
    context_text = "\n\n---\n\n".join([doc.page_content for doc, score in results])

    # rag prompt
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query)
    print(prompt)

    # text generation
    model = ChatOpenAI()
    response_text = model.predict(prompt)

    # source notation
    sources = [doc.metadata.get("source", None) for doc, _score in results]
    formatted_response = f"\n\nResponse: {response_text}\nSources: {sources}"
    print(formatted_response)


if __name__ == "__main__":
    main()

