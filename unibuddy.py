class UniBuddy:
    def __init__(self):
        self.user_data = {}

    def collect_personal_information(self):
        print("Welcome to UniBuddy! Let's get to know you.")
        self.user_data['name'] = input("What's your name? ")
        self.user_data['age'] = input("How old are you? ")
        self.user_data['favourite_color'] = input("What's your favourite color? ")

    def personalize_responses(self):
        print(f"Nice to meet you, {self.user_data['name']}!")
        print(f"I see that your favorite color is {self.user_data['favourite_color']}.")

    def answer_questions(self):
        while True:
            user_input = input("Ask me anything (type 'exit' to end): ").lower()

            if user_input == 'exit':
                break
            else:
                self.respond_to_query(user_input)

    def respond_to_query(self, query):
        if 'name' in query:
            print(f"My name is UniBuddy. You can call me that!")
        elif 'age' in query:
            print(f"I'm just a computer program, so I don't have an age. But I'm here to help you!")
        elif 'color' in query or 'colour' in query:
            print(f"My favorite color is binary! Just kidding, I'm all about helping you, not colors.")
        else:
            print("I'm not sure how to answer that. Feel free to ask me something else!")

    def run(self):
        self.collect_personal_information()
        self.personalize_responses()
        self.answer_questions()


if __name__ == "__main__":
    unibuddy = UniBuddy()
    unibuddy.run()
