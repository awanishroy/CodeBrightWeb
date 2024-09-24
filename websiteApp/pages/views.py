from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib import messages
import requests
import pandas as pd
import json
from websiteApp.pages.serializers import *
from rest_framework import viewsets , status
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods


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

@csrf_protect
@require_http_methods(["POST"])
def contact_us_post(request):
    api_url = "https://apis.codebright.in/portfolio-api/contact-us-message-add"
    
    # Extract form data from request.POST
    payload = {
        "PR_WEBSITE_ID": 1,
        "PR_FIRST_NAME": request.POST.get('firstName'),
        "PR_LAST_NAME": request.POST.get('lastName'),
        "PR_EMAIL": request.POST.get('emailAddress'),
        "PR_PHONE": request.POST.get('phone'),
        "PR_MESSAGE": request.POST.get('PR_MESSAGE'),
        "PR_PRIVACY_POLICY_ACCEPT": request.POST.get('privacy_policy_accept') == 'on'
    }

    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        if response.status_code == 200:
            site_data = response.json()
            return JsonResponse({
                'status': 'success',
                'message': 'Thank you for your interest in Code Bright Technologies. Our team will reach out to you soon!',
                'site_data': site_data
            })
        else:
            return JsonResponse({
                'status': 'error',
                'message': 'An error occurred while processing your request. Please try again later.'
            }, status=500)
    
    except requests.RequestException as e:
        print(f"API request failed: {str(e)}")
        return JsonResponse({
            'status': 'error',
            'message': 'An error occurred while processing your request. Please try again later.'
        }, status=500)


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


