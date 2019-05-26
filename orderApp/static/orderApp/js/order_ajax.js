$(".change_count_product").click(function (e) {
   e.preventDefault();

   const button = $(this);
   const form = button.parent();
   const form_data = form.serialize();
   var form_url = "";
   const count_product_block = button.siblings('[class="count_product"]');
   const error_count_block = button.siblings('[class="error_count"]');

   if (button.attr('class').indexOf('add_product') >= 0) {
       form_url = '/order/add/';
   } else if (button.attr('class').indexOf('delete_product') >= 0) {
       form_url = '/order/delete/';
   }
   if (form_data.length && form_url.length) {
       $.ajax({
           type: form.attr('method'),
           url: form_url,
           data: form_data,
           dataType: 'json',
           success: function (data) {
               $(".order_count").load(" .order_count > *");
               $(".total").load(" .total > *");
               $("#price_id_" + data.id).load(" #price_id_" + data.id + " > *");
               count_product_block.html(data.count_product);

               if (data.error_count.length) {
                   error_count_block.html(data.error_count);
               } else {
                   error_count_block.html("");
               }
           },
           error: function (data) {
               alert("ajax error");
           },
       });
   }else {
       alert("Размер не выбран");
   }
});

$(".add_product").click(function (e) {
    const count_product_block = $(this).siblings('[class="count_product"]');
    if (count_product_block.html() + 1 > 1) {
        $(this).siblings('[class="change_count_product delete_product"]').css("visibility", "visible");
    }
});

$(".delete_product").click(function (e) {
    const count_product_block = $(this).siblings('[class="count_product"]');
    if (count_product_block.html() - 1 === 1) {
        $(this).css("visibility", "hidden");
    }
});



