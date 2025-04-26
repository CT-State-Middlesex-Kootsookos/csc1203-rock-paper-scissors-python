from database_interface import database_interface

class result_tracker():

    def __init__(self):
        self.db = database_interface()
        self.results = self.get_result()

    def store_result(self, initials, result):
        if (initials not in self.results):
            self.results[initials] = {}
        if (result in self.results[initials]):
            self.results[initials][result] = self.results[initials][result] + 1
        else:
            self.results[initials][result] = 1

        self.db.store(self.results)

    def get_result(self):
        return self.db.read()
        
    def print_previous_results(self, player_initial):
        previous_results = self.get_result()
        for player_initial in previous_results:
            print(player_initial)
            for result in previous_results[player_initial]:
                print(result + " : " + str(previous_results[player_initial][result]))

