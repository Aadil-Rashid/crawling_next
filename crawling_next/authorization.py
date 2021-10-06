from users.models import UserModel
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


content_type = ContentType.objects.get_for_model(UserModel)
superAdmin_permissions = Permission.objects.get_or_create(
    codename="super_Admin_permission",
    name="super Admin can access this",
    content_type=content_type,
)

nonAdmin_permissions = Permission.objects.get_or_create(
    codename="non_Admin_permission",
    name="Non Admin users can access this",
    content_type=content_type,
)


