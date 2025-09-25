import streamlit as st
import numpy as np
from typing import Dict, Any, List


def question_problems_generator(key: str, label: str) -> int:
    options = [
        "Charge straight in, no hesitation",
        "Take a step back, analyze carefully",
        "Ask for help and work with others",
        "Build a tool or system to solve it",
        "Try something unexpected just to see what happens",
    ]

    answer = st.radio(
        label=label,
        options=options,
        key=key,
        index=None,
    )
    return options.index(answer) if answer is not None else None


def question_problems_comparator(answer) -> np.ndarray:
    answer_key = [
        np.array([0, 1, 0, 0, 0, 0, 0, 0, 0]),  # Soldier
        np.array([0, 0, 0, 0, 0, 0, 0, 1, 1]),  # Sniper, Spy
        np.array([0, 0, 0, 0, 1, 0, 1, 0, 0]),  # Heavy, Medic
        np.array([0, 0, 0, 0, 0, 1, 0, 0, 0]),  # Engineer
        np.array([0, 0, 1, 1, 0, 0, 0, 0, 0]),  # Pyro, Demoman
    ]

    return np.zeros(9) if answer not in range(len(answer_key)) else answer_key[answer]


def question_energy_generator(key: str, label: str) -> int:
    options = [
        "Loud and outgoing, always moving",
        "Serious and focused",
        "Supportive and dependable",
        "Calm and practical",
        "Chaotic but fun",
    ]
    answer = st.radio(label=label, options=options, key=key, index=None)
    return options.index(answer) if answer is not None else None


def question_energy_comparator(answer) -> np.ndarray:
    answer_key = [
        np.array([1, 0, 0, 0, 0, 0, 0, 0, 0]),  # Scout
        np.array([0, 0, 0, 0, 0, 0, 0, 1, 1]),  # Sniper, Spy
        np.array([0, 0, 0, 0, 1, 0, 1, 0, 0]),  # Heavy, Medic
        np.array([0, 1, 0, 0, 0, 1, 0, 0, 0]),  # Soldier, Engineer
        np.array([0, 0, 1, 1, 0, 0, 0, 0, 0]),  # Pyro, Demoman
    ]

    return np.zeros(9) if answer not in range(len(answer_key)) else answer_key[answer]


def question_snack_generator(key: str, label: str) -> int:
    options = [
        "Quick snack, like chips or candy",
        "Something strong, like coffee or dark chocolate",
        "A full hearty meal",
        "Something simple and practical",
        "Whatever's the most fun or colorful",
    ]
    answer = st.radio(label=label, options=options, key=key, index=None)
    return options.index(answer) if answer is not None else None


def question_snack_comparator(answer) -> np.ndarray:
    answer_key = [
        np.array([1, 0, 0, 0, 0, 0, 0, 0, 0]),  # Scout
        np.array([0, 0, 0, 0, 0, 0, 1, 0, 1]),  # Medic, Spy
        np.array([0, 1, 0, 0, 1, 0, 0, 0, 0]),  # Soldier, Heavy
        np.array([0, 0, 0, 0, 0, 1, 0, 1, 0]),  # Engineer, Sniper
        np.array([0, 0, 1, 1, 0, 0, 0, 0, 0]),  # Pyro, Demoman
    ]

    return np.zeros(9) if answer not in range(len(answer_key)) else answer_key[answer]


def question_movie_generator(key: str, label: str) -> int:
    options = [
        "Fast-talking comic relief",
        "The rival or anti-hero",
        "The loyal best friend",
        "The brainy planner",
        "The mysterious wildcard",
    ]
    answer = st.radio(label=label, options=options, key=key, index=None)
    return options.index(answer) if answer is not None else None


