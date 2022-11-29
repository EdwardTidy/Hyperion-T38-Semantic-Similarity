# Import modules for this program, assign variable for Natural Language Processing
import spacy
nlp = spacy.load('en_core_web_md')

# Define a function that takes in the description of a film and returns the top match from a file
def watch_next(blurb):

    # Create an empty list to attend similarity scores to and a variable for the blurb we will be comparing again
    similarityList = []
    blurb_nlp = nlp(blurb)

    # Read file and compare similarity for each film description against the film that was watched
    with open("movies.txt", "r+") as moviesFile:
        for movie in moviesFile:
            movieIdentifier = movie[:9]
            movieBlurb = nlp(movie[9:])

            # Append movie name and similarity score
            similarityList.append(f"{movieIdentifier} {float(blurb_nlp.similarity(movieBlurb))}")
    
    # Function to sort by the similarity score
    def myFunc(score):
        return (score[9:])
    similarityList.sort(key=myFunc)

    # Identify top matched movie
    topMatch = similarityList[-1]
    topMatch = topMatch[:9]

    # Find top matched moview description from movies file
    with open("movies.txt", "r+") as moviesFile:
        for movie in moviesFile:
            if topMatch in movie:
                print(movie)

planet_hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# Call function with description of movie that was watched
watch_next(planet_hulk)