from django.urls import path
from . import views


urlpatterns = [

    # ========================== HOME START ===========================

    path('',views.index,name='index'),

    # =========================== HOME END ============================



    # ========================= COMPANY START =========================

    path('company', views.company, name='company'),

    path('about_us', views.about, name='company.about'),
    path('partners', views.partners, name='company.partners'),
    path('careers', views.careers, name='company.careers'),
    path('events', views.events, name='company.events'),
    path('team', views.team, name='company.team'),

    path('blog', views.blog, name='company.blog'),
    path('blog/slug', views.blog_details, name='company.blog_details'),

    path('contact-us', views.contact_us, name='company.contact_us'),

    # ========================= COMPANY END ============================


    # ========================== PRODUCT START =========================

    path('product/overview', views.product_overview, name='product.overview'),
    path('product/pricing', views.product_pricing, name='product.pricing'),
    path('product/features', views.product_features, name='product.features'),
    path('product/case-studies', views.product_case_studies, name='product.case_studies'),
    path('product/new-releases', views.product_new_releases, name='product.new_releases'),
    path('product/solutions', views.product_solutions, name='product.solutions'),

    # ========================== PRODUCT END ===========================


    # =========================== LEGAL START ==========================

    path('legal/licenses', views.legal_licenses, name='legal.licenses'),
    path('legal/settings', views.legal_settings, name='legal.settings'),
    path('legal/cookies', views.legal_cookies, name='legal.cookies'),
    path('legal/document', views.legal_document, name='legal.document'),
    path('legal/terms', views.legal_terms, name='legal.terms'),
    path('legal/privacy', views.legal_privacy, name='legal.privacy'),

    # =========================== LEGAL END =============================


    # =========================== PORTFOLIO START =======================

    path('portfolio', views.portfolio, name='portfolio'),

    # =========================== PORTFOLIO END =========================


    # =========================== SERVICES START ========================

    path('services', views.services, name='services'),

    # =========================== SERVICES END ==========================


    # =========================== OUR FIELDS START ======================

    path('our-fields', views.our_fields, name='our_fields'),

    # =========================== OUR FIELDS END ========================


    # =========================== OUR FAQ START =========================

    path('faq', views.faq, name='faq'),

    # ============================ OUR FAQ END ==========================


    # =========================== OTHERS START =========================

    path('how-we-do', views.how_we_do, name='how_we_do'),

    # ============================ OTHERS END ==========================

]