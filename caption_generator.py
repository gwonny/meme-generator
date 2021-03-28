import random

NOUNS=[]
ADJECTIVES=[]
VERBS=[]

MEME_TEMPLATES = (

    "ONE DOES NOT SIMPLY | {VERB} {NOUN}",
    "When you {VERB} a {NOUN} | Thats not getting {VERB}ed",
    "{NOUN} | Y U NO {VERB} {NOUN}s",
    "{VERB} ALL OF THE {NOUN}s"
)



def randomNoun():
    r = random.randint(0, len(NOUNS))
    return NOUNS[r]
def randomAdj():
    r = random.randint(0, len(ADJECTIVES))
    return ADJECTIVES[r]
def randomVerb():
    r = random.randint(0, len(VERBS))
    return VERBS[r]
def generate_caption(caption_template):

    if (caption_template == ''):
        pass
    else:
        pass



