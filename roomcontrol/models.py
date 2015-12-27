from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=12)
    description = models.CharField(max_length=127)
    states = models.CharField(max_length=127)  # string in format like "0 1 2 3 4 5 6 7 8 9"

    # Get the states string from the database and covert to a list of integers
    def get_states(self):
        statestring_list = self.states.split(" ")
        state_list = []
        for item in statestring_list:
            state_list.append(item)
        return state_list

    def get_current_state(self):
        try:
            state_query = State.objects.filter(device=self)
            state_query = state_query.order_by('-time')
            state = state_query[0]
            return state.state
        except:
            return "Error: no states found for device " + self.get_name()

    def get_name(self):
        try:
            name = self.name
            return name
        except:
            pass

    def check_state(self, state):
        state_list = self.get_states()
        if state in state_list:
            return True
        else:
            return False


class State(models.Model):
    device = models.ForeignKey(Device)
    state = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)


