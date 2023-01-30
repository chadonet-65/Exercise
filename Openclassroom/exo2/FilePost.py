from Openclassroom.exo2.Post import Post


class FilePost(Post):
    def __init__(self, user, time_posted, content, file):
        self.user = user
        self.time_posted = time_posted
        self.content = content
        self.file = file

    def display(self):
        super().display()
        print("pièce jointe")
        self.file.display()