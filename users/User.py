class User:
    all_posts = []
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.posts = []
    
    def create_post(self, content):
        post = {
          "author": self.username,
          "content": content
        }
        self.posts.append(post)
        User.all_posts.append(post)
        print(self.username + " posted: " + content)
    
    def delete_post(self, content):
        post_to_remove = None
        for post in self.posts:
            if post["content"] == content:
                post_to_remove = post
                break
        
        if post_to_remove:
            self.posts.remove(post_to_remove)
            User.all_posts.remove(post_to_remove)
            print("Post deleted.")
        else:
            print("Post not found.")

user1 = User("Keith", "keith@email.com")

print("--- Creating Posts ---")
user1.create_post("This is my first app post")
user1.create_post("Debugging Python code")

print("Check Global Feed")
print("Global posts count:", len(User.all_posts))

print("Check Individual Feed")

print(f"{user1.username}'s posts:", [p['content'] for p in user1.posts])

