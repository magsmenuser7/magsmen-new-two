

// Contact Form 
$(document).ready(function () {
    $('#sendbtn').click(function () {

        let name = $('#name').val();
        let email = $('#email').val();
        let phone = $('#phone').val();
        let subject = $('#subject').val();
        let message = $('#message').val();
        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();

         // Regular expressions for validation
         let emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
         let phonePattern = /^[0-9]{10}$/; // Adjust the pattern based on your phone format requirements
 
         // Validation for required fields
         if (name == "") {
             alert("Name Field Required");
             return;
         }
         if (email == "") {
             alert("Email Field Required");
             return;
         }
         if (!emailPattern.test(email)) {
             alert("Invalid Email Format");
             return;
         }
         if (phone == "") {
             alert("Phone Field Required");
             return;
         }
         if (!phonePattern.test(phone)) {
             alert("Invalid Phone Format. Please enter a 10-digit phone number.");
             return;
         }
         if (subject == "") {
             alert("Subject Field Required");
             return;
         }
         if (message == "") {
             alert("Message Field Required");
             return;
         }




        let data = new FormData();
        data.append("name", name);
        data.append("email", email);
        data.append("phone", phone);
        data.append("subject", subject);
        data.append("message", message);
        data.append('csrfmiddlewaretoken', csrfmiddlewaretoken)



        $.ajax({
            url: "/contact/",
            method: 'POST',
            processData: false,
            contentType: false,
            cache: false,
            mimeType: "multipart/form-data",
            data:data,

            success: function (data) {
                $('#contactsbmt')[0].reset();
                alert("sucessfully sending message")
                //    $('.returnmessage').append("Your message has been received, We will contact you soon.")
            },
            error: function (data) {
                alert("Your message has been faild, please try agian.")
                //    $('.returnmessage').append("Your message has been faild, please try agian.")
            }
        })

    })

})



// Apply Form 
$(document).ready(function () {
    $('#applybtn').click(function () {
        let name = $('#name').val();
        let email = $('#email').val();
        let phonenumber = $('#phonenumber').val();
        let selectcategory = $('#selectcategory').val();
        let location = $('#location').val();
        let file = $('#uploadfile')[0].files[0];
        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();

         // Regular expressions for validation
         let emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
         let phonePattern = /^[0-9]{10}$/; // Adjust the pattern based on your phone format requirements
 
         // Validation for required fields
         if (name == "") {
             alert("Name Field Required");
             return;
         }
         if (email == "") {
             alert("Email Field Required");
             return;
         }
         if (!emailPattern.test(email)) {
             alert("Invalid Email Format");
             return;
         }
         if (phonenumber == "") {
             alert("Phone Field Required");
             return;
         }
         if (!phonePattern.test(phonenumber)) {
             alert("Invalid Phone Format. Please enter a 10-digit phone number.");
             return;
         }
         if (selectcategory == "selectcategory") {
             alert("Please select your category Field ");
             return;
         }
         if (location == "location") {
             alert("Location Field Required");
             return;
         }

        if (!file){
            alert('Please upload a file');
            return;
        }





        let data = new FormData();
        data.append("name", name);
        data.append("email", email);
        data.append("phone", phonenumber);
        data.append("selectcategory", selectcategory);
        data.append("location", location);
        data.append("file", file);
        data.append('csrfmiddlewaretoken', csrfmiddlewaretoken)



        $.ajax({
            url: "/apply/",
            method: 'POST',
            processData: false,
            contentType: false,
            cache: false,
            mimeType: "multipart/form-data",
            data:data,

            success: function (data) {
                $('#apply-form')[0].reset();
                alert("sucessfully sending message")
                //    $('.returnmessage').append("Your message has been received, We will contact you soon.")
            },
            error: function (data) {
                alert("Your message has been faild, please try agian.")
                //    $('.returnmessage').append("Your message has been faild, please try agian.")
            }
        })

    })

})


// ==================== Apply form =======================//

// $(document).ready(function(){
//     $('#applybtn').click(function(){
//         let name = $('#name').val()
//         let email = $('#email').val()
//         let phonenumber = $('#phonenumber').val()
//         let selectcategory = $('#selectcategory').val()
//         let location = $('#location').val()
//         let file = $('#uploadfile')[0].files[0];
//         let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()

//         if (name === '') {
//             alert('Name field required');
//             return; // Stop execution if validation fails
//         }
//         if (email === '') {
//             alert('Email field required');
//             return; // Stop execution if validation fails
//         }
//         if (!isValidEmail(email)) {
//             alert('Invalid email format');
//             return; // Stop execution if validation fails
//         }
//         if (phonenumber === '') {
//             alert('Phone number required');
//             return; // Stop execution if validation fails
//         }
//         if (!isValidPhone(phonenumber)) {
//             alert('Invalid phone number format');
//             return; // Stop execution if validation fails
//         }

