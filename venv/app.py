import chromadb;

chroma_client = chromadb.Client()

collection_name = "test_collection"

collection = chroma_client.get_or_create_collection(collection_name)

documents = [
    {"id":"doc1","text":"Hello world!"},
    {"id":"doc2","text":"How are you?"},
    {"id":"doc3","text":"Good, see you later!"}
]

for doc in documents:    
    collection.upsert(ids=doc["id"],documents=[doc["text"]])

query_text = "Rizwan"

results = collection.query(
    query_texts = [query_text],
    n_results = 3
)
print(results)
for idx, documents in enumerate(results):
    print(f"idx: {idx}")
    # print(f"documents: {documents.documents}")
    # print(f"documents: {documents.distances}")
#     print(f"documents {documents}:")
 