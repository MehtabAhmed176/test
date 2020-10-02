import flask
from flask import request, jsonify
from flask import render_template
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    
        return render_template("index.html")

@app.route('/jobscore', methods=['POST'])
def file():

    # Store the resume in a variable
    resume =request.form['ResumeData']
    jd=request.form['JD']
    print(resume)
    print(jd)

    #Create a list of resume and job descrition
    text = [resume, jd]


    #Create a count vectorizer object and convert the text documents to a matrix of token counts.
    cv = CountVectorizer()

    #Something
    count_matrix = cv.fit_transform(text)
    print("\nSimilarity Scores:")
    print(cosine_similarity(count_matrix))

    #get the match percentage
    matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
    matchPercentage = round(matchPercentage, 2) # round to two decimal
    print("Your resume matches about "+ str(matchPercentage)+ "% of the job description.")

    return str(matchPercentage)