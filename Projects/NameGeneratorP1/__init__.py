from dotenv import load_dotenv
load_dotenv()


from Services.openAiCompletion import textCompletionService
from utils.queryMaker import queryMaker
from utils.textMapper import textMapper

def main():
    print("""
    Hello!
    I'm gamertargs generator
    ----------------------------
    I'm willing to help you. Please keep in mind the instructions below
    > Enter just one word per question
    > thats it 🤪
    """)
    qualification = input('How to describe yourself(brave/funny/shy): ')
    food = input('Plese type your favorite food: ')
    birthYear = input('Please enter your birth year: ')

    aiQuery = queryMaker([qualification, food, birthYear])

    aiResponse = textCompletionService(aiQuery)

    result = textMapper(aiResponse)
    print(f"\n 🚀I tried to generate the best gamertags for you, so please check it below \n {result}")


if __name__ == '__main__':
    main()

