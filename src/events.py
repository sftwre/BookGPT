
from utils import BaseEventChain, ChatOpenAI

class ChapterPlotChain(BaseEventChain):

    HELPER_PROMPT = """
    Generate a list of attributes that characterized an exciting story.

    List of attributes:"""

    PROMPT = """
    You are a writer and your job is to generate the plot for one and only one chapter of a novel.
    You are provided with the title, the main plot of the novel and the main character.
    Additionally,  you are provided with the plots of the previous chapters and and the outline of the novel.
    Make sure to generate a plot that describe accurately the story of the chapter.
    Each chapter should have its own arc, but should be consistent with the other chapters and the overall story.
    The summary should be consistent with the genre of the novel.
    The summary should be consistent with the style of the author.

    Consider the following attributes to write an exciting story:
    {features}

    subject: {subject}
    Genre: {genre}
    Author: {author}

    Title: {title}
    Main character's profile: {profile}

    Novel's Plot: {plot}

    Outline:
    {outline}

    Chapter Plots:
    {summaries}

    Return the plot and only the plot
    Plot of {chapter}:"""
    
    def run(self, subject, genre, author,
             profile, title, plot, summaries_dict,
             chapter_dict, chapter):
        
        features = ChatOpenAI().predict(self.HELPER_PROMPT)

        outline = '\n'.join([
            '{} - {}'.format(chapter, description)
            for chapter, description in chapter_dict.items()
        ])

        summaries = '\n\n'.join([
            'Plot of {}: {}'.format(chapter, summary)
            for chapter, summary in summaries_dict.items()
        ])

        return self.chain.predict(
            subject=subject,
            genre=genre,
            author=author,
            profile=profile,
            title=title,
            plot=plot,
            features=features,
            outline=outline,
            summaries=summaries,
            chapter=chapter
        )