from django.shortcuts import render
from django.views.generic.base import View


def index(request):
    return render(request, 'index.html')


class OrdersView(View):
    def get(selfself, request):
        data = {
            'orders':
                [
                    {'title': 'Первый заказ', 'id': '1'},
                    {'title': 'Второй заказ', 'id': '2'},
                    {'title': 'Третий заказ', 'id': '3'},
                ]
        }
        return render(request, 'orders.html', data)


class OrderView(View):
    def get(self, request, id):
        data = {
            'order': {
                'id': id
            },
            'order_dict':
                [
                    {'id': '1', 'item1': 'Молоко', 'item2': 'Хлеб', 'item3': 'Кетчуп', 'item4': 'Мясо'},
                    {'id': '2', 'item1': 'Стрепсилс', 'item2': 'Глицин', 'item3': 'C5H5OH', 'item4': 'Пластырь'},
                    {'id': '3', 'item1': 'Трансформер', 'item2': 'Лего', 'item3': 'Световой меч', 'item4': 'Пластилин'},
                ]
        }

        return render(request, 'order.html', data)
