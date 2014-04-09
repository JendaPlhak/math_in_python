$(document).ready(function(){

	state = false;
	//var verticalScrollBar = $(window).scrollTop();
    /*$('#navbar ul li').click(function(){
        var index = [0,1];
        index.remove('1');
        document.write(index);
        
        $('.task ul:nth-child('+($(this).index()+1)+')').slideToggle();
    });*/
    
    $('#plhak, #kvapil').hover(
        function(){
            $(this).css('color','#227799');
        },
        function(){
            $(this).css('color','#225588');
        }
        );

   

    $('.code').hide();
	
	$('#buttonCode').click(function(){
		if($(this).html() == 'Show code'){

			$(this).html('Hide code');
			$('.code').slideDown('5000');
			$('html,body').animate({scrollTop: $(this).offset().top},'slow');

		}
		else{
			$(this).html('Show code');
			$('.code').slideUp();
		}
	});

	

	plhakHidden     = true;
	plhakBarHidden  = true;
    plhakTaskHidden = true;

    kvapilHidden    = true;
    kvapilBarHidden = true;
    kvapilTaskHidden= true;

    var tasksPlhak  = {
        "1" : ["collatzo", "archimed_spiral", "ulam_spiral", "gcd"],
        "2" : ["pascals_triangle"],
        "3" : ["turtle","fractals"],
        "4" : ["turtle","polygon", "effects", "hide_and_seek"],
        "5" : ["intersection", "triangulation","gift_wrapping"],
        "6" : ["chaos_game"]
    }
    var tasksKvapil = {
        "1" : ["collatzo", "gcd"],
        "2" : ["pascals_triangle"],
        "3" : ["turtle","fractals"],
        "4" : ["turtle","polygon", "effects", "hide_and_seek"],
        "5" : ["intersection", "triangulation","gift_wrapping"],
        "6" : ["chaos_game"]
    }

    $('.barTask').click(function(){
        //document.write( $(this).parent().attr('id').indexOf("Plhak"));
        var index      = $(this).index()+1;
        if ( $(this).parent().attr('id').indexOf("Plhak") >= 0 ){
            var name       = "plhak";
            var lengthTask = tasksPlhak[ index ].length;
            var tasks      = tasksPlhak;
        }else{
            var name       = "kvapil";
            var lengthTask = tasksKvapil[ index ].length;
            var tasks      = tasksKvapil;
        }
        $('#navTask').empty();
        for(var i=0; i<lengthTask; i++){
            var task = tasks[ index ][i];
            $('#navTask').append('\
                <div class="task">\
                    <a href="/'+name+'/'+task+'">'+task.replace(/_/g," ")+'</a>\
                </div>');
        }
    });

    $('.barTask').hover(
        function(){
            for( var i=0; i<=$(this).index()+1; i++ ){
                $('#navbar ul li div div div:nth-child('+i+')').css('background-color','#87a0bb');
            }
        },
        function(){
            for( var i=0; i<=$(this).index()+1; i++ ){
                $('#navbar ul li div div div:nth-child('+i+')').css('background-color','#d6d6d6');
            }
        }
    );


	$('#kvapil').click(function(){
        if( kvapilHidden && kvapilBarHidden && plhakHidden){
            $('#plhak').animate({left:'-=200px'},'slow');
            plhakHidden = false;
            $(this).animate({left:'-=200px'}, 'slow');
            $('#outerKvapil').animate({width:'+=200px'}, 'slow');
            $('#innerKvapil').animate({right:'+=200px'}, 'slow');
            kvapilHidden    = false;
            kvapilBarHidden = false;
        }else if( !kvapilHidden && !kvapilBarHidden && !plhakHidden){
            $('#plhak').animate({left:'+=200px'},'slow');
            plhakHidden = true;
            $(this).animate({left:'+=200px'}, 'slow');
            $('#outerKvapil').animate({width:'-=200px'}, 'slow');
            $('#innerKvapil').animate({right:'-=200px'}, 'slow');
            kvapilHidden    = true;
            kvapilBarHidden = true;
        }else if( !plhakHidden && kvapilHidden && kvapilBarHidden){
            $('#outerPlhak').animate({width:'-=200px'},'fast');
            $('#innerPlhak').animate({right:'-=200px'},'fast');
            plhakBarHidden = true;
             $(this).animate({left:'-=200px'}, 'slow');
            $('#outerKvapil').animate({width:'+=200px'}, 'slow');
            $('#innerKvapil').animate({right:'+=200px'}, 'slow');
            kvapilHidden    = false;
            kvapilBarHidden = false;
        }
    });

    $('#plhak').click(function(){
        if ( plhakHidden && plhakBarHidden && kvapilHidden ){
            $(this).animate({left:'-=200px'}, 'slow');
            $('#outerPlhak').animate({width:'+=200px'},'slow');
            $('#innerPlhak').animate({right:'+=200px'},'slow');
            plhakHidden     = false;
            plhakBarHidden  = false;
        }else if ( !plhakHidden && !plhakBarHidden && kvapilHidden){
            $(this).animate({left:'+=200px'}, 'slow');
            $('#outerPlhak').animate({width:'-=200px'},'slow');
            $('#innerPlhak').animate({right:'-=200px'},'slow');
            plhakHidden     = true;
            plhakBarHidden  = true;
        }else if( !plhakHidden && !kvapilHidden && !kvapilBarHidden){
            $('#kvapil').animate({left:'+=200px'},'slow');
            $('#outerKvapil').animate({width:'-=200px'}, 'slow');
            $('#innerKvapil').animate({right:'-=200px'}, 'slow');
            kvapilHidden    = true;
            kvapilBarHidden = true;
            $('#outerPlhak').animate({width:'+=200px'},'slow');
            $('#innerPlhak').animate({right:'+=200px'},'slow');
            plhakHidden     = false;
            plhakBarHidden  = false;
        }
    });

});