   // Get the select element
   const categoryFilter = document.getElementById('categoryFilter');
  
   // Get all the product cards
   const productCards = document.querySelectorAll('.col.text-center');
 
   // Add event listener to the select element
   categoryFilter.addEventListener('change', function () {
       const selectedCategory = categoryFilter.value; // Get the selected category value
 
       // Loop through all the product cards
       productCards.forEach(function (card) {
           const category = card.dataset.category; // Get the data-category value of the card
 
           // Show/hide the card based on the selected category
           if (selectedCategory === 'all' || selectedCategory === category) {
               card.style.display = 'block';
           } else {
               card.style.display = 'none';
           }
       });
   });