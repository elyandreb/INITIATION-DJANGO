from urllib import request
from django.forms import BaseModelForm
from django.shortcuts import redirect, render
from django.http import HttpResponse

from monApp.forms import CategorieForm, ContactUsForm, ProduitForm, RayonForm, StatutForm
from monApp.models import Categorie, Contenir, Produit, Rayon, Statut
from django.views.generic import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models import Count, Prefetch
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator

def accueil(request,param):
    return HttpResponse("<h1>Hello " + param + " ! You're connected</h1>")

def contact(request):
    return render(request, 'monApp/contact.html')

def apropos(request):
    return render(request, 'monApp/about.html')

class ProduitListView(ListView):
    model = Produit
    template_name = "monApp/list_produits.html"
    context_object_name = "prdts"

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Produit.objects.filter(intituleProd__icontains=query).select_related('categorie').select_related('statut')
        return Produit.objects.all().select_related('categorie').select_related('statut')

    def get_context_data(self, **kwargs):
        context = super(ProduitListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes produits"
        return context

class ProduitDetailView(DetailView):
    model = Produit
    template_name = "monApp/detail_produit.html"
    context_object_name = "prdt"
    def get_context_data(self, **kwargs):
        context = super(ProduitDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du produit"
        return context

class CategorieListView(ListView):
    model = Categorie
    template_name = "monApp/list_categorie.html"
    context_object_name = "cats"
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Categorie.objects.filter(nomCat__icontains=query).annotate(produit=Count('produits'))
        return Categorie.objects.annotate(produit=Count('produits'))
    def get_context_data(self, **kwargs):
        context = super(CategorieListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes catégories"
        return context
    
class CategorieDetailView(DetailView):
    model = Categorie
    template_name = "monApp/detail_categorie.html"
    context_object_name = "cat"
    def get_queryset(self):
        return Categorie.objects.annotate(produit=Count('produits'))
    def get_context_data(self, **kwargs):
        context = super(CategorieDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail de la catégorie"
        context['prdts'] = self.object.produits.all()
        return context

class StatutListView(ListView):
    model = Statut
    template_name = "monApp/list_statuts.html"
    context_object_name = "stats"
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Statut.objects.filter(libelle__icontains=query).annotate(prt=Count('produit'))
        return Statut.objects.annotate(prt=Count('produit'))
    def get_context_data(self, **kwargs):
        context = super(StatutListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes statuts"
        return context
    
class StatutDetailView(DetailView):
    model = Statut
    template_name = "monApp/detail_statut.html"
    context_object_name = "stat"
    def get_queryset(self ) :
        return Statut.objects.annotate(prt=Count('produit'))
    def get_context_data(self, **kwargs):
        context = super(StatutDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du statut"
        context['prdts'] = self.object.produit.all()
        return context

class RayonListView(ListView):
    model = Rayon
    template_name = "monApp/list_rayon.html"
    context_object_name = "rays"
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Rayon.objects.filter(nomRay__icontains=query).prefetch_related(
                Prefetch('contenir_rayon', queryset=Contenir.objects.select_related('produit'))
            )
        return Rayon.objects.all().prefetch_related(
            Prefetch('contenir_rayon', queryset=Contenir.objects.select_related('produit'))
        )
    def get_context_data(self, **kwargs):
        context = super(RayonListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes rayons"
        ryns_dt = []
        for rayon in context['rays']:
            total = 0
            for contenir in rayon.contenir_rayon.all():
                total += contenir.produit.prixUnitaireProd * contenir.quantite
            ryns_dt.append({'rayon': rayon,'total_stock': total})
            print (ryns_dt)
        context['ryns_dt'] = ryns_dt
        return context
    
class RayonDetailView(DetailView):
    model = Rayon
    template_name = "monApp/detail_rayon.html"
    context_object_name = "ray"
    def get_context_data(self, **kwargs):
        context = super(RayonDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du rayon"
        prdts_dt = []
        total_rayon = 0
        total_nb_produit = 0
        for contenir in self.object.contenir_rayon.all():
            total_produit = contenir.produit.prixUnitaireProd * contenir.quantite
            prdts_dt.append({ 'produit': contenir.produit,
                'quantite': contenir.quantite,
                'prix_unitaire': contenir.produit.prixUnitaireProd,
                'total_produit': total_produit} )
            total_rayon += total_produit
            total_nb_produit += contenir.quantite
        context['prdts_dt'] = prdts_dt
        context['total_rayon'] = total_rayon
        context['total_nb_produit'] = total_nb_produit
        return context

class HomeView(TemplateView):
    template_name = "monApp/page_home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['titreh1'] = "Hello Django " + self.kwargs.get('param', '')
        return context
    
    def post(self, request, **kwargs):
        return render(request, self.template_name)
    

class AboutView(TemplateView):
    template_name = "monApp/page_home.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['titreh1'] = "About us"
        return context
    
    def post(self, request, **kwargs):
        return render(request, self.template_name)
    
def ContactView(request):
    titreh1 = "Contact us !"
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MonProjet Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@monprojet.com'],
            )
            return redirect('email_sent')
    else:
        form = ContactUsForm()
    return render(request, "monApp/page_home.html", {'titreh1': titreh1, 'form': form})

class ConnectView(LoginView):
    template_name = 'monApp/page_login.html'
    def post(self, request, **kwargs):
        lgn = request.POST.get('username', False)
        pswrd = request.POST.get('password', False)
        user = authenticate(username=lgn, password=pswrd)
        if user is not None and user.is_active:
            login(request, user)
            return render(request, 'monApp/page_home.html', {'param': lgn, 'message': "You're connected"})
        else:
            return render(request, 'monApp/page_register.html')
        
class RegisterView(TemplateView):
    template_name = 'monApp/page_register.html'
    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        mail = request.POST.get('mail', False)
        password = request.POST.get('password', False)
        user = User.objects.create_user(username, mail, password)
        user.save()
        if user is not None and user.is_active:
            return render(request, 'monApp/page_login.html')
        else:
            return render(request, 'monApp/page_register.html')
        
class DisconnectView(TemplateView):
    template_name = 'monApp/page_logout.html'
    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)
    
class sentEmailView(TemplateView):
    template_name = 'monApp/email_sent.html'
    def get_context_data(self, **kwargs):
        context = super(sentEmailView, self).get_context_data(**kwargs)
        context['titre1'] = "Email envoyé"
        return context

@method_decorator(login_required, name='dispatch')
class ProduitCreateView(CreateView):
    model = Produit
    form_class=ProduitForm
    template_name = "monApp/create_produit.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        prdt = form.save()
        return redirect('dtl_prdt', prdt.refProd)

@login_required
def ProduitUpdate(request, pk):
    prdt = Produit.objects.get(refProd=pk)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=prdt)
        if form.is_valid():
            # mettre à jour le produit existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du produit que nous venons de mettre à jour
            return redirect('dtl_prdt', prdt.refProd)
    else:
        form = ProduitForm(instance=prdt)
    return render(request, 'monApp/update_produit.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class ProduitDeleteView(DeleteView):
    model = Produit
    template_name = "monApp/delete_produit.html"
    success_url = "/monApp/produits/"
    context_object_name = "prdt"
    def get_context_data(self, **kwargs):
        context = super(ProduitDeleteView, self).get_context_data(**kwargs)
        context['titre1'] = "Suppression du produit"
        return context

@method_decorator(login_required, name='dispatch')
class CategorieCreateView(CreateView):
    model = Categorie
    form_class=CategorieForm
    template_name = "monApp/create_categorie.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        cat = form.save()
        return redirect('dtl_cat', cat.idCat)

@login_required
def CategorieUpdate(request, pk):
    cat = Categorie.objects.get(idCat=pk)
    if request.method == 'POST':
        form = CategorieForm(request.POST, instance=cat)
        if form.is_valid():
            # mettre à jour le produit existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du produit que nous venons de mettre à jour
            return redirect('dtl_cat', cat.idCat)
    else:
        form = CategorieForm(instance=cat)
    return render(request, 'monApp/update_categorie.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class CategorieDeleteView(DeleteView):
    model = Categorie
    template_name = "monApp/delete_categorie.html"
    success_url = "/monApp/categories/"
    context_object_name = "cat"
    def get_context_data(self, **kwargs):
        context = super(CategorieDeleteView, self).get_context_data(**kwargs)
        context['titre1'] = "Suppression de la catégorie"
        return context
    

@method_decorator(login_required, name='dispatch')
class StatutCreateView(CreateView):
    model = Statut
    form_class=StatutForm
    template_name = "monApp/create_statut.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        stat = form.save()
        return redirect('dtl_statut', stat.idStatut)

@method_decorator(login_required, name='dispatch')
class StatutUpdate(UpdateView):
    model = Statut
    form_class=StatutForm
    template_name = "monApp/update_statut.html"
    context_object_name = "stat"
    def get_context_data(self, **kwargs):
        context = super(StatutUpdate, self).get_context_data(**kwargs)
        context['titre1'] = "Modification du statut"
        return context
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        stat = form.save()
        return redirect('dtl_statut', stat.idStatut)

@method_decorator(login_required, name='dispatch')
class StatutDeleteView(DeleteView):
    model = Statut
    template_name = "monApp/delete_statut.html"
    success_url = "/monApp/statuts/"
    context_object_name = "stat"
    def get_context_data(self, **kwargs):
        context = super(StatutDeleteView, self).get_context_data(**kwargs)
        context['titre1'] = "Suppression du statut"
        return context

@method_decorator(login_required, name='dispatch')
class RayonCreateView(CreateView):
    model = Rayon
    form_class=RayonForm
    template_name = "monApp/create_rayon.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        ray = form.save()
        return redirect('dtl_ray', ray.idRay)

@method_decorator(login_required, name='dispatch')
class RayonUpdate(UpdateView):
    model = Rayon
    form_class=RayonForm
    template_name = "monApp/update_rayon.html"
    context_object_name = "ray"
    def get_context_data(self, **kwargs):
        context = super(RayonUpdate, self).get_context_data(**kwargs)
        context['titre1'] = "Modification du rayon"
        return context
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        ray = form.save()
        return redirect('dtl_ray', ray.idRay)

@method_decorator(login_required, name='dispatch')
class RayonDeleteView(DeleteView):
    model = Rayon
    template_name = "monApp/delete_rayon.html"
    success_url = "/monApp/rayons/"
    context_object_name = "ray"
    def get_context_data(self, **kwargs):
        context = super(RayonDeleteView, self).get_context_data(**kwargs)
        context['titre1'] = "Suppression du rayon"
        return context