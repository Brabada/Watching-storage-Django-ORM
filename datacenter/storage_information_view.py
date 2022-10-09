from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from datetime import timedelta

def format_duration(duration):
    time = timedelta(seconds=duration)
    return time


def storage_information_view(request):
    # Программируем здесь

    visits = Visit.objects.filter(leaved_at=None)

    non_closed_visits = []
    for visit in visits:
        duration = visit.get_duration()
        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': visit.entered_at,
                'duration': format_duration(duration),
            }
        )

    # non_closed_visits = [
    #     {
    #         'who_entered': 'Richard Shaw',
    #         'entered_at': '11-04-2022 25:34',
    #         'duration': f'{format_duration(7599)}',
    #     },
    #     {'who_entered': 'Richard Shaw',
    #         'entered_at': '11-04-2022 25:34',
    #         'duration': f'{format_duration(7599)}',}
    # ]
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
