from pyscript import document
import random

creator_info = {
    "name": "Jose Mateo Madrid Salacup",
    "bio": (
        "Hi! I'm Jose Mateo, a Grade 10 student from OB Montessori Center - Fairview. "
        "My biggest dream is to pursue a career in medicine as a pediatrician—researching childhood "
        "illnesses and creating a warm, comforting healthcare environment for young patients. When I'm not "
        "studying or coding with Python and PyScript, you can find me online window shopping, "
        "writing on my MacBook, or diving into global documentaries."
    ),
    "interests": [
        "Pediatrics & Medical Science",
        "Pop Music, EDM, Rap, Hip-Hop, & R&B",
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

interests_list = ", ".join(creator_info["interests"])

info_html = f"""
<p><strong>Name:</strong> {creator_info["name"]}</p>
<p><strong>About Me:</strong> {creator_info["bio"]}</p>
<p><strong>Interests:</strong> {interests_list}</p>
<p><strong>Favorite Quote:</strong> <em>{creator_info["quote"]}</em> {creator_info["quote_author"]}</p>
"""
document.getElementById("profile-output").innerHTML = info_html

def show_fun_fact(event):
    global last_fact
    available_facts = [f for f in fun_facts if f != last_fact]
    chosen_fact = random.choice(available_facts)
    last_fact = chosen_fact
    document.getElementById("fact-output").innerText = chosen_fact
