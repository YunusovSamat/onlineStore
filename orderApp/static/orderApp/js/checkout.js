$(".button_create_app").click(function () {
    $(".window_checkout_form").css("display", "block");
});

$(".button_save").click(function () {
    const data = $("#app_form").serializeArray();
    var i;
    var flag = true;
    var name = "";
    var address;

    for (i = 0; i < data.length-1; i++) {
        arr = Object.values(data[i]);
        if (arr[1].length <= 0) {
            flag = false;
        }
        if (arr[0] === "name" || arr[0] === "surname") {
            name += arr[1] + " ";
        }
        if (arr[0] === "address") {
            address = arr[1];
        }
    }
    if (flag) {
        $(".window_checkout_form").css("display", "none");
        $(".create_an_application").css("display", "none");
        $(".change_application_total").css("display", "block");
        if (name.length) {
            $(".insert_name").html(name);
        }
        $(".insert_address").html(address);
    } else {
        $(".block_errors").html("Заполните обязательные поля");
    }
});


const checkout_form = document.getElementsByClassName('window_checkout_form')[0];
const checkout_form_create = document.getElementsByClassName('button_create_app')[0];
const checkout_form_open = document.getElementsByClassName('button_change')[0];

checkout_form_create.onclick = function() {
    checkout_form.style.display = 'block';
};

checkout_form_open.onclick = function() {
    checkout_form.style.display = 'block';
};

checkout_form.onclick = function (e) {
    if (e.target === checkout_form) {
        checkout_form.style.display = 'none';
    }
};