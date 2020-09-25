from django.contrib import admin

from employee_info.models import Company, CostCenter, Employment, Organisation, Resource


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['companyCode']


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['company', 'resourceId', 'firstName', 'lastName']
    list_filter = ['company']
    readonly_fields = ['manages_list', 'subordinates']


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ['company', 'orgId', 'name', 'manager']
    list_filter = ['company']
    # readonly_fields = ['employments']


@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin):
    list_display = ['resource', 'mainPosition', 'workPlace', 'costCenter']


@admin.register(CostCenter)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['description', 'value', 'company']
    list_filter = ['company']
