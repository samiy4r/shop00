let csrftoken = getCookie('csrftoken');
// The following function are copying from 
// https://docs.djangoproject.com/en/dev/ref/csrf/#ajax
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
              }
            }
          }
          return cookieValue;
        }
        
function add_to_cart(product_id) {
  // console.log(product_id)
  fetch("http://127.0.0.1:8000/cart/addtocart/", {
  method: "POST",
  body: JSON.stringify({
    productid: product_id,
  }),
  headers: { "X-CSRFToken": csrftoken }
})
.then((response)=> response.json())
.then((json) => document.querySelector('.count').innerHTML++);
}

function delete_form_cart(product_id) {
  fetch("http://127.0.0.1:8000/cart/deleteformcart/", {
    method: "POST",
    body: JSON.stringify({
      productid: product_id,
    }),
    headers: { "X-CSRFToken": csrftoken }
  })
  .then((response)=> response.json())
  .then((json) => {if (json.data == 'success') {location.reload()}});
}

function add_count(product_id){
  fetch("http://127.0.0.1:8000/cart/addcount/" , {
  method : "POST",
  body: JSON.stringify({
    productid : product_id,
  }),
  headers: {"X-CSRFToken": csrftoken }
  })
  .then((response)=> response.json())
  
  .then((json) => { if (json.data == "1" ) {location.reload()}} )
  
}

function minus_count(product_id){
  fetch("http://127.0.0.1:8000/cart/minuscount/" , {
  method : "POST",
  body: JSON.stringify({
    productid : product_id,
  }),
  headers: {"X-CSRFToken": csrftoken }
  })
  .then((response)=> response.json())
  
  .then((json) => { if (json.data == "1" ) {location.reload()}} )
  
}