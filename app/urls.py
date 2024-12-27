from django.urls import path
from .views import home,about,expertise,brand_consulting,personal_brand_consulting,image_consulting,corporate_rebranding,brand_expresso,brand_creation,\
link_fluence,launchpad,works,telugufoods,suryacolors,tdhrishika,tenalidoublehorse,triplex,vsbsurface,zavaine,blog,blogdetails,\
contact,Ourmedia,Questionsform,subscribe,privacy_policy,terms_conditions,cancellation_and_refund_policy,faqs,Newsletter,Brand,Newslettertwo,\
Newsletterthree,BrandRefresh,DigitalTwin_BrandStrategy,Monochromatic_colors_in_branding,band_corner_the_new_age_of_buying_brand_activism,\
brand_naming_unlock_the_soul_of_your_brand,the_power_of_consistency_why_brand_tone_matters,career,apply_form,magsmen_brand_portfolio,\
a_cutting_edge_approach_in_branding,accessyourbrand,submit_form


from django.contrib.sitemaps.views import sitemap
from app.sitemap import PostSitemap,StaticPagesSitemap
from django.views.generic.base import TemplateView
from .views import contact_api_view,get_contacts


sitemaps = {
    'posts': PostSitemap,
    'static_pages': StaticPagesSitemap,
}



urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('expertise/', expertise, name="expertise"),
    path('brand-consulting/', brand_consulting, name="brand-consulting"),
    path('personal-brand-consulting/', personal_brand_consulting, name="personal-brand-consulting"),
    path('image-consulting/', image_consulting, name="image-consulting"),
    path('corporate-rebranding/',corporate_rebranding,name="corporate-rebranding"),
    path('brand-expresso/',brand_expresso,name="brand-expresso"),
    path('brand-creation/',brand_creation,name="brand-creation"),
    path('link-fluence/',link_fluence,name="link-fluence"),
    path('launchpad/',launchpad,name="launchpad"),
    path('works/',works,name="works"),
    path('telugufoods/',telugufoods,name="telugufoods"),
    path('suryacolors/',suryacolors,name="suryacolors"),
    path('tdhrishika/',tdhrishika,name="tdhrishika"),
    path('tenalidoublehorse/',tenalidoublehorse,name="tenalidoublehorse"),
    path('triplex/',triplex,name="triplex"),
    path('vsbsurfaces/',vsbsurface,name="vsbsurfaces"),
    path('zavaine/',zavaine,name="zavaine"),
    path('blog/',blog,name="blog"),
    path('blog-details/<str:slug>',blogdetails,name="blog-details"),
    path('career/',career,name="career"),
    path('contact/',contact,name="contact"),
    path('apply/',apply_form,name="apply"),
    path('gallery/',Ourmedia,name="gallery"),
    path('questions/', Questionsform , name='questions'),
    path('subscribe/',subscribe, name='subscribe'),
    path('privacy-policy/', privacy_policy , name='privacy-policy'),
    path('terms-conditions/', terms_conditions , name='erms-conditions'),
    path('cancellation-refund-policy/', cancellation_and_refund_policy , name='cancellation-refund-policy'),
    path('faqs/', faqs, name='faqs'),
    path('magsmen-brand-portfolio/',magsmen_brand_portfolio,name='magsmen-brand-portfolio'),
    path('news-letter-august-2023/',Newsletter,name='news-letter-august-2023'),
    path('brand-architecture/',Brand,name='brand-architecture'),
    path('brand-corner-october-edition/',Newslettertwo,name='the-name-of-the-article-indian-brand-success-stories'),
    path('brand-corner-november-edition/',Newsletterthree,name='brand-corner-november-edition'), 
    path('brand-refresh-vs-rebranding/',BrandRefresh,name="brand-refresh-rebranding"),
    path('digital-twin-brand-strategy/',DigitalTwin_BrandStrategy,name="digital-twin-brand-strategy"),
    path('monochromatic-colors-in-branding/',Monochromatic_colors_in_branding,name="monochromatic-colors-in-branding"),
    path('the-new-age-of-buying-brand-activism/',band_corner_the_new_age_of_buying_brand_activism,name="the-new-age-of-buying-brand-activism"),
    path('brand-naming-unlock-the-soul-of-your-brand/',brand_naming_unlock_the_soul_of_your_brand,name="brand-naming-unlock-the-soul-of-your-brand"),
    path('the-power-of-consistency-why-brand-tone-matters/',the_power_of_consistency_why_brand_tone_matters,name="the-power-of-consistency-why-brand-tone-matters"),
    path('a-cutting-edge-approach-in-branding/',a_cutting_edge_approach_in_branding,name="a-cutting-edge-approach-in-branding"),
    path('sitemap.xml/',sitemap,{'sitemaps':sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    # path('sitemap.xml/', TemplateView.as_view(template_name='sitemap.xml', content_type='application/xml')),
    path('robots.txt',TemplateView.as_view(template_name="uifiles/robots.txt", content_type="text/plain")),
    path('api/contact/', contact_api_view, name='contact-api'),
    path('api/getcontact/',get_contacts, name='getcontact-api'),
    path('accessyour-brand/',accessyourbrand, name='accessyour-brand'),
    path('submit-form/',submit_form, name='submit-form'),
]