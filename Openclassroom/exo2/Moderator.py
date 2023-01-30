class Moderator:
    def edit(self, post, content):
        """modifier un sms"""
        post.content = content

    def delete(self, thread, post):
        """supprimer un message"""
        index = thread.posts.index(post)
        del thread.posts[index]