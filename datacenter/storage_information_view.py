from django.utils.timezone import localtime
from datacenter.models import Visit, get_duration, format_duration, is_visit_long
from django.shortcuts import render


def storage_information_view(request):

    all_visiters_inside = Visit.objects.filter(leaved_at=None)

    non_closed_visits = []
    for visiter in all_visiters_inside:
        who_entered = visiter.passcard.owner_name
        entered_at = localtime(visiter.entered_at)
        duration = get_duration(visiter)
        formated_duration = format_duration(duration)
        is_strange = is_visit_long(duration)
        non_closed_visits.append(
            {
                'who_entered': who_entered,
                'entered_at': entered_at,
                'duration': formated_duration,
                'is_strange': is_strange,
            }
        )

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
