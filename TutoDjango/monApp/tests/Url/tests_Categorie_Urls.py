from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from monApp.models import Categorie
from monApp.views import CategorieDeleteView, CategorieListView, CategorieDetailView, CategorieCreateView, CategorieUpdate
class CategorieUrlsTest(TestCase):
    def setUp(self):
        self.ctgr = Categorie.objects.create(nomCat="CategoriePourTest")
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
    def test_categorie_detail_response_code(self):
        url = reverse('dtl_cat', args=[self.ctgr.idCat]) #idCat existant
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    def test_categorie_detail_response_code_KO(self):
        url = reverse('dtl_cat', args=[9999]) # idCat non existant
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    def test_categorie_list_url_is_resolved(self):
        url = reverse('lst_cats')
        self.assertEqual(resolve(url).view_name, 'lst_cats')
        self.assertEqual(resolve(url).func.view_class,CategorieListView)
    def test_categorie_detail_url_is_resolved(self):
        url = reverse('dtl_cat', args=[1])
        self.assertEqual(resolve(url).view_name, 'dtl_cat')
        self.assertEqual(resolve(url).func.view_class, CategorieDetailView)
    def test_categorie_create_url_is_resolved(self):
        url = reverse('crt_cat')
        self.assertEqual(resolve(url).view_name, 'crt_cat')
        self.assertEqual(resolve(url).func.view_class, CategorieCreateView)
    def test_categorie_update_url_is_resolved(self):
        url = reverse('cat_chng', args=[1])
        self.assertEqual(resolve(url).view_name, 'cat_chng')
        self.assertEqual(resolve(url).func, CategorieUpdate)
    def test_categorie_delete_url_is_resolved(self):
        url = reverse('cat_del', args=[1])
        self.assertEqual(resolve(url).view_name, 'cat_del')
        self.assertEqual(resolve(url).func.view_class, CategorieDeleteView)
    def test_categorie_list_response_code(self):
        response = self.client.get(reverse('lst_cats'))
        self.assertEqual(response.status_code, 200)
    
    def test_categorie_create_response_code_OK(self):
        response = self.client.get(reverse('crt_cat'))
        self.assertEqual(response.status_code, 200)

    def test_categorie_update_response_code_OK(self):
        url = reverse('cat_chng', args=[self.ctgr.idCat]) # idCat existant
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    def test_categorie_update_response_code_KO(self):
        url = reverse('cat_chng', args=[9999]) # idCat non existant
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    def test_categorie_delete_response_code_OK(self):
        url = reverse('cat_del', args=[self.ctgr.idCat]) # idCat existant
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    def test_categorie_delete_response_code_KO(self):
        url = reverse('cat_del', args=[9999]) # idCat non existant
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_redirect_after_categorie_creation(self):
        response = self.client.post(reverse('crt_cat'), {'nomCat': 'CategoriePourTestRedirectionCreation'} )
        # Statut 302 = redirection
        self.assertEqual(response.status_code, 302)
        # Redirection vers la vue de detail
        self.assertRedirects(response, '/monApp/categories/2/')
        def test_redirect_after_categorie_updating(self):
            response = self.client.post(reverse('cat_chng', args=[self.ctgr.idCat]),
            data={"nomCat": "CategoriePourTestRedirectionMaj"})
            # Statut 302 = redirection
            self.assertEqual(response.status_code, 302)
            # Redirection vers la vue de detail
            self.assertRedirects(response, f'/monApp/categorie/{self.ctgr.idCat}/')
        def test_redirect_after_categorie_deletion(self):
            response = self.client.post(reverse('cat_del', args=[self.ctgr.pk]))
            # Vérifie qu'on a bien une redirection
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, reverse('lst_cats'))
            # Vérifie que la catégorie a bien été supprimée de la base
            self.assertFalse(Categorie.objects.filter(pk=self.ctgr.pk).exists())