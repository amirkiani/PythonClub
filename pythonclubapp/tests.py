from django.test import TestCase
from .models import Product, ProductType, Review
from .views import index, gettypes, getproducts
from django.urls import reverse
from django.contrib.auth.models import User

class ProductTypeTest(TestCase):
   def test_string(self):
       type=ProductType(typename="Tablet")
       self.assertEqual(str(type), type.typename)

   def test_table(self):
       self.assertEqual(str(ProductType._meta.db_table), 'producttype')

class ProductTest(TestCase):
   #set up one time sample data
   def setup(self):
       type = ProductType(typename='laptop')
       product=Product(productname='Lenovo', producttype=type, productprice='500.00')
       return product
   def test_string(self):
       prod = self.setup()
       self.assertEqual(str(prod), prod.productname)
  
   #test the discount property
   def test_discount(self):
       prod=self.setup()
       self.assertEqual(prod.memberdiscount(), 25.00)

   def test_type(self):
       prod=self.setup()
       self.assertEqual(str(prod.producttype), 'laptop')

   def test_table(self):
       self.assertEqual(str(Product._meta.db_table), 'product')

class ReviewTest(TestCase):
   def test_string(self):
       rev=Review(reviewtitle="Best Review")
       self.assertEqual(str(rev), rev.reviewtitle)

   def test_table(self):
       self.assertEqual(str(Review._meta.db_table), 'review')

class IndexTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 200)
  
class GetProductsTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('products'))
       self.assertEqual(response.status_code, 200)

def setUp(self):
        self.u=User.objects.create(username='myuser')
        self.type=ProductType.objects.create(typename='laptop')
        self.prod = Product.objects.create(productname='product1', producttype=self.type, user=self.u, productprice=500, productentrydate='2019-04-02', productdescription="a product")
        self.rev1=Review.objects.create(reviewtitle='prodreview', reviewdate='2019-04-03', product=self.prod, reviewrating=4, reviewtext='some review')
        self.rev1.user.add(self.u)
        self.rev2=Review.objects.create(reviewtitle='prodreview', reviewdate='2019-04-03', product=self.prod,  reviewrating=4, reviewtext='some review')
        self.rev2.user.add(self.u)

def test_product_detail_success(self):
        response = self.client.get(reverse('productdetails', args=(self.prod.id,)))
        # Assert that self.post is actually returned by the post_detail view
        self.assertEqual(response.status_code, 200)

def test_discount(self):
        discount=self.prod.memberdiscount()
        self.assertEqual(discount, 25.00)

def test_number_of_reviews(self):
        reviews=Review.objects.filter(product=self.prod).count()
        self.assertEqual(reviews, 2)

#Form tests
class ProductType_Form_Test(TestCase):
    def test_typeform_is_valid(self):
        form=ProductTypeForm(data={'typename': "type1", 'typedescription' : "some type"})
        self.assertTrue(form.is_valid())

def test_typeform_minus_descript(self):
        form=ProductTypeForm(data={'typename': "type1"})
        self.assertTrue(form.is_valid())

def test_typeform_empty(self):
        form=ProductTypeForm(data={'typename': ""})
        self.assertFalse(form.is_valid())