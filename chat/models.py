from django.db import models


# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=150)
    room = models.ForeignKey('Room', on_delete=models.CASCADE,related_name='players', null=True)
    
    def __str__(self):
        return self.name
    
class Room(models.Model):
    room_code = models.CharField(max_length=6, null=True)
    is_active = models.BooleanField(default=False)
    
    max_players = models.PositiveIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    
    connected_players = models.ManyToManyField(Player, related_name='connected_players', blank=True)
    
    def __str__(self):
        return self.room_code