//         if (selectcategory === 'selectcategory'){
//             alert("Category field required")
//             return;
//         }

//         if (location === 'location'){
//             alert("Location field required")
//             return;
//         }
        
//         if (!file){
//             alert('Please upload a file');
//             return;
//         }





//         // SubmitEvent()

//         let data = new FormData();
//         data.append("name", name),
//         data.append("email",email),
//         data.append("phonenumber",phonenumber),
//         data.append("selectcategory",selectcategory),
//         data.append("location",location),
//         data.append("file",file),
//         data.append('csrfmiddlewaretoken',csrfmiddlewaretoken)

//         $.ajax({
//             url:"applyform/",
//             method: 'POST',
//             processData:false,
//             contentType:false,
//             cache:false,
//             data:data,
//             success:function(data, status,xhr){
//                 // $('#apply-form')[0].reset();
//                 if(data.success === true){
//                     alert("Job Form Applied success")
//                     // window.location.href ='/';
//                 }else{
//                     alert(data.error)
//                     // window.location.href = '/applyform/'
//                 }
//             },
//             error:function(data){
//                 alert("fail, submitted data")
//             }
            
//         })
    
//     });
// });

// function isValidEmail(email) {
//     let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
//     return emailRegex.test(email);
// }

// function isValidPhone(phonenumber) {
//     let phoneRegex = /^\d{10}$/;
//     return phoneRegex.test(phonenumber);
// }




// subscribe form

// document.addEventListener('DOMContentLoaded', function () {
//     // Get URL parameters
//     const urlParams = new URLSearchParams(window.location.search);
//     const successMessage = urlParams.get('success');
//     const errorMessage = urlParams.get('error');

//     // Show an alert if there's a success or error message
//     if (successMessage) {
//         alert(successMessage);
//     } else if (errorMessage) {
//         alert(errorMessage);
//     }

//     // Remove the query parameters from the URL
//     if (successMessage || errorMessage) {
//         window.history.replaceState(null, '', window.location.pathname);
//     }
// });





// Subscribe Form

// document.getElementById("subscribe-form").addEventListener("submit", async (event) => {
//     event.preventDefault();
//     const email = document.getElementById("subscribe-email").value;

//     const response = await fetch("/subscribe/", {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/x-www-form-urlencoded",
//             "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
//         },
//         body: `email=${encodeURIComponent(email)}`,
//     });

//     const result = await response.json();
//     alert(result.message);
// });



$(document).ready(function () {
    $('#subscribe-form').submit(function () {
        let email = $('#email').val();
        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();

        let data = new FormData();
        data.append("email", email);
        data.append('csrfmiddlewaretoken', csrfmiddlewaretoken)



        $.ajax({
            url: "subscribe/",
            method: 'POST',
            processData: false,
            contentType: false,
            cache: false,
            mimeType: "multipart/form-data",
            data:data,

            success: function(response) {
                // Check the response status and display the message
                if (response.status === "success") {
                    alert(response.message);  // Display success message
                    
                } else {
                    alert(response.message);  // Display error message

                }
            },
            error: function(xhr, status, error) {
                // Handle any error that occurs during the AJAX call
                alert("You are already subscribed");
            }
        })

    })

})









// get started form

