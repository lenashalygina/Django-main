#27
def count_votes(candidates, votes):
    vote_counts = {}
    for candidate in candidates:
        vote_counts[candidate] = 0
    for vote in votes:
        if vote in candidates:
            vote_counts[vote] += 1
    return vote_counts

def find_winner(vote_counts):
    max_votes = max(vote_counts.values())
    winners = [candidate for candidate, votes in vote_counts.items() if votes == max_votes]
    if len(winners) == 1:
        return winners[0]
    else:
        winners.sort(key=lambda x: (len(x), x))
        return winners[0]

candidates = ["Аскаров", "Бекмуханов", "Ернур", "Пешая", "Карим", "Шаримазданов"]

votes = []
print("Кандидаты в выборы:", candidates)
while True:
    vote = input("Вы отдаете голос за (или 'конец' для завершения голосования): ")
    if vote == "конец":
        break
    votes.append(vote)

vote_counts = count_votes(candidates, votes)

winner = find_winner(vote_counts)

print("Победитель выборов:", winner)
print("Количество голосов победителя:", vote_counts[winner])


#29
class MainClass:
    def __init__(self, text):
        self.text = text

    def set_text(self, text=None):
        if text:
            self.text = text
        else:
            self.text = ""

class ChildClass(MainClass):
    def __init__(self, text, number):
        super().__init__(text)
        self.number = number

main_obj = MainClass("Hello")
print(main_obj.text)  # Вывод: Hello

main_obj.set_text("New text")
print(main_obj.text)  # Вывод: New text

child_obj = ChildClass("World", 42)
print(child_obj.text)   # Вывод: World
print(child_obj.number) # Вывод: 42

child_obj.set_text("Updated text")
print(child_obj.text)  # Вывод: Updated text


#30
class MainClass:
    def __init__(self, text):
        self.text = text

    def set_text(self, text=None):
        if text:
            self.text = text
        else:
            self.text = ""

    def print_info(self):
        print("MainClass:")
        print("Text:", self.text)


class ChildClass(MainClass):
    def __init__(self, text, number):
        super().__init__(text)
        self.number = number

    def print_info(self):
        print("ChildClass:")
        print("Text:", self.text)
        print("Number:", self.number)


main_obj = MainClass("Hello")
main_obj.print_info()

child_obj = ChildClass("World", 42)
child_obj.print_info()

objects = [main_obj, child_obj]
for obj in objects:
    obj.print_info()
    print("---------------")


