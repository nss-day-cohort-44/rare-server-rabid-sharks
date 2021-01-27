

# let's define a class
class Comment():
    # class initializer, 5 params
    # DON'T FORGET the SELF
    def __init__(self, post_id, author_id, content, subject, created_on):
        self.id = id
        self.post_id = post_id
        self.author_id = author_id
        self.content = content
        self.subject = subject
        self.created_on = created_on
