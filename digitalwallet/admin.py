from django.contrib import admin
from .models import Customer,wallet,Account,Card,Thirdparty,Notification,Receipt,Loan,Reward,Transaction
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name", "last_name","address",)
    searchFields=("fist_name","last_name",)

# class WalletAdmin(admin.ModelAdmin):
#     list_display=("balance", "isactive","customer","pin","currency","date_created",)
#     searchFields=("balance", "isactive","customer","pin","currency","date_created")

# class AccountAdmin(admin.ModelAdmin):
#     list_display=("account_number", "account_name","account_type","balance","wallet",)
#     searchFields=("account_number", "account_name","account_type","balance","wallet")
    
# class TransactionAdmin(admin.ModelAdmin):
#     list_display=("account_number", "account_name","account_type","balance","wallet",)
#     searchFields=("account_number", "account_name","account_type","balance","wallet")
# Register your models.
admin.site.register(Customer,CustomerAdmin)
# admin.site.register(Wallet)
# admin.site.register(Account)
# admin.site.register(Card)
# admin.site.register(Thirdparty)
# admin.site.register(Notification)
# admin.site.register(Receipt)
# admin.site.register(Loan)
# admin.site.register(Reward)
# admin.site.register(Transaction)

