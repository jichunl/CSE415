import re   # Loads the regular expression module.
import random


def xl74agent():
    introduce()

    # while True:
    #     the_input = input('TYPE HERE:>> ')
    #     if re.match('bye', the_input):
    #         print('That was a fun conversation.')
    #         print('Have a good day, my friend.')
    #         return
    #
    #     print(respond(the_input))

def introduce():
    return ("""I\'m Senpai.
    I am a collage student.
    Only black tea will be served during our talk.
    We better have the conversation at the roof level.
    Follow me. 
    By the way, you can talk to xl74 if you think something goes wrong.""")


def agentName():
    return 'SenpaiMan'



feeling_cycle = 0

reason_cycle = 0

wait_cycle = 0

memories = []

activity_memory = ''


def respond(the_input):
    wordlist = re.split(' ', remove_punctuation(the_input))
    wordlist[0] = wordlist[0].lower()

    mapped_wordlist = you_me_map(wordlist)

    global activity_memory
    global  memories
    #   Add the keyword to memory list if the sentence mentioned it
    for w in wordlist:
        if w in MEMORY_LIST:
            memories = [w] + memories

    if wordlist[0] == '':
        #   User says nothing
        return ("Silence is not what I expected. " +
                "Tell me more about yourself.")

    if wordlist[0:2] == ['good', 'morning']:
        #   Ask user about weather
        return "Good morning. What is the weather today?"

    if 'rainy' in wordlist:
        #   Suggest about activity
        return "Let's have some fun indoor."

    if 'sunny' in wordlist:
        #   Suggest about activity
        return "I suggest we go outside."

    if 'cooking' in wordlist:
        #   Ask about food for cooking
        #   Memorize activity
        activity_memory = 'cooking'
        return "Do you have food suggestion?"

    if 'shopping' in wordlist:
        #   Ask about food for buying
        #   Memorize activity
        activity_memory = 'shopping'
        return "Do you have suggestion for food?"

    if 'level' in wordlist:
        #   Return some measurement
        return random.choice(['One', 'Two', 'Three', 'Four']) + '.'

    if ('salad' in wordlist) or ('taco' in wordlist):
        #   Give opinions about certain food
        return "I hate those."

    if ('meat' in wordlist) or ('junkfood' in wordlist):
        #   Give opinions about certain food
        return "I love that!"

    if 'insist' in wordlist:
        #   Suggest something about early mentioned activity
        if activity_memory != '':
            return ("You talked about " + activity_memory + "; "
                    + "other ideas?")
        return "Other ideas?"

    if wordlist[-2:] == ['favorite', 'restaurant']:
        #   Give favorite restaurant
        fav_res = random.choice([
            'KurgerBing',
            'EagleSlow',
            'WacDownload',
            'BakoShell'
        ])
        return fav_res  + " is my favorite restaurant; order it."

    if 'minutes' in wordlist:
        #   Cycle about time
        global wait_cycle
        result = {
            0: "That is long waiting time.",
            1: "I am still waiting.",
            2: "I will keep waiting.",
            3: "Its finally delivered!"
        }.get(wait_cycle)

        wait_cycle = (wait_cycle + 1) % 4
        return result

    if ('dinner' in wordlist) or ('lunch' in wordlist) or ('breakfast' in wordlist):
        #   Give opinion about dinner
        return "Please give me some tea. It's too spicy."

    if 'full' in wordlist:
        #   Reply to fullness
        return "I think I am still hungry."

    if 'BMI' in wordlist:
        #   Talk about BMI
        if 'high' in wordlist:
            return "No I am not. I force you to give me more food!"
        elif 'low' in wordlist:
            return "It is not good. Eat more, my friend."
        else:
            return "Exercise and eat well guarantee balanced BMI value."

    if 'declined' in wordlist:
        #   Show anger when request is rejected
        return "Useless! I will do it myself!"

    if  wordlist[0:2] == ['i', 'am']:
        if re.match(r".+ing$", wordlist[2]):
            #   User is doing something
            return "Why are you " + stringify(wordlist[2:]) + '?'

        #   User is something
        return ("Interesting. What makes you " +
                stringify(mapped_wordlist[2:]) + '?')

    if wordlist[0:2] == ['i', 'have']:
        #   User have something or have done something
        return ("That sounds like something special. Why " +
                stringify(mapped_wordlist) + '.')

    if wordlist[0:2] == ['i', 'feel']:
        #   Cycle among 3 answers, positive, negative, questioning.
        global feeling_cycle

        result = {0: "You are right; I feel the same way.",
                  1: "I am sorry but I don't think so.",
                  2: "Why do you feel like that?"}.get(feeling_cycle)

        feeling_cycle = (feeling_cycle + 1) % 3
        return result

    if wpred(wordlist[0]):
        if wordlist[0] == 'why':
            if  wordlist[1:3] == ['are', 'you']:
                #   When asked something about the bot's idea
                return "I don't know; I sometimes cannot control myself."

            #   Choose randomly from a set of 2 answers to reasoning.
            return random.choice([
                "I really hope I know the reason, but I don't.",
                "I know you know the answer, don't you?"])

        if wordlist[0] == 'when':
            if wordlist[1:3] == ['will', 'you']:
                #   When asked about bot's schedule
                return "I think I will have it done by this weekend."

            if wordlist[1:3] == ['have', 'you']:
                #   When asked about something in the past
                return random.choice([
                    "It was too long ago. I cannot recall it.",
                    "I have " + stringify(mapped_wordlist[3:]) +
                    " a month ago."])

            #   Answer something about time
            return "I don't know exactly. Tell me more about it."

        if wordlist[0] == 'where':
            if wordlist[1] in ['is', 'are']:
                #   When asked the location of something
                return "I know the location must be near the Earth."

            #   Answer something about location
            return "You will find it on search engine."

        if wordlist[0] == 'how':
            return "That is a hard one. I wish you could find it out yourself."

    if 'because' in wordlist:
        #   Cycle among 2 answers for reasoning
        global reason_cycle
        result = {1: "Why do you think that is the reason?",
                  2: "I see your reasoning."}.get(reason_cycle)
        reason_cycle = (reason_cycle + 1) % 2
        return result

    if 'yes' in wordlist:
        if 'right' in wordlist:
            #   User confirms correctness
            return 'I told you that.'
        #   User confirms something
        return "I think you might be right."

    if 'no' in wordlist:
        if 'wrong' in wordlist:
            #   User confirms wrongness
            return 'What is right then?'
        #   User negates something
        return 'Are you sure about that?'

    if verbp(wordlist[0]):
        #   Random choose to reply to suggestion
        return random.choice([
            "I will try that out!",
            "I am not sure about that.",
            "Can you show me how to " + stringify(wordlist) + '?'
        ])

    if wordlist[0:3] == ['do', 'you', 'think']:
        #   User asks about opinion
        return "I will answer this question later."

    if dpred(wordlist[0]):
        #   User asks for doing something
        return {
            'do': 'Yes, I do ',
            'can': 'I think I can ',
            'should': 'Give me a reason to ',
            'would': 'I would not try to ',
            'could': 'It is my pleasure to ',
            'will': 'I probably will '
        }.get(wordlist[0]) + stringify(wordlist[2:])

    if 'maybe' in wordlist:
        #   User shows uncertainty
        return 'You could be right; let\'s talk more about it.'

    if 'you' in mapped_wordlist or 'You' in mapped_wordlist:
        #   Repeat whatever user says in changed case and in questioning
        return ("Did you just say that " +
                stringify([mapped_wordlist[0].lower()] + mapped_wordlist[1:])
                + '?')

    result = random.choice(KEEP_THE_CONVERSATION)
    if result == "GO_BACK_TO_MEMORY" and len(memories) != 0:
        #   Talk about memory
        #   Pop the first memorized word
        memorized_word = memories[0]
        memories = memories[1:]

        return {
            'exercise': 'Have you recently been exercising?',
            'diet': 'How does it feel to be on diet?',
            'sports': 'What sport do you like the most?',
            'games': 'I think games are great!',
            'study': 'What are you studying for?'
        }.get(memorized_word)
    else:
        #   Nothing to talk
        return result


