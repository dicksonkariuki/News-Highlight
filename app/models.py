class Source:
    """
    Source class to define  News Source objects
    """
    def __init__(self,id,title,description,url,category,country):
        self.id = id
        self.title = title
        self.description = description
        self.url = url 
        self.category = category 
        self.country = country

class Articles:
    """
    Articles class to define the News article objects
    """
    def __init__(self,id, name,title, author,description,url,urlToImage,publishedAt)
        self.id = id 
        self.name = name
        self.title = title
        self.author = author
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