def question_movie_comparator(answer) -> np.ndarray:
    answer_key = [
        np.array([1, 0, 0, 0, 0, 0, 0, 0, 0]),  # Scout
        np.array([0, 0, 0, 0, 0, 0, 0, 1, 1]),  # Sniper, Spy
        np.array([0, 0, 0, 0, 1, 0, 1, 0, 0]),  # Heavy, Medic
        np.array([0, 0, 0, 0, 0, 1, 0, 0, 0]),  # Engineer
        np.array([0, 0, 1, 1, 0, 0, 0, 0, 0]),  # Pyro, Demoman
    ]

    return np.zeros(9) if answer not in range(len(answer_key)) else answer_key[answer]


def question_vibe_generator(key: str, label: str) -> int:
    options = [
        "Always chasing the next thing",
        "Reliable and steady",
        "Tinkering with ideas and tools",
        "Helping people directly",
        "Unpredictable and playful",
    ]
    answer = st.radio(label=label, options=options, key=key, index=None)
    return options.index(answer) if answer is not None else None


def question_vibe_comparator(answer) -> np.ndarray:
    answer_key = [
        np.array([1, 0, 0, 0, 0, 0, 0, 0, 0]),  # Scout
        np.array([0, 1, 0, 0, 1, 0, 0, 0, 0]),  # Soldier, Heavy
        np.array([0, 0, 0, 0, 0, 1, 0, 0, 0]),  # Engineer
        np.array([0, 0, 0, 0, 0, 0, 1, 0, 0]),  # Medic
        np.array([0, 0, 1, 1, 0, 0, 0, 0, 1]),  # Pyro, Demoman, Spy
    ]

    return np.zeros(9) if answer not in range(len(answer_key)) else answer_key[answer]


def question_drink_generator(key: str, label: str) -> int:
    options = [
        "Soda – pure sugar rocket fuel",
        "Whiskey – breakfast, lunch, and dinner",
        "Coffee – bitter as my soul",
        "Protein Shake – gains before brains",
        "Fine Wine – because I’m better than you",
    ]
    answer = st.selectbox(label=label, options=options, key=key, index=None) # NEW
    return options.index(answer) if answer is not None else None


def question_drink_comparator(answer) -> np.ndarray:
    answer_key = [
        np.array([1, 0, 1, 0, 0, 0, 0, 0, 0]),  # Soda → Scout, Pyro
        np.array([0, 0, 0, 1, 0, 1, 0, 0, 0]),  # Whiskey → Demo, Engineer
        np.array([0, 1, 0, 0, 0, 0, 1, 0, 0]),  # Coffee → Soldier, Medic
        np.array([0, 0, 0, 0, 1, 0, 0, 0, 0]),  # Protein Shake → Heavy
        np.array([0, 0, 0, 0, 0, 0, 0, 1, 1]),  # Fine Wine → Spy, Sniper
    ]

    return np.zeros(9) if answer not in range(len(answer_key)) else answer_key[answer]


def question_chaos_generator(key: str, label: str) -> int:
    answer = st.slider( # NEW
        label=label,
        min_value=0,
        max_value=100,
        step=1,
        key=key,
    )

    return answer // 20


def question_chaos_comparator(answer) -> np.ndarray:
    answer_key = [
        np.array([0, 0, 0, 0, 1, 0, 0, 0, 1]),  # Heavy, Sniper
        np.array([0, 1, 0, 0, 0, 1, 0, 0, 0]),  # Soldier, Engineer
        np.array([0, 0, 0, 0, 0, 0, 1, 1, 0]),  # Medic, Spy
        np.array([1, 0, 0, 1, 0, 0, 0, 0, 0]),  # Scout, Demo
        np.array([0, 0, 1, 0, 0, 0, 0, 0, 0]),  # Pyro
    ]

    return np.zeros(9) if answer not in range(len(answer_key)) else answer_key[answer]


def question_books_generator(key: str, label: str) -> List[int]:
    options = [
        "The Bible – a mix of discipline, faith, and guidance",                   # Soldier, Medic
        "Explosives for Dummies – chaotic, dangerous, but somehow effective",     # Demoman, Pyro
        "How to Win Friends and Influence People – clever, strategic networking", # Engineer, Spy
        "The Art of War – serious, tactical, and focused",                        # Sniper, Heavy
        "A Romance Novel – impulsive, passionate, and full of drama",
    ]
    answer = st.multiselect(label=label, options=options, key=key)  # NEW
    return [options.index(ele) for ele in answer]


