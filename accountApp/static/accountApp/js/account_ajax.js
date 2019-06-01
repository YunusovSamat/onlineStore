$('#login_button').click(function (event) {
    const form = $(this).parent();

    account_send_post(event, $(this));
});

$('#signup_button').click(function (event) {

    account_send_post(event, $(this));
});

function account_send_post(e, button) {
    e.preventDefault();
    const form = button.parent();
    const array = form.serializeArray();
    var flag = true;

    array.forEach(function (elem) {
       if (Object.values(elem)[1].length <= 0) {
           flag = false;
           return false;
       }
    });

    if (flag) {
        $.ajax({
            type: form.attr('method'),
            url: form.attr('action'),
            data: form.serialize(),
            dataType: 'json',
            success: function (data) {
                if (button.attr("id") === "login_button") {
                    if (data.login_error.length) {
                        $('.login_error').html(data.login_error);
                    } else {
                        $('.login_error').html("");
                        $('.login_form').css('display', 'none');
                        $('.block_account').load(' .block_account > *');
                    }
                } else if (button.attr("id") === "signup_button") {
                    if (data.signup_errors.length) {
                        $('.signup_errors').html(data.signup_errors);
                    } else {
                        $('.signup_errors').html("");
                        $('.signup_form').css('display', 'none');
                        $('.block_account').load(' .block_account > *');
                    }
                }
            },
            error: function (data) {
                alert("ajax error");
            },
        });
    } else {
        if (button.attr("id") === "login_button") {
            $('.login_error').html("Все поля обзязательны для заполнения");
        } else if (button.attr("id") === "signup_button") {
            $('.signup_errors').html("Все поля обзязательны для заполнения");
        }
    }
}