def stringify(wordlist):
    #   'Create a string from wordlist, but with spaces between words.'
    return ' '.join(wordlist)


punctuation_pattern = r"\,|\.|\?|\!|\;|\:"


def remove_punctuation(text):
    #   'Returns a string without any punctuation.'
    return re.sub(punctuation_pattern, '', text)


def wpred(w):
    #   'Returns True if w is one of the question words.'
    return w in ['when','why','where','how']


def dpred(w):
    #   'Returns True if w is an auxiliary verb.'
    return w in ['do', 'can', 'should' ,'would', 'could', 'will']


KEEP_THE_CONVERSATION = [
    'Tell me more about it.',
    'Keep talking, I\'m listening.',
    'Why do you say that?.',
    'Would you like some tea as a break?',
    'How do you feel about it?',
    'I am curious about that.',
    'I have to go now. Bye.',
    'GO_BACK_TO_MEMORY']


MEMORY_LIST = ['exercise', 'diet', 'sports', 'games', 'study']


CASE_MAP = {'i':'you', 'I':'you', 'me':'you','you':'me',
            'my':'your','your':'my',
            'yours':'mine','mine':'yours','am':'are'}


def you_me(w):
    'Changes a word from 1st to 2nd person or vice-versa.'
    try:
        result = CASE_MAP[w]
    except KeyError:
        result = w
    return result


def you_me_map(wordlist):
    #   'Applies YOU-ME to a whole sentence or phrase.'
    return [you_me(w) for w in wordlist]

def verbp(w):
    #   'Returns True if w is one of these known verbs.'
    return (w in ['go', 'have', 'be', 'try', 'eat', 'take', 'help',
                  'make', 'get', 'jump', 'write', 'type', 'fill',
                  'put', 'turn', 'compute', 'think', 'drink',
                  'blink', 'crash', 'crunch', 'add'])


xl74agent() # Launch the program.

