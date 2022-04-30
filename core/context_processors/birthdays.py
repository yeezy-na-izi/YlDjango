from users.models import Profile
from django.utils.timezone import now


def get_users_birthdays(request):
    return {'users_birthdays':
            Profile.objects.filter(birthday=now().date())
            .only('user__first_name', 'user__last_name')
            .order_by('user__first_name', 'user__last_name')
            }
