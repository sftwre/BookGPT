from dotenv import load_dotenv
load_dotenv()
from characters import MainCharacterChain
from structure import get_structure

subject = "Machine War"
author = "Ernest Hemingway"
genre = "horror"

main_character_chain = MainCharacterChain()
profile = main_character_chain.run('profile.pdf')

title, plot, chapters_dict = get_structure(subject, genre, author, profile)