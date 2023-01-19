from django.contrib import admin
from .models import Member
import uuid

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "phone", "joined_date",)
  uid = uuid.uuid1()
  pos = str(uid).find("-")
  slug_hash = str(uid)[:pos]
  prepopulated_fields = {"slug_hash": (slug_hash,)}
  prepopulated_fields = {"slug": ("firstname", "lastname", "slug_hash")}
  
admin.site.register(Member, MemberAdmin)