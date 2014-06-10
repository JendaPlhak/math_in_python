$(document).ready(function(){

    // change color on hover definitely > css
    $('#plhak, #kvapil').hover(
        function(){
            $(this).css('color','#227799');
        },
        function(){
            $(this).css('color','#225588');
        }
        );

   
    // Hides the code section on the beginning > css
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

	
    // set logic about barTask at the begining
	plhakHidden     = true;
	plhakBarHidden  = true;
    plhakTaskHidden = true;

    kvapilHidden    = true;
    kvapilBarHidden = true;
    kvapilTaskHidden= true;

    var tasksPlhak  = {
        "1" : ["collatzo", "spirals", "gcd", "simple_graphics"],
        "2" : ["pascals_triangle", "combinatory_number","exponentiation","ludolphine_number"],
        "3" : ["Turtle","pictures","fractals"],
        "4" : ["simple_shapes","polygon", "effects", "hide_and_seek"],
        "5" : ["intersection", "triangulation","gift_wrapping"],
        "6" : ["chaos_game", "bifurcation","L-systems"],
        "7" : ["complex_fractals"],
        "8" : ["star", "barnsley_fern", "sierpinski_relatives"],
        "9" : ["linear_regression", "clustering"],
        "10" : ["number_maze", "no_left_turn", "sokoban"],
        "11" : ["maze_generator"]
    }
    var tasksKvapil = {
        "1" : ["collatzo", "basic_graphics", "ulam_spiral", "gcd"],
        "2" : ["pascals_triangle"],
        "3" : ["lib_turtle", "fractals", "basic_img"],
        "4" : ["turtle","polygon", "effects", "hide_and_seek"],
        "5" : ["intersection", "triangulation","gift_wrapping"],
        "6" : ["chaos_game"],
        "7" : ["complex_fractals"],
        "8" : ["affine_transformation"],
        "9" : ["mp_inverse","data_cluster"],
        "10": ["number_maze","mazelib"],
        "11": ["empty"]
    }

    $('.barTask').click(function(){
        //document.write( $(this).parent().attr('id').indexOf("Plhak"));
        var index = $(this).index()+1;
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
            $('#plhak').animate({left:'-=360px'},'slow');
            plhakHidden = false;
            $(this).animate({left:'-=360px'}, 'slow');
            $('#outerKvapil').animate({width:'+=360px'}, 'slow');
            $('#innerKvapil').animate({right:'+=360px'}, 'slow');
            kvapilHidden    = false;
            kvapilBarHidden = false;
        }else if( !kvapilHidden && !kvapilBarHidden && !plhakHidden){
            $('#plhak').animate({left:'+=360px'},'slow');
            plhakHidden = true;
            $(this).animate({left:'+=360px'}, 'slow');
            $('#outerKvapil').animate({width:'-=360px'}, 'slow');
            $('#innerKvapil').animate({right:'-=360px'}, 'slow');
            kvapilHidden    = true;
            kvapilBarHidden = true;
        }else if( !plhakHidden && kvapilHidden && kvapilBarHidden){
            $('#outerPlhak').animate({width:'-=360px'},'fast');
            $('#innerPlhak').animate({right:'-=360px'},'fast');
            plhakBarHidden = true;
             $(this).animate({left:'-=360px'}, 'slow');
            $('#outerKvapil').animate({width:'+=360px'}, 'slow');
            $('#innerKvapil').animate({right:'+=360px'}, 'slow');
            kvapilHidden    = false;
            kvapilBarHidden = false;
        }
    });

    $('#plhak').click(function(){
        if ( plhakHidden && plhakBarHidden && kvapilHidden ){
            $(this).animate({left:'-=360px'}, 'slow');
            $('#outerPlhak').animate({width:'+=360px'},'slow');
            $('#innerPlhak').animate({right:'+=360px'},'slow');
            plhakHidden     = false;
            plhakBarHidden  = false;
        }else if ( !plhakHidden && !plhakBarHidden && kvapilHidden){
            $(this).animate({left:'+=360px'}, 'slow');
            $('#outerPlhak').animate({width:'-=360px'},'slow');
            $('#innerPlhak').animate({right:'-=360px'},'slow');
            plhakHidden     = true;
            plhakBarHidden  = true;
        }else if( !plhakHidden && !kvapilHidden && !kvapilBarHidden){
            $('#kvapil').animate({left:'+=360px'},'slow');
            $('#outerKvapil').animate({width:'-=360px'}, 'slow');
            $('#innerKvapil').animate({right:'-=360px'}, 'slow');
            kvapilHidden    = true;
            kvapilBarHidden = true;
            $('#outerPlhak').animate({width:'+=360px'},'slow');
            $('#innerPlhak').animate({right:'+=360px'},'slow');
            plhakHidden     = false;
            plhakBarHidden  = false;
        }
    });

});