def question_books_comparator(answer) -> np.ndarray:
    answer_key = [
        np.array([0, 1, 0, 0, 0, 0, 0, 1, 0]),  # Bible → Soldier, Medic
        np.array([0, 0, 1, 1, 0, 0, 0, 0, 0]),  # Explosives → Demo, Pyro
        np.array([0, 0, 0, 0, 0, 1, 0, 0, 1]),  # Win Friends → Engie, Spy
        np.array([0, 0, 0, 0, 0, 0, 1, 0, 1]),  # Art of War → Sniper, Heavy
        np.array([1, 0, 1, 0, 0, 0, 0, 0, 0]),  # Romance → Scout, Pyro
    ]

    if not answer:
        return np.zeros(9)

    total = np.zeros(9)
    for answer in answer:
        total += answer

    return total


questions = [
    {
        "text": "How do you usually approach problems?",
        "caption": "What 11 PhD's does to a man",
        "image_extension": "jpg",
        "generator": question_problems_generator,
        "comparator": question_problems_comparator,
    },
    {
        "text": "Which of these best describes your energy in a group?",
        "caption": "Just kickin' around",
        "image_extension": "gif",
        "generator": question_energy_generator,
        "comparator": question_energy_comparator,
    },
    {
        "caption": "Aye, went tae Mexico an’ woke up wi’ a sombrero an’ no’ me left shoe!",
        "text": "Pick your poison: what’s your favorite drink?",
        "image_extension": "gif",
        "generator": question_drink_generator,
        "comparator": question_drink_comparator,
    },
    {
        "text": "What’s your go-to snack personality?",
        "caption": "Hmmm sandvich",
        "image_extension": "gif",
        "generator": question_snack_generator,
        "comparator": question_snack_comparator,
    },
    {
        "text": "If you were in a movie, you’d be…",
        "caption": "Heavy was awarded a Saxxy for his work on the End of the Line short",
        "image_extension": "png",
        "generator": question_movie_generator,
        "comparator": question_movie_comparator,
    },
    {
        "text": "Which vibe feels the most like you?",
        "caption": "Bakin' bacon",
        "image_extension": "gif",
        "generator": question_vibe_generator,
        "comparator": question_vibe_comparator,
    },
    {
        "caption": "Hmmph hmmm!",
        "text": "How much do you agree: 'I thrive in absolute chaos — the messier, the better.'",
        "image_extension": "gif",
        "generator": question_chaos_generator,
        "comparator": question_chaos_comparator,
    },
    {
        "caption": "",
        "text": "If you had to pick some books to read on a vacation, which would it be?",
        "image_extension": "jpg",
        "generator": question_books_generator,
        "comparator": question_books_comparator,
    }
]

