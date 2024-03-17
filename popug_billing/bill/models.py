import uuid

from django.db import models


class BillStatus(models.TextChoices):
    ACTIVE = 'active', 'Active'
    CLOSED = 'closed', 'Closed'
    PROCESSED = 'processed', 'Processed'


class TransactionType(models.TextChoices):
    INCOME = 'income', 'Income'
    EXPENSE = 'expense', 'Expense'
    PAYMENT = 'payment', 'Payment'


class CustomUser(models.Model):
    public_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True)

    name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    email = models.EmailField()
    balance = models.IntegerField(default=0)


class Task(models.Model):
    # public_id = models.IntegerField()
    title = models.CharField(max_length=30)
    description = models.TextField()
    cost = models.IntegerField()


class BillingCycle(models.Model):
    public_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(choices=BillStatus, default=BillStatus.ACTIVE, max_length=100)
    started_at = models.TimeField(auto_now=True)
    processed_at = models.TimeField(default=None)
    closed_at = models.TimeField(default=None)


class Transaction(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    billing_cycle_id = models.ForeignKey(BillingCycle, on_delete=models.CASCADE)
    credit = models.IntegerField()
    debit = models.IntegerField()
    type = models.CharField(choices=TransactionType, default=TransactionType.INCOME, max_length=100)
    created_at = models.TimeField(auto_now_add=True)
