$(".add_product").click(function (e) {
    e.preventDefault();
    var this_form = $(this).parent();

    if (this_form.serialize() != "") {
        $.ajax({
            type: this_form.attr('method'),
            url: "/order/add/",
            data: this_form.serialize(),
            dataType: 'json',
            success: function (data) {
                $(".order_count").load(" .order_count > *");
                $(".total").load(" .total > *");
                $("#price_id_" + data.id).load(" #price_id_" + data.id + " > *");
                $("#count_id_" + data.id).html(data.count_product);
                if (data.error_count != "") {
                    alert(data.error_count)
                }
            },
            error: function (data) {
                alert("ajax error");
            }
        });
    } else {
        alert("Размер не выбран");
    }
});

$(".delete_product").click(function (e) {
    e.preventDefault();
    var this_form = $(this).parent();
    if (this_form.serialize() != "") {
        $.ajax({
            type: this_form.attr('method'),
            url: '/order/delete/',
            data: this_form.serialize(),
            dataType: 'json',
            success: function (data) {
                $(".order_count").load(" .order_count > *");
                $(".total").load(" .total > *");
                $("#price_id_" + data.id).load(" #price_id_" + data.id + " > *");
                $("#count_id_" + data.id).html(data.count_product);
                if (data.error_count != "") {
                    alert(data.error_count)
                }
            },
            error: function (data) {
                alert("ajax error");
            }
        });
    }
});