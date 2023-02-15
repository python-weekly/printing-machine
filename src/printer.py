from .resource import Resource
from .format import Format
from .money_machine import MoneyMachine
from data.data import resources


class Printer:
  def __init__(self):
    self.resource = Resource(resources)
    self.format = Format()
    self.money_machine = MoneyMachine(resources['profit'])

  def start(self):
    POWER = True
    print('welcome to automated printer')
    while POWER:
      print_format = input(
        f'\nWhat format would you like {self.format.print_format}? \n').lower()

      if print_format == 'off':
        POWER = False
        print('Thanks for using our service Bye...')
        return

      elif print_format == 'report':
        print()
        print(self.resource.report)
        print(self.money_machine.report)

      else:
        format_item = self.format.find_format(print_format)
        if format_item:
            no_pages = self.no_pages()
            is_resource_enough = self.resource.is_resource_enough(format_item, no_pages)
            if is_resource_enough and self.money_machine.make_transaction(format_item, no_pages):
                self.resource.print_document()

  @staticmethod
  def no_pages():
    while True:
      try:
        return int(input('How many pages?\n'))
      except ValueError:
        print('Please insert a valid number')
