// Remove Items From Cart

// A $( document ).ready() block.
$(document).ready(function () {

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




