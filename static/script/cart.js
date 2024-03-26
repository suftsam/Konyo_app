// Function to open the cart
function openCart() {
    var cartContainer = document.querySelector('.cartContainer');
    cartContainer.style.display = 'block';
}

// Function to close the cart
function closeCart() {
    var cartContainer = document.querySelector('.cartContainer');
    cartContainer.style.display = 'none';
}

// Function to toggle the cart (open/close)
function toggleCart() {
    var cartContainer = document.querySelector('.cartContainer');
    if (cartContainer.style.display === 'block') {
        closeCart();
    } else {
        openCart();
    }
}


    // Load existing items from localStorage on page load
    window.onload = function () {
        loadCartItems();
        updateAddToCartButtonState();
    };

    // Function to add items to the cart or remove if already in the cart
    function addToCart(title, imageUrl, price) {
        // Retrieve existing cart items from local storage
        var cartItems = getCartItems();

        // Check if the item is already in the cart
        var itemIndex = cartItems.findIndex(function (item) {
            return item.title === title;
        });

        if (itemIndex !== -1) {
            // If the item is already in the cart, remove it
            cartItems.splice(itemIndex, 1);
        } else {
            // If the item is not in the cart, add it
            var newItem = {
                title: title,
                imageUrl: imageUrl,
                price: price
            };
            cartItems.push(newItem);
        }

        // Save the updated cart items to local storage
        saveCartItems(cartItems);

        // Update the displayed cart
        updateCartDisplay();

        // Update the "Add to Cart" button text based on whether the item is in the cart
        updateAddToCartButton(title);
    }

    // Function to update the "Add to Cart" button text
    function updateAddToCartButton(title) {
        var addToCartButtons = document.querySelectorAll('.cart-button');
        var cartItems = getCartItems();
        addToCartButtons.forEach(function (button) {
            if (button.getAttribute('data-title') === title) {
                // Check if the item is in the cart and update the button text accordingly
                var isItemInCart = cartItems.some(function (item) {
                    return item.title === title;
                });

                if (isItemInCart) {
                    button.innerText = 'Remove from Cart';
                } else {
                    button.innerText = 'Add to Cart';
                }
            }
        });
    }

    // Function to remove items from the cart
    function removeCartItem(index) {
        // Remove the item from the cart list
        var cartItems = getCartItems();
        cartItems.splice(index, 1);
        saveCartItems(cartItems);

        // Update the displayed cart
        updateCartDisplay();
    }

    // Function to load cart items from localStorage
    function loadCartItems() {
        var cartItems = getCartItems();
        for (var i = 0; i < cartItems.length; i++) {
            displayCartItem(cartItems[i], i);
        }
    }

     // Function to update the cart display
     function updateCartDisplay() {
        // Retrieve cart items from localStorage
        var cartItems = getCartItems();

        // Clear existing items and display the updated cart
        var cartItemsContainer = document.getElementById("cartItems");
        cartItemsContainer.innerHTML = "";

        // Display each cart item
        for (var i = 0; i < cartItems.length; i++) {
            displayCartItem(cartItems[i], i);
        }

        // Update the cart description
        var cartDescription = document.querySelector('.cart-description span');
        cartDescription.textContent = `Items in Cart: ${cartItems.length}`;
    }

    // Function to display a cart item in the cart container
    function displayCartItem(cartItem, index) {
        var cartItemElement = document.createElement("div");
        cartItemElement.classList.add("cart-item");

        cartItemElement.innerHTML = `

        <div id="cartItems">
            <div class="image-container">
                <img src="${cartItem.imageUrl}" alt="${cartItem.title}" class="cart-item-image">
            </div>
            <div class="details">
                <div class="tittle"><span>Title:</span> ${cartItem.title}</div>
                <div class="price"><span>Price:</span> $${cartItem.price}</div>
                <a href="#" class="button remove" onclick="removeCartItem(${index})">remove</a>
            </div>
        </div>
        `;

        document.getElementById("cartItems").appendChild(cartItemElement);
    }

    // Function to retrieve cart items from localStorage
    function getCartItems() {
        var cartItemsJson = localStorage.getItem("cartItems");
        return cartItemsJson ? JSON.parse(cartItemsJson) : [];
    }

    // Function to save cart items to localStorage
    function saveCartItems(cartItems) {
        localStorage.setItem("cartItems", JSON.stringify(cartItems));
    }