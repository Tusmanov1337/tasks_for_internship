class EvenNumbers:
    def __init__(self, upper_bound=None):
        self.max_it = upper_bound
        self.curr_it = 0
        self.none_returned = False
        self.valid_input = type(upper_bound) == int

    def __iter__(self):
        return self

    def __next__(self):
        if not self.none_returned and not self.valid_input:
            self.none_returned = True
            return None
        elif not self.valid_input:
            raise StopIteration
        else:
            if self.curr_it < self.max_it:
                return_value = 2 * self.curr_it
                self.curr_it += 1
                return return_value
            else:
                raise StopIteration


