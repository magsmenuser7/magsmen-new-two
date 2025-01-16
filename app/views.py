from django.shortcuts import render
from .models import BlogPost,ContactData,Media,StepformData,Subscribe,CareerInfo,ApplyForm,IntalksForm,PortfolioPopupSubmission
from django.core.paginator import Paginator
from django.core.mail import send_mail,EmailMessage
from django.contrib import messages
from django.http import FileResponse, HttpResponseRedirect, JsonResponse
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from magsmen import settings
import os


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactSerializer


# Create your views here.



@api_view(['POST'])
def contact_api_view(request):
    if request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Contact saved successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def get_contacts(request):
    contacts = IntalksForm.objects.all()  # Replace 'Contact' with your model name
    serializer = ContactSerializer(contacts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



def home(request):
    blog_list = BlogPost.objects.filter().order_by('-Id')[:2]
    return render(request, 'uifiles/home.html',{'blog_list':blog_list})


@csrf_exempt
def subscribe(request):
    if request.method == "POST":
        email = request.POST.get('email')

        # Check if the email field is provided
        if not email:
            return JsonResponse({"status": "error", "message": "Email field cannot be empty."}, status=400)

        # Check if the email already exists in the database
        if Subscribe.objects.filter(Email=email).exists():
            return JsonResponse({"status": "error", "message": "You're already subscribed."}, status=400)

        try:
            # Save the email to the database
            Subscribe.objects.create(Email=email)

            # Send a confirmation email
            send_mail(
                subject='Subscription Confirmation',
                message='Thank you for subscribing to our newsletter!',
                from_email='connectmagsmen@gmail.com',  # Replace with your email
                recipient_list=[email],
                fail_silently=False,
            )

            # Redirect to a success message
            return JsonResponse({"status": "success", "message": "You have been subscribed successfully."})

        except Exception as e:
            # Log the error (optional: use a logger for production apps)
            print(f"Error occurred during subscription: {e}")
            return HttpResponseRedirect('/?error=An error occurred. Please try again later.')

    # Redirect to the home page for invalid request methods
    return HttpResponseRedirect('/?error=Invalid request method.')


@csrf_exempt
def submit_form(request):
    if request.method == 'POST':
        popname = request.POST.get('popname')
        popemail = request.POST.get('popemail')
        popphone = request.POST.get('popphone')

        # Save the data to the database
        portfolio_submission = PortfolioPopupSubmission(
            name=popname,
            email=popemail,
            phone=popphone
        )
        portfolio_submission.save()

        # Send an email
        send_mail(
            subject="Magsmen Portfolio Form Submission",
            message=f"Name: {popname}\nEmail: {popemail}\nPhone: {popphone}",
            from_email="connectmagsmen@gmail.com",
            recipient_list=['connectmagsmen@gmail.com','kajasuresh522@gmail.com'],
            fail_silently=False,
        )

        return JsonResponse({'message': 'Portfolio submitted successfully!'})

    return JsonResponse({'error': 'Invalid request'}, status=400)



def about(request):
    return render(request, 'uifiles/about.html')

def expertise(request):
    return render(request, 'uifiles/expertise.html')

def brand_consulting(request):
    return render(request, 'uifiles/brand-consulting.html')

def personal_brand_consulting(request):
    return render(request, 'uifiles/personal-brand-consulting.html')

def image_consulting(request):
    return render(request, 'uifiles/image-consulting.html')

def corporate_rebranding(request):
    return render(request, 'uifiles/corporate-rebranding.html')

def brand_expresso(request):
    return render(request, 'uifiles/brand-expresso.html')

def brand_creation(request):
    return render(request, 'uifiles/brand-creation.html')

def link_fluence(request):
    return render(request, 'uifiles/link-fluence.html')

def launchpad(request):
    return render(request, 'uifiles/launchpad.html')

def works(request):
    return render(request, 'uifiles/works.html')

def telugufoods(request):
    return render(request, 'uifiles/telugufoods.html')

def suryacolors(request):
    return render(request, 'uifiles/suryacolors-two.html')

def tdhrishika(request):
    return render(request, 'uifiles/tdhfoods.html')

def tenalidoublehorse(request):
    return render(request, 'uifiles/tenalidoublehorse.html')

def triplex(request):
    return render(request, 'uifiles/triplex.html')

def vsbsurface(request):
    return render(request, 'uifiles/vsbsurface.html')

def zavaine(request):
    return render(request, 'uifiles/zavaine.html')

def blog(request):
    blog_posts = BlogPost.objects.filter().order_by('-Id')[:2]
    blog_item = BlogPost.objects.filter().order_by('-Id')
    paginator = Paginator(blog_item, 4) # paginate 10 posts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'uifiles/blog.html',{'blog_posts':blog_posts,'blog_item':posts,'posts':posts,'page':page})


def blogdetails(request,slug):
    blogpost = BlogPost.objects.get(Sluglink=slug)
    return render(request, 'uifiles/blog-details.html',{'blogpost':blogpost})

def career(request):
    career_job = CareerInfo.objects.all()
    return render(request, 'uifiles/careers.html',{'career_job':career_job})


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        subject = request.POST.get('subject',"")
        message = request.POST.get('message',"")
        oContactinfo = ContactData(Name=name,Email=email,Phone=phone,Subject=subject,Message=message)
        oContactinfo.save()
        
        message ='''
        Name:{}
        Email:{}
        Phone:{}
        Subject:{}
        Message:{}
        From:{}
        '''.format(name,email,phone,subject,message,email)
        try:
            send_mail(subject, message,'connectmagsmen@gmail.com',recipient_list=['connectmagsmen@gmail.com','kajasuresh522@gmail.com']) 
            messages.success(request,'Message has been sucesfully send')
        except:
            messages.error(request,'Your message has been failed, Please Try Agian')
    return render(request, 'uifiles/contact.html')

    
def Ourmedia(request):
    media_items = Media.objects.filter().order_by('-Id')[:2]
    media = Media.objects.filter().order_by('-Id')
    paginator = Paginator(media,4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'uifiles/media.html',{'media_items':media_items,'media':posts,'posts':posts,'page':page})




def Questionsform(request):
    if request.method == 'POST':
        storedFormData = request.POST.get('storedFormData')
        
        # Convert JSON string to dictionary
        stored_form_data = json.loads(storedFormData)
        
        # name=request.POST.get('name')
        # email=request.POST.get('email')
        # phone=request.POST.get('phone')
        # storedFormData = request.POST.get('storedFormData')
        brandposition = request.POST.get('brandposition')
        corevalue = request.POST.get('corevalue')
        brandtarget = request.POST.get('brandtarget')
        customerfeedback = request.POST.get('customerfeedback')
        brandperform = request.POST.get('brandperform')
        brandchallenge = request.POST.get('brandchallenge')
        brandmotivation = request.POST.getlist('brandcheck')
        achieve = request.POST.get('achieve')
        brandexpectation = request.POST.get('brandexpectation')

        oQuestion_data = StepformData(name=stored_form_data.get('fname'),email=stored_form_data.get('femail'),phone=stored_form_data.get('fphone'),Brandmarketposition=brandposition,BrandCorevalue=corevalue,Brandperceive_targetaudience=brandtarget,CustomerFeedback=customerfeedback,BrandPerformence=brandperform,Challenges_Obstacles=brandchallenge,Brand_Motivation=brandmotivation,Goals_Achieves=achieve,Expectations=brandexpectation)
        oQuestion_data.save()
        
         # Send email notification
        subject = 'Step Form Submission Notification'
        message = 'A form has been submitted with the following details:\n\n' \
                  f'Name: {stored_form_data.get("fname")}\n' \
                  f'Email: {stored_form_data.get("femail")}\n' \
                  f'Phone: {stored_form_data.get("fphone")}\n\n' \
                  'Additional form details:\n' \
                  f'Brand Position: {brandposition}\n' \
                  f'Core Value: {corevalue}\n' \
                  f'Target Audience: {brandtarget}\n' \
                  f'Customer Feedback: {customerfeedback}\n' \
                  f'Brand Performance: {brandperform}\n' \
                  f'Brand Challenge: {brandchallenge}\n' \
                  f'Brand Motivation: {", ".join(brandmotivation)}\n' \
                  f'Achievements: {achieve}\n' \
                  f'Brand Expectation: {brandexpectation}'
        
        from_email = 'connectmagsmen@gmail.com'  # Update with your sender email
        to_email = ['connectmagsmen@gmail.com']  # Update with recipient email(s)
        
        try:
            send_mail(subject, message,'connectmagsmen@gmail.com', recipient_list=['connectmagsmen@gmail.com','kajasuresh522@gmail.com'])
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return render(request, 'uifiles/multistepform.html')


def apply_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phonenumber')
        selectcategory = request.POST.get('selectcategory')
        location = request.POST.get('location')
        file = request.FILES.get('file')

        oApplyformdata = ApplyForm(Name=name,Email=email,Phone=phone_number,SelectCategory=selectcategory,Location=location,Uploadfile=file)
        oApplyformdata.save()

        subject = 'Job Notification: {}'.format(name)
        message ='''
        New Job Notification

        Name: {}
        Email: {}
        Phone Number: {}
        Selected Category: {}
        Location: {}

        '''.format(name, email, phone_number, selectcategory, location)

        try:
            send_mail(subject, message,'connectmagsmen@gmail.com',recipient_list=['connectmagsmen@gmail.com','kajasuresh522@gmail.com']) 
            messages.success(request,'Message has been sucesfully send')
        except:
            messages.error(request,'Your message has been failed, Please Try Agian')

    return render(request, 'uifiles/applyform.html')



def handler404(requerst, exception):
    return render(requerst, 'uifiles/404.html',status=400)

def privacy_policy(request):
    return render(request,'uifiles/privacy-policy.html')

def terms_conditions(request):
    return render(request,'uifiles/terms-conditions.html')

def cancellation_and_refund_policy(request):
    return render(request,'uifiles/cancellation-refundpolicy.html')

def faqs(request):
    return render(request,'uifiles/faqs.html')

def accessyourbrand(request):
    return render(request,'uifiles/access-your-brand.html')


def magsmen_brand_portfolio(request):
    pdf_filename = 'owl-Magsmen-Brand-Presentation.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename}"'
    return response


def Newsletter(request):
   
    pdf_filename = 'news-letter-august-2023.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename}"'
    return response

def Newslettertwo(request):
    pdf_filename_two = 'the-name-of-the-article-indian-brand-success-stories.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename_two)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename_two}"'
    return response

def Newsletterthree(request):
    pdf_filename_two = 'brand-corner-november-edition.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename_two)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename_two}"'
    return response

def Brand(request):
    pdf_filename_three = 'brand-architecture.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename_three)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename_three}"'
    return response


def BrandRefresh(request):
    pdf_filename_four = 'brand-refresh-rebranding-june.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename_four)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename_four}"'
    return response


def DigitalTwin_BrandStrategy(request):
    pdf_filename_five = 'digital-twin-brand-strategy.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename_five)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename_five}"'
    return response


def Monochromatic_colors_in_branding(request):
    pdf_filename_six = 'monochromatic-colors-in-branding.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename_six)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename_six}"'
    return response

def band_corner_the_new_age_of_buying_brand_activism(request):
    pdf_filename_seven = 'band-corner-the-new-age-of-buying-brand-activism.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename_seven)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename_seven}"'
    return response

def brand_naming_unlock_the_soul_of_your_brand(request):
    pdf_filename_eight = 'brand-naming-unlock-the-soul-of-your-brand.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename_eight)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename_eight}"'
    return response

def the_power_of_consistency_why_brand_tone_matters(request):
    pdf_filename_nine = 'the-power-of-consistency-why-brand-tone-matters.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename_nine)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename_nine}"'
    return response


def a_cutting_edge_approach_in_branding(request):
    pdf_filename_ten = 'a-cutting-edge-approach-in-branding-compressed.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename_ten)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename_ten}"'
    return response

def brand_corner_trademarks(request):
    pdf_filename_ten = 'brand_corner_trademarks_and_deceptive_practices.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename_ten)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename_ten}"'
    return response
