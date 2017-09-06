from __future__ import unicode_literals

from django.db import models
from ..log_reg.models import User

class CatManager(models.Manager):
    def create_cat(self, postData):
        errors = {}
        if not postData['cat_name'] or not postData['cat_age']:
            errors['error'] = "Fields can not be empty"
        if len(errors):
            return (False, errors)
        else:
            creator = User.objects.get(id = postData['user_id'])
            self.create(name = postData['cat_name'], age = int(postData['cat_age']), creator = creator)
            return (True, "Succes")
    
    def delete_cat(self, cat_id):
        self.get(id = cat_id).delete()

    def edit_cat(self, postData):
        errors = {}
        if not postData['cat_name'] or not postData['cat_age']:
            errors['error'] = "Fields can not be empty"
        if len(errors):
            return (False, errors)
        else:
            cat = self.get(id = postData['cat_id'])
            cat.name = postData['cat_name']
            cat.age = postData['cat_age']
            cat.save()
            return (True, "Succes")


class LikeManager(models.Manager):
    def add_like(self, user_id, cat_id):
        user = User.objects.get(id = user_id)
        cat = Cat.objects.get(id = cat_id)
        self.create(cat = cat, user = user)
        print "============MIAAAAAUUUUUUU==========="
        return True

class Cat(models.Model):
    name = models.CharField(max_length = 255)
    age = models.IntegerField(default = 0)
    creator = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = CatManager()
    def __str__(self):
        return self.name

class Like(models.Model):
    cat = models.ForeignKey(Cat, on_delete = models.CASCADE, related_name = "likes")
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = LikeManager()

# Create your models here.
