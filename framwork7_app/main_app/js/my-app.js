// Initialize your app
var myApp = new Framework7({
    animateNavBackIcon:true,
    template7Pages: true,
    precompileTemplates: true
});

// Export selectors engine
var $$ = Dom7;

// Add main View
var mainView = myApp.addView('.view-main', {
    // Enable dynamic Navbar
    dynamicNavbar: true,
    // Enable Dom Cache so we can use all inline pages
    domCache: true
});

// Funcion to handle Cancel button on Login page
$$('#cancel-register').on('click', function () {
    // Clear field values
    $$('#register-flight_name').val('');
    $$('#register-flight_number').val('');
    $$('#register-departure_city').val('');
    $$('#register-arrival_city').val('');
    $$('#register-departure_time').val('');
    $$('#register-arrival_time').val('');
    $$('#register-departure_date').val('');
    $$('#register-arrival_date').val('');
});

// Function to handle Submit button on Register page
$$('#summit-newflight').on('click', function () {

    var flight_name = $$('#register-flight_name').val();
    var flight_number = $$('#register-flight_number').val();
    var departure_city = $$('#register-departure_city').val();
    var arrival_city = $$('#register-arrival_city').val();
    var departure_time = $$('#register-departure_time').val();
    var arrival_time = $$('#register-arrival_time').val();
    var departure_date = $$('#register-departure_date').val();
    var arrival_date = $$('#register-arrival_date').val();

    console.log('Submit clicked');
    console.log('flight_name: ' + flight_name);
    console.log('flight_number: ' + flight_number);
    console.log('departure_city: ' + departure_city);
    console.log('arrival_city: ' + arrival_city);
    console.log('departure_time: ' + departure_time);
    console.log('arrival_time: ' + arrival_time);
    console.log('departure_date: ' + departure_date);
    console.log('arrival_date: ' + arrival_date);

    if (!flight_name || !flight_number) {
        myApp.alert('Please fill in all Registration form fields');
        return;
    }

    // Methods to handle speciffic HTTP response codes
    var success201 = function(data, textStatus, jqXHR) {

        // We have received response and can hide activity indicator
        myApp.hideIndicator();

        console.log('Response body: '+data);

        // Will pass context with retrieved user name
        // to welcome page. Redirect to welcome page
        mainView.router.load({
            template: Template7.templates.welcomeTemplate,
            context: {
                name: flight_name
            }
        });
    };

    var notsuccess = function(data, textStatus, jqXHR) {
        // We have received response and can hide activity indicator
        myApp.hideIndicator();
        myApp.alert('Login was unsuccessful, please try again');
    };

    var query = 'http://127.0.0.1:8000/flights/';
    var postdata = {};
    postdata.flight_name = flight_name;
    postdata.flight_number = flight_number;
    postdata.departure_city = departure_city;
    postdata.arrival_city = arrival_city;
    postdata.departure_time = departure_time;
    postdata.arrival_time = arrival_time;
    postdata.departure_date = departure_date;
    postdata.arrival_date = arrival_date;

    myApp.showIndicator();

    $$.ajax({
        url: query,

        type: "POST",
        // if successful response received (http 2xx)
        contentType: "application/json",
        data: JSON.stringify(postdata),

        statusCode: {
            201: success201,
            400: notsuccess,
            500: notsuccess
        }
    });
});

//
//     postdata.flight_name = flight_name;
//     postdata.flight_number = flight_number;
//     postdata.departure_city = departure_city;
//     postdata.arrival_city = arrival_city;
//     postdata.departure_time = departure_time;
//     postdata.arrival_time = arrival_time;
//     postdata.departure_date = departure_date;
//     postdata.arrival_date = arrival_date;
//     myApp.showIndicator();
//     $$.ajax({
//         url: query,
//         headers: {},
//         type: "POST",
//         contentType: "application/json",
//         data: JSON.stringify(postdata),
//         statusCode: {
//             201: success201,
//             400: notsuccess,
//             500: notsuccess
//         }
//     });
// });


