from Openclassroom.exo2.FilePost import FilePost
from Openclassroom.exo2.Post import Post


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print(f"L'utilisateur {self.username} est connecté.")

    def post(self, thread, content, file=None):
        """post un message dans la file de discusion"""
        if file:
            post = FilePost (self, "aujourdhui", content=content)
        else:
            post = Post(user=self, time_posted="aujourd'hui", content=content)
        thread.add_post(post)
        return post

    def make_thread(self, title, content):
        """ Créé un nouveau fil de discusssion"""
        post = Post(self, "aujourd'hui", content)
        return Thread(title, "aujourd'hui", post)

    def __str__(self):
        return self.username
