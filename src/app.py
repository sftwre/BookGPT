from dotenv import load_dotenv
load_dotenv()
from characters import MainCharacterChain
from structure import get_structure
from events import get_events
from writing import write_book
from publishing import DocWriter

subject = "Machine War"
author = "Ernest Hemingway"
genre = "horror"

main_character_chain = MainCharacterChain()
profile = main_character_chain.run('profile.pdf')
doc_writer = DocWriter()

title, plot, chapters_dict = get_structure(subject, genre, author, profile)
summaries_dict, event_dict = get_events(subject, genre, author,
                                        profile, title, plot, chapters_dict)

book = write_book(genre, author, title, profile, plot, summaries_dict, event_dict)

doc_writer.write_doc(book, chapters_dict, title)