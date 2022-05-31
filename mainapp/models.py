from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    deleted = models.BooleanField(default=False, verbose_name='Deleted')

    class Meta:
        abstract = True
        ordering = ['-created_at']

    def delete(self, *args, **kwargs):
        self.deleted = False
        self.save()


class News(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Title')
    preview = models.CharField(max_length=255, verbose_name='Preview')
    body = models.TextField(verbose_name='body')
    body_as_markdown = models.BooleanField(default=False)

    def __str__(self):
        return f'#{self.pk} {self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Courses(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Name')
    cost = models.DecimalField(verbose_name='Cost', max_digits=8, decimal_places=2, default=0)
    image = models.ImageField(verbose_name='Image')
    availability_course = models.BooleanField(default=True)
    description = models.CharField(max_length=255, verbose_name='Description')
    description_as_markdown = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.pk} {self.name}'


class Lesson(BaseModel):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    num = models.PositiveIntegerField(verbose_name="Lesson number")
    title = models.CharField(max_length=256, verbose_name="Name")
    description = models.TextField(
        verbose_name="Description", blank=True, null=True
    )
    description_as_markdown = models.BooleanField(
        verbose_name="As markdown", default=False
    )

    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.course.name} | {self.num} | {self.title}"

    def delete(self, *args):
        self.deleted = True
        self.save()

    class Meta:
        ordering = ("course", "num")


class CourseTeachers(models.Model):
    course = models.ManyToManyField(Courses)
    name_first = models.CharField(max_length=128, verbose_name="Name")
    name_second = models.CharField(max_length=128, verbose_name="Surname")
    day_birth = models.DateField(verbose_name="Birth date")
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:

        return "{0:0>3} {1} {2}".format(
            self.pk, self.name_second, self.name_first
        )

    def delete(self, *args):

        self.deleted = True
        self.save()
