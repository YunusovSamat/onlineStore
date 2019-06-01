$(".add_product").click(function (event) {
    const add_button = $(this);
    change_count_product(event, add_button, '/order/add/');

    const count_product_block = add_button.siblings('[class="count_product"]');
    if (count_product_block.html() + 1 > 1) {
        add_button.siblings('[class="delete_product"]').css("visibility", "visible");
    }
});

$(".delete_product").click(function (e) {
    const del_button = $(this);
    change_count_product(event, del_button, '/order/delete/');

    const count_product_block = del_button.siblings('[class="count_product"]');
    if (count_product_block.html() - 1 === 1) {
        del_button.css("visibility", "hidden");
    }
});

function change_count_product(e, button, form_url) {
    e.preventDefault();

    const form = button.parent();
    const form_data = form.serialize();
    const count_product_block = button.siblings('[class="count_product"]')
    const error_count_block = button.siblings('[class="error_count"]');

    if (form_data.length) {
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

                    if (button.attr("class").indexOf("link_button") !== -1){
                        show_window_done();
                    }
                }
            },
            error: function (data) {
                alert("ajax error");
            },
        });
    } else {
        alert("Размер не выбран");
    }
}

function show_window_done() {
    const window_done = document.getElementById('window_done');
    const window_done_close = document.getElementById('window_done_close');

    window_done.style.display = 'block';

    window_done_close.onclick = function() {
        window_done.style.display = 'none';
    };

    window_done.onclick = function (e) {
        if (e.target === window_done) {
            window_done.style.display = 'none';
        }
    };
}

