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
    path('event/slug', views.view_events, name='company.views_events'),
    
    path('team', views.team, name='company.team'),

    path('blog', views.blog, name='company.blog'),
    path('blog/slug', views.blog_details, name='company.blog_details'),

    path('contact-us', views.contact_us, name='company.contact_us'),
    path('contact-us-post', views.contact_us_post, name='company.contact_us_post'),


    # ========================= COMPANY END ============================


    # ========================== PRODUCT START =========================

    path('product/overview', views.product_overview, name='product.overview'),
    path('product/pricing', views.product_pricing, name='product.pricing'),
    path('product/features', views.product_features, name='product.features'),

    path('product/case-studies', views.product_case_studies, name='product.case_studies'),
    path('product/case-studies/slug', views.view_case_studies, name='product.view_case_studies'),

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


    # =========================== OTHERS START ==========================

    path('how-we-do', views.how_we_do, name='how_we_do'),

    # ============================ OTHERS END ===========================

    path('add-book', views.cbtBookViewSet.as_view({'post': 'addUpdateBookData'})),
    path('update-book/<int:PR_BOOK_ID>', views.cbtBookViewSet.as_view({'post': 'addUpdateBookData'})),
    
    path('import-book-data', views.cbtBookViewSet.as_view({'post': 'importBookData'})),

    path('add-class', views.cbtClassViewSet.as_view({'post': 'addUpdateClassData'})),
    path('update-class/<int:PR_CLASS_ID>', views.cbtClassViewSet.as_view({'post': 'addUpdateClassData'})),

    path('add-board', views.cbtBoardViewSet.as_view({'post': 'addUpdateBoardData'})),
    path('update-board/<int:PR_BOARD_ID>', views.cbtBoardViewSet.as_view({'post': 'addUpdateBoardData'})),
    
    path('add-series', views.cbtSeriesViewSet.as_view({'post': 'addUpdateSeriesData'})),
    path('update-series/<int:PR_SERIES_ID>', views.cbtSeriesViewSet.as_view({'post': 'addUpdateSeriesData'})),
    
    path('add-book-type', views.cbtBookTypeViewSet.as_view({'post': 'addUpdateBookTypeData'})),
    path('update-book-type', views.cbtBookTypeViewSet.as_view({'post': 'addUpdateBookTypeData'})),


]