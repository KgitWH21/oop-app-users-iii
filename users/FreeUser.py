from .User import User


class FreeUser(User):
    def create_post(self, content):
        if len(self.posts) < 2:
            super().create_post(content)
            return True

        print("Free user limited to two posts")
        return False