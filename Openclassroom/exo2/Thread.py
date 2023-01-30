class Thread:
    """fil de discusion"""

    def __init__(self, title, time_posted, post):
        self.title = title
        self.time_posted = time_posted
        self.post = [post]

    def display(self):
        print("------THREAD------")
        print(f"titre: {self.title}, date: {self.time_posted}")
        print()
        for post in self.posts:
            post.display()
            print()
        print("-------------------")

    def add_post(self, post):
        self.posts.append(post)