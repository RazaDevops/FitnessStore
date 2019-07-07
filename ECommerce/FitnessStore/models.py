from django.db import models

class Person(models.Model):
    pname = models.CharField(max_length = 50)
    plocation = models.CharField(max_length = 50)

    class Meta:
        db_table = "Person"

'''class userLogin(models.Model):
    uname =  models.CharField(max_length = 50)
    upass =  models.CharField(max_length = 50)'''

class custinfo(models.Model):
    cfname = models.CharField(max_length = 50)
    cmail = models.CharField(max_length = 50)
    cpass = models.CharField(max_length = 50)
    ccontact = models.CharField(max_length = 50)

    class Meta:
        db_table = "custinfo"


class strengthprod(models.Model):
    stprodtype = models.CharField(max_length = 50)
    stprodweight = models.CharField(max_length = 50)
    stprodprice = models.FloatField(default=0.0)
    stprodpic = models.ImageField(upload_to = 'static/Images/', default = 'upload pic')
    def __str__(self):
        return self.stprodtype

    class Meta:
        db_table = "strengthprod"

'''class yandmprod(models.Model):
    ynmprodtype = models.CharField(max_length = 50)
    ynmprodwight = models.CharField(max_length = 50)
    ynmprodprice = models.FloatField(default=0.0)
    ynmprodpic = models.ImageField(upload_to = 'static/Images/', default = 'upload pic')
    def __str__(self):
        return self.ynmprodtype

    class Meta:
        db_table = "YandMProd"'''


class Cart(models.Model):    
    prod = models.ForeignKey(strengthprod, on_delete=models.CASCADE)
    user = models.ForeignKey(custinfo, on_delete=models.CASCADE)

    class Meta:
        db_table = "Cart"


