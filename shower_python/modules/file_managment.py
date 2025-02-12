import json
from typing import Tuple
from time import localtime, struct_time, time, ctime


class TimeStoreFile():

    def __init__(self, filepath) -> None:

        self.filepath = filepath
        with open(filepath, "r") as file:
            self.file = dict(json.load(file))

        self.users = [TimeStoreUser(self, name) for name in self.file.keys()]
        self.usernames = list(self.file.keys())

    def get_data(self):
        return self.file

    def __findusr__(self, name):
        for user in self.users:
            if user.name == name:
                return user
                
    def __updata__(self):
        for user, name in zip(self.users, self.usernames):
            self.file[name] = user.get_data()
        with open(self.filepath, "w") as file:
            json.dump(self.file, file)

    def add_user(self, user):
        self.usernames.append(user)
        self.users.append(TimeStoreUser(self, user, True))
        self.__updata__()

    def add_time(self, user):
        usr = self[user]
        if usr != None:
            usr.add_session()
        else:
            raise ValueError(f"User {user} was not found")

    def __getitem__(self, name: str, /):
        return self.__findusr__(name)


class TimeStoreUser():

    def __init__(self, File:TimeStoreFile, Name, New = False) -> None:

        self.file = File
        if not New:
            self.stored_data = File.get_data()[Name]
            if type(self.stored_data) != type([]):
                raise TypeError("Sorry, invalid json file, for each user there should be a list of times")
            self.sessions = [TimeStored(self, time) for time in range(len(self.stored_data))]
        else:
            self.sessions = []

        self.name = Name

    def get_data(self):
        self.update_data()
        return self.stored_data

    def update_data(self):
        self.stored_data = []
        for session in self.sessions:
            if session.end != 0:
                self.stored_data.append([session.start, session.end])

    def add_session(self):
        if not self.sessions or self.sessions[-1].end != 0:
            session = TimeStored(self)
            self.sessions.append(session)
            session.index = len(self.sessions)-1
        else:
            self.sessions[-1].end = time()
        self.file.__updata__()

    def is_showering(self):
        return self.sessions[-1].end == 0

    def __getitem__(self, index: int, /):
        return self.sessions[index]

    def __str__(self) -> str:
        return self.name + ": " + str(self.stored_data)

class TimeStored():

    def __init__(self, User:TimeStoreUser, Index:int = -1) -> None:
        self.data = User
        self.start = time()
        self.end = 0
        self.session = []
        #if the TimeStored came from a file or is it new
        if Index != -1:
            self.index = Index
            self.session = User.stored_data[Index]
            self.end = self.session[1]
            self.start = self.session[0]

    def get_time(self) -> struct_time:
        return localtime(self.start)

    def time_finished(self):
        if self.end == 0:
            self.end = time()
        else:
            raise AttributeError("The finished time is already set")
    def __str__(self) -> str:
        return f"start: {self.start}, end: {self.end}"
