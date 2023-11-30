"""
Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.
"""


class InstanceCounter:
    counter = 0

    def __init__(self):
        InstanceCounter.counter += 1
