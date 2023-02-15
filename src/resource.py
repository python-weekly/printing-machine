
class Resource:
    def __init__(self, resource):
        self.resource = resource
        self.resource_qty = {}

    @property
    def report(self):
        return f'Ink: {self.resource["ink"]}\nPaper: {self.resource["paper"]}'

    def is_resource_enough(self, format_item, no_pages):
        self.resource_qty['ink'] = no_pages * format_item.ink
        self.resource_qty['paper'] = no_pages * format_item.paper

        for key, value in self.resource_qty.items():
            if self.resource[key] < value:
                print(f'Sorry there is not enough {key}')
                return False

        return True

    def print_document(self):
      for key, value in self.resource_qty.items():
        self.resource[key] -= value
        
      print()
      print('Here is your work!!!')
      print("Thanks for using our Printer service. Hope you enjoy it!!")
