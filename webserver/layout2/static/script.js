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
});