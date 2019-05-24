// var form1 = $('#form1');
// form1.submit(function () {
//     $.ajax({
//         type: form1.attr('method'),
//         url: form1.attr('action'),
//         data: form1.serialize(),
//         dataType: 'json',
//         success: function (data) {
//             document.getElementsByClassName('order_count')[0].innerHTML = data.count;
//             if (data.error_count != null) {
//                 alert(data.error_count)
//             }
//         },
//         error: function(data) {
//             alert("error");
//         }
//     });
//     return false;
// });

$(".link_button").click(function (event) {
    event.preventDefault();
    var button = this;
    alert($(button).siblings("[name='count_id']").attr('value'));
    // console.log($(button).siblings('[name="count_id"]').attr('value'));

});