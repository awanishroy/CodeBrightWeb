from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib import messages


# ======================================== HOME PAGE START =====================================

def index(request):
    seo = {
        'title': 'Home - CodeBright',
        'description': 'Welcome to the homepage of CodeBright. Learn more about our services and offers.',
        'keywords': 'home, company, services'
    }

    data = {
        'Seo' : seo
    }

    return render(request, 'websiteApp/index.html', data)

# ======================================== HOME PAGE END =======================================



# ======================================== COMPANY START ========================================

def company(request):
    seo = {
        'title': 'About Company  - CodeBright',
        'description': 'Learn more about CodeBright, our history, mission, and values.',
        'keywords': 'about us, company history, mission'
    }

    data = {
        'Seo' : seo
    }

    return render(request, 'websiteApp/company/company.html', data)

def about(request):
    seo = {
        'title': 'About Us - CodeBright',
        'description': 'Learn more about CodeBright, our history, mission, and values.',
        'keywords': 'about us, company history, mission'
    }

    data = {
        'Seo' : seo
    }

    return render(request, 'websiteApp/company/company.html', data)

def partners(request):
    seo = {
        'title': 'Partners - CodeBright',
        'description': 'Discover our partners and collaborators who help us deliver quality services.',
        'keywords': 'partners, collaborations, business partners'
    }

    data = {
        'Seo' : seo
    }

    return render(request, 'websiteApp/company/partners.html', data)

def careers(request):
    seo = {
        'title': 'Careers - CodeBright',
        'description': 'Explore career opportunities at CodeBright and join our talented team.',
        'keywords': 'careers, job opportunities, work with us'
    }

    data = {
        'Seo' : seo
    }

    return render(request, 'websiteApp/company/careers.html', data)

def events(request):
    seo = {
        'title': 'Events - CodeBright',
        'description': 'Stay updated with the latest events and activities hosted by CodeBright.',
        'keywords': 'events, company events, activities'
    }
    data = {
        'Seo' : seo
    }
    return render(request, 'websiteApp/company/events.html', data)

def view_events(request):
    seo = {
        'title': 'Events - CodeBright',
        'description': 'Stay updated with the latest events and activities hosted by CodeBright.',
        'keywords': 'events, company events, activities'
        }
    data = {
        'Seo' : seo
        }
    
    return render(request, 'websiteApp/company/view_event.html', data)

def team(request):
    seo = {
        'title': 'Our Team - CodeBright',
        'description': 'Meet the dedicated team members who drive the success of CodeBright.',
        'keywords': 'team, employees, staff'
    }

    data = {
        'Seo' : seo
    }

    return render(request, 'websiteApp/company/team.html', data)

def blog(request):
    seo = {
        'title': 'Blog - CodeBright',
        'description': 'Read the latest posts and updates from the CodeBright blog.',
        'keywords': 'blog, company updates, articles'
    }

    data = {
        'Seo' : seo
    }

    return render(request, 'websiteApp/company/blog.html', data)

def blog_details(request):
    seo = {
        'title': 'Blog Details - CodeBright',
        'description': 'Read the latest posts and updates from the CodeBright blog.',
        'keywords': 'blog, company updates, articles'
        }
    data = {
        'Seo' : seo
    }

    return render(request, 'websiteApp/company/blog_details.html', data)

def contact_us(request):
    seo = {
        'title': 'Contact Us - CodeBright',
        'description': 'Get in touch with us through our contact form or email address.',
        'keywords': 'contact, contact form, email'
        }
    data = {
        'Seo' : seo
        }
        
    return render(request, 'websiteApp/company/contact_us.html', data)

def contact_us_post(request):
    if request.method == "POST":
        # Retrieve form data
        PR_FIRST_NAME = request.POST.get('firstName')
        PR_LAST_NAME = request.POST.get('lastName')
        PR_EMAIL = request.POST.get('emailAddress')
        PR_PHONE = request.POST.get('phone')

        # # Save form data to the database
        # data = CbtBharatEcoFuels(
        #     PR_FIRST_NAME=PR_FIRST_NAME,
        #     PR_LAST_NAME=PR_LAST_NAME,
        #     PR_EMAIL=PR_EMAIL,
        #     PR_PHONE=PR_PHONE,
        # )
        # data.save()

        messages.success(request, 'Thank you for your interest in Code Bright Technologies. Our team will reach out to you soon!')
        return redirect('index')
    else:
        messages.error(request, 'Something went wrong. Please try again.')
        return redirect('index')
        

# ======================================== COMPANY END ========================================



# ======================================== PRODUCT START ========================================

def product_overview(request):
    seo = {
        'title': 'Product Overview - CodeBright',
        'description': 'Get an overview of our product features and benefits.',
        'keywords': 'product, overview, features'
    }

    data = {
        'Seo': seo
    }

    return render(request, 'websiteApp/product/overview.html', data)

def product_pricing(request):
    seo = {
        'title': 'Pricing - CodeBright',
        'description': 'Explore pricing plans and options for CodeBright products.',
        'keywords': 'pricing, plans, cost'
    }

    data = {
        'Seo': seo
    }

    return render(request, 'websiteApp/product/pricing.html', data)

def product_features(request):
    seo = {
        'title': 'Features - CodeBright',
        'description': 'Discover the features and functionalities of CodeBright products.',
        'keywords': 'features, functionalities, product details'
    }

    data = {
        'Seo': seo
    }

    return render(request, 'websiteApp/product/features.html', data)

