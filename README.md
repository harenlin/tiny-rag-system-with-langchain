# Tiny Retrieval Augmented Generation System with LangChain
### HOW TO RUN
1. Install the requirement packages.
```
pip3 install -r requirement.txt
```

2. Set up Chroma database for our corpus. (Make sure you modified the ```data``` directory to store the files.)
```
python3 create_db.py
```

3. Input the query and run the RAG application.
```
python3 rag.py --query "What is builder design pattern?"
```

### Reference
1. [Youtube Video - RAG + Langchain Python Project: Easy AI/Chat For Your Docs](https://www.youtube.com/watch?v=tcqEUSNCn8I)
2. [Design Patterns](https://github.com/kamranahmedse/design-patterns-for-humans)
