from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q #what is?
from .forms import ChemicalForm, SpecificationForm, UserForm, ProjectForm, AttributeForm
from .models import Chemical, Specification
from .models import Project
from .models import Formula, Attribute
import simplejson as json
from django.http import HttpResponse
from django.template.context import RequestContext

def home(request):
    return render(request, 'chemical/home.html')

def chemical(request, chemical_id):
    if not request.user.is_authenticated():
        return render(request, 'chemical/login.html')
    else:
        chemical_name = get_object_or_404(Chemical, id = chemical_id)
        chemical = Chemical.objects.filter(id = chemical_id)
        specifications = Specification.objects.filter(chemical = chemical_id)
        form = SpecificationForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            specification = form.save(commit=False)
            specification.chemical = chemical_name
            specification.save()
        form = SpecificationForm() 
        context = {
            "form": form,
            'specifications': specifications,
            "chemical": chemical,
            'chemical_name': chemical_name
        }
    return render(request, 'chemical/chemical.html', context)

    
def tutorials(request):
    return render(request, 'chemical/tutorials.html')
    
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'chemical/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                all_project = Project.objects.filter(user=request.user)
                return render(request, 'chemical/home.html', {'all_project': all_project})
            else:
                return render(request, 'chemical/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'chemical/login.html', {'error_message': 'Invalid login'})
    return render(request, 'chemical/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                chemical = Chemical.objects.filter(user=request.user)
                return render(request, 'chemical/home.html', {'chemical': chemical})
    context = {
        "form": form,
    }
    return render(request, 'chemical/register.html', context)

def projects(request):
    if not request.user.is_authenticated():
        return render(request, 'chemical/login.html')
    else:
        all_project = Project.objects.all()
       
        form = ProjectForm(request.POST or None, request.FILES or None)
       
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
        form = ProjectForm()
        context = {
            "form": form,
            'all_project': all_project
        }
        return render(request, 'chemical/projects.html', context)
        
def formulas(request, project_id):
    if not request.user.is_authenticated():
        return render(request, 'chemical/login.html')
    else:
        form = FormulaForm(request.POST or None, request.FILES or None)
        project_name = get_object_or_404(Project, id = project_id)
        all_formula = Formula.objects.filter(project = project_id)
        if form.is_valid():
            formula = form.save(commit=False)
            formula.project = project_name
            formula.save()
        form = FormulaForm()
        context = {
            "form": form,
            'all_formula': all_formula
        }
        return render(request, 'chemical/formulas.html', context)
        

        
def chemicals(request):
    if not request.user.is_authenticated():
        return render(request, 'chemical/login.html')
    else:
        all_chemical = Chemical.objects.all()
        context = {
            'all_chemical': all_chemical
        }
        form = ChemicalForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            chemical = form.save(commit=False)
            chemical.save()
        form = ChemicalForm() 
        context = {
            "form": form,
            'all_chemical': all_chemical,
        }
        
        return render(request, 'chemical/chemicals.html', context)
        
def group(request, group_id):
    if not request.user.is_authenticated():
        return render(request, 'chemical/login.html')
    else:
        formula_name = get_object_or_404(Formula, id = formula_id)
       
        total = 0
        
        context = {
            "formula_name": formula_name, 
            'formula_id': formula_id,
            'total': total
        }
        
        return render(request, 'chemical/group.html', context)
        

        
        

 # workbook      
def index(request):
    template = 'chemical/index.html'

    app_action = request.POST.get('app_action')
    posted_data = request.POST.get('json_data')

    if posted_data is not None and app_action == 'save':
        this_sheet = request.POST.get("sheet")
        this_workbook = request.POST.get("workbook_name")
        sheet_id = request.POST.get("sheet_id")

        posted_data = json.dumps(posted_data)

        if(sheet_id):
            wb = Workbook(id=sheet_id, workbook_name=this_workbook, 
                   sheet_name=this_sheet, data=posted_data)
        else:
            wb = Workbook(workbook_name=this_workbook, 
                   sheet_name=this_sheet, data=posted_data)
        wb.save()

    elif app_action == 'get_sheets':
        wb_name = request.POST.get('workbook_name')
        sheets = Workbook.objects.filter(workbook_name=wb_name)

        # use list comprehension to create python list which is like a JSON object
        sheets = [{ "sheet_id":i.id, "workbook_name": i.workbook_name.encode("utf-8"),
                    "sheet_name": i.sheet_name.encode("utf-8"), 
                    "data": json.loads(i.data.encode("utf-8"))} for i in sheets ]

        # dumps -> serialize to JSON
        sheets = json.dumps(sheets)

        return HttpResponse( sheets, mimetype='application/javascript' )

    elif app_action == 'list':
        workbooks = Workbook.objects.values('workbook_name').distinct()

        # use list comprehension to make a list of just the work books names
        workbooks = [ i['workbook_name'] for i in workbooks ]

        # encode into json format before sending to page
        workbooks = json.dumps(workbooks)

        # We need to return an HttpResponse object in order to complete
        # the ajax call
        return HttpResponse( workbooks, mimetype='application/javascript' )

    return render(request, template, {})