from utils import BaseStructureChain, ChatOpenAI

class TitleChain(BaseStructureChain):

    PROMPT = """
    Your job is to generate the title for a novel about the following subject and main character.
    Return a title and only a title!
    The title should be consistent with the genre of the novel.
    The title should be consistent with the style of the author.

    Subject: {subject}
    Genre: {genre}
    Author: {author}

    Main character's profile: {profile}

    Title:"""

    def run(self, subject, genre, author, profile):
        return self.chain.predict(
            subject=subject,
            genre=genre,
            author=author,
            profile=profile
        )
    
class PlotChain(BaseStructureChain):

    PROMPT  = """
    Your job is to generate the plot for a novel. Return a plot and only a plot!
    Describe the full plot of the story and don't hesitate to create new characters.
    You are provided the following subject, title and main character's profile.
    Make sure that the main character is at the center of the story.
    The plot should be consistent with the genre of the novel.
    The plot should be consistent with the style of the author.

    Consider the following attributes to write an exciting story:
    {features}

    subject: {subject}
    Genre: {genre}
    Author: {author}

    Title: {title}
    Main character's profile: {profile}

    Plot:"""

    HELPER_PROMPT  = """
    Generate a list of attributes that characterized an exciting story.
    List of attributes:"""

    def run(self, subject, genre, author, profile, title):
        features = ChatOpenAI().predict(self.HELPER_PROMPT)
        plot = self.chain.predict(
            features=features,
            subject=subject,
            genre=genre,
            author=author,
            profile=profile,
            title=title
        )
        return plot
    
class ChaptersChain(BaseStructureChain):

    PROMPT = """
    Your job is to generate a list of chapters.
    ONLY the list and nothing more!
    You are provided with a title, a plot and a main character for a novel.
    Generate a list of chapters describing the plot of the novel.
    """