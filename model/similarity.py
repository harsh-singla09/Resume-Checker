from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



def calculate_similarity(resume_text, job_description):

    documents = [
        resume_text,
        job_description
    ]


    vectorizer = TfidfVectorizer(
        stop_words="english"
    )


    tfidf_matrix = vectorizer.fit_transform(documents)


    similarity_score = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )


    score = similarity_score[0][0]


    return round(score * 100, 2)



# Test
if __name__ == "__main__":

    resume = """
    Python developer with Flask,
    SQL and machine learning experience
    """


    job = """
    Looking for Python developer
    with Flask and SQL skills
    """


    result = calculate_similarity(
        resume,
        job
    )


    print(f"Match Score: {result}%")