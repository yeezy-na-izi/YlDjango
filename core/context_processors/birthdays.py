from users.models import Profile
from django.utils.timezone import now


def get_users_birthdays(request):
    return {
        'users_birthdays':
            Profile.objects.filter(
                birthday__month=now().month,
                birthday__day=now().day
            ).only('user__first_name', 'user__last_name').order_by('user__first_name', 'user__last_name')
    }
