class Article:
    """Model class representing an article."""
    def __init__(self, title, author, num_characters, publisher, summary):
        self.title = title
        self.author = author
        self.num_characters = num_characters
        self.publisher = publisher
        self.summary = summary

    def __str__(self):
        return f"Article '{self.title}' by {self.author}"

class ArticleView:
    """View class for displaying an article."""
    @staticmethod
    def display_article(article):
        print(f"Title: {article.title}")
        print(f"Author: {article.author}")
        print(f"Number of Characters: {article.num_characters}")
        print(f"Published at: {article.publisher}")
        print(f"Summary: {article.summary}\n")

class ArticleController:
    """Controller class to mediate between the model (Article) and the view (ArticleView)."""
    def __init__(self, article, view):
        self.article = article
        self.view = view

    def display_view(self):
        self.view.display_article(self.article)

# Example usage:
if __name__ == "__main__":
    # Create an instance of Article
    article = Article("The Rise of Python", "Jane Doe", 2500, "Python Journal", "An analysis of the factors driving Python's popularity.")

    # Create an instance of ArticleView
    view = ArticleView()

    # Create an instance of ArticleController with the model and view
    controller = ArticleController(article, view)

    # Display the article using the controller
    controller.display_view()