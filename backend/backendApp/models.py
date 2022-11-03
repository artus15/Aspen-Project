from django.db import models

class PlayerClass(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    wins = models.IntegerField()
    
    def getName(self):
        return self.name
    
    def getWins(self):
        return self.wins