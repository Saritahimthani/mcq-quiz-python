import sys

class Question:
    def __init__(self, prompt, options, correct_answer):
        self.prompt = prompt
        self.options = options
        self.correct_answer = correct_answer

questions = [
    Question("\033[96m1) Which HTTP method is commonly used for creating a new resource in a RESTful API?\033[0m", 
             ["\033[93ma) GET\033[0m", 
              "\033[93mb) POST\033[0m", 
              "\033[93mc) PUT\033[0m", 
              "\033[93md) DELETE\033[0m"], 
             "a"),
    Question("\033[96m1) What does API stand for in the context of web development?\033[0m", 
             ["\033[93ma) Application Protocol Interface\033[0m", 
              "\033[93mb) Application Programming Interface\033[0m", 
              "\033[93mc) Advanced Programming Interface\033[0m", 
              "\033[93md) Advanced Protocol Interface\033[0m"], 
             "b"),
    Question("\033[96m1) What format is commonly used for data exchange in RESTful APIs?\033[0m", 
             ["\033[93ma) XML\033[0m", 
              "\033[93mb) JSON\033[0m", 
              "\033[93mc) CSV\033[0m", 
              "\033[93md) HTML\033[0m"], 
             "b"),
    Question("\033[96m1) Which Python library is commonly used for making HTTP requests to web APIs?\033[0m", 
             ["\033[93ma) PyRequests\033[0m", 
              "\033[93mb) httplib2\033[0m", 
              "\033[93mc) urllib\033[0m",
              "\033[93md) requests\033[0m"], 
             "d"),
    Question("\033[96m1) What is the purpose of an API key in web APIs?\033[0m", 
             ["\033[93ma)  To authenticate users\033[0m", 
              "\033[93mb) To authorize access to the API\033[0m", 
              "\033[93mc) To encrypt data during transmission\033[0m", 
              "\033[93md) To optimize database queries\033[0m"], 
             "b"),
    Question("\033[96m1) Which Python module is commonly used for parsing JSON responses from web APIs?\033[0m", 
             ["\033[93ma) json\033[0m", 
              "\033[93mb) xml\033[0m", 
              "\033[93mc) csv\033[0m", 
              "\033[93md) pickle\033[0m"], 
             "a"),
    Question("\033[96m1) What is the status code for a successful HTTP request in which content is returned?\033[0m", 
             ["\033[93ma) 200\033[0m", 
              "\033[93mb) 400\033[0m", 
              "\033[93mc) 404\033[0m", 
              "\033[93md) 500\033[0m"], 
             "a"),
    Question("\033[96m1) What does CORS stand for in the context of web APIs?\033[0m", 
             ["\033[93ma) Cross-Origin Resource Sharing\033[0m", 
              "\033[93mb) Cross-Origin Request Sharing\033[0m", 
              "\033[93mc) Cross-Origin Response Sharing\033[0m", 
              "\033[93md) Cross-Origin Resource Synchronization\033[0m"], 
             "a"),
    Question("\033[96m1) Which Python library is commonly used for creating web APIs?\033[0m", 
             ["\033[93ma) Django\033[0m", 
              "\033[93mb) Flask\033[0m", 
              "\033[93mc) Pyramid\033[0m", 
              "\033[93md) All of the above\033[0m"], 
             "d"),
    Question("\033[96m1) What is the purpose of rate limiting in web APIs?\033[0m", 
             ["\033[93ma) To restrict the number of API requests per user\033[0m", 
              "\033[93mb) To improve server performance\033[0m", 
              "\033[93mc) To prevent unauthorized access\033[0m", 
              "\033[93md) To encrypt data during transmission\033[0m"], 
             "a"),
    Question("\033[96m1) Which HTTP status code indicates that the requested resource was not found?\033[0m", 
             ["\033[93ma) 200\033[0m", 
              "\033[93mb) 400\033[0m", 
              "\033[93mc) 404\033[0m", 
              "\033[93md) 500\033[0m"], 
             "c"),
    Question("\033[96m1)What is the primary role of authentication tokens in web APIs?\033[0m", 
             ["\033[93ma) To validate user credentials\033[0m", 
              "\033[93mb) To authorize access to protected resources\033[0m", 
              "\033[93mc) To encrypt data during transmission\033[0m", 
              "\033[93md) To improve server performance\033[0m"], 
             "b"),
    Question("\033[96m1)Which Python library is commonly used for building RESTful APIs in Flask?\033[0m", 
             ["\033[93ma) Flask-RESTful\033[0m", 
              "\033[93mb) Flask-API\033[0m", 
              "\033[93mc) Flask-RestPlus\033[0m", 
              "\033[93md) Flask-REST\033[0m"], 
             "c"),
    Question("\033[96m1)What is the purpose of pagination in web APIs?\033[0m", 
             ["\033[93ma) To optimize database queries\033[0m", 
              "\033[93mb) To limit the number of API requests per user\033[0m", 
              "\033[93mc) To split large datasets into smaller, manageable chunks\033[0m", 
              "\033[93md) To prevent unauthorized access\033[0m"], 
             "c"),
    Question("\033[96m1)Which HTTP method is commonly used for creating a new resource in a RESTful API?\033[0m", 
             ["\033[93ma) GET\033[0m", 
              "\033[93mb) POST\033[0m", 
              "\033[93mc) PUT\033[0m", 
              "\033[93md) DELETE\033[0m"], 
             "B"),
    Question("\033[96m1)What is the purpose of versioning in web APIs?\033[0m", 
             ["\033[93ma) To improve server performance\033[0m", 
              "\033[93mb) To restrict access to certain API endpoints\033[0m", 
              "\033[93mc) To maintain backward compatibility\033[0m", 
              "\033[93md) To encrypt data during transmission\033[0m"], 
             "c"),
    Question("\033[96m1)Which Python module is commonly used for working with URLs in web APIs?\033[0m", 
             ["\033[93ma) urlparse\033[0m", 
              "\033[93mb) requests\033[0m", 
              "\033[93mc) urllib\033[0m", 
              "\033[93md) urlparse\033[0m"], 
             "d"),
    Question("\033[96m1)What is the primary role of HTTP headers in web API requests and responses?\033[0m", 
             ["\033[93ma) To specify the content type of the data\033[0m", 
              "\033[93mb) To provide metadata about the request or response\033[0m", 
              "\033[93mc) To authenticate users\033[0m", 
              "\033[93md) To authorize access to protected resources\033[0m"], 
             "b"),
    Question("\033[96m1)Which Python library is commonly used for asynchronous web API requests?\033[0m", 
             ["\033[93ma) asyncio\033[0m", 
              "\033[93mb) requests\033[0m", 
              "\033[93mc) aiohttp\033[0m", 
              "\033[93md) httpx\033[0m"], 
             "c"),
    Question("\033[96m1)What is the purpose of content negotiation in web APIs?\033[0m", 
             ["\033[93ma) To optimize database queries\033[0m", 
              "\033[93mb) To negotiate the price of API access\033[0m", 
              "\033[93mc) To specify the format of the data in the request or response\033[0m", 
              "\033[93md) To prevent unauthorized access\033[0m"], 
             "c"),
]

def run_quiz(questions):
    score = 0

    print("\n" * 2)  # Add space before the quiz
    print("\033[95mPython Web APIs\033[0m\n")
    print("\033[95mIntroduction to Coding Project\033[0m\n\n" + "-" * 80)

    for i, question in enumerate(questions):
        print("\033[1m" + question.prompt + "\033[0m")  # Use \033[1m for bold
        for option in question.options:
            print(option)
        print("\n" + "-" * 80 + "\n")  # Add dashes as separation between questions

        answer = input("\033[92mEnter your answer (a, b, c, or d): \033[0m").lower()
        if answer == question.correct_answer:
            print("\n\033[92mCorrect!\033[0m\n")
            score += 1
        else:
            print("\n\033[91mIncorrect.\n\033[0m", "\n\033[92mThe correct answer is:", question.correct_answer, "\033[0m\n")

    print("\n" * 2)  # Add space after the quiz
    print("Your score is:", score, "/", len(questions))

run_quiz(questions)
