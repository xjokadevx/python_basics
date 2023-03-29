import re


def textMapper(openAiResponse):
    finalGamertags = []

    for choiceElement in openAiResponse['choices']:
        choiceGamertags = re.split(r"\n[0-9].\s*", choiceElement['text'])
        finalGamertags += choiceGamertags

    return finalGamertags

