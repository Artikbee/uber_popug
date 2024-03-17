from django.db.models.signals import post_save
from django.dispatch import receiver
from models import CustomUser
from producer import publish
from typing import NoReturn


# from popug_schema_registry.v1.user_create_dto import UserCreateDTO


@receiver(post_save, sender=CustomUser)
def create_message_to_rabbitmq(sender, instance, created, **kwargs) -> NoReturn:
    datadto = {
        'public_id': instance.public_id,
        'name': instance.name,
        'role': instance.role,
        'email': instance.email

    }

    # datadto = UserCreateDTO(
    #     public_id=instance.public_id,
    #     name=instance.name,
    #     role=instance.role,
    #     email=instance.email
    # )

    publish('user.created', datadto)
