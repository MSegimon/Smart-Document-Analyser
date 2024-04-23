import mysql.connector
import json

from db import getDBCursor, mydb
from TextAnalysis.sentiment import calculate_sentiment_tone
from TextAnalysis.sumarize import summarize, extractKeywordsNormalized
from inputValidation import validate_integer
from fileFunctions import get_file_by_id

def recursive_summarize(content):
    """Recursively summarize text within nested HTML-like JSON structure."""
    combined_summaries = ""
    for item in content:
        # Check if current node has nested content
        if 'content' in item and item['content']:
            # Recursively summarize nested content
            nested_summary = recursive_summarize(item['content'])
            combined_summaries += " " + nested_summary
        else:
            # Directly append the text if there is no nested content
            combined_summaries += " " + item['text']

    # Combine all the summaries or texts from current level and summarize
    full_text = combined_summaries
    return summarize(full_text)

def summarize_text(id, session_cookie):
    """Summarizes the text from a nested HTML-like JSON structure."""
    
    if not validate_integer(id):
        raise None
    
    # Get the file content by ID
    file_content = get_file_by_id(id, session_cookie)
    
    if not isinstance(file_content, list):
        raise ValueError("Input data must be a list of dictionaries representing HTML-like structure.")

    # Start summarizing from the root level
    final_summary = recursive_summarize(file_content)
    return final_summary

def recursive_sentiment(content):
        """Recursively calculate sentiment of text within nested HTML-like JSON structure."""
        count = 0.0
        sentiment_scores = 0.0
        for item in content:
            # Check if current node has nested content
            if 'content' in item and item['content']:
                # Recursively calculate sentiment of nested content
                nested_sentiment = recursive_sentiment(item['content'])
                sentiment_scores += nested_sentiment
                count += 1
            else:
                # Calculate sentiment score for the text if there is no nested content
                sentiment_score = calculate_sentiment_tone(item['text'])
                sentiment_scores += sentiment_score[0]
                count += 1

        return sentiment_scores / count

def calculate_sentiment(id, session_cookie):
    """Calculates the sentiment of the text from a nested HTML-like JSON structure."""

    if not validate_integer(id):
        raise None

    # Get the file content by ID
    file_content = get_file_by_id(id, session_cookie)
    
    if not isinstance(file_content, list):
        raise ValueError("Input data must be a list of dictionaries representing HTML-like structure.")
    
    # Calculate sentiment from the root level
    sentiment_scores = recursive_sentiment(file_content)
    return sentiment_scores


# Test the summarize_text function

# Example JSON data in string format
# json_data = """
# [
#     {
#         "tag": "h1",
#         "text": "Modric strike helps Real Madrid secure narrow LaLiga win over Sevilla",
#         "content": [
#             {
#                 "tag": "p",
#                 "text": "Real Madridtook another step towards theLaLigatitle on Sunday night with a narrow1-0 win over Sevillaat the Estadio Santiago Bernabeu.",
#                 "content": []
#             },
#             {
#                 "tag": "p",
#                 "text": "In what proved to be a very tight and cagey affair,Luke Modric's strike was enough to take Real Madrideight points clear ofBarcelona.",
#                 "content": []
#             },
#             {
#                 "tag": "p",
#                 "text": "AfterSevillahad the first big chance of the match, Real Madridthought they had taken the lead within the first 10 minutes whenVinicius Jrpicked out a superb pass toLucas Vazquez.",
#                 "content": []
#             },
#             {
#                 "tag": "p",
#                 "text": "The right-back connected with the pass as he burst into the box, and he finished excellently. However, the goal was then ruled out as there was a foul fromNacho Fernandezin the build-up.",
#                 "content": []
#             },
#             {
#                 "tag": "h2",
#                 "text": "Real Madrid's defensive injuries",
#                 "content": [
#                     {
#                         "tag": "p",
#                         "text": "Nachohas become an important player forReal Madridafter the injuries toDavid Alaba and Eder Militao, and it was a major boost thatAntonio Rudigerwas fit enough to start against Sevilla and relieveAurelien Tchouamenifrom his temporary centre-back role.",
#                         "content": []
#                     },
#                     {
#                         "tag": "p",
#                         "text": "Barring a shot fromFede Valverde, Real Madrid failed to create much in the first half andSevilla'sgame plan was clearly working.",
#                         "content": []
#                     },
#                     {
#                         "tag": "p",
#                         "text": "Valverdehit the post in the early stages of the second half, which was followed up by a good save fromAndriy Lunin to deny Sevilla's Isaac Romero.",
#                         "content": []
#                     }
#                 ]
#             },
#             {
#                 "tag": "h2",
#                 "text": "Referee suffers an injury before Modric winner",
#                 "content": [
#                     {
#                         "tag": "p",
#                         "text": "In a very unusual event, referee Isiro Diaz de Mera picked up an injury and had to leave the field. He was replaced by Fernandez Buergo who has only refereed in the third tier of Spanish football before.",
#                         "content": []
#                     },
#                     {
#                         "tag": "p",
#                         "text": "A point of interest wasSergio Ramos' performance.TheReal Madridlegend was excellent throughout, along with his defensive partners. Despite that,Luka Modricwas able to break the deadlock with less than 10 minutes to go.",
#                         "content": []
#                     },
#                     {
#                         "tag": "p",
#                         "text": "Sevillaappealed for an offside in the build-up but the superb strike from the Croatian midfielder stood.",
#                         "content": []
#                     },
#                     {
#                         "tag": "p",
#                         "text": "The win meansReal Madridare nine points ahead of Girona, having played a game more, whilst Sevilla remain in 15th.",
#                         "content": []
#                     }
#                 ]
#             }
#         ]
#     }
# ]
# """

# Call the function and print the result
#print("Final summary: " + summarize_text(json_data))

# Call the function and print the result
# sentiment_scores = calculate_sentiment(json_data)
# print("Sentiment scores:", sentiment_scores)
