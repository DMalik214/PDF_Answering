import numpy as np

def load_glove_embeddings(file_path):
    embeddings_index = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            values = line.split()
            word = values[0]
            coefs = np.asarray(values[1:], dtype='float32')
            embeddings_index[word] = coefs
    return embeddings_index

def sentence_embedding(sentence, embeddings):
    words = sentence.split()
    embedding = np.mean([embeddings.get(word, np.zeros((100,))) for word in words], axis=0)
    return embedding

def find_most_similar_sentence(context_sentences, question, embeddings):
    question_emb = sentence_embedding(question, embeddings)
    max_similarity = -1
    most_similar_sentence = ""
    for sentence in context_sentences:
        sentence_emb = sentence_embedding(sentence, embeddings)
        similarity = np.dot(question_emb, sentence_emb) / (np.linalg.norm(question_emb) * np.linalg.norm(sentence_emb))
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_sentence = sentence
    return most_similar_sentence if max_similarity > 0.5 else "I don't know."

if __name__ == "__main__":
    context = "The quick brown fox jumps over the lazy dog."
    question = "What does the fox do?"
    embeddings_path = 'glove.6B.100d.txt'
    glove_embeddings = load_glove_embeddings(embeddings_path)
    answer = find_most_similar_sentence([context], question, glove_embeddings)
    print(answer)