def product_case_studies(request):
    seo = {
        'title': 'Case Studies - CodeBright',
        'description': 'Read case studies showcasing how our product has helped clients.',
        'keywords': 'case studies, success stories, client testimonials'
    }

    data = {
        'Seo': seo
    }

    return render(request, 'websiteApp/product/case_studies.html', data)

def view_case_studies(request):
    seo = {
        'title': 'Case Studies - CodeBright',
        'description': 'Read case studies showcasing how our product has helped clients.',
        'keywords': 'case studies, success stories, client testimonials'
    }

    data = {
        'Seo': seo
    }

    return render(request, 'websiteApp/product/view_case_studies.html', data)

def product_new_releases(request):
    seo = {
        'title': 'New Releases - CodeBright',
        'description': 'Stay updated with the latest releases and updates for our products.',
        'keywords': 'new releases, updates, product news'
    }

    data = {
        'Seo': seo
    }

    return render(request, 'websiteApp/product/new_releases.html', data)

def product_solutions(request):
    seo = {
        'title': 'Solutions - CodeBright',
        'description': 'Explore the various solutions our product offers to different problems.',
        'keywords': 'solutions, product applications, use cases'
    }

    data = {
        'Seo': seo
    }

    return render(request, 'websiteApp/product/solutions.html', data)

# ======================================== PRODUCT END ==========================================



# ======================================== LEGAL START ==========================================

def legal_licenses(request):
    seo = {
        'title': 'Licenses - CodeBright',
        'description': 'Information about licenses for CodeBright products and services.',
        'keywords': 'licenses, product licenses, legal'
    }

    data = {
        'Seo': seo
    }

    return render(request, 'websiteApp/legal/licenses.html', data)

def legal_settings(request):
    seo = {
        'title': 'Settings - CodeBright',
        'description': 'Privacy and settings information for CodeBright products.',
        'keywords': 'settings, privacy, user settings'
    }

    data = {
        'Seo': seo
    }

    return render(request, 'websiteApp/legal/settings.html', data)

def legal_cookies(request):
    seo = {
        'title': 'Cookies - CodeBright',
        'description': 'Learn about our use of cookies and how they impact your privacy.',
        'keywords': 'cookies, privacy policy, data'
    }

    data = {
        'Seo': seo
    }

    return render(request, 'websiteApp/legal/cookies.html', data)

def legal_document(request):
    seo = {
        'title': 'Document - CodeBright',
        'description': 'Access important documents related to CodeBright services.',
        'keywords': 'document, legal documents, access'
    }

    data = {
        'Seo': seo
    }

    return render(request, 'websiteApp/legal/document.html', data)

def legal_terms(request):
    seo = {
        'title': 'Terms - CodeBright',
        'description': 'Read the terms and conditions for using CodeBright services.',
        'keywords': 'terms, terms and conditions, usage policy'
    }

    data = {
        'Seo': seo
    }

    return render(request, 'websiteApp/legal/terms.html', data)

def legal_privacy(request):
    seo = {
        'title': 'Privacy - CodeBright',
        'description': 'Understand our privacy policy and how we protect your data.',
        'keywords': 'privacy, privacy policy, data protection'
    }

    data = {
        'Seo': seo
    }

    return render(request, 'websiteApp/legal/privacy.html', data)

# ======================================== LEGAL END ============================================


# ======================================= PORTFOLIO START =======================================

def portfolio(request):
    seo = {
        'title': 'Portfolio - CodeBright',
        'description': 'Browse our portfolio of projects and services.',
        'keywords': 'portfolio, projects, services'
        }
    data = {
        'Seo': seo
        }
    return render(request, 'websiteApp/portfolio/portfolio.html', data)

# ======================================= PORTFOLIO END =========================================


# ======================================= SERVICES START ========================================

def services(request):
    seo = {
        'title': 'Services - CodeBright',
        'description': 'Discover our range of services and how we can help you.',
        'keywords': 'services, service, help'
        }
    data = {
        'Seo': seo
        }
    return render(request, 'websiteApp/services/services.html', data)

# ======================================= SERVICES END ===========================================


# ======================================= OUR FIELDS START =======================================

def our_fields(request):
    seo = {
        'title': 'Our Fields - CodeBright',
        'description': 'Learn about our areas of expertise and how we can help you.',
        'keywords': 'our fields, areas of expertise'
        }
    data = {
        'Seo': seo
        }
    return render(request, 'websiteApp/our_fields/our_fields.html', data)

# ======================================= OUR FIELDS END =========================================


# =========================================== FAQ START ==========================================

def faq(request):
    seo = {
        'title': 'FAQ - CodeBright',
        'description': 'Get answers to your questions about our services and more.',
        'keywords': 'faq, questions, answers'
        }
    data = {
        'Seo': seo
        }
    return render(request, 'websiteApp/faq/faq.html', data)

# ============================================ FAQ END ============================================



# =========================================== OTHERS START ==========================================

def how_we_do(request):
    seo = {
        'title': 'How We Do - CodeBright',
        'description': 'Learn about our process and how we deliver results.',
        'keywords': 'how we do, process, results'
        }
    data = {
        'Seo': seo
        }
    return render(request, 'websiteApp/others/how_we_do.html', data)

# ============================================ OTHERS END ===========================================

