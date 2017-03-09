// Initialize your app
var myApp = new Framework7({
    animateNavBackIcon:true
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

    if (!flight_name || !flight_number) {
        myApp.alert('Please fill in all Registration form fields');
        return;
    }

    var query = 'localhost:8000/flights';
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
        headers: {},
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(postdata),
        statusCode: {
            201: success201,
            400: notsuccess,
            500: notsuccess
        }
    });
});


