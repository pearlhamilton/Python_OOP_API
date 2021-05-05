import requests
from .repo import Repo


class CLI(): 
    def __init__(self):
        self._user_input=""



    def get_user_input(self):
        self._user_input = input("What is your github username?")
        self.get_github_data()


    
    def get_github_data(self):
        req=requests.get(f'https://api.github.com/users/{self._user_input}/repos')
        for data in req.json():
            Repo(data)
        self.print_repos()


    def print_repos(self):
        for idx, repo in  enumerate (Repo.all_repos, start=1):
            print(idx, repo.name)
        self.get_user_choice()


    def get_user_choice(self):
        try:
            self._user_input = input(f'''\nWhich repo would you like see more info for?\n''')
            if self._user_input == 'exit':
                return self.goodbye()
            if not self.valid_input(self._user_input):
                raise ValueError
            self.show_repo()
            self.get_user_choice()
        except ValueError:
            print(f'Sorry,that is not a valid input.\n')
            self.print_repos()


    def show_repo(self):
        repo = Repo.find_by_input(self._user_input)
        print(repo)





    @staticmethod
    def valid_input(i):
        return int(i) > 0 and int(i) <= len(Repo.all_repos)

        

    @staticmethod
    def goodbye():
        print(f'\nSee ya!.\n')
                







