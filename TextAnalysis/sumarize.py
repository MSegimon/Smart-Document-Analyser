import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest

def extractKeywordsNormalized(doc):
    # Extract keywords
    keywords = []
    pos_tag = ['PROPN', 'ADJ', 'NOUN', 'VERB']
    for token in doc:
        if(token.text in STOP_WORDS or token.text in punctuation):
            continue
        if(token.pos_ in pos_tag):
            keywords.append(token.text)

    freq_word = Counter(keywords)

    # Normalize the frequency of the words
    max_freq = Counter(keywords).most_common(1)[0][1]
    for word in freq_word.keys():
        freq_word[word] = (freq_word[word]/max_freq)

    return freq_word

def summarize(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)

    freq_word = extractKeywordsNormalized(doc)

    # Weighing sentences
    sent_strength = {}
    for sent in doc.sents:
        for word in sent:
            if word.text in freq_word.keys():
                if sent in sent_strength.keys():
                    sent_strength[sent] += freq_word[word.text]
                else:
                    sent_strength[sent] = freq_word[word.text]

    # Getting the summary (half sentences with the highest weight)
    num_sent = int(len(sent_strength)* 3/4)
    summary = nlargest(num_sent, sent_strength, key=sent_strength.get)

    # Convert summary to string
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)

    return summary

# Test
#text = "Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to progressively improve their performance on a specific task. Machine learning algorithms build a mathematical model of sample data, known as “training data”, in order to make predictions or decisions without being explicitly programmed to perform the task. Machine learning algorithms are used in the applications of email filtering, detection of network intruders, and computer vision, where it is infeasible to develop an algorithm of specific instructions for performing the task. Machine learning is closely related to computational statistics, which focuses on making predictions using computers. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. Data mining is a field of study within machine learning and focuses on exploratory data analysis through unsupervised learning. In its application across business problems, machine learning is also referred to as predictive analytics."
#print(summarize(text))
