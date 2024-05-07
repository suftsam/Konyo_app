// Function to open the cart
function openMenu() {
    var menuContainer = document.querySelector('.menuContainer');
    menuContainer.style.display = 'block';
}

// Function to close the cart
function closeMenu() {
    var menuContainer = document.querySelector('.menuContainer');
    menuContainer.style.display = 'none';
}

// Function to toggle the cart (open/close)
function toggleMenu() {
    var menuContainer = document.querySelector('.menuContainer');
    if (menuContainer.style.display === 'block') {
        closeCart();
    } else {
        openMenu();
    }
}


// Function to open the resume
function openResume() {
    var menuContainer = document.querySelector('.resumeContainer');
    menuContainer.style.display = 'block';
}

// Function to close the resume
function closeResume() {
    var menuContainer = document.querySelector('.resumeContainer');
    menuContainer.style.display = 'none';
}

// Function to toggle the resume (open/close)
function toggleResume() {
    var menuContainer = document.querySelector('.resumeContainer');
    if (menuContainer.style.display === 'block') {
        closeResume();
    } else {
        openResume();
    }
}



// // Function to open the cart
// function openResume() {
//     var menuContainer = document.querySelector('.resumeContainer');
//     menuContainer.style.display = 'block';
// }

// // Function to close the cart
// function closeResume() {
//     var menuContainer = document.querySelector('.resumeContainer');
//     menuContainer.style.display = 'none';
// }

// // Function to toggle the cart (open/close)
// function toggleResume() {
//     var menuContainer = document.querySelector('.resumeContainer');
//     if (menuContainer.style.display === 'block') {
//         closeResume();
//     } else {
//         openResume();
//     }
// }


// // Function to open the email
// function openEmail() {
//     var emaiContainer = document.querySelector('.emailContainer');
//     emaiContainer.style = 'display: block; left: 0;';
// }

// // Function to close the email
// function closeEmail() {
//     var emailContainer = document.querySelector('.emailContainer');
//     emailContainer.style = 'display: none'; 
// }

// // Function to toggle the cart (open/close)
// function toggleEmail() {
//     var emailContainer = document.querySelector('.emailContainer');
//     if (emailContainer.style.display === 'block') {
//         closeEmail();
//     } else {
//         openEmail();
//     }
// }