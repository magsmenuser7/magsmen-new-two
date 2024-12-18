

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