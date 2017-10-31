from django.db import models

DIFFICULTIES = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
)

# Create your models here.
class Bounty(models.Model):
    taskName = models.CharField("Task Name", max_length = 64)
    taskDescription = models.charField("Description: ", max_length = 512)
    taskDifficulty = models.IntegerField("Difficulty", choices=DIFFICULTIES, default='1')

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return '{}-{}'.format(taskName, taskDifficulty)