class cbtBookViewSet(viewsets.ModelViewSet):
    
    def addUpdateBookData(self, request , PR_BOOK_ID = None):
        try:
            data = request.data
            if PR_BOOK_ID != None:
                try:
                    instance = CbtBookData.objects.get(PR_BOOK_ID=PR_BOOK_ID)
                    serializer = CbtBookDataSerializer(instance, data=data, partial=True)
                except CbtBookData.DoesNotExist:
                    return Response({'message': 'Data Not Found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                serializer = CbtBookDataSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'success'}, status=status.HTTP_201_CREATED if 'PR_ID' not in data else status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return JsonResponse({'message': 'fail', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def importBookData(self, request):
        """
        Handles bulk book data import using a CSV or Excel file upload.
        """
        try:
            file = request.FILES.get('PR_FILE')
            if not file:
                return JsonResponse({'message': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

            # Read the file into a DataFrame
            df = pd.read_excel(file)  # Use pd.read_csv(file) if handling CSV files
            
            # Fill missing values with specified defaults
            df.fillna({
                'Title': '', 
                'Sub Title': '', 
                'ISBN': '', 
                'Board Id':'', 
                'Class Id':'' , 
                'Series Id':'', 
                'BookType Id': '' ,
                'Imprint':'' ,
                'Author':'', 
                'Edition':'', 
                'Company': '',
                'Book Code': '', 
                'Copyright': '', 
                'Date Of Release': pd.NaT, 
                'Binding': '',
                'Language': '', 
                'Pages': '', 
                'TrimSize': '', 
                'Weight': '', 
                'List Price': '',
                'Discount': '', 
                'BookNumber': '', 
                'ClassLevel': '', 
                'ProductDivision': '',
                'BroadSubject': '', 
                'Detailed Subject': '', 
                'ProductDescription': ''}, inplace=True)

            # Start a transaction
            book_objects = []
            for index, row in df.iterrows():
                # Create a book object for each row in the DataFrame
                book = CbtBookData(
                    PR_TITLE=row['Title'],
                    PR_SUB_TITLE=row['Sub Title'],
                    PR_ISBN=row['ISBN'],
                    PR_BOARD_id=row['Board Id'],
                    PR_CLASS_id=row['Class Id'],
                    PR_SERIES_id=row['Series Id'],
                    PR_BOOK_TYPE_id=row['BookType Id'], 
                    PR_IMPRINT=row['Imprint'],
                    PR_BOOK_CODE=row['Book Code'],
                    PR_COPYRIGHT=row['Copyright'],
                    PR_DATE_OF_RELEASE=pd.to_datetime(row['Date Of Release']).date() if pd.notna(row['Date Of Release']) else None,
                    PR_BINDING=row['Binding'],
                    PR_LANGUAGE=row['Language'],
                    PR_PAGES=int(row['Pages']) if pd.notnull(row['Pages']) else None,
                    PR_TRIM_SIZE=row['TrimSize'],
                    PR_WEIGHT=float(row['Weight']) if pd.notnull(row['Weight']) else None,
                    PR_LIST_PRICE=float(row['List Price']) if pd.notnull(row['List Price']) else None,
                    PR_DISCOUNT=float(row['Discount']) if pd.notnull(row['Discount']) else None,
                    PR_BOOK_NUMBER=int(row['BookNumber']) if pd.notnull(row['BookNumber']) else None,
                    PR_CLASS_LEVEL=row['ClassLevel'],
                    PR_PRODUCT_DIVISION=row['ProductDivision'],
                    PR_BROAD_SUBJECT=row['BroadSubject'],
                    PR_DETAILED_SUBJECT=row['Detailed Subject'],
                    PR_PRODUCT_DESCRIPTION=row['ProductDescription'],
                )
                book_objects.append(book)

            # Bulk create all book objects in one transaction
            CbtBookData.objects.bulk_create(book_objects)

            return JsonResponse({'message': 'Books imported successfully!'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return JsonResponse({'message': 'Import failed', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         
class cbtClassViewSet(viewsets.ModelViewSet):

    def addUpdateClassData(self, request , PR_CLASS_ID = None):
        try:
            data = request.data
            if PR_CLASS_ID != None:
                try:
                    instance = CbtClasses.objects.get(PR_CLASS_ID=PR_CLASS_ID)
                    serializer = CbtClassesSerializer(instance, data=data, partial=True)
                except CbtClasses.DoesNotExist:
                    return Response({'message': 'Data Not Found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                serializer = CbtClassesSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'success'}, status=status.HTTP_201_CREATED if 'PR_ID' not in data else status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return JsonResponse({'message': 'fail', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class cbtBoardViewSet(viewsets.ModelViewSet):
    
    def addUpdateBoardData(self,request , PR_BOARD_ID = None):
        try:
            data = request.data
            if PR_BOARD_ID != None:
                try:
                    instance = CbtBoard.objects.get(PR_BOARD_ID=PR_BOARD_ID)
                    serializer = CbtBoardSerializer(instance, data=data, partial=True)
                except CbtBoard.DoesNotExist:
                    return Response({'message': 'Data Not Found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                serializer = CbtBoardSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'success'}, status=status.HTTP_201_CREATED if 'PR_ID' not in data else status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return JsonResponse({'message': 'fail', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class cbtSeriesViewSet(viewsets.ModelViewSet):
    
    def addUpdateSeriesData(self, request, PR_SERIES_ID=None):
        try:
            data = request.data

            if PR_SERIES_ID is not None:
                try:
                    instance = CbtSeries.objects.get(PR_SERIES_ID=PR_SERIES_ID)
                    serializer = CbtSeriesSerializer(instance, data=data, partial=True)
                except CbtSeries.DoesNotExist:
                    return Response({'message': 'Data Not Found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                serializer = CbtSeriesSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                if PR_SERIES_ID is not None:
                    return Response({'message': 'Series updated successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'Series created successfully'}, status=status.HTTP_201_CREATED)
            else:
                # Return validation errors
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # Handle any unforeseen errors
            return JsonResponse({'message': 'fail', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class cbtBookTypeViewSet(viewsets.ModelViewSet):
    
    def addUpdateBookTypeData(self,request,PR_BOOK_TYPE_ID):
        try:
            data = request.data
            if PR_BOOK_TYPE_ID != None:
                try:
                    instance = CbtBoard.objects.get(PR_BOOK_TYPE_ID=PR_BOOK_TYPE_ID)
                    serializer = CbtClassesSerializer(instance, data=data, partial=True)
                except CbtBoard.DoesNotExist:
                    return Response({'message': 'Data Not Found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                serializer = CbtClassesSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'success'}, status=status.HTTP_201_CREATED if 'PR_ID' not in data else status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return JsonResponse({'message': 'fail', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    