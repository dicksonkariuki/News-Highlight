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
        