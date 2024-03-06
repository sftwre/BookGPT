from dotenv import load_dotenv
load_dotenv()
from characters import MainCharacterChain
from structure import get_structure
from events import get_events
from writing import write_book

subject = "Machine War"
author = "Ernest Hemingway"
genre = "horror"

main_character_chain = MainCharacterChain()
profile = main_character_chain.run('profile.pdf')

title, plot, chapters_dict = get_structure(subject, genre, author, profile)
summaries_dict, event_dict = get_events(subject, genre, author,
                                        profile, title, plot, chapters_dict)

book = write_book(genre, author, title, profile, plot, summaries_dict, event_dict)