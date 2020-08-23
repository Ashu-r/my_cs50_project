const start = $('#start');
const pricebtn = $('#bgt .btn');
const pricecustom = $('#bgt input');
const allbgt = $('#bgt');

$(document).ready(function() {
	$(start).click(function() {
		$('.intro').removeClass('d-md-block d-md-none');
		// $('#intro').addClass('d-none');
		$('.intro').hide();
		$(this).hide();
		$('#bgt').removeClass('d-none');
		$('#bgt').show();
	});

	$(pricebtn).click(function() {
		// if ((this).hasClass(otherbgt));
		let clickedbtn = $(this).val();
		$('#bgt').hide();
		$(this).attr('name', 'price');
	});
	// $(pricecustom).keypress(function(event) {
	// 	// if ((this).hasClass(otherbgt));
	// 	let keycode = event.keyCode ? event.keyCode : event.which;
	// 	if (keycode == '13') {
	// 		let eninput = $(this).val();
	// 		$('#bgt').hide();
	// 		$(this).attr('name', 'price');
	// 	}
	// });
});
