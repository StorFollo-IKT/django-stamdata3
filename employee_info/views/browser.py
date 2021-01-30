from django.contrib.auth.decorators import permission_required
from django.http import Http404
from django.shortcuts import render, redirect

from employee_info.models import Resource, Company, Organisation, CostCenter

title = 'Vis informasjon om ansatte'


def index(request):
    return render(request, 'employee_info/index.html', {'companies': Company.objects.all(),
                                                        'title': title})


@permission_required('employee_info.view_employment')
def resource(request):
    employee_num = request.GET.get('employee')
    if not employee_num:
        employee_num = request.GET.get('value')

    company = request.GET.get('company')
    resource_id = request.GET.get('id')

    if resource_id:
        try:
            resource_obj = Resource.objects.get(id=resource_id)
        except Resource.DoesNotExist:
            raise Http404('Ugyldig id')

    elif employee_num and company:
        try:
            resource_obj = Resource.objects.get(company__companyCode=company,
                                                resourceId=employee_num)
        except Resource.DoesNotExist:
            return render(request, 'employee_info/index.html',
                          {'companies': Company.objects.all(),
                           'error_resource':
                               'Ingen ansatt i %s med ressursnummer %s' %
                               (company, employee_num)})
    else:
        return redirect('employee_info_browser:index')

    return render(request, 'employee_info/resource.html',
                  {'resource': resource_obj,
                   'title': 'Ansatt',
                   'companies': Company.objects.all()})


@permission_required('employee_info.view_organisation')
def organisation(request):
    company = request.GET.get('company')
    organisation_num = request.GET.get('value')
    if not company:
        return render(request, 'employee_info/select_company.html', {'title': 'Velg firma',
                                                                     'companies': Company.objects.all()
                                                                     })
    elif not organisation_num:
        organisation_obj = Organisation.objects.filter(company__companyCode=company)
        organisation_obj = organisation_obj.select_related('manager', 'parent')

        return render(request, 'employee_info/select_organisation.html',
                      {'title': 'Velg organisasjonsenhet',
                       'organisations': organisation_obj,
                       'company': company})
    try:
        organisation_obj = Organisation.objects.select_related('manager', 'parent'). \
            prefetch_related('employments__resource'). \
            get(company__companyCode=company, orgId=organisation_num)

        return render(request, 'employee_info/organisation.html',
                      {'organisation': organisation_obj, 'company': company})
    except Organisation.DoesNotExist:
        return render(request, 'employee_info/index.html',
                      {'title': title,
                       'companies': Company.objects.all(),
                       'error_org':
                           'Ingen organisasjonsenhet i %s med nummer %s' %
                           (company, organisation_num)})
