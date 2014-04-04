$(document).ready(function() {

	$('.code').hide();
	
	$('#buttonCode').click(function(){
		if($(this).val() == 'Show code'){
			$(this).val('Hide code');
			$('.code').slideDown();
		}
		else{
			$(this).val('Show code');
			$('.code').slideUp();
		}

	});

	$('.side_menu').hide();
	$('#side_menu li').click(function(){
		$(this).children('ul').slideToggle();
	});
});