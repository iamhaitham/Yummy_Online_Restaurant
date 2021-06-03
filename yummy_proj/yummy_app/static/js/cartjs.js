// Remove Items From Cart

// A $( document ).ready() block.
$(document).ready(function () {
	$("a.remove").click(function () {
		event.preventDefault();
		$(this).parent().parent().parent().hide(400);
	});

	// Just for testing, show all items
	$("a.btn.continue").click(function () {
		$("li.items").show(400);
	});
});
