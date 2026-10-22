from brain import brain


def context_for_ai(path):
    with open(path, "r") as file:
        return file.read()


def ask_for_prompt():
    prompt = input(
        "What would you like to ask our Agent about our Credit Card Terms? "
    )
    return prompt


def flow():

    final_prompt = ask_for_prompt()

    final_context = context_for_ai(
        "credit_card_terms.csv"
    )

    return final_prompt, final_context


def main():

    print("Welcome")

    final_prompt, final_context = flow()

    response_from_ai = brain(
        final_context,
        final_prompt
    )

    return {
        "message": "Our Agent has responded 🤖:",
        "Ai Agent": response_from_ai
    }


print(main())