function writetousbtn(){

    var fname = document.getElementById("fname").value.trim();
    var femail = document.getElementById("femail").value.trim();
    var fphone = document.getElementById("fphone").value.trim();
   
   if(fname === ''){
       alert("Name Field Required");
       return;
   }
   if(femail === ''){
       alert("Email Field Required");
       return;
   }
   if (!isValidEmail(femail)) {
       alert("Invalid Email Format");
       return;
   }
   
   if(fphone === ''){
       alert("Phone Field Required");
       return;
   }
   
   if (!isValidPhone(fphone)) {
       alert("Invalid Phone Number Format");
       return;
   }
   
   
   
       let formdata = {
           fname: fname,
           femail: femail,
           fphone: fphone,
       };
   
       let formDataJson = JSON.stringify(formdata);
       localStorage.setItem('formdata', formDataJson);
       window.location.href = 'questions/';
   
   }
   function isValidEmail(email) {
       const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
       return emailPattern.test(email);
   }
   function isValidPhone(phone) {
       const phonePattern = /^\d{10}$/; // Adjust pattern according to your requirement
       return phonePattern.test(phone);
   }
   
   
   
   $(document).ready(function(){
       $('#allformssubmit').click(function(event){
           event.preventDefault();
           let brandpositionradio = $('input[name="brandpositionradio"]:checked').val();
           let mission = $('#mission').val()
           let brandtargetradio = $('input[name="brandtargetradio"]:checked').val();
           let engagebrandradio = $('input[name="engagebrandradio"]:checked').val();
           let brandperform = $('#brandperform').val()
           let brandchallenge = $('#brandchallenge').val()
           // let brandcheck = $('input[name=brandcheck]:checked').map(function(){
           //     return $(this).val();
           // }).get();
           var motivations = [];
           $('input[name="brandcheck"]:checked').each(function() {
               motivations.push($(this).val());
           });
           let achieve = $('#achieve').val()
           let brandexpectation = $('#brandexpectation').val()
           let storedFormDataJson = localStorage.getItem('formdata');
           let storedFormData = JSON.parse(storedFormDataJson);
           let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()
           
           
   
   
   
           let data = new FormData();
           data.append('brandposition',brandpositionradio),
           data.append('corevalue',mission),
           data.append('brandtarget',brandtargetradio),
           data.append('customerfeedback',engagebrandradio),
           data.append('brandperform',brandperform),
           data.append('brandchallenge',brandchallenge),
           data.append('brandcheck',motivations),
           data.append('achieve',achieve),
           data.append('brandexpectation',brandexpectation),
           data.append('storedFormData', JSON.stringify(storedFormData));
           data.append('csrfmiddlewaretoken',csrfmiddlewaretoken),
   
           $.ajax({
               url:"/questions/",
               method: 'POST',
               processData:false,
               contentType:false,
               cache:false,
               data:data,
               success:function(data, status,xhr){
                   $('#userAccountSetupForm')[0].reset();
                   if(data.success === true){
                       alert("All Done.Thank You")
                       window.location.href ='/';
                   }else{
                       alert(data.error)
                       window.location.href = '/questions/'
                   }
               },
               error:function(data){
                   alert("fail, submitted data")
               }
               
           })
   
       })
       
   })
   
   
   // Select all checkboxes
   document.getElementById('checkall').addEventListener('change', function () {
       const checkboxes = document.querySelectorAll('input[name="brandcheck"]');
       checkboxes.forEach((checkbox) => {
           checkbox.checked = this.checked;
       });
   });
   
   
   // Enable/disable Next button based on input validation
   document.querySelectorAll('input[type="text"], textarea').forEach((input) => {
       input.addEventListener('input', function () {
           const nextBtn = document.querySelector(`button[step_number="${currentStep + 1}"]`);
           if (this.value.trim() !== '') {
               nextBtn.disabled = true;
           } else {
               nextBtn.disabled = false;
           }
       });
   });
   
   













// // portfolio popup functionality
//    $(document).ready(function () {
//     $('#popupbtn').click(function {
        
//         // Retrieve field values
//         let popname = $('#popname').val();
//         let popemail = $('#popemail').val();
//         let popphone = $('#popphone').val();
//         let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();

//         // Regular expressions for validation
//         let emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
//         let phonePattern = /^[0-9]{10}$/; // Adjust for your phone number format

//         // Validation for required fields
//         if (popname === "") {
//             alert("Name field is required");
//             return;
//         }
//         if (popemail === "") {
//             alert("Email field is required");
//             return;
//         }
//         if (!emailPattern.test(popemail)) {
//             alert("Invalid email format");
//             return;
//         }
//         if (popphone === "") {
//             alert("Phone field is required");
//             return;
//         }
//         if (!phonePattern.test(popphone)) {
//             alert("Invalid phone format. Please enter a 10-digit phone number.");
//             return;
//         }




//         let data = new FormData();
//         data.append("popname", popname);
//         data.append("popemail", popemail);
//         data.append("popphone", popphone);
//         data.append('csrfmiddlewaretoken', csrfmiddlewaretoken)





//         // If validation passes, you can send data to the server (e.g., via AJAX)

//         $.ajax({
//             url: 'submit-form/',
//             method: 'POST',
//             processData: false,
//             contentType: false,
//             cache: false,
//             mimeType: "multipart/form-data",
//             data:data,


//             success: function (response) {
//                 alert('Form submitted successfully');
//                 $('#popup-form')[0].reset(); // Reset the form on success
//             },
//             error: function (error) {
//                 alert('There was an error submitting the form. Please try again.');
//             }
//         });
//     });
// });



// // portfolio popup functionality
//    document.getElementById('popup-form').addEventListener('submit', function(event) {
//     event.preventDefault();

//     const formData = new FormData(this);

//     fetch('/submit-form/', {
//         method: 'POST',
//         body: formData,
//         headers: {
//             'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
//         }
//     })
//     .then(response => response.json())
//     .then(data => {
//         alert(data.message || data.error);
//     })
//     .catch(error => console.error('Error:', error));
// });

