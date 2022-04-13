from typing import Any,Dict
from  django.views.generic import TemplateView
from django.shortcuts import render


class StudentView(TemplateView):
    template_name= "student/index.html"

    #def get_context_data(self,**kwargs:Any) -> Dict[str,Any]:
        #return super().get_context_data(**kwargs)
    def get(self,request,status=None):
        print(request.GET.get("edad"))
        context={
            "edad":request.GET.get("edad"),
            "list_test" : [1,2,3,4]
        } 
        return render(request,self.template_name,context)

    #import requests 
    #def post(self,request):
        #pass 