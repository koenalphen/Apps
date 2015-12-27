from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from roomcontrol.models import Device, State


@csrf_protect
def main(request):
    devices = Device.objects.all()
    context = {
        'devices': devices
    }
    return render(request, 'roomcontrol/main.html', context)

@csrf_protect
def submit(request):
    device_id = request.GET["device_id"]
    state = request.GET["state"]
    device = get_object_or_404(Device, pk=device_id)
    if device.check_state(state):
        state_to_add = State(device=device, state=state)
        state_to_add.save()
        return HttpResponse("Succes! Current state is now " + str(device.get_current_state()))
    else:
        return HttpResponse("State zit niet in de mogelijke states")

@csrf_protect
def retrieve(request):
    device_id = request.GET["device_id"]
    device = get_object_or_404(Device, pk=device_id)
    state = device.get_current_state()
    return HttpResponse(state)
