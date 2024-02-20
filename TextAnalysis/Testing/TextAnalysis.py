import spacy

# Load the efficiency spaCy model
nlp = spacy.load('en_core_web_sm')
# Load the large spaCy model
#nlp = spacy.load('en_core_web_trf')


text = """Compatibility of systems of linear constraints over the set of natural numbers.
Criteria of compatibility of a system of linear Diophantine equations, strict inequations,
and nonstrict inequations are considered. Upper bounds for components of a minimal set of
solutions and algorithms of construction of minimal generating sets of solutions for all types
of systems are given. These criteria and the corresponding algorithms for constructing a minimal
supporting set of solutions can be used in solving all the considered types systems and systems of mixed types."""


def text_analysis(text):
    doc = nlp(text)
    # Tokenization
    tokens = [token.text for token in doc]
    # Lemmatization
    lemmas = [token.lemma_ for token in doc]
    # Part of Speech tagging
    pos = [token.pos_ for token in doc]
    # Named Entity Recognition
    entities = [(entity.text, entity.label_) for entity in doc.ents]

    print(f"Tokens: {tokens}")
    print(f"Lemmas: {lemmas}")
    print(f"POS: {pos}")
    print(f"Entities: {entities}")

#text_analysis(text)


from spacytextblob.spacytextblob import SpacyTextBlob

def calculate_sentiment_tone(text):
    nlp.add_pipe('spacytextblob')
    doc = nlp(text)
    sentiment = doc._.blob.polarity
    tone = doc._.blob.subjectivity
    
    if sentiment < 0:
        print("Sentiment: Negative")
    elif sentiment > 0:
        print("Sentiment: Positive")
    else:
        print("Sentiment: Neutral")

    print(f"Tone: {tone}")

calculate_sentiment_tone(text)




def extract_keywords(text):
    if 'textrank' not in nlp.pipe_names:
        import pytextrank
        nlp.add_pipe("textrank")
    else:
        print("'textrank' already exists in the pipeline.")

    doc = nlp(text)
    
    for p in doc._.textrank.summary(limit_phrases=15, limit_sentences=5):
        print(p)

#extract_keywords(text)
