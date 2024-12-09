from django.db import models

# Create your models here.
class FeedBack(models.Model):
    army_number = models.CharField(max_length=100, default="Army number")
    rank = models.CharField(max_length=100, default="Rfn")
    name = models.CharField(max_length=100)
    feedback = models.TextField()
    course = models.CharField(max_length=100, default="python")
    unitName = models.CharField(max_length=100, default="Unit Name")
    question1 = models.CharField(max_length=20, default="Python")
    question2 = models.CharField(max_length=20, default="Python")
    question3 = models.CharField(max_length=20, default="Python")
    question4 = models.CharField(max_length=20, default="Python")
    question5 = models.CharField(max_length=20, default="Python")
    question6 = models.CharField(max_length=20, default="Python")
    question7 = models.CharField(max_length=20, default="Python")
    question8 = models.CharField(max_length=20, default="Python")


    def __str__(self):
        return f"{self.army_number} - {self.rank} - {self.name} - {self.course} | ADM Side Improvement: {self.question1} | Instructor Rating: {self.question2} | Time Duration: {self.question3} | Tech Eqpt: {self.question4} | Course Syllabus: {self.question5} | Overall Experience: {self.question6} | Extra classes: {self.question7} | ufficient Time: {self.question8}"
