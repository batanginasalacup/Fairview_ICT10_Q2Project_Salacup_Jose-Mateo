from pyscript import document
import random

# Creator profile data stored in a structured dictionary
creator_info = {
    "name": "Jose Mateo Madrid Salacup",
    "tagline": "Grade 10 Student | Aspiring Pediatrician | Music & Literature Enthusiast",
    "bio": (
        "Hi! I'm Jose Mateo, a Grade 10 student from OB Montessori Center - Fairview. "
        "My biggest dream is to pursue a career in medicine as a pediatrician—researching childhood "
        "illnesses and creating a warm, comforting healthcare environment for young patients. When I'm not "
        "studying or coding with Python and PyScript, you can find me online window shopping, "
        "writing on my MacBook, or diving into global documentaries."
    ),
    "interests": [
        "Pediatrics & Medical Science",
        "Pop Music, EDM, Rap, Hip-Hip, & R&B",
        "True Crime Documentaries",
        "Fashion & Purse Collecting",
        "LGBTQ+ & Women's Rights Advocacy"
    ],
    "quote": "\"If you can't love yourself, how in the hell are you going to love somebody else?\"",
    "quote_author": "— RuPaul"
}

fun_facts = [
    "I've been researching true crime cases and watching global crime documentaries since I was eleven!",
    "I find using my MacBook as an escape from reality.",
    "One of my favorite songs to listen to is 'Born To Die' by Lana Del Rey.",
    "I love collecting unique wardrobe pieces and purses.",
    "I speak up for LGBTQ+ rights and women's rights."
]

last_fact = ""

def load_profile():
    document.getElementById("creator-name").innerText = creator_info["name"]
    document.getElementById("creator-tagline").innerText = creator_info["tagline"]
    document.getElementById("creator-bio").innerText = creator_info["bio"]
    document.getElementById("creator-quote").innerText = creator_info["quote"]
    document.getElementById("quote-author").innerText = creator_info["quote_author"]

    interests_div = document.getElementById("interests-container")
    badges_html = "".join(
        f'<span class="badge-interest">{item}</span>' for item in creator_info["interests"]
    )
    interests_div.innerHTML = badges_html

def show_fun_fact(event):
    global last_fact
    available_facts = [fact for fact in fun_facts if fact != last_fact]
    chosen_fact = random.choice(available_facts)
    last_fact = chosen_fact
    document.getElementById("fun-fact-output").innerText = f"✨ {chosen_fact}"

# Run initialization when PyScript loads
load_profile()