characters = [
    {
        "name": "Scout",
        "description": "Fast boi, talks twice as fast as he runs! You are not scared to take risks and are always up to something. People either love your energy or get completely exhausted by it. You’ve got a mischievous streak, but deep down you’re just here to have fun and prove yourself. Quick on your feet, quick with your mouth — you’re chaos with sneakers.",
    },
    {
        "name": "Soldier",
        "description": "Patriotic rocket jumper extraordinaire! You live life like it’s a constant pep rally, fueled by stubbornness and sheer willpower. Plans? Who needs ‘em, you just charge in headfirst and somehow make it work. People admire your confidence… or wonder if you’ve hit your head one too many times. Either way, you bring intensity and loyalty everywhere you go.",
    },
    {
        "name": "Pyro",
        "description": "Mmph mmph mmph! (Translation: chaos incarnate). You live in your own little world, and it’s somehow both adorable and terrifying. To some, you’re a pure cinnamon roll; to others, you’re a walking nightmare. The truth is, you thrive in unpredictability and aren’t afraid to embrace your inner weirdo. Life’s more fun when everything’s on fire, right?",
    },
    {
        "name": "Demoman",
        "description": "Explosive-loving, one-eyed Scottish cyclops! You’re the life of the party and the bringer of total destruction — often at the same time. People can count on you for a laugh, but also for blowing a hole in the wall when it’s least expected. Your vibe is equal parts hilarious and reckless, but somehow it all works out. If chaos had a drinking buddy, it would be you.",
    },
    {
        "name": "Heavy",
        "description": "Big guy, bigger gun, biggest appetite for sandwiches. You’re the gentle giant type — intimidating on the outside, but warm and loyal to the people you care about. Folks know not to mess with you, but your close friends get to see your softer, funnier side. You’re dependable, strong, and a little goofy — a true tank in both heart and spirit.",
    },
    {
        "name": "Engineer",
        "description": "Texan mastermind of ‘buildin’ stuff’ and pressing buttons. You’re clever, resourceful, and probably the one who fixes everyone else’s messes. People rely on you more than you realize, because you make complicated things look simple. You’d rather build stability than rush into chaos, but when the situation calls for it, you’ve always got a gadget (or a plan) ready.",
    },
    {
        "name": "Medic",
        "description": "Mad scientist with a medical license (maybe). You’ve got brains, curiosity, and a slightly unsettling love of experimenting. People might find you eccentric, but they can’t deny how much they need you when things get tough. You’re the type who pushes boundaries and finds joy in the strange, and honestly? That’s what makes you unforgettable.",
    },
    {
        "name": "Sniper",
        "description": "Professional loner who considers camping a lifestyle. You’re calm, focused, and maybe a little detached — but that’s because you like doing things your own way. Crowds aren’t really your scene; you’d rather hang back, observe, and strike when the timing is perfect. People underestimate you until it’s too late, and honestly? You like it that way.",
    },
    {
        "name": "Spy",
        "description": "French accent, sharp knife, and your worst trust issues. You’re smooth, charming, and always five steps ahead of everyone else. People never quite know what you’re up to, and that’s exactly how you like it. You thrive on mystery, style, and a little bit of drama. Deep down, though, you just enjoy keeping life interesting — and maybe breaking a few hearts along the way.",
    },
]


def question_template(question_number: int, question_dict: Dict[str, Any]) -> np.ndarray:
    st.subheader(f"Question {question_number}")

    _, middle_col, _ = st.columns(3)
    with middle_col:
        st.image(f"Images/questions/question_{question_number}.{question_dict['image_extension']}", caption=question_dict["caption"])

    answer = question_dict["generator"](key=str(question_number), label=question_dict["text"])
    st.write("---")

    return question_dict["comparator"](answer)


def determine_character(score_vector: np.ndarray) -> Dict[str, Any]:
    winning_index = np.argmax(score_vector)
    return characters[winning_index]


def display_result(character: Dict[str, Any]):
    st.balloons() # NEW
    st.subheader(f"You are: The {character['name']}")
    _, middle_col, _ = st.columns([1, 2, 1])
    with middle_col:
        st.image(f"Images/characters/{character['name'].lower()}.gif")
    st.write(character["description"])


def run_quiz() -> None:
    answered_questions = 0
    total_questions = len(questions)

    st.title("Which TF2 Class Are You?")
    st.video("https://www.youtube.com/watch?v=hB0uIFcLRbc") # NEW
    st.write(
        "So, you want to discover who you would be in the Team Fortress 2 (AKA TF2, AKA the GOAT)? "
        "Fear no more as Merasmus, the Administrator, and I have brought this quiz officially approved by Gabe Newell "
        "to tell you who you would be out of the 9 classes!"
    )
    st.write("---")

    result_vector = np.zeros(9)

    for i, question in enumerate(questions):
        current_answer_vector = question_template(i + 1, question)
        result_vector += current_answer_vector

        if np.any(current_answer_vector):
            answered_questions += 1

    if st.button("Submit"):
        if answered_questions < total_questions:
            st.warning("You have unanswered questions!")
        else:
            character = determine_character(result_vector)
            display_result(character)


if __name__ == "__main__":
    run_quiz()