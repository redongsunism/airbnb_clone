from django.db import models
from rooms import models as room_models

class Banner(room_models.AbstractItem):

    """ Banner Object Definition """

    image = models.ImageField("배너 이미지", upload_to="banner_photos", blank=True)
