 
from django import template
from django.contrib.auth.models import Group 


def has_group(request , group_name):
    group = Group.objects.filter(name=group_name)
    if group:
        group = group.first()
        return group in request.user.groups.all()
    else:
        return False   
  
def get_user_id(request ):

        return request.user.id    