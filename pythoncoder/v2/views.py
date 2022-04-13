from telnetlib import PRAGMA_HEARTBEAT
from django.views.generic import TemplateView
from django.shortcuts import render
from pythoncoder.students.models import Curso
from .forms import CursoForms 

class FormularioView(TemplateView):
    template_name="forms/index.html"
    def get(self,request):
        context={
            "form":CursoForms()
        }                                    #metodo get xq enviar esta estructura pero tambeins e cargara a nibvel html
        return render(request,self.template_name,context)
    def post(self,request):
        #name=request.POST["name"]
        #camada=request.POST["camada"]

        #print(f"CURSO:{name}")
        #print(f"CAMADA:{camada}")

        
        #obj_curso=Curso(name=name,camada=camada)
        #obj_curso.save()

        response=CursoForms(request.POST)     #Enviarle un dict basicamente , validacion 

        if response.is_valid:
          print(response)
          obj_response=response.cleaned_data  #retorna la info en otro formato luego de la validacion

          name=request.POST["name"]
          camada=request.POST["camada"]
          print(f"CURSO:{name}")
          print(f"CAMADA:{camada}")
 
        
        

          obj_response=response.cleaned_data       #es un validor 
          obj_curso=Curso(name=obj_response.get("name"),
                        camada=obj_response.get("camada"))
          obj_curso.save()
        
        context={
            "form":CursoForms()


        }          


        return render(request,self.template_name,context)

class  SearchView(TemplateView):
    template_name="forms/search.html"

    def post(self,request):
        print("CAMADA")
        print(request.POST.get("camada"))
        context={ 
            "elements":Curso.objects.filter(    #campo filtrar genera elem,ento arreglo en elements
                camada__icontains=request.POST.get("camada")   #alamacena informacion
            )
        }
        return render(request,self.template_name,context)  # rendizar y hacer for en esos elementos 

    
