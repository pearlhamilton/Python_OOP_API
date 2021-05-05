class Repo():

    all_repos = []

    def __init__(self, data):
        self._name = data['name']
        self._language = data['language']
        self._forks = data['forks']
        self._owner = data['owner']['login']
        self._save()


    def _save(self):
        self.all_repos.append(self)


    @property 
    def name(self):
        return self._name

    def __str__(self):
        return (f'{self._owner} created {self._name} in {self._language}. It has {self._forks} forks')

  
    @classmethod
    def find_by_input(cls, user_input):
        return cls.all_repos[int(user_input)-1]