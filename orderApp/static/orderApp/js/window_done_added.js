// var window_done = $("#window_done");
// var btn_done_open = $(".add_product");
// var btn_done_close = $("#window_done_close");
//
// // window_done.css("display", "block");
//
// btn_done_open.click(function () {
//    window_done.css("display", "block");
// });
//
// btn_done_close.click(function () {
//    window_done.css("display", "none");
// });
//
// window_done.click(function (e) {
//    if (e.target === window_done) {
//        window_done.css("display", "none");
//    }
// });

// btn_done_close.onclick = function () {
//     window_done.style.display = 'none';
// };
//
// window_done.onclick = function (e) {
//     if (e.target == window_done) {
//         window_size.style.display = 'none';
//     }
// };

var window_done = document.getElementById('window_done');
var btn_done_open = document.getElementsByClassName("add_product")[0];
var btn_done_close = document.getElementById("window_done_close");


btn_done_open.onclick = function () {
    window_done.style.display = 'block';
};

btn_done_close.onclick = function () {
    window_done.style.display = 'none';
};

window_done.onclick = function (e) {
    if (e.target === window_done) {
        window_done.style.display = 'none';
    }
};