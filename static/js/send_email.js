document.addEventListener('DOMContentLoaded', function () {
    var sendEmailForm = document.getElementById('sendEmailForm');
    sendEmailForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission behavior
        sendSelectedItemsToEmail();
    });
});

function sendSelectedItemsToEmail() {
    var userId = document.getElementById('user-id').value;

    // Retrieve the selected items from local storage
    var selectedDrinks = localStorage.getItem('selectedDrinks');
    var selectedServices = localStorage.getItem('selectedServices');
    var selectedComplementaryDrinks = localStorage.getItem('selectedComplementaryDrinks');
    var selectedBarber = localStorage.getItem('selectedBarber');
    var selectedSchedule = localStorage.getItem('selectedSchedule');
    var overallTotalPrice = localStorage.getItem('overallTotalPrice');

    // Get the email input from the user
    var customerEmail = document.getElementById('customerEmail').value;
    var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // Create a data object to send to the server
    var data = {
        selectedDrinks: selectedDrinks,
        selectedServices: selectedServices,
        selectedComplementaryDrinks: selectedComplementaryDrinks,
        selectedBarber: selectedBarber,
        selectedSchedule: selectedSchedule,
        overallTotalPrice: overallTotalPrice,
        email: customerEmail,
        user_id: userId, // Pass the user ID
        csrfmiddlewaretoken: csrfToken,
    };

    // Send the data to the server using fetch
    fetch('/send_email/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken, // Include CSRF token in the request headers
        },
        body: JSON.stringify(data),
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Network response was not ok.');
        }
    })
    .then(data => {
        // Handle the response from the server
        if (data.status === 'success') {
            // Display success message to the user
            console.log(data);
            alert('Selected items have been sent to your email.');
        } else {
            // Display error message to the user
            console.error('Error sending selected items:', data);
            alert('An error occurred while sending the selected items.');
        }
    })
    .catch(error => {
        console.error('Fetch error:', error);
        alert('An error occurred while sending the selected items.');
    });
}