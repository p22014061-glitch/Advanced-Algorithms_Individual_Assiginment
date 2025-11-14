from Graph import Graph
from Person import Person

class FriendNet:

    my_graph = None

    def __init__(self):
        self.my_graph = Graph()

    def add_new_profile(self, name, privacy, biography):
        person = Person(name, privacy, biography)
        self.my_graph.add_vertex(person)
        return person

    def display_all_profiles(self):
        for i, person in enumerate(self.my_graph.graph, start=1):
            print(f"{i}.) {person.getName()}")

    def display_profile(self, index):
        person = list(self.my_graph.graph)[index - 1]
        print(f"Name: {person.getName()}")
        if person.getPrivacy() == 'U':
            print(f"Biography: {person.getBiography()}")
        else:
            print("This profile is private. Biography is hidden.")

    def add_follow(self, follower, followed):
        self.my_graph.add_edge(follower, followed)

    def view_followers(self, index):
        target = list(self.my_graph.graph)[index - 1]
        followers = []
        for person in self.my_graph.graph:
            if target in self.my_graph.graph[person]:
                followers.append(person.getName())

        print("Followers List:")
        if followers:
            for name in followers:
                print(f"- {name}")
        else:
            print("No any account follow this users profile.")

    def view_followed(self, index):
        person = list(self.my_graph.graph)[index - 1]
        followings = self.my_graph.list_outgoing(person)
        print("Followings List:")
        if followings:
            for followed in followings:
                print(f"- {followed.getName()}")
        else:
            print("This account no follow any profile.")

    def unfollow_user(self, follower, followed):
        self.my_graph.remove_edge(follower, followed)


def show_menu():
    print("\n*************************************************")
    print("Welcome to FriendNet, Your Social Media App:")
    print("*************************************************")
    print("1. View names of all profiles")
    print("2. View details for any profile")
    print("3. View followers of any profile (choose any followed to view follower list.)")
    print("4. View followed accounts of any profile (choose any follower to view followed list.)")
    print("5. Add a User Profile")
    print("6. Follow Another User")
    print("7. Unfollow Another User")
    print("8. Quit")
    print("*************************************************")

def main():
    app = FriendNet()

    alice = app.add_new_profile("Alice", "P", "A cheerful girl who loves photography.")
    ben = app.add_new_profile("Ben", "U", "An outgoing traveler and food lover.")
    claire = app.add_new_profile("Claire", "U", "Enjoys sharing lifestyle tips online.")
    david = app.add_new_profile("David", "U", "A gamer who streams casually.")
    emma = app.add_new_profile("Emma", "P", "An artist who posts her sketches.")

    app.add_follow(alice, ben)
    app.add_follow(alice, claire)
    app.add_follow(alice, emma)

    app.add_follow(ben, alice)
    app.add_follow(ben, claire)

    app.add_follow(emma, alice)
    app.add_follow(emma, david)


    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print("======================================")
            print("View All Profile Names: ")
            print("======================================")
            app.display_all_profiles()
            print("--------------------------------------------------------")
            input()

        elif choice == "2":
            try:
                print("======================================")
                print("View Details for Any Profile: ")
                print("======================================")
                app.display_all_profiles()
                index = int(input("Select whose profile to view: "))
                app.display_profile(index)
                print("--------------------------------------------------------")
                input()
            except (ValueError, IndexError):
                print("Invalid!")
                input()

        elif choice == "3":
            print("======================================")
            print("View Followers for Any Profile")
            print("======================================")
            app.display_all_profiles()
            try:
                index = int(input("Select whose profile to view followers: "))
                app.view_followers(index)
                print("--------------------------------------------------------")
            except (ValueError, IndexError):
                print("Invalid input.")
            input()

        elif choice == "4":
            print("======================================")
            print("View Followed Accounts for Any Profile: ")
            print("======================================")
            app.display_all_profiles()
            try:
                index = int(input("Select whose profile to view followings: "))
                app.view_followed(index)
                print("--------------------------------------------------------")
            except (ValueError, IndexError):
                print("Invalid input.")
            input()

        elif choice == "5":
            print("======================================")
            print("Add a new user profile")
            print("======================================")

            while True:
                name = input("Enter your name: ").strip()
                if not name:
                    print("Name cannot be empty.")
                elif any(person.getName().lower() == name.lower() for person in app.my_graph.graph):
                    print("A profile with this name already exists. Please enter a different name.")
                else:
                    break

            while True:
                privacy = input("Enter privacy (U for public, P for private): ").upper()
                if privacy in ["U", "P"]:
                    break
                else:
                    print("Invalid. Please enter again!")

            biography = input("Enter biography: ")
            app.add_new_profile(name, privacy, biography)
            print("Added successfully.")
            input()

        elif choice == "6":
            print("======================================")
            print("Follow Another User")
            print("======================================")
            app.display_all_profiles()
            try:
                follower_index = int(input("Enter follower profile number: "))
                followed_index = int(input("Enter user profile number to follow: "))
                follower = list(app.my_graph.graph)[follower_index - 1]
                followed = list(app.my_graph.graph)[followed_index - 1]

                if follower == followed:
                    print("You cannot follow your own account.")
                elif followed in app.my_graph.graph[follower]:
                    print(f"{follower.getName()} is already following {followed.getName()}.")
                else:
                    app.add_follow(follower, followed)
                    print(f"{follower.getName()} now follows {followed.getName()}.")
            except (ValueError, IndexError):
                print("Invalid selection.")
            input()

        elif choice == "7":
            print("======================================")
            print("Unfollow Another User")
            print("======================================")
            app.display_all_profiles()
            try:
                follower_index = int(input("Enter follower profile number: "))
                followed_index = int(input("Enter user profile number to unfollow: "))
                follower = list(app.my_graph.graph)[follower_index - 1]
                followed = list(app.my_graph.graph)[followed_index - 1]

                if follower == followed:
                    print("You cannot unfollow your own account.")
                elif followed in app.my_graph.graph[follower]:
                    app.unfollow_user(follower, followed)
                    print(f"{follower.getName()} has unfollowed {followed.getName()}.")
                else:
                    print(f"{follower.getName()} is not following {followed.getName()}.")
            except (ValueError, IndexError):
                print("Invalid selection.")
            input()

        elif choice == "8":
            print("Quit Successful!")
            break

        else:
            print("Invalid choice. Please choice again!")
            input()


if __name__ == "__main__":
    main()
