from dotenv import load_dotenv
load_dotenv()
from characters import MainCharacterChain
from structure import TitleChain, PlotChain

subject = "Machine War"
author = "Ernest Hemingway"
genre = "horror"

main_character_chain = MainCharacterChain()
title_chain = TitleChain()
plot_chain = PlotChain()
profile = main_character_chain.run('profile.pdf')


title = title_chain.run(subject=subject,
                        author=author,
                        genre=genre,
                        profile=profile
                        )

plot = plot_chain.run(
    subject=subject,
    author=author,
    genre=genre,
    profile=profile,
    title=title
)

print(title)
print()
print(plot)

