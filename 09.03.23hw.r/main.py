#1
from myapp.models import MyModel

models = MyModel.objects.all()

for model in models:
    model.title = f"{model.title} ({model.id})"
    model.save()


#11.1
def find_lost_card(N, cards):
    total_sum = (N * (N + 1)) // 2
    remaining_sum = sum(cards)
    lost_card = total_sum - remaining_sum
    return lost_card

N = int(input("Введите число N: "))
cards = list(map(int, input("Введите номера оставшихся карточек: ").split()))
lost_card = find_lost_card(N, cards)
print("Потерянная карточка:", lost_card)


#11.2
def print_squares(N):
    i = 1
    while i*i <= N:
        print(i*i)
        i += 1

N = int(input("Введите целое число N: "))
print("Квадраты натуральных чисел, не превосходящие N:")
print_squares(N)

