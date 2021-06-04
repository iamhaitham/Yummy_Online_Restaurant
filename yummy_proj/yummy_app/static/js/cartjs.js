// Remove Items From Cart

// A $( document ).ready() block.
$(document).ready(function () {


    $(":input").bind('keyup change click', function (e) {
        m = $(this)
        id = $(this).parent().parent().parent().find('#itemid').text()
        id = id.split("#")[1]
        console.log(id)
        if (!$(this).data("previousValue") ||
            $(this).data("previousValue") != $(this).val()
        ) {
            $(this).data("previousValue", $(this).val());
            qty = parseInt($(this).val())
            price = $(this).parent().parent().parent().find(".myprice").html()
            price = parseInt(price) * qty
            price = $(this).parent().parent().parent().find('#itemprice').html('₪' + price)
            $.ajax({
                url: '/yummy/update/' + id,
                method: 'get',
                data: {
                    quantity: qty // will be accessible in $_POST['data1']
                },
                success: function (serverResponse) {
                    // Replace the html inside a div with the class "posts" with the server response
                    $(document).find('.subtotal').html(serverResponse)
                }
            });
        }

    });

    $(":input").each(function () {
        $(this).data("previousValue", $(this).val());
    });

    function attach_remove_handlers() {
        handleremove();
    }

    function handleremove() {
        $('a.remove').click(function () {
            event.preventDefault();
            $(this).parent().parent().parent().hide(400, function () {
                var pos = $(this).find('#itemid').text();
                console.log(pos);
                id = pos.split("#")[1]
                console.log(id);
                $.ajax({
                    url: '/yummy/removeFromCart/' + id,
                    method: 'get',
                    data: "",
                    success: function (serverResponse) {
                        // Replace the html inside a div with the class "posts" with the server response
                        $('.content').html(serverResponse)
                        attach_remove_handlers()
                    }
                });
            });
        });
    }

    handleremove();

    // Just for testing, show all items
    $("a.btn.continue").click(function () {
        $("li.items").show(400);
    });
});




