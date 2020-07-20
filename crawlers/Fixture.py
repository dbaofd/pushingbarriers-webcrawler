# Game schedule class
class Fixture():
    def __init__(self, rnd, date, time, venue, address, opposition, team, team_id):
        self.rnd = rnd  # round
        self.date = date
        self.time = time
        self.venue = venue
        self.address = address
        self.opposition = opposition
        self.team = team
        self.team_id = team_id

    def get_rnd(self):
        return self.rnd

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time

    def get_venue(self):
        return self.venue

    def get_address(self):
        return self.address

    def get_opposition(self):
        return self.opposition

    def get_team(self):
        return self.team

    def get_team_id(self):
        return self.team_id


def print_fixtures(my_fixtures):
    for index in range(0, len(my_fixtures)):
        print(my_fixtures[index].get_rnd() + "\n" + my_fixtures[index].get_date() + "\n" + my_fixtures[
            index].get_time() + "\n" + my_fixtures[index].get_venue() + "\n" + my_fixtures[index].get_address()
              + '\n' + my_fixtures[index].get_opposition() + "\n" + my_fixtures[index].get_team() + "\n",
              my_fixtures[index].get_team_id())
        print("**************************")
