from django.db import models

class User(models.Model):
    UserId = models.AutoField(primary_key = True)
    FirstName = models.CharField(max_length = 30)
    LastName = models.CharField(max_length = 30)
    Email = models.CharField(max_length = 30)
    Contact = models.CharField(max_length = 10)
    District = models.CharField(max_length = 30)
    AddressLine1 = models.CharField(max_length = 30)
    AddressLine2 = models.CharField(max_length = 30)
    ZipCode = models.CharField(max_length = 10)
    IsAdmin = models.BooleanField(default = False)
    IsSuperAdmin = models.BooleanField(default = False)
    IsActive = models.BooleanField(default = False)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    Password = models.CharField(max_length=30)

class Roles(models.Model):
    RoleId = models.AutoField(primary_key = True)
    Role = models.CharField(max_length = 200)
    
class Parking(models.Model):
    ParkingId = models.AutoField(primary_key = True)
    Location = models.CharField(max_length = 30)
    Latitude = models.CharField(max_length = 30)
    Longitude = models.CharField(max_length = 30)

class ParkingDetails(models.Model):
    ParkingDetailsId = models.AutoField(primary_key = True)
    VehicleType = models.CharField(max_length = 20)
    PricePerHour = models.CharField(max_length = 20)
    AvailableSpace = models.CharField(max_length = 10)

class Booking(models.Model):
    BookingId = models.AutoField(primary_key = True)
    ParkingFrom = models.DateTimeField(auto_now_add=True)
    ParkingTo = models.DateTimeField(auto_now_add=True)

class VehicleType(models.Model):
    VehicleTypeId = models.AutoField(primary_key = True)
    VehicleName = models.CharField(max_length = 20)

class Payment(models.Model):
    PaymentId = models.AutoField(primary_key = True)
    TotalPrice = models.FloatField(max_length = 50)

class PaymentDetails(models.Model):
    PaymentDetailsId = models.AutoField(primary_key = True)
    TotalPrice = models.FloatField(max_length = 50)