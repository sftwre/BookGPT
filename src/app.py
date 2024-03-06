from dotenv import load_dotenv
load_dotenv()
from characters import MainCharacterChain
from structure import get_structure
from events import ChapterPlotChain

subject = "Machine War"
author = "Ernest Hemingway"
genre = "horror"

main_character_chain = MainCharacterChain()
profile = main_character_chain.run('profile.pdf')

title, plot, chapters_dict = get_structure(subject, genre, author, profile)

chapter_plot_chain = ChapterPlotChain()
summaries_dict = {}

for chapter, _ in chapters_dict.items():

    summaries_dict[chapter] = chapter_plot_chain.run(
        subject,
        genre,
        author,
        profile,
        title,
        plot,
        summaries_dict,
        chapters_dict,
        chapter
    )

for chapter, plot in summaries_dict.items():
    print(chapter)
    print(plot)